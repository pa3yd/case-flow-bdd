# 【归档】Technical Fit 判定规则

> 来源：`references/bdd-fit-rules.md` 第二 / 三 / 四部分（V1.0 冻结前）
> 归档原因：**C / B 类**——Technical Fit 判定阈值属于工程计算基础，超出「BDD 客户完整企业背调 + 客户开发判断」范围
> 回收条件：Boromond 技术确认各参数适用范围阈值与否决条件后，于平台 L3 计算层回收
> 归档日期：2026-09-26

---

## 第二部分 · Technical Fit 规则（原文）

**回答的问题**：现有技术数据是否足够判断 BDD 技术适用性？
**数据要求**：**必须真实水质数据。** 无数据直接输出 `Insufficient Data`。

### 取值定义

| 取值 | 触发条件 |
|---|---|
| `Insufficient Data` | 缺少任一必需技术参数 |
| `Sufficient — Likely Suitable` | 数据齐全 且 全部落在适用范围内 且 未触发否决条件 |
| `Sufficient — Likely Unsuitable` | 数据齐全 但触发任一否决条件 |
| `Engineer Review Required` | 数据齐全，但落在规则未覆盖的区间 |

### 必需技术参数（缺任一 → `Insufficient Data`）

| # | 参数 | 权重 |
|---|---|---|
| ① | 进水 COD（或目标特征污染物浓度） | 必需 |
| ② | 特征污染物类型 | 必需 |
| ③ | 盐度 / 氯离子含量 | 必需 |
| ④ | 处理水量 m³/d | 必需 |
| ⑤ | 目标限值 / 执行标准 | 必需 |

> 是否还有其他必需参数？是否有可不提供的参数？

### 适用范围阈值

> 由 Boromond 技术确认。填写前所有参数一律视为"未覆盖"，输出 `Engineer Review Required`。
> **禁止填写未经工程师确认的经验值。**

| 参数 | 适用区间 | 否决阈值 | 备注 |
|---|---|---|---|
| COD 浓度 | 待填 | 待填 | |
| 盐度 / 氯离子 | 待填 | 待填 | |
| 水量 | 待填 | 待填 | |
| pH | 待填 | 待填 | |
| 悬浮物 / SS | 待填 | 待填 | |
| 含氟情况 | 待填 | 待填 | |
| 温度 | 待填 | 待填 | |

### 否决条件

> 由 Boromond 技术确认。以下为**待确认的候选方向**，非结论。

| 候选否决方向 | 是否成立 | 阈值 | 说明 |
|---|---|---|---|
| 低浓度 + 大水量（电耗不经济） | 待填 | 待填 | 需明确 COD 与水量双阈值 |
| 高悬浮物 / 含油未预处理 | 待填 | 待填 | 需明确干扰机制与前置要求 |
| 含氟废水 | 待填 | 待填 | 需明确对电极寿命的影响程度 |
| 其他 | 待填 | 待填 | |

### 硬规则

- **`Insufficient Data` 时禁止用行业经验值代替。** 不得写"该行业通常 COD 约 X"。
- 数据不足时**禁止输出任何工艺参数**（电流密度、停留时间、能耗、电极面积）。
- `Sufficient — Likely Suitable` 是**趋势判断，不是技术结论**。不得对外表述为"可处理"。
- 所有需要实际处理效果的场景，一律指向小试。
- Technical Fit 高**不得**推导出可输出技术方案。

### 待确认问题

- [ ] 是否需要区分"主氧化"与"深度处理"两种适用场景，并分别定义阈值？
- [ ] `Engineer Review Required` 的默认升级人是谁？
- [ ] 小试结果的回溯是否应反过来修正本文件的阈值？

---

## 第三部分 · 判定流程（原文）

```
1. 收集必需参数 ① ~ ⑤
        │
        ├─ 有缺失？ ── 是 ─→ Insufficient Data
        │                        →（串联）Quotation Readiness = Need technical data
        ▼否
2. 逐项对照「否决条件」
        │
        ├─ 触发任一 ─→ Sufficient — Likely Unsuitable
        ▼未触发
3. 逐项对照「适用范围阈值」
        │
        ├─ 全部在区间内 ─→ Sufficient — Likely Suitable
        ├─ 有项落在区间外但未触发否决 ─→ Engineer Review Required
        └─ 规则未覆盖该参数 ─→ Engineer Review Required
```

---

## 第四部分 · 待校准项汇总（原文）

| # | 待填内容 | 归属 | 阻塞影响 |
|---|---|---|---|
| 1 | 必需参数清单是否增删 | 技术 | Technical Fit 判定准确性 |
| 2 | 适用范围阈值（7 项参数） | 技术 | 全部输出 `Engineer Review Required` |
| 3 | 否决条件与阈值 | 技术 | 无法识别不适合的水质 |
| 4 | 主氧化 / 深度处理是否分开定义 | 技术 | 判定粒度 |
| 5 | `Engineer Review Required` 的升级路径 | 技术 | 流程落地 |

**在以上项全部确认前，Technical Fit 实质上只会输出 `Insufficient Data` 或 `Engineer Review Required`——这是设计上的保守选择，不是缺陷。**

---

## 冻结时的连锁影响记录

Technical Fit 从 Skill 移出后，以下位置同步失效，已一并归档：

| 位置 | 内容 | 处置 |
|---|---|---|
| `reply-playbook.md` L151-165 | 场景 H「敢劝退」（触发条件 = Technical Fit = Likely Unsuitable） | 随 reply-playbook 整体归档 |
| `customer-type-playbook.md` 报价路径行 | 引用 Quotation Readiness | 随策略列归档 |
| `SKILL.md` 硬规则 4 | TF → QR 串联规则 | 已删除 |
| `SKILL.md` 硬规则 10 | Quotation Readiness 不输出金额 | 已删除 |
| `output-card-template.md` 主卡 | Technical Fit / Quotation Readiness 两行 | 已删除 |

**"数据充分性检查"逻辑保留**：判断"客户是否已提供关键技术参数"的能力未丢失，已迁移至 `SKILL.md` 第 8 步 Missing Critical Data（该判断属客户开发范畴——"该向客户要什么"）。
