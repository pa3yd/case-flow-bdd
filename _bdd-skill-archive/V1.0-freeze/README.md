# BDD Customer Intelligence Skill · V1.0 Freeze 归档区

> 归档日期：2026-09-26
> 触发：V1 Freeze & Scope Check 正式执行
> 归档原则：**不删除有未来价值的内容，统一归档**

---

## 一、为什么归档

V1 冻结后 Skill 唯一职责收窄为：**BDD 客户完整企业背调 + 客户开发判断**。

以下能力被判定为 **B（未来可能使用）** 或 **C（超出当前 Scope）**，从 Skill 中移出，但内容完整保留在此，平台阶段可直接回收。

---

## 二、归档文件清单

| 文件 | 类型 | 原位置 | 归档原因 |
|---|---|---|---|
| `SKILL.pre-freeze.md` | 全量快照 | `SKILL.md` | 冻结前完整版本，供 diff 对照 |
| `evidence-policy.pre-freeze.md` | 全量快照 | `references/evidence-policy.md` | 同上 |
| `output-card-template.pre-freeze.md` | 全量快照 | `assets/output-card-template.md` | 同上 |
| `bdd-fit-rules.pre-freeze.md` | 全量快照 | `references/bdd-fit-rules.md` | 同上 |
| `must-ask-params.pre-freeze.md` | 全量快照 | `references/must-ask-params.md` | 同上 |
| `customer-type-playbook.pre-freeze.md` | 全量快照 | `references/customer-type-playbook.md` | 同上 |
| `reply-playbook.md` | **整体归档** | `references/reply-playbook.md` | C 类占比最高（28%）。承载"执行"而非"判断"：话术模板、分阶段跟进节奏 Day 0~30、报价相关场景 B/F/G |
| `disclosure-policy.md` | **整体归档** | `references/disclosure-policy.md` | 属销售 SOP 非背调：资料开放三档、应对话术、可交换原则。**第二节危险信号已迁移至** `evidence-policy.md` 第五节 |
| `bdd-fit-rules.technical.md` | 拆分归档 | `references/bdd-fit-rules.md` 第二~四部分 | Technical Fit 判定阈值 = 工程计算基础 |
| `must-ask-params.quotation.md` | 拆分归档 | `references/must-ask-params.md` 第一/五节 | Quotation Readiness 门槛 = 报价流程 |
| `customer-type-playbook.strategy-columns.md` | 拆分归档 | `references/customer-type-playbook.md` 策略列 | 决策周期 / 报价路径 / 资料开放 / 价格敏感度 = 销售打法 |
| `output-card-template.appendix-B-C.md` | 拆分归档 | `assets/output-card-template.md` 附录 B/C | 回复草稿 + 推进节奏 |

---

## 三、回收条件（各归档件的重启触发点）

| 归档件 | 回收条件 |
|---|---|
| `bdd-fit-rules.technical.md` | Boromond 技术确认各参数适用范围阈值与否决条件后 → 平台 L3 计算层 |
| `must-ask-params.quotation.md` | Skill 职责扩展至商务流程，或平台接入商务系统时 |
| `disclosure-policy.md` | 需要对外发布"资料开放 SOP"独立文档时 |
| `reply-playbook.md` | 需要独立"回复执行" Skill 时（**建议独立成 Skill，不塞回本 Skill**） |
| `customer-type-playbook.strategy-columns.md` | 平台 L4 推理层需要销售策略输出时 |
| `output-card-template.appendix-B-C.md` | 恢复回复草稿与跟进节奏输出时 |

---

## 四、注意

- 本目录**在 Skill 目录之外**，不会被 Skill 机制加载。
- 本目录内容为**归档**，不参与 V1 运行。修改本目录不影响 Skill 行为。
- Skill 内 `SKILL.md` 第十一节记录了归档指针与回收条件。
