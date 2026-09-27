# EnviroChemie · BDD Customer Intelligence

2026-09-26 | 来源：仅官网网址 `https://www.envirochemie.com/en/`（未提供公司名、无询盘原文、无往来记录）
执行版本：BDD Customer Intelligence Skill V1.1.1
本次为 **V1.1.1 展示层回归**：复用 V1.1 已检索证据与全部判断结果，**仅按展示层规格重排版式，判断规则未调整、字段值未改动**。

---

## 第一层 · 主判断卡

### WHO · 客户是谁

| 字段 | 判定 |
|---|---|
| **公司 Company** | ENVIROCHEMIE GmbH（德国）· Verified |
| **国家 Country** | 德国 · 黑森州 Roßdorf（达姆施塔特近郊）；海外子公司分布荷兰、奥地利、瑞士、保加利亚、波兰、摩洛哥、罗马尼亚、巴西 |
| **主营业务 Business** | 德国工业水与废水处理公司：既做工程总包与设备制造，也自己生产水处理药剂、并承接设施运营；自有技术中心与中试装置 |
| **客户类型 Customer Type** | 环保工程公司（EPC）· **Partner·EPC** |

### WHY · 为什么值得看

| 字段 | 判定 |
|---|---|
| **行业匹配 Industry Match** | 🔵 Adjacent（**A1 工业废水 EPC / AOP / 集成商**） |
| **BDD机会 BDD Opportunity** | 🟢 High · **EPC / Integration Opportunity +\| Technology Partner Opportunity** · 🔴 **Conflict: 潜在竞争**（自有 AOP 产品线 UV/H₂O₂ 与臭氧，与 BDD 目标场景重叠） |
| **需求状态 Demand Status** | 🟡 Potential |

### WHERE / WHO · 从哪里切入

| 字段 | 判定 |
|---|---|
| **现有废水处理 Current Treatment** | 🟢 Confirmed · Partner 口径——**可提供**：物理化学 · 生物处理（含厌氧沼气 Biomar）· **膜技术** · 离子交换 · 气浮 · **ZLD**；**AOP 线为 H₂O₂ + UV（自有 Envochem AOP 产品线）与臭氧**；公司自述「**verfahrensoffen**」（工艺开放），在自有实验室与中试装置中比对不同 AOP 工艺；交付模式含设备供货 · EPC 工程 · **O&M 设施运营**（承接 HIM GmbH 的 WAA 污水处理设施与 GWRA 地下水治理设施运营维护合同）；2026 年项目群覆盖 PFAS 去除、重金属离子交换、硫酸盐去除、蒸发冷凝液处理、制药含脂/乳化漂洗水、钢铁加工废水、食品加工废水、高纯水 |
| **优先厂区 Priority Site** | N/A（生产与技术中心集中于 Roßdorf，海外为销售型子公司；**不构成"≥ 3 个制造厂区"的多厂区制造集团**） |
| **关键联系人 Contact** | 工艺 / 技术工程师（首选）→ 技术总监层<br>　Name: Dr Robert Lutze ｜ Position: Managing Director, Plant Engineering（分管 Sales & Process Design 与 Project Execution）｜ Source: 官网新闻稿 2026-06-01<br>　（公开接触入口、非技术决策层：Nina Reppich｜Head of Marketing & Communications｜Source: 同上） |

### ACTION · 现在怎么办

| 字段 | 判定 |
|---|---|
| **待确认信息 Missing Info** | [Business] ① 采购形态与合作定位（电极 / 模组供应 vs 整套集成 vs 长期技术合作）② 是否存在竞争保护边界（其自有 AOP 线与 BDD 的定位关系）③ 供应商准入与验证要求　[Project] ④ 是否有在谈项目可纳入评估　[Technical] ⑤ 典型项目水质类型与主要污染物 |
| **下一步 Next Action** | 先与其 Plant Engineering 部门确认是否有把电化学氧化纳入工艺组合的规划与目标工段，以及合作定位与竞争边界；若确认存在在谈项目，转交技术评估流程 |

> **开发建议 Sales Conclusion**
>
> 🟡 **建议先验证**
>
> 　自身就是工业废水 EPC 与 AOP 供应商，2026 年项目群 11 项 + 2 项 O&M 运营合同在手，属可触达的组合补齐型伙伴；但**财务警示已触发**（公开数据连续两年亏损），且尚未确认是否会把电化学氧化纳入工艺组合，先复核财务口径与合作定位


**BDD Opportunity 判定依据**

- **Reason**：Partner Path。① `Industry Fit = Adjacent`（A1）✔ ② **技术 / 集成 / 渠道能力已确认**（商业登记经营范围载明水与废水处理设备的**规划·制造**·销售·安装；WZ 分类为机械制造；Roßdorf 自有液体药剂混合灌装产线 30 t/日；自有技术中心与中试装置；公开采购记录显示其承接污水处理设施与地下水治理设施的运营维护合同）✔ ③ **技术组合与 BDD 场景存在公开可证的重叠**（其 AOP 线面向难降解有机物 / API 残留 / PFAS，与 BDD 目标场景同源；且公司自述工艺开放）✔ ④ **渠道 / 项目证据 ≥2，实为 3 项**（2026 年官网项目群 11 项 + 公开采购记录 2 项 O&M 合同 + 集团 9 处海外实体）
  → 四项判据全部成立 → `High`。
- **⚠️ 回归重点说明（Partner Path 三条硬约束均已执行）**：
  ① **走 Partner Path** ✔（Customer Type = EPC，非终端业主）
  ② **不以自身废水作为主要判断依据** ✔ —— 本卡 `Reason` 未引用"其 Roßdorf 产线可能产生清洗废水"这类推断（V1 卡中的 E31 推断已**弃用**，见 D1）
  ③ **识别出 EPC / Technology Partner Opportunity 并提取技术组合** ✔
- **🔴 竞争标注**：其自有 AOP 产品线（UV/H₂O₂、臭氧）与 BDD 目标场景重叠 → 按 `opportunity-type-rules.md` 第三节**必须标注 `Conflict: 潜在竞争`**，不得隐藏。
- **Evidence**：E3 / E4 / E12 / E13 / E14 / E15 / E16 / E18 / E19 / E20 / E21
- **Confidence**：High
- **Opportunity Type**：**EPC / Integration Opportunity +| Technology Partner Opportunity**

**Demand Status 明细**

- **Public Wastewater Evidence**：🟡 Potential — 2026 年项目群 11 项公开在谈/执行项目 + 2 项污水处理与地下水治理设施运营维护合同（07/2025–06/2028），构成充分的**伙伴侧项目信号**；但**无任何证据指向其采购 BDD 类电极 / 模组的意图**
- **Customer-stated Demand**：⚪ Unknown · not searched — 本次无询盘文字
- → **取较高者：Potential**

**风险**

- **Commercial Risk**：⚪ Unknown
- **Risk Note**：其自有 AOP 产品线与 BDD 场景重叠，属"交易对手既采购又竞争"的关系；但本次无往来内容可供观察索取行为，**按规则该事实不参与定级，仅作附注**。
- **Financial Warning**：🔴 **Yes**
- **财务说明（重要）**：公开数据来源显示营业额 €227.2M（2023）/ €209.9M（2022）/ €200.8M（2021）/ €160.7M（2020），**2023 年亏损 -€7.7M、2022 年亏损 -€7.9M（2021、2020 为盈利）**，构成"连续亏损"判据。
  **来源为商业登记数据转引（Confidence Low），且公司已不再单独公布年报、并入集团合并报表** → **建议业务方在使用前复核财务口径**。
  按 `sales-conclusion-rules.md`，`FW = Yes` 使结论**最高不超过 `建议先验证`**，并在结论中明示。

---

## 第二层 · 附录 A · Evidence 明细

<details>
<summary>附录 A · Evidence 明细（32 条）</summary>

| # | 类型 | 结论 | Source | Reason | Confidence | Decision Impact |
|---|---|---|---|---|---|---|
| E1 | FACT | 工商全称 EnviroChemie GmbH；注册地 In den Leppsteinswiesen 9, 64380 Roßdorf，德国 | 官网 Legal notice | — | High | Medium |
| E2 | FACT | Amtsgericht Darmstadt HRB 3883；VAT DE 111 627 671；注册资本 €1,501,000（2025-01-08 增资后） | 官网 Legal notice；northdata.de | — | High | Low |
| E3 | FACT | 商业登记经营范围："Die Planung, die Herstellung, der Vertrieb und die Montage von Anlagen zur Wasser- und Abwasserbehandlung…"（水与废水处理设备的**规划、制造**、销售与安装；化学技术产品进出口；水技术领域服务） | northdata.de（转引 Handelsregister） | — | Medium | **High** |
| E4 | FACT | WZ 2025 行业分类：C.28.29.0 其他非行业专用机械制造 | firmendata.com | — | Low | Medium |
| E5 | FACT | 1976 年成立（firmendata 记 1980，**口径冲突**）；1996 年总部迁至德国；经营范围含"自有液体药剂生产" | 维基百科 Envirochemie 条目；firmendata.com | — | Low | Low |
| E6 | FACT | 隶属 SKion Water GmbH（Bad Homburg），最终由 Susanne Klatten 的 SKion GmbH 全资持有；SKion Water 集团含 Ovivo、EnviroChemie、ELIQUO、Paques 等，集团营业额约 6.5～7 亿欧元 | skion.de 官网新闻；bluetechforum.com | — | High | Medium |
| E7 | FACT | 官网自述"more than 50 years"；2026-06-13 举办 50 周年庆典 | 官网新闻 | — | High | Low |
| E8 | FACT | 2026-06-01 管理层扩充：Dr Robert Lutze 任 Managing Director（Plant Engineering，含 Sales & Process Design 与 Project Execution）；Ulrich Böhm 任 Managing Director（Services）；Stefan Letschert 为 CFO | 官网新闻稿 2026-06-01（cision 官方发布同文） | — | High | **High** |
| E9 | FACT | 员工数**口径冲突**：登记数据 1,080（2023）/ 出口数据库 1,500 与 1,600 / B2B 平台 101-200 / 维基 500（2018） | firmendata；deutsche-exportdatenbank；diedeutscheindustrie；prospeo；维基百科 | — | Low | Medium |
| E10 | FACT | 营业额 €227.2M（2023）/ €209.9M（2022）/ €200.8M（2021）/ €160.7M（2020）；**2023 亏损 -€7.7M、2022 亏损 -€7.9M**（2021、2020 盈利） | firmendata.com（转引公开年报数据） | — | Low | **High** |
| E11 | FACT | 公司不再单独公布年报，已并入 Enviro Mondial GmbH 集团合并报表 | northdata.de | — | Medium | Medium |
| E12 | FACT | Roßdorf 总部自建**液体水处理药剂生产车间**（混合与灌装），800 m²，日产 30 t（混凝剂、絮凝剂、调理剂、消毒剂、抑制剂、中和剂）；2015 年初投运 | foodprocessing-technology.com（转载公司新闻稿） | — | Medium | **High** |
| E13 | FACT | 2017-07 起扩建 Roßdorf 总部：新建 2,100 m² 三层办公楼（供 85 名员工），选址为**原装配车间**所在地；同期声明"新技术中心与化学品生产设施现已全面投运" | pharmaceutical-networking.com（转载公司新闻稿） | — | Medium | High |
| E14 | FACT | 设自有工艺实验室、技术中心与中试装置，客户定制方案可在自有技术中心或中试装置中测试；产品在德国与瑞士三个基地开发与供应 | chemeurope.com / bionity.com（引用公司简介） | — | Medium | **High** |
| E15 | FACT | 技术线为物理化学、生物、膜技术；**AOP 采用 H₂O₂ + UV（Envochem AOP）与臭氧**；另有离子交换、气浮、ZLD、厌氧沼气（Biomar）；制药废水与 PFAS 为重点场景 | pharmaceutical-networking.com；wateronline.com | — | Medium | **High** |
| E16 | FACT | 公司自述「**verfahrensoffen**」（工艺开放），在自有实验室与中试装置中试验不同 AOP 工艺 | processtechnology.wiley.com（引用公司人士表述） | — | Medium | **High** |
| E17 | FACT | 业务结构：设备工程 62% / 服务与水化学 26% / 设施运营 12%（2023） | firmendata.com | — | Low | Medium |
| E18 | FACT | 公开采购记录：承接 HIM GmbH（Bereich Altlastensanierung）"ASG/92/602 Betrieb und Wartung WAA"（**污水处理设施**运营与维护），07/2025–06/2028，含 07/2028–06/2029 选项；采购日期 2025-10-29 | firmendata.com（转引德国招标数据） | — | Low | **High** |
| E19 | FACT | 公开采购记录：承接 HIM GmbH "ASG/99/249 Betrieb und Wartung GWRA"（地下水治理设施运营与维护）；采购日期 2025-07-07 | firmendata.com | — | Low | High |
| E20 | FACT | 2026 年官网项目群：西班牙 300 MW 电解水高纯水（2 个 EnviModule）；瑞典新钢厂重金属离子交换直排；荷兰 Chemours Dordrecht PFAS 去除；比利时纤维水泥硫酸盐去除；德国能源公司 Knapsacker Hügel 蒸发冷凝液约 480 m³/d；奥地利制药厂 Envochem UFI 约 35 m³/d；奥地利 Wuppermann 钢铁加工废水 Envochem COL HD 约 120 m³/d；德国奶酪厂 715 m³/d；阿尔及利亚 Laiterie Soummam 5,000 m³/d；德国化妆品厂 60 m³ 含水回用；德国马铃薯加工厂 1,800→2,300 m³/d 扩容（含现场运营，2028 完成） | 官网 news-events；wateronline.com | — | High | **High** |
| E21 | FACT | 2026-06 获保加利亚矿业与地质协会（BMGK）"矿产资源行业贡献奖" | 官网新闻 | — | High | Low |
| E22 | FACT | 自述资质：ISO 9001 / 14001 / 50001 / 45001；符合 WHG §62 专业公司资质；VDMA / DWA / DGMT 会员 | 第三方转述资质页；pharmaceutical-networking.com | — | Low | Medium |
| E23 | FACT | 集团实体清单：德国 EnviroFALK、EnviroDTS、EnviroFALK PharmaWaterSystems；海外 EnviroChemie BV（荷兰）、Ges.m.b.H.（奥地利）、Bulgaria EOOD、AG Abwassertechnik（瑞士）、Polska、Maghreb、DiAqua Technology SRL（罗马尼亚）、do Brasil | 官网 Locations & Contact | — | High | Medium |
| E24 | UNKNOWN · searched | 环保处罚记录（德国联邦 / 州层面） | — | 已检索未查到 | — | Medium |
| E25 | UNKNOWN · searched | BImSchG 许可 / 水法许可（wasserrechtliche Erlaubnis） | — | 已检索未查到 | — | Medium |
| E26 | UNKNOWN · searched | 环评 / UVP 公示 | — | 已检索未查到 | — | Low |
| E27 | UNKNOWN · searched | 公司自身污水排放数据（水量、水质） | — | 已检索未查到 | — | Low |
| E28 | UNKNOWN · searched | 环保 / 工艺岗位招聘信息 | — | 已检索未查到 | — | Low |
| E29 | UNKNOWN · searched | 与 BDD / 电化学氧化相关的既有技术路线或合作方 | — | 已检索未查到 | — | **High** |
| E30 | UNKNOWN · searched | 中东实体现状（2018 年资料曾列 EnviroChemie FZCO·迪拜机场自贸区；现行官网未列） | — | 已检索未查到 | — | Low |
| D1 | INFERENCE（V1 已弃用） | ~~Roßdorf 化学品生产与中试装置运行**可能**产生清洗类工业废水~~ | — | **V1.1 弃用**：Partner Path 不以自身废水为主要判断依据（硬约束 6）；该推断亦为 Confidence Low 且无官方来源确认 → **不再作为任何判据** | Low | Low |
| E31 | INFERENCE | 其现有 AOP 产品线（UV / H₂O₂、臭氧）与电化学氧化所面向的目标污染物类型**存在场景重叠**（难降解有机物、API 残留、PFAS 等） | — | 依据 E15 / E16 / E20：官网项目清单载明的污染物类型与电化学氧化典型应用场景重合；公司自述工艺开放。**此为场景重叠的事实观察，不构成任何技术可行性判断** | Medium | **High** |
| E32 | INFERENCE | 其自有 AOP 产品线与 BDD 目标场景重叠 → 构成 **Conflict: 潜在竞争** | — | 依据 E15：自有 AOP 产品线（UV/H₂O₂、臭氧）与 BDD 同属难降解有机物氧化的技术路线；按 `opportunity-type-rules.md` 第三节必须显式标注 | Medium | **High** |

**类型定义**：FACT 必须有 Source；INFERENCE 必须有 Reason + Confidence；UNKNOWN 必须带三态后缀且不得补全。

**Decision Impact**：只影响展示优先级，不影响真实性判断。

**可溯源率**：23 / 23 = **100%**

**UNKNOWN 说明**：E24～E30 为 **`searched`**（已按允许渠道检索未查到），**非"不存在"**。德国的环境监管记录不通过统一公开数据库发布，本次未能定位到许可与处罚公示入口。**不得解读为"该公司无环境问题"。**
**V1.1 变化**：新增 **D1** 记录 V1 中被用作判据、V1.1 已弃用的推断项（弃用原因：违反 Partner Path 口径硬约束）。

</details>

---

## 边界声明

本次执行未输出：工艺参数、设备选型、技术方案、达标承诺、金额（公司公开财务与项目数据除外）、报价状态、回复草稿、跟进节奏、客户案例名单。
`Technical Fit` 与 `Quotation Readiness` 按范围冻结规定**不输出**。
**未输出"建议小试"，未固定"寄 5~10 L 水样"**（V1.1 已删除该越界规则）。
**未采信**：B2B 数据聚合站（prospeo.io）列出的具名生产负责人及手机号 —— 不在允许来源清单内，已整体弃用。