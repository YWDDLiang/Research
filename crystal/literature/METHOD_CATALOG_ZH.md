# 方法与来源目录

截至2026年10月9日：69条记录，去重68项工作。C18与P21是同一UniWorld-V2/Edit-R1工作的两个视角。三条方法线中37项选读到方法或结果；评价补充另列读深度。

完整字段见[catalog_records.json](catalog_records.json)，可筛选表见[method_catalog.csv](method_catalog.csv)。本表保留原始身份标签；published_main_conference表示已核正式主会，preprint表示预印本，作者报告录用与独立会议核实分开。

## 基础生成与表示

| ID | 工作与原始来源 | 日期／会议状态 | 实际任务 | 核心挑战 |
|---|---|---|---|---|
| F01 | [Diffusion Transformers with Representation Autoencoders](https://arxiv.org/html/2510.11690v1) | 2025-10-13；ICLR 2026；published_main_conference | ImageNet类别条件；无T2I主实验 | 重建训练的窄VAE latent缺少语义结构；高维表示又难去噪。 |
| F02 | [Scaling Text-to-Image Diffusion Transformers with Representation Autoencoders](https://arxiv.org/html/2601.16208v1) | 2026-01-22；preprint | 真正自由文本T2I；GenEval、DPG；0.5B–9.8B DiT | ImageNet的RAE优势能否扩展到开放词汇、文字和大模型。 |
| F03 | [REPA-E: Unlocking VAE for End-to-End Tuning with Latent Diffusion Transformers](https://arxiv.org/abs/2504.10483) | 2025-04-14；ICCV 2025；published_main_conference | ImageNet；MSCOCO T2I扩展和2025-10 T2I-VAE发布 | 固定tokenizer限制生成；标准扩散损失直接联合训练会退化。 |
| F04 | [Semantics Lead the Way: Harmonizing Semantic and Texture Modeling with Asynchronous Latent Diffusion](https://arxiv.org/html/2512.04926v1) | 2025-12-04；CVPR 2026；published_main_conference | ImageNet类别条件；无T2I主实验 | 语义先于纹理形成，同步联合去噪未利用这一顺序。 |
| F05 | [Latent Denoising Makes Good Tokenizers](https://arxiv.org/html/2507.15856v1) | 2025-07-21；ICLR 2026；published_main_conference | ImageNet；最终版包含MSCOCO T2I | 好的重建latent不一定能从噪声/缺失状态被生成模型恢复。 |
| F06 | [There is No VAE: End-to-End Pixel-Space Generative Modeling via Self-Supervised Pre-training](https://arxiv.org/html/2510.12586v3) | 2025-10-14；ICLR 2026；published_main_conference | ImageNet类别条件；pixel diffusion与consistency；无T2I | pixel生成要同时学语义和细节，强噪声上普通SSL容易崩。 |
| F07 | [Back to Basics: Let Denoising Generative Models Denoise](https://arxiv.org/html/2511.13720v1) | 2025-11-17；CVPR 2026；published_main_conference | ImageNet256/512/1024类别条件；无T2I主实验 | 高维噪声/速度目标需要拟合非数据流形；有限容量大patch模型困难。 |
| F08 | [PixelDiT: Pixel Diffusion Transformers for Image Generation](https://arxiv.org/html/2511.20645v1) | 2025-11-25；CVPR 2026；published_main_conference | ImageNet类别条件；真正1024×1024 T2I | autoencoder丢失细节并隔断端到端优化；直接像素计算大。 |
| F09 | [PixelDiT2: Representation-Grounded Pixel Diffusion Transformers](https://arxiv.org/html/2609.24919v1) | 2026-09-21；NeurIPS 2026；author_reported_accepted_upcoming_official_poster_not_verified | ImageNet类别条件；无T2I主实验 | pixel模型缺乏显式表示先验，表示学习与像素生成互相拖累。 |
| F10 | [An Empirical Study of Training Pixel-Space Text-to-Image Diffusion Models](https://arxiv.org/html/2608.16887v1) | 2026-08-17；preprint | 真正大规模自由T2I；GenEval、DPG | ImageNet pixel配方在大型T2I是否同样高效。 |
| F11 | [NextStep-1: Toward Autoregressive Image Generation with Continuous Tokens at Scale](https://arxiv.org/html/2508.10711v1) | 2025-08-14；ICLR 2026；published_main_conference | 真正T2I、编辑与图文交错 | 离散VQ损失信息；重型整图diffusion削弱统一AR优势。 |
| F12 | [D-AR: Diffusion via Autoregressive Models](https://arxiv.org/abs/2505.23660) | 2025-05-29；ICLR 2026；published_main_conference | ImageNet类别条件、部分token预览和布局；无T2I主实验 | 展平图像patch缺乏自然因果顺序。 |
| F13 | [DC-AR: Efficient Masked Autoregressive Image Generation with Deep Compression Hybrid Tokenizer](https://arxiv.org/html/2507.04947v1) | 2025-07-07；ICCV 2025；published_main_conference | 真正T2I；MJHQ30k、GenEval | 高压缩VQ难保细节；纯连续MAR又需很多步骤。 |
| F14 | [CaTok: Taming Mean Flows for One-Dimensional Causal Image Tokenization](https://arxiv.org/pdf/2603.06449) | 2026-03-06；CVPR 2026；published_main_conference | ImageNet重建/类别AR；无T2I主实验 | 人为1D顺序、全token条件decoder与NTP因果性冲突；nested dropout失衡。 |
| F15 | [Generation then Reconstruction: Accelerating Masked Autoregressive Models via Two-Stage Sampling](https://arxiv.org/html/2510.17171v1) | 2025-10-20；ICLR 2026；published_main_conference | ImageNet MAR；LightGen7B真正T2I | 空间相关token同一步建模困难，统一计算浪费在容易补全的区域。 |
| F16 | [Mean Flows for One-step Generative Modeling](https://arxiv.org/abs/2505.13447) | 2025-05-19；NeurIPS 2025；published_main_conference | ImageNet类别条件；无T2I主实验 | 瞬时速度必须多步积分；单步并非换采样步数即可。 |
| F17 | [Improved Mean Flows: On the Challenges of Fastforward Generative Models](https://arxiv.org/html/2512.02012v1) | 2025-12-01；CVPR 2026；published_main_conference | ImageNet类别条件；无T2I主实验 | 原MF目标自依赖，JVP使用未观测条件速度；CFG训练定死。 |
| F18 | [One-step Latent-free Image Generation with Pixel Mean Flows](https://arxiv.org/html/2601.22158v2) | 2026-01-29；ICML 2026；published_main_conference | ImageNet类别条件；无T2I主实验 | 像素高维与一步跨度同时要求过高容量。 |
| F19 | [Generative Modeling via Drifting](https://arxiv.org/html/2602.04770v2) | 2026-02-04；preprint | ImageNet类别条件latent/pixel；无T2I主实验 | 推理反复演化样本昂贵；端到端直接生成缺少分布移动信号。 |
| F20 | [Bidirectional Normalizing Flow: From Data to Noise and Back](https://arxiv.org/html/2512.10953v1) | 2025-12-11；CVPR 2026；published_main_conference | ImageNet类别条件；无T2I主实验 | 精确解析逆的因果解码限制NF采样速度和架构。 |

## 条件控制与推理

| ID | 工作与原始来源 | 日期／会议状态 | 实际任务 | 核心挑战 |
|---|---|---|---|---|
| C01 | [LightBagel: A Light-weighted, Double Fusion Framework for Unified Multimodal Understanding and Generation](https://arxiv.org/abs/2510.22946) | 2025-10-27（首稿）；预印本；看到ICLR 2026投稿材料，但未核实正式接收记录 | 真实T2I、图像编辑、多模态理解 | 强VLM与DiT各自有效，但只传递VLM末层语义会压缩空间细节，重新统一预训练又昂贵。 |
| C02 | [Think-Then-Generate: Reasoning-Aware Text-to-Image Diffusion with LLM Encoders](https://proceedings.mlr.press/v306/kou26b.html) | 2026-01-15（首稿）；ICML 2026主会，PMLR 306:60480–60494 | 真实T2I；另有推理编辑扩展 | LLM文本编码器被当作静态特征提取器，能表达事实不代表条件适合DiT执行。 |
| C03 | [ThinkGen: Generalized Thinking for Visual Generation](https://arxiv.org/abs/2512.23568) | 2025-12-29（首稿）；CVPR 2026主会 | 真实T2I、文字渲染、编辑、参考条件生成与反思 | 统一模型的CoT可能仅帮助某类知识任务，却扰乱长提示、组合或文字渲染。 |
| C04 | [Interleaving Reasoning for Better Text-to-Image Generation（IRG）](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ad48f017e6c3d474caf511208e600459-Abstract-Conference.html) | 2025-09-08（首稿早于窗口；近一年主会谱系补充）；ICLR 2026主会 | 真实T2I，经初始生成再编辑细化 | 先写完想法再出图的流程无法观察渲染出的细节错误。 |
| C05 | [Show, Don’t Tell: Morphing Latent Reasoning into Image Generation（LatentMorph）](https://proceedings.mlr.press/v306/chen26fv.html) | 2026-02-02（首稿）；ICML 2026主会，PMLR 306:17940–17959 | 真实T2I；Janus-Pro自回归图像token主实验 | 生成隐藏状态不易被理解分支读取，理解隐藏状态也不能直接改变下一图像token；频繁图像/文字decode-encode额外丢失信息。 |
| C06 | [Hint2Gen: Bridging Understanding and Generation via Code-structured Hints](https://openaccess.thecvf.com/CVPR2026?day=2026-06-07) | 2026-06（主会公开；未核实更早首稿日）；CVPR 2026主会，36593–36603 | 主要是问题图+指令的推理生成/编辑；不以纯开放域T2I结果替代它 | 模型能用符号解决迷宫/拼装等任务，却难把解答落实在指定图像位置。 |
| C07 | [3D Space as a Scratchpad for Editable Text-to-Image Generation](https://arxiv.org/abs/2601.14602) | 2026-01-21（首稿）；CVPR 2026主会 | 真实T2I；支持生成后3D编辑 | 2D框和文本难表示朝向、遮挡、深度与相对尺度，也难维持编辑对象身份。 |
| C08 | [CTCal: Rethinking Text-to-Image Diffusion Models via Cross-Timestep Self-Calibration](https://arxiv.org/abs/2603.20741) | 2026-03-21（首稿）；CVPR 2026主会 | 真实T2I：绑定、空间、计数 | 同一图文对在高噪声时缺少可靠实体-空间对应；标准去噪损失间接监督绑定，多个主体响应又不均。 |
| C09 | [Guiding Diffusion Models with Semantically Degraded Conditions（CDG）](https://arxiv.org/abs/2603.10780) | 2026-03-11（首稿）；CVPR 2026主会 | 真实T2I；训练外条件引导 | 完整提示与null的差可能同时推动一般去噪和语义变化，对细粒度条件的分辨不足。 |
| C10 | [DynFusion: Rethinking Condition Fusion for Adaptive Multi-Conditional Text-to-Image Generation](https://wrap.warwick.ac.uk/id/eprint/197869/) | 2026-03-03（大学归档；主会2026-06）；CVPR 2026主会；大学保存正式版本 | 文本+depth/edge/subject/background多条件T2I | 静态叠加异质条件会产生冗余和相互冲突，条件强度需求又随时间、任务、层变化。 |
| C11 | [Scone: Bridging Composition and Distinction in Subject-Driven Image Generation via Unified Understanding-Generation Modeling](https://arxiv.org/abs/2512.12675) | 2025-12-14（首稿）；CVPR 2026主会Highlight；官方节目与作者repo确认 | 参考条件新图生成；主体选择与多主体组合 | 参考图里有多个候选，能组合参考图不代表能选对指令要求的主体；背景和非目标主体会串入结果。 |
| C12 | [ContextGen: Contextual Layout Anchoring for Identity-Consistent Multi-Instance Generation](https://proceedings.iclr.cc/paper_files/paper/2026/hash/9b01b79449b54c24ead5725e14affa79-Abstract-Conference.html) | 2025-10-13（首稿）；ICLR 2026主会 | 文本+布局+多参考的新图生成；不是纯文本输入 | 拼接layout压缩了细节，重叠遮挡丢失身份；独立reference又易串扰。 |
| C13 | [Disentangling to Re-couple: Resolving the Similarity-Controllability Paradox in Subject-Driven Text-to-Image Generation（DisCo）](https://arxiv.org/abs/2604.00849) | 2026-04-01（首稿）；CVPR 2026主会；官方节目确认 | reference+文本修改的新图生成/主体驱动编辑 | 提示同时描述身份与情境会与具体reference冲突；严格分开后又可能像贴图、不融于新环境。 |
| C14 | [WithAnyone: Toward Controllable and ID Consistent Image Generation](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d432fbe4877ee1a6a51632a18e69784f-Abstract-Conference.html) | 2025-10-16（首稿）；ICLR 2026主会 | 单/多人身份参考+文本的新图生成；编辑变体独立 | 单图重建训练把同身份误学成同姿态/光照拷贝，身份相似与可控变化互相拉扯。 |
| C15 | [StyleComposer: Training-Free Multi-Reference Style Composition](https://arxiv.org/abs/2608.05213) | 2026-08-05（首稿）；预印本；官方实验室仍标arXiv | 文本+颜色/纹理/结构reference的新图生成 | 同一style embedding混合颜色、纹理、结构，强化某参考会把不需要的内容一并迁移。 |
| C16 | [Qwen-Image-Layered: Towards Inherent Editability via Layer Decomposition](https://openaccess.thecvf.com/content/CVPR2026/html/Yin_Qwen-Image-Layered_Towards_Inherent_Editability_via_Layer_Decomposition_CVPR_2026_paper.html) | 2025-12-17（首稿）；CVPR 2026主会 | 主模型image-to-RGBA-layers；论文另含text-to-RGBA、text-to-layers训练与结果 | 全部内容在单画布纠缠，修改局部会让非目标内容漂移；局部编辑要求可独立操作的对象。 |
| C17 | [Masked Region Transformer for Layered Image Generation and Editing at Scale（MRT）](https://openaccess.thecvf.com/content/CVPR2026/html/Tang_Masked_Region_Transformer_for_Layered_Image_Generation_and_Editing_at_CVPR_2026_paper.html) | 2026-06（主会；首稿月份2026-05）；CVPR 2026主会 | text-to-layers、image-to-layers、layers-to-layers | 层数多时每层整幅画布token成本高，画布外对象内容缺失又妨碍移动与重用。 |
| C18 | [UniWorld-V2 / Edit-R1: Reinforce Image Editing with Diffusion Negative-aware Finetuning and MLLM Implicit Feedback](https://arxiv.org/abs/2510.16888) | 2025-10-19（首稿）；预印本；该轮未核实正式主会接收 | 指令图像编辑；不把编辑基准总分当纯T2I | 编辑指令差异大，SFT易只复刻已有修改；普适编辑奖励难，MLLM离散判断噪声大。 |
| C19 | [The Consistency Critic: Correcting Inconsistencies in Generated Images via Reference-Guided Attentive Alignment（ImageCritic）](https://openaccess.thecvf.com/content/CVPR2026/html/Ouyang_The_Consistency_Critic_Correcting_Inconsistencies_in_Generated_Images_via_Reference-Guided_CVPR_2026_paper.html) | 2025-11-25（首稿）；CVPR 2026主会 | 已有生成结果的reference-guided后编辑 | 主体大体正确，文字/logo等局部细节仍不一致；整图重生会改变已正确部分。 |
| C20 | [Swift-Image: Exploring the Performance Frontier of Compact Unified Image Generation Models（v2标题省略Swift-Image前缀）](https://arxiv.org/abs/2608.20334) | 2026-08-20（首稿）；2026-08-21 v2；预印本技术报告 | 真实T2I、单图与多图编辑；此处统一生成/编辑而非理解问答统一 | 模型紧凑时，多种生成/编辑与后训练目标相互干扰；复杂用户请求需要转为可渲染说明。 |

## 反馈与推理计算

| ID | 工作与原始来源 | 日期／会议状态 | 实际任务 | 核心挑战 |
|---|---|---|---|---|
| P01 | [Flow-GRPO: Training Flow Matching Models via Online RL](https://proceedings.neurips.cc/paper_files/paper/2025/hash/3a10c46572628d58cb44fb705f25cbbf-Abstract-Conference.html) | 2025-05初稿；2025-12主会；NeurIPS 2025主会 | 文生图组合性、OCR、偏好 | 确定性flow缺少逐步探索和可用转移似然 |
| P02 | [DiffusionNFT: Online Diffusion Reinforcement with Forward Process](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d8e68ddfe22520b45b8fb8d5cbde5a21-Abstract-Conference.html) | 2025-09-19初稿；2026主会；ICLR 2026主会Oral；原稿在窗口前，按正式主会纳入 | 文生图后训练 | 逐步似然与采样器限制使flow强化学习昂贵 |
| P03 | [GDRO: Group-level Reward Post-training Suitable for Diffusion Models](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_GDRO_Group-level_Reward_Post-training_Suitable_for_Diffusion_Models_CVPR_2026_paper.html) | 2026-01-05初稿；2026-06主会；CVPR 2026主会 | FLUX.1-dev OCR/GenEval | 在线rollout占训练成本；排名变好不保证优样本似然变高 |
| P04 | [Compositional Text-to-Image Generation Via Region-aware Bimodal Direct Preference Optimization](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Compositional_Text-to-Image_Generation_Via_Region-aware_Bimodal_Direct_Preference_Optimization_CVPR_2026_paper.html) | 2026-06正式主会；CVPR 2026主会 | 属性绑定/关系/计数 | 全图偏好被无关像素和文本错误混淆 |
| P05 | [TDM-R1: Reinforcing Few-Step Diffusion Models with Non-Differentiable Reward](https://proceedings.mlr.press/v306/luo26j.html) | 2026-03-08初稿；2026-07主会；ICML 2026主会 | 1/4步文生图、OCR、偏好 | 少步直接奖励加权去噪容易模糊；非微分reward无法直接反传 |
| P06 | [Reinforce Adjoint Matching](https://arxiv.org/html/2605.10759v1) | 2026-05-11 v1；预印本；未确认正式会议 | SD3.5-M组合/OCR/偏好后训练 | 精确控制目标会引入高方差/长轨迹VJP |
| P07 | [DRM: Diffusion-based Reward Model With Step-wise Guidance](https://arxiv.org/html/2605.25661v1) | 2026-05-25初稿；2026-06主会；CVPR 2026主会（CVF论文记录和官方仓库） | 噪声态偏好评分、Step-GRPO、逐步采样 | VLM语义表示遗漏感知品质；终点奖励credit粗 |
| P08 | [Beyond VLM-Based Rewards: Diffusion-Native Latent Reward Modeling](https://arxiv.org/html/2602.11146v1) | 2026-02-11 v1；预印本；未确认正式会议 | 潜空间偏好模型/对齐 | 像素VLM评分昂贵且latent-domain不匹配 |
| P09 | [Sample-Adaptive Latent Rewards for Uncertainty-Guided Diffusion Post-Training](https://arxiv.org/html/2608.06125v1) | 2026-08-06 v1；预印本；未确认正式会议 | SURE-LRM潜奖励和置信度 | 同一噪声级样本可有不同评分可靠性 |
| P10 | [Understanding Reward Hacking in Text-to-Image Reinforcement Learning](https://arxiv.org/html/2601.03468v1) | 2026-01-06初稿；2026-06程序列出主会；CVPR 2026主会（官方program佐证）；深读arXivv1 | T2I奖励盲区与ArtifactReward | 偏好/检测/VQA高分可能奖励不真实结构 |
| P11 | [Beyond the Dirac Delta: Mitigating Diversity Collapse in Reinforcement Fine-Tuning for Versatile Image Generation](https://arxiv.org/html/2601.12401v1) | 2026-01-18 v1；预印本；未确认正式会议 | DRIFT质量/多样性Pareto | 单目标强化会集中到少数高分输出 |
| P12 | [Multi-Axis Max@K Reinforcement Learning for Representative Diversity in Text-to-Image Generation](https://arxiv.org/html/2607.14962v1) | 2026-07-16 v1；预印本；未确认正式会议 | 预定义模式覆盖、race5及race5×gender2外观分类 | 单样本高分和feature差异不能保证特定稀有模式出现 |
| P13 | [PromptRL: Prompt Matters in RL for Flow-Based Image Generation](https://proceedings.mlr.press/v306/wang26kl.html) | 2026-02-01初稿；2026-07主会；ICML 2026主会 | 语言改写器+图像flow共同RL | prompt phrasing过拟合和组内多样性减少 |
| P14 | [Diffusion Tree Sampling: Scalable inference-time alignment of diffusion models](https://proceedings.neurips.cc/paper_files/paper/2025/file/d6484394c4cb5e1f4ecad8d90b912025-Paper-Conference.pdf) | 2025-06-25初稿；2025-12主会；NeurIPS 2025主会 | DTS分布采样与DTS*高reward搜索 | 噪声态clean估计reward有偏；旧轨迹计算丢失 |
| P15 | [Test-Time Scaling of Diffusion Models via Noise Trajectory Search](https://openreview.net/pdf?id=fnkkY7UGRl) | 2025-05/06初稿；2025-12主会；NeurIPS 2025主会 | EDM/Stable Diffusion噪声轨迹搜索 | 增加去噪步收益饱和；MCTS全搜索昂贵 |
| P16 | [Inference-Time Scaling of Discrete Diffusion Models via Importance Weighting and Optimal Proposal Design](https://proceedings.iclr.cc/paper_files/paper/2026/hash/3df1eca840e82b11bbc33f68c773c38e-Abstract-Conference.html) | 2025-05-28初稿；2026主会；ICLR 2026主会 | 离散扩散SMC，包含T2I/语言/生物设计 | 粒子weights退化且proposal不合目标 |
| P17 | [Inference-Time Scaling of Diffusion Models via Progressive Seed Pruning](https://arxiv.org/html/2607.21591v1) | 2026-07 v1；2026 ECCV；ECCV 2026（官方repo声明，未另核会议程序） | SD1.5/SDXL/SD3.5 seed选择 | 固定粒子数浪费大量低潜力终程 |
| P18 | [Flash-BoN: Instant Drafts for Inference-Time Scaling in Diffusion Models](https://arxiv.org/html/2607.04461v1) | 2026-07-05初稿；2026 ECCV；ECCV 2026（官方repo声明） | 廉价draft、多阶段验证、完整refinement | 只算NFE隐藏verifier开销 |
| P19 | [Enhanced Text-to-Image Generation by Fine-grained Multimodal Reasoning](https://arxiv.org/html/2604.13491v1) | 2026-04-15 v1；预印本；未确认正式会议 | FiMR显式反馈与局部自修正 | 整图judge遗漏细小约束，语言rationale可能被decoder绕过 |
| P20 | [RewardFlow: Generate Images by Optimizing What You Reward](https://openaccess.thecvf.com/content/CVPR2026/html/Susladkar_RewardFlow_Generate_Images_by_Optimizing_What_You_Reward_CVPR_2026_paper.html) | 2026-04-09初稿；2026-06主会；CVPR 2026主会 | 训练无关文生图/局部编辑 | 局部要求与整体品质多目标耦合 |
| P21 | [Uniworld-V2: Reinforce Image Editing with Diffusion Negative-aware Finetuning and MLLM Implicit Feedback](https://arxiv.org/html/2510.16888v1) | 2025-10-19 v1；技术预印本；仓库现名Edit-R1 | 通用指令编辑 | 多任务无统一reward，MLLM分数噪声影响更新 |
| P22 | [GRPO-Guard: Mitigating Implicit Over-Optimization in Flow Matching via Regulated Clipping](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_GRPO-Guard_Mitigating_Implicit_Over-Optimization_in_Flow_Matching_via_Regulated_Clipping_CVPR_2026_paper.html) | 2025-10-25初稿；2026-06主会；CVPR 2026主会 | flow在线RL更新稳定性 | 时间相关ratio/clipping失衡，代理reward涨而其它质量降 |

## 评价与泛化

| ID | 工作与原始来源 | 日期／会议状态 | 实际任务 | 核心挑战 |
|---|---|---|---|---|
| E01 | [GenEval 2: Addressing Benchmark Drift in Text-to-Image Evaluation](https://arxiv.org/html/2512.16853v1) | 2025-12-18；预印本；本轮未确认最终会议状态 | 真实文生图评测 | 评价器随输出分布变化偏离人工判断 |
| E02 | [Benchmarking Diversity in Image Generation via Attribute-Conditional Human Evaluation](https://arxiv.org/html/2511.10547v1) | 2025-11-13；预印本；本轮未确认最终会议状态 | 文生图集合多样性评价 | 整体距离混合内容差异与有意义属性变化 |
| E03 | [When Pretty Isn't Useful: Investigating Why Modern Text-to-Image Models Fail as Reliable Training Data Generators](https://arxiv.org/html/2602.19946v1) | 2026-02；CVPR 2026 主会，CVF正式版本已核对 | 文生图合成数据的下游用途 | 视觉质量进步没有同步改善合成数据训练价值 |
| E04 | [GenExam: A Multidisciplinary Text-to-Image Exam](https://arxiv.org/html/2509.14232v5) | 2025-09；ICML 2026；官方会议目录与作者仓库已核对 | 知识和约束密集的绘图考试 | 视觉观感难代表技术绘图正确性 |
| E05 | [WISE: A World Knowledge-Informed Semantic Evaluation for Text-to-Image Generation](https://arxiv.org/html/2503.07265v2) | 2025-03；作者官方仓库标注ICML 2026；首次稿件早于窗口 | 知识密集的文生图评价 | 显式词语匹配不足以实现隐含知识 |
| E06 | [Local Mechanisms of Compositional Generalization in Conditional Diffusion](https://arxiv.org/html/2509.16447v1) | 2025-09-19；ICML 2026 主会，PMLR正式记录已核对 | 受控CLEVR组合泛化；自然图像机制探索 | 熟悉概念的新组合何时能被生成 |
| E07 | [NAMESAKES: Probing Identity Memorization in Text-to-Image Models](https://arxiv.org/html/2606.20155v1) | 2026-06-18；预印本；本轮未确认正式会议状态 | 人脸身份记忆探测 | 仅凭外观难区分记忆与泛化 |
