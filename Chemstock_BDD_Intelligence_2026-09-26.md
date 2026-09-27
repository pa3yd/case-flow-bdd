# CHEMSTOCK LLC · BDD Customer Intelligence

2026-09-26 | 来源：用户提供官网网址 `https://chemstock.ae/`（无询盘原文、无往来记录）
执行版本：BDD Customer Intelligence Skill V1.1
本次为 **V1.1 回归测试**：复用 V1 已检索证据（证据编号沿用），未新增检索。

---

## 第一层 · 主判断卡

| 字段 | 判定 |
|---|---|
| **Company** | CHEMSTOCK LLC（阿联酋）· Partially Verified |
| **Country** | 阿联酋 · 迪拜（JLT）· 乌姆盖万（工业区）· 阿布扎比 |
| **What They Do** | 阿联酋的工业化学品与实验室产品分销商，同时做化学品仓储物流；独家分销 Hanna Instruments 等品牌，产品线里有水处理药剂（混凝剂、絮凝剂、氧化剂）和分析仪器电极探头 |
| **Customer Type** | 贸易商 / 分销代理 · **Partner·Distributor** |
| **Industry Match** | 🔵 Adjacent（A2 工业化学品 / 水处理药剂分销） |
| **Current Wastewater Treatment / Technology** | Partner 口径——**可提供**：水处理药剂供应（混凝剂与絮凝剂：明矾、三氯化铁、硫酸铁、PAC、聚电解质；氧化剂与消毒剂：双氧水、次氯酸钙、次氯酸钠）＋ 实验室分析仪器与电极探头分销（Hanna Instruments 独家）。**无公开证据表明其提供工艺包、成套设备或工程集成能力** → 工艺技术组合：⚪ Unknown |
| **BDD Opportunity** | 🟡 Medium · **Distribution Opportunity** |
| **Demand Status** | ⚪ Unknown |
| **Priority Site** | N/A（非多厂区制造集团） |
| **Who to Contact** | 负责人 / 总经理（首选）→ 业务 / 采购负责人 · No verified contact found |
| **What Is Missing** | [Business] ① 需求性质（渠道分销 vs 自用项目）② 终端客户行业结构（是否覆盖高 COD 难降解废水行业）③ 是否具备设备 / 电极类产品的交付与售后能力　[Project] ④ 是否有在手项目或明确目标终端 |
| **Next Action** | 先确认其是否为渠道分销需求、终端客户行业结构，以及是否具备设备 / 电极类产品的交付与售后能力；本轮不释放技术资料 |
| **Sales Conclusion** | 🟡 **建议先验证**<br>　渠道覆盖化工、制药、纺织、造纸、油气等行业客户，且已代理水处理药剂与在线分析仪器，构成可用的 `Distribution Opportunity`；但"渠道分销还是自用项目"未确认、终端行业结构未知、无设备类交付能力证据，先补 Business 级信息 |

**BDD Opportunity 判定依据**

- **Reason**：Partner Path。① `Industry Fit = Adjacent`（A2）✔ ② 分销 / 渠道能力已确认（官网自述自 1988 年即为 trading organization；持有 Hanna Instruments、SDFCL、Jeiotech 独家分销与 Meling 授权分销；产品均源自第三方品牌）✔ ③ **技术组合重叠不成立**——其水处理相关产品为**化学品（药剂）与实验室仪器**，非**工艺技术**；分销商不提供工艺包，故不与 BDD 形成"技术组合"重叠 ✖ ④ 渠道 / 项目证据 ≥2（覆盖 7 大行业客户群 + 三处办公与仓储物流设施 + 多品牌独家分销关系）✔
  → ③ 不成立，`High` 不可达；主体级证据充分，判定 `Medium`。
  **不判 `Low` 的理由**：其水处理药剂线（混凝、絮凝、氧化、消毒）服务的处理目标与 BDD 场景同源，且渠道可触达工业客户 → 不存在"与 BDD 场景无任何重叠"的情形。
- **Evidence**：E2 / E3 / E4 / E5 / E6 / E12 / E14
- **Confidence**：Medium
- **Opportunity Type**：**Distribution Opportunity**

**Demand Status 明细**

- **Public Wastewater Evidence**：⚪ Unknown · searched — 该公司为分销 / 仓储型主体，非废水产生方；未检索到自有废水设施披露。**UAE 无等同中国的公开环境许可与处罚查询渠道。**
- **Customer-stated Demand**：⚪ Unknown · not searched — 本次无询盘文字。
- → **取较高者：Unknown**

**风险**

- **Commercial Risk**：⚪ Unknown
- **Risk Note**：分销型主体的终端不透明与价格敏感为通用关注点；但本次仅有官网网址、无任何往来内容可供观察，**按规则类型级先验不参与定级**。
- **Financial Warning**：⚪ Unknown（无公开财务信息）

---

## 第二层 · 附录 A · Evidence 明细

<details>
<summary>附录 A · Evidence 明细（24 条）</summary>

| # | 类型 | 结论 | Source | Reason | Confidence | Decision Impact |
|---|---|---|---|---|---|---|
| E1 | FACT | 域名 `chemstock.ae` 对应主体 CHEMSTOCK LLC，同址列示迪拜与乌姆盖万办公点及 `sales@chemstock.ae` | https://www.hannainst.com/uae-oman | — | High | Medium |
| E2 | FACT | 企业自述：1988 年始于沙特达曼，初期即为工业化学品与工程产品的**贸易组织**，现于阿联酋 / 印度 / 中国设办公室 | https://chemstock.ae/about-us/（企业自述） | — | Medium | High |
| E3 | FACT | 业务构成：工业化学品、实验室化学品与耗材、实验室设备与家具、玻璃器皿、化学品仓储与物流、实验室交钥匙方案 | https://chemstock.ae/about-us/ | — | High | High |
| E4 | FACT | 产品组合含「Water Treatment Chemicals」：混凝剂与絮凝剂（明矾、三氯化铁、硫酸铁、PAC、聚电解质）；消毒与氧化剂（双氧水、次氯酸钙、次氯酸钠）；其他（亚硫酸氢钠、活性炭） | https://chemstock.ae/wp-content/uploads/2021/12/Chemstock-Industrial-Chemicals-Brochure.pdf | — | High | High |
| E5 | FACT | 分销关系：Hanna Instruments 独家、SDFCL 独家、Jeiotech 独家、Meling 授权；含水分分析仪、氯/pH/ORP 分析仪、**电极与探头** | 官方产品手册 + https://www.hannainst.com/uae-oman | — | High | High |
| E6 | FACT | 覆盖行业：玻璃与陶瓷、爆破与采矿、涂料、钢铁与水泥、食品与饲料、线缆、印刷包装、洗涤剂与香精；官网另称服务石油天然气、制药、纺织、制浆造纸、食品饮料、农业、建筑 | 官方产品手册 + https://chemstock.ae/industrial-chemicals/ | — | High | High |
| E7 | FACT | 员工规模**来源冲突**：Crustdata 36 人 / SignalHire 100–200 人 / TradeWheel 60 人以上 | crustdata · signalhire · tradewheel | — | Low | Low |
| E8 | FACT | 第三方登记：UAE 主体 CHEMSTOCK LLC 成立 2020-06-17，登记业务为化学品批发贸易 | credencedata.com | — | Low | Medium |
| E9 | FACT | 地址记录：迪拜 JLT Cluster C, Goldcrest Executive；乌姆盖万 New Industrial Area, Plot 518；另有阿布扎比 Mohamed Bin Zayed City 地址 | hannainst.com · crustdata | — | Medium | Low |
| E10 | FACT | 官网材料自称 ISO 9001:2015 认证公司 | 官方产品手册 | — | High | Low |
| E11 | FACT | 可检索岗位：销售协调、物流协调、市场负责人、产品经理、业务拓展、行政、司机，**未见生产岗或环保岗** | signalhire.com | — | Low | Medium |
| E12 | INFERENCE | 该公司为分销 / 贸易型组织，未开展自有化学品生产 | — | 官网自述 trading organization；产品均源自第三方品牌；无厂房 / 产线 / 生产岗位证据；第三方将其归类为 Chemical Manufacturing，与官网自述冲突，冲突状态下不采信该归类 | Medium | High |
| E13 | INFERENCE | UAE 主体（2020 登记）与集团（自称 1988 始于沙特）为不同法律实体 | — | 第三方登记显示 UAE LLC 成立 2020；官网称集团始于 1988；品牌方页面仅列 UAE 办公室 | Medium | Low |
| E14 | INFERENCE | Customer Type = Partner·Distributor | — | 官网自述贸易组织 + 独家及授权分销商身份 + 产品源自第三方品牌 + 无自有生产设施；**替代 V1 的"参保 < 20 人"门槛，改用"采购再转售"这一实质事实** | Medium | High |
| E15 | INFERENCE | Opportunity Type = Distribution Opportunity | — | Path = Partner·Distributor，且无工艺包 / 成套设备 / 工程集成能力的公开证据 | Medium | High |
| E16 | INFERENCE | 其水处理药剂线所服务的处理目标（混凝、絮凝、氧化、消毒）与 BDD 场景**部分同源** | — | 依据 E4 产品组合与 BDD 的目标污染物类型（难降解有机物）在处理目标层面重合；**但药剂 ≠ 工艺技术组合，不构成 Partner 的技术组合重叠** | Medium | High |
| E17 | INFERENCE | BDD Relevance = Medium（非 Low） | — | A2 渠道属性已确认、渠道证据 ≥2；③ 技术组合重叠不成立故不达 High；不存在"与 BDD 场景无任何重叠"的 Low 情形 | Medium | High |
| E18 | UNKNOWN · searched | 自有生产 / 掺配 / 分装设施 | — | 已按官网 + 品牌方页面 + 第三方登记检索，未查到 | — | Medium |
| E19 | UNKNOWN · no source | 环保处罚记录 | — | 阿联酋无公开处罚查询渠道 | — | Low |
| E20 | UNKNOWN · no source | 环评公示 / 排污许可 / 环境许可 | — | 同上 | — | Low |
| E21 | UNKNOWN · searched | 招投标 / 项目 / ESG / 扩产信号 | — | 已检索未查到 | — | Medium |
| E22 | UNKNOWN · searched | 废水产生与处理现状 | — | 非废水产生方；未查到自有废水设施 | — | Medium |
| E23 | UNKNOWN · searched | 是否接触过 BDD / 电化学氧化技术，是否曾询价 | — | 已检索未查到 | — | Medium |
| E24 | UNKNOWN · searched | 注册资本 / 公开财务信息 | — | 已检索未查到 | — | Low |

**类型定义**：FACT 必须有 Source；INFERENCE 必须有 Reason + Confidence；UNKNOWN 必须带三态后缀且不得补全。

**Decision Impact**：只影响展示优先级，不影响真实性判断，与类型、Confidence 正交。

**可溯源率**：11 / 11 = **100%**

</details>

---

## 边界声明

本次执行未输出：工艺参数、设备选型、技术方案、达标承诺、金额、报价状态、回复草稿、跟进节奏、客户案例名单。
`Technical Fit` 与 `Quotation Readiness` 按范围冻结规定**不输出**。
**未输出"建议小试"，未固定"寄 5~10 L 水样"**（V1.1 已删除该越界规则）。
