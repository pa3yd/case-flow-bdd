# AartiIndustries · BDD Customer Intelligence

2026-09-26 | 来源：公司名 + 官网 `https://www.aarti-industries.com/`（无询盘原文、无往来记录）
执行版本：BDD Customer Intelligence Skill V1.1
本次为 **V1.1 回归测试**：复用 V1 已检索证据（证据编号沿用），未新增检索。

---

## 第一层 · 主判断卡

| 字段 | 判定 |
|---|---|
| **Company** | AARTI INDUSTRIES LTD（印度）· Verified |
| **Country** | 印度 · 古吉拉特邦 Vapi 注册 · 孟买企业办公室 |
| **What They Do** | 印度大型特殊化学品制造商，做苯系和甲苯系化工中间体，单一业务分部占营业额 100%，16 个制造基地，出口占 57% |
| **Customer Type** | 终端业主 · **End-user** |
| **Industry Match** | 🟢 Target（**T4 精细化工**，并属 **T3 高 COD / 难降解工业废水**性质口径） |
| **Current Wastewater Treatment / Technology** | 物化 + 生化 + 膜 + 多效蒸发/结晶；**8 座厂区已 ZLD、3 座 ZLD-ready、其余在推进**；**100% 废水经厂内三级处理**；不取用地下水；水回用 42%（1,232,772 KL）；单位新鲜水耗 2.56 KL/MT；**ETP 最终排放参数在线监测已接入 CPCB / SPCB**；Tarapur（Topaz）已实现 ZLD 并全部回用作冷却塔补水、**MIDC 已于 2019-11-15 断开排污接管**；现有 ETP 容量 75 m³/day；废水治理实例含以石灰替代烧碱中和 2,5 DCNB 与 SAC 废水、废酸 LCTM 净化 |
| **BDD Opportunity** | 🟢 High · **End-user Opportunity** |
| **Demand Status** | 🟡 Potential |
| **Priority Site** | **Tarapur（印度 · 马哈拉施特拉邦 · Topaz Division）** · 有半年度 EC 合规报告载明已实现 ZLD、无 CETP 排放、月废水产生量逐月数据，且 1000 KLD 废水回收系统（EPC + O&M）在该厂区推进 —— 现有设施与未回用段并存<br>　备选：Jhagadia Zone IV（95 英亩新基地，含中试厂与 Multi-Purpose Plant） |
| **Who to Contact** | ① 环保负责人 / 安环（EHS）负责人（首选）→ No verified contact found<br>　② 技术总工 / 生产技术负责人 → Name: Shyam Dhekekar ｜ Position: Chief Technical and Sustainability Officer ｜ Source: 官网 Who We Are + BSE 年报文件 |
| **What Is Missing** | [Business] ① 是否存在具体废水治理 / 提标 / 高浓母液处理项目的需求方与决策链　[Project] ② 目标厂区与目标工段（新建 / 提标 / 母液处理）③ 项目阶段与时间节点　[Technical] ④ 目标污染物浓度与处理水量 |
| **Next Action** | 先向 Tarapur 厂区 EHS 负责人或技术负责人确认是否存在具体提标 / 高浓母液 / 水回用项目及目标工段；若确认存在项目，转交技术评估流程 |
| **Sales Conclusion** | 🟢 **建议开发**<br>　主体级证据充分（16 个制造单元 + 8 座 ZLD 且存在未闭环厂区 + 政府 EC 合规报告含废水数据 + 环境改善专项资本开支 + 扩产项目），行业属目标市场，无财务警示；尚无具体项目文件级证据，故未达"重点开发" |

**BDD Opportunity 判定依据**

- **Reason**：End-user Path。① `Industry Fit = Target`（T4 + T3）✔ ② **制造业活动已确认**（16 个制造基地；单一分部占营业额 100%；官网载明硝化、氯化、加氢、氨解、Halex、氟化、水解、磺化、氧化、烷基化、重氮化等工艺段）✔ ③ **PWE 成立**（官网水管理与废水治理实例 + 政府 EC 半年度合规报告含废水数据 + ETP 在线监测接入 CPCB/SPCB）✔ ④ **主体级证据 ≥2，实为 5 项**：**现有处理设施**（8 座 ZLD + 3 座 ZLD-ready + 100% 厂内三级处理 + Tarapur ETP 与 1000 KLD 回收系统）+ **环境证据**（ISO 14001、Responsible Care、CDP Water A-）+ **项目信号**（Dahej ₹200–250 cr 后向一体化装置、Jhagadia Zone IV 95 英亩新基地）+ **窗口信号**（官网明示"其余厂区仍在推进 ZLD"，水回用率 42% 未闭环）+ **环境投入**（FY25 ₹102 cr / FY26 ₹60 cr）
  → 四项判据全部成立 → `High`。
  **关键判读（回归重点）**：**已有 8 座成熟 ZLD 不构成 `Low`。** 按 `current-treatment-rules.md` 第四节规则 1，须同时核对降级三条件——本次**三项均不成立**（存在未闭环厂区、有扩产与新建项目、有高浓母液与废酸等遗留工艺段），故不降级。
- **Evidence**：E4 / E5 / E6 / E8 / E9 / E10 / E11 / E12 / E13 / E14 / E15 / E16 / E17
- **Confidence**：High
- **Opportunity Type**：**End-user Opportunity**

**Demand Status 明细**

- **Public Wastewater Evidence**：🟡 Potential — 官网与政府 EC 合规报告载明既有设施与运行数据、扩产项目与环境投入，但**未查到**任何指向具体废水治理项目的文件或招标
- **Customer-stated Demand**：⚪ Unknown · not searched — 本次无询盘文字
- → **取较高者：Potential**

**风险**

- **Commercial Risk**：⚪ Unknown
- **Risk Note**：印度上市公司，公开披露充分；本次无往来内容可供观察索取行为，**类型级先验不参与定级**。近 12 个月未见环保处罚硬信号。
- **Financial Warning**：🟢 No（BSE / NSE 持续披露、AGM 于 2026-09-21 正常召开、无公开违约或评级下调信号）

---

## 第二层 · 附录 A · Evidence 明细

<details>
<summary>附录 A · Evidence 明细（32 条）</summary>

| # | 类型 | 结论 | Source | Reason | Confidence | Decision Impact |
|---|---|---|---|---|---|---|
| E1 | FACT | 工商全称 AARTI INDUSTRIES LTD；CIN L24110GJ1984PLC007301；RoC-Ahmedabad；状态 Active；注册地址 Plot No. 801/23, GIDC Estate, Phase III, Vapi, Gujarat 396195 | MCA 登记（经 instafinancials 转录） | — | Low | Medium |
| E2 | FACT | 官网自述领先特殊化学品制造商；注册办公室 Vapi、企业办公室 Mumbai（Embassy 247, Vikhroli W） | 官网首页 / contact / who-we-are | — | High | Medium |
| E3 | FACT | 上市主体 BSE 524208 / NSE AARTIIND；第 43 届 AGM 于 2026-09-21 召开；Integrated Annual Report FY2025-26 已发布 | BSE/NSE 披露 + 官网投资者板块 | — | High | Medium |
| E4 | FACT | 单一业务分部 = 特殊化学品，占总营业额 100%；出口占 57%；服务 30 个国内 + 60 个国际市场 | BRSR FY2025-26（2026-08-27 提交） | — | High | High |
| E5 | FACT | 16 个制造基地；Vapi（Zone I）、Jhagadia（Zone II / Zone IV）、Dahej（SEZ II）、Tarapur、Kutch（Bhachau, Anushakti）+ ARTC Navi Mumbai 研发中心 | 官网首页 + /contact + 年报报告边界 | — | High | **High** |
| E6 | FACT | 公开载明制造工艺：硝化、氯化、加氢、氨解、Halex、氟化、水解、磺化、氧化、烷基化、重氮化 | 官网能力 / 产品页 + 年报 | — | High | High |
| E7 | FACT | 规模**来源冲突**：BRSR FY2025-26 载 2,302 员工 + 10,781 工人；官网"5,800+ employees"；第三方 5,868 | 见 Source | — | Medium | Low |
| E8 | FACT | 水管理：42%（1,232,772 KL）水回用；**8 座设施为 ZLD、3 座 ZLD-ready**；100% 废水经厂内三级处理；不取用地下水；单位新鲜水耗 2.56 KL/MT | 官网 /sustainability/environment | — | High | **High** |
| E9 | FACT | 废水治理实例：以石灰替代烧碱中和 2,5 DCNB（26 KLD）与 SAC（50 KLD）废水；CaSO₄ 过滤后供水泥行业；低 TDS 滤液转生化系统 | 官网环境页案例 | — | High | High |
| E10 | FACT | 废酸净化 LCTM 工艺成效：COD 由 12,000 降至 <1,000 mg/l；硝酸含量由 10,000 PPM 降至 <50 PPM | 官网环境页案例 | — | High | High |
| E11 | FACT | ETP 最终排放参数与在线监测已接入 CPCB / SPCB 门户，实时监控 | FY2023-24 董事报告 + 官网环境页 | — | Medium | High |
| E12 | FACT | Tarapur（Topaz）半年度 EC 合规报告（2025-04~2025-09）：已实现 ZLD；全部废水处理后回用作冷却塔补水、**不向 CETP 排放**；MIDC 已于 2019-11-15 断开排污接管；现有 ETP 容量 75 m³/day；月废水产生量 524 / 376 / 272 / 679 / 858 / 1,347 m³ | 官网 EC Compliance Report（AIL Topaz Division） | — | High | **High** |
| E13 | FACT | 环境改善专项资本开支：FY25 ₹102 cr；FY26 ₹60 cr | 官网 sustainability-overview；FY2025-26 年报 | — | High | **High** |
| E14 | FACT | 扩产 / 项目信号：2026-03-05 宣布 Dahej SEZ 投资约 ₹200–250 cr 建后向一体化装置（工期两年）；Jhagadia Zone IV 新增 95 英亩绿色制造基地（含中试厂与 Multi-Purpose Plant） | BSE 披露（2026-03-05）+ 官网 manufacturing-capabilities | — | High | **High** |
| E15 | FACT | 废水回用项目：与 Felix Water Technologies 合作建设 1000 KLD 废水回收系统，EPC + O&M 模式 | felixindustries.co（供应商官网） | — | Medium | High |
| E16 | FACT | 环境 / ETP 岗位持续招聘：Bhachau 招 Environment Officer、ETP Operator；Dahej 于 2026-05/06/07 多次 walk-in 招 Environment Officer、ETP Field Operator，均要求化工装置 ETP 经验 | 招聘聚合站 | — | Low | High |
| E17 | FACT | 认证与评级：ISO 14001:2015、ISO 45001、ISO 9001、ISO 50001、Responsible Care、CDP Water Security Leadership Band "A-"、S&P Global CSA 62/100、Sustainability Yearbook 2025 | 官网 corporate-governance / environment | — | High | Medium |
| E18 | FACT | EcoVadis 评级**来源冲突**：官网页脚列 "Ecovadis Gold Rating"；第三方称 2026-06 获 Platinum（87/100） | 见 Source | — | Medium | Low |
| E19 | FACT | 涉诉：Aarti Industries Ltd. vs Shabbirbhai Rahimbhai Vora（2025 Supreme(Guj) 1267）—— 古吉拉特高等法院劳动争议，当事人为自 2008-09-01 起任职的 **Effluent Treatment Plant Operator** | supremetoday.ai（判决转录） | — | Medium | Medium |
| E20 | FACT | Rajendra V. Gogri 任 Chairman & MD；Suyog Kotecha 任 CEO & Executive Director | 官网 corporate-governance / who-we-are | — | High | Medium |
| E21 | FACT | 公开可核实相关岗位真人：Shyam Dhekekar — Chief Technical and Sustainability Officer | 官网 who-we-are + BSE 年报文件 | — | Medium | High |
| E22 | FACT | 【已排除 · 误关联】GPCB 2026-07-18 依 Water Act 33A 下达的 Saykha（Bharuch）关闭令属 **Aarti Drugs Limited（AARTIDRUGS）**，非本主体 | indianpharmapost / chemicaltoday / BSE 披露 | — | High | **High** |
| E23 | FACT | 【已排除 · 误关联】2026-03-22 Tarapur Unit-VI（Plot D-18）二甲硫醚泄漏属 **Aarti Pharmalabs Limited（AARTIPHARM）**；本主体 Tarapur 基地为 Plot L-5/L-8/L-9-1（Topaz Division） | BSE 披露（SYMBOL: AARTIPHARM, 2026-03-24） | — | High | **High** |
| E24 | INFERENCE | Customer Type = End-user | — | 拥有 16 个自有制造基地、自建 ETP 与 ZLD 设施、自行承担排放责任 | High | High |
| E25 | INFERENCE | 废水特征以高 COD、酸性、含氮有机物（硝基 / 胺类中间体）为主，并存在高盐 / 高 TDS 段 | — | 依据 E6 公开载明工艺段与 E9/E10 官网废水案例推断；**未采信任何数值作为客户水质数据** | Medium | High |
| E26 | INFERENCE | **存在尚未完成 ZLD 的厂区，构成提标 / 改造窗口** | — | 官网明示 8 座 ZLD、3 座 ZLD-ready、"other facilities progressing towards ZLD readiness"，水回用率 42% → 仍有厂区未闭环；**该事实排除 `Low` 降级** | Medium | **High** |
| E27 | UNKNOWN · searched | 近 12 个月环保处罚记录 | — | 已检索未查到 | — | High |
| E28 | UNKNOWN · searched | 环评公示 / 公众听证（近 12 个月） | — | 已检索未查到 | — | Medium |
| E29 | UNKNOWN · searched | 公开招标 / 中标公告（废水处理类） | — | 已检索未查到 | — | Medium |
| E30 | UNKNOWN · searched | 排污许可（CTO / CCA）变更公示 | — | 已检索未查到 | — | Low |
| E31 | UNKNOWN · not searched | 客户侧废水需求陈述 | — | 本次无询盘文字 | — | High |
| E32 | UNKNOWN · searched | 环保负责人 / 安环（EHS）负责人具名信息 | — | 已检索未在允许来源清单内查到 | — | Medium |

**类型定义**：FACT 必须有 Source；INFERENCE 必须有 Reason + Confidence；UNKNOWN 必须带三态后缀且不得补全。

**Decision Impact**：只影响展示优先级，不影响真实性判断。

**可溯源率**：22 / 22 = **100%**

**排除说明**：E22、E23 两条经交叉核对确认属**同集团名称相近但法律主体不同**的公司（Aarti Drugs Ltd、Aarti Pharmalabs Ltd），已按 `evidence-policy.md` 排除，未计入 Demand Status 与 Commercial Risk。

</details>

---

## 边界声明

本次执行未输出：工艺参数、设备选型、技术方案、达标承诺、金额（公司公开财务数据除外）、报价状态、回复草稿、跟进节奏、客户案例名单。
`Technical Fit` 与 `Quotation Readiness` 按范围冻结规定**不输出**。
**未输出"建议小试"，未固定"寄 5~10 L 水样"**（V1.1 已删除该越界规则）。
