---
title: "Are Crystal Generative Models Truly Discovering Novel Structures?"
slug: "substitution-novelty"
year: 2026
venue: "arXiv preprint"
category: "evaluation"
audit_role: "新颖性审计 / 替换派生"
paper_url: "https://arxiv.org/abs/2606.23166"
project_url: ""
last_verified: "2026-09-03"
---

# Are Crystal Generative Models Truly Discovering Novel Structures?

> 历史首轮记录；原核查日期：2026-09-03。2026-10-09依据既有索引精简文字，没有新增论文核验或复现。
>
> [返回当前研究入口](../README.md)

指出常用数据库去重会把训练结构的元素替换体计为新结构，并以 substitution-aware 分析重新审计代表性模型的结构新颖性。

出处：2026 · arXiv preprint；evaluation。

[论文](https://arxiv.org/abs/2606.23166)；首轮未核实项目入口。

首轮状态：已审计；2026 新预印本，百分比随版本和口径复核

## 1. Scientific problem

“未与训练库 StructureMatcher 匹配”并不等于结构拓扑创新；模型可能只复用已知原型并替换元素。

## 2. Mathematical task

将生成结构分成训练重复、元素替换可导出、已知原型复用和更强意义上的结构新颖类别。

## 3. Data-generating process

代表性生成模型样本、训练数据库、结构匹配/原型归一化、元素映射或替换搜索，以及稳定性过滤结果。

## 4. Core mechanism

把元素身份与几何/拓扑骨架分离，检查是否存在从训练结构经元素重标记即可获得的生成结构。

## 5. Claim–evidence alignment

论文报告在所审计模型和筛选口径下，大量化学有效且亚稳候选属于训练重复或 substitution-derived，挑战了宽松 novelty 的解释。

## 6. Hidden assumptions

元素替换关系的搜索足够完备且不会过度合并真正不同的化学键合；结构弛豫前后比较可归一；训练集可完整获得。

## 7. Strongest alternative explanation

模型可能在已知拓扑上提出科学上有价值的新化学组成；因此 substitution-derived 不等于无价值，只是否定“新结构原型”的强声明。

## 8. Missing baseline

拓扑图/配位环境、弛豫后原型、专家判读以及 prospective 合成价值；与随机替换和化学规则替换基线比较。

## 9. Killer experiment

若更严格的键合拓扑、弛豫后晶胞和人工审查发现大量被判 substitution-derived 的样本具有新连接方式，则当前规则过度合并。

## 10. Contribution type

它改变了 novelty 的操作定义，并迫使论文把“新组成”“新结构原型”“新性质”和“新可合成材料”分开。

首轮角色：新颖性审计 / 替换派生。历史六维记录：[2, 2, 1, 0, 2, 1]。

## 11. Transferable abstraction

可迁移到分子、蛋白和代码生成：字符串/实体不重复不代表机制或结构新颖，必须剥离简单变换群。

## 12. Final verdict

这是高价值概念纠偏。其结论应被理解为对现有 novelty 口径的反证，而非否定原型迁移在材料发现中的意义。

首轮使用建议：当前项目必须报告 duplicate、substitution-derived、prototype-known、motif-novel 四级 novelty，并与随机/规则替换比较。

具体结论范围：不能仅凭该论文的百分比断言所有模型都在记忆；不同模型、数据切分和结构归一化会改变比例。

### 首轮留下的后续问题

构建弛豫前后双口径 substitution graph，并让结构专家盲评一批边界样本，量化自动规则的假阳性/假阴性。
