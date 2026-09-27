# Festo · BDD Customer Intelligence

2026-09-27 | 来源：公司名 + 官网 `https://www.festo.com/`（未提供联系人、无询盘原文、无往来记录）
执行版本：BDD Customer Intelligence Skill V1.1.3（FW Rule Patch）

### 01 WHO ｜客户是谁

| 字段 | 判定 |
|---|---|
| **公司 Company** | FESTO SE & CO. KG（德国）· Verified⟪P2⟫总部 Esslingen am Neckar（Baden-Württemberg，Ruiter Strasse 82）；1925 年创立；**独立家族企业**（Stoll 家族）；管理委员会主席 Thomas Böck；两大板块 Automation 与 Didactic |
| **国家 Country** | 德国 · 集团总部 Esslingen am Neckar⟪P2⟫生产厂区分布于德国（Esslingen-Berkheim、St. Ingbert-Rohrbach、Osnabrück）、瑞士、匈牙利、保加利亚、捷克、乌克兰、印度、中国（上海 / 济南）、新加坡、巴西、美国；2025 年新开印度 Krishnagiri 工厂 |
| **主营业务 Business** | 工业自动化技术制造商（气动、电伺服气动与电气自动化）与工业技术教育提供商⟪P2⟫约 36,000 种目录产品、服务 35+ 行业；集团 2025 财年营业额 €3.33 十亿（同比 −3.7%），员工约 20,600 人，研发投入占营业额 9.5% |
| **客户类型 Customer Type** | 终端业主 · End-user |

### 02 WHY ｜为什么值得看

| 字段 | 判定 |
|---|---|
| **行业匹配 Industry Match** | ⚪ Unknown（T3 证据门槛未过；不属 T1 / T2 / T4，亦非 A1~A3）⟪P2⟫原判 `Target`（按 T3 高 COD / 难降解性质口径）经 Patch A 复核**不成立**：公开证据只证明「铝阳极氧化（表面处理）+ 压铸 + 机加工产生工业废水」，**未载明**高 COD / 难降解 / 难生物降解 / 难处理 / 深度处理 / 高级氧化需求 / 明确复杂污染物 —— 属 T3 硬规则列举的「只存在阳极氧化废水 / 机加工废水 / 压铸废水 / 普通表面处理废水」情形，**不得判 `Target`**。亦不属 A1 工业废水 EPC·AOP·集成 / A2 工业化学品·水处理药剂分销 / A3 设计院·院所；因确有工业废水，不能正面确证为 `Outside`（非涉水行业）→ 落 `Unknown` |
| **BDD机会 BDD Opportunity** | ⚪ Unknown · End-user Opportunity |
| **需求状态 Demand Status** | 🟡 Potential |

### 03 WHERE / WHO ｜从哪里切入

| 字段 | 判定 |
|---|---|
| **现有废水处理 Current Treatment** | 🟡 部分确认 Partial · 官网明确：只将受污染废水排入公共下水道系统，生产废水在排放前按工艺特定污染物处理，处理设施持有必要许可并监测污染物参数⟪P2⟫官网另载：除未受污染雨水外不向自然水体或地下水排放；并有废水资源化措施（优化产生废水的工艺并回用废水）与济南厂区阳极氧化线。**仅披露"存在持证处理设施并按污染物参数处理"，未披露具体工艺单元** |
| **优先厂区 Priority Site** | **Krishnagiri（印度 · 泰米尔纳德邦）** · 权重 2 命中 —— 2025 年新建投产的生产厂（一期 2025-06 启用、二期已预留土地），属新增产能项目窗口⟪P2⟫权重 2 依据：Festo India 官方通知与行业媒体专访载明新厂定位为过程自动化与不锈钢部件、一期已投运、二期已预留土地；另有土耳其与墨西哥新增产能规划。备选：**Jinan（中国 · 山东）**——2021-04 全面投运的中国最大生产基地，含**阳极氧化线**与铝压铸，涉水工艺密度全集团最高 |
| **关键联系人 Contact** | 集团环保 / 环境管理负责人（首选）→ 优先厂区 Krishnagiri 工厂环保 / EHS 负责人（落地接触点）→ 集团生产 / 技术负责人⟪P2⟫首选岗位负责确认目标厂区与集团层面项目机制。No verified contact found —— 未查到现行具名环保 / EHS 负责人（Festo 曾于 2009 年环境报告公布环保联系人，**距今已逾 15 年，不作具名依据**）。官网披露具名高层 **Thomas Böck（Chairman of the Management Board）**（Source：《Sustainability Report Compact 2025》署名），属集团最高层，非首选接触岗位 |

### 04 ACTION ｜现在怎么办

| 字段 | 判定 |
|---|---|
| **待确认信息 Missing Info** | [Business] ① 需求方与决策链归属（集团总部还是各生产厂区自行决定）② 是否存在废水治理 / 提标预算与责任部门⟪P2⟫　[Project] ③ 是否存在具体废水治理 / 提标 / 新建项目及目标厂区（尤其印度新厂二期与济南厂）④ 项目阶段与时间节点　[Technical] ⑤ 目标厂区生产废水的水质类型与特征污染物 |
| **下一步 Next Action** | 先向集团环保部门与印度 Krishnagiri 新厂、济南厂区环保负责人确认需求方归属，并核实是否存在具体废水治理或提标项目及目标厂区；若确认存在项目，转交技术评估流程 |

> **开发建议 Sales Conclusion**
>
> 🟡 **建议先验证**
>
> `Industry Fit` 经 Patch 收紧后落 `Unknown`（T3 性质证据缺失），`BDD Relevance` 随之落 `Unknown` —— **未识别出 BDD 可切入场景**；公开证据只到「有制造 + 有生产废水 + 有持证处理设施 + 有污染物监测」这一层，**未见高 COD / 难降解 / 高级氧化 / 常规处理受限等与 BDD 场景直接相关的信号**，故先验证「是否存在 BDD 适用场景」⟪P2⟫（需求侧仍为 `Potential`：官网按财年披露生产废水量并载明处理、许可与监测；**无商业风险与财务困境证据**；业务变化信号仅作背景与观察项，不作降档依据）。**本档位由规则机械重算，非人工指定**

**BDD Opportunity 判定依据**

- **Reason**：End-user Path。① `Industry Fit = **Unknown**` ✗ —— Patch A 后 T3 须过证据门槛：本例只有铝阳极氧化（表面处理）、压铸、机加工工业废水，**未见高 COD / 难降解 / 难处理 / 深度处理 / AOP 需求等废水性质证据**，故不得判 `Target`；亦不属 T1 / T2 / T4 与 A1~A3 ② **制造业活动已确认**（14 个全球生产中心；已知制造厂区含德国 Esslingen-Berkheim 与 St. Ingbert-Rohrbach、瑞士 Pieterlen、匈牙利 Budapest、保加利亚 Sofia、捷克 Česká Lípa、乌克兰 Simferopol、印度 Bangalore 与 Krishnagiri、中国上海与济南、新加坡、巴西 São Paulo、美国 Hauppauge）✔ ③ **PWE 成立**（官网可持续报告按财年披露生产废水与总排水量，并明确生产废水排放前按工艺特定污染物处理、处理设施持照并监测污染物参数；另有 2009 年度环境保护报告按厂区列示水耗与废水章节）✔ ④ **主体级证据 ≥ 2 项**：生产废水处理与许可披露（E8 / E9）+ 水与废水资源化措施（E10）+ 厂区级环境报告体系与 ISO 14001（E11 / E12）+ 三年排水趋势与节水措施（E19 / E10）✔ —— 但 **条件 ① 不成立**：`High` 与 `Medium` 均要求行业对口 → 落 `Unknown`。**另核**：本例与废水相关的证据全部达**一般性**层级（制造业 / 废水产生 / 处理设施 / 排污许可 / 用水量 / 通用 ESG 水声明），**无任何 BDD-specific 污染物或处理难点**（具体处理工艺单元亦未披露，E21）→ `BDD Opportunity = Unknown`，**不得因「有工业废水」升格**
- **Evidence**：E7 / E8 / E9 / E10 / E11 / E12 / E19（**均不构成 BDD-specific 证据**；E21 载处理工艺单元未披露）
- **Confidence**：High
- **Opportunity Type**：**End-user Opportunity**

**Demand Status 明细**

- **Public Wastewater Evidence**：🟡 Potential — 官网可持续报告 2025 按财年披露生产废水量与总排水量，并明确生产废水排放前按工艺特定污染物处理、处理设施持有必要许可、监测处理与污染物参数；2021 年报告载有济南阳极氧化装置投产与废水回用措施；三年排水量持续上升（194,042 → 216,502 → 231,701 m³）。**均为官网环境披露级（间接信号）**，**无文件级项目证据、近 12 个月无硬性外部信号** → 按 `evidence-policy.md` 4.2 落 `Potential`
- **Customer-stated Demand**：⚪ Unknown · not searched — 本次无询盘文字
- → **取较高者：Potential**

**风险**

- **Commercial Risk**：⚪ Unknown
- **Risk Note**：本次无往来内容可供观察索取行为。**近 12 个月未查到环保处罚、排污许可变更或环评公示记录**（E20）
- **Financial Warning**：⚪ **Unknown**
  - **判定依据（按 `evidence-policy.md` 6.1 白名单逐项核对）**：**未命中任何财务困境证据** —— 无资不抵债 / 破产 / 流动性危机 / 债务违约 / 持续经营重大疑虑 / 法院或债务层面财务重组；亦未见监管披露的重大财务困难（E2 / E17）
  - **为何不是 `No`**：Festo 为**家族全资持有的非上市企业**，**无公开财务报表可供核验**（仅有官网披露的营业额口径），按 `evidence-policy.md` 6.1「无公开财务信息 → `Unknown`」处理。**`Unknown` 不导致降档**
  - **已知财务事实（如实记录）**：2025 财年营业额 €3.33 十亿，**同比 −3.7%**；区域分化明显（北美 / 南美 / 欧洲除 DACH 小幅增长，印度增长最强，中国与东南亚 / 韩日小幅下滑，DACH 停滞）—— 营收下滑**不属于 6.1 白名单任何一项**，仅记录

**业务变化（Context / Watch Item，不参与降档）**

- **Business Change Signal**：🟡 **Yes**
- **Reason**：① **新增产能（印度）**：2025 年在印度泰米尔纳德邦 Krishnagiri 新建生产厂，2025-05-05 起切换供货、**2025-06 一期正式启用**，二期已预留土地；产品聚焦过程自动化与不锈钢部件（气缸等机械类），暂不产电子件；② **产能布局调整**：规划在**土耳其与墨西哥**新增产能，官方口径为"local for local"本地化制造战略；③ **职能中心新建**：2026-02 在班加罗尔启用集团首个全球能力中心（GCC）；④ **区域表现分化**：2025 年营业额同比 −3.7%，增长最强来自印度，中国市场小幅下滑；⑤ **集团治理层**：管理委员会主席为 Thomas Böck
- **Source**：Festo India 官方通知文件（2025-03-18）；官网新闻稿（2025 财年业绩）；行业媒体专访（Festo 管理委员会成员 Frank Notz）；印度主流媒体（The Hindu，2026-02）；《Sustainability Report Compact 2025》
- **用途（硬规则）**：**只作 Context / Watch Item** —— 不触发 `Financial Warning = Yes`、不触发 `Commercial Risk = High`，也不导致 `Sales Conclusion` / `BDD Opportunity` / `Demand Status` 降档（`evidence-policy.md` 7.3）

---

## 第二层 · 附录 A · Evidence 明细

<details>
<summary>附录 A · Evidence 明细（22 条）</summary>

| # | 主题 | 类型 | 结论 | Source | Reason | Confidence | Decision Impact |
|---|---|---|---|---|---|---|---|
| E1 | 主体登记与企业性质 | FACT | Festo SE & Co. KG；总部 Esslingen am Neckar（Baden-Württemberg，Ruiter Strasse 82，德国）；1925 年创立；**独立家族企业**（Stoll 家族）；两大业务板块 Automation 与 Didactic | 官网 Facts and figures；《Sustainability Report Compact 2025》；第三方公司资料 | — | High | **High** |
| E2 | 集团规模与营业额 | FACT | 2025 财年营业额 **€3.33 十亿**（同比 −3.7%）；员工约 **20,600 人**（德国 8,200 / 海外 12,400）；研发投入占营业额 **9.5%**；全球约 250 个分支机构、覆盖 176 个国家 | 《Sustainability Report Compact 2025》；官网新闻稿 | — | High | **High** |
| E3 | 业务板块与产品 | FACT | 两大板块：**Automation**（气动、电伺服气动与电气自动化技术、软件与 AI 方案）与 **Didactic**（学习系统、培训与咨询）；约 36,000 种目录产品；服务 35+ 行业（含汽车、食品包装、电子、半导体、生命科学、制药、化工、**水处理**、绿氢等） | 官网 Facts and figures；《Sustainability Report Compact 2025》 | — | High | Medium |
| E4 | 全球制造网络规模 | FACT | 集团可持续报告载：**14 个全球生产中心**；另有 10 个物流中心、58 个工程中心、26 个体验中心 | 《Sustainability Report Compact 2025》 | — | High | **High** |
| E5 | 已知制造厂区清单 | FACT | 制造 / 装配厂区含：德国 Esslingen-Berkheim、St. Ingbert-Rohrbach、Osnabrück（polyvanced）；瑞士 Pieterlen（Festo Microtechnology）/ Biel；匈牙利 Budapest；保加利亚 Sofia；捷克 Česká Lípa；乌克兰 Simferopol；印度 Bangalore；中国 Shanghai 与 Jinan；新加坡；巴西 São Paulo；美国 Hauppauge（NY） | Festo《Annual Environmental Protection Report 2009》厂区清单；Festo 公司简介（2016，11 个全球生产中心） | — | Medium | **High** |
| E6 | 济南厂区沿革与规模 | FACT | 2007 年收购济南华能气动元器件公司；2017 年向济南政府购置 **43 万 m²** 土地规划工业 4.0 新厂；2019-01 一期启用；**2021-04 济南全球生产中心全面投运**，为 Festo 中国最大生产基地；费斯托（中国）2021 年获批跨国公司地区总部 | 行业媒体（弗戈工业在线）；公开资料 | — | Medium | **High** |
| E7 | 生产工序与涉水环节 | FACT | 官网可持续报告载：**生产用水占总用水量 30.0%**；2021 年报告载"**济南（中国）阳极氧化装置投产**"使生产用水占比不成比例上升；另披露铝压铸（压铸炉铝渣 / 铝灰回收再利用）与气缸、电子元件制造 | 《Sustainability Report Compact 2025》；《Sustainability Report 2021》 | — | High | **High** |
| E8 | 生产废水量与取排水数据 | FACT | 官网可持续报告 2025 财年（2024-10 至 2025-09）：排水 **生产废水 82,185 m³**、生活污水 100,386 m³、冷却 / 空调 21,480 m³、其他 27,650 m³，**合计 231,701 m³**；取水合计 **315,630 m³**（地下水 15,233 + 公共供水 300,397 m³） | 《Sustainability Report Compact 2025》 | — | High | **High** |
| E9 | 生产废水处理与许可（PWE 核心） | FACT | 官网可持续报告载：「**我们只将受污染的废水排入公共下水道系统。我们的生产废水在排放前按工艺特定污染物进行处理。我们为所有处理设施持有必要许可，并对处理过程与污染物参数进行监测。除未受污染的雨水外，我们不向自然水体或地下水排放任何废水。**」（GRI 303-3 / 303-4） | 《Sustainability Report 2021》 | — | High | **High** |
| E10 | 废水回用与节水措施 | FACT | 官网载："在可能的情况下，我们优化产生废水的生产工艺，并将废水回用于其他用途"；2021 年总部冷却方式改造为低耗水混合冷却器，年节水 3,000–4,000 m³ | 《Sustainability Report 2021》 | — | High | Medium |
| E11 | 厂区级环境报告体系 | FACT | Festo 曾发布《Annual Environmental Protection Report》，**按厂区逐一列示**能源消耗、**水耗与废水**、排放与废弃物章节，并载明各生产厂区按 ISO 14001 建立国际环境管理体系 | Festo《Annual Environmental Protection Report 2009》 | — | Medium | Medium |
| E12 | 环境管理体系与认证 | FACT | 集团自 **1999 年起获 ISO 14001 认证**（1996–2002 年为 EMAS I）；**15 个厂区通过 ISO 14001**、15 个通过 ISO 9001、2 个通过 OHSAS 18001、9 个通过 ISO 13485 | 官网 Facts and figures | — | High | High |
| E13 | SBTi 与气候目标 | FACT | 2025 年 SBTi 验证其 Scope 3 减排目标（含产品使用阶段）；持续按产品碳足迹（PCF）方法推进全产品组合数据建设 | 《Sustainability Report Compact 2025》 | — | High | Medium |
| E14 | 印度新建工厂（业务变化核心） | FACT | 2025-03-18 通知客户：新制造基地设于**印度泰米尔纳德邦 Krishnagiri 区（Bairamangalam-635113）**，自 **2025-05-05** 起由新厂供货；**2025 年 6 月一期（Phase I）正式启用**，已预留土地规划二期；产品为气动与过程自动化组合（气缸等机械类产品，**聚焦过程自动化与不锈钢部件**），暂不生产电子件；另有**土耳其与墨西哥**新增产能规划 | Festo India Private Limited 官方通知文件（2025-03-18）；行业媒体专访（Festo 管理委员会成员 Frank Notz） | — | High | **High** |
| E15 | 印度新厂对取水的影响 | FACT | 官网可持续报告载：地下水取水量上升，**主要因印度新工厂投产**，该厂大部分用水需求由地下水覆盖 | 《Sustainability Report Compact 2025》 | — | High | **High** |
| E16 | 印度全球能力中心 | FACT | 2026-02 在班加罗尔启用集团首个全球能力中心（GCC，71,000 平方英尺，已聘 250+ 人，2030 年目标 600–800 人），承担工程、数字方案、软件与数据分析 | 印度主流媒体（The Hindu） | — | Medium | Medium |
| E17 | 2025 财年区域表现 | FACT | 官网新闻稿载：2025 年营业额同比 −3.7%；北美、南美与欧洲（除 DACH）小幅增长；**增长最强来自印度市场**；中国、东南亚、韩国、日本小幅下滑；DACH 本土市场停滞 | 官网新闻稿 | — | High | Medium |
| E18 | 集团治理层 | FACT | 管理委员会：**Thomas Böck（主席 / CEO）**、Dr. Frank Melzer（产品与技术）、Dr. Jaroslav Patka（财务与人力）、Gerhard F. Borho（IT 与数字化）、Ansgar Kriwet（销售） | 《Sustainability Report Compact 2025》署名；第三方公司资料 | — | High | Medium |
| E19 | 三年取排水趋势 | FACT | 总取水 277,795 → 303,579 → **315,630 m³**（2023 / 2024 / 2025 财年）；总排水 194,042 → 216,502 → **231,701 m³**；其中**生产废水 73,737 → 80,336 → 82,185 m³** —— 三年持续上升 | 《Sustainability Report Compact 2025》 | — | High | **High** |
| E20 | 近 12 个月环境处罚与许可记录 | UNKNOWN · searched | 近 12 个月（2025-09 至 2026-09）Festo 集团及各生产厂区的**环保处罚 / 排污许可变更 / 环评公示**公开记录 —— 已按允许渠道检索未查到 | — | 已检索官网、可持续报告、行业媒体与公开监管渠道 | — | **High** |
| E21 | 废水处理工艺单元 | UNKNOWN · searched | 各生产厂区生产废水的**具体处理工艺单元与组合**（采用何种处理技术）—— 已检索官网可持续报告、年度环境报告摘要与公开渠道，仅见"按工艺特定污染物处理"的概括表述，**未见单元级披露** | — | 已检索官网与公开渠道 | — | **High** |
| E22 | 具体废水项目与决策链 | UNKNOWN · not searched | 是否存在可纳入评估的具体废水治理 / 提标 / 新建项目；集团总部与各生产厂区之间的资本开支决策链归属 | — | 无客户陈述、无项目文件可查 | — | **High** |

</details>

---

## 附录 B · 审计信息（仅 Markdown，不进入业务 PDF）

**类型定义**：FACT 必须有 Source；INFERENCE 必须有 Reason + Confidence；UNKNOWN 必须带三态后缀且不得补全。

**Decision Impact**：只影响展示优先级，不影响真实性判断。

**可溯源率**：FACT 19 / FACT 总数 19 = **100%**

**集团级 vs 厂区级说明**：E6 / E7 / E14 / E15 / E16 为**厂区级或基地级**事实；E1 / E2 / E3 / E4 / E8 / E9 / E10 / E12 / E13 / E17 / E18 / E19 为**集团级**事实；E5 为**厂区清单级**事实（来源为 2009 年年度环境报告，**年份较早，仅供厂区名单参考**）；E11 为**报告体系级**事实。**三者不得混写** —— 例如 E8 / E19 的取水量与排水量为**集团合计口径**（报告未按厂区拆分），**不得写成任一厂区数据**；E15 明确把地下水取水上升归因于印度新厂，但**未给出该厂单独取水量**，不得据此推算厂区数值。

**同名主体排除**：本次未发现需排除的无关同名主体。需注意区分：① **Festo SE & Co. KG**（德国 Esslingen，集团母体）；② **Festo Didactic SE**（德国 Denkendorf，教育板块法人）；③ **Festo India Private Limited**（印度，含 Krishnagiri 新厂）；④ **Festo (China) Ltd. / Festo Production Ltd.**（上海）与济南生产基地；⑤ **Festo Microtechnology AG**（瑞士 Pieterlen）与 **polyvanced GmbH**（德国 Osnabrück / 捷克 Česká Lípa）—— 均为集团成员。另需排除：中国市场另有名称近似的自动化企业（如"费斯托"中文译名对应的同名混淆），本次检索命中均指向上述德国集团。

**来源冲突项**：① **生产中心数量**：官网新闻稿（较早）载"22 个生产中心"、公司简介（2016）载"11 个全球生产中心"、可持续报告 2025 载"**14 个全球生产中心**"—— 照录三个口径，未择一采信，主卡采用最新（2025）口径 ② **员工数口径**：约 20,000+ / 20,600 / 20,608（不同来源）③ **ISO 14001 认证厂区数**：官网中英文页面分别载"15 个驻地通过"与"3 个分公司通过"（口径与年份不同）—— 照录未择一。**以上均不影响任何判定字段。**

**UNKNOWN 三态汇总**：`UNKNOWN · searched` 2 条（E20 环境处罚与许可记录、E21 废水处理工艺单元）；`UNKNOWN · not searched` 1 条（E22 具体项目与决策链）；`UNKNOWN · no source` 0 条。

**BDD-Specific Relevance Gate 判定（Patch 2026-09-27 · 仅作用于 End-user `High`）**：**`Weak`**
- **命中的「一般性」证据**：制造业活动（E4 / E5）、废水产生（E8 / E19）、持证处理设施与排放许可（E9）、用水量数据（E8 / E19）、通用 ESG 水声明（E11 / E12）。
- **未命中任何 BDD-specific 信号**：无高 COD、无难降解 / 难生物降解、无持久性有机污染物、无高级氧化（在用或评估中）、无常规处理受限、无深度处理需求、无明确难处理污染物（具体处理工艺单元亦未见披露，E21）。
- → `Weak` → 按 `bdd-relevance-rules.md` 第三节映射，End-user `BDD Opportunity` 上限 `Medium`；本例因 **条件 ①（Industry Fit = Target）不成立**，`Industry Fit = Unknown` 的封顶**优先于** Gate 映射 → 最终 `Unknown`。
- **`Industry Match`（Patch A）**：T3 证据门槛**未过**；不属 T1 / T2 / T4；不属 A1~A3；因确有工业废水，不能正面确证 `Outside` → `Unknown`。
- **`Sales Conclusion` 路径**：第 1 步一票否决（`Commercial Risk = Unknown` ≠ `High`；`BDD Relevance = Unknown` ≠ `Low`）不触发 → 第 2 步要求「`Relevance = Unknown` **且** `Demand Status` 无任何证据」，本例 `Demand = Potential`（有证据）故**不触发** → 第 3 / 4 步均要求 `High` / `Medium`，不触发 → **第 5 步「其余情况」→ `建议先验证`**。
- **`Opportunity Type` 未改动**（`End-user Opportunity`）：本 Patch 禁止修改 `Opportunity Type`；其分类依据为客户类型与 Path，未变。**已在报告「Observation / TBD」中登记该处语义不一致。**

**证据强度提示**：E5（厂区清单）来源为 2009 年年度环境报告，**年份较早**，Confidence 标 `Medium`，且**未用于** `BDD Relevance` 的 Evidence 列表（该列表使用 2025 年报告的 14 个生产中心口径）；E6 / E11 / E16 来源为行业媒体或早期报告，Confidence 标 `Medium`。

**判定要点**：本主体为**自有 14 个全球生产中心的工业自动化设备制造商**，按 `customer-type-playbook.md` 判 `End-user`。`Industry Fit` 判 `Target` 的依据是 **T3 高 COD / 难降解工业废水性质口径**（铝阳极氧化属表面处理 / 电镀族工序，与压铸、机加工共同产生需按工艺特定污染物专门处理的工业废水），**不是**因"制造业"或"化工相关客户行业"而归类；T1 / T2 / T4 均不适用。`BDD Relevance` 判 `High` 的依据是"行业对口 + 制造业确认 + **PWE 成立** + 主体级证据 ≥ 2"四项**同时**满足；需强调其 PWE 强度主要来自**官网对生产废水处理、许可与污染物监测参数的明确披露**，而非来自项目信号。财务警示与业务变化**判定路径完全分离**：前者因无公开财务报表落 `Unknown`，后者仅记录新增产能与布局调整。

### 边界声明

本次执行未输出：工艺参数、设备选型、技术方案、达标承诺、金额、报价状态、回复草稿、跟进节奏、客户案例名单。
`Technical Fit` 与 `Quotation Readiness` 按范围冻结规定**不输出**。
**未输出"建议小试"，未固定"寄 5~10 L 水样"**（V1.1 已删除该越界规则）。
主卡 `Contact` 的具名信息来自 **Festo 官网可持续报告署名**（符合"官网来源"要求）；2009 年环境报告中的人名因**时效已逾 15 年**未采信；未输出电话、邮箱或个人联系方式。
`Sales Conclusion`、`Financial Warning` 与 `Business Change Signal` 均按 `sales-conclusion-rules.md` 与 `evidence-policy.md` 第六、七节的逐条规则匹配得出，未作主观调整。
