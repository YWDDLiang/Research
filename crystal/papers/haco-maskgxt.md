---
title: "Discovering Crystal Structure Prediction Algorithms with an AI Co-Scientist"
slug: "haco-maskgxt"
year: 2026
venue: "arXiv 2026"
category: "AI co-scientist/CSP"
audit_role: "跨域机制迁移/系统"
paper_url: "https://arxiv.org/abs/2606.22866"
project_url: "https://github.com/kiyoung98/maskgxt"
last_verified: "2026-09-03"
---

# Discovering Crystal Structure Prediction Algorithms with an AI Co-Scientist

> 文献分析；资料核查截至2026-09-03。
>
> [返回当前研究入口](../README.md)

通过 HACO 跨域检索将 CV 的 MaskGIT 迁移为 MaskGXT：离散化晶格、坐标、空间群与 Wyckoff token，并迭代置信度解码。

出处：2026 · arXiv 2026；AI co-scientist/CSP。

[论文](https://arxiv.org/abs/2606.22866) · [官方/作者项目](https://github.com/kiyoung98/maskgxt)

文献状态：2026 新预印本；另有 HACO 系统代码 https://github.com/kiyoung98/HACO。

## 1. Scientific problem

自回归 CSP 慢且受顺序偏置，连续扩散又可能不便统一离散晶体规格；能否采用并行掩码生成。

## 2. Mathematical task

给定组成，离散化完整结构 token；训练随机 mask 恢复，推理从全 mask 并行预测并按置信度逐步固定。

## 3. Data-generating process

基于 MP-20、MPTS-52 及 polymorph-aware split；坐标分箱和 sub-bin refinement 决定误差下限。

## 4. Core mechanism

迁移 MaskGIT 的并行迭代解码，加入周期标签平滑、晶体对称 token、空间群分层采样与坐标细化。

## 5. Claim–evidence alignment

摘要报告标准 Match Rate 和 MP-20 polymorph split 的 METRe 提升；支持跨域算子可行，但 AI co-scientist 的因果贡献较难独立验证。

## 6. Hidden assumptions

坐标离散误差可控；置信度是正确解码顺序的好代理；HACO 找到的方法优于普通人工检索并非事后叙事。

## 7. Strongest alternative explanation

收益可能由人工加入的晶体先验、更多搜索实验和分层采样造成，而不是 MaskGIT 或 AI co-scientist。

## 8. Missing baseline

相同晶体 token 的 autoregressive/parallel diffusion、随机方法检索、去掉 HACO 叙事的人工 baseline。

## 9. Killer experiment

固定 tokenization 和晶体先验，仅替换解码算子；若 MaskGIT 不再占优，则跨域发现核心减弱。另需记录 HACO 候选淘汰轨迹以审计选择偏差。

## 10. Contribution type

MaskGXT 的离散并行机制有实质贡献；HACO 是系统/过程贡献，证据标准与模型贡献不同。

工作定位：跨域机制迁移/系统。六维贡献描述：[1, 2, 2, 1, 2, 0]。

## 11. Transferable abstraction

这是跨领域迁移的优秀范例：迁移生成算子，再用领域约束逐项改造，而不是只换 backbone 名称。

## 12. Final verdict

对我们最有启发的是方法发现流程与离散—连续接口；同时要警惕成功后的回溯性故事。

研究参考：作为 MaskGIT 晶体迁移、polymorph-aware 评测和 co-scientist 案例。

具体结论范围：不能据一次成功就声称 AI 能普遍发现算法，也不能把所有增益归因于 MaskGIT。

### 相关研究问题

复现 MaskGXT 的 tokenization/decoder 分离消融，并把同流程用于 basin token 而非完整坐标分箱。
