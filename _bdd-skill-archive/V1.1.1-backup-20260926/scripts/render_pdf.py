#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
render_pdf.py — BDD Customer Intelligence Skill V1.1.1 渲染层

职责：Markdown → HTML → PDF（业务员版三页）
============================================================

【渲染层隔离要求 — 硬要求，不可绕过】
  本脚本**只做格式转换**：
    · 不新增结论
    · 不推断缺失字段
    · 不改写 / 润色任何文字
    · 不重新计算任何等级或颜色
    · 不补全 Unknown
  颜色映射为**查表**（映射表来源：references/output-visual-rules.md），
  表内无匹配时输出中性色，**不得猜测**。
  Markdown 为权威版本；两者冲突时以 Markdown 为准。

【V1.1.1 Presentation Patch】
  仅改展示：13 个 Internal Key 不变，新增 Display Label 别名表（仅用于还原内部标识）；
  主卡按四组 WHO / WHY / WHERE·WHO / ACTION 呈现；
  `Sales Conclusion` 渲染为第一页结论卡；`Current Treatment` 状态徽标原样显示。
  **本层不参与任何判断。**

  渲染前必须通过**主卡 13 字段完整性校验**；缺任一字段 → 报错退出，不生成 PDF。

用法：
  python render_pdf.py <input.md> [--out <output.pdf>] [--html <output.html>] [--single]
    --single   输出完整单页版（不分页），用于内部复核

依赖：Google Chrome / Microsoft Edge（headless）
"""

import argparse
import html as html_mod
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# ---------------------------------------------------------------- 主卡 13 字段
# 来源：assets/output-card-template.md（V1.1 / V1.1.1）
# **Internal Key，保持不变。Display Label 见 FIELD_ALIASES。**
REQUIRED_FIELDS = [
    "Company",
    "Country",
    "What They Do",
    "Customer Type",
    "Industry Match",
    "Current Wastewater Treatment / Technology",
    "BDD Opportunity",
    "Demand Status",
    "Priority Site",
    "Who to Contact",
    "What Is Missing",
    "Next Action",
    "Sales Conclusion",
]

# --------------------------------------------- V1.1.1 Display Label → Internal Key
# 仅用于把主卡显示标签还原为内部标识。Internal Key 为唯一权威标识。
FIELD_ALIASES = {
    "公司 Company": "Company",
    "国家 Country": "Country",
    "主营业务 Business": "What They Do",
    "客户类型 Customer Type": "Customer Type",
    "行业匹配 Industry Match": "Industry Match",
    "现有废水处理 Current Treatment": "Current Wastewater Treatment / Technology",
    "BDD机会 BDD Opportunity": "BDD Opportunity",
    "需求状态 Demand Status": "Demand Status",
    "优先厂区 Priority Site": "Priority Site",
    "关键联系人 Contact": "Who to Contact",
    "待确认信息 Missing Info": "What Is Missing",
    "下一步 Next Action": "Next Action",
    "开发建议 Sales Conclusion": "Sales Conclusion",
}

# 结论卡标记（marker 原文属该字段显示标签，不改写）
CONCLUSION_MARK = "开发建议 Sales Conclusion"

# 四组标题识别（版式识别，非内容规则）
GROUP_TITLE_RE = re.compile(r"^(WHO|WHY|WHERE\s*/\s*WHO|ACTION)\s*·")

# --------------------------------------- Current Treatment 四态（查表，不推断）
# 来源：references/output-visual-rules.md 第二部分第三节
# 状态文字由 Markdown 给出；此处仅登记合法取值，缺失时**不补全**。
CURRENT_TREATMENT_STATES = ("Confirmed", "Partial", "Planned", "Unknown")

# ------------------------------------------------- 颜色语义映射表（查表，不推断）
# 来源：references/output-visual-rules.md
COLOR_TABLE = {
    "🟢": "ok",      # Confirmed / Positive / High relevance
    "🟡": "warn",    # Potential / Needs validation
    "🔴": "bad",     # Risk / Negative / Conflict
    "⚪": "unk",     # Unknown
    "🔵": "info",    # Neutral facts
}

COLOR_LEGEND = (
    ("ok", "🟢 已确认 / 正面 / 高相关"),
    ("warn", "🟡 待验证 / 潜力"),
    ("bad", "🔴 风险 / 负面 / 冲突"),
    ("unk", "⚪ 未知"),
    ("info", "🔵 中性事实"),
)

# ---------------------------------------------------------------- Markdown 子集解析


def esc(t: str) -> str:
    return html_mod.escape(t, quote=False)


def normalize_field(label: str) -> str:
    """Display Label → Internal Key。映射失败返回原文（兼容 V1.1 旧格式）。"""
    t = re.sub(r"\*\*", "", label).strip()
    return FIELD_ALIASES.get(t, t)


def colorize(text: str) -> str:
    """把五色 emoji 替换为色块 span。仅查表，不推断。"""
    out = esc(text)
    for emoji, cls in COLOR_TABLE.items():
        if emoji in out:
            out = out.replace(emoji, f'<span class="dot {cls}"></span>')
    return out


def inline(text: str) -> str:
    """行内元素：颜色 → 显式换行 → 粗体 → 行内代码 → 链接。顺序不可颠倒。"""
    t = colorize(text)
    # V1.1.1：Markdown 中显式书写的 `<br>` / `<br/>` 生效为换行（纯格式转换）
    t = t.replace("&lt;br&gt;", "<br/>").replace("&lt;br/&gt;", "<br/>")
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', t)
    return t


CELL_PIPE_PROT = "\x00P\x00"


def split_row(line: str):
    """拆分表格行。

    V1.1.1：先保护转义竖线 `\\|`，避免 `+|`（复合机会类型分隔符）被误拆成两列 ——
    这是纯排版修复，不改变任何单元格文本。
    """
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    s = s.replace("\\|", CELL_PIPE_PROT)
    return [c.strip().replace(CELL_PIPE_PROT, "|") for c in s.split("|")]


def is_table_sep(line: str) -> bool:
    s = line.strip()
    if not s.startswith("|"):
        return False
    return bool(re.fullmatch(r"\|[\s:\-|]+\|", s))


def md_to_html_body(lines):
    """返回 (html_blocks, page_breaks) —— page_breaks 为需要强制分页的块索引集合。"""
    out = []
    i = 0
    n = len(lines)
    page_break_before = set()
    block_idx = 0

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # 分页指令（版式规则，非内容规则）
        if stripped == "<!-- PAGEBREAK -->":
            page_break_before.add(block_idx)
            i += 1
            continue

        if not stripped:
            i += 1
            continue

        # 分隔线
        if re.fullmatch(r"-{3,}|\*{3,}", stripped):
            out.append('<hr class="sep"/>')
            block_idx += 1
            i += 1
            continue

        # 表格
        if stripped.startswith("|") and i + 1 < n and is_table_sep(lines[i + 1]):
            header = split_row(stripped)
            body_rows = []
            j = i + 2
            while j < n and lines[j].strip().startswith("|"):
                body_rows.append(split_row(lines[j]))
                j += 1
            t = ['<table><thead><tr>']
            t += [f"<th>{inline(c)}</th>" for c in header]
            t.append("</tr></thead><tbody>")
            for r in body_rows:
                t.append("<tr>")
                for c in r:
                    t.append(f"<td>{inline(c)}</td>")
                t.append("</tr>")
            t.append("</tbody></table>")
            out.append("".join(t))
            block_idx += 1
            i = j
            continue

        # details / summary
        if stripped.startswith("<details>"):
            out.append('<div class="fold">')
            block_idx += 1
            i += 1
            continue
        if stripped.startswith("</details>"):
            out.append("</div>")
            block_idx += 1
            i += 1
            continue
        if stripped.startswith("<summary>"):
            txt = re.sub(r"</?summary>", "", stripped)
            out.append(f'<div class="fold-title">{inline(txt)}</div>')
            block_idx += 1
            i += 1
            continue

        # 标题
        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            lvl = len(m.group(1))
            txt = m.group(2)
            # V1.1.1：四组标题加样式类（识别 WHO / WHY / WHERE·WHO / ACTION）
            cls = ' class="group-title"' if GROUP_TITLE_RE.match(txt) else ""
            out.append(f"<h{lvl}{cls}>{inline(txt)}</h{lvl}>")
            block_idx += 1
            i += 1
            continue

        # 引用（V1.1.1：含结论卡标记的引用块 → 结论卡样式）
        if stripped.startswith(">"):
            buf = []
            is_conclusion = False
            while i < n:
                cur = lines[i].strip()
                if cur.startswith(">"):
                    raw = cur.lstrip(">").strip()
                    if raw:
                        buf.append(raw)
                        if CONCLUSION_MARK in raw:
                            is_conclusion = True
                    i += 1
                elif (not cur) and i + 1 < n and lines[i + 1].strip().startswith(">"):
                    i += 1  # 空行分隔的同一引用块（结论卡可能分行书写）
                else:
                    break
            cls = ' class="conclusion"' if is_conclusion else ""
            out.append(f"<blockquote{cls}>"
                       + "<br/>".join(inline(b) for b in buf) + "</blockquote>")
            block_idx += 1
            continue

        # 代码块
        if stripped.startswith("```"):
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            out.append("<pre>" + esc("\n".join(buf)) + "</pre>")
            block_idx += 1
            continue

        # 列表
        if re.match(r"^\s*([-*]|\d+\.)\s+", line):
            ordered = bool(re.match(r"^\s*\d+\.\s+", line))
            tag = "ol" if ordered else "ul"
            items = []
            while i < n and re.match(r"^\s*([-*]|\d+\.)\s+", lines[i]):
                txt = re.sub(r"^\s*([-*]|\d+\.)\s+", "", lines[i])
                items.append(f"<li>{inline(txt)}</li>")
                i += 1
            out.append(f"<{tag}>" + "".join(items) + f"</{tag}>")
            block_idx += 1
            continue

        # 段落（连续非空行合并）
        buf = []
        while i < n:
            s = lines[i].strip()
            if (not s) or s.startswith("#") or s.startswith("|") or s.startswith(">") \
               or s.startswith("```") or s.startswith("<details>") or s.startswith("</details>") \
               or s.startswith("<summary>") or re.fullmatch(r"-{3,}", s) \
               or re.match(r"^\s*([-*]|\d+\.)\s+", lines[i]) \
               or s == "<!-- PAGEBREAK -->":
                break
            buf.append(lines[i].strip())
            i += 1
        if buf:
            out.append("<p>" + "<br/>".join(inline(b) for b in buf) + "</p>")
            block_idx += 1

    return out, page_break_before


# ---------------------------------------------------------------- 校验


def extract_main_card_fields(md_text: str):
    """提取主卡字段，返回 **Internal Key** 列表。

    V1.1.1：主卡按 WHO / WHY / WHERE·WHO / ACTION **四组分表**，
    因此需遍历**全部**以「字段 / Field」为表头的表格并累加（不再遇首个即停）。
    第一列为 Display Label 时，经 `normalize_field` 还原为 Internal Key。
    `Sales Conclusion` 为独立结论卡（引用块），单独识别后计入。
    """
    lines = md_text.splitlines()
    fields = []
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("|") and i + 1 < len(lines) and is_table_sep(lines[i + 1]):
            header = [h.strip() for h in split_row(s)]
            if header and header[0] in ("字段", "Field"):
                j = i + 2
                while j < len(lines) and lines[j].strip().startswith("|"):
                    row = split_row(lines[j])
                    if row:
                        name = normalize_field(row[0])
                        if name and name not in fields:
                            fields.append(name)
                    j += 1
                i = j
                continue
        i += 1

    # 结论卡（V1.1.1）：Sales Conclusion 已移出主卡表格
    if CONCLUSION_MARK in md_text and "Sales Conclusion" not in fields:
        fields.append("Sales Conclusion")
    return fields


def validate(md_text: str):
    """主卡 13 字段完整性校验。返回 (ok, missing, found)。"""
    found = extract_main_card_fields(md_text)
    missing = [f for f in REQUIRED_FIELDS if f not in found]
    return (len(missing) == 0), missing, found


# ---------------------------------------------------------------- 三页切分


def paged_split(blocks):
    """按业务员版三页切分（纯版式操作，不改内容）。

    Page 1  客户快照 —— 主卡 + 三个固定小块
    Page 2  为什么是这个客户 —— 判读说明段
    Page 3  关键证据 —— 附录 A（按 Decision Impact 排序，High 优先）

    识别依据为**文本标记**（若为 h2 或加粗段落均可）：
      进入 Page 2：出现「判定依据」/「Demand Status 明细」/「风险」
      进入 Page 3：出现「附录 A」/ details 折叠块
    """
    page1, page2, page3 = [], [], []
    mode = 1
    for b in blocks:
        plain = re.sub(r"<[^>]+>", "", b)
        if mode == 1 and ("判定依据" in plain or "Demand Status 明细" in plain):
            mode = 2
        if mode in (1, 2) and ("附录 A" in plain or "fold-title" in b):
            mode = 3
        if mode == 1:
            page1.append(b)
        elif mode == 2:
            page2.append(b)
        else:
            page3.append(b)
    return [page1, page2, page3]


def sort_evidence_table(blocks):
    """附录 A 表格按 Decision Impact 排序（High 优先）。仅重排，不删改内容。"""
    out = []
    for b in blocks:
        if not b.startswith("<table>"):
            out.append(b)
            continue
        rows = re.findall(r"<tr>(.*?)</tr>", b, re.S)
        if not rows:
            out.append(b)
            continue
        head = rows[0]
        body = rows[1:]
        if "Decision Impact" not in head:
            out.append(b)
            continue

        def rank(r):
            low = r.lower()
            for k, v in ((">high<", 0), (">medium<", 1), (">low<", 2)):
                if k in low:
                    return v
            return 3

        out.append("<table><thead>" + head + "</thead><tbody>"
                   + "".join(sorted(body, key=rank)) + "</tbody></table>")
    return out


# ---------------------------------------------------------------- HTML 组装

CSS = """
@page { size: A4; margin: 12mm 11mm; }
* { box-sizing: border-box; }
body {
  font-family: "Microsoft YaHei", "PingFang SC", "Helvetica Neue", Arial, sans-serif;
  color: #1c1f23; background: #ffffff; font-size: 10.5pt; line-height: 1.55;
  margin: 0; padding: 0;
}
.page { page-break-after: always; }
.page:last-child { page-break-after: auto; }
.page-head {
  border-bottom: 2px solid #1c1f23; padding-bottom: 3px; margin: 0 0 8px 0;
  font-size: 9pt; letter-spacing: .12em; text-transform: uppercase; color: #5a626b;
  display: flex; justify-content: space-between;
}
h1 { font-size: 17pt; margin: 2px 0 4px 0; letter-spacing: -.01em; }
h2 { font-size: 12pt; margin: 12px 0 6px 0; padding-left: 7px; border-left: 3px solid #1c1f23; }
h3 { font-size: 10.8pt; margin: 10px 0 4px 0; color: #33383e; }
p { margin: 4px 0; }
table { border-collapse: collapse; width: 100%; margin: 6px 0; font-size: 9.6pt; }
th, td { border: 1px solid #d6dae0; padding: 4px 6px; text-align: left; vertical-align: top; }
th { background: #f2f4f6; font-weight: 600; }
tbody tr:nth-child(even) td { background: #fafbfc; }
td:first-child { white-space: nowrap; }
code { background: #f2f4f6; padding: 0 3px; border-radius: 2px;
       font-family: Consolas, "Courier New", monospace; font-size: 9pt; }
blockquote { margin: 6px 0; padding: 5px 9px; background: #f7f8fa;
             border-left: 3px solid #b9c0c8; color: #3d444c; font-size: 9.6pt; }
pre { background: #f7f8fa; border: 1px solid #e3e7eb; padding: 7px 9px;
      font-family: Consolas, monospace; font-size: 8.8pt; white-space: pre-wrap; }
ul, ol { margin: 4px 0 4px 18px; padding: 0; }
li { margin: 2px 0; }
hr.sep { border: 0; border-top: 1px solid #e3e7eb; margin: 9px 0; }
.fold { margin: 6px 0; }
.fold-title { font-weight: 600; font-size: 9.8pt; margin: 8px 0 3px 0; }

/* ---- V1.1.1 展示层：四组标题与结论卡（纯样式，不改内容） ---- */
h3.group-title {
  font-size: 8.8pt; letter-spacing: .16em; text-transform: uppercase;
  color: #454c54; margin: 9px 0 3px 0; padding-bottom: 2px;
  border-left: 0; border-bottom: 1px solid #d6dae0;
}
h3.group-title:first-of-type { margin-top: 5px; }
blockquote.conclusion {
  margin: 12px 0 4px 0; padding: 9px 13px 10px 13px;
  background: #f6f8fa; border: 1.4px solid #2a2f35; border-left: 6px solid #2a2f35;
  color: #1c1f23; font-size: 10.6pt; line-height: 1.5;
}
blockquote.conclusion strong:first-child {
  display: block; font-size: 8.4pt; letter-spacing: .16em;
  text-transform: uppercase; color: #5a626b; margin-bottom: 4px;
}
blockquote.conclusion strong:nth-of-type(2) {
  font-size: 12pt; letter-spacing: .01em;
}
.dot { display: inline-block; width: 8px; height: 8px; border-radius: 50%;
       margin-right: 3px; vertical-align: baseline; }
.dot.ok   { background: #1f9d55; }
.dot.warn { background: #d99a04; }
.dot.bad  { background: #cf2e2e; }
.dot.unk  { background: #9aa1a9; }
.dot.info { background: #2f6fb5; }
.legend { margin-top: 10px; font-size: 8.6pt; color: #5a626b;
          border-top: 1px solid #e3e7eb; padding-top: 5px; }
.legend span.item { margin-right: 12px; }
.pagenum { font-size: 8.6pt; color: #8a9099; }
"""


def build_html(md_text: str, single: bool) -> str:
    lines = md_text.splitlines()
    blocks, _ = md_to_html_body(lines)
    blocks = sort_evidence_table(blocks)

    # 抽取标题（第一个 h1）
    title = ""
    for b in blocks:
        if b.startswith("<h1>"):
            title = b
            break

    if single:
        pages = [blocks]
        page_names = ["Full"]
    else:
        groups = paged_split(blocks)
        pages = groups
        page_names = ["Customer Snapshot", "Why This Customer", "Key Evidence"]

    html_parts = [
        "<!DOCTYPE html><html lang='zh-CN'><head><meta charset='utf-8'>",
        f"<title>{esc(title)}</title><style>{CSS}</style></head><body>",
    ]

    for idx, page in enumerate(pages):
        name = page_names[idx]
        html_parts.append("<section class='page'>")
        html_parts.append(
            f"<div class='page-head'><span>{esc(name)}</span>"
            f"<span class='pagenum'>{idx + 1} / {len(pages)}</span></div>"
        )
        if idx == 0 and title:
            html_parts.append(title)
            body = [b for b in page if b != title]
        else:
            body = page
        html_parts.extend(body)
        if idx == len(pages) - 1:
            legend = "".join(
                f"<span class='item'><span class='dot {c}'></span>{esc(t)}</span>"
                for c, t in COLOR_LEGEND
            )
            html_parts.append(f"<div class='legend'>{legend}</div>")
        html_parts.append("</section>")

    html_parts.append("</body></html>")
    return "\n".join(html_parts)


# ---------------------------------------------------------------- Chrome 打印


def find_browser():
    cands = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "/usr/bin/google-chrome",
        "/usr/bin/chromium",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    ]
    for c in cands:
        if os.path.isfile(c):
            return c
    for name in ("google-chrome", "chromium", "chromium-browser", "chrome"):
        p = shutil.which(name)
        if p:
            return p
    return None


def html_to_pdf(html_path: Path, pdf_path: Path) -> None:
    browser = find_browser()
    if not browser:
        raise RuntimeError(
            "未找到 Chrome / Edge。请安装 Google Chrome 或 Microsoft Edge 后重试。"
        )
    tmp_profile = tempfile.mkdtemp(prefix="bdd_pdf_")
    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        f"--user-data-dir={tmp_profile}",
        "--no-pdf-header-footer",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={str(pdf_path)}",
        html_path.as_uri(),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    if not pdf_path.exists() or pdf_path.stat().st_size == 0:
        raise RuntimeError(
            "PDF 生成失败。\n"
            f"exit={proc.returncode}\nstdout={proc.stdout[-1500:]}\nstderr={proc.stderr[-1500:]}"
        )
    shutil.rmtree(tmp_profile, ignore_errors=True)


# ---------------------------------------------------------------- main


def main():
    ap = argparse.ArgumentParser(description="BDD Customer Intelligence — MD → HTML → PDF")
    ap.add_argument("input", help="输入 Markdown 文件")
    ap.add_argument("--out", help="输出 PDF 路径（默认与输入同名）")
    ap.add_argument("--html", help="同时保留 HTML 的路径")
    ap.add_argument("--single", action="store_true", help="输出完整单页版（内部复核用）")
    args = ap.parse_args()

    md_path = Path(args.input).resolve()
    if not md_path.is_file():
        print(f"[FAIL] 输入文件不存在：{md_path}")
        return 2

    md_text = md_path.read_text(encoding="utf-8")

    # ---- 校验（硬门禁：缺字段不出 PDF）
    ok, missing, found = validate(md_text)
    print("=" * 66)
    print("BDD Customer Intelligence · 渲染前校验")
    print("=" * 66)
    print(f"输入文件           : {md_path}")
    print(f"主卡字段数         : {len(found)} / {len(REQUIRED_FIELDS)}")
    if not ok:
        print(f"CHECK_main_card    : FAIL — 缺 {len(missing)} 项：{', '.join(missing)}")
        print("\n[FAIL] 主卡字段不完整，按渲染层隔离要求**不生成 PDF**。")
        print("       请先补齐 Markdown 主卡后再渲染。")
        return 3
    print("CHECK_main_card    : PASS")
    print("CHECK_evidence_col : "
          + ("PASS" if "Decision Impact" in md_text else "WARN — 附录缺 Decision Impact 列"))

    # ---- HTML
    html_doc = build_html(md_text, args.single)
    if args.html:
        html_path = Path(args.html).resolve()
    else:
        html_path = Path(tempfile.gettempdir()) / (md_path.stem + ".render.html")
    html_path.write_text(html_doc, encoding="utf-8")
    print(f"CHECK_html         : PASS — {html_path}")

    # ---- PDF
    pdf_path = Path(args.out).resolve() if args.out else md_path.with_suffix(".pdf")
    try:
        html_to_pdf(html_path, pdf_path)
    except Exception as e:  # noqa: BLE001
        print(f"CHECK_pdf          : FAIL — {e}")
        print("\n[FAIL] PDF 生成失败。**Markdown 保留不变**，请检查浏览器可用性后重试。")
        return 4

    size_kb = pdf_path.stat().st_size / 1024
    print(f"CHECK_pdf          : PASS — {pdf_path} ({size_kb:.1f} KB)")
    print("=" * 66)
    print("渲染层声明：本次仅做格式转换，未新增 / 推断 / 改写任何结论；")
    print("           颜色由映射表机械查得；Markdown 为权威版本。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
