# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-07-21 09:22:03 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [HyMCache: A KV Cache Framework for Multi-Turn LLM Serving with CXL-Hybrid Memory](https://arxiv.org/abs/2607.18141v1)

**Authors**: Hakbeom Jang, Inho Song, Sam H. Noh, Jongryool Kim  
**Category**: cs.DC  
**Published**: 2026-07-21  
**Score**: 119.5  
**Type**: new  
**ArXiv ID**: 2607.18141v1  

#### Abstract
Long-context, multi-turn, and agentic LLM workloads increasingly reuse previously processed context, making KV-cache reuse essential for reducing redundant computation. However, this reuse shifts the bottleneck to the memory tier that stores and serves reusable KV states at cluster scale. GPU HBM an...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：HyMCache: A KV Cache Framework for Multi-Turn LLM Serving with CXL-Hybrid Memory
1. 论文的主要贡献和创新点
✅ 解决的问题
长上下文、多轮及agentic LLM工作负载的KV缓存复用可减少冗余计算，但GPU HBM与主机DRAM成本过高，无法扩展至TB级共享上下文容量，现有KV缓存框架难以在低成本介质上实现高效的大规模KV缓存复用，内存复用的瓶颈转移到存储可扩展的内存层。
现有方法缺陷：GPU HBM/主机DRAM成本高昂，无法支撑TB级共享上下文容量；基于SSD的远程存储KV缓存缺乏高效的DRAM管理，无法匹配DRAM级的KV缓存性能，导致多轮LLM服务性能受限。

🚀 提出的新方法与思路
**HyMCache框架**，该框架集成CXL混合内存（CXL-HM，结合少量设备内DRAM与CXL接口后的大容量SSD）。利用多轮KV缓存访问的读主导、可预测、仅追加的特性，重新设计CXL-HM内的DRAM管理策略；采用请求级前缀预取与机会写缓冲，在设备DRAM中暂存延迟敏感的读操作，实现以SSD级成本达到DRAM级的KV缓存效率。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| KV缓存复用成本 | 以SSD级存储成本，实现接近DRAM级的KV缓存效率，可支撑TB级共享上下文容量 |
| 服务性能 | 在相同DRAM预算下，显著优于本地LMCache框架 |
| 资源开销 | 相比1TB分布式DRAM的Mooncake框架，DRAM用量仅为其1/16，大幅降低资源成本 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
任务为多轮LLM Serving服务性能评估，实验部署场景包含单聚合器、PD-disaggregated serving两种；评估指标包括服务性能（越高越好）、DRAM用量（越低越好），论文未明确指标的具体定义名称。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| local LMCache | KV缓存框架 | 依赖本地DRAM存储KV缓存 |
| Mooncake | KV缓存框架 | 采用1TB分布式DRAM存储KV缓存 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**论文摘要：HyMCache与local LMCache的性能对比（单节点/PD-disaggregated serving场景）**
| 场景 | 同DRAM预算下性能对比 |
| ---- | ------------------ |
| 单节点（单聚合器） | HyMCache性能优于local LMCache |
| PD-disaggregated serving | HyMCache性能优于local LMCache |
💡 结论：在相同DRAM预算下，HyMCache在两种LLM服务部署场景下的性能均显著优于本地LMCache框架。

**论文摘要：HyMCache与Mooncake的性能和资源对比**
| 对比项 | HyMCache | Mooncake（1TB分布式DRAM） |
| ---- | -------- | ------------------------- |
| 服务性能 | 约低30% | 基准 |
| DRAM用量 | 为Mooncake的1/16 | 1TB |
💡 结论：相比1TB分布式DRAM的Mooncake，HyMCache在DRAM用量仅为其1/16的情况下，性能仅低约30%，实现了低成本与性能的平衡。

其他实验（主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）：论文未报告

4. 关键结论和发现
- 主要发现：1. 集成CXL混合内存的HyMCache框架，可在大幅降低DRAM用量的同时保持较好的多轮LLM服务性能；2. 针对CXL-HM的DRAM管理优化（请求级前缀预取、机会写缓冲），有效提升了低成本介质上的KV缓存访问效率；3. 在不同LLM服务部署场景（单聚合器、PD-disaggregated serving）下均表现优于现有本地KV缓存框架。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：HyMCache是一种基于CXL混合内存的KV缓存框架，通过优化内存管理实现了低成本下的高效多轮LLM服务，可大幅减少DRAM用量并保持较好性能。

</details>

---

### 2. [An Explicit World Model Based on Data-First Ontology: DaoQL Multimodal Storage Validation and Counterfactual Reasoning Evaluation](https://arxiv.org/abs/2607.17269v1)

**Authors**: Zhanbo Li, Shifeng Wu, Xiangjin Meng, Wenjie Cai  
**Category**: cs.AI  
**Published**: 2026-07-21  
**Score**: 105.0  
**Type**: new  
**ArXiv ID**: 2607.17269v1  

#### Abstract
Large language models encode world models implicitly in neural weights, which exposes four structural risks in high-precision domains such as medicine and finance: hallucination, frozen knowledge, poor explainability, and poor modifiability. This paper proposes data-first ontology: LLMs are treated ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

An Explicit World Model Based on Data-First Ontology: DaoQL Multimodal Storage Validation and Counterfactual Reasoning Evaluation
1. 论文的主要贡献和创新点
✅ 解决的问题
Large language models将世界模型隐式编码在神经权重中，在医疗、金融等高精密领域暴露幻觉、知识冻结、可解释性差、可修改性差四类结构风险；隐式模型缺乏原子读/delta语义，无法为高精密领域提供必要的架构保证。

🚀 提出的新方法与思路
**data-first ontology**：将LLM作为推理和语言引擎，把确定性知识转移至显式多模态数据库DaoQL；正式化显式世界模型，证明在规则独立、确定性评估、固定冲突解决的条件下，显式模型为可组合反事实分解提供充分条件，而隐式模型无 comparable架构保证；实现的系统聚焦于DaoQL的验证存储层和显式Eval路径，整合图、列、向量、全文引擎至单一进程；KVCache图节点、专家热更新、DaoQL-Agent运行时为未来工作。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 反事实推理能力 | 显式模型在规则独立等条件下为可组合反事实分解提供充分架构保证，隐式模型无对应保证 |
| 多模态存储整合 | 将图、列、向量、全文引擎整合至单一进程 |
| 高精密领域适配性 | 迁移确定性知识至显式数据库，降低幻觉、知识冻结等结构风险 |
| 可解释性与可修改性 | 显式结构提升可解释性，确定性知识迁移后更易修改 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| LDBC SNB SF1 | 用于相关性能测试的数据集 |
| ANN-Benchmarks | 用于相关性能测试的数据集 |

🎯 实验设置与评估指标
任务为验证DaoQL多模态存储性能与反事实推理性能，指标如下：
| 指标 | 含义（箭头方向） |
| --- | --- |
| 图广度优先搜索延迟 | 越低越好（↓） |
| HNSW延迟 | 越低越好（↓） |
| Fluent混合查询延迟 | 越低越好（↓） |
| 查询覆盖率 | 越高越好（↑） |
| 每秒查询率（QPS） | 越高越好（↑） |
| Recall@10 | 越高越好（↑） |
| 可组合反事实分解能力 | 越高越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| GPT-4o alone | 隐式世界模型方法 | 仅用LLM处理任务，存在隐式模型的四类结构风险 |
| DaoQL+GPT-4o | 显式世界模型方法 | 结合显式多模态数据库DaoQL与LLM，用于反事实推理任务 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**嵌入式单机场景性能**
| 指标 | 结果 |
| --- | --- |
| 图BFS延迟 | 1.20 ms |
| HNSW延迟 | 83.1 us |
| Fluent混合查询延迟 | 105.8 us |
| LDBC SNB SF1查询覆盖率 | 34/34 |
| LDBC SNB SF1整体QPS | 1.8 |
| ANN-Benchmarks Recall@10 | ≥99%（修复bridge-edge保护后，千级QPS下） |
| 五领域反事实实验（n=1250）可组合反事实分解性（DaoQL+GPT-4o） | 94% |
| 五领域反事实实验（n=1250）可组合反事实分解性（GPT-4o alone） | 45% |
💡 结论：DaoQL在嵌入式单机场景具备高效多模态查询性能，结合GPT-4o的组合显式模型在五领域反事实推理中，可组合分解能力达94%，较单独GPT-4o提升49个百分点，工程潜力显著。

1. 主benchmark性能（L2/碰撞率等）：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 核心发现1：隐式编码世界模型的LLM在医疗、金融等高精密领域存在幻觉、知识冻结、可解释性差、可修改性差四类结构风险；
- 核心发现2：数据优先本体的显式模型在规则独立等条件下，为可组合反事实分解提供充分架构保证，隐式模型无对应保证；
- 核心发现3：DaoQL+GPT-4o在五领域反事实推理中，可组合反事实分解能力达94%，较单独GPT-4o提升49个百分点。

方法局限性：实验结果需注意与客户端-服务器系统的部署形态差异；KVCache图节点、专家热更新、DaoQL-Agent运行时等关键组件尚未实现，未纳入当前实验。

未来工作：完成KVCache图节点、专家热更新、DaoQL-Agent运行时的开发；优化系统以适配不同部署形态，进一步提升QPS等性能指标。

> ✅ **总结一句话**：本文提出基于数据优先本体的显式世界模型，通过DaoQL多模态数据库结合LLM，缓解了隐式模型在高精密领域的结构风险，显著提升了反事实推理的可组合分解能力。

</details>

---

### 3. [AGG: Jacobian-Aggregated Group Gradient for Efficient GRPO Training of Diffusion Models](https://arxiv.org/abs/2607.17572v1)

**Authors**: Ruiyi Ding, Jie Li, He Kang, Ziyan Liu, Chengru Song, Yuan chen  
**Category**: cs.LG  
**Published**: 2026-07-21  
**Score**: 96.0  
**Type**: new  
**ArXiv ID**: 2607.17572v1  

#### Abstract
Group Relative Policy Optimization (GRPO) is a powerful reinforcement learning algorithm for aligning generative models with human preferences. While successful in large language models~\cite{shao2024deepseekmathpushinglimitsmathematical}, its extension to diffusion and flow matching models introduc...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

AGG: Jacobian-Aggregated Group Gradient for Efficient GRPO Training of Diffusion Models
1. 论文的主要贡献和创新点
✅ 解决的问题
Group Relative Policy Optimization (GRPO)算法在大型语言模型中成功应用，但其扩展到DiT backbone的扩散模型训练时，梯度需在采样轨迹的每一个时间步进行反向传播，导致高分辨率文本到图像（T2I）训练存在严重计算瓶颈，成本过高。

🚀 提出的新方法与思路
**JAGG（Jacobian-Aggregated Group Gradient）**：将每W个连续步骤的完整Transformer反向传播次数从W减少至2，通过端点雅可比的t加权插值近似中间步骤雅可比，再将每步上游信号聚合成两个复合梯度，通过一次联合反向传播应用；该插值在速度关于$(z,t)$线性时完全精确，提出余弦相似度路由规则（jagg_frac）仅在假设成立时启用JAGG。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 训练效率 | 实现约2倍的反向传播速度提升 |
| 生成质量 | 质量退化可忽略 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务为高分辨率文本到图像（T2I）的GRPO训练，评估指标论文未报告。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能**：论文未报告
**效率对比（FPS / 参数量）**：论文在T2I基准实验中显示JAGG实现约2倍反向传播加速，质量退化可忽略
**跨域 / zero-shot迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告

4. 关键结论和发现
- 主要发现：1. JAGG通过雅可比聚合分组梯度，将DiT扩散模型GRPO训练的反向传播次数从W/步降至2/W步，有效降低计算成本；2. 端点雅可比插值策略在速度关于$(z,t)$线性时完全精确，余弦相似度路由规则（jagg_frac）可智能控制方法启用时机；3. 在T2I基准上实现约2倍反向传播加速，同时保持生成质量退化可忽略。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：JAGG针对扩散模型GRPO训练的计算瓶颈，提出雅可比聚合分组梯度策略，在T2I基准上实现约2倍反向传播加速，且生成质量退化极小。

</details>

---

### 4. [PGN: Design and Implementation of a Vision-Language Navigation System Based on Pangu Multimodal Foundation Model](https://arxiv.org/abs/2607.17806v1)

**Authors**: Li Xian, Mingxi Li, Yizheng Wang, Yiming Shen, Qi Chen, Zhuoling Xiao  
**Category**: cs.AI  
**Published**: 2026-07-21  
**Score**: 88.5  
**Type**: new  
**ArXiv ID**: 2607.17806v1  

#### Abstract
Vision-Language Navigation (VLN) requires an embodied agent to interpret a natural-language instruction and predict actions from temporally ordered visual observations. Adapting a multimodal large language model to VLN requires visual-language alignment, compact temporal inputs, action-space groundi...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

PGN: Design and Implementation of a Vision-Language Navigation System Based on Pangu Multimodal Foundation Model
1. 论文的主要贡献和创新点
✅ 解决的问题
适配多模态大语言模型到Vision-Language Navigation（VLN）任务，需解决视觉-语言对齐、紧凑时序输入、动作空间 grounding、目标硬件稳定训练等核心适配需求。

🚀 提出的新方法与思路
**PGMM视觉-语言对齐阶段**：冻结EVA-ViT-G/14视觉编码器与冻结的语言主干，训练Q-Former及两层MLP投影器，实现视觉与语言模态的对齐。
**双阶段模型适配策略**：第一阶段完成视觉-语言对齐后，第二阶段将模型适配至专家导航轨迹，采用五观察窗口、epoch依赖的时序采样、推理后动作的输出格式；该阶段冻结对齐的视觉通路，更新三个结构token embeddings与LoRA适配器。
**硬件适配方案**：采用混合精度计算、选择性FP32计算，结合DeepSpeed ZeRO-2框架，在8个Ascend 910B NPU上完成模型训练。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
论文未报告 | 论文未明确报告与现有方法的对比优势，仅提出针对VLN适配的双阶段训练及硬件适配方案

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
论文未报告 | 离线VLN动作预测的教师强制开环评估

🎯 实验设置与评估指标
任务：教师强制、开环的离线Vision-Language Navigation动作预测
指标 | 含义（箭头标方向）
--- | ---
Normalized Action Match (NAM) | 衡量离线专家动作对齐程度，越高越好（↑）
Non-empty Rate (NER) | 衡量模型输出非空比例，越高越好（↑）

⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
**论文未提及对应表号：V9在教师强制开环评估下的结果**
指标 | 数值
--- | ---
Normalized Action Match (NAM) | 62.29%
Non-empty Rate (NER) | 100.00%
💡 结论：论文仅在开环评估下报告了V9的NAM与NER指标，该指标量化离线专家动作对齐程度，未报告闭环导航相关的核心性能指标。
其余未提及的实验（主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）：论文未报告

4. 关键结论和发现
- 主要发现
1. PGN是基于OpenPangu-7B构建的离线Vision-Language Navigation动作预测系统，采用双阶段训练策略实现视觉-语言对齐与专家轨迹适配。
2. 论文报告的V9在教师强制开环评估下，NAM为62.29%，NER为100.00%。
3. 当前采用的评估指标仅能量化离线专家动作对齐程度，无法评估闭环导航的关键性能。
- 方法局限性
论文报告的评估指标仅覆盖离线专家动作对齐维度，未评估VLN任务核心的闭环导航性能（如误差积累、路径效率、目标完成情况），相关内容属于未来工作。
- 未来工作
开展Vision-Language Navigation的闭环导航相关评估，包括误差积累、路径效率及目标完成情况。

> ✅ **总结一句话**：PGN是基于OpenPangu-7B的离线Vision-Language Navigation动作预测系统，通过双阶段训练及硬件适配实现，其开环评估显示出较好的离线专家动作对齐效果，闭环导航性能待进一步评估。

</details>

---

### 5. [PPO-HSC: An Exploratory Reinforcement Learning Framework Based on Wide-Area Policy Coverage Optimization](https://arxiv.org/abs/2607.16206v1)

**Authors**: Yujie Shen, Haowen Chen  
**Category**: cs.AI  
**Published**: 2026-07-21  
**Score**: 82.5  
**Type**: new  
**ArXiv ID**: 2607.16206v1  

#### Abstract
This paper introduces PPO-HSC (Proximal Policy Optimization with High-order Sampling Coverage), an exploratory reinforcement learning framework designed to address the "Invisible Shackles" of mode collapse in Large Language Model (LLM) fine-tuning. While standard Reinforcement Learning from Verifiab...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

PPO-HSC: An Exploratory Reinforcement Learning Framework Based on Wide-Area Policy Coverage Optimization
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：Large Language Model (LLM)微调中，现有标准Reinforcement Learning from Verifiable Rewards (RLVR)方法存在模式崩溃痛点——模型过度优化已知解决方案，牺牲探索性，丧失探索更广泛解流形的能力。
方法缺陷：标准RLVR方法通过强化高奖励轨迹微调LLM，易陷入模式崩溃，无法兼顾解的多样性与探索能力。

🚀 提出的新方法与思路
**PPO-HSC with High-order Sampling Coverage (HSC) reward**：该框架为解决LLM微调的模式崩溃问题设计，核心是引入HSC奖励机制：通过维护已验证唯一解的动态轨迹库，生成鼓励语义新颖性的可微信号，同时加入合理性约束以确保生成解的结构理性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 解多样性 | 支持发现低相似度但高有效性的推理模式，提升生成解的多样化程度 |
| 状态空间覆盖 | 驱动模型探索更广泛的解流形，增强状态空间覆盖范围 |
| 任务性能 | 在数学推理、代码生成任务中保持或超越SOTA RL基线的准确性与语法完整性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| GSM8K | 数学推理任务 |
| SVAMP | 数学推理任务 |

🎯 实验设置与评估指标
任务：在数学推理（GSM8K、SVAMP）和代码生成任务中对PPO-HSC与SOTA RL基线进行性能评估。
| 指标 | 含义 |
| --- | --- |
| 解多样性 | 衡量模型生成解的多样化程度，↑越高表示多样性越好 |
| 状态空间覆盖 | 衡量模型对解空间的探索广度，↑越高表示覆盖越广 |
| 准确性 | 衡量任务解决的正确率，↑越高表示准确性越好 |
| 语法完整性 | 衡量代码生成内容的语法正确性，↑越高表示完整性越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| PPO-HSC | 本文提出的探索式强化学习框架 | 融入HSC奖励机制，支持解多样性与空间覆盖优化 |
| SOTA RL基线 | 传统强化学习微调方法 | 基于RLVR，易出现模式崩溃问题 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（L2/碰撞率等）**：论文未报告
**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot 迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告

4. 关键结论和发现
- 主要发现：PPO-HSC框架可显著增强LLM微调过程中的解多样性与状态空间覆盖，同时保持或超越SOTA RL基线的任务性能；HSC奖励机制为解决LLM微调的模式崩溃问题提供了有效路径。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：PPO-HSC框架通过引入HSC奖励机制优化策略广域覆盖，解决了LLM微调中的模式崩溃问题，在提升解多样性与探索能力的同时保持了优秀的任务性能。

</details>

---

### 6. [LenGuard-GPC: Length Guarding with Guided-Prompt Consistency for Spatial Reasoning Reinforce Learning](https://arxiv.org/abs/2607.17243v1)

**Authors**: Xingjian Tao, Yiwei Wang, Yujun Cai, Jing Tang  
**Category**: cs.AI  
**Published**: 2026-07-21  
**Score**: 82.0  
**Type**: new  
**ArXiv ID**: 2607.17243v1  

#### Abstract
Multi-view spatial reasoning requires vision-language models to compare visual evidence across images, align object correspondences, and infer spatial relations over long visual contexts, a setting where chain-of-thought reasoning tends to grow verbose without becoming more accurate. Reinforcement l...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

LenGuard-GPC: Length Guarding with Guided-Prompt Consistency for Spatial Reasoning Reinforce Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
多视图空间推理要求视觉语言模型对比多图像的视觉证据、对齐物体对应、推断长视觉上下文的空间关系，当前存在两点核心缺陷：
1. 思维链推理易变得啰嗦但准确性未必提升；
2. 标准GRPO采用稀疏的结果级反馈作为奖励，既无法提供推理轨迹中错误点的信号，也无法控制推理长度。

🚀 提出的新方法与思路
**LenGuard-GPC框架**：一种密集奖励框架，针对每个采样的推理轨迹，对比标准提示与引导提示下的token级预测分布，将得到的token-sum KL divergence作为密集奖励信号；引入**分阶段长度奖励**，因KL惩罚会累积，若不加控制会奖励无论质量的短响应，该分阶段长度奖励可将推理长度维持在受控范围内，而非单纯鼓励简短。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 奖励信号类型 | 从稀疏结果级反馈转为密集token级奖励信号，可反馈推理过程的质量 |
| 长度控制 | 具备分阶段长度奖励机制，可将推理长度维持在合理受控范围，避免无意义的短响应 |
| 任务适配性 | 适配多视图空间推理这类长视觉上下文推理任务，解决思维链冗长但准确性未提升的问题 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 六个多视图空间推理基准 | 用于评估方法在多视图空间推理任务上的性能 |

🎯 实验设置与评估指标
任务：多视图空间推理（要求模型对比多图像视觉证据、对齐物体对应、推断长视觉上下文的空间关系）
| 指标 | 含义（箭头标方向） |
|------|------------------|
| 准确率 | ↑ 越高越好 |
| 平均响应长度 | ↓ 越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| vanilla GRPO | 强化学习基线方法 | 采用稀疏结果级反馈的奖励，未对推理长度进行控制 |

3. 主要实验结果和性能指标
📊 定量结果汇总
仅明确报告：在六个多视图空间推理基准上，LenGuard-GPC相比vanilla GRPO提升了准确率并降低了平均响应长度，其余实验细节（如表号、具体数值等）未提及。
- 主 benchmark 性能：论文未报告
- 效率对比（FPS / 参数量）：论文未报告
- 跨域 / zero-shot 迁移：论文未报告
- 鲁棒性 / 扰动测试：论文未报告
- 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. LenGuard-GPC能在多视图空间推理任务上提升模型准确率，同时缩短模型响应的平均长度；2. 基于引导提示一致性的token级KL散度密集奖励搭配分阶段长度奖励，可解决标准GRPO存在的稀疏反馈、无长度控制的问题。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：LenGuard-GPC是一种针对多视图空间推理任务的密集奖励强化学习框架，通过token-sum KL divergence的密集奖励与分阶段长度奖励，实现了准确率提升与响应长度缩短的双重效果。

</details>

---

### 7. [C$^2$KV: Compressed and Composable KV Cache Reuse for Efficient LLM Inference](https://arxiv.org/abs/2607.17715v1)

**Authors**: Chuheng Du, Junyi Chen, Hanlin Tang, Kan Liu, Tao Lan, Lin Qu, Chaoyue Niu, Shengzhong Liu, Guihai Chen, Fan Wu  
**Category**: cs.CL  
**Published**: 2026-07-21  
**Score**: 78.0  
**Type**: new  
**ArXiv ID**: 2607.17715v1  

#### Abstract
Long-context inference is central to modern large language model (LLM) applications such as retrieval-augmented generation and multi-document reasoning. To mitigate the growing inference cost, recent work has explored key-value (KV) cache reuse to reduce redundant prefill computation. However, exist...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：C²KV: Compressed and Composable KV Cache Reuse for Efficient LLM Inference
1. 论文的主要贡献和创新点
✅ 解决的问题
现有的KV缓存复用方法主要聚焦于计算节省，却忽略了长上下文LLM服务中存储和访问大型KV缓存的高额成本；将KV压缩与非前缀KV复用直接结合会导致严重的精度退化，这一矛盾尚未被现有方法有效解决。

🚀 提出的新方法与思路
**可组合压缩KV缓存流形**：设计为位置无关的流形，适配非前缀KV复用场景，满足模块化可拼接的需求。
**轻量sidecar Extractor模块**：包含可学习的压缩tokens与结构化注意力流，能够生成模块化的KV表示，支持灵活复用与拼接，且无需修改冻结的基础LLM模型。
**压缩-拼接协同训练策略**：对齐提取阶段的KV表示与其下游复用行为，解决压缩与复用结合带来的精度下降问题。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| KV缓存存储成本 | 可有效降低 |
| KV缓存传输成本 | 可有效降低 |
| 长上下文推理速度 | 可实现加速 |
| 生成质量 | 可保留原始生成质量 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
任务：长上下文LLM推理加速与生成质量保持。
评估指标：涉及KV缓存存储成本、传输成本、推理速度、生成质量；论文未报告具体指标的定义、取值范围及对应标注方向。

⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. C²KV是一种统一的非前缀KV缓存复用框架，可同时优化KV缓存的存储、传输成本与长上下文推理效率；2. 该方法能够在提升长上下文LLM推理效率的同时，有效保留生成质量。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：C²KV是面向高效LLM推理的统一非前缀KV缓存复用框架，通过联合优化KV提取与推理时的拼接过程，在降低长上下文场景下KV缓存的存储与传输成本的同时，保留生成质量。

</details>

---

### 8. [SEAM-V: A Hybrid-Decoupled RISC-V Vector Processor with Backend-Visible EP Context for Sustained Vector Throughput](https://arxiv.org/abs/2607.17899v1)

**Authors**: Weiying Wang, Zhiwei Zhang  
**Category**: cs.AR  
**Published**: 2026-07-21  
**Score**: 77.0  
**Type**: new  
**ArXiv ID**: 2607.17899v1  

#### Abstract
Data-parallel workloads in deep learning and scientific computing continue to drive demand for higher processor throughput, energy efficiency, and scalability. The RISC-V Vector Extension (RVV) supports scalable execution through a vector-length-agnostic programming model. However, many tightly coup...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

SEAM-V: A Hybrid-Decoupled RISC-V Vector Processor with Backend-Visible EP Context for Sustained Vector Throughput
1. 论文的主要贡献和创新点
✅ 解决的问题
现有RISC-V Vector Extension（RVV）的紧耦合实现（TC）依赖标量核心逐个提供向量指令，存在向量指令供应缺口、标量侧进度延迟，以及短向量、循环尾部、控制/内存交织阶段的保守依赖处理等问题，导致向量吞吐量受限。
🚀 提出的新方法与思路
**Hybrid-Decoupled Vector Execution Architecture**：SEAM-V提出的核心架构，通过任务级解耦、本地指令供应、VLIW风格的指令打包，形成连续的执行包（EP）流以避免向量指令供应缺口；EP序列化为单个请求后，EP身份标识及请求绑定的预取上下文对动态向量后端可见，支持同EP候选 hazard 抑制与请求绑定预取，同时混合分发路径在满足安全条件时可提供有限的跨EP向量重叠，进一步提升吞吐量。
🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 向量执行连续性 | 通过EP流设计避免指令供应缺口，提升执行连贯性 |
| hazard 处理效率 | 同EP上下文中可实现候选 hazard 抑制，减少不必要的依赖等待 |
| 预取优化能力 | 请求绑定的预取上下文可见，支持更精准的预取 |
| 计算单元利用率 | 满足安全条件时支持有限跨EP向量重叠，提升资源利用 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标
任务为对比SEAM-V与Ara-based紧耦合RVV实现（TC）的向量处理器性能，评估指标及含义如下：
| 指标 | 含义（↑越高越好） |
|------|------------------|
| 几何平均加速比 | 整体向量任务性能提升倍数 |
| 应用组加速比 | 不同类型向量应用的性能提升倍数 |
| AVL=32时一维向量kernel几何平均加速比 | 固定向量长度下的一维向量任务性能提升倍数 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| Ara-based Tightly Coupled RVV Implementation（TC） | 传统RVV实现基线 | 紧耦合设计，依赖标量核心逐个提供向量指令 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表：性能对比（cycle-accurate RTL评估）**
| 方法 | 17个代表性kernel几何平均加速比 | 一维可变AVL组加速比 | BLAS和矩阵组加速比 | 固定-size应用组加速比 | AVL=32时六个一维向量kernel几何平均加速比 |
|------|--------------------------------|----------------------|----------------------|------------------------|--------------------------------------------|
| SEAM-V | 1.34x ✅ | 1.50x ✅ | 1.25x ✅ | 1.27x ✅ | ~3x ✅ |
💡 结论：cycle-accurate RTL评估结果显示，SEAM-V相比基线TC实现，在各类向量任务上均实现了性能提升，尤其在一维向量任务且AVL=32时性能提升接近3倍，验证了架构对向量吞吐量的优化效果。
其余实验（效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）：论文未报告

4. 关键结论和发现
- 主要发现：1. 传统紧耦合RVV实现的指令供应缺口和保守依赖处理问题可通过SEAM-V的混合解耦架构及EP上下文可见性设计有效缓解；2. SEAM-V在17个代表性kernel上相比Ara-based TC实现取得1.34x的几何平均加速比，不同应用组均有显著性能提升；3. 当向量长度（AVL）为32时，一维向量kernel的几何平均加速比接近3倍，验证了架构在典型向量任务中的性能优势。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：SEAM-V作为面向RISC-V向量扩展的混合解耦向量处理器架构，通过执行包上下文可见性优化执行流程，在多种向量应用任务中相比传统紧耦合RVV实现显著提升了向量吞吐量。

</details>

---

### 9. [Hardware-Transparent I/O Governance in Disaggregated Heterogeneous Storage](https://arxiv.org/abs/2607.16578v1)

**Authors**: Rajarshi Chowdhury, Akshay Shah, Sue K. Lee  
**Category**: cs.DC  
**Published**: 2026-07-21  
**Score**: 76.0  
**Type**: new  
**ArXiv ID**: 2607.16578v1  

#### Abstract
Shared-nothing disaggregated storage clusters that serve both latency-sensitive databases and opaque block-volume workloads face two governance problems unsolved by existing schedulers: maintaining consistent performance across heterogeneous hardware generations, and enforcing global I/O limits when...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Hardware-Transparent I/O Governance in Disaggregated Heterogeneous Storage
1. 论文的主要贡献和创新点
✅ 解决的问题：共享无拆解异构存储集群服务延迟敏感数据库和 opaque 块卷工作负载时，现有调度器未解决两大痛点：1）维持异构硬件代际间的性能一致性；2）当访问模式倾斜至部分存储节点时，强制全局I/O限制。
🚀 提出的新方法与思路
**I/O Resource Manager (IORM)**：部署于Oracle Exadata Exascale生产环境的多阶段分布式调度器，整合三类机制：
1. **Hardware-aware cost modeler**：利用 datasheet 派生的固定成本标准化I/O核算，使I/O限制在异构硬件代际间保持一致；
2. **Quantum-based rate limiter with bounded carry-forward credits**：适配数据库流量微突发，同时强制执行长期服务水平目标（SLO）；
3. **Distributed adaptive feedback controller**：跨集群重新分配未使用 entitlement，缓解拓扑访问倾斜问题。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 异构硬件兼容性 | 硬件感知成本模型消除了不同硬件代际间I/O限制的差异 |
| 流量突发适配 | 带限制结转credit的量子速率限流器可平衡数据库微突发需求与长期SLO |
| 访问倾斜缓解 | 分布式自适应反馈控制器可动态分配集群资源，解决拓扑级访问倾斜 |
| 生产可用性 | 已在Oracle Exadata Exascale生产环境部署验证 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |
🎯 实验设置与评估指标
任务：在共享无拆解异构存储集群中（运行多租户工作负载，含数据库和块卷）验证IORM的I/O治理能力。
| 指标 | 含义（箭头） |
| ---- | ---- |
| 收敛偏差 | I/O实际用量与配置限制的相对偏差 ↓ |
| 跨租户干扰 | 非目标租户的性能损失程度 ↓ |
| 故障恢复时间 | 存储节点故障后恢复全吞吐量的时长 ↓ |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**8节点测试集群场景**
| 场景条件 | 结果 |
| ---- | ---- |
| 极端顺序访问倾斜 | IORM收敛至配置限制的5%以内 |
| 多租户并发运行（最多100个租户卷） | 无跨租户干扰 |
| 存储节点故障后 | 15秒内恢复全吞吐量 |
💡 结论：IORM在8节点测试集群的多租户负载场景下，可满足异构存储集群的性能SLO，应对访问倾斜和节点故障等异常情况。
（注：论文未报告主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验的相关结果）

4. 关键结论和发现
- 主要发现：① 硬件感知成本模型、带结转credit的量子速率限流器、分布式自适应反馈控制器的组合，可有效解决异构共享无拆解存储集群的性能一致性和访问倾斜问题；② IORM具备生产级可用性，已部署于Oracle Exadata Exascale环境。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：本文提出的I/O Resource Manager是部署于Oracle Exadata Exascale生产环境的多阶段分布式I/O调度器，通过三类创新机制解决了异构共享无拆解存储集群的性能一致性与访问倾斜问题，保障多租户服务水平目标。

</details>

---

### 10. [FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications](https://arxiv.org/abs/2607.18171v1)

**Authors**: Krish Agarwal, Zhuoming Chen, Yanyuan Qin, Zhenyu Gu, Atri Rudra, Beidi Chen  
**Category**: cs.LG  
**Published**: 2026-07-21  
**Score**: 75.5  
**Type**: new  
**ArXiv ID**: 2607.18171v1  

#### Abstract
Real-time multimodal applications, including voice agents and interactive video generation, compose heterogeneous models into pipelines whose efficient deployment requires application-specific decisions about placement, streaming, and intra-model parallelism. Existing serving systems and auto-parall...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications
1. 论文的主要贡献和创新点
✅ 解决的问题
实时多模态应用（包括语音助手、交互式视频生成）通过异构模型组成管道实现，其高效部署需要应用特定的放置、流式、模型内并行决策；现有服务系统和自动并行编译器采用有限转换或固定工作负载假设，新应用的高性能部署需手工完成，效率低。

🚀 提出的新方法与思路
**Agent Harness FlashRT**：一种引导编码代理的代理工具包，用于将简单开发者参考实现提升为优化的多GPU部署，可灵活权衡延迟、吞吐量等目标指标；基于新的chain-of-program范式，通用编码代理通过多遍转换流程处理：首先将参考实现转换为中间表示（IR）以捕捉数据依赖和持久状态范围，再通过序列解释器验证IR，随后进行静态分析识别候选转换；最后代理在测量门控优化循环中迭代实现、验证、基准测试每个候选转换，生成适配不同硬件预算的有效部署。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 优化范式 | 现有服务系统/自动并行编译器依赖固定工作负载假设或有限转换，需手工实现新应用部署；FlashRT基于chain-of-program的代理驱动多阶段优化流程，自动生成适配新应用的优化部署 |
| 硬件适配性 | 现有方法依赖平台成熟专家优化，在未成熟硬件平台表现受限；FlashRT在NVIDIA B200、AMD MI355X等不同成熟度的GPU平台均能实现高效部署，适配不同硬件预算 |
| 指标灵活性 | 现有方法无法灵活权衡延迟、吞吐量等核心性能指标；FlashRT可灵活权衡上述指标，满足不同应用的目标需求 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务为实时多模态应用的多GPU部署优化。
| 指标 | 含义 |
| ---- | ---- |
| 延迟 | 越低越好 |
| 吞吐量 | 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| vLLM-Omni | 专家实现 | 基于专家经验的Qwen3-Omni文本到音频推理部署实现 |
| 现有服务系统/自动并行编译器 | 部署工具 | 采用有限转换或固定工作负载假设，需手工实现新应用的高效部署 |

3. 主要实验结果和性能指标
论文未报告

4. 关键结论和发现
- 2-3 条主要发现
1. FlashRT通过chain-of-program的代理驱动优化流程，可将简单开发者参考实现自动转换为适配不同硬件预算的高效实时多模态应用部署；
2. FlashRT在成熟GPU平台与未成熟GPU平台均实现了优异的优化效果，尤其在未成熟硬件平台（如AMD MI355X）上，其优化表现优于平台原生专家实现；
3. FlashRT可灵活权衡实时多模态应用的延迟、吞吐量等核心性能指标，适配不同应用的目标需求。
- 方法局限性
论文未报告
- 未来工作
论文未报告

> ✅ **总结一句话**：FlashRT是一种基于chain-of-program的代理工具包，通过多阶段代理驱动优化流程，可自动将简单参考实现转换为适配不同硬件平台的高效实时多模态应用部署，能灵活权衡核心性能指标，在未成熟硬件平台上的优化表现尤为突出。

</details>

---

### 11. [Lossless but Not Free: An Empirical Anatomy of Speculative Decoding on Consumer Hardware](https://arxiv.org/abs/2607.17283v1)

**Authors**: Param Chordiya  
**Category**: cs.AI  
**Published**: 2026-07-21  
**Score**: 74.0  
**Type**: new  
**ArXiv ID**: 2607.17283v1  

#### Abstract
Single-stream autoregressive decoding of large language models is bound by memory bandwidth: each generated token requires one full forward pass through the target model, and successive passes cannot be parallelized. Speculative decoding restructures this computation: a small draft model proposes $K...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Lossless but Not Free: An Empirical Anatomy of Speculative Decoding on Consumer Hardware
1. 论文的主要贡献和创新点
✅ 解决的问题
现有单流自回归解码大语言模型受内存带宽限制，每生成一个token需一次目标模型的全前向传播，后续传播无法并行化；speculative decoding虽能重构计算流程，但在消费级硬件上的实证研究不足，且存在配置导致的性能退化问题，部分实现因硬件特性可能出现串行化效应影响性能。

🚀 提出的新方法与思路
**Device-Agnostic Speculative Decoding Implementation**：从零实现支持CUDA、MPS、CPU多后端的跨设备speculative decoding方案；
**Consumer Hardware-Targeted Empirical Study**：针对消费级Apple-silicon笔记本，开展五个不同draft/target后端配置的性能与分布等价性实证分析；
**Multi-Level Distribution Equivalence Validation**：从三个层级验证speculative decoding的分布等价性，包括针对约9200个实模型token的双样本测试（χ²=162.5，dof=200，p=0.976）及贪心序列一致性验证。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
设备适配性 | 支持CUDA、MPS、CPU多后端的跨设备实现，覆盖主流计算平台
硬件针对性 | 聚焦消费级Apple-silicon笔记本实际特性，量化并行验证串行化等隐藏效应
分布严谨性 | 通过多级别验证确认speculative decoding的目标模型输出分布等价性，确保方法正确性
性能洞察 | 明确speculative decoding的加速前提，最优配置实现1.61×的wall-clock加速

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
论文未报告 | 论文未提及具体数据集信息，仅提及用于双样本测试的约9200个实模型token

🎯 实验设置与评估指标
本研究在消费级Apple-silicon笔记本上，针对五个draft/target后端配置开展speculative decoding的性能与分布等价性评估；指标含义如下：
指标 | 含义（箭头）
--- | ---
wall-clock speedup | 实际运行时间加速比，↑越高越好
接受率（Acceptance Rate） | draft模型生成token的接受比例，无明确箭头
χ²值 | 双样本测试卡方值，分布等价性验证指标，论文显示p=0.976（分布等价）
贪心序列一致性 | 与目标模型贪心输出的序列匹配程度，越高越好

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
论文未报告 | 论文未报告 | 论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 分布等价性验证：无对应表号，相关结果为针对约9200个实模型token的双样本测试（χ²=162.5，dof=200，p=0.976），且贪心序列一致性验证通过。💡 结论：验证了speculative decoding与目标模型的输出分布等价，未出现分布偏移问题。
2. 主benchmark性能：论文未报告。💡 结论：论文未提供主benchmark性能指标，无法对应结论。
3. 效率对比：仅提及最优配置（K=6）的wall-clock speedup为1.61×，三个配置出现减速。💡 结论：最优配置可获1.61×的wall-clock加速，部分配置因draft/target延迟不足或串行化效应减速。
4. 跨域/zero-shot迁移：论文未报告。💡 结论：未开展相关实验，无对应结果。
5. 鲁棒性/扰动测试：论文未报告。💡 结论：未开展相关实验，无对应结果。
6. 消融实验：论文未报告。💡 结论：未开展相关实验，无对应结果。

4. 关键结论和发现
- 主要发现：1）Speculative decoding在消费级硬件上的加速效果严格依赖于验证环节的批次并行性，以及draft与目标模型的实际延迟差，不满足则性能退化；2）测试的五个配置中，K=6时最优，实现1.61×的wall-clock加速，三个配置因上述条件不满足减速；3）量化的Metal后端存在“并行”验证串行化的效应，是部分配置减速的关键原因。
- 方法局限性：仅针对Apple-silicon消费级笔记本研究，未覆盖其他硬件；仅测试五个后端配置，未深入分析更多参数影响；未优化存在串行化效应的后端实现。
- 未来工作：论文未明确提及，推测可扩展至更多硬件平台、优化后端消除串行化效应、探索更多配置参数提升加速效果。

> ✅ **总结一句话**：该论文通过从零实现的跨设备speculative decoding方案，在消费级Apple-silicon硬件上完成实证研究，验证了其分布等价性，量化了硬件相关的串行化效应，明确了加速必要条件，最优配置实现1.61×的wall-clock加速。

</details>

---

### 12. [FUSAR-R1: A Large-Scale Reasoning Model for Intelligent Interpretation of SAR Images](https://arxiv.org/abs/2607.16819v1)

**Authors**: Yi Yang, Xiaokun Zhang, Yuxuan Li, Ruyi Zhang, Xinpeng Zhou, Haipeng Wang  
**Category**: cs.AI  
**Published**: 2026-07-21  
**Score**: 73.0  
**Type**: new  
**ArXiv ID**: 2607.16819v1  

#### Abstract
In recent years, large-scale vision-language models have been driving a paradigm shift in intelligent remote sensing image interpretation. By incorporating textual semantic information, the cognitive expression, semantic understanding, and human-computer interaction capabilities of interpretation mo...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：FUSAR-R1: A Large-Scale Reasoning Model for Intelligent Interpretation of SAR Images
1. 论文的主要贡献和创新点
✅ 解决的问题
SAR图像受相干成像机制、复杂散射特性、散斑噪声干扰、目标背景耦合等影响，特征复杂多变，存在显著不确定性与特殊性；现有SAR视觉语言模型存在缺陷：一是不具备人类专家的逐步分析、逻辑判断能力，二是缺乏自我修正能力，难以支撑复杂场景下的可靠智能解释。
🚀 提出的新方法与思路
**显式思维链推理数据构建**：模拟人类专家的SAR图像解释过程，构建显式思维链推理数据，用于指导指令学习，赋予模型基础推理能力。
**强化学习策略优化**：引入强化学习策略，基于推理结果优化模型输出，实现模型的自我修正，提升推理的可靠性。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| SAR解释任务性能 | 在目标检测、目标计数与分类、土地覆盖类别识别等各类SAR解释任务上，持续优于现有多模态大模型 |
| 推理能力与可靠性 | 具备人类专家的逐步分析、逻辑判断能力，可实现自我修正，适配SAR图像的复杂特性 |
2. 核心实验方法和设置
📚 使用的数据集
论文未报告
🎯 实验设置与评估指标
论文未报告
⚔️ 基线方法对比
论文未报告
3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能**：论文未报告
**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot 迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告
4. 关键结论和发现
- 主要发现：1. FUSAR-R1通过构建显式思维链推理数据结合指令学习，赋予模型基础推理能力；2. 引入强化学习策略实现模型输出优化与自我修正，提升了推理可靠性；3. 该模型在各类SAR解释任务上的性能优于现有多模态大模型。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：FUSAR-R1是针对SAR图像智能解释提出的大尺度推理模型，通过模拟专家解释过程构建显式思维链推理数据指导指令学习，并结合强化学习实现模型的自我修正，在各类SAR解释任务上性能优于现有多模态大模型，具备更强的逻辑推理能力与可靠性。

</details>

---

### 13. [ColGraphRAG: Late-Interaction Evidence Retrieval for Multimodal GraphRAG](https://arxiv.org/abs/2607.16208v1)

**Authors**: Seonok Kim  
**Category**: cs.AI  
**Published**: 2026-07-21  
**Score**: 71.5  
**Type**: new  
**ArXiv ID**: 2607.16208v1  

#### Abstract
Graph-grounded multimodal question answering organizes text, tables, and images in a structured evidence graph, yet end-to-end accuracy depends on which multimodal assets are ranked highly enough to enter downstream reasoning; for graph-linked images, single-vector bi-encoder similarity can discard ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# ColGraphRAG: Late-Interaction Evidence Retrieval for Multimodal GraphRAG
1. 论文的主要贡献和创新点
✅ 解决的问题
Graph-grounded多模态问答依赖结构化证据图中各节点的排序保证端到端准确率，传统单向量双编码器相似度在排序graph-linked图像节点时，会丢失细粒度对齐所需的patch与token级结构，导致有效视觉证据被丢弃，影响最终QA结果。

🚀 提出的新方法与思路
**Late-Interaction MaxSim-style Multi-Vector Scoring**：替换GraphRAG中原对graph-linked图像节点的视觉候选排序算子，采用ColBERT/ColPali谱系的Late-Interaction MaxSim式多向量评分；离线图构建、文本与表格侧检索、结构化提取、下游推理等其余模块保持不变。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| graph-linked图像候选检索 | 保留patch和token级细粒度结构，避免丢失有效视觉证据，提升检索阶段表现 |
| 下游多模态QA性能 | 视觉证据重要场景有明显增益，仅文本主导问题表现趋势混合 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| MultimodalQA | 评估本文方法替换视觉候选排序算子后的检索效果与下游QA性能 |

🎯 实验设置与评估指标
任务：Graph-grounded多模态问答
| 指标 | 含义 |
| --- | --- |
| 论文未报告 | graph-linked图像候选的检索阶段点估计变化情况 |
| 论文未报告 | 下游QA任务性能变化情况 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 原GraphRAG基线 | 多模态GraphRAG | 采用单向量双编码器对graph-linked图像节点进行视觉候选排序 |
| ColGraphRAG（本文方法） | 改进型多模态GraphRAG | 采用Late-Interaction MaxSim-style多向量评分替换原视觉候选排序算子，其余模块与原GraphRAG一致 |

3. 主要实验结果和性能指标
📊 定量结果汇总
所有实验均：论文未报告

💡 结论：论文未提供具体实验数值，仅指出在MultimodalQA数据集上，替换视觉候选排序算子为Late-Interaction多向量评分后，视觉证据相关任务有正向收益，文本主导任务表现趋势混合。

4. 关键结论和发现
- 2-3条主要发现：
  1. 替换GraphRAG中graph-linked图像节点的视觉候选排序算子为Late-Interaction MaxSim式多向量评分，可提升该类候选的检索阶段表现，进而优化下游多模态QA性能；
  2. 该改进对视觉证据更重要的场景增益更显著，对文本主导的问题效果呈现混合趋势。
- 方法局限性：当前验证仅基于MultimodalQA数据集，缺乏更广泛的泛化性验证及图层面的细致诊断。
- 未来工作：进行更广泛的方法验证，开展更细致的图层面诊断工作。

> ✅ **总结一句话**：ColGraphRAG通过在多模态GraphRAG中采用Late-Interaction MaxSim-style多向量评分替换传统单向量双编码器的视觉候选排序算子，有效提升了视觉证据相关任务的检索与QA性能，在视觉证据敏感场景增益突出。

</details>

---

### 14. [FlashPDE: A Drop-in Fused Triton Operator Library for Neural PDE Solvers](https://arxiv.org/abs/2607.18020v1)

**Authors**: Peiyu Zang, Bosen Xie, Ruoxiang Xu, Yongqiang Cai  
**Category**: cs.LG  
**Published**: 2026-07-21  
**Score**: 65.5  
**Type**: new  
**ArXiv ID**: 2607.18020v1  

#### Abstract
Physics-Informed Neural Networks (PINNs) solve PDEs by incorporating physical constraints into neural-network training, but large-scale problems are limited by automatic-differentiation memory overhead and inefficient execution of grid-based PDE operators. We present FlashPDE, a drop-in fused operat...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：FlashPDE: A Drop-in Fused Triton Operator Library for Neural PDE Solvers

1. 论文的主要贡献和创新点
✅ 解决的问题：Physics-Informed Neural Networks (PINNs)求解PDE时，大规模问题受自动微分的内存开销、基于网格的PDE算子执行效率低两大核心限制；现有PyTorch有限差分执行方式存在碎片化缺陷，导致执行效率不足。
🚀 提出的新方法与思路
**FlashPDE**：面向网格型科学机器学习设计的即插即用融合算子库，用可微Triton内核替换碎片化的PyTorch有限差分执行逻辑；每个算子整合融合式星型（stencil）评估、解析离散伴随反向传播、边界梯度校正三部分，统一封装在torch.autograd.Function接口下；提供14种可微PDE算子，覆盖1D-3D椭圆型、抛物型、纳维-斯托克斯系统共17种配置，且独立于神经网络架构与训练策略。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 峰值内存使用 | 相比基于坐标的自动微分方法有显著降低 |
| CUDA内核启动次数 | 相比急切模式PyTorch有限差分实现有明显减少 |
| 端到端求解速度 | 在PDE基准测试上有显著提升 |
| 内核级加速 | 单个算子层面有可观的执行速度提升 |
| 数值一致性 | 与PyTorch有限差分参考实现保持数值一致 |
| 兼容性 | 可无缝适配PyTorch生态，不依赖特定神经网络架构与训练策略 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告具体数据集名称，仅使用6个代表性PDE基准测试 | 评估FlashPDE在PDE求解任务中的性能 |
🎯 实验设置与评估指标
任务：评估FlashPDE作为可微PDE算子库在PyTorch生态下求解PDE的内存占用与执行效率性能。
| 指标 | 含义（箭头标方向） |
| --- | --- |
| 峰值内存使用 | GPU运行时的内存占用量，↓越低越好 |
| CUDA内核启动次数 | 运行过程中调用GPU内核的总次数，↓越低越好 |
| 端到端求解时间 | 完成PDE求解任务的总耗时，↓越低越好 |
| 内核级加速 | 单个PDE算子的执行速度提升倍数，↑越高越好 |
| 数值一致性 | 输出结果与PyTorch有限差分参考实现的匹配程度，要求满足数值误差在允许范围 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 基于坐标的自动微分 | 基础自动微分方法 | 传统PINN常用的自动微分方式，内存开销较大 |
| 急切模式PyTorch有限差分实现 | PyTorch原生有限差分实现 | PyTorch现有的有限差分执行方式，存在碎片化执行缺陷，效率不足 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未提供带表号/图号的结构化实验表格，仅在摘要中提及性能提升的定性描述，无对应量化细节的表格式支撑；指定的5类实验（主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）均未以结构化形式报告。
💡 结论：论文提及FlashPDE在PDE求解任务中相比基线方法有性能优势，但具体结构化实验数据未以表格式呈现。

4. 关键结论和发现
- 主要发现：① FlashPDE的可微融合算子设计有效解决了PINN求解大规模PDE时的内存与执行效率痛点；② FlashPDE在PDE任务中相比现有方法实现了可观的性能提升，且能保持数值一致性；③ FlashPDE架构兼容性强，可适配PyTorch生态，不依赖特定神经网络组件。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：FlashPDE是面向网格型科学机器学习的即插即用可微Triton算子库，可提升PINN求解PDE时的内存与执行效率，且兼容PyTorch生态。

</details>

---

### 15. [ExpertPlex: A High-Goodput Disaggregated Serving System for MoE LLMs with Adaptive Persistent Kernels](https://arxiv.org/abs/2607.18002v1)

**Authors**: Bingyang Wu, Chao Jin, Zili Zhang, Xinming Wei, Yinmin Zhong, Ruidong Zhu, Chengxu Yang, Xin Jin, Yuliang Liu  
**Category**: cs.DC  
**Published**: 2026-07-21  
**Score**: 64.0  
**Type**: new  
**ArXiv ID**: 2607.18002v1  

#### Abstract
LLMs scale Mixture-of-Experts (MoE) parameters for superior intelligence, but massive weights and dynamic computation impede efficient serving. Existing instance-level prefill-decode disaggregation isolates the phases on separate full-model replicas. As MoE weights grow, each instance may span tens ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

ExpertPlex: A High-Goodput Disaggregated Serving System for MoE LLMs with Adaptive Persistent Kernels
1. 论文的主要贡献和创新点
✅ 解决的问题
- 现有instance-level prefill-decode disaggregation方法将预填、解码相位部署在独立的全模型副本中，随着MoE LLM参数规模增长，每个服务实例需跨数十至数百个GPU，资源分配粒度极粗，预填到解码的比例配置常与实际需求不匹配，导致某一阶段资源过度供给而另一阶段过载。
- 现有prefill-decode colocation的Green Context方案按相位划分每个GPU的资源，且内核执行期间固定相位资源，无法跟踪跨操作或层间路由的专家负载变化，会引发行头阻塞或预留资源闲置；同时按GPU划分相位会使各Phase的本地资源减少，需依赖更宽的并行度和更多通信，还会造成共享网络上预填与解码流量的干扰。

🚀 提出的新方法与思路
**Expert Sharing**：跨预填、解码相位共享MoE专家，消除超95%的重复模型权重，复用动态稀疏计算；同时将轻量注意力模块与MoE解聚，减少注意力通信成本。
**Adaptive Persistent Kernels**：按tile粒度调度动态专家计算，实现高效、隔离的执行。
**Attention-Initiated MoE Communication**：避免网络干扰，实现跨相位通信与计算的重叠。
**Tile-to-Cluster Model**：优化上述机制，以最大化系统goodput。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 服务吞吐量（goodput） | 较现有两类基线服务架构实现显著提升 |
| 模型权重冗余度 | 消除超95%的重复模型权重 |
| 资源调度灵活性 | 支持动态适配跨操作及层间的专家负载变化，避免行头阻塞与资源闲置 |
| 通信效率 | 减少注意力通信成本，实现跨相位通信与计算重叠，降低网络流量干扰 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务：MoE LLM的高效 serving服务性能评估。
| 指标 | 含义（箭头方向） |
| --- | --- |
| goodput | 服务吞吐量，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Instance-level prefill-decode disaggregation | 实例级解聚服务架构 | 预填与解码相位部署在独立的全模型副本，资源分配粒度粗，易出现预填-解码比例配置与需求不匹配的问题 |
| Prefill-decode colocation（Green Context方案） | 同驻式预填-解码解聚 | 按相位划分每个GPU资源，内核期间固定相位资源，无法动态适配资源变化，会引发行头阻塞或资源闲置，且易存在网络流量干扰 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告实验结果对应的表号、图号或章节。

4. 关键结论和发现
- 主要发现：在服务MiniMax-M2.7与GLM-5.1-FP8时，ExpertPlex服务架构的goodput显著优于现有的instance-level prefill-decode disaggregation和prefill-decode colocation方案；Expert Sharing机制能有效降低MoE LLM的重复权重冗余度。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：ExpertPlex通过跨相位共享MoE专家、解聚轻量注意力模块、采用自适应持久内核及优化通信调度机制，有效提升了MoE LLM服务的吞吐量，解决了现有解聚架构的资源浪费与网络干扰问题。

</details>

---

### 16. [OrientSAM: Mitigating Camera-Centric Shortcut in Multimodal Spatial Reasoning via Orientation-Aware Spatial Alignment](https://arxiv.org/abs/2607.17657v1)

**Authors**: Wenxiao Fan, Hang Yin, Kan Li  
**Category**: cs.AI  
**Published**: 2026-07-21  
**Score**: 63.5  
**Type**: new  
**ArXiv ID**: 2607.17657v1  

#### Abstract
Multimodal large language models (MLLMs) still struggle with spatial reasoning that requires perspective transformation. In particular, they often rely on camera-centric cues rather than reasoning from the reference object's viewpoint, leading to systematic errors in non-camera reference settings. I...

---

### 17. [Adaptive Mamba Neural Operators](https://arxiv.org/abs/2607.18043v1)

**Authors**: Zeyuan Song, Zheyu Jiang  
**Category**: cs.LG  
**Published**: 2026-07-21  
**Score**: 62.0  
**Type**: new  
**ArXiv ID**: 2607.18043v1  

#### Abstract
Accurately solving partial differential equations (PDEs) on arbitrary geometries and a variety of meshes is an important task in science and engineering applications. In this paper, we propose Adaptive Mamba Neural Operators (AMO), which integrates reproducing kernels for state-space models (SSMs) r...

---

### 18. [Pailitao-MMSearch: Building Native E-Commerce Multimodal Search Foundation](https://arxiv.org/abs/2607.17499v1)

**Authors**: Xiaohan Ye, Xu Chen, Zihan Gong, Jian Ding, Lianyu Du, Baicheng Chen, Yunmeng Shu, Jingqian Zhao, Zhixiang Zhao, Shuaiqi Jia, Chong Ma, Shuwen Xiao, Xiangheng Kong, Yuan Gao, Jun Song, Jinsong Lan, Xiaoyong Zhu, Bo Zheng  
**Category**: cs.AI  
**Published**: 2026-07-21  
**Score**: 56.5  
**Type**: new  
**ArXiv ID**: 2607.17499v1  

#### Abstract
The evolution of e-commerce has fundamentally transformed how users search for products, shifting from simple text-based keyword queries to complex multimodal interactions that seamlessly combine product images, natural language descriptions, and mixed-intent instructions. However, existing approach...

---

### 19. [EdgeCoInfer: Hierarchical Collaborative Inference for On-Device Multimodal Large Models](https://arxiv.org/abs/2607.17143v1)

**Authors**: Lin Tan, David K. Y. Yau, Songtao Guo  
**Category**: cs.DC  
**Published**: 2026-07-21  
**Score**: 56.0  
**Type**: new  
**ArXiv ID**: 2607.17143v1  

#### Abstract
Modern mobile applications predominantly execute concurrent Multimodal Large Language Models (MLLMs) to provide ubiquitous intelligence. However, satisfying this demand within edge environments faces significant challenges due to multi-task concurrency and strictly coupled hard constraints. To addre...

---

### 20. [Rater State Bias in RLHF Preference Data: An Audit Framework](https://arxiv.org/abs/2607.16195v1)

**Authors**: Elena Kopteva, Vitaliy Hlynianyi-Zhuk  
**Category**: cs.AI  
**Published**: 2026-07-21  
**Score**: 52.0  
**Type**: new  
**ArXiv ID**: 2607.16195v1  

#### Abstract
We identify a structured confound in Reinforcement Learning from Human Feedback (RLHF). Pairwise preference labels are intended to reflect the compared outputs, but they may also reflect the rater's state during annotation. Under sustained stressful or distressing conditions, raters' preferences may...

---

### 21. [Reward-Driven LLM Agent Workflows: Synthesizing POMDP Routing and Self-Correction for Autonomous Decision-Making](https://arxiv.org/abs/2607.17038v1)

**Authors**: Amez Amanj Ali, Kuo-Kun Tseng  
**Category**: cs.AI  
**Published**: 2026-07-21  
**Score**: 48.5  
**Type**: new  
**ArXiv ID**: 2607.17038v1  

#### Abstract
This paper addresses key technical challenges in current large language model (LLM) agent applications, including long-horizon planning, sparse reward attribution, and dynamic environmental interaction, by designing and optimizing an intelligent agent workflow. The proposed architecture is based on ...

---

### 22. [Masked Diffusion Language Models are Strong and Steerable Text-Based World Models for Agentic RL](https://arxiv.org/abs/2607.16204v1)

**Authors**: Darshan Deshpande  
**Category**: cs.AI  
**Published**: 2026-07-21  
**Score**: 47.0  
**Type**: new  
**ArXiv ID**: 2607.16204v1  

#### Abstract
Recent growth in reinforcement learning (RL) has surfaced a need for diverse, specialized training environments. Hand-curated environments with fixed task and reward difficulties become ineffective signals as model performance improves, and sparse rewards over long horizons induce mode collapse on s...

---

### 23. [Enabling Spatially Fine-Grained DVFS in Neural Processing Units for Energy-Efficient LLM Serving](https://arxiv.org/abs/2607.16473v1)

**Authors**: Yuqi Xue, Jerry Wu, Corey Yu, Jian Huang  
**Category**: cs.AR  
**Published**: 2026-07-21  
**Score**: 47.0  
**Type**: new  
**ArXiv ID**: 2607.16473v1  

#### Abstract
As neural processing units (NPUs) evolve rapidly to accommodate the ever-increasing compute demand of large language models (LLMs), their power consumption is becoming a limiting factor. Our study shows that using dynamic voltage and frequency scaling (DVFS) to exploit the service-level objective (S...

---

### 24. [FlowBlock: Wavefront-Parallel Decoding for Self-Correcting Diffusion Language Models](https://arxiv.org/abs/2607.17652v1)

**Authors**: Bing Tian, Haikun Liu, Xiaocheng Zhong, Zhuohui Duan, Zhaokai Luo, Huayi Jin, Zhiyong Wang, Xiaofei Liao  
**Category**: cs.AI  
**Published**: 2026-07-21  
**Score**: 46.5  
**Type**: new  
**ArXiv ID**: 2607.17652v1  

#### Abstract
Block-wise diffusion large language models (dLLMs) decode sequentially at the block level, enabling effective KV-cache reuse across blocks but making inter-block decoding strictly serial. Prior work has attempted to unlock inter-block parallelism through post-training methods, but achieves only mode...

---

### 25. [ST-Veto: Spatio-Temporal Token Veto for Diffusion MLLMs via Taylor Prediction and Visual Grounding](https://arxiv.org/abs/2607.17884v1)

**Authors**: Keuntae Kim, Beomseok Lee, Hyunwoo Kim, Yong Suk Choi  
**Category**: cs.AI  
**Published**: 2026-07-21  
**Score**: 45.5  
**Type**: new  
**ArXiv ID**: 2607.17884v1  

#### Abstract
Vision Language Models (VLMs) achieve strong reasoning with Chain-of-Thought (CoT) prompting but incur high sequential-generation cost, error accumulation, and limited self-correction. Diffusion Multimodal Large Language Models (dMLLMs) unmask tokens in an order-agnostic process, improving efficienc...

---

### 26. [Taurus: Accelerating Out-of-Core Graph Neural Network Inference on Billion-Scale Graphs](https://arxiv.org/abs/2607.17374v1)

**Authors**: Pranjal Naman, Yogesh Simmhan  
**Category**: cs.DC  
**Published**: 2026-07-21  
**Score**: 45.5  
**Type**: new  
**ArXiv ID**: 2607.17374v1  

#### Abstract
Graph Neural Network (GNN) inference on billion-scale graphs is challenging due to the large memory footprint of features and embeddings and high disk I/O costs in out-of-core settings. Existing distributed GNN systems incur high communication times and infrastructure costs, while disk-based GNN sys...

---

### 27. [Reinforcement Learning: From Algorithms To Foundation Models](https://arxiv.org/abs/2607.17560v1)

**Authors**: Zihan Ding  
**Category**: cs.AI  
**Published**: 2026-07-21  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2607.17560v1  

#### Abstract
Reinforcement learning (RL) provides a framework for sequential decision making under explicit objectives. In its classical form, RL studies how an agent should act to maximise long-term reward in a dynamic environment. In richer settings, the problem extends beyond a single agent and fixed environm...

---

### 28. [SpecLA: Efficient Speculative Decoding for Linear-Attention Models](https://arxiv.org/abs/2607.16673v1)

**Authors**: Zhibin Wang, Xuying Han, Zhaohua Yang, Fuliang Liu, Xue Li, Rong Gu, Sheng Zhong, Chen Tian  
**Category**: cs.CL  
**Published**: 2026-07-21  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2607.16673v1  

#### Abstract
Linear-attention models replace the growing KV cache with recurrent states, but autoregressive decoding still reads, updates, and writes these states one token at a time. Speculative decoding can reduce this cost by verifying several draft tokens in one target pass, yet existing speculative systems ...

---

### 29. [SelKV: Selective KV Cache Merging with Per-Token Merge-or-Drop and Attention Compensation](https://arxiv.org/abs/2607.16213v1)

**Authors**: Soumia Bouyahiaoui, Manel Kara laouar, Aicha Boutorh, Mohamed Hadj Ameur  
**Category**: cs.AI  
**Published**: 2026-07-21  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2607.16213v1  

#### Abstract
Large Language Models (LLMs) generate text autoregressively, relying on a key-value (KV) cache whose memory footprint grows linearly with context length, creating a major bottleneck. Recent compression methods mitigate this cost via token merging; however, these approaches often rely on indiscrimina...

---

### 30. [Technical Report: AI-Assisted Gated DeltaNet Optimization on NVIDIA Blackwell](https://arxiv.org/abs/2607.16831v1)

**Authors**: Hyunjun Shin, Jiseung Jang, Jaewoo Maeng, Hyunjun Kim  
**Category**: cs.DC  
**Published**: 2026-07-21  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2607.16831v1  

#### Abstract
AI-assisted GPU programming is often framed as a kernel-generation loop: ask a model to produce faster CUDA code, benchmark the result, and repeat. This case study argues that contest-grade optimization involves more than improving the kernel body. We examine the Agent-Assisted submission by our tea...

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
