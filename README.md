# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-08-21 06:25:39 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving](https://arxiv.org/abs/2608.19758v1)

**Authors**: Qihang Fan, Huaibo Huang, Zhiying Wu, Bingning Wang, Ran He  
**Category**: cs.CL  
**Published**: 2026-08-21  
**Score**: 123.5  
**Type**: new  
**ArXiv ID**: 2608.19758v1  

#### Abstract
Long-context modeling is a pivotal capability for Large Language Models, yet the quadratic complexity of attention remains a critical bottleneck, particularly during the compute-intensive prefilling phase. Our previous work, FlashPrefill, mitigates this cost through instantaneous pattern discovery a...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving
1. 论文的主要贡献和创新点
✅ 解决的问题
长上下文LLM的prefilling阶段注意力存在二次复杂度瓶颈，早期FlashPrefill仅为算法原型，距离生产部署存在差距。

🚀 提出的新方法与思路
**Mean Correction Term**：引入均值校正项，有效抑制近似误差，即使在极高稀疏度下也能将性能退化控制在可接受范围。
**Redesigned Sparse Attention Operator**：重新设计稀疏注意力算子，结合PackGQA内存访问、warp specialization、pingpong pipelining，完全适配最新的FlashAttention-3/4实现，支持FP8推理以满足实际量化需求。
**Native Paged KV Cache & Continuous Batching Support**：原生支持分页KV缓存与连续批处理，可作为注意力后端集成至SGLang等现代推理框架。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
生产部署适配性 | 支持分页KV缓存、连续批处理，适配FlashAttention-3/4实现，支持FP8量化，可集成至SGLang等现代推理框架
长上下文prefill近似鲁棒性 | 引入均值校正项抑制近似误差，控制极端稀疏度下的性能退化

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
任务为长上下文LLM推理prefill阶段的性能评估，评估指标为加速比（↑越高越好）。
指标 | 含义
--- | ---
加速比 | 相比基线方法的性能提升倍数（↑越高越好）

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
FlashAttention-2 | 现有prefill注意力实现 | 传统长上下文LLM prefill注意力实现
FA3/4对齐的稠密基线 | FlashAttention-3/4适配的稠密方法 | 遵循FlashAttention-3/4标准的稠密注意力基线

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告

4. 关键结论和发现
- FlashPrefill V2解决了早期FlashPrefill原型距离生产部署的问题，同时维持了高效的长上下文prefill性能。
- 引入的均值校正项可有效抑制稀疏注意力的近似误差，优化后的算子适配FlashAttention-3/4并支持FP8量化，满足实用部署需求。
- FlashPrefill V2原生支持分页KV缓存与连续批处理，可集成至现代推理框架，具备实际应用价值。
方法局限性
论文未报告
未来工作
论文未报告

> ✅ **总结一句话**：FlashPrefill V2是一款适配生产部署的长上下文LLM prefill注意力方法，通过均值校正抑制近似误差、优化算子并支持现代推理框架，具备实用的性能提升潜力。

</details>

---

### 2. [DARS: Dual-Level Credit Assignment RL with Structured Reasoning for Instruction-Based Image Editing](https://arxiv.org/abs/2608.20161v1)

**Authors**: Haoxiang Cao, Jiajiong Cao, Xuanpu Zhang, Changqian Yu, Chaoqun Wang  
**Category**: cs.AI  
**Published**: 2026-08-21  
**Score**: 66.0  
**Type**: new  
**ArXiv ID**: 2608.20161v1  

#### Abstract
Instruction-based image editing uses a planner-renderer pipeline: a vision-language model (VLM) first converts the instruction into an edit plan, and a diffusion model then executes that plan. Training such systems with only final-image rewards is inefficient because a poor edit does not reveal whet...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

DARS: Dual-Level Credit Assignment RL with Structured Reasoning for Instruction-Based Image Editing
1. 论文的主要贡献和创新点
✅ 解决的问题
指令式图像编辑采用规划器-渲染器的流水线结构，仅依靠最终图像奖励训练的效率较低；其缺陷包括：1）差的编辑结果无法明确是规划器还是渲染器导致的；2）规划主导的编辑场景难以在自由形式的推理轨迹中定位。
🚀 提出的新方法与思路
**双级信用分配RL框架**：针对规划器-渲染器两阶段任务，通过多计划多渲染rollouts估计计划间与计划内的奖励变异性以实现软模块路由，同时利用rollout平均奖励生成难度估计，用于自适应课程学习。
**规划器结构化推理机制**：规划器输出包含四个字段的结构化推理结果，支持前缀门控奖励计算与token级优势重加权，将结果级全局反馈转化为局部监督信号。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 基准性能 | 在五个基准上优于使用相同骨干网络、数据、奖励模型及rollout预算的Joint RL基线 |
| 场景适配性 | 在推理密集型编辑场景中，增益最为显著 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 五个基准 | 用于指令式图像编辑任务的性能评估 |
🎯 实验设置与评估指标
该任务为指令式图像编辑，采用规划器-渲染器的强化学习流水线；论文未报告具体评估指标名称。
| 指标 | 含义 |
| --- | --- |
| 论文未报告 | 论文未报告具体指标，仅说明整体性能对比结果 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Joint RL基线 | 强化学习基线 | 与DARS使用相同骨干网络、数据、奖励模型及rollout预算 |
3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体表号及对应定量数值，仅指出DARS在五个基准上的性能优于相同设置的Joint RL基线，在推理密集型编辑场景中增益最大。
4. 关键结论和发现
- 主要发现：
  1. 所提出的DARS框架能有效提升指令式图像编辑的性能，优于相同设置的Joint RL基线；
  2. DARS在推理密集型的指令式图像编辑任务上，相比基线的增益更为显著。
- 方法局限性：论文未报告
- 未来工作：论文未报告
✅ **总结一句话**：DARS是针对规划器-渲染器两阶段指令式图像编辑任务设计的双级信用分配强化学习框架，通过多计划多渲染rollouts实现软模块路由与自适应课程学习，结合规划器的结构化推理机制将结果反馈转为局部监督，在五个基准上优于相同设置的Joint RL基线，推理密集型编辑场景增益最大。

</details>

---

### 3. [Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation](https://arxiv.org/abs/2608.20256v1)

**Authors**: Gijs Kassenaar, Zhao Yang, Vincent Fran\c{c}ois-Lavet  
**Category**: cs.AI  
**Published**: 2026-08-21  
**Score**: 62.0  
**Type**: new  
**ArXiv ID**: 2608.20256v1  

#### Abstract
Reasoning language models trained with reinforcement learning typically operate under a fixed token budget rather than an explicitly adaptive one, which can lead to over-computation on easy problems and insufficient computation on difficult ones. We study whether a model can learn to allocate its ow...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation
1. 论文的主要贡献和创新点
✅ 解决的问题
强化学习训练的推理语言模型通常采用固定token预算，缺乏自适应计算分配能力，导致简单问题出现过度计算、复杂问题计算不足的核心矛盾。

🚀 提出的新方法与思路
**自适应推理模式选择框架**，核心是让模型在响应的第一个token时选择三种预定义推理模式（NoThink：快速回答、Short：简要推理、Long：扩展推理）；该模式选择过程通过Group Relative Policy Optimization (GRPO)学习，无单独路由器模块；采用塑形奖励机制使各模式在不同响应长度下具备价值，同时设置模式专属硬token上限以保持三类模式的区分度。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 计算分配 | 自适应分配推理资源，避免固定预算导致的过度计算或计算不足问题 |
| 性能与效率 | 在基准数据集上保持接近基准模型的准确率，同时大幅减少平均响应长度 |
| 迁移能力 | 无需再训练即可迁移到其他基准任务，对简单问题的token节省幅度更大 |
| 路由器逻辑 | 路由器按问题难度排序，选择对应推理模式而非随机选择，Brief等简要模式准确率优于Long模式 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| MATH | 训练所提自适应推理模型 |
| MATH500 | 训练后模型的held-out测试集 |
| GSM8K | 自适应方法的跨基准迁移测试集 |

🎯 实验设置与评估指标
任务为推理语言模型的自适应计算分配能力评估；指标：准确率（↑越高越好）、平均响应长度（↓越低越好）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Base Model | 固定token预算的推理模型 | 采用固定token数量的响应预算，无自适应调整能力 |
| Proposed Adaptive Method | 自适应模式选择的推理模型 | 可根据问题难度选择三类推理模式调整响应长度 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主基准性能（MATH500）**
论文未提供对应表号，仅报告所提方法在held-out MATH500上的准确率接近基准模型。
💡 结论：所提自适应推理方法在核心测试集上的推理准确率与固定预算基准模型接近。

**效率对比**
论文未提供对应表号，仅报告所提方法的平均响应长度较基准模型显著降低。
💡 结论：自适应模式选择可大幅减少推理过程的token用量，提升计算效率。

**跨域/zero-shot迁移**
论文未提供对应表号，仅报告所提方法无需再训练即可迁移到其他基准任务（如GSM8K），且对简单问题的token节省幅度更大。
💡 结论：所提自适应方法具备良好的跨任务泛化能力。

鲁棒性/扰动测试：论文未报告
消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. 模型可通过GRPO学习有效选择三类推理模式，不会崩溃至单一选择，且路由器按问题难度排序而非随机选择；2. 自适应方法在保持接近基准准确率的同时大幅降低平均响应长度；3. 无需再训练即可将自适应能力迁移至其他基准任务，简单问题的token节省效果更显著。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出基于GRPO训练的自适应推理框架，可让推理语言模型按需选择三种推理模式，在保持推理准确率的同时显著减少响应token用量，且具备无需再训练即可跨基准迁移的能力。

</details>

---

### 4. [Design and Empirical Evaluation of a Network-Centric, On-Premises Architecture for Earth Observation Data Access](https://arxiv.org/abs/2608.20283v1)

**Authors**: Jo\~ao Pinelo, Jo\~ao Gon\c{c}alves, Denis Willett, Amit Ruhela, Derek Steinmoeller, Uriel Mendoza, Pelumi S. Alao, Ronald Soares Lopes, Rogerio Atem de Carvalho, Pedro Mattos  
**Category**: cs.DC  
**Published**: 2026-08-21  
**Score**: 55.0  
**Type**: new  
**ArXiv ID**: 2608.20283v1  

#### Abstract
Earth observation (EO) programmes generate data at volumes that exceed the transfer and storage capacity of most institutional networks. Public cloud platforms address this for well-resourced organisations, but institutions across the Atlantic basin face constraints in connectivity, sovereignty and ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Design and Empirical Evaluation of a Network-Centric, On-Premises Architecture for Earth Observation Data Access
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：地球观测（EO）项目的数据传输、存储容量超出多数机构网络的处理能力；公共云虽适配资源充足组织，但大西洋盆地机构受连接性、主权、资金约束，仅能选择本地部署（on-premises）路径。
现有方法缺陷：公共云无法适配大西洋盆地受约束机构；云原生数据格式的高效部分读取性能依赖底层网络带宽，但该依赖从未被单独测量；传统本地架构未以网络为核心设计。

🚀 提出的新方法与思路
**网络中心型本地部署架构**，以AIR数据中心（大西洋云的核心节点）为首个部署实例，构建由100 GbE fabric的MinIO对象存储集群、PostGIS元数据目录、OGC API-EDR访问层组成的系统；完成三类评估：1）持续并行负载下的fabric特征化；2）EO代表性工作负载的对象存储吞吐量；3）相同硬件上限流基线（隔离网络带宽为唯一变量）的对比、合作机构的多站点复制基准（表征架构依赖的联邦基元）。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 变量隔离评估 | 首次隔离网络带宽作为唯一变量，量化其对云原生EO数据格式吞吐量的影响 |
| 场景适配 | 专为大西洋盆地受连接、主权、资金限制的机构设计，提供可行的本地EO数据访问方案 |
| 联邦性能支撑 | 覆盖架构依赖的联邦基元（多站点复制）的基准测试，为跨机构EO数据共享提供依据 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| EO-representative workloads | 用于评估MinIO对象存储集群的吞吐量性能 |
（注：论文未报告具体数据集名称）

🎯 实验设置与评估指标
实验任务：评估网络带宽对本地部署架构下EO bulk数据访问的存储吞吐量的影响，以及架构的多站点复制性能；评估指标包括存储吞吐量、网络带宽、端点内存拓扑相关的带宽利用率、多站点复制性能。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 限流基线（throttled baselines） | 对比基线 | 与目标架构使用相同硬件，隔离网络带宽为唯一变量，用于验证网络带宽的影响 |

3. 主要实验结果和性能指标
📊 定量结果汇总
（仅论文明确报告的结果，其余实验均为论文未报告）
**表1：网络带宽与存储吞吐量的关系（bulk EO数据访问场景）**
| 定量发现内容 | 数值 | 来源 |
| --- | --- | --- |
| 网络带宽主导存储吞吐量的阈值 | 高于10 Gbps/服务器 | 论文摘要 |
| 超过阈值后的带宽约束因素 | 端点内存拓扑（而非容量） | 论文摘要 |
| 低于阈值时的存储吞吐量约束 | 仅网络容量 | 论文摘要 |
| 高于阈值时的网络投资特点 | 回报取决于端点内存配置，可延迟购置 | 论文摘要 |
💡 结论：针对该硬件类，bulk EO数据访问的存储吞吐量在网络带宽低于10 Gbps/服务器时由网络容量主导，超过后受端点内存拓扑约束。

其余实验（主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）：论文未报告

4. 关键结论和发现
- 主要发现：1. 针对大西洋盆地受约束机构的EO数据访问需求，网络中心型本地部署架构可行；2. bulk EO数据访问存在网络带宽阈值（该硬件类下高于10 Gbps/服务器），阈值以上需重点关注端点内存拓扑的约束；3. 架构的联邦基元（多站点复制）性能可通过基准测试有效表征。
- 方法局限性：论文未报告多站点复制的具体性能数值，未覆盖非bulk类型的EO数据访问场景，未开展鲁棒性、跨域迁移或消融实验评估。
- 未来工作：进一步完善多站点复制的性能评估，拓展架构适配更多类型的EO数据访问场景，探索不同硬件配置下的网络-内存配置阈值。

> ✅ **总结一句话**：该论文提出适配大西洋盆地受连接、主权、资金限制机构的网络中心型本地EO数据访问架构，通过隔离网络带宽变量的实验，明确了bulk EO数据访问中网络与内存配置的阈值，为本地EO数据访问的硬件部署提供了依据。

</details>

---

### 5. [Answer-Level Trust Selection for Physical Vision-Language Reasoning](https://arxiv.org/abs/2608.19807v1)

**Authors**: Rongyu Yu, Ke Niu, Fengxiang He  
**Category**: cs.LG  
**Published**: 2026-08-21  
**Score**: 53.5  
**Type**: new  
**ArXiv ID**: 2608.19807v1  

#### Abstract
Vision-language models (VLMs) can estimate physical quantities such as duration, speed, and acceleration from visual observations, but existing benchmarks primarily assess overall model performance against annotated ground truth. In deployment, a key question is whether an individual prediction can ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Answer-Level Trust Selection for Physical Vision-Language Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
Vision-language models（VLMs）可从视觉观测估计时长、速度、加速度等物理量，但现有基准仅评估模型整体对标注真值的性能；部署时面临关键问题——未知真值时无法判断单个预测是否可信，且自一致性单独无法捕获重要失败模式，VLM可能生成稳定但错误的估计或依赖文本先验而非视觉证据。

🚀 提出的新方法与思路
**Answer-Level Trust Selection (ATS)**：这是一个post-hoc、模型无关的框架，用于接受或拒绝单个VLM的预测；该框架无需微调、辅助验证器或访问模型的内部logits，而是聚合从重复查询和受控干预中导出的8个可解释行为诊断分数，生成统一的信任分数。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 模型兼容性 | 模型无关，可适配任意VLM |
| 部署要求 | 无需微调、辅助验证器或访问模型内部logits，部署成本低 |
| 失败模式识别能力 | 可识别仅靠重复一致性会遗漏的稳定但错误的预测、依赖文本先验而非视觉证据的预测 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告

🎯 实验设置与评估指标
任务为定量物理推理的答案选择性预测，即对单个VLM预测判断是否可信；论文未报告具体指标名称及含义。

⚔️ 基线方法对比：论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
**表N：名称（场景）**
论文未报告
💡 结论：论文未报告
其余实验（主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）：论文未报告

4. 关键结论和发现
- 主要发现：
  1. 干预式诊断有助于识别重复一致性单独可能遗漏的稳定但错误的预测、依赖文本先验而非视觉证据的预测；
  2. 更多失败案例的拒绝可能以降低正确预测的保留率为代价；
  3. ATS补充了VLM的模型级能力评估与答案级可靠性评估，可用于定量VLM预测。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出了post-hoc、模型无关的Answer-Level Trust Selection框架，通过聚合8个可解释诊断分数实现定量物理推理中单个VLM预测的可信度评估，可识别重复一致但错误、依赖文本先验的预测，但存在拒绝失败案例可能降低正确预测保留率的 trade-off，补充了VLM的模型级与答案级评估。

</details>

---

### 6. [Learning how to Forget: Fine-tuning for Long-Context Sparse Attention](https://arxiv.org/abs/2608.19920v1)

**Authors**: Matthias Seeger, Zeyu Zhang, Vihang Patil, Konstantinos Benidis, Sebastian Schelter  
**Category**: cs.CL  
**Published**: 2026-08-21  
**Score**: 49.0  
**Type**: new  
**ArXiv ID**: 2608.19920v1  

#### Abstract
A lot of prior work addressed key-value (KV) cache selection and compression by sparse attention to enable long-context inference for transformer language models without excessive hardware budgets. We provide a new method for fine-tuning models with sparse attention. It works for any KV cache policy...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Learning how to Forget: Fine-tuning for Long-Context Sparse Attention
1. 论文的主要贡献和创新点
✅ 解决的问题
现有工作通过稀疏注意力实现Transformer语言模型的长上下文推理，核心痛点为未兼顾模型与稀疏注意力策略的共同适配，或硬件预算要求较高，且缺乏易用高效的实现工具。
🚀 提出的新方法与思路
**Long-Context Sparse Attention Fine-tuning Method**：提出的微调方法适用于任意KV缓存策略，仅需中等硬件预算（如单Nvidia A100 GPU，40 GB RAM）即可运行，可实现模型与稀疏策略的共同适配；同时提供H2O稀疏注意力的高效实现（含专用缩放点积注意力内核支持），并开源KeysAndValues库，提供所有涉及方法的易用高性能代码。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 方法普适性 | 适用于任意KV缓存策略 |
| 硬件门槛 | 中等预算硬件即可运行 |
| 性能表现 | 常优于基于sequence parallelism训练的精确注意力模型 |
| 实现便捷性 | 提供H2O稀疏注意力的高效内核支持，开源KeysAndValues库提供易用高性能代码 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告
🎯 实验设置与评估指标
论文未报告
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Exact attention (sequence parallelism) | 基线方法 | 采用精确注意力，需序列并行，为现有对比基准 |
| H2O sparse attention | 稀疏注意力策略 | 实验中领先策略，本研究对其提供高效实现 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告

4. 关键结论和发现
- 主要发现：提出的长上下文稀疏注意力微调方法可实现模型与稀疏策略的共同适配，性能常优于基于sequence parallelism训练的精确注意力模型，硬件要求适中。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出一种适用于任意KV缓存策略的长上下文稀疏注意力微调方法，仅需中等硬件即可运行，能实现模型与稀疏策略的共同适配，性能常优于基于sequence parallelism的精确注意力模型，并提供稀疏注意力高效实现及开源工具库KeysAndValues。

</details>

---

### 7. [Write Once, Run Everywhere: The Axon DSL for Shape-Safe and Framework-Agnostic LLM Architectures](https://arxiv.org/abs/2608.19889v1)

**Authors**: Jacob Nielsen, Danial Namazifard, Lukas Galke Poech, Peter Schneider-Kamp  
**Category**: cs.AI  
**Published**: 2026-08-21  
**Score**: 48.5  
**Type**: new  
**ArXiv ID**: 2608.19889v1  

#### Abstract
The entire ecosystem of open-source language models effectively relies on a single platform. What if this platform was forced to shut down tomorrow? Implementing and maintaining efficient model definitions and translating them between different training and inference regimes is a resource-heavy task...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Write Once, Run Everywhere: The Axon DSL for Shape-Safe and Framework-Agnostic LLM Architectures
1. 论文的主要贡献和创新点
✅ 解决的问题
现有开源LLM生态依赖单一平台，若该平台关闭将引发风险；实现、维护高效模型定义及跨训练推理范式转换的任务资源消耗大，严重限制模型效率和可移植性，阻碍模型扩展与部署。

🚀 提出的新方法与思路
**Axon DSL**：设计一种类Haskell语法的强类型领域特定语言，用于实现LLM架构的“一次编写、多处运行”范式；其基于语言规范而非特定框架的愿景，促进开放合作，允许研究者实现专业化架构的同时不放弃优化基础设施或接受部署锁定；支持生成简洁可审计的规范，可自动编译为PyTorch、带Triton的PyTorch、JAX、MLX、vLLM等主流框架的独立实现。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 平台依赖 | 基于语言规范而非单一平台，避免平台锁定风险 |
| 模型开发成本 | 降低模型定义及跨框架转换的资源消耗 |
| 框架兼容性 | 支持自动生成PyTorch、带Triton的PyTorch、JAX、MLX、vLLM多框架的实现 |
| 部署灵活性 | 提供无部署锁定的部署选项 |
| 可审计性 | 生成简洁可审计的模型规范 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
任务：LLM推理性能对比
| 指标 | 含义 |
| ---- | ---- |
| 中位数加速比 | Axon实现与Transformers参考实现的性能对比（越高越好 ↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Transformers参考实现 | LLM推理基线 | 各主流框架提供的LLM参考实现，用于性能对比基准 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告

4. 关键结论和发现
- 主要发现：1. Axon DSL实现了LLM架构的框架无关性，避免了部署锁定问题；2. 基于Axon生成的模型在多个主流框架上的推理性能相比Transformers参考实现有显著提升；3. 将Axon模型部署为原生vLLM架构（含PagedAttention和KV-cache）时性能优势进一步放大。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：Axon是一种强类型领域特定语言，实现了LLM架构的一次编写、跨框架运行，可自动生成多主流框架的独立实现并显著提升推理性能，解决了现有LLM生态依赖单一平台的风险。

</details>

---

### 8. [A Thread-Register Decoupled GPU Execution Model for Efficient Tensor Computation](https://arxiv.org/abs/2608.19628v1)

**Authors**: Zihan Liu, Jingwen Leng, Yangjie Zhou, Yitong Ding, Guanlin Zhu, Yilu Huang, Chiheng Jin, Chen Zhang, Shixuan Sun, Yu Feng, Anbang Wu, Minyi Guo, Jian Weng, Jiajin Tu, Junsong Wang  
**Category**: cs.AR  
**Published**: 2026-08-21  
**Score**: 47.5  
**Type**: new  
**ArXiv ID**: 2608.19628v1  

#### Abstract
Modern GPUs increasingly integrate Tensor Cores into the execution pipeline. Although aggregate tensor throughput continues to grow, aided by an operand supply that has evolved from register-based in Ampere to redundancy-free, memory-based in Hopper and Blackwell, efficiently orchestrating the compl...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

A Thread-Register Decoupled GPU Execution Model for Efficient Tensor Computation
1. 论文的主要贡献和创新点
✅ 解决的问题
现代GPU集成Tensor Cores后，整体张量吞吐量持续增长，但现代AI工作负载（GEMM操作与非GEMM操作交织）暴露出现有执行模型存在固定并行性、粗粒度调度两大核心瓶颈；同时Hopper、Blackwell采用无冗余内存基操作数供应，与Ampere的寄存器基方式存在架构差异，进一步增加了完整张量计算流水线的高效编排难度。

🚀 提出的新方法与思路
**FIBER（线程-寄存器解耦GPU执行模型）**，该方法扩展了GPU的SIMT模型，将基本执行实例fiber与私有寄存器所有权解耦，fiber仅携带最小控制状态，通过共享视图访问SM的寄存器；同时扩展了ISA、微架构与编译器，实现共享寄存器寻址、无冲突操作数交付、基于fiber的程序映射，为矩阵操作数供应提供无冗余替代方案，针对性解决现有模型的并行性与调度瓶颈。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 并行性适配 | 支持动态并行性扩展，解决固定并行性瓶颈 |
| 调度粒度 | 实现细粒度寄存器级数据流调度，替代粗粒度调度 |
| 架构适配 | 适配Hopper、Blackwell的无冗余内存基操作数供应，弥补不同GPU架构的供应方式差异 |
| 工作负载支持 | 适配GEMM与非GEMM操作交织的现代AI混合工作负载 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标
针对混合精度LLM服务场景开展实验，评估指标如下：
| 指标 | 含义 |
| --- | --- |
| 端到端加速比 | 相比基准方案的性能提升倍数，↑越高越好 |
| 内核级增益 | 内核层的性能提升倍数，↑越高越好 |
⚔️ 基线方法对比：论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：混合精度LLM服务场景下FIBER的性能增益**
| GPU平台 | 端到端加速比 | 内核级最大增益 |
| --- | --- | --- |
| Ampere | 2.25x（原始FP16计算为1.15x）✅ | 最高2.49x |
| Hopper | 1.8x | - |
| Blackwell | 2.09x | - |
💡 结论：在混合精度LLM服务场景下，FIBER在Ampere、Hopper、Blackwell三款GPU平台均实现性能提升，其中Ampere平台端到端加速比最高。

4. 关键结论和发现
- 主要发现1：FIBER通过将fiber与寄存器所有权解耦，实现动态并行性扩展与细粒度寄存器级数据流调度，有效解决现代AI混合工作负载的张量计算流水线编排瓶颈。
- 主要发现2：在混合精度LLM服务场景下，FIBER在不同代际GPU平台均实现可观性能增益，Ampere平台端到端加速比达2.25x，内核级增益最高达2.49x。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：论文提出的FIBER线程-寄存器解耦GPU执行模型，适配现代AI混合工作负载的张量计算需求，在多款代际GPU的LLM服务场景下实现了显著的性能加速。

</details>

---

### 9. [Beyond Multimodal Alignment: Certifying Physical Language through Response Substitution and Ordered Execution](https://arxiv.org/abs/2608.19492v1)

**Authors**: Kaizhen Tan, Xin Xu, Siru Tao, Yixiao Li, Hanzhe Hong, Yang Feng, Heqing Du  
**Category**: cs.LG  
**Published**: 2026-08-21  
**Score**: 46.5  
**Type**: new  
**ArXiv ID**: 2608.19492v1  

#### Abstract
World models increasingly treat compact multimodal representations as interfaces between perception and physical interaction, yet existing probes do not establish whether different sensors carry the same executable meaning or whether that meaning survives a new action composition. We introduce an op...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Beyond Multimodal Alignment: Certifying Physical Language through Response Substitution and Ordered Execution
1. 论文的主要贡献和创新点
✅ 解决的问题
现有世界模型的多模态探针未建立不同传感器携带的可执行意义是否一致，也未验证该意义在新动作组合中是否保留，无法分离物理语言的不同层面能力。
🚀 提出的新方法与思路
**operational capability hierarchy**：将物理语言能力分离为属性访问、响应替换、融合闭合、有序执行等可独立测试的成就。
**Disjoint-Bridge Operator-Substitution Certificate (DBOSC)**：设计验证方案，检查独立训练的模态编译器在训练面板外的证据上是否能互换进入冻结的响应图表。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 可执行意义一致性验证 | 解决现有探针无法验证模态间可执行意义一致性的缺陷 |
| 动作组合意义保留测试 | 可验证物理意义在新动作组合中的延续性 |
| 能力分层测试 | 通过operational capability hierarchy分离不同层面的物理语言成就 |
| 跨样本泛化测试 | DBOSC可在训练外样本上测试模态响应互换性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Cluster Haptic | 测试音频与加速度表征的可执行意义一致性（未见过的表面） |
| controlled elastoplastic system | 测试有序执行与互补模态盲区下的动作组合意义 |
🎯 实验设置与评估指标
任务：验证多模态表征的可执行意义在未见过样本及动作组合中的保留性，探究执行器与图表对任务的影响。
| 指标 | 含义 | 方向 |
| --- | --- | --- |
| NMSE | 归一化均方误差，衡量预测值与真实值的物理动作差异 | ↓ 越低越好 |
| 响应空间距离比值 | 错表面与同表面表征的响应空间距离之比，衡量表征一致性 | ↑ 越大说明同表面表征越一致 |
| 注册检查通过率 | 符合要求的测试项数量占总注册项的比例 | ↑ 越高越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 现有多模态探针 | 探测方法 | 仅评估多模态匹配度，未验证可执行意义与动作组合意义 |
| entity-blind predictor | 预测器 | 仅基于实体特征预测，未建模执行流程与动作序列 |
| population chart | 响应图表 | 全局冻结响应图，性能低于任务定制的图表 |
| full fused info matrix | 融合矩阵 | 使用全部多模态融合信息，性能更优 |
| diagonal restricted fused info matrix | 融合矩阵 | 仅使用融合信息的对角部分，性能与全融合相当 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**Cluster Haptic场景（无表号）**
| 指标 | 数值 | 结论 |
| --- | --- | --- |
| 同表面与错表面响应空间距离比值 | 4.5x | 未见过的表面上，同表面多模态表征的一致性更高 |
| 覆盖的未见过表面数量 | 19 | 结果具有普适性 |
💡 结论：未见过的物理表面上，音频与加速度表征携带的可执行意义保持一致。

**controlled elastoplastic system场景（无表号）**
| 指标 | 数值 | 对比 |
| --- | --- | --- |
| 收敛预算下oracle NMSE | 0.18 | 三阶任务图表可完成目标物理动作 |
| 注册检查通过率 | 14/16 | 多数任务符合预期要求 |
| 全vs对角融合矩阵性能 | 相当 | 融合信息的对角限制即可满足任务需求 |
| 执行器性能差距 | 38x | 发射整个程序的执行器比实体盲预测器性能差 |
💡 结论：物理语言任务的完成依赖执行器而非表征图表，融合信息存在非可识别性限制，仅用对角部分即可达到全融合性能。

4. 关键结论和发现
- 现有多模态探针的核心局限是未验证模态间可执行意义一致性及动作组合意义的保留，DBOSC与operational capability hierarchy可有效实现物理语言能力的分层测试与跨样本验证；
- 多模态表征的可执行意义在未见过的物理表面及动作组合中具有一致性，任务执行的关键是执行器而非表征图表；
- 压缩与融合本身无法确定未见过的组合律，存在非可识别性限制，融合信息的对角部分可媲美全融合性能；
方法局限性：论文未报告方法在触觉表面、弹塑性系统之外的其他物理场景的泛化能力，也未报告极端扰动下的鲁棒性表现；
未来工作：探索更多物理场景下的可执行意义测试，解决组合律的非可识别性问题，优化执行器的程序级建模能力。

> ✅ **总结一句话**：该论文提出operational capability hierarchy与DBOSC方法，验证了多模态表征在未见过样本及动作组合中可执行意义的一致性，分离了物理语言测试的不同层面成就，明确了执行器与融合信息的关键影响。

</details>

---

### 10. [Learning Hierarchical Skill Policies with Offline Quality-Diversity Reinforcement Learning](https://arxiv.org/abs/2608.19684v1)

**Authors**: Tanachai Anakewat, Takayuki Osa, Tatsuya Harada  
**Category**: cs.AI  
**Published**: 2026-08-21  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2608.19684v1  

#### Abstract
Recent studies investigate how to leverage pre-collected datasets to improve the policy performance and sample efficiency of RL. One promising approach to achieve this goal is to employ a two-stage strategy: In the first stage, diverse skills are extracted as a low-level policy from a given dataset,...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Learning Hierarchical Skill Policies with Offline Quality-Diversity Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有两阶段分层技能策略中，低层次技能提取依赖无监督学习（如trajectory VAE），其质量高度依赖离线数据集的质量，导致学习过程的鲁棒性不足。
🚀 提出的新方法与思路
**QDOS（Quality-Diversity Offline Skill learning）**：是用于鲁棒离线到在线学习的统一 pipeline，核心包含两部分：1）优势加权质量多样性预训练目标，通过轨迹段的估计优势权衡技能提取与多样性目标，实现多样且高价值的技能提取；2）双数据集复用策略，将离线数据既用于技能预训练，又通过伪标签填充在线重播缓冲区，提升数据利用率。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 技能提取能力 | 解决低层次技能质量依赖数据集质量的痛点，提取的技能兼具多样性与高价值性 |
| 学习鲁棒性 | 统一离线技能预训练与在线数据复用，实现从离线到在线的稳定过渡 |
| 任务性能 | 在结构化操作、非结构化 locomotion 的稀疏奖励任务中，相较于强基线有显著提升，加速探索并提高最终回报 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 用于技能预训练，以及通过伪标签填充在线重播缓冲区 |

🎯 实验设置与评估指标
任务为结构化操作任务、非结构化 locomotion 任务（稀疏奖励领域）；论文未报告具体评估指标。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告（所有指定实验均未报告具体数据、表号或结论）

4. 关键结论和发现
- 主要发现
1. QDOS通过优势加权的质量多样性预训练目标，有效提取了兼具多样性和高价值性的技能，缓解了低层次策略对离线数据集质量的依赖；
2. 双数据集复用策略实现了离线数据的高效利用，加速了离线到在线的学习过程；
3. 在稀疏奖励的结构化操作、非结构化 locomotion 任务中，QDOS的性能显著优于强基线。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：提出了QDOS方法，结合优势加权质量多样性预训练与双数据集复用策略，实现鲁棒的离线到在线分层技能策略学习，在稀疏奖励的操作和 locomotion 任务中性能优于基线。

</details>

---

### 11. [Compliance, Capability, and Conflict: Benchmarking Multimodal LLMs under System Messages](https://arxiv.org/abs/2608.19207v1)

**Authors**: Juan Yeo, Geewook Kim  
**Category**: cs.CL  
**Published**: 2026-08-21  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2608.19207v1  

#### Abstract
Production deployments of Multimodal Large Language Models (MLLMs) increasingly rely on system messages to govern model behavior. Yet existing benchmarks either evaluate constraints in text only or embed them into the user turn, leaving system-message adherence in multimodal contexts largely unmeasu...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Compliance, Capability, and Conflict: Benchmarking Multimodal LLMs under System Messages
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多模态大模型（MLLM）的评估基准要么仅在文本中评估约束，要么将约束嵌入用户提问轮次，未对多模态场景下的系统消息遵循性进行测量；同时现有研究未探究合规性是否以牺牲基础视觉-语言能力为代价，存在评估体系的缺失。

🚀 提出的新方法与思路
**VSysBench**：基于MMVet-v2构建的基准，将系统消息约束分为5大类、22个子类，覆盖从视觉环境下的文本指令到完全视觉基础的约束，为每个约束配对对应的不对齐版本以测试指令层级下的冲突压力；采用Joint Satisfaction Rate（JSR）和Cross-Constraint Sensitivity（CCS）两个指标，联合评估模型响应的约束合规性与答案正确性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 多模态系统消息场景覆盖 | 覆盖从视觉环境中文本指令到完全视觉基础的多级别系统消息约束，适配多模态场景评估需求 |
| 评估维度完整性 | 同时评估约束合规性与基础视觉-语言能力，通过JSR和CCS两个指标联合衡量二者平衡情况 |
| 指令层级冲突测试 | 为每个约束配对不对齐版本，可有效测试模型在指令层级冲突下的表现 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| MMVet-v2 | 构建VSysBench基准，用于评估多模态大模型在系统消息下的合规性及相关能力 |

🎯 实验设置与评估指标
任务：评估多模态大模型在系统消息下的约束合规性、答案正确性，以及不同模型在指令冲突下的表现。
| 指标 | 含义 |
| --- | --- |
| Joint Satisfaction Rate（JSR） | 衡量模型响应同时满足约束合规性和答案正确性的比例，↑越高越好 |
| Cross-Constraint Sensitivity（CCS） | 衡量模型在指令冲突下的敏感度，↓越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 16个MLLMs | 现有多模态大模型 | 覆盖开放权重模型与顶级专有模型，用于验证VSysBench的有效性及不同模型的表现差异 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（L2/碰撞率等）**
论文未报告
**表2：效率对比（FPS/参数量）**
论文未报告
**表3：跨域/zero-shot迁移**
论文未报告
**表4：鲁棒性/扰动测试**
论文未报告
**表5：消融实验**
论文未报告
💡 结论：施加系统消息会显著降低多模态大模型的基础任务准确率；开放权重模型在用户指令冲突下合规性崩溃，顶级专有模型的合规性保持稳定；视觉基础类约束是所有模型最难满足的约束类别。

4. 关键结论和发现
- 主要发现：1）现有多模态大模型评估基准缺失系统消息在多模态场景下的遵循性评估，且未探究合规性与基础视觉-语言能力的权衡；2）系统消息会损害多模态大模型的基础任务准确率，且不同权重类型模型在指令冲突下的合规表现存在明显差异；3）视觉基础类约束是多模态大模型遵循系统消息时最难满足的约束类别。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：该论文提出VSysBench基准，填补了多模态大模型系统消息遵循性评估的空白，揭示了系统消息对模型基础能力的负面影响及不同模型在指令冲突下的表现差异。

</details>

---

### 12. [CacheRoute: Planned Prefix-Affinity Routing for Large-Scale LLM Serving](https://arxiv.org/abs/2608.19677v1)

**Authors**: Huang Cheng  
**Category**: cs.DC  
**Published**: 2026-08-21  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2608.19677v1  

#### Abstract
Prefix caching avoids prefill only when a repeated request returns to a server that still holds the prefix KV. Cache-blind balancing disperses that reuse; fixed affinity preserves it but can overload a server. CacheRoute resolves this tradeoff with a periodic routing plan. It admits high-rate keys t...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

CacheRoute: Planned Prefix-Affinity Routing for Large-Scale LLM Serving
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾是大规模LLM服务中前缀缓存复用与服务负载间的权衡：
1. 前缀缓存仅在重复请求回到持有前缀KV的服务器时，才能避免prefill步骤；
2. cache-blind balancing方法的缺陷：会分散缓存复用，导致KV缓存命中率低；
3. fixed affinity方法的缺陷：虽保留了缓存复用，但会造成服务器过载。

🚀 提出的新方法与思路
**CacheRoute（Planned Prefix-Affinity Routing）**：通过周期性路由计划解决上述权衡问题；将高频率键接纳到稳定的热集合，按预期负载放置其分配；热点键可使用多个目标，主要半合成聚合中的每个键仅使用一个目标。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| KV缓存命中率 | 较cache-blind balancing方法大幅提升 |
| QPS性能 | 在指定实验设置下达到五个基线最强者的2.3倍，满足3.5秒p99 SLO |
| 路由策略 | 平衡缓存复用与负载均衡，避免固定亲和性的服务器过载问题及cache-blind的缓存复用分散问题 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 半合成聚合 | 用于分离亲和性与放置对性能的影响 |
| Llama-3.3-70B workloads | 用于主benchmark性能测试 |
| 控制实验的8B workloads | 用于相关控制实验 |
| burst实验的workloads | 用于相关控制实验 |
| 32B workloads | 用于验证亲和性恢复不足时的性能影响（反例实验） |

🎯 实验设置与评估指标
任务：大规模LLM服务的前缀缓存路由优化，需满足3.5秒的p99延迟SLO。
| 指标 | 含义 |
| --- | --- |
| QPS | 每秒查询数，越高越好（↑） |
| KV缓存命中率 | 命中前缀KV缓存的请求比例，越高越好（↑） |
| p99延迟 | 99分位请求延迟，需≤3.5秒，越低越好（↓） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 5个基线方法 | 对比方法 | CacheRoute性能优于所有五个基线方法，是其中最强者的2.3倍 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告各定量结果对应的表号、图号，故无法列出具体定量结果表格。

4. 关键结论和发现
- 主要发现1：CacheRoute通过周期性路由计划平衡前缀缓存复用与服务负载，既解决了cache-blind balancing导致的缓存复用分散问题，又避免了固定亲和性方法的服务器过载问题。
- 主要发现2：在Llama-3.3-70B的主benchmark实验中，CacheRoute的性能在指定设置下显著优于五个基线方法，KV缓存命中率和QPS均有大幅提升。
- 主要发现3：当亲和性方法带来的KV工作恢复不足时，残留的负载偏斜会削弱或消除其性能提升，因此部署亲和性策略时不能仅依赖工作负载统计，需通过影子回放进行验证。
- 方法局限性：在亲和性恢复的KV工作不足的场景下，性能提升会被残留的负载偏斜抵消，导致无法达到预期效果。
- 未来工作：探索无需依赖影子回放的亲和性部署验证方法，或优化亲和性策略以减少残留负载偏斜的影响。

> ✅ **总结一句话**：CacheRoute通过周期性路由计划平衡大规模LLM服务中前缀缓存的复用与负载均衡，大幅提升KV缓存命中率和QPS，但部署亲和性策略前需通过影子回放验证，避免负载偏斜带来的性能损失。

</details>

---

### 13. [G-MARK: Grounded Multi-Agent Reasoning for Cooperative Driving via Knowledge Graphs](https://arxiv.org/abs/2608.19964v1)

**Authors**: Bhavya Gupta, Onat Gungor, Tajana Rosing  
**Category**: cs.LG  
**Published**: 2026-08-21  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2608.19964v1  

#### Abstract
Autonomous driving systems must operate under partial observability, where safety-critical objects may be occluded or visible only to neighboring connected vehicles. Vehicle-to-vehicle cooperation can reduce this uncertainty, but existing cooperative driving methods often compress multi-agent eviden...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：G-MARK: Grounded Multi-Agent Reasoning for Cooperative Driving via Knowledge Graphs
1. 论文的主要贡献和创新点
✅ 解决的问题
现有协同驾驶方法多将多智能体证据压缩为隐特征或隐藏多模态状态，导致无法明确各对象的观测主体、对象是否对自车（ego vehicle）可见，以及冲突证据对下游决策的影响；而自动驾驶系统需在部分可观测场景下运行，安全关键对象可能被遮挡或仅被相邻车辆观测，存在不确定性问题。
🚀 提出的新方法与思路
**Grounded Multi-Agent Reasoning Framework（G-MARK）**：将协同的以对象为中心的观测转换为显式的、具有来源属性的知识图谱（KGs），所生成的KGs保留对象假设及其来源属性、自车与伙伴车辆的可见性、不确定性、冲突、空间关系、规划相关上下文；再从KGs推导共享特征表示，支持轻量化任务头以完成对象推理、运动预测、控制选择、轨迹预测任务。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 遮挡推理准确率 | 比SOTA基线提升42.2% |
| 控制选择误差 | 比SOTA基线降低13.1% |
| 轨迹规划准确率 | 与SOTA基线相当 |
| 结构化通信载荷 | 比SOTA基线小25.6倍 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |
🎯 实验设置与评估指标
实验任务为协同驾驶相关任务，评估指标如下：
| 指标 | 含义（箭头） |
| --- | --- |
| 遮挡推理准确率 | ↑（越高越好） |
| 控制选择误差 | ↓（越低越好） |
| 轨迹规划准确率 | ↑（越高越好） |
| 结构化通信载荷 | ↓（越低越好） |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| State-of-the-art baseline | 协同驾驶方法 | 采用隐特征或隐藏多模态状态压缩多智能体证据 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（无对应表号）**
| 指标 | 与SOTA基线的差异 |
| --- | --- |
| 遮挡推理准确率 | 提升42.2% ✅ |
| 控制选择误差 | 降低13.1% |
| 轨迹规划准确率 | 相当 |
💡 结论：G-MARK在遮挡推理准确率、控制选择误差指标上优于现有SOTA基线，轨迹规划准确率与基线相当。

**效率对比（无对应表号）**
| 维度 | 与SOTA基线的差异 |
| --- | --- |
| 结构化通信载荷 | 比基线小25.6倍 ✅ |
💡 结论：G-MARK的结构化通信载荷远小于现有SOTA基线方法。

跨域/zero-shot迁移：论文未报告；鲁棒性/扰动测试：论文未报告；消融实验：论文未报告。
4. 关键结论和发现
- 主要发现：G-MARK通过显式知识图谱保留多智能体观测的来源、可见性等关键信息，有效提升了协同驾驶的遮挡推理和控制选择性能；G-MARK在保持与SOTA相当的轨迹规划准确率的同时，结构化通信载荷大幅降低。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：G-MARK是一种基于知识图谱的显式多智能体推理框架，通过将多智能体观测转化为来源感知的知识图谱，提升了协同驾驶的部分推理性能并降低了通信载荷。

</details>

---

### 14. [ReCache: Efficient KV Cache Reuse and Compression for Tool-Augmented LLM Agents](https://arxiv.org/abs/2608.19662v1)

**Authors**: Yichu Fang, Sitong Wei, Haozhe Hu, Xiaoyu Shen  
**Category**: cs.CL  
**Published**: 2026-08-21  
**Score**: 35.5  
**Type**: new  
**ArXiv ID**: 2608.19662v1  

#### Abstract
Agentic language models repeatedly encode tool and skill schemas that recur across requests in different combinations and orders, preventing standard prefix caching from reusing their key--value (KV) states. We introduce \textbf{ReCache}, a framework for independently caching resource representation...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# ReCache: Efficient KV Cache Reuse and Compression for Tool-Augmented LLM Agents

## 1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：Agentic语言模型会在不同请求中以不同组合和顺序重复编码跨请求的工具与技能模式，标准前缀缓存无法复用其键值（KV）状态，引发推理效率低下的痛点。
现有方法缺陷：标准前缀缓存缺乏对跨请求重复资源编码的KV复用能力；常规缓存机制难以同时兼顾任务性能和推理开销的平衡。

🚀 提出的新方法与思路
**Resource-wise attention**：移除不同资源间的交互，为各资源分配局部位置，生成组合不变性的KV块，支持资源独立的KV复用，打破跨资源交互的冗余计算。
**资源可见性限制机制**：将资源的可见范围限制在经贡献筛选的层-KV头-组路由中，减少冗余的资源访问，降低不必要的计算开销。
**结构与语义修剪**：仅保留调用过程中关键的字段，进一步压缩KV缓存规模，降低推理的计算和内存负担。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 任务性能 | Resource-wise attention可匹配密集调用的任务性能 |
| 时间效率 | 显著提升首token生成速度 |
| 内存占用 | 大幅降低KV张量的内存分配 |
| 注意力计算效率 | 加速注意力计算过程 |

## 2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 7个公开的工具和技能使用数据集 | 构建评估基准，包含资源不相交测试 |

🎯 实验设置与评估指标
任务：工具增强型LLM代理的工具/技能使用任务（基于公开基准开展）
| 指标 | 含义 | 方向 |
| --- | --- | --- |
| Inv-F1 | 调用F1值，衡量工具使用任务性能 | ↑ |
| 时间-to-first-token | 生成首token的耗时，衡量推理时间效率 | ↓ |
| KV张量内存占用 | KV缓存的内存分配量，衡量内存开销 | ↓ |
| 注意力加速比 | 注意力计算的速度提升倍数 | ↑ |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 密集调用（dense invocation） | 基线方法 | 无KV缓存优化的原始调用方式，作为性能参照 |

## 3. 主要实验结果和性能指标
📊 定量结果汇总
### 主benchmark性能
论文未明确报告对应表号，仅提及Resource-wise attention与密集调用的Inv-F1性能相当，具体数据无对应表号。
### 效率对比（FPS/参数量）
论文未报告FPS或参数量指标，仅提及时间-to-first-token效率、KV内存及注意力加速结果，无对应表号。
### 跨域/zero-shot迁移
论文未报告
### 鲁棒性/扰动测试
论文未报告
### 消融实验
论文未报告

💡 结论：ReCache通过分离可复用资源编码与选择性资源访问，在保持任务性能的同时有效降低了工具增强型LLM代理的推理开销。

## 4. 关键结论和发现
- 主要发现：1. 分离可复用的模式编码与选择性资源访问，可在Agentic LLM代理中实现推理开销降低且任务性能损失有限；2. ReCache的Resource-wise attention模块兼顾了任务性能与推理速度；3. 资源可见性限制和修剪技术可有效压缩KV缓存的内存占用并加速注意力计算。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：ReCache框架通过Resource-wise attention、资源可见性限制及结构与语义修剪技术，分离工具和技能模式的可复用编码与选择性资源访问，在保持任务性能的同时，显著降低了工具增强型LLM代理的推理计算与内存开销。

</details>

---

### 15. [SAPO: Single-Rollout Autoregressive Policy Optimization for Agentic Reinforcement Learning](https://arxiv.org/abs/2608.19842v1)

**Authors**: Dayang Liang, Lang Feng, Bo An, Yunlong Liu  
**Category**: cs.AI  
**Published**: 2026-08-21  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2608.19842v1  

#### Abstract
Agentic reinforcement learning (RL) has become a critical stage in the post-training of large language models. Existing critic-free, group-relative methods estimate policy advantages from multiple rollouts, avoiding the substantial memory overhead of conventional proximal policy optimization (PPO) a...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

SAPO: Single-Rollout Autoregressive Policy Optimization for Agentic Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有Agentic RL领域的critic-free、组相对策略优化方法存在三个核心局限：① 缺乏显式价值泛化和有效的时间信用分配；② 长期复杂任务中存在潜在的优势崩溃；③ 需要在采样预算与策略性能间进行代价高昂的权衡。

🚀 提出的新方法与思路
**SAPO框架**：一种低内存、高计算效率的Agentic RL框架，核心为策略与价值函数共享单个自回归backbone；利用LLM的自回归结构在不同因果边界生成策略与价值预测（参数共享）；同时独立优化PPO目标与辅助的在线策略SARSA目标。
**轨迹级广义优势估计器**：结合lambda-returns与批归一化，用于稳健估计每一步的贡献，解决时间信用分配问题。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 策略性能 | 在ALFWorld与WebShop任务上，平均性能比PPO高15.1个百分点，比GRPO高12.1个百分点 |
| 内存开销 | 消除了单独critic模型的内存成本 |
| 计算效率 | 比PPO降低了33.2%的每迭代运行时间 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| ALFWorld | 性能评估实验 |
| WebShop | 性能评估实验 |

🎯 实验设置与评估指标
在ALFWorld和WebShop的长程交互任务上开展Agentic RL训练实验；指标及含义如下：
| 指标 | 含义 |
| --- | --- |
| 任务性能百分比 | 越高越好 |
| 每迭代运行时间 | 越低越好 |
| 内存开销 | 越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| PPO | 策略优化方法 | 传统近端策略优化，需单独的critic模型 |
| GRPO | 策略优化方法 | 无critic的组相对策略优化方法，需多rollout估计策略优势 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主基准性能实验（无对应表号）**
| 方法 | 平均性能提升（对比PPO） | 平均性能提升（对比GRPO） |
| --- | --- | --- |
| SAPO | +15.1个百分点 ✅ | +12.1个百分点 ✅ |
💡 结论：SAPO在ALFWorld与WebShop基准任务上的策略性能显著优于PPO和GRPO。

**效率对比实验（无对应表号）**
| 维度 | SAPO | PPO | 改进幅度 |
| --- | --- | --- | --- |
| 每迭代运行时间 | 论文未报告具体数值 | 论文未报告具体数值 | 比PPO降低33.2% ✅ |
| 内存开销 | 消除单独critic模型的内存成本 | 需单独critic模型，内存成本高 | 消除了单独critic模型的额外内存开销 ✅ |
💡 结论：SAPO的内存与计算效率均优于传统PPO方法。

跨域/zero-shot迁移：论文未报告；鲁棒性/扰动测试：论文未报告；消融实验：论文未报告。

4. 关键结论和发现
- SAPO框架训练稳定，同时实现了更高的策略性能与更优的内存、计算效率。
- 轨迹级广义优势估计器结合lambda-returns与批归一化，可有效解决时间信用分配问题，助力SAPO稳健训练。
- SAPO在ALFWorld和WebShop任务上的性能显著超越现有主流PPO、GRPO方法。

- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出了共享单个自回归backbone的Agentic RL策略优化框架SAPO，在ALFWorld与WebShop任务上性能优于PPO和GRPO，同时显著降低了内存与计算开销，实现了低内存、高计算效率的Agentic RL训练。

</details>

---

### 16. [Projector Is All You Train](https://arxiv.org/abs/2608.19726v1)

**Authors**: Nyx Iskandar, Saathvik Selvan, Slater Victoroff  
**Category**: cs.CL  
**Published**: 2026-08-21  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2608.19726v1  

#### Abstract
The typical training process of a multimodal large language model (MLLM) involves adapting both the language model backbone and the projector between the backbone and a modality-specific encoder. We ask whether fine-tuning the backbone of an MLLM is necessary to adapt it to a new modality. Through e...

---

### 17. [Rule-Compliant Visual Spatial Planning for Multimodal Large Language Models](https://arxiv.org/abs/2608.20237v1)

**Authors**: Yu Chen, Ting Lei, Yaoyi Li, Jia Cai, Zhecen Wu, Yang Liu  
**Category**: cs.AI  
**Published**: 2026-08-21  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.20237v1  

#### Abstract
Multimodal large language models (MLLMs) combine linguistic reasoning with visual perception, yet their ability to perform visual spatial planning under explicit or previously unseen rule constraints remains underexplored. This setting requires models to jointly understand spatial layouts, interpret...

---

### 18. [NepOOC-M: Bilingual Nepali-English Benchmark and Comparative Analysis of Multimodal Architectures for OOC Detection](https://arxiv.org/abs/2608.19212v1)

**Authors**: Sanjeev Khatiwada  
**Category**: cs.CL  
**Published**: 2026-08-21  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.19212v1  

#### Abstract
Out-of-context (OOC) misinformation pairs authentic images with misleading captions to construct false narratives without image manipulation, making detection a problem of multimodal alignment rather than image forensics. Despite the prevalence and consequences of OOC misinformation in Nepal, no pub...

---

### 19. [Robust Incomplete Multimodal Sentiment Analysis via Iterative Proxy Correction](https://arxiv.org/abs/2608.19971v1)

**Authors**: Zhifa Geng, Subin Huang, Hao Guo, Junjie Chen, Sanmin Liu, Chao Kong  
**Category**: cs.CL  
**Published**: 2026-08-21  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.19971v1  

#### Abstract
Multimodal sentiment analysis aims to infer affective states by integrating language, visual, and acoustic cues. However, real-world multimodal inputs are often incomplete or corrupted, which can weaken cross-modal complementarity and introduce misleading information into downstream fusion. Existing...

---

### 20. [From Retrieved Context to Runtime Control: Adaptive Compression for Edge-based RAG](https://arxiv.org/abs/2608.19535v1)

**Authors**: Zlatan Feric, Amir Taherin, Yanzhi Wang, David Kaeli  
**Category**: cs.AI  
**Published**: 2026-08-21  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2608.19535v1  

#### Abstract
Retrieval-augmented generation (RAG) improves language-model responses by grounding generation in external passages, which comes with overhead: retrieved context lengthens the prompt, increasing prefill work, KV-cache footprint, memory traffic, latency, and energy. Context compression offers a natur...

---

### 21. [Dynamic Gated Cross-Modal Fusion with Sarcastic-aware Contrastive Regularization for Multimodal Sarcasm Detection](https://arxiv.org/abs/2608.19942v1)

**Authors**: Hao Guo, Subin Huang, Junjie Chen, Zhifa Geng, Sanmin Liu, Chao Kong  
**Category**: cs.CL  
**Published**: 2026-08-21  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2608.19942v1  

#### Abstract
Multimodal sarcasm detection aims to identify sarcastic intent from multimodal content, where inconsistencies between literal meaning and contextual cues often signal irony. This task has attracted increasing research attention. However, accurate detection remains challenging due to instance-depende...

---

### 22. [Ask Self, Ask Others: Relation Is All You Need](https://arxiv.org/abs/2608.20172v1)

**Authors**: Yuting Ge, Pengju Yang, Mingkai Nie  
**Category**: cs.LG  
**Published**: 2026-08-21  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2608.20172v1  

#### Abstract
Attention directly derives normalized information flow from pairwise scores. We introduce Relation, an alternative token-mixing primitive that first organizes pairwise evidence into explicit Self and Exchange relations and derives information flow afterward. This relational organization gives rise t...

---

### 23. [When to Retrain: An Empirical Study of Retraining Policies for Streaming ML Under Concept Drift, Budget, and Latency Constraints](https://arxiv.org/abs/2608.19488v1)

**Authors**: Sawan Dasari  
**Category**: cs.LG  
**Published**: 2026-08-21  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2608.19488v1  

#### Abstract
Production machine learning systems degrade under concept drift, yet practitioners have little principled guidance on when to retrain. Retraining is costly, retraining budgets are finite, and a retrained model does not take effect instantly: training and deployment latency leave a stale model servin...

---

### 24. [Beyond Memory Majority: Latent-Source Reasoning for Multi-Agent Memory Arbitration](https://arxiv.org/abs/2608.19701v1)

**Authors**: Chenchen Lin, Wenhao Yuan, Xuehe Wang, Edith Cheuk Han Ngai  
**Category**: cs.AI  
**Published**: 2026-08-21  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2608.19701v1  

#### Abstract
Long-term multi-agent systems continuously accumulate the memories produced by different agents. Existing memory methods typically treat retrieved memories as independent evidence and combine them through voting or weighting. However, this independence assumption often fails in multi-agent settings:...

---

### 25. [Orthogonal JEPA: Factorized Predictive States for Latent World Models](https://arxiv.org/abs/2608.20065v1)

**Authors**: Taoyong Cui, Pheng Ann Heng, Wanli Ouyang  
**Category**: cs.LG  
**Published**: 2026-08-21  
**Score**: 24.0  
**Type**: new  
**ArXiv ID**: 2608.20065v1  

#### Abstract
World models construct latent states that support prediction, planning, and reasoning about an underlying system. Joint-embedding predictive architectures (JEPAs) offer a direct way to learn such states by predicting targets in representation space instead of reconstructing every detail of the obser...

---

### 26. [Contrastive Mixed Prompt Learning for Incomplete Multimodal Sentiment Analysis with Unseen Modality Combination](https://arxiv.org/abs/2608.20019v1)

**Authors**: Kaixin Xu, NaiJin Liu, Yulin Kang, Tangyue Jin, Zixuan Yu, Wenxi Zhao, Yibei Liu, Qianle Zhang, Yangyang Wu, Mengying Zhu, Meng Xi  
**Category**: cs.AI  
**Published**: 2026-08-21  
**Score**: 23.5  
**Type**: new  
**ArXiv ID**: 2608.20019v1  

#### Abstract
Incomplete multimodal sentiment analysis has garnered significant attention in recent years. Existing approaches typically assume that data is missing at random or are designed specifically for certain missing patterns, ignoring the modality combination inconsistency between training and testing pha...

---

### 27. [Empirical Characterization of Learning Geometry in Hybrid Quantum Forecasting Models](https://arxiv.org/abs/2608.19497v1)

**Authors**: Sandra Leticia Ju\'arez-Osorio, Jorge I. Hernandez-Martinez, Jesus Ivan Ruiz-Martinez, Andres Mendez-Vazquez, Eduardo Rodriguez-Tello  
**Category**: cs.LG  
**Published**: 2026-08-21  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2608.19497v1  

#### Abstract
We characterize the learning dynamics of a compact hybrid quantum forecasting model through comparison with a structurally aligned classical baseline. Using stationary harmonic-mixture and nonstationary chirp benchmarks with controlled spectral complexity and data availability, we analyze empirical ...

---

### 28. [AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement](https://arxiv.org/abs/2608.20318v1)

**Authors**: Yizhe Chi, Wenyi Li, Deyao Hong, Xiaoqiu Wang, Mingju Gao, Kaisen Yang, Bingxiang He, Youjie Zheng, Calvin Xiao, Qinhuai Na  
**Category**: cs.AI  
**Published**: 2026-08-21  
**Score**: 22.5  
**Type**: new  
**ArXiv ID**: 2608.20318v1  

#### Abstract
Recursive self-improvement (RSI) asks whether an AI system can improve the process that produces AI systems, so that the next system inherits the improvement. That process is the training algorithm: a better objective or update rule improves the compute\mbox{-}capability exchange rate for every subs...

---

### 29. [When Irrelevant Text Matters: Affine Margin Shifts in Multimodal Large Language Models](https://arxiv.org/abs/2608.19208v1)

**Authors**: Yinfeng Wang, Zhiyuan Yao, Zheren Fu, Lei Zhang, Zhendong Mao  
**Category**: cs.CL  
**Published**: 2026-08-21  
**Score**: 22.5  
**Type**: new  
**ArXiv ID**: 2608.19208v1  

#### Abstract
Multimodal large language models (MLLMs) are frequently exposed to auxiliary textual context, the impact of which on visually grounded tasks remains underexplored. In this paper, we investigate the influence of task-irrelevant context by formulating it as a controlled intervention within a binary vi...

---

### 30. [Beyond Imitation: Filtering On-Policy Distillation by Reasoning Progress](https://arxiv.org/abs/2608.19408v1)

**Authors**: Chen Yang, Haiyuan Wan, Rengrong Xiong, Yize Chen, Danny H. K. Tsang  
**Category**: cs.AI  
**Published**: 2026-08-21  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2608.19408v1  

#### Abstract
On-policy distillation (OPD) has emerged as an effective framework for post-training language models by pairing student-generated trajectories with dense token-level supervision from a teacher. However, OPD implicitly assumes that teacher-derived rewards are an appropriate proxy for reasoning progre...

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
