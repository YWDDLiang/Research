---
title: "Crystal Structure Generation with Autoregressive Large Language Modeling"
slug: "crystallm"
year: 2023
venue: "Nature Communications 2024"
category: "LLM 生成"
audit_role: "表示/系统先例"
paper_url: "https://arxiv.org/abs/2307.04340"
project_url: "https://github.com/lantunes/CrystaLLM"
last_verified: "2026-09-03"
---

# Crystal Structure Generation with Autoregressive Large Language Modeling

> 历史首轮记录；原核查日期：2026-09-03。2026-10-09依据既有索引精简文字，没有新增论文核验或复现。
>
> [返回当前研究入口](../README.md)

把 CIF 当作文本序列，用 GPT 类自回归模型按组成和可选空间群生成结构，并可结合能量预测器与 MCTS 改善候选。

出处：2023 · Nature Communications 2024；LLM 生成。

[论文](https://arxiv.org/abs/2307.04340) · [官方/作者项目](https://github.com/lantunes/CrystaLLM)

首轮状态：已发表；首轮审计基于论文、官方代码与 Nature Communications 版本。

## 1. Scientific problem

能否利用成熟语言模型直接建模晶体文件，从而以低推理成本提出可用于 CSP 的初始候选。

## 2. Mathematical task

输入为组成/空间群提示，输出 CIF token 序列；最大似然学习 p(CIF|condition)，MCTS 版本再用能量代理引导搜索。

## 3. Data-generating process

训练来自数百万 CIF；同一物理结构可能有多种文本表示，数据库来源、标准化和去重决定模型看到的规律。

## 4. Core mechanism

将数值字段离散为 token，使用自回归 Transformer 学习语法与结构统计，并用外部能量模型给树搜索评分。

## 5. Claim–evidence alignment

语法有效、物理约束、DFT 个例和条件生成支持可行性；证据并不能证明 LLM 形成了可解释的晶体化学世界模型。

## 6. Hidden assumptions

CIF 序列化不引入有害非唯一性；规模效应来自预训练知识而非参数量；能量代理在搜索分布外可靠。

## 7. Strongest alternative explanation

模型可能主要记忆语法、元素替换和常见原型；MCTS 提升也可能完全来自外部 evaluator。

## 8. Missing baseline

从零训练的小 Transformer、检索+模板替换、打乱自然语言预训练权重、规范化序列与原始 CIF 对照。

## 9. Killer experiment

保持数据和参数量不变，比较预训练 LLM、随机初始化 Transformer、n-gram/模板模型及 substitution-aware novelty；若差异很小，LLM 知识叙事不成立。

## 10. Contribution type

证明 CIF 自回归生成可行，属于重要先例与系统整合；表示的非唯一性后来由 Mat2Seq 更直接处理。

首轮角色：表示/系统先例。历史六维记录：[1, 1, 1, 1, 1, 0]。

## 11. Transferable abstraction

迁移的是“离散全局 proposal 可由序列模型承担”，而不是自然语言本身。

## 12. Final verdict

值得读，但要把 LLM、文本表示、训练规模与 MCTS evaluator 四种贡献拆开。

首轮使用建议：作为 LLM 晶体生成基线和全局候选 proposal 参考。

具体结论范围：不能把生成语法正确或 DFT 个例直接称为理解势能面；也不能忽视原型记忆。

### 首轮留下的后续问题

用统一数据训练 100M/1B/7B 模型，控制预训练与容量，并测 basin coverage 与 substitution novelty。
