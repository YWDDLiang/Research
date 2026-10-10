---
title: "CrystalDiT: A Diffusion Transformer for Crystal Generation"
slug: "crystaldit"
year: 2025
venue: "AAAI 2026"
category: "de novo 生成"
audit_role: "架构/训练策略"
paper_url: "https://arxiv.org/abs/2508.16614"
project_url: "https://github.com/hanyi2021/CrystalDiT"
last_verified: "2026-09-03"
---

# CrystalDiT: A Diffusion Transformer for Crystal Generation

> 文献分析；资料核查截至2026-09-03。
>
> [返回当前研究入口](../README.md)

用统一 Transformer 同时处理晶格与原子变量，加入周期表二维元素编码、平衡训练/选点策略和概率元素解码。

出处：2025 · AAAI 2026；de novo 生成。

[论文](https://arxiv.org/abs/2508.16614) · [官方/作者项目](https://github.com/hanyi2021/CrystalDiT)

文献状态：已发表；SUN 数字在论文版本与仓库可能有更新，索引以原论文为准。

## 1. Scientific problem

复杂多流架构是否真的必要，以及元素、晶格、坐标分开建模是否削弱它们的耦合。

## 2. Mathematical task

联合建模完整晶体的扩散过程，主要面向 de novo；目标是提高稳定、唯一、新颖的联合成功率。

## 3. Data-generating process

基于 MP-20 等数据库与代理稳定性评估；SUN 对去重、训练集版本和 MLIP 很敏感。

## 4. Core mechanism

把所有晶体 token 放入统一 attention，利用元素周期表位置编码，并用平衡 checkpoint 选择避免只优化单一指标。

## 5. Claim–evidence alignment

论文报告 MP-20 SUN 和 unique/novel 提升；说明简单统一架构有竞争力，但贡献与模型选择策略、评测口径耦合。

## 6. Hidden assumptions

统一 attention 是主因；周期表编码公平；SUN 比较使用相同弛豫器、训练集和阈值。

## 7. Strongest alternative explanation

提升可能来自 checkpoint selection、解码策略和评测调参，而不是 DiT 架构本身。

## 8. Missing baseline

同参数量多流 Transformer、无周期表编码、固定 checkpoint 规则、统一 LeMat-GenBench 重评。

## 9. Killer experiment

用独立 benchmark 代码和盲选 checkpoint 重现 SUN；若排名对选择规则高度敏感，则架构结论需弱化。

## 10. Contribution type

清晰的简化架构与训练策略贡献，但没有重新定义晶体生成问题。

工作定位：架构/训练策略。六维贡献描述：[0, 1, 1, 1, 1, 0]。

## 11. Transferable abstraction

迁移的是联合 token 交互与简洁架构优先原则；先证明分流是否必要，再堆模块。

## 12. Final verdict

有价值的工程/架构论文，不能仅凭单一 SUN 排名视为范式突破。

研究参考：作为 de novo Transformer backbone 和“简单强基线”。

具体结论范围：不能把高 SUN 直接解释为更强结构创新，需结合 substitution novelty 和 evaluator robustness。

### 相关研究问题

在 LeMat-GenBench、substitution-aware novelty 和 PhononBench 上统一重评。
