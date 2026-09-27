# Partner Cooperation Evidence Gate Patch — 交付报告

**执行日期**：2026-09-27 ｜ **Skill 版本**：V1.1.3（含 FW Rule Patch + BDD-Specific Relevance Gate Patch）
**备份**：`_bdd-skill-archive/V1.1.3-backup-20260927-c/`（15 文件 md5 全 MATCH，可完整回退）

---

## 1. 修改文件清单

**已改 4 个（全部规则文件；`render_pdf.py` 零改动）**

| 文件 | 行数变化 | 改了什么 |
|---|---|---|
| `references/bdd-relevance-rules.md` | +约 150 | **主体**：新增第五节 `Partner Cooperation Evidence Gate`（四档 + 硬规则 10 条 + 条件 A~F + 映射表 + Conflict 5 项检查 + 与 End-user Gate 的区别）；第三节 B 表加 E / F；判定流程新增第 7 步；封顶速记 +3 行；错误对照 +4 条；待校准 +3 项；原五~十一节顺延为六~十二 |
| `SKILL.md` | +约 70 | Patch 声明块；§三 新增「三条禁止推导」；§五 取值定义表 Partner 列改 A~F + 硬规则 +3 条；决策链图与硬规则 8；§八 第 7 步 Partner 专用顺序；**硬性约束 31 / 32**；§十二 文件说明；TBD 24 / 25 / 26 |
| `references/opportunity-type-rules.md` | +7 | 第三节加 `Conflict` 边界交叉引用（**不改五值与复合规则**） |
| `references/output-visual-rules.md` | **±0** | 仅 1 行计数同步：`30 条`→`32 条硬性约束` |

**共 15 个文件（未增减）／5,641 行。**

## 2. Partner `High` Before / After

| | Before | After |
|---|---|---|
| 条件 | ① 行业对口 ② 能力确认 ③ 技术组合重叠 ④ ≥2 项渠道 / 项目证据 | **A** 行业对口 **B** 能力确认 **C** 技术组合重叠 **D** ≥2 项渠道 / 项目证据 **+ E** **`Partner Cooperation Evidence ∈ {Confirmed, Supported}`** **+ F** **Conflict 控制** |
| `Medium` | 重叠度或渠道证据仅 1 项 | 上列 **或 A+B+C+D 已满足但 Gate 未过** |
| 问题 | **对任何大型水处理 EPC 都会自动成立** → 机会档位虚高（GEA / Veolia 两例复现） | 新增「合作机会」证据维度，与能力 / 场景证据**分别取证** |

## 3. Partner Cooperation Evidence Gate 完整规则

**回答的唯一问题**：是否存在**公开证据**表明 **Boromond / 第三方 BDD 技术**有机会进入该 Partner 的**技术、采购或项目交付体系**？
**不回答**：Partner 技术强不强 / 是否覆盖 BDD 场景 / 项目多不多。

| 档 | 判据（须 FACT + Source） |
|---|---|
| `Confirmed` | ① 存在**落在 BDD / 高级氧化 / 电化学氧化 / 难降解氧化域**的**外部方技术被集成或联合交付的具体案例（须点名技术 / 装置 / 项目）**；② 正在采购第三方电化学氧化设备 / 电极 / 模组；③ 招标或采购 BDD / diamond electrode / electro-oxidation 产品；④ 公开文件出现外部电极 / 反应器 / 电化学技术供应商；⑤ 已存在同技术域内「类似 Boromond 角色」的外部合作方 |
| `Supported` | 有明确第三方技术合作 / 供应 / 集成机制，**但证据不落在 BDD 域**（OEM / technology partner ecosystem、approved vendor / supplier qualification、多家第三方核心工艺设备、EPC 公开采购外部核心组件、长期与外部工艺公司联合交付、产品线非完全自研封闭） |
| `Unverified` | 只能确认 EPC 能力 / 技术组合 / 项目数量 / 场景重叠，**未发现**任何第三方集成 / 采购 / 合作机制证据 |
| `Conflict` | 出现自有 BDD 竞争技术信号，**且同时缺乏**合作开放证据 |

**判定顺序**：BDD 域内外部集成证据 → `Confirmed`；BDD 域外合作机制 → `Supported`；均无 → `Unverified`；自有同域竞争且无开放证据 → `Conflict`。

**合作证据强度两维度**（仅 `Confirmed` + `Conflict = Yes` 并存时用于 `High` / `Medium` 定档）：**BDD 域相关性**（加分：落在高级氧化 / 电化学氧化域；减分：膜 / 分离 / 药剂 / 仪控）· **机制外部性**（加分：集团外独立主体；减分：集团内兄弟公司 / 网络成员）。**定档口径：两维度均加分 → 可判 `High`；任一维度减分 → 落 `Medium`。**

**映射表（机械执行）**

| Cooperation | Conflict | `BDD Opportunity` |
|---|---|---|
| `Confirmed` | No / Low | `High` |
| `Confirmed` | Yes | `High` 或 `Medium`（按两维度重算，**不得机械 High**） |
| `Supported` | No | `High` 或 `Medium` |
| `Supported` | Yes | **通常最高 `Medium`** |
| `Unverified` | 任意 | **不得 `High`**（通常 `Medium` / `Unknown`） |
| `Conflict` | Yes 且无开放证据 | **不得 `High`** |

**三条分离硬规则**：`Strong Technical Capability` ≠ `High Cooperation Opportunity` ｜ `Strong Scenario Overlap` ≠ `High Cooperation Opportunity` ｜ **技术越 proprietary 不得解释为越有吸引力**（对 Boromond 意味着更难切入）。
**字段独立**：Gate 只影响**机会强度**，不改 `Opportunity Type`；`Demand Status` 与之**双向独立**；不新增 Internal Key / PDF 字段 / 评分。

## 4. Conflict Before / After

| | Before | After |
|---|---|---|
| 定位 | 标签（标注即可） | **不是装饰性标签** —— 出现 `Conflict` 时判 `High` 前**必须检查 5 项**：① 技术路线是否直接重叠 ② 是否自研 / proprietary ③ **是否有第三方集成机制** ④ **是否有外部核心组件采购证据** ⑤ Boromond 属 supplier / partner / competitor 哪一类 |
| 否决条 | 无 | **第 3、4 项均为 `Unknown` → 不得因技术重叠或项目能力强而判 `High`** |
| 与档位关系 | 不参与档位 | 只影响**机会强度**；**不改 `Opportunity Type` 五值与复合规则** |

## 5–7. 三家公司回归结果

### Veolia Water Technologies — Gate = `Supported`

| 维度 | 结果 | 依据 |
|---|---|---|
| （1）机制存在性 | **✔** | 与 **MIOX** 签**联合分销协议**；获 **Genesis Water** 技术的**全球矿业独家推广权**并被**授予 approved vendor status**；与 **NanoH2O** 签约并经**中试为其膜做供应商资格验证**后向其客户供货；PFAS / 微污染物域"**partnerships with startups**"；研发体系公开"评估膜性能以**选择合适供应商**"、**220 个国际合作伙伴**（E33 / E34 / E35） |
| （2）机制外部性 | **✔** | 相对方均为集团外独立主体 |
| （3）BDD 域相关性 | **✗** | **未发现任何第三方高级氧化 / 电化学氧化技术被其集成或联合交付**；其氧化域与电化学氧化均**自有**（E7 / E8）；电化学氧化的产品化形态与技术来源 = `UNKNOWN · searched`（E31） |
| Conflict 5 项 | ① 直接重叠 **是** ② proprietary **是** ③ 第三方集成机制 **是（非 Unknown）** ④ 外部组件采购证据 **是（非 Unknown）** ⑤ **以 competitor 为主** | — |

**判定**：`Supported` + `Conflict = Yes` → **通常最高 `Medium`** → `BDD Opportunity = Medium`。

### GEA Group — Gate = `Unverified`

| 维度 | 结果 | 依据 |
|---|---|---|
| （1）机制存在性 | **✗** | ZLD 与工业废水整线公开表述为 **"single-source supplier"**，产品线品牌（Niro / Westfalia Separator / GEA Wiegand / Tuchenhagen / GEA Filtration）**均为集团自有**（E30）；**已检索未查到**第三方核心工艺采购 / OEM / approved vendor / 联合交付证据（E31） |
| （2）（3） | 不判定 | 因（1）未成立 |
| Conflict 5 项 | ① 直接重叠 **否（仅场景重叠）** ② proprietary **是** ③ 第三方集成机制 **`Unknown`** ④ 外部组件采购证据 **`Unknown`** ⑤ 无法判定 | **第 3、4 项均为 `Unknown`** |

**判定**：`Unverified` + Conflict → **不得 `High`** → `BDD Opportunity = Medium`。（`Financial Warning` 仍为 `No`，FW Rule Patch 结果**未被改动**。）

### EnviroChemie — Gate = `Confirmed`（但机制外部性减分）

| 维度 | 结果 | 依据 |
|---|---|---|
| （1）机制存在性 | **✔** | **up2e! 开发的 Roturi® 臭氧工艺装置被集成进其 Envochem AOP 装置**（"AOP using ozone with a Roturi® device"）；自述 **«verfahrensoffen»（工艺开放）**、在中试中比对不同 AOP 路线；**EnviModul 模块化装置"允许按需追加工艺段"**（E33 / E34）；集团内跨公司联合交付（Enwa）、**外部研究机构 IUTA + Roche**、**外部仪表合作伙伴**（E35） |
| （2）机制外部性 | **✗（减分）** | up2e! / Enwa **均为 EnviroWater Group 成员**（2020-10 由 EnviroChemie Group 更名，隶属 SKion Water）→ **集团 / 网络内**；集团外仅研究机构与仪表伙伴，**非核心工艺技术** |
| （3）BDD 域相关性 | **✔（加分）** | Roturi® 为**臭氧高级氧化强化装置**，落在高级氧化域 |
| Conflict 5 项 | ① **部分**（自有 AOP 同属高级氧化家族，非电化学路线）② proprietary **是** ③ 第三方集成机制 **是** ④ 外部组件采购 **部分** ⑤ **partner 通道最清晰** | — |

**判定**：命中 5.1 ① → `Confirmed`；`Confirmed` + `Conflict = Yes` → 两维度重算（**域相关性加分 / 外部性减分**）→ 按定档口径「任一维度减分 → `Medium`」→ `BDD Opportunity = Medium`。

> **三家对比结论**：**EnviroChemie 是三个回归主体中唯一存在 BDD 域内外部技术集成证据者**，合作开放度最高；但因该案例相对方为集团内成员，按 5.1 定档口径仍落 `Medium`。**未被人工锁定为 `High`，也未为通过测试而改写。**

## 8. 三家公司 BDD Opportunity Before / After

| 主体 | Before | After | Gate |
|---|---|---|---|
| Veolia Water Technologies | 🟢 `High` | 🟡 **`Medium`** | `Supported` + Conflict |
| GEA Group | 🟢 `High` | 🟡 **`Medium`** | `Unverified` |
| EnviroChemie | 🟢 `High` | 🟡 **`Medium`** | `Confirmed`（外部性减分） |

**三家全部由 High 落为 Medium —— 这正是本 Patch 的目的**（原 B 表对任何大型水处理 EPC 自动成立）。

## 9. Sales Conclusion Before / After

| 主体 | Before | After | 重算路径（沿用既有五值规则，未改规则） |
|---|---|---|---|
| Veolia | 🟢 建议开发 | 🟡 **建议先验证** | 一票否决 ✗ → 第 2 步 ✗ → 第 3 步需 `High` ✗ → 第 4 步 A 需 `High` ✗、B 需 `Demand ∈ {Confirmed, Strong Signal}` ✗ → **第 5 步** |
| GEA | 🟢 建议开发 | 🟡 **建议先验证** | 同上（`FW = No`、`Risk = Unknown` 均不构成降档依据） |
| EnviroChemie | 🟡 建议先验证 | 🟡 **建议先验证**（维持） | `Relevance = Medium` + 卡上现有 `FW = Yes` → 第 4 步 A 需 `High` ✗ → 第 5 步 |

> **EnviroChemie 的 `FW = Yes` 系 FW Rule Patch 之前的旧口径**（依据为低置信度第三方登记来源的连续亏损数据）。本 Patch **未授权修改 `Financial Warning`**，故按卡上现有取值参与重算；若按现行 6.1 白名单同步，该字段应回落、结论将变为 `建议开发` —— 已在卡内与 Observation 中显式标注。

## 10–12. 字段保持情况

| 检查项 | 结果 |
|---|---|
| **Demand Status** | ✅ 三家**全部保持** 🟡 `Potential`（Gate 未反向影响） |
| **Opportunity Type** | ✅ 三家**全部保持** `EPC / Integration Opportunity +\| Technology Partner Opportunity`（Gate 只改强度） |
| **Financial Warning** | ✅ 三家**取值未动**（Veolia `No` / GEA `No` / EnviroChemie 卡上原值 `Yes`，未修改） |
| `Priority Site` / `Current Treatment` / `Contact` / `Commercial Risk` / `Business Change Signal` | ✅ 未动 |
| 13 个 Internal Key | ✅ 未增删（12 表格行 + 1 结论卡） |

## 13. 未修改规则文件清单（md5 全 MATCH）

`scripts/render_pdf.py` · `assets/output-card-template.md` · `evidence-policy.md` · `sales-conclusion-rules.md` · `customer-type-playbook.md` · `current-treatment-rules.md` · `contact-role-map.md` · `must-ask-params.md` · `lead-signals.md` · `wastewater-signal-map.md` · `bdd-fit-rules.md` —— **共 11 个**。
另：End-user Path · `BDD-Specific Relevance Gate` · T1~T4 与 Industry Map · T3 证据门槛 · Demand Status / PWE·CSD · Financial Warning 白名单 · Business Change Signal · Commercial Risk · Current Treatment · Priority Site · Contact Strategy · Evidence Policy · FACT / INFERENCE / UNKNOWN · `Sales Conclusion` 五值与规则 · 13 Internal Key · Default Invocation Protocol · 三页结构与 Page 1/2/3 · **`render_pdf.py`** · Output Delivery Rule · Markdown / PDF 输出机制 **均未动**。
未新增：Partner Score / Supplier Score / 100 分制 / 技术评分 / 信用评分 / CRM / Supplier Database / Vendor Qualification System / Procurement Module / 新 Skill / 报价 / 设备选型 / 技术方案。

## 14. 是否影响 End-user Path

**否。** 新 Gate 在规则文件中写死「**仅作用于 Partner Path**」；判定流程标注 End-user 跳过第 7 步；`BDD-Specific Relevance Gate`（第四节）四档与映射**一字未改**；两个 Gate 明确「**不得混用**」并列表对比。已完成 End-user 案例（Ajay-SQM / BASF / CABB / Festo / ACC）**未重跑、不受影响**。

## 15. 是否影响 PDF / UI

**否。** `render_pdf.py` 与 `output-card-template.md` md5 完全一致；三份卡仍 **3 页**（逐页单独渲染各 1 页）· 12 表格行 + 1 结论卡 · Page 2 五卡 · Page 3 八条 · 越界输出 0 处。**Gate 档位名与规则术语在业务 PDF 中 0 处**（含修复 1 处：EnviroChemie 卡首部说明曾含 Gate 名）。变的只是**机会档位取值、结论卡取值、判定依据措辞与附录 B**。

## 16. Negative Control（轻量逻辑测试 · 未产出完整卡）

**选定主体：Industrie De Nora S.p.A.（De Nora Water Technologies）**

| 输入 | 证据 |
|---|---|
| Capability | **极高** —— "100+ years pioneering advancements in **electrochemistry**"；全球电极龙头，**DSA® 自有专利电极技术**、**proprietary systems**；5 个研发中心；水技术组合含 **AOP（Advanced Oxidation Processes）**、SORB（PFAS / 砷）、Capital Controls® 臭氧、CECHLO / ClorTec 现场次氯酸钠、TETRA® 介质过滤 |
| Scenario Overlap | **极高** —— 其 AOP 明确面向"municipal and industrial water streams"难处理污染物；应用清单含 **PFAS 水处理**、工业工艺水 |
| 自有封闭技术体系 | **是** —— "high-efficiency electrodes and **proprietary systems**"、"our **DSA® technology**"；产品组合均为自有品牌 |
| 第三方核心技术集成证据 | **未发现** |

**门控结果**：`Partner Cooperation Evidence = Conflict`（自有电化学平台，**与 BDD 同域**）且**无开放合作证据** → 按映射表 **`BDD Opportunity` 不得 `High`**；若机械执行（A~D 成立但 E 未过）落 `Medium`。

**验证目的达成**：**Capability High + Scenario Overlap High 不能自动推出 BDD Opportunity High** —— 即使主体是电化学领域的**最强能力者**，只要技术自研封闭、无第三方集成通道，机会强度即不得判 `High`。

## 17. 是否出现副作用

1. **Partner 档位系统性下沉（本 Patch 目的所在）**：三家同时由 `High` → `Medium`，Partner 渠道开发优先级需业务方复核（TBD 26）
2. **唯一越界改动**：`output-visual-rules.md` 1 行计数同步（`30 条`→`32 条硬性约束`），diff 确认恰为 1 行
3. **发现渲染器健壮性缺口（未修改）**：`render_pdf.py` 的 `md_to_html_body` 对「前面有表格、但自身下一行不是分隔行的 `|` 开头行」**没有兜底推进** → 会**无限循环**（本次因我在表格与 `</details>` 之间误留空行而触发 3 次，已从 Markdown 侧修正）。**按 Spec 禁止修改 `render_pdf.py`，故仅登记为 Observation / TBD。**
4. **EnviroChemie 的 `FW = Yes` 为旧口径**：与本 Patch 结果叠加后，其"机会 Medium + 财务警示 Yes"两条各自成立；若业务方决定同步 FW 白名单，结论会变为 `建议开发`（已登记）
5. **无其他副作用**：`Sales Conclusion` 五值规则未改、`Opportunity Type` / `Demand Status` / `Financial Warning` / `Priority Site` / `Current Treatment` / 13 Key / PDF 结构 / `render_pdf.py` 全部零改动

## 18. 新增 Observation / TBD

**Observation**

| # | 内容 |
|---|---|
| O1 | **三家 Partner 同时落 `Medium`** —— 是否意味着 Gate 过严、或原档位确实虚高，需业务方用真实渠道判断校准 |
| O2 | **「集团内网络成员提供核心工艺装置」是否算 `Confirmed` 的完全外部性证据**（EnviroChemie / up2e! 案例）—— 这是三家结果分野的关键点 |
| O3 | **`Support`（Veolia）与 `Unverified`（GEA）在档位上同为 `Medium`** —— 二者在业务含义上差异明显（有机制 vs 无机制），但映射表未区分，未来或需分档 |
| O4 | `render_pdf.py` 无兜底推进的无限循环风险（见副作用 3） |
| O5 | EnviroChemie 卡的 `FW = Yes` 属旧口径残留，与其他卡的 FW 口径不一致 |

**TBD（已写入 `SKILL.md` §十四 与 `bdd-relevance-rules.md` 第十二节）**

| # | 内容 |
|---|---|
| 24 | `Confirmed` / `Supported` 边界 —— 「集团内网络成员提供核心工艺装置」是否算 `Confirmed` |
| 25 | 合作证据强度两维度（BDD 域相关性 / 机制外部性）的定档权重是否够用 |
| 26 | Partner Gate 是否导致 Partner 机会普遍下沉（三例同时重算） |
| 27 | 是否修复 `render_pdf.py` 的兜底推进缺口（需单独授权） |

---

**执行纪律声明**：三家结果全部由 **Evidence → Cooperation Gate → Conflict → BDD Opportunity → 既有 Sales Conclusion 规则** 逐级机械得出 —— Veolia / GEA 的 `Medium`、EnviroChemie 的 `Medium` **均非人工指定**；EnviroChemie **未因"正向控制组"身份被锁 High**；Negative Control 独立验证了"能力 + 场景 ≠ 合作机会"。完成后**已停止**：未进入 V1.1.4、未改 Priority Site、未改 PDF、未重跑其余历史客户、未新增字段。
