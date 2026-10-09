---
title: "Symmetry-Breaking De Novo Crystal Generation via Markovian Jump Diffusion"
slug: "sbcd"
year: 2026
venue: "arXiv 2026"
category: "对称生成"
audit_role: "新近机制预印本"
paper_url: "https://arxiv.org/abs/2608.13457"
project_url: ""
last_verified: "2026-09-03"
---

# Symmetry-Breaking De Novo Crystal Generation via Markovian Jump Diffusion

> 历史首轮记录；原核查日期：2026-09-03。2026-10-09依据既有索引精简文字，没有新增论文核验或复现。
>
> [返回当前研究入口](../README.md)

从最低对称先验出发，用 Markovian jump diffusion 显式建模空间群之间的离散跳转，把对称破缺/恢复纳入生成。

出处：2026 · arXiv 2026；对称生成。

[论文](https://arxiv.org/abs/2608.13457)；首轮未核实项目入口。

首轮状态：2026-08 新预印本；结论暂定，尚需代码和独立复现。

## 1. Scientific problem

现有对称生成器常固定或从经验分布采样空间群，不能在生成过程中建模不同空间群之间的依赖。

## 2. Mathematical task

联合状态含连续结构变量与离散空间群，跳扩散过程在群之间转移并生成完整晶体规格。

## 3. Data-generating process

在 MP-20、MPTS-52 等数据库上训练；所谓“物理启发”来自对称破缺类比，并非真实温压相变轨迹。

## 4. Core mechanism

以 Markov jump 处理离散群转移、连续扩散处理几何，形成混合离散—连续随机过程。

## 5. Claim–evidence alignment

摘要报告优于 symmetry-preserving 对照；当前证据支持算法可能有效，但尚不足以确认广泛 SOTA、物理真实性或鲁棒性。

## 6. Hidden assumptions

空间群图上的转移设计合理；最低对称 prior 不会引入偏置；数据库空间群频率能监督真实转换规律。

## 7. Strongest alternative explanation

增益可能来自更灵活的空间群搜索或额外容量，而非“对称破缺物理”。

## 8. Missing baseline

独立 categorical space-group diffusion、任意转移矩阵、软空间群分类器、无物理命名的 jump process。

## 9. Killer experiment

打乱或随机化群转移邻接关系；若结果不变，物理对称破缺叙事不成立，只剩通用离散跳转机制。

## 10. Contribution type

潜在强机制贡献，但当前仍是需要严格审计的新预印本。

首轮角色：新近机制预印本。历史六维记录：[1, 2, 2, 0, 0, 0]。

## 11. Transferable abstraction

可迁移的是离散结构模式与连续几何的 jump-diffusion 联合建模，正好对应 basin family + local geometry。

## 12. Final verdict

值得跟踪，尤其适合反思硬 Wyckoff 约束；现阶段不应当作已被充分验证的事实。

首轮使用建议：作为跨空间群生成和全局离散模式变量的前沿参考。

具体结论范围：不能把数学上的群跳转等同于真实物理相变或自发对称破缺。

### 首轮留下的后续问题

代码公开后做随机转移图、等参数 categorical baseline 和低能破缺结构测试。
