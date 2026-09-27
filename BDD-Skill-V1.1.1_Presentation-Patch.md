# BDD Customer Intelligence Skill · V1.1.1 Presentation Patch 交付报告

**执行日期**：2026-09-26
**Patch 类型**：展示层（Presentation Layer）only
**Skill 目录**：`C:/Users/Administrator/.workbuddy/skills/bdd-inquiry-analyzer/`
**V1.1 备份**：`D:/Case Flow/_bdd-skill-archive/V1.1-backup-20260926/`（15 文件，md5 全 MATCH，可完整回退）

---

## 一、变更内容

### 1.1 改动文件（4 个）

| 文件 | 变更 |
|---|---|
| `references/output-visual-rules.md` | **新增第二部分「展示层」**（Display Label 映射 / 四组分组 / Current Treatment 四态 / 结论卡 / 展示层边界）；原二~六部分顺延为三~七部分；第五部分新增「V1.1.1 排版修复」 |
| `assets/output-card-template.md` | 主卡改四组呈现 + Display Label；`Sales Conclusion` 移出表格为结论卡；新增「Display Label 对照」表与「Current Treatment 状态徽标」规则；禁止项新增「展示层禁止项」小节 |
| `scripts/render_pdf.py` | 新增 `FIELD_ALIASES` 别名表与 `normalize_field()`；`extract_main_card_fields()` 支持多表格累加 + 结论卡识别；blockquote 支持结论卡样式；h3 支持四组标题样式；`inline()` 与 `split_row()` 两处排版修复 |
| `SKILL.md` | 标题版本号 → V1.1.1；新增 V1.1.1 声明段；第十节输出结构改四组呈现 + Current Treatment 状态硬规则；第十二节文件说明同步 |

### 1.2 13 个 Internal Key 完全不变 + 新增 Display Label

| # | Internal Key（**未改**） | Display Label（新增） | 组 |
|---|---|---|---|
| 1 | `Company` | 公司 Company | WHO |
| 2 | `Country` | 国家 Country | WHO |
| 3 | `What They Do` | 主营业务 Business | WHO |
| 4 | `Customer Type` | 客户类型 Customer Type | WHO |
| 5 | `Industry Match` | 行业匹配 Industry Match | WHY |
| 6 | `BDD Opportunity` | BDD机会 BDD Opportunity | WHY |
| 7 | `Demand Status` | 需求状态 Demand Status | WHY |
| 8 | `Current Wastewater Treatment / Technology` | 现有废水处理 Current Treatment | WHERE / WHO |
| 9 | `Priority Site` | 优先厂区 Priority Site | WHERE / WHO |
| 10 | `Who to Contact` | 关键联系人 Contact | WHERE / WHO |
| 11 | `What Is Missing` | 待确认信息 Missing Info | ACTION |
| 12 | `Next Action` | 下一步 Next Action | ACTION |
| 13 | `Sales Conclusion` | 开发建议 Sales Conclusion（**结论卡**） | ACTION |

> 渲染脚本通过别名表把 Display Label 还原为 Internal Key；校验、字段引用、规则判据一律仍用 Internal Key。

### 1.3 第一页四组结构

**WHO · 客户是谁** → **WHY · 为什么值得看** → **WHERE / WHO · 从哪里切入** → **ACTION · 现在怎么办**

顺序固定，对应业务员阅读链路：认识 → 判断 → 切入 → 行动。

### 1.4 Current Treatment 四态徽标

| 徽标 | 判据（**必须有一个 E# 支撑**） |
|---|---|
| `🟢 Confirmed` | 证据明确载明已建成 / 在运行 / 在售交付 |
| `🟡 Partial` | 证据只覆盖部分环节，或原文含"部分厂区 / 部分工艺"限定 |
| `🔵 Planned` | 证据明确表述为规划 / 拟建 / 在建，尚未投运 |
| `⚪ Unknown` | 无相关证据（**不得据"这类厂应该有"填**） |

**不参与任何判断字段，不与 `BDD Opportunity` 联动。**

### 1.5 结论卡

`Sales Conclusion` 从主卡表格移出，渲染为第一页四组之后的独立卡片（深色边框 + 加大取值字号），**取值与原因逐字保留**。

### 1.6 附带修复两处既有排版缺陷

| # | 缺陷 | 修复 | 性质 |
|---|---|---|---|
| 1 | 值中显式 `<br>` 被转义为字面 `&lt;br&gt;` | `inline()` 还原为真换行 | 纯排版 |
| 2 | 值中 `\|`（复合类型 `+\|`）导致表格被拆成两列 | `split_row()` 先保护 `\|` 再拆分 | 纯排版 |

---

## 二、Before / After 第一页对比

截图目录：`D:/Case Flow/_v111-comparison/`

| 文件 | 说明 |
|---|---|
| `Umicore_Page1_Before.png` / `_After.png` | Umicore 第一页对比 |
| `EnviroChemie_Page1_Before.png` / `_After.png` | EnviroChemie 第一页对比 |

### 2.1 结构对比（Umicore）

| | Before（V1.1） | After（V1.1.1） |
|---|---|---|
| 主卡形态 | 单表格，13 行平铺 | **4 组分表**，带组标题 |
| 字段名 | 仅英文 Internal Key | **中文 + 英文 Display Label** |
| 分组标题 | 无 | `WHO · 客户是谁` / `WHY · 为什么值得看` / `WHERE / WHO · 从哪里切入` / `ACTION · 现在怎么办` |
| Current Treatment | `比利时霍博肯（Hoboken）厂：物化处理 + …` | `🟢 Confirmed · 比利时霍博肯（Hoboken）厂：物化处理 + …` |
| Sales Conclusion | 表格最后一行，与其它字段同权重 | **表格外独立结论卡**，深色边框、取值 12pt |
| `<br>` | 显示为字面文本 | 正常换行 |
| 阅读动线 | 需逐行扫 13 行 | 先看 WHO 认公司 → WHY 判机会 → WHERE 找切入 → ACTION 看结论卡 |

### 2.2 结构对比（EnviroChemie）

同上，另多一处修复：

| | Before（V1.1） | After（V1.1.1） |
|---|---|---|
| BDD机会行 | `+\|` 把表格拆成两列，值溢出到额外列 | **单元格不裂开**，`EPC / Integration Opportunity +\| Technology Partner Opportunity · 🔴 Conflict: 潜在竞争` 同格显示 |

### 2.3 演示顺序（约 5 分钟）

1. 打开 `EnviroChemie_Page1_Before.png` → 指出：13 行平铺、无分组、`<br>` 字面泄漏、BDD机会行裂列。
2. 打开 `EnviroChemie_Page1_After.png` → 指出：四组标题、中英标签、`🟢 Confirmed` 徽标、底部结论卡、裂列已修。
3. 打开 `Umicore_Page1_After.png` → 指出：结论卡 `🟢 建议开发` 与 V1.1 完全一致（判断未变）。

---

## 三、展示层回归结果（Umicore + EnviroChemie）

### 3.1 排版 / 字段完整性 / 结论一致性

| # | 检查项 | Umicore | EnviroChemie |
|---|---|---|---|
| 1 | 13 个 Display Label 齐全 | ✅ 13/13 | ✅ 13/13 |
| 2 | 四组标题渲染（顺序正确） | ✅ 4 组 | ✅ 4 组 |
| 3 | 字段数未增减（12 表格 + 1 结论卡） | ✅ | ✅ |
| 4 | Current Treatment 状态徽标 | ✅ 🟢 Confirmed | ✅ 🟢 Confirmed |
| 5 | 结论卡在 Page 1 内 | ✅ | ✅ |
| 6 | 结论卡为独立醒目块（唯一） | ✅ | ✅ |
| 7 | 结论卡含五值之一 | ✅ | ✅ |
| 8 | PDF 约 3 页 | ✅ 3 页 | ✅ 3 页 |
| 9 | 附录 A · Evidence 结构保留 | ✅ | ✅ |
| 10 | 无越界输出（小试 / 报价 / 选型） | ✅ 0 处 | ✅ 0 处 |
| 11 | 无字面 `<br>` 泄漏 | ✅ | ✅ |
| 12 | 表格列数一致（`+\|` 未拆列） | ✅ | ✅ |

**RESULT_presentation_layer : 24 / 24 PASS**

### 3.2 判断内容一致性（逐字段比对）

| 项 | Umicore | EnviroChemie |
|---|---|---|
| V1.1 字段数 / V1.1.1 字段数 | 13 / 13 | 13 / 13 |
| 判断内容逐字一致字段 | 12 / 13 | 12 / 13 |
| 仅多状态前缀（展示层新增） | 1 → `Current Treatment` | 1 → `Current Treatment` |
| **判断内容有差异字段** | **0** | **0** |
| Sales Conclusion 取值一致 | ✅ True | ✅ True |
| Sales Conclusion 全文一致 | ✅ True | ✅ True |

**CHECK_judgement_consistency : PASS — 判断内容零变更**

### 3.3 渲染前校验

| 项 | 结果 |
|---|---|
| `CHECK_main_card` | PASS — 13 / 13 |
| `CHECK_evidence_col` | PASS |
| `CHECK_pdf` | PASS — Umicore 468.7 KB / EnviroChemie 524.3 KB |

---

## 四、约束合规核对（8 条）

| # | 约束 | 结果 | 依据 |
|---|---|---|---|
| 1 | 13 个 Internal Key 完全不变，仅加 Display Label | ✅ | 别名表反向还原；`REQUIRED_FIELDS` 未改 |
| 2 | 第一页按四组展示 | ✅ | 4 组标题渲染，顺序固定 |
| 3 | Current Treatment 加四态状态，只能来自现有证据 | ✅ | 两家属 `Confirmed`，分别由 E12（Umicore）与 E3/E4/E12（EnviroChemie）支撑 |
| 4 | Sales Conclusion 为第一页最醒目结论卡（五色 + 原因） | ✅ | `blockquote.conclusion`，位置 p1 < concl < p2 |
| 5 | Markdown 完整 Evidence 结构不变；PDF 约 3 页 | ✅ | 附录 A 原样保留；两份均 3 页 |
| 6 | PDF 渲染层不得改变任何判断结果 | ✅ | 逐字段比对 0 差异；脚本无判断逻辑 |
| 7 | 不新增字段 / Skill / 评分 / CRM 功能 | ✅ | 文件数 15 未变；字段数 13 未变 |
| 8 | 用 Umicore + EnviroChemie 做展示层回归 | ✅ | 24/24 PASS + 判断零变更 PASS |

**未改动**：Evidence Policy / Customer Path / Industry Map / BDD Opportunity / Demand Status / Commercial Risk / Opportunity Type / Priority Site 全部判断逻辑，以及硬性约束 1~25、决策链 14 节点、工作流 14 步。

---

## 五、交付产物清单

| 产物 | 路径 |
|---|---|
| V1.1.1 客户情报卡 MD | `D:/Case Flow/Umicore_BDD_Intelligence_2026-09-26_V1.1.1.md`<br>`D:/Case Flow/EnviroChemie_BDD_Intelligence_2026-09-26_V1.1.1.md` |
| V1.1.1 业务员版 PDF（三页） | `D:/Case Flow/Umicore_BDD_Intelligence_2026-09-26_V1.1.1.pdf`<br>`D:/Case Flow/EnviroChemie_BDD_Intelligence_2026-09-26_V1.1.1.pdf` |
| 第一页对比截图（4 张） | `D:/Case Flow/_v111-comparison/` |
| V1.1 全量备份（可回退） | `D:/Case Flow/_bdd-skill-archive/V1.1-backup-20260926/` |

**V1.1 原版产物保留未动**（`*_BDD_Intelligence_2026-09-26.md/.pdf`），供对照。

---

## 六、待确认（不阻塞）

| # | 待确认 | 归属 |
|---|---|---|
| 1 | 四组阅读顺序（WHO → WHY → WHERE/WHO → ACTION）是否符合业务员翻查习惯 | 销售 |
| 2 | `Current Treatment` 四态徽标是否需要加中文（已确认 / 部分 / 规划中 / 未知） | 销售 |
| 3 | 结论卡视觉权重是否足够（当前为深色边框 + 12pt 取值） | 销售 |
| 4 | 是否需要对既有 5 家卡（Chemstock / Hikal / Aarti）也重排一次 | 业务方 |

---

*本 Patch 为展示层变更。判断规则、字段语义、Evidence 政策均保持 V1.1 原样。*
