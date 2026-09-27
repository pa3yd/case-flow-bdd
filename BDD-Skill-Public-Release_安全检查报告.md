# BDD Customer Intelligence Skill · Public 发布安全检查报告

| 项 | 值 |
|---|---|
| 报告时间 | 2026-09-27 |
| Public 目录 | `D:/bdd-customer-intelligence-skill/` |
| Public 仓库名 | `bdd-customer-intelligence-skill`（Public） |
| Private 仓库 | `case-flow-bdd`（**保持 Private，未改动、未公开**） |
| 当前状态 | **文件整理完成 · 安全检查通过 · 尚未 Push，等待确认** |

---

## 结论

**安全检查通过。** Public 目录已满足全部禁止项要求：

- 客户名称 / 厂区 / 人名 **0 残留**
- 邮箱 / API Key / Token / 凭据 **0 残留**
- 客户 PDF / 客户 MD / 情报卡 / Patch 报告 / 归档目录 / memory / 实施计划 **全部为 0 个文件**
- Private 仓库 Git 历史 **未复制** —— Public 目录为全新 `git init`，无任何 commit、无 remote
- Private 侧 15 个 Skill 文件 **md5 全部一致**，确认本次操作未触碰 Private

**唯一未处理项**：Skill 文档中仍保留约 60 处 `Patch` 字样（规则版本说明，不含客户信息）。详见第四节。

---

## 一、准备公开的完整文件清单

**共 18 个文件。**

### 1.1 Skill 本体（15 个 · 运行必需）

| # | 路径 | 作用 |
|---|---|---|
| 1 | `SKILL.md` | 主文件：决策链 + 硬性约束 + 14 步工作流 + 默认调用协议 |
| 2 | `references/bdd-fit-rules.md` | Industry Fit 判定 + 目标市场地图 + T3 证据门槛 |
| 3 | `references/bdd-relevance-rules.md` | BDD Relevance 判定 + 两个 Gate |
| 4 | `references/customer-type-playbook.md` | 客户类型六分类 + 双路径分流 |
| 5 | `references/current-treatment-rules.md` | 现有处理方案 / 技术组合提取 |
| 6 | `references/opportunity-type-rules.md` | Opportunity Type 五值 + Priority Site |
| 7 | `references/evidence-policy.md` | 证据政策 + Demand Status + Financial Warning 白名单 + Business Change Signal |
| 8 | `references/sales-conclusion-rules.md` | Sales Conclusion 五值判定 |
| 9 | `references/lead-signals.md` | 外部信号检索规则 |
| 10 | `references/wastewater-signal-map.md` | 行业 → 废水特征关键词表 |
| 11 | `references/must-ask-params.md` | 必问参数清单 + 三级优先级 |
| 12 | `references/contact-role-map.md` | 联系角色映射 |
| 13 | `references/output-visual-rules.md` | 颜色语义 + 展示层 + 交付边界 + PDF 三页模板 |
| 14 | `assets/output-card-template.md` | 输出模板（13 字段主卡 + 附录 A/B） |
| 15 | `scripts/render_pdf.py` | 渲染层（MD → HTML → PDF，Chrome headless） |

### 1.2 新增文件（3 个）

| # | 路径 | 说明 |
|---|---|---|
| 16 | `README.md` | **面向同事新写**，7 章：是什么 / 适合什么场景 / 如何安装 / 如何调用 / 输出什么 / 如何更新 / 数据安全 |
| 17 | `.gitignore` | 仅排 Python 缓存、系统垃圾、临时文件、密钥类 |
| 18 | `LICENSE` | **内部使用声明**（非开源许可）—— 见第五节待确认项 |

---

## 二、安全检查结果

| # | 检查项 | 方法 | 结果 |
|---|---|---|---|
| 1 | 已跑客户公司名 | 逐个 grep 13 家 + 竞品 | **PASS · 0 命中** |
| 2 | 真实厂区名 | grep Tarapur / Vapi / Hoboken / Kokkola / Nysa / Olen / Brugge | **PASS · 0 命中** |
| 3 | 真人姓名 | grep Shyam Dhekekar / Scharpwinkel 等 | **PASS · 0 命中** |
| 4 | 邮箱地址 | 正则全文扫描 | **PASS · 0 命中** |
| 5 | API Key / Token / 凭据 | grep api_key / ghp_ / AKIA / sk- / Bearer | **PASS · 0 命中** |
| 6 | 私有工作区路径 | grep `Case Flow` | **PASS · 0 命中** |
| 7 | 归档目录引用 | grep `_bdd-skill-archive` / `_v111` / `_v112` / `_v113` | **PASS · 0 命中** |
| 8 | 客户数据类数字 | grep 「N 座 ZLD」「N 个制造基地」「€金额」「万 m³」 | **PASS · 0 命中** |
| 9 | PDF 文件 | find `*.pdf` | **PASS · 0 个** |
| 10 | 客户情报卡 | find `*_BDD_Intelligence_*` / `客户情报卡*` | **PASS · 0 个** |
| 11 | memory 目录 | find `*/.workbuddy/*` | **PASS · 0 个** |
| 12 | 实施计划 / 优化方案 | find `*实施计划*` / `*优化方案*` | **PASS · 0 个** |
| 13 | Patch 测试报告 | find `*Patch*报告*` | **PASS · 0 个** |
| 14 | Private Git 历史 | `git log` / `git remote -v` | **PASS · 无 commit、无 remote** |
| 15 | Private 仓库受影响 | md5 对比 15 个 Skill 文件 | **PASS · 15/15 一致** |
| 16 | Private 仓库工作区 | `git status --short` | **PASS · 0 修改 / 0 未跟踪** |

---

## 三、脱敏改动明细

**11 个文件被改写（4 个文件未动**：`contact-role-map.md`、`must-ask-params.md`、`wastewater-signal-map.md`、`render_pdf.py`**）。**

改动原则：**只替换「具体主体」为「类型化描述」或「占位符」，不改动任何判定逻辑、阈值、规则结构与字段定义。**

### 3.1 `assets/output-card-template.md`（最严重 · 差异 26 行）

模板里原本嵌着一张**真实客户情报卡**，已整块替换为虚构示例。

| 原文 | 改为 |
|---|---|
| `# Aarti Industries · BDD Customer Intelligence` | `# Sample Chemicals · BDD Customer Intelligence` |
| `AARTI INDUSTRIES LTD（印度）· Verified` | `SAMPLE CHEMICALS LTD（示例国）· Verified` |
| `印度 · 古吉拉特邦 Vapi 注册，孟买总部` | `示例国 · 某州注册，总部位于某市` |
| `16 个制造基地，出口占一半以上` | `多个制造基地，出口占比较高` |
| `Tarapur（印度 · 马哈拉施特拉邦）` | `` `<厂区名>`（示例国 · 某州） `` |
| **`Shyam Dhekekar｜Chief Technical and Sustainability Officer`**（真人姓名） | `` `<岗位名称>`｜Source: 官网 `` |
| `8 座厂区已 ZLD、3 座 ZLD-ready` | `部分厂区已 ZLD、其余在推进` |
| `硝化/氯化/加氢等工艺段` | `主导工艺段` |
| `2026-09-26` / `V1.1.3` | `YYYY-MM-DD` / `<当前版本>` |

**新增**：示例块前加「以下为虚构示例」声明；联系人处**新增人员来源纪律**（人名仅可来自官网 / 政府公示 / 招投标 / 上市公告 / 官方媒体，第三方聚合站一律弃用）。

### 3.2 `SKILL.md`（差异 20 行）

| 位置 | 原文 | 改为 |
|---|---|---|
| 默认调用协议示例 | `背调 GEA Group，gea.com` | `背调 <公司全称>，<官网域名>` |
| 变更归档 ×3 | `D:/Case Flow/_bdd-skill-archive/…` | `内部工作区归档区（不随本分发版发布）` |
| TBD 第 23 项 | `（Festo / GEA 等曾按旧口径判 Target）` | `（部分历史主体曾按旧口径判 Target）` |
| TBD 第 24 项 | `（EnviroChemie 案例）` | 删除 |
| TBD 第 26 项 | `（三例同时重算：Veolia / GEA / EnviroChemie…）` | `（多例同时重算后机会档位普遍下降）` |

### 3.3 其余 9 个 references 文件（差异 52 行）

| 文件 | 改动要点 |
|---|---|
| `bdd-fit-rules.md` | 删除「（Chemstock）」标注 |
| `bdd-relevance-rules.md` | 删除「Hikal / Aarti / Umicore / EnviroChemie」四家名；`GEA 与 Veolia 两个真实案例` → `多个大型水处理 EPC 案例`；`Umicore 型主体` → `多厂区电池材料制造集团型主体`；TBD 表去公司名 |
| `current-treatment-rules.md` | `Aarti 已建 8 座 ZLD` → `已建多座 ZLD 的制造集团`；`EnviroChemie 的技术组合` → `EPC / 集成商的技术组合` |
| `customer-type-playbook.md` | `EnviroChemie 这类` → `EPC / 集成商这类`；删除「（Chemstock 回归重点）」 |
| `evidence-policy.md` | 删除「（BASF 集团、GEA Group）」 |
| `lead-signals.md` | `Hoboken 厂排放量` → `单个厂区排放量`；`Aarti Industries / Aarti Drugs / Aarti Pharmalabs` → `XX 工业 / XX 制药 / XX 医药` |
| `opportunity-type-rules.md` | `EnviroChemie 型主体` → `EPC 兼自有工艺线型主体`；`Umicore 型示例` → `多厂区制造集团型示例`；示例厂区 `Hoboken / Olen / Brugge / Kokkola / Nysa` → 占位符；`€4 亿湿法冶金装置` → `大型装置` |
| `output-visual-rules.md` | Evidence Card 示例里去 `Hoboken`；文件名示例 → `AcmeChemicals` / `AcmeEPC`；去掉 `D:/Case Flow/` 绝对路径 |
| `sales-conclusion-rules.md` | 删除「由 5 家公司回归测试发现并修正 —— EnviroChemie 案例」；示例标题去 `Chemstock 型` / `Umicore 型` |

---

## 四、未处理事项（供你决定）

### 4.1 `Patch` 字样（约 60 处）

分布：`SKILL.md` 24 · `bdd-relevance-rules.md` 15 · `evidence-policy.md` 4 · `bdd-fit-rules.md` 4 · `render_pdf.py` 3 · 其余 5 文件各 1~2。

**性质**：全部是**规则版本的说明**，例如「Patch A 已收紧 T3」「FW Rule Patch 重定义触发条件」「本 Patch 不改 Opportunity Type 五值」。

**判断**：不含任何客户信息，也**不是** Patch 测试报告文件。保留有助于理解每条规则的由来。

**选项**：
- **A（默认·已采用）** 保留 —— 保持规则溯源完整，同事能看懂"这条为什么这样定"
- **B** 统一替换为中性词（如 `Patch` → `规则修订`）—— 更贴近业务读者，但需再改 60 处
- **C** 整段删除所有版本沿革说明 —— 文档最干净，但会丢失"规则由来"，不建议

### 4.2 `_*-comparison/` `_*-preview/` 通配符（3 处）

这是**临时目录的命名规范**（告诉使用者"这类目录是内部渲染产物，不进交付"），不是具体目录名。已保留。

---

## 五、待你确认的 3 项

| # | 事项 | 我的默认处理 | 需要你确认 |
|---|---|---|---|
| 1 | `LICENSE` 内容 | 已写**内部使用声明**（非开源，禁止再分发） | 是否符合预期？若希望开源（如 MIT），请告知 |
| 2 | `Patch` 字样 | 保留（第四节选项 A） | 是否要改为选项 B / C |
| 3 | `README.md` 中仓库 address 占位 | 写为 `<仓库地址>` | Push 后可回填真实地址 |

---

## 六、确认后的发布步骤

**当前 Public 目录状态**：18 个文件已暂存，无 commit、无 remote，**未 Push**。

```powershell
cd "D:/bdd-customer-intelligence-skill"

# 1) 提交（Git 身份若已配置则直接执行）
git commit -m "Initial release: BDD Customer Intelligence Skill V1.1.3"

# 2) 关联远程仓库（在 GitHub 网页新建 Public 仓库 bdd-customer-intelligence-skill）
git remote add origin https://github.com/<你的用户名>/bdd-customer-intelligence-skill.git

# 3) 推送
git push -u origin main
```

> **注意**：`case-flow-bdd` 保持 Private 不变；两个仓库相互独立，Public 不含 Private 的任何历史。

---

*报告结束 · 等待确认后再执行 Push*
