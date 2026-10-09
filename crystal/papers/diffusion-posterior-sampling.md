---
title: "Diffusion Posterior Sampling for General Noisy Inverse Problems"
slug: "diffusion-posterior-sampling"
year: 2022
venue: "ICLR 2023"
category: "cross-domain"
audit_role: "生成先验 + 测量似然"
paper_url: "https://arxiv.org/abs/2209.14687"
project_url: "https://github.com/DPS2022/diffusion-posterior-sampling"
last_verified: "2026-09-03"
---

# Diffusion Posterior Sampling for General Noisy Inverse Problems

> 历史首轮记录；原核查日期：2026-09-03。2026-10-09依据既有索引精简文字，没有新增论文核验或复现。
>
> [返回当前研究入口](../README.md)

将预训练扩散模型作为先验，通过近似似然梯度在采样时解决有噪声、非线性逆问题。

出处：2022 · ICLR 2023；cross-domain。

[论文](https://arxiv.org/abs/2209.14687) · [官方/作者项目](https://github.com/DPS2022/diffusion-posterior-sampling)

首轮状态：已审计；基础逆问题方法

## 1. Scientific problem

仅依靠生成先验不能保证样本与具体测量一致，而每种测量重新训练条件模型成本高。

## 2. Mathematical task

从后验 p(x|y) 近似采样，其中 p(x) 由扩散模型表示，p(y|x) 由已知前向测量模型给出。

## 3. Data-generating process

图像先验数据、观测 y、已知线性/非线性噪声前向算子。

## 4. Core mechanism

在反向扩散中叠加近似的 measurement consistency 梯度，以贝叶斯分解连接先验与观测。

## 5. Claim–evidence alignment

论文在多类逆问题中展示无需任务特定重训练的重建能力，并支持噪声和非线性测量。

## 6. Hidden assumptions

前向算子可微且近似正确；似然梯度近似在扩散中间状态有效；先验覆盖真实解。

## 7. Strongest alternative explanation

重建提升可能来自强图像先验，后验近似未必校准；错误前向模型会把样本推向伪解。

## 8. Missing baseline

优化式数据一致性、classifier guidance、任务特定条件模型、MCMC/SMC 后验采样和 posterior calibration。

## 9. Killer experiment

若在多解问题上样本不能覆盖真实后验、只给单一先验偏好解，或在前向模型误差下失效，则后验采样声明需收窄。

## 10. Contribution type

它建立了“生成模型是先验，不是答案”的重要逆问题接口。

首轮角色：生成先验 + 测量似然。历史六维记录：[2, 1, 2, 1, 2, 0]。

## 11. Transferable abstraction

晶体可令 y 为 PXRD/PDF/局部谱，构造 p(s|A,y)，使生成从数据库拟合转向实验约束下的结构后验。

## 12. Final verdict

这是比泛化性质条件更科学明确的迁移方向，但晶体前向谱模拟、周期等价和多相混合会带来新难点。

首轮使用建议：作为未来实验结构解析支线，而非当前多势阱 CSP 主线的必需模块。

具体结论范围：不能把 measurement-guided 单个重建视为完整后验，也不能忽略实验系统误差和不可辨识性。

### 首轮留下的后续问题

在合成 PXRD 的可控多晶型数据上测试 posterior coverage、校准和前向误差鲁棒性，再进入真实实验。
