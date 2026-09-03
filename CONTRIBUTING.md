# Contributing

这个仓库用于积累**可审计的研究判断**，不是简单收藏链接。新增内容必须区分论文事实、本库推断、未验证假设和独立复现结果。

## 1. 内容类型

### Paper audit

位置：

```text
crystal/papers/<slug>.md
```

要求完成十二项论文审计，并更新：

- `crystal/README.md`
- `crystal/bibliography/papers.json`
- `crystal/bibliography/paper-index.csv`
- 相关 landscape/matrix（若判断发生变化）

### Direction audit

使用：

```text
templates/direction-audit-template.md
```

适用于一个大方向，而不是单篇论文。

### Experiment decision record

使用：

```text
templates/experiment-decision-template.md
```

每次实验只回答一个主要决策问题。

### Research idea

使用：

```text
templates/idea-falsification-template.md
```

Idea 进入执行前必须包含危险基线、杀手实验和停止条件。

---

## 2. 新增论文流程

### Step 1：核验一手来源

优先级：

1. 正式论文页；
2. arXiv/OpenReview/会议页面；
3. 官方/作者仓库；
4. 官方数据/模型卡。

媒体和二手博客只能作为线索。

### Step 2：锁定版本

记录：

- 论文版本和日期；
- 代码 commit/release；
- 数据版本；
- evaluator 版本；
- 最后核验日期。

2026 等近期预印本的标题、数据规模和结果可能更新。

### Step 3：生成模板

```bash
python scripts/new_paper.py \
  --slug example-paper \
  --title "Example Paper" \
  --year 2026 \
  --venue "arXiv preprint" \
  --paper-url "https://..."
```

### Step 4：完成十二项审计

不能只改元数据。至少填写：

- scientific problem；
- mathematical task；
- data-generating process；
- core mechanism；
- claim–evidence alignment；
- hidden assumptions；
- strongest alternative explanation；
- missing baseline；
- killer experiment；
- contribution type；
- transferable abstraction；
- final verdict。

### Step 5：更新机器可读索引

`papers.json` 是结构化 source of truth。  
所有 URL、报告路径和六维评分必须同步。

### Step 6：运行检查

```bash
python scripts/validate_repo.py
```

---

## 3. 审计深度

每篇报告应标记当前深度：

| 等级 | 内容 |
|---|---|
| L0 metadata | 只核验题目、摘要、页面和项目；不能称“已审计” |
| L1 full-paper audit | 阅读全文并完成十二项报告 |
| L2 code audit | 阅读官方实现、配置、数据与 evaluator |
| L3 reproduction | 独立运行核心结果与危险基线 |
| L4 prospective validation | 新数据、DFT 或实验盲测 |

初版报告可以是 L1 前的结构化首轮审计，但必须明确未复现，不得用“已证明”。

---

## 4. 写作规则

### 分开三种陈述

**论文事实：**

> 论文在给定设置下报告某结果。

**本库推断：**

> 本库判断该增益可能来自某机制。

**待验证假设：**

> 若干预实验成立，才可支持该机制。

不要把三者合成一句话。

### 避免模糊词

尽量不用：

- “真正理解”
- “物理感知”
- “智能搜索”
- “显著更好”
- “首次”
- “通用”
- “可合成”

除非后面紧跟操作定义和证据。

### 评价论文而非作者

“故事型”描述贡献结构，不评判作者动机。  
审计应针对问题、假设、实验和结论。

---

## 5. 六维贡献评分

\[
\Delta =
(\Delta P,\Delta I,\Delta O,\Delta C,\Delta E,\Delta K)
\]

评分必须附理由：

- 0：基本未改变；
- 1：明显推进；
- 2：实质改变领域坐标系或能力。

不要以总分替代文字判断。

---

## 6. 最危险基线原则

优先加入能够用更简单机制解释结果的基线：

- 检索；
- 规则；
- 原型/元素替换；
- 小模型；
- 随机；
- best-of-\(N\)；
- rejection sampling；
- 更多数据；
- 更多计算；
- 相同后处理。

弱基线不会使论文更强，只会使 claim 更脆弱。

---

## 7. Killer experiment 原则

一个合格的杀手实验应：

- 只改变核心机制；
- 控制数据、参数、采样和 oracle 预算；
- 预先定义支持与反证结果；
- 能在完整训练前以较低成本运行；
- 失败后触发停止、简化或收窄。

---

## 8. 链接与项目状态

- `project_url` 只填已核验的官方/作者项目；
- 未找到时留空，并写“尚未核验到”；
- 不把社区复现误写成官方代码；
- 仓库动态状态以最后核验日期为准；
- 不直接纳入第三方代码副本，优先记录 URL、commit 和 license。

---

## 9. Pull request / commit checklist

- [ ] 问题定义清楚；
- [ ] 输入、输出、目标和预算清楚；
- [ ] 数据来源与缺失信息清楚；
- [ ] 作者 claim 和本库判断分开；
- [ ] 有危险基线；
- [ ] 有杀手实验；
- [ ] 有不可支持的 claim；
- [ ] 有适用边界；
- [ ] 项目地址已核验或明确留空；
- [ ] 主索引、JSON、CSV 与报告一致；
- [ ] `validate_repo.py` 通过；
- [ ] 更新日志包含日期和判断变化。

---

## 10. 更新已有判断

新论文、复现或实验推翻旧判断时，不要静默覆盖。报告中追加：

```text
Date:
Previous judgment:
New evidence:
New judgment:
Why it changed:
Remaining uncertainty:
```

这个仓库最重要的资产不是“永远正确”，而是可追踪地记录证据如何改变研究判断。
