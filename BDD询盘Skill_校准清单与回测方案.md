# BDD Customer Intelligence Skill · 校准清单与回测方案（V1 Freeze）

> Skill 路径：`C:\Users\Administrator\.workbuddy\skills\bdd-inquiry-analyzer\`
> 版本：**V1 · Scope Frozen**（2026-09-26 冻结）
> 状态：**结构已冻结，等待业务规则校准**（下方留空项填完即可投入使用）
> 归档区：`D:/Case Flow/_bdd-skill-archive/V1.0-freeze/`

---

## 一、这个 Skill 是什么 / 不是什么

| | 内容 |
|---|---|
| **唯一职责** | **BDD 客户完整企业背调 + 客户开发判断** |
| **输出** | 两层客户情报卡：1 屏主卡（10 字段）+ Evidence 附录 |
| **是什么（更强的部分）** | 内置 BDD 行业专属线索检索（**环保处罚 / 招投标 / 环评公示 / 排污许可**）+ 严格单向决策链（防止维度互相污染）+ BDD Relevance 8 项输入判定（阻断"行业对口→相关性高"的误判） |
| **不是** | ❌ 不出技术方案 ❌ 不做设备选型 ❌ 不出金额 ❌ 不承诺处理效果 ❌ 不生成工程参数 ❌ 不写回复邮件 ❌ 不做项目跟进 ❌ 不接案例库 |

### V1 Freeze 相对上一版的变化

| 变化 | 说明 |
|---|---|
| **职责收窄** | 从"背调 + 判断 + 回复执行 + 跟进流程 + 报价门槛"→ 只剩"**背调 + 开发判断**" |
| **链路重构** | 7 环 → **12 步**，新增 Company Verification / Company Profile / Evidence Collection 前置 |
| **BDD Opportunity → BDD Relevance** | 判定规则**重写**：从"仅行业 + 需求证据"改为**综合 8 项输入**，Industry Fit 降为其中一个输入 |
| **Technical Fit 归档** | 阈值属工程计算基础 → 移出 |
| **Quotation Readiness 归档** | 属报价流程 → 移出 |
| **reply-playbook 整体归档** | 承载执行而非判断 → 移出，仅迁移场景选择逻辑与触发信号 |
| **disclosure-policy 整体归档** | 属销售 SOP → 移出，危险信号表并入 evidence-policy |
| 主卡字段 | 11 行（文档误标为 10）→ **10 行**，且文档与实模板现已一致 |
| **自动串联推导全删** | 不再有任何跨字段自动推导（原则见 SKILL.md 硬规则 5） |

---

## 二、Skill 文件结构（10 个文件）

```
bdd-inquiry-analyzer/
├── SKILL.md                              职责边界 + 12 步链路 + BDD Relevance 规则
│                                         + 证据政策 + 工作流 + 15 条硬性约束
├── references/
│   ├── evidence-policy.md                FACT/INFERENCE/UNKNOWN + Demand Evidence 分级
│   │                                     + Commercial Risk 危险信号定级（唯一来源）
│   ├── lead-signals.md                   三件套检索指引 + Company Verification 三态 + 主体核实
│   ├── bdd-relevance-rules.md            BDD Relevance：8 项输入 + 判定流程 + 常见错误
│   ├── bdd-fit-rules.md                  Industry Fit 目标市场定义（骨架，待填）
│   ├── wastewater-signal-map.md          废水信号识别（骨架，待填）
│   ├── customer-type-playbook.md         六类客户判定 + 保留策略
│   ├── contact-role-map.md               联系岗位 + 接触战略 + 触发信号
│   └── must-ask-params.md                必问参数清单 + 数据合理性自检
└── assets/
    └── output-card-template.md           两层输出模板（主卡 10 字段 + 附录 A）
```

**纯 markdown，无 Python 脚本、无 API Key、无外部依赖** → 零维护成本、零执行风险、改规则只需改文字。

---

## 三、校准清单（**唯一阻塞项**）

Skill 的默认规则基于 BDD 行业公开通行做法推导。以下属 Boromond 自有经验，**不填就会判断偏离实际**。

### A. BDD Relevance 判据 → `references/bdd-relevance-rules.md` 第八节

**这是 V1 新增的、也是最重要的校准项。**

- [ ] 四值判据（High / Medium / Low / Unknown）是否符合实际业务口径？
- [ ] **"制造业活动"的确认标准是什么？**（参保人数阈值？厂址？设备招标？招聘记录？）
- [ ] 8 项输入是否需要增删？
- [ ] 是否存在"已使用其他技术路线"仍应视为 `Medium` 的例外？
- [ ] `Reason` 是否有对内约定写法？

### B. Industry Fit 与行业清单 → `references/bdd-fit-rules.md`

- [ ] **目标市场行业清单**：哪些算 `Target` / `Adjacent` / `Outside`？（销售）
- [ ] 是否存在"必须拒绝"的行业？（销售）
- [ ] `Adjacent` 的判定边界如何界定？
- [ ] 行业名称以什么为准（国民经济行业分类？客户自述？经营范围表述）？

### C. 客户类型规则 → `references/customer-type-playbook.md` 末尾

- [ ] **六类**客户的判定信号是否准确？需增删什么？
- [ ] 是否需要第 7 类客户？
- [ ] 工程公司占业务比重约多少 %？是不是主要走量渠道？
- [ ] 设计院这一渠道目前重视程度如何？

### D. 废水特征识别 → `references/wastewater-signal-map.md` 第五节

- [ ] 实际遇到过的行业清单与识别关键词（销售）
- [ ] 客户描述中常见的废水特征关键词（销售）
- [ ] 每个特征对应的干扰因素类型（技术）
- [ ] 哪些数据属于"必需"、哪些属于"视情况"（技术 + 销售）

### E. 推荐联系岗位与接触战略 → `references/contact-role-map.md` 第六节

- [ ] 六类客户的岗位序列是否与实际接触经验一致？
- [ ] 终端业主中小民企是否确实可跳过中间层直达老板？
- [ ] 是否有其他常见岗位需补入（集团环保部、第三方运维方）？
- [ ] 允许的"公开来源"清单是否需要增删？
- [ ] **第四节接触战略矩阵是否符合实际打法？**

### F. 证据政策 → `references/evidence-policy.md` 第八节

- [ ] Demand Evidence 五级判据是否与实际一致？
- [ ] 环保处罚记录的时效窗口（现设 12 个月）是否合适？
- [ ] 是否需要增加其他硬信号来源（环保督查通报、行业黑名单）？
- [ ] **Commercial Risk 危险信号的 High / Medium 分级是否合适？**

### G. 必问参数与数据校验 → `references/must-ask-params.md` 第五节

- [ ] 5 项关键参数是否需要增删？
- [ ] 各客户类型必问清单是否需增删？
- [ ] 检测报告时效窗口（现设 6 个月）是否合适？
- [ ] 最小可接项目水量门槛：_______ m³/d
- [ ] 客户常见的数据提供形式（自述 / 报告 / 表格）

### H. 已归档内容配套确认（不在 Skill 内，仅记录）

以下项当前**不阻塞 Skill 运行**，待平台阶段处理：

- [ ] Technical Fit 阈值（7 项参数 + 否决条件）→ 技术
- [ ] Quotation Readiness 人工覆盖规则（哪些标准品可直接报价）→ 销售
- [ ] 资料开放三档清单（尤其哪些小试报告已脱敏）→ 销售
- [ ] 回复话术的署名落款与固定中英译法 → 销售

---

## 四、回测方案（校准完成后必做）

**用 3 个真实历史询盘回测，这是判断 Skill 是否可用的唯一标准。**

### ⚠️ 结果论已删除

**删除**了「成交 = 真项目 / 丢单 = 假项目」的判定逻辑。

- **Demand Evidence 的 Ground Truth 必须基于"当时可获得的证据"判断**，不能基于后来结果。
- **历史最终结果继续保留为 `Business Outcome`**，用于观察 Skill 的建议与后续实际发展的关系，**但不得反向作为真假项目标签**。

### 用例选择（必须包含这 3 种）

| 用例 | 选什么 | 观察重点 |
|---|---|---|
| **T1** | 一个当年证据充分、后来成交的询盘 | 证据链是否完整？Customer Type 是否正确？ |
| **T2** | 一个当年证据充分、后来未成交的询盘 | **不应因为"未成交"而被判低 Demand Evidence**；Commercial Risk 是否识别出真实风险？ |
| **T3** | 一个当年证据薄弱、判断困难的询盘 | 是否正确输出 `Unknown` / `Unverified`，而非硬猜？ |

**V1 Freeze 新增建议**：加 1 个 **T4 = 行业对口但不确定是否有生产活动的询盘**（如 API 企业），专门验证新增的 **BDD Relevance 8 项输入判定**是否阻断了"行业对口 → 相关性高"的误判。

### 判定标准（全过才算可用）

| # | 检查项 | 通过标准 |
|---|---|---|
| 1 | **Evidence 可溯源率** | FACT 中标注 Source 的比例 = **100%** |
| 2 | **Fact / Inference / Unknown 标注准确性** | 抽查全部条目，无错标、无混排 |
| 3 | **Company Verification** | 三态输出正确；名称有歧义时输出 `Unverified`，未选"最像的一家" |
| 4 | **Company Profile** | 查不到字段留 `Unknown`，未填"估计值" |
| 5 | **Customer Type** | 3/3（或 4/4）正确（或正确输出 `Unconfirmed`） |
| 6 | **Industry Fit** | 行业不在清单内时输出 `Unknown`，未凭常识推断 |
| 7 | **BDD Relevance** | ① 未出现 Industry Fit → BDD Relevance 直接推导<br>② 强制附注 Reason / Evidence / Confidence 齐全<br>③ 无废水信号 + 无环境证据时未超过 `Medium` |
| 8 | **Demand Evidence** | 基于当时证据可解释；未受 Business Outcome 影响 |
| 9 | **Commercial Risk** | 只用询盘当时可观察事实；未使用"是否成交" |
| 10 | **Missing Critical Data** | 能识别出当年实际遗漏的关键参数；未输出报价状态 |
| 11 | **Contact Strategy** | 岗位角色正确；未生成未经公开来源验证的具体人名 |
| 12 | **Recommended Next Action** | 与决策链末端一致，且指向可执行动作（含推进寄样） |
| 13 | **是否存在幻觉** | 无编造来源、无编造联系人、无编造参数 |
| 14 | 格式 | 主卡 1 屏内；`Unknown` 字段未被填充 |
| 15 | **越界检查** | 未出现 Technical Fit / Quotation Readiness / 回复草稿 / 跟进节奏 / 报价 / 设备选型 / 技术方案 |

### Business Outcome 记录格式（观察用，不参与判定）

```markdown
| 用例 | Business Outcome | 备注 |
|---|---|---|
| T1 | 成交 | — |
| T2 | 未成交 | 原因：客户改工艺路线（与 Skill 判断无关） |
| T3 | 未成交 | 原因：客户项目取消 |
| T4 | {结果} | BDD Relevance 判定是否被后续证实 |
```

**任一项不通过 → 回到校准清单改对应规则文件 → 重跑。**
规则改动不涉及主流程，改文字即可生效。

---

## 五、日常使用方式

```
场景 1：收到新询盘
  → 贴询盘原文 + 客户公司名，说"分析这个询盘"
  → 得到两层客户情报卡

场景 2：只有公司名（展会名片、陌生来电）
  → "帮我背调一下 XX 公司，我们做 BDD 电极的"
  → 得到主卡 + Evidence 附录

场景 3：判断该联系谁
  → "这个客户该找谁对接"
  → 得到 Recommended Contact Role（岗位级别，不生成人名）+ 接触战略

场景 4：不确定这客户有没有 BDD 机会
  → "这家公司值不值得投入"
  → 得到 BDD Relevance 四值 + Reason / Evidence / Confidence

场景 5：怀疑对方套方案
  → "这个客户一直在要工艺参数，风险高不高"
  → 得到 Commercial Risk 定级 + 危险信号依据
```

> **已移除场景**：客户催报价 → 报价判断不在本 Skill 范围（输出 Missing Critical Data 清单，报价由人工 / 商务系统处理）。

---

## 六、Skill 与平台的分工（重要，别混淆）

| | Skill（V1 已冻结） | 平台 |
|---|---|---|
| 管什么 | 客户背调 + 开发判断 | 案例库 + 设备计算 + 技术方案 |
| 技术判断 | ❌ 不做（Technical Fit 已归档） | ✅ 平台 L3 计算层 |
| 报价 | ❌ 不做 | ✅ 商务系统 |
| 有无状态 | 无状态，每次冷启动 | 有状态，持续积累 |
| 数据依赖 | 只依赖公开信息 | 依赖 Boromond 历史案例（**最大瓶颈**） |
| 建成时间 | **已完成，校准后即可用** | 3~4.5 个月 |
| 风险 | 低（内部参考） | 中（对外输出需谨慎） |

**为什么先做 Skill**：它不被"数据资产化"这个最大瓶颈卡住，能立刻见效。

**更重要的是**：Skill 的判定规则经回测证明准确后，**这些规则可以直接搬进平台的检索层与推理层**——一次投入，两处复用。

---

## 七、归档说明

**归档位置**：`D:/Case Flow/_bdd-skill-archive/V1.0-freeze/`（Skill 目录之外，不会被加载）

| 归档件 | 内容 | 回收条件 |
|---|---|---|
| `reply-playbook.md` | 8 场景话术 + 跟进节奏 Day 0~30 | 需要独立"回复执行" Skill 时 |
| `disclosure-policy.md` | 资料开放三档 + 应对话术 + 可交换原则 | 需对外发布"资料开放 SOP"时 |
| `bdd-fit-rules.technical.md` | Technical Fit 阈值 + 判定流程 | 技术确认阈值后 → 平台 L3 |
| `must-ask-params.quotation.md` | Quotation Readiness 四态 + 报价归属 | Skill 扩至商务流程 / 平台接商务系统时 |
| `customer-type-playbook.strategy-columns.md` | 决策周期 / 报价路径 / 资料开放 / 价格敏感度 | 平台 L4 需要销售策略输出时 |
| `output-card-template.appendix-B-C.md` | 附录 B 回复草稿 + 附录 C 推进节奏 | 恢复回复草稿输出时 |
| `*.pre-freeze.md`（6 个） | 冻结前全量快照 | 供 diff 对照 |

详见归档区 `README.md`。

---

## 八、已在 WorkBuddy 侧做的配套修改

- 原 `ai-inquiry-analysis`（泳具外贸专用）的 description 已限定为「仅限体育用品／游泳装备等消费品外贸」，并在正文顶部加了转向提示，**消除触发词冲突**。
- 该 Skill 的 Python 流程与产品库**未做任何改动**，原有用法不受影响。

---

## 九、V1 Freeze 边界声明（本轮刻意不做）

- ❌ Technical Fit（技术匹配度）判定
- ❌ 项目报价与报价条件判断
- ❌ 设备选型
- ❌ 小试技术方案
- ❌ 工程计算
- ❌ 正式技术方案
- ❌ 正式项目跟进流程
- ❌ 自动邮件 / 回复
- ❌ 案例数据库
- ❌ 复杂评分系统、100 分制客户评分
- ❌ 重构其他 WorkBuddy Skill

上述项均属**平台阶段或执行层**工作，与本 Skill 边界不重叠。

---

*最后更新：2026-09-26 · V1 Scope Frozen*
