# Trinseo · BDD Customer Intelligence

2026-09-27 | 来源：公司名 + 公开检索（未提供联系人、无询盘原文、无往来记录）
执行版本：BDD Customer Intelligence Skill V1.1.3（FW Rule Patch）
**用途说明：本卡为 `Financial Warning Rule Patch` 的 Negative Control（负向对照）测试用例 —— 用于验证修复误报后，`Financial Warning` 仍能识别真实财务风险。**

### 01 WHO ｜客户是谁

| 字段 | 判定 |
|---|---|
| **公司 Company** | TRINSEO PLC（注册地爱尔兰，总部美国宾夕法尼亚州 Wayne）· Partially Verified⟪P2⟫原 NYSE 上市代码 TSE；2026-03-30 起自 NYSE 摘牌，转 OTC 交易（TSEOF）；运营主体含 Trinseo Deutschland GmbH 等 |
| **国家 Country** | 美国（集团总部）· 制造与销售覆盖欧洲、北美、亚洲⟪P2⟫欧洲厂区含德国 Schkopau / Stade / Rheinmünster、荷兰 Terneuzen / Hoek、比利时 Tessenderlo、芬兰 Hamina、瑞典 Norrköping、法国 Saint-Avold、意大利 Rho |
| **主营业务 Business** | 全球特种材料解决方案供应商，生产苯乙烯类聚合物、PC、PMMA/MMA 与苯乙烯-丁二烯胶乳⟪P2⟫下游覆盖包装、建材、汽车、纺织与医疗；三大板块：Engineered Materials、Latex Binders、Polymers / Plastics Solutions；15 个厂区涉及塑料颗粒处理 |
| **客户类型 Customer Type** | 终端业主 · End-user |

### 02 WHY ｜为什么值得看

| 字段 | 判定 |
|---|---|
| **行业匹配 Industry Match** | 🟢 Target⟪P2⟫（T4 精细化工 / 聚合物制造 + T3 高 COD / 难降解工业废水性质口径） |
| **BDD机会 BDD Opportunity** | 🟢 High · End-user Opportunity |
| **需求状态 Demand Status** | 🟡 Potential |

### 03 WHERE / WHO ｜从哪里切入

| 字段 | 判定 |
|---|---|
| **现有废水处理 Current Treatment** | ⚪ 未知 Unknown⟪P2⟫未查到任何厂区废水处理设施或工艺的公开披露。官网仅有**水管理类**披露：淡水取水量较 2017 基准下降 30%、2030 目标 −20%、站点级 water stewardship 计划、在 Louisville 站点安装排水口过滤器、在 Schkopau 改进粉尘收集 —— 这些**不构成废水处理单元的证据**，故状态判 `未知` |
| **优先厂区 Priority Site** | **Schkopau（德国 · 萨克森-安哈尔特州）** · 权重 3 + 权重 4 双命中，唯一有厂区级水体相关环境披露的制造基地⟪P2⟫权重 3 依据——官网德文公司页明确该站点运行**多套聚苯乙烯装置**（1999 投运，含 GPPS 均聚与 HIPS 接枝聚合）与**合成橡胶**装置，位于「化学三角」化工园区，制造密度高；权重 4 依据——官网明确披露该站点**改进粉尘收集**并取得 **OCS（Operation Clean Sweep®）外部认证**。备选：Terneuzen（荷兰）—— 50 万吨/年苯乙烯装置 + ABS 溶解中试装置 + OCS 认证 |
| **关键联系人 Contact** | 集团技术 / 可持续发展负责人（含环境事务）→ 目标厂区 EHS / 环保负责人⟪P2⟫Name: Han Hendriks ｜ Position: Chief Technology & Sustainability Officer ｜ Source: 官网新闻稿（2026-07，第 16 份可持续报告发布） |

### 04 ACTION ｜现在怎么办

| 字段 | 判定 |
|---|---|
| **待确认信息 Missing Info** | [Business] ① 重组期间是否仍审批新增环保类资本开支及其预算与决策权归属 ② 环保 / EHS 负责人是否变动⟪P2⟫（现由 DIP 融资金融人主导资本开支决策）　[Project] ③ 是否存在具体废水治理 / 提标 / 新建项目及目标厂区 ④ 项目阶段与时间节点　[Technical] ⑤ 目标厂区生产废水的水质类型与特征污染物 |
| **下一步 Next Action** | 先确认重组期间环保类资本开支的审批权与预算归属，以及是否存在具体废水治理项目与目标厂区；若确认存在项目，转交技术评估流程 |

> **开发建议 Sales Conclusion**
>
> 🟡 **建议先验证**
>
> 财务警示已触发且经四问判定**影响本次采购与付款能力**（风险主体即目标采购主体、处于 Chapter 11 保护），按规则上限降至本档⟪P2⟫（资本开支已压缩至每季约 $10 百万、流动性 $187 百万；若无财务警示，本卡将落「建议开发」—— 见附录 B 的对照计算）。此外需求状态仅为 Potential、现有处理方案未知，需先补 Project 级信息

**BDD Opportunity 判定依据**

- **Reason**：End-user Path。① `Industry Fit = Target`（T4 + T3 性质口径）✔ ② **制造业活动已确认**（欧洲 9 个以上厂区，含 Schkopau 多套聚苯乙烯与合成橡胶装置、Terneuzen 50 万吨/年苯乙烯装置、Stade PC、Rheinmünster 胶乳；15 个厂区涉及颗粒物处理）✔ ③ **PWE 成立**（官网环境披露级：排水口过滤器 + 站点级 water stewardship 计划 + 淡水取水量削减 30% + 厂区级 OCS 外部认证）✔ ④ **主体级证据 ≥ 2 项**：现有环境管理披露（E8/E9/E10）+ 主体与厂区事实（E4/E5）+ 政府与监管类文件（E11/E12/E13）✔ → 四项判据全部成立 → `High`
- **Evidence**：E4 / E5 / E8 / E9 / E10 / E11 / E12 / E13
- **Confidence**：High
- **Opportunity Type**：**End-user Opportunity**

**Demand Status 明细**

- **Public Wastewater Evidence**：🟡 Potential — 官网公开披露与排水 / 水体相关的环境管理措施与目标（排水口过滤器、淡水取水量削减、站点级水管理计划、厂区 OCS 外部认证），属**间接信号**；**无废水处理设施、排放数据或项目文件级证据**
- **Customer-stated Demand**：⚪ Unknown · not searched — 本次无询盘文字
- → **取较高者：Potential**

**风险**

- **Commercial Risk**：⚪ Unknown
- **Risk Note**：本次无往来内容可供观察索取行为。**近 12 个月未查到环保处罚或许可变更记录**（E22）。财务困境不计入本字段定级（`evidence-policy.md` 第五节只用可观察交互事实）→ 由 `Financial Warning` 承载
- **Financial Warning**：🔴 **Yes**
  - **判定依据（全部命中 `evidence-policy.md` 6.1 白名单，均为 FACT + 可靠公开 Source）**：
    - **第 5 项 · Going-concern warning**：2026-03-31 10-Q 按 ASC 205-40 明确结论 —— **对自报表发布日起一年内持续经营能力存在重大疑虑**（E12）
    - **第 4 项 · Debt default**：2026 Q1 未按期支付若干利息，宽限期届满未付，构成 Senior Credit Agreement 与 2L Notes Indenture 项下**违约事件并触发跨违约**，相关债务加速到期（E13）
    - **第 2 / 6 项 · Bankruptcy + Court-supervised financial restructuring**：2026-05-26 **主动申请第 11 章（Chapter 11）破产保护**；2026-05-13 签署重组支持协议，拟削减约 $20 亿债务、年利息费用减少约 $1.4 亿；现由**法院批准的 DIP（债务人持有）融资**支持运营（E16 / E17）
    - **第 3 项 · Liquidity crisis**：2026 Q1 经营活动现金流出 $232.9 百万、流动性仅 $114.2 百万；股东权益赤字 $1,222.9 百万、累计亏损 $1,455.2 百万（E11）
    - **第 8 项 · 官方披露的重大财务困难**：S&P 于 2026-03-20 将发行人信用评级下调至 **'D'（Default）**；NYSE 于 2026-03-30 生效摘牌（E14 / E15）
  - **结论**：`Yes`，无需复核口径 —— 五项白名单证据同时成立，**无任何集团层面正面财务事实可对冲**
- *(本卡不存在需要与财务警示并列记录的业务变化对冲突情形 —— 见下)*

**业务变化（Context / Watch Item，不参与降档）**

- **Business Change Signal**：🟡 **Yes**
- **Reason**：持续多年的资产关停与结构调整 —— 确认关闭德国 Böhlen 苯乙烯装置（30 万吨/年）与上游乙苯装置（33 万吨/年）；Stade 关停一条 PC 生产线；Hamina 的 SB 胶乳自 2023 年中减产；Matamoros PMMA 板材整合至美国 Florence；关闭意大利 virgin MMA 生产设施；重启 Americas Styrenics 出售流程；Tessenderlo 聚苯乙烯装置因极端风暴受损触发不可抗力；2026-01 新任命两名具债务重组经验董事
- **Source**：官网 2026 Q2 财报新闻稿；SEC 10-Q；Chemical Week（E6 / E7 / E19 / E20）
- **用途（硬规则）**：**只作 Context / Watch Item**。本卡中 `Financial Warning = Yes` **独立成立于五项白名单证据**，并非由业务变化推出 —— 两者互为印证但判定路径完全分开（`evidence-policy.md` 6.2 / 7.3）

---

## 第二层 · 附录 A · Evidence 明细

<details>
<summary>附录 A · Evidence 明细（22 条）</summary>

| # | 主题 | 类型 | 结论 | Source | Reason | Confidence | Decision Impact |
|---|---|---|---|---|---|---|---|
| E1 | 主体登记与上市状态 | FACT | Trinseo PLC，注册地爱尔兰，集团总部美国宾夕法尼亚州 Wayne；原 NYSE 代码 TSE，2026-03-30 生效摘牌后转 OTC 交易（TSEOF）；运营主体含 Trinseo Deutschland GmbH | 官网新闻稿；SEC Form 10-Q；公开报道 | — | High | **High** |
| E2 | 集团规模与营收 | FACT | 2026 Q1 净销售额 $724.7 百万；2026 Q2 净销售额 $845 百万（同比 +8%，主要由价格传导驱动，销量下降）；全球特种材料解决方案供应商 | SEC 10-Q（2026-03-31）；官网 2026 Q2 财报新闻稿 | — | High | High |
| E3 | 业务板块构成 | FACT | 三大板块：Engineered Materials（PMMA / MMA）、Latex Binders（苯乙烯-丁二烯胶乳）、Polymers / Plastics Solutions（聚苯乙烯、聚碳酸酯等） | 官网 2026 Q2 财报新闻稿；官网公司页 | — | High | Medium |
| E4 | 欧洲厂区清单 | FACT | 欧洲制造与中试厂区：德国 Schkopau（聚苯乙烯 + 合成橡胶）、Stade（PC）、Rheinmünster（胶乳）；荷兰 Terneuzen（苯乙烯 / ABS 中试）、Hoek；比利时 Tessenderlo（聚苯乙烯）；芬兰 Hamina（SB 胶乳）；瑞典 Norrköping（胶乳）；法国 Saint-Avold；意大利 Rho（PMMA 解聚示范） | 官网公司页与新闻稿；Chemical Week | — | High | **High** |
| E5 | Schkopau 装置情况 | FACT | Trinseo Deutschland GmbH 位于「化学三角」（Halle–Leipzig 之间）；Schkopau 站点运行**多套聚苯乙烯装置**（1999 投运），含 GPPS 均聚与 HIPS 接枝聚合两类产品 | 官网德文公司页 | — | High | **High** |
| E6 | Böhlen 苯乙烯装置关停 | FACT | 确认关闭德国 Böhlen 苯乙烯装置（300,000 吨/年）及上游乙苯装置（330,000 吨/年）；公司称原因为全球苯乙烯市场竞争地位不足、装置规模偏小、欧洲天然气价格高企 | Chemical Week（引公司声明） | — | Medium | Medium |
| E7 | 其他资产关停与整合 | FACT | Stade 关停一条 PC 生产线（保留下游复合业务）；Hamina SB 胶乳自 2023 年中减产；Matamoros（墨西哥）PMMA 板材整合至美国 Florence（肯塔基） | Chemical Week | — | Medium | Medium |
| E8 | 排水口控制措施（水体相关） | FACT | 官网载：Trinseo 为 Operation Clean Sweep® 成员；Tessenderlo、Terneuzen、Hoek、Schkopau、Saint-Avold 等厂区取得 **OCS 外部认证**；在 Louisville 站点**安装排水口过滤器（drain filters）**、在 **Schkopau 改进粉尘收集**，以减少颗粒物进入环境；多个厂区多年无重大或应报的塑料材料流失 | 官网 Sustainability · Responsible Operations | — | High | **High** |
| E9 | 水管理目标与绩效 | FACT | 2030 目标：淡水取水量较 2017 基准下降 20%；2024 年已实现 **−30%**；公司称厂区在可行处使用再生水以降低淡水取水量 | 官网 Sustainability · Responsible Operations | — | High | Medium |
| E10 | FY2025 可持续与水体管理目标扩展 | FACT | 官网披露：FY2025 为第 16 份年度可持续与 CSR 报告（《Shining Through Uncertainty》），参照 GRI 2021 通用准则并纳入 SASB 框架；达成原淡水目标后将水目标扩展为**站点级 water stewardship 长期韧性计划** | 官网新闻稿（2026-07）；chemXplore 转载 | — | High | Medium |
| E11 | 2026 Q1 财务状况 | FACT | 净销售额 $724.7 百万（同比 −8%）；净亏损 $115.9 百万；经营活动现金流出 $232.9 百万；流动性 $114.2 百万；总债务约 $27.7 亿；股东权益赤字 $1,222.9 百万；累计亏损 $1,455.2 百万；利息费用 $78.7 百万 | SEC Form 10-Q（2026-03-31） | — | High | **High** |
| E12 | 持续经营重大疑虑 | FACT | 按 ASC 205-40 评估，公司明确结论：**对自财务报表发布日起一年内的持续经营能力存在重大疑虑（substantial doubt）**；管理层的缓解措施包括与债权人谈判、临时豁免与修订及战略 / 财务替代方案 | SEC Form 10-Q（2026-03-31） | — | High | **High** |
| E13 | 债务违约与加速到期 | FACT | 2026 Q1 公司选择不支付若干利息，Senior Credit Agreement 与 2L Notes Indenture 项下宽限期届满未付，构成**违约事件并触发跨违约**（Refinance Credit Agreement、OpCo Super-Priority Revolver、AR Securitization Facility）；相关债务加速到期，几乎所有 $27.7 亿借款被重分类为流动负债 | SEC Form 10-Q；第三方研报 | — | High | **High** |
| E14 | 信用评级下调至违约级 | FACT | 2026-03-20 S&P Global Ratings 将 Trinseo 发行人信用评级由 'CCC-' 下调至 **'D'（Default）** | 第三方研报引 S&P 评级行动 | — | Medium | **High** |
| E15 | NYSE 摘牌 | FACT | NYSE 于 2026-03-02 启动摘牌程序（30 个交易日平均市值低于 $15 百万），2026-03-30 生效摘牌；股票转 OTC 交易，代码 TSEOF | 第三方研报；公开报道 | — | Medium | High |
| E16 | Chapter 11 与重组支持协议 | FACT | 2026-05-13 签署重组支持协议（RSA）：拟削减约 **$20 亿**债务、年利息费用减少约 **$1.4 亿**；**2026-05-26 主动申请第 11 章（Chapter 11）破产保护**；预期现有贷款人取得重组后公司 **100%** 股权、现有股东权益归零 | 第三方研报；公开报道 | — | Medium | **High** |
| E17 | DIP 融资与重组期运营 | FACT | 债务重组进程由**法院批准的 DIP（债务人持有）融资**支持；公司称在推进资产负债表重组的同时**按常规方式持续经营**，并履行对员工、供应商与其他客户的义务 | 官网 2026 Q2 财报新闻稿 | — | High | **High** |
| E18 | 2026 Q2 经营与现金流 | FACT | 净销售额 $845 百万（+8%）；净亏损 $120 百万（含 $89 百万税前费用，主要与贷款人谈判、重组成本与资产重组计划相关）；Adjusted EBITDA $81 百万；经营活动现金流出 $115 百万；资本支出 $10 百万；自由现金流 −$125 百万；期末现金 $198 百万（其中 $17 百万受限），总流动性 $187 百万 | 官网 2026 Q2 财报新闻稿 | — | High | **High** |
| E19 | 重组期资产处置与停产 | FACT | 关闭意大利 virgin MMA 生产设施；与合资伙伴重启 Americas Styrenics 出售流程；Tessenderlo 聚苯乙烯装置因严重风暴造成运营损伤而触发**不可抗力** | 官网 2026 Q2 财报新闻稿 | — | High | Medium |
| E20 | 董事会引入重组专家 | FACT | 2026 年 1 月公司任命两名具备债务重组与战略交易经验的新董事 | SEC Form 10-Q（2026-03-31） | — | High | Medium |
| E21 | 分管技术 / 可持续的高管 | FACT | Han Hendriks 为 Trinseo **Chief Technology & Sustainability Officer**，官网新闻稿具名（负责技术、可持续与循环解决方案） | 官网新闻稿（2026-07） | — | High | Medium |
| E22 | 近 12 个月环境处罚与许可记录 | UNKNOWN · searched | 近 12 个月（2025-09 至 2026-09）Trinseo 各厂区的**环保处罚 / 排污许可变更 / 环评公示**公开记录 —— 已按允许渠道检索未查到 | — | 已检索官网、SEC 文件、行业媒体与监管聚合渠道 | — | Medium |

</details>

---

## 附录 B · 审计信息（仅 Markdown，不进入业务 PDF）

**类型定义**：FACT 必须有 Source；INFERENCE 必须有 Reason + Confidence；UNKNOWN 必须带三态后缀且不得补全。

**Decision Impact**：只影响展示优先级，不影响真实性判断。

**可溯源率**：FACT 20 / FACT 总数 20 = **100%**

**集团级 vs 厂区级说明**：E4 / E5 / E6 / E7 / E8 / E9 / E10 为**厂区级或设施级**事实；E1 / E2 / E3 / E11 / E12 / E13 / E14 / E15 / E16 / E17 / E18 / E19 / E20 / E21 为**集团级**事实。**两者不得混写** —— 例如 E11 的股东权益赤字与债务规模属集团合并口径，不得写成任一厂区数据；E8 的排水口过滤器与粉尘收集措施为**特定站点**事实，不得外推至全部厂区。

**同名主体排除**：未发现需排除的无关同名主体。检索中出现的关联实体（Trinseo Deutschland GmbH、Trinseo Europe GmbH、Americas Styrenics LLC、Aristech Surfaces）经比对均为同一集团或已披露的合资 / 收购主体；另有历史名称 `Styron`（2010 年自 Dow 分拆时使用）属同一主体沿革。

**来源冲突项**：① 总部与注册地口径（公司注册地爱尔兰，集团总部与主要办公地美国宾夕法尼亚州 Wayne）② 时间口径（Chapter 11 申请日：第三方研报记为 2026-05-26，官网 Q2 财报称"继续推进由法院批准 DIP 融资支持的债务重组"）—— 以上照录各来源，未择一采信。

**UNKNOWN 三态汇总**：`UNKNOWN · searched` 1 条（E22）；`UNKNOWN · not searched` 0 条（本卡未做未检索类标注）；`UNKNOWN · no source` 0 条。

**对照计算（Negative Control 专用 · 证明 FW 仍在起作用）**

同一组字段下，仅改动 `Financial Warning`：

| 计算 | BDD Relevance | Demand Status | Commercial Risk | Financial Warning | Business Change Signal | Sales Conclusion |
|---|---|---|---|---|---|---|
| **A · 实际值** | High | Potential | Unknown | **Yes** | Yes | **🟡 建议先验证** |
| **B · 对照值（假设 FW = No）** | High | Potential | Unknown | No | Yes | **🟢 建议开发** |

- 路径 A：第 1 步一票否决不触发 → 第 2 步不触发 → 第 3 步需 Demand ∈ {Confirmed, Strong Signal}，不满足 → **第 4b 步**：四问中第 1 问（严重程度＝破产保护 + 违约 + 持续经营疑虑）、第 2 问（风险主体＝集团即目标采购主体）、第 3 问（影响采购与付款能力＝是）、第 4 问（影响项目执行能力＝是）**全部指向影响本次判断** → 上限降至 `建议先验证`。
- 路径 B：第 4 步 A 档四条（`Relevance = High` 且 `Demand = Potential` 且 `Risk ≠ High` 且 `FW ≠ Yes`）**全部满足** → `建议开发`。
- **结论：`Financial Warning` 在修复误报后仍能识别真实财务困境，并仍对 `Sales Conclusion` 产生可观察的一档影响（建议开发 → 建议先验证）。**
- 同一组字段下 `Business Change Signal` 由 Yes 改为 No，两条路径的结论**均不变** —— 印证该字段不参与降档。

**判定要点**：本主体为**自有多个制造厂区的聚合物 / 特种材料制造商**，按 `customer-type-playbook.md` 判 `End-user`。财务警示与业务变化**判定路径完全分离**：前者仅依 6.1 白名单五项证据成立，后者仅记录资产关停与结构调整，两者互不代表。

### 边界声明

本次执行未输出：工艺参数、设备选型、技术方案、达标承诺、金额、报价状态、回复草稿、跟进节奏、客户案例名单。
`Technical Fit` 与 `Quotation Readiness` 按范围冻结规定**不输出**。
**未输出"建议小试"，未固定"寄 5~10 L 水样"**（V1.1 已删除该越界规则）。
主卡 `Contact` 的具名信息来自 **Trinseo 官网新闻稿**（符合"官网来源"要求）；未输出电话、邮箱或个人联系方式。
`Sales Conclusion`、`Financial Warning` 与 `Business Change Signal` 均按 `sales-conclusion-rules.md` 与 `evidence-policy.md` 第六、七节的逐条规则匹配得出，未作主观调整。
