# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-08-19 06:12:12 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [SignalReasoner: Assessing the Upper Bound of 3B Models for Signal Mathematical Reasoning](https://arxiv.org/abs/2608.17301v1)

**Authors**: Guozheng Sun  
**Category**: cs.AI  
**Published**: 2026-08-19  
**Score**: 64.0  
**Type**: new  
**ArXiv ID**: 2608.17301v1  

#### Abstract
Post-training with supervised chain-of-thought fine-tuning and reinforcement learning from verifiable rewards has substantially improved the mathematical reasoning capabilities of large language models (LLMs). However, their application to signal processing problems remains relatively under-explored...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

SignalReasoner: Assessing the Upper Bound of 3B Models for Signal Mathematical Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题：现有大语言模型的数学推理优化多聚焦通用任务，在信号处理这类特定领域的数学推理上应用不足；同时3B规模小模型在该领域的性能上限、以及GRPO、GSPO、GMPO三类RL策略在信号数学推理任务中的表现优劣未被充分研究。
🚀 提出的新方法与思路
**Domain-Aware SFT-RL Pipeline**：构建两种适配信号数学推理的训练范式，第一种是直接对WirelessMATHBench-XL应用带可验证奖励的强化学习；第二种是先在蒸馏的无线领域思维链（CoT）语料上完成监督微调（SFT），再开展相同的领域特定强化学习阶段。
**Tri-Paradigm RL Strategy Evaluation**：在上述两种训练范式下，分别测试Group Relative Policy Optimization (GRPO)、Group Sequence Policy Optimization (GSPO)、Geometric-Mean Policy Optimization (GMPO)三类RL策略的性能。
🔍 相比现有方法的优势
维度 | 优势
--- | ---
领域适配性 | 针对研究生级信号处理数学问题优化语言模型，填补该领域应用空白
小模型性能评估 | 明确评估3B规模模型在信号数学推理任务的性能上限，拓展小模型在特定领域的应用
多策略对比 | 同时测试三类典型RL策略在信号推理任务的表现，为领域任务的策略选择提供参考
2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
WirelessMATHBench-XL | 研究生级信号处理数学推理问题的评估基准
🎯 实验设置与评估指标
任务为适配Qwen2.5-3B-Base模型处理信号处理领域的数学推理问题，评估指标为整体准确率。
指标 | 含义
--- | ---
整体准确率 | 越高越好 ↑
⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
未训练Qwen2.5-3B-Base模型 | 基线模型 | 未经过任何信号数学相关训练/微调，作为性能基准
3. 主要实验结果和性能指标
📊 定量结果汇总
所有实验基于WirelessMATHBench-XL评估，论文未提及具体表号。
最优模型（结合领域CoT SFT初始化的RL策略）的整体准确率为39.12% ✅；未训练Qwen2.5-3B-Base模型的整体准确率为12.37%。
💡 结论：针对信号处理数学推理任务，经过领域感知CoT SFT结合RL训练的3B模型性能远优于未训练的基础模型，提升幅度超三倍。
其他实验：
主benchmark性能（L2/碰撞率等） | 论文未报告
效率对比（FPS/参数量） | 论文未报告
跨域/zero-shot迁移 | 论文未报告
鲁棒性/扰动测试 | 论文未报告
消融实验 | 论文未报告
4. 关键结论和发现
- 主要发现1：针对信号处理数学推理任务，采用领域感知CoT SFT初始化再结合RL的训练范式，可使3B规模的Qwen2.5模型实现超三倍的性能提升，最佳整体准确率达39.12%；
- 主要发现2：论文对GRPO、GSPO、GMPO三类RL策略在信号推理任务的表现进行了评估，以探究哪种策略在稳定性或准确性上更优，但未明确给出某类策略的绝对优势结论；
- 方法局限性：论文未报告；
- 未来工作：论文未报告。

> ✅ **总结一句话**：该论文针对信号处理数学推理任务，以WirelessMATHBench-XL为基准，探究了3B规模Qwen2.5模型的两种强化学习训练范式及三类RL策略的表现，实现了比未训练基础模型超三倍的性能提升，评估了该规模模型在该领域的性能上限。

</details>

---

### 2. [The Road Less Traveled: Congestion-Aware NoC Placement and Packet Routing for FPGAs](https://arxiv.org/abs/2608.17266v1)

**Authors**: Soheil Gholami Shahrouz, Vaughn Betz  
**Category**: cs.AR  
**Published**: 2026-08-19  
**Score**: 51.5  
**Type**: new  
**ArXiv ID**: 2608.17266v1  

#### Abstract
To help scale to ever-larger and more complex designs, recent FPGA architectures now integrate network-on-chips (NoCs). NoCs help transfer high-bandwidth data over long distances within the chip without using scarce low-delay long routing wire segments. While NoC-enhanced FPGAs aid system integratio...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：The Road Less Traveled: Congestion-Aware NoC Placement and Packet Routing for FPGAs
1. 论文的主要贡献和创新点
✅ 解决的问题
FPGA架构集成NoC后，需优化NoC的延迟、带宽利用率并避免链路过载（congestion），同时还要优化连接NoC路由器的设计模块的可编程路由资源使用；现有方法易忽略NoC相关约束，导致拥塞等问题。

🚀 提出的新方法与思路
**加入NoC链路拥塞成本至VPR布局引擎**：在开源CAD流程VPR的布局引擎中加入NoC链路拥塞成本，使布局阶段就能考虑NoC拥塞问题。
**集成Turn模型NoC路由算法至布局引擎**：将Turn模型NoC路由算法集成到布局引擎，利用路径多样性进一步降低拥塞。
**NoC路由的SAT建模方法**：针对前两种方法未完全缓解的拥塞场景，将NoC路由建模为布尔可满足性（SAT）问题进行求解。
**增强VPR布局引擎的RL智能体**：强化VPR布局引擎中的RL智能体，引入NoC感知的移动类型，减少长线路长度。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| NoC拥塞程度 | 布局拥塞建模结合Turn模型路由可平均减少90.7%的NoC拥塞，结合SAT建模可进一步降至比基线低95.1% |
| 聚合带宽需求 | 仅平均增加4%，带宽影响小 |
| 线路长度 | 针对大量使用NoC的设计，减少8.8% |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 29个benchmark组成的套件 | 用于评估所提各类方法的性能表现 |

🎯 实验设置与评估指标
任务为评估针对FPGA NoC的布局与路由方法对NoC拥塞、带宽需求及线路长度等设计指标的影响。
| 指标 | 含义（箭头方向） |
| --- | --- |
| NoC拥塞程度 | 反映NoC链路过载情况，数值越低拥塞越轻，↓ |
| 聚合带宽需求 | 反映设计的总带宽占用，数值越低越好，↓ |
| 线路长度 | 反映可编程路由资源的使用情况，数值越短越好，↓ |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 原始VPR布局与路由方法 | 基线方法 | 未考虑NoC链路拥塞成本，无针对NoC的感知优化 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**结合布局拥塞建模与Turn模型路由的主实验结果（29个基准平均）**
| 方法 | NoC拥塞减少率（vs基线） | 聚合带宽需求变化 |
| --- | --- | --- |
| 布局拥塞建模+Turn模型路由 | 90.7% ✅ | +4% |
| 布局拥塞建模+Turn模型路由+SAT方法 | 95.1% ✅ | 论文未报告 |
💡 结论：结合布局阶段的NoC拥塞建模与Turn模型路由可显著降低NoC拥塞，小幅增加聚合带宽需求，进一步采用SAT建模可获得更优的拥塞缓解效果。

**RL智能体增强实验结果（大量使用NoC的设计）**
该实验无对应表号、图号，按论文描述呈现：所提NoC感知移动类型增强的RL布局智能体，可使针对大量使用NoC的设计的线路长度减少8.8%。
💡 结论：针对NoC使用密集的设计，增强布局阶段的RL智能体可有效缩短线路长度，减少路由资源消耗。

4. 关键结论和发现
- 主要发现：①布局阶段融入NoC链路拥塞成本并结合Turn模型路由，在29个基准上平均减少90.7%的NoC拥塞，仅增加4%聚合带宽需求；②在上述方法基础上，采用SAT建模NoC路由可进一步将拥塞降至比基线低95.1%；③针对大量使用NoC的设计，引入NoC感知移动类型的RL布局智能体可减少8.8%的线路长度。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：该论文针对FPGA集成NoC后CAD流程面临的拥塞与资源优化难题，提出布局拥塞建模、Turn模型路由、SAT路由建模及RL智能体增强等方法，有效缓解NoC拥塞并平衡其他设计指标，提升FPGA设计的性能与资源利用率。

</details>

---

### 3. [Neuro-symbolic learning over OWL 2 DL via consequence-based compilation to differentiable circuits](https://arxiv.org/abs/2608.17741v1)

**Authors**: Olga Mashkova, Asaad Mohammedsaleh, Fernando Zhapa-Camacho, Robert Hoehndorf  
**Category**: cs.AI  
**Published**: 2026-08-19  
**Score**: 51.0  
**Type**: new  
**ArXiv ID**: 2608.17741v1  

#### Abstract
OWL 2 DL ontologies, grounded in the description logic $\mathcal{SROIQ}$, express large knowledge bases in biomedicine and the Semantic Web. Neuro-symbolic (NeSy) learners over description logics either embed the ontology in a continuous space, abandoning classical entailment, or restrict to the Hor...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Neuro-symbolic learning over OWL 2 DL via consequence-based compilation to differentiable circuits
1. 论文的主要贡献和创新点
✅ 解决的问题
现有针对OWL 2 DL（对应描述逻辑$\mathcal{SROIQ}$）的神经符号（NeSy）学习方法存在两类缺陷：一是将本体嵌入连续空间，放弃了经典逻辑推理；二是仅限制在Horn片段$\mathcal{EL}^{++}$，该片段仅有单一规范模型，无法支持更广泛的OWL 2 DL功能。

🚀 提出的新方法与思路
**Baobab（$\mathcal{SROIQ}$本体编译与神经符号学习框架）**：该方法将具有有限ABox的$\mathcal{SROIQ}$本体编译为Sentential Decision Diagram（SDD），具体流程为：①在基于结果的演算下饱和本体的命题核心；②将本体剩余的$\mathcal{SROIQ}$特征（名项、数量限制、角色公理）实例化到有效域；再通过SDD的 evidence-conditioned weighted model count 训练感知网络，实现部分ABox监督下的真实图像识别任务。此外，针对非Horn描述逻辑中的推理捷径问题，提出用查询的正当理由索引的混合模型，可表示校准后验，解决独立感知坍缩的问题，且Baobab的编译器与表示结果均在Lean 4中完成机器验证，保障了正确性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 支持的描述逻辑范围 | 支持完整OWL 2 DL对应的$\mathcal{SROIQ}$，而非仅局限于Horn片段$\mathcal{EL}^{++}$ |
| 推理保真度 | 通过编译为SDD并基于weighted model count，保留经典逻辑推理，避免嵌入方法放弃推理的缺陷 |
| 推理捷径缓解 | 首次在非Horn描述逻辑中，通过查询正当理由索引的混合模型表征校准后验，缓解神经符号学习中的推理捷径问题 |
| 方法正确性 | 编译器与表示结果经Lean 4机器验证，具备形式化正确性保障 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| MNIST | 用于测试CNN在部分ABox监督下学习数字（结合后继关系）、恢复潜在本体概念，以及真实图像MNIST任务的性能 |

🎯 实验设置与评估指标
任务：构建结合含所有独特$\mathcal{SROIQ}$特征的本体与MNIST数字任务、真实图像MNIST任务的场景，测试Baobab框架下模型的图像识别、本体概念恢复能力，以及推理捷径的缓解效果。
| 指标 | 含义 |
| ---- | ---- |
| 论文未报告 | 论文未明确给出具体评估指标及其箭头方向 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| DL嵌入型神经符号方法 | 对比基线 | 将本体嵌入连续空间，放弃经典逻辑推理 |
| $\mathcal{EL}^{++}$相关神经符号方法 | 对比基线 | 仅支持Horn片段$\mathcal{EL}^{++}$，该片段仅有单一规范模型 |
| 单-WMC方法 | 对比基线 | 在真实图像MNIST任务中无法达到贝叶斯最优后验 |
| BEARS-ensemble假设类方法 | 对比基线 | 在真实图像MNIST任务中无法达到贝叶斯最优后验 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**包含所有$\mathcal{SROIQ}$特征的本体+MNIST数字任务场景**
基于Baobab的CNN模型可学习读MNIST数字并结合后继关系，恢复潜在本体概念；独立感知方法在该任务上的表现与随机水平一致。
💡 结论：Baobab框架下的神经符号学习可有效恢复复杂OWL 2 DL对应的本体概念，性能优于独立感知方法。

**真实图像MNIST任务场景**
当监督允许多个本体一致补全时，独立感知会发生坍缩（出现推理捷径）；基于查询正当理由索引的混合模型（Baobab提出）可表征校准后验，达到贝叶斯最优后验；单-WMC方法与BEARS-ensemble假设类方法在该任务上无法达到贝叶斯最优后验，这是首次在非Horn描述逻辑中表征并缓解推理捷径问题。
💡 结论：Baobab提出的基于查询正当理由索引的混合模型可有效缓解非Horn描述逻辑神经符号学习中的推理捷径，实现贝叶斯最优后验。

4. 关键结论和发现
- 主要发现：1）Baobab框架将$\mathcal{SROIQ}$本体编译为SDD，结合weighted model count训练感知网络，可支持OWL 2 DL的完整功能，同时保留经典逻辑推理，避免了现有方法放弃推理或仅支持Horn片段的缺陷；2）非Horn描述逻辑的神经符号学习中存在推理捷径问题（独立感知坍缩），基于查询正当理由索引的混合模型可缓解该问题；3）Baobab的方法正确性通过Lean 4机器验证，具备形式化保障。
- 方法局限性：论文未报告
- 未来工作：论文未报告具体未来工作方向，仅开源了代码

> ✅ **总结一句话**：Baobab是首个支持OWL 2 DL（$\mathcal{SROIQ}$）的神经符号学习框架，通过将本体编译为SDD实现了保留经典推理的本体处理，可缓解非Horn描述逻辑神经符号学习中的推理捷径问题，且方法正确性经过形式化验证。

</details>

---

### 4. [ESR-HGNN: Eliminating Semantic Redundancy for Efficient Mini-batch HGNN Inference](https://arxiv.org/abs/2608.17865v1)

**Authors**: Dengke Han, Mingyu Yan, Duo Wang, Wenming Li, Xiaochun Ye, Dongrui Fan  
**Category**: cs.AR  
**Published**: 2026-08-19  
**Score**: 47.0  
**Type**: new  
**ArXiv ID**: 2608.17865v1  

#### Abstract
Heterogeneous graph neural networks (HGNNs) are highly effective in processing heterogeneous graph data and have been widely adopted in critical domains. As real-world graph data continues to scale, performing direct inference on entire graphs becomes increasingly infeasible, making mini-batch metho...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

ESR-HGNN: Eliminating Semantic Redundancy for Efficient Mini-batch HGNN Inference
1. 论文的主要贡献和创新点
✅ 解决的问题
HGNN处理大规模异构图数据时，端到端小批量推理中基于元路径的采样是性能瓶颈，源于图结构不规则遍历引发的大量随机内存访问；现有采样范式因固有语义冗余存在过多冗余遍历，导致采样效率低、小批量HGNN推理性能次优。

🚀 提出的新方法与思路
**冗余感知HGNN采样范式**：利用metapath trie复用遍历路径，消除冗余内存访问；
**多通道硬件采样单元（ESR-HGNN）**：将上述采样范式映射为多通道硬件单元；
**可复用性驱动的元路径分组技术**：聚类元路径以最大化硬件通道内的可复用遍历路径，提升语义并行场景下的效率。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 现有采样方法 | 采样效率低，端到端小批量HGNN推理性能次优 |
| ESR-HGNN | 平均采样性能较CPU、GPU提升一个数量级；伴随显著节能；与GPU及先进HGNN推理加速器集成后端端小批量推理大幅加速 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
论文未报告任务具体设置与评估指标的详细内容。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
所有实验未报告具体表号、图号及详细实验细节，仅摘要提及相关结论如下：
1. 主 benchmark 性能：论文未报告；
2. 效率对比（FPS / 参数量）：仅摘要提及平均采样性能较CPU、GPU提升一个数量级，伴随显著节能；
3. 跨域 / zero-shot 迁移：论文未报告；
4. 鲁棒性 / 扰动测试：论文未报告；
5. 消融实验：论文未报告。

4. 关键结论和发现
- 2-3条主要发现
  1. 基于元路径的小批量HGNN采样中，语义冗余引发的冗余遍历是大规模图下端到端推理的核心性能瓶颈；
  2. 利用metapath trie复用遍历路径，结合多通道硬件单元与可复用性驱动的元路径分组，可有效消除语义冗余带来的内存访问问题；
  3. ESR-HGNN可兼容现有HGNN推理加速硬件，实现端到端小批量推理的大幅加速。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：ESR-HGNN通过元路径字典树复用遍历路径、可复用性驱动的元路径分组消除语义冗余，实现HGNN小批量采样性能与能效的大幅提升，集成后端端小批量推理加速。

</details>

---

### 5. [DTX: A Throughput-First Training Accelerator for Diffusion and Transformer Models](https://arxiv.org/abs/2608.16953v1)

**Authors**: Shashank  
**Category**: cs.AR  
**Published**: 2026-08-19  
**Score**: 46.5  
**Type**: new  
**ArXiv ID**: 2608.16953v1  

#### Abstract
DTX is a throughput-first training accelerator for diffusion and transformer models. Any summation serialized through a single FP32 adder is a loop-carried dependence that pins a machine near 2 FLOP/cycle regardless of physical design; DTX is built so no such chain exists anywhere -- every reduction...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

DTX: A Throughput-First Training Accelerator for Diffusion and Transformer Models
1. 论文的主要贡献和创新点
✅ 解决的问题
当前训练加速器中，求和操作通过单个FP32加法器序列化处理会形成循环依赖，导致机器算力被钉在约2 FLOP/cycle，无法发挥硬件性能，是影响模型训练吞吐量的核心痛点。

🚀 提出的新方法与思路
**DTX加速器**：是针对diffusion和transformer模型设计的吞吐量优先训练加速器，核心设计包括：全局消除循环依赖（所有归约操作采用流水线二叉树结构，每个FP算子为两阶段流水线且 initiation interval为1）；集成8×8 weight-stationary systolic array（带有融合偏置/激活/赋形后处理模块）、8 lane向量单元、8 lane融合AdamW流水线、流水线Philox高斯源，上述组件由4槽VLIW字在统一64 KB tile空间内协同发布；验证采用容忍度匹配FP64黄金模型的方案，含精确相等例外，且存在紧边界。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 算力效率 | 216 FLOP/cycle，约为循环依赖基线的108倍 |
| 功耗效率 | 与GPU对比，吞吐量每瓦提升6-10倍 |
| 同节点基线对比 | sky130工艺后，比优化的循环依赖MAC基线高1.9倍 |
| 模型训练效果 | 支持diffusion-MLP训练并显著降低损失 |
| 硬件可行性 | sky130工艺下DRC干净GDS，后route后达到83.3 MHz |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标
任务为diffusion-MLP的训练；指标含义如下：
| 指标 | 含义 |
| --- | --- |
| 模型训练损失 | 训练过程中模型损失值，↓越低越好 |
| 算力密度（FLOP/cycle） | 每周期可实现的浮点运算量，↑越高越好 |
| 吞吐量每瓦 | 单位功耗下的计算吞吐量，↑越高越好 |
| 硬件时钟频率 | 流片后电路工作频率，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 优化的循环依赖MAC基线 | 硬件基线方法 | 存在循环依赖的传统硬件结构 |
| GPU | 通用计算基线 | 通用GPU训练平台 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**验证实验（无表号）**
| 指标 | 结果 |
| --- | --- |
| 测试通过数/总测试数 | 17/17 |
| 测试元素总数 | 107108 |
| 零失败验证 | ✅ |
| 前提违反程序预算倍率 | 5340x |
💡 结论：DTX的验证方案满足误差要求，远超出性能预算的违规测试也能被精准检测。

**diffusion-MLP训练实验（无表号）**
| 指标 | 结果 |
| --- | --- |
| 训练起始损失 | 56.4 |
| 训练最终损失 | 26.0 ✅ |
💡 结论：DTX支持diffusion-MLP训练并有效降低模型损失。

**硬件性能实验（无表号）**
| 指标 | 结果 |
| --- | --- |
| 单周期浮点运算量 | 216 FLOP/cycle ✅ |
| 相对于循环依赖基线的性能倍数 | 108x |
| 与GPU的吞吐量每瓦倍数 | 6-10x |
| sky130工艺后route时钟频率 | 83.3 MHz |
| 相对于同节点循环依赖MAC基线的性能倍数 | 1.9x ✅ |
💡 结论：DTX硬件结构实现了超高的算力效率，在流片后达到了预期性能，功耗效率优于GPU和传统基线。

4. 关键结论和发现
- 主要发现：1）通过全局消除循环依赖的硬件设计，DTX实现了108倍于传统循环依赖结构的算力效率；2）DTX支持diffusion-MLP训练，且在硬件流片后达到了工艺要求；3）DTX的功耗效率相对于GPU提升6-10倍，硬件可行性经sky130流片验证。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：DTX是针对diffusion和transformer模型的吞吐量优先训练加速器，通过消除循环依赖的创新硬件设计，实现了超高计算效率、优异的模型训练效果和功耗效率。

</details>

---

### 6. [Emotion Across Speech and Faces: Shared Affective Mechanisms in Multimodal Foundation Models](https://arxiv.org/abs/2608.17102v1)

**Authors**: Xiutian Zhao, Luqi Sun, Bj\"orn Schuller, Berrak Sisman  
**Category**: cs.CL  
**Published**: 2026-08-19  
**Score**: 45.5  
**Type**: new  
**ArXiv ID**: 2608.17102v1  

#### Abstract
Modern multimodal foundation models (MFMs) have made rapid progress on tasks requiring integrated perception across speech, vision, and language, including emotion recognition. However, it remains unclear whether they recognize speech and facial emotion through shared affective functional units or m...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Emotion Across Speech and Faces: Shared Affective Mechanisms in Multimodal Foundation Models
1. 论文的主要贡献和创新点
✅ 解决的问题：现有多模态基础模型（MFMs）在语音、视觉、语言融合的情感识别任务上取得快速进展，但尚未明确其识别语音和面部情感的内在机制是依赖共享的情感功能单元，还是模态特定通路。
🚀 提出的新方法与思路
**情感敏感神经元（ESNs）分析**：聚焦Gemma-4-12B-it、MiniCPM-o-4.5、Qwen2.5-Omni-7B这三个MFMs的稀疏解码器中与情感类别选择性关联的神经元；采用语音情感识别（SER）和面部表情识别（FER）作为互补探测手段，分别识别声学、视觉ESNs；对视觉ESNs开展因果干预（去激活、激活调整）验证其因果有效性；分析声学与视觉ESNs的情感重叠性和层分布；进行跨模态干预，探索ESNs的跨模态因果迁移性。
🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 情感机制解析维度 | 首次开展多模态基础模型解码器层面的情感功能单元的激活级分析 |
| 跨模态有效性验证 | 通过针对性干预（去激活、激活调控）和跨模态操作，明确ESNs的因果属性与双向迁移性 |
| 情感表征一致性分析 | 揭示语音与面部情感表征在ESNs层面的部分结构对齐特征 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：任务为语音情感识别（SER）和面部表情识别（FER），评估指标相关内容论文未报告
⚔️ 基线方法对比：论文未报告

3. 主要实验结果和性能指标
论文未报告

4. 关键结论和发现
- 主要发现：1）MFMs的稀疏解码器中存在情感敏感神经元（ESNs），其中视觉ESNs具备因果有效性：去激活它们会选择性损害对应面部情感的识别，调整其激活会选择性提升对应情感的识别率；2）声学与视觉ESNs存在情感匹配重叠，且层分布相似，二者间存在部分结构对齐；3）跨模态干预显示，从一模态识别出的ESNs应用于另一模态时，会产生情感特异性影响，存在双向因果迁移。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该研究首次在多模态基础模型的解码器层解析情感功能单元，揭示语音与面部情感识别存在部分共享的情感机制，为多模态情感模型的可解释性与定向调控提供了新思路。

</details>

---

### 7. [GUPO: Gradient Uncertainty-aware Policy Optimization for Post-Training Large Language Models](https://arxiv.org/abs/2608.17411v1)

**Authors**: Peizheng Guo, Jianqi Zhang, Xingyu Zhang, Yun Fan, Jiahuan Zhou, Changwen Zheng, Wenwen Qiang  
**Category**: cs.LG  
**Published**: 2026-08-19  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2608.17411v1  

#### Abstract
Group Relative Policy Optimization (GRPO) has become a widely used approach for post-training Large Language Models (LLMs) for reasoning. In GRPO, the group gradients induced by different queries within the same mini-batch are directly averaged to form the policy update. However, these group gradien...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

GUPO: Gradient Uncertainty-aware Policy Optimization for Post-Training Large Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题：Group Relative Policy Optimization (GRPO)是后训大语言模型（LLM）推理的常用方法，但其将同批次不同查询（query）的组梯度直接平均以生成策略更新的做法存在缺陷：组梯度易出现方向冲突，导致策略更新效果差；且GRPO将组梯度视为确定性贡献，未考虑不同组梯度的可靠性差异。
🚀 提出的新方法与思路
**Gradient Uncertainty-aware Policy Optimization (GUPO)**：采用贝叶斯公式将每个组梯度建模为随机变量并估计其概率分布，再通过基于Dirichlet的公式推导梯度不确定性，最终利用该不确定性在校准组梯度聚合过程中各自的贡献。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 组梯度冲突处理 | 解决GRPO中组梯度方向冲突导致策略更新效果差的问题 |
| 梯度贡献建模 | 考虑组梯度的不确定性，而非将其视为确定性贡献，更合理地聚合梯度以生成策略更新 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告具体数据集名称 | 用于评估GUPO的性能 |
🎯 实验设置与评估指标
任务为后训大语言模型用于推理，具体评估指标论文未报告。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| GRPO | 基准方法 | 原用于后训LLM推理的组梯度平均聚合策略 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体定量结果，仅提及大量基准实验验证了GUPO的有效性，无具体表号、数值等细节。

4. 关键结论和发现
- 主要发现：GUPO通过贝叶斯框架建模组梯度的概率分布并结合Dirichlet形式的梯度不确定性，解决了GRPO的组梯度冲突及未考虑梯度可靠性的问题，能提升策略更新的效果。
- 方法局限性：论文未报告
- 未来工作：论文未报告
✅ **总结一句话**：GUPO是针对后训大语言模型推理的GRPO存在的组梯度冲突与梯度可靠性忽视问题，提出的基于梯度不确定性校准的策略优化方法，通过贝叶斯建模组梯度概率分布并结合Dirichlet推导不确定性来优化梯度聚合，提升策略更新效果。

</details>

---

### 8. [DeAR: Decentralized Agentic Reasoning via Capability Grounding and Collaborative Thought Navigation](https://arxiv.org/abs/2608.17282v1)

**Authors**: Xing Wei, Changmeng Zheng, XiaoYong Wei, Xiufen Ye, Qing Li  
**Category**: cs.AI  
**Published**: 2026-08-19  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2608.17282v1  

#### Abstract
Existing agentic reasoning systems typically rely on centralized protocols. This design introduces routing bottlenecks and static role allocations that often fail when handling complex multimodal queries. We propose DeAR (Decentralized Agentic Reasoning), a framework that shifts from central control...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：DeAR: Decentralized Agentic Reasoning via Capability Grounding and Collaborative Thought Navigation
1. 论文的主要贡献和创新点
✅ 解决的问题
现有agentic reasoning系统采用中心化协议，存在路由瓶颈与静态角色分配缺陷，处理复杂多模态查询时难以获得良好效果。

🚀 提出的新方法与思路
**Decentralized Capability Grounding**：针对输入查询实现依赖的智能体专业化，使智能体可根据任务需求调整自身能力侧重，适配不同查询类型。
**Thought Map Navigation**：实现智能体间的目标性对等交互，引导交互过程聚焦于任务关键环节，提升推理效率。
**Topology Update**：用于自适应错误修正，通过动态调整智能体间的协作拓扑结构优化推理结果，修正过程中的偏差。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 系统架构 | 采用去中心化自主对等协作模式，消除中心化设计带来的路由瓶颈 |
| 智能体协作 | 支持查询依赖的角色专业化，解决静态角色分配无法适配复杂任务的问题 |
| 错误修正 | 搭配拓扑更新机制实现自适应错误修正，提升推理鲁棒性 |
| 任务性能 | 在9种多模态推理与基于文本的QA基准上，性能持续优于近期基线方法 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 9种不同的多模态推理和基于文本的QA基准 | 评估DeAR方法在相关任务上的性能表现 |

🎯 实验设置与评估指标
任务为多模态推理和基于文本的QA任务，论文未报告具体评估指标名称及指标的优劣方向。
| 指标 | 含义 |
| --- | --- |
| 论文未报告 | 论文未报告 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 近期基线方法 | 对比方法 | 近期提出的agentic reasoning相关基线方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体实验结果对应的表号、图号及定量数值，仅指出在9种多模态推理与基于文本的QA基准任务中，DeAR的性能优于近期基线方法。

4. 关键结论和发现
- 主要发现：1. DeAR作为去中心化智能体推理框架，通过三类协作机制实现自主对等交互，在多模态推理与QA任务上性能优于近期基线；2. 所提出的查询依赖智能体专业化、目标性交互、自适应拓扑更新机制，共同保障了推理的有效性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：DeAR是一种采用去中心化自主对等协作模式的智能体推理框架，通过三类机制优化多模态推理与基于文本的QA任务表现，性能优于近期基线方法。

</details>

---

### 9. [Structure-Internalized Rule Language Model for Faithful Knowledge Graph Reasoning](https://arxiv.org/abs/2608.17443v1)

**Authors**: Xingrui Zhuo, Jiapu Wang, Manzong Huang, Gongqing Wu, Xindong Wu  
**Category**: cs.AI  
**Published**: 2026-08-19  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2608.17443v1  

#### Abstract
Knowledge Graph Reasoning (KGR) aims to discover latent facts by leveraging the structural evidence available in KGs, posing a challenge to the structural semantic understanding capability of KGR models. Recent studies have demonstrated that Large Language Models (LLMs) can achieve remarkable progre...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Structure-Internalized Rule Language Model for Faithful Knowledge Graph Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有将大语言模型（LLMs）应用于知识图谱推理（KGR）的方法，存在KG结构上下文与LLM参数知识间的表示不一致问题，该问题导致LLM难以感知符合KG约束的推理证据，论文将该问题称为LLM在KG上的推理证据感知漂移，损害了推理的有效性与忠实性，这一核心矛盾尚未被充分解决。

🚀 提出的新方法与思路
**Structure-Internalized Rule Generator（SIRG）**：为解决上述问题设计的核心模块，作用是整合结构规则生成，耦合结构知识的参数学习与推理逻辑的忠实性评估，让LLM锚定到KG关联的推理证据上；该模块包含三个关键组成部分：a) 增强的上下文学习块，结合结构关系记忆以协调结构知识与参数知识；b) 基于结构不变性学习的KG tokenizer，提供可学习的结构表示；c) 基于规则约束消息传播的神经符号推理器，提供忠实的规则执行反馈。
SIRLM整体框架可无缝集成到标准LLM训练范式（如SFT、GRPO）中。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| KGR任务性能 | 在36个数据集上对17种SOTA KGR方法实现显著优越性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 36个数据集 | 用于KGR任务的实验评估 |

🎯 实验设置与评估指标
任务：知识图谱推理（KGR），通过对比SIRLM与17种SOTA KGR方法的性能验证方法有效性。
| 指标 | 含义 |
| --- | --- |
| 论文未报告 | 论文未报告具体评估指标名称及含义 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 17种SOTA KGR方法 | 现有KGR方法 | 用于与SIRLM进行性能对比 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体实验结果对应的表号、图号及详细数值，仅在摘要中提及：在36个数据集上对比17种SOTA KGR方法时，SIRLM表现出显著优越性。

💡 结论：SIRLM在36个数据集上针对17种SOTA KGR方法的对比中，表现出显著的性能优势。

4. 关键结论和发现
- 主要发现：① 论文将LLM在KG推理中遇到的表示不一致问题定义为推理证据感知漂移，SIRLM通过结构规则生成模块解决了该问题；② SIRLM框架可无缝适配SFT、GRPO等标准LLM训练范式；③ SIRLM在36个数据集上超越17种SOTA KGR方法，性能优势显著。
- 方法局限性：论文未报告SIRLM的局限性相关内容。
- 未来工作：论文未报告未来工作的具体方向。

> ✅ **总结一句话**：本文提出的SIRLM通过整合结构规则生成，耦合KG结构知识与LLM参数学习，解决了LLM在KGR中的推理证据感知漂移问题，在36个数据集上对17种SOTA KGR方法实现了显著性能优势。

</details>

---

### 10. [Towards Safer RAG: Only Agents Capable of System 2 Thinking may Access Untrusted Documents](https://arxiv.org/abs/2608.17153v1)

**Authors**: Mehrdad Ghassabi  
**Category**: cs.CL  
**Published**: 2026-08-19  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2608.17153v1  

#### Abstract
Retrieval-Augmented Generation (RAG) has significantly enhanced the performance of large language models (LLMs), yet these systems remain vulnerable to knowledge-poisoning attacks, in which misinformation in retrieved documents can influence the model's final outputs. Notably, an LLM may correctly d...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Towards Safer RAG: Only Agents Capable of System 2 Thinking may Access Untrusted Documents
1. 论文的主要贡献和创新点
✅ 解决的问题
RAG系统易受知识投毒攻击，恶意检索文档会误导最终输出；现存的Cordon Principle隔离答案合成模型与原始证据虽能防御攻击，但存在显著计算开销；且存在LLM能正确检测文档错误却仍受其影响的矛盾。

🚀 提出的新方法与思路
**基于System 2思维的安全RAG原则**，要求仅具备 deliberative System 2推理能力的代理方可访问不可信文档，替代Cordon Principle的严格隔离策略以降低计算开销；同时引入量化错误信息检测与下游影响差异的新型指标，用于评估安全RAG的防御效果。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 隔离策略 | 无需严格隔离答案合成模型与原始证据，相比Cordon Principle更灵活 |
| 计算开销 | 无Cordon Principle带来的显著计算开销，更实用 |
| 抗投毒鲁棒性 | 具推理能力的代理可更有效抵御错误检索文档的影响，优于标准语言模型 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
实验用于对比不同类型语言模型对知识投毒攻击的抗性，评估指标为量化错误信息检测与下游影响差异的新型指标，指标值越低代表差异越小（错误信息越难误导）↓。
| 指标 | 含义 |
| ---- | ---- |
| 错误信息检测与下游影响差异 | 量化LLM检测文档错误的能力与受该错误影响程度之间的差异，↓越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 标准语言模型（standard language models） | 基线对照 | 不具备deliberative System 2推理能力 |
| 具推理能力的语言模型（reasoning language models） | 本文实验对比的模型 | 具备deliberative System 2推理能力，测试抗错误证据影响的性能 |
| Cordon Principle | 现有安全RAG方法 | 隔离答案合成模型与原始证据，能防御攻击但存在高计算开销 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告

4. 关键结论和发现
- 主要发现：1. LLM存在能检测文档错误但仍受其误导的现象；2. 仅让具备System 2推理能力的代理访问不可信文档，可在防御知识投毒攻击的同时避免Cordon Principle带来的高计算开销；3. 具System 2推理能力的模型对抗错误检索文档的鲁棒性显著优于标准语言模型。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出的仅允许具备System 2推理能力的代理访问不可信文档的安全RAG原则，既有效防御了知识投毒攻击，又降低了现有Cordon Principle带来的计算开销，为安全RAG系统设计提供了更实用的新思路。

</details>

---

### 11. [Data-DPO: Direct Preference Optimization for Target Model Data Selection in LLM Post-Training](https://arxiv.org/abs/2608.16926v1)

**Authors**: Peng Sun, Yi Yang, Antong Zhang, Chunxiao Li, Yanbo Wang, Dianbo Liu, xin chen, Kai Yu, Lu Chen, Tianfan Fu  
**Category**: cs.LG  
**Published**: 2026-08-19  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2608.16926v1  

#### Abstract
Data selection in supervised fine-tuning aims to select a small set of effective samples from large-scale candidate data, reducing training cost while preserving model performance. However, existing methods usually treat data value as a relatively static property, and pay limited attention to the co...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文：Data-DPO: Direct Preference Optimization for Target Model Data Selection in LLM Post-Training
1. 论文的主要贡献和创新点
✅ 解决的问题
现有SFT数据选择方法存在两点核心缺陷：一是将数据价值视为相对静态的属性，二是对数据与目标模型能力分布的兼容性关注有限，导致难以在减少训练成本的同时有效保留模型性能。

🚀 提出的新方法与思路
**Data-DPO方法**：通过一步探测观测目标模型在不同样本上的局部训练反馈，将样本间的激活差异转化为成对数据偏好，训练轻量奖励模型学习面向目标模型的数据偏好；在最终选择阶段，进一步结合目标模型偏好、外部质量得分与边际多样性，构建更稳定有效的训练子集。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 目标模型适应性 | 关注数据与目标模型能力分布的兼容性，突破数据价值静态属性的局限 |
| 数据选择逻辑 | 基于目标模型局部反馈生成的成对偏好，融合多维度因素构建训练子集 |
| 成本与性能平衡 | 从大规模候选数据中筛选小样本子集，降低训练成本的同时保障性能 |
| 场景泛用性 | 在多数据集、多数据预算下均表现优异 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Vision-Flan | 实验验证 |
| LLaVA-CoT | 实验验证 |

🎯 实验设置与评估指标
论文未报告具体的任务细节与评估指标。

⚔️ 基线方法对比
论文未报告具体的基线方法名称及相关细节。

3. 主要实验结果和性能指标
📊 定量结果汇总
论文仅明确提及在Vision-Flan和LLaVA-CoT数据集的多个数据预算下，Data-DPO一致优于现有数据选择基线，且稳定超越全数据训练的性能，未报告具体定量结果的表号、数值等细节。

4. 关键结论和发现
- 主要发现：1. Data-DPO通过观测目标模型局部反馈、融合多维度因素构建训练子集，可有效实现SFT阶段数据选择的成本与性能平衡；2. 该方法在Vision-Flan、LLaVA-CoT数据集的多个数据预算下，表现优于现有数据选择基线及全数据训练。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：Data-DPO是面向目标模型的LLM后训练SFT数据选择方法，通过观测模型局部反馈、融合多维度因素筛选训练子集，能在降低训练成本的同时提升模型性能，在多个数据集及数据预算下均优于现有基线及全数据训练效果。

</details>

---

### 12. [Hierarchical Data Selection via Manifold Coverage and Sparse Feature Coverage in LLM Post-training](https://arxiv.org/abs/2608.16927v1)

**Authors**: Peng Sun, Yi Yang, Antong Zhang, Chunxiao Li, Yanbo Wang, Dianbo Liu, xin chen, Kai Yu, Lu Chen, Tianfan Fu  
**Category**: cs.LG  
**Published**: 2026-08-19  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2608.16927v1  

#### Abstract
As supervised fine-tuning data continues to scale, selecting high-value subsets from large candidate pools is crucial for reducing training cost and improving model performance. Existing methods often measure diversity directly in the original embedding space, where geometric metrics entangle domina...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Hierarchical Data Selection via Manifold Coverage and Sparse Feature Coverage in LLM Post-training
1. 论文的主要贡献和创新点
✅ 解决的问题：监督微调数据规模不断扩大，从大型候选池中选择高价值子集对降低LLM后训练成本、提升模型性能至关重要；现有数据选择方法直接在原始嵌入空间衡量多样性，其几何指标会将主导语义方向、细粒度监督差异与局部噪声混淆，存在语义成分混淆的缺陷。
🚀 提出的新方法与思路
**低维主流形坐标学习模块**：采用密集自编码器学习低维主流形坐标，用于完成粗粒度语义分组；
**质量感知稀疏特征覆盖模块**：在各分组内使用TopK稀疏自编码器，实现质量感知的稀疏特征覆盖。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 数据选择效果 | 在Vision Flan与LLaVA-CoT数据集的多个数据预算下，MASS优于现有强数据选择基线；部分设置下仅需小部分数据即可匹配或超越全数据训练的性能 |
| 训练成本 | 通过分层选择高价值数据子集，可降低LLM后训练的训练成本 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| Vision Flan | 测试MASS数据选择方法的性能 |
| LLaVA-CoT | 测试MASS数据选择方法的性能 |
🎯 实验设置与评估指标
论文未报告具体实验任务类型、评估指标及对应含义。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 现有强数据选择基线 | 数据选择方法 | 直接在原始嵌入空间衡量多样性的传统数据选择方法 |
3. 主要实验结果和性能指标
📊 定量结果汇总
所有实验均未在论文中报告具体表号、数值等详细结果信息：
**主 benchmark 性能（L2/碰撞率等）**：论文未报告
**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot 迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告
4. 关键结论和发现
- 主要发现：1. MASS通过粗粒度主流形分组+细粒度稀疏特征覆盖的分层架构，解决了现有方法在原始嵌入空间中混淆不同语义成分的问题；2. MASS在多个数据预算下的数据选择效果显著优于现有强基线；3. MASS可仅用少量数据子集达到或超过全数据训练的性能。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：MASS是一种分层数据选择方法，通过粗粒度流形分组与细粒度稀疏特征覆盖，能在LLM后训练中高效选出高价值数据子集，降低训练成本且可匹配或超越全数据训练的性能。

</details>

---

### 13. [SCENARIODIFF: A Scenario-level Guidance Framework for Multimodal Time Series Forecasting--Extended Version](https://arxiv.org/abs/2608.17164v1)

**Authors**: Tuan-Binh Tran, Dat Nguyen Cong, Duc-Trong Le, Thanh Trung Huynh, Tung Kieu  
**Category**: cs.LG  
**Published**: 2026-08-19  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2608.17164v1  

#### Abstract
Textual context such as news, reports, and logs can provide valuable signals for time series forecasting, especially when future dynamics are driven by external events that are not yet visible in historical values. Existing multimodal forecasting methods often either ask large language models (LLMs)...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

SCENARIODIFF: A Scenario-level Guidance Framework for Multimodal Time Series Forecasting--Extended Version
1. 论文的主要贡献和创新点
✅ 解决的问题
- 核心痛点：新闻、报告、日志等文本上下文对时间序列预测（尤其是受未来可见性之外的外部事件驱动的预测）有重要价值，但现有多模态时间序列预测方法存在不足；
- 现有方法缺陷1：部分方法让大型语言模型（LLMs）直接预测数值，缺乏对文本上下文的结构化利用；
- 现有方法缺陷2：部分方法隐式融合文本与时间序列，导致上下文对预测的影响难以解释和控制；

🚀 提出的新方法与思路
**Hierarchical Contextual Reasoning Framework**：将弱对齐、含噪声的文档上下文分为三个层级处理，适配多模态时间序列预测需求：
- Historical Context Agent：从原始文档中提取逐步的文本证据；
- Scenario Agent：为预测的未来时间范围生成定性的场景描述；
- Anchor Guidance Agent：为事件相关的未来区域生成稀疏锚点；
**Multimodal Diffusion Transformer**：以三个层级的结构化上下文信号作为条件，实现多模态时间序列预测；
**Anchor Blended Sampling**：在无需重新训练模型的前提下，局部优化生成的时间序列轨迹；

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 上下文影响可解释性 | 采用显式分层的上下文推理结构，每一层的输出对应不同粒度的语境信息，可追溯语境对预测的影响路径 |
| 上下文影响可控性 | 结构化的分层信号可针对性调控不同层面的预测条件，避免隐式融合导致的黑箱式影响 |
| 事件驱动域适配性 | 针对受外部事件驱动的时间序列预测任务，可有效利用事件相关的上下文信号，适配场景需求 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Time-MMD | 作为主实验基准，用于验证SCENARIODIFF在多模态时间序列预测任务中的有效性 |

🎯 实验设置与评估指标
任务为多模态时间序列预测，输入包含时间序列数据与对应文本上下文，输出为未来的时间序列轨迹；论文未报告具体的评估指标及对应表号。

⚔️ 基线方法对比
论文未报告基线方法的具体列表、类型及特点。

3. 主要实验结果和性能指标
📊 定量结果汇总
- 主benchmark性能（L2/碰撞率等）：论文未报告具体定量数值及对应表号；
- 效率对比（FPS / 参数量）：论文未报告；
- 跨域 / zero-shot 迁移：论文未报告；
- 鲁棒性 / 扰动测试：论文未报告；
- 消融实验：论文未报告各模块的效果对比及对应指标数值；

4. 关键结论和发现
- 主要发现：
  1. 针对事件驱动的多模态时间序列预测任务，显式的分层场景指导框架SCENARIODIFF具有明显的有效性；
  2. 在弱对齐、含噪声的文档上下文场景下，结构化的分层上下文信号相比隐式融合方式更适合挖掘文本的预测价值；
- 方法局限性：论文未报告；
- 未来工作：论文未报告；

> ✅ **总结一句话**：SCENARIODIFF通过分层上下文推理框架结合多模态扩散变换器，为事件驱动的多模态时间序列预测提供了显式、可解释可控的场景指导，在Time-MMD基准的事件驱动域任务中表现突出。

</details>

---

### 14. [Auditing Exposure to Harmful Content on TikTok using Multimodal Language Models: A Cross-National, Age-Stratified Study](https://arxiv.org/abs/2608.17583v1)

**Authors**: Hamidreza Saffari, Francesco Pierri  
**Category**: cs.CL  
**Published**: 2026-08-19  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.17583v1  

#### Abstract
Online video platforms can expose young users to harmful content, but independent audits remain difficult because video annotation is costly and moderation judgments vary across languages. We audit TikTok in France, Italy, and Sweden with sockpuppet accounts representing four age personas (13, 16, 1...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Auditing Exposure to Harmful Content on TikTok using Multimodal Language Models: A Cross-National, Age-Stratified Study
1. 论文的主要贡献和创新点
✅ 解决的问题
在线视频平台会向年轻用户暴露有害内容，但独立审计面临三大痛点：视频标注成本高、跨语言审核判断差异大、缺乏分年龄层的系统性跨境审计方法。

🚀 提出的新方法与思路
**Multimodal LLMs支撑的跨境分年龄层有害内容审计**：采用sockpuppet账号模拟13、16、19、40岁四个年龄层，在法国、意大利、瑞典三国的TikTok上，通过被动For-You页滚动、主动滚动搜索有害关键词后再滚动的方式收集36971个视频；选取Gemini 2.5 Flash，采用8帧采样加文本的多模态输入形式，对比本地母语标注验证其表现后，用该模型对10%样本开展审计。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 审计成本 | 采用MLLM减少视频标注的高昂成本，单审计总API费用约50美元，仅为本地视频上传成本的一半 |
| 跨语言适配性 | 依托MLLM的多语言处理能力，规避了跨语言审核判断差异的问题 |
| 年龄分层能力 | 支持模拟不同年龄层用户的行为模式，实现分年龄层的精准有害内容暴露审计 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 法国、意大利、瑞典三国通过sockpuppet账号收集的36971个TikTok视频 | 作为有害内容审计的主要分析数据集 |
| 300个视频的参考集 | 用于验证四个Multimodal LLMs的表现，以选取最优审计模型 |

🎯 实验设置与评估指标
任务为审计TikTok针对不同国家、年龄层用户的有害内容暴露情况；评估指标包括MLLM标注与本地母语标注的一致性（kappa系数，越高越好）、审计的API调用成本（越低越好）。
指标 | 含义
--- | ---
kappa系数 | 衡量MLLM标注与本地母语专业标注的一致性程度
API调用成本 | 开展审计所产生的总费用

⚔️ 基线方法对比
论文未报告基线方法的具体类型及特点，仅提及验证了四个Multimodal LLMs，最终选取表现最优的Gemini 2.5 Flash开展后续审计。

3. 主要实验结果和性能指标
📊 定量结果汇总
**论文未报告** 主 benchmark性能（L2/碰撞率等）
**论文未报告** 效率对比（FPS / 参数量）
**论文未报告** 跨域 / zero-shot迁移
**论文未报告** 鲁棒性 / 扰动测试
**论文未报告** 消融实验
- Gemini 2.5 Flash的聚合kappa系数为0.42，为四个验证的Multimodal LLMs中表现最优
- 关键词搜索返回的有害内容比例为35-56%，在12个国家-年龄组合中的10个中，该比例是被动滚动基线的1.5-7.5倍
- 上述有害内容比例的增长峰值为暂时性，会抹平法国和瑞典原本存在的年龄差异
- 被动滚动场景下，意大利各年龄层用户的有害内容暴露率最高，其中意大利19岁年龄层的有害内容暴露率达48.6%
- TikTok平台自身安全过滤器的拒绝率为1.1%，低估了最明确的有害内容
- MLLM审计的总API费用约50美元

4. 关键结论和发现
- 主要发现：1. 主动搜索有害关键词会导致TikTok有害内容暴露的显著增加，但该增长具有暂时性，会抹平法国和瑞典原本观测到的年龄差异；2. 被动滚动TikTok For-You页时，意大利各年龄层用户的有害内容暴露率高于法国、瑞典；3. TikTok平台自身的安全过滤器对最明确的有害内容存在低估情况，审核覆盖不足。
- 方法局限性：论文未报告明确的方法局限性内容。
- 未来工作：论文未报告明确的未来工作内容。

> ✅ **总结一句话**：本研究提出的基于Multimodal LLMs和sockpuppet账号的低成本、可扩展审计方法，实现了对TikTok跨境分年龄层的有害内容暴露审计，揭示了不同国家的暴露差异及平台安全过滤器的不足。

</details>

---

### 15. [The Price of Thinking: Reasoning Effort as a Model-Specific API Contract](https://arxiv.org/abs/2608.16956v1)

**Authors**: Yeabin Moon  
**Category**: cs.AI  
**Published**: 2026-08-19  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2608.16956v1  

#### Abstract
API buyers purchase a dated contract, not a model name alone: the contract includes the requested and served model, reasoning-effort term or its omission, output rail, service product, prompt, and price schedule. We study the reasoning-effort term through a registered paired contrast of Sonnet 5 wit...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

The Price of Thinking: Reasoning Effort as a Model-Specific API Contract
1. 论文的主要贡献和创新点
✅ 解决的问题：API购买者并非仅基于模型名采购，而是购买包含模型、推理强度等元素的“dated contract”，但目前对API合同中推理强度条款的成本与收益关系的受控对比研究不足，且推理强度的省略语义具有模型特异性尚未得到充分验证。
🚀 提出的新方法与思路：**预注册配对对比实验设计**：以Sonnet 5模型为研究对象，开展该模型在API合同中包含明确高推理强度条款与省略该条款的配对对照实验；使用30个AIME 2026项目，每个项目调用5次；对付费尝试分配固定终端类别，重采样项目但保留重复调用；实验前冻结请求注册表、解析器、终端分类、统计计划和分析管道。
🔍 相比现有方法的优势：论文未报告
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| AIME 2026项目 | 用于对比Sonnet 5模型在不同推理强度API合同下的性能与成本表现 |
🎯 实验设置与评估指标
任务为对比Sonnet 5模型的API合同在包含明确高推理强度条款与省略该条款时的调用成本、准确性及单位正确答案成本。
| 指标 | 含义 | 方向 |
| --- | --- | --- |
| 单次调用成本 | 每次API调用的费用 | ↓ |
| 准确性 | 模型输出的正确率 | ↑ |
| 单位正确答案成本 | 每获得1个正确答案所需的费用 | ↓ |
⚔️ 基线方法对比
论文未报告
3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告
论文中明确报告的定量结果如下：
- 明确高推理强度合同下单次调用成本比省略条款高\$0.01031，95%置信区间为[+\$0.00204, +\$0.01974]；
- 准确性对比为+0.0133，95%置信区间为[-0.0267, +0.0467]，未检测到准确性差异；
- 单位正确答案成本：明确高推理强度合同下为\$0.08665，省略条款下为\$0.07662。
4. 关键结论和发现
- 在Sonnet 5模型的API合同中，设置明确高推理强度条款会提升单次调用成本与单位正确答案成本；
- 该实验未检测到明确高推理强度条款与省略条款之间存在准确性差异，但置信区间允许最高4.67个百分点的准确性增益，无法排除此种可能性；
- API合同中推理强度的省略语义具有模型特异性，现有文档仅达到文档级质量，原始结构不明确时无法验证；
- 研究结论仅适用于Sonnet 5模型、AIME 2026项目及实验采集日期，泛化性受限。
未来工作：论文未报告
> ✅ **总结一句话**：论文通过预注册配对对比实验，揭示了Sonnet 5模型的API合同中明确高推理强度条款对调用成本及单位正确答案成本的影响，未在该实验设置下检测到准确性差异，同时明确了推理强度条款的模型特异性语义。

</details>

---

### 16. [Write, Execute, Refine: From Skill Followers to Skill Optimizers via Reinforcement Learning from Execution Feedback](https://arxiv.org/abs/2608.17587v1)

**Authors**: Kang Peng, Zhiwei Zhang, Yichen Zhang, Zezhong Wang, Yiming Du, Geng Tu, Baojun Wang, Bin Liang, Ruifeng Xu, Kam-Fai Wong  
**Category**: cs.CL  
**Published**: 2026-08-19  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2608.17587v1  

#### Abstract
Expert-written natural language skills can improve tool-using agents, yet agent-authored skills perform 8-11 points worse than using no skill. This gap suggests that following procedural guidance and improving it from execution evidence are distinct capabilities. Inference time loops can repair skil...

---

### 17. [Repetition as Reinforcement: Enhancing Sample Efficiency via Instant Episode Repetition in Reinforcement Learning](https://arxiv.org/abs/2608.17347v1)

**Authors**: Hoda Yamani, Yuning Xing, Koen van Rijnsoever, Bruce A. MacDonald, Henry Williams  
**Category**: cs.LG  
**Published**: 2026-08-19  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2608.17347v1  

#### Abstract
Repetition is a fundamental mechanism in human learning, where revisiting successful experiences strengthens memory, consolidates skills, and improves future performance. Motivated by this biological principle, we introduce Instant Episode Repetition (IER), a simple and novel mechanism that improves...

---

### 18. [Towards Better Agents for Multi-Turn User Interaction: The Next User Turn Is More Than Context](https://arxiv.org/abs/2608.17499v1)

**Authors**: Yiwen Zhao, Zhihao Wen, Yuchen Mao, Mingxuan Jiang, Yihao Hu, Pan Wang, Xin Zhang, Wei Wu  
**Category**: cs.AI  
**Published**: 2026-08-19  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2608.17499v1  

#### Abstract
User-facing tool agents must coordinate dialogue and tool use as user goals unfold over multiple turns. Yet interactive reinforcement learning typically reduces each rollout to a terminal reward, assigning the same credit to effective elicitation, errors, and later repair. The next user turn is more...

---

### 19. [The IOL-AI Challenge: An Open Challenge towards Advancing Linguistic Reasoning](https://arxiv.org/abs/2608.18011v1)

**Authors**: Eduardo S\'anchez, Rita Berrada, Dan-Mircea Mirea, Sara Rajaee, Alexander Piperski, Ana Meta Dolinar, Boris Iomdin, Andrey Nikulin, Mariya Shmatova, Marzieh Fadaee, Julia Kreutzer  
**Category**: cs.CL  
**Published**: 2026-08-19  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2608.18011v1  

#### Abstract
Reasoning in LLMs is overwhelmingly studied in domains that provide a model with rules: mathematics and code. Linguistic puzzles invert this: the solver must first discover the system before reasoning within it. We present the IOL-AI Challenge, an open-science competition run on the unseen problems ...

---

### 20. [TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration](https://arxiv.org/abs/2608.17336v1)

**Authors**: Hanzhi Zhang, Qiao Zhang, Qinglei Cao, Heng Fan, Yan Huang, Kewei Sha, Yunhe Feng  
**Category**: cs.AI  
**Published**: 2026-08-19  
**Score**: 29.0  
**Type**: new  
**ArXiv ID**: 2608.17336v1  

#### Abstract
Long-context prefill in large language models (LLMs) incurs substantial computation and memory traffic because dense self-attention computes quadratic query-key scores. Existing methods either use a uniform low-precision path or select token interactions, leaving spatial precision routing over hardw...

---

### 21. [Agent Lightning v1.0: Towards Harnessed Agentic RL](https://arxiv.org/abs/2608.17528v1)

**Authors**: Zhiyuan He, Siwei Zhang, Zhiwen Zhou, Yuqing Yang, Yu Kang, Yuge Zhang, Luna K. Qiu, Tin Yan Tsui, Jiahang Xu, Chong Luo  
**Category**: cs.AI  
**Published**: 2026-08-19  
**Score**: 24.0  
**Type**: new  
**ArXiv ID**: 2608.17528v1  

#### Abstract
Modern agents operate inside agent harnesses that manage tools, context, and control flow, making the harness a critical part of the agent system. Our original Agent Lightning introduced a disaggregated architecture that connects arbitrary agents to RL training through an LLM endpoint proxy, an appr...

---

### 22. [Beyond the Trace: Coupling an Interpretable Reasoning-State Readout to Native MoE Routing](https://arxiv.org/abs/2608.17638v1)

**Authors**: Kang Chen, Sihan Zhao, Yixin Cao, Yugang Jiang  
**Category**: cs.AI  
**Published**: 2026-08-19  
**Score**: 23.5  
**Type**: new  
**ArXiv ID**: 2608.17638v1  

#### Abstract
What a reasoning model writes is only a partial record of the process that produces it. We introduce a two-level internal readout for mixture-of-experts reasoning. We first distill vocabulary-scale J-space into J64, a 64-axis semantic frame learned from the model's own reasoning states. J64 reveals ...

---

### 23. [Recirculation](https://arxiv.org/abs/2608.17981v1)

**Authors**: Michael C. Mozer, Shoaib Ahmed Siddiqui, Danny Sawyer, Sunny Sanyal, Rosanne Liu  
**Category**: cs.LG  
**Published**: 2026-08-19  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2608.17981v1  

#### Abstract
We describe an inference-time architectural enhancement for off-the-shelf foundation models that markedly reduces perplexity and boosts accuracy across generation and reasoning tasks. Our approach incurs essentially no additional latency during generation, though it requires serial processing in the...

---

### 24. [There is No Theoretical Curse of Multilinguality For Embedding Space Structure](https://arxiv.org/abs/2608.17088v1)

**Authors**: Niyati Bafna, Neha Verma, Vil\'em Zouhar, Philipp Koehn, David Yarowsky  
**Category**: cs.CL  
**Published**: 2026-08-19  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2608.17088v1  

#### Abstract
A central goal of multilingual NLP is to achieve high monolingual performance per language and cross-lingual alignment for large-scale language coverage with a multilingual model. The curse of multilinguality describes the phenomenon of degradation in multilingual model performance as we increase la...

---

### 25. [Leveraging Association Context Retrieval in Knowledge Edit- ing to Build White-Box Attacks on LLMs](https://arxiv.org/abs/2608.17836v1)

**Authors**: Roman Maksimov, Vladimir Aletov, Vladimir Solodkin, Dmitry Bylinkin, Daniil Medyakov, Aleksandr Beznosikov  
**Category**: cs.LG  
**Published**: 2026-08-19  
**Score**: 21.5  
**Type**: new  
**ArXiv ID**: 2608.17836v1  

#### Abstract
As large language models (LLMs) are granted increasing autonomy, it is essential to investigate methods that can induce unsafe behavior. We propose a novel white-box attack inspired by locate-then-edit approaches from the field of Knowledge Editing. Our choice is motivated by the observation that mo...

---

### 26. [KernelArc: A Multi-Agent Framework for GPU Kernel Optimization](https://arxiv.org/abs/2608.17071v1)

**Authors**: Joyjit Kundu, Ben Stoffelen, Kaili Wang, Peter Vrancx, Ludovic Denoyer  
**Category**: cs.AI  
**Published**: 2026-08-19  
**Score**: 18.0  
**Type**: new  
**ArXiv ID**: 2608.17071v1  

#### Abstract
We present KernelArc, a multi-agent framework for autonomous GPU kernel optimization across heterogeneous workloads. Strategy-specialized agents run in parallel and coordinate through conclusions-only shared memory, a deterministic benchmark guard, and read-only cross-agent state with plateau-trigge...

---

### 27. [LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents](https://arxiv.org/abs/2608.17393v1)

**Authors**: Yiming Du, Yuxin Jiang, Tao Yuan, Jianbo Dai, Shaowei Wang, Jierun Chen, Chaofan Tao, Xianzhi Yu, Lifeng Shang, Kam-Fai Wong, Xiaohui Li, Haoli Bai  
**Category**: cs.AI  
**Published**: 2026-08-19  
**Score**: 17.0  
**Type**: new  
**ArXiv ID**: 2608.17393v1  

#### Abstract
Reinforcement learning for coding agents increasingly relies on long-running agent harnesses to manage tool integration, repository contexts, and execution feedback. However, the native execution environments of these harnesses are inherently misaligned with policy-gradient training: environmental c...

---

### 28. [Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Requirements](https://arxiv.org/abs/2608.17310v1)

**Authors**: Zhi Zheng, Rongsheng Chen, Yunpeng Ba, Zhenkun Wang, Yee Whye Teh, Wee Sun Lee  
**Category**: cs.LG  
**Published**: 2026-08-19  
**Score**: 15.5  
**Type**: new  
**ArXiv ID**: 2608.17310v1  

#### Abstract
Reinforcement Learning (RL) has been promising in single-turn LLM fine-tuning. However, long-horizon agentic reasoning introduces increasingly branching interactions and sparse rewards, exposing several limitations of RL: its heavyweight backpropagation-based training stack makes it impractical to f...

---

### 29. [ETHEREAL: A 25.6-$\\mu$s/inf. Low-latency Event-driven Graph-neural-network Processor for High-resolution Vision at the Edge](https://arxiv.org/abs/2608.17787v1)

**Authors**: Adrian Kneip, Martin Lefebvre, Daniel Gehrig, Victoria Catal\'an Pastor, Davide Scaramuzza, Marian Verhelst, Charlotte Frenkel  
**Category**: cs.AR  
**Published**: 2026-08-19  
**Score**: 15.0  
**Type**: new  
**ArXiv ID**: 2608.17787v1  

#### Abstract
Dynamic vision sensors (DVS) are enticing candidates to reach the low-latency, sub-ms target of edge-vision applications, as they generate events with a $\mu$s-level time resolution. However, using DVS front ends also calls for novel algorithm/hardware back ends capable of efficiently handling strea...

---

### 30. [PlanPO: Group Planning-Aware Policy Optimization for Multi-Turn Agentic LLMs](https://arxiv.org/abs/2608.17289v1)

**Authors**: Dayang Liang, Liyuan He, Xuan Feng, Shuxin Li, Bo An, Yunlong Liu  
**Category**: cs.AI  
**Published**: 2026-08-19  
**Score**: 14.0  
**Type**: new  
**ArXiv ID**: 2608.17289v1  

#### Abstract
Group-relative policy optimization has emerged as a key paradigm for training agentic large language models (LLMs) on multi-turn interactive tasks. However, most existing variants fail to distinguish advantages among successful trajectories even when these trajectories differ substantially in their ...

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
