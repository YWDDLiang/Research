---
title: "Flow Matching on General Geometries"
slug: "riemannian-flow-matching"
year: 2023
venue: "ICLR 2024"
category: "cross-domain"
audit_role: "流形生成原语"
paper_url: "https://arxiv.org/abs/2302.03660"
project_url: "https://github.com/facebookresearch/riemannian-fm"
last_verified: "2026-09-03"
---

# Flow Matching on General Geometries

> 历史首轮记录；原核查日期：2026-09-03。2026-10-09依据既有索引精简文字，没有新增论文核验或复现。
>
> [返回当前研究入口](../README.md)

将 Flow Matching 扩展到一般黎曼流形，为球面、环面和乘积流形上的几何一致生成提供统一工具。

出处：2023 · ICLR 2024；cross-domain。

[论文](https://arxiv.org/abs/2302.03660) · [官方/作者项目](https://github.com/facebookresearch/riemannian-fm)

首轮状态：已审计；基础方法论文

## 1. Scientific problem

欧氏插值会离开具有约束的状态空间或忽略内在距离，导致几何对象生成的路径与不变性不合理。

## 2. Mathematical task

在黎曼流形上定义条件概率路径、切向量场和测地/近似测地运输，学习流形内的生成流。

## 3. Data-generating process

球面、环面、旋转群等合成/实际数据，以及可计算的流形操作。

## 4. Core mechanism

将向量场限制在切空间并使用流形几何定义插值和 ODE，从表示层消除一部分无效状态。

## 5. Claim–evidence alignment

论文在多种非欧几里得数据上验证几何一致性与生成性能，为晶体分数坐标的 torus 建模提供基础。

## 6. Hidden assumptions

选用流形准确表示等价关系；测地线/指数映射计算稳定；乘积几何的权重合理。

## 7. Strongest alternative explanation

收益可能来自更正确的周期表示，而非 flow matching；对于晶格商空间，简单流形近似仍可能遗漏等价晶胞。

## 8. Missing baseline

周期 wrapped diffusion、欧氏坐标加周期 loss、不同晶胞参数化，以及真实 quotient-space 方法。

## 9. Killer experiment

若几何一致基线在相同表示下与 RFM 相当，或结果对任意度量权重极敏感，则“流形 FM”贡献需收窄。

## 10. Contribution type

它改变表示和生成原语，使算法尊重状态空间；对晶体是方法基础而非完整科学答案。

首轮角色：流形生成原语。历史六维记录：[1, 2, 2, 1, 1, 0]。

## 11. Transferable abstraction

应迁移其『先识别状态空间，再设计路径』的原则，特别是分数坐标环面与晶格正定/等价结构。

## 12. Final verdict

重要基础。它解决几何合法性，不解决稳定性、势能面、多晶型覆盖或数据库偏差。

首轮使用建议：用于审计所有晶体 flow/diffusion 是否在正确的商空间上工作，以及近似几何会造成哪些模式偏差。

具体结论范围：不能因为向量场在流形上就称其物理一致；几何约束与能量动力学是不同层次。

### 首轮留下的后续问题

比较 torus/Riemannian、wrapped Euclidean 与显式晶胞等价归一化，在相同模型下分析边界伪影和 basin 覆盖。
