---
title: "WyckoffDiff -- A Generative Diffusion Model for Crystal Symmetry"
slug: "wyckoffdiff"
year: 2025
venue: "ICML 2025"
category: "对称离散生成"
audit_role: "表示/离散机制"
paper_url: "https://arxiv.org/abs/2502.06485"
project_url: "https://github.com/httk/wyckoffdiff"
last_verified: "2026-09-03"
---

# WyckoffDiff -- A Generative Diffusion Model for Crystal Symmetry

> 文献分析；资料核查截至2026-09-03。
>
> [返回当前研究入口](../README.md)

在 protostructure/Wyckoff 表示上进行离散扩散，使对称性按构造成立，并提出 Fréchet Wrenformer Distance 衡量对称分布。

出处：2025 · ICML 2025；对称离散生成。

[论文](https://arxiv.org/abs/2502.06485) · [官方/作者项目](https://github.com/httk/wyckoffdiff)

文献状态：已发表；官方代码已核验。

## 1. Scientific problem

逐原子连续生成难以稳定产生空间群对称，且高维冗余；能否直接生成压缩的对称描述。

## 2. Mathematical task

输入噪声离散状态，输出元素—Wyckoff 占位等 protostructure，再经下游坐标实现/弛豫得到晶体。

## 3. Data-generating process

训练依赖可靠的 Wyckoff 分解；连续自由参数和后续几何质量可能不在离散模型内充分解决。

## 4. Core mechanism

设计适配集合/占位的离散扩散网络，硬编码对称合法性，并用新的嵌入距离评估生成分布。

## 5. Claim–evidence alignment

快速生成、对称有效性和分布指标支持表示优势；最终稳定性仍受结构实例化与 relaxer 影响。

## 6. Hidden assumptions

Wyckoff 表示保留发现所需自由度；FWrenformer 距离与材料发现价值相关；硬约束不会错过重要破缺结构。

## 7. Strongest alternative explanation

结果可能来自压缩搜索空间与后处理，而非离散扩散；新指标可能偏好相同表示族。

## 8. Missing baseline

Wyckoff 频率模型、无扩散的 autoregressive set model、相同 downstream relaxer 的随机 protostructure。

## 9. Killer experiment

固定生成的 Wyckoff protostructure，替换离散模型；并在对称破缺目标上测上限。若简单频率模型等效，网络贡献有限。

## 10. Contribution type

表示、离散生成和对称评价三项贡献较清楚。

工作定位：表示/离散机制。六维贡献描述：[1, 2, 2, 2, 1, 0]。

## 11. Transferable abstraction

迁移价值是先生成低维等价类/结构骨架，再把连续几何交给第二阶段。

## 12. Final verdict

强对称路线论文，但与我们强调的未知多盆地探索存在潜在上限冲突。

研究参考：作为 Wyckoff 离散模型与 fast proposal 基线。

具体结论范围：不能把 protostructure 新颖等同于完整结构新颖，不能忽略连续实例化失败。

### 相关研究问题

用同一批 protostructure 比较不同 continuous decoder，并分析其可达低能盆地集合。
