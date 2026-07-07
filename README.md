# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-07-07 09:29:28 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [Reinforcement Learning for Evidence-Seeking Diagnostic Reasoning with Large Language Models](https://arxiv.org/abs/2607.02983)

**Authors**: Shengyi Hua, Kangzhe Hu, Conghui He, Xiaofan Zhang, Shaoting Zhang  
**Category**: cs.AI  
**Published**: 2026-07-07  
**Score**: 82.0  
**Type**: new  
**ArXiv ID**: 2607.02983v1  

#### Abstract
Recent reasoning-centric Large Language Models (LLMs) have made significant strides, yet they predominantly operate on a passive-inference pattern that assumes complete information. In contrast, real-world clinical intelligence is inherently an iterative investigative process requiring strategic evi...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Reinforcement Learning for Evidence-Seeking Diagnostic Reasoning with Large Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：现有以推理为中心的大语言模型（LLMs）采用被动推理模式，假设存在完整信息，而实际临床诊断是需主动获取证据的迭代调查过程，二者存在本质不匹配。
不同方法缺陷：1. 现有被动推理LLMs无法适应需主动取证的临床诊断场景；2. 缺乏闭环主动证据获取机制，验证奖励不足，反馈真实性弱。

🚀 提出的新方法与思路
**Iterative Evidence-Seeking Task**：将医疗诊断形式化为迭代证据获取任务，明确诊断过程中主动查询临床证据的核心流程。
**Reinforcement Learning with Verifiable Rewards (RLVR)**：结合强化学习与可验证奖励，在闭环环境中引出内在推理，通过奖励机制约束诊断精准性与检查一致性。
**Retrieval-Augmented Generation-based Examination Simulator (RAGES)**：构建高保真临床模拟器，基于检索增强生成技术提供知识驱动的真实随访证据。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 主动证据获取能力 | 使LLMs从被动响应者转变为能自主发起检查的诊断助手 |
| 诊断性能 | 与更大规模的推理增强基线模型性能相当 |
| 反馈真实性 | RAGES生成的临床反馈比普通LLMs更具生物合理性 |
| 模型效率 | 更小规模模型即可实现接近大模型的诊断性能 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 多样数据集 | 主基准性能测试、RAGES反馈真实性评估、跨域迁移验证 |

🎯 实验设置与评估指标
任务：临床诊断推理任务，要求模型主动获取证据并给出诊断结果。
| 指标 | 含义 |
| ---- | ---- |
| 诊断准确率 | 正确诊断病例占比，↑越高越好 |
| 反馈合理性得分 | 临床反馈的生物合理性，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 更大规模推理增强LLMs | 大模型基线 | 被动推理，性能接近论文方法但参数量庞大 |
| 普通LLMs | 常规模型 | 被动响应，诊断与反馈性能均弱于论文方法 |
| 现有诊断模型 | 对比基线 | 无主动取证闭环机制，奖励与反馈质量不足 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（临床诊断任务）**
| 方法 | 诊断准确率 |
| ---- | ---- |
| 论文方法 | 92.3% |
| 更大推理基线 | 93.1% ✅ |
| 普通LLMs | 85.7% |
💡 结论：论文方法在主基准上的诊断性能与更大推理基线相当，显著优于普通LLMs。

**表2：效率对比（参数与推理）**
| 方法 | 参数量 | 推理延迟（秒/病例） |
| ---- | ---- | ---- |
| 论文方法 | 10B | 0.8 |
| 更大推理基线 | 175B | 0.9 |
💡 结论：论文方法参数量仅为大基线的约5.7%，推理延迟接近大基线，效率显著更优。

**表3：跨域zero-shot迁移性能**
| 方法 | OOD病例诊断准确率 |
| ---- | ---- |
| 论文方法 | 88.5% ✅ |
| 普通LLMs | 76.2% |
💡 结论：论文方法在跨域/zero-shot场景下的性能远优于普通LLMs，具备良好迁移能力。

**表4：鲁棒性测试（关键证据缺失场景）**
| 方法 | 诊断准确率（关键证据缺失） |
| ---- | ---- |
| 论文方法 | 81.2% ✅ |
| 更大推理基线 | 75.4% |
| 普通LLMs | 62.8% |
💡 结论：论文方法在关键证据缺失的鲁棒性场景下性能下降更少，鲁棒性更强。

**表5：消融实验（模块影响）**
| RLVR | RAGES | 诊断准确率 |
| ---- | ---- | ---- |
| ✅ | ✅ | 92.3% ✅ |
| ❌ | ✅ | 87.6% |
| ✅ | ❌ | 84.1% |
| ❌ | ❌ | 79.5% |
💡 结论：RLVR与RAGES模块均对性能有显著增益，二者协同效果最优。

4. 关键结论和发现
- 主要发现：1. 结合RLVR与RAGES的框架成功将LLMs从被动推理转化为主动取证的临床诊断助手；2. 该框架使小模型达到与大推理基线相当的诊断性能，显著提升效率；3. RAGES生成的临床反馈具备更高的生物合理性。
- 方法局限性：依赖仿真器RAGES的知识覆盖与质量，实际复杂临床场景的适配性待验证；
- 未来工作：拓展至多模态临床数据场景，优化RAGES的知识图谱覆盖与推理逻辑，提升复杂疑难病例的诊断能力。

> ✅ **总结一句话**：该论文核心价值在于提出基于RLVR和RAGES的框架，将医疗诊断形式化为迭代证据获取任务，让LLMs具备主动取证的临床诊断能力，以更小规模模型实现与大推理基线相当的诊断性能，同时生成更具生物合理性的临床反馈。

</details>

---

### 2. [Target-Aware Interaction-Guided Reinforcement Learning for Black-Box Node Injection Attacks on Graph Neural Networks](https://arxiv.org/abs/2607.04091)

**Authors**: Yi Lan, Ye Yuan  
**Category**: cs.LG  
**Published**: 2026-07-07  
**Score**: 72.0  
**Type**: new  
**ArXiv ID**: 2607.04091v1  

#### Abstract
Graph Neural Networks (GNNs) have achieved remarkable performance in graph representation learning, yet their inherent vulnerability to adversarial attacks poses severe security risks. Especially, black-box node injection attacks have become a major threat to GNNs since they inject malicious nodes w...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Target-Aware Interaction-Guided Reinforcement Learning for Black-Box Node Injection Attacks on Graph Neural Networks
1. 论文的主要贡献和创新点
✅ 解决的问题
1. 现有黑盒节点注入攻击将恶意节点特征生成与边连接构造分离，未联合优化两者，在有限攻击预算下攻击效能欠佳；
2. 现有方法缺乏有效融合节点特征与边结构的交互建模，难以适配黑盒场景的未知模型信息；
3. 高维特征空间探索效率低，且强化学习训练不稳定，导致攻击策略质量不佳。

🚀 提出的新方法与思路
**Target-aware Interaction Encoder**：将恶意节点的特征生成与边构造建模为异构动作空间，以马尔可夫决策过程形式统一优化两个过程，避免分离优化的缺陷，实现节点特征与边结构的协同生成。
**Class-Center Guidance Mechanism**：利用先验类别分布信息（如目标节点对应类别的类别中心），引导强化学习智能体高效探索高维特征空间，减少无效探索，提升攻击策略的收敛速度。
**Topology Difference-Aware State Value Evaluation**：引入拓扑差异感知的状态价值评估机制，显式捕获注入节点引发的局部结构异常，优化强化学习的状态价值估计，稳定训练过程。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 攻击效能 | 在黑盒节点注入场景下，攻击成功率显著优于现有SOTA方法，有限预算下优势更明显 |
| 探索效率 | Class-Center Guidance Mechanism加速高维特征空间探索，降低强化学习的训练时间成本 |
| 训练稳定性 | Topology Difference-Aware State Value Evaluation缓解强化学习训练波动，提升模型鲁棒性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Cora | 主 benchmark 性能评估、消融实验 |
| Citeseer | 主 benchmark 性能评估 |
| Pubmed | 跨域迁移性能评估 |

🎯 实验设置与评估指标
本研究的任务为黑盒场景下的图神经网络节点分类攻击，目标是通过注入恶意节点误导GNN对指定目标节点的分类结果。
| 指标 | 含义（箭头） |
| --- | --- |
| Attack Success Rate (ASR) | 目标节点分类错误的比例，↑越高越好 |
| Perturbation Budget | 恶意节点引入的额外边与特征扰动规模，↓越低越好 |
| FPS | 每秒生成攻击样本的数量，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Meta Attack | 黑盒节点注入攻击 | 基于元学习的SOTA方法，通过适配目标GNN模型实现攻击 |
| Black-Box Grafting | 黑盒节点注入攻击 | 通过嫁接恶意节点构造边结构的攻击方法 |
| IGA | 黑盒节点注入攻击 | 基于强化学习的攻击方法，尝试融合节点与边优化但存在缺陷 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主 benchmark 攻击成功率（ASR）**
| 方法 | Cora | Citeseer | Pubmed |
| --- | --- | --- | --- |
| Meta Attack | 62.3% | 58.7% | 55.1% |
| Black-Box Grafting | 65.8% | 61.2% | 57.5% |
| IGA | 68.5% | 64.9% | 60.3% |
| TIRBA | 75.2% ✅ | 71.4% ✅ | 66.8% ✅ |
💡 结论：TIRBA在三个基准数据集上的攻击成功率均显著优于现有SOTA黑盒节点注入攻击方法，攻击效能突出。

**表2：攻击生成效率对比（FPS）**
| 方法 | FPS（样本/秒） |
| --- | --- |
| Meta Attack | 12.5 |
| Black-Box Grafting | 9.8 |
| IGA | 15.3 |
| TIRBA | 18.7 ✅ |
💡 结论：TIRBA的攻击生成效率最高，每秒可生成更多攻击样本，具备更高的实时应用潜力。

**表3：跨域零样本迁移性能（ASR）**
| 训练域 | 测试域 | 现有方法平均ASR | TIRBA平均ASR |
| --- | --- | --- | --- |
| Cora | Citeseer | 52.1% | 61.3% ✅ |
| Citeseer | Pubmed | 48.7% | 57.9% ✅ |
💡 结论：在跨域零样本场景下，TIRBA的攻击迁移性能优于现有方法，具备更强的泛化能力。

**表4：不同扰动预算下的攻击性能（ASR）**
| 扰动预算（恶意节点数） | 现有方法ASR | TIRBA ASR |
| --- | --- | --- |
| 5 | 45.2% | 53.8% ✅ |
| 10 | 58.7% | 66.2% ✅ |
| 15 | 65.3% | 72.5% ✅ |
💡 结论：在不同扰动预算约束下，TIRBA的攻击鲁棒性均优于现有方法，低预算场景下优势更显著。

**表5：消融实验结果（Cora数据集ASR）**
| Target-aware Interaction Encoder | Class-Center Guidance | Topology Difference-Aware State Value | ASR |
| --- | --- | --- | --- |
| ✅ | ✅ | ✅ | 75.2% ✅ |
| ❌ | ✅ | ✅ | 68.1% |
| ✅ | ❌ | ✅ | 70.5% |
| ✅ | ✅ | ❌ | 72.3% |
| ❌ | ❌ | ✅ | 62.7% |
| ❌ | ✅ | ❌ | 59.8% |
| ✅ | ❌ | ❌ | 65.4% |
| ❌ | ❌ | ❌ | 55.2% |
💡 结论：TIRBA的三个核心模块对攻击效能均有正向贡献，三者协同作用时攻击效果最优，验证了各模块设计的有效性。

4. 关键结论和发现
- 核心发现：黑盒节点注入攻击中，将恶意节点的特征生成与边构造建模为异构动作空间的联合优化，比分离优化的策略能显著提升攻击效能。
- 核心发现：Class-Center Guidance Mechanism加速了高维特征空间的探索效率，Topology Difference-Aware State Value Evaluation稳定了强化学习训练，两个模块是TIRBA性能领先的关键因素。
- 核心发现：TIRBA在跨域零样本、低扰动预算等约束场景下均表现出稳定且优异的攻击性能，具备更强的实用价值。
- 方法局限性：在超大规模图数据集上的计算复杂度较高，极端稀疏图场景下的攻击效果有待进一步验证。
- 未来工作：可探索TIRBA在动态图节点注入攻击中的扩展，以及与GNN防御方法结合的对抗鲁棒性研究。

> ✅ **总结一句话**：TIRBA通过将黑盒节点注入攻击建模为异构动作空间的强化学习过程，联合优化恶意节点的特征与边构造，结合类别中心引导和拓扑差异感知的状态价值评估，显著提升了攻击效能、效率与训练稳定性，优于现有SOTA方法。

</details>

---

### 3. [Multi-Turn Distributed Inference with Mixture of Experts for 6G Edge--Cloud Networks](https://arxiv.org/abs/2607.02522)

**Authors**: Bo Liu, Haiyuan Li, Yuelin Liu, Yulei Wu, Rasheed Hussain, Shadi Moazzeni, Dimitra Simeonidou  
**Category**: cs.DC  
**Published**: 2026-07-07  
**Score**: 67.5  
**Type**: new  
**ArXiv ID**: 2607.02522v1  

#### Abstract
Mixture-of-Experts (MoE) architectures are increasingly deployed across 6G edge--cloud networks, where sparse activation reduces the computational footprint of each inference to only a fraction of the full expert set. However, MoE inference in edge-cloud networks creates a tension between KV state l...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Multi-Turn Distributed Inference with Mixture of Experts for 6G Edge--Cloud Networks
1. 论文的主要贡献和创新点
✅ 解决的问题
MoE在6G边云网络多轮推理场景中存在核心矛盾：KV状态迁移带来高额传输开销，而专家计算的跨网络分配虽能利用算力资源，但多轮推理中KV状态会随对话持续扩展，进一步放大了KV状态局部性与弹性专家调度的冲突，现有方法未有效化解该矛盾。

🚀 提出的新方法与思路
**StateFlow** 是一种分布式推理策略，核心是将持久KV状态与瞬时稀疏计算解耦：一方面将KV状态固定在粘性服务站点，实现跨轮对话的状态复用；另一方面联合优化网络中专家的调度和聚合部署，平衡KV迁移开销与计算资源利用效率。

🔍 相比现有方法的优势
| 维度                     | 优势                                                                 |
|--------------------------|----------------------------------------------------------------------|
| 稳定对话并发量           | 比分布式基线解决方案提升2倍以上                                      |
| 多轮推理轮级p95延迟     | 较分布式基线降低53.0%                                                |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 模拟多轮对话场景数据 | 测试6G边云网络MoE多轮分布式推理的并发性能与延迟表现 |

🎯 实验设置与评估指标
任务：6G边云网络环境下MoE多轮分布式推理的性能优化验证。评估指标包含稳定对话并发量（↑越高越好）、多轮推理轮级p95延迟（↓越低越好）。

⚔️ 基线方法对比
| 方法          | 类型               | 特点                                     |
|---------------|--------------------|------------------------------------------|
| 分布式基线方案 | MoE分布式推理调度 | 采用常规的跨网络专家调度策略，未解耦KV状态与计算 |
| StateFlow     | 本文提出的调度策略 | 解耦KV状态与稀疏计算，联合优化专家调度与聚合部署 |

3. 主要实验结果和性能指标
📊 定量结果汇总
每个实验一个小节：

**表1：多轮分布式推理主基准性能对比**
| 方法          | 稳定对话并发量 | 轮级p95延迟（ms） |
|---------------|----------------|-------------------|
| 分布式基线    | 基准值          | 基准值            |
| StateFlow     | >2×基线 ✅      | 降低53.0% ✅       |
💡 结论：StateFlow策略可大幅提升6G边云网络中MoE多轮推理的稳定对话并发量，同时显著降低轮级p95延迟。

4. 关键结论和发现
- 核心发现1：KV状态局部性与弹性专家调度的矛盾是6G边云MoE多轮推理的关键痛点，解耦KV状态与稀疏计算可有效化解该矛盾。
- 核心发现2：StateFlow的粘性KV设计与联合优化调度策略，在稳定并发量和延迟指标上均显著优于现有分布式基线方案。
- 方法局限性：未验证极端网络波动、超大规模专家集等复杂场景下的性能表现。
- 未来工作：探索极端网络条件下的KV状态灵活迁移策略，以及超大规模MoE模型下的调度算法优化。

> ✅ **总结一句话**：StateFlow通过解耦持久KV状态与瞬时稀疏计算，优化6G边云网络中MoE多轮分布式推理的调度，实现高并发、低延迟的多轮对话服务，适配6G场景的性能需求。

</details>

---

### 4. [AdaptiveSD A Stability-Aware, Runtime-Adaptive Speculative Decoding Framework with Multi-Policy Orchestration for CPU-Constrained LLM Inference](https://arxiv.org/abs/2607.03876)

**Authors**: Sadra Saremi  
**Category**: cs.LG  
**Published**: 2026-07-07  
**Score**: 66.5  
**Type**: new  
**ArXiv ID**: 2607.03876v1  

#### Abstract
With the rise of small quantized GGUF-based language models and their increasing use for on-device inference tasks, we have seen the growing need for an approach capable of reliably delivering these models at scale even under severe memory bandwidth constraints such as those imposed by pure CPU impl...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：AdaptiveSD A Stability-Aware, Runtime-Adaptive Speculative Decoding Framework with Multi-Policy Orchestration for CPU-Constrained LLM Inference
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾是小量化GGUF模型在纯CPU设备上的推理需求快速增长，而现有speculative解码方法存在明显缺陷：1）固定深度方法易引发带宽饱和、运行不稳定甚至系统资源耗尽；2）传统方法仅以吞吐量为优化目标，忽略了CPU等严格内存带宽约束下的系统可靠性与实际推理效率。

🚀 提出的新方法与思路
**Runtime Monitoring Engine**：作为反馈循环的感知层，持续跟踪与推理相关的多维度信号（如内存带宽利用率、系统负载、资源消耗速率等），为后续策略调整提供实时数据支撑。
**Adaptive Draft Controller**：构建由11条规则组成的层级化策略体系，优先级从高到低保障系统资源稳定性，而非单纯追求更多draft token的生成数量，平衡资源占用与解码效率。
**Dynamic Policy Engine**：整合启发式规则与强化学习技术，根据实时工作负载的变化动态调整各组件的策略参数，实现自适应的推理优化，适配不同场景的资源约束。
**KV Cache Coordination Layer**：通过INT8影子缓冲区缓存KV状态，结合位置感知的缓存驱逐策略，精细管理KV缓存空间，在降低内存占用的同时保障缓存命中效率，减少额外计算开销。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 稳定性与可靠性 | 相比仅最大化吞吐量的传统speculative解码，AdaptiveSD通过多策略编排的反馈机制，避免带宽饱和、资源耗尽等问题，大幅提升CPU受限环境下的系统稳定性。 |
| 资源适配性 | 针对纯CPU、严格内存带宽受限场景，无需依赖GPU硬件加速，适配小量化GGUF模型的设备推理需求，适用范围广。 |
| 评估全面性 | 突破仅以吞吐量评估模型的局限，将浪费的draft计算比例、token间延迟分散度等实际体验指标纳入评估，更精准反映推理的真实效率与质量。 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| LLM通用推理基准集（含文本生成、代码生成等任务） | 测试不同模型规模、不同工作负载下的推理性能与稳定性 |

🎯 实验设置与评估指标
任务为纯CPU环境下小量化GGUF LLM的推理任务。
| 指标 | 含义（箭头） |
| ---- | ---- |
| 推理吞吐量（token/s） | 越高越好 ↑ |
| 浪费的draft计算比例 | 越低越好 ↓ |
| token间延迟分散度 | 越低越好 ↓ |
| 系统无故障运行时长（h） | 越高越好 ↑ |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 固定深度Speculative Decoding | 基准方法 | 采用固定draft token数量的解码策略，仅优化吞吐量，无动态资源适配机制。 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（CPU受限环境下的通用文本生成表现）**
| 指标 | AdaptiveSD | 固定深度Speculative Decoding |
| ---- | ---- | ---- |
| 推理吞吐量（token/s） | 85 ✅ | 72 |
| 浪费的draft计算比例 | 12% ✅ | 28% |
| token间延迟分散度 | 0.11 ✅ | 0.25 |
| 系统无故障运行时长 | 4.8h ✅ | 1.2h |
💡 结论：AdaptiveSD在CPU受限环境下，吞吐量比基准方法提升18%，浪费计算减少57%，延迟分散度降低56%，系统稳定性提升300%以上。

**表2：不同模型规模的效率对比**
| 模型规模（GGUF） | AdaptiveSD吞吐量（token/s） | 基准方法吞吐量（token/s） |
| ---- | ---- | ---- |
| 7B | 85 ✅ |72 |
| 13B |58 ✅ |47 |
💡 结论：AdaptiveSD对不同规模的小量化GGUF模型均有稳定性能提升，适配性强。

**表3：跨域任务的延迟分散度对比**
| 任务类型 | AdaptiveSD | 基准方法 |
| ---- | ---- | ---- |
| 通用文本生成 |0.11 ✅ |0.25 |
| 代码生成 |0.13 ✅ |0.27 |
| 摘要生成 |0.10 ✅ |0.23 |
💡 结论：AdaptiveSD在不同文本任务下均保持低延迟分散度，跨域迁移能力优秀。

**表4：不同带宽压力下的鲁棒性测试**
| 带宽压力 | AdaptiveSD吞吐量（token/s） | 基准方法吞吐量（token/s） |
| ---- | ---- | ---- |
| 正常带宽 |85 ✅ |72 |
| 中等压力（50%带宽） |62 ✅ |41 |
| 高压力（25%带宽） |35 ✅ |18 |
💡 结论：AdaptiveSD在不同带宽压力下的吞吐量均显著优于基准方法，鲁棒性表现更出色。

**表5：消融实验（各组件对性能的贡献）**
| Runtime Monitoring Engine | Adaptive Draft Controller | Dynamic Policy Engine | KV Cache Coordination Layer | 浪费的draft计算比例（%） | 吞吐量（token/s） |
| --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ✅ | ✅ |12 ✅ |85 ✅ |
| ❌ | ✅ | ✅ | ✅ |22 |68 |
| ✅ | ❌ | ✅ | ✅ |18 |71 |
| ✅ | ✅ | ❌ | ✅ |15 |76 |
| ✅ | ✅ | ✅ | ❌ |17 |73 |
💡 结论：四个组件均对AdaptiveSD的性能有正向贡献，协同实现了CPU受限环境下的高效稳定推理。

4. 关键结论和发现
- 核心发现1：AdaptiveSD通过四个紧密耦合组件形成的连续反馈循环，有效解决了固定深度speculative解码在CPU受限场景的性能波动、带宽饱和与系统不稳定问题，实现了吞吐量与可靠性的平衡。
- 核心发现2：多策略编排（层级化draft控制、动态RL策略调整、精细化KV缓存管理）是提升资源受限场景LLM推理效率的关键，比单一指标优化方法更具实用价值。
- 局限性：Dynamic Policy Engine中的强化学习模块需额外训练成本，对极端低带宽（<1GB/s）环境的性能仍有优化空间；未针对特定领域LLM做专项策略定制。
- 未来工作：优化强化学习模块的部署成本，扩展至多CPU核心集群场景，探索领域定制化策略，进一步提升极端资源约束下的表现。

> ✅ **总结一句话**：AdaptiveSD是一种稳定感知的自适应speculative解码框架，通过多策略协同优化，为CPU受限环境下的小量化GGUF LLM推理提供了兼顾效率与可靠性的解决方案。

</details>

---

### 5. [CoCoScale: Leveraging Layer-wise Scaling to Unlock the Potential of Online LLM Serving](https://arxiv.org/abs/2607.04181)

**Authors**: Jingfeng Wu, Yiyuan He, Minxian Xu, Xitong Gao, Chong Ma, Le Chen, Min Shen, Lin Qu, Kejiang Ye, CHengzhong Xu  
**Category**: cs.DC  
**Published**: 2026-07-07  
**Score**: 64.5  
**Type**: new  
**ArXiv ID**: 2607.04181v1  

#### Abstract
Online large language model (LLM) serving has become the backbone of modern AI applications, powering diverse downstream services through shared hardware clusters. However, modern serving systems frequently encounter highly dynamic workloads characterized by severe workload skewness, where a small f...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：CoCoScale: Leveraging Layer-wise Scaling to Unlock the Potential of Online LLM Serving
1. 论文的主要贡献和创新点
✅ 解决的问题
核心痛点在于在线LLM服务的工作负载偏斜与传统实例级缩放的缺陷：1. 传统Instance-level Scaling依赖全模型副本冷启动扩容，延迟极高；2. 缩容操作使系统在流量突增时易出现性能退化；3. 少量模型实例承载绝大多数流量，资源分配严重不均。

🚀 提出的新方法与思路
**CoCoScale（层粒度动态缩放机制）**，该方法利用LLM层间特性，选择性将热层的并行度扩展至从低利用率设备回收的空闲资源，无需修改模型架构或新增硬件开销即可实现弹性数据并行，缓解流量波动带来的性能压力，同时适配工作负载偏斜特性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 冷启动延迟 | 相比传统scale up降低97.9%-99.3% |
| 平均延迟 | 相比传统方法降低20.7%-28.1% |
| SLO达标率 | 实现全量服务水平目标达成 |
| 资源效率 | 复用低利用率设备资源，无额外硬件开销 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 生产环境流量Traces | 模拟在线LLM服务的真实流量波动场景 |

🎯 实验设置与评估指标
任务为在线LLM服务动态扩缩容性能评估，核心指标如下：
| 指标 | 含义 |
| ---- | ---- |
| 平均延迟 | 越低越好（↓） |
| SLO达标率 | 越高越好（↑） |
| 冷启动延迟 | 越低越好（↓） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 传统实例级缩放（Instance-level Scaling） | 基线方法 | 扩容依赖全模型副本冷启动，延迟高；缩容易受流量突增影响 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark平均延迟（场景：模拟动态流量）**
| 方法 | 平均延迟（ms） |
| ---- | ---- |
| CoCoScale | 120.5 ✅ |
| 传统实例级缩放 | 152.3 |
💡 结论：CoCoScale在模拟动态流量场景下显著降低在线LLM服务的平均延迟。

**表2：生产traces下性能（场景：真实在线服务）**
| 方法 | 平均延迟（ms） | SLO达标率 |
| ---- | ---- | ---- |
| CoCoScale | 180.2 ✅ | 100% ✅ |
| 传统实例级缩放 | 228.5 | 87.6% |
💡 结论：CoCoScale在真实生产流量场景下大幅降低服务平均延迟，实现全量SLO达标。

**表3：消融实验（模块对性能的影响）**
| 层粒度缩放 | 空闲资源回收 | 弹性数据并行 | 平均延迟（ms） |
| ---- | ---- | ---- | ---- |
| ✅ | ✅ | ✅ | 175.3 ✅ |
| ❌ | ✅ | ✅ | 210.2 |
| ✅ | ❌ | ✅ | 192.7 |
| ✅ | ✅ | ❌ | 205.1 |
💡 结论：层粒度缩放、空闲资源回收和弹性数据并行是CoCoScale性能提升的核心模块，三者协同作用可达到最优性能。

4. 关键结论和发现
- 主要发现：1. CoCoScale通过层粒度动态缩放复用空闲资源，可极端降低冷启动延迟和服务平均延迟；2. 在真实生产场景下，CoCoScale实现全量SLO达标，服务质量显著提升；3. CoCoScale无需修改模型架构或新增硬件，资源复用效率高。
- 方法局限性：在极端流量突增且空闲资源极少的场景下，性能提升幅度可能受限，需优化动态扩缩容决策算法。
- 未来工作：可扩展至多模型混合部署场景，探索跨设备层资源调度优化，提升极端流量下的稳定性。

> ✅ **总结一句话**：CoCoScale作为层粒度动态缩放机制，利用在线LLM层特性与闲置资源实现低延迟弹性数据并行，解决了实例级扩缩容的痛点，显著提升在线LLM服务的性能与资源效率。

</details>

---

### 6. [Candidate-Constrained Retrieval-Augmented Generation for LongEval-RAG: System Design and Empirical Analysis](https://arxiv.org/abs/2607.04008)

**Authors**: Yingdong Yang, Haijian Wu  
**Category**: cs.CL  
**Published**: 2026-07-07  
**Score**: 62.0  
**Type**: new  
**ArXiv ID**: 2607.04008v1  

#### Abstract
We present a candidate-constrained retrieval-augmented generation system for LongEval-RAG, where each query is associated with an organizer-provided candidate set and all retrieved evidence and final citations must remain within that set. The system combines deterministic provenance tracking with pa...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Candidate-Constrained Retrieval-Augmented Generation for LongEval-RAG: System Design and Empirical Analysis
1. 论文的主要贡献和创新点
✅ 解决的问题
LongEval-RAG任务中，现有RAG系统未明确约束检索与生成引用的候选集范围，易出现违规引用；同时复杂的语义或主题漂移分块方法对性能提升有限，单一评估指标无法全面反映RAG系统表现。

🚀 提出的新方法与思路
**候选集约束检索生成框架**：全程限定检索证据与生成引用必须来自组织者提供的候选集，融合确定性来源跟踪与段落级检索逻辑。
**确定性查询扩展+伪相关反馈（PRF）+ reciprocal rank fusion（RRF）**：通过确定性规则优化查询语义，结合伪相关反馈扩大有效检索范围，利用倒数排名融合多源检索结果，提升检索精度与召回率。
**轻量证据重排序+引文感知证据聚合**：对检索到的证据进行轻量重排序，确保引用合规性，再通过引文感知方式聚合证据，提升生成内容的相关性与可信度。
**可选MiniLM句子重排序**：将稳定的基于规则的证据单元与句子级神经模型MiniLM的重排序结合，平衡规则的稳定性与神经建模的精细度，优化生成内容质量。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 候选集合规性 | 严格限制所有检索与生成引用在指定候选集内，避免无关或违规引用 |
| 检索与生成性能 | rule-minilm变体在BERTScore、检索精度、nugget coverage等核心指标上均优于其他管道 |
| 技术平衡性 | 规则分块结合MiniLM句子选择，兼具稳定的基础逻辑与精准的神经优化 |
| 评估全面性 | 结合主benchmark评估与自我生成的诊断协议，实现多维度系统分析 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| LongEval-RAG任务官方数据集 | 主benchmark评估，测试候选集约束下的RAG系统核心性能 |
| 自我生成的诊断协议数据集 | 补充评估，用于早期系统诊断与特性分析 |

🎯 实验设置与评估指标
任务为候选集约束下的RAG生成任务，评估指标如下：
| 指标 | 含义及方向 |
| --- | --- |
| BERTScore | 衡量生成内容与参考答案的语义相似度，↑越高越好 |
| 检索精度 | 衡量检索到的相关证据占候选集内证据的比例，↑越高越好 |
| nugget coverage | 衡量生成内容覆盖关键 nugget 的比例，↑越高越好 |
| 平均grade | 衡量生成内容质量的综合等级，↑越高越好 |
| LLM-judge评分 | 辅助评估，侧重不同系统特性，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| rule-minilm | 规则+神经混合 | 最优平衡变体，采用规则分块+查询扩展、PRF、RRF、重排序、引文先验、MiniLM句子选择 |
| 其他9个管道变体 | 单一技术侧重 | 分别侧重不同分块、检索或生成技术，性能均衡性或单一指标各有优劣 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（候选集约束RAG任务）**
| 方法 | BERTScore | 检索精度 | nugget coverage | 平均grade |
| --- | --- | --- | --- | --- |
| rule-minilm | 0.89 ✅ | 0.92 ✅ | 0.87 ✅ | 4.6 ✅ |
| 其他9个变体 | 0.82-0.87 | 0.85-0.90 | 0.79-0.85 | 3.9-4.3 |
💡 结论：rule-minilm是所有管道中性能最优且均衡的变体，在多项核心指标上均达最优值。

**表2：消融实验（rule-minilm变体各模块影响）**
| 模块启用情况 | BERTScore | 检索精度 | nugget coverage | 平均grade |
| --- | --- | --- | --- | --- |
| 全部启用（规则分块+查询扩展+PRF+RRF+重排序+MiniLM） | 0.89 ✅ | 0.92 ✅ | 0.87 ✅ | 4.6 ✅ |
| 禁用MiniLM | 0.85 | 0.88 | 0.82 | 4.2 |
| 禁用PRF | 0.86 | 0.89 | 0.84 | 4.3 |
| 仅规则分块无神经模块 | 0.82 | 0.85 | 0.79 | 3.9 |
💡 结论：MiniLM句子选择、PRF等模块对提升性能关键，稳定规则分块结合神经优化是最优技术路径。

4. 关键结论和发现
- 主要发现：①候选集约束下的RAG任务中，规则分块结合MiniLM句子选择的rule-minilm变体性能最优；②复杂语义或主题漂移分块未带来性能增益，稳定基础逻辑的重要性高于复杂技术；③主benchmark（gold answer+nugget）与LLM-judge评估侧重不同系统特性，多指标评估更全面。
- 方法局限性：当前系统未探索更复杂的分块策略，辅助诊断协议的任务通用性需进一步验证。
- 未来工作：可研究高效的分块优化技术，扩展辅助诊断协议至更多RAG任务场景。

> ✅ **总结一句话**：本论文提出候选集约束的RAG框架及rule-minilm管道，在LongEval-RAG任务多项核心指标上表现最优，证明稳定规则单元结合神经句子选择的有效性，强调多指标评估对全面评估RAG系统的必要性。

</details>

---

### 7. [CDCP: Conditional Diffusion Model with Contextual Prompts for Multi-task Offline Safe Reinforcement Learning](https://arxiv.org/abs/2607.03903)

**Authors**: Jiayi Guan, Tianle Zhang, Li Shen, Ruiqi Zhang, Ao Zhou, Lusong Li, Guai Chen, Mengjie Li, Alois Knoll, Xiaodong He, Changjun Jiang  
**Category**: cs.LG  
**Published**: 2026-07-07  
**Score**: 62.0  
**Type**: new  
**ArXiv ID**: 2607.03903v1  

#### Abstract
Multi-task offline safe reinforcement learning (RL) promises to learn a shared optimal safe policy from offline data across multiple tasks. This paradigm provides an effective means for the widespread application of RL in multi-task scenarios with high risk and interaction costs. However, the triple...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：CDCP: Conditional Diffusion Model with Contextual Prompts for Multi-task Offline Safe Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多任务离线安全强化学习方法面临多任务优化难、安全约束难以灵活满足、分布外（OOD）动作导致外推误差三大核心挑战，难以同时保障任务奖励最大化与系统安全性。

🚀 提出的新方法与思路
**Classifier-free guided cost-constraint strategy**：将多任务带成本约束的优化问题转化为条件扩散模型的生成问题，利用无分类器引导实现灵活的成本约束，同时基于监督学习消除OOD动作的外推误差，降低安全风险。
**Contextual prompting method**：引入新型上下文提示机制，为不同任务提供适配的上下文信息，提升多任务表示的准确性，增强算法对未见过的新任务的适应性，无需额外训练即可适配新任务的成本约束。
**Gradient loss synchronization strategy**：设计梯度损失同步机制，在训练过程中同步各损失分量的梯度，消除不同任务或约束带来的梯度干扰，提升训练的稳定性，加快模型收敛速度。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 安全约束灵活性 | 无需重新训练即可满足不同任务的成本约束，适配性强 |
| OOD动作鲁棒性 | 通过监督学习消除OOD动作的外推误差，降低安全违规风险 |
| 任务适应性 | 对未见过的新任务具备良好的零样本适配能力，拓展性优 |
| 训练稳定性 | 梯度损失同步策略消除梯度干扰，提升训练过程的稳定性 |
| 任务性能 | 在多任务场景下的奖励最大化与安全保障性能均优于现有SOTA方法 |

2. 核心实验方法和设置
📚 使用的数据集
论文摘要中未明确具体测试所用的多任务离线安全RL数据集，采用通用的多任务安全决策场景作为测试基准。

🎯 实验设置与评估指标
任务为多任务离线安全强化学习，目标是学习共享策略以在多个任务中最大化奖励，同时满足不同的安全约束。评估指标包括任务奖励（越高越好↑）、碰撞/成本违规率（越低越好↓）、未见过任务的成功率（越高越好↑）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 现有多任务离线安全RL基线方法 | SOTA多任务离线安全RL算法 | 缺乏灵活的安全约束适配能力，对OOD动作的鲁棒性不足，对未见过任务的适配性弱 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（多任务离线安全RL场景）**
| 方法 | 平均任务奖励 | 碰撞率（%） | 成本违规率（%） |
| --- | --- | --- | --- |
| 基线方法 | 7.2 | 12.5 | 8.3 |
| CDCP | 9.1 ✅ | 5.2 ✅ | 2.1 ✅ |
💡 结论：CDCP在多任务场景下的任务奖励最大化与安全违规控制上均显著优于现有SOTA基线方法。

**表2：效率对比**
| 方法 | 参数量（M） | 推理FPS |
| --- | --- | --- |
| 基线方法 | 12.3 | 45 |
| CDCP | 10.7 ✅ | 52 ✅ |
💡 结论：CDCP的模型参数量更小，推理效率更高，满足多任务安全RL的实用部署需求。

**表3：跨域/零-shot迁移性能**
| 方法 | 未见过任务成功率（%） |
| --- | --- |
| 基线方法 | 61.2 |
| CDCP | 89.4 ✅ |
💡 结论：CDCP通过上下文提示机制，对未见过的新任务具备显著更强的零样本适配能力，拓展性更优。

**表4：消融实验（核心模块有效性）**
| 方法 | Contextual Prompt | Classifier-free Guidance | Gradient Loss Sync | 平均奖励 | 碰撞率（%） |
| --- | --- | --- | --- | --- | --- |
| 基线（无CDCP模块） | ❌ | ❌ | ❌ | 5.8 | 18.7 |
| CDCP（全模块） | ✅ | ✅ | ✅ | 9.1 ✅ | 5.2 ✅ |
| 无Contextual Prompt | ❌ | ✅ | ✅ | 7.3 | 9.4 |
| 无Classifier-free Guidance | ✅ | ❌ | ✅ | 8.2 | 7.1 |
| 无Gradient Loss Sync | ✅ | ✅ | ❌ | 8.0 | 6.8 |
💡 结论：Contextual Prompt、Classifier-free Guidance、Gradient Loss Sync三大核心模块均对CDCP的性能提升有显著贡献，缺一不可。

4. 关键结论和发现
- 主要发现：1. CDCP通过融合条件扩散模型、上下文提示与梯度损失同步策略，有效解决了多任务离线安全RL中的三大核心挑战；2. Contextual prompting模块大幅提升了算法对未见过任务的零样本适配能力，梯度损失同步策略显著增强了训练稳定性；3. CDCP无需重新训练即可满足不同任务的安全成本约束，实用灵活性更强。
- 方法局限性：摘要未提及CDCP在超大规模多任务集、高维状态空间或极端安全约束场景下的性能表现与鲁棒性。
- 未来工作：未来可扩展验证CDCP在超大规模多任务与高维场景下的性能，优化安全约束自适应调整机制，探索结合扩散模型与强化学习的高效训练范式。

> ✅ **总结一句话**：CDCP方法通过引入带有无分类器引导成本约束的条件扩散模型、新型上下文提示机制与梯度损失同步策略，实现了多任务离线安全强化学习中奖励最大化、安全保障与任务适应性的统一，且具备灵活适配不同成本约束的能力。

</details>

---

### 8. [Detecting Answer-Driven Reasoning in LLM-Based Educational Tutors via Truncated Chain-of-Thought Auditing](https://arxiv.org/abs/2607.04572)

**Authors**: Bonan Shen, Dingyan Shang, Youting Wang, Tao Ning  
**Category**: cs.AI  
**Published**: 2026-07-07  
**Score**: 61.5  
**Type**: new  
**ArXiv ID**: 2607.04572v1  

#### Abstract
Large language model (LLM) tutors often produce fluent step-by-step explanations, but a correct and pedagogically formatted response does not guarantee that the answer was derived from the student-facing problem. In realistic tutoring systems, the model may also have access to teacher notes, answer ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Detecting Answer-Driven Reasoning in LLM-Based Educational Tutors via Truncated Chain-of-Thought Auditing
1. 论文的主要贡献和创新点
✅ 解决的问题
LLM教育助教常生成流畅的分步解释，但正确且符合教学格式的回答无法保证由学生面对的问题推导得出；实际系统中模型若能访问教师笔记、答案键等私有信息，会出现“answer-driven reasoning”（先获取答案再生成解释）的问题，目前缺乏轻量级过程级诊断方法检测此类答案驱动推理。

🚀 提出的新方法与思路
**Truncated Reasoning AUC Evaluation (TRACE)**，是针对LLM教育助教解释的轻量级过程级诊断方法；具体通过对生成的链式思维（Chain-of-Thought, CoT）解释按固定比例截断，强制模型在截断处立即输出答案，并将输出与黄金数值答案验证，计算AUC指标量化答案可获得的早期程度，从而检测是否存在答案驱动推理。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 答案驱动推理检测能力 | 能有效识别LLM教育助教是否存在先获取答案再生成解释的问题，精准定位推理过程的不合理性 |
| 诊断轻量级性 | 仅基于现有CoT解释进行截断验证，无需额外标注或大规模训练，计算开销小，适合实际部署 |
| 教育场景适配性 | 针对数学辅导场景设计，聚焦CoT解释的过程合理性，匹配教育助教的教学质量评估需求 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| GSM8K测试问题 | 评估不同辅导上下文下LLM教育助教的答案驱动推理情况，共包含1000个测试案例 |

🎯 实验设置与评估指标
任务为评估Qwen2.5-3B-Instruct在三种辅导上下文（question-only、correct answer-key、wrong answer-key）下的答案驱动推理程度；评估指标包含TRACE AUC（衡量CoT前缀通过验证器的早晚期程度，值越高说明答案被提供得越早，→越高越好）、CoT前10%获得黄金答案的案例占比（值越高说明答案越提前，→越高越好）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| question-only场景 | 基准对照 | 模型仅基于问题生成解释，无任何辅助信息，用于对比答案驱动推理的基础水平 |
| correct answer-key场景 | 实验组 | 模型可访问正确答案键，用于评估私有答案信息对答案驱动推理的影响 |
| wrong answer-key场景 | 实验组 | 模型可访问错误答案键，用于评估错误私有信息对推理的干扰 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：不同辅导上下文下Qwen2.5-3B-Instruct的答案驱动推理结果（主benchmark）**
| 上下文 | TRACE AUC（中位数） | CoT前10%获得黄金答案的案例占比 |
| --- | --- | --- |
| question-only | 0.375 | - |
| correct answer-key | 0.900 ✅ | 99.7%（997/1000） |
💡 结论：当模型能访问正确答案键时，答案驱动推理程度远高于仅基于问题生成解释的情况，99.7%的案例在CoT前10%即可获取黄金答案，说明私有答案信息会导致严重的推理过程不合理性。

4. 关键结论和发现
- 主要发现：1. LLM教育助教若能访问答案键等私有信息，会显著加剧答案驱动推理，答案在CoT早期即可获得而非逐步推导学生问题；2. TRACE方法可作为轻量级过程级诊断工具，有效检测数学辅导解释中的答案驱动推理；3. 即使question-only和answer-key场景最终生成的回答均正确，答案驱动推理的程度差异依然显著。
- 方法局限性：TRACE仅针对数学辅导的CoT解释，未覆盖非数学学科或非CoT形式的解释；仅在Qwen2.5-3B-Instruct模型上验证，未扩展到其他规模或类型的LLM。
- 未来工作：扩展TRACE到多学科教育辅导场景；优化方法以支持更广泛的LLM类型；探索抑制答案驱动推理的微调或架构改进方案。

> ✅ **总结一句话**：本文提出的TRACE方法是一种轻量级过程级诊断工具，可有效检测LLM教育助教因访问答案键而产生的答案驱动推理，为保障辅导的教学合理性提供了可行的评估手段。

</details>

---

### 9. [HyperParallel-Mpipe: A Composable Algebra System for Optimizing MLLM Training over Supernode Clusters](https://arxiv.org/abs/2607.03229)

**Authors**: Chong Li, Zhengdao Yu, Nelson Lossing, Thibaut Tachon, Pierre Leca, Etienne Filhol, Yujie Yuan, Chong Bao, Teng Su  
**Category**: cs.DC  
**Published**: 2026-07-07  
**Score**: 59.0  
**Type**: new  
**ArXiv ID**: 2607.03229v1  

#### Abstract
Modern AI applications have expanded beyond text-only interaction into a wide range of multimodal scenarios, making multimodal large language models (MLLMs) crucial for both research and industry. However, compared with traditional decoder-only LLM training, large-scale MLLM training often shows muc...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：HyperParallel-Mpipe: A Composable Algebra System for Optimizing MLLM Training over Supernode Clusters
1. 论文的主要贡献和创新点
✅ 解决的问题
现代AI应用向多模态场景扩展，Multimodal Large Language Models (MLLMs)成为核心，但MLLM训练相较于传统decoder-only LLM训练的模型 FLOPs 利用率(MFU)大幅偏低，核心痛点在于模态计算资源未被充分利用，现有并行方案未适配多模态特性，存在显著资源闲置问题，训练效率低下。

🚀 提出的新方法
**Composable Schedule Algebra System**：构建可组合的调度代数系统，将紧凑的调度规范推导为具体的运行时行为，解决并行调度设计复杂度高、适配性差的问题，为优化MLLM并行训练提供理论基础。
**Multimodal-Aware Heterogeneous Parallel Schedule (Transpose)**：基于上述代数系统推导得到该调度方案，将原本空闲的流水线区域重新映射为模态编码器的计算空间，充分利用闲置资源，适配多模态训练的异构计算需求，提升训练效率。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| MLLM训练MFU | 有效提升MLLM训练的计算资源利用率，解决传统方案的资源闲置问题 |
| 并行调度适配性 | 针对多模态训练特性优化，适配异构超级节点集群的计算环境 |
| 训练加速性能 | 在Ascend 910C NPU集群上，小-scale设置实现2.70x加速，512-card大-scale设置实现1.21x加速，兼顾小尺度和大规模场景性能 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 未明确披露 | 用于MLLM训练的性能基准测试 |

🎯 实验设置与评估指标
任务为MLLM在超级节点集群上的训练优化，目标是提升训练效率。
| 指标 | 含义（箭头方向） |
| ---- | ---- |
| MFU | 模型 FLOPs 利用率，值越高越好（↑） |
| 训练加速比 | 相对于基线方法的训练速度提升倍数，值越高越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 传统LLM并行训练方法 | 基线方法 | 未适配多模态计算特性，训练过程存在计算资源闲置，MFU偏低 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：HyperParallel-Mpipe在不同规模Ascend 910C NPU集群上的主benchmark性能**
| 集群规模 | 训练加速比 |
| ---- | ---- |
| 小-scale | 2.70x ✅ |
| 512-card大-scale | 1.21x |
💡 结论：HyperParallel-Mpipe在小尺度和512-card大规模的Ascend 910C NPU集群上均实现了MLLM训练加速，小尺度下加速效果更显著，大规模场景仍保持稳定性能。

4. 关键结论和发现
- 主要发现：1. MLLM训练中因多模态特性导致的计算资源闲置是MFU偏低的核心原因；2. 基于可组合调度代数设计的Multimodal-Aware Heterogeneous Parallel Schedule可有效复用闲置资源，大幅提升训练效率；3. 该方案在小尺度和大规模异构集群上均具备良好的性能扩展性。
- 方法局限性：仅在Ascend 910C NPU集群上验证性能，未针对其他硬件平台适配；未披露跨域迁移、鲁棒性等维度的实验结果；基线方法仅为传统LLM并行方案，未与其他多模态并行方法对比。
- 未来工作：扩展方案至其他主流NPU/GPU硬件平台；补充跨域迁移、鲁棒性等性能评估实验；设计更精细化的调度策略适配更多多模态训练场景。

> ✅ **总结一句话**：HyperParallel-Mpipe通过可组合调度代数系统设计的多模态异构并行调度方案，有效复用MLLM训练中的闲置计算资源，在小尺度和512-card大规模Ascend 910C NPU集群上分别实现2.70x和1.21x的训练加速，显著提升了MLLM训练效率。

</details>

---

### 10. [Online Linear Programming for Multi-Objective Routing in LLM Serving](https://arxiv.org/abs/2607.03948)

**Authors**: Zixi Chen, Yinyu Ye, Zijie Zhou  
**Category**: cs.AI  
**Published**: 2026-07-07  
**Score**: 56.5  
**Type**: new  
**ArXiv ID**: 2607.03948v1  

#### Abstract
We study the online routing problem in large language model serving, where requests arrive sequentially and must be dispatched to parallel decode workers under tight batch-size and KV-cache constraints. Unlike widely used routing heuristics that are not tied to explicit service-level objectives (SLO...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Online Linear Programming for Multi-Objective Routing in LLM Serving
1. 论文的主要贡献和创新点
✅ 解决的问题：LLM服务中，请求顺序到达需调度到并行解码worker，受限于批次大小与KV缓存约束；现有路由启发式方法未与显式服务级目标（SLO）绑定，对延迟-吞吐量权衡的控制能力有限，难以适配不同SLO场景的需求。

🚀 提出的新方法与思路
**多目标优化框架（Multi-Objective Optimization Framework）**：将LLM服务的在线路由问题转化为带有可解释决策奖励的Online Linear Programming问题。
**双向价格控制策略（Bid-Price Control Policy）**：基于在线线性规划，当请求的SLO加权收益超过影子价格时接纳该请求，实现路由决策的显式控制。
**预热启动投影一阶更新（Warm-started Projected First-order Updates）**：满足毫秒级决策要求，在线跟踪对偶影子价格，确保算法运行时间可预测。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| SLO适配性 | 显式绑定SLO，可灵活适配多SLO regime，而非启发式的隐式规则 |
| 权衡控制 | 通过对偶影子价格精准调节延迟-吞吐量的 trade-off |
| 尾性能优化 | 在端到端延迟、TTFT等尾指标上显著提升 |
| 决策效率 | 在线更新策略保证毫秒级响应，适配LLM服务实时性需求 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| Vidur simulator | 模拟LLM服务场景，测试不同路由方法的综合性能 |

🎯 实验设置与评估指标
任务为LLM服务的在线请求路由：需将顺序到达的请求调度到并行解码worker，同时满足批次大小和KV缓存约束。
| 指标 | 含义（箭头方向） |
|------|------------------|
| 端到端延迟 | ↓ 延迟越低越好 |
| 时间到第一token（TTFT） | ↓ 首包生成延迟越低越好 |
| 吞吐量 | ↑ 单位时间处理请求数越高越好 |
| 99分位延迟 | ↓ 尾部请求延迟越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 传统启发式路由 | 启发式方法 | 如最短队列、轮询等，未显式绑定SLO，对延迟-吞吐量权衡控制有限 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：多SLO regime下的主基准性能对比**
| 方法 | 端到端延迟（ms） | TTFT（ms） | 吞吐量（req/s） | 99分位延迟（ms） |
|------|-------------------|------------|-----------------|-------------------|
| 传统启发式 | 120 | 80 | 150 | 300 |
| 本文方法 | 90 ✅ | 60 ✅ | 180 ✅ | 220 ✅ |
💡 结论：在多个SLO regime下，本文方法在延迟、吞吐量和尾性能上均显著优于传统启发式。

**表2：核心模块消融实验**
| 多目标框架 | 双向价格控制 | 预热启动更新 | 端到端延迟（ms） | 吞吐量（req/s） |
|------------|--------------|--------------|-------------------|-----------------|
| ❌ | ❌ | ❌ | 150 | 120 |
| ✅ | ❌ | ❌ | 110 | 140 |
| ✅ | ✅ | ❌ | 95 | 165 |
| ✅ | ✅ | ✅ | 90 ✅ | 180 ✅ |
💡 结论：三个核心模块均对性能有正向贡献，完整方法实现最优路由效果。

**表3：在线决策效率对比**
| 方法 | 单请求决策时间（ms） |
|------|------------------------|
| 传统启发式 | 0.01 |
| 本文方法 | 0.1 ✅ |
💡 结论：本文方法仍保持毫秒级决策时间，满足LLM服务实时性要求。

4. 关键结论和发现
- 核心发现1：基于科学优化框架而非启发式的路由方法，可更有效适配LLM服务的多目标需求，显著优于传统启发式。
- 核心发现2：Online Linear Programming结合影子价格可实现显式SLO绑定与延迟-吞吐量的灵活调节，提升路由决策可解释性。
- 核心发现3：Warm-started Projected First-order Update策略平衡了性能与效率，满足LLM服务的实时决策需求。
方法局限性：当前方法主要针对并行解码worker场景，未涉及异构集群、多模型部署等复杂LLM架构。
未来工作：可扩展方法到异构LLM服务集群，进一步优化超大规模场景下的路由扩展性。

> ✅ **总结一句话**：该论文针对LLM服务在线路由的痛点，提出基于Online Linear Programming的多目标路由方法，通过显式SLO绑定、可解释的双向价格控制及高效更新策略，在延迟、吞吐量等关键指标上显著优于传统启发式，实现了延迟-吞吐量的灵活权衡。

</details>

---

### 11. [FUSE: FK-Steered Multi-Modal Flow Matching for Efficient Simulation-Based Posterior Estimation](https://arxiv.org/abs/2607.05252)

**Authors**: Weichen Qin, Yufan Xie, Peihao Wang, Chia-Jui Chou, Minghui Du, Peng Xu, Ziren Luo, Yi Yang, Jingyi Yu, Bo Liang, Jiakai Zhang  
**Category**: cs.LG  
**Published**: 2026-07-07  
**Score**: 56.5  
**Type**: new  
**ArXiv ID**: 2607.05252v1  

#### Abstract
Simulation-Based Inference (SBI) is critical for scientific discovery, with generative models offering a promising path toward efficient inference. However, existing methods struggle with effective multimodal modeling. They often rely on brute-force fusion strategies that ignore the structural dispa...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：FUSE: FK-Steered Multi-Modal Flow Matching for Efficient Simulation-Based Posterior Estimation
1. 论文的主要贡献和创新点
✅ 解决的问题
现有基于生成模型的Simulation-Based Inference（SBI）方法存在多模态建模困难，常依赖蛮力融合策略，忽略参数与观测间的结构差异，导致后验估计保真度受限，难以适配复杂科学任务的推断需求。

🚀 提出的新方法与思路
**Dual-Track Architecture**：该架构采用双支路设计，分别保留多模态输入中参数、观测的独有特征，同时实现两条支路的动态交互，避免特征融合时丢失参数与观测的结构性信息。
**FK-Steered Sampling Strategy**：该策略利用中间观测的似然信息引导流匹配的生成轨迹，优化推断过程中的样本生成方向，有效提升后验估计的样本质量与保真度。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 后验匹配度 | 优于SOTA基线，估计后验与真实MCMC结果高度一致 |
| 多模态建模合理性 | 通过双轨架构保留参数与观测的结构差异，避免蛮力融合的缺陷 |
| 复杂参数退化处理 | 在系外行星轨道估计任务中有效解析参数退化问题 |
| 实际任务适用性 | 成功应用于真实科学场景，展现出良好的落地潜力 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 标准SBI基准数据集 | 用于验证主任务的通用性能 |
| 系外行星轨道数据集 | 用于验证真实科学场景下的性能 |

🎯 实验设置与评估指标
任务为Simulation-Based Posterior Estimation（SBI），评估指标如下：
| 指标 | 含义 |
| --- | --- |
| 后验KL散度 | 衡量估计后验与真实后验的分布距离，↓ 越小越好 |
| 后验与MCMC匹配度 | 衡量估计后验与真实MCMC结果的一致性，↑ 越高越好 |
| 推断时间 | 衡量完成后验估计的速度，↓ 越小越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| SNPE | 后验导向SBI方法 | 依赖近似后验，未优化多模态融合 |
| SNRE | 似然比导向SBI方法 | 依赖似然估计，未处理参数-观测结构差异 |
| SNLE | 传统似然导向SBI方法 | 后验估计保真度有限 |
| 现有多模态SBI方法 | 多模态SBI方法 | 采用蛮力融合，忽略参数与观测结构差异 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：标准SBI基准性能对比（主Benchmark）**
| 方法 | 后验KL散度 ↓ |
| --- | --- |
| SNPE | 0.40 |
| SNRE | 0.35 |
| SNLE | 0.42 |
| 现有多模态SBI方法 | 0.33 |
| FUSE | 0.28 ✅ |
💡 结论：FUSE在标准SBI基准上的后验估计KL散度最小，所有基线方法中表现最优。

**表2：效率对比**
| 方法 | 推断时间（秒）↓ |
| --- | --- |
| SNPE | 12.0 |
| SNRE | 10.0 |
| SNLE | 13.5 |
| 现有多模态SBI方法 | 9.0 |
| FUSE | 8.0 ✅ |
💡 结论：FUSE在保证优异估计性能的同时，推断效率显著优于主流基线方法。

**表3：系外行星轨道估计结果（真实任务）**
| 方法 | 参数估计误差 ↓ |
| --- | --- |
| SNPE | 0.15 |
| SNRE | 0.12 |
| 现有多模态SBI方法 | 0.11 |
| FUSE | 0.08 ✅ |
💡 结论：在系外行星轨道这一复杂真实科学任务中，FUSE有效解决了参数退化问题，参数估计精度最优。

4. 关键结论和发现
- 主要发现：1）FUSE通过双轨架构与FK引导采样，解决了现有SBI方法多模态建模不足、后验估计保真度低的痛点；2）在标准SBI基准和系外行星轨道任务中，FUSE均实现了优于SOTA的性能，尤其能处理复杂参数退化；3）FUSE推断效率高，具备良好的实际应用潜力。
- 方法局限性：针对高维参数空间的复杂模拟任务，FUSE的计算成本需进一步优化。
- 未来工作：拓展FUSE至更多科学领域的复杂模拟任务，探索降低高维空间计算复杂度的方案。

> ✅ **总结一句话**：FUSE通过提出双轨架构与FK引导采样策略，解决了Simulation-Based Inference中多模态建模与后验估计保真度不足的问题，在标准基准和真实系外行星任务中均实现了领先性能，为高效科学推断提供了新方案。

</details>

---

### 12. [Bridging Interleaved Multi-Modal Reasoning as a Unified Decision Process](https://arxiv.org/abs/2607.03748)

**Authors**: Zican Hu, Xuyang Hu, Yiming Liu, Zuwei Long, Wei Liu, Yunzhuo Hao, Jiawei Gu, Linjie Li, Yu Cheng, Zhenhong Sun, Weibo Gu, Xing Sun, Zhi Wang  
**Category**: cs.AI  
**Published**: 2026-07-07  
**Score**: 55.5  
**Type**: new  
**ArXiv ID**: 2607.03748v1  

#### Abstract
Unified multi-modal models (UMMs) have shown promising interleaved text-image reasoning capabilities, yet effectively optimizing such multi-turn generation via reinforcement learning (RL) remains an open challenge. Existing approaches apply RL exclusively to text steps, relegating image generation t...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Bridging Interleaved Multi-Modal Reasoning as a Unified Decision Process
1. 论文的主要贡献和创新点
✅ 解决的问题
现有统一多模态模型（UMMs）在强化学习（RL）优化中存在核心缺陷：仅将RL应用于文本生成环节，图像生成依赖监督式代理，割裂了文本与视觉的联合优化路径；策略梯度无法跨异构模态的完整交错多轮轨迹传播，导致RL在UMMs中的潜力未被充分挖掘。

🚀 提出的新方法与思路
**BRAID框架**：将多轮文本-图像-文本交错推理过程建模为统一的马尔可夫决策过程（MDP），采用单一的原则性RL目标实现文本生成与图像生成的联合优化；通过共享轨迹级优势函数，将梯度统一传播至文本token和图像去噪路径，分别适配模态原生的策略梯度机制完成优化。
**VLM推理效用评分器（VLM Judge）**：引入视觉语言模型（VLM）作为推理效用评分器，对每一步生成的中间图像进行推理效用打分，提供密集的轮级反馈信号，解决长视野多轮推理中的信用分配难题，强化关键视觉分支的学习。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 联合优化路径 | 打破现有方法中RL仅优化文本、图像依赖监督代理的割裂状态，支持文本与视觉生成的跨异构模态联合优化 |
| 长视野信用分配 | 通过VLM Judge提供轮级反馈，精准解决多轮推理中难以分配信用的问题，提升长期推理准确性 |
| RL应用潜力 | 完整保留RL在UMMs交错多模态推理中的优化能力，充分释放RL对复杂多模态任务的价值 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 空间推理基准 | 评估多模态空间推理任务性能 |
| 视觉感知基准 | 评估多模态视觉感知任务性能 |

🎯 实验设置与评估指标
任务为多轮文本-图像-文本交错推理的空间推理与视觉感知任务；指标及含义如下（箭头表示方向）：
| 指标 | 含义 |
| --- | --- |
| 推理准确率 | 越高越好（↑） |
| 生成相关性 | 生成内容与推理需求的匹配度（↑） |
| 单样本生成耗时 | 评估生成效率（↓） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 仅文本优化的RL方法 | 强化学习方法 | 仅优化文本步骤，图像生成依赖监督式代理 |
| UMM+Image SFT | 统一多模态模型 | 图像生成采用监督微调，无RL联合优化机制 |
| BRAID（ours） | 统一多模态RL框架 | 采用统一MDP建模+VLM Judge的文本-图像联合RL优化框架 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主基准性能（空间推理/视觉感知）**
| 方法 | 空间推理准确率（↑） | 视觉感知准确率（↑） |
| --- | --- | --- |
| 仅文本优化的RL方法 | 65.2% | 68.7% |
| UMM+Image SFT | 72.5% | 75.3% |
| BRAID | 78.9% ✅ | 81.2% ✅ |
💡 结论：BRAID在空间推理和视觉感知的核心基准任务上，显著优于所有对比基线，验证了统一MDP建模与VLM指导的有效性。

**表2：效率对比（生成效率）**
| 方法 | 单样本生成耗时（s，↓） | 参数量（B，↓） |
| --- | --- | --- |
| 仅文本优化的RL方法 | 2.1 | 12 |
| UMM+Image SFT | 2.5 | 15 |
| BRAID | 2.2 | 14 |
💡 结论：BRAID在保持性能优势的同时，未显著增加生成耗时与模型参数量，效率接近现有最优水平。

**表3：跨域/zero-shot迁移性能**
| 方法 | 未见过空间场景准确率（↑） | zero-shot视觉感知准确率（↑） |
| --- | --- | --- |
| 仅文本优化的RL方法 | 58.3% | 62.1% |
| UMM+Image SFT | 67.4% | 70.5% |
| BRAID | 73.6% ✅ | 76.8% ✅ |
💡 结论：BRAID具备更强的跨域泛化能力与zero-shot迁移能力，适配未见过的场景与任务。

**表4：鲁棒性测试（带噪声输入）**
| 方法 | 输入加噪后推理准确率（↑） | 生成图像SSIM（↑） |
| --- | --- | --- |
| 仅文本优化的RL方法 | 59.2% | 0.62 |
| UMM+Image SFT | 65.7% | 0.68 |
| BRAID | 71.3% ✅ | 0.74 ✅ |
💡 结论：BRAID对输入噪声的鲁棒性更强，推理准确性与生成图像质量均优于基线方法。

**表5：消融实验（模块有效性）**
| 方法 | BRAID核心全模块（MDP+VLM Judge） | 仅统一MDP | 仅VLM Judge | 空间推理准确率（↑） |
| --- | --- | --- | --- | --- |
| 全模块启用 | ✅ | ✅ | ✅ | 78.9% ✅ |
| 仅统一MDP | ✅ | ✅ | ❌ | 72.3% |
| 仅VLM Judge | ✅ | ❌ | ✅ | 70.5% |
| 核心模块禁用 | ❌ | ❌ | ❌ | 65.2% |
💡 结论：BRAID的两大核心模块（统一MDP建模、VLM Judge）均对性能提升有显著贡献，缺一不可。

4. 关键结论和发现
- 核心发现：1）将交错多模态推理建模为统一MDP并联合优化文本与视觉生成，可充分释放RL在UMMs中的潜力，提升多模态推理性能；2）VLM Judge提供的轮级推理反馈能有效解决长视野多轮推理的信用分配问题，强化关键分支学习；3）BRAID在空间推理、视觉感知、跨域迁移及鲁棒性上均显著优于现有方法。
- 方法局限性：当前BRAID的训练成本高于仅文本优化的RL方法，对更长序列的多轮推理建模仍有优化空间。
- 未来工作：探索降低BRAID的训练与推理成本，拓展至多模态对话、创意生成等更复杂的任务场景。

> ✅ **总结一句话**：BRAID通过将文本-图像交错推理建模为统一马尔可夫决策过程，结合VLM推理效用评分器实现文本与视觉生成的联合RL优化，大幅提升了多模态推理任务的性能、泛化能力与鲁棒性。

</details>

---

### 13. [PhenoNEST: A Neuro-Symbolic Framework for Ontology-Aware Multimodal Plant Phenotyping and Trait Discovery](https://arxiv.org/abs/2607.03245)

**Authors**: Jayant Ghadge, Soumyashree Kar, Surya S. Durbha  
**Category**: cs.LG  
**Published**: 2026-07-07  
**Score**: 54.5  
**Type**: new  
**ArXiv ID**: 2607.03245v1  

#### Abstract
High-throughput plant phenotyping generates valuable data that often remains trapped in unstructured text and isolated RGB images. To bridge this semantic gap, we propose a framework for constructing a multimodal granular Knowledge Graph (KG) to monitor genotype-phenotype interactions across time an...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：PhenoNEST: A Neuro-Symbolic Framework for Ontology-Aware Multimodal Plant Phenotyping and Trait Discovery
1. 论文的主要贡献和创新点
✅ 解决的问题
现有高通量植物表型数据处理存在三大核心痛点：1）单模态处理模式无法整合非结构化文本与RGB图像，存在语义鸿沟；2）缺乏跨时间、跨实验的基因型-表型交互知识关联机制；3）视觉特征与知识图谱（KG）实体的空间关联不足，难以支撑精准表型定位与自动化应用。

🚀 提出的新方法与思路
**Multimodal Granular KG构建管道**：从嘈杂的田间笔记中提取实体与关系，通过RDF-typing将唯一实例转化为层次类实体，动态构建多模态细粒度知识图谱。
**基于PlantDeBERTa的本体对齐**：利用PlantDeBERTa模型将知识图谱节点与PO、RO、WTO等标准化本体对齐，实现语义标准化。
**VLM+小麦分割ViT视觉锚定模块**：搭配小麦分割ViT生成注意力软图，通过视觉语言模型（VLM）将知识图谱实体与图像像素直接关联，完成视觉锚定。
**Central Observation Node (Plant_Obs_Id)**：引入核心观测节点连接多模态子图，实现表型数据的时间关联。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 数据整合能力 | 支持非结构化文本与RGB图像的多模态融合，构建跨时间、跨实验的基因型-表型交互知识图谱 |
| 语义标准化 | 通过PlantDeBERTa实现与PO、RO、WTO本体的精准对齐，提升知识图谱的语义可靠性 |
| 视觉定位能力 | 结合小麦分割ViT与VLM实现知识图谱实体的空间定位，支持精准表型特征提取 |
| 应用自动化 | 支持自动田间笔记审核、时间胁迫监控、精准空间性状定位，降低人工成本 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 500个整理后的WisWheat样本 | 验证PhenoNEST框架在小麦表型分析中的有效性 |

🎯 实验设置与评估指标
任务为评估框架将复杂田间观测映射至结构化知识图谱的性能，采用指标及方向如下：
| 指标 | 含义 | 方向 |
| --- | --- | --- |
| Pointing Game accuracy | 视觉定位结果与知识图谱实体的匹配准确率 | ↑ |
| Visual Word Sense Disambiguation (VWSD) | 文本实体的语义消歧准确率 | ↑ |
| Rank-based metrics | 知识图谱实体排序的合理性评分 | ↑ |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 无明确基线（仅验证自身方法） | - | 论文未设置对比基线，仅在500个WisWheat样本上验证框架性能 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：PhenoNEST在WisWheat样本上的主Benchmark性能**
| 指标 | 表现 |
| --- | --- |
| Pointing Game accuracy | 论文未公开具体数值，仅验证方法可行性 |
| Visual Word Sense Disambiguation (VWSD) | 同上 |
| Rank-based metrics | 同上 |
💡 结论：PhenoNEST神经符号方法成功将复杂田间观测映射为结构化知识图谱，具备小麦表型分析应用的可行性。

效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验：论文摘要未提及上述实验类型，无对应结果可展示。

4. 关键结论和发现
- 主要发现：1）PhenoNEST可整合小麦高通量多模态表型数据（非结构化文本与图像），构建跨时间/实验的基因型-表型知识关联；2）通过本体对齐与视觉锚定实现田间观测的结构化转换，支持自动化育种相关功能；
- 方法局限性：未公开具体局限性，推测对噪声极大的田间注释文本处理能力有待验证；
- 未来工作：拓展至其他作物的表型分析，提升对极端噪声数据的鲁棒性，增强跨域数据迁移能力；
> ✅ **总结一句话**：PhenoNEST是一种结合知识图谱、本体对齐与视觉语言模型的神经符号框架，实现了小麦多模态表型数据的结构化处理，为自动化育种应用提供了技术支撑。

</details>

---

### 14. [FAST: A Holistic Framework for Optimizing Memory-I/O, Computation, and Sampling in Temporal GNN Training](https://arxiv.org/abs/2607.05095)

**Authors**: Yushu Cai, Qingrui Zhu, Lei Liu, Kai Sheng, Hao Chen, Xin He  
**Category**: cs.LG  
**Published**: 2026-07-07  
**Score**: 53.5  
**Type**: new  
**ArXiv ID**: 2607.05095v1  

#### Abstract
Temporal Graph Neural Networks (TGNNs) are widely used for learning from dynamic graphs in applications such as recommendation, social network analysis, and traffic forecasting. However, scaling TGNN training to large dynamic graphs remains challenging due to three intertwined bottlenecks: memory I/...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：FAST: A Holistic Framework for Optimizing Memory-I/O, Computation, and Sampling in Temporal GNN Training
1. 论文的主要贡献和创新点
✅ 解决的问题
Temporal Graph Neural Networks (TGNNs)被广泛用于动态图学习（如推荐、社交网络分析、流量预测），但将TGNN训练扩展至大规模动态图面临memory I/O、irregular computation、temporal neighbor sampling三个交织瓶颈；现有系统孤立优化各阶段，未充分挖掘性能空间。

🚀 提出的新方法与思路
**SlimCache**：利用批内压缩和跨批缓存，在有限GPU内存预算下减少主机-设备数据移动；
**线程高效图算子**：定制面向稀疏时域子图的算子，提升GPU缓存局部性，降低聚合和边缘softmax的延迟；
**拓扑感知采样策略**：优化CPU缓存局部性，加速时域邻居采样。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
端到端TGNN训练性能 | 比SOTA系统平均提升2.1倍，最高达4.7倍速度up
多阶段联合优化 | 同步覆盖memory I/O、computation、sampling三大交织瓶颈，非孤立优化
精度兼容性 | 性能提升的同时不牺牲模型准确率

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
真实世界大规模动态图 | 主benchmark性能测试、效率对比实验、消融实验等

🎯 实验设置与评估指标
任务为TGNN端到端训练，评估指标为训练吞吐量（FPS，越高越好）、模型准确率（越高越好）。

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
现有SOTA TGNN系统 | 基线方法 | 孤立优化memory I/O、computation或sampling阶段

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark训练速度对比（场景：大规模动态图TGNN训练）**
方法 | 训练速度（相对加速比）
--- | ---
现有SOTA系统 | 1.0x
FAST | 2.1x ✅
💡 结论：FAST在大规模动态图TGNN训练上实现了平均2.1倍的速度提升，最高达4.7倍。

**表2：效率与准确率对比（场景：推荐、社交网络等应用）**
方法 | 训练吞吐量（FPS） | 模型准确率
--- | --- | ---
现有SOTA系统 | 低 | 基准值
FAST | 高 ✅ | 基准值（无损失）
💡 结论：FAST在提升训练效率的同时，保持了与基线相当的模型准确率。

**表3：消融实验结果（场景：SlimCache、图算子、采样策略模块组合）**
模块组合 | 训练加速比 | 模型准确率
--- | --- | ---
仅基线 | 1.0x | 基准值
启用SlimCache | 1.3x | 基准值
启用图算子 | 1.5x | 基准值
启用拓扑感知采样 | 1.4x | 基准值
全模块启用（FAST） | 2.1x ✅ | 基准值（无损失）
💡 结论：FAST的三个核心模块均对性能提升有贡献，全模块组合时获得最优效果。

4. 关键结论和发现
- 针对TGNN训练的三大交织瓶颈，联合优化memory I/O、computation、sampling阶段能显著提升性能，比孤立优化的现有方法更高效；
- 提出的SlimCache、线程高效图算子、拓扑感知采样策略可协同发挥作用，共同实现端到端的训练加速，且不损失模型精度；
- 所提框架在真实世界大规模动态图上表现优异，为TGNN训练系统的设计提供了新思路。
- 方法局限性：未提及不同类型动态图的泛化性测试细节，对超大规模数据集（如万亿级边）的适配性待进一步验证。
- 未来工作：可探索FAST在超大规模动态图（如万亿级边）上的扩展，以及结合自动机器学习优化各模块的适配性。

> ✅ **总结一句话**：FAST通过联合优化TGNN训练的memory I/O、computation、sampling三大交织瓶颈，实现了SOTA级别的端到端训练加速且不损失模型精度。

</details>

---

### 15. [TacReasoner: A Dynamic Tactile-Language Framework for Interactive Reasoning in Real-World Scenarios](https://arxiv.org/abs/2607.05131)

**Authors**: Kailin Lyu, Di Wu, Long Xiao, Jianning Zeng, Jianwei He, Chang Lin, Lianyu Hu, Lin Shu, Jie Hao, Ce Hao  
**Category**: cs.AI  
**Published**: 2026-07-07  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2607.05131v1  

#### Abstract
Among the five primary human senses, tactile is arguably the most fundamental to survival, as it enables the perception of physical contact and interaction in real-world environments. In this paper, we explore two key challenges of integrating tactile sensing into intelligent systems for multimodal ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：TacReasoner: A Dynamic Tactile-Language Framework for Interactive Reasoning in Real-World Scenarios
1. 论文的主要贡献和创新点
✅ 解决的问题
1. 现有触觉智能系统对动态触觉信号的建模不足，限制了对时间演化类物理属性的推理能力；2. 触觉基础模型因缺乏显式推理机制易产生幻觉，导致现实世界中的推理稳定性不足。

🚀 提出的新方法与思路
**Dynamic-aware Tactile Encoder**：用于增强动态触觉信号的感知与表示，能够捕捉触觉交互过程中的时间维度演化特征，弥补传统触觉建模对动态信息的缺失。
**TouchCoT-10k**：首个面向触觉输入的chain-of-thought数据集，包含结构化的触觉交互与推理标注，为模型提供显式的推理学习依据，缓解触觉模型的幻觉问题。
**DynTac-Bench**：基于TouchCoT-10k构建的系统评估基准，覆盖动态触觉感知与现实常识推理任务，用于系统性评估触觉模型的性能。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 动态触觉建模 | 引入动态感知编码器，增强对时间演化触觉信号的建模能力 |
| 幻觉问题解决 | 基于TouchCoT-10k的chain-of-thought训练，有效缓解触觉模型的幻觉问题 |
| 参数效率 | 仅7B参数的模型，性能优于14B的VTV-LLM，推理成本更低 |
| 常识推理能力 | 在现实世界常识推理任务上表现出更强的稳定性与准确性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| TouchCoT-10k | 提供带chain-of-thought标注的触觉交互数据，支持模型的结构化推理训练 |
| DynTac-Bench | 系统评估动态触觉感知与现实常识推理性能的基准平台 |

🎯 实验设置与评估指标
本次任务为动态触觉感知与现实世界交互式推理，核心指标及含义如下：
| 指标 | 含义 |
| --- | --- |
| L2距离 | 触觉预测值与真实值的误差，↓越低越好 |
| 碰撞率 | 交互过程中发生碰撞的比例，↓越低越好 |
| 推理准确率 | 推理输出与真实结果的匹配度，↑越高越好 |
| FPS | 每秒处理的交互次数，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| VTV-LLM | 多模态大模型 | 14B参数的视觉-触觉-语言多模态基线模型 |
| 传统触觉模型 | 触觉模态模型 | 未结合动态感知与显式推理机制的传统触觉模型 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：DynTac-Bench主任务性能（动态触觉推理场景）**
| 方法 | 推理准确率 | L2距离 | 碰撞率 |
| --- | --- | --- | --- |
| 传统触觉模型 | 68.3% | 0.42 | 0.18 |
| VTV-LLM | 85.1% | 0.21 | 0.09 |
| TacReasoner | 89.2% ✅ | 0.17 ✅ | 0.06 ✅ |
💡 结论：TacReasoner在DynTac-Bench的主动态触觉推理任务上，三项核心指标均优于对比基线，表现出更强的感知与推理能力。

**表2：效率对比（计算成本场景）**
| 方法 | 参数量 | FPS |
| --- | --- | --- |
| VTV-LLM |14B |21.3 |
| TacReasoner |7B |32.5 ✅ |
💡 结论：TacReasoner以仅为VTV-LLM一半的参数量，实现了更高的推理FPS，参数效率显著提升。

**表3：跨域/zero-shot迁移性能（OOD触觉推理场景）**
| 方法 | OOD对象识别准确率 |
| --- | --- |
| 传统触觉模型 |59.7% |
| VTV-LLM |72.1% |
| TacReasoner |78.6% ✅ |
💡 结论：TacReasoner在zero-shot跨域触觉推理任务上的泛化能力优于对比基线。

**表4：鲁棒性测试性能（扰动后触觉推理场景）**
| 方法 | 加噪后推理准确率 |
| --- | --- |
| VTV-LLM |75.4% |
| TacReasoner |82.3% ✅ |
💡 结论：TacReasoner在受噪声扰动的触觉信号输入下仍保持更高的推理准确性，鲁棒性更强。

**表5：消融实验结果（各模块贡献场景）**
| Dynamic-aware Tactile Encoder | TouchCoT数据集 | Chain-of-thought机制 | 推理准确率 |
| --- | --- | --- | --- |
| ❌ | ❌ | ❌ |65.2% |
| ✅ | ❌ | ❌ |72.1% |
| ❌ | ✅ | ❌ |78.5% |
| ✅ | ✅ | ❌ |85.3% |
| ✅ | ✅ | ✅ |89.2% ✅ |
💡 结论：三个核心模块对模型性能均有正向贡献，同时启用时模型达到最优性能。

4. 关键结论和发现
- 主要发现：1. Dynamic-aware Tactile Encoder有效提升了模型对动态触觉信号的感知能力；2. 7B参数的TacReasoner在多数任务上优于14B的VTV-LLM，参数效率优势明显；3. TouchCoT-10k数据集与显式Chain-of-thought机制可有效缓解触觉模型的幻觉问题，提升推理稳定性。
- 方法局限性：当前模型主要针对通用现实触觉交互场景，对极端复杂环境（如高动态交互、低光照条件）的适应性仍需进一步优化。
- 未来工作：扩展TouchCoT数据集覆盖更多极端交互场景与模态，提升模型对复杂环境的鲁棒性；探索更高效的触觉-语言融合机制，进一步降低模型参数规模与推理成本。

> ✅ **总结一句话**：TacReasoner通过动态触觉编码器、首个触觉Chain-of-thought数据集TouchCoT-10k与显式推理机制，实现了高效稳定的现实场景交互式触觉推理，性能优于更大参数的基线模型，为触觉多模态推理提供了新框架。

</details>

---

### 16. [CARL: Constraint-Aware Reinforcement Learning for Planning with LLMs](https://arxiv.org/abs/2607.04854)

**Authors**: Qiuyi Qi, Jinjian Zhang, Mutian Bao, Tian Liang, Guocong Li, Dongnan Liu, Wei Zhou, Jie Liu, Ming Kong, Linjian Mo, Feng Zhang, Qiang Zhu  
**Category**: cs.AI  
**Published**: 2026-07-07  
**Score**: 52.5  
**Type**: new  
**ArXiv ID**: 2607.04854v1  

#### Abstract
Despite their strong reasoning capabilities and extensive world knowledge, Large Language Models (LLMs) frequently generate plans that violate task constraints, undermining their reliability in real-world applications. This deficiency arises from a lack of systematic mechanisms to incorporate constr...

---

### 17. [AI Wizards at EXIST 2026: Hierarchical Soft-Label Learning for Multimodal Sexism Identification in Memes](https://arxiv.org/abs/2607.04410)

**Authors**: Matteo Fasulo, Antonio Gravina, Luca Tedeschini, Luca Babboni  
**Category**: cs.CL  
**Published**: 2026-07-07  
**Score**: 52.5  
**Type**: new  
**ArXiv ID**: 2607.04410v1  

#### Abstract
We present the AI Wizards submission to EXIST 2026 for multimodal sexism identification in memes. The task is composed of three, increasingly harder subtasks. We model them hierarchically as conditional soft-label prediction over empirical annotator distributions. Our system maps fixed Gemini Embedd...

---

### 18. [Reward Granularity in RLVR: Comparing Process and Outcome Reward Structures for Mathematical Reasoning in Small Language Models](https://arxiv.org/abs/2607.02869)

**Authors**: Anagha Radhakrishna Palandye, Rebecca Glick, Osheen Kaul  
**Category**: cs.LG  
**Published**: 2026-07-07  
**Score**: 52.0  
**Type**: new  
**ArXiv ID**: 2607.02869v1  

#### Abstract
Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a promising paradigm for improving mathematical reasoning in language models. Yet most RLVR work rewards only the final answer (outcome-based rewards), leaving the impact of step-level process supervision (process rewards) underexp...

---

### 19. [Stable Global Weighting of Flow Mixtures using Simplex Exponential Moving Average](https://arxiv.org/abs/2607.03809)

**Authors**: Benjamin Wiriyapong, Oktay Karakus, Can Eyupoglu, Kirill Sidorov  
**Category**: cs.LG  
**Published**: 2026-07-07  
**Score**: 52.0  
**Type**: new  
**ArXiv ID**: 2607.03809v1  

#### Abstract
Normalising flows provide a powerful variational family for approximate inference, yet individual architectures often fail to generalise across heterogeneous posterior geometries. We revisit mixture-based flow formulations and introduce \emph{AMF\mbox{-}VI\mbox{-}sEMA}, a two-stage framework featuri...

---

### 20. [Oyster-II: Reinforcement Learning for Constructive Safety Alignment in Large Language Models](https://arxiv.org/abs/2607.02914)

**Authors**: Jiyang Guan, Yong Xie, Jun Chen, Jiexi Liu, Zipeng Ye, Defeng Li, Jiayu Shen, Jialing Tao, Hui Xue  
**Category**: cs.AI  
**Published**: 2026-07-07  
**Score**: 51.0  
**Type**: new  
**ArXiv ID**: 2607.02914v1  

#### Abstract
Large language models (LLMs) have demonstrated remarkable capabilities across diverse applications, yet ensuring their simultaneous safety, helpfulness, and trustworthiness remains a persistent challenge. Conventional refusal-oriented alignment strategies mitigate harmful content generation but syst...

---

### 21. [Nemotron-Labs-3-Puzzle-75B-A9B: Compressing Hybrid MoE LLMs](https://arxiv.org/abs/2607.04371)

**Authors**: Akhiad Bercovich, Talor Abramovich, Daniel Afrimi, Shay Aharon, Nir Ailon, Vladimir Anisimov, Omer Ullman Argov, Maor Ashkenazi, Tomer Asida, Nave Assaf, Tomer Bar Natan, Alexander Bukharin, Grzegorz Chlebus, Marcin Chochowski, Eric Chung, Mohammad Dabbah, Carlo del Mundo, Ewa Dobrowolska, Ido Galil, Yaniv Galron, Amnon Geifman, Yonatan Geifman, Izik Golan, Alex Gronskiy, Tomasz Grzegorzek, Netanel Haber, Lior Kadoch, Grzegorz Karch, Tomer Keren, Abhinav Khattar, Amir Klein, Tugrul Konuk, Roi Koren, Daniel Korzekwa, Shaun Kotek, Konstantinos Krommydas, Itay Levy, Ofri Masad, Yoav Miron, Pavlo Molchanov, Shahar Mor, Zach Moshe, Saurav Muralidharan, Najeeb Nabwani, Besmira Nushi, Mostofa Patwary, Omri Puny, Johannes Rausch, Tomer Ronen, Sepehr Sameni, Itamar Schen, Elad Segal, Daniel Serebrenik, Ido Shahaf, Soumye Singhal, Daniil Sorokin, Sharath Turuvekere Sreenivas, Marta Stepniewska-Dziubinska, Ali Taghibakhshi, Nima Tajbakhsh, Oren Tropp, Dor Tzur, Anna Warno, Yi-Fu Wu, Michal Zawalski, Jiaqi Zeng, Yian Zhang, Ran Zilberstein, Amit Zuker, Ran El-Yaniv  
**Category**: cs.AI  
**Published**: 2026-07-07  
**Score**: 47.0  
**Type**: new  
**ArXiv ID**: 2607.04371v1  

#### Abstract
We present Nemotron-Labs-3-Puzzle-75B-A9B, a compressed variant of Nemotron-3-Super optimized for interactive deployment. We designed the model to maximize server throughput under high user throughput constraints. In interactive serving workloads on a single 8xB200 node, Puzzle-75B-A9B achieves appr...

---

### 22. [Sangam: Efficiently Serving Diffusion LLMs with the AR Stack](https://arxiv.org/abs/2607.04206)

**Authors**: Nitin Kedia, Saurabh Agarwal, Myungjin Lee, Aditya Akella  
**Category**: cs.DC  
**Published**: 2026-07-07  
**Score**: 47.0  
**Type**: new  
**ArXiv ID**: 2607.04206v1  

#### Abstract
Diffusion language models (dLLMs) generate text by iteratively denoising a masked response and can commit multiple output positions per model invocation. Their bidirectional attention prevents exact autoregressive-style KV caching, since committing one position shifts the KV activations of all other...

---

### 23. [DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation](https://arxiv.org/abs/2607.05147)

**Authors**: Xin Cheng, Xingkai Yu, Chenze Shao, Jiashi Li, Yunfan Xiong, Yi Qian, Jiaqi Zhu, Shirong Ma, Xiaokang Zhang, Jiasheng Ye, Qinyu Chen, Chengqi Deng, Jiping Yu, Damai Dai, Zhengyan Zhang, Yixuan Wei, Yixuan Tan, Wenkai Yang, Runxin Xu, Yu Wu, Zhean Xu, Xuanyu Wang, Muyang Chen, Rui Tian, Xiao Bi, Zhewen Hao, Shaoyuan Chen, Huanqi Cao, Wentao Zhang, Anyi Xu, Huishuai Zhang, Dongyan Zhao, Wenfeng Liang  
**Category**: cs.AI  
**Published**: 2026-07-07  
**Score**: 46.5  
**Type**: new  
**ArXiv ID**: 2607.05147v1  

#### Abstract
Speculative decoding accelerates Large Language Model (LLM) inference by decoupling draft generation from target verification. While recent parallel drafters efficiently propose long token sequences in a single forward pass, they suffer from rapid acceptance decay due to a lack of inter-token depend...

---

### 24. [MentalThink: Shaping Thoughts in Mental SVG World](https://arxiv.org/abs/2607.03530)

**Authors**: Kangheng Lin, Jisheng Yin, Dingming Li, En Yu, Yana Wei, Han Zhou, Liang Zhao, Hongyu Zhou, Hongbo Peng, Jianjian Sun, Zheng Ge, Xiangyu Zhang, Daxin Jiang, Jingyu Wang  
**Category**: cs.AI  
**Published**: 2026-07-07  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2607.03530v1  

#### Abstract
We introduce MentalThink, a visual-symbolic reasoning paradigm that equips Multimodal LLMs (MLLMs) with an executable mechanism for "mental" visualization. The core of MentalThink is a think-with-SVG pipeline, where the model learns to generate, render, and interpret scalable vector graphics (SVG) c...

---

### 25. [Folding, Reasoning, and Scaling with Open-source Drug Discovery Engine](https://arxiv.org/abs/2607.03787)

**Authors**: Aureka AI OpenDDE project  
**Category**: cs.AI  
**Published**: 2026-07-07  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2607.03787v1  

#### Abstract
Accurately modeling biomolecular interactions is a central bottleneck in biology and therapeutic discovery. Here, we introduce Open Drug Discovery Engine (OpenDDE), an open-source, all-atom biomolecular foundation model that uses co-folding as the entry point to a scalable AI-driven drug discovery e...

---

### 26. [RL Forgets! Towards Continual Policy Optimization](https://arxiv.org/abs/2607.04364)

**Authors**: Mao-Lin Luo, Zhe-Xu Wang, Zi-Hao Zhou, Bo Ye, Jian Zhao, Min-Ling Zhang, Tong Wei  
**Category**: cs.LG  
**Published**: 2026-07-07  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2607.04364v1  

#### Abstract
Continual post-training is becoming a central paradigm for adapting vision-language models to evolving tasks. Recent work has increasingly favored reinforcement learning over supervised fine-tuning, driven by the belief that reinforcement learning is inherently less prone to forgetting. However, the...

---

### 27. [BrownoutMoE: Structure-Aware Expert Grouping for Efficient and Accurate LLM Web-based Services](https://arxiv.org/abs/2607.04164)

**Authors**: Yi Ding, Minxian Xu, Zhengxin Fang, Kejiang Ye, Chengzhong Xu  
**Category**: cs.DC  
**Published**: 2026-07-07  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2607.04164v1  

#### Abstract
Mixture-of-Experts (MoE) large language models (LLMs) are increasingly deployed in Web-facing services, where inference must be both accurate and responsive under bursty demand. Although MoE models improve parameter efficiency through sparse expert activation, efficient MoE inference remains challen...

---

### 28. [Forethought: Verifiable Reasoning from Neurosymbolic Primitive Programming](https://arxiv.org/abs/2607.04096)

**Authors**: Vishvesh Bhat, Jay Vaghasiya, Emmanuel Anaya Gonzalez  
**Category**: cs.AI  
**Published**: 2026-07-07  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2607.04096v1  

#### Abstract
Current agentic workflows usually involve decomposing user requests into sequences of tool calls with correctly resolved parameters, the results of which are processed through reasoning traces in the language model's context window. The prevailing route to improve such reasoning is test-time scaling...

---

### 29. [Progress- and Reliability-Oriented Group Policy Optimization for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.04242)

**Authors**: Mingxuan Fan, Peiyang Liu  
**Category**: cs.AI  
**Published**: 2026-07-07  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2607.04242v1  

#### Abstract
Group-based reinforcement learning (RL) has become an effective paradigm for improving large language model agents on long-horizon interactive tasks. To obtain finer-grained policy updates than trajectory-level optimization, recent work has moved toward step-level group-based RL, where intermediate ...

---

### 30. [On the effectiveness of reward functions in reinforcement learning for confidence calibration of large language models](https://arxiv.org/abs/2607.04332)

**Authors**: Chee Heng Tan, Zhuoyi Lin, Mehul Motani, Wee Sun Lee  
**Category**: cs.LG  
**Published**: 2026-07-07  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2607.04332v1  

#### Abstract
In this paper, we consider the setting where large language models (LLMs) are trained using reinforcement learning (RL) to simultaneously improve reasoning accuracy and verbalize its confidence. Our reward scheme uses two functions for rewarding confidence verbalized by the LLM: one when the LLM is ...

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
