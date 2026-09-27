# Output Visual Rules · 颜色语义与 PDF 导出（V1.1 / V1.1.1）

**回答的问题**：情报卡怎么呈现，业务员能 30 秒读懂；存档版 PDF 长什么样。

> **V1.1.1 Presentation Patch**：本文件新增第二部分「展示层（Presentation Layer）」。
> 该部分**只定义展示**：显示标签、分组、状态徽标、结论卡样式。
> **不修改任何判断规则**，不新增字段，不新增评分。
> Internal Key 与全部判断逻辑保持 V1.1 原样。

---

## 第一部分 · 固定颜色语义

### 一、五色定义（**唯一来源，不得扩展**）

| 颜色 | 语义 | 用于 | 标记 |
|---|---|---|---|
| 🟢 **绿** | Confirmed / Positive / High relevance | 已确认的事实 · 高相关性 · 无风险的正面结论 | `🟢` |
| 🟡 **黄** | Potential / Needs validation | 待验证 · 潜力型 · 需先补信息 | `🟡` |
| 🔴 **红** | Risk / Negative / Conflict | 风险 · 负面 · 冲突（含潜在竞争） | `🔴` |
| ⚪ **灰** | Unknown | 未查到 / 无法判断 | `⚪` |
| 🔵 **蓝** | Neutral facts | 中性事实（描述性、不表态） | `🔵` |

### 二、字段 → 颜色映射

| 字段 | 取值 → 颜色 |
|---|---|
| **Customer Type** | End-user / Partner → 🔵；`Unconfirmed` → ⚪ |
| **Industry Match** | `Target` → 🟢；`Adjacent` → 🔵；`Outside` → 🔴；`Unknown` → ⚪ |
| **Current Wastewater Treatment / Technology** | **状态徽标（V1.1.1 四态）**：`Confirmed` → 🟢；`Partial` → 🟡；`Planned` → 🔵；`Unknown` → ⚪<br>**正文技术组合**：中性描述 → 🔵（与徽标解耦） |
| **BDD Opportunity**（四档） | `High` → 🟢；`Medium` → 🟡；`Low` → 🔴；`Unknown` → ⚪ |
| **BDD Opportunity**（Opportunity Type） | 有明确类型 → 🔵；`Unknown` → ⚪；含 `Conflict` → 🔴 |
| **Demand Status** | `Confirmed` / `Strong Signal` → 🟢；`Potential` → 🟡；`Weak` → 🔴；`Unknown` → ⚪ |
| **Commercial Risk** | `Low` → 🟢；`Medium` → 🟡；`High` → 🔴；`Unknown` → ⚪ |
| **Financial Warning** | `No` → 🟢；`Unknown` → ⚪；`Yes` → 🔴（**不设黄色档**） |
| **Priority Site** | 有 → 🟢；`N/A` → ⚪ |
| **What Is Missing** | 按级：Business → 🔴；Project → 🟡；Technical → 🔵 |
| **Who to Contact** | `No verified contact found` → ⚪；有具名 → 🟢 |
| **Sales Conclusion** | 建议重点开发 / 建议开发 → 🟢；建议先验证 → 🟡；暂不优先 → 🔴；信息不足 → ⚪ |
| **Evidence 类型** | FACT → 🔵；INFERENCE → 🟡；UNKNOWN → ⚪ |

### 三、硬规则

| # | 规则 |
|---|---|
| 1 | **禁止 100 分制、AI 评分、星级、加权总分。** 颜色只表达**类别语义**，不表达程度。 |
| 2 | **禁止渐变、阴影、拟物化。** 只用纯色块 + 文字标签。 |
| 3 | **颜色不是唯一信息载体。** 每个色块必须同时带文字（如 `🟢 High`），保证打印 / 色盲可读。 |
| 4 | **不得为"看起来更好"而改色。** 颜色由字段取值机械映射，不人工调整。 |
| 5 | 同一取值在所有公司卡上颜色必须一致——**保证横向可比**。 |

---

## 第二部分 · 展示层 Presentation Layer（V1.1.1 新增）

> **范围声明**：本部分只规定**怎么显示**。
> **13 个 Internal Key 完全不变**，判断结论一字不改。展示层**不得**产生任何新的判断结果。

### 一、Display Label 映射（**Internal Key 不变，仅新增显示标签**）

| # | Internal Key（**保持不变，勿改**） | Display Label（新增显示） | 所属组 |
|---|---|---|---|
| 1 | `Company` | **公司 Company** | WHO |
| 2 | `Country` | **国家 Country** | WHO |
| 3 | `What They Do` | **主营业务 Business** | WHO |
| 4 | `Customer Type` | **客户类型 Customer Type** | WHO |
| 5 | `Industry Match` | **行业匹配 Industry Match** | WHY |
| 6 | `BDD Opportunity` | **BDD机会 BDD Opportunity** | WHY |
| 7 | `Demand Status` | **需求状态 Demand Status** | WHY |
| 8 | `Current Wastewater Treatment / Technology` | **现有废水处理 Current Treatment** | WHERE / WHO |
| 9 | `Priority Site` | **优先厂区 Priority Site** | WHERE / WHO |
| 10 | `Who to Contact` | **关键联系人 Contact** | WHERE / WHO |
| 11 | `What Is Missing` | **待确认信息 Missing Info** | ACTION |
| 12 | `Next Action` | **下一步 Next Action** | ACTION |
| 13 | `Sales Conclusion` | **开发建议 Sales Conclusion** | ACTION（**结论卡**） |

**硬规则**

| # | 规则 |
|---|---|
| 1 | Display Label 只用于**显示**。脚本校验、字段引用、规则判据一律使用 Internal Key。 |
| 2 | **不得**因改显示名而改变字段语义、取值范围或判定逻辑。 |
| 3 | Display Label 为**固定字符串**，不得自由改写或增删中英文部分。 |
| 4 | 渲染脚本通过**别名表**把 Display Label 映射回 Internal Key；映射失败 → 按原文处理，不报错。 |

### 二、第一页四组分组（WHO → WHY → WHERE/WHO → ACTION）

主卡 13 字段按**决策阅读顺序**分四组。分组只改**呈现顺序与标题**，不改字段内容。

| 组 | 标题 | 回答 | 含字段 |
|---|---|---|---|
| **WHO** | `WHO · 客户是谁` | 这家公司是什么？ | 公司 / 国家 / 主营业务 / 客户类型 |
| **WHY** | `WHY · 为什么值得看` | 有没有机会？需求多强？ | 行业匹配 / BDD机会 / 需求状态 |
| **WHERE / WHO** | `WHERE / WHO · 从哪里切入` | 从哪个厂区、找谁？ | 现有废水处理 / 优先厂区 / 关键联系人 |
| **ACTION** | `ACTION · 现在怎么办` | 缺什么、下一步、值不值得投入？ | 待确认信息 / 下一步 / **开发建议（结论卡）** |

**硬规则**

| # | 规则 |
|---|---|
| 1 | 四组顺序固定，**不得调换**（阅读链路：认识 → 判断 → 切入 → 行动）。 |
| 2 | 分组**不改变字段归属语义**，也不表示字段间存在推导关系。 |
| 3 | **13 个字段一个都不能少**，也不得出现第 14 个字段。 |
| 4 | 三个固定小块（BDD Opportunity 判定依据 / Demand Status 明细 / 风险）**不属四组**，仍按原位置展示。 |

### 三、`Current Treatment` 显示状态（四态）

**状态只能来自现有证据，不得推断。**

| 显示状态 | 判据（**必须由一个具体 E# 支撑**） | 颜色 |
|---|---|---|
| `Confirmed` | 证据明确载明**已建成 / 在运行 / 在售交付**的处理单元或工艺组合 | 🟢 |
| `Partial` | 证据只覆盖**部分环节**：仅载明单个单元、工艺组合不完整，或原文本身含"部分厂区 / 部分工艺"限定 | 🟡 |
| `Planned` | 证据明确表述为**规划 / 拟建 / 在建**，尚未投运 | 🔵 |
| `Unknown` | 无任何相关证据（**不得据"这类厂应该有"填**） | ⚪ |

**显示格式**

```
🟢 Confirmed · {技术组合原文}
```

**硬规则**

| # | 规则 |
|---|---|
| 1 | 状态**必须有 E# 支撑**；无 E# → `Unknown`。 |
| 2 | 证据表述为计划 / 拟建 / 在建 → **只能** `Planned`，**不得**写 `Confirmed`。 |
| 3 | 覆盖不完整 → `Partial`，**不得**升为 `Confirmed`。 |
| 4 | **状态与 `BDD Opportunity` 不联动**：既有 ETP / ZLD ≠ 无机会；规划中 ≠ `High`。 |
| 5 | 状态**不参与任何判断字段**，仅为展示。判定依据仍在 `Current Wastewater Treatment / Technology` 字段本身。 |
| 6 | Partner Path 下，状态描述的是"**可提供 / 在交付**的技术组合"，不适用"自身废水"口径。 |

### 四、`Sales Conclusion` 结论卡（第一页最醒目）

`Sales Conclusion` **从主卡表格中移出**，渲染为第一页（Page 1）的独立结论卡，置于四组之后。

```
┌────────────────────────────────────────────┐
│  开发建议 SALES CONCLUSION                 │
│                                            │
│  🟢 建议开发                                │
│  主体级证据充分（…），属目标市场，无财务警示；  │
│  尚无具体项目文件级证据，故未达"重点开发"      │
└────────────────────────────────────────────┘
```

**硬规则**

| # | 规则 |
|---|---|
| 1 | 结论**取值与原因文字一字不改**，只改变位置与视觉权重。 |
| 2 | 五色语义沿用第一部分映射；**不得**为醒目而改色。 |
| 3 | 结论卡**不得**新增建议、行动项、评分或后续话术。 |
| 4 | 结论卡必须在 Page 1 内，**不得**被挤到第 2 页。 |
| 5 | Markdown 源中该字段仍属主卡 13 字段之一，校验照常计入。 |

### 五、展示层边界（**不得越界**）

| # | 禁止 |
|---|---|
| 1 | 修改任何判断规则（Evidence Policy / Customer Path / Industry Map / BDD Opportunity / Demand Status / Commercial Risk / Opportunity Type / Priority Site） |
| 2 | 新增字段、新增 Skill、新增评分、新增 CRM 功能 |
| 3 | 因"更好看"调整任何取值、颜色或结论 |
| 4 | 在渲染层推断、补全、润色任何内容 |
| 5 | 改动 Markdown 的**完整 Evidence 结构**（附录 A 原样保留） |

---

## 第三部分 · 交付文件命名

```
{Company}_BDD_Intelligence_{YYYY-MM-DD}.md
{Company}_BDD_Intelligence_{YYYY-MM-DD}.pdf
```

| 项 | 规则 |
|---|---|
| `{Company}` | 主体简称，**不含空格与特殊字符**（如 `Chemstock` / `Hikal` / `AartiIndustries` / `Umicore` / `EnviroChemie`） |
| `{YYYY-MM-DD}` | 生成日期 |
| 存放位置 | 工作区根目录（`D:/Case Flow/`） |

---

## 第四部分 · PDF 三页模板（业务员版）

**Markdown 保留完整 Evidence；PDF 为业务员版本，建议约 3 页。**

### Page 1 · Customer Snapshot（客户快照）

内容：**主判断卡全部 13 字段**（原样搬运，不改写结论），按四组呈现，末尾为结论卡。

```
┌─ Page 1 · Customer Snapshot ─────────────────────────────┐
│  {Company} · {Country}                                   │
│  {日期} | 来源：{输入形式}                                │
│                                                          │
│  WHO · 客户是谁                                           │
│    公司 Company              {全称}（{国家}）· {核实三态}  │
│    国家 Country              {国家 · 主要运营地区}          │
│    主营业务 Business         {一句话}                      │
│    客户类型 Customer Type    {类型} · {Path}               │
│                                                          │
│  WHY · 为什么值得看                                       │
│    行业匹配 Industry Match   🔵 Adjacent                  │
│    BDD机会 BDD Opportunity   🟢 High · {Opportunity Type} │
│    需求状态 Demand Status    🟡 Potential                 │
│                                                          │
│  WHERE / WHO · 从哪里切入                                 │
│    现有废水处理 Current       🟢 Confirmed · {技术组合}     │
│      Treatment                                            │
│    优先厂区 Priority Site    {厂区} / N/A                  │
│    关键联系人 Contact        {岗位}（+ 具名）               │
│                                                          │
│  ACTION · 现在怎么办                                      │
│    待确认信息 Missing Info   [Business] … [Project] …     │
│    下一步 Next Action        {一句话}                      │
│                                                          │
│  ╔══════════════════════════════════════════════════════╗ │
│  ║ 开发建议 SALES CONCLUSION                            ║ │
│  ║ 🟡 建议先验证                                         ║ │
│  ║ {1~2 句原因}                                          ║ │
│  ╚══════════════════════════════════════════════════════╝ │
└──────────────────────────────────────────────────────────┘
```

**限制**：**1 页内**。超页则压缩 `Business` 与 `Current Treatment` 的描述长度，**不得删字段、不得删结论卡、不得把结论卡移到第 2 页**。

> 三个固定小块（`BDD Opportunity 判定依据` / `Demand Status 明细` / `风险`）**不放在 Page 1**，归入 Page 2。

### Page 2 · Why This Customer（为什么是这个客户）

内容：

| 段 | 内容 |
|---|---|
| ① 判断依据 | `BDD Opportunity` 的 Reason / Evidence / Confidence / Opportunity Type |
| ② 两类废水证据 | PWE 与 CSD 分别列示，各附等级与来源 |
| ③ 现有处理 / 技术组合 | `Current Wastewater Treatment / Technology` 全文 |
| ④ 优先厂区 | `Priority Site` 的 Why + Evidence（不适用则说明原因） |
| ⑤ 风险与财务警示 | `Commercial Risk` + `Risk Note` + `Financial Warning` |
| ⑥ 结论逻辑 | Sales Conclusion 的规则路径（用了哪几条判据） |

**限制**：**1 页内**。无 `Priority Site` 时该段压缩为一行。

### Page 3 · Key Evidence（关键证据）

内容：**只列 `Decision Impact = High` 的 Evidence**；若不足 5 条，补 `Medium` 至 5~8 条。

```
| # | 类型 | 结论 | Source | Confidence | Impact |
```

末尾附：
- **可溯源率**：{已标注 Source 的 FACT 数} / {FACT 总数}
- **UNKNOWN 汇总**（含三态），一行一条
- **边界声明**：本卡不输出技术方案 / 设备选型 / 工艺参数 / 达标承诺 / 金额 / 报价状态

**限制**：**1 页内**。超出则只保留 `Impact = High`。

---

## 第五部分 · 渲染管线与隔离要求

### 一、管线

```
Markdown（唯一判断产出）
    │
    ▼  纯格式转换（无判断）
HTML（内联 CSS，五色语义）
    │
    ▼  Chrome headless --print-to-pdf
PDF（业务员版）
```

**工具**：`scripts/render_pdf.py`

### 二、渲染层隔离（**硬要求**）

> **PDF 渲染层不得反向影响 Customer Intelligence 判断逻辑。**

| # | 规则 |
|---|---|
| 1 | 渲染脚本**只做格式转换**：解析 Markdown → 输出 HTML → 打印 PDF。**不得新增、推断、改写、润色任何结论。** |
| 2 | **不得在渲染层做判断**：不重新计算等级、不推断缺失字段、不补全 `Unknown`。 |
| 3 | **一致性校验**：渲染前必须校验 Markdown 主卡 **13 字段齐全**；缺任一字段 → **报错退出，不生成 PDF**。 |
| 4 | **颜色映射在渲染层实现**，但映射表**来源于本文件**（单一事实来源），脚本内只做查表。 |
| 5 | 渲染失败时**保留 Markdown**，并明确报错；**不得用简化版 PDF 替代**。 |
| 6 | **Markdown 为权威版本。** 两者冲突时以 Markdown 为准。 |

### 三、Page 切分实现

用 CSS 分页强制切页：

```css
.page { page-break-after: always; }
.page:last-child { page-break-after: auto; }
```

Markdown 中不写分页标记；由渲染脚本按 `## Page N` 标题识别并切页（**版式规则，非内容规则**）。

### 四、V1.1.1 排版修复（**纯格式，不改内容**）

| # | 缺陷 | 修复 |
|---|---|---|
| 1 | 主卡值中显式书写的 `<br>` 被转义为字面文本 `&lt;br&gt;` | `inline()` 将 `&lt;br&gt;` 还原为 `<br/>`，正常换行 |
| 2 | 值中含转义竖线 `\|`（复合机会类型 `+\|`）时表格被误拆成两列 | `split_row()` 先保护 `\|` 再按 `|` 拆分，单元格不裂开 |

> 两项均为**排版修复**：单元格文本逐字不变，仅纠正 HTML 结构与列数。
> 修复后必须复核 **PDF 仍为 3 页**（`<br>` 生效会增高内容）。

---

## 第六部分 · 与其他文件的职责边界

| 文件 | 负责 |
|---|---|
| **本文件** | 颜色语义（唯一来源）+ 命名规范 + PDF 三页模板 + 渲染隔离要求 |
| `assets/output-card-template.md` | Markdown 输出模板（主卡 13 字段 + 附录 A） |
| `sales-conclusion-rules.md` | Sales Conclusion 的**取值**（本文件只负责它的颜色） |
| `evidence-policy.md` | Evidence 类型与 Decision Impact 的定义 |
| `scripts/render_pdf.py` | 本文件的**实现**，不含判断逻辑 |

---

## 第七部分 · 待业务方确认

| # | 待确认 | 归属 |
|---|---|---|
| 1 | 五色语义是否与内部习惯一致（尤其红色用于"冲突"） | 销售 |
| 2 | PDF 三页的字段取舍是否符合业务员阅读习惯 | 销售 |
| 3 | 是否需要中文 / 英文双语输出 | 销售 |
| 4 | 是否需要在 PDF 页脚加公司标识与免责声明 | 公司 |
| 5 | **V1.1.1 四组阅读顺序（WHO → WHY → WHERE/WHO → ACTION）是否符合业务员实际翻查习惯** | 销售 |
| 6 | **`Current Treatment` 四态徽标是否需要加中文（已确认 / 部分 / 规划中 / 未知）** | 销售 |
