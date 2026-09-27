---
name: bdd-inquiry-analyzer
description: BDD（掺硼金刚石）电极与电化学氧化废水处理业务专用询盘分析与客户背调，服务 Boromond/波乐美业务口径。当用户提供客户询盘、公司名、联系人、名片、邮件或聊天记录，需要判断客户类型、需求证据等级、行业契合度、BDD 机遇、技术匹配度、商业风险、缺失关键数据、报价准备状态、推荐联系角色与下一步行动时使用。也用于：Boromond 询盘分析、BDD 客户背调、这个客户是不是套方案的、这个询盘该不该跟、该不该报价、该问客户什么问题、推进寄样小试、BDD 回复话术、工业废水客户背景调查、需求证据等级、报价准备就绪、推荐联系岗位。输出两层判断卡：1 屏主卡 + 证据附录。
agent_created: true
---

# BDD 询盘分析与客户背调 · V1

针对 BDD 电极 / 电化学氧化废水处理业务（Boromond / 波乐美）的询盘判断工具。

**产出不是一份漂亮的背调报告，而是一张 1 屏判断卡：需求有多实、风险有多高、缺什么、下一步做什么。**

---

## 一、单向决策链（本 Skill 的骨架，不可跳步）

```
Evidence（FACT / INFERENCE / UNKNOWN）
        │
        ├────────────────┐
        ▼                ▼
  Industry Fit      Demand Evidence
        │                │
        └───────┬────────┘
                ▼
        BDD Opportunity
                ▼
         Technical Fit
                ▼
      Quotation Readiness
                ▼
           Next Action
```

### 硬规则

| # | 规则 |
|---|---|
| 1 | **严格单向。** 上游未判定，下游不得先行判定。 |
| 2 | **不得多模块分别调用 LLM 得出互相冲突的结论。** 整张卡由同一次推理产出。 |
| 3 | **不得反向回推。** Next Action 不得倒过来影响 Technical Fit 或 Demand Evidence。 |
| 4 | **串联规则（唯一允许的自动推导）**：`Technical Fit = Insufficient Data` 且缺少关键技术参数 → `Quotation Readiness = Need technical data`。 |
| 5 | **人工覆盖（Manual Override）保留**：允许人工规则覆盖 Quotation Readiness，用于「标准产品可直接报价」等特殊场景。覆盖必须留痕：标注 `Manual override` + 覆盖理由 + 依据。 |

---

## 二、四个概念必须严格区分

这四个词最容易互相污染，是判断失真的最大来源。

| 概念 | 回答的问题 | 取值 | 数据要求 |
|---|---|---|---|
| **Industry Fit** | 这个行业是否属于 Boromond 目标市场？ | Target / Adjacent / Outside / Unknown | 只需知道行业 |
| **Demand Evidence** | 是否存在实际项目 / 采购 / 治理需求**证据**？ | Confirmed / Strong Signal / Potential / Weak / Unknown | 只需背调证据 |
| **BDD Opportunity** | 客户现有业务与问题中是否存在 BDD 应用机会？ | High / Medium / Low / Unknown | 需行业 + 需求证据 |
| **Technical Fit** | 现有**技术数据**是否足够判断 BDD 技术适用性？ | Sufficient — Likely Suitable / Sufficient — Likely Unsuitable / Insufficient Data / Engineer Review Required | **必须真实水质数据** |

### 两条禁止自动推导

- ❌ **Industry Fit 高 ≠ Demand Evidence 高。** 行业对口不代表这家公司真有项目。
- ❌ **BDD Opportunity 高 ≠ Technical Fit 高。** 有应用场景不代表这水质技术可行。

> Industry Fit 是**行业属性**，Demand Evidence 是**企业事实**，BDD Opportunity 是**场景判断**，Technical Fit 是**技术判断**。四者证据来源完全不同，不能互相替代。

---

## 三、Evidence Policy（证据政策）

**适用范围：所有关键外部结论，不限于企业信息。**

| 类型 | 定义 | 强制字段 |
|---|---|---|
| **FACT** | 可追溯到公开来源，或客户明确陈述 | **必须**有 `Source` |
| **INFERENCE** | 基于 FACT 的合理推断 | **必须**有 `Reason` + `Confidence` |
| **UNKNOWN** | 未查到 / 无法判断 | **不得自行补全** |

### 三条铁律

1. **FACT 无 Source = 不得标为 FACT**，降级为 INFERENCE 或 UNKNOWN。
2. **INFERENCE 无 Reason 或无 Confidence = 不得输出**。
3. **UNKNOWN 保持空白。** 不允许用行业经验值、同类客户类比、"通常来说"来填充。宁可留白，不可补全。

详细分级标准见 `references/evidence-policy.md`。

---

## 四、核心认知（执行前必读）

BDD 业务标准路径：

```
询盘 → 参数补全 → 寄样小试 → 小试报告 → 报价 → 合同
```

**推论 1**：询盘阶段唯一该追求的 KPI 是"推进到寄样"。
**推论 2**：报价是最后一步。参数不齐不进报价流程。
**推论 3**：防套参数比防假客户更重要——本行业"免费检测 + 方案定制"是标配，被套参数是最高频损失。

---

## 五、什么时候用

- 客户询盘文字（邮件、WhatsApp、微信、阿里/1688 后台、展会名片）
- 只有公司名 / 联系人 / 官网域名
- 明确要求"分析这个客户"、"该不该报价"、"帮我回复"

**不适用**：体育用品/泳具等消费品外贸询盘 → 用 `ai-inquiry-analysis`。
**不适用**：具体技术方案设计、设备选型计算、报价核价核价、工程参数输出 → 属人工工程师职责。

---

## 六、工作流（8 步，严格按决策链顺序）

### 第 1 步：信息提取与缺口盘点

**只提取，不判断。** 缺失字段写"未提供"，不要猜。

| 字段 | 说明 |
|---|---|
| 公司名 | 全称优先 |
| 联系人 / 职位 | 仅用于推断客户类型与联系角色，不作结论 |
| 联系方式 | 邮箱域名可反查公司 |
| 询盘来源 | 官网 / 阿里 / 展会 / 转介绍 / 电话 |
| 询盘原文 | 完整保留 |
| 客户已提供的技术数据 | COD、氨氮、水量、盐度、pH、目标限值、行业 |
| 客户已提的要求 | 要报价？要方案？要样品？要案例？ |

### 第 2 步：客户背调 → 输出 Evidence 列表

用 WebSearch / WebFetch 检索。**每条产出必须标注 FACT / INFERENCE / UNKNOWN。**

检索优先级（详见 `references/lead-signals.md`）：

| 优先级 | 查什么 |
|---|---|
| ★★★ | 环保处罚记录 |
| ★★★ | 环评公示 / 排污许可证 |
| ★★☆ | 招投标信息 |
| ★★☆ | 主体信息（成立时间、注册资本、参保人数、是否实体工厂） |
| ★★☆ | 行业与产污类型 |
| ★☆☆ | 集团/子公司关系、新闻、招聘 |

**注意**：本步只产出 Evidence，**不产出任何判定**。判定在第 4 步。

### 第 3 步：客户类型判定

按 `references/customer-type-playbook.md` 判定为六类之一：

```
终端业主 / 环保工程公司（EPC·集成商） / 设计院 / 科研院所高校 / 贸易商中间商 / Unconfirmed
```

判据必须来自第 2 步的 Evidence。信息不足时输出 `Unconfirmed`，不得猜。

### 第 4 步：四维判定（严格按顺序，不可跳步）

**① Industry Fit**
对照 `references/bdd-fit-rules.md` 的目标市场定义。只需行业，不需要水质数据。
当行业不在已定义清单内 → `Unknown`，不得推断。

**② Demand Evidence** — 五级
按 `references/evidence-policy.md` 的证据映射表定级。
**只依据第 2 步的 Evidence，不依据行业好坏，也不依据最终是否成交。**

**③ BDD Opportunity**
在第 ① ② 都判定完成后，判断客户业务与问题中是否存在 BDD 应用机会。
可以调用 `references/wastewater-signal-map.md` 做定性识别，但**不得输出技术参数**。

**④ Technical Fit**
判定依据是**现有技术数据是否足够**。
- 缺进水浓度 / 特征污染物 / 盐度或氯离子任一项 → **`Insufficient Data`**
- 数据齐全且落在 `bdd-fit-rules.md` 定义范围内 → `Sufficient — Likely Suitable`
- 数据齐全但触发否决条件 → `Sufficient — Likely Unsuitable`
- 规则未覆盖 → `Engineer Review Required`

**硬规则**：`Insufficient Data` 时**禁止**用行业经验值代替，禁止输出任何工艺参数。

### 第 5 步：Missing Critical Data

列出补齐后能推进决策的关键数据，**最多 5 项**。格式：

```
① 进水 COD ② 处理水量 m³/d ③ 目标限值
```

数据齐全时输出 `None`。

### 第 6 步：Commercial Risk

按 `references/disclosure-policy.md` 的危险信号定级：Low / Medium / High / Unknown。

**判据只用询盘当时可观察的事实。** 禁止使用"最终是否成交"作为依据。

### 第 7 步：Quotation Readiness

四态枚举，**只输出状态，不输出金额**：

| 状态 | 触发条件 |
|---|---|
| `Ready for quotation` | 5 项关键参数齐 + 资料边界已确认 |
| `Not ready` | 缺商务条件（需求量、交付节奏、采购时间表） |
| `Need technical data` | **Technical Fit = Insufficient Data 且缺关键技术参数（自动串联）** |
| `Engineer review` | 涉及技术判定，需工程师确认 |

**人工覆盖**：允许以 `Manual override` 标注覆盖，须附理由与依据（例：标准品现货可直接报价）。金额一律由商务系统承载。

### 第 8 步：Contact Role + Next Action + 输出

**Contact Role**：按 `references/contact-role-map.md`，根据客户类型推荐应联系的**岗位角色**。
- 只推荐角色，例如「环保负责人」「技术总工」「工艺设计师」
- 公开来源确实查到真人时，可展示 `Name + Position + Source`
- 查不到 → 输出 `No verified contact found`。**禁止生成人名/电话/邮箱/微信**

**Next Action**：一句话，且必须与决策链末端一致（例："拿到 COD / 水量 / 目标限值三项，推进寄样"）。

**输出**：按 `assets/output-card-template.md` 的两层结构。

---

## 七、硬性约束（违反即视为分析无效）

| # | 约束 | 原因 |
|---|---|---|
| 1 | 决策链严格单向，不跳步、不回推 | 防止各模块独立判断互相冲突 |
| 2 | Industry Fit 高 ≠ Demand Evidence 高；BDD Opportunity 高 ≠ Technical Fit 高 | 概念混淆是最大失真来源 |
| 3 | 无真实水质数据 → Technical Fit 必须 `Insufficient Data` | 禁止用行业经验值代替技术判定 |
| 4 | FACT 必须有 Source；INFERENCE 必须有 Reason + Confidence；UNKNOWN 不得补全 | 幻觉防线 |
| 5 | 查不到就输出 `UNKNOWN` / `未查到` | 中小企业公开信息稀薄是常态 |
| 6 | 主卡不承载 Evidence 明细 | 1 屏约束 |
| 7 | 不输出工艺参数、设备选型、达标承诺、工程参数 | 安全边界 |
| 8 | 不给客户案例名单与联系方式 | 公司资产 |
| 9 | 只推荐 Contact Role；无公开来源证据不得生成具体人名/电话/邮箱 | 合规风险点 |
| 10 | Quotation Readiness 只输出状态，不输出金额 | 金额时效敏感，且属商务决策 |
| 11 | 输出必含"建议小试"（在 Next Action 或附录） | 行业标准流程 + 风险防火墙 |
| 12 | Commercial Risk 判据不得使用"是否成交" | 结果论会污染规则且无法验证 |

---

## 八、输出结构（两层）

### 主判断卡（1 屏，固定 10 字段）

```
Company                  公司名（地区）
Customer Type            五类之一 / Unconfirmed
Industry Fit             Target / Adjacent / Outside / Unknown
Demand Evidence          Confirmed / Strong Signal / Potential / Weak / Unknown
BDD Opportunity          High / Medium / Low / Unknown
Technical Fit            Sufficient — Likely Suitable / Sufficient — Likely Unsuitable /
                         Insufficient Data / Engineer Review Required
Commercial Risk          Low / Medium / High / Unknown
Missing Critical Data    最多 5 项 / None
Quotation Readiness      Ready for quotation / Not ready / Need technical data / Engineer review
Recommended Contact Role 岗位角色（+ Name/Position/Source 或 No verified contact found）
Next Action              一句话
```

**主卡不放 Evidence / Source / Confidence / Fact·Inference·Unknown。**
`Unknown` 的字段**直接留 `Unknown`**，不为了填满模板而占位。

### 附录（折叠区）

Evidence 明细表 + 回复草稿 + 推进节奏。

详见 `assets/output-card-template.md`。

---

## 九、文件说明

```
SKILL.md                                本文件：决策链 + 概念区分 + 证据政策 + 工作流 + 硬性约束
references/evidence-policy.md           Evidence Policy：FACT/INFERENCE/UNKNOWN 定义与分级映射表
references/bdd-fit-rules.md             Industry Fit 目标市场定义 + Technical Fit 判定框架（骨架，待填）
references/wastewater-signal-map.md     行业关键词 → 废水类型识别表（骨架，待填）
references/lead-signals.md              检索指引：环保处罚 / 环评 / 招投标 / 主体核实
references/customer-type-playbook.md    六类客户判定标准 + 策略矩阵
references/contact-role-map.md          客户类型 → 推荐联系岗位序列
references/must-ask-params.md           必问参数清单 + Quotation Readiness 门槛
references/disclosure-policy.md         技术资料开放边界 + 商业风险危险信号
references/reply-playbook.md            分场景回复话术 + 分阶段跟进节奏
assets/output-card-template.md          两层输出模板
```

---

## 十、TBD · 需向 Boromond 技术/销售确认

以下为本轮**刻意留空**的项，未经确认前 Skill 会输出 `Unknown` 或 `Insufficient Data`，不会自行推断：

| # | TBD 项 | 归属 |
|---|---|---|
| 1 | **目标市场行业清单**（哪些算 Target / Adjacent / Outside） | 销售 |
| 2 | **Technical Fit 判定阈值**（各参数适用范围、否决条件） | 技术 |
| 3 | **行业 → 废水特征关键词表** | 技术 |
| 4 | **资料开放边界三档清单**（尤其哪些小试报告已脱敏） | 销售 |
| 5 | **Quotation Readiness 的人工覆盖规则**（哪些标准品可直接报价） | 销售 |
| 6 | **六类客户的判定信号**是否准确 | 销售 |
| 7 | **必问参数**是否有必须增删的项 | 技术 + 销售 |

确认后改对应 reference 文件即可，无需改动本文件主流程。
