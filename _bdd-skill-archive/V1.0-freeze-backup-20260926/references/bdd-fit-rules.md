# Industry Fit 判定规则

**回答的问题**：这个**行业**是否属于 Boromond 目标市场？

**数据要求**：仅需行业名称，**不需要水质数据**。

> **V1 冻结变化**：本文件原含 Technical Fit 判定规则（阈值 / 否决条件 / 判定流程），已移出 Skill → 归档至
> `D:/Case Flow/_bdd-skill-archive/V1.0-freeze/bdd-fit-rules.technical.md`
> 原因：Technical Fit 属工程计算基础，超出「BDD 客户完整企业背调 + 客户开发判断」范围。

---

## 一、取值定义

| 取值 | 含义 |
|---|---|
| `Target` | 属于 Boromond 核心目标市场行业 |
| `Adjacent` | 非核心，但存在可迁移的应用场景 |
| `Outside` | 明确不在目标市场 |
| `Unknown` | 行业不在下方清单内，或行业无法确认 |

---

## 二、目标市场行业清单

> 【待填】由 Boromond 销售/技术确认，将行业分入三档。
> **填写前，所有行业一律输出 `Unknown`。**

| 档位 | 行业 |
|---|---|
| `Target` | 【待填】 |
| `Adjacent` | 【待填】 |
| `Outside` | 【待填】 |

---

## 三、硬规则

| # | 规则 |
|---|---|
| 1 | 行业不在清单内 → **`Unknown`**，不得凭常识推断。 |
| 2 | **Industry Fit = High（Target）不得推导 BDD Relevance = High。** 它只是 BDD Relevance 的 8 项输入之一。 |
| 3 | Industry Fit 描述的是**行业属性**，与具体客户的采购需求无关。 |
| 4 | 同一行业的所有公司，Industry Fit 取值相同——**这是它与 BDD Relevance 的根本区别**。 |
| 5 | Industry Fit 高不得推导 Demand Evidence 高。行业对口不代表这家公司真有项目。 |

> 完整推导禁令见 `bdd-relevance-rules.md` 第五节与 `SKILL.md` 第三节。

---

## 四、待确认问题

- [ ] 核心目标市场行业的定义标准是什么？（按废水类型？按行业门类？按项目规模？）
- [ ] 是否存在"必须拒绝"的行业（安全 / 合规 / 成本原因）？
- [ ] `Adjacent` 的判定边界如何界定？
- [ ] 行业名称以什么为准（国民经济行业分类？客户自述？经营范围表述）？

---

## 五、与其他文件的职责边界

| 文件 | 负责 |
|---|---|
| **本文件** | Industry Fit 判定（行业 → 四值） |
| `bdd-relevance-rules.md` | BDD Relevance 判定（8 项输入 → 四值 + 强制附注） |
| `wastewater-signal-map.md` | 从询盘文字识别行业与废水信号 |
| `lead-signals.md` | 从外部来源检索证据 |
| `evidence-policy.md` | 决定标注 FACT / INFERENCE / UNKNOWN |

**本文件不做任何技术判断，不输出任何技术参数与数值区间。**

---

## 六、待校准项

| # | 待填内容 | 归属 | 阻塞影响 |
|---|---|---|---|
| 1 | 目标市场行业清单（Target / Adjacent / Outside） | 销售 | `Industry Fit` 全部输出 `Unknown` |
| 2 | 是否存在"必须拒绝"的行业 | 销售 | 无筛除能力 |
| 3 | `Adjacent` 边界标准 | 销售 | 判定粒度 |
