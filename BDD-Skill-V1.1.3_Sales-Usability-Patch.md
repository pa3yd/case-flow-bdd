# BDD Customer Intelligence Skill · V1.1.3 Sales Usability Patch

**执行日期**：2026-09-27
**范围**：仅 Presentation / PDF Rendering / Output Visual Layer + SKILL.md 默认调用协议
**判断逻辑改动**：**零**

---

## 一、修改文件清单

**共 15 个文件（未增减）／4,987 行（+295）**

### 已改 4 个（全部展示层）

| 文件 | 改动 |
|---|---|
| `SKILL.md` | 版本 → V1.1.3；**新增「零、Default Invocation Protocol」**；第十节第二层改为附录 A / 附录 B 双层；第 14 步补 PDF 三页对照表；第十二节文件说明同步 |
| `references/output-visual-rules.md` | 第五部分 Page 2 / Page 3 模板**整体重写**；新增「不进 PDF 的内容」清单；第六部分补审计区切分与三页装配规则；第七部分职责边界同步；第三部分第八节标注为 V1.1.2 历史记录 |
| `assets/output-card-template.md` | 标题 → V1.1.3；结构总览加附录 B；新增「Markdown → 业务 PDF 三页对应」表；附录 A 表头加 `主题` 列并说明；新增「附录 B · 审计信息」模板；新增「展示层禁止项（V1.1.3）」 |
| `scripts/render_pdf.py` | 1,016 → 1,114 行。Page 2 改为 5 张销售信息卡；Page 3 改为 KEY EVIDENCE 卡片（主题/简洁事实/Source）；新增审计区切分；`field_full` 改为存字段完整原文 |

### 未改 11 个判断规则文件（md5 逐一 MATCH）

`evidence-policy.md` · `bdd-relevance-rules.md` · `bdd-fit-rules.md` · `customer-type-playbook.md` · `opportunity-type-rules.md` · `sales-conclusion-rules.md` · `current-treatment-rules.md` · `lead-signals.md` · `must-ask-params.md` · `contact-role-map.md` · `wastewater-signal-map.md`

### 交付产物

| 文件 | 说明 |
|---|---|
| `BASF_BDD_Intelligence_2026-09-27.md` | 更新为 V1.1.3 结构（附录 A 加 `主题` 列；审计段落归入附录 B） |
| `BASF_BDD_Intelligence_2026-09-27.pdf` | 重新渲染 · **3 页** |
| `_v113-comparison/` | 6 张截图（Page 1 / 2 / 3 × Before / After） |
| `_bdd-skill-archive/V1.1.2-backup-20260927/` | V1.1.2 全量备份（15 文件 md5 全 MATCH，可完整回退） |

---

## 二、改动一：Default Invocation Protocol（SKILL.md 新增「零」节）

**日常只给公司名或网址 + 表达背调意图，即自动执行完整 14 步流程。**

| 触发意图 | 示例输入（原样即可触发） |
|---|---|
| 背调 | `背调 GEA Group，gea.com` |
| 客户分析 | `分析客户：GEA Group，gea.com` |
| 是否值得开发 | `GEA Group 是否值得作为 BDD 客户开发？` |
| 其他同义表达 | 查一下这家公司 / 这家公司什么来头 / 判断一下是不是 BDD 客户 / 帮我看看 gea.com |

**默认行为（用户无需重复输入）**：完整 14 步 · Markdown + PDF 双输出 · 自动用当前版本号 · 自动按模板输出 13 个 Internal Key · 自动执行「禁止预设结论」· 缺失信息自动写 `Unknown`

**仅两种情形才追问**：① 既无公司名也无网址；② 公司名存在多个完全不同的同名主体

**严格回归测试 Prompt 保留**：显式规格句式（重申版本号 + 禁止预设 + 逐字段 + 输出格式）仍然逐条生效，本协议不覆盖、不简化。

---

## 三、改动二：PDF Page 2 / Page 3

### Page 1 · 完全不变

唯一差异是页脚的**执行版本号**行（`V1.1.2` → `V1.1.3`）。**13 个字段、四组结构、Badge、结论卡 HTML 逐字节一致。**

### Page 2 · Before / After

| | Before（V1.1.2） | After（V1.1.3） |
|---|---|---|
| 页眉 | `WHY THIS CUSTOMER` | **`SALES INTELLIGENCE ｜开发情报`**（11pt 加粗深色） |
| 版式 | 「字段详细内容 · Field Details」大字段表 + 判定依据 + Demand Status + **风险**段 | **5 张销售信息卡**，单列流式 |
| 内容 | 5 个长字段的「其余部分」+ 判定依据全文 + 风险与财务警示全文 | ① `Why BDD｜为什么和 BDD 有关`（判定依据 + PWE/CSD）② `Current Treatment｜目前怎么处理` ③ `Priority Site｜优先厂区` ④ `Who to Contact｜找谁` ⑤ `What to Verify｜还要确认什么` |
| 长字段处理 | 只显示被压缩掉的「其余部分」，需回看 Page 1 才能读通 | **显示完整原文**（摘要 + 其余拼接），Page 2 可独立读懂 |
| 阅读负担 | 表格列窄、行长、术语多 | 5 段结论式短段落 |

### Page 3 · Before / After

| | Before（V1.1.2） | After（V1.1.3） |
|---|---|---|
| 页眉 | `KEY EVIDENCE` | **`KEY EVIDENCE ｜关键依据`**（11pt 加粗深色） |
| 卡片标题 | `E1 · FACT · HIGH IMPACT` | **`E1 · 主体登记与上市信息`**（编号 + 主题） |
| 卡片字段 | 结论 Conclusion / 来源 Source / **置信度 Confidence** | **简洁事实 / 来源** |
| 审计术语 | FACT · INFERENCE · UNKNOWN · Confidence · HIGH IMPACT | **0 处** |
| 条数 | 6 条 | **8 条** |
| 页尾 | 类型定义 + Decision Impact 说明 + 可溯源率 + 集团级 vs 厂区级 + 同名主体排除 + 来源冲突项 + **边界声明** | **无**（全部移到 Markdown 附录 B） |
| 布局 | 卡片 + 6 段审计长文 | 卡片流式，无 7 列窄表格 |

**保留在 Markdown 的完整审计层**（一字未删）：附录 A 全 29 条 × 8 列（含 FACT/INFERENCE/UNKNOWN · Confidence · Decision Impact · Source · Reason）＋ 附录 B（可溯源率 · 类型定义 · Decision Impact 说明 · 集团级 vs 厂区级 · 同名主体排除 · 来源冲突项）＋ `## 边界声明`

**渲染层切分规则**：从 `## 附录 B` 或 `## 边界声明` 起不入 PDF —— 只影响 PDF 版式，**Markdown 原文不动**。

---

## 四、BASF 展示回归结果（22 / 22 PASS）

| # | 检查项 | 结果 |
|---|---|---|
| 1 | 13 个字段完整（Internal Key） | ✅ 13 / 13 |
| 2 | Page 1 主卡字段逐字段一致（完整原文级） | ✅ 0 差异 |
| 3 | Page 1 实际渲染值逐字段一致 | ✅ 0 差异 |
| 4 | Sales Conclusion 取值 + 全文一致 | ✅ `🟡 建议先验证` |
| 5 | Current Treatment 状态 + 正文一致 | ✅ `🟢 已确认 Confirmed` |
| 6 | **PDF 仍为 3 页** | ✅ 3 页 |
| 7 | HTML 仍为 3 个 section | ✅ 3 段 |
| 8 | Page 1 仅版本号一行差异 | ✅ 差异 2 行（均为版本行） |
| 9 | Page 2 = 5 张销售信息卡 | ✅ 5 张 |
| 10 | Page 2 卡片标题正确 | ✅ 五标题逐字匹配 |
| 11 | Page 2 无大型字段表 | ✅ 无 `<table>` |
| 12 | Page 2 页眉 = `SALES INTELLIGENCE ｜开发情报` | ✅ |
| 13 | Page 3 = 6 ~ 8 条关键依据 | ✅ 8 条 |
| 14 | **Page 3 无审计术语** | ✅ 0 处 |
| 15 | Page 3 页眉 = `KEY EVIDENCE ｜关键依据` | ✅ |
| 16 | Page 3 无 7 列窄表格 | ✅ |
| 17 | **Markdown Evidence 条数一致** | ✅ 29 → 29 |
| 18 | **Evidence 正文逐字一致**（类型/结论/Source/Reason/Confidence/Impact） | ✅ 0 差异 |
| 19 | Evidence 新增 `主题` 列已填满 | ✅ 29 / 29 |
| 20 | 审计 / 边界信息未进入 PDF | ✅ 0 处 |
| 21 | 审计信息仍完整保留在 Markdown | ✅ |
| 22 | 无越界输出（小试 / 报价 / 选型 / 工艺参数） | ✅ 0 处 |

**RESULT : 22 / 22 PASS**

### 兼容性冒烟测试

用同一渲染器回放**旧版报告**（`Umicore_..._V1.1.2.md`、`GEA_BDD_Intelligence_2026-09-27.md`，均无 `主题` 列、无附录 B）：**均 3 页、5 张信息卡、8 条关键依据、无报错**；`主题` 缺失时降级为只显示证据编号 `E3 / E6 / E7 / E8`。已有 8 份历史报告**无需重渲染即可继续使用**。

---

## 五、本次仅展示层修改声明

**未修改**：Evidence Policy · Customer Path · Industry Map · BDD Opportunity 判断规则 · Demand Status 判断规则 · Commercial Risk · Financial Warning · Opportunity Type · Priority Site · Sales Conclusion 五值与判定逻辑 · 13 个 Internal Key · FACT / INFERENCE / UNKNOWN 规则 · 25 条硬性约束。

**未新增**：字段（13 个 Internal Key 未动）· Skill · 评分 · CRM 功能。**未进入 V1.2。**

渲染层仍只做版式转换与字段搬运，不新增、不推断、不改写、不润色任何内容；渲染前 13 字段完整性校验照旧强制。

---

## 六、两点需你确认（不阻塞，未擅自处理）

### 1. `主题` 列 —— Page 3 规格的必然产物

Page 3 要求每条写「**主题** / 简洁事实 / Source」，但原附录 A 表没有「主题」字段。本次处理方式：

- 附录 A 表格新增 **`主题`** 列（第 2 列），由分析阶段填**中性短标题**（如「废水处理厂投运与工艺升级」），**不参与任何判断**；
- 缺失时渲染层只显示证据编号，**不推断补写**。

如果你不希望 Markdown 多这一列，可回退为「仅显示编号」，Page 3 卡片标题就只剩 `E1` —— 说一声即可（属下一轮）。

### 2. Commercial Risk / Financial Warning 已不在业务 PDF

按你的 5 张卡规格，Page 2 不含「风险」段。当前情况：

- `Commercial Risk` / `Risk Note` / `Financial Warning` **仍完整保留在 Markdown**（主卡下方「风险」块）；
- BASF 的 **FW = Yes** 已在 **Page 1 结论卡原因**中写明（"但 Financial Warning = Yes（集团持续公开重组与裁员…），按规则上限降至本档"），业务员第一页即可看到；
- 但其他案例若 FW 未进入结论原因，PDF 中将看不到该风险。

如需在 Page 2 增加第 6 张卡「风险提示｜Risk」，属规格变更，请另行确认。

---

*Skill 本体 15 个文件；V1.1.2 备份可完整回退。*
