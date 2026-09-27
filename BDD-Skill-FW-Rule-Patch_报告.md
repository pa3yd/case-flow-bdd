# BDD Customer Intelligence Skill · Financial Warning Rule Patch

**执行日期**：2026-09-27
**基线版本**：V1.1.3（本次为**规则修订 Patch**，版本号保持 V1.1.3 + 标记 `FW Rule Patch`）
**核心修正**：**Business Change / Restructuring（业务变化 / 重组） ≠ Financial Distress / Financial Risk（财务困境）**

---

## 1. 修改文件清单

**共 15 个文件（未增减）／5,186 行（+199）**

逐文件行数：`SKILL.md` 754→777（+23）· `references/evidence-policy.md` 264→358（+94）· `references/sales-conclusion-rules.md` 191→246（+55）· `assets/output-card-template.md` 400→427（+27）· `references/output-visual-rules.md` 623→623（**0**）。

### 已改 5 个

| 文件 | 改动 |
|---|---|
| `references/evidence-policy.md` | **第六节 Financial Warning 整体重写**（6.1 白名单 / 6.2 移出清单 / 6.3 集团 vs 厂区 / 6.4 证据冲突 / 6.5 硬规则）；**新增第七节 Business Change Signal**；原七~十节顺延为八~十一节；错误对照表 +3 行；待校准项改写 |
| `references/sales-conclusion-rules.md` | 判定输入区标注 `Business Change Signal` **不是判定输入**；**新增第 4b 步「FW = Yes 的降档判定（不得机械降档）」四问**；第 1 步与第 5 步同步改写；硬规则 +3 条（8/9/10）；示例 2b 改写为真实财务困境型、**新增示例 2c（业务变化 ≠ 财务警示）**；Evidence 标注要求 +1 行 |
| `SKILL.md` | 新增 **V1.1.3 · FW Rule Patch** 说明块；第 10 步改为 `Commercial Risk + Financial Warning + Business Change Signal`；第 13 步修正一票否决口径；**硬性约束 25 → 27 条**（新增 26 / 27）；决策链与第十节三个固定小块同步；零节预设禁令 + 文件说明 + TBD 同步 |
| `assets/output-card-template.md` | 主卡下方新增 **「业务变化（Context / Watch Item）」块**；新增「风险块与业务变化块」规则表（6 行）；主卡禁止项 +4 行 |
| `references/output-visual-rules.md` | **仅 1 处计数同步**：`25 条硬性约束` → `27 条硬性约束`（展示规则与 PDF 结构零改动） |

### 交付产物

| 文件 | 说明 |
|---|---|
| `BASF_BDD_Intelligence_2026-09-27.md` / `.pdf` | 重算，PDF **3 页** |
| `GEA_BDD_Intelligence_2026-09-27.md` / `.pdf` | 重算，PDF **3 页** |
| `Trinseo_FW-NegativeControl_2026-09-27.md` / `.pdf` | **Negative Control** 测试用例，PDF **3 页** |
| `_fw-patch-comparison/` | 5 张截图（BASF / GEA 结论卡 Before-After + Trinseo Page 1） |
| `_bdd-skill-archive/V1.1.3-backup-20260927/` | V1.1.3 全量备份（15 文件 md5 全 MATCH） |

---

## 2. Financial Warning · Before / After 规则

| | **Before（V1.1.3 原规则）** | **After（本 Patch）** |
|---|---|---|
| **`Yes` 判据** | 公开财报连续亏损 / 亏损扩大；**裁员或重组公告**；减资；欠薪或债务违约诉讼；**信用评级下调**；**被列为被执行人或失信主体** | **只认财务困境证据（8 类白名单）**：① Insolvency / 资不抵债 ② Bankruptcy / 破产 ③ Liquidity crisis / 严重流动性危机 ④ Debt default / 债务违约 ⑤ **Going-concern warning / 持续经营重大疑虑** ⑥ Court-supervised financial restructuring / 法院或债务层面财务重组 ⑦ 连续、重大且具**集团层面影响**的亏损 **且**存在明确财务压力证据（四条同时） ⑧ 官方财报 / 审计报告 / 监管披露明确指出的重大财务困难 |
| **`No`** | 有公开财报且盈利，且无上述任一项 | **未命中 6.1 白名单**即判 `No`（不再要求"有财报且盈利"） |
| **`Unknown`** | 无公开财务信息，或信息不足 | 不变 |
| **裁员 / 重组 / 高管变化 / 厂区亏损 / 降本计划** | 直接触发 `Yes` | **一律不得触发 `Yes`** → 全部改判 `Business Change Signal` |
| **集团 vs 厂区** | 仅一句"需注明口径" | **6.3 明确规则**：厂区 / 业务单元亏损、裁员、产能调整 → 归 Business Change Signal，**不得推出集团 `FW = Yes`** |
| **证据冲突** | 无 | **6.4 明确规则**：同时存在「裁员 / 重组 / 厂区亏损」与「集团盈利 / 正常现金流 / 上调指引 / 分红 / 回购 / 正常重大投资」时 → **优先判 Business Change Signal = Yes**，`FW` 依真实财务证据定级（无白名单证据 → `No`）；**不得用单条负面新闻覆盖更完整的集团财务事实** |
| **对 Sales Conclusion 的作用** | 实质等同于"降一档"（第 4 步门槛要求 `FW ≠ Yes`） | **6.5 硬规则 6**：`FW = Yes` **不得机械降档** —— 必须经 `sales-conclusion-rules.md` **第 4b 步四问**，并在结论原因中**说明理由** |
| **硬规则条数** | 5 条 | 6 条（新增"不得机械降档"） |

### 新增：Sales Conclusion **第 4b 步**（`FW = Yes` 的四问 + 判定规则）

| # | 必须回答的问题 |
|---|---|
| 1 | **财务风险严重程度**：是破产 / 违约 / 持续经营重大疑虑，还是仅"连续亏损"？ |
| 2 | **风险主体层级**：是集团 / 母公司，还是某个厂区、子公司或非目标主体？ |
| 3 | **是否影响本次潜在采购与付款能力**：是否有公开证据显示仍在正常采购 / 正常重大投资 / 正常付款？ |
| 4 | **是否影响相关项目执行能力**：是否影响项目推进、交付或运维能力？ |

| 情形 | 结论上限 |
|---|---|
| 四问中任一**指向影响本次目标采购主体 / 采购与付款能力 / 项目执行** | **`建议先验证`** |
| 风险主体**不是**本次目标采购主体或 `Priority Site`，**且**有公开证据显示采购、付款、项目执行均未受影响 | **可不降档** |
| 无法判断上一行 | 取保守侧 → `建议先验证` |

> **输出强制要求**：只要 `FW = Yes`，结论原因中**必须**出现一句「为什么该财务风险会影响（或不影响）本次 BDD 客户开发判断」。

---

## 3. Business Change Signal · 新规则

**回答的问题**：这家企业**当前正在发生哪些经营层面的变化**？
**定位**：**`Context / Watch Item`（背景与观察项）—— 不是风险定级，不参与降档。**
**取值**：`Yes` / `No` / `Unknown`

### 3.1 纳入范围（从 Financial Warning 移出，10 类）

Layoffs / 裁员 · Management changes / 高管变化 · Organizational restructuring / 组织架构调整 · Business-unit restructuring / 业务单元调整 · Plant consolidation / 工厂整合 · Capacity reduction / 产能调整 · Portfolio adjustment / 业务组合调整 · Strategic transformation / 战略转型 · **Site-level operating loss / 单一厂区经营亏损** · Cost-cutting program / 降本计划

### 3.2 输出要求

判 `Yes` **必须**输出 `Reason` + `Source`（`evidence-policy.md` 7.2）。

### 3.3 硬规则（8 条 · **不得单独降档**）

| # | 规则 |
|---|---|
| 1 | **不得单独触发** `Financial Warning = Yes` |
| 2 | **不得单独触发** `Commercial Risk = High` |
| 3 | **不得单独导致** `Sales Conclusion` 降档 |
| 4 | **不得导致** `BDD Opportunity` 降档 |
| 5 | **不得导致** `Demand Status` 降档 |
| 6 | 只作 **Context / Watch Item** |
| 7 | **不得写进任何"风险"字段的定级依据**（只能作为附注 / 背景说明） |
| 8 | 只有**同时**具备 6.1 白名单证据时，才可升级为 `Financial Warning = Yes` |

同步落到 **SKILL.md 硬性约束 26 / 27**（原 25 条 → 27 条）：

| # | 约束 |
|---|---|
| **26** | **`Business Change Signal = Yes` 不得单独触发 `FW = Yes` / `Commercial Risk = High`，不得单独导致任何字段降档** |
| **27** | **`FW = Yes` 不得机械降档** —— 必须经四问判定并解释理由；不得用单条负面新闻覆盖更完整的集团财务事实 |

---

## 4. BASF 回归结果

| 检查项 | 结果 |
|---|---|
| 重组 / 裁员是否正确进入 **Business Change Signal** | ✅ **Yes**（含 Reason + Source）：全球裁员约 7,000 人 · CoreShift 重组计划 · adipic acid/CDon/CPon 装置关闭 · 2026-07 多套高耗能装置永久关闭 · hydrosulfites 业务退出 · Ludwigshafen 员工降至 3 万以下 · 基地连续第四年亏损 |
| 是否仍被错误判成 **Financial Warning = Yes** | ✅ **已修正为 `No`** —— 逐项核对 6.1 白名单未命中；两条原依据已重分类（裁员重组→组织与人员调整；基地亏损→单一厂区经营亏损） |
| 集团盈利等正面财务事实是否被同时考虑 | ✅ **已完整记录**：2023–2025 连续盈利（净利 €379 / 1,298 / 1,619 百万）· 2026 上半年销售额 €17.2 十亿（+€2.4 十亿）· 价格 +11.5% · 销量 +7.3% · EBITDA before special items €2.4 十亿（+€854 百万）· 上调全年指引至 €6.9–7.7 十亿 · 最高 €10 亿股票回购 |
| 严重程度复核 | ✅ 已做：BASF SE 单体 2025 年 income from operations −€1,585 百万、含重组费用增加 €333 百万 → 性质为**重组当期费用**，未见持续经营 / 偿债能力公开疑虑 → 不构成 6.1 第 5 / 7 项 |
| Sales Conclusion 是否按完整证据链重算 | ✅ 由规则机械重算（见第 7 节） |
| PDF | ✅ **3 页**（Page1 1 页 / Page2 5 卡 / Page3 8 条） |

---

## 5. GEA Group 回归结果

| 检查项 | 结果 |
|---|---|
| 组织调整 / 管理层变化是否进入 **Business Change Signal** | ✅ **Yes**（含 Reason + Source）：2025-10-07 ad-hoc 公告执行董事会由三席扩至六席 · **解散 14 人全球执行委员会** · COO 执行董事会领域撤销（过渡至 2026-06-30）· 区域矩阵取消、区域 CEO / CFO 离职 · 中国与印度改为直报 CEO · 采购职能集中化 · 第三方报道约 100 名员工受影响、预计 10–20 名管理层离职 · CFO 于 2025-10-31 离职 |
| 是否不再自动成为 **Financial Warning** | ✅ **已修正为 `No`** —— 三条原依据（重组公告 / COO 撤销与区域 CEO·CFO 离职 / 影响人数与 CFO 离职）**全部属组织架构与管理层变化，不在 6.1 白名单内** |
| 集团盈利等正面财务事实是否被同时考虑 | ✅ **已完整记录**：2025 订单 intake €5,924 百万（有机 +9.1%）· 营收 €5,495 百万（有机 +3.7%）· 净利润 €414 百万 · EBITDA before restructuring €907 百万（margin 16.5%，上年 15.4%）· EPS €2.60–2.70 · 股息提高至 €1.30 · 进入 DAX · **2026 指引有机营收 +5.0%~+7.0%**、EBITDA margin 16.6%~17.2%、ROCE 34%~38% |
| Sales Conclusion 是否不再因普通组织调整被机械降档 | ✅ **是** —— 由 `建议先验证` 重算为 **`建议开发`** |
| PDF | ✅ **3 页**（Page1 1 页 / Page2 5 卡 / Page3 8 条） |

---

## 6. Negative Control 结果

**测试案例**：**Trinseo PLC**（注册地爱尔兰，集团总部美国宾州 Wayne；全球特种材料 / 聚合物制造商）
**选择理由**：同时具备 6.1 白名单中的**五项**证据，且行业属 BDD 目标市场（T4 精细化工 / 聚合物制造 + T3 性质口径），不是抽象构造。

### 实际判定

| 字段 | 值 |
|---|---|
| Customer Type · Path | 终端业主 · **End-user** |
| Industry Match | 🟢 **Target** |
| BDD Opportunity | 🟢 **High · End-user Opportunity** |
| Demand Status | 🟡 **Potential** |
| Current Treatment | ⚪ **未知 Unknown** |
| Priority Site | **Schkopau（德国）**，备选 Terneuzen（荷兰） |
| Commercial Risk | ⚪ Unknown |
| **Financial Warning** | 🔴 **Yes** ✅ |
| **Business Change Signal** | 🟡 **Yes** |
| **Sales Conclusion** | 🟡 **建议先验证** |

### `Financial Warning = Yes` 的五项白名单证据（全部 FACT + 可靠公开 Source）

| 6.1 项 | 证据 | Source |
|---|---|---|
| **第 5 项 Going-concern** | 按 ASC 205-40 明确结论：**对一年内持续经营能力存在重大疑虑**（substantial doubt） | SEC Form 10-Q（2026-03-31） |
| **第 4 项 Debt default** | 2026 Q1 未按期付息、宽限期届满未付，构成违约并**触发跨违约**，债务加速到期；几乎所有 $27.7 亿借款重分类为流动负债 | SEC Form 10-Q |
| **第 2 / 6 项 Bankruptcy + 法院层面财务重组** | **2026-05-26 主动申请第 11 章破产保护**；2026-05-13 签署 RSA（拟削减约 $20 亿债务）；由**法院批准的 DIP 融资**支持运营 | 官网 2026 Q2 财报新闻稿；公开报道 |
| **第 3 项 Liquidity crisis** | 2026 Q1 经营现金流出 $232.9 百万、流动性仅 $114.2 百万；股东权益赤字 $1,222.9 百万、累计亏损 $1,455.2 百万 | SEC Form 10-Q |
| **第 8 项 官方披露重大财务困难** | S&P 于 2026-03-20 将评级下调至 **'D'（Default）**；NYSE 于 2026-03-30 生效摘牌（转 OTC: TSEOF） | S&P 评级行动；公开报道 |

### ⭐ 关键验证：**FW 修复后仍能影响 Sales Conclusion**（对照计算）

同一组字段，**仅改动 `Financial Warning`**：

| 计算 | Relevance | Demand | Risk | **FW** | **BCS** | **Sales Conclusion** |
|---|---|---|---|---|---|---|
| **A · 实际值** | High | Potential | Unknown | **Yes** | Yes | **🟡 建议先验证** |
| **B · 对照值** | High | Potential | Unknown | **No** | Yes | **🟢 建议开发** |

- 路径 A：第 3 步需 Demand ∈ {Confirmed, Strong Signal} → 不满足；**第 4b 步四问全部指向影响本次判断**（① 严重程度＝破产保护 + 违约 + 持续经营疑虑 ② 风险主体＝集团即目标采购主体 ③ 影响采购与付款能力＝是 ④ 影响项目执行能力＝是）→ 上限降至 `建议先验证`
- 路径 B：第 4 步 A 档四条**全部满足** → `建议开发`

> **结论：`Real Financial Distress → Financial Warning = Yes` 成立，且该字段仍对 `Sales Conclusion` 产生可观察的一档影响。修复没有把 `Financial Warning` 改成"永不触发"。**
>
> **反向印证**：同一对照组中把 `Business Change Signal` 由 Yes 改为 No，路径 A / B 的结论**均不变** → 印证该字段不参与降档。

---

## 7. Sales Conclusion · Before / After

**结论均由修正后的规则机械重算，未人工指定。**

| 主体 | Before | After | 变化路径（规则依据） |
|---|---|---|---|
| **BASF** | 🟡 建议先验证<br><sub>（"但 Financial Warning = Yes（集团持续公开重组与裁员…），按规则上限降至本档"）</sub> | 🟢 **建议开发**<br><sub>（"无商业风险与财务困境证据（集团 2023–2025 连续盈利、2026 上半年改善并上调指引）；业务变化信号已记录为背景与观察项，不作为降档依据"）</sub> | `FW` Yes→No ⇒ 第 4 步 A 档四条（Relevance=High ✔ / Demand=Potential ✔ / Risk≠High ✔ / FW≠Yes ✔）全部满足 |
| **GEA Group** | 🟡 建议先验证<br><sub>（"但 Financial Warning = Yes（2025-10-07 公告重组执行董事会与组织架构…），按规则上限降至本档"）</sub> | 🟢 **建议开发**<br><sub>（"无商业风险与财务困境证据（集团 2025 年营收与利润双增…）；组织架构与管理层变化属业务变化信号，只作背景与观察项，不作为降档依据"）</sub> | 同上 |
| **Trinseo（NC）** | —（新案例） | 🟡 **建议先验证** | 第 4b 步四问指向影响本次采购与执行 ⇒ 上限降档；对照值（FW=No）为 `建议开发` |

**两个案例的 `BDD Relevance` / `Demand Status` / `Commercial Risk` / `Priority Site` / `Next Action` 等字段均未变**（见第 9 节逐字段比对）。

---

## 8. 未修改规则文件清单

### 10 个文件 md5 与 V1.1.3 备份**完全一致**

`references/bdd-fit-rules.md` · `references/bdd-relevance-rules.md` · `references/contact-role-map.md` · `references/current-treatment-rules.md` · `references/customer-type-playbook.md` · `references/lead-signals.md` · `references/must-ask-params.md` · `references/opportunity-type-rules.md` · `references/wastewater-signal-map.md` · **`scripts/render_pdf.py`（渲染层零改动）**

### 1 个文件仅 1 处计数同步（已显式声明）

`references/output-visual-rules.md` —— 差异 **2 行**，全部为同一句：`25 条硬性约束` → `27 条硬性约束`。**展示规则与 PDF 结构零改动。**

### 未改动项核对

| 项 | 状态 |
|---|---|
| 13 个 Internal Key | ✅ 未动（Page 1 仍为 13 字段） |
| PDF 视觉结构（Page 1 / Page 2 五卡 / Page 3 Key Evidence） | ✅ 未动（三家均 3 页 / 5 卡 / 8 条） |
| Evidence Policy（FACT / INFERENCE / UNKNOWN / Confidence / Decision Impact） | ✅ 未动（三家 Evidence 逐字一致） |
| Customer Type · End-user / Partner Path | ✅ 未动 |
| Industry Map · Industry Match · BDD Opportunity · Demand Status · Current Treatment · Priority Site · Contact Strategy · Opportunity Type | ✅ 未动 |
| Default Invocation Protocol | ✅ 未动 |
| Markdown / PDF 输出机制 | ✅ 未动 |
| 新增财务评分 / 信用评分 / 100 分制 / 财务尽调系统 / 新 Skill / CRM 功能 | ✅ **均未新增** |

---

## 9. 判断一致性检查

### 9.1 规则层

`52 / 52 PASS`（含白名单 8 类 / 移出清单 10 类 / 7.3 五条不得 / 6.3 / 6.4 / 第 4b 步四问 / 硬约束 26·27 / 一票否决口径修正 / 输出模板业务变化块）

### 9.2 案例层（Before → After 逐字段）

| 检查 | BASF | GEA |
|---|---|---|
| 变化字段（13 字段全集） | **仅 `Sales Conclusion`** | **仅 `Sales Conclusion`** |
| Page 1 实际渲染值变化 | **仅结论卡** | **仅结论卡** |
| Evidence 条数 | 29 → 29 | 29 → 29 |
| Evidence 逐字（类型 / 结论 / Source / Reason / Confidence / Impact） | **0 差异** | **0 差异** |
| 13 字段完整 | 13 / 13 | 13 / 13 |
| PDF 页数 | 3 页 | 3 页 |
| 越界输出 | 0 处 | 0 处 |

### 9.3 一处**已修正的既有内部不一致**

`SKILL.md` 第 13 步原写「一票否决优先（`Risk = High` / **`FW = Yes`** / `BDD Relevance = Low` → `暂不优先`）」，
与 `sales-conclusion-rules.md` 「**`Financial Warning = Yes` 不构成一票否决**」**长期矛盾**。
本 Patch 已把 SKILL.md 改为「`Risk = High` / `BDD Relevance = Low` → `暂不优先`」，并补注 `FW = Yes` 的处理路径。

---

## 10. 是否出现新副作用

| # | 事项 | 判定 |
|---|---|---|
| 1 | **PDF 结构与页数** | ✅ 无副作用。三家均 **3 页 / Page2 5 卡 / Page3 8 条**，Page3 无审计术语，审计信息未进 PDF |
| 2 | **判断内容被意外改动** | ✅ 无。BASF / GEA 逐字段比对仅 `Sales Conclusion` 变化；Evidence 逐字 0 差异 |
| 3 | **`output-visual-rules.md` 被改** | ⚠️ **已发生的唯一越界**：1 处计数同步（25 → 27 条硬性约束）。**非展示规则改动**，已在第 8 节显式声明；如需回退请告知 |
| 4 | **GEA 报告的附录结构** | ⚠️ **需你知晓**：GEA 的 Markdown 原为 **V1.1.2 期产物**（无 `主题` 列、审计段落散在附录 A 内），用当前 V1.1.3 渲染层会导致 **PDF 涨到 4 页**。本次做了 2 处**规格对齐**：① 附录 A 补 `主题` 列（29 条）② 审计段落归入 `## 附录 B`。**判断内容零改动、Evidence 逐字 0 差异**；不这样做则 GEA 的 PDF 无法符合 V1.1.3 规格。BASF 已于上一轮完成对齐，本次无需处理 |
| 5 | **`Sales Conclusion` 结论普遍上移** | ⚠️ **属预期效果，非副作用**：过去"有裁员/重组公告即降档"导致高相关主体被系统性压低。修复后 BASF / GEA 升至 `建议开发`。**是否可接受属业务口径问题，需你确认** |
| 6 | **`Financial Warning` 是否会变"永不触发"** | ✅ 已由 Negative Control 排除：Trinseo 五项白名单证据 ⇒ `FW = Yes`，且对照计算证明仍能降低一档 |
| 7 | **`Unknown` 语义** | ✅ 未变。`FW = Unknown` 仍不导致降档 |
| 8 | **新增字段 / 评分 / 功能** | ✅ 无。`Business Change Signal` 是**状态标签 + Reason + Source**，不是评分、不进 Page 1 的 13 字段、不新增 PDF 卡片 |
| 9 | **`Business Change Signal` 无 PDF 展示位** | ⚠️ 已知限制（按你的规格「暂时不新增为 PDF 第 6 张卡」）：目前只出现在 **Markdown** 与 **Sales Conclusion 原因**中。已登记为 TBD 待你决定 |
| 10 | **渲染层与其余规则文件** | ✅ `scripts/render_pdf.py` 及其他 10 个规则文件 md5 与备份完全一致 |

---

## 附：待你确认（不阻塞）

1. `references/output-visual-rules.md` 的 1 处计数同步是否认可（不认可可回退，但会与 SKILL.md 的 27 条不一致）。
2. GEA 报告的 V1.1.3 规格对齐（`主题` 列 + 附录 B）是否认可；其余 7 份历史报告是否也需要同一处理。
3. 结论文由"普遍降档"改为"按证据链回归"后，是否需要对历史 8 家重新跑一轮（会改变 Umicore / Hikal / Aarti / EnviroChemie 等的档案口径）。

*Skill 本体 15 个文件；V1.1.3 备份可完整回退。*
