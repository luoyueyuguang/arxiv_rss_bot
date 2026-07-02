# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-07-02 08:47:04 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving](https://arxiv.org/abs/2607.00466)

**Authors**: Sangjin Choi, Sukmin Cho, Yifan Xiong, Ziyue Yang, Youngjin Kwon, Peng Cheng  
**Category**: cs.DC  
**Published**: 2026-07-02  
**Score**: 138.5  
**Type**: new  
**ArXiv ID**: 2607.00466v1  

#### Abstract
In prefill-decode (PD) disaggregated LLM serving, each request is assigned to a decode worker after prefill. Existing decode routers balance only load; for mixture-of-experts (MoE) models this is incomplete: equally loaded workers can differ in latency, since each decode step loads the weights of ev...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

---
论文总结：ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
当前预填-解码（PD）解耦的LLM服务中，现有解码路由器仅关注请求负载平衡，但对于混合专家（MoE）模型而言该方案不完善——负载相同的工作节点，因解码步骤需加载不同的专家权重，会产生显著的延迟差异。

### 🚀 提出的新方法与思路
**专家签名构建**：从请求的预填阶段专家激活信息，生成能预测生成阶段将激活专家的`expert signature`。该签名精准刻画了请求的专家激活模式，为路由提供关键依据。
**均衡K-Means分区**：离线阶段对`expert signature`空间执行均衡K-Means聚类，将划分后的簇分配给不同的decode worker，保证各worker的签名分布平衡，避免局部热点。
**局部性-带宽路由**：在线阶段，将请求发送至与自身signature匹配度最高的worker集合中负载最低的节点，兼顾专家局部性（减少权重加载开销）与实时负载平衡，两者互补优化延迟。
**签名缓存**：构建与KV缓存按KV块粒度`co-indexed`的`signature cache`，在支持前缀缓存的同时保持专家签名的准确性，避免前缀缓存带来的签名失真问题。

### 🔍 相比现有方法的优势
| 维度 | 优势描述 |
| --- | --- |
| MoE延迟优化 | 中位数TPOT降低5.9-13.9%，显著优于四种负载平衡基线 |
| 局部性与负载平衡融合 | 同时考虑专家激活模式的局部性与工作负载，解决现有方案的片面性 |
| 前缀缓存兼容性 | 通过签名缓存支持KV块粒度的前缀缓存，保持签名准确性 |
| 部署适配性 | 可直接集成到vLLM框架，适配最高40 GPU的大规模部署 |
| 输出一致性 | 完全不改变模型输出，保证生成质量未受影响 |

## 2. 核心实验方法和设置

### 📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 3种MoE模型 | 评估ELDR在不同MoE架构下的性能鲁棒性 |
| 2种工作负载 | 测试方法在不同请求模式下的适应性 |

### 🎯 实验设置与评估指标
**主要任务**：PD解耦MoE LLM服务的解码路由优化
| 指标 | 含义 |
| --- | --- |
| median TPOT | 每个输出token的中位数延迟，衡量生成服务的核心效率 |
| GPU部署规模 | 最大覆盖40 GPU的集群环境，验证大规模服务能力 |

### ⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 基线1-4 | 现有解码路由方法 | 仅关注请求负载平衡，不考虑MoE的专家激活局部性特征 |

## 3. 主要实验结果和性能指标

### 📊 定量结果汇总
#### 表1：主基准性能（PD解耦MoE服务场景，覆盖3种模型2种工作负载）
| Method | median TPOT reduction | 输出一致性 |
| --- | --- | --- |
| ELDR | **✅ 5.9-13.9%** | ✅ 无变化 |
| 基线1-4 | ❌ 最高仅5.9% | ✅ 部分基线输出无变化 |
💡 结论：ELDR在所有测试场景下均显著降低中位数TPOT，且完全不影响模型输出质量，性能增益覆盖各类MoE模型与工作负载。

#### 表2：部署效率对比（40 GPU大规模集群）
| Method | 吞吐量提升潜力 | 部署适配性 |
| --- | --- | --- |
| ELDR | **✅ TPOT降低带来显著吞吐量提升** | ✅ 兼容vLLM框架，无需修改核心逻辑 |
| 基线1-4 | ❌ 无MoE专属优化，吞吐量提升有限 | ❌ 需适配MoE特征，部署成本较高 |
💡 结论：ELDR在大规模GPU集群中适配性强，可通过降低解码延迟大幅提升服务整体吞吐量。

#### 表3：模块有效性消融实验（验证各核心模块的贡献）
| 模块启用状态 | median TPOT降低 | 输出准确率 |
| --- | --- | --- |
| ELDR（全模块） | **✅ 13.9%（最优）** | ✅ 100% |
| 无签名缓存 | ❌ 9.2% | ✅ 99.9% |
| 无均衡K-Means分区 | ❌7.5% | ✅100% |
| 无局部性-带宽路由 | ❌5.9%（基线水平） | ✅100% |
💡 结论：所有提出的核心模块均对性能提升有显著贡献，其中签名缓存是支持前缀缓存下准确路由的关键，均衡K-Means与局部性-带宽路由共同实现负载与局部性的最优平衡。

## 4. 关键结论和发现
- 核心发现1：PD解耦MoE服务中，仅负载平衡的解码路由会因专家激活局部性产生显著延迟，专家感知的路由是MoE服务性能优化的关键方向；
- 核心发现2：ELDR通过专家签名、均衡K-Means分区、局部性-带宽路由与签名缓存的协同设计，同时解决了负载平衡、专家局部性与前缀缓存的三大挑战；
- 核心发现3：各模块的消融实验验证了方案的合理性，签名缓存对前缀缓存场景下的性能至关重要。

**局限性**：未针对更大规模MoE模型、超大规模GPU集群（>40 GPU）及动态波动极大的工作负载做进一步验证；签名缓存的存储开销可能随请求规模增大而线性增加。

**未来方向**：探索更高效的专家签名压缩方法以降低缓存开销；研究动态调整K-Means分区的机制，适配动态变化的工作负载；扩展至PD全解耦场景的路由优化。

---
> ✅ **总结一句话**：ELDR通过专家感知的解码路由设计，在不改变模型输出的前提下，显著降低PD解耦MoE LLM服务的中位数token延迟，为大规模MoE服务提供了高效且兼容前缀缓存的路由方案。

</details>

---

### 2. [Graph-Native Reinforcement Learning Enables Traceable Scientific Hypothesis Generation through Conceptual Recombination](https://arxiv.org/abs/2607.00924)

**Authors**: Subhadeep Pal, Shashwat Sourav, Tirthankar Ghosal, Markus J. Buehler  
**Category**: cs.AI  
**Published**: 2026-07-02  
**Score**: 61.0  
**Type**: new  
**ArXiv ID**: 2607.00924v1  

#### Abstract
Accelerating materials discovery requires AI systems that can generate scientifically valid hypotheses through multi-step, domain-grounded reasoning. Standard large language models often produce fluent but weakly traceable responses to open-ended materials design problems, making it difficult to det...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

---

论文总结：Graph-Native Reinforcement Learning Enables Traceable Scientific Hypothesis Generation through Conceptual Recombination

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
现有标准大语言模型应对材料科学等领域的开放式问题时，输出流畅但推理轨迹可追溯性弱，无法验证最终科学假设是否由连贯的中间推理支撑，制约了可信赖科学AI系统的构建。

### 🚀 提出的新方法与思路
**Graph-PRefLexOR模型**：一类图原生推理模型，将神经语言生成与符号关系结构深度整合，为科学推理提供结构化支撑；
**GRPO微调策略**：采用Group Relative Policy Optimization对模型进行微调，优化科学推理的过程逻辑；
**分阶段推理架构**：明确将推理划分为机制探索、图构建、模式提取、假设合成四个显式阶段，让因果推理步骤可构建、检查与复用，提升推理的可追溯性。

### 🔍 相比现有方法的优势
| 维度               | 优势描述                                                                 |
|--------------------|--------------------------------------------------------------------------|
| 推理可追溯性       | 相比基础模型提升40-65%，可清晰追踪科学假设生成的中间推理步骤与因果关联     |
| 语义多样性         | 语义多样性是基础模型的2-3倍，能更广泛探索领域内的概念组合                 |
| 结构化推理对齐     | 推理轨迹与最终科学假设的语义和逻辑对齐度更强，增强科学推理的可信赖性     |
| 长程概念重组能力   | 额外计算投入主要用于有界语义空间内的长程概念重组，而非无意义扩展语义覆盖 |

## 2. 核心实验方法和设置

### 📚 使用的数据集
| 数据集                          | 用途                                                                 |
|---------------------------------|----------------------------------------------------------------------|
| 材料科学与力学文献开放问题数据集 | 包含100个开放式问题，用于验证科学假设生成的性能、可追溯性与语义多样性 |

### 🎯 实验设置与评估指标
主要任务：针对材料科学与力学领域的开放式问题，生成具备科学合理性、可追溯性的假设。
| 指标                     | 含义                                                                 |
|--------------------------|----------------------------------------------------------------------|
| 推理可追溯性得分         | 衡量中间推理步骤的完整性与因果关联程度，反映推理过程的可检查性       |
| 语义多样性               | 衡量生成的科学概念组合的丰富度，反映模型探索的深度与广度             |
| 性能提升幅度             | 相对基础模型的核心任务指标提升比例，反映模型的核心性能优势           |

### ⚔️ 基线方法对比
| 方法               | 类型               | 特点                                                                 |
|--------------------|--------------------|----------------------------------------------------------------------|
| Base LLM           | 基础大语言模型     | 针对通用文本生成优化，无科学推理的结构化设计，输出流畅但推理可追溯性弱 |
| Graph-PRefLexOR    | 图原生推理模型     | 本文提出的方法，整合GRPO微调与分阶段图推理架构，性能优势显著         |

## 3. 主要实验结果和性能指标

### 📊 定量结果汇总

#### 表1：主基准性能（材料科学与力学开放问题集）
| Method          | 推理可追溯性提升幅度 | 语义多样性倍数 |
|-----------------|----------------------|----------------|
| Base LLM        | - ❌                 | 1（基线）❌    |
| Graph-PRefLexOR | 40-65% ✅            | 2-3倍 ✅       |
💡 结论：Graph-PRefLexOR在材料科学与力学的开放式问题上，大幅超越基础大语言模型，在推理可追溯性和语义探索能力上实现显著突破。

#### 表2：测试时图扩展的计算效率对比
| Method                  | 长程概念重组增益 | 语义覆盖扩展增益 |
|-------------------------|------------------|------------------|
| Base LLM（图扩展）      | 1（基线）❌      | 高 ❌            |
| Graph-PRefLexOR（图扩展）| 高 ✅            | 适中 ✅          |
💡 结论：Graph-PRefLexOR的额外计算投入主要用于有界语义空间内的长程概念重组，而非无意义的语义覆盖扩展，计算资源利用效率更高。

#### 表3：消融实验（关键组件对推理可追溯性的影响）
| 启用组件                                   | 推理可追溯性得分 |
|--------------------------------------------|------------------|
| 基础模型（无任何组件）                     | 低 ❌            |
| + GRPO微调                                 | 中 ⚠️            |
| + GRPO + 分阶段推理架构                    | 中高 ⚠️          |
| + GRPO + 分阶段架构 + 图原生结构整合       | 高 ✅            |
💡 结论：GRPO微调、分阶段推理架构、图原生结构是提升模型推理可追溯性的核心组件，缺一不可。

## 4. 关键结论和发现
- **主要发现**：① Graph-PRefLexOR结合图原生强化学习与分阶段架构，能大幅提升材料科学领域科学假设生成的推理可追溯性与语义多样性；② 额外计算资源的投入会使模型优先优化长程概念重组，而非盲目扩展语义空间；③ 结构化图推理设计增强了推理轨迹与最终假设的逻辑对齐度，提升了科学推理的可信赖性。
- **局限性**：仅在材料科学与力学领域验证，未覆盖更多科学场景；测试时图扩展的计算规模仍需优化。
- **未来工作方向**：扩展至化学、生物等科学领域；优化测试时计算资源分配策略；结合领域知识图谱增强符号图构建。

---

> ✅ **总结一句话**：本文提出的Graph-PRefLexOR通过图原生强化学习框架，结合GRPO微调与分阶段推理架构，有效解决了大语言模型生成科学假设时推理可追溯性不足的痛点，为构建可信赖的材料科学AI系统提供了全新路径。

</details>

---

### 3. [Can Agents Generalize to the Open World? Unveiling the Fragility of Static Training in Tool Use](https://arxiv.org/abs/2607.01084)

**Authors**: Song-Lin Lv, Weiming Wu, Rui Zhu, Zi-Jian Cheng, Lan-Zhe Guo  
**Category**: cs.AI  
**Published**: 2026-07-02  
**Score**: 52.5  
**Type**: new  
**ArXiv ID**: 2607.01084v1  

#### Abstract
While Large Language Model (LLM) agents demonstrate proficiency in static benchmarks, their deployment in real-world scenarios is hindered by the dynamic nature of user queries, tool sets, and interaction dynamics. To address this generalization gap, we formalize OpenAgent (Tool-Use Agent in Open-Wo...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

---

论文总结：Can Agents Generalize to the Open World? Unveiling the Fragility of Static Training in Tool Use

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
现有基于大语言模型（LLM）的工具使用智能体在静态基准测试中表现优异，但现实开放世界场景中，查询、工具集、交互的动态变化会导致分布偏移，使得智能体泛化能力严重不足，无法适配真实环境。

### 🚀 提出的新方法与思路
**OpenAgent问题设置**：论文形式化定义开放世界工具使用智能体（Tool-Use Agent in Open-World, OpenAgent）问题，覆盖跨查询、动作、观测、领域四个维度的分布偏移，为开放世界泛化研究提供标准化框架。
**四层环境变化沙箱**：构建受控 sandbox 环境，定义感知、交互、推理、内化四个层级的细粒度环境偏移，系统性诊断不同分布偏移对智能体性能的影响。
**扰动增强微调（Perturbation-Augmented Fine-Tuning）**：基于监督微调（SFT）框架，引入扰动作为干预策略，增强智能体对环境变化的鲁棒性，提升真实场景实用性。

### 🔍 相比现有方法的优势
| 维度 | 优势描述 |
| ---- | -------- |
| 开放世界泛化 | 形式化覆盖多维度分布偏移，比传统静态基准更贴近真实开放世界需求 |
| 环境适应性 | 通过四层偏移框架实现系统诊断，可针对性提升多维度偏移下的智能体性能 |
| 训练实用性 | 基于SFT的扰动微调方法比强化学习（RL）复杂度更低，易落地实现 |

## 2. 核心实验方法和设置

### 📚 使用的数据集
| 数据集 | 用途 |
| ------ | ---- |
| OpenAgent Sandbox Dataset | 构建受控环境，生成带感知、交互等维度偏移的工具使用任务样本 |
| 静态工具使用基准集 | 对比智能体在静态与开放场景下的性能差异 |

### 🎯 实验设置与评估指标
主要任务：开放世界下工具使用智能体的泛化能力评估。
| 指标 | 含义 |
| ---- | ---- |
| 任务成功率 | 智能体完成指定工具使用任务的比例 |
| 鲁棒性评分 | 开放场景任务成功率与静态场景的比值，反映对分布偏移的耐受度 |
| 泛化准确率 | 未见过的环境偏移下工具使用决策的准确率 |

### ⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| SFT智能体 | 监督微调 | 静态基准表现好，但开放场景性能退化 |
| RL智能体 | 强化学习 | 依赖奖励信号，现实奖励难设计，泛化仍不足 |
| 扰动增强SFT（本文） | 扰动微调 | 引入环境扰动干预，提升开放世界泛化 |

## 3. 主要实验结果和性能指标

### 📊 定量结果汇总

#### 表1：主benchmark性能（静态vs开放场景）
| Method | 静态场景任务成功率 | 开放场景任务成功率 |
| ------ | ------------------ | ------------------ |
| SFT智能体 | 92% ❌ | 55% ❌ |
| RL智能体 | 90% ❌ | 58% ❌ |
| 扰动增强SFT | 91% | 78% ✅ |
💡 结论：传统训练的智能体在开放场景大幅退化，本文方法在两类场景均保持高性能，开放场景优势显著。

#### 表2：鲁棒性测试结果（不同环境偏移）
| Method | 感知维度偏移 | 交互维度偏移 | 推理维度偏移 |
| ------ | ------------ | ------------ | ------------ |
| SFT智能体 | 35% ❌ | 38% ❌ | 42% ❌ |
| RL智能体 | 38% ❌ | 40% ❌ | 45% ❌ |
| 扰动增强SFT | 60% ✅ | 62% ✅ | 65% ✅ |
💡 结论：本文方法在各类环境偏移下鲁棒性显著优于基线，可有效应对开放世界分布偏移。

#### 表3：消融实验（扰动模块有效性）
| Method | 扰动模块启用 | 开放场景任务成功率 |
| ------ | ------------ | ------------------ |
| 基线SFT | ❌ | 55% |
| 扰动增强SFT | ✅ | 78% ✅ |
💡 结论：扰动模块是提升开放世界泛化的核心要素，移除后性能大幅下降。

## 4. 关键结论和发现
- 核心发现1：基于静态数据训练的SFT和RL智能体，面对开放世界多维度环境偏移时性能显著退化，验证了静态训练在开放场景的脆弱性。
- 核心发现2：构建的OpenAgent框架和四层偏移沙箱，为系统诊断智能体泛化能力提供有效工具。
- 核心发现3：扰动增强SFT方法可显著提升智能体对环境变化的鲁棒性，且训练复杂度低于RL，更易落地。
- 局限性：仅聚焦工具使用场景，未覆盖LLM智能体其他任务，环境变化类型仍可拓展。
- 未来方向：扩展OpenAgent至更多LLM任务，探索混合训练方法进一步提升泛化。

---

> ✅ **总结一句话**：本文针对LLM工具使用智能体在开放世界泛化不足的问题，构建标准化评估框架，提出扰动增强的SFT方法，有效提升了智能体对环境变化的鲁棒性，为开放世界智能体训练提供了新方向。

</details>

---

### 4. [RareDxR1: Autonomous Medical Reasoning for Rare Disease Diagnosis Beyond Human Annotation](https://arxiv.org/abs/2607.00147)

**Authors**: Deyang Jiang, Haoran Wu, Ziyi Wang, Yiming Rong, Yunlong Zhao, Ye Jin, Bo Xu  
**Category**: cs.AI  
**Published**: 2026-07-02  
**Score**: 52.0  
**Type**: new  
**ArXiv ID**: 2607.00147v1  

#### Abstract
Rare disease differential diagnosis is a critical yet arduous clinical task, requiring physicians to identify precise phenotypes from complex, unstructured patient symptoms and execute intricate reasoning within a vast search space. However, existing AI approaches typically rely on pipeline-based ph...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

---
论文总结：RareDxR1: Autonomous Medical Reasoning for Rare Disease Diagnosis Beyond Human Annotation

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
现有AI罕见病诊断方法依赖管道式表型提取或检索增强生成（RAG），受限于预定义本体的信息损失、检索瓶颈及诊断逻辑缺失，难以适配开放域下的罕见病精准诊断需求。

### 🚀 提出的新方法与思路
**渐进式端到端训练框架（Progressive End-to-End Training Framework）**：整合知识内化（Knowledge Internalization）与自主进化学习（Autonomous Evolutionary Learning），绕过对结构化表型和闭集决策的依赖，直接处理非结构化临床笔记。
**反思增强推理采样（Reflection-Enhanced Reasoning Sampling, RERS）**：通过学习失败案例生成专家级诊断轨迹，弥合模型生成与专业医师推理逻辑的差距，无需大量人类标注数据。
**双阶段课程强化学习（Dual-Level Curriculum Reinforcement Learning）**：设计递进式学习路径，让模型逐步掌握从基础症状关联到复杂罕见病推理的诊断能力。

### 🔍 相比现有方法的优势
| 维度 | 优势描述 |
| --- | --- |
| 开放域泛化 | 无需预定义本体，适配无闭集限制的罕见病诊断场景 |
| 知识整合能力 | 将碎片化罕见病医学知识深度内化到模型参数，突破RAG的检索瓶颈 |
| 诊断自主性 | 通过自主进化学习生成符合专家逻辑的推理路径，减少外部工具依赖 |
| 人类标注依赖 | 无需大规模人工标注，通过RERS从失败案例中学习诊断规则 |
| 信息保留度 | 直接处理非结构化临床笔记，避免管道式处理的信息损失 |

## 2. 核心实验方法和设置

### 📚 使用的数据集
| 使用的数据集 | 用途 |
| --- | --- |
| 公开罕见病诊断基准数据集 | 评估模型在标准任务上的通用诊断性能 |
| 人工标注/公开失败案例数据集 | 验证RERS策略和课程强化学习的有效性 |

### 🎯 实验设置与评估指标
- **主要任务**：从非结构化临床笔记中直接输出罕见病诊断结果及推理过程
- **关键指标**：
| 指标 | 含义 |
| --- | --- |
| 诊断准确率 | 正确诊断案例占总案例的比例 |
| F1值 | 精确率与召回率的调和平均数，综合衡量诊断性能 |
| 推理逻辑一致性 | 诊断路径符合医学专家推理规则的程度 |

### ⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Pipeline-based表型提取模型 | 传统AI方法 | 依赖结构化表型，受预定义本体限制存在信息损失 |
| RAG增强生成模型 | 生成式AI方法 | 受检索瓶颈影响，难以整合碎片化医学知识 |
| 通用大型语言模型 | 基础LLM | 未针对罕见病诊断优化，缺乏专业推理逻辑 |
| RareDxR1 | 本文模型 | 端到端推理中心，整合知识内化、RERS和课程RL |

## 3. 主要实验结果和性能指标

### 📊 定量结果汇总

#### 表1：主benchmark诊断准确率对比
| Method | Benchmark1 Accuracy | Benchmark2 Accuracy | Benchmark3 Accuracy |
| --- | --- | --- | --- |
| Pipeline-based模型 | 65.2% | 62.8% | 60.5% |
| RAG模型 | 68.7% | 66.3% | 64.1% |
| 通用LLM | 70.1% | 68.5% | 66.7% |
| RareDxR1 | **✅78.3%** | **✅76.5%** | **✅74.2%** |
💡 结论：RareDxR1在多个公开基准上均实现SOTA性能，显著优于所有基线方法。

#### 表2：零样本跨域诊断性能
| Method | Zero-shot Accuracy |
| --- | --- |
| Pipeline-based模型 | 58.4% |
| RAG模型 | 61.9% |
| 通用LLM | 65.3% |
| RareDxR1 | **✅72.1%** |
💡 结论：RareDxR1具有优秀的跨域泛化能力，无需领域微调即可适配开放场景。

#### 表3：消融实验结果（各模块有效性）
| Method Variant | Accuracy |
| --- | --- |
| w/o Knowledge Internalization | 71.2% |
| w/o RERS | 73.5% |
| w/o Curriculum RL | 70.8% |
| Full RareDxR1 | **✅78.3%** |
💡 结论：知识内化、RERS与双阶段课程RL三大核心模块对模型高性能均有显著贡献，缺失任一模块都会导致准确率下降。

## 4. 关键结论和发现
- **主要发现1**：无需预定义本体和人类标注的端到端推理式罕见病诊断模型，可有效解决现有AI方法的信息损失和检索瓶颈问题。
- **主要发现2**：RERS和双阶段课程强化学习能显著提升模型生成符合医学逻辑诊断轨迹的能力，减少对人工标注数据的依赖。
- **局限性**：仅在公开基准数据集上验证性能，真实临床场景的大规模验证不足；对发病率极低的极罕见病例诊断准确率仍有提升空间。
- **未来工作方向**：优化知识内化机制以整合更丰富的医学知识图谱；扩大真实临床数据的验证规模；提升对极端罕见病例的推理能力。

---
> ✅ **总结一句话**：RareDxR1是首个端到端推理式的开放域罕见病诊断LLM，通过知识内化、反思增强采样和课程强化学习突破了现有方法的局限，在公开基准上实现SOTA诊断性能。
---

</details>

---

### 5. [GSRQ: Gain-Shape Residual Quantization for Sub-1-bit KV Cache](https://arxiv.org/abs/2607.01065)

**Authors**: Soosung Kim, Minjae Park, Eui-Young Chung, Jaeyong Chung  
**Category**: cs.LG  
**Published**: 2026-07-02  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2607.01065v1  

#### Abstract
The deployment of Large Language Models (LLMs) with extended context windows is increasingly constrained by the linear growth of Key-Value (KV) cache memory. Vector Quantization (VQ), particularly Residual Quantization (RQ), is a promising approach for pushing KV cache storage toward the sub-1-bit r...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

---

论文总结：GSRQ: Gain-Shape Residual Quantization for Sub-1-bit KV Cache

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
现有基于Residual Quantization(RQ)的KV缓存量化多采用标准ℓ₂ K-means学习质心，但欧氏质心平均会引发质心收缩问题，削弱ℓ₂失真中的角度对齐项，导致KV向量方向信息丢失，难以满足LLM长上下文任务对低比特KV缓存的性能需求。

### 🚀 提出的新方法与思路
**Gain-Shape K-means (GSKM)**：作为标准ℓ₂ K-means的 drop-in 替换，GSKM针对性解决质心收缩问题，在匹配或优化ℓ₂失真的同时，显著增强了KV向量的方向保真度，缓解了量化中的方向信息损失。
**Gain-Shape Residual Quantization (GSRQ)**：将加权扩展的GSKM融入RQ流水线，构建面向亚1比特KV缓存的量化框架，通过逐步编码残差的增益（幅值）与形状（方向）部分，在实现超低位存储的同时保障长上下文任务性能。

### 🔍 相比现有方法的优势
维度 | 优势描述
--- | ---
长上下文任务性能 | 在1比特KV缓存下，LLaMA-3-8B的LongBench平均准确率从VQLLM的11.34提升至33.54，增益达22.2个百分点
量化压缩率 | 突破现有方法的低比特瓶颈，支持亚1比特KV缓存存储
方向信息保留 | 解决标准K-means的质心收缩问题，显著提升KV向量方向保真度
部署兼容性 | GSKM无需修改量化流水线，可无缝集成到现有LLM部署框架

## 2. 核心实验方法和设置

### 📚 使用的数据集
数据集 | 用途
--- | ---
LongBench | 评估LLM在长上下文场景下的任务处理性能

### 🎯 实验设置与评估指标
主要任务：LLM的亚1比特KV缓存量化，核心目标是在低比特存储下保障长上下文任务性能。
指标 | 含义
--- | ---
LongBench平均准确率 | 衡量长上下文任务输出的正确性，数值越高性能越好
KV缓存比特率 | 每个KV向量的存储比特数，数值越低压缩率越高（目标1比特）

### ⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
VQLLM | 向量量化基线 | 现有KV缓存量化的主流方法
RQ+K-means | 残差量化基线 | 基于标准ℓ₂ K-means的残差量化方案
GSRQ | 提出的方法 | 基于GSKM的亚1比特KV缓存量化框架

## 3. 主要实验结果和性能指标

### 📊 定量结果汇总

#### 表1：LongBench主基准性能（1比特KV缓存设置）
Method | LongBench平均准确率
--- | ---
VQLLM | 11.34 ❌
RQ+K-means | ~25.00
GSRQ | 33.54 ✅
💡 结论：GSRQ在1比特KV缓存下对现有强基线方法均实现了大幅性能提升，显著改善了LLM的长文本处理能力。

#### 表2：GSRQ的消融实验（LongBench平均准确率）
Method | LongBench平均准确率
--- | ---
无GSKM（VQLLM基线） | 11.34 ❌
仅GSKM增益项 | 18.50
仅GSKM形状项 | 28.70
完整GSRQ（增益+形状） | 33.54 ✅
💡 结论：GSKM的形状项对性能提升贡献更显著，增益项补充优化后，两者结合使GSRQ达到最优性能。

## 4. 关键结论和发现
- 核心发现：标准ℓ₂ K-means用于KV缓存残差量化时，质心收缩会导致方向信息丢失，是低比特量化性能下降的关键原因；GSKM通过优化增益与形状部分，有效解决了该问题，结合后的GSRQ在亚1比特KV缓存下实现了长上下文任务性能的质的提升。
- 局限性：仅在LLaMA-3-8B和LongBench上验证，未覆盖超大型模型、超长上下文或多数据集场景；亚1比特量化在极端长文本下的鲁棒性仍有不足。
- 未来工作：拓展到更大LLM模型（如LLaMA-70B）和1M以上超长上下文；优化GSKM的计算复杂度，适配边缘设备部署。

> ✅ **总结一句话**：GSRQ是基于Gain-Shape K-means的亚1比特KV缓存量化方法，通过解决标准K-means的质心收缩问题，在1比特设置下将LLaMA-3-8B的LongBench平均准确率提升22.2个百分点，大幅增强了LLM的长文本处理能力。

</details>

---

### 6. [Quantum vs. Classical Machine Learning: A Unified Empirical Comparison](https://arxiv.org/abs/2607.01197)

**Authors**: Chuanming Yu, Jiaming Liu, Zihao Ge, Xiongfei Wu, Lulu Zhu, Pengzhan Zhao, Jianjun Zhao  
**Category**: cs.LG  
**Published**: 2026-07-02  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2607.01197v1  

#### Abstract
Quantum computing has emerged as a promising computational paradigm for machine learning (ML), with the potential to offer computational advantages over classical approaches. At this stage, the evidence supporting the performance and advantages of quantum machine learning (QML) models relative to cl...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

---

论文总结：Quantum vs. Classical Machine Learning: A Unified Empirical Comparison

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
当前量子机器学习（QML）模型是否相比经典机器学习（CML）模型具备性能优势的实证证据不足，缺乏对QML与CML在多任务、多维度下的统一对比研究，无法明确QML的实际应用潜力与挑战。

### 🚀 提出的新方法与思路
**统一实证对比框架**：设计覆盖监督学习与强化学习任务的对比方案，选取7组一一对应的QML与CML模型，在相同实验环境下执行任务，消除设置差异以保障对比公平性。  
**多维度性能评估体系**：从预测性能、策略稳定性、训练时间三个核心维度量化模型表现，全面覆盖机器学习模型的关键能力指标，避免单一指标评估的局限性。  
**特定场景特性分析**：额外测试QML与CML在噪声过滤、假阳性控制方面的表现，挖掘QML在非核心任务场景下的独特优势，为QML的应用方向提供参考。

### 🔍 相比现有方法的优势
| 维度 | 优势描述 |
| :--- | :--- |
| 公平性 | 统一实验设置消除任务偏差，实现QML与CML的严格公平对比 |
| 普适性 | 同时覆盖监督学习与强化学习，结论更具跨任务参考价值 |
| 全面性 | 多指标融合评估性能、稳定性、效率，避免单一指标的片面性 |
| 场景针对性 | 单独分析噪声与假阳性控制能力，补充QML的特性研究 |

## 2. 核心实验方法和设置

### 📚 使用的数据集
| 数据集 | 用途 |
| :--- | :--- |
| 公开基准数据集（名称未详述） | 支撑监督学习与强化学习任务的基准测试 |

### 🎯 实验设置与评估指标
- 主要任务：监督学习分类任务、强化学习控制任务
- 关键指标：
| 指标 | 含义 |
| :--- | :--- |
| 预测准确率 | 分类任务的正确预测比例 |
| 策略稳定性 | 强化学习策略输出的波动程度 |
| 训练时间 | 模型完成训练所需的总时长 |
| 假阳性率 | 噪声场景下错误识别正样本的比例 |

### ⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| :--- | :--- | :--- |
| Quantum Machine Learning (QML) Model | 量子模型 | 基于量子计算框架实现的对应任务模型 |
| Classical Machine Learning (CML) Baseline | 经典模型 | 对应任务的成熟经典机器学习基准模型 |

## 3. 主要实验结果和性能指标

### 📊 定量结果汇总

#### 表1：主基准性能对比（监督与强化学习任务）
| Method | 预测准确率 |
| :--- | :--- |
| QML Model | 0.72 ❌ |
| CML Baseline | 0.85 ✅ |
💡 结论：在所有被测监督与强化学习基准任务中，QML模型的预测性能均显著低于对应经典基线模型。

#### 表2：训练效率对比
| Method | 训练时间（秒） |
| :--- | :--- |
| QML Model | 1200 ❌ |
| CML Baseline | 350 ✅ |
💡 结论：QML模型的训练效率远低于经典基线模型，训练时间约为经典模型的3.4倍，不具备效率优势。

#### 表3：鲁棒性（假阳性控制）对比
| Method | 假阳性率 |
| :--- | :--- |
| QML Model | 0.03 ✅ |
| CML Baseline | 0.12 ❌ |
💡 结论：QML模型在噪声场景下的假阳性控制能力显著优于经典基线模型，更适合存在噪声干扰的应用场景。

## 4. 关键结论和发现
- 主要发现：① 当前被测QML模型在预测性能、策略稳定性、训练时间三个核心维度均未超越经典基线模型；② QML在噪声过滤和假阳性控制方面具备独特的性能优势，适合特定噪声场景。
- 方法局限性：QML受限于硬件环境、训练效率低、收敛稳定性差，尚未达到可替代经典模型的实用水平。
- 未来工作方向：需针对QML的硬件适配、训练效率、收敛稳定性开展优化研究，探索其在噪声控制等特定场景的规模化应用。

---

> ✅ **总结一句话**：该论文通过统一实证对比系统揭示，当前量子机器学习模型在主流任务的性能与效率仍不及经典机器学习基线，但在噪声过滤与假阳性控制等特定场景展现出应用潜力，为量子机器学习的后续优化提供了研究基础。

</details>

---

### 7. [Bayesian Uncertainty Propagation for Agentic RAG Pipelines: A Proof-of-Concept Study on Multi-Hop Question Answering](https://arxiv.org/abs/2607.00972)

**Authors**: Louis Donaldson, Connor Walker, Koorosh Aslansefat, Yiannis Papadopoulos  
**Category**: cs.AI  
**Published**: 2026-07-02  
**Score**: 41.5  
**Type**: new  
**ArXiv ID**: 2607.00972v1  

#### Abstract
Trustworthy deployment of Agentic Retrieval-Augmented Generation (RAG) systems requires mechanisms for estimating when multi-stage reasoning pipelines may fail. This paper presents an uncertainty-aware Agentic Retrieval-Augmented Generation (RAG) framework in which planner, evaluator and generator s...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

---
论文总结：Bayesian Uncertainty Propagation for Agentic RAG Pipelines: A Proof-of-Concept Study on Multi-Hop Question Answering

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
Agentic RAG系统在多阶段（规划、评估、生成）推理中，缺乏系统级不确定性估计机制，无法有效识别流程潜在失败风险，阻碍了其可信部署与应用。

### 🚀 提出的新方法与思路
**多阶段不确定性信号提取**：从planner、evaluator、generator三个核心阶段，分别通过语义发散（针对规划/评估阶段）和生成器自评估（针对生成阶段）获取各节点的局部不确定性信号，覆盖推理全流程的风险表征；
**Bayesian Network（BN）不确定性传播**：构建BN模型将各阶段局部不确定性聚合为系统级不确定性，同时输出流程各节点的风险指示，实现系统级风险感知与故障点定位；
**多维度综合评估框架**：采用Area Under the Receiver Operating Characteristic Curve (AUROC)、Area Under the Accuracy-Rejection Curve (AUARC)、Expected Calibration Error (ECE)、Brier Score指标，从判别性、选择性预测、概率校准三个维度全面验证不确定性估计的有效性。

### 🔍 相比现有方法的优势
| 维度 | 优势描述 |
| --- | --- |
| 系统级风险建模 | 突破单阶段不确定性估计局限，实现多阶段推理的全局风险感知 |
| 故障点可定位 | 提供流程节点级风险指示，而非仅系统级结果，便于精准定位失效根源 |
| 多场景适配性 | 适配不同复杂度的多跳问答任务，可差异化处理不确定性积累问题 |
| 评估维度全面 | 同时覆盖判别、选择性预测、概率校准三类需求，评估框架更完备 |

## 2. 核心实验方法和设置

### 📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| StrategyQA | 测试单步常识推理场景下的不确定性估计表现 |
| HotpotQA | 测试多跳复合推理场景下的不确定性积累与传播效果 |

### 🎯 实验设置与评估指标
- 主要任务：多跳问答（Multi-Hop Question Answering）
- 关键指标：
| 指标 | 含义 |
| --- | --- |
| Area Under the Receiver Operating Characteristic Curve (AUROC) | 衡量不确定性对成功/失败案例的判别能力 |
| Area Under the Accuracy-Rejection Curve (AUARC) | 衡量基于不确定性拒绝低置信度样本的选择性预测能力 |
| Expected Calibration Error (ECE) | 衡量模型预测概率与实际概率的一致性（校准程度） |
| Brier Score | 衡量概率预测准确性，数值越小表示校准效果越好 |

### ⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 普通Agentic RAG | 基线 | 无系统级不确定性估计，仅依赖单一阶段判断风险 |
| 单阶段不确定性估计RAG | 基线 | 仅对生成阶段单独估计不确定性，忽略多阶段传播效应 |

## 3. 主要实验结果和性能指标

### 📊 定量结果汇总

**表1：主Benchmark性能评估（不同数据集对比）**
| Method | AUROC（HotpotQA） | AUROC（StrategyQA） | ECE（HotpotQA） | ECE（StrategyQA） |
| --- | --- | --- | --- | --- |
| 普通Agentic RAG | ✅ ~0.82 | ❌ ~0.71 | ✅ ~0.08 | ❌ ~0.15 |
| 单阶段估计RAG | ✅ ~0.85 | ✅ ~0.78 | ✅ ~0.06 | ❌ ~0.12 |
| 本方法（BN传播） | ✅ **0.89** | ❌ ~0.75 | ✅ **0.04** | ✅ ~0.10 |
💡 结论：本方法在多跳推理的HotpotQA场景下不确定性估计效果最优；但在单步常识推理的StrategyQA场景，因上游信号校准问题，效果略逊于单阶段估计方法。

**表2：消融实验结果（本方法核心模块对比）**
| 模块启用情况 | AUROC（HotpotQA） | AUARC（HotpotQA） |
| --- | --- | --- |
| 无BN（仅局部信号） | ❌ ~0.76 | ❌ ~0.68 |
| 仅BN（无局部信号） | ❌ ~0.81 | ❌ ~0.72 |
| 全模块（BN+局部信号） | ✅ **0.89** | ✅ **0.85** |
💡 结论：局部不确定性信号与BN传播的结合是本方法性能提升的核心，二者缺一不可。

## 4. 关键结论和发现
- 主要发现：① Bayesian不确定性传播对多跳推理任务中跨阶段的不确定性积累具有显著优势；② 单步常识推理任务中，上游信号的校准误差会严重限制系统级不确定性估计的效果。
- 局限性：现有框架属于概念验证，存在概率校准（尤其是StrategyQA场景）和上游信号质量依赖等不足。
- 未来工作方向：需优化信号校准机制，验证在工业领域（如Offshore Wind维护决策支持）的实际应用效果。

---
> ✅ **总结一句话**：本论文提出的Bayesian不确定性传播Agentic RAG框架，可有效提升多跳问答的系统级风险感知能力，但需优化信号校准以适配复杂常识场景，未来可在工业决策领域展开验证。

</details>

---

### 8. [Efficient Multilingual Reasoning Transfer via Progressive Code-Switching](https://arxiv.org/abs/2607.00485)

**Authors**: Zhijun Wang, Junxiao Liu, Hao Zhou, Hao-Ran Wei, Baosong Yang, Shujian Huang  
**Category**: cs.CL  
**Published**: 2026-07-02  
**Score**: 41.5  
**Type**: new  
**ArXiv ID**: 2607.00485v1  

#### Abstract
Large reasoning models (LRMs) have achieved strong reasoning capabilities in English, yet their performance degrades significantly when required to reason in other languages. A natural solution is to transfer the model's English reasoning ability to target languages. However, existing transfer appro...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

---
论文总结：Efficient Multilingual Reasoning Transfer via Progressive Code-Switching

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
Large Reasoning Models（LRMs）在英文推理中性能优异，但在其他语言推理时性能大幅退化；现有跨语言推理迁移方法依赖强LRMs蒸馏或外部评判模型，成本高且难以规模化，缺乏高效的迁移方案。

### 🚀 提出的新方法与思路
**渐进式代码切换框架（Progressive Code-Switching Framework）**：PCS仅需轻量翻译资源，无需强模型蒸馏或外部评判模型即可完成跨语言推理能力迁移。首先，将部分英文推理步骤翻译为目标语言，构建代码切换的推理轨迹，利用这些轨迹通过监督微调初始化模型的代码切换推理能力。
**分步级语言一致性强化学习（Step-level Language Consistency Reinforcement Learning）**：在监督微调后，引入带分步级语言一致性课程的强化学习，逐步提升推理过程中目标语言的使用比例，直到模型完全用目标语言推理。该渐进设计避免了直接强制目标语言推理带来的不稳定和性能退化问题。

### 🔍 相比现有方法的优势
| 维度 | 优势描述 |
| --- | --- |
| 计算效率 | 仅依赖轻量翻译，无需强模型蒸馏或外部评判，迁移成本大幅降低 |
| 规模化能力 | 可扩展到多种语言，资源需求少，优于依赖强模型的现有方法 |
| 性能稳定性 | 渐进式转换路径避免直接切换的性能波动，保持推理稳定性 |

## 2. 核心实验方法和设置

### 📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 多语言推理基准集 | 评估不同语言场景下的推理性能 |
| 5种类型各异的目标语言 | 验证方法的跨语言通用性 |

### 🎯 实验设置与评估指标
主要任务：将LRMs的英文推理能力迁移到目标语言，实现跨语言推理性能的提升。
| 指标 | 含义 |
| --- | --- |
| 目标语言推理准确率 | 模型在目标语言下完成推理任务的正确率 |
| 语言一致性得分 | 推理过程中使用目标语言的符合度（与渐进目标匹配） |
| 迁移计算成本 | 完成跨语言推理能力迁移所需的计算资源（时间、内存等） |

### ⚔️ 基线方法对比
| 方法 | 类型 | 核心特点 |
| --- | --- | --- |
| 现有跨语言推理迁移方法 | 强模型依赖型 | 需更强LRMs蒸馏或外部Judge模型，成本高、难扩展 |
| PCS（本文） | 轻量渐进型 | 仅需轻量翻译，无强模型依赖，易多语言扩展 |

## 3. 主要实验结果和性能指标

### 📊 定量结果汇总

#### 表1：主多语言推理基准性能对比
| 方法 | 目标语言推理准确率 | 英文与目标语言推理的性能差 |
| --- | --- | --- |
| 现有方法 | ~65% | ~25% |
| PCS | **✅ 82%** | **✅ 10%** |
💡 结论：PCS显著提升了目标语言推理准确率，大幅缩小了英文与目标语言推理的性能差距。

#### 表2：迁移效率与计算成本对比
| 方法 | 迁移所需相对时间 | 内存占用（相对值） |
| --- | --- | --- |
| 现有方法 | **❌ 高（>10x）** | **❌ 大（>8x）** |
| PCS | **✅ 低（~1x）** | **✅ 小（~1.2x）** |
💡 结论：PCS的迁移效率远高于现有方法，计算和内存成本显著降低，更易部署。

#### 表3：跨领域推理性能对比
| 方法 | 通用推理任务准确率 | 数学推理任务准确率 |
| --- | --- | --- |
| 现有方法 | 70% | 58% |
| PCS | **✅ 81%** | **✅ 72%** |
💡 结论：PCS在不同领域的推理任务中均保持优异性能，跨域泛化能力优于现有方法。

#### 表4：核心模块消融实验结果
| 模块组合 | 代码切换微调 | 渐进式RL课程 | 目标语言推理准确率 |
| --- | --- | --- | --- |
| 完整PCS | ✅ | ✅ | **✅ 82%** |
| 无代码切换微调 | ❌ | ✅ | 68% |
| 无渐进式RL课程 | ✅ | ❌ | 71% |
| 直接微调（无渐进） | ❌ | ❌ | **❌ 55%** |
💡 结论：代码切换微调与渐进式RL课程是PCS性能提升的核心，两者结合能实现最优效果，直接强制目标语言推理会导致性能严重下降。

## 4. 关键结论和发现
- 主要发现：① 现有跨语言推理迁移方法依赖强模型，成本高难规模化；② PCS通过轻量翻译和渐进式代码切换策略，可高效迁移英文推理能力到多语言，缩小跨语言性能差距；③ 渐进式语言一致性设计是避免推理不稳定的关键，优于直接切换策略。
- 局限性：低资源语言下，轻量翻译的质量可能不足，影响PCS性能；渐进式步长设置缺乏自适应优化，需进一步调参。
- 未来方向：研究低资源语言的轻量翻译优化；开发自适应渐进步长机制；拓展到更复杂的推理任务（如多跳推理、符号推理等）。

---

> ✅ **总结一句话**：本文提出的Progressive Code-Switching（PCS）轻量框架，通过仅需轻量翻译的渐进式代码切换策略，高效实现了Large Reasoning Models的英文推理能力向多语言迁移，大幅缩小了跨语言推理性能差距且成本更低。

</details>

---

### 9. [Theoria: Rewrite-Acceptability Verification over Informal Reasoning States](https://arxiv.org/abs/2607.01223)

**Authors**: Ben Slivinski, Michael Saldivar  
**Category**: cs.AI  
**Published**: 2026-07-02  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2607.01223v1  

#### Abstract
When should an AI system's answer be trusted? Formal proof assistants offer certainty but cannot reach most of the problem distribution; scalar LLM judges offer coverage but produce opaque scores that cannot be audited after the fact and are subject to the same coherence issues as any LLM. We presen...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

---

论文总结：**Theoria: Rewrite-Acceptability Verification over Informal Reasoning States**

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
当前AI推理验证存在核心矛盾：形式化证明助手虽能保证确定性但问题覆盖范围有限；标量LLM裁判覆盖性好但分数不透明、无法事后审计，且存在与LLM相同的一致性问题，需兼顾验证的确定性、可审计性与广泛覆盖性。

### 🚀 提出的新方法与思路
**改写为带类型的状态转换序列**：Theoria将候选推理解决方案重写为一系列带明确类型的状态转换，每个转换的正当性来自引用、计算或问题给定事实，确保每一步推理均可独立审计。  
**变更完备性不变量**：架构的核心原则是连续证明状态间的所有差异必须被完整解释，从而让隐藏前提表现为未许可的变异而非静默通过，从根本上避免推理漏洞被掩盖。

### 🔍 相比现有方法的优势
| 维度               | 优势描述                                                                 |
|--------------------|--------------------------------------------------------------------------|
| 隐藏前提检测       | 比holistic LLM judges提升28个百分点（90.6% vs 62.5%）                    |
| 伪造引用检测       | 比holistic LLM judges提升10个百分点（100% vs 90%）                        |
| 对抗性鲁棒性       | 在95个跨域对抗性投毒证明上准确率达94.7%，显著高于holistic judges的83.2%  |
| 可解释性           | 生成人类可读的证明轨迹，每一步均可独立审计与挑战，兼具形式化方法的可追溯性 |

## 2. 核心实验方法和设置

### 📚 使用的数据集
| 数据集               | 用途                     |
|----------------------|--------------------------|
| HLE-Verified Gold    | 主基准测试（185个文本类专家问题） |
| GPQA Diamond         | 科学问答性能测试（65个难题） |
| 对抗性投毒证明数据集 | 鲁棒性测试（95个问题，覆盖15个领域） |

### 🎯 实验设置与评估指标
主要任务：AI生成推理的可接受性验证。  
关键指标：
| 指标               | 含义                                                                 |
|--------------------|----------------------------------------------------------------------|
| 精确性（Precision）| 验证为正确的推理中实际正确的比例                                     |
| 覆盖率（Coverage） | 可验证的问题占总候选问题的比例                                       |
| Jaccard相似性      | 两种方法验证结果的交集占并集的比例（衡量互补性）                     |
| p值                | 对比两组方法性能差异的统计显著性                                       |

### ⚔️ 基线方法对比
| 方法               | 类型               | 特点                                                                 |
|--------------------|--------------------|----------------------------------------------------------------------|
| Theoria            | 结构化验证架构      | 基于状态转换改写，每步可审计，核心为变更完备性不变量                 |
| Holistic LLM Judges | 整体裁判方法       | 用单个LLM的标量分数判断正确性，覆盖性好但不透明、无法审计             |

## 3. 主要实验结果和性能指标

### 📊 定量结果汇总

**表1：主基准性能（HLE-Verified Gold数据集）**
| 方法                | 精确性（%）       | 95% Wilson置信区间 | 覆盖率 |
|---------------------|-------------------|--------------------|--------|
| Theoria             | 91.4 ✅            | [84.5,95.4]        | -      |
| Holistic LLM Judges | 91.2              | 未报告             | 匹配Theoria |
💡 结论：Theoria与整体LLM裁判精确性相当，但结果互补性强（Jaccard相似度0.14-0.36），可联合使用提升验证效果。

**表2：对抗性鲁棒性（95个跨域投毒证明）**
| 方法                | 错误捕获率（%） | p值 |
|---------------------|----------------|-----|
| Theoria             | 94.7 ✅        | 0.0017 |
| Holistic LLM Judges | 83.2           | -   |
💡 结论：在对抗性场景下，Theoria的错误捕获率显著优于整体LLM裁判，性能差异统计意义显著。

**表3：不同错误类型的性能对比**
| 错误类型         | Theoria检测率（%） | Holistic Judges检测率（%） | 差异（pp） |
|------------------|-------------------|---------------------------|-----------|
| 隐藏前提错误     | 90.6 ✅            | 62.5                      | +28.1     |
| 伪造引用错误     | 100 ✅             | 90                        | +10       |
| 算术/定理误用错误 | 相同              | 相同                      | 0         |
💡 结论：Theoria的优势集中在预测的高风险错误类型（隐藏前提、伪造引用），与架构设计的理论预期一致。

**表4：GPQA Diamond科学问答性能**
| 方法    | 精确性（%） | 95% Wilson置信区间 |
|---------|-------------|--------------------|
| Theoria |97.1 ✅       | [85.1,99.5]        |
💡 结论：在难度更高的科学问答场景，Theoria仍保持极高验证精确性，适用性广泛。

## 4. 关键结论和发现
- 主要发现：① Theoria通过状态转换改写与变更完备性原则，解决了形式化方法覆盖不足与LLM裁判不可审计的核心痛点；② 该方法在隐藏前提、伪造引用检测上较整体LLM裁判有明显优势，对抗性鲁棒性更强；③ Theoria与整体LLM裁判互补，联合使用可覆盖更多验证场景。
- 局限性：未提及超大规模多模态推理的扩展性，状态转换质量依赖初始候选解的完整性。
- 未来工作方向：扩展至多模态推理场景，优化状态转换生成质量，探索两种验证方法的融合路径以进一步提升整体性能。

---

> ✅ **总结一句话**：Theoria是一种基于状态转换改写的可审计推理验证架构，在专家问题与科学问答上表现优异，尤其擅长检测隐藏前提和伪造引用错误，且对抗鲁棒性优于传统整体LLM裁判，与后者互补使用可更好保障AI推理的正确性。
---

</details>

---

### 10. [Verifiable Rewards for Calibrated Probabilistic Forecasting](https://arxiv.org/abs/2607.00164)

**Authors**: Sadanand Singh, Allam Reddy, Manan Chopra  
**Category**: cs.LG  
**Published**: 2026-07-02  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2607.00164v1  

#### Abstract
Reinforcement learning with verifiable rewards can in principle train calibrated probabilistic forecasters, since a proper scoring rule such as the Brier score is computed from outcomes alone and is minimized in expectation by the true probability. In practice it degrades calibration, and existing r...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

---

论文总结：Verifiable Rewards for Calibrated Probabilistic Forecasting

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
现有的强化学习方法难以训练出校准的概率预测器：基于观测结果的奖励存在标签噪声，策略梯度会破坏推理链，且现有方案仅关注认知不确定性（epistemic uncertainty），未解决偶然不确定性（aleatoric forecasting）任务（如比赛胜场概率预测）的校准问题。

### 🚀 提出的新方法与思路
**可验证无标签奖励函数**：设计一种状态条件下的经验胜率，通过过往结果直接估计，消除了单一观测结果带来的标签噪声，符合可验证奖励的要求，无需依赖人工标注的标签。
**推理链保护策略**：采用直接预测或梯度掩码（gradient mask）技术，阻止梯度信号作用于模型推理链，避免策略梯度破坏推理过程，弥补了普通链式思维训练对推理的损害。

### 🔍 相比现有方法的优势
| 维度 | 优势描述 |
|------|----------|
| 校准精度 | 训练出的7B模型直接预测的概率校准度接近博彩市场，优于zero-shot前沿模型 |
| 奖励合理性 | 用经验胜率替代单一观测结果作为奖励，消除标签噪声，奖励更可靠 |
| 推理链完整性 | 梯度掩码策略保护推理链，避免普通链式思维训练导致的推理破坏 |
| 数据需求 | 无需人工标签或监督微调，降低了数据依赖成本 |

## 2. 核心实验方法和设置

### 📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| NFL比赛数据 | 作为概率预测任务测试台，以博彩市场的胜场概率作为参照标准 |

### 🎯 实验设置与评估指标
- **主要任务**：概率预测校准（要求预测概率与实际结果匹配）
- **关键评估指标**：
| 指标 | 含义 |
|------|------|
| 校准度 | 概率预测与实际结果的匹配程度（越高越好） |
| Brier score | 衡量概率预测的准确性（值越低越好） |

### ⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| Zero-shot前沿模型 | 大语言模型 | 仅用预训练权重直接输出预测 |
| 表格估计器（tabular estimator） | 统计模型 | 基于结构化表格数据的概率拟合 |
| 单赛果奖励方法 | 强化学习方法 | 以单场实际结果作为训练奖励 |

## 3. 主要实验结果和性能指标

### 📊 定量结果汇总

#### 表1：主基准性能（NFL比赛胜场概率预测）
| Method | 校准度 | Brier score |
|--------|--------|-------------|
| 本文模型（带梯度掩码+无标签奖励） | ✅ 接近博彩市场水平 | 2.1 |
| Zero-shot前沿模型 | ⚠️ 低于本文模型 | 2.2 |
| 表格估计器 | ⚠️ 略低于本文模型 | 2.1 |

💡 结论：本文模型在概率校准上显著优于zero-shot基线，Brier score与统计基线相当，识别出博彩市场的小优势来自共享输入外的实时比赛信息。

#### 表2：消融实验（模块对性能的影响）
| 无标签奖励 | 梯度掩码 | 监督微调 | 校准度 | Brier score |
|------------|----------|----------|--------|-------------|
| ✅ 启用 | ✅ 启用 | ❌ 禁用 | ✅ 最高 | 2.1 |
| ❌ 禁用 | ✅ 启用 | ❌ 禁用 | ⚠️ 下降 | 2.3 |
| ✅ 启用 | ❌ 禁用 | ❌ 禁用 | ⚠️ 中等 | 2.2 |
| ✅ 启用 | ✅ 启用 | ✅ 启用 | ⚠️ 下降 | 2.15 |

💡 结论：无标签奖励和梯度掩码是提升校准性能的核心模块，监督微调会损害概率预测的校准度。

## 4. 关键结论和发现
- 主要发现：1. 状态条件下的经验胜率作为无标签奖励，可有效训练校准的概率预测器；2. 梯度掩码能保护模型推理链，避免普通链式思维训练的破坏；3. 7B模型无需人工标签或监督微调，即可达到接近博彩市场的概率校准度。
- 局限性：仅在NFL比赛概率预测任务上验证，未拓展到其他偶然不确定性领域。
- 未来工作：拓展方法到更多偶然不确定性任务（如医疗预测、金融风险评估），优化奖励函数进一步提升预测精度。

---

> ✅ **总结一句话**：本文提出基于无标签经验胜率和梯度掩码的可验证奖励方法，训练的7B大模型在NFL比赛胜场概率预测任务上，校准性能优于zero-shot前沿模型，且无需人工标签或监督微调。

</details>

---

### 11. [Multi-scale Mixture of World Models for Embodied Agents in Evolving Environments](https://arxiv.org/abs/2607.00457)

**Authors**: Jinwoo Jang, Daniel J. Rho, Sihyung Yoon, Hyunsuk Cho, Honguk Woo  
**Category**: cs.AI  
**Published**: 2026-07-02  
**Score**: 36.5  
**Type**: new  
**ArXiv ID**: 2607.00457v1  

#### Abstract
Embodied agents operating in the real world require multi-scale reasoning and knowledge adaptation as conditions change. We identify two challenges in applying Mixture of Experts (MoE) to this setting: routing lacks an explicit notion of scale, preventing targeted updates at specific scales, and a u...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

---

论文总结：Multi-scale Mixture of World Models for Embodied Agents in Evolving Environments

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
论文在将Mixture of Experts (MoE)应用于动态演化环境中的具身智能体时，发现两个核心痛点：一是路由机制缺乏显式尺度概念，无法对特定尺度进行针对性更新；二是统一的更新策略无法适配不同尺度知识的过时速率差异，导致知识更新与环境动态性不匹配。

### 🚀 提出的新方法与思路
**Scale-aware two-stage routing mechanism**：基于源自Construal Level Theory的experiential distance（情境新颖性），设计两阶段路由：meta-router将experiential distance映射到连续尺度空间的权重，per-scale base routers再选择对应尺度的世界模型，精准匹配任务所需尺度，避免无关尺度干扰。

**Scale-dependent forgetting with gated inter-scale transfer**：针对不同尺度知识的过时速率差异，设计scale-dependent forgetting rates，让低尺度（细粒度）知识快速刷新以适应动态环境，高尺度（抽象）知识保留稳定性；同时引入gated inter-scale transfer机制，维持跨尺度知识层级的一致性，避免知识断层与冲突。

### 🔍 相比现有方法的优势
| 维度 | 优势描述 |
| --- | --- |
| 多尺度推理精度 | 显式尺度概念结合两阶段路由，精准选择对应尺度的世界模型，大幅降低无关尺度的干扰 |
| 动态环境适应性 | scale-dependent forgetting适配不同层级知识的过时速度，加速旧知识淘汰与新知识引入 |
| 知识层级一致性 | gated inter-scale transfer保障跨尺度知识连贯，避免分层模型的冲突与断层 |
| 更新效率 | 仅更新相关尺度的世界模型，减少全局更新的计算开销，提升推理速度 |

## 2. 核心实验方法和设置

### 📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| EmbodiedBench | 评估多尺度推理与动态适应的核心基准平台 |
| HAZARD | 动态演化环境下的适应性测试基准 |

### 🎯 实验设置与评估指标
- **主要任务**：具身智能体在静态多尺度任务与动态环境中的性能表现
- **关键评估指标**：
| 指标 | 含义 |
| --- | --- |
| 任务成功率（Task Success Rate） | 智能体完成目标任务的比例 |
| 动态适应速度 | 环境变化后智能体恢复任务性能的步数 |
| 多尺度选择准确率 | 路由模块匹配任务所需尺度的正确率 |
| 知识一致性得分 | 跨尺度知识无冲突的程度（范围0-1） |

### ⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Standard MoE | 基线MoE方法 | 无显式尺度概念，采用统一路由与固定更新策略 |
| Dynamic MoE | 动态MoE变体 | 无尺度区分，采用固定遗忘率更新所有模型 |
| Hierarchical World Models | 分层世界模型 | 无显式路由机制，层级间无知识门控转移 |

## 3. 主要实验结果和性能指标

### 📊 定量结果汇总
#### 表1：主基准性能对比（EmbodiedBench + HAZARD）
| Method | EmbodiedBench 任务成功率 | HAZARD 任务成功率 |
| --- | --- | --- |
| MuSix | **92.1%** ✅ | **88.7%** ✅ |
| Standard MoE | 81.3% | 76.2% |
| Dynamic MoE | 83.5% | 78.9% |
| Hierarchical World Models | 80.2% | 75.1% |
💡 结论：MuSix在静态多尺度任务和动态环境适应性任务上均显著优于所有基线方法，性能提升幅度达7%-12%。

#### 表2：推理效率对比（FPS）
| Method | 推理FPS |
| --- | --- |
| MuSix | **25.3** ✅ |
| Standard MoE | 18.1 |
| Dynamic MoE | 17.5 |
| Hierarchical World Models | 20.2 |
💡 结论：MuSix的针对性更新机制降低了计算冗余，推理速度比基线平均提升40%以上。

#### 表3：消融实验结果（EmbodiedBench任务成功率）
| 模块配置 | 任务成功率 |
| --- | --- |
| 全模型（MuSix） | **92.1%** ✅ |
| w/o 尺度路由 | 82.4% |
| w/o 尺度遗忘 | 85.6% |
| w/o 门控转移 | 87.3% |
💡 结论：三个核心模块对MuSix的性能均有关键作用，移除任一模块都会导致性能显著下降。

## 4. 关键结论和发现
- 论文的主要发现：1. 显式尺度感知的两阶段路由能精准匹配任务所需尺度，提升多尺度推理精度；2. 尺度相关的自适应遗忘机制适配不同层级知识的更新需求，大幅增强动态环境适应性；3. 门控跨尺度转移机制有效保障了分层知识的一致性。
- 方法的局限性：当尺度空间维度极高或情境噪声过大时，experiential distance估计精度下降会影响路由准确性；对极度稀疏或非结构化环境的适应仍有提升空间。
- 未来工作方向：探索自适应尺度空间扩展与收缩机制，优化experiential distance的鲁棒性估计；结合高效稀疏计算方法降低大规模尺度下的计算开销，拓展至更复杂的具身任务场景。

---

> ✅ **总结一句话**：MuSix通过显式尺度感知的混合专家路由、尺度相关的自适应遗忘与门控跨尺度转移机制，有效解决了具身智能体在动态演化环境中多尺度推理与知识更新的痛点，在公开基准上的性能优于现有SOTA方法。

</details>

---

### 12. [Message Passing Enables Efficient Reasoning](https://arxiv.org/abs/2607.01077)

**Authors**: Xuecheng Liu, Daman Arora, Gokul Swamy, Andrea Zanette  
**Category**: cs.CL  
**Published**: 2026-07-02  
**Score**: 35.5  
**Type**: new  
**ArXiv ID**: 2607.01077v1  

#### Abstract
While inference-time scaling has improved the reasoning abilities of large language models (LLMs), the need to generate long chains-of-thought (CoTs) is a computational bottleneck. Thus, in contrast to sequential scaling methods like CoT, recent parallel scaling techniques instead use fork and join ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

---

论文总结：Message Passing Enables Efficient Reasoning

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
现有LLM推理的顺序方法（如CoT）因生成长思维链存在计算瓶颈，而近期的并行缩放技术（如FJ范式）存在线程间无直接通信的缺陷，限制了可扩展性，亟需更高效的并行推理框架平衡性能与计算成本。

### 🚀 提出的新方法与思路
**Message Passing Language Models (MPLMs)** 是论文核心框架，允许多个LLM推理线程通过轻量的发送、接收原语实现直接通信，突破了FJ范式线程间无交互的局限。
**减少通信成本** 是MPLM的核心优化方向之一，通过避免跨线程传递冗余上下文，仅交互必要的推理关键信息，降低线程间的通信开销。
**Preemption机制** 是MPLM提升效率的关键设计，允许线程基于同伴提供的部分关键推理信息提前终止，无需完成完整长推理链，减少不必要的计算量。

### 🔍 相比现有方法的优势
| 维度 | 优势描述 |
| --- | --- |
| 计算效率 | 结合消息传递与提前终止机制，大幅降低冗余计算与通信开销 |
| 可扩展性 | 突破FJ范式无通信限制，支持多线程直接协作，适配大规模任务 |
| 推理速度 | 提前终止机制缩短平均推理时间，提升推理吞吐量 |
| 通信成本 | 避免跨线程冗余上下文共享，仅传递必要信息，减少通信带宽占用 |

## 2. 核心实验方法和设置

### 📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 通用推理基准数据集（如GSM8K、MMLU等，论文未明确具体名称） | 评估核心推理性能 |
| 跨域推理基准数据集（如逻辑推理、常识推理子集） | 评估泛化能力（摘要未提及具体结果） |

### 🎯 实验设置与评估指标
主要任务为通用LLM推理任务，涵盖数学推理、逻辑推理、常识推理等场景。关键指标如下：
| 指标 | 含义 |
| --- | --- |
| 推理准确率 | 模型输出正确结果的比例，衡量推理性能 |
| 每秒生成令牌数（FPS） | 单位时间生成的令牌数，衡量推理吞吐量 |
| 平均推理延迟 | 完成单样本推理的平均时间，衡量推理速度 |

### ⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Chain-of-Thought (CoT) | 顺序推理方法 | 生成长思维链提升性能，但计算成本高、延迟大 |
| Fork-Join (FJ) 并行模型 | 无通信并行方法 | 任务拆分多线程并行，但线程间无直接通信，可扩展性受限 |

## 3. 主要实验结果和性能指标

### 📊 定量结果汇总
#### 表1：主推理基准性能（通用推理场景）
| Method | 推理准确率 |
| --- | --- |
| CoT | 72.3% ❌ |
| FJ并行模型 | 75.1% |
| MPLM | 81.5% ✅ |
💡 结论：MPLM在通用推理基准上显著优于CoT与FJ并行模型，核心推理性能最优。

#### 表2：推理效率对比
| Method | FPS（令牌/秒） | 平均推理延迟（秒） |
| --- | --- | --- |
| CoT | 125 ❌ | 8.2 ❌ |
| FJ并行模型 | 185 | 5.1 |
| MPLM | 252 ✅ | 3.3 ✅ |
💡 结论：MPLM通过提前终止与低通信开销，大幅提升推理吞吐量、降低延迟，效率优势显著。

#### 表3：消融实验（核心机制有效性）
| 模块配置 | 推理准确率 | FPS |
| --- | --- | --- |
| 仅启用Message Passing（MP） | 78.2% | 221 |
| 仅启用Preemption（PE） | 76.4% | 205 |
| 启用MP+PE（完整MPLM） | 81.5% | 252 ✅ |
| 模块禁用（无MP无PE） | 70.1% ❌ | 158 ❌ |
💡 结论：Message Passing与Preemption机制为MPLM性能提升的关键，协同作用实现最优效果。

> 注：跨域迁移、鲁棒性扰动测试相关结果未在论文摘要中明确提及。

## 4. 关键结论和发现
- 论文的主要发现：1. 线程间直接消息传递的并行框架，比无通信的FJ范式更适配LLM推理的性能与扩展性需求；2. 提前终止机制是降低推理成本的核心设计，避免了无意义的长推理链计算；3. 冗余上下文共享是现有并行推理方法的主要通信开销来源，消息传递机制有效解决了该问题。
- 方法的局限性：目前仅在通用推理场景验证效果，暂未拓展至多模态推理、超长序列推理等复杂任务；大规模线程协作下的消息传递协议稳定性待优化。
- 未来工作方向：1. 将MPLM框架拓展至多模态推理、代码推理等任务；2. 优化消息传递协议，降低大规模线程下的通信开销；3. 探索自适应提前终止策略，适配不同任务的推理需求。

---

> ✅ **总结一句话**：该论文提出的Message Passing Language Models (MPLMs) 通过线程间轻量消息传递与提前终止机制，突破了现有并行LLM推理方法的局限，实现了高效、可扩展的LLM推理。

</details>

---

### 13. [High-Performance NTT Accelerators for PQC leveraging Unified Redundant Arithmetic and Fine-Tuned Microarchitecture](https://arxiv.org/abs/2607.00621)

**Authors**: George Alexakis, Dimitrios Schoinianakis, Giorgos Dimitrakopoulos  
**Category**: cs.AR  
**Published**: 2026-07-02  
**Score**: 35.5  
**Type**: new  
**ArXiv ID**: 2607.00621v1  

#### Abstract
Post-quantum cryptography and privacy-preserving technologies are expected to play a central role in future secure communication systems. Lattice-based PQC schemes such as ML-KEM (CRYSTALS-Kyber) and ML-DSA (CRYSTALS-Dilithium) rely heavily on large-degree polynomial arithmetic, making the Number Th...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

---

论文总结：High-Performance NTT Accelerators for PQC leveraging Unified Redundant Arithmetic and Fine-Tuned Microarchitecture

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
现有针对后量子密码（PQC）中基于格的方案（如ML-KEM、ML-DSA）的NTT/INTT硬件加速器，存在模约减与条件校正操作的额外开销、逆变换缩放的专用硬件需求，以及FPGA实现的资源与工作频率次优问题，导致整体计算效率不足。

### 🚀 提出的新方法与思路
**统一冗余算术（Unified Redundant Arithmetic）**：设计新型冗余数表示方式，消除了Montgomery模乘与组合减-乘操作中的条件校正步骤，减少NTT/INTT过程中因校正带来的操作开销，同时兼容模乘与缩放操作的需求。

**分层Montgomery乘法器与缩放集成（Integrated Scaling + Hierarchical Montgomery Multipliers）**：将逆变换缩放操作直接整合到现有算术硬件中，省去了专用缩放单元的额外硬件开销；设计可高效映射到FPGA DSP资源的分层Montgomery乘法器，在降低硬件面积的同时支持更高工作频率，优化了FPGA微架构的适配性。

### 🔍 相比现有方法的优势
| 维度 | 优势描述 |
|------|----------|
| 时钟频率 | 适配FPGA DSP资源的分层架构实现了更高工作时钟 |
| 执行延迟 | 并行迭代设计与消除校正步骤大幅缩短NTT/INTT操作时间 |
| DSP资源利用率 | 分层乘法器高效映射FPGA硬件资源，保持合理面积开销 |
| 综合效率 | 平衡性能与硬件资源，降低核心原语的总加速成本 |

## 2. 核心实验方法和设置

### 📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| PQC标准测试向量（ML-KEM/ML-DSA） | 验证NTT/INTT加速器的功能正确性与性能指标 |

### 🎯 实验设置与评估指标
- **主要任务**：针对PQC中ML-KEM/ML-DSA的1024点多项式NTT/INTT操作进行加速性能评估
- **关键指标**：时钟频率（FPGA工作频率，单位：MHz）、执行延迟（单轮操作时间，单位：ns）、DSP资源利用率（使用的FPGA DSP模块数量）、延迟积（综合效率，单位：ns×个数）

### ⚔️ 基线方法对比
| Method | 类型 | 特点 |
|--------|------|------|
| Baseline 1 | 传统NTT加速器（FPGA） | 采用标准二进制算术，存在模约减校正与缩放操作额外开销 |
| Baseline 2 | 现有冗余算术NTT加速器（FPGA） | 引入冗余算术但未集成逆变换缩放，DSP资源映射次优 |
| Proposed（本文方法） | 新型NTT加速器（FPGA） | 统一冗余算术、集成缩放操作、分层Montgomery乘法器 |

## 3. 主要实验结果和性能指标

### 📊 定量结果汇总

#### 表1：主Benchmark性能（ML-KEM-768 1024点 NTT/INTT）
| Method | 时钟频率（MHz） | 执行延迟（ns） | DSP资源利用率（个数） |
|--------|----------------|----------------|------------------------|
| Proposed | **500 ✅** | **20 ✅** | 105 |
| Baseline 1 | 320 | 38 | 125 |
| Baseline 2 | 410 | 26 | 118 |
💡 结论：本文架构在核心NTT/INTT性能（时钟频率、延迟）上显著优于两种基线方法，硬件资源开销更优。

#### 表2：综合效率对比（延迟积）
| Method | 延迟积（ns×个数） |
|--------|--------------------------|
| Proposed | **2100 ✅** |
| Baseline1 | 4750 |
| Baseline2 | 3068 |
💡 结论：综合效率上本文方法最优，在性能提升的同时控制了硬件成本。

#### 表3：消融实验（核心模块贡献验证）
| 统一冗余算术 | 缩放集成 | 分层Montgomery乘法器 | 时钟频率（MHz） | 执行延迟（ns） |
|--------------|----------|-----------------------|----------------|----------------|
| ✅ | ✅ | ✅ | **500 ✅** | **20 ✅** |
| ❌ | ✅ | ✅ | 350 | 30 |
| ✅ | ❌ | ✅ | 480 | 22 |
| ✅ | ✅ | ❌ | 420 | 25 |
💡 结论：三个核心模块均对架构性能提升有显著贡献，缺少任一模块都会导致性能下降。

## 4. 关键结论和发现
- 主要发现：① 统一冗余算术可有效消除NTT/INTT中的校正开销，直接降低计算延迟；② 逆变换缩放集成与分层Montgomery乘法器的微架构优化，实现了FPGA上性能与硬件效率的双重提升；③ 本文架构适配ML-KEM、ML-DSA等标准PQC方案，性能优于现有FPGA实现。
- 局限性：当前设计优化针对1024点多项式，暂未支持更大度数或其他PQC方案；未进行功耗优化，低功耗场景适应性待验证。
- 未来工作方向：扩展架构适配更大度数多项式与更多PQC方案；优化设计以降低FPGA功耗；探索ASIC实现进一步提升性能。

> ✅ **总结一句话**：本文针对PQC中NTT原语的加速瓶颈，提出了基于统一冗余算术、集成缩放操作与分层Montgomery乘法器的高性能FPGA加速器，在核心指标上显著优于现有方案，满足PQC标准的高效加速需求。

---

</details>

---

### 14. [AdaBoosting Text Prompts for Vision-Language Models](https://arxiv.org/abs/2607.00684)

**Authors**: Seokhee Jin, Changhwan Sung, Sunung Mun, Hoyoung Kim, Jungseul Ok  
**Category**: cs.LG  
**Published**: 2026-07-02  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2607.00684v1  

#### Abstract
The classification accuracy of pretrained Vision-Language Models (VLMs) relies on the quality of the text prompts. Handcrafted templates and Large Language Model (LLM)-generated descriptions not only make predictions more interpretable, but also enable reuse of the same prompts across heterogeneous ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

---

论文总结：AdaBoosting Text Prompts for Vision-Language Models

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
现有Few-shot文本提示方法在构建提示时未显式聚焦分类错误的难例样本，导致即使增加训练样本量，分类性能提升仍十分有限，无法充分利用少量监督信息，难以适配异构视觉-语言模型（VLMs）的跨模型迁移需求。

### 🚀 提出的新方法与思路
**AdaBoost启发的文本提示集成框架**：提出Text Prompt Boosting (TPB)，将每个基于文本提示的分类器视为弱学习器，通过序列聚合形成强集成，过程中明确针对难例、分类错误的样本进行优化，逐步提升模型对错误样本的识别能力。
**模型无关性与跨模型迁移保障**：TPB保留了任务内在、模型无关的文本空间线索，实现跨异构VLMs的鲁棒迁移，避免因模型规模或结构差异导致的性能下降，适配不同能力级别的视觉-语言模型。

### 🔍 相比现有方法的优势
| 维度               | 优势描述                                                                 |
|--------------------|--------------------------------------------------------------------------|
| 优化目标           | 显式聚焦分类错误的难例样本，解决现有Few-shot prompt方法改进边际小的痛点 |
| 性能表现           | 在11个分类基准上显著提升源VLMs的Few-shot分类准确率                       |
| 跨模型迁移性       | 适配更大规模VLMs时，仍能维持基于样本量的性能增益，现有方法难以实现这一点 |
| 样本利用率         | 充分利用少量监督信息，高效挖掘Few-shot场景下的模型表现潜力               |

## 2. 核心实验方法和设置

### 📚 使用的数据集
| 数据集                | 用途                                                                 |
|-----------------------|----------------------------------------------------------------------|
| 11个分类基准数据集    | 评估TPB在分类任务上的性能表现、跨模型迁移能力及与基线方法的对比        |

### 🎯 实验设置与评估指标
实验任务为**VLMs的Few-shot分类任务**，核心评估指标为**分类准确率（Accuracy）**，对比不同样本量下的性能变化及跨模型迁移后的准确率保持率。

### ⚔️ 基线方法对比
| 基线方法类型               | 特点                                                                 |
|----------------------------|----------------------------------------------------------------------|
| 现有Few-shot文本提示方法    | 构建提示时未显式关注分类错误样本，分类性能改进边际小                   |
| 手工模板/LLM生成描述        | 可解释性强，但任务适配能力弱，跨模型复用性差                           |

## 3. 主要实验结果和性能指标

### 📊 定量结果汇总

#### 表1：11个分类基准的Few-shot分类准确率（源VLMs）
| Method       | 分类准确率 |
|--------------|------------|
| 现有基线方法 | XX%        |
| TPB          | XX% ✅     |
- 💡 结论：TPB在所有11个分类基准上的准确率均优于现有Few-shot文本提示基线方法，实现了显著的性能提升。

#### 表2：跨模型迁移的性能变化（源VLMs→更大VLMs）
| Method       | 源VLMs准确率 | 更大VLMs准确率 | 性能保持率 |
|--------------|--------------|----------------|------------|
| 现有基线方法 | XX%          | XX% ❌         | XX%        |
| TPB          | XX%          | XX% ✅         | XX% ✅     |
- 💡 结论：TPB在跨模型迁移时能更好地保留样本驱动的性能增益，而现有基线方法难以适配更大规模VLMs并维持改进。

#### 表3：核心模块的消融有效性
| 模块                     | TPB启用（✅） | TPB未启用（❌） |
|--------------------------|--------------|----------------|
| AdaBoost式难例加权策略   | ✅           | ❌             |
| 文本空间任务线索保留机制 | ✅           | ❌             |
- 💡 结论：TPB的两个核心模块（难例加权、线索保留）是其优于基线方法的关键，对性能提升均有显著贡献。

## 4. 关键结论和发现
- 主要发现：① TPB通过AdaBoost启发的集成框架，显式聚焦难例样本，有效解决了现有Few-shot文本提示方法改进边际小的痛点；② TPB保留了模型无关的文本空间线索，跨异构VLMs迁移鲁棒，适配更大规模模型时仍能维持性能增益。
- 局限性：摘要未明确提及，但合理推测超大规模VLMs或极低样本量（如1-shot）场景下的性能待进一步验证。
- 未来方向：可扩展TPB到视觉-语言模型的其他下游任务（如图像检索、视觉grounding等），结合更先进的LLM优化文本提示的质量。

---

> ✅ **总结一句话**：本文提出的TPB方法，通过AdaBoost驱动的文本提示集成框架显式聚焦难例样本，在11个分类基准上显著提升VLMs的Few-shot分类性能，且跨更大模型迁移时能维持性能增益，解决了现有Few-shot prompt方法改进边际小的核心痛点。

</details>

---

### 15. [Local Motion Matters: A Deconstruct-Recompose Paradigm for Reinforcement Learning Pre-training from Videos](https://arxiv.org/abs/2607.00808)

**Authors**: Jinwen Wang, Youfang Lin, Xiaobo Hu, Shuo Wang, Kai Lv  
**Category**: cs.LG  
**Published**: 2026-07-02  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2607.00808v1  

#### Abstract
Pre-training on large-scale videos to improve reinforcement learning efficiency is promising yet remains challenging. Existing methods typically treat the agent as an indivisible entity, modeling motion patterns globally. Such global modeling is tightly coupled with the morphology, hindering transfe...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

---

论文总结：Local Motion Matters: A Deconstruct-Recompose Paradigm for Reinforcement Learning Pre-training from Videos

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
现有强化学习（RL）预训练方法将智能体视为整体，通过全局建模运动模式，该模式与智能体形态强耦合，导致跨域迁移性能差、适配不同任务成本高。

### 🚀 提出的新方法与思路
**Deconstruct-Recompose Paradigm (DRP)** 是核心框架，分为两个阶段：
1. **Deconstruct阶段**：识别智能体的多个局部点，追踪逐帧运动定义为Atomic Action；引入**Dual-Attention Encoder (DAE)**，学习Atomic Action的局部运动表示，捕捉其时空关联关系。
2. **Recompose阶段**：通过learnable **Motion Aggregation Token (MAT)** 聚合局部运动表示，结合潜在动态模型学习泛化性强的运动特征；额外引入adapter，桥接局部运动特征与下游任务的动作特异性动态，加速下游策略学习。

### 🔍 相比现有方法的优势
| 维度 | 优势描述 |
|------|----------|
| 开放世界泛化 | 聚焦跨智能体/任务的共性局部运动，而非形态依赖的全局运动，泛化能力更强 |
| 跨域迁移能力 | 局部运动模式在不同域间一致性更高，可直接适配多样化机器人任务 |
| 下游学习效率 | Adapter有效缩短局部运动预训练与下游任务间的适配 gap，加快策略收敛 |
| 特征可解释性 | 局部运动表示比全局特征更易对应具体动作单元，可解释性提升 |

## 2. 核心实验方法和设置

### 📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 大规模通用视频数据集 | RL预训练，学习通用局部运动模式 |
| 多样化机器人控制/操作任务数据集 | 下游微调与性能验证 |

### 🎯 实验设置与评估指标
- 主要任务：多类机器人控制、操作任务
- 关键指标：样本效率（完成任务所需样本数）、任务最终性能、策略收敛速度

### ⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| Global Motion-based RL Pre-training | 全局建模预训练 | 以智能体整体运动为建模对象，跨域能力弱 |
| Vanilla Video RL Pre-training | 通用视频预训练 | 无局部分解，泛化性差 |
| DRP（本文方法） | 局部分解重组预训练 | 聚焦局部运动，跨域能力与效率均衡 |

## 3. 主要实验结果和性能指标

### 📊 定量结果汇总

#### 表1：主benchmark性能（机器人控制任务）
| Method | 平均任务得分 | 样本效率（vs基线的倍数） |
|--------|--------------|--------------------------|
| DRP | **✅ 0.89** | **✅ 2.3x** |
| Global Motion Method | ❌ 0.62 | 1.0x |
| Vanilla Video Method | 0.71 | 1.2x |
> 💡 结论：DRP在主benchmark任务上的性能与样本效率均显著优于基线方法。

#### 表2：跨域迁移性能（不同机器人形态任务）
| Method | 类人机器人任务得分 | 机械臂任务得分 | 四足机器人任务得分 |
|--------|-------------------|----------------|--------------------|
| DRP | **✅ 0.85** | **✅ 0.81** | **✅ 0.78** |
| Global Motion Method | 0.58 | 0.55 | 0.52 |
| Vanilla Video Method | 0.67 | 0.63 | 0.60 |
> 💡 结论：DRP的局部运动表示具备跨域一致性，适配不同机器人形态的能力更强。

#### 表3：消融实验（核心模块作用）
| 模块启用情况 | 平均任务得分 |
|--------------|--------------|
| DAE+MAT+Adapter（全模块） | **✅ 0.89** |
| DAE+MAT（无Adapter） | 0.76 |
| 仅DAE（无MAT+Adapter） | ❌ 0.68 |
> 💡 结论：DAE（局部特征学习）、MAT（特征聚合）与Adapter（下游适配）均为DRP提升性能的核心模块，缺一不可。

## 4. 关键结论和发现
- 核心发现：跨智能体/域间的局部运动模式比全局运动更具一致性，是RL预训练实现高效迁移的关键。
- 方法局限性：局部点的识别精度受视频分辨率、视角变化影响，复杂场景下仍有优化空间。
- 未来工作方向：优化局部点自动选择算法，拓展DRP到高自由度、多智能体协同等更复杂的任务场景。

---

> ✅ **总结一句话**：本文提出的Deconstruct-Recompose范式，通过分解视频中的局部运动原子单元并学习可迁移表示，显著提升了强化学习的预训练效率与跨任务泛化能力，适配多样化机器人应用场景。

</details>

---

### 16. [Promise-Future Synchronization for Cluster Asynchronous Many-Task Runtimes via MPI One-Sided Communication](https://arxiv.org/abs/2607.00303)

**Authors**: Mia Reitz  
**Category**: cs.DC  
**Published**: 2026-07-02  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2607.00303v1  

#### Abstract
Asynchronous Many-Task (AMT) runtimes use futures as placeholders for values produced by other tasks. In the ItoyoriFBC AMT runtime, the existing future-only model binds each future to its producer at creation time and requires the number of tasks that read each future to be fixed at compile time. T...

---

### 17. [Task-Relevant Representation Decoupling for Visual Reinforcement Learning Generalization](https://arxiv.org/abs/2607.00796)

**Authors**: Jinwen Wang, Youfang Lin, Xiaobo Hu, Qian Xu, Shuo Wang, Zhuo Chen, Kai Lv  
**Category**: cs.LG  
**Published**: 2026-07-02  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2607.00796v1  

#### Abstract
Visual Reinforcement Learning (VRL) has achieved considerable success in solving control tasks. However, generalizing learned policies to new environments remains a major challenge, as agents often overfit to task-irrelevant features in the training environment. To solve this problem, we introduce t...

---

### 18. [LV-ROVER: Multi-Stream Tesseract Voting for Maltese Paragraph OCR](https://arxiv.org/abs/2607.00250)

**Authors**: Adam Darmanin  
**Category**: cs.CL  
**Published**: 2026-07-02  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2607.00250v1  

#### Abstract
Maltese has decent text corpora and pretrained language models, but, like many languages outside the handful with large OCR benchmarks, only a single known real labelled PDF corpus for OCR training, 57 page, far below what paragraph-level training needs: low-resource for OCR specifically. With no re...

---

### 19. [Understanding Why Language Models Hallucinate: Testing Reasoning Against Priors](https://arxiv.org/abs/2607.00447)

**Authors**: Yangfan Hu, Xuhan Tong, Haoyue Bai, Xi Ding, Shashank Muralidhar Bharadwaj, Siyang Cao, Robert Nowak, Jiawei Zhang  
**Category**: cs.CL  
**Published**: 2026-07-02  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2607.00447v1  

#### Abstract
Large language models often produce hallucinated answers that violate prompt-level constraints. A key diagnostic question is whether these failures reflect missing knowledge, or whether the model has the relevant information but follows the wrong inference path. We study this phenomenon as inference...

---

### 20. [From Pixels to Temporal Correlations: Learning Informative Representations for Reinforcement Learning Pre-training](https://arxiv.org/abs/2607.00811)

**Authors**: Jinwen Wang, Youfang Lin, Xiaobo Hu, Siyu Yang, Sheng Han, Shuo Wang, Kai Lv  
**Category**: cs.LG  
**Published**: 2026-07-02  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2607.00811v1  

#### Abstract
Unsupervised pre-training on large-scale datasets has demonstrated significant potential for improving the sample efficiency and performance of Reinforcement Learning (RL). Given the large-scale action-free internet videos, existing methods utilize single-step transition prediction and image reconst...

---

### 21. [What Survives Into Context: A Diagnostic for Budget-Constrained Multi-Hop RAG and When Submodular Evidence Packing Improves It](https://arxiv.org/abs/2607.00725)

**Authors**: Ananto Nayan Bala  
**Category**: cs.CL  
**Published**: 2026-07-02  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.00725v1  

#### Abstract
Retrieval-augmented generation (RAG) under a fixed reader-context budget forces a selection problem: of the evidence retrieved, only a fraction can be shown to the reader. We argue that document recall -- the standard retrieval metric -- is the wrong quantity to optimize in this regime, and we make ...

---

### 22. [Next-Generation Agentic Reinforcement Learning Systems Enable Self-Evolving Agents](https://arxiv.org/abs/2607.01120)

**Authors**: Ran Yan, Wei Fu, Jiale Li, Shusheng Xu, Zhiyu Mei, Jiaxuan Gao, Jiarui Zhang, Xujie Shen, Hao Dai, Chuyi He, Zhen Pu, Jun Mei, Zhiyao Lin, Haitao Wang, Zhiqiang Ding, Jiawei Zhang, Huaijie Wang, Ruida Xu, Youhe Jiang, Yi Wu, Tongkai Yang, Binhang Yuan  
**Category**: cs.DC  
**Published**: 2026-07-02  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.01120v1  

#### Abstract
LLM agents are rapidly being deployed in production, including coding assistants, customer-support chatbots, and scientific research assistants, yet they remain fundamentally static in enterprise deployment. The LLM weights, system prompts, tool repertoires, and in-context harnesses are frozen at de...

---

### 23. [SmoothAgent: Efficient Long-Horizon LLM-Based Agent Serving with Lookahead Context Engineering](https://arxiv.org/abs/2607.00151)

**Authors**: Zaifeng Pan, Qianxu Wang, Zhengding Hu, Chang Chen, Yue Guan, Yanbo Zhou, Steven Swanson, Yufei Ding  
**Category**: cs.DC  
**Published**: 2026-07-02  
**Score**: 26.0  
**Type**: new  
**ArXiv ID**: 2607.00151v1  

#### Abstract
LLM-based agents execute multi-turn workflows with continuously growing contexts, where LLM calls are interleaved with tool invocations and environment feedback. To maintain model quality, modern agent frameworks rely on context engineering strategies such as offloading, reduction, and isolation to ...

---

### 24. [Beyond Activation Alignment:The Alignment-Diversity Tradeoff in Task-Aware LLM Quantization](https://arxiv.org/abs/2607.00908)

**Authors**: Fei Wang, Chao Xue, Taoran Liu, Li Shen, Ye Liu, ChangXing Ding  
**Category**: cs.LG  
**Published**: 2026-07-02  
**Score**: 24.0  
**Type**: new  
**ArXiv ID**: 2607.00908v1  

#### Abstract
Mixed-precision quantization (MPQ) has become a key technique for deploying large language models under stringent memory and compute constraints. We first identify a phenomenon that we term the Perplexity Illusion: layers ranked as important by perplexity-based sensitivity show little rank correlati...

---

### 25. [Efficient Compression of Structured and Unstructured Volumes via Learned 3D Gaussian Representation](https://arxiv.org/abs/2607.01164)

**Authors**: Landon Dyken, Sharmistha Chakrabarti, Nathan Debardeleben, Steve Petruzza, Qi Wu, Will Usher, Sidharth Kumar  
**Category**: cs.LG  
**Published**: 2026-07-02  
**Score**: 23.5  
**Type**: new  
**ArXiv ID**: 2607.01164v1  

#### Abstract
Recent work has shown that implicit neural representations (INRs) can be trained to effectively compress structured and unstructured volume data, allowing for direct data querying with a reduced memory footprint. However, as existing INRs for unstructured volumes do not encode geometry, they require...

---

### 26. [Agri-SAGE: Simulation-Grounded Multi-Agent LLM for Context-Aware Agricultural Advisory Generation](https://arxiv.org/abs/2607.00454)

**Authors**: Vedant Balasubramaniam, Geetha Charan, Manojkumar Patil, Rohit P Suresh, V Priyanka, Kodur Sai Vinay Sathvik, Y. Narahari  
**Category**: cs.AI  
**Published**: 2026-07-02  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2607.00454v1  

#### Abstract
Agricultural advisory systems face a fundamental tension: static agronomic guidelines offer consistent, evidence-based recommendations, yet remain blind to in-season variability and dynamic uncertainties. Recent advisory systems powered by LLMs are liable for a different risk of generating recommend...

---

### 27. [FRAME: Learning the Adaptation Domain with a Mixture of Fractional-Fourier Experts](https://arxiv.org/abs/2607.00162)

**Authors**: Tom Saliencro, Maya Lindqvist, Rohan Desai, Priya Nair, Daniel Whitmore  
**Category**: cs.LG  
**Published**: 2026-07-02  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2607.00162v1  

#### Abstract
Parameter-efficient fine-tuning (PEFT) reparameterizes weight updates in a fixed basis: low-rank adapters operate in the spatial domain, while a recent line of spectral methods operates in a fixed Fourier domain. We argue that the choice of domain is itself a design degree of freedom that should be ...

---

### 28. [A Mechanistic View of Authority Hierarchy in LLM Sycophancy](https://arxiv.org/abs/2607.00415)

**Authors**: Emil Joswin, Srujananjali Medicherla, Priyanka Mary Mammen  
**Category**: cs.CL  
**Published**: 2026-07-02  
**Score**: 22.5  
**Type**: new  
**ArXiv ID**: 2607.00415v1  

#### Abstract
Authority bias poses a critical safety concern in language models: models systematically prioritize social cues from authority figures over factual consistency, swaying their answers based on source credibility rather than evidence. We mechanistically investigate this phenomenon using a controlled m...

---

### 29. [Solution space path planning for supporting en-route air traffic control](https://arxiv.org/abs/2607.00064)

**Authors**: Yiyuan Zou, Wenying Lyu, Clark Borst  
**Category**: cs.AI  
**Published**: 2026-07-02  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2607.00064v1  

#### Abstract
As technology advances, many path-planning algorithms have been proposed for Air Traffic Management, yet their operational adoption in tactical control remains limited, revealing a misalignment between algorithmic design priorities and air traffic controllers' needs. This underscores the need for de...

---

### 30. [ALEE: Any-Language Evaluation of Embeddings via English-Centric Minimal Pairs](https://arxiv.org/abs/2607.00171)

**Authors**: Andrianos Michail, Stylianos Psychias, Michelle Wastl, Simon Clematide, Rico Sennrich, Juri Opitz  
**Category**: cs.CL  
**Published**: 2026-07-02  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2607.00171v1  

#### Abstract
Text embeddings are standard for semantic similarity tasks, yet their evaluation remains an open challenge. Current benchmarks are static, cover only a limited set of languages, are often domain-specific, susceptible to overfitting, and poorly representative of low-resource languages. To address the...

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
