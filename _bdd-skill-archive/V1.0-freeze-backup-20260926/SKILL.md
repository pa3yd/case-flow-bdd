---
name: bdd-inquiry-analyzer
description: |
  BDD（掺硼金刚石）/ 电化学氧化工业废水处理业务的客户情报与企业背调工具，服务 Boromond（波乐美）业务口径。
  【自动触发】无需用户点名本 Skill。只要意图是查清一家工业企业是什么、是不是 BDD 潜在客户、值不值得开发，就应主动调用——即使对话中完全没有出现 BDD / 波乐美 / 废水字样。
  【触发意图】1) 背调某家公司；2) 分析某家公司；3) 查这家公司什么来头 / 是做什么的；4) 判断这家公司是不是 BDD 潜在客户；5) 判断这个客户值不值得开发 / 该不该跟；6) 调查企业主营业务 · 产品 · 工厂 · 产线 · 行业 · 规模；7) 调查企业环保与废水情况（是否排污、有无污水站、环评公示、排污许可、环保处罚）；8) 调查企业与 BDD 的相关性；9) 查找企业潜在需求信号；10) 查找应该联系的部门或职位；11) 用户仅提供公司名 / 官网 / 域名 / 名片 / 询盘原文 / 邮件 / 聊天记录就要求分析客户。
  【输入门槛】只要给出公司名或网址即可启动；信息缺失时输出 Unknown，不得编造。
  【输出】两层客户情报卡：1 屏主卡（公司核实 / 公司概况 / 客户类型 / 行业契合度 / BDD 相关性 / 需求证据 / 商业风险 / 缺失关键数据 / 推荐联系角色 / 下一步）+ Evidence 附录（每条结论标注 FACT / INFERENCE / UNKNOWN + Source + Confidence）。
  【适用范围】仅用于工业废水治理相关业务的潜在客户——化工、制药、印染、焦化、电镀、半导体、危废、垃圾渗滤液、工业园区污水等领域，含终端业主、环保工程公司、设计院、科研院所、贸易商。
  【排除】不做方案设计、选型、工程计算与项目跟进类交付，不代写邮件，不涉及商务价格。体育用品 / 泳帽泳镜等消费品外贸询盘 → 改用 ai-inquiry-analysis；纯财务 · 股价 · 投融资分析、纯工商信息查询、招聘求职背调、供应商验厂、非工业类公司分析 → 不用本 Skill。
agent_created: true
---

# BDD 客户情报与背调 · V1（Scope Frozen）

针对 BDD 电极 / 电化学氧化废水处理业务（Boromond / 波乐美）的客户情报工具。

**唯一职责：对潜在客户进行完整企业背调，输出客户开发判断依据。**

**产出不是一份漂亮的背调报告，而是一张 1 屏情报卡：这家公司是什么、该不该跟、风险多高、缺什么、该找谁、下一步做什么。**

---

## 一、职责边界（V1 冻结）

### ✅ 本 Skill 只负责

1. **BDD 客户完整企业背调** —— 公司核实 + 公司概况 + 外部环境证据检索
2. **客户开发判断** —— 客户类型 / 行业契合度 / BDD 相关性 / 需求证据 / 商业风险 / 缺失数据 / 联系策略 / 下一步

### ❌ 本 Skill 不负责（明确排除）

| 不做 | 归属 |
|---|---|
| Technical Fit（技术匹配度） | 平台计算层 / 工程师（阈值见归档区） |
| 项目报价 | 商务系统 |
| 设备选型 | 工程师 |
| 小试技术方案 | 工程师 |
| 工程计算 | 工程师 / 平台计算层 |
| 正式技术方案 | 工程师 |
| 正式项目跟进流程 | 销售 CRM / 人工 |
| 自动邮件 / 回复 | 独立"回复执行"Skill（如需要，另建） |
| 案例数据库 | 平台 |

> **为什么划这条线**：背调只依赖公开信息，不被"数据资产化"瓶颈卡住，能立刻见效。技术判断与报价需要案例库、计算引擎与工程师签字，硬塞进本 Skill 会退化成"LLM 凭常识编参数"，对外使用有真实风险。

### 三条不可越界的输出禁令

1. **不输出工艺参数**（电流密度、停留时间、功耗、电极面积）
2. **不承诺处理效果 / 不承诺达标 / 不承诺通过验收**
3. **不做设备选型、不出技术方案、不出金额**

> 备注：不生成未经公开来源验证的具体人名 / 电话 / 邮箱（详见 `contact-role-map.md`）。
> 已归档内容路径与回收条件见第十一节。

---

## 二、单向决策链（本 Skill 的骨架，不可跳步）

```
Input（询盘 / 公司名 / 名片 / 聊天记录）
        │
        ▼
Company Verification           公司核实
        │
        ▼
Evidence Collection            证据收集（生产 FACT / INFERENCE / UNKNOWN）
        │
        ▼
Company Profile                公司概况
        │
        ▼
Customer Type                  客户类型
        │
        ▼
Industry Fit                   行业契合度        ←── 仅行业属性
        │
        ▼
BDD Relevance                  BDD 相关性        ←── 8 项输入，见第四节
        │
        ▼
Demand Evidence                需求证据
        │
        ▼
Commercial Risk                商业风险
        │
        ▼
Missing Critical Data          缺失关键数据
        │
        ▼
Contact Strategy               联系策略
        │
        ▼
Next Action                    下一步行动
        │
        ▼
Evidence Appendix              证据附录（呈现，非新判定）
```

### 硬规则

| # | 规则 |
|---|---|
| 1 | **严格单向。** 上游未判定，下游不得先行判定。 |
| 2 | **不得多模块分别调用 LLM 得出互相冲突的结论。** 整张卡由同一次推理产出。 |
| 3 | **不得反向回推。** Next Action 不得倒过来影响上游任何字段。 |
| 4 | **Evidence 前置采集、末尾呈现。** 物理上必须先产出证据（第 3 步），最后才作为附录展示（第 12 步）。**"排在末尾"是输出顺序，不是判定顺序。** |
| 5 | **不做任何自动串联推导。** V1 移除了所有 TF→QR 类型的跨字段自动推导，每个字段独立依据证据判定。 |

---

## 三、三个概念必须严格区分

这三个词最容易互相污染，是判断失真的最大来源。

| 概念 | 回答的问题 | 取值 | 数据要求 |
|---|---|---|---|
| **Industry Fit** | 这个**行业**是否属于 Boromond 目标市场？ | Target / Adjacent / Outside / Unknown | 只需知道行业 |
| **BDD Relevance** | 这家公司**自身**是否存在 BDD 可切入的应用场景？ | High / Medium / Low / Unknown | **8 项输入，见第四节** |
| **Demand Evidence** | 是否存在实际项目 / 采购 / 治理需求**证据**？ | Confirmed / Strong Signal / Potential / Weak / Unknown | 只需背调证据 |

> Industry Fit 是**行业属性**，BDD Relevance 是**公司级场景判断**，Demand Evidence 是**企业需求事实**。三者证据来源不同，不能互相替代。

### 一条禁止推导（本 V1 最重要的一条）

> ❌ **Industry Fit = High → 不得自动推导 BDD Relevance = High。**

**Industry Fit 只是 BDD Relevance 的 8 项输入之一。**

**示例（必读）**：某 API 原料药企业
- `Industry Fit = Target`（行业属目标市场）
- 但**未确认生产活动、无废水信号、无环境证据**
- → `BDD Relevance = Medium` 或 `Unknown`（**不得给 High**）

**原因**：行业对口只说明"这个行业里可能有生意"，不说明"这家公司自己会产生需要 BDD 处理的废水"。可能是纯贸易型、只做制剂分装、或废水早已委托第三方处理。

### 另一条禁止推导

> ❌ **BDD Relevance = High → 不得推导 Demand Evidence = High。**

有应用场景 ≠ 这家公司现在有采购需求。

---

## 四、BDD Relevance 判定规则（8 项输入）

**BDD Relevance 必须综合以下 8 类输入，不得只依赖 Industry Fit。**

| # | 输入 | 从哪来 | 数据要求 |
|---|---|---|---|
| 1 | **Industry** 行业 | 询盘自述 / 工商经营范围 | 必须 |
| 2 | **Company Business** 公司业务 | 工商信息 / 官网 | 必须 |
| 3 | **Products** 产品 | 官网 / 产品目录 / 电商店铺 | 必须 |
| 4 | **Manufacturing Activity** 制造业活动 | 厂址 / 参保人数 / 设备招标 / 招聘 | **关键项** |
| 5 | **Manufacturing Process** 制造工艺 | 仅**公开可验证时**使用 | 可选；不可推断 |
| 6 | **Wastewater Signals** 废水信号 | 询盘文字（`wastewater-signal-map.md`） | 必须 |
| 7 | **Environmental Evidence** 环境证据 | 处罚 / 排污许可 / 环评（`lead-signals.md`） | 强烈建议 |
| 8 | **Project / EIA / Permit / Tender / ESG / Job signals**<br>项目 / 环评 / 许可证 / 招标 / ESG / 就业信号 | 公开检索 | 强烈建议 |

### 取值定义

| 取值 | 判据（需同时满足） |
|---|---|
| `High` | ① 行业在目标市场 **且** ② 已确认制造业活动 **且** ③ 有明确废水信号 **且** ④ 至少有 1 项环境证据或项目信号支撑 |
| `Medium` | 行业对口 + 有部分信号（如仅制造业活动，或仅废水信号），但**环境证据缺失** |
| `Low` | 行业对口但**明确不存在** BDD 可切入场景（如纯贸易/纯研发无中试/废水已委托第三方且无改造迹象） |
| `Unknown` | 关键输入不足，无法判断（**信息少时就用这个，不要凑**） |

### 强制附注

**BDD Relevance 的每一次输出都必须附：**

```
Reason                             判定理由（为什么是这个等级）
Evidence                           支撑证据（编号指向 Evidence 附录的行）
Confidence                         High / Medium / Low
```

**缺任一字段 → 该判定视为无效。**

### 硬规则

- 不得因 `Industry Fit = High` 直接给 `BDD Relevance = High`。
- 没有废水信号 + 没有环境证据时，**最高只能给 `Medium`**。
- 判定依据不足时输出 `Unknown`，**不得用"该行业通常有废水"来升格**。
- `Manufacturing Process`（制造工艺）只能在**公开可验证**时使用（如环评文件载明的工艺段）。不得靠行业常识推断工艺。
- BDD Relevance 高**不代表** Technical Fit 可行——本 Skill 不做技术判断。

---

## 五、Evidence Policy（证据政策）

**适用范围：所有关键外部结论。** 不限于企业信息——每一个进入情报卡的结论都必须遵守。

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

## 六、工作流（12 步，严格按决策链顺序）

### 第 1 步 · Input 输入

接收：询盘原文 / 公司名 / 联系人 / 名片 / 邮件 / 聊天记录 / 展会信息。

**完整保留原文**，不做改写、不做摘要、不做判断。

### 第 2 步 · Company Verification 公司核实

**确认"这家公司真实存在、主体唯一、名称准确"。**

| 核实项 | 来源 |
|---|---|
| 工商全称（与客户自述名称比对） | 企业信用信息公示系统 |
| 统一社会信用代码 | 同上 |
| 存续状态（在营 / 注销 / 吊销） | 同上 |
| 成立时间 | 同上 |
| 注册地址（是否与客户所述一致） | 同上 |
| 名称歧义 / 重名排查 | 多源交叉 |

**核实结果三态**：

| 结果 | 含义 |
|---|---|
| `Verified` | 主体唯一、名称准确、在营 |
| `Partially Verified` | 存在但信息不全，或名称有出入 |
| `Unverified` | 查不到，或重名无法区分 |

**硬规则**：名称有歧义时**不得选择最像的一家**。输出 `Unverified`，并在 Missing Critical Data 中列出"需客户提供工商全称"。

### 第 3 步 · Evidence Collection 证据收集

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

**注意**：本步只产出证据，**不产出任何等级判定**。判定在第 6~9 步。

### 第 4 步 · Company Profile 公司概况

**回答"这家公司是什么"。** 这是背调的交付主体。

| 字段 | 说明 | 查不到时 |
|---|---|---|
| 工商全称 | 与核实结果一致 | 用客户自述并标注 |
| 成立时间 | — | `Unknown` |
| 注册资本 | — | `Unknown` |
| 参保人数 | 最接近真实规模的数据 | `Unknown` |
| 所在地 | 省 / 市 | `Unknown` |
| 主营范围 | 工商经营范围 | `Unknown` |
| 主营产品 | 官网 / 产品目录 | `Unknown` |
| 是否实体工厂 | 有厂址 + 有环保设施 | `Unknown` |
| 企业性质 | 民营 / 国企 / 上市 / 外资 | `Unknown` |
| 集团 / 子公司关系 | 影响决策链长度 | `Unknown` |

**硬规则**：
- 查不到的字段**直接写 `Unknown`**，不得用"估计""约""大概"填充。
- 概况中每条 FACT 都要有 Source（在 Evidence 附录中可追溯）。

### 第 5 步 · Customer Type 客户类型

按 `references/customer-type-playbook.md` 判定为六类之一：

```
终端业主 / 环保工程公司（EPC·集成商） / 设计院 / 科研院所高校 / 贸易商中间商 / Unconfirmed
```

判据必须来自第 3 步的证据。信息不足时输出 `Unconfirmed`，**不得猜**。

### 第 6 步 · Industry Fit 行业契合度

对照 `references/bdd-fit-rules.md` 的目标市场定义。

**只需行业，不需要水质数据。**

| 取值 | 含义 |
|---|---|
| `Target` | 属 Boromond 核心目标市场行业 |
| `Adjacent` | 非核心，但存在可迁移场景 |
| `Outside` | 明确不在目标市场 |
| `Unknown` | 行业不在已定义清单内，或行业无法确认 |

**硬规则**：行业不在清单内 → `Unknown`，**不得凭常识推断**。

### 第 7 步 · BDD Relevance BDD 相关性

**按第四节规则，综合 8 项输入判定。**

注意：
- Industry Fit 只是 8 项输入之一，**不得直接换算**
- 必须附 `Reason` + `Evidence` + `Confidence`
- 可调用 `references/bdd-relevance-rules.md`（判定细则）与 `references/wastewater-signal-map.md`（废水信号识别）
- **禁止输出任何技术参数与数值区间**

### 第 8 步 · Demand Evidence 需求证据

按 `references/evidence-policy.md` 的证据映射表定级为五级：

```
Confirmed / Strong Signal / Potential / Weak / Unknown
```

**只依据第 3 步的证据**——不依据行业好坏，不依据 BDD Relevance 高低，**也不依据最终是否成交**。

### 第 9 步 · Commercial Risk 商业风险

按 `references/evidence-policy.md` 第五节的危险信号表定级：`Low / Medium / High / Unknown`。

**判据只用询盘当时可观察的事实。禁止使用"最终是否成交"作为依据。**

### 第 10 步 · Missing Critical Data 缺失关键数据

列出**补齐后能推进决策**的关键数据，**最多 5 项**。格式：

```
① 进水 COD ② 处理水量 m³/d ③ 目标限值
```

数据齐全时输出 `None`。

**注意**：本步只回答"该向客户要什么"，**不回答"能不能报价"**。参数完整度依据见 `references/must-ask-params.md`。

### 第 11 步 · Contact Strategy 联系策略

**两部分：找谁 + 什么时机找。**

**① 找谁** —— 按 `references/contact-role-map.md`，根据客户类型推荐应联系的**岗位角色**：
- 只推荐角色，例如「环保负责人」「技术总工」「工艺设计师」
- 公开来源确实查到真人时，可展示 `Name + Position + Source`
- 查不到 → 输出 `No verified contact found`
- **禁止生成人名 / 电话 / 邮箱 / 微信**

**② 场景选择** —— 按 `Demand Evidence` + `Commercial Risk` 的组合决定接触策略：

| Demand Evidence | Commercial Risk | 策略 |
|---|---|---|
| Confirmed / Strong Signal | Low / Medium | **正常推进**：索要缺失数据 + 邀请寄样小试 |
| Confirmed / Strong Signal | High | **先收紧再推进**：先确认真实性 / 走保密流程，再推进寄样 |
| Potential / Weak | 任意 | **先补证据**：通过提问确认项目是否存在，暂不投入技术资源 |
| Unknown | 任意 | **先确认类型与需求**：保持现有接触点，不主动升级 |

> 两者可同时成立（需求很实 + 风险很高）——此时**先按高风险收紧，再按强需求推进**。

**③ 触发信号**（定向接触时机，详见 `contact-role-map.md` 第五节）

### 第 12 步 · Next Action + Evidence Appendix 输出

**Next Action**：一句话，且必须与决策链末端一致。

**Evidence Appendix**：附录 A · Evidence 明细（类型 / 结论 / Source / Reason / Confidence）。

**输出**：按 `assets/output-card-template.md` 的两层结构。

---

## 七、硬性约束（违反即视为分析无效）

| # | 约束 | 原因 |
|---|---|---|
| 1 | 决策链严格单向，不跳步、不回推 | 防止各模块独立判断互相冲突 |
| 2 | **Industry Fit = High → 不得推导 BDD Relevance = High** | 行业对口 ≠ 这家公司有 BDD 场景 |
| 3 | **BDD Relevance = High → 不得推导 Demand Evidence = High** | 有场景 ≠ 有采购需求 |
| 4 | BDD Relevance 必须附 `Reason` + `Evidence` + `Confidence` | 判定可追溯 |
| 5 | 无废水信号 + 无环境证据 → BDD Relevance 最高只能 `Medium` | 防止行业经验值升格 |
| 6 | FACT 必须有 Source；INFERENCE 必须有 Reason + Confidence；UNKNOWN 不得补全 | 幻觉防线 |
| 7 | 查不到就输出 `UNKNOWN` / `Unverified` / `Unknown` | 中小企业公开信息稀薄是常态 |
| 8 | Company Verification 名称有歧义时输出 `Unverified`，不得选最像的一家 | 主体错 = 全盘错 |
| 9 | Company Profile 查不到字段**留 `Unknown`**，不得填"估计值" | 制造虚假完整度 |
| 10 | 主卡不承载 Evidence 明细 | 1 屏约束 |
| 11 | **不输出工艺参数、设备选型、达标承诺、技术方案、金额** | 安全边界 |
| 12 | 不给客户案例名单与联系方式 | 公司资产 |
| 13 | 只推荐 Contact Role；无公开来源证据不得生成具体人名/电话/邮箱 | 合规风险点 |
| 14 | Commercial Risk 判据不得使用"是否成交" | 结果论会污染规则且无法验证 |
| 15 | 输出必含"建议小试"（在 Next Action 或附录） | 行业标准流程 + 风险防火墙 |

---

## 八、输出结构（两层）

### 第一层 · 主判断卡（1 屏，固定 10 字段）

```
Company                      工商全称（地区）+ 核实状态
Company Profile              成立时间 / 参保人数 / 主营 / 是否实体工厂
Customer Type                六类之一 / Unconfirmed
Industry Fit                 Target / Adjacent / Outside / Unknown
BDD Relevance                High / Medium / Low / Unknown
                             + Reason / Evidence / Confidence（三行）
Demand Evidence              Confirmed / Strong Signal / Potential / Weak / Unknown
Commercial Risk              Low / Medium / High / Unknown
Missing Critical Data        最多 5 项 / None
Recommended Contact Role     岗位角色（+ Name/Position/Source 或 No verified contact found）
                             + 接触策略（一句话）
Next Action                  一句话
```

**主卡不放 Evidence 明细。** `Unknown` 的字段**直接留 `Unknown`**，不为了填满模板而占位。

> `BDD Relevance` 是唯一在主卡内展开三行的字段（Reason / Evidence / Confidence），因其判定规则最复杂且最易失真。

### 第二层 · 附录（折叠区）

**仅附录 A** —— Evidence 明细表。

```
<附录 A · Evidence 明细>
| # | 类型 | 结论 | Source | Reason | Confidence |
```

**可溯源率**：已标注 Source 的 FACT 数 / FACT 总数，目标 100%。

详见 `assets/output-card-template.md`。

---

## 九、文件说明（V1 冻结后）

```
SKILL.md                                本文件：职责边界 + 决策链 + 概念区分 + BDD Relevance 规则
                                        + 证据政策 + 工作流 12 步 + 15 条硬性约束
references/evidence-policy.md           证据政策：FACT/INFERENCE/UNKNOWN + Demand Evidence 分级
                                        + Commercial Risk 危险信号定级（唯一定级来源）
references/lead-signals.md              检索指引：三件套（环保处罚/环评/招投标）+ 主体核实
references/bdd-relevance-rules.md       BDD Relevance 判定规则：8 项输入 + 判定流程 + 常见错误
references/bdd-fit-rules.md             Industry Fit 目标市场定义（骨架，待填）
references/wastewater-signal-map.md     废水信号识别：行业关键词 + 特征关键词（骨架，待填）
references/customer-type-playbook.md    六类客户判定标准 + 保留策略（已瘦身）
references/contact-role-map.md          客户类型 → 联系岗位 + 接触战略 + 触发信号
references/must-ask-params.md           必问参数清单 + 数据合理性自检
assets/output-card-template.md          两层输出模板（主卡 10 字段 + 附录 A）
```

**共 10 个文件。**

---

## 十、TBD · 需向 Boromond 技术/销售确认

未经确认前 Skill 会输出 `Unknown` / `Unverified`，不会自行推断。

| # | TBD 项 | 归属 | 不填的后果 |
|---|---|---|---|
| 1 | **目标市场行业清单**（Target / Adjacent / Outside） | 销售 | `Industry Fit` 永远 `Unknown` |
| 2 | **行业 → 废水特征关键词表** | 技术 + 销售 | `BDD Relevance` 的信号识别能力受限 |
| 3 | **BDD Relevance 四级的判据**是否符合实际业务口径 | 销售 | 等级偏差 |
| 4 | **六类客户的判定信号**是否准确，是否需第 7 类 | 销售 | `Customer Type` 误判 → 策略全错 |
| 5 | **六类客户岗位序列**是否符合实际接触经验 | 销售 | 联系角色不准 |
| 6 | **必问参数**是否有必须增删的项 | 技术 + 销售 | Missing Critical Data 不准 |
| 7 | **Demand Evidence 五级判据**是否正确 | 销售 | 等级偏差 |
| 8 | 环保处罚时效窗口（现设 12 个月）是否合适 | 销售 | 信号时效误判 |
| 9 | 检测报告时效窗口（现设 6 个月）是否合适 | 技术 | 同上 |
| 10 | 是否存在"必须拒绝"的行业（安全/合规/成本） | 销售 | 无筛除能力 |

---

## 十一、已归档内容（V1.0 Freeze）

以下能力已从本 Skill 移出，**内容完整保留**在 Skill 外归档区。

**归档位置**：`D:/Case Flow/_bdd-skill-archive/V1.0-freeze/`

| 归档件 | 内容 | 回收条件 |
|---|---|---|
| `reply-playbook.md` | 8 场景回复话术 + 跟进节奏 Day 0~30 + 语言格式 | 需要独立"回复执行" Skill 时 |
| `disclosure-policy.md` | 资料开放三档 + 应对话术 + 可交换原则 | 需对外发布"资料开放 SOP"时 |
| `bdd-fit-rules.technical.md` | Technical Fit 阈值 + 判定流程 + 否决条件 | Boromond 技术确认阈值后 → 平台 L3 |
| `must-ask-params.quotation.md` | Quotation Readiness 四态 + 报价流程归属 | Skill 扩展至商务流程 / 平台接商务系统时 |
| `customer-type-playbook.strategy-columns.md` | 决策周期 / 报价路径 / 资料开放 / 价格敏感度 | 平台 L4 推理层需要销售策略输出时 |
| `output-card-template.appendix-B-C.md` | 附录 B 回复草稿 + 附录 C 推进节奏 | 恢复回复草稿与跟进节奏输出时 |
| `*.pre-freeze.md`（6 个） | 冻结前全量快照 | 供 diff 对照 |

> **注意**：归档区在 Skill 目录之外，不会被 Skill 机制加载。

**已迁移至 Skill 内的内容**：

| 原位置 | 内容 | 现位置 |
|---|---|---|
| `reply-playbook.md` L3-8 | 场景选择依据（Demand Evidence + Commercial Risk 组合） | 本文件第 11 步 Contact Strategy |
| `reply-playbook.md` L196-201 | 触发式跟进信号表 | `references/contact-role-map.md` 第五节 |
| `disclosure-policy.md` L59-75 | Commercial Risk 危险信号表 | `references/evidence-policy.md` 第五节（唯一来源） |

---

## 十二、与其他 Skill 的边界

| 场景 | 用哪个 Skill |
|---|---|
| BDD / 工业废水客户背调与开发判断 | **本 Skill** |
| 体育用品 / 泳具等消费品外贸询盘 | `ai-inquiry-analysis` |
| 回复邮件、话术生成 | 无（V1 已移出；如需，另建独立 Skill） |

**不适用**：具体技术方案设计、设备选型计算、报价核价、工程参数输出 → 属人工工程师职责。
