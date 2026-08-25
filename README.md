# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-08-25 06:18:54 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [MCite-RL: Towards Reliable Multimodal RAG via Citation-enhanced Agentic Reinforcement Learning](https://arxiv.org/abs/2608.21808v1)

**Authors**: Suifeng Zhao, Zida Liu, Xinyu Lei, Lei Sun, Jun Gao, Sujian Li  
**Category**: cs.CL  
**Published**: 2026-08-25  
**Score**: 94.5  
**Type**: new  
**ArXiv ID**: 2608.21808v1  

#### Abstract
Multimodal Retrieval-Augmented Generation (RAG) with visual citation is crucial for ensuring the traceability and verifiability of MLLMs. However, current RAG and SFT-based methods struggle to achieve robust cross-modal reasoning, causing imprecise visual citations or decoupling between the citation...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

MCite-RL: Towards Reliable Multimodal RAG via Citation-enhanced Agentic Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
当前Multimodal RAG及基于SFT的方法存在跨模态推理稳健性不足的核心痛点，其中Multimodal RAG方法存在引用与生成答案脱钩的缺陷，基于SFT的方法存在视觉引用不精确的缺陷，共同导致多模态大语言模型（MLLMs）的可追溯性与可验证性不足。
🚀 提出的新方法与思路
**Agentic Refinement模块**：该模块用于视觉引用任务，通过迭代检索、推理和递归裁剪逐步缩小搜索空间，将视觉引用从静态步骤转化为动态的、证据驱动的推理过程。
**Citation-enhanced Reward机制**：在强化学习范式中整合过程级反馈与结果级反馈，实现对答案准确性与源可追溯性的协同优化。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 引用与答案的协同优化 | 有效实现引用精度与答案质量的联合提升 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Wiki-VISA | 本实验的基准测试数据集 |
| FinRAGBench-V | 本实验的基准测试数据集 |
| MMLongBench-Doc | 本实验的基准测试数据集 |
🎯 实验设置与评估指标
论文未报告
⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体的定量实验结果及对应表格（无明确数值、表号信息）

4. 关键结论和发现
- 主要发现：MCite-RL框架通过Agentic Refinement模块和Citation-enhanced Reward机制，在Wiki-VISA、FinRAGBench-V、MMLongBench-Doc等多模态RAG基准上有效实现了引用精度与答案质量的联合优化。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：MCite-RL是一种引用增强的智能体强化学习框架，解决了现有多模态RAG方法视觉引用不精确或引用与答案脱钩的问题，可在多个基准上协同提升引用精度与答案质量。

</details>

---

### 2. [GTA-RAG: Graph-Trajectory-Augmented Reinforcement Learning for Multi-Turn Retrieval-Augmented Reasoning](https://arxiv.org/abs/2608.22479v1)

**Authors**: Jun Chen, Yongchao Liu, Pengyu Qiu, Jiajun Zheng, Juelu Zhang, Yujie Zeng, Qin Zhang, Ziyue Qiao, Xiao Luo  
**Category**: cs.CL  
**Published**: 2026-08-25  
**Score**: 94.0  
**Type**: new  
**ArXiv ID**: 2608.22479v1  

#### Abstract
Retrieval-augmented generation (RAG) enables LLMs to access external knowledge for answering knowledge-intensive questions. For complex multi-hop questions, multi-turn retrieval-augmented reasoning extends RAG into an iterative process that repeatedly searches for and integrates evidence across docu...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

GTA-RAG: Graph-Trajectory-Augmented Reinforcement Learning for Multi-Turn Retrieval-Augmented Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有用于agentic RAG的强化学习方法通常采用最终答案奖励，存在监督信号稀疏的问题，且未考虑模型是否实际获取了所需的证据链，无法满足多跳检索增强推理对证据获取的要求。

🚀 提出的新方法与思路
**Graph-Trajectory-Augmented RL Framework**：该框架从实体-文档图中采样连通文档路径，合成多跳QA轨迹，通过部署的检索器验证这些轨迹以获取可执行的轨迹级监督信号；随后使用Group Relative Policy Optimization（GRPO）优化检索策略，采用轨迹引导奖励函数，该奖励同时鼓励生成准确答案和获取目标证据文档，最后在自然QA实例上进行答案奖励训练。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 推理性能 | 在多跳和简单QA基准上均优于基于RL的RAG基线 |
| 证据链覆盖 | 显著提升证据链覆盖能力 |
| 监督信号质量 | 提供轨迹级监督，解决仅用最终答案奖励导致的监督信号稀疏问题 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 三个多跳QA基准 | 评估多跳检索增强推理性能 |
| 两个简单QA基准 | 评估简单问答性能 |

🎯 实验设置与评估指标
任务：多轮检索增强推理，包含多跳和简单QA任务。论文未报告具体评估指标名称及细节。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 基于RL的RAG基线 | 对比基线 | 采用最终答案奖励的强化学习方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能**：论文未报告具体定量数值、对应表号或图号。
**效率对比**：论文未报告。
**跨域/zero-shot迁移**：论文未报告。
**鲁棒性/扰动测试**：论文未报告。
**消融实验**：论文未报告。

4. 关键结论和发现
- 主要发现：GTA-RAG在三个多跳和两个简单QA基准上均优于基于RL的RAG基线；GTA-RAG能显著提升证据链覆盖；轨迹级监督结合GRPO的框架可有效优化多轮检索增强推理。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：GTA-RAG是一种结合图轨迹增强强化学习与轨迹级监督的多轮检索增强推理框架，可提升推理性能和证据链覆盖，优于现有基于RL的RAG基线。

</details>

---

### 3. [SAEM: Stage-Aware Expert Management for Memory-Efficient MoE Inference in Chain-of-Thought Reasoning](https://arxiv.org/abs/2608.21614v1)

**Authors**: Yujie Zhang, Bin Gao, Tulika Mitra  
**Category**: cs.AI  
**Published**: 2026-08-25  
**Score**: 89.5  
**Type**: new  
**ArXiv ID**: 2608.21614v1  

#### Abstract
Chain-of-thought (CoT) prompting improves LLM reasoning by decomposing complex problems into intermediate steps, but its sequential nature increases decoding latency and memory usage. Mixture-of-Experts (MoE) models scale capacity through sparse expert activation, yet their full expert weights often...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

SAEM: Stage-Aware Expert Management for Memory-Efficient MoE Inference in Chain-of-Thought Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
CoT提示通过将复杂问题分解为中间步骤提升LLM推理能力，但其串行特性会增加解码延迟与内存使用；Mixture-of-Experts（MoE）模型通过稀疏专家激活拓展容量，但全专家权重常超出GPU内存，需进行高成本的GPU-CPU传输；现有运行时对所有令牌统一处理，忽略CoT轨迹的关键结构属性——连续推理阶段呈现连贯可预测的专家激活模式，进而导致缓存低效与不必要的数据移动。

🚀 提出的新方法与思路
**Stage-Aware Caching**：检测推理阶段边界，利用阶段级激活连贯性指导专家的放置，优化缓存策略；
**Expert-Aligned Token Repacking**：调整令牌的打包方式，适配专家激活的阶段特性；
**In-Situ CPU Execution**：在CPU端原位执行部分操作，减少不必要的数据传输与内核碎片化问题。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| MoE推理性能 | 在受限GPU内存下，对比最强的状态-of-the-art缓存与卸载基线，吞吐量实现提升 |
| 计算与数据效率 | 减少数据传输与内核碎片化 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 数学和科学推理工作负载 | 评估SAEM在CoT推理场景下的MoE推理性能 |

🎯 实验设置与评估指标
实验任务为数学和科学推理的Chain-of-Thought推理下的MoE推理，评估指标如下：
| 指标 | 含义 |
| --- | --- |
| 吞吐量 | MoE推理的吞吐量，越高越好↑ |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 最强的状态-of-the-art缓存与卸载基线 | MoE推理运行时基线 | 对所有令牌统一处理，未利用CoT的阶段级激活特性 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能**：论文未提供对应表号、图号或章节标注的定量数值，仅提及存在吞吐量提升（无法定位具体结果来源）
**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot 迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告

4. 关键结论和发现
- 主要发现：1. CoT推理的连续阶段存在连贯可预测的专家激活模式，该特性可用于优化MoE推理运行策略；2. SAEM的阶段感知专家管理方案可在受限GPU内存下提升MoE推理的吞吐量；3. 校准数据与工作负载匹配时，SAEM的性能提升更显著。
- 方法局限性：论文未报告
- 未来工作：论文未报告

✅ **总结一句话**：SAEM是一种面向CoT推理的阶段感知MoE推理运行时，通过整合阶段感知缓存、专家对齐令牌重打包与原位CPU执行，减少数据传输与内核碎片化，在受限GPU内存下提升了MoE推理的吞吐量。

</details>

---

### 4. [PowerSlider: Exploiting Phase Asymmetry for LLM Serving under Demand Response](https://arxiv.org/abs/2608.21719v1)

**Authors**: Yueying Li, Jiayang Chen, Yuanfan Chen, Leo Han, Haoran Qiu, Esha Choukse, Rodrigo Fonseca, Udit Gupta  
**Category**: cs.DC  
**Published**: 2026-08-25  
**Score**: 89.5  
**Type**: new  
**ArXiv ID**: 2608.21719v1  

#### Abstract
AI inference clusters are increasingly constrained by instantaneous power, not just energy: grid operators condition new capacity on demand response, imposing time-varying power caps. Existing LLM serving systems optimize a static energy objective or shed fixed priority tiers under load; either way,...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

PowerSlider: Exploiting Phase Asymmetry for LLM Serving under Demand Response
1. 论文的主要贡献和创新点
✅ 解决的问题
AI推理集群受瞬时功率和能源双重约束，电网运营商通过需求响应机制设置时变功率上限；现有LLM serving系统要么优化静态能源目标，要么在负载下舍弃固定优先级层，两种方式在功率上限变化时均会出现goodput崩溃；LLM流水线不同阶段（compute-bound的prefill、memory-bound的answer decode、需KV缓存协同调度的推理思考阶段）的功率-性能特性存在不对称性，需将功率资源定向分配给单位功率性能损失最小的阶段。

🚀 提出的新方法与思路
**Flex SLO合约**：将用户的松弛转化为优化约束，平衡服务质量与功率约束；
**prefill-think-answer阶段解耦**：暴露LLM流水线各阶段的频率与KV缓存控制自由度，实现细粒度功率分配；
**KKT在线求解器**：每次功率上限变化时在7.7 ms内完成重新求解，配套故障安全机制（DVFS达到静态功率瓶颈时，关断已耗尽的实例）保障功率合规。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 30%功率上限降低场景下在线goodput | 达78.3%，为最佳基线（47.6%）的1.64倍 |
| 延迟尾部分布 | 维持在1.3×额定值内，远低于基线（2.3-6×，最高12×） |
| CAISO电网紧急日场景（最低0.41×额定功率）下平均goodput | 达92%，最低时54%，所有基线均低于7% |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| SGLang生产轨迹 | 在线LLM serving基准实验 |
| CAISO电网紧急日重放数据 | 极端时变功率约束下的serving实验 |

🎯 实验设置与评估指标
任务：LLM服务在时变功率上限下的性能优化。
| 指标 | 含义 |
| --- | --- |
| 在线goodput | 越高越好 |
| 延迟尾部分布（相对于额定值的倍数） | 越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 最佳基线（共5种） | 通用LLM serving优化方法 | 采用静态能源优化或固定优先级调度策略，功率上限变化时性能显著下降 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**在线LLM serving基准实验（30%功率上限降低场景）**
论文正文报告结果如下：
| 指标 | PowerSlider | 最佳基线 | 最优值标记 |
| --- | --- | --- | --- |
| 在线goodput | 78.3% | 47.6% | 78.3% ✅ |
| 95分位延迟倍数 | 1.3× | 2.3-6× | 1.3× ✅ |
💡 结论：PowerSlider在30%功率上限降低场景下的在线好put和延迟性能均显著优于基线方法。

**极端功率约束实验（CAISO电网紧急日场景）**
论文正文报告结果如下：
| 指标 | PowerSlider | 所有基线 | 最优值标记 |
| --- | --- | --- | --- |
| 平均goodput | 92% | 均低于7% | 92% ✅ |
| 最低goodput（功率0.41×额定时） | 54% | 未明确（均低于7%） | 54% ✅ |
💡 结论：PowerSlider在极端时变功率约束下仍能保持较高的服务性能，基线方法无法适配该场景。

**消融实验**：论文未报告

4. 关键结论和发现
- 主要发现：1. LLM流水线各阶段的功率-性能特性存在不对称性，需细粒度调度适配时变功率约束；2. PowerSlider的Flex SLO合约、阶段解耦和KKT在线求解器可快速适配功率上限变化，实现高效服务；3. 在极端电网功率约束下，PowerSlider的性能远优于现有基线方法。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：PowerSlider通过利用LLM流水线各阶段的功率性能不对称性，结合Flex SLO合约、阶段解耦和KKT在线求解器，在时变功率约束下实现了LLM服务的高吞吐量与低延迟性能。

</details>

---

### 5. [Hints, Critics, and Teachers: Prior Injection for Sparse-Reward RL in Vision-Language Math Reasoning](https://arxiv.org/abs/2608.21811v1)

**Authors**: Qiqian Fu  
**Category**: cs.AI  
**Published**: 2026-08-25  
**Score**: 83.0  
**Type**: new  
**ArXiv ID**: 2608.21811v1  

#### Abstract
Reinforcement learning for vision-language math reasoning starves under sparse reward: on a pool of 20,830 visual-math problems where Qwen2-VL-2B answers 3.6% of rollouts correctly, 85-97% of GRPO rollout groups are entirely wrong and contribute zero gradient. We train eleven methods under identical...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Hints, Critics, and Teachers: Prior Injection for Sparse-Reward RL in Vision-Language Math Reasoning
1. 论文的主要贡献和创新点
✅解决的问题
视觉语言数学推理的强化学习面临稀疏奖励困境：20830道视觉数学题中Qwen2-VL-2B的rollout正确率仅3.6%，85-97%的GRPO rollout组完全错误，无法提供有效梯度。现有先验注入方法存在缺陷，部分先验无法有效传递给策略（被教师截断、门控抑制或因批评器参数错误丢失）。
🚀 提出的新方法与思路
**多类型先验注入策略**：针对稀疏奖励RL的视觉语言数学推理任务，注入三种不同类型的先验：文本类型先验（参考解提示）、分布类型先验（7B教师模型的on-policy蒸馏）、价值类型先验（带MSE或HL-Gauss分类损失的预训练批评器），在11种方法中验证有效先验的作用。
**提示引导探索机制**：明确提示增益的核心是Hint-Guided Exploration，而非UFT的辅助损失。
**批评器损失替换优化**：将批评器的MSE损失替换为HL-Gauss交叉熵损失，提升模型性能。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 先验传递有效性 | 有效传递先验的方法与先验失效的方法在域内指标和跨域迁移（DynaMath）上完全分离，无重叠 |
| 域内性能提升 | 替换批评器的MSE损失为HL-Gauss交叉熵损失，域内性能提升14.4个百分点 |
| 跨域迁移预测准确性 | 选择最难的域内评估切片，可更准确预测模型的跨域迁移能力 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 20830道视觉数学题 | 训练以及域内性能评估 |
| DynaMath | 跨域迁移性能评估 |
🎯 实验设置与评估指标
任务：视觉语言数学推理的稀疏奖励强化学习，采用GRPO算法进行rollout。
| 指标 | 含义（箭头方向） |
| --- | --- |
| 域内准确率 | 20830道视觉数学题上的推理正确率，↑ 越高越好 |
| 跨域准确率 | DynaMath数据集上的推理正确率，↑ 越高越好 |
| Spearman相关性 | 评估切片与跨域迁移能力的关联程度，↑ 越高表示预测越准确 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 无先验基线 | 基准方法 | 未注入任何先验 |
| 教师截断先验方法 | 先验失效方法 | 先验被教师截断，无法传递给策略 |
| 门控抑制先验方法 | 先验失效方法 | 先验被门控机制抑制 |
| 参数错误批评器方法 | 先验失效方法 | 批评器参数错误，导致先验丢失 |
| UFT辅助损失方法 | 对比方法 | 采用UFT辅助损失，用于验证提示增益的核心机制 |
| 有效先验方法（共6种） | 提出的有效方法 | 先验可有效传递给策略 |

3. 主要实验结果和性能指标
📊 定量结果汇总
正文提及的关键结果：
- HL-Gauss替换MSE损失的域内性能提升：+14.4个百分点
- 易域内切片与跨域迁移相关性：Spearman rho = -0.74，n=11，permutation p=0.011
- 最难域内切片与跨域迁移相关性：Spearman rho = +0.89，p<0.001
- 有效先验与失效先验的指标分离：无重叠
💡 结论：有效传递先验的方法可显著提升视觉语言数学推理的性能，且评估切片的选择会影响跨域迁移的预测准确性，最难域内切片更适合预测跨域迁移能力。
（注：主benchmark性能、效率对比、鲁棒性测试、消融实验均论文未报告）

4. 关键结论和发现
- 主要发现：1. 有效传递先验可显著提升视觉语言数学推理的稀疏奖励RL性能，且此类方法与先验失效方法在域内指标和跨域迁移上完全分离；2. 域内评估切片的选择会误导跨域迁移的预测：易域内切片与跨域迁移负相关，而最难域内切片与跨域迁移正相关，该反转源于近chance的多选择子集奖励模型对未改变模型的奖励；3. 提示引导的探索是提示增益的核心，替换批评器的MSE损失为HL-Gauss交叉熵损失可带来14.4个百分点的域内性能提升。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：针对视觉语言数学推理的稀疏奖励RL困境，本文通过注入文本、分布、价值三类先验，结合提示引导探索和HL-Gauss损失替换，显著提升了域内性能和跨域迁移能力，且发现域内评估切片的选择会影响跨域迁移的预测准确性。

</details>

---

### 6. [CaRGo-T: Causal Reasoning Graph-of-Thought improves Multimodal Humor Comprehension](https://arxiv.org/abs/2608.23172v1)

**Authors**: Abhilash Nandy, Rahul Seetharaman, Aman Bansal, Rounak Saha, Manav Nitin Kapadnis, Millon Madhur Das, Pawan Goyal, Niloy Ganguly  
**Category**: cs.CL  
**Published**: 2026-08-25  
**Score**: 73.5  
**Type**: new  
**ArXiv ID**: 2608.23172v1  

#### Abstract
Large-scale vision-language models (VLMs) have demonstrated remarkable versatility across a wide range of multimodal tasks. However, understanding humor remains challenging because humorous content often depends on subtle interactions among entities, events, context, and implicit relationships acros...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

CaRGo-T: Causal Reasoning Graph-of-Thought improves Multimodal Humor Comprehension
1. 论文的主要贡献和创新点
✅ 解决的问题
传统大型视觉语言模型（VLMs）在多模态幽默理解任务上存在局限：幽默内容依赖图像与文本模态间实体、事件、上下文及隐式关系的微妙互动，这类复杂推理链难以通过常规提示或线性Chain-of-Thought推理有效捕捉。

🚀 提出的新方法与思路
**CaRGo-T (Causal Reasoning Graph-of-Thought)**：该推理框架将多模态幽默背后的因果与上下文关系表示为轻量型基于图的推理结构，图被序列化为VLM生成的代码类表示，可被相同或不同VLM解释，以在零样本或上下文学习设置中生成最终预测。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 多模态推理建模 | 采用轻量型图结构，替代常规线性推理或传统提示，有效捕捉跨模态因果与上下文关系 |
| 目标信息相关性 | 生成的推理表示包含更多与任务目标输出相关的信息 |
| 任务性能表现 | 幽默理解任务约提升1-20%，幽默检测任务约提升1-3%，优于现有基于推理的基线方法 |
| 适用场景 | 支持零样本或上下文学习设置，可适配相同或不同VLM |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 涵盖讽刺、反讽、梗图等多种喜剧形式的四个数据集 | 用于幽默理解、幽默检测两个任务的评估 |

🎯 实验设置与评估指标
任务为幽默理解、幽默检测多模态任务，评估指标论文未明确说明具体名称及含义。
| 指标 | 含义 |
| --- | --- |
| 论文未报告 | 论文未明确说明评估指标的具体名称及含义 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 现有基于推理的基线方法 | 未明确 | 未明确 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能**
论文未报告对应结果的表号、图号等定位信息，仅提及CaRGo-T相比现有推理基线方法，在幽默理解任务上实现约1-20%的性能提升，在幽默检测任务上实现约1-3%的性能提升。
💡 结论：CaRGo-T框架可在多模态幽默相关任务上获得优于现有推理基线方法的性能。

效率对比：论文未报告
跨域/zero-shot迁移：论文未报告具体结果，仅提及框架支持零样本或上下文学习设置
鲁棒性/扰动测试：论文未报告
消融实验：论文未报告

4. 关键结论和发现
- 主要发现：①CaRGo-T是针对多模态幽默理解的有效框架，可提升幽默理解与幽默检测任务的性能；②该框架生成的推理表示相比基线方法，包含更多与任务目标相关的信息；③框架支持零样本或上下文学习，可适配不同VLM。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：CaRGo-T是一种基于因果推理图结构的多模态幽默理解框架，通过建模跨模态的因果与上下文关系，有效捕捉多模态幽默的复杂互动，实现了幽默理解与检测任务的性能提升，并生成了更具目标相关性的推理表示。

</details>

---

### 7. [Think with Structured Grounding: Perceptual Reinforcement Learning for Chart and Visual-Tabular Understanding](https://arxiv.org/abs/2608.22429v1)

**Authors**: Changjiang Jiang, Qiannian Zhao, Lei Xin, Jinxiang Xie, Preslav Nakov, Zhuohan Xie  
**Category**: cs.AI  
**Published**: 2026-08-25  
**Score**: 66.0  
**Type**: new  
**ArXiv ID**: 2608.22429v1  

#### Abstract
Multimodal Large Language Models (MLLMs) capable of thinking with images often rely on external tools for fine-grained perception. However, this reliance introduces significant inference latency and fails to effectively resolve the spatial-structural gap-a fundamental challenge in text-dense and str...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Think with Structured Grounding: Perceptual Reinforcement Learning for Chart and Visual-Tabular Understanding
1. 论文的主要贡献和创新点
✅ 解决的问题
1. 依赖外部工具的多模态大语言模型（MLLMs）会引入显著推理延迟，且无法有效解决文本密集、具有严格相对空间排列结构的视觉（如图表、可视化表格）的空间结构差距问题；
2. 无外部工具的标准MLLMs无法有效处理这类细粒度视觉推理任务。
🚀 提出的新方法与思路
**TwSG**：是一种新型细粒度图像感知框架，旨在将复杂图像的工具使用能力内化到模型中；它将多步推理和微裁剪的益处合并为推理阶段的单一高效前向传播。
该框架的训练流程包含两个阶段：
**冷启动监督微调（SFT）阶段**：使用带聚焦区域描述的多轮数据来促进模型的复杂推理和错误恢复；
**强化微调（RFT）阶段**：由新型过程奖励机制TL-GRPO驱动，以鼓励模型进行策略性推理。
此外，该方法还会利用MLLM以地面真实答案为指导识别关键区域，提示教师模型生成高质量视觉问答（VQA）数据，并将细粒度、基于区域的监督信号蒸馏回全图像表示。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 推理效率 | 减少推理延迟 |
| 任务性能 | 大幅提升任务准确率 |
| 模型鲁棒性 | 显著提升模型鲁棒性 |
| 模型能力 | 赋予模型原生细粒度区域描述和灵活推理能力 |
2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：论文未报告
⚔️ 基线方法对比：论文未报告
3. 主要实验结果和性能指标
论文未报告
4. 关键结论和发现
- 主要发现：1. TwSG可减少推理延迟同时大幅提升准确率和鲁棒性；2. TwSG能赋予模型原生细粒度区域描述与灵活推理能力。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：TwSG是一种将复杂图像感知工具能力内化的新型细粒度图像感知框架，通过两阶段训练提升了模型在图表和视觉表格理解任务中的推理效率与性能。

</details>

---

### 8. [ESCRAG-R1: Retrieval-Augmented Reinforcement Learning for Emotional Support Conversation](https://arxiv.org/abs/2608.21925v1)

**Authors**: Weichu Liu, Yuxuan Hu, Yirong Sun, Ningning Mao, Ziyun Zhang, Jian Chen, Mingyang Xu, Qishan Zhong, Chengming Li  
**Category**: cs.AI  
**Published**: 2026-08-25  
**Score**: 61.0  
**Type**: new  
**ArXiv ID**: 2608.21925v1  

#### Abstract
Emotional Support Conversation (ESC) systems aim to provide holistic support by balancing professional therapeutic competence with natural empathy. However, existing methods struggle to simultaneously achieve structured, stage-aware reasoning and seamless empathy-expertise alignment, often resulting...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：ESCRAG-R1: Retrieval-Augmented Reinforcement Learning for Emotional Support Conversation
1. 论文的主要贡献和创新点
✅ 解决的问题
现有情感支持对话（ESC）系统难以同时实现结构化的阶段感知推理，以及共情能力与专业咨询能力的无缝对齐，常出现临床策略与通用安慰人工拼接的缺陷。

🚀 提出的新方法与思路
**ESCRAG-R1框架**：整合检索式心理引导至Group Relative Policy Optimization（GRPO）中，将外部检索得到的心理相关知识转化为健壮的学习信号，在对话生成前激发模型的明确内部推理，从根本上重塑模型的内部策略。
**ESC-Preference数据集构建**：基于“来访者-咨询师-评判”的评估框架，构建高质量的偏好数据集，为ESC系统的优化提供精确的共情感知奖励信号。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 推理结构 | 可实现结构化的阶段感知推理 |
| 能力对齐 | 缓解共情表达与专业指导的人工拼接，实现二者的自然整合 |
| 奖励监督 | 提供具有精确共情感知的训练监督信号 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| ESC-Preference | 为ESCRAG-R1的优化提供具有精确共情感知的可靠监督信号 |

🎯 实验设置与评估指标
任务：情感支持对话系统的性能评估
论文未报告实验设置的具体细节与评估指标的相关信息。

⚔️ 基线方法对比
论文未报告基线方法的具体类型与特点。

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体的实验结果、表号、指标数值及各类实验（主benchmark、效率、跨域/zero-shot、鲁棒性、消融实验）的相关数据。

4. 关键结论和发现
- 主要发现：
  1. ESCRAG-R1整合检索式心理引导与GRPO的框架，可有效缓解现有ESC系统中临床策略与通用安慰人工拼接的问题，实现专业指导与共情表达的自然整合；
  2. ESC-Preference数据集可为ESC系统的优化提供精确的共情感知奖励信号；
- 方法局限性：论文未报告；
- 未来工作：论文未报告；

> ✅ **总结一句话**：ESCRAG-R1是整合检索式心理引导与Group Relative Policy Optimization的情感支持对话系统框架，能够缓解现有方法中专业指导与共情表达人工拼接的缺陷，实现二者的自然整合。

</details>

---

### 9. [WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs](https://arxiv.org/abs/2608.22704v1)

**Authors**: Yiming Yao, Chenyang Lyu, Xuanfan Ni, Longyue Wang, Weihua Luo, Yazheng Yang, Jinsong Su  
**Category**: cs.CL  
**Published**: 2026-08-25  
**Score**: 55.0  
**Type**: new  
**ArXiv ID**: 2608.22704v1  

#### Abstract
Long-form audio inputs make the KV cache the dominant memory cost of speech LLMs. Prefill-only KV compression methods permanently discard audio KV positions once evicted, with no pathway to recover them during decoding. We show this is fragile on long-form audio: prefill attention concentrates near ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs
1. 论文的主要贡献和创新点
✅ 解决的问题：长音频输入下，KV缓存是语音大模型的主要内存成本；仅预填充阶段的KV压缩方法会永久丢弃置换后的音频KV位置，解码阶段无法恢复，在长音频场景中表现脆弱；同时预填充注意力集中于音频开头（注意力汇效应）、解码注意力分布广泛且二者重要性排名重叠性弱，加剧了该类方法的失效问题。
🚀 提出的新方法与思路
**WnW (Waxing-and-Waning KV cache)**：通过离线校准将KV头分为anchor、tidal、fixed三类角色；Anchor头保留在GPU中作为解码时的重要性观测者；Tidal头保留CPU驻留的补充部分，基于聚合的anchor头得分分块召回；Fixed头仅保留GPU子集，其余永久丢弃。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 内存效率 | 仅在GPU保留20%的音频token，同时可实现接近全缓存的模型准确率 |
| 泛化性 | 结果可推广至不同语言、任务和领域 |
| 时间开销 | CPU-GPU召回带来的解码时间开销小 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| LibriSpeech-Long | 评估各KV缓存优化方法的性能 |
🎯 实验设置与评估指标
任务为长语音相关的语音大模型任务；使用两个3B的backbone：Voxtral-mini-3b和Qwen2.5-Omni-3B；评估指标为模型准确率（越高越好）。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 仅预填充KV压缩方法 | 基线方法 | 永久丢弃置换后的KV位置，解码阶段无法恢复，在长音频场景中易失效 |
| Full-Cache | 对照方法 | 完整保留所有KV缓存，无内存压缩，无提前失效风险 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能**
论文未提供具体表号或定量数值，仅提及在LibriSpeech-Long数据集上，WnW保留近Full-Cache准确率，而预填充-only基线无法终止。
💡 结论：WnW可在长音频场景下实现接近全缓存的性能，解决了仅预填充压缩方法在长音频上失效的问题。
**效率对比（FPS / 参数量）**
论文未报告FPS、参数量的具体定量数据，仅说明CPU-GPU召回的解码时间开销小。
💡 结论：WnW的CPU-GPU召回机制带来的额外时间开销较低。
**跨域 / zero-shot 迁移**
论文未提供具体跨域/zero-shot迁移的定量数据，仅提及结果可推广至不同语言、任务和领域。
💡 结论：WnW的性能具有跨场景的泛化能力。
**鲁棒性 / 扰动测试**
论文未报告相关实验。
**消融实验**
论文未报告相关实验。
4. 关键结论和发现
- 主要发现：
  1. 长音频语音大模型中，预填充注意力存在集中于音频开头的注意力汇效应，解码注意力分布广泛，二者的KV重要性排名重叠性弱，导致仅预填充的KV压缩方法在长音频场景中失效。
  2. WnW通过分类KV头为anchor、tidal、fixed三类角色，平衡了内存占用与模型性能，仅在GPU上保留20%的音频token即可实现接近全缓存的精度。
  3. WnW的CPU-GPU召回机制带来的解码时间开销小，且性能可推广至不同语言、任务和领域。
- 方法局限性：论文未报告方法的局限性。
- 未来工作：论文未报告未来工作方向。

> ✅ 总结一句话：WnW是针对长语音大模型设计的KV缓存优化方法，通过分类KV头角色平衡内存占用与性能，在长音频场景下实现近全缓存的精度，且具有良好的跨场景泛化性与低额外开销。

</details>

---

### 10. [Text-Anchored Semantic Perturbations for Transferable Jailbreak Attacks on Multimodal Large Language Models](https://arxiv.org/abs/2608.22312v1)

**Authors**: Wenyun Li, Guiping Cao, Xiangyuan Lan, Zheng Zhang  
**Category**: cs.CL  
**Published**: 2026-08-25  
**Score**: 54.5  
**Type**: new  
**ArXiv ID**: 2608.22312v1  

#### Abstract
Multimodal Large Language Models (MLLMs) have achieved remarkable progress in vision-language interaction, yet their safety alignment remains vulnerable to jailbreak attacks. A key challenge is that safety behavior learned in the textual space does not reliably transfer to fused cross-modal represen...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Text-Anchored Semantic Perturbations for Transferable Jailbreak Attacks on Multimodal Large Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题
MLLMs安全对齐存在漏洞，文本空间学习的安全行为无法可靠迁移到融合后的跨模态表示，导致多模态输入可通过潜在语义线索被利用。
🚀 提出的新方法与思路
**Text-Anchored Semantic Perturbation Attack (TA-SPA)**：一种黑盒jailbreak攻击框架，核心是在文本锚定的语义空间中优化可迁移扰动，包含两个核心模块。
**Text-Anchored Semantic Factorization (TASF)**：TA-SPA的组成模块，作用是鼓励跨模态语义因子与模态特定残差分离。
**Semantic-Preserving Augmentation (SPA)**：TA-SPA的组成模块，作用是在保持语义一致性的前提下多样化有害目标锚点。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 攻击类型 | 黑盒攻击框架 |
| 攻击效果 | 具备强攻击有效性 |
| 可迁移性 | 攻击可迁移至商用MLLMs |
| 防御鲁棒性 | 在代表性防御下表现有竞争力 |
2. 核心实验方法和设置
📚 使用的数据集
论文未报告
🎯 实验设置与评估指标
任务：MLLM的可迁移jailbreak攻击；指标：论文未报告
⚔️ 基线方法对比
论文未报告
3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（场景）**
论文未报告
💡 结论：论文未报告
**表2：效率对比（场景）**
论文未报告
💡 结论：论文未报告
**表3：跨域/zero-shot迁移（场景）**
论文未报告
💡 结论：论文未报告
**表4：鲁棒性/扰动测试（场景）**
论文未报告
💡 结论：论文未报告
**表5：消融实验（场景）**
论文未报告
💡 结论：论文未报告
4. 关键结论和发现
- 主要发现：1. MLLMs的跨模态融合表征存在安全漏洞，文本空间的安全行为无法可靠迁移，可通过潜在语义线索发起jailbreak攻击；2. TA-SPA框架具备强攻击有效性和跨商用MLLMs的可迁移性，在代表性防御下表现有竞争力；3. TASF模块实现了预期的语义因子分解，但未达到完全解耦的效果。
- 方法局限性：论文未报告
- 未来工作：论文未报告
✅ **总结一句话**：本文提出TA-SPA黑盒攻击框架，通过TASF和SPA模块优化文本锚定语义空间的可迁移扰动，实现对商用MLLMs的有效可迁移jailbreak攻击，且在代表性防御下表现有竞争力，为表征层面安全对齐提供了研究动机。

</details>

---

### 11. [Mechanistic Interpretability of Chain-of-Thought Reasoning via Sequential Activation Patching](https://arxiv.org/abs/2608.22332v1)

**Authors**: Murat Dura, Serkan \"Ozt\"urk, Selma Tekir  
**Category**: cs.CL  
**Published**: 2026-08-25  
**Score**: 52.0  
**Type**: new  
**ArXiv ID**: 2608.22332v1  

#### Abstract
Large Language Models (LLMs) demonstrate remarkable problem-solving capabilities when guided by Chain-of-Thought (CoT) prompting, yet the internal mechanisms underlying these improvements remain poorly understood. In this work, we investigate where CoT-related causal effects emerge across the genera...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Mechanistic Interpretability of Chain-of-Thought Reasoning via Sequential Activation Patching
1. 论文的主要贡献和创新点
✅ 解决的问题
1. 现有研究对Chain-of-Thought（CoT）提升LLM问题解决能力的内部机制（尤其是因果效应在推理轨迹中的分布）理解不足；
2. 传统的单静态token位置激活patching方法无法表征CoT推理中跨token的时间分布效应。

🚀 提出的新方法与思路
**Sequential Activation Patching框架**：追踪CoT条件下的注意力头激活跨token位置，采用词性（Part-of-Speech）引导的分析来聚合激活效应。
**Sequential Multi-Head Patching**：用于评估分布式注意力头集的联合贡献，同时结合跨问题和随机激活控制手段验证识别结果的可靠性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 时间分布效应表征 | 可刻画CoT推理中跨token位置的时间分布因果效应，弥补传统静态单token方法的缺陷 |
| 注意力头联合贡献评估 | 支持评估分布式注意力头集在CoT推理中的联合作用，更贴合CoT的分布式特性 |
| 激活效应聚合 | 通过词性引导的分析实现跨token激活效应的有效聚合，提升分析的针对性 |
| 因果性验证 | 结合跨问题和随机激活控制，增强识别的注意力头功能重要性的验证可信度 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务：分析Chain-of-Thought推理的内部机制，识别对最终答案计算有贡献的注意力头
| 指标 | 含义 |
| --- | --- |
| 论文未报告 | 论文未报告 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：
无对应表号，实验设置为对识别出的注意力头进行零消融；结果显示该类头对成功生成答案具有功能重要性，且涉及推理轨迹维护、答案锚定、示例-目标分离、数值生成等多种重叠机制。
💡 结论：识别出的注意力头在CoT推理及最终答案生成中发挥关键作用，对应存在多种与CoT相关的核心机制。

4. 关键结论和发现
- 主要发现
  1. CoT相关的因果效应呈现分布式特征，跨越推理轨迹的多个token位置；
  2. 与CoT计算相关的注意力头参与推理轨迹维护、答案锚定、示例-目标分离、数值生成等多种关键机制；
  3. LLM中存在支持CoT推理的分布式推理子电路。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出Sequential Activation Patching框架与Sequential Multi-Head Patching方法，弥补了传统静态激活patching无法表征CoT时间分布效应的缺陷，揭示了CoT推理的分布式注意力机制及相关子电路，为LLM中CoT的机制可解释性提供了新思路。

</details>

---

### 12. [GUI-Primitives: Diagnosing Spatial Reasoning Failures in Vision-Language GUI Grounding](https://arxiv.org/abs/2608.21832v1)

**Authors**: Md Abrar Jahin, Md Rizwan Parvez  
**Category**: cs.CL  
**Published**: 2026-08-25  
**Score**: 51.5  
**Type**: new  
**ArXiv ID**: 2608.21832v1  

#### Abstract
Computer-use agents ground natural-language instructions in screenshots to locate interface elements, yet existing benchmarks do not isolate whether models bind relational language to the correct element. We introduce GUI-Primitives, a 994-item benchmark of contrastive instruction pairs over seven s...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：GUI-Primitives: Diagnosing Spatial Reasoning Failures in Vision-Language GUI Grounding

1. 论文的主要贡献和创新点
✅ 解决的问题
现有GUI grounding基准无法隔离视觉语言模型是否将关系语言绑定到正确元素，无法诊断空间推理失败；多数视觉语言模型在该任务上表现有限，多数预测偏离指定候选区域，失败根源未被明确区分。

🚀 提出的新方法与思路
**GUI-Primitives基准**：构建含7种空间关系（左/右、上/下、包含、对齐、邻近、列表序号、遮挡）的994项对比指令对，固定截图和锚点，改变关系表达式使正确目标在两个指定候选间移动；验证196项子集（5名注释者，well-formedness κ=0.94，target selection κ=0.79）；分类预测所属候选区域，区分失败源于候选定位还是关系理解；提出标记两个指定候选的oracle诊断方法以提升选择准确率。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 基准设计 | 对比指令对固定截图和锚点，精准隔离空间推理失败的根源 |
| 诊断能力 | 区分预测落在候选区域内外，明确不同空间关系的推理难度差异 |
| 性能评估 | 提供基于候选区域分类的表现分析，定位任务瓶颈 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| GUI-Primitives | 视觉语言GUI grounding任务的空间推理诊断基准，含994项对比指令对，覆盖7种空间关系 |

🎯 实验设置与评估指标
任务：视觉语言模型将自然语言指令与GUI截图中的界面元素匹配定位
| 指标 | 含义（箭头标方向） |
| ---- | ---- |
| 严格点在框准确率 | 越高越好 |
| 条件目标选择准确率 | 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 19种视觉语言模型 | 待评估模型 | 测试GUI grounding任务的空间推理表现 |
| ScreenSpot-Pro | 探索性基准方法 | 与GUI-Primitives基准准确率存在关联 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能**
论文未报告对应表号，无法提供精确定量数值；论文提及19个视觉语言模型的严格点在框准确率表现有限、部分预测偏离候选区域、不同关系下目标选择表现存在差异、与ScreenSpot-Pro准确率存在关联及标记候选可提升选择准确率，但未明确具体数值。
💡 结论：GUI-Primitives可有效诊断视觉语言模型在GUI grounding中的空间推理失败，多数失败源于候选定位而非关系理解，标记候选的oracle方法仅为诊断手段，不可部署。

效率对比：论文未报告
跨域 / zero-shot 迁移：论文未报告
鲁棒性 / 扰动测试：论文未报告
消融实验：论文未报告

4. 关键结论和发现
- 视觉语言模型在GUI grounding的空间推理任务中表现有限，失败多源于候选定位而非关系理解；
- GUI-Primitives基准中，不同空间关系的推理难度不同，部分关系（如包含、遮挡）下表现较差；
- 基准准确率与ScreenSpot-Pro准确率存在关联，标记指定候选可大幅提升目标选择准确率但为oracle诊断方法，无法实际部署。

方法局限性：仅为诊断基准，未提供可部署的空间推理解决方法；未报告效率、跨域迁移、鲁棒性等测试结果。

未来工作：开发针对难推理关系的GUI grounding方法；拓展GUI-Primitives基准以支持更多场景和关系类型。

> ✅ **总结一句话**：论文提出的GUI-Primitives基准有效诊断了视觉语言模型在GUI grounding任务中的空间推理失败，揭示多数失败源于候选定位而非关系理解，标记候选的oracle方法可提升目标选择准确率但不可部署。

</details>

---

### 13. [Beyond Success and Failure: Length-Aware Contrastive Learning for GUI Agents](https://arxiv.org/abs/2608.21830v1)

**Authors**: Chengyang Gu, Le Zhang, Jingbo Zhou, Yize Chen, Yu Shi, Siqi Bao, Zheng-Fan Wu, Hua Wu, Hui Xiong  
**Category**: cs.AI  
**Published**: 2026-08-25  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2608.21830v1  

#### Abstract
Graphical User Interface (GUI) agents powered by Multimodal Large Language Models (MLLMs) have shown strong potential for automating tasks across diverse digital environments, where reinforcement learning (RL) has become a dominant training paradigm. However, widely used methods such as Group Relati...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Beyond Success and Failure: Length-Aware Contrastive Learning for GUI Agents
1. 论文的主要贡献和创新点
✅ 解决的问题
现有GUI代理主流RL方法（如GRPO）存在奖励梯度不对齐问题，导致优化低效且不稳定；近期的RLVR相关对比方法仅依赖结果级监督，无法捕捉同结果类别内轨迹质量的细粒度差异。

🚀 提出的新方法与思路
**LACL-GUI**，即Length-Aware Contrastive Learning for GUI Agents，是一种对比RLVR框架，首次将轨迹级质量信号引入GUI代理的策略优化；它在成功与失败轨迹中均引入结构化偏好，既鼓励成功执行的简洁性，又基于与成功轨迹的差异区分失败质量，同时保留优化稳定性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 监督信号层级 | 引入轨迹级质量信号，可捕捉细粒度轨迹差异（现有方法仅采用结果级监督） |
| 优化稳定性 | 保持RLVR框架的优化稳定性，避免梯度异常 |
| 代理性能 | 提供更有效的学习信号，提升GUI代理整体性能 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告

🎯 实验设置与评估指标：论文未报告具体任务与评估指标

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Group Relative Policy Optimization (GRPO) | 主流RL训练范式 | 存在奖励梯度不对齐问题，优化低效且不稳定 |
| 现有RLVR对比方法 | 对比RLVR方法 | 仅依赖结果级监督，无法区分同结果类别内的细粒度轨迹质量差异 |
| LACL-GUI | 提出的对比RLVR框架 | 引入轨迹级质量信号与结构化轨迹偏好，兼顾优化稳定性，提升代理性能 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. 轨迹级监督信号对对比RLVR框架下的GUI代理学习具有重要价值；2. LACL-GUI提供的学习信号更有效；3. LACL-GUI相比现有方法可提升GUI代理性能。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：论文提出LACL-GUI，一种长度感知的对比RLVR框架，通过引入轨迹级质量信号优化GUI代理，解决了现有方法的梯度不对齐、细粒度轨迹质量区分不足的问题，有效提升了代理性能与学习稳定性。

</details>

---

### 14. [Beyond Factual Knowledge: Benchmarking and Learning Step-Level Procedural Rule Reasoning in Large Language Models](https://arxiv.org/abs/2608.22753v1)

**Authors**: Bohan Yu, Pengfei Cao, Chen Han, Chenxi Zhou, Zhiheng Zhang, Zhiyang Xie, Wenhao Teng, Xiangwen Liao, Jun Zhao, Kang Liu  
**Category**: cs.CL  
**Published**: 2026-08-25  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2608.22753v1  

#### Abstract
Large language models (LLMs) excel at text understanding and generation, yet still struggle to reliably understand and apply externally provided procedural rules at scale. To evaluate this capability, we introduce RuleWorld, a large-scale benchmark that reformulates rules as globally reusable abstra...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Beyond Factual Knowledge: Benchmarking and Learning Step-Level Procedural Rule Reasoning in Large Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题
- 大型语言模型（LLMs）虽具备出色的文本理解与生成能力，但在规模化可靠理解、应用外部提供的程序规则方面仍存在困难。
- 现有基准多将规则视为特定实例化事实，未将其作为全局可复用的抽象单元，无法全面评估LLMs的程序规则推理能力。
- 现有LLMs面对大规模规则池时，规则推理性能存在明显缺陷。

🚀 提出的新方法与思路
**RuleWorld基准**：构建大规模基准，将规则重新设计为全局可复用的抽象单元，覆盖单规则、并行多规则、多跳推理三类场景，用于全面评估LLMs理解和应用程序规则的能力。
**DynaRule框架**：端到端框架，核心是将给定规则注入KV缓存，把规则检索转为内部可学习的分步过程；采用带特殊token的**Stacked Step-Level Attention Training**模块，支持推理阶段的动态规则重注意力与更新，使模型每一步都能聚焦最相关规则，动态替换过时规则以提升多步推理的稳定性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 规则设计 | 将规则视为全局可复用抽象单元，而非特定实例事实，贴合实际应用场景 |
| 大规模规则池性能 | 在10K规则规模下，Recall@1超85%，平均QA准确率较现有方法提升最高19个点 |
| 多步推理稳定性 | 通过动态规则重注意力与更新机制，显著提升多步规则推理的稳定性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| RuleWorld | 用于评估大型语言模型理解和应用外部提供的、全局可复用的抽象程序规则的能力，涵盖单规则、并行多规则、多跳推理三类场景 |

🎯 实验设置与评估指标
本次任务为在RuleWorld基准上评估大型语言模型的程序规则推理性能，包括不同场景下的问答准确性与规则检索准确性。
| 指标 | 含义（箭头标方向） |
| ---- | ---- |
| 平均QA准确率 | 衡量问答任务的准确程度，越高越好 |
| Recall@1 | 衡量首个检索到相关规则的准确率，越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 现有LLM相关方法 | 基于大规模语言模型的规则应用方法 | 采用传统规则嵌入方式，面对大规模规则池时规则推理效果差 |
| 强基线（论文未具体列出名称） | 规则推理相关强基线方法 | 常规规则处理逻辑，性能弱于DynaRule |

3. 主要实验结果和性能指标
📊 定量结果汇总
由于论文未提供具体实验表号，仅依据论文提及内容整理如下：
**主benchmark性能**
| 方法 | 平均QA准确率 | Recall@1（10K规则） |
| ---- | ---- | ---- |
| 现有LLM相关方法 | 较低 | 较低 |
| 强基线（论文未列出） | 中等 | 中等 |
| DynaRule | 提升最高19个点✅ | 超85%✅ |
💡 结论：DynaRule在RuleWorld基准上，较现有方法在平均QA准确率和10K规则下的Recall@1上有显著提升，解决了现有模型在大规模规则池下的推理缺陷。

效率对比（FPS/参数量）：论文未报告。
跨域/zero-shot迁移：论文未报告。
鲁棒性/扰动测试：论文未报告。
消融实验：论文未报告。

4. 关键结论和发现
- 主要发现：1. 大型语言模型在规模化处理外部提供的程序规则时存在明显挑战，尤其是面对大规模规则池的场景；2. RuleWorld基准能有效评估LLMs将规则作为全局可复用抽象单元的程序规则推理能力；3. DynaRule的动态规则重注意力与更新机制可显著提升多步规则推理的稳定性和性能。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：该论文提出RuleWorld基准和DynaRule框架，有效解决了现有大型语言模型在规模化理解应用程序规则能力上的不足，大幅提升了规则推理的性能。

</details>

---

### 15. [Small Reasoning Models are Instruction Followers in Function Calling](https://arxiv.org/abs/2608.22472v1)

**Authors**: Yalda Taheri, Mohammad Hassan Heydari, Erfan Naaman, Afsaneh Fatemi  
**Category**: cs.AI  
**Published**: 2026-08-25  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2608.22472v1  

#### Abstract
Function calling represents the core capability of agentic large language models (LLMs). Existing research has focused on enhancing LLMs function-calling accuracy through fine-tuning, reinforcement learning (RL), and multi-agent frameworks, particularly for native function-calling LLMs. This work de...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Small Reasoning Models are Instruction Followers in Function Calling
1. 论文的主要贡献和创新点
解决的问题：现有提升LLM功能调用准确性的方法（微调、强化学习、多智能体框架等）多聚焦于原生功能调用LLM；LLM在功能调用语境下的表现弱于指令跟随语境下的表现，原生功能调用（NFC）和基于提示的功能调用（PFC）基线存在性能不足。
🚀 提出的新方法与思路
**Instruction-Followed Function Calling（IFFC）**，核心思路为将功能调用逻辑从主LLM中解耦，委托至一个在指令跟随范式下运行的专用小型模型。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 功能调用准确性 | 始终优于原生功能调用（NFC）和基于提示的功能调用（PFC）基线，对推理导向LLM增益尤为显著 |
| 量化鲁棒性 | 在激进量化下维持性能稳定，无显著准确性下降 |
| 部署效率 | 支持边缘计算场景的高效部署 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务为提升可靠且资源高效的功能调用，具体指标论文未报告。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Native Function Calling (NFC) | 基线方法 | 基于原生功能调用LLM |
| Prompt-based Function Calling (PFC) | 基线方法 | 基于提示的功能调用方法 |

3. 主要实验结果和性能指标
论文未报告具体表号、图号及定量结果，所有实验结果相关内容均为“论文未报告”。

4. 关键结论和发现
- 主要发现：
  1. LLM在指令跟随语境（标准用户-助手交互）下的功能调用表现优于专用工具调用语境；
  2. IFFC框架的功能调用性能始终优于NFC和PFC基线，对推理导向LLM增益尤为显著；
  3. IFFC在激进量化下维持性能稳定，无显著准确性下降，可支持边缘计算场景的高效部署。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出将功能调用逻辑解耦至小型指令跟随模型的IFFC框架，实现了更优的功能调用准确性与量化鲁棒性，为边缘计算场景提供了可靠高效的功能调用方案。

</details>

---

### 16. [Evaluating Multimodal Narrative Understanding of Popular Hollywood Films](https://arxiv.org/abs/2608.21430v1)

**Authors**: David Bamman, Kent K. Chang, Allison Cooper, Juishan Hsu, Reina Kushihashi, Madison Mar, Arnav Podichetty, Rachael Samberg, Ipek Nil Sancak, Yuhan Shao  
**Category**: cs.AI  
**Published**: 2026-08-25  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2608.21430v1  

#### Abstract
Multimodal language models increasingly show promise for enabling the large-scale computational analysis of film, opening up new avenues for learning about film history and the evolution of narrative techniques. But the creation of stable benchmarks built around Hollywood films is complicated by cop...

---

### 17. [Evaluation of Small Vision-Language Models on Qualitative Mechanical Problems](https://arxiv.org/abs/2608.22143v1)

**Authors**: Henry Fordjour Ansah (Louisiana State University of New Orleans), Shreya Banerjee (Louisiana State University of New Orleans), Pranish Ghimire (Louisiana State University of New Orleans)  
**Category**: cs.AI  
**Published**: 2026-08-25  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2608.22143v1  

#### Abstract
Qualitative mechanical problem-solving (QMPS) refers to solving qualitative problems from the mechanical domain. Qualitative problems can be solved with minimal discipline-specific information, without any robust quantitative calculation, generally by using qualitative reasoning and commonsense know...

---

### 18. [Beyond What Meets the Eye: Unveiling Situational Illusions for Multimodal Large Language Models](https://arxiv.org/abs/2608.22232v1)

**Authors**: Zhiming Yang, Zhuoxi Xiong, Donglin Zhou, Wenjun Wei, Shiyao Cui, Jinqiao Shi  
**Category**: cs.AI  
**Published**: 2026-08-25  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2608.22232v1  

#### Abstract
Real-world situation appearances can deviate from their underlying physical states, challenging the reliability of multimodal large language models (MLLMs) in practical applications. In this paper, we term this phenomenon situational illusions and investigate: (1) how MLLMs perform under such illusi...

---

### 19. [Is Next-Chunk Reasoning RL Really Better than SFT? Revisiting Training Strategies under no-CoT Data](https://arxiv.org/abs/2608.23256v1)

**Authors**: Yinhao Tang, Youqing Fang, Yanan Sun, Jiangning Liu, Ziyi Wang, Xun Zhao, Weiming Zhang, Bin Liu, Kuikun Liu, Wenwei Zhang, Kai Chen  
**Category**: cs.AI  
**Published**: 2026-08-25  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2608.23256v1  

#### Abstract
Recent work proposes next-chunk reasoning RL for leveraging no-CoT data---corpora such as worked solutions and textbook derivations that contain reasoning-rich content but lack explicit chain-of-thought annotations. The method trains a model to generate implicit reasoning traces and rewards them by ...

---

### 20. [The Chase Is the Curriculum, the Capture Anchors the Credit: Pursuit-Evasion Self-Play for Zero-Data LLM Reasoning](https://arxiv.org/abs/2608.21871v1)

**Authors**: Jing Yu, Shengchao Chen, Yiyun Tan  
**Category**: cs.CL  
**Published**: 2026-08-25  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2608.21871v1  

#### Abstract
Reinforcement learning with verifiable rewards has become the dominant recipe for improving large language model reasoning, yet it presumes large human-curated task collections. Zero-data self-play removes this dependency, but existing methods vet learnability only by probing candidates and rejectin...

---

### 21. [Knowing Isn't Always Saying: When Do Spatial Encodings Reach Answers in Vision-Language Models?](https://arxiv.org/abs/2608.22916v1)

**Authors**: Zeyu Wang, Xinming Xu  
**Category**: cs.CL  
**Published**: 2026-08-25  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2608.22916v1  

#### Abstract
Vision-language models are known to encode spatial information in their hidden states, yet often fail to use it when answering. However, it remains unclear when and where this encoded information reaches the answer. We address this with direction patching, a class-conditioned causal intervention app...

---

### 22. [L\\"etzCross: A Cross-Lingual Page-Level Benchmark for Multimodal Retrieval over Luxembourgish Documents](https://arxiv.org/abs/2608.21714v1)

**Authors**: Omar El Bachyr, Fred Philippy, Laura Maria Bernardy, Saad Ezzini, Jacques Klein, Tegawende Bissyande  
**Category**: cs.CL  
**Published**: 2026-08-25  
**Score**: 41.5  
**Type**: new  
**ArXiv ID**: 2608.21714v1  

#### Abstract
Recent page-image retrievers such as ColPali have improved retrieval over visually rich documents, yet little is known about how they behave in cross-lingual, low-resource settings. We introduce L\"etzCross, a benchmark for cross-lingual page-level retrieval over Luxembourgish PDF documents, with do...

---

### 23. [Weakly supervised concept Bottleneck Learning for Robust Two stage Object centric visual reasoning](https://arxiv.org/abs/2608.22584v1)

**Authors**: Sparsh Tiwari, Gesina Schwalbe, Bettina Finzel  
**Category**: cs.AI  
**Published**: 2026-08-25  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2608.22584v1  

#### Abstract
Two-stage neuro-symbolic architectures provide an elegant paradigm for visual problem solving by cleanly separating connectionist perception of predefined symbols from possibly later defined relational reasoning thereon. However, anchoring high-level predicates into visual frames typically necessita...

---

### 24. [From Thermal Preference Prediction to Adaptive Thermal Intervention: A Reinforcement Learning Approach Using Physiological and Environmental Sensing](https://arxiv.org/abs/2608.20423v1)

**Authors**: Isibor Kennedy Ihianle, Emmanuel Manu, Ehsan Asnaashari, Mojgan Jadidi, Pedro Machado, Amrit Sagoo, Ahmad Lotfi  
**Category**: cs.LG  
**Published**: 2026-08-25  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2608.20423v1  

#### Abstract
Personalised thermal comfort is essential for occupant wellbeing and for the development of more responsive building-control strategies, yet conventional Heating, Ventilation, and Air Conditioning (HVAC) systems rely on static setpoints and population-level comfort models that fail to capture indivi...

---

### 25. [Hidden Axis of Uncertainty: Latent-Posterior Alignment in Graph Neural Networks with Bayesian Output Layers](https://arxiv.org/abs/2608.20758v1)

**Authors**: Suk Hoon Choi, Damdae Park, Junhyuk Choi, Hyein Jung, Changsoo Kim, Ung Lee, Kyeongsu Kim  
**Category**: cs.LG  
**Published**: 2026-08-25  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2608.20758v1  

#### Abstract
Bayesian Neural Networks (BNNs) with Bayesian output layers provide a principled and tractable framework for quantifying predictive uncertainty, yet the mechanisms shaping that uncertainty remain unclear. While conventional theory attributes uncertainty reduction to posterior contraction, the corres...

---

### 26. [KVBoost: Chunk-Level Key-Value Cache Reuse with Deviation-Guided Recomputation for Efficient Large Language Model Inference](https://arxiv.org/abs/2608.21362v1)

**Authors**: Srihari Unnikrishnan  
**Category**: cs.AI  
**Published**: 2026-08-25  
**Score**: 38.0  
**Type**: new  
**ArXiv ID**: 2608.21362v1  

#### Abstract
Transformer-based large language models (LLMs) incur high prefill latency because key-value (KV) tensors must be recomputed for each request. Existing prefix-caching systems reduce this cost but require prompts to share a leading contiguous prefix, limiting effectiveness when shared content appears ...

---

### 27. [NeuroPrefetcher: Storage-Aware Sparse LLM Inference via Delta Prefetching](https://arxiv.org/abs/2608.22643v1)

**Authors**: Nobel Dhar, Md Romyull Islam, Xuechen Zhang, Gongjin Sun, Sahidul Islam, Bobin Deng, Kun Suo  
**Category**: cs.DC  
**Published**: 2026-08-25  
**Score**: 37.5  
**Type**: new  
**ArXiv ID**: 2608.22643v1  

#### Abstract
Deploying large language models on edge devices is increasingly limited by a widening gap between model size and available memory. Existing approaches such as quantization, smaller models, and offloading can raise the effective memory limit, but they still assume that the model can be compressed or ...

---

### 28. [Precision-Aware Variable Bit Processing Elements for Hardware-Efficient Systolic Array Designs](https://arxiv.org/abs/2608.22378v1)

**Authors**: Dantu Nandini Devi, Madhav Rao  
**Category**: cs.AR  
**Published**: 2026-08-25  
**Score**: 36.5  
**Type**: new  
**ArXiv ID**: 2608.22378v1  

#### Abstract
Systolic arrays (SAs) have emerged as prominent hardware accelerators for matrix operations in deep learning, while floating point number formats enable precision control across computational domains. This research investigates approximate computing techniques for floating point (FP) multipliers in ...

---

### 29. [TailSieve: Partial-Rollout-Guided Tail Routing for LLM Rollouts](https://arxiv.org/abs/2608.22788v1)

**Authors**: Tianqi Xu, Lu Lv, Haoyang Huang, Wenjie Huang, Zhanming Shen, Yuhao Shen, Baolin Zhang, Xinyi Hu, Shuang Ge, Jun Dai, Tianyu Liu, Suorong Yang, Zhikai Li, Ye Bai, Jun Zhang, Lei Chen, Yue Li, Mingchen Wan  
**Category**: cs.AI  
**Published**: 2026-08-25  
**Score**: 35.5  
**Type**: new  
**ArXiv ID**: 2608.22788v1  

#### Abstract
Large-scale rollouts have become a core component of modern LLM systems, spanning reinforcement learning (RL) post-training, on-policy distillation (OPD), and sampling-heavy evaluation pipelines. Unlike online serving, which is typically optimized for request-level latency and throughput, a small nu...

---

### 30. [Bern2Edge: A Neurosymbolic Compiler for Edge Deployment via Bernstein Polynomial Networks](https://arxiv.org/abs/2608.20497v1)

**Authors**: Malak Gamal El-Din, Yifan Zhang, Yasser Shoukry, Sitao Huang, Salma Elmalaki  
**Category**: cs.LG  
**Published**: 2026-08-25  
**Score**: 35.5  
**Type**: new  
**ArXiv ID**: 2608.20497v1  

#### Abstract
Deploying high-accuracy neural networks on resource-constrained edge devices remains challenging, as existing approaches treat training, compression, and hardware synthesis as separate stages, leaving a gap between software-trained models and efficient end-to-end deployment with limited support for ...

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
