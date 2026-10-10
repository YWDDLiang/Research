---
title: "Fine-Tuned Language Models Generate Stable Inorganic Materials as Text"
slug: "crystal-text-llm"
year: 2024
venue: "ICLR 2024"
category: "LLM 生成"
audit_role: "规模/能力实证"
paper_url: "https://arxiv.org/abs/2402.04379"
project_url: "https://github.com/facebookresearch/crystal-text-llm"
last_verified: "2026-09-03"
---

# Fine-Tuned Language Models Generate Stable Inorganic Materials as Text

> 文献分析；资料核查截至2026-09-03。
>
> [返回当前研究入口](../README.md)

系统比较不同规模预训练语言模型在文本化晶体生成上的能力，报告稳定性随模型规模提升，并支持 infilling 与文本条件。

出处：2024 · ICLR 2024；LLM 生成。

[论文](https://arxiv.org/abs/2402.04379) · [官方/作者项目](https://github.com/facebookresearch/crystal-text-llm)

文献状态：已发表；官方代码已核验。

## 1. Scientific problem

通用 LLM 的预训练与规模是否能迁移到结构化数值文本，并在无专用等变架构时生成稳定晶体。

## 2. Mathematical task

最大似然微调文本晶体分布；输入可为提示或部分结构，输出完整文本结构，再由 MLIP/DFT 判断亚稳性。

## 3. Data-generating process

依赖文本化数据库与大模型预训练；训练集重复、元素替换和原型模式可能被语言模型记忆。

## 4. Core mechanism

用 LLaMA 等预训练模型直接自回归生成结构文本，并比较模型规模与条件任务。

## 5. Claim–evidence alignment

论文报告物理约束率、MLIP/DFT 的 metastability 和模型规模趋势；支持大 LM 可以做该任务，但不区分预训练知识、容量和数据记忆。

## 6. Hidden assumptions

语言预训练提供有用归纳偏置；不同规模比较公平；DFT 验证候选没有选择偏差。

## 7. Strongest alternative explanation

70B 优势可能纯粹来自容量和更低训练损失；稳定候选可能是数据库原型的近邻或替换。

## 8. Missing baseline

同规模随机初始化、非语言预训练、相同 token 预算的小型专用模型、严格 prototype split。

## 9. Killer experiment

冻结数据并做预训练权重置乱/随机初始化，按训练原型距离分层评估；若优势仅在近邻区域，世界模型解释应收缩。

## 10. Contribution type

规模实证和灵活文本接口贡献强，数学表示贡献弱于 Mat2Seq。

工作定位：规模/能力实证。六维贡献描述：[1, 1, 1, 2, 1, 0]。

## 11. Transferable abstraction

迁移价值是把模型规模效应、预训练效应和结构表示效应分开测量。

## 12. Final verdict

是 FlowLLM 和后续混合路线的重要基础，但“LLM 更懂化学”仍需机制性证据。

研究参考：作为 LLM base distribution 与模型规模消融基线。

具体结论范围：不能仅凭生成稳定率声称推理或世界模型；必须报告结构记忆与替换来源。

### 相关研究问题

用 Mat2Seq/图 token 重训小中大模型，加入原型 OOD split 与 basin identity 预测探针。
