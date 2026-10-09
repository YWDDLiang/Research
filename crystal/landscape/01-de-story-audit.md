# 已有能力与当前研究增量

[返回研究入口](../README.md) · 2026-10-09 · 研究设计，无新实验结果。

近期原始工作已经提供联合生成、独立模态时钟、物理奖励适配、概念表示和对称解码。研究增量应落到具体学习对象，而不是重新给这些能力命名。

| 已有工作 | 原文中的能力 | 对当前提案留下的问题 |
|---|---|---|
| [OMatG](https://proceedings.mlr.press/v267/hollmer25a.html)、[MatterGen](https://www.nature.com/articles/s41586-025-08628-5) | 元素、坐标和晶格联合生成 | 哪种具体化学修改需要哪种源相关几何补偿 |
| [MCFlow](https://proceedings.mlr.press/v306/seong26a.html) | 独立模态时间和any-to-any生成 | 新方法需超越时间轨迹选择，学习实际修订分布 |
| [ANCHOR](https://arxiv.org/html/2609.33407v1) | 冻结CSP，学习组成搜索及适应性新颖度 | 保留特定源结构是否优于相同组成下重新CSP |
| [CrystalFormer](https://github.com/deepmodeling/CrystalFormer)、[PLaID++](https://proceedings.mlr.press/v306/xu26l.html) | 真实站点交错／Wyckoff表示与后训练 | 科学信息如何绑定到具体周期对象并连续实现 |
| [CrystalREPA](https://arxiv.org/html/2605.08960v1)、[Composable Crystals](https://arxiv.org/html/2605.14769v1) | 物理特征迁移／局部概念组合 | 特征相似之外的对象关系执行与精细响应 |
| [OMatG-IRL](https://proceedings.mlr.press/v306/hollmer26a.html)、[OMatGRPO](https://arxiv.org/html/2610.03880v1) | 速度／物种通道的物理反馈学习 | 同样的计算怎样形成更有用的原生动作知识 |
| [CrystAF](https://arxiv.org/html/2609.36398v1)、[OMatG-flash](https://arxiv.org/html/2609.26402v1) | 物理后训练／少步全原子flow map | 丰富后果与动作学习的独立作用，以及无机DNG范围 |

OMatGRPO的奖励移植在Chemeleon2管线报告52/2500 strict SUN，原Chemeleon2为36/2500。这一作者实验使“同奖励、不同表示”的作用成为实质问题；单看其另一个稀疏SUN对比不能排除组成学习。

上述是文献事实及当前问题判断。新方案的效果尚未实验，具体版本、读取段落和释放入口保存在[来源索引](../evidence/README.md)。43篇旧卡保持首轮核查日期，作为历史资料，不混入本轮新核验数量。
