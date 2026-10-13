# 晶体生成：数据、模型与验证

面向AI研究者的30页补充汇报，2026年10月13日。与《晶体生成研究演化》配合使用，也可独立用于领域入门。先讲生成对象、数据集、模型和评价方法，再用五页详细说明MatterGen如何把这些环节连接起来。

- [可编辑PowerPoint](crystal-domain-primer-mattergen.pptx)
- [PDF阅读版](crystal-domain-primer-mattergen.pdf)
- [逐页讲稿、计算说明与文献](primer-notes.md)
- [完整来源索引](references.json)

| 页码 | 内容 |
|---|---|
| 1–4 | 周期结构表示、等价编码、CSP、自主生成和条件生成 |
| 5–7 | 数据库与训练集；MP-20、MPTS-52等基准；终态数据与势能轨迹 |
| 8–11 | Diffusion、Flow/SI、LLM及对称模型；MLIP的角色；计算流程与费用 |
| 12–18 | Validity、匹配率、RMSD、分布指标、形成能、凸包、S/U/N/SUN及算例 |
| 19–22 | DFT、结构弛豫、MLIP能量口径、声子、弹性、MD、NEB与实验测量 |
| 23 | MatterGen 1/5：问题、训练数据、竞争相与新颖性参考 |
| 24 | MatterGen 2/5：元素、坐标、晶胞的联合扩散和条件适配 |
| 25 | MatterGen 3/5：同训练数据下的DFT评测、SUN与弛豫位移 |
| 26 | MatterGen 4/5：性质条件、标签来源、预算与合格候选数量 |
| 27 | MatterGen 5/5：筛选、合成、结构表征与模量测量 |
| 28–29 | NMI及相关期刊案例：Chemeleon2、CHGNet、M3GNet、SCIGEN、Chemeleon、SLICES、CrystaLLM |
| 30 | 阅读与复现来源 |

MatterGen发表于Nature主刊。五页内容以正式论文及补充材料为依据，代码版本中的默认评价方式另列于讲稿。第27页区分原文的目标值、DFT计算值、实验换算值，并记录2026年Materials Horizons后续研究对产物身份及新颖性的再分析。

周期坐标、凸包和SUN漏斗中的教学数据为人为构造；MatterGen结果图保留论文的数据、阈值与计算范围。表格和五个数据图均为PowerPoint原生对象，可以编辑。MatterGen Fig. 1与Fig. 6采用原文图片，注明CC BY 4.0许可与来源。逐页备注包含文献、方法细节和适合口头展开的说明。
