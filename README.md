# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-08-18 06:14:25 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [P-PAS: Prefill-Pressure Adaptive Scheduling for Long-Context LLM Serving](https://arxiv.org/abs/2608.15171v1)

**Authors**: Timo S\"amann  
**Category**: cs.DC  
**Published**: 2026-08-18  
**Score**: 87.0  
**Type**: new  
**ArXiv ID**: 2608.15171v1  

#### Abstract
Long-context LLM applications such as retrieval-augmented generation (RAG) and agentic systems often process tens of thousands of input tokens to produce short outputs, making end-to-end request latency an important serving objective. We show that the maximum number of batched tokens (MBT), which co...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

P-PAS: Prefill-Pressure Adaptive Scheduling for Long-Context LLM Serving
1. 论文的主要贡献和创新点
✅ 解决的问题
核心痛点：最大批处理token数（MBT，vLLM的token调度预算控制参数）对延迟的影响具有调度压力依赖性——低压时大token预算更优，高压时小token预算更优，单个静态MBT无法在所有负载场景下取得最优性能；现有静态调度策略未考虑调度压力的动态变化，存在适配性不足的缺陷。

🚀 提出的新方法与思路
**P-PAS（Prefill-Pressure Adaptive Scheduling）**：一种轻量的动态调度策略，核心逻辑是根据并发prefill和decode的状态动态调整token调度预算；低压场景下保留较大的token预算以执行高效的大prefill chunk，调度压力增大时则约束prefill工作以减少对活跃decode的干扰，从而维持低延迟。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 负载适配性 | 可动态适配不同调度压力的负载场景，避免固定MBT无法适配全负载范围的局限 |
| 泛化性 | 论文未报告 |
| 延迟表现 | 跨模型、工作负载、GPU场景下均能维持低端到端请求延迟 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
实验任务为长上下文LLM服务（如检索增强生成、代理系统），处理数万输入token并生成短输出，核心目标为端到端请求延迟。
| 指标 | 含义 |
| --- | --- |
| 端到端请求延迟 | ↓ 越低越好（端到端延迟是核心服务目标） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 固定MBT调度 | 静态调度策略 | 采用固定大小的token调度预算，无动态调整能力 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体的定量实验结果，包括但不限于主benchmark性能、效率对比、跨域迁移、鲁棒性测试及消融实验数据。

4. 关键结论和发现
- 主要发现：
1. 最大批处理token数（MBT）对延迟的影响具有调度压力依赖性，低压下大预算可降低延迟，高压下小预算更优；
2. 预填充块（prefill chunk）大小的效率优势随调度压力变化，低压下大预填充块提升执行效率，高压下小预填充块可减少对活跃解码的干扰；
3. P-PAS通过动态调整调度预算，可在不同负载场景下维持低端到端延迟，规避了固定MBT的局限性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：P-PAS是一种轻量的动态调度策略，通过根据并发预填充和解码状态自适应调整token调度预算，解决了静态MBT无法适配全负载范围导致的端到端延迟问题，在各类模型、工作负载和GPU场景下维持低延迟。

</details>

---

### 2. [Le Critique: Privileged Value Functions for LLM Reinforcement Learning](https://arxiv.org/abs/2608.16739v1)

**Authors**: Siddarth Venkatraman, Matthieu Dinot, Laurence Aitchison  
**Category**: cs.LG  
**Published**: 2026-08-18  
**Score**: 74.5  
**Type**: new  
**ArXiv ID**: 2608.16739v1  

#### Abstract
Reinforcement learning algorithms for Large Language Models (LLMs) are largely distinguished by their variance reduction strategy. Group-relative methods like GRPO reduce gradient variance by sampling multiple rollouts per prompt, but provide only sequence-level credit. Training is also blocked by s...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

### 论文标题：Le Critique: Privileged Value Functions for LLM Reinforcement Learning

---

## 1. 论文的主要贡献和创新点
✅ 解决的问题
- 组相对型LLM-RL方法（如GRPO）通过每个采样多个rollouts减少梯度方差，但仅提供序列级信用，且存在拖后腿rollouts（straggler rollouts）阻碍训练，降低吞吐量并增加离策略性；
- 学习式价值函数理论上可解决上述问题，提供token级优势，但额外的基础设施工程挑战结合无critic方法的实际成功，使得价值函数方法难以融入RL流程（pipeline）。

🚀 提出的新方法与思路
**Privileged Value Functions (PVF)**：提供向RL流程注入额外任务相关token级信号的机制，且不会对策略目标产生偏倚；
**TETHER**：一种基线策略，根据价值函数的准确性自适应地在组相对基线与价值基线之间插值。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 现有组相对方法缺陷解决 | 提供token级信用，避免拖后腿rollouts导致的吞吐量降低、离策略性增加问题 |
| 传统价值函数方法缺陷解决 | 无需额外基础设施工程挑战，可自然融入RL流程 |
| 性能表现 | 在多个推理任务上优于标准价值函数基线，与mean-baseline GRPO相当或更优 |

---

## 2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
论文未报告具体任务类型、具体评估指标及对应规则，仅提及在多个推理任务上开展实验。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| GRPO（mean-baseline） | 组相对RL方法 | 提供序列级信用，存在拖后腿rollouts阻碍训练的问题 |
| 标准价值函数基线 | 学习式价值函数RL方法 | 理论上解决组相对方法缺陷，但实际中受工程成本限制难以应用 |
| 本文PVF策略 | 价值函数增强策略 | 注入任务相关token级信号且不偏倚策略目标 |
| 本文TETHER策略 | 自适应基线策略 | 依据价值函数准确性动态切换基线类型 |

---

## 3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主基准性能：论文未报告
2. 效率对比（FPS/参数量等）：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

---

## 4. 关键结论和发现
- 主要发现：
  1. PVF和TETHER两种策略可稳定提升价值函数RL的性能，显著优于标准价值函数基线；
  2. PVF无需额外基础设施，就能实现价值函数RL的token级优势；
  3. TETHER自适应插值策略可根据价值函数准确性优化RL流程性能。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ 总结一句话：本文针对LLM的RL算法提出PVF和TETHER两种互补策略，解决了组相对方法的序列级信用缺陷和传统价值函数方法的工程瓶颈，在多个推理任务上取得与mean-baseline GRPO相当或更优的性能。

</details>

---

### 3. [GraphLoom: Reliability-Calibrated Graph Evidence Routing for Multimodal KG-RAG](https://arxiv.org/abs/2608.15056v1)

**Authors**: Zafar Ali, Asad Khan, Aalia Malik, Pavlos Kefalas  
**Category**: cs.AI  
**Published**: 2026-08-18  
**Score**: 72.5  
**Type**: new  
**ArXiv ID**: 2608.15056v1  

#### Abstract
Multimodal retrieval-augmented generation (RAG) systems often rely on long unstructured contexts or aggressively expanded evidence graphs, which can introduce noisy evidence, weaken multi-hop reasoning, and increase unsupported generation. We present GraphLoom, a reliability-calibrated multimodal kn...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

GraphLoom: Reliability-Calibrated Graph Evidence Routing for Multimodal KG-RAG
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多模态检索增强生成（RAG）系统存在两类核心痛点：1. 部分方法依赖长非结构化上下文，易引入噪声证据，削弱多跳推理能力；2. 部分方法过度扩展证据图，增加了无支撑生成的风险。现有主流多模态RAG、图检索基线、开源视觉语言基线在答案质量、证据忠实度等方面表现不足，在含大量干扰证据的场景下性能稳定性待提升。

🚀 提出的新方法与思路
**实例级多模态知识图谱构建**：从问题对应的接地场景描述、提取的关系三元组、外部常识知识出发，为每个问题构建专属的实例级多模态知识图谱。
**可靠性感知有界扩展子图检索与路由**：不注入全部检索到的证据，通过分层图内存槽和联合图-序列注意力机制，选择性路由高实用度的证据，同时采用有界扩展机制控制子图规模，避免过度扩展带来的问题。
**交错检索与预算修正检索融合**：将交错检索与预算修正检索结合，在噪声检索条件下实现自适应的多跳证据优化，提升复杂推理场景下的鲁棒性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 答案质量与证据忠实度 | 在答案质量和证据忠实度上，相比强多模态RAG、图检索基线、开源视觉语言基线获得一致提升 |
| MultiModalQA检索性能 | 在MultiModalQA数据集上的检索质量得到改进 |
| 噪声场景稳定性 | 在含大量干扰证据的外部知识检索场景下，性能保持稳定 |
| 方案有效性 | 提供了一种替代长上下文多模态证据注入的可靠性校准图证据路由方案 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| ScienceQA, MultiModalQA, OK-VQA | 评估GraphLoom在多模态问答任务中的性能，验证其在含大量干扰证据池场景下的鲁棒性 |

🎯 实验设置与评估指标
任务为多模态问答任务；评估指标如下：
| 指标 | 含义 |
| --- | --- |
| 答案质量 | 衡量生成答案的准确性（正向指标） |
| 证据忠实度 | 衡量生成内容所依托证据的真实可靠程度（正向指标） |
| 检索质量 | 衡量证据检索的精准度（正向指标） |
| 鲁棒性 | 衡量在干扰证据场景下性能的稳定性（正向指标） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 强多模态RAG | 基线方法 | 现有主流的多模态检索增强生成方案 |
| 图检索基线 | 基线方法 | 基于图结构的现有主流检索方案 |
| 开源视觉语言基线 | 基线方法 | 开源的视觉语言模型基线方案 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能**：论文未报告
**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot 迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告

4. 关键结论和发现
- 主要发现1：GraphLoom提出的可靠性校准图证据路由方案，在答案质量、证据忠实度、MultiModalQA数据集检索质量以及含干扰证据场景下的性能稳定性上，均优于主流基线方法。
- 主要发现2：GraphLoom的方案相比长上下文多模态证据注入，在多模态KG-RAG任务中是更有效的证据注入方式。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：GraphLoom是针对多模态KG-RAG的可靠性校准框架，通过构建实例级多模态知识图谱、可靠性感知子图检索与路由、融合交错与预算修正检索，实现了比主流多模态RAG及相关基线更优的答案质量、证据忠实度及噪声场景下的性能稳定性。

</details>

---

### 4. [DepTGL: A Parallel Framework for Memory-based TGNN Training with Adaptive Temporal Data Dependency Management](https://arxiv.org/abs/2608.16305v1)

**Authors**: Linfang Chen, Zhen Song, Lei Liu, Yu Gu, Yushuai Li, Yanfeng Zhang, Lizhen Cui, Ge Yu, Tianyi Li  
**Category**: cs.DC  
**Published**: 2026-08-18  
**Score**: 67.0  
**Type**: new  
**ArXiv ID**: 2608.16305v1  

#### Abstract
Memory-based Temporal Graph Neural Networks (M-TGNNs) maintain recursively updated node states to capture fine-grained temporal interactions. However, existing distributed frameworks lack effective mechanisms for managing the temporal data dependencies inherent in these models. As a result, they mus...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

DepTGL: A Parallel Framework for Memory-based TGNN Training with Adaptive Temporal Data Dependency Management
1. 论文的主要贡献和创新点
✅ 解决的问题
现有分布式框架针对Memory-based Temporal Graph Neural Networks (M-TGNNs)的训练，缺乏有效管理其固有时序数据依赖的机制，导致必须执行严格的时序更新、产生大量远程同步开销，且在时序事件流倾斜时出现严重的负载不平衡问题。

🚀 提出的新方法与思路
**Hybrid temporal-dependency management scheme**：从数据视角重构M-TGNN的时序依赖管理，通过时序事件缓存辅以选择性依赖驱动通信，平衡通信与缓存开销。
**Gradient-aware cache-synchronization policy**：当模型优化稳定时，自适应抑制边界更新，减少冗余同步。
**Load-aware temporal-pruning strategy**：在时序事件流倾斜导致负载峰值时，消除辅助重放事件，减少冗余数据处理并缓解拖尾者效应。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 训练性能 | 在六个真实时序图上相较SOTA基线取得平均4.99倍的加速比 |
| 同步开销 | 减少冗余同步，平衡通信与缓存开销 |
| 负载均衡 | 缓解时序事件流倾斜场景下的负载不平衡 |
| 冗余数据处理 | 消除辅助重放事件，减少冗余数据处理 |
| 模型精度 | 保持与现有方法相当的精度 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 六个真实时序图 | 评估DepTGL在M-TGNN分布式训练中的性能 |

🎯 实验设置与评估指标
任务：分布式Memory-based Temporal Graph Neural Networks（M-TGNN）的训练
| 指标 | 含义 |
| ---- | ---- |
| 训练加速比 | 模型训练速度提升倍数，↑ 越高越好 |
| 模型精度 | 预测结果的准确程度，保持与基线相当 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 现有SOTA分布式M-TGNN训练框架 | 分布式训练框架 | 存在需严格时序更新、高远程同步开销、时序事件流倾斜时负载不平衡的问题 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（六个真实时序图场景）**
| 指标 | DepTGL结果 | SOTA基线结果 |
| ---- | ---- | ---- |
| 平均训练加速比 | 4.99x ✅ | - |
| 模型精度 | 相当 | 相当 |
💡 结论：在六个真实时序图的分布式M-TGNN训练任务上，DepTGL相较SOTA基线取得平均4.99倍的训练加速，同时维持了与基线相当的精度。

其他实验：
- 效率对比（FPS / 参数量）：论文未报告
- 跨域/zero-shot迁移：论文未报告
- 鲁棒性/扰动测试：论文未报告
- 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. DepTGL通过三类优化策略，有效解决了现有分布式M-TGNN训练框架存在的同步开销大、负载不平衡、冗余数据处理等核心问题；2. 基于六个真实时序图的实验验证了DepTGL在训练效率上的显著优势，且精度与现有方法相当。
- 方法局限性：论文未报告
- 未来工作：论文未明确提及

> ✅ **总结一句话**：DepTGL是针对M-TGNN分布式训练的自适应时序依赖管理框架，通过平衡通信、缓存与负载的多种策略，实现了相较SOTA基线显著的训练效率提升，同时保持模型精度。

</details>

---

### 5. [CEDAR-GRPO: Process-Aware Reinforcement Learning for General Abductive Reasoning in LLMs](https://arxiv.org/abs/2608.14791v1)

**Authors**: Moein Salimi, Danial Parnian, Shaygan Adim, Amirmohammad Ebrahiminasab, Nima Alighardashi, Parsa Gholami, Sahand Akramipour, Mahdi Jafari Siavoshani, Mohammad Hossein Rohban  
**Category**: cs.AI  
**Published**: 2026-08-18  
**Score**: 63.5  
**Type**: new  
**ArXiv ID**: 2608.14791v1  

#### Abstract
Abductive reasoning, often characterized as inference to the best explanation, is central to explanation under uncertainty, from everyday sense-making and investigation to scientific discovery. Yet LLM research has mostly studied abduction through narrow, task-specific benchmarks, making it unclear ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

CEDAR-GRPO: Process-Aware Reinforcement Learning for General Abductive Reasoning in LLMs
1. 论文的主要贡献和创新点
✅ 解决的问题
现有LLM对溯因推理的研究多局限于窄范围、任务特定的基准，无法确定观测到的性能提升是否可跨基准家族迁移；两类核心缺陷：① 仅采用任务特定的训练设置，未关注溯因推理作为可迁移能力的提升；② 未结合过程级的溯因行为设计训练信号。
🚀 提出的新方法与思路
**CEDAR-GRPO**：过程感知的强化学习后训练框架，整合三类奖励信号：最终答案正确性、证据覆盖度、证据到解释的方向性；在4种开源权重LLMs上，采用域中立的混合溯因任务（假设生成、假设选择）完成后训练。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 溯因推理迁移性 | 覆盖11个未见过的跨领域任务，所有测试任务均实现性能提升 |
| 奖励适配性 | 融合溯因推理的内在逻辑设计专属奖励，而非仅依赖最终答案正确性 |
| 过程表现 | 增强模型的溯因行为，包括替代选项探索、对手消除、回溯操作、不确定性标记 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 域中立的混合溯因任务（含假设生成、假设选择） | 用于4种开源权重LLMs的后训练 |
🎯 实验设置与评估指标
任务为在11个未见过的溯因及非溯因任务（涵盖假设选择、缺失事实生成、临床推理等）上评估模型性能；论文未报告具体的评估指标列表及箭头方向。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| CEDAR-GRPO | 提出的后训练框架 | 过程感知RL，结合答案正确性与溯因专属奖励 |
| Base models | 基线 | 未经过后训练的基础LLMs |
| Correctness-only GRPO | 基线 | 仅基于最终答案正确性的GRPO后训练 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告
2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未给出具体表号，仅提及CEDAR-GRPO在所有测试模型的所有未见过任务上均优于基线方法
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：
| 模块名 | RL | Abductive Reward Design | Task Diversity | 迁移性能 |
| --- | --- | --- | --- | --- |
| 完整CEDAR-GRPO | ✅ | ✅ | ✅ | ✅ |
| 无RL | ❌ | ✅ | ✅ | ❌ |
| 无溯因奖励设计 | ✅ | ❌ | ✅ | ❌ |
| 无任务多样性 | ✅ | ✅ | ❌ | ❌ |
💡 结论：消融实验验证了RL机制、溯因专属奖励设计、训练任务多样性均对模型溯因推理的迁移性能有正向贡献。

4. 关键结论和发现
- 主要发现1：CEDAR-GRPO可有效提升LLMs的溯因推理能力，且该能力具备跨未见过任务的可迁移性
- 主要发现2：过程感知的奖励设计（融合答案正确性与溯因专属信号）及训练任务多样性，是实现溯因推理迁移增益的关键因素
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ 总结一句话：CEDAR-GRPO是一种过程感知的强化学习后训练框架，可提升大语言模型的溯因推理能力，且该能力能在多种未见过的跨领域任务中实现迁移。

</details>

---

### 6. [Chronocooked: A Benchmark for Implicit Interval Timing in Reinforcement Learning Agents](https://arxiv.org/abs/2608.16666v1)

**Authors**: Amrapali Pednekar, Alvaro Garrido-Perez, Yara Khaluf, Pieter Simoens  
**Category**: cs.AI  
**Published**: 2026-08-18  
**Score**: 62.5  
**Type**: new  
**ArXiv ID**: 2608.16666v1  

#### Abstract
This paper presents Chronocooked, a reinforcement learning (RL) benchmark suite for studying implicit interval timing in RL agents. Inspired by Overcooked, the suite comprises cooking scenarios that require temporal decision making. The tasks and reward functions are designed such that temporal info...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Chronocooked: A Benchmark for Implicit Interval Timing in Reinforcement Learning Agents
1. 论文的主要贡献和创新点
✅ 解决的问题
现有强化学习领域缺乏专门针对隐式区间时序决策的基准，现有RL agent的时序处理能力存在局限性，难以适配依赖隐式时序的场景（如人类机器人交互、时间相关的人类社会场景），亟需针对性的基准开展研究。

🚀 提出的新方法与思路
**Chronocooked基准套件**：该套件基于Overcooked设计烹饪场景，任务与奖励函数的设计使得时序信息不可观察但对最优性能至关重要；环境保持简单，以支持受控实验和生物合理（biologically plausible）模型的开发。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 任务设计 | 要求隐式时序决策，时序信息不可观察但对性能起关键作用，契合真实场景需求 |
| 环境特性 | 环境设置简单，支持开展可控实验与生物合理模型的验证 |
| 评估体系 | 专门设计评估指标，可用于暴露RL agents在时序能力上的局限性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| Chronocooked基准套件 | 用于研究RL agents的隐式区间时序能力，提供需时序决策的烹饪场景任务 |

🎯 实验设置与评估指标
任务：在Chronocooked的烹饪场景中，RL agents需在时序信息不可观察的情况下做出决策以达到最优性能。
评估指标：论文未报告具体指标名称与含义，仅说明评估指标用于暴露RL agents的时序能力局限性。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| non-recurrent model | 基线方法 | 无循环结构的RL模型 |
| recurrent model | 基线方法 | 含循环结构的RL模型 |
| biologically plausible model | 基线方法 | 符合生物学合理性的RL模型 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告任何定量实验结果，包括主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验等相关结果。

4. 关键结论和发现
- Chronocooked基准套件可用于研究RL agents的隐式区间时序能力，为暴露和解决RL agents的时序处理局限性提供支持。
- 时序感知与处理能力是AI代理适配人类机器人交互、时间依赖人类社会场景的关键，亟需在相关AI代理中整合该能力。
- 方法局限性：论文未报告。
- 未来工作：将时间感知与时序处理整合到AI代理中，拓展其在人类机器人交互、时间依赖人类社会场景的应用部署。

> ✅ **总结一句话**：Chronocooked是专门针对隐式区间时序的强化学习基准套件，为研究和优化RL agents的时序处理能力提供支持，助力适配人类机器人交互等时间相关的AI应用场景。

</details>

---

### 7. [Ask, Condition or Abstain: Reinforcement Learning for Missing-Premise Reasoning](https://arxiv.org/abs/2608.16554v1)

**Authors**: Yongqi Tong, Zhenyu Zhang, Zimi Liu, Kewei Fu, Mingli Song, Haofei Zhang, Junshao Zhang, Hong Zhu, Jiang-Ming Yang, Xin Zhang, Jianshe Li  
**Category**: cs.CL  
**Published**: 2026-08-18  
**Score**: 62.0  
**Type**: new  
**ArXiv ID**: 2608.16554v1  

#### Abstract
Answer-only reinforcement learning (RL) trains reasoning models to solve fully specified problems, but many realistic queries omit a premise needed for a unique answer. In this setting, the useful response is not always refusal: the model should ask for the missing premise, condition its answer on t...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Ask, Condition or Abstain: Reinforcement Learning for Missing-Premise Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
Answer-only RL训练的推理模型仅能处理完全指定的问题，但现实中大量查询缺少得出唯一答案的必要前提，此时模型的合适响应并非仅为拒绝，现有方法未关注这类欠定（underdetermined）任务，无法满足询问缺失前提、条件回答或弃权的处理需求。

🚀 提出的新方法与思路
**Ask-Condition-Abstain Reinforcement Learning (ACA-RL)**：是一个数据增强的强化学习框架，通过推理图引导的流水线将完全指定问题转换为带局部缺口标注的缺失前提训练实例；模型基于5种可观测响应行为的结构化奖励进行训练。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 欠定推理处理 | 支持询问缺失前提、条件回答或弃权的合适响应，避免不恰当的强制回答 |
| 完全指定推理性能 | 保留对完全指定推理任务的竞争力 |
| 基准覆盖类型 | 基准MPB涵盖数学、逻辑、现实世界的缺失前提问题，评估场景贴近现实 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| Missing-Premise Benchmark (MPB) | 包含274个人工验证的实例，涵盖数学、逻辑、现实世界的数学题，用于缺失前提推理任务的评估 |

🎯 实验设置与评估指标
任务为处理欠定推理，即判断问题是否缺少必要前提，并选择询问缺失前提、基于未知量的条件回答或弃权的响应。论文未报告具体评估指标的详细定义及对应表格内容。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Qwen3 | 现有推理模型 | 作为基线对比模型，用于验证ACA-RL的性能提升 |
| Llama | 现有推理模型 | 作为基线对比模型，用于验证ACA-RL的性能提升 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：仅提及在Qwen3和Llama模型上ACA-RL在MPB上持续提升，但未提供对应实验表号及具体数值，无法定位结果来源。
2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 2-3条主要发现：1. ACA-RL框架可有效训练模型处理缺失前提的欠定推理任务，生成询问缺失前提、条件回答或弃权的合适响应；2. ACA-RL在MPB基准上对Qwen3、Llama等现有模型实现持续性能提升，同时保留完全指定推理任务的竞争力；3. 缺失前提推理的NLP评估需关注模型识别任务欠定性及处理不确定性的能力，而非仅聚焦于完全指定问题的回答。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该工作提出ACA-RL数据增强强化学习框架，训练模型在缺失前提的欠定推理场景中生成合适响应，同时保留完全指定推理的竞争力，并发布MPB基准，推动NLP评估关注模型对任务不确定性的识别与处理能力。

</details>

---

### 8. [When Entropy Is Not Enough: Reclaiming Lost Semantics in LLM Output Length Prediction](https://arxiv.org/abs/2608.15592v1)

**Authors**: Feiyang Ren, Shengtao Wen, Lingbing Guo, Yu Tian, Yuanning Cui, Xiang Chen  
**Category**: cs.AI  
**Published**: 2026-08-18  
**Score**: 54.5  
**Type**: new  
**ArXiv ID**: 2608.15592v1  

#### Abstract
Efficient LLM serving is often bottlenecked by the need to pad sequences to a fixed maximum length, and this wastes compute and degrades throughput. Predicting output lengths in advance makes it possible to adopt length-aware scheduling, and this reduces the overhead. This advantage is especially pr...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：When Entropy Is Not Enough: Reclaiming Lost Semantics in LLM Output Length Prediction
1. 论文的主要贡献和创新点
✅ 解决的问题
- 现有LLM输出长度预测方法（如熵引导的token池化）存在核心缺陷：仅以token级熵为主要预测信号，忽略不同token间的语义内容差异，导致重要token被低估、携带少量信息的token被过度重视，损害长度预测的可靠性。

🚀 提出的新方法与思路
**ESTP (Entropy-and-Semantic Token Pooling)**：提出的轻量型框架，核心思路是将token级熵与从LLM预填充阶段自注意力权重导出的基于注意力的重要性分数相结合；该框架复用预填充阶段的激活值，仅增加极小的计算开销，且几乎无额外内存开销。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 预测性能 | 在ForeLen基准上优于基线方法，多数场景下预测准确率更高、误差率更低 |
| 系统级效果 | 集成到长度感知调度器后，可提升端到端LLM serving系统的吞吐量，降低填充比 |
| 开销控制 | 引入的计算延迟极小，无额外显著内存开销 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| ForeLen基准 | 长度预测性能测试 |

🎯 实验设置与评估指标
任务为LLM输出长度预测，评估指标包含预测准确率、误差率，以及端到端系统的吞吐量、填充比（论文未明确指标方向，故不标注）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 熵引导的token池化 | 现有基线方法 | 仅以token级熵为长度预测信号，忽略token间语义内容差异，长度预测可靠性不足 |

3. 主要实验结果和性能指标
📊 定量结果汇总
无明确表号、图号等来源标识的实验结果如下：
1. 主benchmark性能：论文报告ESTP在ForeLen基准上优于基线方法，多数场景下预测准确率更高、误差率更低，无具体数值。
2. 效率对比：论文未报告。
3. 跨域/zero-shot迁移：论文未报告。
4. 鲁棒性/扰动测试：论文未报告。
5. 消融实验：论文未报告。
全部实验的结论：ESTP可有效提升LLM输出长度预测的准确性，且能优化LLM serving系统的吞吐量，同时开销极小。

4. 关键结论和发现
- 主要发现：① 仅依赖token级熵的现有长度预测方法因忽略语义差异，长度预测可靠性不足；② ESTP通过结合熵与自注意力导出的语义重要性，复用预填充阶段的计算资源，实现了低开销的更优长度预测；③ ESTP集成到长度感知调度系统后，可提升LLM serving的整体效率。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：ESTP是轻量型LLM输出长度预测框架，结合token级熵与自注意力的语义重要性分数，在ForeLen基准和端到端LLM serving场景中均展现出更优性能，同时仅引入极小的计算和内存开销。

</details>

---

### 9. [A Unified Mamba--MoE Surrogate for Closed-Loop Simulation and Measurement-Window Forecasting of Inverter Transients](https://arxiv.org/abs/2608.15051v1)

**Authors**: Haoguang Wang, Huy Hoang Le, Akhila Kandivalasa, Christian Moya, Marcos Netto, Guang Lin  
**Category**: cs.LG  
**Published**: 2026-08-18  
**Score**: 54.0  
**Type**: new  
**ArXiv ID**: 2608.15051v1  

#### Abstract
This paper proposes a Mamba surrogate model with mixture-of-experts (MoE) routing to represent the transient dynamics of inverter-based resources. A Mamba surrogate model is a predictive machine learning model built on the Mamba architecture. MoE routing uses a router network to assign data-dependen...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：A Unified Mamba--MoE Surrogate for Closed-Loop Simulation and Measurement-Window Forecasting of Inverter Transients
1. 论文的主要贡献和创新点
✅ 解决的问题
现有方法需两个独立专家模型分别完成逆变器瞬态的闭环仿真与测量窗口预测，存在参数冗余问题；无专家路由的共享Mamba backbone在平衡区附近以外的瞬态动力学任务中，所有输出的预测错误更高。

🚀 提出的新方法与思路
**Unified Mamba-MoE Surrogate**：基于Mamba架构，引入混合专家（MoE）路由与任务条件机制，搭配适配两种预测任务（闭环仿真、测量窗口预测）的目标函数，以及提供预测区间的自适应 conformal layer，构建单模型替代两个独立的专家模型，支持双任务同时执行。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 模型结构 | 单模型替代两个独立专家模型，减少部署成本 |
| 模型参数量 | 参数需求低于Mamba专家对 |
| 预测区间 | 可提供高覆盖率的预测区间 |
| 瞬态预测性能 | 平衡区附近以外的瞬态动力学任务中，所有输出预测错误更低 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 完成逆变器瞬态的闭环仿真与测量窗口预测任务 |

🎯 实验设置与评估指标
任务为逆变器瞬态的闭环仿真与测量窗口预测；评估指标含预测错误、模型参数量、预测区间覆盖率。
| 指标 | 含义 |
| ---- | ---- |
| 预测错误 | 越小越好 ↓ |
| 模型参数量 | 越少越好 ↓ |
| 预测区间覆盖率 | 越高越好 ↑ |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Mamba specialist pair | 基线模型 | 双独立专家模型，分别对应两个预测任务 |
| Shared Mamba backbone without expert routing | 基线模型 | 无MoE路由的单Mamba模型，支持双任务，无专家切换机制 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 提出的Unified Mamba-MoE Surrogate模型可通过单模型同时实现逆变器瞬态的闭环仿真与测量窗口预测，替代两个独立的专家模型。
- 在平衡区附近以外的瞬态动力学任务中，该带MoE路由的模型预测错误低于无MoE路由的共享Mamba backbone。
- 控制器硬件在环仿真验证，仅使用有限测量数据适配共享输出头，可降低保留的预测误差。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：提出的Unified Mamba-MoE Surrogate模型以单模型完成逆变器瞬态的闭环仿真与测量窗口预测，瞬态动力学下预测精度优于无MoE路由的共享Mamba模型，可提供高覆盖率的预测区间，参数需求更少。

</details>

---

### 10. [The Unwritten Benchmark: A New Challenge for Multimodal Machine Learning in Abstract Perceptual Reasoning](https://arxiv.org/abs/2608.14558v1)

**Authors**: Garima Arya Yadav, Nilay Yilmaz, Yezhou Yang  
**Category**: cs.AI  
**Published**: 2026-08-18  
**Score**: 53.5  
**Type**: new  
**ArXiv ID**: 2608.14558v1  

#### Abstract
Current multimodal models have demonstrated remarkable proficiency in recognizing static visual and auditory content. However, their capacity for abstract perceptual reasoning, inferring unseen information from dynamic, generative processes, remains a critical and underexplored frontier. In this pap...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：The Unwritten Benchmark: A New Challenge for Multimodal Machine Learning in Abstract Perceptual Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题：当前多模态模型在静态视觉、听觉内容识别上表现出色，但针对抽象感知推理（从动态生成过程推断未观察到的信息）的能力仍处于未充分探索的前沿，存在研究空白。
🚀 提出的新方法与思路
**The Unwritten Benchmark**：针对多模态模型抽象感知推理能力评估的研究空白，提出新的评估基准，核心任务为acousto-kinematic word inference，要求模型仅通过包含无可见墨水痕迹的手写过程对应的笔刮擦音频和手部动作视频的输入，推断3种书写风格对应的单词，用于探测模型的抽象感知与认知能力。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 抽象感知推理探测 | 聚焦现有多模态模型未充分探索的动态生成过程未观信息推断场景，提供明确的评估任务 |
| 跨模态能力评估 | 可有效评估多模态模型的跨模态因果推理能力及任务所需微运动学的理解程度 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| The Unwritten Benchmark | 用于评估多模态模型在acousto-kinematic word inference任务中的抽象感知推理能力 |
🎯 实验设置与评估指标
任务为acousto-kinematic word inference，要求模型仅通过无可见墨水痕迹的手写过程对应的笔刮擦音频和手部动作视频输入，推断3种书写风格对应的单词；评估指标为有序字母准确率。
| 指标 | 含义（箭头） |
| --- | --- |
| 有序字母准确率 | 正确推断的单词中字母顺序完全匹配的比例，↑越高越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| GPT-4o | 大型多模态机器模型 | 当前领先的多模态模型 |
| Gemini 2.5-Pro | 大型多模态机器模型 | 当前领先的多模态模型 |
3. 主要实验结果和性能指标
📊 定量结果汇总
- 主 benchmark 性能：论文未报告
- 效率对比（FPS / 参数量）：论文未报告
- 跨域 / zero-shot 迁移：论文未报告
- 鲁棒性 / 扰动测试：论文未报告
- 消融实验：论文未报告
💡 结论：人类在该acousto-kinematic word inference任务中表现优异，而当前领先的多模态模型在该任务上性能显著低于人类，均未超过10%，且存在矛盾融合效应，即同时提供音频和视频两种模态输入时，模型性能会下降而非提升。
4. 关键结论和发现
- 2-3 条主要发现：① 当前领先的多模态模型在抽象感知推理任务上与人类存在显著性能差距；② 多模态模型存在矛盾融合效应，多模态输入反而会降低任务性能；③ 现有多模态模型在跨模态因果推理及任务所需微运动学理解上存在根本性不足。
- 方法局限性：现有领先的多模态模型无法有效处理无可见墨水痕迹的动态手写过程推理任务，难以合成互补的感知线索完成抽象感知推理。
- 未来工作：需探索提升多模态模型跨模态因果推理和微运动学理解能力的方法，优化其抽象感知推理性能。
> ✅ **总结一句话**：本文提出了探测多模态模型抽象感知推理能力的新基准The Unwritten Benchmark，发现当前领先的多模态模型在该基准任务上远低于人类水平，且存在矛盾融合效应，暴露了模型在跨模态因果推理和微运动学理解上的不足。

</details>

---

### 11. [The Ethical Decision Head: Operationalizing Normative Ethics in Autonomous Vehicles via Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2608.16710v1)

**Authors**: Thomas Mbrice, Ammar Ali, Sami Mian, Khai Hern Low, Eric Chen, Arshia Aghajani, Wolf Sch\"afer, Amin Shirangi  
**Category**: cs.LG  
**Published**: 2026-08-18  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2608.16710v1  

#### Abstract
As autonomous vehicles (AVs) approach Level 4 and Level 5 operational capability [SAE International, 2018], their on- board decision systems must handle not only safety-critical locomotion but also their subsequent moral weight. This paper details the Ethical Decision Head (EDH), a deep re- inforcem...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：The Ethical Decision Head: Operationalizing Normative Ethics in Autonomous Vehicles via Reinforcement Learning from Human Feedback
1. 论文的主要贡献和创新点
✅ 解决的问题：Level 4/5级自动驾驶车辆（AV）需同时处理安全关键运动控制与道德层面的决策要求，现有研究缺乏将规范伦理学有效转化为AV可训练的道德对齐决策方案、对齐人类实际道德偏好的成熟路径。
🚀 提出的新方法与思路
**Ethical Decision Head (EDH)**：提出一种深度强化学习框架，将伦理推理编码为可微奖励信号，使基于策略梯度的智能体在符合CARLA模拟环境状态表示的碰撞紧急场景中，学习道德对齐的驾驶行为；该框架实例化两种规范伦理学框架：
1. **功利主义框架**：核心为最小化总伤亡；
2. **康德主义框架**：核心为将行驶路径的保持作为绝对命令；
训练采用**Proximal Policy Optimization (PPO)** 算法，基于从200个碰撞-紧急场景的人类偏好标注学习得到的**Bradley-Terry奖励模型**。
🔍 相比现有方法的优势
论文未报告
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 200个碰撞-紧急场景的人类偏好标注 | 为EDH的训练提供人类偏好监督信号，用于学习Bradley-Terry奖励模型 |
🎯 实验设置与评估指标
任务：在CARLA模拟环境的碰撞紧急场景中，训练基于EDH框架的自动驾驶智能体，使其符合规范伦理学要求的道德对齐驾驶行为；
论文未报告评估指标
⚔️ 基线方法对比
论文未报告
3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告
4. 关键结论和发现
- 主要发现：
  1. 规范伦理框架在人类监督下的可学习性存在不对称；康德主义框架可作为管道控制，用于验证训练稳定性、排除基础设施故障的影响；
  2. 碰撞紧急场景中，人类评分者实际奖励自我牺牲的行为，而非功利主义主张的最小化总伤亡；
  3. 基于人类反馈的强化学习（RLHF）在自动驾驶中学习的是人类实际生活中的道德偏好，而非哲学家定义的理论道德规范。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出Ethical Decision Head框架，通过Proximal Policy Optimization结合人类偏好学习的Bradley-Terry奖励模型，实现规范伦理学在自动驾驶中的可操作化，揭示了人类道德理论与实际偏好的偏差，指出RLHF学习的是人类实际生活中的道德而非哲学家定义的理论道德。

</details>

---

### 12. [Interpretable Cross-Lingual Alignment in Small Language Models: Probing Cultural and Pragmatic Reasoning in Japanese-English Bilingual LLMs](https://arxiv.org/abs/2608.14896v1)

**Authors**: Florian Braun  
**Category**: cs.CL  
**Published**: 2026-08-18  
**Score**: 52.5  
**Type**: new  
**ArXiv ID**: 2608.14896v1  

#### Abstract
Large language models work well on English and behave in poorly understood ways on languages typologically far from it. Japanese is a clean example, where evaluation still leans on translation quality and JGLUE-style benchmarks, which roll lexical, syntactic and pragmatic competence into a single sc...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Interpretable Cross-Lingual Alignment in Small Language Models: Probing Cultural and Pragmatic Reasoning in Japanese-English Bilingual LLMs
1. 论文的主要贡献和创新点
✅ 解决的问题
大语言模型在英语上表现良好，但在与英语类型学差异大的语言（如日语）上表现不佳；现有日语相关评估依赖翻译质量和JGLUE-style基准，将词汇、句法和语用能力混合为单一分数，无法处理日语用户常用的特定语用问题（包括敬语、内外群体指代、语境相关礼貌、零指代），这些是通用模型在日语用户面前失效的核心原因。

🚀 提出的新方法与思路
**J-PragEval-v0**：一种最小对（minimal-pair）基准，用于将日语的四种目标语用现象（敬语、隐式主语、内群体指代、间接拒绝）与表面流畅度分离，针对性评估模型的语用推理能力。
**线性探针与教师强制对数概率评估**：结合线性探针（linear probes）和教师强制对数概率评估方法，分析TinySwallow-1.5B模型内部对应四种语用现象的特征信号位置。
**Pragmatic Representation Steering**：一种无参数推理时方法，通过沿着线性探针识别出的类均值差方向修改残差流（residual stream）的激活，调整模型的语用推理行为；其可行性通过对比激活添加基线间接论证，该基线与方法使用相同几何结构，可在有线性信号的区域将探针准确率恢复至逻辑回归的1-2个点内。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 语用能力评估 | 专门针对日语核心语用问题设计，分离了语用表现与表面流畅度，解决了现有混合基准无法单独评估语用能力的缺陷 |
| 模型内部可解释性 | 结合线性探针分析模型内部特征信号的位置与存储方式，明确不同语用现象在模型中的分布差异，提升了跨语言小模型的可解释性 |
| 推理时调整 | 无参数的Pragmatic Representation Steering方法无需微调模型，通过修改激活即可调整语用推理，可行性通过基线对比间接支撑 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| J-PragEval-v0 | 分离日语的四种语用现象（敬语、隐式主语、内群体指代、间接拒绝）与表面流畅度，用于评估日语-英语双语小语言模型的语用推理能力 |

🎯 实验设置与评估指标
任务：探测TinySwallow-1.5B（28层、隐藏大小1536）中对应四种日语语用现象的特征信号位置，评估提出方法的有效性。评估指标：平衡准确率（越高越好）、翻转率（越高越好，指模型根据场景切换正确偏好的比例）、探针准确率（越高越好）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 对比激活添加基线 | 对比基线 | 与Pragmatic Representation Steering使用相同几何结构，用于间接论证该方法的可行性，可将有线性信号区域的探针准确率恢复至逻辑回归的1-2个点内 |
| 逻辑回归 | 线性信号基准 | 作为对比的线性模型，用于衡量探针和基线方法的准确率上限 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**TinySwallow-1.5B中四种日语语用特征的线性探针结果**
| 语用现象 | 层/标记位置 | 平衡准确率 | 翻转率 | 核心说明 |
| --- | --- | --- | --- | --- |
| 敬语寄存器 | 第15层（残差流） | 0.96 | 0.93 | 存在清晰的线性信号 |
| 隐式主语 | 最终提示token | 0.48 | 0.77 | 最终提示标记处无法线性解码，对比信号在生成过程中处理 |
| 内群体指代 | 最终提示token | 0.38 | 0.79 | 最终提示标记处无法线性解码，对比信号在生成过程中处理 |
| 间接拒绝 | - | 0.95 | 0.43 | 在长度归一化教师强制下翻转率降至0.43，因J-PragEval-v0的最小对混淆了礼貌与续篇长度 |

💡 结论：TinySwallow-1.5B中不同日语语用现象的信号存储与处理方式存在显著差异，敬语信号集中在残差流第15层，隐式主语和内群体指代的信号在生成过程中处理，间接拒绝的信号受续篇长度混淆影响。

其他实验（主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）：论文未报告。

4. 关键结论和发现
- 主要发现：① TinySwallow-1.5B中四种日语语用现象的信号位置与处理机制不同，敬语的线性信号集中在残差流第15层，隐式主语和内群体指代的对比信号在生成过程中而非提示处存储，间接拒绝的信号受续篇长度与礼貌的混淆影响；② Pragmatic Representation Steering的对比激活添加基线可在有线性信号的区域将探针准确率恢复至逻辑回归的1-2个点内，间接支撑了该方法的可行性；③ 现有JGLUE类基准无法分离日语的语用能力与表面流畅度，需J-PragEval-v0这类专门的基准来评估。
- 方法局限性：Pragmatic Representation Steering的可行性仅通过间接论证，未进行实际演示；J-PragEval-v0中间接拒绝项的最小对混淆了礼貌与续篇长度，导致翻转率结果下降。
- 未来工作：将Pragmatic Representation Steering方法扩展至Llama-3.1-Swallow-8B模型。

> ✅ **总结一句话**：该论文提出针对日语语用推理的基准J-PragEval-v0和无参数推理调整方法Pragmatic Representation Steering，分析了小型日语-英语双语大模型中四种语用现象的内部信号特性，为跨语言小模型的语用可解释性研究提供了新的思路。

</details>

---

### 13. [Toward AI-Friendly Cartography: Understanding How Color Design Influences Foundation Model Spatial Reasoning on Sequential Choropleth Maps](https://arxiv.org/abs/2608.15736v1)

**Authors**: Yonghe Sun, Zhenjia Liu, Hua Liao, Wenjia Xu, Nai Yang, Weihua Dong, Zhiwei Wei  
**Category**: cs.AI  
**Published**: 2026-08-18  
**Score**: 51.0  
**Type**: new  
**ArXiv ID**: 2608.15736v1  

#### Abstract
Foundation models (FMs) increasingly support multimodal and geospatial reasoning, yet it remains unclear whether cartographic principles designed for human perception are equally effective for machines. Focusing on sequential choropleth maps, we examine how hue palette, color ordering, and lightness...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Toward AI-Friendly Cartography: Understanding How Color Design Influences Foundation Model Spatial Reasoning on Sequential Choropleth Maps
1. 论文的主要贡献和创新点
✅ 解决的问题
现有针对人类感知设计的制图原则是否适用于基础模型（FMs）的地理空间推理尚不明确，缺乏针对顺序choropleth地图的颜色设计（色调调色板、颜色排序、明度对比）对FMs空间推理影响的系统研究，难以支撑面向AI的制图设计。

🚀 提出的新方法与思路
**大规模受控基准驱动的颜色影响研究框架**：构建包含5760张顺序choropleth地图、28800个对应问题的受控基准，覆盖属性识别、空间识别、比较、排序、模式划分五类空间推理任务，评估21种开源和专有多模态FMs；同时开展因子实验分析错误来源，并验证LoRA微调对颜色影响模式的保持性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 研究覆盖维度 | 系统涵盖色调、颜色排序、明度对比三类关键颜色要素对FM空间推理的影响分析 |
| 任务覆盖范围 | 覆盖属性识别、空间识别、比较、排序、模式划分五类地理空间推理任务 |
| 微调效果验证 | 明确LoRA微调对上述颜色影响相对敏感性的保持作用，为模型适配提供参考 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 自主构建的受控序列choropleth地图数据集（含5760张地图、28800个问题） | 用于评估多模态基础模型在不同颜色设计下的空间推理能力，支撑核心研究任务 |

🎯 实验设置与评估指标
任务为评估多模态基础模型在顺序choropleth地图上的五类地理空间推理能力；论文未报告具体评估指标的定义及对应的量化表格，仅在结果部分提及"整体准确率"相关的性能变化。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 21种多模态基础模型（开源+专有） | 基础模型 | 覆盖开源与专有类别，用于系统评估不同模型在不同颜色设计下的空间推理表现 |

3. 主要实验结果和性能指标
📊 定量结果汇总
（注：论文未提供具体结果对应的表号，以下为摘要明确给出的结论）

**主 benchmark 性能**：论文未报告具体量化数值，仅描述影响趋势
💡 结论：色调选择对FM空间推理的影响有限且不一致；破坏顺序颜色排序会显著降低性能，对比较、排序任务的影响尤为突出；降低明度对比持续损害推理能力，超出充分可分性的对比度提升仅带来边际增益；LoRA微调可提高整体准确率，但保持上述颜色要素对FM推理的相对敏感性。

**效率对比（FPS / 参数量）**：论文未报告
💡 结论：论文未报告效率相关对比数据。

**跨域 / zero-shot 迁移**：论文未报告
💡 结论：论文未涉及跨域或zero-shot迁移相关实验。

**鲁棒性 / 扰动测试**：论文未报告
💡 结论：论文未开展鲁棒性或扰动测试相关实验。

**消融实验**：论文未报告对应的消融实验表格，仅提及因子实验结果
💡 结论：因子实验表明，FM的推理错误来源于颜色-图例解码、空间推理、主题属性与空间结构的整合三个环节。

4. 关键结论和发现
- 主要发现：
  1. 面向人类的传统制图原则（顺序颜色排序、充足明度对比）同样适用于机器地图理解，是AI友好制图的核心要点；
  2. 色调选择对多模态基础模型的空间推理影响有限且不一致，在AI友好制图中优先级较低；
  3. 明度对比需达到充分可分性，超出该阈值的对比度提升对FM空间推理的增益极小；
  4. LoRA微调可提升基础模型的地图理解准确率，但不会改变颜色要素对FM空间推理的相对影响模式。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本研究通过构建大规模受控基准，系统分析了顺序choropleth地图的颜色设计对多模态基础模型空间推理的影响，为AI友好型制图设计提供了经验指导与实证依据。

</details>

---

### 14. [SEER: Long-Context Reasoning via Selective Visual-Text Compression](https://arxiv.org/abs/2608.15962v1)

**Authors**: Jiawei Xu, Zhilin Zhai, Jinrui Fang, Ruohan Xu, Mingfei Lu, Yi Zhang, Guanchu Wang, Tianlong Chen, Ying Ding  
**Category**: cs.CL  
**Published**: 2026-08-18  
**Score**: 51.0  
**Type**: new  
**ArXiv ID**: 2608.15962v1  

#### Abstract
Long-context reasoning remains computationally expensive for large language models due to the quadratic complexity of attention over text tokens. Visual-text compression offers a promising alternative by rendering text into images and processing them with vision-language models, often reducing token...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

SEER: Long-Context Reasoning via Selective Visual-Text Compression
1. 论文的主要贡献和创新点
✅ 解决的问题
长上下文推理对大语言模型而言计算成本高昂，源于文本注意力的二次复杂性；现有视觉-文本压缩方法采用统一压缩方式，未考虑查询相关性，可能在需精细提取的区域牺牲精度。

🚀 提出的新方法与思路
**SEER框架**，该框架通过视觉扫描学习选择与查询相关的图像，仅在必要时检索文本内容，结合视觉压缩的高效性与文本推理的精确性；SEER通过在工具交互轨迹上进行监督微调，学习用于选择和检索的自适应工具调用策略。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 压缩策略 | 采用自适应选择而非统一压缩，兼顾查询相关性，在需精细提取时保留精度 |
| 效率与精度平衡 | 保留相对于全文本基线的平均提示词token节省，同时提升提取精度 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 长上下文基准 | 评估模型在长上下文任务上的性能 |

🎯 实验设置与评估指标
任务为长上下文推理相关任务；评估指标包括平均准确率，越高越好。
| 指标 | 含义 |
| --- | --- |
| 平均准确率 | 越高越好 ✅ |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Glyph-9B | 视觉-文本基线 | 现有视觉-文本压缩方法 |
| Qwen3-8B | 大语言模型基线 | 通用大语言模型 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表：LongBench上的平均准确率（长上下文基准场景）**
| 方法 | 平均准确率 |
| --- | --- |
| SEER | 51.11% ✅ |
| Glyph-9B | 48.78% |
| Qwen3-8B | 47.62% |
💡 结论：SEER在长上下文基准LongBench上的平均准确率优于视觉-文本基线Glyph-9B和通用大语言模型基线Qwen3-8B，同时保留了相对于全文本基线的平均提示词token节省优势。

效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验：论文未报告

4. 关键结论和发现
- 2-3 条主要发现
1. SEER通过选择性文本检索提升了提取精度，同时保留了相对于全文本基线的平均提示词token节省；
2. 在长上下文基准LongBench上，SEER的平均准确率优于现有视觉-文本基线Glyph-9B和通用大语言模型基线Qwen3-8B。
- 方法局限性
论文未报告
- 未来工作
论文未报告

> ✅ **总结一句话**：SEER是一种结合视觉压缩效率与文本推理精度的长上下文推理框架，通过自适应选择与查询相关的内容，在长上下文任务上实现了性能提升且保持了计算效率优势。

</details>

---

### 15. [Unifying Graph Neural Networks Through a Common Layer Equation](https://arxiv.org/abs/2608.16097v1)

**Authors**: Sai Karthik Navuluru, Siddhartha Shankar Das, Bo Ni, Hongjie Chen, Yu Wang, Baris Coskunuzer, Nesreen K. Ahmed, Franck Dernoncourt, Mahantesh Halappanavar, Tyler Derr, Ryan A. Rossi, Lakshman Tamil  
**Category**: cs.LG  
**Published**: 2026-08-18  
**Score**: 51.0  
**Type**: new  
**ArXiv ID**: 2608.16097v1  

#### Abstract
Graph neural networks are commonly described through family-specific equations whose notation obscures shared computations and structural differences. We introduce a common layer equation that represents covered architectures through seven components: an update domain, channel set, propagation bank,...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Unifying Graph Neural Networks Through a Common Layer Equation
1. 论文的主要贡献和创新点
✅ 解决的问题
现有图神经网络常用家族特定的方程描述，其符号会混淆共享计算与结构差异，不利于对不同架构的统一理解与分析。

🚀 提出的新方法与思路
**通用层方程（common layer equation）**：提出统一图神经网络的核心框架，其涵盖七种组件：更新域（update domain）、通道集（channel set）、传播库（propagation bank）、逐通道消息映射（per-channel message maps）、通道融合算子（channel-fusion operator）、自我/残差映射（ego/residual map）、更新映射（update map）；通过函数值填充（function-valued fillings），将该通用方程扩展至本地消息传递、注意力机制、谱滤波、全局通信、关系特定通道、高阶域、几何消息等多种场景；通过规范层化简与七个非排他性架构家族的组件分配实现统一的明确可校验；固定槽位准则按计算角色分配操作，定义框架的覆盖边界。
**组件级理论洞察**：提出理论结论，在端点本地消息和节点本地更新条件下，算子支撑约束单层依赖；单层全局混合在所述假设下需要完整的有效算子行。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 架构组织 | 将200多种图神经网络架构纳入通用设计空间，支持组件级别的比较 |
| 架构生成 | 支持生成结构一致的图神经网络架构 |
| 特性关联 | 关联传播选择与过平滑、过压缩、异质性、表达能力等图神经网络关键特性 |
| 问题暴露 | 暴露了将可测量的图属性与任务属性映射到验证组件选择的经验逆问题 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：论文未报告
⚔️ 基线方法对比：论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 提出的通用层方程框架可统一覆盖多种图神经网络架构，将大量已有架构整合至通用设计空间，为架构分析与生成提供基础。
- 该框架建立了传播选择与图神经网络过平滑、过压缩、异质性、表达能力等特性的关联，还提出了有待解决的图/任务属性与组件选择的逆问题。
- 组件级理论洞察揭示了单层图神经网络的依赖约束与全局混合条件。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出通用层方程框架，通过七个标准化组件及函数值填充统一涵盖多种图神经网络架构，实现了架构的可校验统一、组件级分析及与图神经网络关键特性的关联。

</details>

---

### 16. [Pallas: A Proactive KV Cache Migration Framework for LLM Inference in AI-RAN](https://arxiv.org/abs/2608.16477v1)

**Authors**: Tianhang Ding, Jianchun Liu, Hongli Xu  
**Category**: cs.LG  
**Published**: 2026-08-18  
**Score**: 47.5  
**Type**: new  
**ArXiv ID**: 2608.16477v1  

#### Abstract
AI-RAN brings large language model (LLM) serving close to mobile users, but cellular handover can separate an active request from its inference state: the user attaches to a target base station (gNB) while the large and growing key-value (KV) cache remains at the source. Retaining inference at the s...

---

### 17. [Q-First: Attention and Feed-Forward Concurrency at the Smallest Change to the Block](https://arxiv.org/abs/2608.15473v1)

**Authors**: WenJie Fan  
**Category**: cs.DC  
**Published**: 2026-08-18  
**Score**: 47.0  
**Type**: new  
**ArXiv ID**: 2608.15473v1  

#### Abstract
Disaggregated LLM serving puts the KV-cache sweep on memory-optimised hardware and the projections and feed-forward on compute-optimised hardware, then inherits from the decoder block a dependency neither device wants: attention runs first and the feed-forward consumes its output, so within one sequ...

---

### 18. [S2-MoE: Enabling Efficient Self-Speculative Decoding for Mixture-of-Experts on Edge Devices](https://arxiv.org/abs/2608.15018v1)

**Authors**: Haochen Huang, Shengxuan Qiu, Meng Li  
**Category**: cs.AI  
**Published**: 2026-08-18  
**Score**: 46.5  
**Type**: new  
**ArXiv ID**: 2608.15018v1  

#### Abstract
Deploying large language models (LLMs) for inference on edge devices is challenging due to severe memory and bandwidth constraints. While speculative decoding and Mixture-of-Experts (MoE) have been proposed to improve inference efficiency, naively combining them often incurs excessive verification o...

---

### 19. [T-LLM Compiler: Trusted LLM-based Code Optimization and Verification Framework](https://arxiv.org/abs/2608.14953v1)

**Authors**: Zahra Fazel, Sunanda Gamage, Shayan Shirahmad Gale Bagi, Amir H. Ashouri, Tomasz S. Czajkowski, Bryan Chan, Reza Azimi, Yaoqing Gao  
**Category**: cs.AI  
**Published**: 2026-08-18  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2608.14953v1  

#### Abstract
Recent advances in Large Language Models (LLMs) have opened opportunities to apply high-level code transformations to the field of code optimization, and it has since emerged as one of the most fundamental tasks for LLMs to perform; however, at present, LLMs struggle to apply wide-ranging code optim...

---

### 20. [Measuring Reward Hacking and Reasoning-Answer Decoupling Under Position-Confounded Optimization](https://arxiv.org/abs/2608.15445v1)

**Authors**: Suyash Maniyar, Armaan Sandhu, Abhishek Mishra  
**Category**: cs.AI  
**Published**: 2026-08-18  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2608.15445v1  

#### Abstract
When a reward is correct on every training example yet consistent with more than one goal, a model can acquire an unintended one, a failure known as goal misgeneralization. Endpoint accuracy on the training distribution cannot tell the two apart, because solving the task and exploiting a surface fea...

---

### 21. [KV-Rescue: Recovering Reasoning Language Model KV Eviction Loss via Stepwise Interleaving](https://arxiv.org/abs/2608.15797v1)

**Authors**: Minsoo Cheong, Woosang Lim, Vincent-Daniel Yun, Sungjoo Yoo  
**Category**: cs.AI  
**Published**: 2026-08-18  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2608.15797v1  

#### Abstract
KV-cache eviction caps the memory cost of long reasoning traces but is inherently lossy because the model decodes from a partial view of its history. Under aggressive budgets, this not only lowers accuracy but can also cause runaway degeneration, where the model produces incoherent or repetitive tok...

---

### 22. [Probabilistic Circuits as Reasoning Machines in Artificial Intelligence (Part I)](https://arxiv.org/abs/2608.16565v1)

**Authors**: Robert Peharz  
**Category**: cs.AI  
**Published**: 2026-08-18  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2608.16565v1  

#### Abstract
This cumulative habilitation thesis studies probabilistic circuits (PCs) as a powerful and tractable framework for reasoning and learning under uncertainty in artificial intelligence (AI). It first advocates for probability as a core language for AI, emphasizing its connections to logic and informat...

---

### 23. [TRACE-CASH: Trial-History-Conditioned Reinforcement Learning for Adaptive Configuration Exploration in Time-Series CASH](https://arxiv.org/abs/2608.16410v1)

**Authors**: Yu-Han Huang, Yujia Wu, Vincent S. Tseng  
**Category**: cs.LG  
**Published**: 2026-08-18  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2608.16410v1  

#### Abstract
Combined algorithm selection and hyperparameter optimization (CASH) searches a conditional space in which the selected model determines which hyperparameters are active. In time-series forecasting, temporal choices, chronological validation, and costly evaluations further complicate this search. Con...

---

### 24. [TRACE: Trajectory Aware Reasoning for Multi-Turn Adversarial Conversation Evaluation](https://arxiv.org/abs/2608.15594v1)

**Authors**: Md Messal Monem Miah, Adrita Anika, Zhiyuan Yu, Ruihong Huang  
**Category**: cs.AI  
**Published**: 2026-08-18  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2608.15594v1  

#### Abstract
Multi-turn jailbreak attacks have emerged as a critical safety threat to LLMs, as harmful objectives are decomposed across a sequence of apparently benign turns to bypass guardrails. Existing defenses lack the reasoning capacity to identify evolving manipulation patterns, often trading helpfulness f...

---

### 25. [Training and Evaluating Ethical Reinforcement Learning Agents on Per-Episode Distributions](https://arxiv.org/abs/2608.14642v1)

**Authors**: Prabhjyot Singh, Majid Ghasemi, Mark Crowley  
**Category**: cs.LG  
**Published**: 2026-08-18  
**Score**: 41.5  
**Type**: new  
**ArXiv ID**: 2608.14642v1  

#### Abstract
Reinforcement Learning (RL) agents trained on a single reward signal exploit the gap between the designed reward and the intended behavior. This is particularly a problem when we are trying to imbue ethical behavior into RL agents. An agent can look ethical on average while concentrating its violati...

---

### 26. [VARM-Bench: Benchmarking Verifiable Structured Reasoning in Chinese Abusive Speech Moderation](https://arxiv.org/abs/2608.15600v1)

**Authors**: Mingyu Yuan, Shengtao Wen, Lingbing Guo, Zhen Bi, Xiang Chen  
**Category**: cs.AI  
**Published**: 2026-08-18  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2608.15600v1  

#### Abstract
The widespread circulation of abusive online content has increased the need for reliable moderation of Chinese social-media text. Existing Chinese benchmarks support label classification, fine-grained toxicity categorization, and target-aware extraction, but do not provide a unified representation f...

---

### 27. [Why Summaries Turn Neutral: Policy Attribution for Sentiment Drift in Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2608.15530v1)

**Authors**: Mikhail Krasitskii, Alexander Gelbukh, Olga Kolesnikova, Grigori Sidorov  
**Category**: cs.CL  
**Published**: 2026-08-18  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2608.15530v1  

#### Abstract
Reinforcement learning with human feedback (RLHF) aligns LLMs with human preferences, improving summarization fluency and safety, but causes sentiment drift: overly neutral summaries stripped of emotional nuance. We diagnose why RL acts as a sentiment neutralizer and present Policy Attribution, a fr...

---

### 28. [EcoVLA: Energy-Efficient Device-Edge Co-Inference for Vision-Language-Action Models under Real-Time Constraints](https://arxiv.org/abs/2608.15502v1)

**Authors**: Ao Zhou, Bo Dai, Le Yu, Xingyu Liu, Zeyu Hao, Lingkun Long, Chunming Hu, Jianlei Yang  
**Category**: cs.AI  
**Published**: 2026-08-18  
**Score**: 39.5  
**Type**: new  
**ArXiv ID**: 2608.15502v1  

#### Abstract
Vision-Language-Action (VLA) models have emerged as a promising foundation for Embodied AI, but their high inference cost poses significant challenges for deployment in robotic systems. In practice, on-device inference is constrained by limited compute capacity and energy budgets, struggling to simu...

---

### 29. [Every Expert Counts: ExactMoE for Memory-Efficient W4A16 Inference](https://arxiv.org/abs/2608.15383v1)

**Authors**: Amjad Saab  
**Category**: cs.LG  
**Published**: 2026-08-18  
**Score**: 39.5  
**Type**: new  
**ArXiv ID**: 2608.15383v1  

#### Abstract
Sparse mixture-of-experts (MoE) language models reduce arithmetic by activating only a small subset of experts per token, yet deployment still requires storing and moving the full expert bank. We present ExactMoE, an inference design that applies symmetric group-128 four-bit weight quantization only...

---

### 30. [Evaluating Multimodal LLMs across Text and Audio Modalities for Accessible Disaster Assistance](https://arxiv.org/abs/2608.14651v1)

**Authors**: Anuridhi Gupta, Samara Mansoor, Hemant Purohit  
**Category**: cs.AI  
**Published**: 2026-08-18  
**Score**: 36.0  
**Type**: new  
**ArXiv ID**: 2608.14651v1  

#### Abstract
Effective disaster risk communication is a foundational humanitarian challenge, yet current emergency infrastructure fails to meet the needs of individuals with access and functional needs, including hard-of-hearing individuals, pregnant women, mothers with toddlers, and elderly individuals with dem...

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
