---
title: "FlowMM: Generating Materials with Riemannian Flow Matching"
slug: "flowmm"
year: 2024
venue: "ICML 2024"
category: "生成基础"
audit_role: "几何机制"
paper_url: "https://arxiv.org/abs/2406.04713"
project_url: "https://github.com/facebookresearch/flowmm"
last_verified: "2026-09-03"
---

# FlowMM: Generating Materials with Riemannian Flow Matching

> 历史首轮记录；原核查日期：2026-09-03。2026-10-09依据既有索引精简文字，没有新增论文核验或复现。
>
> [返回当前研究入口](../README.md)

把 Riemannian Flow Matching 适配到晶格、周期坐标和元素变量组成的晶体流形，并强调 base distribution 的可设计性与采样效率。

出处：2024 · ICML 2024；生成基础。

[论文](https://arxiv.org/abs/2406.04713) · [官方/作者项目](https://github.com/facebookresearch/flowmm)

首轮状态：已发表；官方仓库已归档但可复现。

## 1. Scientific problem

扩散在晶体非欧状态空间上路径和采样成本较高，且固定高斯 base 未必是最容易运输到稳定晶体的起点。

## 2. Mathematical task

学习从 base distribution 到晶体数据分布的连续向量场；既支持 p(X,L|A) 的 CSP，也支持联合生成 A,X,L。

## 3. Data-generating process

仍以稳定数据库终态为主，训练目标是数据运输而非能量景观搜索。

## 4. Core mechanism

在晶体乘积流形上构造条件概率路径和切空间向量场，用 ODE 积分生成；允许选择集中或数据启发的 base。

## 5. Claim–evidence alignment

标准任务和量化计算验证显示较少积分步与较好质量；支持 RFM 的效率与灵活性，但无法单独识别收益来自 flow、几何还是 base。

## 6. Hidden assumptions

选定流形与度量符合科学等价关系；短路径有利于泛化；ODE 数值误差不会改变不同方法的公平比较。

## 7. Strongest alternative explanation

增益可能主要来自更好的 base distribution、solver 或训练超参，而非 Riemannian flow matching 本身。

## 8. Missing baseline

同一 base 与 backbone 下的 diffusion/flow；同一函数评估次数下的 solver；简单检索 base 加局部修复。

## 9. Killer experiment

固定 base、网络和 NFE，只替换概率路径；再固定路径只替换 base。若优势集中在 base，则论文应被解释为初始化分布工作。

## 10. Contribution type

将通用流形 flow matching 扎实迁移到晶体，属于机制与效率贡献。

首轮角色：几何机制。历史六维记录：[1, 2, 2, 2, 1, 0]。

## 11. Transferable abstraction

最重要抽象是“生成难度取决于源分布、目标分布和连接路径三者”，这为 LLM proposal、轨迹 bridge 和多盆地 base 提供接口。

## 12. Final verdict

是现代晶体流模型的重要基础，但其 CSP 评价仍继承单参考任务局限。

首轮使用建议：作为 Flow/SI/LLM 混合方法的统一基线和 base-distribution 研究平台。

具体结论范围：不能把积分步少直接等同于总计算成本低，也不能由终点质量推断模型探索了势能面。

### 首轮留下的后续问题

对比高斯、检索、LLM、盆地分层 base，在相同 NFE 与弛豫预算下测低能盆地覆盖。
