#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
render_pdf.py — BDD Customer Intelligence Skill V1.1.2 渲染层

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
  `Sales Conclusion` 渲染为第一页结论卡。

【V1.1.2 UI Refinement Patch】
  仅改 Presentation / PDF Rendering / Output Visual Layer：
    · 字段列浅灰蓝底 + 固定 20% 宽 + 垂直居中；短状态渲染为 Badge（不整行染色）
    · Section Header 带编号（01~04）
    · 长字段 `⟪P2⟫` 拆分：Page 1 只显示摘要，完整内容进 Page 2
    · 结论卡强化（中文大号 + 英文副标题 + 左侧色条）
    · Page 3 由 7 列表格改为 **Evidence Card**（只展示 High / Medium 前 6~10 条）
  **本层不参与任何判断。** 完整 Evidence 仍保留在 Markdown，不删除。

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
GROUP_TITLE_RE = re.compile(
    r"^(?:\d{2}\s+)?(WHO|WHY|WHERE\s*/\s*WHO|ACTION)\s*[·｜]")

# --------------------------------------- Current Treatment 四态（查表，不推断）
# 来源：references/output-visual-rules.md 第二部分第三节 / 第三部分第三节
CURRENT_TREATMENT_STATES = ("Confirmed", "Partial", "Planned", "Unknown")

# ------------------------------------------ V1.1.2 Badge 映射（查表，不推断）
# 来源：references/output-visual-rules.md 第三部分第二节
# 仅**精确匹配**短状态词才渲染 Badge；未命中一律原样输出纯文本。
BADGE_WORDS = {
    # 绿 · 正面
    "High": "badge-ok",
    "Target": "badge-ok",
    "Confirmed": "badge-ok",
    "Strong Signal": "badge-ok",
    "建议开发": "badge-ok",
    "建议重点开发": "badge-ok",
    # 黄 · 待验证
    "Medium": "badge-warn",
    "Potential": "badge-warn",
    "Partial": "badge-warn",
    "建议先验证": "badge-warn",
    # 红 · 风险 / 负面（**只用于风险、冲突、负面**）
    "Risk": "badge-bad",
    "Conflict": "badge-bad",
    "Low": "badge-bad",
    "Weak": "badge-bad",
    "Outside": "badge-bad",
    "暂不优先": "badge-bad",
    # 灰 · 未知
    "Unknown": "badge-unk",
    "信息不足": "badge-unk",
    # 蓝 · 中性事实
    "Adjacent": "badge-info",
    "Planned": "badge-info",
    "Neutral Facts": "badge-info",
}

# Current Treatment 四态中文显示（状态仍由 Evidence 支撑，本表只加中文）
CT_CN_STATES = (
    ("🟢 已确认 Confirmed", "badge-ok"),
    ("🟡 部分确认 Partial", "badge-warn"),
    ("🔵 规划中 Planned", "badge-info"),
    ("⚪ 未知 Unknown", "badge-unk"),
)

# 五色点 → Badge 类（用于 `{色点} {状态词}` 形式）
DOT_TO_BADGE = {
    "🟢": "badge-ok",
    "🟡": "badge-warn",
    "🔴": "badge-bad",
    "⚪": "badge-unk",
    "🔵": "badge-info",
}

# Sales Conclusion 英文副标题（展示层映射，不改变判断结果）
CONCL_EN = {
    "建议重点开发": "Recommended — Priority Development",
    "建议开发": "Recommended to Develop",
    "建议先验证": "Verify Before Pursuing",
    "暂不优先": "Low Priority",
    "信息不足，暂缓判断": "Insufficient Information",
}

# 中文结论 → 卡片语义类
CONCL_CLS = {
    "建议重点开发": "ok",
    "建议开发": "ok",
    "建议先验证": "warn",
    "暂不优先": "bad",
    "信息不足，暂缓判断": "unk",
}

# Page 1 → Page 2 的版式标记（不是判断标记）
P2_MARK = "⟪P2⟫"

# 长字段（需要 `⟪P2⟫` 拆分压缩的字段）—— Internal Key
LONG_FIELDS = [
    "Current Wastewater Treatment / Technology",
    "Priority Site",
    "Who to Contact",
    "What Is Missing",
]

# Evidence Card 展示上限（High 优先，要求 6 ~ 10 条；取 6 控制 Page 3 在一页内）
EVIDENCE_CARD_LIMIT = 6

# Internal Key → Display Label（Page 2「字段完整内容」用）
KEY_TO_LABEL = {v: k for k, v in FIELD_ALIASES.items()}

# Display Label → (中文, 英文) 展示拆分（V1.1.2 字段名分字重；文字不改）
LABEL_SPLIT = {
    "公司 Company": ("公司", "Company"),
    "国家 Country": ("国家", "Country"),
    "主营业务 Business": ("主营业务", "Business"),
    "客户类型 Customer Type": ("客户类型", "Customer Type"),
    "行业匹配 Industry Match": ("行业匹配", "Industry Match"),
    "BDD机会 BDD Opportunity": ("BDD机会", "BDD Opportunity"),
    "需求状态 Demand Status": ("需求状态", "Demand Status"),
    "现有废水处理 Current Treatment": ("现有废水处理", "Current Treatment"),
    "优先厂区 Priority Site": ("优先厂区", "Priority Site"),
    "关键联系人 Contact": ("关键联系人", "Contact"),
    "待确认信息 Missing Info": ("待确认信息", "Missing Info"),
    "下一步 Next Action": ("下一步", "Next Action"),
    "开发建议 Sales Conclusion": ("开发建议", "Sales Conclusion"),
}

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


# ------------------------------------------------------------- V1.1.2 Badge

def _badge_hold(badges, cls, txt, tail=""):
    badges.append((cls, txt))
    return f"\x01{len(badges) - 1}\x01" + tail


def extract_badges(value: str, badges):
    """把单元格开头的短状态渲染为占位符。**只查表，未命中即原样返回。**

    匹配优先级：
      ① Current Treatment 四态中文（`🟢 已确认 Confirmed`）
      ② `{色点} {状态词}`（`🟢 High · …`）
      ③ 整串即状态词（`Potential`）
    """
    v = value.strip()

    # ① 四态
    for state, cls in CT_CN_STATES:
        if v.startswith(state):
            return _badge_hold(badges, cls, state, v[len(state):])

    # ② `{色点} {状态词}`
    m = re.match(r"^(🟢|🟡|🔴|⚪|🔵)\s*(.+)$", v)
    if m:
        dot, rest = m.group(1), m.group(2).strip()
        for word in sorted(BADGE_WORDS, key=len, reverse=True):
            if rest == word or re.match(
                r"^" + re.escape(word) + r"(?![A-Za-z])", rest
            ):
                cls = BADGE_WORDS[word] or DOT_TO_BADGE[dot]
                # 状态词后若紧接 `（…）`，括号内容属补充说明，留在 Badge 外
                return _badge_hold(badges, cls, word, rest[len(word):])

    # ③ 整串即状态词（无颜色点）
    plain = re.sub(r"\*\*", "", v).strip()
    if plain in BADGE_WORDS:
        return _badge_hold(badges, BADGE_WORDS[plain], plain)

    return value


def cell_html(value: str) -> str:
    """表格单元格渲染：Badge 提取 → 行内格式 → Badge 还原。"""
    badges = []
    staged = extract_badges(value, badges)
    t = inline(staged)
    for i, (cls, txt) in enumerate(badges):
        t = t.replace(f"\x01{i}\x01",
                      f'<span class="badge {cls}">{esc(txt)}</span>')
    return t


def field_label_html(label: str) -> str:
    """字段名渲染：**中文加粗、英文正常字重**（V1.1.2 展示层拆分，文字不改）。"""
    t = re.sub(r"\*\*", "", label).strip()
    if t in LABEL_SPLIT:
        cn, en = LABEL_SPLIT[t]
        out = f'<span class="fld-cn">{esc(cn)}</span>'
        if en:
            out += f' <span class="fld-en">{esc(en)}</span>'
        return out
    return f'<span class="fld-cn">{esc(t)}</span>'


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


def render_conclusion(buf, p2_full=None):
    """结论卡渲染：中文结论（大号）+ 英文副标题 + 原因。**取值与原因逐字不改。**

    V1.1.2：原因支持 `⟪P2⟫` 拆分 —— 第一页显示摘要，完整原因进 Page 2。
    """
    label = buf[0] if buf else ""
    verdict_raw = buf[1] if len(buf) > 1 else ""
    reason_raw = " ".join(buf[2:]) if len(buf) > 2 else ""

    v_plain = re.sub(r"\*\*", "", verdict_raw).strip()
    key = next((k for k in CONCL_EN if k in v_plain), None)
    cls = CONCL_CLS.get(key, "unk")
    en = CONCL_EN.get(key, "")
    v_text = re.sub(r"^(🟢|🟡|🔴|⚪|🔵)\s*", "", v_plain).strip()

    if p2_full is not None and P2_MARK in reason_raw:
        head, _, tail = reason_raw.partition(P2_MARK)
        p2_full["Sales Conclusion"] = tail.strip().lstrip('；;，,。 ')
        reason_raw = head.strip()

    parts = [f'<div class="concl-label">{inline(label)}</div>',
             f'<div class="concl-verdict">{esc(v_text)}</div>']
    if en:
        parts.append(f'<div class="concl-sub">{esc(en)}</div>')
    if reason_raw:
        parts.append(f'<div class="concl-reason">{inline(reason_raw)}</div>')
    return f'<blockquote class="conclusion concl-{cls}">' + "".join(parts) + "</blockquote>"


def md_to_html_body(lines):
    """返回 (html_blocks, page_breaks, p2_full)。

    p2_full：V1.1.2 长字段的**完整原文**（`⟪P2⟫` 前后拼接），供 Page 2 展示。
    """
    out = []
    i = 0
    n = len(lines)
    page_break_before = set()
    block_idx = 0
    p2_full = {}

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
            is_card = bool(header) and header[0] in ("字段", "Field")
            body_rows = []
            j = i + 2
            while j < n and lines[j].strip().startswith("|"):
                body_rows.append(split_row(lines[j]))
                j += 1
            t = [f'<table class="{"card-table" if is_card else "data-table"}">',
                 "<thead><tr>"]
            t += [f"<th>{inline(c)}</th>" for c in header]
            t.append("</tr></thead><tbody>")
            for r in body_rows:
                t.append("<tr>")
                for ci, c in enumerate(r):
                    # V1.1.2：主卡长字段 `⟪P2⟫` 拆分 —— Page 1 只显示摘要，
                    # 完整原文收集到 p2_full 供 Page 2 展示（**不删内容**）。
                    if is_card and ci == 1 and P2_MARK in c:
                        head, _, tail = c.partition(P2_MARK)
                        fname = normalize_field(r[0]) if r else ""
                        if fname and tail.strip():
                            p2_full[fname] = tail.strip().lstrip('；;，,。 ')
                        c = head.strip()
                    if is_card and ci == 0:
                        t.append(f"<td>{field_label_html(c)}</td>")
                    else:
                        t.append(f"<td>{cell_html(c) if is_card else inline(c)}</td>")
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
            if is_conclusion:
                out.append(render_conclusion(buf, p2_full))
            else:
                out.append("<blockquote>"
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

    return out, page_break_before, p2_full


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


def p2_details_block(p2_full):
    """Page 2 的「字段详细内容」区块（V1.1.2）。

    展示 Page 1 被摘要化后**移走的那部分原文**（`⟪P2⟫` 之后）。
    Page 1 摘要 + 本区块 = 字段完整原文，**内容逐字不改、不新增、不删除**。
    """
    if not p2_full:
        return None
    order = [f for f in LONG_FIELDS if f in p2_full]
    order += [f for f in p2_full if f not in order]
    rows = []
    for k in order:
        label = KEY_TO_LABEL.get(k, k)
        rows.append(f"<tr><td><strong>{esc(label)}</strong></td>"
                    f"<td>{cell_html(p2_full[k])}</td></tr>")
    return ('<h3 class="group-title sub">字段详细内容 · Field Details（Page 1 摘要之外）</h3>'
            '<table class="card-table detail-table"><thead><tr><th>字段</th><th>完整内容</th>'
            '</tr></thead><tbody>' + "".join(rows) + '</tbody></table>')


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
        if mode == 1 and ("字段详细内容" in plain or "判定依据" in plain
                          or "Demand Status 明细" in plain):
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


def _plain(h: str) -> str:
    return re.sub(r"<[^>]+>", "", h or "").strip()


def evidence_to_cards(blocks):
    """附录 A 表格 → **Evidence Card**（V1.1.2）。

    纯版式转换：按既有 `Decision Impact` 排序，取 High / Medium 前 N 条渲染为卡片。
    **不新增、不推断、不改写**任何字段值；完整 Evidence 仍保留在 Markdown。
    """
    out = []
    for b in blocks:
        if not re.match(r'<table class="data-table">', b):
            out.append(b)
            continue
        rows = re.findall(r"<tr>(.*?)</tr>", b, re.S)
        if not rows or "Decision Impact" not in rows[0]:
            out.append(b)
            continue

        cols = [_plain(c) for c in re.findall(r"<th>(.*?)</th>", rows[0])]
        idx = {name: k for k, name in enumerate(cols)}
        if "Decision Impact" not in idx:
            out.append(b)
            continue

        def cell(cells, name):
            k = idx.get(name)
            return cells[k] if k is not None and k < len(cells) else ""

        def rank(cells):
            low = cell(cells, "Decision Impact").lower()
            for key, v in ((">high<", 0), (">medium<", 1), (">low<", 2)):
                if key in low:
                    return v
            return 3

        body = [c for c in (re.findall(r"<td>(.*?)</td>", r, re.S) for r in rows[1:]) if c]
        body.sort(key=rank)
        picked = [c for c in body if rank(c) <= 1][:EVIDENCE_CARD_LIMIT]
        if not picked:
            picked = body[:EVIDENCE_CARD_LIMIT]

        cards = []
        for c in picked:
            eid = cell(c, "#")
            etype_raw = cell(c, "类型")
            etype = _plain(etype_raw)
            impact = _plain(cell(c, "Decision Impact"))
            concl = cell(c, "结论")
            src = cell(c, "Source")
            reason = cell(c, "Reason")
            conf = cell(c, "Confidence")

            lines = [f'<div class="ev-eid">{eid} · {etype_raw} · '
                     f'{esc(impact.upper())} IMPACT</div>']
            for key, val in (("结论 Conclusion", concl), ("来源 Source", src),
                             ("置信度 Confidence", conf)):
                if _plain(val) not in ("", "—", "-"):
                    lines.append(f'<div class="ev-line">'
                                 f'<span class="ev-key">{key}：</span>{val}</div>')
            if etype.upper().startswith("INFERENCE") and _plain(reason) not in ("", "—", "-"):
                lines.append(f'<div class="ev-line">'
                             f'<span class="ev-key">Reason：</span>{reason}</div>')
            if etype.upper().startswith("UNKNOWN"):
                st = etype.split("·", 1)[1].strip() if "·" in etype else "searched"
                lines.append(f'<div class="ev-line">'
                             f'<span class="ev-key">Status：</span>Unknown · {esc(st)}</div>')
            cards.append('<div class="ev-card">' + "".join(lines) + "</div>")

        out.append(f'<div class="ev-list">{len(cards)} 条关键证据</div>'
                   + "".join(cards))
    return out


# ---------------------------------------------------------------- HTML 组装

CSS = """
@page { size: A4; margin: 12mm 11mm; }
* { box-sizing: border-box; }
body {
  font-family: "Microsoft YaHei", "PingFang SC", "Helvetica Neue", Arial, sans-serif;
  color: #1c1f23; background: #ffffff; font-size: 10pt; line-height: 1.5;
  margin: 0; padding: 0;
}
.page { page-break-after: always; }
.page:last-child { page-break-after: auto; }
.page-head {
  border-bottom: 2px solid #1c1f23; padding-bottom: 3px; margin: 0 0 8px 0;
  font-size: 9pt; letter-spacing: .12em; text-transform: uppercase; color: #5a626b;
  display: flex; justify-content: space-between;
}

/* ---- 字体层级（V1.1.2）---- */
h1 { font-size: 16pt; font-weight: 700; margin: 1px 0 3px 0; letter-spacing: -.01em; }
h2 { font-size: 11.5pt; font-weight: 700; margin: 9px 0 5px 0; padding-left: 7px;
     border-left: 3px solid #1c1f23; }
h3 { font-size: 10pt; font-weight: 700; margin: 8px 0 3px 0; color: #33383e; }
p { margin: 3px 0; }

/* ---- V1.1.2 Section Header（四组统一浅灰蓝底、深色加粗）---- */
h3.group-title {
  font-size: 9.5pt; font-weight: 700; letter-spacing: .03em;
  color: #1f2b3a; background: #e8eef5;
  margin: 7px 0 2px 0; padding: 3px 8px;
  border-left: 0; border-bottom: 0; border-radius: 2px;
}
h3.group-title.sub { background: #f2f5f9; color: #47566b; font-size: 9.8pt; }

/* ---- 表格基础 ---- */
table { border-collapse: collapse; width: 100%; margin: 6px 0; font-size: 9.6pt; }
th, td { border: 1px solid #d6dae0; padding: 5px 7px;
         text-align: left; vertical-align: middle; }
th { background: #f2f4f6; font-weight: 600; }
table.data-table td:first-child { white-space: nowrap; }

/* ---- V1.1.2 主卡：字段列浅灰蓝 + 固定 20%；判定列白底 ---- */
table.card-table { font-size: 9.4pt; margin: 3px 0; }
table.card-table td { background: #ffffff; padding: 3.5px 7px; }
table.card-table td:first-child {
  width: 20%; background: #eef2f7; white-space: normal;
  text-align: left; vertical-align: middle;
}
.fld-cn { font-weight: 700; color: #1c1f23; }
.fld-en { font-weight: 400; color: #6b7480; font-size: 9pt; }

/* ---- V1.1.2 Badge（短状态；不整行染色）---- */
.badge {
  display: inline-block; padding: 1px 7px; border-radius: 9px;
  font-size: 9pt; font-weight: 700; line-height: 1.5; white-space: nowrap;
}
.badge-ok   { background: #e3f4ea; color: #1f7a45; border: 1px solid #b7e0c8; }
.badge-warn { background: #fdf3dc; color: #8a6100; border: 1px solid #f0dca6; }
.badge-bad  { background: #fdeaea; color: #ab2222; border: 1px solid #f2c4c4; }
.badge-unk  { background: #f0f2f4; color: #5f6874; border: 1px solid #d9dee3; }
.badge-info { background: #e7f0fa; color: #215d9e; border: 1px solid #bed8f0; }
td .badge { vertical-align: middle; }

/* ---- V1.1.2 结论卡（左色条 + 浅色语义背景）---- */
blockquote.conclusion {
  margin: 9px 0 3px 0; padding: 9px 13px 9px 13px;
  border: 1px solid #d6dae0; border-left: 6px solid #9aa1a9;
  background: #f7f9fb; border-radius: 3px;
}
blockquote.conclusion.concl-ok   { background: #f2faf5; border-color: #cbe7d7;
                                   border-left-color: #1f9d55; }
blockquote.conclusion.concl-warn { background: #fdfaf2; border-color: #f0e2c0;
                                   border-left-color: #d99a04; }
blockquote.conclusion.concl-bad  { background: #fdf4f4; border-color: #f0cccc;
                                   border-left-color: #cf2e2e; }
blockquote.conclusion.concl-unk  { background: #f7f8fa; border-color: #d9dee3;
                                   border-left-color: #9aa1a9; }
.concl-label { font-size: 7.8pt; letter-spacing: .14em; text-transform: uppercase;
               color: #5a626b; font-weight: 700; margin-bottom: 2px; }
.concl-verdict { font-size: 16pt; font-weight: 700; line-height: 1.18; }
.concl-sub { font-size: 9pt; color: #5a626b; margin-top: 0; }
.concl-reason { font-size: 9.2pt; line-height: 1.4; color: #33383e;
                margin-top: 3px; text-align: left; }

/* ---- V1.1.2 Evidence Card（替代 7 列窄表格）---- */
.ev-list { font-size: 8.2pt; color: #6b7480; margin: 4px 0 3px 0; }
.ev-card {
  border: 1px solid #dde2e8; border-left: 3px solid #2f6fb5;
  background: #fbfcfd; border-radius: 2px;
  padding: 4px 8px 4px 8px; margin: 0 0 3px 0;
}
.ev-eid { font-size: 8.2pt; font-weight: 700; letter-spacing: .05em;
          color: #2f6fb5; text-transform: uppercase; margin-bottom: 1px; }
.ev-line { font-size: 8pt; line-height: 1.32; text-align: left; }
.ev-key { font-weight: 700; color: #3d444c; }

/* ---- V1.1.2 Page 2/3 正文密度容器 ---- */
.body-dense { font-size: 9pt; line-height: 1.38; }
.body-dense p { margin: 2.5px 0; }
.body-dense li { margin: 1px 0; }
.body-dense h2 { font-size: 11pt; margin: 7px 0 4px 0; }
.body-dense h3 { font-size: 9.5pt; margin: 6px 0 2px 0; }

/* ---- V1.1.2 Page 2 字段详细内容（紧凑）---- */
table.detail-table { font-size: 8pt; margin: 3px 0; }
table.detail-table td { padding: 2.5px 6px; }
table.detail-table td:first-child { width: 20%; background: #f4f7fa; }

code { background: #f2f4f6; padding: 0 3px; border-radius: 2px;
       font-family: Consolas, "Courier New", monospace; font-size: 9pt; }
blockquote { margin: 6px 0; padding: 5px 9px; background: #f7f8fa;
             border-left: 3px solid #b9c0c8; color: #3d444c; font-size: 9.6pt; }
pre { background: #f7f8fa; border: 1px solid #e3e7eb; padding: 7px 9px;
      font-family: Consolas, monospace; font-size: 8.8pt; white-space: pre-wrap; }
ul, ol { margin: 3px 0 3px 16px; padding: 0; }
li { margin: 1px 0; }
hr.sep { border: 0; border-top: 1px solid #e3e7eb; margin: 9px 0; }
.fold { margin: 6px 0; }
.fold-title { font-weight: 700; font-size: 9.8pt; margin: 8px 0 3px 0; }
.dot { display: inline-block; width: 8px; height: 8px; border-radius: 50%;
       margin-right: 3px; vertical-align: baseline; }
.dot.ok { background: #1f9d55; }
.dot.warn { background: #d99a04; }
.dot.bad { background: #cf2e2e; }
.dot.unk { background: #9aa1a9; }
.dot.info { background: #2f6fb5; }
.legend { margin-top: 10px; font-size: 8.6pt; color: #5a626b;
          border-top: 1px solid #e3e7eb; padding-top: 5px; }
.legend span.item { margin-right: 12px; }
.pagenum { font-size: 8.6pt; color: #8a9099; }
"""


def build_html(md_text: str, single: bool) -> str:
    lines = md_text.splitlines()
    blocks, _, p2_full = md_to_html_body(lines)
    blocks = evidence_to_cards(blocks)

    # V1.1.2：把被摘要化的长字段完整内容挂到 Page 2 首部（**内容逐字不改**）
    detail = p2_details_block(p2_full)
    if detail:
        pos = next((k for k, b in enumerate(blocks) if "判定依据" in _plain(b)), None)
        blocks.insert(pos if pos is not None else 0, detail)

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
        # V1.1.2：Page 2/3 正文包一层容器统一收敛字号（纯版式）
        if idx >= 1:
            html_parts.append("<div class='body-dense'>")
        html_parts.extend(body)
        if idx >= 1:
            html_parts.append("</div>")
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
