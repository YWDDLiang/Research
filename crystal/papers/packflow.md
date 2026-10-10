---
title: "PackFlow: Generative Molecular Crystal Structure Prediction via Reinforcement Learning Alignment"
slug: "packflow"
year: 2026
venue: "arXiv 2026"
category: "分子晶体 CSP"
audit_role: "物理对齐/系统"
paper_url: "https://arxiv.org/abs/2602.20140"
project_url: ""
last_verified: "2026-09-03"
---

# PackFlow: Generative Molecular Crystal Structure Prediction via Reinforcement Learning Alignment

> 文献分析；资料核查截至2026-09-03。
>
> [返回当前研究入口](../README.md)

联合生成分子重原子坐标与晶格，并用 MLIP 能量和力进行 RL physics alignment，接入标准 relax-and-rank 流程。

出处：2026 · arXiv 2026；分子晶体 CSP。

[论文](https://arxiv.org/abs/2602.20140)；首轮未核实项目入口。

文献状态：2026 新预印本；分子晶体与无机晶体边界需明确。

## 1. Scientific problem

分子晶体 packing 的候选组合爆炸，稳定性只有昂贵 relax/energy 后才知道，生成分布与低能盆地错位。

## 2. Mathematical task

输入分子图，输出晶体 packing 和晶格；flow proposal 经 RL 对齐后再弛豫、晶格能排序。

## 3. Data-generating process

数据来自实验分子晶体和 MLIP 代理；盲测个例更接近真实 CSP，但体系数量有限。

## 4. Core mechanism

lattice-aware flow 负责候选，能量/力 reward 后训练把概率质量集中到物理有利区域。

## 5. Claim–evidence alignment

未见分子集、实验多晶型相似度及两个 blind-test 案例支持 proposal 改善；广泛泛化和 DFT 可靠性仍需更多体系。

## 6. Hidden assumptions

MLIP 对分子间作用和晶格能排序足够准确；力/能 reward 不导致模式坍缩；两个 blind case 有代表性。

## 7. Strongest alternative explanation

RL 可能只是更强局部弛豫初始化，或过拟合特定 MLIP；低能集中可能降低其他多晶型覆盖。

## 8. Missing baseline

传统随机/低差异 packing、相同 MLIP 的 gradient relaxation、energy-guided sampling、无 RL 的 best-of-N。

## 9. Killer experiment

测相同分子上多个已知/预测多晶型的 basin recall，并更换势能模型；若只减少初始力而不增加多晶型覆盖，属于 relaxer 优化。

## 10. Contribution type

端到端 CSP 流程和物理后训练证据较强，是无机晶体路线的重要邻域先例。

工作定位：物理对齐/系统。六维贡献描述：[1, 1, 2, 1, 1, 0]。

## 11. Transferable abstraction

迁移的是用“弛豫后落入哪个盆地”评价 proposal，而非只看未弛豫结构分数。

## 12. Final verdict

对我们直接构成先例：energy+force RL 不是新意，必须进一步解决多盆地覆盖与 evaluator 不确定性。

研究参考：用作物理对齐、relax-and-rank 和盲测设计参考。

具体结论范围：不能把分子晶体结论无条件外推到无机晶体，也不能只报告最低能量。

### 相关研究问题

在无机固定组成上复刻同协议，增加 basin archive、Top-K recall 和多 MLIP/DFT。
