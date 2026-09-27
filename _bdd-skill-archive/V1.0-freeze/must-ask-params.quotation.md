# 【归档】Quotation Readiness 门槛与报价流程归属

> 来源：`references/must-ask-params.md` 第一节（部分）+ 第五节（V1.0 冻结前）
> 归档原因：**B / C 类**——Quotation Readiness 属报价流程，超出「BDD 客户完整企业背调 + 客户开发判断」范围
> 回收条件：Skill 职责扩展至商务流程，或平台接入商务系统时
> 归档日期：2026-09-26

---

## 第一节 · Quotation Readiness 门槛（原文）

### 输出只有四个状态，**不输出任何金额**

| 状态 | 触发条件 |
|---|---|
| `Ready for quotation` | 5 项关键参数齐 **且** 资料边界已确认 |
| `Not ready` | 缺商务条件（需求量、交付节奏、采购时间表） |
| `Need technical data` | **Technical Fit = Insufficient Data 且缺关键技术参数（自动串联）** |
| `Engineer review` | 涉及技术判定，需工程师确认 |

### 必须齐备的 5 项

| # | 参数 | 为什么必须有 |
|---|---|---|
| ① | 水质类型（行业 / 特征污染物） | 决定工艺路线方向 |
| ② | 进水 COD（或目标污染物浓度） | 决定污染负荷 |
| ③ | 处理水量 m³/d | 决定设备规模量级 |
| ④ | 目标限值或执行标准 | 决定处理深度要求 |
| ⑤ | 盐度 / 氯离子含量 | 影响电极选型与副产物风险 |

> **注**：这 5 项参数在 V1 冻结后**仍然保留**，但其角色从"报价门槛"改为"Missing Critical Data 的生成依据"——即从"能不能报价"改为"该向客户要什么"。见 `references/must-ask-params.md`。

### 串联规则（冻结时已删除）

```
Technical Fit = Insufficient Data
        且
缺少 ①~⑤ 中任一关键技术参数
              ↓
   Quotation Readiness = Need technical data
```

**此规则随 Technical Fit 一并归档。** 新链中不存在 Quotation Readiness 环节。

### 人工覆盖（Manual Override）

允许人工规则覆盖，用于「标准产品可直接报价」等特殊场景。

**格式**：
```
Quotation Readiness: Ready for quotation（Manual override：标准品现货，规格已确认）
```

**要求**：
- 必须标注 `Manual override`
- 必须附**覆盖理由**与**依据**
- 未标注的覆盖视为无效

> 金额一律由商务系统 / 报价单承载，Skill 不承载任何价格数据。

### 客户催促时的标准回应

> "为准确核算设备规模与运行成本，需要先确认 **[X]、[Y]、[Z]** 三项。这几个参数直接决定电耗和设备配置，若按估算值报价，后续可能出现较大偏差，对双方都不利。您提供后我们给出准确方案。"

**核心逻辑**：不是"我不肯报价"，而是"我要给你准确的价"。

### 待校准项（归档）

- [ ] 5 项关键参数是否需要增删？
- [ ] 哪些**标准品**可适用 `Manual override` 直接报价？
- [ ] `Not ready` 与 `Engineer review` 的实际区分场景？
- [ ] 检测报告时效窗口（现设 6 个月）是否合适？

---

## 第五节 · 报价流程归属说明（原文，C 类）

**Skill 只回答"该不该进报价流程"，不回答"报多少"。**

| 事项 | 归属 |
|---|---|
| 判断是否具备报价条件 | Skill（输出四态之一） |
| 判断缺哪些参数 | Skill（Missing Critical Data） |
| 具体价格、区间、阶梯价、折扣 | ❌ 商务系统 / 报价单 |
| 成本构成、底价 | ❌ 商务系统 |

**为什么**：价格时效敏感（写死在规则文件里，调价后即失效且无人维护），且属商务决策，不该由检索型工具承担。

> **冻结后变化**：整个"报价条件判断"环节从 Skill 移出。Skill 只输出 `Missing Critical Data`（该问什么），不再输出任何报价状态。报价判断由人工 / 商务系统承担。

---

## 冻结时同步失效的位置

| 位置 | 内容 | 处置 |
|---|---|---|
| `customer-type-playbook.md` 报价路径行（6 处） | 引用 Quotation Readiness 状态 | 随策略列归档 |
| `SKILL.md` 旧第 7 步 Quotation Readiness | 整个步骤 | 已删除 |
| `SKILL.md` 硬规则 10 | 只输出状态不输出金额 | 已删除 |
| `output-card-template.md` 主卡 Quotation Readiness 行 | — | 已删除 |
| `校准清单与回测方案.md` A 段 | Quotation Readiness 商务口径 | 已移出 |
