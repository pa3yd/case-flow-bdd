# 工作区长期记忆 · Case Flow

> 只记录跨会话仍有价值的项目约定与架构决策。日常过程记录见 `YYYY-MM-DD.md`。

---

## 一、本工作区在做什么

两条并行的产品线，**边界严格分离，不得互相串味**：

| 线 | 目标 | 状态 |
|---|---|---|
| **Skill 线** | `bdd-inquiry-analyzer` —— BDD 客户情报与背调 | **V1 Scope Frozen（2026-09-26）** |
| **平台线** | 波乐美水质方案智能平台 —— 案例库 + 设备计算 + 方案输出 | 计划已出（`波乐美水质方案智能平台_实施计划.md`），未启动 |

**为什么先做 Skill**：背调只依赖公开信息，不被"Boromond 历史案例数据资产化"这个最大瓶颈卡住，能立刻见效。
**复用关系**：Skill 的判定规则经回测证明准确后，可直接搬进平台 L2 检索层与 L4 推理层——一次投入，两处复用。

---

## 二、bdd-inquiry-analyzer · V1 冻结约定（**强约束**）

### 唯一职责

**BDD 客户完整企业背调 + 客户开发判断。** 除此之外一律不做。

### ❌ 明确不做（写死在 SKILL.md 第一节）

Technical Fit · 项目报价 · 设备选型 · 小试技术方案 · 工程计算 · 正式技术方案 · 正式项目跟进 · 自动邮件/回复 · 案例数据库

### 12 步决策链（严格单向，不跳步、不回推）

```
Input → Company Verification → Evidence Collection → Company Profile
  → Customer Type → Industry Fit → BDD Relevance → Demand Evidence
  → Commercial Risk → Missing Critical Data → Contact Strategy
  → Next Action → Evidence Appendix
```

### 四条不可违反的判定规则

1. **Industry Fit = High → 不得推导 BDD Relevance = High。** Industry Fit 只是 BDD Relevance 的 8 项输入之一。
2. **BDD Relevance = High → 不得推导 Demand Evidence = High。** 有应用场景 ≠ 有采购需求。
3. **无废水信号 + 无环境证据 → BDD Relevance 最高只能 `Medium`。**
4. **不做任何跨字段自动串联推导。**（V1 已删除原 TF→QR 串联）

### BDD Relevance 的 8 项输入

Industry / Company Business / Products / Manufacturing Activity / Manufacturing Process（仅公开可验证时）/ Wastewater Signals / Environmental Evidence / Project·EIA·Permit·Tender·ESG·Job signals

**输出必附** `Reason` + `Evidence` + `Confidence`，缺任一判定无效。

**标准反例（用户明确指定）**：API 原料药企业 —— 行业 `Target`，但未确认生产活动、无废水信号、无环境证据 → `BDD Relevance = Medium` 或 `Unknown`，**不得给 High**。

### 主卡 10 字段（不得增删）

Company · Company Profile · Customer Type · Industry Fit · BDD Relevance · Demand Evidence · Commercial Risk · Missing Critical Data · Recommended Contact Role · Next Action

`BDD Relevance` 是唯一在主卡内展开三行依据（Reason / Evidence / Confidence）的字段。

### 证据政策

FACT 必须有 Source；INFERENCE 必须有 Reason + Confidence；UNKNOWN 不得补全。适用范围是**所有关键外部结论**。

### 自动触发约定（2026-09-26 追加）

- description 用 **YAML 块标量 `|`**，必须含「即使对话中完全没有出现 BDD / 波乐美 / 废水字样也应主动触发」这句。
- **禁止** description 内出现 `报价 / 技术方案 / 设备选型 / 小试方案`（会被误当触发词）。排除类表述统一写「方案设计 · 选型 · 工程计算 · 项目跟进 · 代写邮件 · 商务价格」。
- 与 `ai-inquiry-analysis` 为**双向互斥**：消费品外贸询盘走后者，工业企业/环保/电化学废水背调走本 Skill，两者 description 互相写反向指针。

### 归档区（Skill 目录之外，不参与运行）

`D:/Case Flow/_bdd-skill-archive/V1.0-freeze/` —— 13 个文件，含 6 个 pre-freeze 全量快照 + 6 个 B/C 类归档件 + README（含回收条件）。

### 实跑记录与已知规则缺口（**改 Skill 前必读**）

已完成 **5 次真实背调**，交付物均为 `D:/Case Flow/客户情报卡_{公司}_{日期}.md`（1 屏主卡 + 附录 A）：

| # | 主体 | 国别 | Customer Type | BDD Relevance | Demand Evidence |
|---|---|---|---|---|---|
| 1 | Chemstock LLC | 阿联酋 | 贸易商/中间商 | Low | Unknown |
| 2 | Hikal Limited | 印度 | 终端业主 | Medium | Potential |
| 3 | Aarti Industries Ltd | 印度 | 终端业主 | Medium | Potential |
| 4 | Umicore SA/NV | 比利时 | 终端业主 | Medium | Potential |
| 5 | EnviroChemie GmbH | 德国 | **环保工程公司（EPC）** | Medium | Potential |

**五次实跑暴露并累积的规则缺口**（优化计划见 `D:/Case Flow/BDD-Skill-V1.1_优化方案与执行计划.md`；用户未授权前**不得自行修改 Skill**）：

| 缺口 | 复现次数 | 说明 |
|---|---|---|
| `High` 定义上不可达 | **5 次** | 判据①依赖 Industry Fit，而清单未填 → 恒 `Unknown` |
| 输入 6「废水信号」限定询盘文字 | **4 次** | 仅凭公司名/官网背调时永远封顶 `Medium`，即便环境证据充分 |
| `Commercial Risk` 无询盘时恒 `Unknown` | **4 次** | 危险信号表 13 行全为**询盘交互行为**，无互动则无来源 |
| 接触战略矩阵缺格 | **3 次** | `Potential × Unknown`、`Unknown × Unknown` 未定义，按保守侧外推 |
| `Low` / `Medium` 判据含"行业对口"前提 | 2 次 | 与该字段恒 `Unknown` 冲突 |
| 8 项输入为"废水产生方"口径 | 1 次（第 5 次） | **对 EPC / 集成商型主体不适配**，走量主渠道无法被准确表达 |
| `Commercial Risk` 双口径冲突 | 1 次（第 5 次） | customer-type-playbook 用类型级先验，evidence-policy 自称唯一来源且只用行为信号 |
| 危险信号表不含财务类信号 | 1 次（第 5 次） | 连续亏损属实质回款风险，表内无对应条目 |
| Customer Type 六分类缺"竞争关系"维度 | 1 次（第 5 次） | 既是集成商又自建竞争工艺线的主体无位置 |
| Customer Type 判定表为中国工商口径 | 1 次（第 5 次） | 海外商业登记口径需人工映射 |
| 规模字段在海外主体不可靠 | 贯穿全部 | 同一公司员工数在不同来源可差 10 倍以上 |

**纪律要求（用户已明确，勿放松）**：不输出 Technical Fit / 工艺参数 / 设备选型 / 技术方案 / 达标承诺 / 金额；`Contact Role` 只允许输出岗位角色，人名仅可来自官网 / 政府公示 / 招投标 / 上市公告 / 官方媒体；第三方聚合站（SignalHire、Crustdata、Prospeo 等）人名**一律弃用**。检索到疑似处罚记录时必须交叉核对主体，防止同集团近似名称误关联（Aarti 案例曾差点因此**结论反转**）。

---

## 三、工作方式约定（用户偏好）

| 项 | 约定 |
|---|---|
| 推进节奏 | 编号化 Task / Round / Patch 逐轮迭代 |
| 校验要求 | 执行前后显式校验（文件列表 / 字节数 / HEAD 对比），输出带命名字段的 PASS/FAIL 报告 |
| 报告结构 | 结论 → 修复 → 交付 → 回归测试 |
| 硬约束 | 不重建 UI、不创建重复系统；新规格覆盖旧断言 |
| 改前确认 | 涉及结构改动时**先出审计/建议清单，等用户确认再动手** |
| 归档原则 | **不删除有未来价值的内容，统一归档到 Skill 目录之外** |
| 语言 | 中文叙述 + 英文/代码标识符双语；零基础友好 |

---

## 四、环境与工具

- WorkBuddy 位置：`C:\Users\Administrator\.workbuddy\`
- Skill 存放：`~/.workbuddy/skills/`（用户级）
- 已有相关 Skill：`ai-inquiry-analysis`（**泳具/体育用品外贸专用**，与 BDD 业务不通用，勿混用）
- 账户：Windows / Administrator
- **PDF 渲染链**：本机无 `markdown` / `weasyprint` / `wkhtmltopdf`。可用方案 = **Chrome headless**（`C:/Program Files/Google/Chrome/Application/chrome.exe`，回退 Edge `C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe`）+ 自带 MD 子集解析器（`bdd-inquiry-analyzer/scripts/render_pdf.py`，零依赖）。
- 托管 Python：`C:/Users/Administrator/.workbuddy/binaries/python/versions/3.13.12/python.exe`

---

## 五、BDD Customer Intelligence Skill 当前版本（V1.1.3 · 2026-09-27）

**当前版本 = V1.1.3**，15 个文件（`SKILL.md` + 12 个 references + 1 asset + 1 script）/ 4987 行。

**版本链**：V1 设计 → Freeze → V1.1（结构升级）→ V1.1.1（Presentation Patch）→ V1.1.2（UI Refinement Patch）→ **V1.1.3（Sales Usability Patch）**。V1.1.1 / V1.1.2 / V1.1.3 均**只改展示层**，判断规则零改动。

**默认调用协议（V1.1.3 新增，SKILL.md 第「零」节）**：日常只给 **公司名 / 网址 + 背调意图**（背调 / 分析客户 / 是否值得开发 / BDD客户）即**自动跑完整 14 步**；默认 **Markdown + PDF 双输出**、自动用当前版本号、自动 13 字段、自动禁止预设结论、缺失自动写 `Unknown`。仅两种情形才追问：① 既无公司名也无网址；② 公司名存在多个完全不同的同名主体。**显式规格句式（严格回归测试 Prompt）保留生效，不被简化。**

**文档交付命名规范**：`{Company}_BDD_Intelligence_{YYYY-MM-DD}.md` + 同名 `.pdf`，存工作区根目录。

**主卡 13 字段**（1 页，四组呈现，2026-09-27 起）：`01 WHO ｜客户是谁`（公司/国家/主营业务/客户类型）· `02 WHY ｜为什么值得看`（行业匹配/BDD机会/需求状态）· `03 WHERE / WHO ｜从哪里切入`（现有废水处理/优先厂区/关键联系人）· `04 ACTION ｜现在怎么办`（待确认信息/下一步 + 开发建议结论卡）。

- **展示层（V1.1.2）**：字段列浅灰蓝底 + 固定 20% 宽 + 垂直居中；短状态用 **Badge**（红只用于风险/冲突/负面）；`Current Treatment` 四态中文（已确认/部分确认/规划中/未知）；长字段 `摘要⟪P2⟫其余`（摘要为原文精确前缀）；结论卡中文 16pt + 英文副标题。
- **PDF 三页（V1.1.3）**：**Page 1 完全不变**；**Page 2 = `SALES INTELLIGENCE ｜开发情报`** 5 张销售信息卡（Why BDD / Current Treatment / Priority Site / Who to Contact / What to Verify，字段取**完整原文**）；**Page 3 = `KEY EVIDENCE ｜关键依据`** 6~8 条，每条只写 **编号·主题 / 简洁事实 / 来源**，**PDF 零审计术语**。
- **审计层隔离（V1.1.3）**：`## 附录 B`（可溯源率 / 类型定义 / Decision Impact 说明 / 集团级 vs 厂区级 / 同名主体排除 / 来源冲突项）与 `## 边界声明` **只在 Markdown 保留，不进业务 PDF**（渲染层按此二标记切分，Markdown 原文一字不删）。**附录 B 与此约定必须延续到后续所有报告。**
- **附录 A 新增 `主题` 列（V1.1.3）**：第 2 列，中性短标题（≤20 字），仅作 Page 3 卡片标题的展示标签，**非判断字段**；缺失时渲染层降级为只显示证据编号。

**目标市场地图**：Target = T1 锂电池/电池材料/电池回收 · T2 制药/原料药 · T3 高 COD/难降解（性质口径）· T4 精细化工/农药/染料；Adjacent = A1 工业废水 EPC/AOP/集成 · A2 工业化学品/水处理药剂分销 · A3 设计院/院所。

**BDD Relevance 硬门槛（End-user Path）**：`High` 需 ① 行业对口 + ② 制造业活动确认 + ③ **PWE 或 CSD 至少一项成立** + ④ ≥2 项主体级证据，**四条同时满足**。缺 ③ → 最高 `Medium`。**注意：V1.1 删除的是"无询盘 → 最高 Medium"这条封顶，不是 ③ 本身。**

**2026-09-27 · BDD-Specific Relevance Gate Patch（规则修订 · 仅 End-user）**：
- **Patch A · T3 证据门槛**：`T3` 必须由**废水性质证据**（高 COD / 难降解 / 难处理 / 深度处理 / AOP 需求 / 明确复杂污染物）成立；**只存在工业废水 / 生产废水 / 阳极氧化废水 / 机加工废水 / 压铸废水 / 普通表面处理废水 / 一般排污许可 / 废水处理设施 / 废水量数据 → 一律不得判 `Target`**，改落 `Adjacent` / `Outside` / `Unknown`。举例清单降级为识别辅助（**行业标签不构成证据**）。
- **Patch B · `BDD-Specific Relevance Evidence Gate`**（`Strong` / `Moderate` / `Weak` / `Unknown`）：End-user `High` 的**第 5 个硬门槛**；`Strong`→`High`；`Moderate`/`Weak`→`Medium`；`Unknown`→`Unknown`；`Industry Fit = Unknown` → `Unknown`（**该封顶优先于 Gate 映射**）。**只作用于 End-user；Partner Path 规则不变**；不新增 Internal Key / PDF 字段 / 评分；档位只记 Markdown 附录 B。
- 硬性约束 **27 → 29 条**；新增红线 3「**废水相关性 ≠ BDD 相关性**」。

**2026-09-27 · Partner Cooperation Evidence Gate Patch（规则修订 · 仅 Partner Path）**：
- Partner `BDD Opportunity = High` 新增两条硬门槛：**E** `Partner Cooperation Evidence ∈ {Confirmed, Supported}`；**F** Conflict 控制。
- 新 Gate 只答一个问题：**第三方 BDD 技术能否进入该 Partner 的技术 / 采购 / 交付体系**；四档 `Confirmed` / `Supported` / `Unverified` / `Conflict`；`Unverified` 与 `Conflict`（无开放证据）**一律不得 High**。
- **三条分离硬规则**：能力 ≠ 合作机会；场景重叠 ≠ 合作机会；**技术越 proprietary 越难切入（减分项）**。
- **Conflict 去标签化**：判 High 前必查 5 项，**「第三方集成机制」与「外部组件采购证据」均为 Unknown 时不得判 High**。
- 档位只记 **Markdown 附录 B**；不改 `Demand Status` / `Opportunity Type` / PDF 结构 / 13 Key；**只作用于 Partner Path**。

**交付纪律（Delivery Scope Rule · 2026-09-27，正式输出规则）**：日常客户背调模式**最终只交付 2 个文件** —— `{Company}_BDD_Intelligence_{YYYY-MM-DD}.md` + 同名 `.pdf`。**HTML / Page PNG / 截图 / `_*-comparison` / debug 输出 / 临时提取文件一律只是内部渲染与回归的中间产物**，**不得作为最终交付展示、不列入用户产物、不写进交付清单**；**仅当用户明确要求**「视觉检查 / PDF 回归 / Before-After 对比」时才输出图片类产物。该规则**只约束交付范围**，不得据此修改 PDF / MD 内容、判断规则、13 个 Internal Key 或三页结构。落点：`SKILL.md` 头部声明块 + §零「最终交付边界」+ **硬性约束第 30 条** + `output-visual-rules.md` 第四部分与第六部分第 9 条。

**V1.1.3 硬边界**：不输出 Technical Fit / Quotation Readiness / 工艺参数 / 设备选型 / 技术方案 / 达标承诺 / 金额 / 报价状态；不得输出"建议小试"、不得固定"寄 5~10 L 水样"、不得自动进入小试流程 —— 已确认具体项目时只写「转交技术评估流程」。

---

## 五之二、Financial Warning Rule Patch（2026-09-27 · 规则修订，版本仍为 V1.1.3）

> **核心口径（后续所有报告必须遵守）**：**Business Change / Restructuring（业务变化 / 重组） ≠ Financial Distress / Financial Risk（财务困境）**。

- **`Financial Warning = Yes` 白名单化（仅 8 类）**：Insolvency 资不抵债 · Bankruptcy 破产 · Liquidity crisis 严重流动性危机 · Debt default 债务违约 · **Going-concern warning 持续经营重大疑虑** · Court-supervised financial restructuring 法院或债务层面财务重组 · 连续·重大·**集团层面**亏损**且**具明确财务压力（四条同时）· 官方财报/审计/监管披露明确指出的重大财务困难。**均须附可靠公开 Source。**
- **新增 `Business Change Signal`（`Yes / No / Unknown`）**：承接 10 类从 FW 移出的信息 —— Layoffs 裁员 · Management changes 高管变化 · Organizational restructuring 组织架构调整 · Business-unit restructuring 业务单元调整 · Plant consolidation 工厂整合 · Capacity reduction 产能调整 · Portfolio adjustment 业务组合调整 · Strategic transformation 战略转型 · **Site-level operating loss 单一厂区经营亏损** · Cost-cutting program 降本计划。判 `Yes` **必须输出 `Reason` + `Source`**；定位 **Context / Watch Item**。
- **8 条硬规则**：BCS=Yes **不得单独触发** `FW = Yes` / `Commercial Risk = High`，**不得导致** `Sales Conclusion` / `BDD Opportunity` / `Demand Status` 降档；不得写进风险字段定级依据；仅当同时具备白名单证据才可升级为 FW=Yes。
- **集团 vs 厂区分离**：厂区/业务单元的亏损、裁员、产能调整 → 归 BCS，**不得推出集团 `FW = Yes`**。
- **证据冲突**：同时存在「裁员/重组/厂区亏损」与「集团盈利/正常现金流/上调指引/分红回购/正常重大投资」时 → **优先判 BCS=Yes**，FW 依真实财务证据定级（无白名单证据 → `No`）；**不得用单条负面新闻覆盖更完整的集团财务事实**。
- **`FW = Yes` 不得机械降档（sales-conclusion 第 4b 步）**：必须答四问 —— ① 财务风险严重程度 ② 风险主体层级（集团 / 厂区 / 非目标主体）③ 是否影响本次潜在采购与付款能力 ④ 是否影响相关项目执行能力。任一指向影响本次 → 上限 `建议先验证`；风险主体非目标主体且有证据显示采购·付款·执行未受影响 → 可不降档；**结论原因中必须解释为什么该风险影响或不影响本次判断**。
- **硬性约束 25 → 27 条**（新增 26 BCS 不得单独降档 / 27 FW 不得机械降档）。
- **一票否决 = `Commercial Risk = High` / `BDD Relevance = Low`**（**`FW = Yes` 不在其中** —— 已修掉 SKILL.md 与 sales-conclusion-rules 的长期矛盾）。
- **修复效果**：BASF、GEA 由 `建议先验证` → **`建议开发`**。**Negative Control = Trinseo PLC**（Chapter 11 + 持续经营疑虑 + 债务违约 + S&P 'D'）→ FW = Yes ✅，A/B 对照证明该字段仍能降低一档。
- **文件改动范围**：`evidence-policy.md`（六节重写 + 新增七节）· `sales-conclusion-rules.md`（新增 4b 步）· `SKILL.md`（+硬约束 26/27）· `output-card-template.md`（新增业务变化块）· `output-visual-rules.md`（**仅 1 处计数同步** 25→27）。**`scripts/render_pdf.py` 与其余 10 个规则文件 md5 未改。**
- **备份**：`_bdd-skill-archive/V1.1.3-backup-20260927/`（md5 全 MATCH）。

**版本回退**：`_bdd-skill-archive/{V1.0-freeze-backup-20260926, V1.1-backup-20260926, V1.1.1-backup-20260926, V1.1.2-backup-20260927}/`（md5 全 MATCH）；删除规则见 `_bdd-skill-archive/V1.1-changes/V1.1-removed-rules.md`。

---

## 六、实跑记录（V1.1 起 13 家 · 交付物 = `{Company}_BDD_Intelligence_{日期}.{md,pdf}`）

| # | 主体 | 国别 | Customer Type · Path | Industry | BDD Opportunity | Demand | Sales Conclusion |
|---|---|---|---|---|---|---|---|
| 1 | Chemstock | 阿联酋 | 分销代理 · Partner·Distributor | Adjacent (A2) | Medium · Distribution | Unknown | 🟡 建议先验证 |
| 2 | Hikal | 印度 | 终端业主 · End-user | Target (T2+T4) | High · End-user | Potential | 🟢 建议开发 |
| 3 | Aarti Industries | 印度 | 终端业主 · End-user | Target (T4+T3) | High · End-user | Potential | 🟢 建议开发 |
| 4 | Umicore | 比利时 | 终端业主 · End-user | Target (T1+T3) | High · End-user | Potential | 🟢 建议开发 |
| 5 | EnviroChemie | 德国 | EPC · Partner·EPC | Adjacent (A1) | **Medium · EPC+Technology Partner**（Conflict 潜在竞争） | Potential | 🟡 建议先验证（FW=旧口径 Yes；**Gate=Confirmed／外部性减分**） |
| 6 | **Ajay-SQM** | 美国/法国/智利 | 终端业主 · End-user | Target (T4) | **Medium · End-user** | Unknown | 🟡 建议先验证 |
| 7 | **BASF** | 德国 | 终端业主 · End-user | Target (T4+T3) | **High · End-user** | Potential | 🟢 建议开发（FW Rule Patch 后重算） |
| 8 | **GEA Group** | 德国 | EPC · **Partner·EPC** | Adjacent (A1) | **Medium · EPC/Integration +\| Technology Partner**（Conflict 潜在竞争） | Technology Partner**（Conflict 潜在竞争） | 🟡 建议先验证（**Gate=Unverified**） | 🟢 建议开发（FW Rule Patch 后重算） |
| 9 | **Trinseo**（Negative Control） | 美国/爱尔兰 | 终端业主 · End-user | Target (T4+T3) | High · End-user | Potential | 🟡 建议先验证（**FW=Yes 真实财务困境**） |
| 10 | **CABB Group** | 德国 | 终端业主 · End-user | Target (T4+T3) | High · End-user | **High · End-user**（Gate=Strong） | 🟢 建议开发（**FW=Unknown 私营 / BCS=Yes**） |
| 11 | **Festo** | 德国 | 终端业主 · End-user | **Unknown（T3 门槛未过）** | **Unknown · End-user** | Potential | 🟡 建议先验证（Gate=Weak） |
| 12 | **Automotive Cells Company（ACC）** | 法国 | 终端业主 · End-user | **Target (T1 锂电池)** | **Medium · End-user**（Gate=Moderate） | Potential | 🟡 建议先验证（Gate=Moderate） |
| 13 | **Veolia Water Technologies** | 法国 | 环保工程公司（EPC）· **Partner·EPC** | 🔵 Adjacent (A1) | 🟡 **Medium · EPC / Integration +\| Technology Partner**（🔴 Conflict · 直接技术路线重叠） | Technology Partner**（🔴 **Conflict: 潜在竞争 · 直接技术路线重叠**） | 🟡 建议先验证（**Gate=Supported**） | 🟢 建议开发（**FW=No**） |

> **2026-09-27 · BDD-Specific Relevance Gate Patch 后的三例复核**：
> ① **CABB**（Positive Control）：`Industry Match` 保持 `Target`（T4 命中；T3 亦过新证据门槛），**Gate = `Strong`**（Pratteln 已在用 UV-AOP + 难生物降解 / 常规处理受限 + 精细化工多步合成），`BDD Opportunity` **保持 `High`** —— **自然保持，非人工锁定**。
> ② **Festo**：T3 新证据门槛**未过**（只有阳极氧化 / 机加工 / 压铸废水）→ `Industry Match = Unknown` → `BDD Relevance = Unknown`（Gate = `Weak`）→ 结论降为 `建议先验证`。
> ③ **ACC**：`Industry Match` 保持 `Target`（T1 不受 Patch A 影响），但 **Gate = `Moderate`**（富溶剂工艺 + 电池废水证据充分，**未见高 COD / 难降解 / AOP / 常规处理受限**）→ `BDD Opportunity` 由 `High` 降为 `Medium` → 结论降为 `建议先验证`。

**第 6 家（Ajay-SQM，2026-09-27）关键特征**：首家**制造业活动确认 + 三个化工厂区 + ISO 14001 体系齐全，但因输入 6（PWE/CSD）不成立而判 Medium** 的主体。碘衍生物/特种化学品制造商（Ajay Chemicals + SQM 合资）。Current Treatment 判 `Partial`（仅法国 Évron 厂公开披露"从料流中回收碘的专用单元"，且未确认是否用于废水）。Priority Site = Évron（权重 3 命中）。

**第 7 家（BASF，2026-09-27）关键特征**：首个**大规模跨国主体**案例。234 个生产基地、7 个 Verbund 基地。Current Treatment 判 `Confirmed`（Ludwigshafen 中央机械-生物废水处理厂，1974 投运，官网称欧洲最大机械-生物 / 世界最大工业污水处理厂之一，年处理约 9,000 万 m³ 生产废水 + 2,000 万 m³ 市政污水）。PWE 为官网环境披露级（含年报按 200+ 基地合并排放数据 + 州环境部每年 10-12 次不定期取样）→ Demand Status = `Potential`。**FW = Yes 首次由"裁员/重组公告"判据触发而非连续亏损**（集团 2023-2025 连续盈利，但 2024-01~2026-06 裁员约 7,000 人、CoreShift 计划、多套装置关闭）→ Sales Conclusion = 建议先验证。Contact 为**首个官网来源具名 EHS 高管**（Dr. Katja Scharpwinkel，执行董事会成员兼 Ludwigshafen 基地厂长，分管 Corporate EHSQ）。

**第 8 家（GEA Group，2026-09-27）关键特征**：首个**渠道/技术伙伴型**主体，也是首个**需标注双重身份**的案例。GEA 是工业废水处理设备与 **ZLD 整线**供应商（自有离心分离/错流膜过滤/蒸发/结晶/干燥全系列），按 `customer-type-playbook.md` **判定优先级①命中**（业务含"水处理设备"）→ `Partner·EPC`；虽有多个自有制造基地（Oelde 1,900 人），依"① 优先于 ④"仍走 Partner Path，双重身份已在 Company Profile 注明。Current Treatment = `Confirmed`（Partner 口径：可提供的技术组合）。**Conflict 标注为"应用场景重叠 / 技术路线不重叠"**——已检索确认其技术组合不含电化学氧化，与 EnviroChemie 的"同类 AOP 直接替代"性质不同。Priority Site = Oelde（全球最大生产基地 + 分离技术中心）。**FW = Yes 连续第 2 次由组织架构重组公告触发**（2025-10-07 公告：执行董事会 3→6 席、解散 14 人全球执委会、撤销 COO 领域），而集团同年营收利润双增、股息提高、进入 DAX。

**第 9 家（Trinseo，2026-09-27 · Negative Control）**：FW Rule Patch 的反证案例。2026-05-26 申请 Chapter 11 + ASC 205-40 持续经营重大疑虑 + 债务违约与跨违约 + 流动性危机 + S&P 降至 'D' + NYSE 摘牌 → **FW = Yes**（命中白名单 5 项）；A/B 对照（仅翻转 FW）结论由 `建议先验证` 变 `建议开发`，证明该字段修复后仍起作用。

**第 10 家（CABB Group，2026-09-27）**：FW Rule Patch 后首个常规目标客户。精细化学品 CDMO（农化 / 医药中间体 + 全球高纯 MCA 主要生产商），Permira 全资持股，5 个制造厂区（CH / DE×2 / FI / CN）。**关键特征**：Pratteln（瑞士）厂区**已于 2019 年投运紫外高级氧化（UV-AOP）废水预处理装置、2021 年提能**（来源：CABB 提交 UNGC 的 CR 报告）—— **目标主体本身已是 AOP 使用者**，技术素养极高，与 BDD（电化学氧化，同属 AOP 家族）场景同源；双重重要性分析将「水资源消耗与资源稀缺（ESRS E3）」列为最重大议题之一。**FW = Unknown**（私营无公开财务报表，按 6.1 处理，不降档）；**Business Change Signal = Yes**（2026-02 完成出售美国 Galena 厂区、战略转向 Pharma 与 Life Science、厂区 6→5）；Current Treatment = `部分确认 Partial`（仅 Pratteln 有厂区级自有设施披露）；Priority Site = **Pratteln**。**园区级 ≠ 厂区级**：Knapsack（Chemiepark Knapsack，YNCORIS 两套集中污水厂）与 Gersthofen（MVV Industriepark）的废水由园区运营方处理，附录 B 已显式声明不得写成 CABB 自有设施。

**第 11 家（Festo，2026-09-27）**：**首个「非流程工业」主体**（工业自动化设备制造商，14 个全球生产中心）。Industry Fit 判 `Target` **完全依赖 T3 高 COD / 难降解性质口径** —— 济南厂**阳极氧化线**（属表面处理 / 电镀族）+ 铝压铸 + 机加工。**PWE 强度罕见**：官网可持续报告按财年公布生产废水量（73,737 → 80,336 → 82,185 m³，三年连升），并明确「生产废水排放前按工艺特定污染物处理、处理设施持照并监测污染物参数、除未受污染雨水外不向自然水体或地下水排放」。**Priority Site = Krishnagiri（印度）** —— 首次由**权重 2（新增产能项目：2025 年新建投产、二期已预留土地）**定胜负，而非权重 3（工艺涉水密度，Jinan 备选）。**FW = Unknown**（家族全资非上市）；**Business Change Signal = Yes**（印度 / 土耳其 / 墨西哥新增产能 + local for local + 班加罗尔 GCC）。

**第 12 家（Automotive Cells Company · ACC，2026-09-27）**：**首个 T1 锂电池主体**（Stellantis 45% / Mercedes-Benz 30% / TotalEnergies 25% 合资，AUTOMOTIVE CELLS COMPANY SE，RCS Nanterre 884 638 586，注册资本 €74M）。Industry Match 判 `Target` 由 **T1 直接命中**（登记经营范围含 "Manufacture of batteries and accumulators"），**不依赖 T3 性质口径**。**PWE 质量高且颗粒度细**（CSR Report 2024）：废水去向往 **园区集中污水厂 SIZIAF**、含危险物质废水**作危废外送**、**「不存在与工艺相关的工业水向水网排放」**、NMP 厂内冷凝回收 + 法国服务商再生、含 NMP 液体废液外送持证机构、5 口地下水监测井、ICPE + **上层 SEVESO**、**2023 年运营许可申请**；2024 工业用水 119,747 m³（环评预测 53%）、未直接抽取地下水。**关键窗口信号**：已公开立项 2025 年水回用可研（**purge 类废水回注工艺 + 雨水回用**）+ Block 2 在建 → Priority Site = **Billy-Berclau / Douvrin**。**FW = Unknown（白名单第 3 例、首个判 Unknown 的案例）**：尽管存在股东担保贷款 €845M、中止德意项目债务融资、CEO 公开称爬坡「削弱了公司的财务状况」、报废率 15-20%，但 6.1 八类白名单**全部无证据**且主体未上市无公开报表 → Unknown 不降档；**BCS = Yes**（德意两厂搁置 + CEO 更替 + 转 LFP + 客户集中于 Stellantis）。**同名主体排除新类型**："ACC" 缩写命中 **ACC Limited（印度水泥 · Adani 体系）** 的 BRSR/ESG 报告，已全部排除。
> **方法论新增**：无文本层的 PDF（本 CSR 报告）→ 用「zlib 解压 FlateDecode + 提取 `(...)` 文本串 + **去空格归一化**」自建提取器后再检索；直接对原文 grep 会因 PDF 字母间插空格而 0 命中。

> **2026-09-27 · Partner Cooperation Evidence Gate Patch 后的 Partner 档位重算**：
> ① **Veolia**（`Supported` + Conflict）· ② **GEA**（`Unverified`）· ③ **EnviroChemie**（`Confirmed`，但机制外部性为集团内 → 减分）—— **三家 BDD Opportunity 同时由 `High` 落为 `Medium`**；Sales Conclusion 两家由「建议开发」落为「建议先验证」（EnviroChemie 维持）。
> 原因：原 Partner `High` 四条件对任何大型水处理 EPC 都会自动成立。**能力 / 场景 ≠ 合作机会。**
> **Negative Control = De Nora**（Capability 与 Scenario Overlap 均极高，但自有 DSA® 电极平台封闭、无开放证据）→ 门控 `Conflict` → 不得 `High`。
> **EnviroChemie 是三家唯一有 BDD 域内外部技术集成证据者**（up2e! 的 Roturi® 臭氧装置被集成进其 Envochem AOP 装置），但**未被人工锁 High**。

**第 13 家（Veolia Water Technologies，2026-09-27）**：**首个大规模 Partner Path 主体，也是迄今最强的竞争重叠案例**。法国政府企业目录核实：VEOLIA WATER TECH（VWT），SIREN 414986216，Saint-Maurice（法国）SAS，规模类别 GE，主营 64.20Z（控股）。客户类型 = 环保工程公司（EPC）· **Partner·EPC**（判定优先级 ① 命中；副类型 Technology Partner）。**Partner 四项判据全部成立 → High**：① Adjacent ✔ ② 自有臭氧 / 紫外 / 完整 AOP 产品线（40+ 年）+ EPC 能力 + 板块 38 技术站点 / 11 研发实验室 ✔ ③ 技术组合与 BDD 场景公开可证重叠（AOP 生成羟基自由基「完全矿化为 CO₂ 与水」，目标污染物含 1,4-二噁烷 / NDMA / 药物残留 / 激素）✔ ④ ≥2 渠道项目证据（**2026 年微电子水处理订单 €343M** 含废水回用至 ZLD、新加坡 NEA 首个 PFAS 许可、收购澳洲 Enviropacific、巴西 Sabesp 升级）✔。**🔴 Conflict 升级为「直接技术路线重叠」**：其**官方博客明载**工业端（航空 / 化工高浓度场景）部署**电化学氧化** —— 比 GEA（仅场景重叠）与 EnviroChemie（AOP 同族）都更近。**检索教训：技术路线重叠常先出现在官方博客 / 国别站点，而非主站产品页**（主站只见 O₃/UV/H₂O₂ 组合）。Priority Site = **Dübendorf（瑞士，臭氧/UV/AOP 开发与制造中心）**；Current Treatment = Confirmed（Partner 口径）；**FW = 🟢 No**（集团 2025 营收 €44.4bn、EBITDA €7.05bn 创纪录、净利 +10.9%、杠杆 2.79x、上调指引）；**BCS = Yes**（WTS 30% 少数股权 $1.75bn 全资化 + 组织整合 + 收购 Enviropacific + IFAT 新品）。**层级纪律重点**：近 12 个月集团环境执法（澳 NSW 罚单 A$48,000、清理令、维州 A$100 万）**全部在废物板块澳洲填埋场站点**，不得写成 VWT 记录。来源冲突 8 处（含收入三层口径：品牌 €1.65B / 分部 €4,954M / 法国法人 €1,737.8M 且净利 €0）。

---

## 六、GitHub 仓库与跨机复现（2026-09-27 建立）

**仓库**：`D:/Case Flow` 已 `git init`（分支 `main`），**Private 私有**，全量备份。

**★ 核心结构约定**：Skill 有两份，职责不同——`skill/bdd-inquiry-analyzer/`（仓库内，受 Git 管理，**正本**）与 `~/.workbuddy/skills/bdd-inquiry-analyzer/`（**运行副本**）。
**WorkBuddy 只读后者，不读项目目录** → **凡 `git pull` 或改动 Skill，必须重跑 `tools/restore-skill.ps1` 才会生效**。这是最容易踩的坑。

**`tools/` 三脚本（本仓库专用，勿删）**
| 脚本 | 方向 | 特性 |
|---|---|---|
| `restore-skill.ps1` | 仓库 → 本机 | 自动备份旧版 + MD5 逐文件校验 |
| `sync-skill.ps1` | 本机 → 仓库 | NEW/MODIFIED/DELETED 差异清单 + 校验 |
| `verify-project.ps1` | 只读体检 | 10 项检查，PASS/WARN/FAIL 汇总 + 退出码 |

**踩过的坑（勿重犯）**
- `.gitattributes` **有意不设 `eol` 强制**：本仓库全 Windows 使用，保持原始 CRLF 字节，仓库副本与本机副本 MD5 才一致；一旦 Git 改写换行符，`sync-skill.ps1` 会全部误报 MODIFIED。PDF/PNG/Office 一律标 `binary`。
- `.gitignore` 只排系统垃圾与密钥类；`.workbuddy/*` 排除但**保留 `memory/`**（项目记忆要一起备份）。
- 本地仓库配置：`core.quotepath=false`（中文文件名可读）· `core.autocrlf=false` · `core.longpaths=true`。
- 校验基线：**229 文件** · Skill **15/15 md5 MATCH** · 体检 **PASS=10 / WARN=2 / FAIL=0** · 总量 16MB。

**保密纪律**：客户情报卡含客户名 / 厂区 / 联系人岗位 / 商业判断，属公司业务资料 → **仓库必须保持 Private**，`origin` 永不指向公开地址（Git 历史一旦被抓取无法收回）。公司设备政策若禁止同步到个人账号，改用 `git bundle` 离线打包或公司内网托管。

### 双仓库结构（2026-09-27 建立 · 长期约束）

| 仓库 | 可见性 | 内容 | 位置 |
|---|---|---|---|
| `case-flow-bdd` | **Private** | 全量开发备份：Skill 本体 + 客户情报卡 + 归档 + Patch 报告 + 项目记忆 | `D:/Case Flow/` |
| `bdd-customer-intelligence-skill` | **Public** | 分发版：**只含脱敏后的 Skill 本体 + README + LICENSE + .gitignore（18 文件）** | `D:/bdd-customer-intelligence-skill/` |

**★ 两者的内容已分叉，不得互相回灌；每次发版需重新脱敏。**

**Public 版脱敏原则（必须遵守）**：只把「具体主体」换成「类型化描述」或占位符，**绝不动判定逻辑 / 阈值 / 字段定义 / 规则结构**。
具体对照：公司名 → `Sample Chemicals` 或类型名（如 `多厂区电池材料制造集团型主体`、`EPC 兼自有工艺线型主体`）；人名 → `<岗位名称>`；厂区 → `<厂区名>`；私有路径 → `内部工作区归档区（不随本分发版发布）`。

**公开前必查 8 项**：客户名 · 真实厂区 · 真人姓名 · 邮箱 · 密钥凭据 · 私有工作区路径 · 归档目录引用 · 客户数据类数字（N 座 ZLD / €金额 / 万 m³）。**基线：全部 0 命中**。

**工具环境观察**：本机 PowerShell 工具**不回传 `Write-Host`/`Write-Output`**，须**写文件 + Read** 才能取到输出；Bash 直接调 `powershell.exe` 会被安全策略拒绝。

---

*最后更新：2026-09-27（含 FW Rule Patch + BDD-Specific Relevance Gate Patch + Delivery Scope Rule + Partner Cooperation Evidence Gate Patch；实跑至 13 家；新增 GitHub 私有仓库与跨机复现方案）*
