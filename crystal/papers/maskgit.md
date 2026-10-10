---
title: "MaskGIT: Masked Generative Image Transformer"
slug: "maskgit"
year: 2022
venue: "CVPR 2022"
category: "cross-domain"
audit_role: "并行迭代离散生成"
paper_url: "https://arxiv.org/abs/2202.04200"
project_url: "https://github.com/google-research/maskgit"
last_verified: "2026-09-03"
---

# MaskGIT: Masked Generative Image Transformer

> 文献分析；资料核查截至2026-09-03。
>
> [返回当前研究入口](../README.md)

通过双向掩码预测与置信度驱动的迭代重掩码，实现比自回归更并行的离散 token 生成。

出处：2022 · CVPR 2022；cross-domain。

[论文](https://arxiv.org/abs/2202.04200) · [官方/作者项目](https://github.com/google-research/maskgit)

文献状态：基础 CV 方法

## 1. Scientific problem

自回归离散生成严格串行、误差顺序固定，而一次性掩码填充缺少逐步修正。

## 2. Mathematical task

从全掩码 token 网格出发，多轮并行预测并固定高置信 token、重掩码低置信 token。

## 3. Data-generating process

图像离散 tokenizer 产生的 token 网格与类别条件。

## 4. Core mechanism

用迭代并行 refinement 替代左到右生成，把置信度调度变成生成顺序。

## 5. Claim–evidence alignment

论文展示显著采样加速及有竞争力的图像质量，后续启发 MaskGXT 等晶体离散模型。

## 6. Hidden assumptions

tokenization 保留任务结构；模型置信度可作为正确的固定顺序；不同位置可并行条件独立近似。

## 7. Strongest alternative explanation

速度/质量增益可能依赖 VQ tokenizer 和图像网格局部性；置信度未必等于晶体物理重要性。

## 8. Missing baseline

自回归、离散 diffusion、随机重掩码、基于结构敏感性的调度和相同 NFE/参数比较。

## 9. Killer experiment

若晶体 token 的模型置信度与最终结构误差/势阱身份无关，且随机调度相当，则 MaskGIT 迁移只是工程加速。

## 10. Contribution type

它改变离散生成算子和采样并行性，属于可复用机制贡献。

工作定位：并行迭代离散生成。六维贡献描述：[2, 1, 2, 2, 1, 0]。

## 11. Transferable abstraction

对晶体要迁移的是 iterative masked refinement；必须重新定义 token 等价性、lattice/atom 分工和物理置信度。

## 12. Final verdict

基础 CV 贡献明确。HACO/MaskGXT 的价值不在“使用 Transformer”，而在证明该算子适合晶体多晶型生成。

研究参考：可用于审计 DLM 路线：并行掩码是否改善模式探索，还是只减少延迟。

具体结论范围：不能把图像早/晚 token 规律直接假设为晶体 lattice/coordinate 阶段规律。

### 相关研究问题

测量不同 token/轮次对弛豫后 basin identity、晶格和局部环境的因果敏感性，再设计重掩码策略。
