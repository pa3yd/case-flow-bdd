# Output Visual Rules · 颜色语义与 PDF 导出（V1.1 新增）

**回答的问题**：情报卡怎么呈现，业务员能 30 秒读懂；存档版 PDF 长什么样。

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
| **Current Wastewater Treatment / Technology** | 已确证 → 🔵；`Unknown` → ⚪ |
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

## 第二部分 · 交付文件命名

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

## 第三部分 · PDF 三页模板（业务员版）

**Markdown 保留完整 Evidence；PDF 为业务员版本，建议约 3 页。**

### Page 1 · Customer Snapshot（客户快照）

内容：**主判断卡全部 13 字段**（原样搬运，不改写结论）。

```
┌─ Page 1 · Customer Snapshot ─────────────────────┐
│  {Company} · {Country}                           │
│  {日期} | 来源：{输入形式}                        │
│                                                  │
│  What They Do          一句话                      │
│  Customer Type         {类型} · {Path}            │
│  Industry Match        🟢 Target                  │
│  Current Treatment     现有方案 / 技术组合          │
│  BDD Opportunity       🟡 Medium                  │
│                        · EPC / Integration Opp.   │
│  Demand Status         🟡 Potential               │
│                        · PWE: {等级}               │
│                        · CSD: {等级}               │
│  Priority Site         {厂区} / N/A                │
│  Commercial Risk       ⚪ Unknown                 │
│  Financial Warning     🟢 No                      │
│  What Is Missing       [Business] … [Project] …   │
│  Who to Contact        {岗位}                      │
│  Next Action           一句话                      │
│  Sales Conclusion      🟡 建议先验证                │
│                        {1~2 句原因}               │
└──────────────────────────────────────────────────┘
```

**限制**：**1 页内**。超页则压缩 `What They Do` 与 `Current Treatment` 的描述长度，**不得删字段、不得删 Sales Conclusion**。

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

## 第四部分 · 渲染管线与隔离要求

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

---

## 第五部分 · 与其他文件的职责边界

| 文件 | 负责 |
|---|---|
| **本文件** | 颜色语义（唯一来源）+ 命名规范 + PDF 三页模板 + 渲染隔离要求 |
| `assets/output-card-template.md` | Markdown 输出模板（主卡 13 字段 + 附录 A） |
| `sales-conclusion-rules.md` | Sales Conclusion 的**取值**（本文件只负责它的颜色） |
| `evidence-policy.md` | Evidence 类型与 Decision Impact 的定义 |
| `scripts/render_pdf.py` | 本文件的**实现**，不含判断逻辑 |

---

## 第六部分 · 待业务方确认

| # | 待确认 | 归属 |
|---|---|---|
| 1 | 五色语义是否与内部习惯一致（尤其红色用于"冲突"） | 销售 |
| 2 | PDF 三页的字段取舍是否符合业务员阅读习惯 | 销售 |
| 3 | 是否需要中文 / 英文双语输出 | 销售 |
| 4 | 是否需要在 PDF 页脚加公司标识与免责声明 | 公司 |
