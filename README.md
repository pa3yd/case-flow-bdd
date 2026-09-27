# BDD Customer Intelligence · Boromond 波乐美

> BDD（掺硼金刚石）电极 · 电化学氧化工业废水处理业务的**客户情报与企业背调工具**。
> 本仓库是私人工作备份：Skill 本体 + 实跑交付物 + 版本归档 + 改造报告。

**仓库性质：Private 私有** —— 内含客户情报、联系人岗位与业务判定方法，**禁止公开**。

---

## 章节导航

| 章节 | 你会用到它的场景 |
|---|---|
| 一 | 这个仓库装了什么（目录说明） |
| **二** | **首次上传到 GitHub** —— 在本机操作，只剩 3 步 |
| **三** | **换电脑复现** —— 明天到公司电脑，照做 5 步 |
| 四 | 日常工作流（改完 Skill 后怎么同步） |
| 五 | 环境要求 |
| 六 | 保密与安全约定 |
| 七 | 故障排查 |

---

## 一、这个仓库装了什么

```
D:\Case Flow\
│
├── skill\bdd-inquiry-analyzer\      ★ 核心：Skill 本体（15 个文件）
│   ├── SKILL.md                        主文件：决策链 + 硬性约束 + 工作流
│   ├── references\                     12 个判定规则文件
│   ├── assets\output-card-template.md  输出模板（13 字段主卡 + 附录 A/B）
│   └── scripts\render_pdf.py           零依赖 MD→HTML→PDF 渲染器
│
├── tools\                           ★ 自动化脚本（本仓库专用）
│   ├── restore-skill.ps1               仓库 → 本机 WorkBuddy（部署）
│   ├── sync-skill.ps1                  本机 WorkBuddy → 仓库（回同步）
│   └── verify-project.ps1              环境体检（只读，不改任何文件）
│
├── *_BDD_Intelligence_*.md / .pdf   客户情报交付物（md + 3 页 PDF）
├── 客户情报卡_*.md                  V1 时代的旧版交付物（存档用）
│
├── BDD-Skill-*_报告.md             各次 Patch 的改造报告
├── BDD-Skill-V1.1_优化方案与执行计划.md
├── BDD询盘Skill_校准清单与回测方案.md
├── 波乐美水质方案智能平台_实施计划.md
│
├── _bdd-skill-archive\             ★ 版本归档（9 个版本快照，不参与运行）
├── _v111-comparison\ 等 6 个目录     改造过程中的预览图与对比产物
│
└── .workbuddy\memory\              项目长期记忆（MEMORY.md + 每日日志）
```

### 为什么 Skill 要放两份？

WorkBuddy **只从 `%USERPROFILE%\.workbuddy\skills\` 读取 Skill**，它不会去读你的项目文件夹。
所以：

- `D:\Case Flow\skill\` = **受 Git 管理的正本**（能上传、能回溯版本）
- `C:\Users\<你>\.workbuddy\skills\` = **WorkBuddy 实际运行的副本**

两者用 `tools\` 下的脚本**双向同步**，MD5 逐文件校验，不会出现"改了没生效"。

---

## 二、首次上传到 GitHub（在本机操作）

> 仓库已经建好了（`git init`、`.gitignore`、`.gitattributes` 均已完成，228 个文件已暂存）。
> 你只剩下面 3 步。

### 第 1 步：填写 Git 身份（一次性）

打开 **PowerShell**，逐行执行：

```powershell
git config --global user.name  "你的名字或GitHub用户名"
git config --global user.email "你的邮箱"
```

> 建议用 GitHub 账号邮箱；不想暴露真实邮箱就用 GitHub 提供的
> `<用户名>@users.noreply.github.com` 形式。

### 第 2 步：在 GitHub 网页建一个**私有**空仓库

1. 浏览器打开 <https://github.com/new>
2. **Repository name**：`case-flow-bdd`（名字随意）
3. **Visibility**：选 **Private** ← 这一项选错无法挽回，务必确认
4. **不要**勾选 `Add a README file` / `.gitignore` / `license`（会与本地冲突）
5. 点 **Create repository**，然后停在页面上，复制 https 地址备用

### 第 3 步：提交并推送

回到 PowerShell（把地址替换成你自己的）：

```powershell
cd "D:\Case Flow"

git commit -m "chore: initial commit - BDD Customer Intelligence V1.1.3"

git remote add origin https://github.com/你的用户名/case-flow-bdd.git

git push -u origin main
```

**第一次 push 会弹窗要求登录 GitHub**（Git Credential Manager）——
选 `Sign in with your browser`，浏览器里授权一次即可，之后不用再输。

看到类似 `branch 'main' set up to track 'origin/main'` 就是成功了。

### 验证

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\verify-project.ps1
```

`git remote` 那行从 `WARN` 变成 `PASS` 即表示已连上远程仓库。

---

## 三、换电脑复现（公司电脑，5 步）

> 目标：把 Skill 装好、能跑通一次背调。
> 全程不需要管理员权限（装软件那一步除外）。

### 第 1 步：装三个软件

| 软件 | 下载地址 | 说明 |
|---|---|---|
| **Git for Windows** | <https://git-scm.com/download/win> | 一路默认安装即可 |
| **WorkBuddy** | 按公司统一渠道安装 | 自带 Python，Skill 的运行宿主 |
| **Google Chrome** | <https://www.google.com/chrome/> | 生成 PDF 用；有 Edge 也行 |

### 第 2 步：克隆仓库

打开 PowerShell：

```powershell
cd D:\
git clone https://github.com/你的用户名/case-flow-bdd.git "D:\Case Flow"
```

私有仓库同样会弹窗登录，选浏览器授权。

> 如果 `D:\Case Flow` 已存在，改成别的目录名，例如 `D:\Case Flow-work`。

### 第 3 步：把 Skill 部署到本机 WorkBuddy

```powershell
cd "D:\Case Flow"
powershell -ExecutionPolicy Bypass -File .\tools\restore-skill.ps1
```

脚本会：备份已有的同名 Skill → 复制 15 个文件 → 逐个 MD5 校验。
看到 `PASS  15/15 files verified` 才算合格。

### 第 4 步：环境体检

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\verify-project.ps1
```

期望结果：**FAIL = 0**。
`WARN` 项不影响使用（例如没装 python 只影响手动重渲染 PDF）。

### 第 5 步：在 WorkBuddy 里实测

1. **重启 WorkBuddy**（让它重新扫描 skills 目录，这步不能省）
2. 新建对话，直接说：

   > 背调 Veolia Water Technologies，veoliawatertechnologies.com

3. 确认它自动触发 `bdd-inquiry-analyzer`，并输出 13 字段情报卡 + PDF

跑通即代表迁移成功。之后可对照根目录的 `VeoliaWaterTechnologies_BDD_Intelligence_2026-09-27.pdf` 检查格式是否一致。

---

## 四、日常工作流

### 场景 A：只是看看 / 交付客户卡

不用做任何事，直接读根目录的 `.md` 与 `.pdf` 即可。

### 场景 B：改了 Skill 的判定规则

```powershell
cd "D:\Case Flow"

# 1) 把本机改好的 Skill 同步回仓库（含差异清单 + MD5 校验）
powershell -ExecutionPolicy Bypass -File .\tools\sync-skill.ps1

# 2) 提交并推送
git add -A
git commit -m "skill: 说明这次改了什么"
git push
```

### 场景 C：在另一台电脑拉了新版本

```powershell
cd "D:\Case Flow"
git pull

# 把新版本重新部署到本机 WorkBuddy
powershell -ExecutionPolicy Bypass -File .\tools\restore-skill.ps1
```

> **铁律**：只要 `git pull` 了新版本，就必须再跑一次 `restore-skill.ps1`。
> 否则 WorkBuddy 跑的还是旧 Skill —— 这是最容易踩的坑。

### 场景 D：想回退到某个历史版本

归档在 `_bdd-skill-archive\`，每个子目录是一份完整快照：

```powershell
# 例如回退到 V1.1.3-backup-20260927-c
$src = "D:\Case Flow\_bdd-skill-archive\V1.1.3-backup-20260927-c"
$dst = "$env:USERPROFILE\.workbuddy\skills\bdd-inquiry-analyzer"
Copy-Item $src $dst -Recurse -Force
```

---

## 五、环境要求

| 项 | 要求 | 备注 |
|---|---|---|
| 操作系统 | Windows 10 / 11 | 本仓库按 Windows 维护 |
| Git | 2.28+ | 需要 `git init -b` 支持 |
| WorkBuddy | 已安装并登录 | Skill 的运行宿主，自带 Python |
| Chrome 或 Edge | 任一 | 渲染 PDF 用，`render_pdf.py` 会自动探测路径 |
| Python | 3.10+ | **可选** —— 仅手动重渲染 PDF 时需要 |
| 磁盘 | ≥ 100 MB | 仓库约 16 MB |

`render_pdf.py` 的浏览器路径是**自动探测**的（覆盖 Chrome/Edge 的 5 个常见安装位置，
以及 Linux/macOS 路径），换电脑**无需修改任何代码**。

---

## 六、保密与安全约定

1. **仓库必须保持 Private。**
   客户情报卡含客户名称、厂区、联系人岗位与商业判断，属公司业务资料。

2. **不要把 `origin` 改成公开仓库地址。**
   一旦公开推送，Git 历史会被爬虫抓取，事后转私有也**无法收回已抓取的内容**。

3. **密钥类文件永不入库**（`.gitignore` 已做兜底拦截）：
   `config.json` / `.env` / `*.key` / `*.pem` / `secrets.json` / `credentials.json`
   —— 如果将来有人要往这个仓库加 API Key，先停下来。

4. **公司电脑的合规提醒：**
   若公司设备管理政策不允许将业务资料同步到个人 GitHub 账号，
   请改用公司内部代码托管（如 GitLab / 内网共享盘）。
   **上传前建议先跟主管确认一次。**

5. **PDF 与 PNG 已在 `.gitattributes` 中标记为 binary**，
   Git 不会改写其换行符，跨机器克隆不会损坏文件。

---

## 七、故障排查

### Q1：`git push` 报 403 / Authentication failed

凭据过期或权限不足。清理后重新登录：

```powershell
git credential-manager erase
# 或直接改用 Personal Access Token 作为密码
```

### Q2：公司网络访问不了 GitHub

按顺序尝试：

1. 换用手机热点验证是否为网络策略问题
2. 配置公司代理：
   ```powershell
   git config --global http.proxy http://代理地址:端口
   git config --global https.proxy http://代理地址:端口
   ```
3. 走公司内部托管（GitLab / 内网盘），把本地仓库打包带走：
   ```powershell
   # 本机
   git bundle create bdd-backup.bundle --all
   # 目标机
   git clone bdd-backup.bundle "D:\Case Flow"
   ```
   `git bundle` 会把**全部提交历史**打成一个文件，是断网环境最可靠的搬运方式。

### Q3：WorkBuddy 里不触发这个 Skill

依次检查：

1. 文件真的在不在：`%USERPROFILE%\.workbuddy\skills\bdd-inquiry-analyzer\SKILL.md`
2. 跑一遍 `tools\verify-project.ps1`，看 `skill (local)` 是否为 PASS
3. **重启 WorkBuddy** —— 它只在启动时扫描 skills 目录
4. 确认没和另一个 Skill（`ai-inquiry-analysis`，泳具外贸专用）混淆

### Q4：`powershell 无法加载文件，因为在此系统上禁止运行脚本`

这是执行策略限制。用带 `-ExecutionPolicy Bypass` 的方式调用：

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\restore-skill.ps1
```

只有在**公司组策略锁死**执行策略、连 Bypass 都无效时，才需要联系 IT。

### Q5：`sync-skill.ps1` 说所有文件都 MODIFIED，但没改过任何东西

说明本机 Skill 与仓库副本换行符不一致（CRLF vs LF）。
本地已设 `core.autocrlf=false` 应当避免此问题；若仍出现，执行：

```powershell
git config core.autocrlf false
git rm -r --cached . ; git add -A
```

### Q6：`git status` 里中文文件名显示成 `\346\226\207...`

本地已设 `core.quotepath=false`。若在新机器上复现：

```powershell
git config --global core.quotepath false
```

---

*Skill 当前版本：V1.1.3（含 BDD-Specific Relevance Gate + Partner Cooperation Evidence Gate）*
*文件总数：15（SKILL.md + 12 references + 1 asset + 1 script）*
