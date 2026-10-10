---
title: "Invariant Tokenization of Crystalline Materials for Language Model Enabled Generation"
slug: "mat2seq"
year: 2025
venue: "NeurIPS 2024"
category: "LLM 表示"
audit_role: "表示/形式化"
paper_url: "https://arxiv.org/abs/2503.00152"
project_url: ""
last_verified: "2026-09-03"
---

# Invariant Tokenization of Crystalline Materials for Language Model Enabled Generation

> 文献分析；资料核查截至2026-09-03。
>
> [返回当前研究入口](../README.md)

通过 Niggli/primitive cell 等规范化步骤把等价的三维晶体映射为唯一、可重构、SE(3) 与周期不变的一维序列。

出处：2025 · NeurIPS 2024；LLM 表示。

[论文](https://arxiv.org/abs/2503.00152)；首轮未核实项目入口。

文献状态：已发表；资料核查时未确认官方代码仓库。

## 1. Scientific problem

直接使用 CIF 会让同一物理晶体对应多个序列，语言模型被迫学习无意义的坐标系和晶胞选择。

## 2. Mathematical task

输入为晶体等价类，输出规范序列；核心目标先是定义近似单射/规范化映射，再用 LM 学习该序列分布。

## 3. Data-generating process

仍使用数据库终态，但数据表示经过规范化；规范化失败、数值容差和边界退化会影响唯一性。

## 4. Core mechanism

先寻找旋转等变、周期不变的规范晶胞，再确定原子排序与数值序列，使等价描述尽量折叠为一个表示。

## 5. Claim–evidence alignment

理论性质与生成实验支持其表示价值；真正贡献主要在 tokenization，而不是语言模型本身。

## 6. Hidden assumptions

规范化在所有晶体上稳定且数值连续；唯一序列不会在近边界结构上产生不连续跳变；信息完整性可实际保持。

## 7. Strongest alternative explanation

改进可能来自去重、标准化和降低序列熵，而不是 LM 生成能力。

## 8. Missing baseline

同一规范化用于小 Transformer、非自回归模型和检索；不同规范化方法的鲁棒性比较。

## 9. Killer experiment

对结构施加微小扰动、等价晶胞变换和原子重排，测试序列编辑距离是否稳定；若微扰导致大幅 token 跳变，生成学习可能受离散不连续影响。

## 10. Contribution type

强表示贡献：把 LLM 晶体生成中的数学不适定性显式提出并解决。

工作定位：表示/形式化。六维贡献描述：[1, 2, 1, 1, 1, 0]。

## 11. Transferable abstraction

可迁移的是先构造对等价群作用不变且可逆的 canonical interface，再选择序列模型。

## 12. Final verdict

比“直接用 CIF 喂 LLM”更扎实；即使未来不用 LLM，表示问题仍然成立。

研究参考：用作任何序列/DLM 晶体项目的表示审计基线。

具体结论范围：不能把 canonicalization 等同于物理合理性，也不能忽略数值不连续与标准化失败样本。

### 相关研究问题

比较 Mat2Seq、原始 CIF、Wyckoff token 和结构图 token 在小模型与大模型下的样本效率。
