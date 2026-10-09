# 已有能力与当前研究需要建立的新认识

[研究入口](../README.md) · 2026-10-10

近期原始工作已经提供联合生成、独立模态时钟、物理反馈学习、概念表示、层级探索与对称实现。四组研究从这些能力出发，进一步研究它们为何有效、何时失效和怎样形成可迁移的发现能力。

| 原始工作 | 已有能力 | 值得进一步回答的问题 |
|---|---|---|
| [OMatG](https://proceedings.mlr.press/v267/hollmer25a.html)、[MatterGen](https://www.nature.com/articles/s41586-025-08628-5) | 元素、坐标和晶格联合生成 | 有限信息与数据下，怎样学习化学—几何兼容关系？ |
| [MCFlow](https://proceedings.mlr.press/v306/seong26a.html)、[CrysBFN](https://arxiv.org/html/2502.02016v1) | 多模态条件生成；周期belief与精度条件 | 条件视图与实际信息状态怎样影响新组合形成？ |
| [Composable Crystals](https://arxiv.org/html/2605.14769v2)、[UFO-MGen](https://arxiv.org/html/2609.26547v1) | 局部concept组合；scaffold与连续实现 | 模型复用了什么知识，整体兼容需要什么共同条件？ |
| [PLaID++](https://proceedings.mlr.press/v306/xu26l.html) | 对称表示与偏好学习，稳定性和SUN变化受采样影响 | 学习目标、表示与多种成功的概率怎样相互作用？ |
| [ANCHOR](https://arxiv.org/html/2609.33407v1) | 组成搜索、历史新颖性与冻结CSP | 何时重新分配探索足够，何时需形成新的条件结构知识？ |
| [OMatG-IRL](https://proceedings.mlr.press/v306/hollmer26a.html)、[GSS](https://arxiv.org/html/2604.27636v1) | 物理反馈改变生成与结构搜索 | 反馈何时作用于仍能改变合格结果的选择？ |
| [CrystAF](https://arxiv.org/html/2609.36398v1)、[PackFlow](https://arxiv.org/html/2602.20140v1) | 分子晶体的后训练、修复与物理对齐 | 即时响应、完整后果与知识摊销怎样联系？ |
| [QD](https://arxiv.org/html/2403.03511)、[SHAFT](https://arxiv.org/html/2411.04323) | 多结果档案；层级奖励比例探索 | 未知合格集合怎样形成、学入并保持可获得？ |

表中工作覆盖无机DNG、CSP和分子packing，原任务与成功定义分别保留。四组全文提供具体阅读段落、竞争解释和新增科学命题；方法名称与当前提案的假设分开记录。

[四组深入分析](../programs/README.md) · [来源记录](../evidence/README.md) · [历史范围](../evidence/historical-evidence.md)
