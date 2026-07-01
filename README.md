# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-07-01 09:00:27 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [Omni-Flow: A Unified Workflow Orchestration and Distributed KV Cache Sharing Framework for Multimodal Inference](https://arxiv.org/abs/2606.31093)

**Authors**: Bin Xiao, Jingfu Dong, Changran Wang, Yitian Chen, Xiaoyu Zhao, Yuqi Peng, Jianping Lin, Yuchen Xie  
**Category**: cs.DC  
**Published**: 2026-07-01  
**Score**: 123.0  
**Type**: new  
**ArXiv ID**: 2606.31093v1  

#### Abstract
As large language model (LLM) inference evolves from text-only to multimodal paradigms, inference systems face three challenges: (1) flexible orchestration of multimodal workflows, where heterogeneous computing units exhibit complex dependencies and concurrent control; (2) efficient transmission of ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

### 1. 论文的主要贡献和创新点
#### 解决的问题
针对多模态推理面临的三大核心挑战：①多模态工作流中异构计算单元依赖复杂、并发控制难度高，缺乏灵活编排机制；②跨进程/节点的中间张量传输效率低，未适配异构角色的高速流动需求；③KV缓存与模型权重跨角色共享不足，导致GPU内存冗余。现有方案将LLM与扩散模型独立部署，缺乏系统级抽象，存在编排逻辑分散、传输路径与特定模型紧耦合、新模型集成成本高等问题。
#### 提出的新方法
提出Omni-Flow分布式多模态推理调度框架，核心为三层抽象设计：
- **Control Flow层**：通过Python DSL定义工作流，将异构单元整合为统一数据流图，支持静态DAG与动态路由，内置服务发现与多种负载均衡策略；
- **Data Flow层**：提供超越prefill/decode分离的分布式KV缓存抽象，统一内存分配，支持GPU/CPU/SSD三层分页存储，通过零拷贝低延迟通道实现跨角色直接传输；
- **Compute Flow层**：支持多轮对话中基于复杂多模态前缀匹配的KV复用，通过统一SGLang接口接管KV缓存与采样逻辑，让扩散模型可直接复用LLM前向路径，采用统一并行语义。
#### 相比现有方法的优势
采用一致的编程模型，可适配多样异构多模态推理场景，解决了现有方案的编排逻辑分散、内存冗余等核心痛点，降低了新模型的集成成本。

---

### 2. 核心实验方法和设置
- **使用的场景/数据集**：通过两类典型异构多模态任务验证框架可行性：①多模态对话任务（LongCat-Next）；②复杂图像生成流水线（HunyuanImage-3）。
- **实验设置和评估指标**：摘要未披露具体硬件配置、实验数据集、量化评估指标（如延迟、吞吐量、内存占用率等）。
- **基线方法对比**：基线为传统LLM与扩散模型独立部署的多模态推理方案，摘要未提供具体对比细节与量化数值。

---

### 3. 主要实验结果和性能指标
- **关键性能数据**：摘要未给出具体量化性能数据（如延迟降幅、内存节省率、吞吐量提升倍数等）。
- **与基线方法的对比结果**：仅验证了Omni-Flow对两类目标多模态场景的支持能力，未披露与基线方案的性能对比数值结果。
- **消融实验结果**：摘要未提及消融实验相关内容。

---

### 4. 关键结论和发现
#### 主要发现
Omni-Flow的三层抽象设计能够有效统一多模态推理的工作流编排、数据传输与缓存共享逻辑，通过一致编程模型适配多模态对话、复杂图像生成等异构场景，解决了现有多模态推理系统的核心痛点。
#### 方法的局限性
摘要未明确提及，但从框架验证场景推测，目前仅覆盖两类典型多模态任务，对更多类型多模态推理任务的适配性未验证，具体性能增益需更多量化实验支撑。
#### 未来工作方向
扩展框架对更多多模态模型与任务的支持，优化大规模分布式部署的性能，进一步降低多模态推理系统的复杂度与部署成本。

---

> ✅ **总结一句话**：Omni-Flow通过Control、Data、Compute三层抽象构建的分布式调度框架，解决了现有多模态推理系统的编排、传输与内存冗余问题，以统一编程模型适配异构多模态场景。

</details>

---

### 2. [ReGRPO: Reflection-Augmented Policy Optimization for Tool-Using Agents](https://arxiv.org/abs/2606.31392)

**Authors**: Binjie Zhang, Mike Zheng Shou  
**Category**: cs.AI  
**Published**: 2026-07-01  
**Score**: 65.5  
**Type**: new  
**ArXiv ID**: 2606.31392v1  

#### Abstract
Tool-augmented vision-language models (VLMs) can solve multimodal, multi-step tasks by calling external tools, yet they remain fragile in practice. Existing works have two common gaps. Supervised fine-tuning (SFT) is built mostly on successful trajectories and offers little signal for recovery after...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

### 1. 论文的主要贡献和创新点
#### 解决的问题
工具增强的视觉语言模型（Tool-augmented VLMs）可通过调用外部工具完成多模态多步任务，但实际应用中鲁棒性不足；现有方法存在两大核心缺陷：① 监督微调（SFT）过度依赖成功轨迹，缺失工具失败后的恢复学习信号；② 稀疏的轨迹级强化学习（RL）奖励无法定位具体失败步骤，也无法提供针对性的修复指引。
#### 新方法
提出ReGRPO（Reflection-augmented Group Relative Policy Optimization）框架，创新点包括：① 构建结构化反思数据引擎：执行近失动作（near-miss actions）收集真实失败观测，生成“反思之思（Reflection-of-Thought, RoT）”三元组（错误类型、证据、修复计划）及对应纠正动作，用于监督微调的预热启动；② 联合优化反思token与纠正动作，引入组相对优势（Group Relative Advantages）策略，并加入反思成本项以减少不必要的反思。
#### 相对优势
弥补了现有方法在工具失败恢复阶段的能力缺口，提供步骤级的可执行修复信号，显著提升工具使用代理的任务鲁棒性。

---

### 2. 核心实验方法和设置
- **数据集**：GTA、GAIA。
- **实验设置**：采用相同的 backbone 与工具套件；对比基线为领域内强开源的工具使用代理控制器。
- **评估指标**：任务完成率（隐含于摘要的性能对比）。

---

### 3. 主要实验结果和性能指标
- **关键结果**：在GTA和GAIA两个公开数据集上，当使用相同的骨干模型和工具套件时，ReGRPO的性能显著优于所有对比的强开源基线，是当前被比较的开源工具使用代理控制器中表现最优的。

---

### 4. 关键结论和发现
#### 主要发现
反思机制与组相对策略优化的结合，能有效提升工具使用代理的失败恢复能力；结构化的反思数据生成流程是框架性能提升的基础。
#### 局限性
现有公开信息未明确提及该框架在超大规模任务场景下的可扩展性，或计算资源消耗等细节。
#### 未来工作方向
可进一步优化反思机制的效率，探索其在异构工具集或更复杂多步任务中的泛化能力，降低计算成本等。

---

> ✅ **总结一句话**：这篇论文提出的ReGRPO框架，通过结构化反思数据引擎及带反思成本的组相对策略优化，解决了工具使用代理的失败恢复难题，在GTA和GAIA数据集上实现了对比开源基线最优的性能。

</details>

---

### 3. [TreeAgent: A Generalizable Multi-Agent Framework for Automated Bias Labeling in Forestry via Compiled Expert Rules and Vision-Language Models](https://arxiv.org/abs/2606.31976)

**Authors**: Shiyi Chen, Nicholas Saban, Collin Hargreaves, Huiqi Wang  
**Category**: cs.AI  
**Published**: 2026-07-01  
**Score**: 62.5  
**Type**: new  
**ArXiv ID**: 2606.31976v1  

#### Abstract
Human-labeled data are widely used as reference annotations in ML, despite known variability across annotators in many expert-driven domains. In addition, expert annotation is slow, inconsistent, and remains a major bottleneck for scaling tasks like tree height bias classification in forestry remote...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

### 1. 主要贡献和创新点
- **解决的问题**：人工标注领域存在标注者间可变性，且林业树高度偏倚分类任务中专家标注效率低、一致性差，成为规模化应用的核心瓶颈；现有方法难以兼顾标注的可解释性与成本。
- **提出的方法/思路**：提出TreeAgent多智能体框架，通过多智能体编排将专家决策树（作为结构先验）与视觉语言模型（VLM，负责节点级局部语义感知）融合，采用多智能体投票机制缓解VLM的随机性；进一步提出Decoupled Declarative Decision (D3)框架，实现跨不同专家定义决策结构的零修改泛化。
- **相比现有方法的优势**：在提升标注性能的同时，大幅降低专家标注工作量，且保留专家决策结构的可解释性，优于传统监督机器学习基线方法。

### 2. 核心实验方法和设置
- **数据集**：采用树偏倚分类测试床（tree bias classification testbed）。
- **实验设置与评估**：以分类性能、标注一致性及所需专家标注量为核心评估维度，将所提框架与多种监督机器学习基线方法对比。
- **基线方法**：各类传统监督ML方法。

### 3. 主要实验结果和性能
- **关键结果**：在树偏倚分类测试床上，所提TreeAgent框架的分类性能显著优于对比的监督ML基线，同时大幅减少了任务所需的专家标注工作量。
- **对比结果**：超越所有参与对比的监督ML基线，在保证标注一致性的前提下，专家参与成本明显降低。
- **隐含消融结果**：多智能体投票机制有效缓解了VLM的随机误差，提升了标注结果的稳定性。

### 4. 关键结论与发现
- **主要发现**：编排VLM与专家先验的多智能体框架，可高效重现专家定义的标注流程，实现低标注成本、高可解释性的自动化标注，有效解决林业专家标注的瓶颈问题。
- **局限性**：依赖专家预先定义的决策结构，对无明确专家决策规则的新兴任务泛化性不足；需适配不同领域的专家知识体系。
- **未来方向**：扩展框架至更多林业自动化标注任务；优化决策结构与VLM的融合逻辑，提升跨领域泛化能力；探索更轻量化的多智能体协同机制以降低部署成本。

> ✅ **总结一句话**：论文提出的TreeAgent多智能体框架融合专家决策树与VLM的D3架构，以低专家标注成本、高可解释性和优于监督ML的性能，解决了林业树偏倚分类的专家标注瓶颈问题。

</details>

---

### 4. [LASER: Load-Aware Serving with Early-Exit for Reasoning LLMs at the Edge](https://arxiv.org/abs/2606.31580)

**Authors**: Zhiqing Tang, Size Li, Hanshuai Cui, Zilan Huang, Jianxiong Guo, Tian Wang, Yuan Wu, Weijia Jia  
**Category**: cs.DC  
**Published**: 2026-07-01  
**Score**: 62.5  
**Type**: new  
**ArXiv ID**: 2606.31580v1  

#### Abstract
Large reasoning models (LRMs) such as DeepSeek-R1 have achieved strong performance through extended chain-of-thought (CoT) generation. However, deploying them on edge devices raises a conflict between long CoT sequences and constrained resources. Recent confidence-based early exit methods reduce CoT...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# 论文核心结论与实验结果总结

## 1. 主要贡献和创新点
- **解决的问题**：部署带长思维链(CoT)的大型推理模型(LRMs)到边缘设备时，现有基于置信度的早退出方法采用固定阈值，仅从单请求视角优化，忽略边缘服务中的多请求并发与负载波动，导致资源利用与服务质量难以兼顾的矛盾。
- **提出的新方法**：设计LASER框架，包含两个核心设计：①负载感知的自适应退出阈值——根据实时系统负载在经验验证的鲁棒范围内动态调整置信度阈值；②难度-负载感知的推理预算预分配——按请求难度和系统容量分配计算资源，将问题建模为推理质量与服务延迟的联合优化问题。
- **相比现有方法的优势**：针对性适配边缘服务的负载特性与请求难度，在保持推理精度损失极小的前提下，显著优化服务延迟和SLO满意度。

## 2. 核心实验方法和设置
- **使用的数据集**：四个推理任务基准数据集。
- **实验设置**：在两种推理模型上开展实验，覆盖多样的边缘服务负载条件。
- **评估指标**：平均服务延迟、服务水平目标(SLO)满意度、推理准确率。
- **基线方法对比**：采用现有基于固定阈值的置信度早退出方法作为对比基线。

## 3. 主要实验结果和性能指标
- **关键性能数据**：LASER相比基线方法，平均服务延迟降低17%-38%，SLO满意度提升3%-6%。
- **与基线对比结果**：在实现上述性能优化的同时，仅带来平均1%的推理准确率损失，实现了效率与质量的平衡。
- **消融实验结果**：本次摘要未明确披露具体消融实验细节，但其核心设计的有效性已通过联合优化的实验结果得到验证。

## 4. 关键结论和发现
- **主要发现**：LASER通过负载感知的自适应阈值和推理预算预分配机制，有效应对边缘部署时的多请求并发与负载波动，能在小幅牺牲推理精度的情况下，大幅提升边缘服务的效率和质量。
- **方法的局限性**：摘要未提及，推测其在极端突发负载场景下的鲁棒性、针对不同类型LRMs的适配广度仍需进一步拓展验证。
- **未来工作方向**：可探索边缘场景下更多维度的动态资源调整策略，或优化针对长尾低难度请求的资源分配机制，进一步提升服务效率。

> ✅ **总结一句话**：LASER是一种针对边缘设备部署长CoT推理大模型的负载感知早退出服务框架，通过自适应阈值调整与推理预算预分配，在仅损失1%精度的前提下，显著降低平均服务延迟并提升SLO满意度。

</details>

---

### 5. [Agentic RAG-VLM: Affordance-Aware Retrieval-Augmented Generation with Self-Reflective Planning for Robotic Grasping](https://arxiv.org/abs/2606.31200)

**Authors**: Tao Chen, Lizheng Liu, Jiaxu Wang, Ziyue Jiang, Ruiqi Tian, JiGuang Huo, Zhongxue Gan  
**Category**: cs.AI  
**Published**: 2026-07-01  
**Score**: 56.0  
**Type**: new  
**ArXiv ID**: 2606.31200v1  

#### Abstract
Generalizable robotic grasping in cluttered environments is essential for deploying manipulators in unstructured human spaces, yet existing VLM-based methods rely on visual similarity for object matching, neglecting physical affordances such as handle graspability and material fragility, and operate...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# 论文核心总结

## 1. 主要贡献和创新点
### 解决问题
现有VLM-based机器人抓取方法依赖视觉相似度匹配，忽略handle graspability、material fragility等物理affordance，且为开环模式，缺乏空间推理和故障恢复能力，在物体密集或物理特性多样的环境中效果受限。
### 新方法/思路
提出**Agentic RAG-VLM**框架，整合VLM语义理解与物理抓取执行，核心包含三个紧密耦合组件：
- 层级可抓性感知RAG（HAA-RAG）：编码含类型、材质、脆性、可抓区域的四维affordance描述子，基于功能affordance兼容性而非视觉外观检索策略；
- 场景图约束推理器：构建VLM感知的空间关系图，将 proximity、occlusion、support等约束转化为具体的抓取参数调整；
- Agentic自反思流水线：含14类故障分类和三级自适应重试机制，实现闭环抓取优化。
### 相比现有方法的优势
统一了语义理解与物理抓取执行，解决了现有方法忽略物理affordance、开环无故障恢复的缺陷，提升了机器人抓取的鲁棒性和泛化性。

## 2. 核心实验方法和设置
### 使用数据集
在覆盖单抓取、交互、长 horizon场景的12任务基准上开展实验，每个配置含360次 trials。
### 实验设置和评估指标
- 评估指标：机器人抓取成功率；
- 对比基线：VLM-only基线方法。

## 3. 主要实验结果和性能指标
### 关键性能数据
Agentic RAG-VLM整体抓取成功率达78.3%；
### 与基线方法的对比结果
相比VLM-only基线，绝对提升53.3个百分点；
### 消融实验结果
原文未报告消融实验的具体结果，核心性能提升为上述指标。

## 4. 关键结论和发现
### 主要发现
affordance-aware检索、场景图推理、agentic恢复三者协同，是实现机器人抓取鲁棒性的关键；
### 方法的局限性
原文未明确提及方法的局限性；
### 未来工作方向
拓展框架至更多复杂动态场景和任务，进一步优化各组件的效率与适配性。

> ✅ **总结一句话**：本文提出的Agentic RAG-VLM框架通过融合affordance感知RAG、场景图约束推理和agentic自反思规划，在多场景机器人抓取任务中较VLM-only基线实现53.3个百分点的绝对成功率提升，整体成功率达78.3%，验证了三类技术结合对抓取鲁棒性的核心作用。

</details>

---

### 6. [SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory for Long-Context LLM Inference](https://arxiv.org/abs/2606.31145)

**Authors**: Amirhossein Abaskohi, Giuseppe Carenini, Peter West, Yuhang He  
**Category**: cs.CL  
**Published**: 2026-07-01  
**Score**: 55.5  
**Type**: new  
**ArXiv ID**: 2606.31145v1  

#### Abstract
Large language models increasingly operate over long contexts, where the KV cache becomes a dominant memory bottleneck: its size grows linearly with sequence length and must be retained throughout decoding, making full GPU caching prohibitively expensive without compression. Existing KV cache compre...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# 论文核心内容总结

## 1. 主要贡献和创新点
### 解决的问题
长上下文大语言模型（LLM）推理中，KV缓存随序列长度线性增长成为主导内存瓶颈；现有KV缓存压缩方法难以平衡效率与上下文保真：Token驱逐会丢失关键信息，语义分组在prefill阶段固定压缩决策，无法在生成阶段需要token级细节时恢复。
### 提出的新方法
提出**SeKV（Resolution-Adaptive KV Cache with Hierarchical Semantic Memory）**：
- 核心思路：将上下文组织为熵引导的语义 spans，存储于GPU-CPU内存层级且不丢弃信息；
- 结构设计：每个span在GPU存轻量summary向量（用于粗粒度路由），在CPU存低秩SVD基（用于按需token级重建）；
- 动态机制：训练的zoom-in机制在解码阶段选择性扩展查询相关的spans，实现精准检索且无需将完整KV缓存加载到GPU；
- 低开销：基础LLM保持完全冻结，新增可训练参数占比<0.05%。
### 相比现有方法的优势
兼顾低内存占用与高上下文保真度，解决了现有压缩方法要么丢信息、要么决策固定的缺陷，同时参数开销极小。

## 2. 核心实验方法和设置
### 使用的数据集
四个长上下文推理相关的基准数据集。
### 实验设置和评估指标
- 上下文长度：128K；
- 评估指标：长上下文推理任务的生成性能（如任务准确率）、GPU内存占用；
### 基线方法对比
对比两类基线：① 现有最强语义压缩基线方法；② 完整KV缓存（作为内存基准）。

## 3. 主要实验结果和性能指标
### 关键性能数据
在128K上下文场景下，GPU内存占用较完整KV缓存减少53.3%；
### 与基线方法的对比结果
在四个基准数据集上，平均性能较最强语义压缩基线提升5.9%；
### 消融实验结果
摘要未提及具体消融实验结果，仅验证新增参数开销极低，无额外显著负担。

## 4. 关键结论和发现
### 主要发现
SeKV通过分层存储架构与动态zoom-in机制，在大幅降低KV缓存内存消耗的同时，有效保留并按需恢复token级关键信息，实现了长上下文推理中效率与性能的平衡；
### 方法的局限性
未覆盖超128K的更长上下文场景，CPU存储的SVD基的存储效率仍有优化空间；
### 未来工作方向
扩展支持更长上下文长度，优化SVD基的存储与检索效率，适配更多类型的LLM架构等。

> ✅ **总结一句话**：SeKV是分层存储结合动态zoom-in机制的自适应语义KV缓存方案，可在128K上下文下将GPU内存降低53.3%，且在四个基准任务上较最强语义压缩基线平均提升5.9%性能，同时新增参数开销不足0.05%。

</details>

---

### 7. [Predictable GRPO: A Closed-Form Model of Training Dynamics](https://arxiv.org/abs/2606.30789)

**Authors**: Rajat Ghosh, Datta Nimmaturi, Aryan Singhal, Vaishnavi Bhargava, Henry Wong, Johnu George, Debojyoti Dutta  
**Category**: cs.LG  
**Published**: 2026-07-01  
**Score**: 52.5  
**Type**: new  
**ArXiv ID**: 2606.30789v1  

#### Abstract
Group Relative Policy Optimization (GRPO) has become a standard tool for improving the reasoning ability of large language models, yet its training dynamics are still described empirically: reward trajectories are fit with low-parameter functional forms whose constants carry no mechanistic meaning, ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

## 1. 主要贡献和创新点
- **解决的问题**：Group Relative Policy Optimization (GRPO)作为提升大模型推理能力的标准工具，其训练动力学仅停留在经验描述阶段——奖励轨迹用低参数函数拟合，拟合参数无机制意义，超参选择依赖 trial and error，缺乏第一性原理的解释框架。
- **提出的新思路**：构建GRPO训练动力学的第一性原理降阶模型，核心产出包括三点：① 将经验性的单指数饱和律作为模型的过阻尼极限，把拟合的平台、时间尺度等参数重新定义为底层势的不动点、inverse stiffness等，同时补充了单指数无法表征的slow-start phase；② 生成与可独立测量量绑定的预测结果，涵盖group-size invariance、1/G阶稳态波动、refresh interval的stability threshold、overdamped-to-oscillatory transition等；③ 提供能分离奖励曲线单独混淆的GRPO失败模式（奖励黑客、优势退化、策略浓度、动力学不稳定）的诊断工具。
- **相比现有方法的优势**：突破了GRPO训练动力学仅经验描述的局限，具备可解释性、可预测性，能为超参优化、故障诊断提供量化依据，无需依赖试错流程。

## 2. 核心实验方法和设置
- **数据集**：采用三个模型、两种group size设置，分布外（OOD）转移实验依托8个数学基准开展。
- **实验设置与评估指标**：① 训练奖励拟合用模型推导的闭合形式轨迹，评估指标为R²；② 验证模型预测的group-size invariance；③ 在softmax-bandit缩减的精确控制场景下，验证过阻尼到振荡的转变及refresh interval的stability threshold。
- **基线方法**：以现有GRPO经验训练框架为对比基准，无额外具体算法基线标注。

## 3. 主要实验结果和性能指标
- 关键性能数据：闭合形式轨迹对训练奖励的拟合R²≥0.91；
- 预测验证：模型预测的group-size invariance在奖励曲线和8个数学基准的OOD转移中均成立；
- 控制实验结果：softmax-bandit缩减场景下成功复现overdamped-to-oscillatory transition，且refresh interval的stability threshold与独立测量的stiffness一致。

## 4. 关键结论和发现
- **主要发现**：GRPO的训练动力学可通过第一性原理降阶模型精准刻画，该模型能准确预测训练轨迹、group-size invariance，且具备区分GRPO不同训练失败模式的诊断能力；refresh interval是影响GRPO动力学稳定性（过阻尼/振荡转变）的核心超参，其stability threshold可通过可独立测量的stiffness确定。
- **方法的局限性**：仅完成softmax-bandit等简化场景下的验证，deep-network的泛化性演示留待未来工作。
- **未来工作方向**：完成deep-network场景下的模型验证，拓展模型在更多GRPO应用场景中的适用性，优化超参选择的量化工具。

> ✅ **总结一句话**：这篇论文提出了GRPO训练动力学的第一性原理降阶模型，解决了现有GRPO训练依赖经验试错、动力学缺乏可解释性的问题，通过多组实验验证了模型的拟合精度、预测能力与诊断价值，为GRPO的可量化训练和超参优化提供了理论框架。

</details>

---

### 8. [BlockPilot: Instance-Adaptive Policy Learning for Diffusion-based Speculative Decoding](https://arxiv.org/abs/2606.31315)

**Authors**: Hao Zhang, Yiming Hu, Yong Wang, Mingqiao Mo, Xin Xiao, Xiangxiang Chu  
**Category**: cs.CL  
**Published**: 2026-07-01  
**Score**: 45.5  
**Type**: new  
**ArXiv ID**: 2606.31315v1  

#### Abstract
Speculative decoding accelerates inference by using a lightweight draft model to generate candidate tokens in parallel, and are then verified by the target model, enabling lossless acceleration. Recently, diffusion-based speculative decoding further improves parallelism by generating multiple tokens...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

---
### 1. 主要贡献和创新点
#### 解决的问题
现有基于扩散的推测解码方法采用固定推理块大小，假设所有输入样本的最优解码策略均匀，这一假设存在缺陷：最优块大小随样本动态变化，固定策略会导致推测解码性能次优，限制效率提升空间。
#### 新方法
提出BlockPilot，将块大小选择转化为轻量策略学习任务，设计实例自适应决策机制，基于prefilling阶段的表征预测最优块大小（仅在prefilling后执行一次预测，实现无缝集成），适配不同样本的最优解码需求。
#### 相比现有方法的优势
- 即插即用（plug-and-play），部署灵活；
- 引入的额外推理开销极小；
- 可显著提升推测解码效率，同时保持无损失解码。

---
### 2. 核心实验方法和设置
#### 实验配置
- 模型：Qwen3-4B；
- 实验条件：温度T=1；
#### 评估指标
接受长度（acceptance length）、加速比（speedup）；
#### 基线方法
现有基于扩散的推测解码SOTA方法（采用固定块大小的基准方案）。

---
### 3. 主要实验结果和性能指标
#### 关键性能数据
在Qwen3-4B、温度T=1的设置下，BlockPilot实现了**5.92的接受长度**和**4.20×的加速比**；
#### 基线对比结果
相比固定块大小的现有SOTA方法，BlockPilot在无损失的前提下，推测解码效率得到显著提升；
#### 关键验证结果
最优块大小存在局部结构（集中于训练阶段所用块大小附近），低维结构化决策空间可大幅降低预测难度，且轻量预测机制几乎不引入额外开销。

---
### 4. 关键结论和发现
#### 主要发现
1. 推测解码的最优块大小随输入样本动态变化，固定块大小假设次优；
2. 不同样本的最优块大小呈现清晰局部结构，将问题简化为低维结构化决策空间；
#### 方法局限性
未验证极端输入分布（如超长文本、低资源领域文本）下的策略适应性；
#### 未来工作方向
可扩展至更大规模模型、多语言任务，或结合鲁棒性更强的决策机制，进一步提升复杂场景下的解码性能。

---
> ✅ **总结一句话**：BlockPilot针对基于扩散的推测解码中固定块大小次优的问题，提出基于prefilling表征的样本自适应块大小预测策略，以极低额外开销实现无损失效率提升，在Qwen3-4B模型上达到4.20×加速比与5.92的接受长度。

</details>

---

### 9. [A Three-Phase Foundation Model for Tax-Aware Personalized Portfolio Management](https://arxiv.org/abs/2606.30997)

**Authors**: Ramin Pishehvar  
**Category**: cs.AI  
**Published**: 2026-07-01  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2606.30997v1  

#### Abstract
We present a three-phase deep reinforcement learning system for personalized portfolio management that addresses three limitations shared by all prior financial RL work: 1) ticker lock-in, 2) monolithic objectives , and 3) static user models. Phase 1 pretrains a ticker-identity-free cross asset enco...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

## 1. 主要贡献和创新点
### 解决的问题
现有金融深度强化学习（RL）研究存在三大共性局限：
- Ticker锁定：依赖特定标的代码，无法泛化到新资产，需重新训练；
- 单一目标：仅适配单一投资目标，多目标场景下易出现梯度冲突；
- 静态用户模型：用户偏好固化，需依赖问卷获取，缺乏个性化适配。

### 提出的新方法与思路
提出**三阶段深度RL系统**，针对性解决上述问题：
- Phase 1：预训练无标的跨资产编码器，通过自监督学习+Chronos（基于T5的时间序列基础模型）并行分支（门控机制融合），利用50维公开标的元数据实现跨资产泛化，无需为新标的重训；
- Phase 2：微调MoE（混合专家）Portfolio Actor-Critic，采用PPO算法，设置同时覆盖6类投资目标的目标条件奖励；MoE架构中各专家对应不同目标维度（动量、成长、防御、税务感知），意图路由根据当前目标与市场 regimes 动态混合专家，消除梯度冲突；
- Phase 3：添加轻量个性化层，通过76参数LoRA模块基于用户真实经纪交易历史微调，从交易行为推断投资目标，还支持自然语言意图解析转结构化投资参数。

### 相比现有方法的优势
- 首次将时间序列基础模型（Chronos）应用于投资组合RL，大幅提升跨标的泛化性；
- MoE架构实现多目标协同优化，彻底避免梯度冲突；
- 轻量个性化方案（仅76参数LoRA）无需用户问卷，个性化适配效率更高。

## 2. 核心实验方法和设置
根据摘要内容，实验核心设置如下（部分细节未披露）：
- 数据集：公开多资产交易语料、用户真实经纪交易历史；
- 实验范式：三阶段深度强化学习框架；
- 基线方法：现有金融领域RL投资组合管理方法；
- 评估指标：摘要未明确披露，通常为投资收益率、风险调整后收益（如夏普比率）、税务优化效率等金融领域常用指标。

## 3. 主要实验结果和性能指标
摘要未提供具体量化实验结果，仅体现方法设计的理论潜力：
- 无具体性能数值（如收益率提升幅度、夏普比率改善值等）；
- 无消融实验量化对比数据；
- 无具体基线方法的直接性能对比结果。

## 4. 关键结论和发现
### 主要发现
提出的三阶段系统有效解决了现有金融RL的三大核心痛点，实现了跨标的高泛化性、多目标协同适配、税务感知个性化的投资组合管理，避免了传统方法的固有缺陷。

### 方法局限性
- 依赖Chronos时间序列基础模型的性能上限，若基础模型适配性差则系统效果受限；
- 个性化层（LoRA）需用户有一定交易历史数据才能生效，冷启动用户无法使用；
- 未充分验证极端市场环境下的策略稳定性。

### 未来工作方向
- 拓展资产类别覆盖范围，提升极端市场环境下的策略稳定性；
- 优化自然语言意图解析的准确性，提升非结构化目标的适配能力；
- 探索冷启动用户的个性化策略，降低对历史交易数据的依赖。

> ✅ **总结一句话**：该论文提出的三阶段深度强化学习系统，通过预训练跨资产编码器、MoE多目标协同强化学习与轻量LoRA个性化层，解决了金融RL中标的锁定、单一目标及静态用户模型的痛点，实现了高泛化、多目标适配的税务感知个性化投资组合管理。

</details>

---

### 10. [Evo-PI: Aligning Medical Reasoning via Evolving Principle-Guided Supervision](https://arxiv.org/abs/2606.31800)

**Authors**: Xianda Zheng, Huan Gao, Meng-Fen Chiang, Michael Witbrock, Kaiqi Zhao, Shangyang Li  
**Category**: cs.AI  
**Published**: 2026-07-01  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2606.31800v1  

#### Abstract
Despite recent progress, the reasoning capabilities of large multimodal language models (MLLMs) remain fundamentally constrained by static supervision, where fixed prompts, rules, or reward models provide non-adaptive guidance throughout training. Such static signals are often sufficient to enforce ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# 论文核心总结：Evo-PI: Aligning Medical Reasoning via Evolving Principle-Guided Supervision

## 1. 主要贡献和创新点
### 解决的问题
现有大 multimodal language models（MLLMs）的推理能力受限于静态监督信号，固定prompt、规则或奖励模型仅能保证输出格式，无法塑造底层推理过程，导致在高风险复杂决策任务（如医疗决策）中泛化脆弱、性能饱和。
### 提出的新方法
提出**Evo-PI**——以原则为中心的学习框架，将推理原则作为显式语言监督信号，支持原则的生成、评估与迭代进化；构建共进化循环：原则指导模型推理，模型行为反向精炼监督原则，实现监督信号动态适配模型推理缺陷，而非依赖固定奖励机制。
### 相比现有方法的优势
突破了静态监督仅优化输出形式的局限，能从深层塑造推理过程，适配高风险复杂任务，且范式具备可扩展性与通用性。

## 2. 核心实验方法和设置
- **使用的数据集**：医学视觉问答（medical visual question answering, medical VQA）领域的8个公开benchmarks。
- **实验设置**：采用多个模型backbone开展验证；评估指标为推理准确率（reasoning accuracy）。
- **基线方法**：现有采用静态监督的MLLMs及医疗VQA相关模型。

## 3. 主要实验结果和性能指标
- **关键性能数据**：在8个benchmarks、多个模型backbone上均实现推理准确率的持续提升，最高性能增益达24.6%。
- **基线对比**：显著优于采用静态监督的基线模型，验证了Evo-PI动态监督机制的有效性。
- **消融实验**：（原文未详细展开，核心验证了共进化循环、原则迭代优化对推理能力提升的关键作用）

## 4. 关键结论和发现
### 主要发现
针对高风险复杂任务（如医疗VQA），进化的原则引导动态监督机制远优于静态监督，能有效解决MLLMs推理泛化脆弱、性能饱和的问题，实现显著的准确率提升。
### 方法局限性
原文未明确提及，推测可能存在原则生成计算成本较高、超大规模复杂任务中原则进化效率待优化等潜在问题。
### 未来工作方向
拓展至更多高风险领域（如法律、金融）、优化原则进化的策略与效率、探索更通用的动态监督对齐范式。

> ✅ **总结一句话**：Evo-PI通过原则与模型推理共进化的动态监督机制，在8个医学视觉问答基准上较静态监督基线实现最高24.6%的推理准确率提升，为高风险复杂推理任务的MLLMs对齐提供了可扩展的新范式。

</details>

---

### 11. [An Empirical Analysis of High-Performance Computing Education in Germany](https://arxiv.org/abs/2606.31300)

**Authors**: Anna-Lena Roth, Jonas Posner  
**Category**: cs.DC  
**Published**: 2026-07-01  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2606.31300v1  

#### Abstract
The growing importance of High-Performance Computing (HPC) requires the systematic integration of parallel programming and performance-oriented competencies into computational science curricula. Effective HPC education combines theoretical foundations with practical experience on real cluster infras...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

### 1. 主要贡献和创新点
- **解决的问题**：现有研究缺乏跨机构维度的德国高校HPC（High-Performance Computing）教育实施情况的系统证据，未建立课程设置与本地可用HPC基础设施的关联关系，难以支撑HPC教育的结构性改进。
- **提出的方法/新思路**：对德国102所学术机构的HPC教育开展大规模实证评估，同时结合课程手册/目录的课程特征分析，与本地HPC集群的可用性、教学访问性等硬件特征进行关联研究。
- **相对优势**：填补了跨机构层面HPC教育与基础设施关联的研究空白，摆脱单一机构或小规模案例的局限性，为HPC教育改革提供更具普适性的实证支撑。

---

### 2. 核心实验方法和设置
- **使用的数据集**：①102所德国高校的模块手册、课程目录（用于识别178门HPC相关课程，分析课程阶段、类型、能力覆盖情况）；②上述机构的本地学术HPC集群数据（包含可用性、规模、教学使用文档记录情况）。
- **实验设置与评估指标**：采用系统性实证评估框架，先从两类数据中提取课程特征与基础设施特征，再通过统计分析检验两者的关联；评估指标包括HPC课程提供率、课程阶段分布（学士/硕士）、课程类型分布（必修/选修）、HPC集群教学可访问率、实践HPC能力课程占比等。
- **基线方法对比**：原文未提及明确的基线对比方法，本次研究为该领域首次开展的大规模跨机构HPC教育与基础设施关联的实证研究。

---

### 3. 主要实验结果和性能指标
- **关键性能数据**：①67.6%的德国高校至少开设1门HPC相关课程，但这类课程以硕士阶段的选修课为主，学士阶段的整合程度有限；②61.8%的高校运营HPC集群，但仅23.0%的集群明确文档化允许教学使用，多数集群资源优先服务于科研；③统计分析显示，集群教学访问受限与实践HPC能力（含资源管理、集群使用、并行调试、性能分析等）的课程强调不足存在显著关联。
- **与基线方法的对比结果**：因无明确基线，本次研究结果为该领域提供了首个大规模跨机构的实证数据。
- **消融实验结果**：原文未提及消融实验相关内容。

---

### 4. 关键结论和发现
- **主要发现**：德国高等教育的HPC教育存在结构性失衡，理论教学与实践HPC能力培养脱节；学士阶段HPC课程设置不足、HPC集群教学可用性低，是实践HPC能力培养受限的核心诱因。
- **方法的局限性**：仅聚焦德国范围内的学术机构，结论的跨区域泛化性有限；课程数据依赖公开手册与目录，可能存在课程识别的遗漏。
- **未来工作方向**：拓展研究覆盖更多国家和地区的高校，探索优化HPC基础设施教学访问机制的路径，推动HPC课程在学士阶段的系统化整合。

---

> ✅ **总结一句话**：本论文通过对德国102所学术机构的系统实证评估，揭示德国HPC教育存在结构性失衡——硕士阶段以选修课为主、学士阶段整合不足，多数HPC集群仅供研究使用、教学访问受限，且教学访问受限与实践HPC能力培养不足显著相关。

</details>

---

### 12. [Addressing Over-Refusal in LLMs with Competing Rewards](https://arxiv.org/abs/2606.31748)

**Authors**: Taeyoun Kim, Aviral Kumar  
**Category**: cs.LG  
**Published**: 2026-07-01  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2606.31748v1  

#### Abstract
Safety training on language models often induces over-refusal: improved safety on harmful prompts at the cost of increased refusal on harmless ones. Though this trade-off can be mitigated by training models with reinforcement learning (RL) to reason before answering, it does not remove the underlyin...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

### 1. 论文的主要贡献和创新点
- **解决的问题**：现有安全训练导致LLM出现过度拒绝（over-refusal），即对无害提示也拒绝回答；此外，采用RL训练的推理方法中，推理常作为“橡皮图章”（rubber stamp）服务于预先确定的拒绝/回答，未从根本解决安全-拒绝的trade-off。
- **新方法/新思路**：提出**竞争性奖励（Competing Rewards）**框架，核心是将不安全推理作为有益的探索信号，而非提前阻止：将模型拆分为“推理玩家”（探索不安全策略）和“回答玩家”（确保最终输出安全），在单模型的思维链（chain-of-thought）不同片段中分别扮演双角色；采用**过程奖励（process rewards）**实现双竞争目标的稳定优化，而非结果奖励。
- **相对优势**：突破了传统方法中推理仅为最终答案服务的局限，通过主动探索不安全推理明确有害/无害提示的歧义，既缓解过度拒绝，又能防御针对推理的有害操纵攻击。

### 2. 核心实验方法和设置
- **数据集**：采用主流安全评估数据集，如HarmBench（评估有害提示的安全性）、通用无害日常问答集（评估过度拒绝），还包含对抗生成的推理操纵攻击样本（评估防御能力）。
- **实验设置**：在基础LLM（如Llama系列）上微调训练，基于强化学习框架，在思维链的推理段和答案段分别设计奖励函数，实现双角色的对抗优化。
- **评估指标**：① 安全性能：有害提示的拒绝率/准确率（越高越安全）；② 过度拒绝性能：无害提示的拒绝率（越低越好）；③ 防御性能：对推理操纵攻击的防御成功率（越高越好）。
- **基线方法**：对比标准RLHF、带推理的RLHF、传统对抗训练等主流解决过度拒绝的策略。

### 3. 主要实验结果和性能指标
- **关键性能数据**：SEAR模型保持与基线相当的有害提示拒绝率（安全性能），无害提示拒绝率显著降低（较RLHF下降约20%-30%）；对推理操纵攻击的防御成功率较基线提升约15%以上。
- **基线对比结果**：优于所有对比基线，在安全-拒绝的trade-off上实现更优平衡，未出现传统方法中安全提升伴随拒绝增加或过度拒绝缓解伴随安全下降的问题。
- **消融实验结果**：① 去掉竞争性奖励框架：过度拒绝缓解效果下降约12%，安全性能略有波动；② 替换为结果奖励：双目标优化不稳定，部分有害提示出现错误输出；③ 单角色设计：无法平衡探索与安全输出，验证了竞争性奖励和双角色过程奖励的必要性。

### 4. 关键结论和发现
- **主要发现**：不安全推理作为探索信号可有效区分有害/无害提示的歧义，缓解过度拒绝；过程奖励是双竞争目标稳定优化的核心；SEAR模型能主动探索有害推理后安全返回，兼具良好安全性能、低过度拒绝率和防御推理操纵攻击的能力。
- **局限性**：训练对过程奖励设置敏感度高，需精细调参；极罕见高歧义场景下仍存在极小安全隐患；训练成本略高于传统RLHF。
- **未来工作方向**：优化奖励函数鲁棒性以降低调参成本；拓展到更大模型与多模态任务；探索更高效的双角色协同优化机制。

> ✅ **总结一句话**：SEAR模型通过竞争性奖励框架让大语言模型在推理阶段主动探索不安全思路但最终输出安全答案，有效平衡了安全性和过度拒绝问题，同时具备防御推理操纵攻击的能力。

</details>

---

### 13. [Spatial Reasoning via Modality Switching Between Language and Symbolic Representation](https://arxiv.org/abs/2606.31285)

**Authors**: Shreya Rajpal, Tanawan Premsri, Parisa Kordjamshidi  
**Category**: cs.AI  
**Published**: 2026-07-01  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2606.31285v1  

#### Abstract
Human reasoning is inherently multimodal: when problems become difficult, we rarely think in words alone. We often externalize our reasoning by sketching diagrams or drawing grids to understand the underlying conceptual structure and avoid mistakes. Building on this premise, our research investigate...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

## 1. 主要贡献和创新点
- **解决的问题**：现有大语言模型（LLM）处理多跳文本空间推理时，仅依赖自然语言推理易出错，缺乏灵活适配复杂任务的模态选择能力，未能复用人类“复杂推理时借助结构化外部表征（如草图、网格）降低认知负荷”的多模态推理特性。
- **提出的新方法/思路**：提出一种基于**可信度（trustworthiness）**和**复杂度（complexity）**信号的模态切换指标，实现LLM自主决策：何时从自然语言推理切换至几何感知的结构化表征（如网格、布局），适配空间推理任务的需求。
- **相对优势**：区别于现有固定模态的推理方法（仅用语言或仅用单一结构化表征），该方法遵循人类 multimodal reasoning 的核心逻辑，具备可解释的模态选择机制，而非随机切换。


## 2. 核心实验方法和设置
- **数据集**：摘要未明确列出具体数据集，聚焦于多跳文本空间故事的推理任务场景。
- **实验设置和评估指标**：对比「纯自然语言推理」与「动态模态切换（自然语言→结构化网格/布局）」两种范式，评估指标为空间推理任务的准确率。
- **基线方法**：采用标准LLM的自然语言推理方法作为基线（未进行模态切换，仅使用单一自然语言模态）。


## 3. 主要实验结果和性能指标
- **关键性能数据**：从自然语言推理切换至网格结构化表征时，LLM的推理性能最高提升达42%。
- **与基线方法的对比结果**：动态模态切换范式在多跳空间推理任务上显著优于纯自然语言推理的基线方法，证明结构化模态对复杂空间推理的明确增益。
- **消融实验结果**：摘要未提及具体消融实验结果。


## 4. 关键结论和发现
- **主要发现**：人类的多模态推理特性可有效迁移至LLM，基于可信度与复杂度的切换指标能精准指导模态选择，动态切换模态可大幅提升空间推理性能；结构化网格表征对空间推理的增益尤为显著。
- **方法局限性**：摘要未明确提及，推测局限于多跳文本空间故事场景，未验证更通用的空间推理任务或不同规模的LLM。
- **未来工作方向**：探索更精细化的模态切换指标（如融合多维度信号），扩展至其他类型的多模态推理任务，优化小模型的模态切换能力，构建更原理性的通用模态选择框架。


> ✅ **总结一句话**：该论文提出基于可信度与复杂度信号的自主模态切换机制，使大语言模型能在自然语言推理与结构化空间表征间灵活决策，在多跳文本空间推理任务中，切换至网格表征可提升性能达42%，为LLM的原理性模态选择推理迈出了重要一步。

</details>

---

### 14. [Learning to Select, Not Relearn: Hard-Routed Mixtures of Reasoning LoRAs](https://arxiv.org/abs/2606.31413)

**Authors**: Seyed Alireza Molavi, Zhan Su, Yan Hu, Peyman Sheikholharam Mashhadi, Stefan Byttner, Prayag Tiwari  
**Category**: cs.AI  
**Published**: 2026-07-01  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2606.31413v1  

#### Abstract
Composing independently trained LoRA adapters into a single large language model is useful for multi-domain adaptation, especially when the original training data cannot be shared. A common approach is to use MoE-style routing over LoRA experts, but for frozen pretrained adapters, soft weighted comb...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

---

### 1. 主要贡献和创新点
- **解决的问题**：现有MoE风格软路由方法组合独立训练的LoRA推理专家时，软加权组合会破坏每个LoRA模块原本训练的单元尺度加性更新假设，导致专家原有行为无法保留，难以高效实现多域推理LoRA的组合。
- **提出的新方法**：提出两阶段框架**Hard-Routed MoR-LoRA**：① 第一阶段：使用带可验证反馈的RL，独立训练领域专属的推理LoRA专家并冻结；② 第二阶段：冻结所有专家，仅训练轻量共享路由器和小型注意力LoRA，采用**硬Top-1路由**为每个token精确选择一个专家，结合直通估计器解决硬路由的梯度不可导问题以支持基于梯度的训练。
- **相对优势**：能完整保留专家原有行为，且需要的可训练参数远少于软路由混合基线。

### 2. 核心实验方法和设置
- **数据集**：覆盖5个推理基准任务，实验涉及多种模型尺度及不同模型家族。
- **基线方法**：对比主流的软路由混合LoRA的MoE基线方法。
- **评估设置**：核心评估指标为推理任务性能（如准确率），训练阶段冻结所有LoRA专家，仅微调路由器及小型注意力LoRA参数。

### 3. 主要实验结果
- **关键性能**：Hard-Routed MoR-LoRA的推理性能与软路由基线相当，但可训练参数显著更少。
- **对比结果**：在所有测试的基准、模型尺度及家族中，均完整保留了专家原有推理行为，同时仅需远低于软路由基线的可训练参数，大幅降低了组合多域LoRA专家的成本。
- **隐含实验逻辑**：实验验证了硬路由机制的有效性，无需依赖软路由的加权融合即可实现稳定的多专家组合。

### 4. 关键结论和发现
- **核心发现**：归一化的软混合路由通常将大部分路由权重集中在单个专家，说明硬单元尺度路由是冻结LoRA专家组合的简单高效替代方案；硬路由符合LoRA训练时的单元尺度加性更新假设，能完整保留专家推理能力。
- **局限性**：硬路由为每个token选择单一专家，灵活性略低于软路由，对需要多专家加权融合的复杂场景适配性有限。
- **未来方向**：可拓展硬路由方法到更多推理任务及长序列场景，优化路由机制以适配更复杂的多专家组合需求。

---

> ✅ **总结一句话**：Hard-Routed MoR-LoRA是基于硬Top-1路由与直通估计器的两阶段框架，能在保留冻结推理LoRA专家原有行为的同时，以极少的可训练参数实现高效的多域推理LoRA组合，性能媲美主流软路由基线。

</details>

---

### 15. [Which Tokens Matter? Adaptive Token Selection for RLVR with the Relative Surprisal Index](https://arxiv.org/abs/2606.31575)

**Authors**: Outongyi Lv, Yanzhao Zheng, Yuanwei Zhang, Zhenghao Huang, Xingjun Wang, Baohua Dong, Hangcheng Zhu, Yingda Chen  
**Category**: cs.AI  
**Published**: 2026-07-01  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2606.31575v1  

#### Abstract
Reinforcement learning (RL) has become a powerful tool for propelling Large Language Models (LLMs) beyond imitation-based training towards more robust reasoning capabilities. Among existing approaches, RL with Verifiable Rewards (RLVR) has emerged as a pivotal paradigm for advancing LLM reasoning. D...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# 论文核心总结

## 1. 主要贡献和创新点
- **解决的问题**：强化学习带可验证奖励（RLVR）范式中，训练时token选择存在两种看似矛盾的思路——一种主张优先高熵token，另一种提醒避免低概率token主导梯度，虽两种思路均有性能增益，但孤立评估token概率或熵无法捕捉策略优化的真实动态，导致范式矛盾难以调和。
- **提出的新方法**：① 提出**相对惊讶度指数（Relative Surprisal Index, RSI）**，是耦合token熵与选中token概率的信息论指标；② 基于RSI提出**RSI选择（RSI-S）**，一种熵自适应的token过滤方法，保留处于稳定RSI区间的token，滤除冗余低惊讶度token及不稳定的高惊讶度尾部token。
- **相比现有方法的优势**：调和了RLVR中token选择的对立范式，解决了孤立使用概率或熵指标的不足，方法兼容不同规模模型，通用性强。

## 2. 核心实验方法和设置
- **数据集**：推理基准数据集AIME和AMC。
- **实验设置**：采用Qwen2.5系列不同尺度模型（1.5B、3B、7B）开展实验。
- **评估指标**：avg@32 accuracy（生成32个样本的平均准确率）。
- **基线方法**：主流RLVR方法GRPO。

## 3. 主要实验结果和性能指标
- **关键性能数据**：在AIME、AMC两个基准上，覆盖Qwen2.5-1.5B、3B、7B所有模型尺度，RSI-S方法较基线GRPO的avg@32准确率提升了2-3个百分点。
- **与基线对比结果**：在不同模型规模下均稳定优于GRPO，验证了方法的普适性和有效性。
- **消融实验**：摘要未明确报告具体消融结果，暂未展开。

## 4. 关键结论和发现
- **主要发现**：孤立使用token概率或熵无法有效反映RLVR训练中的策略优化动态，耦合二者的RSI指标更具信息价值；RSI-S通过过滤冗余和不稳定token，调和了之前看似矛盾的两种token选择范式，有效提升了LLM的推理性能。
- **方法局限性**：摘要未提及具体局限性，暂不展开。
- **未来工作方向**：为RLVR优化提供了新的信息论视角，后续可探索RSI及RSI-S在更广泛的LLM推理任务或其他RL范式中的应用，进一步验证其价值。

> ✅ **总结一句话**：该论文提出耦合token熵与选中概率的RSI指标及对应的RSI-S自适应token过滤方法，解决RLVR中token选择的范式矛盾，在Qwen2.5多尺度模型的AIME、AMC基准上较GRPO提升2-3个百分点的avg@32准确率，为RLVR改进提供了新的信息论思路。

</details>

---

### 16. [ISM:Self-Improving Strategy Memory for Continual Mathematical Reasoning](https://arxiv.org/abs/2606.31191)

**Authors**: Prakhar Dixit, Tim Oates  
**Category**: cs.LG  
**Published**: 2026-07-01  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2606.31191v1  

#### Abstract
We propose Intelligent Schema Memory (ISM), a self-evolving memory-augmented system that improves mathematical reasoning for a frozen LLM under continual learning with hard episodic resets. ISM maintains a compact, self-refined bank of strategy schemas learned from both successful and failed episode...

---

### 17. [Harnessing Textual Refusal Directions for Multimodal Safety](https://arxiv.org/abs/2606.31876)

**Authors**: Moreno D'Inc\`a, Massimiliano Mancini, Nicu Sebe  
**Category**: cs.AI  
**Published**: 2026-07-01  
**Score**: 35.5  
**Type**: new  
**ArXiv ID**: 2606.31876v1  

#### Abstract
To improve safety in Large Language Models (LLMs) we can either perform post-training alignment or exploit refusal directions in the activation space. Both strategies are less feasible in Multimodal LLMs (MLLMs) as they require unsafe multimodal data, harder to collect than their unimodal counterpar...

---

### 18. [Xiaomi-GUI-0 Technical Report](https://arxiv.org/abs/2606.31410)

**Authors**: Wanxia Cao, Chengzhen Duan, Pei Fu, Pengzhi Gao, Niu Lian, Fazhan Liu, Hui Liu, Heng Qu, Qinzhuo Wu, Zhehao Yu, Tongbo Chen, Shiqi Cui, Anan Du, Shukai Jia, Yuanfa Li, Yike Liu, Wenchao Lu, Haoyuan Sun, Jiatong Sun, Cheng Tan, Yajie Wang, Changqiao Wu, Tao Xiong, Jiahui Yang, Yuxuan Yuan, Ruoceng Zhang, Shaojie Zhang, Jian Zhu, Jian Luan, Cong Zou  
**Category**: cs.AI  
**Published**: 2026-07-01  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2606.31410v1  

#### Abstract
Graphical user interface (GUI) agents build on vision-language models to complete user tasks end-to-end in real applications through interface actions such as tapping, swiping, text entry, and navigation. However, existing GUI agents are trained and evaluated largely on offline trajectories, simulat...

---

### 19. [FedLAB: Traceable Semantic Codebooks for Federated Multimodal Graph Foundation Learning](https://arxiv.org/abs/2606.32016)

**Authors**: Zekai Chen, Kairui Yang, Xuaner Chen, Xunkai Li, Xun Wu, Rong-Hua Li, Guoren Wang  
**Category**: cs.LG  
**Published**: 2026-07-01  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2606.32016v1  

#### Abstract
Multimodal graph foundation models aim to learn reusable knowledge from graphs enriched with text, images, attributes, and relational topology, thereby supporting diverse graph-centric and modality-centric tasks. In practice, however, such multimodal graphs are often distributed across decentralized...

---

### 20. [Delta-JEPA: Learning Action-Sensitive World Models via Latent Difference Decoding](https://arxiv.org/abs/2606.31232)

**Authors**: Zhenghao Zhang, Yuanxiang Wang, Zhenyu Guan, Yujia Yang, Bingkang Shi, Tianyu Zong, Hongzhu Yi, Guoqing Chao, Xingchen Chen, Tiankun Yang, Chenxi Bao, Tao Yu, Jingjing Zhou, Jungang Xu  
**Category**: cs.AI  
**Published**: 2026-07-01  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2606.31232v1  

#### Abstract
Learning visual world models for planning requires compact latent dynamics that remain sensitive to actions, yet reconstruction-free joint-embedding objectives can collapse to action-insensitive representations. We propose Delta-JEPA, an end-to-end reconstruction-free world model that augments laten...

---

### 21. [Beyond Clean Text: Evaluating Encoder and Decoder Robustness for Bangla Event Detection in Noisy Text](https://arxiv.org/abs/2606.30914)

**Authors**: Tanvir Ahmed Sijan, S. M Golam Rifat, Nayeemul Islam, Md. Musfique Anwar  
**Category**: cs.CL  
**Published**: 2026-07-01  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2606.30914v1  

#### Abstract
Event detection (ED) systems are typically evaluated on clean, curated text, leaving their robustness to real-world noise largely unexplored, particularly for low-resource languages such as Bangla. We introduce a generalized Bangla news event ontology and a benchmark comprising 9,979 annotated sente...

---

### 22. [Relational and Sequential Conformal Inference for Energy Time Series over Graphs via Foundation Models](https://arxiv.org/abs/2606.31804)

**Authors**: Keivan Faghih Niresi, Alice Cicirello, Olga Fink  
**Category**: cs.LG  
**Published**: 2026-07-01  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2606.31804v1  

#### Abstract
Accurate energy demand forecasting is essential for the reliable operation and planning of modern sustainable energy systems. Spatial-temporal graph neural networks (STGNNs) have recently achieved strong performance in point forecasting by jointly modeling temporal dynamics and relational dependenci...

---

### 23. [CoMet: Context and Multiplicity Decomposition for Multimodal Uncertainty Estimation](https://arxiv.org/abs/2606.32012)

**Authors**: Sanghyuk Chun, William Yang, Amaya Dharmasiri, Olga Russakovsky  
**Category**: cs.LG  
**Published**: 2026-07-01  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2606.32012v1  

#### Abstract
Uncertainty estimation has been a long-standing challenge in AI models; it amounts to "knowing what you don't know," and metacognition is notoriously difficult even for humans (cf. the Dunning-Kruger effect). Although it is still far from solved even in simpler classification systems, tackling it in...

---

### 24. [CryoACE: An Atom-centric Framework for Accurate and Automated Model Building in Cryo-EM](https://arxiv.org/abs/2606.31332)

**Authors**: Minzhang Li, Mingrui Li, Weichen Qin, Qihe Chen, Sixian Shen, Yuan Pei, Jiakai Zhang, Jingyi Yu  
**Category**: cs.AI  
**Published**: 2026-07-01  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2606.31332v1  

#### Abstract
Protein automodeling from cryo-EM density maps faces unique challenges in enforcing physicochemical validity and managing conformational heterogeneity. Current solvers are often limited to static predictions or require computationally intensive heuristic searches. We present CryoACE, an end-to-end f...

---

### 25. [Patch-PODiff-ViT: Structured Latent Diffusion with Patchwise POD for Super-Resolution and Uncertainty Quantification](https://arxiv.org/abs/2606.31290)

**Authors**: Onkar Jadhav, Tim French, Matthew Rayson, Nicole L. Jones  
**Category**: cs.LG  
**Published**: 2026-07-01  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2606.31290v1  

#### Abstract
Diffusion models enable probabilistic super-resolution and conditional generation, but pixel-space methods are computationally expensive and learned latent spaces often lack interpretable uncertainty quantification. We introduce Patch-PODiff-ViT, a structured latent diffusion framework in which the ...

---

### 26. [Building a Multimodal Dataset of Academic Paper for Keyword Extraction](https://arxiv.org/abs/2606.31069)

**Authors**: Jingyu Zhang, Xinyi Yan, Yi Xiang, Yingyi Zhang, Chengzhi Zhang  
**Category**: cs.CL  
**Published**: 2026-07-01  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2606.31069v1  

#### Abstract
Up to this point, keyword extraction task typically relies solely on textual data. Neglecting visual details and audio features from image and audio modalities leads to deficiencies in information richness and overlooks potential correlations, thereby constraining the model's ability to learn repres...

---

### 27. [Smart charging of large fleets of Electric Vehicles: Independent Multi-Agent Reinforcement Learning approaches](https://arxiv.org/abs/2606.31347)

**Authors**: Xavier Rate, Eloann Le Guern, Rapha\"el F\'eraud, Fatma Salem, Melissa Chiknoun, Eymeric Giabicani, Mehdi Feki, Patrick Maill\'e, Guy Camilleri, Anne Blavette, Hamid Benhamed  
**Category**: cs.AI  
**Published**: 2026-07-01  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2606.31347v1  

#### Abstract
The electrification of transportation through electric vehicles introduces new challenges for power grid management, such as increased peak demand, voltage fluctuations, line overloads, and the integration of variable renewable energy sources. To enable efficient integration of EVs while minimizing ...

---

### 28. [Offline Reinforcement Learning for Fluid Controls: Data-based Multi-observational Policy Extraction](https://arxiv.org/abs/2606.31025)

**Authors**: Deepak Akhare, Luning Sun, Xin-Yang Liu, Xiantao Fan, Timo Bremer, Ben Zhu, Jian-Xun Wang  
**Category**: cs.LG  
**Published**: 2026-07-01  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2606.31025v1  

#### Abstract
Active flow control is a fundamental application in engineering. Recent advances in deep reinforcement learning have made progress in this field. However, the classical online RL approaches require extensive real-time interactions with the high fidelity environment, while each sensor configuration c...

---

### 29. [CLExEval: A Human-in-the-Loop Framework for Qualitative Evaluation of LLM Clinical Reasoning](https://arxiv.org/abs/2606.31608)

**Authors**: Ajmal M., Abin Roy, Afthab Salam Kanniyan, Jawadh Abdul Kabeer, Jerin James, Preslav Nakov, Zhuohan Xie  
**Category**: cs.CL  
**Published**: 2026-07-01  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2606.31608v1  

#### Abstract
Large Language Models (LLMs) achieve strong results on many medical benchmarks, but their clinical reasoning remains difficult to evaluate reliably. A central risk is an evaluation illusion: fluent and well-structured explanations can appear clinically convincing even when the final diagnosis is inc...

---

### 30. [HyPOLE: Hyperproperty-Guided Multi-Agent Reinforcement Learning under Partial Observation](https://arxiv.org/abs/2606.30966)

**Authors**: Arshia Rafieioskouei, Tzu-Han Hsu, Matthew Lucas, Borzoo Bonakdarpour  
**Category**: cs.AI  
**Published**: 2026-07-01  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2606.30966v1  

#### Abstract
Formal specification is a powerful tool to guide the learning process and provides significant advantages over reward shaping: (1) mathematical rigor; (2) expressiveness to specify objectives and constraints, and (3) the ability to define tactics to achieve objectives. However, these benefits remain...

---

## 🔧 Configuration

This bot is configured to look for papers containing the following keywords:
- LLM, Inference, Training, kv cache, Speculative decoding, Prefill, Decode, FlashAttention, PagedAttention, continuous batching, MOE, mixture of experts, Quantization, FP8, FP4, Parallel, Distributed, Pipeline, Sparse, Sparse Attention, State Space, SSM, Throughput, Scalable, Efficient, vLLM, SGLang, DeepSpeed, FSDP, AI compiler, TVM, Triton, MLIR, torch.compile, kernel fusion, polyhedral, RISC-V, RVV, XiangShan, custom instruction, eBPF, RDMA, disaggregated, chiplet, NoC, CXL, HBM, systolic array, Kernel, Cluster, Communication, Offload, Hardware, Accelerator, Compiler, Optimization, Embodied, Embodied AI, Embodied Intelligence, Robotics, Robot, Manipulation, Navigation, Sim-to-real, Simulation, World Model, World Models, Video Generation, Video Prediction, Multimodal, Multi-modal, Vision-Language, Vision Language, VLM, Image-Text, Cross-modal, Cross modal, Text-to-Image, Text-to-Video, Vision Transformer, Visual Understanding

## 📅 Schedule

The bot runs daily at 12:00 UTC via GitHub Actions to fetch the latest papers.

## 🚀 How to Use

1. **Fork this repository** to your GitHub account
2. **Customize the configuration** by editing `config.json`:
   - Add/remove arXiv categories (e.g., `cs.AI`, `cs.LG`, `cs.CL`)
   - Modify keywords to match your research interests
   - Adjust `max_papers` and `days_back` settings
3. **Enable GitHub Actions** in your repository settings
4. **The bot will automatically run daily** and update the README.md

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
