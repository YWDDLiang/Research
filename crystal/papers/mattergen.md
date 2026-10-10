---
title: "MatterGen: a generative model for inorganic materials design"
slug: "mattergen"
year: 2023
venue: "Nature 2025"
category: "逆向设计"
audit_role: "系统/规模/验证"
paper_url: "https://arxiv.org/abs/2312.03687"
project_url: "https://github.com/microsoft/mattergen"
last_verified: "2026-09-03"
---

# MatterGen: a generative model for inorganic materials design

> 文献分析；资料核查截至2026-09-03。
>
> [返回当前研究入口](../README.md)

联合生成元素、坐标和晶格，并通过 adapter 支持多种性质条件；依靠大规模数据、计算筛选、DFT 与实验验证形成完整材料设计系统。

出处：2023 · Nature 2025；逆向设计。

[论文](https://arxiv.org/abs/2312.03687) · [官方/作者项目](https://github.com/microsoft/mattergen)

文献状态：已发表；文献分析区分架构、数据规模、筛选和验证贡献。

## 1. Scientific problem

如何在全周期表范围内生成稳定、新颖并满足多种性质约束的无机材料。

## 2. Mathematical task

输入为空或性质/化学/对称条件，输出完整晶体；训练是条件生成，部署是生成—MLIP/DFT 筛选—实验验证链。

## 3. Data-generating process

使用规模远大于经典 MP-20 的材料与非平衡数据；训练分布、筛选器和计算预算共同决定结果。

## 4. Core mechanism

对元素类型、分数坐标和晶格设计联合扩散，使用性质 adapter 在标注较少时微调，并配套大规模验证。

## 5. Claim–evidence alignment

论文报告稳定新颖率、接近弛豫态、性质命中、DFT 验证和实验合成；证据链显著强于只报 benchmark 的工作。

## 6. Hidden assumptions

MLIP/DFT 筛选能可靠外推；训练数据去重与 novelty 判定充分；实验案例可以代表系统能力而非少量成功选择。

## 7. Strongest alternative explanation

相当部分提升可能来自更大数据、更多算力、更强筛选和候选选择，而不是联合扩散架构。

## 8. Missing baseline

同数据同算力的简化架构、离子替换/原型枚举加相同筛选、去掉 adapter 的直接条件训练。

## 9. Killer experiment

控制训练数据和筛选预算后比较架构；若简化模型达到相同候选发现率，则“模型创新”应降格为规模与系统贡献。

## 10. Contribution type

高价值系统、规模与验证贡献；不是纯算法开山，但把生成式材料设计推进到更完整证据链。

工作定位：系统/规模/验证。六维贡献描述：[1, 2, 2, 2, 2, 1]。

## 11. Transferable abstraction

迁移的是“从模型指标到多保真验证闭环”的系统观，以及把数据规模效应与方法效应分离。

## 12. Final verdict

领域标杆系统。阅读时必须拆开数据、架构、计算和实验验证，不能把全部成功归于一个 diffusion 名称。

研究参考：用作 de novo、条件设计和高标准验证链的上限参照，不要求在有限算力下完整复现。

具体结论范围：不能仅用其 SUN 数字跨论文比较，也不能忽视其训练规模与后筛选成本。

### 相关研究问题

在统一 LeMat-GenBench 和相同后筛选预算下，对 MatterGen checkpoint 与轻量模型做分层比较。
