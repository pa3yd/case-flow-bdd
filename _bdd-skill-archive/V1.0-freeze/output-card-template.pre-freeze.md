# 判断卡输出模板（两层结构）

## 结构总览

| 层 | 内容 | 长度上限 |
|---|---|---|
| **第一层** | 主判断卡（10 固定字段） | **1 屏（约 20 行）** |
| **第二层** | 附录：Evidence 明细 + 回复草稿 + 推进节奏 | 不限，折叠 |

主卡**不放** Evidence / Source / Confidence / Fact·Inference·Unknown。那些全部在附录。

---

## 第一层 · 主判断卡

```markdown
# 询盘判断卡 · {公司名}
{日期} | 来源：{询盘来源}

| 字段 | 判定 |
|---|---|
| Company | {公司全称}（{地区}） |
| Customer Type | {终端业主 / 环保工程公司 / 设计院 / 科研院所高校 / 贸易商中间商 / Unconfirmed} |
| Industry Fit | {Target / Adjacent / Outside / Unknown} |
| Demand Evidence | {Confirmed / Strong Signal / Potential / Weak / Unknown} |
| BDD Opportunity | {High / Medium / Low / Unknown} |
| Technical Fit | {Sufficient — Likely Suitable / Sufficient — Likely Unsuitable / Insufficient Data / Engineer Review Required} |
| Commercial Risk | {Low / Medium / High / Unknown} |
| Missing Critical Data | {①{项} ②{项} ③{项} / None} |
| Quotation Readiness | {Ready for quotation / Not ready / Need technical data / Engineer review}{（Manual override：{理由}）} |
| Recommended Contact Role | {岗位角色} {/ No verified contact found} |
| Next Action | {一句话，含"建议小试"或具体推进动作} |
```

### 字段填写规则

| 字段 | 规则 |
|---|---|
| **Company** | 用工商全称；查不到全称时用客户自述名称并标 `（客户自述）` |
| **Customer Type** | 判据必须来自 Evidence；不足时 `Unconfirmed`，**不得猜** |
| **Industry Fit** | 对照 `bdd-fit-rules.md`；行业不在已定义清单 → `Unknown` |
| **Demand Evidence** | 只依据 Evidence。**不得因行业对口就升为 Confirmed / Strong Signal** |
| **BDD Opportunity** | 在 Industry Fit 与 Demand Evidence 都判定后才判。**不得因 Opportunity 高就把 Technical Fit 拉高** |
| **Technical Fit** | 数据不足必须 `Insufficient Data`，**禁止用行业经验值代替** |
| **Commercial Risk** | 只用语询盘当时可观察的事实。**禁止用"是否成交"** |
| **Missing Critical Data** | 最多 5 项，只列**能推进决策**的。齐全写 `None` |
| **Quotation Readiness** | 只输出状态，**不输出金额**。`Need technical data` 由 Technical Fit 自动串联 |
| **Recommended Contact Role** | 只输出**岗位角色**。查到真人可附 `Name + Position + Source`；查不到写 `No verified contact found` |
| **Next Action** | 一句话。必须与决策链末端一致 |

### 留白规则（重要）

**`Unknown` 的字段直接留 `Unknown`，不要为了填满模板而写内容。**

| 错误做法 | 正确做法 |
|---|---|
| 查不到参保人数 → 写"估计 100 人左右" | 留 `Unknown` |
| 无水质数据 → 写"预计 COD 1500 左右" | `Technical Fit: Insufficient Data` |
| 无公开线索 → 写"可能正在规划环保改造" | `Demand Evidence: Unknown` |
| 找不到联系人 → 写一个推测姓名 | `No verified contact found` |

---

## 第二层 · 附录（折叠区）

```markdown
---
<details>
<summary>附录 A · Evidence 明细</summary>

| # | 类型 | 结论 | Source | Reason | Confidence |
|---|---|---|---|---|---|
| 1 | FACT | {内容} | {URL / 客户自述} | — | High |
| 2 | INFERENCE | {内容} | — | {推断理由} | Medium |
| 3 | UNKNOWN | {未查到的项} | — | — | — |

**类型定义**：FACT 必须有 Source；INFERENCE 必须有 Reason + Confidence；UNKNOWN 不得补全。

**可溯源率**：{已标注 Source 的 FACT 数} / {FACT 总数}

</details>

<details>
<summary>附录 B · 回复草稿（{中文/英文}）</summary>

{按 reply-playbook.md 对应场景生成，中文 150~250 字 / 英文 80~150 词}

</details>

<details>
<summary>附录 C · 推进节奏</summary>

| 时间 | 动作 |
|---|---|
| Day 0 | {回复 + 追问 X 项} |
| Day 2 | {未回复则换渠道} |
| Day 5 | {提供新价值，不催单} |
| Day 10 | {推进寄样小试} |

</details>
```

---

## 禁止项

| 禁止 | 原因 |
|---|---|
| 输出具体工艺参数（电流密度、能耗、停留时间） | 核心壁垒 + 属工程师职责 |
| 做设备选型 | 安全边界 |
| 承诺达标 / 承诺通过验收 | 法律责任 |
| 输出具体金额（含区间） | 时效敏感 + 属商务决策 |
| 提供客户案例名单与联系方式 | 公司资产 |
| 生成未经公开来源验证的具体人名/电话/邮箱 | 合规风险 |
| 主卡出现 Evidence / Confidence 明细 | 破坏 1 屏约束 |
| 用 `Unknown` 字段的推测内容填满模板 | 制造虚假完整度 |
| 把 FACT 与 INFERENCE 混在同一格 | 幻觉主要来源 |

---

## 长度控制

| 段 | 上限 |
|---|---|
| 主卡表格 | 11 行（含表头） |
| Missing Critical Data | 5 项 |
| 附录 A Evidence | 不限，但每行必须完整 |
| 回复草稿 | 中文 250 字 / 英文 150 词 |
| **主卡总计** | **1 屏** |

超出则精简附录，**不精简主卡**。

---

## 分级输出（按信息量自动调整）

| 用户提供了什么 | 输出什么 |
|---|---|
| 完整询盘原文 + 公司名 | 完整两层结构 |
| 只有公司名 / 联系方式 | 主卡 + 附录 A；`Next Action` 指向获取联系方式或询盘信息 |
| 只有询盘原文，无公司名 | 主卡（`Company` 标客户自述）+ 附录 A 标注"需公司名方可检索" |
| 信息极少 | 主卡如实填 `Unknown` / `Insufficient Data`，不硬凑分析 |

---

## 填写示例（说明留白风格）

```markdown
| Company | 湖南某某化工有限公司（客户自述） |
| Customer Type | 终端业主（判据：参保 320 人 / 有实体厂 / 谈"我们的废水"） |
| Industry Fit | Target |
| Demand Evidence | Strong Signal |
| BDD Opportunity | Medium |
| Technical Fit | Insufficient Data |
| Commercial Risk | Low |
| Missing Critical Data | ①进水 COD ②处理水量 m³/d ③盐度 / 氯离子 |
| Quotation Readiness | Need technical data |
| Recommended Contact Role | 环保负责人 / 技术总工（No verified contact found） |
| Next Action | 索要 ①②③ 三项数据并邀请寄 5~10 L 水样做免费小试 |
```

注意：`Technical Fit` 与 `Quotation Readiness` 在此联动——数据不足直接串联到 `Need technical data`，不需要单独推理。
