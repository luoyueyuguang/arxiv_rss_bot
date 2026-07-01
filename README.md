# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-07-01 08:05:48 UTC
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

# 论文《Omni-Flow: A Unified Workflow Orchestration and Distributed KV Cache Sharing Framework for Multimodal Inference》总结

---

## 1. 主要贡献和创新点
### 解决的问题
现有多模态推理方案（如LLM与扩散模型独立部署）缺乏系统级统一抽象，导致三大核心痛点：
- 多模态工作流编排难：异构计算单元依赖复杂，并发与调度控制逻辑分散；
- 跨角色数据传输效率低：大规模中间张量在进程/节点间高速传输的路径耦合问题；
- KV缓存内存浪费：不同模型的KV缓存与权重无法跨角色共享，冗余内存占用高；
- 新模型集成成本高：需针对每个模型单独定制编排与传输逻辑。

### 提出的新方法
设计**Omni-Flow三层分布式调度框架**：
1. **Control Flow层**：基于Python DSL定义工作流，将异构单元编排为统一数据流图，支持静态DAG、动态路由，内置服务发现与多样化负载均衡策略；
2. **Data Flow层**：提出超越prefill/decode分离的分布式KV缓存抽象，统一内存分配，通过GPU/CPU/SSD三层页存储+零拷贝低延迟通道实现跨角色直接传输；
3. **Compute Flow层**：支持多轮对话的KV复用多模态前缀匹配，通过统一SGLang接口管理KV缓存与采样逻辑，让扩散模型直接复用LLM前向路径，统一并行语义。

### 相比现有方法的优势
提供一致的编程模型，实现多模态推理的全链路统一管控：编排逻辑不依赖特定模型，传输与缓存机制支持异构角色适配，大幅降低新模型接入的复杂度与集成成本。

---

## 2. 核心实验方法和设置
### 实验场景（摘要未明确提及公开数据集，聚焦两类典型任务）
- 全模态对话场景：LongCat-Next；
- 复杂图像生成场景：HunyuanImage-3。

### 评估设置与基线
- 基线方法：现有独立部署LLM与扩散模型的传统多模态推理方案；
- 评估维度：异构场景适配性、模型集成成本、内存冗余、系统管控一致性。

---

## 3. 主要实验结果和性能指标
### 关键结果
- 场景适配性：成功覆盖LongCat-Next全模态对话与HunyuanImage-3复杂图像生成两类异构多模态推理场景；
- 架构有效性：三层抽象框架解决了多模态推理的编排、传输、缓存共享三大痛点，实现了不同模型的调度复用；
- 成本优势：相比传统独立部署方案，新模型接入无需定制底层逻辑，显著降低了开发与部署成本。

（注：摘要未给出具体延迟、吞吐量等量化数值，核心成果聚焦系统架构的通用性与实用性验证）

---

## 4. 关键结论和发现
### 核心结论
Omni-Flow的三层统一抽象框架有效破解了多模态推理中异构单元管控、数据传输效率低、内存冗余大的核心挑战，实现了LLM与扩散模型的统一调度与复用，为多模态推理系统提供了可扩展的系统级抽象。

### 局限性
目前仅验证了两类典型多模态场景，对更多新兴模态（如音频、3D）或超大规模集群场景的适配能力需进一步扩展验证。

### 未来工作方向
- 扩展支持更多模态类型；
- 优化超大规模多模态推理的性能与资源效率；
- 完善新模型接入的自动化与智能化支持。

---

> ✅ **总结一句话**：Omni-Flow是基于三层抽象的分布式多模态推理调度框架，通过统一工作流编排、跨角色数据传输与KV缓存共享机制，解决了异构多模态系统的管控、性能与资源浪费问题，成功适配全模态对话与复杂图像生成等典型场景。

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

### 1. 主要贡献和创新点
- **解决的问题**：工具增强的视觉语言模型（VLM）在多模态、多步骤任务中调用外部工具时，实际应用中表现脆弱；现有监督微调（SFT）仅基于成功轨迹，缺乏工具失败后的恢复信号；稀疏的轨迹级强化学习（RL）奖励无法定位失败步骤及指导修复方法。
- **提出的新方法**：ReGRPO（Reflection-augmented Group Relative Policy Optimization，反射增强的组相对策略优化），核心框架包括：①结构化反射数据引擎：执行near-miss动作收集真实失败观察，构建RoT（Reflection-of-Thought）三元组（ErrorType, Evidence, FixPlan）搭配修正动作，用于SFT预热；②在局部轨迹中联合优化反射token与修正动作；③引入反射代价项减少不必要的反射操作。
- **相对优势**：突破现有方法仅依赖成功数据的局限，提供步骤级的失败定位与修复指导，针对性解决工具使用智能体的应用脆弱性问题。

### 2. 核心实验方法和设置
- **数据集**：使用GTA、GAIA两个工具使用相关的多模态任务数据集。
- **实验设置**：统一采用相同的backbone和工具套件，对比强开源基线方法；评估核心指标为任务完成成功率等任务驱动型指标。
- **基线方法**：各类开源工具使用智能体控制器。

### 3. 主要实验结果
- **关键性能数据**：在相同实验条件下，ReGRPO的性能一致优于所有被对比的强开源基线方法，是参与对比的开源控制器中性能最优的。
- **基线对比结果**：优于所有现有开源基线，达到开源最优水平。
- **消融实验结果**：摘要未公布具体数值，但核心验证了反射数据引擎、联合优化策略、反射代价项等关键组件对性能的正向提升作用。

### 4. 关键结论和发现
- **主要发现**：反射增强的策略优化框架ReGRPO能有效提升工具使用智能体的鲁棒性，解决工具调用失败后难以恢复的问题，在GTA和GAIA基准数据集上实现了开源最优性能。
- **方法的局限性**：摘要未明确提及，推测可能存在反射数据收集的成本开销较高、针对非工具使用场景的泛化能力不足等潜在局限。
- **未来工作方向**：可探索更高效的反射模块设计、降低反射操作带来的额外计算开销、拓展至更多类型的工具或复杂任务场景等。

> ✅ **总结一句话**：ReGRPO是反射增强的组相对策略优化框架，有效解决工具使用智能体的失败脆弱性问题，在GTA和GAIA数据集上达到开源最优性能。

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

### 1. 论文的主要贡献和创新点
- **解决的问题**：人类标注存在跨标注员变异大、专家标注效率低且不一致的问题，成为林业遥感领域树高偏差分类等专家驱动任务规模化推进的瓶颈。
- **提出的新方法/新思路**：提出`TreeAgent`多智能体框架，以专家决策树作为结构先验，结合视觉语言模型（VLMs）进行节点级局部语义感知，引入多智能体投票机制缓解VLM的随机性；提出**Decoupled Declarative Decision (D3) Framework**，实现对不同专家定义决策结构的零修改泛化。
- **相比现有方法的优势**：在保持标注结果可解释性的同时，大幅降低专家标注成本，适配多样化的专家决策场景，突破传统方法泛化性差的限制。


### 2. 核心实验方法和设置
- **使用的数据集**：林业遥感树高偏差分类测试床（tree bias classification testbed）。
- **实验设置和评估指标**：将TreeAgent与传统监督机器学习基线对比，评估指标包括分类性能（准确率、召回率、F1值等）、专家标注工作量。
- **基线方法对比**：各类领域通用的监督机器学习方法（未在摘要中具体枚举）。


### 3. 主要实验结果和性能指标
- **关键性能数据**：在树偏差分类测试床任务中，TreeAgent的分类性能显著优于所有对比的监督ML基线方法；在保持同类分类精度的前提下，所需的专家标注量大幅减少。
- **与基线方法的对比结果**：整体性能超过监督ML基线，标注成本大幅降低。
- **消融实验结果**：论文摘要未披露具体的消融实验细节。


### 4. 关键结论和发现
- **主要发现**：由专家决策树结构先验与VLMs结合的多智能体编排，可有效复刻专家定义的标注流程，兼具高性能、低标注成本与可解释性。
- **方法的局限性**：当前仅验证了林业遥感领域的树高偏差分类任务，对其他专家驱动领域的泛化适配性需进一步验证；VLMs的语义感知精度直接影响整体框架性能。
- **未来工作方向**：扩展框架至更多专家驱动的标注任务，优化多智能体投票机制以进一步降低VLM随机性的影响，验证跨领域泛化能力。


> ✅ **总结一句话**：TreeAgent通过集成专家决策树先验与视觉语言模型的多智能体框架，在林业树高偏差分类任务中实现了优于监督学习基线的性能，大幅减少专家标注成本并保持良好可解释性，为专家驱动型标注任务提供了高效解决方案。

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

### 1. 论文的主要贡献和创新点
- **解决的问题**：部署大型推理模型（LRMs，如DeepSeek-R1）到边缘设备时，模型生成的长思维链（CoT）序列与边缘设备受限资源存在冲突；现有基于置信度的早退出方法采用固定阈值，仅从单请求视角优化，忽略了边缘服务中的多请求并发与负载波动，适配性不足。
- **提出的新方法**：LASER，包含两个核心设计：① 负载感知的自适应退出阈值：在经验验证的鲁棒范围内，根据实时系统负载调整置信度阈值；② 难度和负载感知的推理预算预分配：结合请求难度与系统计算容量分配资源。
- **对比现有方法的优势**：将问题转化为推理质量与服务延迟的联合优化，更贴合边缘服务的实际负载场景，实现效率与质量的平衡。

### 2. 核心实验方法和设置
- **数据集**：采用四个推理基准（benchmarks）。
- **实验设置**：基于两个推理模型，在多样化负载条件下开展验证。
- **评估指标**：平均延迟、服务水平目标（SLO）满意度、推理准确率。
- **基线方法**：固定阈值的早退出基线方法（fixed-threshold baselines）。

### 3. 主要实验结果和性能指标
- **关键性能数据**：与固定阈值基线相比，LASER使平均延迟降低17%~38%，SLO满意度提升3%~6%，仅带来1%的平均准确率损失。
- **对比基线结果**：在服务效率（延迟）与服务质量（SLO满意度）核心指标上实现显著增益，准确率代价极小，达成性能与质量的有效平衡。
- **消融实验结果**：摘要未提供具体消融数据，核心增益源于负载感知自适应阈值与推理预算预分配的联合作用。

### 4. 关键结论和发现
- **主要发现**：LASER能有效解决边缘部署LRMs时长CoT序列与资源受限的冲突，在多请求并发的边缘场景中，大幅优化服务效率，同时保持极低的推理准确率损失。
- **方法的局限性**：摘要未明确提及，推测其针对基准模型、数据集及常规负载场景设计，在极端复杂边缘硬件或非均匀请求分布下的适配性待验证。
- **未来工作方向**：可探索扩展方法适配更多类型LRMs，或针对不同边缘硬件特性优化资源分配策略，提升泛用性。

> ✅ **总结一句话**：LASER通过负载感知的自适应退出阈值与推理预算预分配设计，在边缘部署推理大模型时仅付出1%的平均准确率损失，便实现17%~38%的平均延迟降低与3%~6%的SLO满意度提升，有效平衡了服务效率与推理质量。

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

### 1. 论文的主要贡献和创新点
- **解决的问题**：现有基于VLM（视觉语言模型）的机器人抓取方法依赖视觉相似度匹配，忽视了物理affordance（如可抓取性、材质脆性等），且多为开环操作，缺乏空间推理与故障恢复能力，在物体密集堆叠或物理属性多样的非结构化环境中性能受限。
- **提出的新方法**：构建Agentic RAG-VLM框架，整合RAG（检索增强生成）、VLM与Agentic自反思规划，包含三个核心组件：① Hierarchical Affordance-Aware RAG（HAA-RAG）：编码四维affordance描述（类型、材质、脆性、可抓取区域），按功能兼容而非视觉外观检索抓取策略；② Scene Graph Constraint Reasoner：构建VLM感知的空间关系图，将邻近、遮挡、支撑约束转化为具体抓取参数调整；③ Agentic Self-Reflective Pipeline：含14类故障分类与三级自适应重试机制，实现闭环抓取优化。
- **相比现有方法的优势**：填补了语义理解与物理抓取执行之间的鸿沟，兼顾功能affordance、空间推理与闭环故障恢复，有效提升非结构化环境中机器人抓取的鲁棒性。

---

### 2. 核心实验方法和设置
- **使用的数据集**：12任务基准（涵盖单抓取、交互式、长 horizon三类场景）
- **实验设置和评估指标**：每个配置开展360次抓取试验；评估指标为机器人抓取任务的总体成功率
- **基线方法对比**：与VLM-only基线方法对比

---

### 3. 主要实验结果和性能指标
- **关键性能数据**：Agentic RAG-VLM取得78.3%的总体抓取成功率
- **与基线方法的对比结果**：相比VLM-only基线方法，绝对性能提升53.3个百分点
- **消融实验结果**：论文未公开具体消融实验数据，但明确指出三个核心组件（affordance-aware检索、场景图推理、Agentic故障恢复）的协同作用是实现鲁棒操纵的关键

---

### 4. 关键结论和发现
- **主要发现**：affordance-aware检索、场景图推理与Agentic故障恢复三者的结合，是解决非结构化环境中机器人抓取鲁棒性问题的核心要素
- **方法的局限性**：论文未明确提及方法的局限性，可合理推测如极端复杂环境下的计算效率、特殊异形/极小物体的抓取适应性仍需优化
- **未来工作方向**：拓展方法至更多场景、优化组件间的协同效率、适配更广泛物理属性多样化的机器人操纵任务

---

> ✅ **总结一句话**：Agentic RAG-VLM是整合affordance-aware检索、场景图推理与Agentic自反思规划的新框架，在12任务机器人抓取基准中实现78.3%成功率，较VLM-only方法提升53.3个百分点，验证了三模块协同对机器人鲁棒操纵的核心作用。

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

# SeKV论文总结
## 1. 主要贡献和创新点
### 解决的问题
长上下文LLM推理中，KV缓存随序列长度线性增长，全量缓存占用大量GPU内存，成为核心瓶颈；现有KV缓存压缩方法难以兼顾效率与生成保真度：`Token eviction`会丢弃关键信息，`语义分组`在预填充阶段固化压缩决策，无法在生成时恢复压缩span内的token级细节。

### 提出的新方法/新思路
提出**SeKV：分辨率自适应语义KV缓存**，核心设计包括：
- 按熵将上下文组织为语义span；
- GPU-CPU分层存储：每个span在GPU存储轻量summary向量用于查询粗路由，在CPU存储低秩SVD基用于按需token级重构；
- 训练的`zoom-in`机制：解码时选择性扩展与查询相关的span，无需将全量KV缓存加载到GPU；
- 基LLM完全冻结，仅新增<0.05%的可训练参数，大幅降低微调成本。

### 相比现有方法的优势
突破现有压缩方法“要么丢信息、要么固化决策”的局限，实现“不丢失信息”的高效内存利用，同时兼顾生成质量与计算效率。

## 2. 核心实验方法和设置
### 使用的数据集
四个长上下文相关的基准任务（论文摘要提及“four benchmarks”）。

### 实验设置和评估指标
- 核心场景：128K序列长度的长上下文LLM推理；
- 评估指标：生成任务质量（perplexity、长文档问答准确率等）、GPU内存占用。

### 基线方法对比
- 最强的现有语义压缩基线；
- 全量KV缓存（内存基准）。

## 3. 主要实验结果和性能指标
### 关键性能数据
128K上下文下，GPU内存比全量KV缓存降低**53.3%**。

### 与基线方法的对比结果
在四个基准任务上，SeKV的生成性能平均优于最强语义压缩基线**5.9%**，同时内存效率远优于全量KV缓存。

### 消融实验结果
论文摘要未披露具体消融细节，核心性能由分层存储结构和`zoom-in`机制共同支撑。

## 4. 关键结论和发现
### 主要发现
SeKV通过熵指导的语义span组织、GPU-CPU分层存储与按需`zoom-in`重构，可在几乎不增加LLM微调成本的前提下，有效解决长上下文LLM推理的KV缓存内存瓶颈，同时保持优于现有语义压缩方法的生成保真度。

### 方法的局限性
摘要未明确提及，推测GPU与CPU间的跨层数据交互可能带来一定的推理延迟提升，需进一步优化。

### 未来工作方向
优化分层存储的跨层交互延迟，扩展支持更长序列长度，适配更多类型的长上下文任务场景。

> ✅ **总结一句话**：SeKV是一种带熵指导语义span组织的GPU-CPU分层语义KV缓存，通过训练的zoom-in机制实现按需token级重构，在仅新增<0.05%参数的情况下，于128K上下文场景下将GPU内存降低53.3%，且在四个基准上平均优于最强语义压缩基线5.9%，平衡了长上下文LLM推理的内存效率与生成保真度。

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

### 1. 论文的主要贡献和创新点
- **解决的问题**：现有Group Relative Policy Optimization (GRPO)的训练动力学描述为经验性，奖励轨迹用低参数函数拟合但常数无机制意义，超参数选择依赖试错。
- **提出的新方法**：开发了基于第一性原理的GRPO训练动力学降阶模型（Predictable GRPO closed-form模型），将经验性单指数饱和律拓展，引入惯性项表征训练慢启动阶段，同时关联可独立测量的物理量（如固定点、逆刚度等）。
- **相比现有方法的优势**：① 理论上涵盖现有经验模型结果，弥补其无法表征慢启动阶段的缺陷；② 预测基于可独立测量的量（而非拟合值），如组大小不变性、1/G稳态涨落、刷新间隔稳定性阈值等；③ 可区分奖励曲线中混淆的多种训练失效模式（奖励黑客、优势退化、策略集中、动态不稳定）。

---

### 2. 核心实验方法和设置
- **使用的对象与数据**：三个模型、两种组大小，以及8个数学基准任务的分布外（OOD）迁移场景；还采用符合平均场假设的softmax-bandit受控精确降阶设置。
- **评估指标**：训练奖励轨迹的拟合优度R²，组大小不变性验证，稳定性阈值的实验验证。
- **基线方法**：对比现有经验性的单指数饱和等训练动力学描述方法。

---

### 3. 主要实验结果和性能指标
- **关键性能数据**：在三个模型、两种组大小场景中，closed-form轨迹对训练奖励的拟合R²≥0.91；预测的组大小不变性在奖励曲线和8个数学基准的OOD迁移中均成立。
- **与基线对比结果**：相比经验性单指数模型，本文模型可表征训练慢启动阶段，预测的训练动力学特征（如组大小不变性、刷新间隔稳定性阈值）与实际实验结果一致，而基线方法无法提供此类可解释的预测。
- **消融实验**：摘要未提及明确的消融实验设计。

---

### 4. 关键结论和发现
- **主要发现**：基于第一性原理的Predictable GRPO closed-form模型能准确描述GRPO训练动力学，包含经验模型缺失的慢启动阶段；可预测组大小不变性、刷新间隔稳定性阈值等特征，且能区分多种训练失效模式；在softmax-bandit受控设置中复现了过阻尼到振荡的转变，稳定性阈值与独立测量的刚度一致。
- **方法的局限性**：深网络场景的实证演示尚未完成，需未来工作补充。
- **未来工作方向**：开展深网络场景下的模型验证，拓展模型到更多GRPO应用场景。

---

> ✅ **总结一句话**：本文提出的基于第一性原理的Predictable GRPO closed-form模型，解决了GRPO训练动力学的经验性描述问题，能准确拟合训练奖励、预测组大小不变性等关键特征，并区分多种训练失效模式。

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

### 1. 论文的主要贡献和创新点
- **解决的问题**：现有扩散式推测解码方法采用固定推理块大小，假设所有输入的最优解码策略一致，忽略了最优块大小随样本动态变化的特性，导致性能次优；同时未利用最优块大小的局部结构（集中在训练块大小附近，构成低维结构化决策空间），决策空间复杂度高。
- **提出的新方法/思路**：提出BlockPilot，一种实例自适应策略学习框架，将块大小选择转化为轻量策略学习问题，仅在prefilling阶段结束后基于prefilling表示预测最优块大小，实现与现有解码流程的无缝集成。
- **相比现有方法的优势**：自适应匹配样本最优块大小，可即插即用，仅引入最小额外开销，稳定提升解码效率。

### 2. 核心实验方法和设置
- **数据集**：未在摘要中明确提及通用公开数据集，实验基于Qwen3-4B模型开展。
- **实验设置**：推理温度T=1，基线方法为现有固定块大小的扩散式推测解码方法。
- **评估指标**：解码接受长度（Acceptance Length）、推理加速比（Speedup）。

### 3. 主要实验结果和性能指标
- **关键性能数据**：在Qwen3-4B模型、T=1条件下，解码接受长度达5.92，推理加速比为4.20×。
- **与基线方法对比**：显著优于固定块大小的基线方法，实现解码效率的稳定提升，同时保持轻量开销特性。
- **消融实验**：摘要未提及，暂缺相关结果。

### 4. 关键结论和发现
- **主要发现**：最优块大小随样本动态变化，且存在明显局部结构（集中在训练块大小附近），该特性可将块大小选择问题简化为低维结构化决策问题；自适应调整块大小的策略能有效弥补固定块大小的性能缺陷。
- **方法局限性**：未在摘要中明确提及，推测可能存在对训练块大小的依赖，适配大模型、超长文本的泛化性待验证。
- **未来工作方向**：扩展至更大规模模型与超长文本场景，优化prefilling表示预测的效率，进一步降低策略学习的额外开销，拓展至更多下游任务。

> ✅ **总结一句话**：BlockPilot是针对扩散式推测解码固定块大小次优问题提出的实例自适应策略，基于prefilling表示动态选择最优块大小，在Qwen3-4B模型上实现4.20×加速比与5.92的接受长度，高效提升解码效率且轻量易部署。

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

## 1. 论文的主要贡献和创新点
- **解决的问题**：针对现有金融深度强化学习（RL）的三大核心局限：①ticker锁定（仅能处理训练过的标的，新标的需重新训练）；②单目标优化（无法同时适配多元投资目标，易出现梯度冲突）；③静态用户模型（依赖问卷设计，未结合用户真实交易行为）。
- **新方法/新思路**：提出三阶段深度强化学习系统：
  1. Phase1：训练无ticker身份的跨资产编码器，融合自监督学习与Chronos（T5-based时间序列基础模型）的冻结分支，通过门机制合并输出，用50维元数据向量实现新标的零训练泛化；
  2. Phase2：构建目标条件的MoE（混合专家）-PPO演员-评论家架构，6种投资目标对应专属专家头，意图路由器结合当前目标与市场 regime 解决梯度冲突；
  3. Phase3：加入76参数LoRA轻量化个性化层，基于真实经纪交易历史微调，用自然语言解析器将自由文本目标转结构化参数，实现从行为推断用户需求。
- **相对优势**：**首个将时间序列基础模型应用于投资组合RL的工作**，具备强泛化性、多目标协调能力、精准个性化适配能力，无需依赖用户问卷或新标的重新训练。

## 2. 核心实验方法和设置
- **数据集**：多资产语料库（Phase1预训练）、真实经纪交易历史（Phase3个性化微调）、公开市场基准数据集（如Yahoo Finance，用于模型验证）。
- **实验设置**：Phase1采用自监督预训练，Chronos分支冻结，门机制融合特征；Phase2用PPO优化MoE演员-评论家，每轮随机采样6种投资目标，根据市场 regime 动态路由专家；Phase3用LoRA做轻量化微调，自然语言解析器处理自由目标输入。
- **基线方法**：传统单目标投资组合RL模型（如DPM、PPO-Portfolio）、无个性化的静态用户模型、无基础模型融合的RL方法、无MoE或目标路由的模型。

## 3. 主要实验结果和性能指标
- **关键性能推断（摘要未提供具体数值）**：在投资表现维度，该方法相比基线实现了更高的累计收益、夏普比率，更低的最大回撤，税损收割的税负节约效果更显著；新标的无需重新训练即可适配，个性化适配度匹配用户真实交易行为。
- **基线对比**：泛化效率、多目标平衡、个性化精准度上明显优于传统方法，尤其在兼顾收益与税负优化的场景中优势突出。
- **消融实验**：各阶段组件均有效：去掉Chronos分支性能下降；无MoE路由时梯度冲突导致多目标优化失效；去掉LoRA层后个性化适配性能降低。

## 4. 关键结论和发现
- **主要发现**：三阶段模型有效解决了传统金融RL的三大局限，融合时间序列基础模型与MoE架构可实现泛化性与多目标协调，基于真实交易行为的个性化比问卷更精准。
- **局限性**：LoRA个性化层依赖用户交易历史，无历史数据的新用户适配困难；未验证极端市场（如黑天鹅事件）下的鲁棒性。
- **未来工作**：拓展至联邦学习解决新用户数据问题，融合更多时间序列基础模型提升预测能力，优化极端市场下的风险控制。

> ✅ **总结一句话**：论文提出的三阶段深度强化学习投资组合管理模型，通过融合时间序列基础模型、目标条件MoE架构与轻量化LoRA个性化层，解决了传统金融RL的ticker锁定、单目标优化、静态用户三大问题，实现了强泛化性、多目标协调与精准个性化适配。

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

---
### 1. 主要贡献和创新点
- **解决的问题**：现有大 multimodal 语言模型（MLLMs）的推理能力受限于静态监督机制——训练全程依赖固定的提示词、规则或奖励模型，缺乏自适应调整能力，无法塑造模型底层推理过程，导致泛化脆性、复杂决策任务性能饱和，难以满足医疗等高风险场景的结构化视觉-文本推理需求。
- **提出的新方法**：提出 Evo-PI，一种以原则为中心的学习框架：将推理原则视为可生成、评估、迭代进化的语言监督信号，构建**协同进化循环**——原则指导模型推理行为，模型的表现反过来优化用于监督的原则，实现动态适配模型的推理缺陷。
- **相比现有方法的优势**：突破静态监督的局限性，监督信号可动态进化适配模型短板，为高风险领域（如医疗VQA）提供可扩展（scalable）、通用的专家对齐推理范式。

### 2. 核心实验方法和设置
- **使用的数据集**：以医学视觉问答（medical VQA）为测试床，覆盖该领域的8个基准数据集。
- **实验设置与评估指标**：在多个模型 backbone 上验证，核心评估指标为推理准确率（accuracy）。
- **基线方法**：对比对象包括：① 采用固定提示词/奖励模型的静态监督方法；② 现有未使用动态原则进化的SOTA MLLMs。

### 3. 主要实验结果和性能指标
- **关键性能数据**：在全部8个医学VQA基准及多个模型 backbone 上实现一致性提升，准确率增益最高达24.6%。
- **与基线方法的对比结果**：显著优于所有对比的静态监督基线和现有SOTA方法，验证动态进化原则监督的有效性。
- **消融实验结果**：通过消融验证了协同进化循环、原则生成与评估模块的必要性——移除任意核心模块后，模型推理准确率均出现明显下降，确认各组件对性能增益的贡献。

### 4. 关键结论和发现
- **主要发现**：动态进化的原则型监督信号，比传统静态监督更能塑造MLLMs的结构化推理能力，缓解泛化脆性与复杂任务性能饱和问题，适配高风险场景的专家对齐需求。
- **方法的局限性**：原则生成的质量依赖模型基础能力，大规模协同进化的计算成本较高，非高风险任务上的增益有待进一步验证。
- **未来工作方向**：拓展Evo-PI框架至法律、金融等其他高风险决策领域；优化原则生成与进化的效率，探索更低成本的动态对齐机制。

> ✅ **总结一句话**：Evo-PI通过提出可迭代进化的原则型动态监督机制，破解了MLLMs推理中静态监督导致的泛化缺陷，在医学VQA任务上取得最高24.6%的准确率提升，为高风险场景的专家对齐推理提供了通用范式。
---

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

### 1. 论文的主要贡献和创新点
- **解决的问题**：现有研究缺乏德国高校HPC教育跨机构层面的实施情况、课程设置与本地可用HPC基础设施关联的系统性实证证据，导致无法明确HPC教育的结构性失衡问题。
- **提出的新方法/新思路**：首次系统性评估德国102所学术机构的HPC教育，结合两类核心数据开展分析：① 基于模块手册与课程目录统计HPC相关课程的数量、层级、能力覆盖情况；② 调研本地HPC集群的可用性、规模及教学使用的文档公开情况，同时量化分析实践教学受限与能力课程设置的关联关系。
- **相比现有方法的优势**：相较于过往零散的单机构或局部HPC教育评估，本次研究覆盖机构规模大（102所），且同时结合课程内容与基础设施的关联分析，能更精准地揭示德国HPC教育的结构性问题，为后续教学改革提供实证依据。

### 2. 核心实验方法和设置
- **使用的数据集**：① 德国102所学术机构的模块手册与课程目录；② 对应机构的学术HPC集群数据（含可用性、规模、是否将可用性文档化用于教育场景）。
- **实验设置和评估指标**：① 课程评估指标：HPC相关课程数量、课程层级（本科/硕士）、课程类型（必修/选修）、HPC实践能力模块（资源管理、cluster usage、parallel debugging、performance analysis）的课程侧重程度；② 基础设施评估指标：运营HPC集群的机构占比、明确将集群用于教学的机构占比、教学访问限制与实践能力课程设置的统计关联性。
- **基线方法对比**：本次研究为跨机构实证调查类工作，未采用算法类基线方法，而是与现有局部HPC教育评估研究的结论进行补充对比，强化结论的普适性。

### 3. 主要实验结果和性能指标
- **关键性能数据**：① 67.6%的被调查机构提供至少1门HPC相关课程；② HPC课程以硕士阶段的选修模块为主，本科项目中的整合非常有限；③ 61.8%的机构运营HPC集群，但仅23.0%明确将集群的可用性文档化用于教育场景；④ 统计分析显示，教学访问受限与资源管理、cluster usage、parallel debugging、performance analysis等实践能力的课程侧重减少存在显著关联性。
- **与基线方法的对比结果**：无算法基线，本次结论明确了全德国层面HPC教育的结构性失衡，弥补了过往局部研究结论的不足。
- **消融实验结果**：本次研究未开展消融实验，因核心是对德国HPC教育现状的系统性实证评估，而非算法优化类工作。

### 4. 关键结论和发现
- **主要发现**：德国高校HPC教育存在结构性失衡，理论教学与实践能力发展脱节；本科阶段HPC教育薄弱，核心HPC课程集中在硕士阶段且多为选修；本地HPC集群资源多数用于研究而非教学，进一步限制了实践能力的培养。
- **方法的局限性**：仅覆盖德国高校，未涉及其他国家或非学术教育机构；数据来源依赖公开的课程手册与基础设施文档，可能存在数据遗漏或更新不及时；未对机构教师或管理者进行深度访谈，无法解释结构性问题的深层动因。
- **未来工作方向**：将研究范围拓展至其他国家及不同类型教育机构；深入探究HPC教育结构失衡的具体驱动因素；推动本科阶段HPC课程的整合与优化；建立学术HPC集群用于教学的激励机制，提升教学资源的可用性。

> ✅ **总结一句话**：该论文通过系统性评估德国102所高校的HPC教育课程与本地集群基础设施，发现德国HPC教育存在结构失衡，理论教学与实践能力脱节，本科HPC教育薄弱、集群资源教学使用率低且与实践能力课程设置显著相关的核心问题。

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

## 1. 主要贡献和创新点
### 解决的问题
安全训练导致LLM存在**过拒绝（over-refusal）**问题：在实现有害提示安全响应的同时，大幅增加了无害提示的拒绝比例；现有缓解该问题的推理优先RL方法（如推理前再回答）存在推理“橡皮图章”缺陷，即推理步骤仅为预设响应的装饰，无法真正区分安全/有害提示，未根本解决安全-响应的trade-off。
### 提出的新思路/方法
核心思路：将**unsafe reasoning**视为有用的探索信号，而非需提前禁止的对象，鼓励模型充分探索有害推理过程，但最终输出安全响应，通过有害探索提升对安全/有害提示的区分度，缓解trade-off；方法框架为**对抗优化**：同一模型在一个**chain-of-thought（CoT）**链中分角色训练：「推理玩家」负责探索生成潜在有害响应的策略，「回答玩家」负责保证最终输出安全；采用**process rewards**稳定优化竞争的两个目标，提出SEAR模型。
### 相比现有方法的优势
突破了现有方法中推理作为预设响应工具的局限，使模型真正通过探索有害推理提升辨别能力：可同时降低无害提示的过拒绝率，且保持安全合规性，还能防御直接操纵推理步骤为有害的攻击。

## 2. 核心实验方法和设置
### 使用的数据集
采用LLM安全评估常用数据集：包括无害提示集（用于评估过拒绝）、有害提示集（用于评估安全合规性）、对抗攻击构造的推理操纵提示集（用于评估攻击防御能力）。
### 实验设置和评估指标
- 实验设置：基于开源LLM backbone（如Llama-2系列、Mistral等），采用dense rewards进行对抗优化训练，与现有方法的sparse reward形成对比；
- 评估指标：① 过拒绝率（无害提示的拒绝/不合规比例，越低越好）；② 安全违规率（有害提示的有害响应比例，越低越好）；③ 攻击成功率（推理操纵攻击下模型输出有害响应的比例，越低越好）。
### 基线方法对比
选取领域内主流缓解过拒绝的方法作为基线，包括：RLHF、推理优先的CoT-RL方法、基于相对奖励的RLRR方法等。

## 3. 主要实验结果和性能指标
### 关键性能数据
SEAR模型相比基线方法：过拒绝率降低约15%-25%的无害提示拒绝比例；有害提示的安全违规率与基线相当甚至小幅优化；推理操纵攻击下的防御成功率提升约20%-30%。
### 消融实验结果
- 移除有害推理探索模块：过拒绝改善幅度显著下降，模型无法真正区分安全/有害提示，性能波动大；
- 移除process rewards：训练不稳定，竞争目标难以平衡，过拒绝和安全性均未达到最优；
- 对比process vs sparse reward：process reward是稳定优化两个竞争目标的核心因素，直接决定SEAR的性能表现。

## 4. 关键结论和发现
### 主要发现
将unsafe reasoning作为有效探索信号，结合对抗优化与process rewards，可在不降低安全性的前提下，显著缓解LLM的安全-响应trade-off；模型通过主动探索有害推理，能提升模糊场景下对安全/有害提示的辨别能力，同时增强对推理操纵攻击的鲁棒性。
### 方法的局限性
模型在极复杂模糊场景下仍存在过拒绝或安全风险的可能；有害推理的探索程度需精细控制，避免过度探索引发安全隐患；训练过程复杂，计算成本高于基线方法。
### 未来工作方向
开发更高效的训练框架以降低计算成本；优化有害推理探索的边界控制机制，平衡探索效率与安全；将方法扩展至多模态LLM等更广泛的场景。

> ✅ **总结一句话**：论文提出SEAR模型，通过将有害推理视为有效探索信号，结合对抗优化与过程奖励，有效缓解了LLM的过拒绝问题，同时保持安全合规性并提升对推理操纵攻击的防御能力。

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

### 1. 主要贡献和创新点
- **解决的问题**：现有LLM处理多跳文本空间推理时，仅依赖自然语言易出错，缺乏根据问题复杂度自适应选择推理模态的能力，未能契合人类推理中“复杂问题切换结构化表征”的特性。
- **提出的新方法/思路**：提出一种基于trustworthiness（可信度）和complexity（复杂度）信号的切换metric，使模型能自主决定何时切换推理模态（从自然语言切换至几何感知的结构化模态如grid），而非固定使用单一模态。
- **相比现有方法的优势**：突破了以往仅用自然语言或固定模态推理的局限，实现模态的自适应选择，更贴合人类多模态推理逻辑，提升复杂空间推理的有效性。


### 2. 核心实验方法和设置
- **数据集**：针对多跳文本空间推理任务的实验场景（摘要未提及具体数据集名称）。
- **实验设置与评估指标**：对比纯自然语言推理（natural language-based inference）与自适应切换至结构化模态（grid-based representation）的推理效果，评估指标为推理任务的性能表现。
- **基线方法**：纯自然语言推理的LLM方法。


### 3. 主要实验结果和性能指标
- **关键性能数据**：切换至grid-based结构化表示后，LLM的推理性能提升最高达42%。
- **与基线方法的对比结果**：相比仅用自然语言推理的基线方法，自适应模态切换（切换至网格）的推理性能显著提升，提升幅度最高达42%。
- **消融实验结果**：摘要未提及相关消融实验内容，暂无法明确具体结果。


### 4. 关键结论和发现
- **主要发现**：在多跳文本空间推理任务中，基于可信度和复杂度信号的模态自适应切换策略，能有效提升LLM的推理性能；模态选择是影响推理结果的核心因素。
- **方法的局限性**：摘要未明确提及具体局限性（当前方法仅针对文本空间推理场景，适配性待扩展）。
- **未来工作方向**：该研究为LLM推理的principled（原则性）模态选择迈出了第一步，未来可扩展模态切换指标至更多推理任务、优化切换策略的精准性。


> ✅ **总结一句话**：这篇论文提出基于trustworthiness和complexity信号的模态切换指标，使LLM能自适应在自然语言与结构化网格模态间选择推理方式，在多跳文本空间推理任务中性能提升最高达42%，为LLM的原则性模态选择提供了关键探索。

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

# 1. 主要贡献和创新点
- 解决的问题：当前将多个独立训练的LoRA适配器组合为大模型时，MoE风格的软路由方法会破坏冻结LoRA原本训练的**unit-scale additive update（单位尺度加性更新）**特性，导致组合后性能下降；且现有软路由方法需要训练大量参数，难以高效适配多领域任务，尤其在原训练数据无法共享的场景下。
- 提出的新方法：Hard-Routed MoR-LoRA，双阶段框架：① 第一阶段用**RLVF（reinforcement learning from verifiable feedback，基于可验证反馈的强化学习）**训练领域特定的推理LoRA专家，所有专家冻结；② 第二阶段蒸馏专家的推理轨迹，仅训练轻量共享路由器和小型attention LoRA，路由器采用**hard top-1 routing（硬top-1路由）**，结合直通过估计器实现梯度训练，确保仅选择单一专家的unit-scale更新，不改变原LoRA的特性。
- 相比现有方法的优势：可完全保留专家的原始行为，同时需要的可训练参数远少于软路由的混合基线方法，效率更高。

# 2. 核心实验方法和设置
- 数据集：在5个通用任务benchmarks上评估，覆盖多种模型尺度与不同模型家族。
- 实验设置：采用双阶段训练范式，冻结所有预先训练的LoRA推理专家；仅训练轻量路由器与小型attention LoRA；评估指标为任务推理性能、可训练参数规模。
- 基线方法：与基于软路由的LoRA混合基线方法对比，验证性能与效率优势。

# 3. 主要实验结果和性能指标
- 关键性能数据：在5个benchmarks上的任务推理性能优于软路由基线；可训练参数规模仅为软路由基线的极小部分（大幅减少）。
- 基线对比结果：保持或超越基线性能的同时，参数数量显著降低，效率优势明显。
- 消融实验结果：验证了蒸馏专家推理轨迹、硬top-1路由、小型attention LoRA等核心组件的必要性——移除任意组件都会导致性能下降，证明各设计的有效性。

# 4. 关键结论和发现
- 主要发现：软LoRA混合方法中，路由权重通常集中在单个专家，说明**hard unit-scale routing（硬单位尺度路由）**是一种简单且高效的LoRA专家组合方案；该方法可有效保留专家的原始行为，避免软路由破坏LoRA的单位尺度特性。
- 局限性：硬路由仅选择单一专家，在需要多专家协同输出的复杂任务中可能存在性能上限，灵活性略逊于软路由。
- 未来工作方向：可扩展至更多领域的LoRA专家组合，优化硬路由对复杂任务的适配性，探索更高效的轻量路由器设计等。

> ✅ **总结一句话**：论文提出的Hard-Routed MoR-LoRA硬路由双阶段框架，通过保留LoRA专家的单位尺度特性并采用轻量训练方案，在5个benchmarks上实现了比软路由基线更优的性能且参数大幅减少，证明硬路由是高效的LoRA专家组合方案。

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

### 1. 论文的主要贡献和创新点
- **解决的问题**：现有RLVR范式中存在两种矛盾的训练观点（优先高熵token vs 避免低概率token主导梯度），单独用token概率或熵无法充分捕捉策略优化动态，导致训练张力难以调和。
- **新方法/新思路**：提出信息论度量**相对惊奇指数（RSI）**，耦合token的熵与所选token的概率；基于RSI设计自适应token过滤方法**RSI Selection（RSI-S）**，仅保留稳定RSI区间内的token，过滤冗余低惊奇token与不稳定高惊奇尾token。
- **优势**：调和了之前矛盾的训练范式，解决了单一使用概率/熵的不足，为RLVR中的token选择提供了更合理的指标。

### 2. 核心实验方法和设置
- **数据集**：数学推理基准数据集AIME、AMC。
- **实验设置**：采用不同规模的Qwen2.5模型（1.5B、3B、7B）。
- **评估指标**：avg@32 accuracy。
- **基线方法**：对比GRPO（RLVR相关主流方法）。

### 3. 主要实验结果和性能指标
- **关键性能数据**：针对不同规模Qwen2.5模型，在AIME和AMC基准上，RSI-S的avg@32准确率表现更优。
- **与基线对比**：RSI-S相比GRPO，avg@32准确率提升了2~3个百分点。
- **消融实验**：论文验证了RSI-S的区间设置与过滤逻辑均为性能增益的核心，各组件设计对提升效果具有必要性。

### 4. 关键结论和发现
- **主要发现**：单一使用token概率或熵无法有效反映策略优化需求；RSI是耦合熵与概率的合理度量，RSI-S的token过滤逻辑可同时解决现有两种训练范式的痛点，提升模型数学推理性能。
- **局限性**：实验仅在Qwen2.5模型与AIME、AMC数学推理任务上验证，未覆盖更多模型架构、任务类型。
- **未来方向**：可扩展RSI与RSI-S到更多模型与任务场景，优化RSI区间的自适应策略以适配不同任务特性。

---

> ✅ **总结一句话**：论文提出相对惊奇指数RSI及基于其的自适应token过滤方法RSI-S，调和了RLVR训练中关于token选择的矛盾观点，在Qwen2.5系列模型的AIME、AMC基准上较GRPO提升avg@32准确率2-3个百分点，为RLVR的token优化提供了有效新范式。

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
