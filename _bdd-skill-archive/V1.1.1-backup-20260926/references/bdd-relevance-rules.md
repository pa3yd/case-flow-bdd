# BDD Relevance 判定规则（V1.1）

**回答的问题**：这家公司 / 这个伙伴，是否存在 BDD 可切入的机会？

**不是**行业属不属于目标市场（那是 `bdd-fit-rules.md` 的 Industry Fit）。

> ⚠️ **本文件的核心作用：阻断"行业对口 → BDD 相关性高"的错误推导。**

---

## 一、V1.1 的两处关键修复

### 修复 1 · 废水证据拆成两类（删除封顶规则）

| 证据类 | 来源 | 说明 |
|---|---|---|
| **Public Wastewater Evidence（PWE）**<br>公开废水证据 | 官网 · 年报 / ESG / BRSR · 政府许可 · 环评 · 合规报告 · 公开案例 · 招聘 | 企业级**公开事实** |
| **Customer-stated Demand（CSD）**<br>客户侧需求陈述 | **询盘文字** · 客户自述 | 客户级**需求陈述** |

> ❌ **已删除规则**：「无询盘废水信号 → BDD Relevance 最高 `Medium`」。
>
> **删除原因**：该规则使「仅凭公司名 + 官网做背调」的场景**从定义上不可能达到 `High`**，即使已掌握官网环境政策、政府合规报告、完整排放数据。
> 在 5 次实跑中连续复现（Hikal / Aarti / Umicore / EnviroChemie 均被封顶 `Medium`）。
>
> **V1.1 规则**：PWE **或** CSD 任一成立即可满足废水证据条件。两者分别记录、分别标注来源。

### 修复 2 · 按 Customer Type 使用不同的内部逻辑

`End-user Path` 与 `Partner Path` **判断对象不同**，不能用同一套判据：

| Path | BDD Relevance 回答的问题 | 主要依据 |
|---|---|---|
| **End-user Path** | 这家企业**是否产生 BDD 可切入的废水**？ | 制造业活动 + PWE（现有设施 / 排放 / 许可）+ 窗口信号 |
| **Partner Path** | 这个伙伴**是否会把 BDD 纳入其交付组合**？ | 能力确认 + 技术组合重叠 + 渠道 / 项目信号 |

> **Partner Path 不得以"它自己产生多少废水"为主要判断依据。**
> 与 EnviroChemie 同类的 EPC / 集成商 / 分销商，其价值在于渠道与交付能力，不在于自身排污。

---

## 二、8 项输入（分 Path 适用）

| # | 输入 | 来源 | End-user | Partner |
|---|---|---|---|---|
| 1 | **Industry** 行业 | 询盘 / 工商 / 官网 | 必须 | 必须 |
| 2 | **Company Business** 公司业务 | 工商 / 官网 | 必须 | 必须 |
| 3 | **Products** 产品 / 服务 | 官网 / 目录 | 必须 | 必须 |
| 4 | **Activity Confirmation** 活动确认<br>（End-user：制造业活动 / Partner：技术·集成·渠道能力） | 厂址 · 规模 · 设备招标 · 招聘 · 案例 · 资质 | **关键项** | **关键项** |
| 5 | **Process / Technology** 工艺或技术组合 | 公开可验证时 | 可选 | **建议** |
| 6 | **Public Wastewater Evidence（PWE）** | 官网 / 政府 / 年报 | **必须之一** | **必须之一** |
| 7 | **Environmental Evidence** 环境证据 | 处罚 / 许可 / 环评 | 强烈建议 | 建议 |
| 8 | **Project / EIA / Tender / ESG / Job signals** | 公开检索 | 强烈建议 | 强烈建议 |

**输入 6 与 7 的区别**：输入 6 描述**设施与排放现状**（有无处理、用什么），输入 7 描述**监管痕迹**（有无处罚 / 许可 / 环评）。

---

## 三、取值定义

### A. End-user Path

| 取值 | 判据（需同时满足） |
|---|---|
| `High` | ① Industry Fit ∈ {Target, Adjacent} **且** ② 制造业活动已确认 **且** ③ PWE **或** CSD 至少一项成立 **且** ④ **≥ 2 项主体级证据**（环境证据 / 项目信号 / 现有处理设施 / 窗口信号） |
| `Medium` | ① 行业对口 **且** ② 制造业活动已确认 **且** ③ 仅 1 项主体级证据，或 PWE / CSD 均缺失 |
| `Low` | 已确证**三项同时成立**：全厂区闭环 + 无扩产/加严/处罚 + 无遗留难降解段；**或** 主体确证为非制造业（纯研发 / 纯持有 / 无任何生产活动） |
| `Unknown` | 关键输入不足（主体未核实 / 无法确认是否有生产活动 / 无任何废水相关信息） |

### B. Partner Path

| 取值 | 判据（需同时满足） |
|---|---|
| `High` | ① Industry Fit ∈ {Target, Adjacent} **且** ② 技术 / 集成 / 分销能力已确认 **且** ③ 其技术组合与 BDD 场景存在**公开可证的重叠** **且** ④ **≥ 2 项渠道 / 项目证据**（公开项目案例 / 采购记录 / 合作方 / 在谈项目清单） |
| `Medium` | ① 行业对口 **且** ② 能力已确认 **且** ③ 重叠度或渠道证据仅 1 项 |
| `Low` | 确证其技术线与 BDD 场景**无任何重叠**，且明确不集成第三方工艺（工艺封闭 + 无渠道） |
| `Unknown` | 能力或技术组合无法确认 |

---

## 四、两条不可越过的红线

### 红线 1 · 行业对口 ≠ BDD Relevance 高

> ❌ `Industry Fit = Target` → **不得**推导 `BDD Relevance = High`。

**示例（必读）**：某 API 原料药企业
- `Industry Fit = Target`（行业属 T2）
- 但**未确认生产活动、无 PWE / CSD、无环境证据**
- → `BDD Relevance = Unknown`（**不得给 High**）

### 红线 2 · 领域吻合 ≠ 自动 High

> ❌ **不得因其行业属 Lithium Battery / Battery Materials 就直接给 `High`。**

**Umicore 型主体（回归测试重点）**：
- 行业属 T1（Battery Materials）→ `Industry Fit = Target`
- **但这不构成 `High` 依据。** 必须逐项核验 ② 制造业活动、③ PWE / CSD、④ 主体级证据。
- 若主体级证据充分（如自有个位数量级厂区、政府合规报告、在建项目）→ `High` 是**由证据支撑**的，`Reason` 必须逐条列出证据编号。
- 若仅有"行业是电池" → 最高 `Medium`。

**强制写法**：给 `High` 时，`Reason` 必须显式写出 ≥ 2 项主体级证据及其编号。缺则视为无效。

---

## 五、强制附注（缺任一 → 判定无效）

```
Reason            判定理由（已确认什么 / 缺什么）
Evidence          支撑证据编号（指向附录 A，如 E4 / E8 / E12）
Confidence        High / Medium / Low
Opportunity Type  End-user / Technology Partner / EPC·Integration / Distribution / Unknown
```

| 附注字段 | 写法要求 |
|---|---|
| `Reason` | 不得只写"行业对口"。必须写明已确认的主体级事实与缺失项；给 `High` 时必须列 ≥ 2 项证据编号 |
| `Evidence` | 引用附录 A 编号；无证据支撑写 `无`，不得留空 |
| `Confidence` | 官方来源 + 多源互证 = High；单一可信来源 = Medium；聚合站 / B2B 平台 = Low |
| `Opportunity Type` | 见 `opportunity-type-rules.md`，五值之一 |

---

## 六、判定流程

```
1. Path 确定？（见 customer-type-playbook.md 分流）
   ├─ Undetermined ─→ BDD Relevance = Unknown（先确认客户类型）
   ▼
2. 输入 1~3 可获取？
   ├─ 否 ─→ Unknown
   ▼是
3. 输入 4（活动 / 能力确认）
   ├─ End-user 无生产活动证据 ─→ 最高 Medium（或 Low，若确证非制造业）
   ├─ Partner 能力无法确认 ────→ 最高 Medium
   ▼
4. 输入 6（PWE 或 CSD）
   ├─ 两者均无 ─→ 最高 Medium        ← 注意：V1.1 起 PWE 单独成立即可
   ▼至少一项
5. 输入 5 / 7 / 8（工艺或技术组合 / 环境证据 / 项目信号）
   ├─ ≥ 2 项主体级证据 ─→ High
   ├─ 仅 1 项 ─────────→ Medium
   ▼
6. 判 Low 前必须核对"降级三条件"（见 current-treatment-rules.md 第四节）
```

**封顶规则速记（V1.1 更新）**

| 缺失项 | 封顶 |
|---|---|
| 无活动 / 能力确认 | `Medium` |
| 无 PWE **且** 无 CSD | `Medium` |
| 主体级证据仅 1 项 | `Medium` |
| 主体未核实 | `Unknown` |
| Path 未定 | `Unknown` |

> ⚠️ **已不存在"无询盘 → 最高 Medium"这条封顶。** `PWE` 单独成立即可支撑 `High`。

---

## 七、常见错误对照（必读）

| # | 错误写法 | 问题 | 正确写法 |
|---|---|---|---|
| 1 | `Industry Fit = Target` → `High` | 禁止推导 | 逐项对照；仅行业对口 → 最高 `Medium` |
| 2 | "它是电池行业" → `High` | **红线 2** | 必须列 ≥ 2 项主体级证据 |
| 3 | 无询盘 → 封顶 `Medium` | **V1.1 已删除** | 有 PWE 即可支持 `High` |
| 4 | 有 ETP / ZLD → `Low` | 已有设施 ≠ 无机会 | 先核对窗口信号与降级三条件 |
| 5 | EPC 型主体按"自身废水"判 | Partner Path 口径错 | 判"是否会纳入交付组合 + 渠道 / 项目证据" |
| 6 | 写"该行业通常产生高浓度废水" → `High` | 行业经验值替代企业事实 | `Unknown`，或补主体级证据 |
| 7 | 采信非公开来源推断工艺 | 工艺属企业信息 | 仅采信公开可验证来源，否则跳过输入 5 |
| 8 | 缺 `Reason` / `Evidence` / `Confidence` / `Opportunity Type` | 判定无效 | 四项必填 |
| 9 | 字段留空 | 破坏主卡完整性 | 无法判断时也要输出 `Unknown` |

---

## 八、与 Industry Fit 的关系

| | Industry Fit | BDD Relevance |
|---|---|---|
| 层级 | **行业级** | **公司 / 伙伴级** |
| 口径 | 商业定位 | 机会场景 |
| 输入 | 只要行业 / 业务属性 | 8 项输入 + Path |
| 主体差异 | 同行业取值相同 | **同行业内每家公司可不同** |
| 可否互相推导 | ❌ | ❌ |

> **同行业内取值可变**——这是 BDD Relevance 存在的全部意义。

---

## 九、与其他文件的职责边界

| 文件 | 负责 |
|---|---|
| **本文件** | BDD Relevance 判定（分 Path 逻辑 → 四值 + 四项附注） |
| `bdd-fit-rules.md` | Industry Fit 判定（含最小目标市场地图） |
| `customer-type-playbook.md` | 客户类型 + Path 分流 |
| `current-treatment-rules.md` | 现有处理方案 / 技术组合的提取与判读 |
| `opportunity-type-rules.md` | Opportunity Type + Priority Site |
| `wastewater-signal-map.md` | 从文字识别 CSD 与特征信号 |
| `lead-signals.md` | 从外部来源检索 PWE 与环境证据 |
| `evidence-policy.md` | 标注 FACT / INFERENCE / UNKNOWN；Demand Status 与 Commercial Risk 定级 |

**本文件不做技术可行性判断，不输出任何技术参数与数值区间。**

---

## 十、待校准项

| # | 待确认 | 归属 |
|---|---|---|
| 1 | `High` 要求"≥ 2 项主体级证据"是否过严 / 过松 | 销售 |
| 2 | `Low` 的"降级三条件"是否符合实际经验 | 销售 + 技术 |
| 3 | Partner Path 的"技术组合重叠"如何界定更可靠 | 技术 |
| 4 | 8 项输入是否需要增删 | 销售 + 技术 |
