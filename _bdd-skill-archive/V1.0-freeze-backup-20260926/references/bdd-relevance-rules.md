# BDD Relevance 判定规则

**回答的问题**：这家公司**自身**是否存在 BDD 可切入的应用场景？

**不是**行业属不属于目标市场（那是 `bdd-fit-rules.md` 的 Industry Fit）。

> ⚠️ **本文件的核心作用：阻断"行业对口 → BDD 相关性高"的错误推导。**
> 这是本 Skill 最容易失真的判定点。

---

## 一、8 项输入

**BDD Relevance 必须综合以下 8 类输入，不得只依赖 Industry Fit。**

| # | 输入 | 从哪来 | 必填性 |
|---|---|---|---|
| 1 | **Industry** 行业 | 询盘自述 / 工商经营范围 | 必须 |
| 2 | **Company Business** 公司业务 | 工商信息 / 官网 | 必须 |
| 3 | **Products** 产品 | 官网 / 产品目录 / 电商店铺 | 必须 |
| 4 | **Manufacturing Activity** 制造业活动 | 厂址 / 参保人数 / 设备招标 / 招聘 | **关键项** |
| 5 | **Manufacturing Process** 制造工艺 | 仅**公开可验证时**使用 | 可选 |
| 6 | **Wastewater Signals** 废水信号 | 询盘文字 → `wastewater-signal-map.md` | 必须 |
| 7 | **Environmental Evidence** 环境证据 | 处罚 / 排污许可 / 环评 → `lead-signals.md` | 强烈建议 |
| 8 | **Project / EIA / Permit / Tender / ESG / Job signals**<br>项目 / 环评 / 许可证 / 招标 / ESG / 就业信号 | 公开检索 → `lead-signals.md` | 强烈建议 |

### 各输入的判读逻辑

| 输入 | 说明什么 | 典型证据 |
|---|---|---|
| Industry 行业 | 是否在 BDD 涉水行业范围内 | 客户自述、经营范围 |
| Company Business 公司业务 | 主营业务是否涉及生产制造 | 工商经营范围、官网"关于我们" |
| Products 产品 | 产品是否需要在生产过程中用水/产生废水 | 产品目录、生产工艺描述 |
| **Manufacturing Activity 制造业活动** | **是否真的在"造东西"** | 厂址、参保人数（> 200 人）、生产设备招标、车间岗位招聘 |
| Manufacturing Process 制造工艺 | 工艺中是否有产污环节 | **仅采信环评文件 / 官方公示载明的工艺段** |
| Wastewater Signals 废水信号 | 客户描述中是否出现废水概念 | "我们的废水""污水站""出水 COD" |
| Environmental Evidence 环境证据 | 是否存在政府层面的环境监管痕迹 | 处罚记录、排污许可证、环评公示 |
| Project / EIA / Permit / Tender / ESG / Job signals | 是否有项目在推进 | 环评公示、招投标、ESG 报告、环保岗位招聘 |

---

## 二、取值定义

| 取值 | 判据（需同时满足） |
|---|---|
| `High` | ① 行业在目标市场 **且** ② 已确认制造业活动 **且** ③ 有明确废水信号 **且** ④ 至少有 1 项环境证据或项目信号支撑 |
| `Medium` | 行业对口 + 有部分信号（如仅制造业活动，或仅废水信号），但**环境证据缺失** |
| `Low` | 行业对口但**明确不存在** BDD 可切入场景 |
| `Unknown` | 关键输入不足，无法判断 |

### `Low` 的典型情形

- 纯贸易型 / 纯代理型公司，不自行生产
- 纯研发机构无中试环节
- 废水已委托第三方处理，且无任何改造迹象
- 已确认使用其他技术路线且项目已建成（无 BDD 切入窗口）

### `Unknown` 的典型情形（**信息少时就用这个**）

- 主体未核实（`Unverified`），无法判断业务实质
- 查不到业务与产品信息
- 无废水信号且无环境证据，且无法判断是否有生产活动
- 重名企业无法区分

---

## 三、判定流程

```
1. 输入 1~3（Industry / Business / Products）
        │
        ├─ 均无法获取？ ── 是 ─→ Unknown
        ▼否
2. 输入 4（Manufacturing Activity 制造业活动）
        │
        ├─ 无证据表明有生产活动？ ── 是 ─→ 最高只能 Medium
        ▼确认有
3. 输入 6（Wastewater Signals 废水信号）
        │
        ├─ 无废水信号？ ── 是 ─→ 最高只能 Medium
        ▼有
4. 输入 5（Manufacturing Process，仅公开可验证时）
        │
        ├─ 公开来源载明产污工艺 ─→ 作为强化证据
        └─ 无公开来源 ─→ 跳过，不得推断
        ▼
5. 输入 7 / 8（Environmental Evidence / Project signals）
        │
        ├─ 至少 1 项 ─→ High（若 ②③ 均满足）
        └─ 均无 ─→ Medium
```

**封顶规则速记**

| 缺失项 | 封顶 |
|---|---|
| 无制造业活动证据 | `Medium` |
| 无废水信号 | `Medium` |
| 无环境证据 + 无项目信号 | `Medium` |
| 主体未核实 | `Unknown` |

---

## 四、强制附注

**每次输出 BDD Relevance 都必须附三项：**

```
Reason       判定理由（为什么是这个等级）
Evidence     支撑证据（编号指向附录 A，如 E1 / E4 / E7）
Confidence   High / Medium / Low
```

**缺任一字段 → 判定无效。**

| 附注字段 | 写法要求 |
|---|---|
| `Reason` | 说明**已确认什么 / 缺什么**，不得只写"行业对口" |
| `Evidence` | 引用附录 A 的编号；无证据支撑时写 `无`，不得留空 |
| `Confidence` | 官方来源 + 多源互证 = High；单一可信来源 = Medium；聚合站/B2B 平台 = Low |

---

## 五、常见错误对照（必读）

| # | 错误写法 | 问题 | 正确写法 |
|---|---|---|---|
| 1 | `Industry Fit = Target` → `BDD Relevance = High` | **本 V1 明令禁止**——Industry Fit 只是 8 项之一 | 逐项对照 8 输入。若仅行业对口 → 最高 `Medium`，常为 `Unknown` |
| 2 | 某 API 企业行业对口 → 直接给 `High` | 未确认是否有生产活动、废水、环境证据 | `Medium` 或 `Unknown`。`Reason` 写明"行业对口，但未确认生产活动与废水" |
| 3 | 写"该行业通常产生高浓度废水" → 给 `High` | 用行业经验值替代企业事实 | `Unknown`，或补证据后定级 |
| 4 | 采信非公开来源推断制造工艺 | 工艺属企业信息，公开源才有证据价值 | 仅采信环评/公示载明的工艺段，否则跳过该输入 |
| 5 | 因客户说"我们要改污水站" → 给 `High` | 客户口述是 FACT，但需 ①~④ 同时满足 | 客户口述 → 满足 ③ 废水信号；环境证据仍缺 → `Medium` |
| 6 | 缺 `Reason` / `Evidence` / `Confidence` | 判定无效 | 三项必填 |
| 7 | 该字段留空 | 破坏主卡完整性 | 无法判断时也须输出 `Unknown` |

### 必读示例 · API 原料药企业

```
输入 1 Industry            → 医药原料药，属涉水行业           ✅
输入 2 Company Business    → 经营范围含"原料药制造"           ✅
输入 3 Products            → 官网列有 3 个原料药品种          ✅
输入 4 Manufacturing Act.  → ❌ 未查到厂址、参保人数、设备招标
输入 5 Manufacturing Proc. → 无公开来源，跳过
输入 6 Wastewater Signals  → 询盘未提及废水，只问"有没有相关设备"
输入 7 Environmental Evid. → ❌ 未查到处罚、排污许可、环评
输入 8 Project signals     → ❌ 未查到

判定：BDD Relevance = Unknown
Reason: 行业属涉水范围，但未确认制造业活动，客户未提及废水，且无环境证据与项目信号
Evidence: E1（经营范围）、E3（官网产品页）
Confidence: Low
```

> **这份输出的价值**：它直接告诉销售"**需要先确认这家是否真的在生产**"——这正是 BDD Relevance 该承担的工作。若误给 `High`，销售会按"优质线索"投入技术资源，结果发现是纯贸易型公司。

---

## 六、与 Industry Fit 的关系（一张表说清）

| | Industry Fit | BDD Relevance |
|---|---|---|
| 层级 | **行业级** | **公司级** |
| 口径 | 商业定位 | 技术场景 |
| 回答 | 这个行业是否属目标市场？ | 这家公司是否有 BDD 可切入场景？ |
| 输入 | 只要行业名称 | 8 项输入 |
| 主体差异 | 同行业所有公司取值相同 | **同行业内每家公司可不同** |
| 可否互相推导 | ❌ 不可 | ❌ 不可 |

> **同行业内取值可变**——这是 BDD Relevance 存在的全部意义。若它能由行业推出，就不需要这个字段。

---

## 七、与其他文件的职责边界

| 文件 | 负责 |
|---|---|
| **本文件** | BDD Relevance 判定（8 项输入 → 四值 + 强制附注） |
| `bdd-fit-rules.md` | Industry Fit 判定（行业 → Target / Adjacent / Outside / Unknown） |
| `wastewater-signal-map.md` | 从询盘文字**识别**废水信号（定性） |
| `lead-signals.md` | 从外部来源**检索**环境证据与项目信号 |
| `evidence-policy.md` | 决定标注 FACT / INFERENCE / UNKNOWN；Demand Evidence 分级 |
| `customer-type-playbook.md` | 客户类型判定 |

**本文件不做技术可行性判断，不输出任何技术参数与数值区间。**

---

## 八、待校准项

| # | 待确认 | 归属 |
|---|---|---|
| 1 | 四值判据（尤其"制造业活动"的确认标准）是否符合实际业务口径？ | 销售 |
| 2 | `Manufacturing Activity` 的判定以什么为准（参保人数阈值？厂址？设备招标？） | 销售 |
| 3 | `Low` 的情形是否需要补充（是否有"已明确使用其他技术路线"仍视为 Low 的例外）？ | 销售 + 技术 |
| 4 | 8 项输入是否需要增删？ | 销售 + 技术 |
| 5 | `Reason` 的写法是否有对内约定格式？ | 销售 |
