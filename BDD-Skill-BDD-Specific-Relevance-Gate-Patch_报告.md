# BDD-Specific Relevance Gate Patch · 交付报告

**执行时间**：2026-09-27
**作用对象**：BDD Customer Intelligence Skill V1.1.3（含 FW Rule Patch）
**范围**：仅 Patch A（收紧 T3 定义）+ Patch B（新增 End-user BDD-Specific Relevance Gate）
**备份**：`D:/Case Flow/_bdd-skill-archive/V1.1.3-backup-20260927-b/`（15 文件 md5 全 MATCH，可完整回退）

---

## 1. 修改文件清单

| 文件 | 行数变化 | 改了什么 |
|---|---|---|
| `SKILL.md` | 777 → 826（**+49**） | 顶部 Patch 声明；决策链加第 7 条硬规则（两条链路分别取证）；**新增两条禁止推导**（含新示例 3）；§五 End-user 取值表改 A~E 五条件；§八 第 6 步加 T3 证据门槛、第 7 步加 Gate 顺序；**硬性约束 27 → 29 条**；§十二 文件说明补两条；§十四 TBD 更新第 1 条并新增 1b / 21 / 22 / 23 |
| `references/bdd-fit-rules.md` | 140 → 198（**+58**） | **Patch A 主体**：T3 说明重写；新增「T3 证据门槛（9 项）」+「T3 硬规则（9 项不得单独成立）」；判定流程第 2 步分叉；硬规则 +3 条（8/9/10）；TBD 更新第 1 条 + 新增 1b |
| `references/bdd-relevance-rules.md` | 214 → 326（**+112**） | **Patch B 主体**：新增第四节 Gate（四档判据 + 8 条硬规则 + 与 Industry Fit 分离原则）；§三 End-user 取值表改 A~E 并新增 `Industry Fit = Unknown → Unknown`；新增红线 3；判定流程插入第 6 步 Gate；封顶速记 +3 行；错误对照 +3 条；TBD +3 条 |
| `references/output-visual-rules.md` | 623 → 623（**±0**） | **仅 1 行计数同步**：`27 条硬性约束` → `29 条硬性约束`（第 174 行，V1.1.3 Patch 范围声明句）。**唯一越界项，已声明** |

**共 15 个文件（未增减）／5,405 行**

---

## 2. T3 Before / After

### Before（问题）

```
| T3 | High-COD / Refractory Industrial Wastewater（产生方） |

说明：T3 是性质口径 —— 凡主体业务确证产生高 COD / 难降解有机废水的制造业，
      均归入 Target，即使其行业门类未在列举内（如焦化、印染、电镀、半导体、
      危废处置、垃圾渗滤液、造纸制浆、钢铁冷轧等）。

硬规则：符合 T3 性质口径的制造业（焦化、印染、电镀、…）归入 Target。
```

**缺陷**：`T3` 的**标题**是对的，但**判据没有证据门槛**，而"举例清单"（电镀、表面处理…）在实践中变成了**免证据白名单** ——
只要主体属举例行业或有工业废水，就被判 `Target`。**Festo 即按此路径由"阳极氧化属表面处理族"判 `Target`。**

### After（Patch A）

**T3 = High-COD / refractory / difficult-to-treat industrial wastewater（高 COD / 难降解 / 难处理工业废水）。**

> ❌ "有工业废水" ≠ T3。工业废水 / 制造业废水 / 生产废水这类表述**本身不构成 T3 证据**。
> ❌ "废水相关性" ≠ "BDD 相关性"。
> **行业标签不构成证据。** 举例清单降级为"性质举例"，**不得因主体属于举例行业就直接判 `Target`**。

**T3 证据门槛（须至少命中 1 项，FACT 级 + 附 Source）**

| # | 可接受的 T3 证据 |
|---|---|
| 1 | high COD（高 COD） |
| 2 | refractory wastewater（难降解废水） |
| 3 | hard-to-biodegrade / poorly biodegradable wastewater（可生化性差） |
| 4 | persistent / recalcitrant organics（持久性 / 顽固性有机物） |
| 5 | difficult organic wastewater（难处理有机废水） |
| 6 | deep treatment / polishing requirement（深度处理 / 提标要求） |
| 7 | conventional biological treatment limitation（常规生化处理受限 / 不适用） |
| 8 | difficult industrial effluent requiring advanced treatment（需高级氧化等强化处理的工业废水） |
| 9 | explicitly documented difficult-to-treat pollutants（明确载明的难处理污染物） |

**T3 硬规则（以下证据单独存在时不得判 T3 `Target`）**：只存在工业废水 · 只存在生产废水 · 只存在阳极氧化废水 · 只存在机加工废水 · 只存在压铸废水 · 只存在普通表面处理废水 · 只存在一般排污许可 · 只存在废水处理设施 · 只存在废水量数据。

**不满足时的落点**：属 A1~A3 → `Adjacent`；符合 Outside 界定 → `Outside`；**其余（含"普通制造业废水"）→ `Unknown`**。

（判定流程第 2 步已改为 `T3 ── 须再过「T3 证据门槛」─ 命中 → Target / 未命中 → 继续第 3 步`；T1 / T2 / T4 仍按行业口径，**未改动**。）

---

## 3. BDD-Specific Relevance Gate 规则（Patch B）

**回答**：这家企业的**废水**是否与 BDD（电化学氧化 / 高级氧化）的适用场景存在**明确关系**。
**定位**：**不新增到 13 个 Internal Key · 不新增 PDF 字段 · 不新增评分 / 分数制 · 只用于 End-user `High` 判定 · Partner Path 完全不适用 · 结果只记入 Markdown 附录 B。**

| 档 | 判据（取已命中的最高档） |
|---|---|
| **`Strong`** | 至少一种明确 BDD 相关处理信号：High COD + difficult-to-treat context · refractory organic wastewater · hard-to-biodegrade organics · persistent organic pollutants · API / pharmaceutical refractory wastewater · fine-chemical difficult organic wastewater · **AOP already in use** · **AOP under evaluation** · advanced oxidation requirement · electrochemical oxidation / electro-oxidation · **conventional treatment failure / limitation** · tertiary / deep polishing need for difficult pollutants · documented treatment gap **clearly relevant to destructive oxidation** |
| **`Moderate`** | 较强间接证据：complex organic chemical manufacturing · API / pharmaceutical synthesis · fine chemical multi-step synthesis · **solvent-rich or organic-rich process** · known difficult liquid waste streams · **battery / chemical production with meaningful wastewater evidence** —— **但尚未确认** refractory / high COD / AOP / treatment limitation |
| **`Weak`** | 仅有 manufacturing · wastewater generation · treatment facility · discharge permit · water consumption · generic ESG water statement，**无明确 BDD-specific 污染物或处理难点** |
| **`Unknown`** | 公开资料不足，无法判断该废水是否与 BDD 场景存在明确关系 |

**8 条硬规则**（摘要）：①「有废水」≠ Gate ≥ `Moderate`；② `Strong` 须 E# 级 FACT 证据且 `Reason` 写明信号；③ 不得用行业经验值升格；④ `Industry Fit = Target` 不构成任何 Gate 证据；⑤ 取最高已命中档、不得凑档；⑥ 非 `Strong` 不得判 `High` 且不得人工指定替代值；⑦ 不适用于 Partner Path；⑧ 不新增 Key / 字段 / 评分，只记 Markdown 附录 B。

**映射表（仅当条件 A+B+C+D 已满足时适用，机械取值）**

| Gate | BDD Relevance |
|---|---|
| `Strong` | `High` |
| `Moderate` | `Medium` |
| `Weak` | `Medium` |
| `Unknown` | `Unknown` |

> A~D 本身不满足时 **Gate 不参与**，按原定义取值；`Industry Fit = Unknown` → 条件 ① 即不成立 → `Unknown`（优先于 Gate 映射）。

---

## 4. End-user `High` Before / After

| | Before | After（Patch B 后） |
|---|---|---|
| 条件 | ① Industry Fit ∈ {Target, Adjacent} ② 制造业确认 ③ PWE 或 CSD ④ ≥ 2 项主体级证据 | **A** Industry Fit **= Target**（T3 须过证据门槛）+ **B** 制造业确认 + **C** PWE 或 CSD + **D** ≥ 2 项主体级证据 + **E** **Gate = `Strong`（新增硬门槛）** |
| 判定顺序 | 四条件齐 → 直接 `High` | A~D 齐 → **再过 Gate** → `Strong` 才 `High`；`Moderate` / `Weak` → `Medium`；`Unknown` → `Unknown` |
| `Medium` 判据 | 行业对口 + 制造业确认，但证据仅 1 项或 PWE/CSD 均缺 | 上列 **或** A~D 已满足但 Gate ∈ {`Moderate`, `Weak`} |
| `Unknown` 判据 | 关键输入不足 | 上列 **或** `Industry Fit = Unknown` **或** Gate = `Unknown` |
| 强制附注 | Reason / Evidence / Confidence / Opportunity Type（**四项，未增删**） | **同前，四项不变** —— Gate 档位不进附注、不进 PDF，只进 Markdown 附录 B |

新增红线 3：**废水相关性 ≠ BDD 相关性**；`Industry Fit` 与 Gate **必须分别取证**，不得用一方证据顶替另一方。

---

## 5. CABB 回归结果（Positive Control）

| 检查项 | 结果 |
|---|---|
| `Industry Match` | 🟢 **`Target`（保持）** —— **T4 精细化工 / 农药 · 染料 行业口径直接命中，Patch A 未涉及 T4**；且 **T3 现已一并过证据门槛**（E12 提供"难生物降解 / 深度处理 / 常规处理受限"性质证据），T3 不再是唯一支撑 |
| **`BDD-Specific Relevance Gate`** | **`Strong`** |
| **为什么满足 `Strong`** | ① **AOP 已在用** —— Pratteln 厂区 **2019 年投运紫外高级氧化（UV-AOP）装置**，2021 年优化预处理段显著提升处理能力（E12）② **难生物降解 / 常规处理受限** —— 同一装置「将**复杂污染物分子降解为无毒、易生物降解的小分子**，从而可排入**常规**污水处理厂」，即必须先用高级氧化预处理才能进常规生化（E12）③ **精细化工难处理有机废水** —— 卤化（氯化 / 溴化）、磺化与氯磺化、Cl₂ / H₂O₂ 氧化等多步有机合成，逾 100 台反应釜、总反应容积 >1,300 m³（E8） |
| `BDD Opportunity` | 🟢 **`High`（自然保持）** —— 条件 A~E 全部满足；**由规则自动计算得出，非人工锁定** |
| `Demand Status` | 🟡 `Potential`（**未改动**） |
| `Sales Conclusion` | 🟢 **`建议开发`（未变）** —— 第 3 步因 `Demand = Potential`（要求 Confirmed / Strong Signal）不达"重点开发"；第 4 步 A 档全部满足 → `建议开发` |

---

## 6. Festo 回归结果

| 检查项 | Before | After | 依据 |
|---|---|---|---|
| `Industry Match` | 🟢 `Target`（T3 性质口径） | ⚪ **`Unknown`** | 公开证据只证明「铝阳极氧化（表面处理）+ 压铸 + 机加工产生工业废水」，**未载明**高 COD / 难降解 / 难生物降解 / 难处理 / 深度处理 / AOP 需求 / 明确复杂污染物 → 属 T3 硬规则列举的「只存在阳极氧化废水 / 机加工废水 / 压铸废水 / 普通表面处理废水」情形，**不得判 `Target`**。不属 T1 / T2 / T4；不属 A1~A3；因确有工业废水，不能正面确证 `Outside` → `Unknown` |
| **`BDD-Specific Relevance Gate`** | —（不存在） | **`Weak`** | 仅有一般性证据：制造业（E4 / E5）、废水产生（E8 / E19）、持证处理设施与排放许可（E9）、用水量（E8 / E19）、通用 ESG 水声明（E11 / E12）。**未命中任何 BDD-specific 信号**（无高 COD / 无难降解 / 无持久性有机物 / 无 AOP / 无常规处理受限 / 无深度处理需求 / 无明确难处理污染物；具体处理工艺单元亦未披露，E21） |
| `BDD Opportunity` | 🟢 `High` | ⚪ **`Unknown`** | 条件 ①（Industry Fit = Target）不成立 → `High` 与 `Medium` 均不达（两者都要求行业对口）→ `Unknown`。**`Industry Fit = Unknown` 的封顶优先于 Gate 映射** |
| `Demand Status` | 🟡 `Potential` | 🟡 `Potential`（**未改动**） | 规则禁止修改 |
| `BMS / 财务 / 优先级 / 现有处理 / 联系人` | — | **全部未改动** | 见第 8 节逐字段比对 |
| `Sales Conclusion` | 🟢 `建议开发` | 🟡 **`建议先验证`** | 第 1 步一票否决不触发（`Risk = Unknown` ≠ `High`；`Relevance = Unknown` ≠ `Low`）→ 第 2 步要求「`Relevance = Unknown` **且** `Demand` 无任何证据」，本例 `Demand = Potential` **有证据，不触发** → 第 3 / 4 步均要求 `High` / `Medium`，不触发 → **第 5 步「其余情况」→ `建议先验证`**（先验证"是否存在 BDD 适用场景"） |

> **注意**：Festo 落 `Unknown` 而**不是** `Medium`。原因是没有把 Gate `Weak` 的"上限 Medium"机械套用 —— 按规则体系，**条件 ① 先不成立**，`Industry Fit = Unknown` 的封顶在 Gate 映射之前生效。**全程无人工指定。**

---

## 7. ACC 回归结果

| 检查项 | Before | After | 依据 |
|---|---|---|---|
| `Industry Match` | 🟢 `Target`（T1） | 🟢 **`Target`（保持）** | **Patch A 只收紧 T3，T1 不受影响**；官方登记经营范围含 "Manufacture of batteries and accumulators" |
| **`BDD-Specific Relevance Gate`** | —（不存在） | **`Moderate`** | 命中「**富溶剂 / 富有机工艺**」（电极浆料配料使用有机溶剂 NMP，E10）+「**电池生产且有实质废水证据**」（废水去向、含 NMP 液体废液外送、2025 年水回用可研，E8 / E11 / E13）+ 已知难处理液体废物流（E11）。**未命中任何 `Strong` 信号** —— 无高 COD / 无难降解 / 无持久性有机物 / **无高级氧化（在用或评估中）** / 无常规处理受限 / 无针对难处理污染物的深度处理需求；2025 年可研针对的是 **purge 类废水回注与雨水回用（水量维度）**，**不属"与破坏性氧化相关的处理缺口"**（E13） |
| `BDD Opportunity` | 🟢 `High` | 🟡 **`Medium`** | 条件 A~D 全部成立（行业对口 / 制造确认 / PWE 成立 / ≥2 项主体级证据），**仅条件 E 未通过**（Gate = `Moderate`）→ 由 `High` 降为 `Medium`。**由规则机械计算，非人工指定** |
| `Demand Status` | 🟡 `Potential` | 🟡 `Potential`（**未改动**） | 规则禁止修改 |
| `Sales Conclusion` | 🟢 `建议开发` | 🟡 **`建议先验证`** | 第 1 步 ✗ → 第 2 步（`Relevance` 非 `Unknown`）✗ → 第 3 步（要求 `Demand ∈ {Confirmed, Strong Signal}`，本例 `Potential`）✗ → 第 4 步 A（要求 `Relevance = High`）✗、B（要求 `Demand ∈ {Confirmed, Strong Signal}`）✗ → **第 5 步 → `建议先验证`** |

---

## 8. 三家公司逐字段 Before / After（Page 1 实比，13 字段）

> 方法：用**改前渲染的 HTML** 与**改后渲染的 HTML** 逐字段取值比对（同一渲染层，`render_pdf.py` 未改动，故差异即为判断结果差异）。

### CABB

| 字段 | Before → After |
|---|---|
| 行业匹配 Industry Match | `Target` → `Target（T4 精细化工 / 农药 · 染料）`（**取值不变，仅补写依据**） |
| 其余 12 字段 | **逐字一致** |
| 结论卡取值 | `建议开发` → `建议开发` |

**逐字段：一致 12 / 变更 1**

### Festo

| 字段 | Before → After |
|---|---|
| 行业匹配 Industry Match | `Target` → ⚪ **`Unknown`** |
| BDD机会 BDD Opportunity | `High` → ⚪ **`Unknown`** |
| 其余 11 字段 | **逐字一致** |
| 结论卡取值 | `建议开发` → **`建议先验证`** |

**逐字段：一致 11 / 变更 2**

### ACC

| 字段 | Before → After |
|---|---|
| BDD机会 BDD Opportunity | `High` → 🟡 **`Medium`** |
| 其余 12 字段 | **逐字一致** |
| 结论卡取值 | `建议开发` → **`建议先验证`** |

**逐字段：一致 12 / 变更 1**

**三份卡 Page 3（KEY EVIDENCE）纯文本字数变化均为 ±0** —— 底层 Evidence **一字未删、一字未改**。
**三份卡 Evidence 条数不变**：CABB 25 / Festo 22 / ACC 29。

---

## 9. Sales Conclusion Before / After

| 公司 | Before | After | 变化原因（规则机械得出） |
|---|---|---|---|
| **CABB** | 🟢 建议开发 | 🟢 **建议开发** | 未变（`High` + `Potential` + `Risk ≠ High` + `FW ≠ Yes` → 第 4A 档） |
| **Festo** | 🟢 建议开发 | 🟡 **建议先验证** | `Relevance` 由 `High` 落 `Unknown` → 第 3 / 4 步均不达 → 第 5 步 |
| **ACC** | 🟢 建议开发 | 🟡 **建议先验证** | `Relevance` 由 `High` 落 `Medium`，`Demand` 仍为 `Potential` → 第 4B 档要求 `Demand ∈ {Confirmed, Strong Signal}` 不满足 → 第 5 步 |

**本 Patch 未修改 `Sales Conclusion` 五值体系与任何判定门槛**（`sales-conclusion-rules.md` md5 与备份完全一致）。
上述三个结果全部由既有第 1~5 步对**新 `BDD Relevance`** 逐条匹配得出。

---

## 10. 未修改规则文件清单（md5 与备份完全一致）

| # | 文件 | 说明 |
|---|---|---|
| 1 | `scripts/render_pdf.py` | 渲染层 —— **零改动** |
| 2 | `assets/output-card-template.md` | 输出模板 / 13 Key —— **零改动** |
| 3 | `references/evidence-policy.md` | Evidence Policy · Demand Status · Commercial Risk · FW 白名单 · BCS |
| 4 | `references/sales-conclusion-rules.md` | Sales Conclusion 五值体系 |
| 5 | `references/opportunity-type-rules.md` | Opportunity Type + Priority Site |
| 6 | `references/customer-type-playbook.md` | 客户类型 + End-user / Partner 双路径分流 |
| 7 | `references/current-treatment-rules.md` | Current Treatment |
| 8 | `references/contact-role-map.md` | 联系策略 |
| 9 | `references/must-ask-params.md` | Missing Critical Information 三级 |
| 10 | `references/lead-signals.md` | 检索指引 |
| 11 | `references/wastewater-signal-map.md` | 特征信号 |

**未改动项**（按 Spec）：Customer Type · End-user / Partner Path · Partner Path High 规则 · Demand Status · PWE / CSD 结构 · Financial Warning · Business Change Signal · Commercial Risk · Priority Site · Contact Strategy · Current Treatment · Evidence Policy · FACT / INFERENCE / UNKNOWN · Opportunity Type · Sales Conclusion 五值体系 · 13 个 Internal Key · Page 1 / 2 / 3 PDF 结构 · Default Invocation Protocol · `render_pdf.py` · Markdown / PDF 输出机制。

**未新增**：BDD 评分 · 100 分制 · Technical Fit · 设备选型 · 工艺参数 · 方案推荐 · 测试方案 · Quote Readiness · CRM 功能 · 新 Skill。

---

## 11. 是否出现副作用

| # | 项 | 结论 |
|---|---|---|
| 1 | **唯一越界项**：`output-visual-rules.md` 1 行计数同步（`27 条` → `29 条硬性约束`，第 174 行） | 已在第 1 节声明；diff 确认差异**恰为 1 行**；可回退 |
| 2 | 召回损失（**预期内**，非缺陷） | T3 收紧 + Gate 使部分"有废水但无 BDD 信号"的主体下调：Festo `Target → Unknown`、ACC `High → Medium`。**这正是本 Patch 的目的**；损失规模需业务方确认（见 TBD 23） |
| 3 | **历史报告与新规则不一致** | 其余 9 份历史卡（Chemstock / Hikal / Aarti / Umicore / EnviroChemie / BASF / GEA / Ajay-SQM / Trinseo）仍按旧规则产出。按 Spec「不要重新跑全部历史客户」，**本次未重跑**；已登记 TBD 23 |
| 4 | **`Opportunity Type` 与 `BDD Relevance` 的语义不一致** | Festo 现为 `BDD Relevance = Unknown` 但 `Opportunity Type = End-user Opportunity`。因 Spec **明确禁止修改 `Opportunity Type`**，未改动。已登记 Observation（下方第 14 节） |
| 5 | **`Priority Site` 与 `Industry Match` 的语义张力** | Festo `Industry Match = Unknown` 但仍输出 `Priority Site = Krishnagiri`。因 Spec 禁止修改 `Priority Site`，且该字段依据厂区级证据（而非 Industry Fit），未改动。已登记 Observation |
| 6 | Gate 在业务 PDF 中不可见 | 按 Spec「不新增 PDF 字段」，Gate 档位只写入 **Markdown 附录 B**。业务员看不到"为什么只判 Medium"的档位名（原因正文已说明证据与缺口）。已登记 TBD 22 |
| 7 | PDF 结构 / 页数 / 渲染层 | **零副作用**：三份 PDF 均 **3 页**（逐页单独渲染各 1 页）· Page 2 为 5 张销售信息卡 · Page 3 为 8 条关键依据 · 无 Gate 术语泄漏 · 无审计信息泄漏 · 无 `⟪P2⟫` 标记泄漏 |

---

## 12. 是否影响 Partner Path

**否。**

- Gate 的适用范围在规则文件中被写死为 **"仅作用于 End-user Path 的 `BDD Opportunity = High` 判定"**（`bdd-relevance-rules.md` 第四节定位表第 4 条 + 硬规则第 7 条；`SKILL.md` §五、决策链硬规则 7、§八 第 7 步均重申）。
- Partner Path 的 `High` 判据（**能力确认 + 技术组合重叠 + ≥ 2 项渠道 / 项目证据**）**一字未改**。
- 判定流程中标注 **"Partner Path 跳过本步（Gate），规则不变"**。
- 已完成的 Partner Path 案例（GEA Group = `Partner·EPC` / EnviroChemie = `Partner·EPC +| Technology Partner`）**未重跑、不受影响**。
- **Patch A 的 T3 收紧也不影响 Partner Path** —— Partner Path 判的是"能否把 BDD 纳入交付组合"，不用 T3 性质口径。

---

## 13. 是否影响 PDF / UI

**否。**

| 检查项 | CABB | Festo | ACC |
|---|---|---|---|
| PDF 页数 | 3 | 3 | 3 |
| 逐页单独渲染 | 1 / 1 / 1 | 1 / 1 / 1 | 1 / 1 / 1 |
| Page 1 结构（4 组 Header / 12 表格行 + 1 结论卡） | 4 / 12+1 | 4 / 12+1 | 4 / 12+1 |
| Page 2 `si-card` 数 | 5 | 5 | 5 |
| Page 3 `ev-card` 数 | 8 | 8 | 8 |
| Page 3 审计术语（FACT / INFERENCE / Confidence / Decision Impact） | 0 处 | 0 处 | 0 处 |
| Gate / 审计信息泄漏进 PDF | 0 处 | 0 处 | 0 处 |
| `⟪P2⟫` 标记泄漏 | 无 | 无 | 无 |
| 越界输出（小试 / 寄样 / 选型 / 报价 / 工艺参数） | 0 处 | 0 处 | 0 处 |

`render_pdf.py` md5 与备份**完全一致**；`assets/output-card-template.md` md5 与备份**完全一致**。**Page 1 / 2 / 3 的版式、字段、卡片数、页数全部未变** —— 变的只是三个字段的**取值**与结论卡**取值**。

---

## 14. 新增 Observation / TBD

### Observation（本次观察到、需业务方判断）

| # | 观察 | 建议归属 |
|---|---|---|
| O1 | **`Opportunity Type` 与 `BDD Relevance` 出现语义不一致**：Festo `Relevance = Unknown` 但 `Opportunity Type = End-user Opportunity`。本次因 Spec 禁止修改 `Opportunity Type` 而未动。**若未来允许，建议加一条"`BDD Relevance = Unknown` 时 `Opportunity Type` 同步为 `Unknown`"的联动规则** | 销售 + 架构 |
| O2 | **`Industry Fit = Unknown` 会连带把 `BDD Relevance` 压到 `Unknown`**，而 `Sales Conclusion` 第 5 步的适用范围文本写的是"`BDD Relevance ∈ {High, Medium}`" —— 本次按**第 5 步标题「其余情况」的兜底语义**处理为 `建议先验证`。`sales-conclusion-rules.md` **未修改**（Spec 禁止修改其五值体系）。**建议澄清"`Relevance = Unknown` 且有需求证据"应落哪一档** | 销售 + 架构 |
| O3 | **T3 收紧后，"有复杂有机工艺但未公开载明难降解"的主体没有落点**（既非 Target、又非 A1~A3、也不能判 Outside）→ 现落到 `Unknown`。**建议评估是否新增一类 Target（如 T5「复杂有机合成类制造业」）** | 销售 |
| O4 | **`Priority Site` 与 `Industry Match` 的张力**：Festo 仍输出 `Priority Site`。该字段依据厂区级证据、不依赖 Industry Fit，故未改；**但业务员可能误读为"这是目标客户"** | 销售 |
| O5 | **Gate 在业务 PDF 中不可见** —— 业务员只看到 `Medium` / `Unknown` 与原因正文，看不到档位名与 8 条硬规则。**如需可解释性，建议给 Page 2 加一行"BDD 相关性依据"（属展示层变更，须单独授权）** | 销售 |
| O6 | **CABB 的 `Strong` 结论完全依赖 E12（一份 2022 年提交 UNGC 的 CR 报告）** —— 若该证据被更新或被推翻，CABB 会一并回落 `Medium`。**说明 Gate 的档位对单一证据较敏感** | 技术 + 销售 |

### TBD（已写入 `SKILL.md` §十四 与两个规则文件）

| # | TBD 项 |
|---|---|
| 1 | T3「T3 证据门槛」9 项清单是否需增删；"高 COD"是否需给浓度口径（**当前不设阈值**） |
| 1b | 是否需新增一类 Target（T5「复杂有机合成类制造业」） |
| 21 | Gate 的 `Strong` 信号清单是否需增删；`Moderate` / `Strong` 边界（"富溶剂工艺" vs "已明载难降解"）是否清晰 |
| 22 | Gate 结果是否需要业务可视化位 |
| 23 | Patch A 收紧 T3 后**是否需要重跑历史客户**（Festo / GEA 等曾按旧口径判 Target） |

---

## 附 · 执行纪律声明

1. **Patch A 与 Patch B 全部由规则自动得出三家公司的新结果**，未出现「为通过测试而写死 CABB = High / Festo = Medium / ACC = Medium」的情形 —— 三家结果分别为 `High` / **`Unknown`** / **`Medium`**，其中 **Festo 落在 `Unknown` 而非 `Medium`**，正是因为按规则体系"条件 ① 先不成立"，而非迎合预期。
2. **CABB 未被人工锁定** —— 其 `Strong` 由 E12 / E8 两条证据自然满足，已在第 5 节逐条说明"为什么满足"。
3. 备份可完整回退：`D:/Case Flow/_bdd-skill-archive/V1.1.3-backup-20260927-b/`（15 文件 md5 全 MATCH）。
4. **已完成，按要求停止**：未进入 V1.1.4、未修改 Partner Path、未修改 Priority Site、未重跑其余历史客户、未继续优化。
