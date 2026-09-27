# 客户情报卡输出模板（V1.1）

## 结构总览

| 层 | 内容 | 长度上限 | 写给谁 |
|---|---|---|---|
| **第一层** | 主判断卡（**13 固定字段**） | **1 页** | 业务员（30 秒读懂） |
| **第二层** | 附录 A · Evidence 明细 | 不限，折叠 | 复核者 / 存档 |

> **V1.1 设计原则**：**主卡用大白话，专业规则放后层。**
> 主卡不出现"8 项输入""封顶规则"这类内部术语；它们全部在附录与参考文件中。

**颜色语义见 `references/output-visual-rules.md`（唯一来源）。**

---

## 第一层 · 主判断卡（13 字段）

```markdown
# {Company} · BDD Customer Intelligence

{YYYY-MM-DD} | 来源：{输入形式：询盘原文 / 公司名 / 官网 / 名片}
执行版本：BDD Customer Intelligence Skill V1.1

## 第一层 · 主判断卡

| 字段 | 判定 |
|---|---|
| **Company** | {登记全称}（{国家 / 地区}）· {Verified / Partially Verified / Unverified} |
| **Country** | {国家} · {主要运营地区} |
| **What They Do** | {一句话：这家公司是做什么的，用业务员能转述的话} |
| **Customer Type** | {类型} · {Path: End-user / Partner·子类型 / Undetermined} |
| **Industry Match** | {🟢 Target / 🔵 Adjacent / 🔴 Outside / ⚪ Unknown} |
| **Current Wastewater Treatment / Technology** | {End-user：现有处理方案单元 / Partner：可提供的技术组合 / ⚪ Unknown} |
| **BDD Opportunity** | {🟢 High / 🟡 Medium / 🔴 Low / ⚪ Unknown} · {Opportunity Type} |
| **Demand Status** | {🟢 Confirmed / 🟢 Strong Signal / 🟡 Potential / 🔴 Weak / ⚪ Unknown} |
| **Priority Site** | {厂区名（国家）· 一句话理由 / N/A} |
| **Who to Contact** | {岗位角色} {/ 具名 + 职位} {/ No verified contact found} |
| **What Is Missing** | [Business] {…}　[Project] {…}　[Technical] {…}　/ None |
| **Next Action** | {一句话：本轮做什么} |
| **Sales Conclusion** | {🟢 建议重点开发 / 🟢 建议开发 / 🟡 建议先验证 / 🔴 暂不优先 / ⚪ 信息不足，暂缓判断}<br>　{1~2 句原因} |

**BDD Opportunity 判定依据**

- Reason: {已确认什么 / 缺什么}
- Evidence: {E# / E# …}
- Confidence: {High / Medium / Low}
- Opportunity Type: {五值之一，复合时用 " +| " 连接}

**Demand Status 明细**

- Public Wastewater Evidence: {等级} — {一句话}（E#）
- Customer-stated Demand: {等级} — {一句话}（客户自述 / E#）
- → 取较高者：{等级}

**风险**

- Commercial Risk: {🟢 Low / 🟡 Medium / 🔴 High / ⚪ Unknown}
- Risk Note: {可选，一句话}
- Financial Warning: {🟢 No / 🔴 Yes / ⚪ Unknown}
```

---

## 字段填写规则（大白话要求）

| 字段 | 规则 |
|---|---|
| **Company** | 登记全称 + 核实三态。名称有歧义 → `Unverified`，**不得选最像的一家** |
| **Country** | 只写国家 + 主要运营地区。跨国集团写"总部所在国 + 主要制造分布" |
| **What They Do** | **一句话，用业务员能转述的话。** 不堆术语。例如："德国水处理设备公司，自己造设备、也自己生产水处理药剂" |
| **Customer Type** | 类型 + **Path**。Path 必须显式写出：`End-user` / `Partner·EPC` / `Partner·Integrator` / `Partner·Distributor` / `Partner·Technology Partner` / `Undetermined` |
| **Industry Match** | 对照 `bdd-fit-rules.md` 最小目标市场地图。带颜色 |
| **Current Wastewater Treatment / Technology** | End-user 写"现在用什么处理"；Partner 写"能提供哪些技术"。**只写单元名，不写数值。** 查不到 → `⚪ Unknown` |
| **BDD Opportunity** | 四档 + **Opportunity Type**。复合类型写 `主 +| 副`。含竞争关系 → 标 `🔴 Conflict` |
| **Demand Status** | 主卡只写**较高者**；两类的明细写在下方"Demand Status 明细" |
| **Priority Site** | **仅 ≥ 3 个公开厂区的集团使用**；否则写 `N/A` |
| **Who to Contact** | 岗位角色（可选具名 + 职位 + Source）。查不到真人 → `No verified contact found`（岗位角色仍输出） |
| **What Is Missing** | **按 Business → Project → Technical 排列**，最多 5 项，前缀标级别。齐全 → `None` |
| **Next Action** | 一句话。**不得写"邀请寄样小试"**；已确认具体项目时写"转交技术评估流程" |
| **Sales Conclusion** | 五值之一 + 1~2 句原因。取值规则见 `sales-conclusion-rules.md` |

---

## 主卡禁止项（V1.1）

| 禁止 | 原因 |
|---|---|
| 出现"8 项输入""封顶规则""判据①"等内部术语 | 主卡写给业务员，不写给规则维护者 |
| 主卡超过 1 页 | 30 秒可读约束 |
| 用 `Unknown` 的推测内容填满模板 | 制造虚假完整度 |
| 把 FACT 与 INFERENCE 混在同一格 | 幻觉主要来源 |
| 因 Industry Match = Target 直接给 BDD Opportunity = High | 最重要的一条禁止 |
| 因行业是 Lithium Battery 就自动给 `High` | 必须由主体级证据支撑 |
| 有 ETP / ZLD 就判 `Low` | 已有设施 ≠ 无机会 |
| Partner Path 按"自身废水"评判 | 口径错 |
| `Commercial Risk = Unknown` 写成 `High` | 修复项 |
| 输出工艺参数 / 设备选型 / 技术方案 / 达标承诺 / 金额 | 安全边界 |
| 输出 Technical Fit / Quotation Readiness | 已移出职责 |
| **输出"建议小试" / 固定"寄 5~10 L 水样" / 自动进入小试流程** | **V1.1 已删除，属越界** |
| 输出回复草稿 / 跟进节奏 | 已移出职责 |
| 生成未经公开来源验证的具体人名 / 电话 / 邮箱 | 合规风险 |
| 颜色与取值不一致，或用颜色表达程度 | 破坏横向可比 |
| `UNKNOWN` 不带三态后缀 | 无法区分"查了没有"与"没渠道可查" |

---

## 第二层 · 附录 A · Evidence 明细（折叠区）

```markdown
---
<details>
<summary>附录 A · Evidence 明细（{N} 条）</summary>

| # | 类型 | 结论 | Source | Reason | Confidence | Decision Impact |
|---|---|---|---|---|---|---|
| E1 | FACT | {内容} | {URL / 客户自述} | — | High | High |
| E2 | INFERENCE | {内容} | — | {推断理由} | Medium | Medium |
| E3 | UNKNOWN · searched | {未查到的项} | — | — | — | Low |

**类型定义**：FACT 必须有 Source；INFERENCE 必须有 Reason + Confidence；
UNKNOWN 必须带三态后缀（`searched` / `no source` / `not searched`），不得补全。

**Decision Impact**：High / Medium / Low —— 只影响展示优先级，不影响真实性判断，与类型、Confidence 正交。

**可溯源率**：{已标注 Source 的 FACT 数} / {FACT 总数}　目标 100%

</details>
```

**编号规则**：`E1`、`E2`… 顺序编号。主卡 `Evidence` 字段与 `Priority Site` 均引用这些编号。

**附录不得省略的固定段**：

| 段 | 内容 |
|---|---|
| 排除项 | 同名主体排除的核实过程（若有） |
| 冲突项 | 来源冲突的字段（两条都列） |
| UNKNOWN 汇总 | 三态分类，说明"查了没有"≠"没有" |
| 边界声明 | 本卡不输出什么 |

---

## 分组输出（按输入信息量自动调整）

| 用户提供了什么 | 输出什么 |
|---|---|
| 完整询盘原文 + 公司名 | 完整两层结构（13 字段全填，可含 CSD） |
| 只有公司名 / 官网 | 完整两层结构；`Demand Status` 主要来自 PWE；`What Is Missing` 优先 Business 级 |
| 只有询盘原文，无公司名 | 主卡（`Company` 标客户自述 + `Unverified`）+ 附录 A 标注"需公司名方可检索" |
| 只有官网网址，无公司名 | 先做主体识别；能唯一确定 → 正常输出；不能 → `Unverified` + Business 级缺项 |
| 信息极少 | 主卡如实填 `⚪ Unknown`，`Sales Conclusion = ⚪ 信息不足，暂缓判断`。**不硬凑分析** |

---

## 填写示例（说明大白话风格）

```markdown
# Aarti Industries · BDD Customer Intelligence

2026-09-26 | 来源：公司名 + 官网
执行版本：BDD Customer Intelligence Skill V1.1

## 第一层 · 主判断卡

| 字段 | 判定 |
|---|---|
| **Company** | AARTI INDUSTRIES LTD（印度）· Verified |
| **Country** | 印度 · 古吉拉特邦 Vapi 注册，孟买总部 |
| **What They Do** | 印度大型特殊化学品制造商，做苯系和甲苯系化工中间体，16 个制造基地，出口占一半以上 |
| **Customer Type** | 终端业主 · End-user |
| **Industry Match** | 🟢 Target（T4 精细化工，且产生高 COD 难降解废水） |
| **Current Wastewater Treatment / Technology** | 物化 + 生化 + 膜 + 多效蒸发；8 座厂区已 ZLD、3 座 ZLD-ready、其余在推进；100% 废水厂内三级处理；水回用 42%；排放接入 CPCB/SPCB 在线监测 |
| **BDD Opportunity** | 🟢 High · End-user Opportunity |
| **Demand Status** | 🟡 Potential |
| **Priority Site** | Tarapur（印度 · 马哈拉施特拉邦）· 有半年度 EC 合规报告载明已 ZLD 与月废水产生量，且废水回用合作项目在该厂区推进 |
| **Who to Contact** | 环保负责人 / EHS 负责人（首选）→ 技术总工<br>Shyam Dhekekar｜Chief Technical and Sustainability Officer｜Source: 官网 Who We Are |
| **What Is Missing** | [Business] ① 是否存在具体废水治理项目的需求方与决策链　[Project] ② 目标工段（新建 / 提标 / 高浓母液）③ 项目阶段与时间节点　[Technical] ④ 目标污染物浓度与水量 |
| **Next Action** | 先向 EHS 负责人确认是否存在具体提标或高浓母液处理项目及目标工段；若确认存在项目，转交技术评估流程 |
| **Sales Conclusion** | 🟡 建议先验证<br>　企业级废水证据充分、行业属目标市场，但尚无具体项目证据、需求方未确认；先补 Business / Project 级信息再决定投入 |

**BDD Opportunity 判定依据**

- Reason: 主体级证据充分——16 个制造单元已确认、官网载明硝化/氯化/加氢等工艺段、8 座 ZLD 与未闭环厂区并存、半年度政府合规报告含废水分析、环境改善专项资本开支、EHS/ETP 岗位持续招聘；缺具体项目证据
- Evidence: E4 / E5 / E6 / E8 / E12 / E13 / E14 / E15 / E16
- Confidence: High
- Opportunity Type: End-user Opportunity

**Demand Status 明细**

- Public Wastewater Evidence: Potential — 官网与政府合规报告载明现有设施与运行数据，但无具体项目
- Customer-stated Demand: Unknown — 本次无询盘文字
- → 取较高者：Potential

**风险**

- Commercial Risk: ⚪ Unknown
- Risk Note: 无往来内容可供观察；类型级先验不参与定级
- Financial Warning: 🟢 No（上市公司公告显示盈利，无裁员重组信号）
```

> **说明**：`Industry Match` 输出 `Target`（V1.1 起地图已填）；
> `BDD Opportunity` 输出 `High`——**不再因"无询盘"封顶 `Medium`**（该封顶规则 V1.1 已删除）。
