# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-07-27 09:39:19 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [Scaling Native Multimodal Pre-Training From Scratch](https://arxiv.org/abs/2607.22043v1)

**Authors**: Haoyuan Wu, Aoqi Wu, Hai Wang, Jiajia Wu, Jinxiang Ou, Bei Yu  
**Category**: cs.CL  
**Published**: 2026-07-27  
**Score**: 68.0  
**Type**: new  
**ArXiv ID**: 2607.22043v1  

#### Abstract
Although large language models (LLMs) exhibit remarkable reasoning capabilities, their reliance on text-only pre-training restricts the perception of the multimodal physical world. Native multimodal pre-training avoids this limitation by training models from scratch on multimodal inputs, thereby ach...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Scaling Native Multimodal Pre-Training From Scratch
1. 论文的主要贡献和创新点
✅ 解决的问题
现有大语言模型（LLMs）仅基于文本预训练，无法感知多模态物理世界；传统多模态模型的后期融合架构存在优化不对称性；Native Multimodal预训练范式的缩放属性未被系统表征。
🚀 提出的新方法与思路
**范式缩放研究**：针对固定计算预算场景，研究基于Transformer的视觉-语言模型（VLM）的最优模型规模和token count配置。
**compute law建模**：构建最小目标损失的可预测compute law，分析语言与多模态目标的差异化缩放特性。
**效率前沿推导**：结合数据组成对compute laws和分配指数的影响，推导模型规模、token count及数据混合的效率前沿，为资源分配提供指导。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 多模态感知 | 从scratch进行跨模态预训练，实现深度跨模态整合，缓解传统后期融合架构的优化不对称性 |
| 训练稳定性 | 语言目标的分配规律不受数据组成影响，语言学习稳定 |
| 资源效率 | 明确不同数据混合下的最优模型与token分配，提升计算资源利用率，适配不同数据混合场景 |
| 下游性能 | 实现正向跨模态迁移，提升纯文本空间推理能力，支持鲁棒多模态上下文学习 |
2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
论文未报告具体数据集名称 | 用于Native Multimodal预训练
🎯 实验设置与评估指标
任务：在固定计算预算下，研究基于Transformer的VLM的最优模型规模、token count及数据混合配置，评估预训练效果及下游任务性能
| 指标 | 含义 | 方向 |
| --- | --- | --- |
| 论文未报告具体指标名称 | 预训练最小目标损失 | ↓（越低越好） |
| 论文未报告具体指标名称 | 下游纯文本空间推理性能 | ↑（越高越好） |
| 论文未报告具体指标名称 | 下游鲁棒多模态上下文学习性能 | ↑（越高越好） |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 传统LLMs | 文本预训练模型 | 仅依赖文本预训练，无法感知多模态物理世界 |
| 传统后期融合VLM | 多模态模型 | 存在优化不对称性，跨模态整合深度不足 |
| 本研究的Native Multimodal预训练VLM | 从scratch预训练的多模态模型 | 实现深度跨模态整合，明确缩放规律，具备正向跨模态迁移能力 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**无对应表N：缩放特性与数据组成影响分析**
摘要未报告具体实验对应的表号、图号及详细定量数值，仅提及以下结论性内容：
| 结果项 | 内容 |
| --- | --- |
| 损失规律 | 最小目标损失符合可预测的compute law |
| 语言分配 | 语言分配规律不受数据组成影响，学习稳定 |
| 多模态分配 | 多模态分配规律对数据组成敏感；文本密集混合数据需在更大模型规模下才具计算效率，最优资源分配转向更大模型容量 |
| 下游性能 | Native Multimodal预训练诱导正向跨模态迁移，可提升纯文本空间推理能力，支持鲁棒多模态上下文学习 |
💡 结论：本研究明确了Native Multimodal预训练范式的核心缩放规律及数据组成的影响，证实其正向跨模态迁移的下游价值，为可扩展多模态基础模型训练提供了基础。
（消融实验：论文未报告）
4. 关键结论和发现
- Native Multimodal预训练的最小目标损失遵循可预测的compute law；语言目标的分配规律稳定不受数据组成影响，多模态目标的分配规律则对数据组成敏感，文本密集混合数据需更大模型规模才具计算效率。
- Native Multimodal预训练实现深度跨模态整合，具备正向跨模态迁移能力，可提升纯文本空间推理性能，支持鲁棒多模态上下文学习。
- 现有传统LLMs和传统后期融合VLM存在多模态感知不足、优化不对称性等缺陷，本研究填补了Native Multimodal预训练缩放属性的研究空白。
方法局限性：论文未报告
未来工作：论文未报告

> ✅ **总结一句话**：本论文系统研究了基于Transformer的Native Multimodal预训练VLM在固定计算预算下的最优缩放配置，明确了该范式的核心缩放规律及数据组成的影响，证实其正向跨模态迁移的下游价值，为多模态基础模型的可扩展训练提供了关键基础。

</details>

---

### 2. [TileSight: A First-Principles Tile-Centric Analytical GPU Performance Model from Cores to Clusters](https://arxiv.org/abs/2607.22432v1)

**Authors**: Zhiwen Mo, Yu Cheng, Lei Wang, Zhengju Tang, Lei Xu, Guoyu Li, Yuqi Dong, Lingxiao Ma, Yuqing Xia, Jilong Xue, Fan Yang, Luo Mai, Zhi Yang, Wayne Luk, Hongxiang Fan  
**Category**: cs.DC  
**Published**: 2026-07-27  
**Score**: 61.5  
**Type**: new  
**ArXiv ID**: 2607.22432v1  

#### Abstract
Recent GPU programming frameworks such as Triton, TileLang, and CUDA Tile adopt tiles as first-class primitives, making tile-centric programming the prevailing approach for high-performance GPU kernels. Performance-analysis tooling has not followed: programmers still rely on coarse roofline bounds, ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：TileSight: A First-Principles Tile-Centric Analytical GPU Performance Model from Cores to Clusters

1. 论文的主要贡献和创新点
✅ 解决的问题：现有GPU编程框架已将tiles作为一级编程原语，但对应的性能分析工具未同步发展，程序员需依赖粗粒度roofline边界、不透明机器学习预测器或事后分析工具理解GPU内核执行，在依赖张量核、CUDA核、缓存层次、内存管线、GPU间网络的现代AI workload（内核融合、分布式推理）中，该问题尤为突出。
🚀 提出的新方法与思路
**TileSight**：一种以tile为中心的GPU性能分析模型，将tile从编程原语升级为分析原语，从三个层级建模GPU性能：① GPU核心内部建模计算与内存管线的重叠；② GPU核心之间建模缓存层次结构；③ 跨GPU节点之间建模通信。所有层级共享tile抽象：内层tile层将工作表达为覆盖网络、内存、计算管线的资源向量；跨tile层调度依赖的有序动作以暴露合法重叠，并从tile重用距离推断多级缓存命中率；跨设备层将远程张量访问映射至指定位置，并通过alpha-beta阶段成本实现路由。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 统一抽象 | 以tile为核心抽象覆盖GPU从核心到集群的全层级，解决不同层级建模逻辑不一致问题 |
| 预测性能 | 性能预测精度优于现有针对GPU性能分析的基线方法 |
| 跨架构能力 | 在多种GPU架构间的性能预测迁移性优于现有方法 |
| 优化支持 | 可选择出性能与强厂商、专家基线相当的tile配置 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标
任务：GPU内核及分布式AI workload的性能预测
| 指标 | 含义 | 方向 |
| --- | --- | --- |
| MAPE | 平均绝对百分比误差 | ↓越低越好 |
| wMAPE | 加权平均绝对百分比误差 | ↓越低越好 |
| L2缓存命中率误差 | L2缓存命中率预测值与实际测量值的差值 | ↓越小越好 |
⚔️ 基线方法对比：论文未报告（仅提及优于现有基线，未明确基线的具体类型与特点）

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能（L2/碰撞率等）**：论文未报告对应表/图编号的具体定量结果，根据论文摘要，TileSight的性能预测精度优于现有基线方法，L2缓存命中率预测误差较小。
💡 结论：TileSight在多种GPU上的内核性能预测表现优于现有方法，L2缓存命中率预测接近实际水平。

**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告

4. 关键结论和发现
- 主要发现：1. TileSight作为统一的tile-centric GPU性能分析模型，可有效提升单GPU及多GPU分布式AI workload的性能预测精度；2. TileSight的L2缓存命中率预测接近实际测量值；3. TileSight可支持选择高性能的tile配置。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：TileSight是一种基于tile原语的分层GPU性能分析模型，可准确预测GPU从核心到集群级别的AI workload性能，指导tile配置优化，具备良好的跨架构性能迁移能力，待发表后将开源。

</details>

---

### 3. [Unified Static-Dynamic Pruning for Efficient LLM Inference](https://arxiv.org/abs/2607.21985v1)

**Authors**: Jinhyeok Kim, Yejoon Lee, Jaeyoung Do  
**Category**: cs.DC  
**Published**: 2026-07-27  
**Score**: 58.5  
**Type**: new  
**ArXiv ID**: 2607.21985v1  

#### Abstract
The increasing deployment of large language models (LLMs) has magnified the computational and memory bottlenecks of autoregressive decoding, where low compute intensity and bandwidth-bound kernels dominate inference cost. Weight pruning offers a promising remedy,
  but existing methods remain confin...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Unified Static-Dynamic Pruning for Efficient LLM Inference

1. 论文的主要贡献和创新点
✅ 解决的问题
现有静态剪枝（SP）方法：永久移除冗余权重，但缺乏适配性；
现有动态剪枝（DP）方法：适配输入稀疏性，但引入运行时不规则性；
二者均无法兼顾LLM推理的效率需求。

🚀 提出的新方法与思路
**SPDP统一框架**：整合非结构化静态剪枝与输入自适应动态剪枝的GPU适配LLM推理框架，配套设计Tiled-Column-wise Bitmap Compressed（Tiled-CBC）压缩格式，以及两类互补GPU内核：一是带混合激活感知动态共享内存位图解码（HAD-SMBD）的CUDA-core spMspV内核，用于细粒度运行时激活跳过；二是针对prefill计算优化的Tensor-Core SpMM内核，实现双阶段推理适配。该联合格式与内核设计兼顾静态/动态稀疏性，维持带宽高效内存访问与高计算强度。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 剪枝策略整合 | 克服静态剪枝缺乏适应性、动态剪枝引入运行时不规则性的缺陷 |
| 推理效率 | 优于SpInfer等现有稀疏推理框架 |
| 模型质量 | 匹配基线困惑度，支持更高稀疏度 |
| 内存与计算适配 | 适配GPU推理双阶段，维持带宽高效内存访问与高计算强度 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
任务为GPU环境下的LLM推理性能评估；
| 指标 | 含义 |
|------|------|
| 推理速度 | 越高越好 |
| 困惑度 | 越低越好 |
| 稀疏度 | 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| SpInfer | 现有稀疏推理框架 | 基准对比对象 |

3. 主要实验结果和性能指标
所有定量结果无明确表号、图号或章节来源，按要求处理：
- **主 benchmark 性能（L2/碰撞率等）**：论文未报告
- **效率对比（FPS / 参数量）**：论文未报告
- **跨域 / zero-shot 迁移**：论文未报告
- **鲁棒性 / 扰动测试**：论文未报告
- **消融实验**：论文未报告

4. 关键结论和发现
- 主要发现：1. 统一静态-动态剪枝可推进LLM推理效率与模型质量的帕累托前沿，显著提升LLM推理的吞吐量与每瓦性能。2. 联合格式与内核的设计是兼顾稀疏性下带宽效率与计算强度的关键，适配GPU推理的双阶段特性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：SPDP是整合静态与动态剪枝的GPU适配LLM推理稀疏框架，通过配套的压缩格式与定制GPU内核，在维持模型质量的同时实现推理效率的提升，优于现有稀疏推理框架。

</details>

---

### 4. [J-CoT: Chain-of-Thought in J-Space](https://arxiv.org/abs/2607.21981v1)

**Authors**: Junde Wu, Jiayuan Zhu, Fengling Liu, Minhao Hu, Jiazhen Pan  
**Category**: cs.CL  
**Published**: 2026-07-27  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2607.21981v1  

#### Abstract
Chain-of-thought prompting improves language-model reasoning by carrying intermediate states across successive computation steps. However, relying on natural language as the only recurrent interface is overly restrictive, since many transient computations do not need to be fully verbalized. Existing...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：J-CoT: Chain-of-Thought in J-Space
1. 论文的主要贡献和创新点
✅ 解决的问题
- 现有基于自然语言的Chain-of-Thought（CoT）方法：以自然语言作为唯一中间状态，过于受限，很多临时计算无需完全语言化；
- 现有latent-reasoning方法：传递完整的密集隐藏向量，无显式的机制来选择和组织下一步推理所需的信息。

🚀 提出的新方法与思路
**J-CoT**：基于J-space（模型隐藏表示中的词汇索引坐标系）构建的循环推理框架。每个周期内模型在完整隐藏空间计算；周期边界处，将中间状态表达为词汇索引系数（即J-thought），传递该J-thought，再映射回模型隐藏表示供下一个周期使用。J-CoT无需流畅的中间理由，也无需基于完整隐藏状态进行循环。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 中间状态表达 | 兼顾语言接地性，无需将中间状态解码为句子 |
| 信息传递机制 | 通过J-thought显式选择、组织推理所需信息，而非传递完整隐藏向量 |
| 推理要求 | 避免显式CoT的过度语言化，无需对所有临时计算做自然语言表述 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告具体数据集名称 | 在数学、科学、编码、结构化路径推理任务上开展评估 |

🎯 实验设置与评估指标
论文未报告具体的任务细节、实验设置及评估指标。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 自然语言CoT | 显式推理方法 | 以自然语言为唯一中间状态，需全语言化临时计算 |
| 现有latent-reasoning基线 | 隐式推理方法 | 传递完整隐藏向量，无显式信息选择及组织机制 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体的实验表号及对应数值，仅说明：J-CoT-Zero在匹配主干和推理设置下，在所有评估基准上匹配或超过最强latent-reasoning基线；J-CoT-Train在数学、科学、编码、结构化路径推理任务中获得最高得分。其余实验（主benchmark性能（除上述提及外）、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）均论文未报告。

4. 关键结论和发现
- 主要发现：1）J-CoT-Zero在匹配主干和推理设置下，多任务性能匹配或超越现有最优latent-reasoning方法；2）J-CoT-Train在数学、科学、编码、结构化路径推理任务上取得最高得分；3）J-CoT框架平衡了语言接地性与信息组织效率，解决了现有两类推理方法的核心痛点。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：J-CoT是基于J-space的循环推理框架，通过词汇索引形式的J-thought传递中间状态，兼顾语言接地性与信息组织效率，在多类推理任务上达到或超越现有最优水平。

</details>

---

### 5. [Remedying Coarsening-Based GNN Training under Heterophily via Adaptive Complementary Enhancement](https://arxiv.org/abs/2607.21885v1)

**Authors**: Guoming Li, Jian Yang, Xukun Wang, Zixiao Wang, Shangsong Liang, Yifan Chen  
**Category**: cs.LG  
**Published**: 2026-07-27  
**Score**: 51.5  
**Type**: new  
**ArXiv ID**: 2607.21885v1  

#### Abstract
Coarsening-based training for graph neural networks (GNNs), i.e.\ training on coarsened graphs rather than the original large ones, has become a promising direction for scaling GNNs to massive graphs. However, prior work has been evaluated almost exclusively on \textit{homophilic} graphs, leaving th...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Remedying Coarsening-Based GNN Training under Heterophily via Adaptive Complementary Enhancement
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾为：粗化图GNN训练（基于粗化图而非原始大图训练）虽为GNN扩展至大规模图的有前途方向，但现有相关工作几乎仅在同构图上评估，异质图场景研究不足；且现有粗化方法在异质图上因粗化过程不可避免丢失图信息，导致性能显著下降。

🚀 提出的新方法与思路
**Adaptive Complementary Enhancement（ACE）**：一种即插即用、模型无关的策略，用于重新整合粗化过程中被丢弃的信息。具体而言，ACE学习一个投影器以重构原始节点特征；应用各向异性结构正则化来嵌入局部异质性；采用同方差不确定性加权，自适应平衡由粗化图训练损失与经异质性感知投影器重构的增强节点特征构成的全图辅助损失组成的组合训练目标。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 异质图性能 | 在异质图基准任务上取得一致的性能提升 |
| 同构图性能 | 在同构图上保持与现有方法相当的竞争力 |
| 通用性与开销 | 即插即用、模型无关，附加计算开销小 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告具体名称 | 模型性能基准测试 |

🎯 实验设置与评估指标
论文未报告具体任务类型、实验设置细节及评估指标的含义与方向要求。

⚔️ 基线方法对比
论文未报告具体基线方法的相关信息。

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（L2/碰撞率等）**
论文未报告具体定量数值结果。

**效率对比（FPS / 参数量）**
论文未报告。

**跨域 / zero-shot 迁移**
论文未报告。

**鲁棒性 / 扰动测试**
论文未报告。

**消融实验**
论文未报告。

4. 关键结论和发现
- 主要发现
1. 现有粗化GNN训练方法在异质图上因粗化过程的信息丢失导致性能显著下降，该问题同时通过实验和理论验证；
2. ACE策略可有效缓解异质图下粗化GNN训练的性能退化问题，且在同构图场景仍保持竞争力；
3. ACE作为轻量型策略，仅产生极小的计算开销，适配大规模图训练需求。
- 方法局限性
论文未报告。
- 未来工作
论文未报告。

> ✅ **总结一句话**：提出即插即用、模型无关的Adaptive Complementary Enhancement（ACE）策略，通过整合粗化过程丢弃的信息并引入异质性感知机制，提升异质图下粗化GNN训练的性能，同时在同构图场景保持竞争力且计算开销低。

</details>

---

### 6. [RIS-Kernel: A Model-Agnostic Architecture for Long-Context LLM Inference via Sparse Attention](https://arxiv.org/abs/2607.21927v1)

**Authors**: Anderson R. Santos  
**Category**: cs.LG  
**Published**: 2026-07-27  
**Score**: 49.5  
**Type**: new  
**ArXiv ID**: 2607.21927v1  

#### Abstract
Full self-attention in large language models scales as O(N^2), which limits long-context document analysis to 65,536 tokens and requires costly GPU clusters. The Reduced Interaction Sampling (RIS) inference engine addresses this constraint as a model-agnostic architecture. Without modifying weights,...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

RIS-Kernel: A Model-Agnostic Architecture for Long-Context LLM Inference via Sparse Attention
1. 论文的主要贡献和创新点
✅ 解决的问题
原生全自注意力大语言模型的时间复杂度为$O(N^2)$，限制了长文档分析的上下文窗口上限（仅为65536 tokens），且需昂贵的GPU集群支撑，无法在普通低成本硬件运行。
🚀 提出的新方法与思路
**Reduced Interaction Sampling (RIS) 推理引擎**：作为模型无关架构，无需修改模型权重，采用稀疏随机几何方法将自注意力的时间复杂度降至$O(N \log N)$，适配普通硬件的内存限制；包含两种分支配置：RIS-Stochastic（基于随机采样）、RIS-Structural（基于结构采样）。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 时间复杂度 | 将原生全自注意力的$O(N^2)$复杂度降至$O(N \log N)$，大幅降低计算负载 |
| 硬件需求 | 可在普通无GPU加速的CPU服务器（16-128GB RAM）运行，无需GPU集群 |
| 长上下文支持 | 支持65536 tokens的超长上下文窗口，原生稠密自注意力在此窗口会触发内存不足故障 |
| 上下文适配性能 | 在32768 tokens上下文窗口下，RIS可达到与原生稠密基线相当甚至更优的性能 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告具体实验所用的数据集名称
🎯 实验设置与评估指标
实验任务为长上下文大语言模型的文档分析或检索任务，评估指标为准确率（越高越好），额外采用McNemar配对检验评估性能提升的显著性（阈值为p<0.10，<0.10为边际显著）。
| 指标 | 含义（箭头） |
| --- | --- |
| 准确率 | ↑ 越高越好 |
| McNemar检验p值 | ↓ 越小越显著 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 原生稠密自注意力 | 基线方法 | 全自注意力，时间复杂度$O(N^2)$，需GPU，32768 tokens内为有效性能基线 |
| 零上下文基准 | 性能下限 | 无上下文输入的模型输出，作为性能对比的最低基准 |
| RIS-Stochastic | 提出方法 | RIS的随机采样分支，支持不同采样密度（1%/5%）与采样种子数（10/70）的配置 |
| RIS-Structural | 提出方法 | RIS的结构采样分支，采用1%采样密度、10个种子的配置 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告实验结果对应的表号、图号或章节页码信息，仅在摘要中提及部分定量描述，无法提供对应实验的表格内容。
1. 32768 tokens上下文窗口实验
论文未报告该实验结果对应的来源编号信息。
2. 65536 tokens上下文窗口实验
论文未报告该实验结果对应的来源编号信息。
消融实验
论文未报告消融实验相关的实验设计与结果信息。
效率对比
论文未报告FPS、参数量等效率对比的相关信息。
跨域/zero-shot迁移
论文未报告相关实验的信息。
鲁棒性/扰动测试
论文未报告相关实验的信息。

4. 关键结论和发现
- 主要发现：
1. 稀疏注意力可作为正则化器使用：RIS-Stochastic在低采样密度（1%）配合多采样种子时，可过滤序列噪声提升性能；高密度采样（5%）配合少种子时，会引入分心噪声，性能匹配原生稠密基线。
2. RIS-Structural在低配置（1%采样密度、10个种子）下，可恢复75%的上下文差距，逼近原生稠密基线性能。
3. 在65536 tokens的超长上下文窗口，RIS相比零上下文基准存在幅度为up to 14.06个百分点的性能提升，且该提升具有边际显著性（p=0.078<0.10），此时原生稠密自注意力会触发内存不足故障。
4. 所有评估均在普通无GPU加速的CPU服务器完成，证明长上下文大语言模型推理可在普通学术硬件实现，无需GPU集群支撑。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：RIS-Kernel是一种模型无关的长上下文大语言模型推理架构，通过Reduced Interaction Sampling推理引擎将自注意力复杂度降至$O(N \log N)$，无需修改模型权重，可在普通CPU服务器实现低成本长上下文推理，适配65536 tokens超长上下文窗口且无需GPU，在中等上下文窗口性能接近或优于原生稠密注意力。

</details>

---

### 7. [Adversarial Style Optimization: Enhancing VLM Jailbreaks by GRPO-based Stylistic Triggers Optimization](https://arxiv.org/abs/2607.21619v1)

**Authors**: Bingjun Luo, Jialin Guo, Yue Yao, Xinpeng Ding  
**Category**: cs.CL  
**Published**: 2026-07-27  
**Score**: 46.0  
**Type**: new  
**ArXiv ID**: 2607.21619v1  

#### Abstract
Multimodal Large Language Models (MLLMs) have achieved impressive performance, but their safety alignment remains vulnerable to jailbreak attacks. Existing content-based jailbreaks are often inconsistent and show unsatisfying performance against the rapidly evolving MLLMs, failing to exploit non-con...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Adversarial Style Optimization: Enhancing VLM Jailbreaks by GRPO-based Stylistic Triggers Optimization
1. 论文的主要贡献和创新点
✅ 解决的问题
现有基于内容的多模态大语言模型（MLLMs）越狱攻击存在不一致性，对快速演化的MLLMs性能不佳，且未充分利用MLLMs的非内容型漏洞。

🚀 提出的新方法与思路
**Adversarial Style Optimization (ASO)**：是即插即用的增强模块，用于放大现有视觉越狱攻击。该方法微调图像编辑模型，在给定对抗图像上叠加优化的风格修改，采用Group Relative Policy Optimization (GRPO)智能体进行指导，核心是Structurally-Tiered Reward Function，该函数结合检测模型明确拒绝的logit信号与强大评判模型的高保真语义评估。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 攻击增强效果 | 可显著增强现有SOTA视觉越狱攻击的成功率 |
| 模块特性 | 即插即用，适配现有攻击框架 |
| 漏洞利用类型 | 利用MLLMs的风格不一致性，属于非内容型漏洞利用 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务：评估ASO对现有视觉越狱攻击的增强效果，衡量攻击成功程度。
| 指标 | 含义 |
| --- | --- |
| 攻击成功率（ASR） | 越高越好，数值越高表示攻击越易成功 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体实验的表号、名称及对应定量数值，无符合要求的实验结果表格。

4. 关键结论和发现
- 主要发现：1）MLLMs存在风格不一致性，即对内容的理解不受视觉风格影响，但防御机制易被特定风格触发绕过；2）风格偏差是用于红队测试MLLMs的可扩展漏洞向量。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：提出的Adversarial Style Optimization（ASO）作为即插即用模块，利用MLLMs的风格不一致性放大现有视觉越狱攻击的效果，为MLLMs的安全测试提供了新的可扩展路径。

</details>

---

### 8. [Benchmarking Fine-tuning and Retrieval Strategies for a Multimodal Language Model on the NRC Reactor Operator Licensing Examination](https://arxiv.org/abs/2607.22067v1)

**Authors**: Isak Hwang, Yoon Pyo Lee  
**Category**: cs.CL  
**Published**: 2026-07-27  
**Score**: 45.5  
**Type**: new  
**ArXiv ID**: 2607.22067v1  

#### Abstract
The integration of large language models (LLMs) into the nuclear power industry requires outputs grounded in domain-specific knowledge. This study evaluates a 31-billion-parameter open-weight multimodal model (Gemma 4 31B-IT) on its capacity to apply nuclear knowledge by benchmarking eight model-ret...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Benchmarking Fine-tuning and Retrieval Strategies for a Multimodal Language Model on the NRC Reactor Operator Licensing Examination
1. 论文的主要贡献和创新点
✅ 解决的问题
将大语言模型（LLMs）集成到核工业领域时，需确保输出基于核领域特定知识；现有针对NRC反应堆操作员执照考试的多模态模型性能评估研究不足，未明确不同微调、检索、分块策略在该场景下的适配性，且无微调的模型配置无法满足核行业对输出质量的核心要求。
🚀 提出的新方法与思路
**多模态模型-核领域知识适配框架**：基于310亿参数的开放权重多模态模型Gemma 4 31B-IT，设计8种涵盖不同微调、检索、分块策略的配置：基础模型、仅用Gemini蒸馏的Chain-of-Thought（CoT） rationale的监督微调（SFT）模型、采用BM25稀疏检索美国能源部基础手册的检索增强生成（RAG，对比固定大小滑动窗口分块与结构感知分块两种策略）模型、检索增强微调（RAFT）模型，评估各配置在NRC反应堆操作员执照考试中的表现。
**策略适配分析框架**：对比模型训练状态（微调/未微调）对分块策略偏好的影响，以及RAFT与标准SFT在搜索环境下的表现差异。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 领域适配性 | 针对核工业NRC反应堆操作员执照考试场景设计多维度模型配置，聚焦核领域知识应用能力的评估 |
| 基准全面性 | 覆盖SFT、RAG、RAFT及分块策略等多种技术方案，对比维度丰富，可明确不同策略的表现差异 |
| 实用性导向 | 采用人类通过率作为核心评估标准，符合反应堆操作员执照考试的实际应用要求 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 14个Generic Fundamentals Examinations（GFE，来自2015-2021年3月的考试，含7个压水堆（PWR）和7个沸水堆（BWR）考试） | 评估多模态模型在NRC反应堆操作员执照考试中应用核知识的能力 |
🎯 实验设置与评估指标
任务为评估Gemma 4 31B-IT相关配置在NRC反应堆操作员执照考试中应用核知识的能力，核心目标是满足人类通过率标准（80%）。
| 指标 | 含义（箭头标方向） |
| --- | --- |
| 人类通过率 | 达到80%的考试通过比例（需满足该阈值） |
| 聚合准确率 | 所有考试项目的整体准确率（数值越高越好） |
| PWR项目准确率 | 压水堆考试项目的准确率（数值越高越好） |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 基础模型 | 未微调多模态模型 | 原始未做任何微调的Gemma 4 31B-IT |
| SFT配置 | 监督微调配置 | 经Gemini蒸馏的CoT rationale微调的多模态模型 |
| RAG配置 | 检索增强生成配置 | 采用BM25稀疏检索美国能源部基础手册，含固定大小分块与结构感知分块两种子配置 |
| RAFT配置 | 检索增强微调配置 | 结合检索与微调的多模态模型配置 |
3. 主要实验结果和性能指标
📊 定量结果汇总
无法定位论文中各结果对应的表号、图号等来源，故不输出具体数值，各实验内容如下：
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告
4. 关键结论和发现
- 主要发现：① 采用固定大小分块RAG的SFT配置在NRC反应堆操作员执照考试中表现最优，满足80%的人类通过率标准；② 所有无微调的模型配置均未通过人类通过率标准；③ 分块策略的偏好随模型训练状态变化，且RAFT在搜索环境下的表现弱于标准SFT。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文针对大语言模型应用于核工业需输出领域特定知识的需求，通过基准测试多种微调、检索及分块策略，确定了最优配置以实现反应堆操作员级别的核知识应用能力。

</details>

---

### 9. [Parameter-free Adaptive Sparse Attention via Compression-Based Content Selection](https://arxiv.org/abs/2607.21752v1)

**Authors**: Debarshi Kundu, Swaroop Ghosh, Vasant Honavar  
**Category**: cs.LG  
**Published**: 2026-07-27  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2607.21752v1  

#### Abstract
Data-adaptive sparse attention masks substantially outperform fixed patterns (e.g., BigBird and Longformer) and can even exceed dense attention on long sequences. Existing adaptive approaches---including SBM-Transformer, Dynamic Mask Attention, and NSA---typically require additional learnable parame...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Parameter-free Adaptive Sparse Attention via Compression-Based Content Selection
1. 论文的主要贡献和创新点
✅ 解决的问题
现有自适应稀疏注意力方法（包括SBM-Transformer、Dynamic Mask Attention、NSA）通常需额外可学习参数、自定义梯度估计器或专用CUDA内核；固定稀疏注意力模式（如BigBird、Longformer）性能不及数据自适应稀疏注意力，但现有自适应方法存在上述实现门槛。
🚀 提出的新方法与思路
**Compression-Based Content Selection for Adaptive Sparse Attention**：通过计算每个块的gzip压缩比，识别无法被gzip压缩的非冗余内容块，将长程注意力选择性路由至这些块；该方法基于输入的压缩轮廓生成稀疏掩码，无需额外参数、辅助损失或自定义CUDA内核。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 参数量 | 无额外可学习参数 |
| BPB性能 | 在8K上下文的PG-19字节级语言建模任务上，优于密集注意力、BigBird、Longformer及重实现的SBM-Transformer |
| 序列长度适应性 | 性能优势随序列长度增大，与BigBird的BPB差距从4K上下文时的0.05扩大至8K上下文时的0.63 |
| 收敛速度 | 比对比方法快3.3倍 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| PG-19 | 字节级语言建模 |
🎯 实验设置与评估指标
任务为PG-19上的字节级语言建模；评估指标为BPB（比特每字节，越低越好）、收敛速度。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 重实现的SBM-Transformer | 自适应稀疏注意力 | 唯一的带可学习掩码的基线方法 |
| BigBird | 固定稀疏注意力模式 | 采用固定稀疏注意力掩码 |
| Longformer | 固定稀疏注意力模式 | 采用固定稀疏注意力掩码 |
| 密集注意力 | 全注意力 | 全序列交互的密集注意力 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能（PG-19字节级语言建模，8K上下文）**
| 方法 | BPB |
| ---- | ---- |
| 本文方法 | 1.71 ✅ |
| 密集注意力 | 2.89 |
| BigBird | 2.34 |
| Longformer | 3.21 |
| 重实现的SBM-Transformer | 3.38 |
💡 结论：在8K上下文的PG-19字节级语言建模任务中，本文方法的BPB性能显著优于所有对比基线，且与BigBird的性能差距随序列长度增加而扩大。
效率对比：仅报告收敛速度比对比方法快3.3倍，其余效率指标（如FPS）论文未报告
跨域/zero-shot迁移：论文未报告
鲁棒性/扰动测试：论文未报告
消融实验：论文未报告
4. 关键结论和发现
- 基于gzip压缩的内容选择机制可实现无额外参数的自适应稀疏注意力，在长序列字节级语言建模任务上表现优于多种现有方法
- 该方法的性能优势随序列长度增大而提升
- 相比对比方法，该方法收敛速度提升3.3倍
- 论文未报告方法的局限性
- 论文未报告未来工作
> ✅ **总结一句话**：本文提出一种无需额外参数的自适应稀疏注意力方法，通过gzip压缩比识别内容块实现长程注意力的选择性路由，在PG-19字节级语言建模任务的长序列场景下，性能优于多种基线方法且收敛速度更快。

</details>

---

### 10. [Integrated Order Dispatching and Routing for Last-Mile Pickup via Deep Reinforcement Learning](https://arxiv.org/abs/2607.22356v1)

**Authors**: Yida Xu, Zhaofang Mao, Yuheng Miao, Jiaxin Zhang, Yiting Sun  
**Category**: cs.LG  
**Published**: 2026-07-27  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2607.22356v1  

#### Abstract
In recent years, the growing complexity of last-mile pickup operations has increased the need for fast and accurate decision-making on logistics platforms. This challenge is fundamentally driven by two key and tightly coupled decision-making processes: order dispatching and routing. Solving them sep...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Integrated Order Dispatching and Routing for Last-Mile Pickup via Deep Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
最后一公里取件运营复杂度提升，需快速准确的物流平台决策；订单调度与路径规划是两大紧密耦合的关键决策过程，单独求解会忽略两者的相互依赖，完全端到端学习在大规模可变规模实例上因奖励稀疏性存在不稳定、成本高的缺陷。
🚀 提出的新方法与思路
**Integrated optimization framework**：耦合学习得到的路径规划oracle与实时调度启发式，解决订单调度与路径规划的紧密耦合问题。
**Dynamic-Residual Graph Attention Network encoder with a Look-Ahead Courier-Personalized decoder**：用于路径规划子问题，构建适配路径规划的编码解码模块。
**Routing-oracle-guided dispatching heuristic with local search**：用于调度子问题，依托路径规划oracle提供近优解以选择候选快递员，同时保留实时可扩展性。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 解的质量 | 优于其他基准方法 |
| 求解时间 | 优于其他基准方法 |
| 问题适配性 | 避免单独求解忽略子过程依赖、完全端到端学习不稳定且成本高的缺陷，适配大规模可变规模实例 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Cainiao Logistics真实世界数据集 | 测试所提方法的性能，包含离线评估与在线滚动时域仿真 |
🎯 实验设置与评估指标
任务为优化最后一公里取件的订单调度与路径规划集成问题，评估指标如下：
| 指标 | 含义 |
| --- | --- |
| 解的质量 | 越高越好 |
| 求解时间 | 越低越好 |
⚔️ 基线方法对比
论文未报告具体基线方法的类型与特点。

3. 主要实验结果和性能指标
论文未报告具体实验结果的表号、图号及定量数值，无对应实验表格可呈现。

4. 关键结论和发现
- 主要发现：所提集成优化框架在最后一公里取件问题中，解的质量和求解时间均优于其他基准方法；所提框架可有效支撑物流企业解决实时大规模的最后一公里取件优化问题。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：通过耦合路径规划oracle与实时调度启发式的集成优化框架，提升了最后一公里取件问题的解质量与求解效率，可支撑物流企业的实时大规模优化需求。

</details>

---

### 11. [Enough is as good as a feast: A Comprehensive Analysis of How Reinforcement Learning Mitigates Task Conflicts in LLMs](https://arxiv.org/abs/2607.22039v1)

**Authors**: Zixuan Ren, Jinliang Lu, Junhong Wu, Yang Zhao, Dai Dai, Hua Wu, Haifeng Wang, Chengqing Zong  
**Category**: cs.CL  
**Published**: 2026-07-27  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2607.22039v1  

#### Abstract
Model merging plays a crucial role in consolidating multiple specialized models into a single, unified model, especially in the era of large language models (LLMs). Recent research has primarily focused on developing strategies to enhance merging performance with the trained models, while the impact...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Enough is as good as a feast: A Comprehensive Analysis of How Reinforcement Learning Mitigates Task Conflicts in LLMs
1. 论文的主要贡献和创新点
✅ 解决的问题
现有模型合并研究多聚焦于提升已训练LLM的合并策略性能，而监督微调（SFT）、强化学习（RL）等训练范式对LLM模型合并效果的影响尚未得到充分探索，该研究空白易导致模型合并过程中出现任务冲突、性能退化等问题。

🚀 提出的新方法与思路
**系统对比分析框架**：通过在五个代表性任务上开展全面评估，对比RL训练与SFT训练的LLM在模型合并中的表现；结合大量实证实验与理论分析，挖掘RL缓解LLM任务冲突、适配模型合并的核心因素。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 任务冲突缓解 | RL训练的LLMs可显著减少模型合并过程中的任务冲突 |
| 合并后性能 | RL训练的LLMs在合并后产生的性能退化程度更低 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 五个代表性任务数据集 | 用于评估并对比RL训练与SFT训练的LLM在模型合并中的表现 |

🎯 实验设置与评估指标
实验任务：LLM模型合并效果评估
| 指标 | 含义 |
| --- | --- |
| 论文未报告 | 论文未报告具体评估指标的名称及方向 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| SFT训练的LLMs | 基线对比方法 | 采用传统监督微调范式训练的LLMs，作为RL训练LLMs的对比基准 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（L2/碰撞率等）**：论文未报告
**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot 迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告

4. 关键结论和发现
- 主要发现：① RL训练的LLMs相比SFT训练的LLMs，在模型合并时能显著减少任务冲突，合并后的性能退化程度更低；② RL的在线策略训练控制梯度更新幅度更小，降低覆盖其他任务已有知识的风险；③ RL优化目标“enough is as good as a feast”在模型收敛时会逐步减少冲突参数更新的幅度与数量；④ RL对正负例的联合优化能引导模型向无偏的任务特定参数子空间优化，进一步避免参数冲突。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文通过系统对比分析RL与SFT训练的LLM在模型合并中的表现，揭示了RL训练缓解LLM任务冲突、降低合并后性能退化的优势及核心原因。

</details>

---

### 12. [LatentFlow: Visual Analytics for Latent Space Analysis in Molecular Graph Neural Networks](https://arxiv.org/abs/2607.21941v1)

**Authors**: Shiyi Liu, Jiaqing Chen, Nicholas Hadler, Rostyslav Hnatyshyn, Michael W. Mahoney, Talita Perciano, John F. Hartwig, Gunther H. Weber, Ross Maciejewski  
**Category**: cs.LG  
**Published**: 2026-07-27  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2607.21941v1  

#### Abstract
Chemists and materials scientists increasingly use machine learning models, such as graph neural networks (GNNs), to predict properties of molecules and the outcomes of their reactions. Beyond predictive performance, understanding how these models organize chemical information internally in their la...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

LatentFlow: Visual Analytics for Latent Space Analysis in Molecular Graph Neural Networks
1. 论文的主要贡献和创新点
✅ 解决的问题
现有用于分析分子图神经网络（GNNs）潜在空间（即分子embeddings）的方法，在跨层、跨不同模型状态（如训练epoch、模型配置、输入数据）的潜在空间分析上支持有限，难以理解潜在空间如何随模型变化或与化学概念相关联。

🚀 提出的新方法与思路
**LatentFlow**，是与领域专家合作开发的用于分析分子GNN潜在空间的可视化分析系统，核心包含以下功能：将分子embeddings分组为簇；采用修改后的桑基图（Sankey diagram）跟踪簇跨层与不同模型状态的变化；链接簇至代表性分子及其共享子结构；允许科学家引入自身领域知识并与潜在空间中的模式对比。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 跨层与跨模型状态分析支持 | 支持追踪簇在不同层及各类模型状态（如训练周期、模型配置、输入数据）下的变化 |
| 潜在空间解释能力 | 可关联簇与代表性分子及共享子结构，允许用户引入领域知识以验证潜在空间中的模式 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
任务为评估LatentFlow对分子GNN潜在空间分析的有效性，论文未报告具体评估指标

⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
论文通过两个案例研究评估LatentFlow，未提供主benchmark性能、效率对比（FPS/参数量）、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验相关的定量数据，因此相关内容均为论文未报告。

4. 关键结论和发现
- 主要发现：① LatentFlow有助于科学家理解分子GNN潜在空间的演化；② LatentFlow可识别有意义的分子模式；③ LatentFlow能更好地解释分子GNN的模型行为
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：LatentFlow是面向分子图神经网络潜在空间分析的可视化分析系统，通过修改桑基图追踪簇变化、关联分子子结构等功能，辅助科学家理解潜在空间演化、识别分子模式并解释模型行为。

</details>

---

### 13. [PRISM: Evaluating POSIX Storage Systems for AI Research Workflows](https://arxiv.org/abs/2607.21746v1)

**Authors**: Adithya Kumar, Aditya Basu, Jacob Kahn, Parth Malani, Leo Huang, Kalyan Saladi  
**Category**: cs.DC  
**Published**: 2026-07-27  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2607.21746v1  

#### Abstract
The rapid advancement of AI research is driven by massive investments in GPU clusters, yet the critical role of storage systems in enabling efficient research workflows is often overlooked. Unlike traditional HPC workloads, AI research prioritizes researcher productivity and ease of iteration. Pract...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

PRISM: Evaluating POSIX Storage Systems for AI Research Workflows
1. 论文的主要贡献和创新点
✅ 解决的问题
现有存储系统评估基准仅关注峰值性能，未捕捉AI研究工作负载具有突发性、异质性的IO模式；AI研究工作流需要兼容POSIX的存储系统以兼顾研究员生产力与迭代便捷性，传统HPC导向的存储评估无法适配该需求。
🚀 提出的新方法与思路
**PRISM**：针对GPU集群的评估框架，可复现AI研究的代表性工作负载（覆盖数据摄入、检查点IO、开发者工作流），从可用性和性能两个维度评估POSIX存储系统，帮助选择适配不同环境的存储解决方案。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 评估场景适配 | 现有基准仅关注峰值性能，PRISM覆盖AI研究全阶段工作流，适配其突发、异质的IO模式 |
| 需求匹配 | 现有方法不契合AI研究对POSIX兼容、研究员友好界面的核心需求，PRISM从性能与可用性双维度评估 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标
任务为在GPU集群上评估POSIX存储系统，评估维度包含性能与可用性；论文未报告具体指标与含义。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Lustre | POSIX存储系统 | 分布式并行存储系统 |
| NFS | POSIX存储系统 | Flash-backed网络文件系统 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**无表号：分布式检查点负载场景性能对比**
| 存储系统 | 性能表现 |
| --- | --- |
| Flash-backed NFS | 比同配置Flash-backed Lustre快 up to 3x ✅ |
💡 结论：在分布式检查点负载场景下，Flash-backed NFS方案性能优于同配置的Flash-backed Lustre，可用于指导集群存储选型。
其他实验项：论文未报告

4. 关键结论和发现
- 主要发现：1. AI研究工作负载的IO模式具有突发性、异质性，现有峰值性能导向的存储评估基准无法适配；2. PRISM可有效复现AI研究工作流，助力POSIX存储系统选型；3. 分布式检查点负载场景中，Flash-backed NFS性能优于同配置的Flash-backed Lustre。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：PRISM是适配AI研究工作流的POSIX存储系统评估框架，通过复现代表性AI工作负载，从性能与可用性维度评估存储系统，助力GPU集群的存储方案选型。

</details>

---

### 14. [Duet: Co-Optimizing P2P Message Propagation and Rotating-Leader Consensus](https://arxiv.org/abs/2607.22209v1)

**Authors**: Yifeng Ye, Rongji Huang, Gerui Wang, Mingchao Wan, Yuxing Duan, Jingjing Zhang, Shengyun Liu  
**Category**: cs.DC  
**Published**: 2026-07-27  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2607.22209v1  

#### Abstract
In blockchain systems, peer-to-peer (P2P) overlay networks play a crucial role in providing reliable, scalable and efficient message-delivery services to upper layers. However, the consensus layer and the underlying P2P network remain mutually opaque in existing blockchains, waiving the opportunity ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Duet: Co-Optimizing P2P Message Propagation and Rotating-Leader Consensus
1. 论文的主要贡献和创新点
✅ 解决的问题
现有区块链系统中，共识层与底层P2P网络互相不透明，无法挖掘进一步优化空间；区别于其他P2P应用，区块链可抽象为状态机，但该特性未被充分用于协调共识层与P2P网络的协同优化。
🚀 提出的新方法与思路
**加速领导者轮换**：利用区块链的状态机抽象特性，对旋转领导者共识协议进行优化，加快领导者轮换速度。
**可靠广播范式**：采用树型传播作为正常场景的消息传播方式，必要时降级使用gossip方式，实现可靠广播。
**延迟感知的传播树**：构建基于网络延迟的消息传播树，优化消息传播效率。
🔍 相比现有方法的优势
维度 | 优势
--- | ---
共识与P2P协同优化 | 利用区块链状态机抽象实现共识层与底层P2P网络的可信协调优化
消息传播性能 | 混合树型与gossip的可靠广播范式、延迟感知传播树提升传播效率
领导者轮换效率 | 加快旋转领导者共识的流程速度

2. 核心实验方法和设置
📚 使用的数据集
论文未报告
🎯 实验设置与评估指标
任务：评估区块链系统的消息传播及共识性能，对比不同传播方式的表现。
指标 | 含义
--- | ---
峰值吞吐量 | 越高越好
⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
gossip-based dissemination over the same topology | P2P消息传播方式 | 基于gossip的消息传播，作为性能对比的基线

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告

4. 关键结论和发现
- 主要发现：1. 区块链可抽象为状态机的特性可用于协调共识层与底层P2P网络，实现性能优化；2. 提出的三项改进（加速领导者轮换、混合可靠广播、延迟感知传播树）可有效提升区块链系统的性能；3. 该原型相比同拓扑的gossip-based dissemination在峰值吞吐量上有提升。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：论文提出Duet方法，通过协调区块链共识层与底层P2P网络，针对旋转领导者共识协议及底层消息传播提出三项改进，提升了系统的峰值吞吐量。

</details>

---

### 15. [Khondo: A Multimodal Benchmark for Document Packet Splitting of Bangla Forms](https://arxiv.org/abs/2607.21780v1)

**Authors**: Abu Tyeb Azad, Fahim Ahmed, Ishita Sur Apan, Ezharuddin Jubaer, Sumaiya Karim Katha, Armun Alam, Amin Ahsan Ali, Aman Chadha, Md Mofijul Islam, AKM Mahbubur Rahman  
**Category**: cs.CL  
**Published**: 2026-07-27  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2607.21780v1  

#### Abstract
Document packets, multiple documents concatenated into a single file, are common in government and administrative workflows, yet splitting them into their constituent documents is difficult, especially for low-resource languages. We introduce Khondo (Bangla for split/segment), the first benchmark fo...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Khondo: A Multimodal Benchmark for Document Packet Splitting of Bangla Forms
1. 论文的主要贡献和创新点
✅ 解决的问题
文档包（多个文档拼接成单个文件）在政府行政工作流中普遍存在，但拆分困难，尤其针对孟加拉语这类低资源语言；现有相关数据集多基于英文、OCR文本构建，不适配视觉原生的低资源文档拆分需求。

🚀 提出的新方法与思路
**Khondo基准**：构建首个针对孟加拉语政府表单的文档包拆分基准，具备两大特性：一是双语（孟加拉语-英语）、视觉原生，模型可直接操作页面图像；二是覆盖5种拼接方案（从顺序到完全打乱），涉及14个行政领域，包含真实边界、领域类型和页面顺序的标注信息。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 适用语言类型 | 现有方法依赖高资源语言（如英文）的文本数据；Khondo适配低资源孟加拉语，支持双语场景 |
| 输入模态 | 现有方法基于OCR提取文本处理；Khondo为视觉原生，直接利用页面图像，避免OCR信息丢失问题 |
| 覆盖拼接方案 | 现有方法未系统覆盖从顺序到完全打乱的多种拼接形式；Khondo涵盖5种拼接方案，支持不同场景测试 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Khondo | 针对孟加拉语政府表单的文档包拆分基准，用于评测文档包拆分任务（含页面聚类和页面顺序恢复） |

🎯 实验设置与评估指标
实验任务为文档包拆分，包含页面聚类、页面顺序恢复两个子任务；论文未报告具体评估指标及含义。

⚔️ 基线方法对比
论文未报告基线方法的具体信息。

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能（L2/碰撞率等）**
论文未报告具体性能数值。

**效率对比（FPS / 参数量）**
论文未报告相关数据。

**跨域 / zero-shot迁移**
zero-shot评估下，MLLMs可较好将页面聚类到源文档，但恢复打乱后的页面顺序表现较差；实验覆盖14个行政领域的zero-shot场景，论文未提供具体性能数值。

**鲁棒性 / 扰动测试**
论文未报告相关测试结果。

**消融实验**
论文开展两项受控分析：（a）调整提示指令（是否包含显式页面顺序指令）；（b）调整数据包语言（孟加拉语vs英语）。结果：显式页面顺序指令是排序的必要但非充分条件；英语数据包排序性能优于孟加拉语数据包，页面顺序重构是核心挑战，语言是次要影响因素。

4. 关键结论和发现
- 主要发现：① 低资源语言（如孟加拉语）的文档包拆分中，页面顺序重构是比页面聚类更突出的难点；② 现有MLLMs在该任务的zero-shot场景下，聚类效果较好但排序能力不足；③ 页面顺序指令、数据包语言均影响排序性能，顺序本身是主导挑战，语言为次要稳定影响因素。
- 方法局限性：论文未报告
- 未来工作：聚焦视觉低资源文档理解中的页面顺序重构问题，推动相关技术落地于政府行政工作流。

> ✅ **总结一句话**：论文提出首个针对孟加拉语政府表单的双语视觉原生文档包拆分基准Khondo，通过实验明确了该任务中页面顺序恢复的核心难点，为低资源文档理解领域提供了可控的评测基准。

</details>

---

### 16. [Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills](https://arxiv.org/abs/2607.22529v1)

**Authors**: Siyuan Huang, Pengyu Cheng, Haotian Liu, Tao Chen, Yihao Liu, Jingwei Ni, Shijie Zhou, Ziyi Yang, Gangwei Jiang, Mengyu Zhou, Yu Cheng, Xiaoxi Jiang, Guanjun Jiang  
**Category**: cs.CL  
**Published**: 2026-07-27  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2607.22529v1  

#### Abstract
LLM training is shifting from manual design and annotation to interaction-driven self-evolution. However, existing self-evolutionary methods face a fundamental dilemma between task diversity and verification reliability: environment-bound methods obtain precise feedback but confine learning to narro...

---

### 17. [Quasi-Monte Carlo Initialization for Meta-Reinforcement Learning](https://arxiv.org/abs/2607.21637v1)

**Authors**: Julian G. Soltes  
**Category**: cs.LG  
**Published**: 2026-07-27  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.21637v1  

#### Abstract
This paper explores the efficacy of quasi-Monte Carlo (QMC) weight initialization for meta-reinforcement learning within modern benchmark environments. Various sampling methods are used to bound a population-based search and aggregate an optimal prior from a baseline set of tasks. The QMC meta-prior...

---

### 18. [Adjustment Speed as a Safety Constraint for Nonstationary Reinforcement Learning](https://arxiv.org/abs/2607.21646v1)

**Authors**: Timothy Tomashevskiy  
**Category**: cs.LG  
**Published**: 2026-07-27  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.21646v1  

#### Abstract
Ensuring safety in reinforcement learning under nonstationarity requires determining whether a learning system can safely adapt to forecasted environmental change within the required recovery horizon. Existing safe reinforcement learning methods typically assume stationary environments and do not ex...

---

### 19. [Cloud-Native Evaluation-as-a-Service: A Microservices Architecture for Scalable AI Monitoring with Conformal Guarantees](https://arxiv.org/abs/2607.21623v1)

**Authors**: Lei Yang  
**Category**: cs.LG  
**Published**: 2026-07-27  
**Score**: 23.5  
**Type**: new  
**ArXiv ID**: 2607.21623v1  

#### Abstract
We present EaaS, a cloud-native reference architecture that operationalizes AI evaluation methods as six stateless Kubernetes microservices: conformal prediction with finite-sample-corrected Adaptive Prediction Sets, calibration assessment, drift detection via RFF-approximated Maximum Mean Discrepan...

---

### 20. [LunarFM: A Shared Multimodal Representation of the Moon's Surface](https://arxiv.org/abs/2607.22408v1)

**Authors**: Marc Girona-Mata, Jakob Gawlikowski, Sumit Goski, Gautier Bardi de Fourtou, Valentin T. Bickel, Ben Moseley, Abigail Calzada-Diaz, Sylvester Kaczmarek, Ra\'ul Ramos-Poll\'an  
**Category**: cs.LG  
**Published**: 2026-07-27  
**Score**: 23.5  
**Type**: new  
**ArXiv ID**: 2607.22408v1  

#### Abstract
The renewed global focus on lunar exploration, driven by the prospect of in-situ resource utilization and a sustained human presence on the Moon, has created growing demand for accurate, large-scale characterization of the lunar surface. Although vast quantities of orbital remote-sensing data have b...

---

### 21. [Neural Feature Governance: Extending Atom Prevalence](https://arxiv.org/abs/2607.21671v1)

**Authors**: Idris Karel Seunda Ekwe, Patrick Tenga Shako, Ernest Parfait Fokou\'e  
**Category**: cs.LG  
**Published**: 2026-07-27  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2607.21671v1  

#### Abstract
Neural network compression and interpretability remain open challenges in modern deep learn- ing, where billion-parameter architectures deliver impressive accuracy at the cost of trans- parency, computational efficiency, and reliable uncertainty quantification. This paper introduces Neural Atom Prev...

---

### 22. [Smart predict-then-robustly-optimize](https://arxiv.org/abs/2607.21773v1)

**Authors**: Aakil Caunhye, Xuefei Lu, Belen Martin-Barragan  
**Category**: cs.LG  
**Published**: 2026-07-27  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2607.21773v1  

#### Abstract
In this paper, we propose and study a robust variant of the smart predict-then-optimize approach that accounts for prediction shifts due to disturbance in the covariate feature space. While traditional integrated-learning-and-optimization models assume that side information is perfectly revealed, em...

---

### 23. [Leveraging External Knowledge for Historical Document Restoration via Retrieval-Augmented Large Language Models](https://arxiv.org/abs/2607.21936v1)

**Authors**: Gabeen Kim, Kyeongpil Kang  
**Category**: cs.CL  
**Published**: 2026-07-27  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2607.21936v1  

#### Abstract
Historical documents act as invaluable knowledge archives but often suffer from illegibility due to physical deterioration and damage. While existing restoration methods based on masked language modeling effectively utilize local context, they struggle to restore named entities that require external...

---

### 24. [Evolution-Aware MSA Reasoning for Subsampling via Factor Graphs](https://arxiv.org/abs/2607.22314v1)

**Authors**: Zhangzhi Xiong, Minzhang Li, Haotian Yu, Sixian Shen, Kexin Zhang, Mingrui Li, Jie Zheng, Kewei Tu, Jingyi Yu  
**Category**: cs.LG  
**Published**: 2026-07-27  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2607.22314v1  

#### Abstract
Multiple Sequence Alignments (MSAs) provide protein language models with explicit evolutionary context, but their large depth makes subsampling unavoidable under limited token budgets. Existing strategies, including random selection, identity-based filtering, and diversity-driven sampling, are effec...

---

### 25. [MEUSLI: a Multilingual Projector for LLM-based ASR and Beyond](https://arxiv.org/abs/2607.22100v1)

**Authors**: Lorenzo Concina, Seraphina Fong, Marco Matassoni, Alessio Brutti  
**Category**: cs.CL  
**Published**: 2026-07-27  
**Score**: 14.5  
**Type**: new  
**ArXiv ID**: 2607.22100v1  

#### Abstract
Lightweight projectors are an established way to connect pre-trained speech encoders with large language models (LLMs), mapping acoustic features into token-level embeddings for tasks like ASR and spoken question answering. Existing systems, however, typically only support a few languages and are of...

---

### 26. [IFCLoRA: Topology-Aware Rank Allocation for Parameter-Efficient Fine-Tuning](https://arxiv.org/abs/2607.22251v1)

**Authors**: Wei Zhang, Xinwu Liu, Yihang Cheng  
**Category**: cs.LG  
**Published**: 2026-07-27  
**Score**: 14.5  
**Type**: new  
**ArXiv ID**: 2607.22251v1  

#### Abstract
Low-Rank Adaptation (LoRA) is a widely used parameter-efficient fine-tuning method for large language models, but its performance depends strongly on how a fixed rank budget is distributed across Transformer modules. Existing adaptive-rank methods usually rely on local gradient statistics collected ...

---

### 27. [Efficient Recommendations via Graph Coarsening and Label Propagation](https://arxiv.org/abs/2607.22287v1)

**Authors**: Alessandro Sbandi, Federico Siciliano, Fabrizio Silvestri  
**Category**: cs.LG  
**Published**: 2026-07-27  
**Score**: 14.5  
**Type**: new  
**ArXiv ID**: 2607.22287v1  

#### Abstract
Graph-based recommendations are widely adopted in real-world industrial applications. However, graphs in these systems often reach a massive scale, posing notable scalability and efficiency challenges. This requires techniques that can effectively balance predictive quality with computational cost. ...

---

### 28. [DCS: A Unified Conditional Sensitivity Framework for Cross-Modal Copyright Infringement Detection](https://arxiv.org/abs/2607.22035v1)

**Authors**: Xiafeng Man  
**Category**: cs.LG  
**Published**: 2026-07-27  
**Score**: 13.5  
**Type**: new  
**ArXiv ID**: 2607.22035v1  

#### Abstract
Currently, most foundation models can reproduce or strongly depend on copyrighted training content, but output similarity alone is insufficient for infringement detection, because similar outputs may also arise from public-domain concepts, common stylistic conventions, or ordinary statistical genera...

---

### 29. [Data Quality over Capacity: Internalizing Documents into LoRA Adapters for Closed-Book QA](https://arxiv.org/abs/2607.21861v1)

**Authors**: Joan Figuerola Hurtado  
**Category**: cs.CL  
**Published**: 2026-07-27  
**Score**: 13.0  
**Type**: new  
**ArXiv ID**: 2607.21861v1  

#### Abstract
We study baking documents directly into the weights of a 4-bit Gemma-4-e4b model via LoRA, so a system can answer questions about a corpus closed-book: no retrieval and no context-window budget. Across roughly 100 training runs from single documents to a 99-document corpus, we find that once adapter...

---

### 30. [An Introduction to Bayesian and Frequentist Simulation-Based Inference with Machine Learning](https://arxiv.org/abs/2607.21702v1)

**Authors**: Maximilian Dax, Theo Heimel, Gilles Louppe  
**Category**: cs.LG  
**Published**: 2026-07-27  
**Score**: 13.0  
**Type**: new  
**ArXiv ID**: 2607.21702v1  

#### Abstract
Simulation-based inference (SBI) with machine learning is an increasingly important tool for solving inverse problems in science and engineering, including parameter inference and the inversion of detector effects. We provide an overview of the Bayesian and frequentist statistical frameworks, descri...

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
