# 客户情报卡输出模板（两层结构 · V1 冻结）

## 结构总览

| 层 | 内容 | 长度上限 |
|---|---|---|
| **第一层** | 主判断卡（10 固定字段） | **1 屏** |
| **第二层** | 附录 A · Evidence 明细 | 不限，折叠 |

主卡**不放** Evidence 明细。那些全部在附录 A。

**V1 冻结变化**：附录 B（回复草稿）与附录 C（推进节奏）已移出 → 归档至 `_bdd-skill-archive/V1.0-freeze/output-card-template.appendix-B-C.md`。

---

## 第一层 · 主判断卡

```markdown
# 客户情报卡 · {公司名}
{日期} | 来源：{询盘来源}

| 字段 | 判定 |
|---|---|
| Company | {工商全称}（{地区}）· {Verified / Partially Verified / Unverified} |
| Company Profile | {成立时间} / {参保人数} / {主营} / {是否实体工厂} |
| Customer Type | {终端业主 / 环保工程公司 / 设计院 / 科研院所高校 / 贸易商中间商 / Unconfirmed} |
| Industry Fit | {Target / Adjacent / Outside / Unknown} |
| BDD Relevance | {High / Medium / Low / Unknown} |
| Demand Evidence | {Confirmed / Strong Signal / Potential / Weak / Unknown} |
| Commercial Risk | {Low / Medium / High / Unknown} |
| Missing Critical Data | {①{项} ②{项} ③{项} / None} |
| Recommended Contact Role | {岗位角色} + {接触策略一句话} {/ No verified contact found} |
| Next Action | {一句话，含"建议小试"或具体推进动作} |

**BDD Relevance 判定依据**

- Reason: {为什么是这个等级}
- Evidence: {证据编号，指向附录 A，如 E1 / E4 / E7}
- Confidence: {High / Medium / Low}
```

> **注意**：`BDD Relevance` 是唯一在主卡内必须展开依据的字段——因其 8 项输入的判定最容易失真。

---

### 字段填写规则

| 字段 | 规则 |
|---|---|
| **Company** | 用工商全称 + **核实状态三态**。名称有歧义 → `Unverified`，**不得选最像的一家** |
| **Company Profile** | 成立时间 / 参保人数 / 主营 / 是否实体工厂四项必填；**查不到写 `Unknown`**，不得写"估计""约""大概" |
| **Customer Type** | 判据必须来自 Evidence；不足时 `Unconfirmed`，**不得猜** |
| **Industry Fit** | 对照 `bdd-fit-rules.md`；行业不在已定义清单 → `Unknown` |
| **BDD Relevance** | 综合 8 项输入（见 SKILL.md 第四节）。**Industry Fit 只是其中之一，不得直接换算**。必须附 Reason + Evidence + Confidence |
| **Demand Evidence** | 只依据 Evidence。**不得因行业对口或 BDD Relevance 高就升为 Confirmed / Strong Signal** |
| **Commercial Risk** | 只用询盘当时可观察的事实。**禁止用"是否成交"** |
| **Missing Critical Data** | 最多 5 项，只列**能推进决策**的。齐全写 `None`。**只回答"该要什么"，不回答"能不能报价"** |
| **Recommended Contact Role** | 只输出**岗位角色** + 一句接触策略。查到真人可附 `Name + Position + Source`；查不到写 `No verified contact found` |
| **Next Action** | 一句话。必须与决策链末端一致 |

---

### BDD Relevance 填写对照（最易出错的字段）

| 情况 | 错误写法 | 正确写法 |
|---|---|---|
| 行业对口 + 无废水信号 + 无环境证据 | `BDD Relevance: High` | `BDD Relevance: Medium`（`Reason`：行业对口且已确认制造业活动，但无废水与环境证据） |
| 行业对口 + 未确认是否有生产活动 | `BDD Relevance: High` | `BDD Relevance: Unknown`（`Reason`：无法确认该主体是否有实际生产活动） |
| 行业对口 + 明确废水已委托第三方且无改造迹象 | `BDD Relevance: Medium` | `BDD Relevance: Low` |
| 行业 `Unknown` | 跳过 BDD Relevance | 仍须输出：`BDD Relevance: Unknown`（不要为空） |

---

### 留白规则（重要）

**`Unknown` 的字段直接留 `Unknown`，不要为了填满模板而写内容。**

| 错误做法 | 正确做法 |
|---|---|
| 查不到参保人数 → 写"估计 100 人左右" | `Unknown` |
| 查不到主体 → 选一家名称最像的 | `Unverified` + 列入 Missing Critical Data |
| 无公开线索 → 写"可能正在规划环保改造" | `Demand Evidence: Unknown` |
| 找不到联系人 → 写一个推测姓名 | `No verified contact found` |
| 行业对口 → 直接给 BDD Relevance High | 按 8 项输入逐项对照 |

---

## 第二层 · 附录 A（折叠区）

```markdown
---
<details>
<summary>附录 A · Evidence 明细</summary>

| # | 类型 | 结论 | Source | Reason | Confidence |
|---|---|---|---|---|---|
| E1 | FACT | {内容} | {URL / 客户自述} | — | High |
| E2 | INFERENCE | {内容} | — | {推断理由} | Medium |
| E3 | UNKNOWN | {未查到的项} | — | — | — |

**类型定义**：FACT 必须有 Source；INFERENCE 必须有 Reason + Confidence；UNKNOWN 不得补全。

**可溯源率**：{已标注 Source 的 FACT 数} / {FACT 总数}　目标 100%

</details>
```

**编号规则**：`E1`、`E2`… 顺序编号。主卡 `BDD Relevance` 的 `Evidence` 字段引用这些编号。

---

## 禁止项

| 禁止 | 原因 |
|---|---|
| 输出具体工艺参数（电流密度、能耗、停留时间） | 核心壁垒 + 属工程师职责 |
| 做设备选型 / 出技术方案 | 安全边界 |
| 承诺达标 / 承诺通过验收 | 法律责任 |
| 输出具体金额（含区间） | 时效敏感 + 属商务决策 |
| 输出 Technical Fit / Quotation Readiness | **V1 已移出职责范围** |
| 输出回复草稿 / 跟进节奏 | **V1 已移出职责范围** |
| 提供客户案例名单与联系方式 | 公司资产 |
| 生成未经公开来源验证的具体人名/电话/邮箱 | 合规风险 |
| 主卡出现 Evidence 明细 | 破坏 1 屏约束 |
| 用 `Unknown` 字段的推测内容填满模板 | 制造虚假完整度 |
| 把 FACT 与 INFERENCE 混在同一格 | 幻觉主要来源 |
| 因 Industry Fit = High 直接给 BDD Relevance = High | 本 V1 最重要的一条禁止 |
| `BDD Relevance` 缺 Reason / Evidence / Confidence | 判定视为无效 |

---

## 长度控制

| 段 | 上限 |
|---|---|
| 主卡表格 | 11 行（含表头） |
| BDD Relevance 判定依据 | 3 行（Reason / Evidence / Confidence） |
| Missing Critical Data | 5 项 |
| 附录 A Evidence | 不限，但每行必须完整 |
| **主卡总计** | **1 屏** |

超出则精简附录，**不精简主卡**。

---

## 分级输出（按信息量自动调整）

| 用户提供了什么 | 输出什么 |
|---|---|
| 完整询盘原文 + 公司名 | 完整两层结构 |
| 只有公司名 / 联系方式 | 主卡 + 附录 A；`Next Action` 指向获取询盘信息 |
| 只有询盘原文，无公司名 | 主卡（`Company` 标客户自述 + `Unverified`）+ 附录 A 标注"需公司名方可检索" |
| 信息极少 | 主卡如实填 `Unknown` / `Unverified`，不硬凑分析 |

---

## 填写示例（说明留白风格）

```markdown
# 客户情报卡 · 山西某某焦化有限公司
2026-09-26 | 来源：官网表单

| 字段 | 判定 |
|---|---|
| Company | 山西某某焦化有限公司（山西）· Partially Verified |
| Company Profile | 2011 年成立 / 参保 260 人 / 焦炭生产与销售 / 有实体工厂 |
| Customer Type | 终端业主（判据：有厂址 + 谈"我们污水站"） |
| Industry Fit | Unknown（目标市场清单待填） |
| BDD Relevance | Medium |
| Demand Evidence | Strong Signal |
| Commercial Risk | Medium |
| Missing Critical Data | ①进水 COD ②处理水量 m³/d ③盐度 / 氯离子 ④目标限值 |
| Recommended Contact Role | 环保负责人 / 技术总工（No verified contact found）+ 强需求中风险，走保密流程后推进寄样 |
| Next Action | 索要 ①②③④ 四项并邀请寄 5~10 L 水样做免费小试 |

**BDD Relevance 判定依据**

- Reason: 焦化属涉水行业且已确认制造业活动与实体工厂，但未查到环保处罚与环评公示，无环境证据
- Evidence: E2（参保 260 人）、E6（客户自述污水站改造需求）
- Confidence: Medium
```

> `Industry Fit` 输出 `Unknown`——目标行业清单尚未填写，Skill 不自行推断。
> `BDD Relevance` 输出 `Medium` 而非 `High`——虽行业对口且确认制造业活动，但**缺环境证据**，按硬规则 5 封顶 `Medium`。
