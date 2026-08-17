# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-08-17 06:25:25 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [Designing Reinforcement Learning for Diffusion Models: A Unified Path-Space View](https://arxiv.org/abs/2608.14430v1)

**Authors**: Yixian Xu, Yuanrui Zhang, Shengjie Luo, Liwei Wang, Di He  
**Category**: cs.LG  
**Published**: 2026-08-17  
**Score**: 91.0  
**Type**: new  
**ArXiv ID**: 2608.14430v1  

#### Abstract
Reinforcement learning (RL) post-training provides a direct way to align diffusion models with human preferences and task-specific rewards. However, current RL algorithms for diffusion models remain fragmented: reverse-trajectory methods rely on discretized likelihood ratios, whereas forward-matchin...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Designing Reinforcement Learning for Diffusion Models: A Unified Path-Space View
1. 论文的主要贡献和创新点
✅ 解决的问题：现有扩散模型的RL后训练方法存在碎片化问题，分为reverse-trajectory类（依赖离散似然比）和forward-matching类（基于奖赏标注的加噪rollout样本训练），两类方法原理不同，缺乏统一的理论框架。
🚀 提出的新方法与思路
**正则化Diffusion-RL统一目标推导**：从正则化的扩散-RL目标出发，利用采样SDE间的重要性采样，得到轨迹空间的显式策略梯度估计，该估计包含Flow-GRPO类更新的随机Itô积分。
**统一设计空间构建**：推导等价的降方差值梯度形式，证明其可还原AWM、DiffusionNFT等前向匹配方法的结构，将两类方法的差异归结为方差减少效应，提出由值梯度估计、权重函数、采样选择组织的统一设计空间。
**多样本KDE值梯度与尺度有界权重族**：提出可复用rollout组的多样本KDE值梯度估计，及能保留稳定现有配方、排除奇异情况的尺度有界权重族。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 理论统一性 | 揭示两类diffusion-RL方法的核心差异为方差减少效应，构建了统一的路径空间视角下的设计框架 |
| 性能潜力 | 提出的新方法优于现有diffusion-RL基线（论文未报告具体定量数值） |
| 稳定性 | 提出的尺度有界权重族可排除奇异情况，保留稳定现有配方 |
2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：任务为将扩散模型与人类偏好、任务特定奖赏对齐，评估指标论文未报告
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| reverse-trajectory类RL方法 | 轨迹后验似然比方法 | 依赖离散似然比 |
| forward-matching类RL方法（如AWM、DiffusionNFT） | 前向匹配奖赏标注方法 | 训练基于奖赏标注的加噪rollout样本 |
3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体的表格数据及定量数值，仅在SD3.5-M和Qwen-Image模型上验证了方差减少解释，且提出的配方优于现有diffusion-RL基线。
4. 关键结论和发现
- 主要发现：1. 现有diffusion-RL两类方法的差异并非源于RL原理，而是方差减少效应；2. 推导得到的统一路径空间目标能整合两类方法，构建了可扩展的diffusion-RL设计空间；3. 提出的多样本KDE值梯度估计与尺度有界权重族可提升方法性能与稳定性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文从统一的路径空间视角统一了扩散模型强化学习的两类碎片化方法，揭示其本质差异为方差减少效应，提出新的估计器与权重族并验证其有效性。

</details>

---

### 2. [Beyond Capacity: Scalable MoE LLM Inference via High-Bandwidth Flash with Direct GPU and HBM Paths](https://arxiv.org/abs/2608.14333v1)

**Authors**: Seeyeon Kim, Juhyeong Jin, Joo-Young Kim  
**Category**: cs.AR  
**Published**: 2026-08-17  
**Score**: 68.5  
**Type**: new  
**ArXiv ID**: 2608.14333v1  

#### Abstract
Modern mixture-of-experts (MoE) language models increasingly strain the capacity and cost efficiency of high-bandwidth memory (HBM), as rapidly growing expert weights must be provisioned close to GPUs. High-bandwidth flash (HBF) offers substantially greater capacity, but conventional designs typical...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# Beyond Capacity: Scalable MoE LLM Inference via High-Bandwidth Flash with Direct GPU and HBM Paths
---
## 1. 论文的主要贡献和创新点
✅ 解决的问题：现代MoE LLM的专家权重快速增长，给高带宽内存（HBM）的容量和成本效率带来巨大压力；传统高带宽闪存（HBF）设计通过HBM向GPU传输HBF中的专家权重，未充分利用直接的GPU-HBF连接，导致专家权重传输效率受限且存在潜在瓶颈。
🚀 提出的新方法与思路
**双并行专家传输路由架构**：同时启用两条独立的专家权重传输路径（HBF→GPU直接路径、HBF→HBM基底→GPU中继路径），将完整专家分配至其中一条路径，双路径并发传输，无需复制专家权重，也无共享中继瓶颈。
**提前专家判定机制**：在专家常规执行点前识别即将使用的专家，让HBF读取延迟与前置计算操作重叠，隐藏存储延迟。
**权重与缓存分离管理**：对不可变的专家权重和可变的KV缓存数据独立管理，降低两类流量间的干扰。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 专家传输效率 | 并发双路径传输，无权重复制与中继瓶颈，传输效率更高 |
| 端到端性能 | 优于仅使用单一路径（HBM中继）的传统设计 |
---
## 2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：任务为MoE LLM推理服务，评估指标及含义如下：
| 指标 | 含义 |
| ---- | ---- |
| 吞吐量 | 单位时间处理的请求量，↑ 越高越好 |
| 端到端加速比 | 处理速度提升倍数，↑ 越高越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| HBM中继路径设计 | 基线方法 | 仅通过HBF→HBM→GPU单一路径传输专家权重，未利用直接GPU-HBF连接 |
---
## 3. 主要实验结果和性能指标
📊 定量结果汇总
提及的性能提升未明确对应表号，故按摘要结论呈现：
💡 结论：在代表性MoE工作负载下，所提双路径并发设计的吞吐量和端到端加速比均优于仅采用HBM中继路径的设计。
其他实验类别（主benchmark性能、效率对比、跨域迁移、鲁棒性测试、消融实验）：论文未报告
---
## 4. 关键结论和发现
- 主要发现：1. 并发使用直接与中继双路径可提升专家权重传输效率，优于单一传输路径；2. 提前专家判定机制可隐藏HBF读取延迟，缓解计算与存储干扰；3. 专家权重与KV缓存的分离管理可降低不同流量类别的干扰，提升整体性能。
- 方法局限性：论文未报告
- 未来工作：论文未报告
---
> ✅ **总结一句话**：该论文提出结合双并行专家传输路由、提前专家判定及流量分离管理的MoE LLM推理架构，缓解了HBM容量与成本压力下的专家权重传输效率问题，在代表性工作负载下实现了优于传统设计的性能表现。

</details>

---

### 3. [MoE Expert Execution in Disaggregated LLM Serving with a High-Bandwidth ReRAM Near-Memory Architecture](https://arxiv.org/abs/2608.13962v1)

**Authors**: Kunming Shao, Ming Zeng, Xin Yuan, Binbin Liao, Yangming Zhang, Wei Wang, Tim Kwang-Ting Cheng, Chi-Ying Tsui  
**Category**: cs.AR  
**Published**: 2026-08-17  
**Score**: 67.5  
**Type**: new  
**ArXiv ID**: 2608.13962v1  

#### Abstract
Attention-FFN disaggregation maps LLM modules to specialized pools, creating an opening to keep Mixture-of-Experts (MoE) weights resident in a high-bandwidth FFN pool. Decode SLOs, however, cap the run-batch while sparse routing expands the activated-expert union, so weight traffic amortizes poorly ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

MoE Expert Execution in Disaggregated LLM Serving with a High-Bandwidth ReRAM Near-Memory Architecture
1. 论文的主要贡献和创新点
✅ 解决的问题：在Attention-FFN解聚的LLM服务架构中，Mixture-of-Experts（MoE）权重驻留高带宽FFN池时，Decode服务质量目标（SLO）限制运行批规模，稀疏路由扩大激活专家联合导致权重流量分摊效果差、路由倾斜引发冷专家资源空闲，同时需在无全局共享fabric的前提下，让FFN池满足稀疏联合下的带宽密度要求并恢复资源占用；现有以H20为代表的方案存在权重移动能量高、FFN池延迟高等缺陷。
🚀 提出的新方法与思路
**ReRAM Near-Memory Expert Weight Resident Design**：将MoE权重驻留在高带宽的ReRAM近存架构中，通过本地读取实现高带宽访问，适配FFN池的带宽需求。
**MFU Decomposition**：将实际MoE利用率（MFU）拆解为理想MFU与资源占用两个维度，为优化提供明确方向。
**Side-4 Bounded Core-Local Multicast Pooling**：采用side-4的受限核心本地组播池化策略，恢复FFN池的资源占用效率。
**Coactivation-Aware Placement & Load-Aware Fetch**：通过感知共激活的专家放置策略和感知负载的取数策略，进一步优化资源利用与访问效率。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| FFN池延迟 | 相比H20方案大幅降低 |
| 权重移动能量 | 相比H20方案显著降低 |
| 解码每输出符时间（TPOT） | 相比同构H20池大幅下降 |
| FFN池资源占用 | 经side-4池化后得到明显提升 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未明确报告具体数据集名称 | 用于支撑论文所述的MoE专家执行性能研究 |
🎯 实验设置与评估指标
任务：解聚LLM服务中的MoE专家执行性能评估；评估指标及含义：FFN池延迟（越低越好）、权重移动能量（越低越好）、解码TPOT（越低越好）、FFN池资源占用（越高越好）。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Homogeneous H20 pool | 基线方法 | 采用统一的H20架构作为FFN池的基准方案 |
| H20-attention + ReRAM-FFN system | 对比方案 | 注意力部分采用H20架构，FFN部分采用本文提出的ReRAM近存架构 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未明确报告各实验对应的表号、图号，仅在摘要中提及相关结果表述，无法定位具体数值来源，故按要求说明：
- 主 benchmark 性能（L2/碰撞率等）：论文未报告
- 效率对比（FPS / 参数量）：论文未报告
- 跨域 / zero-shot 迁移：论文未报告
- 鲁棒性 / 扰动测试：论文未报告
- 消融实验：论文未报告
（注：摘要中提及side-4 pooling提升FFN池资源占用、本文方案降低FFN池延迟与权重移动能量、混合架构降低解码TPOT，但因无明确图表编号，无法给出具体数值）
💡 结论（基于摘要提及结果）：论文提出的side-4池化策略可提升FFN池资源占用；在相同峰值计算资源下，本文方案的FFN池延迟和权重移动能量远优于H20方案；本文的混合架构解码吞吐量显著高于同构H20池。

4. 关键结论和发现
- 主要发现：Attention-FFN解聚架构中MoE的稀疏路由与SLO限制带来权重流量分摊差、资源空闲等问题，本文提出的ReRAM近存架构及相关优化策略可有效缓解这些问题，提升LLM服务性能。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：该论文针对解聚LLM服务中MoE专家执行的资源利用与性能瓶颈，提出基于ReRAM近存架构的优化方案，能有效提升FFN池资源占用、降低延迟与权重移动能量，显著提升解码吞吐量。

</details>

---

### 4. [GRPO Beyond English: A Large-Scale Study of GRPO in Non-English and Multilingual Settings](https://arxiv.org/abs/2608.13698v1)

**Authors**: Konstantin Dobler, Federico Scozzafava, Jonathan Janke, Mohamed Ali, Simon Lehnerer  
**Category**: cs.CL  
**Published**: 2026-08-17  
**Score**: 62.0  
**Type**: new  
**ArXiv ID**: 2608.13698v1  

#### Abstract
Reinforcement Learning with Verifiable Rewards (RLVR), often optimized with Group Relative Policy Optimization (GRPO), has become a central recipe for improving the reasoning capabilities of pretrained language models but current studies remain heavily English-centric. We conduct a large-scale empir...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：GRPO Beyond English: A Large-Scale Study of GRPO in Non-English and Multilingual Settings

1. 论文的主要贡献和创新点
✅ 解决的问题
现有基于Group Relative Policy Optimization（GRPO）的强化学习可验证奖励（RLVR）提升语言模型推理能力的研究存在严重的英语中心偏差，仅聚焦英语场景，缺乏针对非英语、多语言场景的大规模系统实证分析，无法明确GRPO在这些场景的表现规律与潜在问题。

🚀 提出的新方法与思路
**大规模多语言非英语GRPO实证研究框架**：从基座模型、训练语言、推理语言奖励等多维度，开展GRPO在非英语与多语言场景的大规模实证分析，系统性探究非英语场景下GRPO的推理表现、跨语言迁移特性及存在的问题。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 场景覆盖范围 | 突破现有GRPO研究的英语偏向，覆盖多语言、非英语场景 |
| 分析维度 | 从基座模型、训练语言、推理语言奖励等多维度系统性研究GRPO表现，提供更全面的规律洞察 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：论文未报告
⚔️ 基线方法对比：论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：
  1. 在母语中训练推理的表现，与在英语中训练推理的表现相比，仅存在较小的差距。
  2. GRPO存在较强的跨语言迁移特性，在某一种语言上进行训练，通常能提升其他多种语言的表现。
  3. GRPO的具体表现高度依赖于基座模型与语言，在部分情况下，在特定语言上进行训练会导致其他语言的域外能力出现严重退化。
- 方法局限性：非英语场景下的RLVR虽能提供广泛的跨语言增益，但需要进行全面评估以检测特定语言引发的退化问题，现有研究未充分开展此类全面评估。
- 未来工作：需进一步加强多语言GRPO的全面评估，避免语言相关的能力退化问题，完善非英语GRPO的系统性研究。

> ✅ **总结一句话**：该论文填补了GRPO研究中英语中心偏差的空白，通过大规模实证揭示了GRPO在非英语及多语言场景下的表现规律、跨语言迁移特性及潜在的语言相关退化问题。

</details>

---

### 5. [Batch-wise Adaptive Pruning: Periodic Neuron Activation-Aware Weight Pruning for Language Reasoning Model](https://arxiv.org/abs/2608.14003v1)

**Authors**: Yongmin Kim, Shota Takashiro, Yusuke Iwasawa, Takeshi Kojima, Yutaka Matsuo  
**Category**: cs.CL  
**Published**: 2026-08-17  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2608.14003v1  

#### Abstract
Large Reasoning Models (LRMs) achieve strong performance on complex tasks through extended chain-of-thought generation, but incur substantial computational costs during inference. In production settings, batched inference is essential for high throughput, yet the existing training-free adaptive prun...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Batch-wise Adaptive Pruning: Periodic Neuron Activation-Aware Weight Pruning for Language Reasoning Model
1. 论文的主要贡献和创新点
✅ 解决的问题
现有的训练-free自适应剪枝方法针对大推理模型（LRMs）设计，但在批量推理场景下存在核心矛盾：批量需共享单个剪枝掩码，现有方法聚合跨样本激活后采用阈值选择，然而离线校准的阈值与聚合后的激活分布不匹配，导致实际稀疏率偏离，推理任务准确率下降；而批量推理是生产环境中保障高吞吐量的关键需求，因此该缺陷亟需解决。

🚀 提出的新方法与思路
**Periodic top-k selection over aggregated importance scores**：替换阈值选择方式，对聚合后的重要性分数采用周期性top-k选择，不受聚合诱导的激活分布偏移影响，且按更新周期执行一次选择而非每token选择，保留推理加速效果。
**Activation memory**：基于重要神经元在长推理生成过程中会周期性重激活的观察，引入激活记忆模块，在更新阶段累积神经元的重要性，从而保留重复出现的重要神经元。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 批量推理下的任务性能 | 论文未报告 |
| 稀疏率控制 | 可实现符合目标的实际稀疏率 |
| 推理效率 | 可实现推理加速 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 用于验证方法在不同推理基准上的性能 |

🎯 实验设置与评估指标
任务为大语言推理模型的批量推理场景，评估指标涉及推理任务准确率、实际稀疏率、推理加速比。
| 指标 | 含义 |
| ---- | ---- |
| 推理任务准确率 | ↑ 越高越好 |
| 实际稀疏率 | 越接近目标稀疏率越好 |
| 推理加速比 | ↑ 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 现有训练-free自适应剪枝方法 | 自适应剪枝方法 | 聚合跨样本激活后采用阈值选择，在批量推理场景下因激活分布偏移导致性能下降 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告各实验对应的表号、图号等来源编号，因此无法提供具体定量结果，各实验模块内容如下：
1. 主 benchmark 性能：论文未报告
2. 效率对比：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. 现有训练-free自适应剪枝方法无法适配大推理模型的批量推理场景，核心问题在于激活分布偏移导致的实际稀疏率偏离和推理性能下降；2. 提出的Periodic top-k选择和Activation memory两个组件可有效解决批量推理下的剪枝性能缺陷；3. 该方法针对长推理生成中的周期性重激活神经元设计了保留机制，适配语言推理任务的特点。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：针对大推理模型批量推理中现有训练-free自适应剪枝方法的性能缺陷，提出了包含Periodic top-k选择和Activation memory的Batch-wise Adaptive Pruning方法，可在保证推理性能的同时实现高效的批量剪枝与推理加速。

</details>

---

### 6. [Second Thought: Reasoning in Parallel as LLM Agents Act and Observe](https://arxiv.org/abs/2608.13667v1)

**Authors**: Zhensu Sun, Chengran Yang, Yunbo Lyu, Jieke Shi, David Lo  
**Category**: cs.AI  
**Published**: 2026-08-17  
**Score**: 46.0  
**Type**: new  
**ArXiv ID**: 2608.13667v1  

#### Abstract
LLM agents in the ReAct paradigm alternate between reasoning, acting, and observing, but deliberate reasoning is confined to the Thought phase: while the agent serializes an action and waits for the environment, its reasoning is frozen. We identify this recurring interval for Action and Observation ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Second Thought: Reasoning in Parallel as LLM Agents Act and Observe
1. 论文的主要贡献和创新点
✅ 解决的问题
ReAct范式下的LLM代理仅在Thought阶段进行推理，Action和Observation阶段存在推理空闲窗口，串行推理模式导致资源浪费与效率低下。

🚀 提出的新方法与思路
**Second Thought**，是训练无的推理框架：在每个Thought阶段结束时分叉四个辅助分支，使其与主循环并发解码，待环境观察结果到达时合并生成的思考内容，将额外推理从主线程的顺序解码路径中移出。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
平均回合数 | 全部9组（模型，基准）组合中均实现降低
主线程解码量 | 在6组中最多降低43%（平均约20%），1组基本不变
Pass@1 | 在7组中无显著变化，2组分别提升12.4、10.2个百分点
计算匹配对比 | 在4组适用场景中，Pass@1更高，顺序解码量减少1.3到3.2

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
三个代理基准 | 评估LLM代理在多回合任务中的推理与执行表现

🎯 实验设置与评估指标
任务为评估ReAct范式下LLM代理的效率与性能，评估指标如下：
指标 | 含义
--- | ---
平均回合数 | ↓ 越低越好
主线程解码量 | ↓ 越低越好
Pass@1 | ↑ 越高越好

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
计算匹配对照组 | 控制组 | 将同等计算预算分配给主线程自身的推理，作为对比基准
ReAct范式 | 现有方法 | 串行执行Thought、Action、Observation，推理仅在Thought阶段进行

3. 主要实验结果和性能指标
**无对应表号的实验结果（来自论文摘要）**
| 指标 | 结果 |
| --- | --- |
| 9组（模型，基准）的平均回合数 | 全部降低 |
| 9组中6组的主线程解码量 | 最多降低43%，平均约20%，剩余1组基本不变 |
| 9组的Pass@1 | 7组无显著变化，2组分别提升12.4、10.2个百分点 |
| 计算匹配对比的4组场景 | Second Thought的Pass@1更高，顺序解码量减少1.3到3.2 |
💡 结论：摘要呈现的实验结果显示Second Thought在降低代理成本的同时，对核心指标Pass@1影响极小，部分场景下有正向提升。

4. 关键结论和发现
- 主要发现：① Second Thought可利用LLM代理Action、Observation阶段的推理空闲窗口，通过并行辅助推理优化代理性能与效率；② 相比计算匹配的控制组，Second Thought在全部4组适用场景中Pass@1更高、顺序解码量更少；③ 在多模型、多代理基准的测试中，Second Thought表现稳定。
- 方法局限性：论文未报告
- 未来工作：论文未报告
✅ **总结一句话**：本文提出的训练无框架Second Thought，通过并行利用LLM代理的推理空闲窗口，在不显著影响核心指标的前提下，有效降低了代理的平均回合数与主线程解码量，提升了推理效率。

</details>

---

### 7. [HI-MeshGraphNets: Efficient and Accurate Mesh-based Physics Learning with Hierarchical Multi-scale Graph Neural Networks](https://arxiv.org/abs/2608.13827v1)

**Authors**: SiHun Lee, Dong-Hyuk Park, Taesoo Bang, Seung-Hoon Kang  
**Category**: cs.LG  
**Published**: 2026-08-17  
**Score**: 45.5  
**Type**: new  
**ArXiv ID**: 2608.13827v1  

#### Abstract
Machine-learned physical surrogate models have become promising alternatives to mesh-based numerical solvers. Among them, graph neural networks (GNNs) are well suited for representing simulation meshes and learning nodal state evolution through message passing. However, conventional flat message pas...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

HI-MeshGraphNets: Efficient and Accurate Mesh-based Physics Learning with Hierarchical Multi-scale Graph Neural Networks
1. 论文的主要贡献和创新点
✅ 解决的问题
- 现有基于GNN的mesh类物理 surrogate模型（如MeshGraphNets）采用的flat message passing机制在大尺寸高保真网格上长程信息传播效率低，需深层处理器才能实现长程交互，导致计算成本上升、内存开销增加，还易出现过平滑问题；
- 现有部分多尺度GNN方法未同时实现高效传播与低资源消耗的平衡。

🚀 提出的新方法与思路
**Hierarchical Multiscale Processor**：替换MeshGraphNets中原有的flat处理器模块，通过farthest-point采样与Voronoi划分对图进行粗化，过程中保留原始网格拓扑结构，依托粗粒度图开展消息传递，使信息可在更少层数下传播更大几何距离。
**Learned Graph Interpolation Network**：对粗粒度图输出的特征进行插值，重建原始细分辨率的特征信息，为下游物理状态演化预测提供适配的细粒度特征。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 预测准确性 | 在三类结构与流体基准任务上，相比MeshGraphNets、Bi-Stride Multi-Scale GNN实现性能提升 |
| 计算效率 | 训练时间消耗低于对比方法 |
| 内存使用 | 训练时峰值内存占用低于对比方法 |
| 扩展性 | 支持高保真网格下的长程信息高效传播，适配更大规模的物理模拟场景 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 三个结构与流体类物理基准数据集（具体名称未在论文中披露） | 验证HI-MGN的性能与效率 |

🎯 实验设置与评估指标
任务：基于mesh的物理 surrogate建模，即学习模拟网格节点的状态演化，替代传统数值求解器。
| 指标 | 含义（箭头标方向） |
| ---- | ---- |
| 预测准确率 | 模型预测的物理状态与真实物理状态的契合度，越高越好 |
| 训练时间 | 模型完成训练所需的时长，越低越好 |
| 峰值内存 | 训练过程中模型占用的内存峰值，越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| MeshGraphNets | 图神经网络（GNN）物理 surrogate模型 | 采用flat处理器，仅支持单尺度消息传递 |
| Bi-Stride Multi-Scale GNN | 多尺度图神经网络物理 surrogate模型 | 支持多尺度消息传递，但未达到HI-MGN的性能与效率 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体定量结果的数值及对应表号、图号等来源信息，仅在摘要中提及HI-MGN在三个结构与流体基准上准确率优于对比方法，训练时间、峰值内存均低于对比方法。
1. 主 benchmark性能：论文未报告具体指标数值
2. 效率对比：论文未报告具体FPS、参数量等效率指标的定量数值
3. 跨域 / zero-shot迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现1：拓扑感知的分层消息传递与学习型粗到细插值的框架，是实现可扩展mesh-based物理 surrogate建模的有效方案；
- 主要发现2：HI-MGN相比传统flat处理器的MeshGraphNets和现有多尺度GNN方法，在保证预测准确性的同时降低了训练时间与内存开销，解决了高保真网格下长程交互的低效问题。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：HI-MeshGraphNets通过分层多尺度图神经网络与学习型插值模块，实现了非结构化网格下物理 surrogate建模的高效长程信息传播，提升了预测性能并降低了计算与内存消耗。

</details>

---

### 8. [Bootstrapping Niche Multilingual Code Translation via Reinforcement Learning with Execution-Based Verifiable Supervision](https://arxiv.org/abs/2608.13854v1)

**Authors**: Kouki Yuki, Jie Zeng, Kyoko Ogawa, Ryunosuke Ikeda, Yohei Kobashi, Takeshi Kojima, Ikuya Yamada, Yusuke Iwasawa, Yutaka Matsuo  
**Category**: cs.CL  
**Published**: 2026-08-17  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2608.13854v1  

#### Abstract
Code translation must preserve executable behavior across many programming languages, yet neural code translation has largely focused on a few popular languages such as C++, Java, and Python. This leaves a niche, many-to-many setting where parallel supervision is sparse, producing plausible but non-...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Bootstrapping Niche Multilingual Code Translation via Reinforcement Learning with Execution-Based Verifiable Supervision
1. 论文的主要贡献和创新点
✅ 解决的问题：现有神经代码翻译模型多聚焦C++、Java、Python等少数流行语言，而niche多对多（many-to-many）编程语言翻译场景的平行监督数据稀少，导致生成的翻译结果看似合理但不可执行，无法满足实际需求。现有方法缺陷：现有方法未针对niche多语言场景设计带执行验证的训练流程，无法解决监督数据不足的核心问题，难以生成可执行的跨语言翻译结果。

🚀 提出的新方法与思路
**多语言执行验证数据扩展**：将可验证的种子Python程序扩展为包含多国语言的执行验证代码池，缓解niche多语言场景中监督数据稀少的问题；
**执行结果驱动的偏好奖励模型构建**：基础LLM生成跨语言翻译候选后，根据代码执行结果标记偏好，训练奖励模型以量化跨语言翻译的质量；
**GRPO优化的多语言翻译流水线**：使用上述奖励模型作为信号，在600组定向语言对（25×24）上通过GRPO算法优化基础LLMs，提升多对多代码翻译的可执行性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 语言覆盖范围 | 支持600组定向语言对的广泛many-to-many翻译，覆盖mid-tier等非流行语言 |
| 翻译正确性 | 基于执行结果的监督机制，保证翻译后代码的可执行性 |
| 场景适配性 | 针对niche多语言场景设计的训练流程，在非流行语言上性能增益更明显 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| HumanEval-X++ | 扩展HumanEval-X构建的niche多对多语言空间的执行基准，用于评估代码翻译性能 |
| 执行验证多语言代码池 | 从种子Python程序扩展得到，作为训练数据用于构建翻译候选的偏好标签 |

🎯 实验设置与评估指标
任务：niche多对多（many-to-many）代码翻译任务
| 指标 | 含义 |
| ---- | ---- |
| 执行通过率 | 翻译后代码可成功执行的比例，越高越好 ↑ |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 未微调的基础LLMs（Qwen-3.5系列） | 未经过多语言代码翻译微调的基础模型 | 仅针对少数流行语言优化，无niche多语言场景适配，翻译可执行性差 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告
2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. 基于执行可验证监督的偏好强化学习方法，能有效解决niche多语言代码翻译中监督数据不足的问题，提升翻译可执行性；2. 所提方法在mid-tier非流行语言上的性能增益，比整体语言集的平均增益更显著。
- 方法局限性：论文未报告
- 未来工作：可进一步优化执行验证数据的扩展策略，拓展极端小语种的翻译覆盖范围，提升模型在特殊场景下的泛化能力。

> ✅ **总结一句话**：本研究提出的基于执行监督的偏好强化学习框架，结合定制的执行基准HumanEval-X++，为niche多对多代码翻译提供了可行解决方案，尤其在mid-tier非流行语言上性能提升突出，为该领域建立了标准化的数据生成与训练范式。

</details>

---

### 9. [Removing Temporal Note Redundancy Improves Multimodal Reinforcement Learning for Medicine](https://arxiv.org/abs/2608.14157v1)

**Authors**: Chenran Weng, Joo Seung Lee, Malini Mahendra, Anil Aswani  
**Category**: cs.AI  
**Published**: 2026-08-17  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2608.14157v1  

#### Abstract
Mechanical ventilation is a critical life-support intervention, requiring dynamic adjustments to ventilator settings as a patient's condition evolves. While reinforcement learning (RL) offers a promising framework for optimizing these sequential decisions, standard approaches rely primarily on struc...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Removing Temporal Note Redundancy Improves Multimodal Reinforcement Learning for Medicine
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾为：用于优化ICU机械通气设置的强化学习（RL）需整合临床自由文本笔记的关键上下文，但标准RL方法存在两类缺陷：① 仅依赖结构化电子健康记录（EHR）数据，缺失自由文本笔记的临床信息；② 整合原始笔记到RL状态空间时，笔记的时间冗余（复制文本、模板化、重复记录）会稀释时间局部更新，降低状态表示质量，损害RL决策效果。

🚀 提出的新方法与思路
**冗余感知多模态状态表示框架（redundancy-aware multimodal state representation framework）**：在RL策略学习前，对自由文本笔记显式移除时间冗余，生成更优质的状态表示。该框架包含两种计算高效的时间冗余去除策略：
1. **嵌入空间分解（embedding-space decomposition）**：对局部历史子空间执行奇异值分解（SVD）；
2. **可解释句子级差分操作（interpretable sentence-level diff operation）**：在文本编码前，过滤已记录的重复句子。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 状态表示生成 | 显式分离笔记中的新旧临床信息，消除时间冗余，提升状态表示质量 |
| RL决策性能 | 在四种off-policy评估方法下，显著优于仅用结构化EHR、原始笔记的基线方法 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| real-world ICU data | 评估所提方法在ICU机械通气决策任务中的RL性能 |

🎯 实验设置与评估指标
任务为优化ICU患者机械通气的动态设置，为临床决策提供支持。
| 指标 | 含义 |
|------|------|
| Model-Based Rollouts | off-policy评估得分，↑越高表示性能越好 |
| Fitted Q-Evaluation | off-policy评估得分，↑越高表示性能越好 |
| Weighted Importance Sampling | off-policy评估得分，↑越高表示性能越好 |
| Weighted Doubly Robust Evaluation | off-policy评估得分，↑越高表示性能越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 仅结构化EHR方法 | 基线 | 仅使用结构化电子健康记录数据 |
| 原始笔记方法 | 基线 | 使用未处理的原始自由文本笔记 |
| 冗余感知多模态状态表示框架 |  proposed方法 | 移除时间冗余后的多模态状态表示，含两种冗余去除策略 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体的表号、图号及定量数值，仅说明所提方法构造的状态表示在所述四种off-policy评估方法下，均显著优于仅用结构化EHR、原始笔记的基线方法。
💡 结论：所提冗余感知多模态状态表示框架可有效消除临床笔记的时间冗余，生成更高质量的状态表示，提升医疗强化学习的临床决策性能。

4. 关键结论和发现
- 主要发现：① 临床自由文本笔记的时间冗余会损害医疗强化学习的状态表示质量，进而降低决策性能；② 显式分离笔记中的新旧临床信息（即移除冗余）可显著提升RL在ICU机械通气决策任务中的性能；③ 嵌入空间分解与句子级差分两种策略均能有效完成时间冗余去除，生成优质状态表示。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该研究提出了显式移除临床笔记时间冗余的冗余感知多模态状态表示框架，用于提升优化ICU机械通气设置的强化学习性能，其表现显著优于仅用结构化电子健康记录数据和原始自由文本笔记的基线方法。

</details>

---

### 10. [The Integer Alibi: Localizing Cross-Kernel Divergence in INT8-Quantized LLM Inference](https://arxiv.org/abs/2608.13756v1)

**Authors**: Teng-Ruei Chen  
**Category**: cs.LG  
**Published**: 2026-08-17  
**Score**: 39.5  
**Type**: new  
**ArXiv ID**: 2608.13756v1  

#### Abstract
Two GPU kernels implementing the same scaled INT8 GEMM interface are usually treated as interchangeable. We test that assumption: holding the checkpoint, prompts, hardware, inference engine, decoding, and quantization configuration fixed, we swap only the INT8 linear kernel (CUTLASS versus Triton) i...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

The Integer Alibi: Localizing Cross-Kernel Divergence in INT8-Quantized LLM Inference
1. 论文的主要贡献和创新点
解决的问题
1. 实现相同scaled INT8 GEMM接口的GPU内核通常被认为可互换，但在vLLM INT8量化LLM推理中固定检查点、提示、硬件、推理引擎、解码及量化配置，仅交换INT8线性内核时，端到端输出不一致；
2. 虽在无溢出绑定下INT32点积精确且与顺序无关，可排除累加器作为差异来源，但需定位具体差异环节。

🚀 提出的新方法与思路
**整数不在场证明（Integer Alibi）**：验证在共享INT8操作数且满足无溢出绑定时，INT32点积精确且与顺序无关，从而排除累加器为INT8 GEMM跨内核差异的来源；进一步将差异定位到精确累加器之后的缩放应用和输出取整操作；作为探针检查，通过干预缩放/取整环节，可恢复端到段位级一致；
**教师强制重放**：关联层与标记，分析差异位置的特性；
计划发布内容：预注册材料、per-layer预测清单、内核选择manifest，以及将内核互换性的差异分析转化为具体一致性检查流程。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 差异定位精度 | 可精确定位INT8量化LLM推理中不同内核实现间差异的具体来源（缩放应用与输出取整） |
| 内核互换性验证 | 提供了将差异分析转化为可落地的内核互换性一致性检查流程的方案 |
| 跨内核差异认知 | 明确INT8与FP8 GEMM跨内核差异的不同特征，为量化内核优化提供依据 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Qwen3-1.7B、Qwen3-8B的线性层操作数 | 对比CUTLASS与Triton两个INT8线性内核在中间层的输出一致性 |

🎯 实验设置与评估指标
任务：vLLM INT8量化LLM推理中，固定除INT8线性内核外的所有变量，对比CUTLASS与Triton内核的端到端及中间层输出一致性。
| 指标 | 含义（箭头方向） |
| --- | --- |
| 端到端序列一致性 | 越高越好（↑） |
| 中间层输出一致性 | 越高越好（↑） |
| 输出差异量级 | 越低越好（↓） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 内核可互换假设 | 现有默认认知 | 认为实现相同scaled INT8 GEMM接口的GPU内核可互换 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**说明**：以下实验均未报告具体实验来源（如表号、图号等）
1. **端到端一致性实验**：在1.7B模型冷重启时，单个内核自输出一致，但跨内核在所有端到端序列对比中无一致序列。
💡 结论：现有默认假设中相同接口INT8内核可互换不成立，端到端输出对INT8线性内核敏感。
2. **中间层输出一致性实验**：向两个内核喂Qwen3-1.7B全部线性层、Qwen3-8B全部线性层的相同操作数，在power-of-two scales下中间层输出位级一致，在实际缩放下输出存在差异。
💡 结论：差异源于累加器后的缩放应用与输出取整，而非累加器本身。
3. **探针检查干预实验**：应用探针检查干预（调整缩放/取整环节）后，端到端序列恢复位级一致。
💡 结论：通过干预缩放/取整环节可消除INT8内核差异导致的端到端不一致。
4. **FP8与INT8 GEMM差异对比实验**：跨内核FP8 GEMM的差异流行度和量级随归约深度增长，INT8 GEMM差异量级远小于FP8 GEMM，在给定范围内差异在较低水平。
💡 结论：INT8量化下的内核差异特性与FP8不同，可忽略性更高。
5. **差异预测实验**：差异位置（翻转位置）集中于小logit边际，可通过相关指标预测翻转风险。
💡 结论：小logit边际可用于预测INT8内核差异导致的推理结果翻转风险。

主 benchmark性能（L2/碰撞率等）：论文未报告
效率对比（FPS / 参数量）：论文未报告
跨域 / zero-shot迁移：论文未报告
鲁棒性 / 扰动测试：论文未报告
消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. 相同scaled INT8 GEMM接口的GPU内核（CUTLASS与Triton）不可互换，仅交换内核即可导致vLLM INT8量化LLM推理的端到端输出不一致；2. INT8 GEMM跨内核差异源于精确INT32累加器之后的缩放应用和输出取整，而非累加器本身；3. INT8 GEMM跨内核差异量级远小于FP8 GEMM，特性差异显著；4. 小logit边际可作为预测INT8内核差异导致的推理结果翻转风险的特征。
- 方法局限性：论文未明确报告方法的局限性，仅针对INT8与FP8 GEMM的跨内核差异分析。
- 未来工作：发布预注册材料、每层预测清单、内核选择manifest，构建可落地的内核互换性一致性检查流程。

> ✅ **总结一句话**：该研究通过“整数不在场证明”思路，揭示了INT8量化LLM推理中不同内核实现间的差异来源，验证了现有内核可互换假设的不成立，为建立量化内核互换性的一致性检查提供了关键依据。

</details>

---

### 11. [FreeBalance: Pre-Routing Online Moe Load Balancing via Residual Workload Prediction](https://arxiv.org/abs/2608.14205v1)

**Authors**: Pengfei Chen, Yize Wu, Shouxu Kuang, Ke Gao, Ling Li  
**Category**: cs.AI  
**Published**: 2026-08-17  
**Score**: 35.5  
**Type**: new  
**ArXiv ID**: 2608.14205v1  

#### Abstract
Load imbalance poses a major bottleneck to the efficiency of expert parallelism in distributed inference of Mixture-of-Experts (MoE) models. The most heavily loaded rank stalls global execution due to skewed routing distributions, directly increasing latency. While offline expert placement can allev...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

FreeBalance: Pre-Routing Online Moe Load Balancing via Residual Workload Prediction
1. 论文的主要贡献和创新点
✅ 解决的问题
1. MoE模型分布式推理的专家并行中，负载不平衡是效率瓶颈，最重负载的rank会拖慢全局执行，直接增加延迟；
2. 离线专家放置仅能缓解持续负载不平衡，但多任务服务的负载存在层和批次依赖的动态路由特性，必须采用在线负载均衡；
3. 现有在线负载均衡方法依赖路由器后的路由统计，只能在路由决策后才启动专家权重加载或迁移，将迁移开销置于推理关键路径上。

🚀 提出的新方法与思路
**Residual Workload Predictor**：利用残差网络中隐藏表示的跨层相似性，构建轻量级的工作量预测器，使能在路由决策可用前主动规划专家迁移；
**Cost-Constrained Swap Framework**：通过成本模型约束专家交换的数量，确保专家迁移与路由前的计算阶段重叠，将同步开销完全隐藏在可用时间窗口内，实现无损失的在线负载均衡。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
max-to-mean rank load ratio | 降低32.8%
end-to-end prefill latency | 降低13.1%
专家迁移关键路径开销 | 平均每层隐藏5.1个专家的平衡开销，原本将占关键路径延迟约8.5%的开销被完全隐藏

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
论文未报告 | 论文未报告

🎯 实验设置与评估指标
任务：MoE模型分布式推理中的在线负载平衡
指标 | 含义
--- | ---
max-to-mean rank load ratio | 衡量各rank负载的不平衡程度，↓越低越好
end-to-end prefill latency | 模型推理的端到端预填充延迟，↓越低越好

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
论文未报告 | 论文未报告 | 论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（场景：MoE分布式推理在线负载平衡）**
论文未报告提及具体实验表号、图号或章节定位的量化指标具体来源，明确内容如下：
| 指标 | 数值 |
--- | ---
max-to-mean rank load ratio | 降低32.8%
end-to-end prefill latency | 降低13.1%
平均每层隐藏的专家平衡数量 | 5.1个
💡 结论：FreeBalance可显著缓解MoE分布式推理的负载不平衡，有效降低端到端预填充延迟，消除了专家迁移对关键路径的开销影响

**效率对比（FPS / 参数量）**
论文未报告
**跨域 / zero-shot 迁移**
论文未报告
**鲁棒性 / 扰动测试**
论文未报告
**消融实验**
论文未报告

4. 关键结论和发现
- 核心发现：利用残差网络跨层隐藏表示相似性构建轻量级工作负载预测器，可提前规划专家迁移，实现迁移与路由前计算阶段的有效重叠；
- 核心发现：结合成本模型约束专家交换数量，可将专家同步开销完全隐藏在可用时间窗口内，避免额外关键路径开销；
- 核心发现：FreeBalance在缓解MoE负载不平衡、降低推理延迟上均取得显著性能增益，是适用于动态多任务服务的在线负载均衡方案。
方法局限性：论文未报告
未来工作：论文未报告
✅ **总结一句话**：FreeBalance是一种基于残差工作负载预测的在线MoE负载均衡框架，通过提前规划专家迁移与计算重叠，无损失地大幅降低MoE分布式推理的负载不平衡率与端到端预填充延迟。

</details>

---

### 12. [Retrieval Grounding Latent Reasoning for Dense Retrieval](https://arxiv.org/abs/2608.14107v1)

**Authors**: Gang Zhou, Xiongxi Yu, Hu Tian, Yang Wei, Lu Pan, Ke Zeng, Shibiao Xu, Xiaolong Zheng  
**Category**: cs.AI  
**Published**: 2026-08-17  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2608.14107v1  

#### Abstract
Reasoning-intensive retrieval requires text representations to capture not only semantic similarity, but also the reasoning needed to determine relevance under a given retrieval instruction. Existing reasoning-enhanced embedding models improve retrieval by incorporating reasoning information into de...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Retrieval Grounding Latent Reasoning for Dense Retrieval
1. 论文的主要贡献和创新点
✅ 解决的问题
1. 现有推理增强嵌入模型用于密集检索时，其监督通常由最终检索目标主导；
2. 这类模型的潜在推理轨迹可能学习到捷径推理模式，在不产生有意义增量检索增益的前提下维持检索性能，无法实现真正的推理增强。

🚀 提出的新方法与思路
**Retrieval Grounding Latent Reasoning (RGLT)**：它是针对密集检索的潜在推理框架，在隐空间通过静音token构造指令条件的潜在推理轨迹以执行非自回归推理；该方法结合过程监督的显式到隐式蒸馏与检索接地监督，利用阶段式CoT重建塑造中间隐态，通过检索效应信用优化潜在推理轨迹上的增量检索增益。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 监督机制 | 采用过程监督的显式到隐式蒸馏与检索接地监督，而非仅以最终检索目标主导监督 |
| 推理轨迹优化 | 针对潜在推理轨迹优化增量检索增益，避免捷径推理模式 |
| 性能表现 | 在推理密集型检索基准上优于强基线方法 |
| 效率 | 保留嵌入推理的高效性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 推理密集型检索基准 | 验证RGLT的检索性能 |

🎯 实验设置与评估指标
任务为推理密集型检索，指标论文未报告。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 强基线 | 基准方法 | 采用最终检索目标主导的监督，未针对潜在推理轨迹设计检索接地监督 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表（无具体编号，仅摘要提及）：推理密集型检索基准性能**
| 方法 | 性能 |
| ---- | ---- |
| RGLT | 优于强基线 ✅ |
| 强基线 | 基准性能 |
💡 结论：RGLT在推理密集型检索基准上的性能优于强基线方法。

1. 效率对比：论文未报告
2. 跨域/zero-shot迁移：论文未报告
3. 鲁棒性/扰动测试：论文未报告
4. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现
1. 现有推理增强嵌入模型的监督由最终检索目标主导，易导致潜在推理轨迹学习到无实际增益的捷径模式；
2. RGLT通过将中间潜在转换与检索改进显式关联，可有效优化推理过程的增量检索增益；
3. RGLT在推理密集型检索任务中实现了更好的性能，同时保持了嵌入推理的高效性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：Retrieval Grounding Latent Reasoning (RGLT) 是一种面向密集检索的潜在推理框架，通过结合过程监督的显式到隐式蒸馏与检索接地监督，解决了现有方法易形成无实际增益的捷径推理模式的问题，在推理密集型检索基准上优于强基线方法且保留高效的嵌入推理。

</details>

---

### 13. [Reinforcement Learning-Based Production Scheduling in an Industry-Based Coating Scenario Using the Digital Model Playground](https://arxiv.org/abs/2608.14122v1)

**Authors**: Arne Kr\"oger, Ralf Buscherm\"ohle, Wilhelm Hasselbring, Henrik Wilbers  
**Category**: cs.AI  
**Published**: 2026-08-17  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2608.14122v1  

#### Abstract
Production scheduling in complex manufacturing environments is challenging when sequence-dependent setup times, stochastic disturbances, and due-date constraints must be addressed simultaneously. While reinforcement learning (RL) methods have shown promising results in research, most studies rely on...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Reinforcement Learning-Based Production Scheduling in an Industry-Based Coating Scenario Using the Digital Model Playground
1. 论文的主要贡献和创新点
✅ 解决的问题
复杂制造环境需同时处理序列相关准备时间、随机干扰、交货期约束等，生产调度极具挑战；现有强化学习（RL）调度研究大多依赖简化的基准流程，工业相关性不足。

🚀 提出的新方法与思路
**Digital Model Playground（DMPG）**：采用开源离散事件仿真框架Digital Model Playground，建模包含序列相关准备时间、机器故障、可变利用率等实际复杂度的工业启发式涂装流程，并在此场景中训练标准RL算法Deep Q-Networks（DQN）和Proximal Policy Optimization（PPO），与传统调度规则做基准测试。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 工业场景贴合度 | 覆盖序列相关准备时间、机器故障、可变利用率等制造实际复杂度，提升RL调度的工业相关性 |
| 可复用性 | 提供可共享的开源框架，为后续RL调度研究提供透明测试床 |
| 性能均衡性 | RL调度算法可在关键性能指标上实现均衡提升，其中PPO性能最稳健 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| Digital Model Playground构建的工业启发式涂装场景 | 建模复杂制造环境，用于训练RL智能体及基准测试 |

🎯 实验设置与评估指标
任务：针对工业涂装流程的生产调度，需处理序列相关准备时间、机器故障、交货期约束等实际制造复杂度。
| 指标 | 含义 |
| ---- | ---- |
| 关键性能指标（KPIs） | 论文未报告具体指标定义 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Deep Q-Networks（DQN） | 强化学习算法 | 标准RL调度算法，用于基准对比 |
| Proximal Policy Optimization（PPO） | 强化学习算法 | 标准RL调度算法，论文提及其性能最稳健，用于基准对比 |
| 传统调度规则 | 传统调度方法 | 基准对比的常规调度方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能
论文未报告具体的定量数值及对应表/图/章节信息，仅提及RL-based调度在关键性能指标上有均衡提升。
2. 效率对比（FPS / 参数量）
论文未报告。
3. 跨域 / zero-shot 迁移
论文未报告。
4. 鲁棒性 / 扰动测试
论文未报告。
5. 消融实验
论文未报告。

4. 关键结论和发现
- 主要发现：
① 在包含序列相关准备时间、机器故障等实际制造复杂度的工业涂装场景中，RL调度方法具备可行性，且能在关键性能指标上实现均衡提升；
② PPO算法在该场景中表现出比DQN更稳健的性能；
③ 开源Digital Model Playground框架可有效弥合学术RL调度研究与工业实践的差距，为后续研究提供测试平台。
- 方法局限性：
论文未明确报告该方法的局限性。
- 未来工作：
利用所提出的Digital Model Playground开放源测试床，开展更多工业场景下的RL调度相关研究。

> ✅ **总结一句话**：该论文通过开源Digital Model Playground框架，在贴合工业实际复杂度的涂装场景中验证了RL调度方法的可行性，尤其PPO算法表现稳健，弥合了学术RL调度研究与工业实践的差距，同时提供了可复用的开放源框架。

</details>

---

### 14. [Intern-S2-Mobius: Foundation Model with Decoupled Knowledge and Reasoning](https://arxiv.org/abs/2608.14290v1)

**Authors**: Kai Chen, Jifeng Ding, Ning Ding, Jiaye Ge, Lixin Gu, Yicheng Gu, Qipeng Guo, Ermo Hua, Haian Huang, Haozheng Hou, Jie Hou, Xiangyu Hong, Che Jiang, Minxi Jin, Cheng Liang, Dahua Lin, Dawei Liu, Kuikun Liu, Chengqi Lv, Haijun Lv, Han Lv, Ningsheng Ma, Biqing Qi, Jianmin Qian, Shiya Su, Youbang Sun, Huanze Tang, Zhongbo Tian, Hanjing Wang, Rui Wang, Ting Wang, Yi Wang, Baiting Wu, Jun Xu, Bowen Yang, Hui Wang, Weida Wang, Haochen Ye, Jiashuo Yu, Shan Yu, Xiaoyi Yu, Qirui Zeng, Qi Zhang, Ming Zhang, Wenwei Zhang, Bowen Zhou, Xinyu Zhou  
**Category**: cs.AI  
**Published**: 2026-08-17  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2608.14290v1  

#### Abstract
We introduce Mobius-v0, an architecture that comprises a globally shared Memory (FFN) that stores knowledge vectors and multiple Reasoners (Self-Attn) that iteratively achieve compositional reasoning. Using hidden states as cache and carrier, reasoners repeatedly query memory for required knowledge-...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Intern-S2-Mobius: Foundation Model with Decoupled Knowledge and Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有基础模型（如Transformer架构）未实现知识与推理的解耦，存在训练数据需求量大、推理效率低的痛点，难以同时平衡训练成本与性能、推理效率。

🚀 提出的新方法与思路
**Mobius-v0架构**：该架构由两部分组成，一是全局共享的Memory（FFN），用于存储知识向量；二是多个Reasoners（Self-Attn），用于实现迭代式组合推理。以隐藏状态作为缓存与载体，Reasoners反复查询Memory获取所需知识向量，知识被传递回推理算子，通过知识与推理分离的架构，实现更好的知识压缩与推理效率。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 知识与推理架构设计 | 实现知识与推理解耦，达成更好的知识压缩和推理效率 |
| 训练数据效率 | 7B规模模型仅需Transformer基线62.6%的训练数据即可达到相似下游性能 |
| 推理效率 | Intern-S2-Mobius（基于Qwen3.5-35B持续预训练）相比基线实现近4倍端到端推理加速 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
以提升基础模型的下游任务性能、推理效率为目标，Markdown表格：
| 指标 | 含义 |
|------|------|
| 下游任务得分 | 越高越好 |
| 端到端推理速度 | 越快越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| Transformer基线 | 传统基础模型架构 | 未分离知识与推理，训练数据需求量大，推理效率低 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能**：论文未报告
**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot 迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告

4. 关键结论和发现
- 主要发现：① 知识与推理分离的Mobius-v0架构可有效提升基础模型的训练数据效率，7B规模模型仅用62.6%的训练数据即可达到同规模Transformer基线的相似下游性能；② 基于Qwen3.5-35B持续预训练的Intern-S2-Mobius，在保持相似下游性能的同时，能显著提升推理效率，实现近4倍端到端推理加速；③ 知识与推理的分离设计可实现更好的知识压缩与推理效率。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：Intern-S2-Mobius采用知识与推理分离的Mobius-v0架构，在不降低下游任务性能的前提下，大幅提升了基础模型的训练数据效率与推理效率。

</details>

---

### 15. [S2Dialog: Multimodal Dialogue Retrieval with Semantic and Acoustic-Style Modeling](https://arxiv.org/abs/2608.14029v1)

**Authors**: Xueqi Wang, Zhigang Wang, Runqing Zhang, Zhenqi Jia, Junfeng Zhao  
**Category**: cs.CL  
**Published**: 2026-08-17  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2608.14029v1  

#### Abstract
Multimodal dialogue retrieval aims to retrieve dialogues from multimodal dialogue banks that are similar to a target dialogue in terms of both textual semantics and acoustic conversational styles. Such dialogue-level retrieval is crucial for many dialogue-related tasks, including Emotion Recognition...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# S2Dialog: Multimodal Dialogue Retrieval with Semantic and Acoustic-Style Modeling
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾为现有多模态对话检索方法的适配粒度与建模能力不足：现有方法多局限于utterance级或单模态匹配，无法满足对话级检索的需求；同时无法捕捉整段对话的全局语义连贯性与声学风格一致性，而对话级检索对Emotion Recognition in Conversation、Spoken Dialogue Systems、Conversational Speech Synthesis等下游任务具有重要价值。现有方法的缺陷分点：
  - 适配粒度缺陷：以utterance级匹配为主，未覆盖完整对话；
  - 模态覆盖缺陷：多为单模态匹配，未有效利用多模态信息；
  - 语义建模缺陷：无法捕捉整段对话的全局语义连贯性；
  - 风格建模缺陷：无法捕捉整段对话的声学风格一致性。

🚀 提出的新方法与思路
**Dialogue-level Textual Retriever**：对对话的文本模态进行编码，生成对话级文本表示，适配对话级检索需求。
**Dialogue-level Acoustic Retriever**：对对话的声学模态进行编码，生成对话级声学表示，适配对话级检索需求。
**Dialogue-level Textual-Acoustic Contrastive Learning**：用于对齐语义与风格相似的对话，区分无关对话，增强多模态检索的对齐效果。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 适配粒度 | 支持完整对话级检索，适配下游任务对对话级参考的需求 |
| 模态覆盖 | 同时处理文本与声学多模态信息，弥补单模态方法不足 |
| 语义建模 | 能捕捉对话全局语义连贯性，适配下游任务对语义一致性的需求 |
| 风格建模 | 能捕捉对话声学风格一致性，适配下游任务对风格参考的需求 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| DailyTalk | 用于多模态对话检索模型的性能评估 |

🎯 实验设置与评估指标
任务为多模态对话检索。论文未报告具体评估指标及其含义。

⚔️ 基线方法对比
论文未报告。

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告任何具体实验结果、表号、图号及对应结论等定量相关内容。

4. 关键结论和发现
- 主要发现：
  1. S2Dialog在多模态对话检索任务上取得了出色的性能；
  2. Dialogue-level Textual-Acoustic Contrastive Learning有助于提升多模态对话检索的语义与风格对齐效果。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：S2Dialog是针对对话级多模态检索的统一框架，通过生成对话级文本与声学表示并引入文本-声学对比学习，有效捕捉对话的全局语义连贯性与风格一致性，在DailyTalk数据集上表现出色。

</details>

---

### 16. [From Passive Delegates to Strategic Negotiators: Reinforcing Social Reasoning in Small Language Models with SocialRL](https://arxiv.org/abs/2608.13787v1)

**Authors**: Wenyue Hua, Zachary Huang, Tyler Payne, Safoora Yousefi, Saleema Amershi, Asli Celikyilmaz  
**Category**: cs.AI  
**Published**: 2026-08-17  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2608.13787v1  

#### Abstract
AI agents increasingly act on their users' behalf, handling tasks such as scheduling meetings, comparing offers, and haggling over prices. These principal-driven tasks routinely place the agent across from a counterpart (another user's agent, a seller, a recruiter) whose goals may conflict with its ...

---

### 17. [SheetCompass: Hierarchical Relation Graphs for Agentic Spreadsheet Reasoning](https://arxiv.org/abs/2608.14452v1)

**Authors**: Panjing He, Mingyue Cheng, Yucong Luo, Li Li, Xiaohan Zhang  
**Category**: cs.AI  
**Published**: 2026-08-17  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2608.14452v1  

#### Abstract
Spreadsheets are widely used to organize, analyze, and manipulate semi-structured data, yet automated spreadsheet reasoning remains challenging for large language models (LLMs). Real-world workbooks often contain implicit cross-table associations, fine-grained column dependencies, and complex spatia...

---

### 18. [Exploring High-Bandwidth Flash for Modern LLM Inference: Opportunities and Challenges](https://arxiv.org/abs/2608.13868v1)

**Authors**: Dowon Son, Yonggon Park, Hyunuk Cho, Hyungkyu Ham, Onur Mutlu, Sungjin Lee, Gwangsun Kim, Jisung Park  
**Category**: cs.AR  
**Published**: 2026-08-17  
**Score**: 25.0  
**Type**: new  
**ArXiv ID**: 2608.13868v1  

#### Abstract
This work investigates the potential benefits and technical challenges of using high-bandwidth flash (HBF) for large language model (LLM) inference. HBF has gained increasing attention as a promising solution to mitigate memory-capacity bottlenecks in modern LLM-serving systems, but its benefits and...

---

### 19. [ARC: Fair Relative Advantage Comparison in Open-Ended Real-World Interaction](https://arxiv.org/abs/2608.13622v1)

**Authors**: Yongqi Tong, Tan Li Hui Faith, Choy Zhen Wen Marcus, Zhou Jin, Kewei Fu, Jiang-Ming Yang, Jianshe Li, Xin Zhang  
**Category**: cs.AI  
**Published**: 2026-08-17  
**Score**: 24.0  
**Type**: new  
**ArXiv ID**: 2608.13622v1  

#### Abstract
Open-ended real-world interaction admits multiple valid behaviors: an agent may answer directly, ask for clarification, provide progress updates, or confirm before acting. This flexibility breaks a core assumption behind group-based RL: rollouts compared within a group are no longer guaranteed to be...

---

### 20. [MobileMem: Learning from a Year of Mobile Experiences](https://arxiv.org/abs/2608.13606v1)

**Authors**: Xinle Deng, Yida Xue, Xiangyuan Ru, Haoming Xu, Shuofei Qiao, Mengru Wang, Yijun Chen, Buqiang Xu, Chen Jiang, Yuchen Eleanor Jiang, Lizhong Wang, Jianfeng Wang, Li Zeng, Haofen Wang, Guilin Qi, Huajun Chen, Ningyu Zhang  
**Category**: cs.AI  
**Published**: 2026-08-17  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2608.13606v1  

#### Abstract
The next generation of AI agents is increasingly moving beyond systems that answer isolated questions toward persistent personal assistants that can understand, remember, and continuously learn from users' experiences. Such assistants require long-term memory to accumulate and leverage user-specific...

---

### 21. [Simulation-Driven Vehicular Traffic Data Augmentation: Extending Sensor Coverage Through Virtual Sensing](https://arxiv.org/abs/2608.13993v1)

**Authors**: Davide Andrea Guastella, Eladio Montero Porras, Evangelos Pournaras, Gianluca Bontempi  
**Category**: cs.AI  
**Published**: 2026-08-17  
**Score**: 22.5  
**Type**: new  
**ArXiv ID**: 2608.13993v1  

#### Abstract
Urban traffic management relies on sensor networks whose spatial coverage is limited by deployment costs and privacy regulations. Machine learning models trained on such sparse data cannot generalize to unmonitored locations and must be retrained whenever the sensor infrastructure changes. We propos...

---

### 22. [BiasTrace: Linking Reasoning Behaviours to Biased Outputs in LLMs](https://arxiv.org/abs/2608.14161v1)

**Authors**: Varsha Ramineni, Hossein A. Rahmani, Jerome Ramos, Karin Sevegnani, Emine Yilmaz  
**Category**: cs.AI  
**Published**: 2026-08-17  
**Score**: 22.5  
**Type**: new  
**ArXiv ID**: 2608.14161v1  

#### Abstract
LLMs exhibit social biases that can produce inaccurate and discriminatory inferences, posing risks in high-stakes applications. While prior work has made progress in measuring and mitigating bias, it largely focuses on final outputs of models, with limited understanding of the mechanisms that produc...

---

### 23. [Coverage Aware Active Evaluation for Failure Discovery with Paired Systems](https://arxiv.org/abs/2608.13719v1)

**Authors**: Anjali Parashar, Rachel Luo, Apoorva Sharma, Sushant Veer, Edward Schmerling, Carson Sobolewski, Mingxin Yu, Chuchu Fan, Marco Pavone  
**Category**: cs.AI  
**Published**: 2026-08-17  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2608.13719v1  

#### Abstract
Autonomous systems can fail in rare and heterogeneous ways, making real-world failure discovery difficult under limited testing budgets. Although cheaper proxies such as simulators, lower-fidelity systems, or related policies can be sampled extensively to find failures, proxy failures often do not t...

---

### 24. [Grounding Without Corrective Control: Truth-Tracking Profiles for Large Language Models](https://arxiv.org/abs/2608.14252v1)

**Authors**: Brett Reynolds  
**Category**: cs.AI  
**Published**: 2026-08-17  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2608.14252v1  

#### Abstract
Recent work suggests that some large language model representations have content or reference. Grounding can secure either without supplying live routes for correction. This paper asks what follows from that gap. An output is answerable when discrepancies can affect what a target- and task-specific ...

---

### 25. [Probabilistic indirect models for undrained shear strength: addressing significant data missing and variability with advanced imputation and machine learning techniques](https://arxiv.org/abs/2608.13934v1)

**Authors**: Haibin Xiong, Shaoheng Dai, Peng Lan, Xuzhen He, Chenxi Tong, Sheng Zhang, Daichao Sheng  
**Category**: cs.LG  
**Published**: 2026-08-17  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2608.13934v1  

#### Abstract
Accurate prediction of undrained shear strength (su) is crucial for geotechnical design, but is often hampered by substantial uncertainty in traditional empirical methods. This study uses the CLAY/10/7490 global database to develop probabilistic indirect models to predict su based on Atterberg limit...

---

### 26. [A Year in LLM Serving: Workload Evolution, Caching and Load-Balancing](https://arxiv.org/abs/2608.13573v1)

**Authors**: William Nixon, Jon Durbin, Florian Standhartinger, Haryadi S. Gunawi, Juncheng Yang  
**Category**: cs.AI  
**Published**: 2026-08-17  
**Score**: 21.5  
**Type**: new  
**ArXiv ID**: 2608.13573v1  

#### Abstract
Large Language Model (LLM) serving has become a critical cloud workload, and realistic traces are essential for motivating and benchmarking serving systems. However, existing LLM serving workload studies remain limited in scale and scope. They often observe short time periods and provide limited vis...

---

### 27. [Boosting Data Augmentation with Stochastic Weight Averaging](https://arxiv.org/abs/2608.14373v1)

**Authors**: Longde Huang, Axel Flinth, Jan E. Gerken  
**Category**: cs.LG  
**Published**: 2026-08-17  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2608.14373v1  

#### Abstract
The symmetries of a learning task have become an important factor in designing modern deep learning solutions. Data augmentation is a straightforward and effective way of incorporating symmetries into a generic neural network. Recent results show that infinitely large deep ensembles show perfect sym...

---

### 28. [Can Language Models Understand mmWave Data? Benchmarking Large Language Models for mmWave Radar-Based Human Understanding](https://arxiv.org/abs/2608.14179v1)

**Authors**: Jeongwan Shin, Jaehyeon Kim, Donguk Ko, Jaeho Choi  
**Category**: cs.AI  
**Published**: 2026-08-17  
**Score**: 15.0  
**Type**: new  
**ArXiv ID**: 2608.14179v1  

#### Abstract
Large language models (LLMs) have shown remarkable reasoning and generative capabilities, motivating their use as universal reasoning engines for perception. While modern approaches such as vision-language models (VLMs) have attempted to incorporate reasoning capabilities into visual sensing, the in...

---

### 29. [Connected Subspace Clustering: Hardness, a Scalable Heuristic, and an Application to Sea Level Geodesy](https://arxiv.org/abs/2608.14215v1)

**Authors**: Johanna Hillebrand, Jan H\"ockendorff, J\"urgen Kusche, Kelin Luo, Heiko R\"oglin, Melanie Schmidt, Christian Sohler, Bernd Uebbing  
**Category**: cs.LG  
**Published**: 2026-08-17  
**Score**: 15.0  
**Type**: new  
**ArXiv ID**: 2608.14215v1  

#### Abstract
Constrained optimization extends classical optimization by integrating side information, making it widely applicable across scientific and engineering domains. Consider a setting where we measure variables at different physical locations. When grouping these measurements, we often want clusters that...

---

### 30. [Depth-Aware Sensitivity Analysis of Mixture-of-Experts Models via Magnitude-Based Expert Masking](https://arxiv.org/abs/2608.13565v1)

**Authors**: Pradeep Kumar Sharma, Shantanu Godbole, Hritvik Shrivastava  
**Category**: cs.AI  
**Published**: 2026-08-17  
**Score**: 14.0  
**Type**: new  
**ArXiv ID**: 2608.13565v1  

#### Abstract
Mixture-of-Experts (MoE) architectures scale large language models (LLMs) while preserving computational efficiency through sparse activation. Despite their widespread adoption, the relative importance of individual MoE layers remains insufficiently characterized, particularly for model compression....

---

## 🔧 Configuration

This bot is configured to look for papers containing the following keywords:
- LLM, Inference, Training, kv cache, Speculative decoding, Prefill, Decode, FlashAttention, PagedAttention, continuous batching, MOE, mixture of experts, Quantization, FP8, FP4, Parallel, Distributed, Pipeline, Sparse, Sparse Attention, State Space, SSM, Throughput, Scalable, Efficient, vLLM, SGLang, DeepSpeed, FSDP, AI compiler, TVM, Triton, MLIR, torch.compile, kernel fusion, polyhedral, RISC-V, RVV, XiangShan, custom instruction, eBPF, RDMA, disaggregated, chiplet, NoC, CXL, HBM, systolic array, Kernel, Cluster, Communication, Offload, Hardware, Accelerator, Compiler, Optimization, Embodied, Embodied AI, Embodied Intelligence, Robotics, Robot, Manipulation, Navigation, Sim-to-real, Simulation, World Model, World Models, Video Generation, Video Prediction, Multimodal, Multi-modal, Vision-Language, Vision Language, VLM, Image-Text, Cross-modal, Cross modal, Text-to-Image, Text-to-Video, Vision Transformer, Visual Understanding

## 📅 Schedule

The bot runs on weekdays at 05:40 UTC via GitHub Actions to fetch the latest papers.

## 🚀 How to Use

1. **Fork this repository** to your GitHub account
2. **Customize the configuration** by editing `config.json`:
   - Add/remove arXiv categories (e.g., `cs.AI`, `cs.LG`, `cs.CL`)
   - Modify keywords to match your research interests
   - Adjust `max_papers` and `days_back` settings
3. **Enable GitHub Actions** in your repository settings
4. **The bot will automatically run on weekdays** and update the README.md

## 📝 Customization

### arXiv Categories
Common categories include:
- `cs.AI` - Artificial Intelligence
- `cs.LG` - Machine Learning
- `cs.CL` - Computation and Language
- `cs.CV` - Computer Vision
- `cs.NE` - Neural and Evolutionary Computing
- `stat.ML` - Machine Learning (Statistics)

### Keywords
Add keywords that match your research interests. The bot will search for these terms in paper titles and abstracts.

### Exclude Keywords
Add terms to exclude certain types of papers (e.g., "survey", "review", "tutorial").

## 🔍 Manual Trigger

You can manually trigger the bot by:
1. Going to the "Actions" tab in your repository
2. Selecting "arXiv Bot Daily Update"
3. Clicking "Run workflow"

---
*Generated automatically by arXiv Bot* 
