# BDD Customer Intelligence Skill · V1 Freeze & Scope Check

> 日期：2026-09-26
> 状态：**仅审计，未改动任何文件**
> 审计范围：11 个 Skill 文件（1,849 行）+ 1 个外部文档（245 行）
> Skill 路径：`C:\Users\Administrator\.workbuddy\skills\bdd-inquiry-analyzer\`

---

## 一、审计基准

**V1 Freeze 后的唯一职责**：针对 Boromond BDD 业务，对潜在客户进行**完整企业背调**，输出**客户开发判断依据**。

**目标链路（9 步）**

```
Company Verification → Company Profile → Customer Type → Industry Fit
   → BDD Relevance → Demand Evidence → Contact Strategy → Evidence → Next Action
```

**明确不负责**：项目报价 / 正式技术方案 / 设备选型 / 小试技术方案 / 工程计算 / 正式项目跟进流程 / 案例数据库

---

## 二、五个必须先拍板的发现

### 发现 1 · 目标链路有 2 步在现有 Skill 中根本不存在

| 目标步骤 | 现状 |
|---|---|
| **Company Verification**（公司核实） | ❌ 无对应步骤。现有第 1 步是"信息提取与缺口盘点"——只提取询盘文字，不做核实。主体核实内容散在 `lead-signals.md` 第二节，但不构成独立步骤，也**不进入输出** |
| **Company Profile**（公司概况） | ❌ 完全不存在。主卡只有 `Company` 一行名称，**无公司概况字段**，无成立时间/规模/主营/工厂等输出位 |

**后果**：按现状冻结，Skill 无法履行"**完整企业背调**"这一唯一职责——它能判断"该不该跟"，但说不清"这家公司是什么"。

**建议**：这不属于"新增功能"，而是**补上目标链已明确定义的缺口**。需你确认是否允许补。

---

### 发现 2 · Evidence 被排在链路倒数第二，与"单向决策链"物理冲突

Evidence（FACT / INFERENCE / UNKNOWN）是判定的**输入源**：Demand Evidence 由证据定级、Customer Type 判据必须来自 Evidence。把它排在 `Contact Strategy` 之后、`Next Action` 之前，在数据流上不成立。

**建议**：拆成双重角色——
- **第 2 步前置采集**（生产 Evidence）
- **末尾以附录呈现**（消费 Evidence）

保留你写的顺序语义（Evidence 最终作为输出的一部分），但明确"采集在前、呈现为末"。

---

### 发现 3 · BDD Relevance 的位置变化会改变它的定义

| | 现在 | 你本轮要求 |
|---|---|---|
| 名称 | BDD **Opportunity** | BDD **Relevance** |
| 位置 | Industry Fit + Demand Evidence **之后** | Industry Fit **之后**、Demand Evidence **之前** |
| 输入依赖 | 行业 **+** 需求证据 | 只有行业 |

**建议：这是更好的设计，采纳。** 两个概念因此变得干净：

| 字段 | 口径 | 回答 |
|---|---|---|
| **Industry Fit** | 商业定位 | 该行业是否属 Boromond 目标市场？ |
| **BDD Relevance** | 技术场景 | 该行业废水是否属 BDD 应用场景？（不需要客户有需求） |

两者一个是商业口径、一个是技术场景口径，互不冗余。**但定义必须改写**：现有 `SKILL.md` L55 写的是"需行业 + 需求证据"，与新区位矛盾。名称统一为 BDD Relevance，弃用 BDD Opportunity。

---

### 发现 4 · 主卡 10 字段 ≠ 本轮 9 步链

主卡含 4 项不在链路内的字段：

| 字段 | 判定 | 理由 |
|---|---|---|
| **Commercial Risk** | ✅ 建议 **A 保留** | 属"客户开发判断依据"（这客户值不值得投入、资料给不给） |
| **Missing Critical Data** | ✅ 建议 **A 保留** | 属"客户开发判断依据"（该问什么） |
| **Technical Fit** | ⚠️ 建议 **B 归档** | 其判定阈值本质是工程计算基础（明确在不负责清单内） |
| **Quotation Readiness** | ⚠️ 建议 **B 归档** | 链路中无此环节，且明确不负责"项目报价" |

---

### 发现 5 · 归档 Technical Fit 会产生连锁断裂

| 断裂点 | 位置 | 说明 |
|---|---|---|
| 场景 H「敢劝退」 | `reply-playbook.md` L150-165 | 触发条件就是 `Technical Fit = Likely Unsuitable`。Technical Fit 归档后该场景**永远无法触发** |
| 报价路径行 | `customer-type-playbook.md` L37/57/78/96/115/130 | 全部指向 Quotation Readiness 状态 |
| 附录 C 推进节奏 | `output-card-template.md` L90-100 | 依赖报价与跟进流程 |
| 硬约束 4/10 | `SKILL.md` L226/L234 | 串联规则与"不输出金额"约束随归档失效 |

**建议**：场景 H 一并归档 B（未来平台里 Technical Fit 恢复后再启用）。

---

## 三、文件级总览

| # | 文件 | 行数 | A | B | C | 建议动作 |
|---|---|---|---|---|---|---|
| 1 | `SKILL.md` | 301 | 中 | 中 | 少 | **重写**决策链 + 工作流 + 输出结构 |
| 2 | `assets/output-card-template.md` | 162 | 多 | 少 | 少 | **重排**主卡字段，附录 B/C 归档 |
| 3 | `references/evidence-policy.md` | 144 | **近全** | — | — | **保留**，删第五节（与 disclosure 重复） |
| 4 | `references/lead-signals.md` | 144 | **近全** | — | — | **保留**，仅改第三节顺序说明 |
| 5 | `references/contact-role-map.md` | 120 | **全** | — | — | **保留**（本文件即 Contact Strategy） |
| 6 | `references/wastewater-signal-map.md` | 98 | **近全** | — | — | **保留** |
| 7 | `references/bdd-fit-rules.md` | 148 | 少 | **多** | 少 | **拆分**：第一部分留 A，二~四部分归档 B |
| 8 | `references/must-ask-params.md` | 176 | 多 | 中 | 少 | **拆分**：二~四节留 A，一/五节归档 B/C |
| 9 | `references/customer-type-playbook.md` | 182 | 多 | 中 | — | **瘦身**：去报价路径 / 资料开放 / 决策周期 |
| 10 | `references/disclosure-policy.md` | 144 | 少 | 多 | 中 | **拆分**：第二节留 A，一/三/四节归档 B |
| 11 | `references/reply-playbook.md` | 230 | **极少** | 中 | **多** | **整体归档**，仅留场景选择逻辑 + 触发信号表 |
| 外 | `D:/Case Flow/BDD询盘Skill_校准清单与回测方案.md` | 245 | 多 | 中 | 少 | **同步瘦身**，A/D/H 段调整 |

---

## 四、逐文件章节级明细

### 1. SKILL.md（301 行）

| 章节 | 行 | 判定 | 处置 |
|---|---|---|---|
| frontmatter description | L3 | ⚠️ | 含"是不是套方案的""该不该报价""回复话术""推进寄样小试"等 C 类触发词 → **删**，改为纯背调口径 |
| 标题 + 定位语句 | L7-13 | A | 保留 |
| 一、单向决策链（图） | L17-33 | ⚠️ 混 | 替换为 9 步链；Technical Fit / Quotation Readiness 出链 |
| 硬规则 1-3 | L39-41 | A | 保留 |
| 硬规则 4（TF→QR 串联） | L42 | **B** | 随 Technical Fit 归档 |
| 硬规则 5（Manual Override） | L43 | **B** | 属报价流程 |
| 二、四概念区分 | L51-56 | ⚠️ 混 | 四行定义改写：BDD Opportunity → **BDD Relevance**（去需求证据依赖，去"场景判断"改"行业技术场景"）；**Technical Fit 行删除** |
| 二、两条禁止推导 | L58-63 | A | 保留并扩充（新增"Industry Fit 高 ≠ BDD Relevance 高"） |
| 三、Evidence Policy | L69-83 | **A** | 保留不动 |
| 四、核心认知（标准路径） | L89-93 | A | 路径图保留（背景知识） |
| 四、推论 1（KPI 是推进寄样） | L95 | **B** | 属销售执行目标 |
| 四、推论 2（报价是最后一步） | L96 | **B** | 属报价流程 |
| 四、推论 3（防套参数） | L97 | **A** | 属 Commercial Risk |
| 五、什么时候用 / 不适用 | L103-108 | A | 保留；"不适用"段可扩充 C 类边界声明 |
| 六、第 1 步 信息提取 | L114-126 | ⚠️ | **拆为两步**：Company Verification（核实）+ Company Profile（概况）；现表只提询盘文字，不核实 |
| 六、第 2 步 背调 → Evidence | L128-143 | A | 保留；顺序说明改为"采集前置" |
| 六、第 3 步 客户类型 | L145-153 | A | 保留 |
| 六、第 4 步 ① Industry Fit | L157-159 | A | 保留 |
| 六、第 4 步 ② Demand Evidence | L161-163 | A | 保留，**顺序后移**到 BDD Relevance 之后 |
| 六、第 4 步 ③ BDD Opportunity | L165-167 | ⚠️ | 改名为 **BDD Relevance**；删"在第①②都判定完成后"→ 改为"只依赖 Industry Fit" |
| 六、第 4 步 ④ Technical Fit | L169-176 | **B** | 归档；其中"数据充分性检查"逻辑改挂到 Missing Critical Data |
| 六、第 5 步 Missing Critical Data | L178-186 | **A** | 保留；去掉对"报价门槛 5 项"的隐含绑定 |
| 六、第 6 步 Commercial Risk | L188-192 | **A** | 保留 |
| 六、第 7 步 Quotation Readiness | L194-205 | **B** | 归档 |
| 六、第 8 步 Contact Role + Next Action | L207-216 | A | 保留；+ Company Profile 输出 |
| 七、硬性约束 12 条 | L220-235 | ⚠️ 混 | 1/2/3/5/6/7/8/9/11/12 保留；**4 归档**；**10 归档**（报价状态） |
| 八、输出结构（主卡 10 字段） | L241-259 | ⚠️ | 重排：删 Technical Fit / Quotation Readiness → 变 8 字段 + Company Profile |
| 八、附录 | L261-265 | ⚠️ | 保留附录 A；**附录 B/C 归档** |
| 九、文件说明 | L269-283 | ⚠️ | 重排（新增 / 归档文件标注） |
| 十、TBD 表 7 项 | L287-301 | ⚠️ 混 | #1/#3/#4/#6/#7 保留（#3 改归属）；**#2 Technical Fit 阈值 → B**；**#5 Quotation Readiness 人工覆盖 → B** |

---

### 2. assets/output-card-template.md（162 行）

| 章节 | 行 | 判定 | 处置 |
|---|---|---|---|
| 结构总览（两层） | L5-10 | ⚠️ | 改为三层：主卡 / 附录 A（Evidence）/ 归档说明 |
| 主卡 Company | L22 | **A** | 保留 |
| 主卡 Customer Type | L23 | **A** | 保留 |
| 主卡 Industry Fit | L24 | **A** | 保留 |
| 主卡 Demand Evidence | L25 | **A** | 保留 |
| 主卡 BDD Opportunity | L26 | ⚠️ | 改名 BDD Relevance |
| 主卡 **Technical Fit** | L27 | **B** | **删除** |
| 主卡 **Commercial Risk** | L28 | **A** | 保留 |
| 主卡 **Missing Critical Data** | L29 | **A** | 保留 |
| 主卡 **Quotation Readiness** | L30 | **B** | **删除** |
| 主卡 Recommended Contact Role | L31 | **A** | 保留 |
| 主卡 Next Action | L32 | **A** | 保留 |
| **缺 Company Profile** | — | **A** | 需新增行 |
| 字段填写规则 | L37-49 | ⚠️ | 同步删 B 项规则 |
| 留白规则（4 组对照） | L51-60 | **A** | 保留（这是本文件最有价值的部分） |
| 附录 A · Evidence 明细 | L66-81 | **A** | 保留 |
| 附录 B · 回复草稿 | L83-88 | **B** | 归档 |
| 附录 C · 推进节奏 | L90-100 | **C** | 归档 |
| 禁止项 9 条 | L105-117 | **A** | 保留；"不输出金额"条保留（商务边界） |
| 长度控制 | L121-131 | A | 保留（主卡变短，上限可收紧） |
| 分级输出 | L135-142 | A | 保留 |
| 填写示例 | L146-162 | ⚠️ | 同步删 Technical Fit / Quotation Readiness 两行 |

---

### 3. references/evidence-policy.md（144 行）

| 章节 | 行 | 判定 | 处置 |
|---|---|---|---|
| 一、三类型定义 | L7-19 | **A** | 保留 |
| 二、Confidence 分级 | L23-34 | **A** | 保留 |
| 三、判定流程图 | L37-49 | **A** | 保留 |
| 四、Demand Evidence 五级映射 | L53-70 | **A** | **核心资产，保留** |
| 五、Commercial Risk 危险信号 | L74-94 | ⚠️ | 与 `disclosure-policy.md` L59-75 **内容重复** → 保留此处作为**唯一定级来源**，删除 disclosure 侧副本 |
| 六、输出格式 + 可溯源率 | L98-123 | **A** | 保留（回测指标） |
| 七、常见错误对照 | L127-136 | **A** | 保留 |
| 八、待校准项 | L140-144 | A | 保留 |

**结论：本文件近乎全 A，仅需去重。**

---

### 4. references/lead-signals.md（144 行）

| 章节 | 行 | 判定 | 处置 |
|---|---|---|---|
| 一、三件套（环保处罚 / 环评 / 招投标） | L9-55 | **A** | 保留 |
| 一、4 辅助信号 | L57-67 | **A** | 保留 |
| 二、主体信息核实（8 项表） | L71-90 | **A** | 保留 → **同时作为 Company Verification 的数据来源** |
| 三、检索输出标准格式 | L94-111 | **A** | 保留 |
| 四、检索失败处理 | L114-123 | **A** | 保留 |
| 五、职责边界 | L126-135 | A | 保留 |
| 六、待校准项 | L139-144 | A | 保留 |

**结论：全 A，最干净的文件。仅需在第二节补"主体核实 → Company Verification 输出"的映射。**

---

### 5. references/contact-role-map.md（120 行）

| 章节 | 行 | 判定 | 处置 |
|---|---|---|---|
| 一、6 条硬性约束 | L9-18 | **A** | 保留（合规关键） |
| 二、六类 → 岗位序列 | L26-83 | **A** | 保留 |
| 三、三种输出格式 | L87-111 | **A** | 保留 |
| 四、待校准项 | L115-120 | A | 保留 |

**结论：全 A。本文件即目标链中的 `Contact Strategy`，无需改动。**

---

### 6. references/wastewater-signal-map.md（98 行）

| 章节 | 行 | 判定 | 处置 |
|---|---|---|---|
| 一、作用边界 | L9-17 | **A** | 保留 |
| 二、行业关键词 → 行业识别 | L20-33 | **A** | 保留（骨架待填） |
| 三、废水特征关键词 → 特征信号 | L37-52 | **A** | 保留（骨架待填） |
| 四、水质数据完整度检查 | L56-73 | **A** | 保留 → 服务 Missing Critical Data |
| 五、待校准项 | L77-85 | A | 保留 |
| 六、职责边界 | L89-98 | A | 保留 |

**结论：近全 A。唯一调整：服务于 BDD Relevance 而非 BDD Opportunity（改 1 处措辞）。**

---

### 7. references/bdd-fit-rules.md（148 行）— **需拆分**

| 章节 | 行 | 判定 | 处置 |
|---|---|---|---|
| 第一部分 · Industry Fit 规则 | L8-43 | **A** | **保留**（目标市场清单待填） |
| 第二部分 · Technical Fit 规则 | L47-111 | **B** | 归档（技术阈值 = 工程计算基础） |
| 第三部分 · 判定流程 | L115-133 | **B** | 归档（含 TF→QR 串联） |
| 第四部分 · 待校准汇总 | L137-148 | ⚠️ | 拆：第 1 项留 A；第 2~6 项归档 B |

**归档后本文件只剩 43 行 + 待确认问题。** 建议改名或保持原名，仅保留 Industry Fit 部分。

---

### 8. references/must-ask-params.md（176 行）— **需拆分**

| 章节 | 行 | 判定 | 处置 |
|---|---|---|---|
| 一、Quotation Readiness 门槛 | L5-58 | **B** | 归档（含 4 态枚举、5 项门槛、Manual Override、催报价话术） |
| 二、必问参数清单（A~F 六类） | L62-119 | **A** | **保留**（这是本文件真正的核心资产，服务 Missing Critical Data） |
| 三、参数合理性自检 | L123-136 | **A** | 保留（数据校验 = 背调质量） |
| 四、数据缺失处理原则 | L140-148 | **A** | 保留 |
| 五、报价流程归属说明 | L152-163 | **C** | 移出（商务口径） |
| 六、待校准项 | L167-176 | ⚠️ | 拆：第 1/4/5 项留 A；第 2/3/6 项归档 B |

**建议：归档后改名或保持原名，实质变为「必问参数与数据校验」。**

---

### 9. references/customer-type-playbook.md（182 行）— **需瘦身**

| 章节 | 行 | 判定 | 处置 |
|---|---|---|---|
| 判定优先级 ①~⑥ | L14-23 | **A** | 保留 |
| 各类：定义 / 识别信号 / 核心诉求 / 常见误区 | 各处 | **A** | 保留 |
| 各类：**推荐联系岗位** 行 | L35/55/76/94/113/129 | ⚠️ | 与 `contact-role-map.md` **重复** → 改为指针，单一来源 |
| 各类：**决策周期** 行 | L36/56/77/95/114 | **B** | 归档（销售打法） |
| 各类：**报价路径** 行 | L37/57/78/96/115/130 | **B/C** | 归档（报价流程） |
| 各类：**资料开放** 行 | L38/58/79/97/116/131 | **B** | 归档（→ disclosure-policy 单一来源） |
| 各类：推进要点 / 战略价值 | 各处 | **A** | 保留 |
| 六、Unconfirmed | L124-133 | **A** | 保留 |
| 策略矩阵速查 | L139-150 | ⚠️ 混 | 保留列：优先级 / 核心推手 / 首要动作 / 商业风险；**删列**：决策周期 / 价格敏感度 / 报价路径 / 技术资料 |
| 组合客户 | L154-160 | **A** | 保留 |
| 职责边界 | L164-172 | A | 更新 |
| 待校准项 | L176-182 | ⚠️ | 第 1/2 项留 A；第 3/4/5 项归档 B |

---

### 10. references/disclosure-policy.md（144 行）— **需拆分**

| 章节 | 行 | 判定 | 处置 |
|---|---|---|---|
| 一、三档资料分类（✅/⚠️/❌） | L11-47 | **B** | 归档（销售 SOP，非背调） |
| 二、危险信号（14 行表 + 定级规则） | L51-75 | **A** | **保留**，但与 evidence-policy 第五节重复 → **建议只留一处**（见下方建议） |
| 三、标准应对话术（5 场景） | L79-101 | **B** | 归档（话术执行） |
| 四、可交换原则 | L105-121 | **B** | 归档（销售谈判） |
| 五、待校准项 | L125-132 | ⚠️ | 第 1/6 项留 A；第 2/3/4/5 项归档 B |
| 六、职责边界 | L134-144 | A | 更新 |

**建议**：本文件在 A 档只剩第二节。可将第二节**并入 `evidence-policy.md` 第五节**（已高度重复），原文件整体归档 B。这样 A 档少一个文件，维护点从两处降为一处。

---

### 11. references/reply-playbook.md（230 行）— **重点检查项，建议整体归档**

| 章节 | 行 | 判定 | 说明 |
|---|---|---|---|
| 顶部｜场景选择依据（Demand Evidence + Commercial Risk） | L3-8 | **A** | 这是**判断 → 行动的桥**，是本 Skill 唯一该留的部分。保留（可并入 SKILL.md 第 8 步） |
| 一｜黄金法则 + 回复 4 段结构 | L10-25 | **B** | 写作方法论，非背调 |
| 二｜场景 A：需求实 + 参数不全 | L31-51 | **B** | 话术模板 |
| 二｜场景 B：**客户催报价** | L56-65 | **C** | 命中"项目报价" |
| 二｜场景 C：Commercial Risk = High | L70-83 | **B** | 逻辑属 A，话术属 B |
| 二｜场景 D：工程公司 | L88-100 | **B** | 话术模板 |
| 二｜场景 E：设计院 | L106-117 | **B** | 话术模板 |
| 二｜场景 F：**科研院所（快速报价发货）** | L122-132 | **C** | 命中"项目报价"+"正式项目跟进" |
| 二｜场景 G：**贸易商（报标准价）** | L138-147 | **C** | 命中"项目报价" |
| 二｜场景 H：**敢劝退** | L151-165 | **B** | 触发条件依赖 Technical Fit（发现 5） |
| 三｜**分阶段跟进节奏 Day 0/2/5/10/20/30** | L171-178 | **C** | **明确命中"正式项目跟进流程"** |
| 三｜二次跟进原则 + 新价值清单 | L182-188 | **C** | 同上 |
| 四｜触发式跟进（5 行信号表） | L194-202 | ⚠️ | **信号表 → A**（背调证据的直接变现，是 Skill 独有价值）；**跟进动作描述 → C** |
| 五｜语言与格式要求 | L208-213 | **B** | 撰写规范 |
| 五｜禁忌 4 条 | L215-219 | ⚠️ | 前 2 条（不承诺达标 / 不给价格）→ **A 边界**，建议移入 SKILL.md 硬约束；后 2 条 → B |
| 六｜待校准项 | L225-230 | **C** | 报价单模板 / 保密协议 / 库存发货周期 → C；署名落款 / 中英译法 → B |

**量化**：A ≈ 30 行（13%）、B ≈ 95 行（41%）、C ≈ 65 行（28%）、结构行 ≈ 40 行。

**建议处置**：
- **保留并迁移**：顶部场景选择逻辑 L3-8 → 迁入 `SKILL.md` 第 8 步；触发信号表 L196-201 → 迁入 `contact-role-map.md` 或独立小节
- **整体归档 B/C**：其余 200 行移出 Skill

**这是本轮唯一一个建议"整体移出"的文件。** 原因是它同时命中你列出不负责项中的三项（项目报价 / 小试技术方案 / 正式项目跟进流程），且它承载的是**执行**而非**判断**——与"输出客户开发判断依据"的职责正交。

---

### 12. 外部文档：D:/Case Flow/BDD询盘Skill_校准清单与回测方案.md（245 行）

| 章节 | 行 | 判定 | 处置 |
|---|---|---|---|
| 一、是什么 / 不是什么 | L9-27 | **A** | 保留，同步改 |
| 二、文件结构（10 文件图） | L31-50 | ⚠️ | 重排 |
| 三、A 段 Quotation Readiness + 商务口径 | L58-67 | **B/C** | 归档（报价 + 小试政策 + 行业黑名单 → C） |
| 三、B 段 客户类型规则 | L69-75 | **A** | 保留 |
| 三、C 段 资料开放边界 | L77-83 | **B** | 归档 |
| 三、D 段 Industry Fit + Technical Fit | L85-94 | ⚠️ | 拆：Industry Fit → A；Technical Fit 阈值 → B |
| 三、E 段 废水特征识别 | L96-100 | **A** | 保留 |
| 三、F 段 推荐联系岗位 | L102-107 | **A** | 保留 |
| 三、G 段 证据政策 | L109-113 | **A** | 保留 |
| 三、H 段 回复话术 | L115-119 | **B** | 归档 |
| 四、回测方案 | L123-168 | ⚠️ | 保留主体；**第 6 项"Technical Fit 检查"随归档删除**；第 10 项"决策链一致性（QR↔TF 串联）"改为新链一致性 |
| 五、日常使用方式（5 场景） | L172-194 | ⚠️ | 场景 3（催报价）→ B；场景 4（套方案）→ A；其余保留 |
| 六、Skill 与平台分工 | L198-211 | **A** | 保留（重要定位文档） |
| 七、WorkBuddy 配套修改 | L215-218 | A | 保留（历史记录） |
| 八、Codex vs WorkBuddy | L222-232 | **C** | 已决策完成，可移出至决策记录 |
| 九、V1 边界声明 | L236-244 | A | 保留，补充本轮新增边界 |

---

## 五、归档执行方案（待确认后执行）

### 归档位置

```
D:/Case Flow/_bdd-skill-archive/V1.0-freeze/
├── reply-playbook.md                  （L10-230 主体）
├── disclosure-policy.md               （第一/三/四/五节）
├── bdd-fit-rules.technical.md         （第二~四部分）
├── must-ask-params.quotation.md       （第一/五节）
└── README.md                          （归档原因 + 回收条件 + 关联的 TBD 项）
```

**为什么不留在 Skill 目录内**：`references/` 下的 markdown 可能被按需读取，留在目录内存在误加载风险。移出到 Skill 外可彻底隔离，同时不丢失内容。

### Skill 内保留的指针

在 `SKILL.md` 末尾加一节，记录已归档内容及回收条件（例：「Technical Fit 判定规则已归档至 `_bdd-skill-archive/V1.0-freeze/`，待 Boromond 技术确认阈值后，于平台阶段回收」）。**不写成可加载文件，只写路径说明。**

---

## 六、冻结后的 Skill 形态预测

| 项 | 现状 | 冻结后 |
|---|---|---|
| 文件数 | 11 | **8**（4 个新 / 2 个归档 / 其余瘦身） |
| 总行数 | 1,849 | **约 1,150**（-38%） |
| 主卡字段 | 10 | **9**（删 TF/QR，增 Company Profile） |
| 附录 | A + B + C | **仅 A** |
| 输出长度 | 主卡 + 3 附录 | 主卡 + 1 附录 |

**保留的 8 个文件**

```
SKILL.md                               决策链 + 概念区分 + 证据政策 + 工作流 + 约束
references/evidence-policy.md          证据政策 + Demand Evidence 分级 + Commercial Risk 定级
references/lead-signals.md             检索指引（三件套 + 主体核实）
references/wastewater-signal-map.md     废水特征信号识别（骨架）
references/bdd-fit-rules.md            Industry Fit 规则（技术部分已归档）
references/customer-type-playbook.md   六类客户判定 + 策略（已瘦身）
references/contact-role-map.md         客户类型 → 联系岗位
references/must-ask-params.md          必问参数 + 数据校验
assets/output-card-template.md         两层输出模板
```

（实际为 9 个文件——4 个新建于 V1 中的文件里 `bdd-fit-rules.md` 保留、其余 3 个全留；`disclosure-policy.md` 与 `reply-playbook.md` 归档。）

---

## 七、需要你拍板的 8 项

| # | 事项 | 我的建议 | 影响 |
|---|---|---|---|
| 1 | **Company Verification / Company Profile 是否补入** | ✅ **必须补** | 不补则"完整企业背调"职责无法履行。属补缺口，非新增功能 |
| 2 | **Technical Fit 去留** | **归档 B**；其"数据充分性检查"逻辑并入 Missing Critical Data | 连带场景 H 归档 |
| 3 | **Quotation Readiness 去留** | **归档 B** | 连带 customer-type-playbook 报价路径行归档 |
| 4 | **Commercial Risk / Missing Critical Data 是否保留** | ✅ **保留 A**（虽不在 9 步链，但属开发判断依据） | 主卡字段数 9 |
| 5 | **Evidence 在链中的位置** | 拆为「第 2 步采集 + 末尾附录呈现」 | 保证单向链成立 |
| 6 | **BDD Relevance 定义改写** | ✅ 改为「只依赖 Industry Fit，判断行业废水是否属 BDD 应用场景」 | 弃用 BDD Opportunity |
| 7 | **reply-playbook 是否整体归档** | ✅ **整体归档**，仅保留 L3-8 场景逻辑 + L196-201 触发信号表 | 本文件 C 占比最高 |
| 8 | **归档位置** | `D:/Case Flow/_bdd-skill-archive/V1.0-freeze/`（Skill 外） | 防误加载 |

---

## 八、边界声明

- 本轮**未删除、未移动、未修改**任何文件
- 未新增任何功能
- 未触及其他 WorkBuddy Skill
- 上述 A/B/C 分类为建议，**未经确认不予执行**

---

*生成时间：2026-09-26 · 审计人：WorkBuddy*
