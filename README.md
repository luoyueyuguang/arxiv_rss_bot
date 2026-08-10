# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-08-10 07:20:55 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [HiSparse: Scaling Sparse-Attention Decoding with Hierarchical KV Cache Management](https://arxiv.org/abs/2608.07009v1)

**Authors**: Zhiqiang Xie, Zhangheng Huang, Tingwei Huang, Ziyi Xu, Ruiyang Ma, Christos Kozyrakis  
**Category**: cs.DC  
**Published**: 2026-08-10  
**Score**: 90.0  
**Type**: new  
**ArXiv ID**: 2608.07009v1  

#### Abstract
Top-k sparse attention makes long-context LLM decoding cheap to compute: each step reads only a few thousand selected KV entries rather than the full context. Serving systems, however, typically keep the entire KV cache in GPU HBM so that every position stays selectable, so a request's memory bill s...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：HiSparse: Scaling Sparse-Attention Decoding with Hierarchical KV Cache Management
1. 论文的主要贡献和创新点
✅ 解决的问题
现有top-k稀疏注意力降低了长上下文大语言模型（LLM）解码的计算成本，但当前服务系统需将整个KV缓存保留在GPU HBM中，导致请求的内存账单随上下文长度增长，解码受限于内存容量，KV缓存超过HBM则无法服务请求。
🚀 提出的新方法与思路
**Hierarchical KV Cache for Sparse-Attention Serving**：将每个请求的完整KV历史存储在主机内存，用小的固定大小GPU缓存限制解码内存占用。
**Fused CUDA Kernel**：在解码CUDA图内解析每层的选点操作，包括命中检测、LRU替换及主机到设备的数据获取。
**Exact Layer-wise Prefetching**：当模型各层共享选点时，通过精确层间预取隐藏约一半的缺失开销，且不改变模型输出。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 内存容量限制 | 突破原KV缓存全存HBM带来的上下文长度增长限制，仅需小固定GPU缓存即可服务长上下文请求 |
| 计算开销 | 融合CUDA内核与分层预取减少额外开销，无IO oracle显示无额外每token计算成本 |
| 模型输出一致性 | 保持与原模型完全一致的输出，无精度损失 |
| 解码服务能力 | 在长上下文工作负载上峰值生成吞吐量最高提升4.7倍，高负载下缩短首token时间 |
2. 核心实验方法和设置
📚 使用的数据集
论文未报告
🎯 实验设置与评估指标
本研究在H200、B200、GH200三款GPU平台上，针对DSA、NSA、Quest三种稀疏注意力家族的模型，对长上下文工作负载的稀疏注意力解码服务性能进行评估。
| 指标 | 含义 |
| --- | --- |
| 峰值生成吞吐量 | 越高越好（↑） |
| 每token延迟 | 越低越好（↓） |
| 首token时间 | 越低越好（↓） |
| 主机设备IO开销 | 内存受限特性的唯一代价 |
⚔️ 基线方法对比
论文未报告
3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（L2/碰撞率等）**
论文未报告
**效率对比（FPS / 参数量）**
论文未报告
**跨域 / zero-shot 迁移**
论文未报告
**鲁棒性 / 扰动测试**
论文未报告
**消融实验**
论文未报告
仅明确报告的定量结果：长上下文工作负载下峰值生成吞吐量最高提升4.7倍，高负载下首token时间缩短，每token延迟与原方法可比；no-IO oracle显示解析机制本身无额外每token成本。
💡 结论：HiSparse在长上下文稀疏注意力解码的服务性能上取得显著提升，未引入额外每token计算开销，仅以主机设备IO为内存受限的代价。
4. 关键结论和发现
- 在三款GPU平台及三种稀疏注意力家族的长上下文工作负载上，HiSparse可将峰值生成吞吐量最高提升4.7倍，保持可比的每token延迟，缩短了高负载下的首token时间。
- HiSparse仅改变KV缓存的存储位置，不影响模型输出准确性，保证了结果一致性。
- HiSparse的解析机制本身无额外可测量的每token计算成本，主机与设备间的IO是其内存受限特性的唯一代价。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：HiSparse通过分层KV缓存管理、融合CUDA内核与精确层间预取技术，实现了稀疏注意力解码的长上下文服务，在保持模型输出准确性的同时大幅提升了长上下文工作负载的峰值生成吞吐量，仅以主机设备IO为内存受限的代价。

</details>

---

### 2. [CrystalGRPO: Target-Aligned and Coverage-Preserving Reinforcement Learning for Flow-Based Crystal Structure Prediction](https://arxiv.org/abs/2608.06582v1)

**Authors**: Kaixiang Su, Hongfei Xue, Qiang Zhu  
**Category**: cs.LG  
**Published**: 2026-08-10  
**Score**: 82.0  
**Type**: new  
**ArXiv ID**: 2608.06582v1  

#### Abstract
Flow-based generative models can efficiently produce candidate structures for crystal structure prediction (CSP), but their pretrained objectives do not directly optimize downstream target recovery. Reinforcement-learning post-training offers a flexible solution, yet existing approaches rely primari...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

CrystalGRPO: Target-Aligned and Coverage-Preserving Reinforcement Learning for Flow-Based Crystal Structure Prediction
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：flow-based生成模型的预训练目标无法直接优化晶体结构预测(CSP)的下游目标恢复；现有强化学习后训练方法存在缺陷：依赖能量奖励（预测能量无法识别参考多型）、采用仅坐标的随机策略、奖励驱动的策略集中会降低有限预算目标恢复所需的候选覆盖率。
🚀 提出的新方法与思路
**CrystalGRPO框架**：扩展现有ODE-to-SDE策略构建到联合坐标-晶格状态；整合MACE预测能量与StructureMatcher的恢复分数；提供两种运行模式：CrystalGRPO-Q（优先单样本恢复）、CrystalGRPO-C（结合全轨迹参考正则化与覆盖感知组优势，保留有限预算目标恢复能力）。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 策略空间 | 从仅坐标的随机策略扩展至联合坐标-晶格状态策略 |
| 奖励设计 | 结合MACE能量与StructureMatcher恢复分数，缓解单一能量奖励无法识别参考多型的问题 |
| 运行模式 | 两种模式可分别适配单样本（CrystalGRPO-Q）和有限预算下的多样本（CrystalGRPO-C）目标恢复需求 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| MP-20 | Crystal结构预测(CSP)相关基准测试 |
| MPTS-52 | Crystal结构预测(CSP)相关基准测试 |
🎯 实验设置与评估指标
任务：针对flow-based生成模型，采用强化学习后训练方法，评估晶体结构预测(CSP)的样本恢复性能。
| 指标 | 含义（箭头方向） |
| ---- | ---- |
| one-sample RMSE | 单样本预测的均方根误差，↓越低越好 |
| twenty-sample RMSE | 二十样本预测的均方根误差，↓越低越好 |
| Top-1 | 前1个候选中包含参考结构的比例，↑越高越好 |
| Top-20 | 前20个候选中包含参考结构的比例，↑越高越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| coordinate-only reinforcement | 基线强化学习方法 | 仅基于坐标的随机策略，依赖能量奖励 |
| PXRDGen | 基线生成模型backbone | flow-based生成模型核心架构 |
| OMatG | 基线生成模型backbone | flow-based生成模型核心架构 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文仅提供趋势性描述，未报告具体表号对应的定量数值：在四个backbone-dataset设置（MP-20、MPTS-52分别搭配PXRDGen、OMatG）中，CrystalGRPO的两种变体均降低one-和twenty-sample RMSE；CrystalGRPO-Q持续改进Top-1指标，CrystalGRPO-C在所有设置下获得更高的Top-20指标。
💡 结论：CrystalGRPO的两种变体均能提升晶体结构预测中样本的恢复性能，且两种模式分别适配不同场景的恢复需求。
其他实验（效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）：论文未报告

4. 关键结论和发现
- 主要发现：1. CrystalGRPO可有效提升flow-based CSP模型的下游目标恢复性能；2. CrystalGRPO-Q适配单样本恢复需求，CrystalGRPO-C适配有限预算下的多样本恢复需求；3. 联合坐标-晶格状态的策略及多源奖励设计优于单一坐标策略和能量奖励。
- 方法局限性：论文未报告
- 未来工作：论文未提及

> ✅ **总结一句话**：本文提出CrystalGRPO框架，通过扩展策略空间、整合多源奖励设计并提供两种适配不同恢复需求的运行模式，在晶体结构预测任务中实现了样本恢复性能的提升。

</details>

---

### 3. [DiDPO: Diff-in-Diff Policy Optimization for Coding Agent Training](https://arxiv.org/abs/2608.07147v1)

**Authors**: Xucong Wang, Zhe Zhao, Liheng Yu, Di Wu, Xiaofeng Cao, Pengkun Wang  
**Category**: cs.AI  
**Published**: 2026-08-10  
**Score**: 73.0  
**Type**: new  
**ArXiv ID**: 2608.07147v1  

#### Abstract
Reinforcement learning with Verifiable Reward (RLVR) has emerged as a powerful paradigm for training coding agents, where the execution feedback from compilation and tests provides objective verification. However, unlike agent tasks, coding agents face a unique and finer-grained credit assignment ch...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

DiDPO: Diff-in-Diff Policy Optimization for Coding Agent Training
1. 论文的主要贡献和创新点
✅ 解决的问题
编码代理训练存在核心矛盾：编码动作会同时对代码版本的不同区域做出多样修改，导致独立代码修改的贡献难以区分；现有用于编码代理训练的Reinforcement learning with Verifiable Reward（RLVR）方法仅利用结果奖励或step-level奖励，无法深入探究代码diff，无法让编码动作的独特属性被训练感知。

🚀 提出的新方法与思路
**DiDPO（Diff-in-Diff Policy Optimization）** 是一种无critic的RL方法，直接从代码diff的结构构建细粒度信用单元，核心流程：1. 将多轮编码交互组织为多个thought-action步骤，从采样轨迹中发现代码diff；2. 通过自定义的“分组性得分（groupability score）”将整个diff拆分为高度相似的子diff，选择锚点，该得分的拆分模式最优平衡锚点的语义范围与组质量；3. 由锚点形成优势组，将diff级优势投影回单个响应token。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 细粒度信用分配 | 现有RLVR方法无法深入代码diff，难以区分独立代码修改的贡献；DiDPO通过代码diff结构构建单元，利用分组性得分拆分sub-diff并投影优势到token，直接解决细粒度信用分配问题 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| long-horizon coding and reasoning benchmarks | 评估编码代理的性能 |

🎯 实验设置与评估指标
任务为训练编码代理，评估其在长周期编码与推理任务上的性能；论文未报告具体评估指标名称。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 现有agentic RL基线方法 | 编码代理训练的RLVR类方法 | 仅利用结果奖励或step-level奖励，无法深入探究代码diff，无法区分独立代码修改的贡献 |

3. 主要实验结果和性能指标
📊 定量结果汇总
无对应表号的具体定量表格内容如下：DiDPO在long-horizon coding and reasoning benchmarks上显著优于强agentic RL基线方法；在Qwen2.5-7B-Coder上，DiDPO超出可比方法10%以上，缩小了与更大模型的差距；论文未报告各实验对应的表号及详细定量数值。

各细分实验情况：
1. 主 benchmark 性能：论文未报告具体指标数值及对应表号
2. 效率对比：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：①DiDPO通过从代码diff结构构建细粒度信用单元，解决了编码代理训练中的细粒度信用分配挑战；②DiDPO在长周期编码和推理基准上显著优于现有agentic RL基线方法，在Qwen2.5-7B-Coder上性能提升10%以上，缩小了与更大模型的差距；③开源了支持多种RL方法和编码基准的agentic RL代码库verl-code。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：DiDPO是一种针对编码代理训练的无critic RL方法，通过代码diff结构构建细粒度信用单元解决细粒度信用分配问题，在长周期编码任务上性能优于现有方法，且开源了相关代码库。

</details>

---

### 4. [Every Cache Entry Earns Its Place: Global Allocation of Resolution and Coverage for KV Cache Compression](https://arxiv.org/abs/2608.07001v1)

**Authors**: Haolin Tian, Yuzhe Liu, Tonghan Wang  
**Category**: cs.LG  
**Published**: 2026-08-10  
**Score**: 64.5  
**Type**: new  
**ArXiv ID**: 2608.07001v1  

#### Abstract
As large language models (LLMs) process increasingly long contexts, KV cache storage and repeated access have become a major bottleneck. Existing KV cache compression methods rely on predefined, fixed compression rules and are typically developed around either token eviction or merging. As a result,...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Every Cache Entry Earns Its Place: Global Allocation of Resolution and Coverage for KV Cache Compression
1. 论文的主要贡献和创新点
✅ 解决的问题
现有KV缓存压缩方法依赖预定义的固定压缩规则，通常围绕token驱逐或合并技术开发，存在两大核心不足：一是缓存资源无法在层、KV头、上下文槽之间自由流动；二是无法联合分配资源以平衡局部分辨率与信息覆盖的需求。

🚀 提出的新方法与思路
**GraceKV**：将KV缓存压缩过程建模为固定缓存预算约束下的全局资源分配问题；把每层-KV头-槽组合定义为原子单元，构建原型树：叶节点对应token级KV条目，每个内部节点用单一原型压缩其所有子节点覆盖的KV空间；非重叠节点的集合构成原子单元的表示；新增树的根节点用于扩展信息覆盖，拆分选中节点可提升局部分辨率；所有候选操作（扩展根节点、拆分节点等）需全局竞争共享缓存预算，最终保留所有树中的节点形成压缩后的KV缓存；该方法可自适应地在原子单元间全局分配缓存资源，协调分辨率与覆盖的平衡，且无需额外训练，整个压缩和推理流程在GPU上执行。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 缓存资源调度 | 支持层、KV头、上下文槽间的全局自由流动，自适应平衡局部分辨率与信息覆盖 |
| 训练推理成本 | 无需额外训练，压缩及推理全程在GPU执行，降低额外开销 |
| 压缩鲁棒性 | 具备高鲁棒性，可承受128倍高压缩比仍保持性能 |
| 任务表现 | 在32组多样长上下文任务与压缩比设置中，多数场景（24组）表现最优 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：论文未明确报告具体的实验任务细节、评估指标名称及含义（仅提及针对多样长上下文任务开展实验）
⚔️ 基线方法对比：论文未报告具体的对比基线方法列表

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能**：论文未提供对应表号的具体定量结果表格，仅在摘要中提及：在32组多样长上下文任务与压缩比设置中，GraceKV有24组表现排名第一，且鲁棒性可达128倍压缩。
💡 结论：论文仅通过摘要说明GraceKV在多数长上下文任务及高压缩场景下性能优异且鲁棒，未提供对应表号的详细结论表格。
其他实验（效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）：论文未报告

4. 关键结论和发现
- 主要发现
1. 全局预算分配的KV缓存压缩机制可有效协调信息覆盖与局部分辨率的平衡；
2. GraceKV无需额外训练，推理时可在GPU上完成压缩流程，实用性较强；
3. GraceKV在多样长上下文任务中表现突出，且具备128倍高压缩比下的良好鲁棒性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

✅ **总结一句话**：GraceKV是一种基于全局资源分配的KV缓存压缩方法，无需额外训练，能在固定缓存预算下自适应协调信息覆盖与局部分辨率，在长上下文任务中表现优异且可承受高倍压缩，实用性与性能表现良好。

</details>

---

### 5. [Capek 0.5: An Execution-Centric Vision-Language Model for Embodied Intelligence](https://arxiv.org/abs/2608.06756v1)

**Authors**: Ying Chen, Weizhen Li, Zhe Hu, Zhenjiang Li, Rui Jiang, Zhifeng Gu, Lihuang Fang, Jiangping Liu, Lei Yi, Jie Chen  
**Category**: cs.AI  
**Published**: 2026-08-10  
**Score**: 57.5  
**Type**: new  
**ArXiv ID**: 2608.06756v1  

#### Abstract
Vision-language models are increasingly serving as the reasoning core of embodied agents. Robot execution is inherently iterative: each action reshapes the scene and physical state, continually renewing what must be perceived, reasoned about, and verified. Meeting these demands requires complementar...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Capek 0.5: An Execution-Centric Vision-Language Model for Embodied Intelligence
1. 论文的主要贡献和创新点
✅ 解决的问题
现有基于视觉语言模型的具身智能方法，通常针对孤立的、特定任务的目标开发不同能力，未围绕具身执行的迭代性（每次动作会改变场景与物理状态，需持续感知、推理、验证）的整体需求来组织和整合这些能力。

🚀 提出的新方法与思路
**执行中心的能力分类法**：将具身能力按执行过程中的功能角色划分为空间推理、时间理解、动作指导、状态验证四个能力族，替代按数据集或任务组织训练的思路，适配具身执行的动态性与迭代性。
**专家模型训练与整合策略**：每个能力族由专用专家模型通过强化学习训练，使用共享主干的可验证奖励；之后通过权重空间合并+路由策略空间蒸馏，将多个专家整合为单个推理时模型。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 能力组织逻辑 | 从按数据集/任务转为按执行功能角色组织，适配具身执行的迭代性、场景动态性 |
| 专家整合方式 | 通过权重空间合并+路由策略空间蒸馏，在形成统一推理模型的同时保留各专门化能力 |
| 评估覆盖范围 | 新增状态验证基准Capek-StateBench，从综合基准、能力保留、闭环执行三个互补视角全面评估 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Capek-StateBench | 论文提出的用于状态验证的新基准 |
| 综合基准套件 | 用于全面性能评估的配套基准 |

🎯 实验设置与评估指标
从综合基准性能、能力保留的受控研究、闭环具身环境执行三个互补视角评估模型表现，论文未报告具体评估指标的数值定义及对应表号、图号。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Capek 0.5初始化模型 | 初始基准模型 | 作为对比基准，用于验证合并后模型的性能提升 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告具体的量化指标数值及对应表号，仅提到Capek 0.5在大多数匹配基准行上优于其初始化模型。
2. 效率对比：论文未报告具体的效率指标及对应表号，仅提及模型实例化规模为2B和35B-A3B。
3. 跨域/zero-shot迁移：论文未报告相关具体实验及指标，仅提到模型可迁移至闭环具身任务执行。
4. 鲁棒性/扰动测试：论文未报告。
5. 消融实验：论文未报告。

4. 关键结论和发现
- 主要发现：① 围绕执行功能角色分类整合具身能力，可构建适配具身智能迭代执行需求的统一视觉语言模型；② 采用权重合并+路由策略蒸馏的整合方式，能从专用专家模型中保留全部四类专门化能力；③ 多维度评估框架可有效验证具身VLM的实际可用性。
- 方法局限性：论文未报告。
- 未来工作：论文未明确提及。

> ✅ **总结一句话**：Capek 0.5是首个围绕执行中心能力分类构建的具身视觉语言模型，通过专用专家模型的强化学习训练与整合策略，在多维度评估中优于初始模型，可完成闭环具身任务执行，适配具身智能的迭代执行需求。

</details>

---

### 6. [StateFlow: Sequence Pipeline Parallelism for Long-Context Modeling with Linear Recurrence](https://arxiv.org/abs/2608.06838v1)

**Authors**: Wenxuan Zhao, Yingfa Chen, Xu Han, Wenjing Han, Tianbo Huang, Zhiyu Li, Ao Sun, Jingheng Xu, Lin Gan, Guangwen Yang  
**Category**: cs.DC  
**Published**: 2026-08-10  
**Score**: 47.0  
**Type**: new  
**ArXiv ID**: 2608.06838v1  

#### Abstract
Long-context training is increasingly important for large language models, and linear attention and state space models have become popular for improving long-context efficiency. However, efficiently parallelizing long-sequence training for recurrent and hybrid models remains challenging.
  We presen...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：StateFlow: Sequence Pipeline Parallelism for Long-Context Modeling with Linear Recurrence

1. 论文的主要贡献和创新点
✅ 解决的问题
长上下文训练对大语言模型愈发重要，线性注意力与状态空间模型可提升长上下文效率，但循环及混合模型的长序列训练并行化仍存在困难。

🚀 提出的新方法与思路
**StateFlow** 是针对带线性循环模型的序列流水线并行系统，方案包括：将每个序列划分为多个块（chunk），调度块执行时在块间传递边界状态与梯度，以减少激活寿命、提升训练吞吐量；采用profile-guided非均匀分块策略，平衡混合模型中循环计算与softmax注意力计算；将暴露有限并行度的状态转换操作与周围计算重叠，优化整体效率。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 训练吞吐量 | 相比传统流水线并行可获得显著提升 |
| 内存占用 | 相比传统流水线并行可获得显著降低 |
| 配置可行性 | 支持原本不可行的大参数、长上下文模型配置 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
针对长上下文语言模型训练任务，评估指标为训练吞吐量（↑越高越好）、内存占用（↓越低越好），实验应用的模型规模为参数最高32B、上下文长度最高256K。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 传统流水线并行 | 并行方法 | 常规序列流水线并行策略 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表：长上下文模型训练性能对比（场景）**
| 指标 | 效果 |
|------|------|
| 训练吞吐量 | 论文未报告具体数值 |
| 内存占用 | 论文未报告具体数值 |
💡 结论：StateFlow应用于带线性循环的大参数、长上下文模型时，相较于传统流水线并行，在训练效率和内存占用方面具备潜在优势。
其他实验（主benchmark性能、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）：论文未报告

4. 关键结论和发现
- 针对带线性循环的长上下文语言模型训练，StateFlow解决了其并行化效率不足的核心问题，通过分块调度、计算平衡与资源重叠优化，提升训练效率。
- StateFlow可支持参数量达32B、上下文长度达256K的模型配置，实现传统方法无法支持的模型规模训练。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出StateFlow序列流水线并行系统，针对带线性循环的长上下文语言模型，通过分块调度、非均匀分块及计算重叠策略，可提升训练吞吐量、降低内存占用，支持传统方法无法实现的大参数、长上下文模型配置。

</details>

---

### 7. [DGEMM with Ozaki Scheme I/II on FP4 Tensor Cores: A Base-13 E2M1 Limb Representation](https://arxiv.org/abs/2608.06812v1)

**Authors**: Shun-ichiro Hayashi, Daichi Mukunoki, Tetsuya Hoshino, Takahiro Katagiri  
**Category**: cs.DC  
**Published**: 2026-08-10  
**Score**: 45.5  
**Type**: new  
**ArXiv ID**: 2608.06812v1  

#### Abstract
This paper proposes a method and its implementation for emulating FP64 matrix multiplication (DGEMM) by constructing, on FP4 (E2M1; 2 exponent bits and 1 mantissa bit) Tensor Cores, Ozaki schemes I and II, which realize high-precision matrix multiplication on low-precision arithmetic units. Prior im...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

DGEMM with Ozaki Scheme I/II on FP4 Tensor Cores: A Base-13 E2M1 Limb Representation
1. 论文的主要贡献和创新点
✅ 解决的问题
现有DGEMM实现基于INT8或FP8 Tensor Cores，未利用吞吐量为FP8两倍的FP4 Tensor Cores，无法在低精度单元上高效实现高精度矩阵乘法。
🚀 提出的新方法与思路
**Base-13 E2M1 Limb Representation Ozaki Scheme I/II**：利用FP4（E2M1）的核心性质——每个FP4值加倍后转换为整数，将整数集按13的倍数偏移覆盖所有整数，将任意整数转换为Base-13的FP4 limb表示；基于该表示，在FP4 Tensor Cores上实现Ozaki Scheme I和II，使FP4单元可用于高精度矩阵乘法，同时还能精确仿真INT8 Tensor Cores的整数GEMM。
🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 运算单元利用 | 首次利用FP4 Tensor Cores实现Ozaki Scheme I/II，FP4 Tensor Cores吞吐量是FP8的两倍 |
| 性能潜力 | 理论上Ozaki Scheme II在FP4上性能略高于FP8对应实现；实测在RTX PRO 6000 Blackwell的大问题规模（$16384^3$）下，性能超过现有FP8-based的Ozaki Scheme II实现 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标
任务为在FP4 Tensor Cores上实现Ozaki Scheme I/II的DGEMM，评估指标为矩阵乘法性能（吞吐量），方向为越高越好。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 基于INT8/FP8的Ozaki Scheme I/II实现 | 现有实现 | 未利用FP4 Tensor Cores的高吞吐量特性 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体实验表号、图号，仅明确：在RTX PRO 6000 Blackwell平台，针对Ozaki Scheme II的FP4实现，性能与现有FP8-based的Ozaki Scheme II实现相当，在大问题规模（$16384^3$）时超过后者；同时通过内核优化提升了峰值性能占比。
💡 结论：基于Base-13 E2M1 limb表示的Ozaki Scheme II FP4实现，在大问题规模下可超越现有FP8-based实现，内核优化有效提升了性能表现。

4. 关键结论和发现
- 主要发现：① 利用Base-13 E2M1 limb表示，可在FP4 Tensor Cores上实现Ozaki Scheme I/II及INT8整数GEMM的精确仿真；② FP4 Tensor Cores吞吐量为FP8的两倍，Ozaki Scheme II在FP4上的性能理论优于FP8实现，实测在大问题规模（$16384^3$）下超过现有FP8-based方案；③ 内核优化可提升FP4 Tensor Cores的峰值性能占比。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：本文提出基于Base-13 E2M1 limb表示的Ozaki Scheme I/II，首次在FP4 Tensor Cores上实现DGEMM，在RTX PRO 6000 Blackwell平台大问题规模下性能超越现有FP8-based实现，为低精度Tensor Cores实现高精度矩阵乘法提供了可行方案。

</details>

---

### 8. [IB-RL: Isolated Bilateral Reinforcement Learning for Strategic Dialogue Agents](https://arxiv.org/abs/2608.06735v1)

**Authors**: Senhao Wang, Chenghao Cai, Haitao Hu, Mingxing Huang, Xingguang Wang, Wenhao Li, Zecheng Lin  
**Category**: cs.AI  
**Published**: 2026-08-10  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2608.06735v1  

#### Abstract
Reinforcement learning (RL) has achieved strong results in improving large language models (LLMs) on tasks with stationary, verifiable rewards, such as mathematical reasoning and code execution. In these settings, the environment follows fixed rules and does not adapt strategically to the agent. Str...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# IB-RL: Isolated Bilateral Reinforcement Learning for Strategic Dialogue Agents
1. 论文的主要贡献和创新点
✅ 解决的问题：现有RL训练战略对话智能体时，采用固定对应智能体或模拟器的范式，会鼓励策略利用对应智能体的特定规律而非学习泛化到不同对应智能体的策略，该问题被称为静态对应智能体不匹配，论文已量化该问题。
🚀 提出的新方法与思路：**IB-RL（Isolated Bilateral Reinforcement Learning）**，核心是让战略对话的两个角色通过协同回合制训练实现共同演化，同时每个角色使用完全独立的优势函数、动作掩码和更新路径优化自身奖励，实现角色间的严格隔离优化。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 策略泛化能力 | 相比单边RL基线，在未见过的对应智能体上的泛化性能显著提升 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| Vehicle TeleSales | 用于Vehicle TeleSales领域的策略泛化评估 |
| Deal-or-NoDeal | 用于Deal-or-NoDeal领域的策略泛化评估 |
🎯 实验设置与评估指标：任务为评估冻结策略在两个战略对话领域对未见过对应智能体的泛化性能；指标如下：
| 指标 | 含义（箭头） |
| ---- | ---- |
| Success@1 | 对话成功比例，越高越好↑ |
| Agreement | 与对应智能体达成一致的比例，越高越好↑ |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 最优单边RL基线 | 单边RL训练方法 | 在固定对应智能体上训练，未实现角色优化隔离 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表（未报告）：Vehicle TeleSales vs Deal-or-NoDeal（战略对话泛化评估）**
| 方法 | Vehicle TeleSales: Success@1 | Deal-or-NoDeal: Agreement |
| ---- | ---- | ---- |
| 最优单边RL基线 | 84.6% | 86.4% |
| IB-RL | 89.6% ✅ | 98.4% ✅ |
💡 结论：IB-RL在Vehicle TeleSales和Deal-or-NoDeal两个战略对话任务上，对未见过对应智能体的泛化性能显著优于最优单边RL基线。
效率对比：论文未报告
跨域/zero-shot迁移：论文未报告
鲁棒性/扰动测试：论文未报告
消融实验：论文未报告

4. 关键结论和发现
- 现有单边RL训练范式存在静态对应智能体不匹配问题，导致策略无法有效泛化到未见过的对应智能体。
- IB-RL通过角色协同演化与独立优化的结合，有效解决了静态对应智能体不匹配问题。
- IB-RL在战略对话的两个基准任务上，对未见过对应智能体的性能优于最优单边RL基线。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：IB-RL通过将战略对话RL训练中的角色协同演化与独立优化相结合，解决了静态对应智能体不匹配问题，提升了策略对未见过对应智能体的泛化性能，在两个战略对话任务上优于现有单边RL基线方法。

</details>

---

### 9. [How Much, Then Where: Credit-Conserving Action-to-Token Allocation for Multi-Turn Agent Reinforcement Learning](https://arxiv.org/abs/2608.07118v1)

**Authors**: Lichao Ma, Yang Sun, Shuaitao Zhao, Yangyi Fang, Cong Qin, Xiaoliang Fu, Yuhang Tian, Yuchen Wei, Junbo Zhu, Yang Wei, Lu Pan, Jiaye Lin  
**Category**: cs.AI  
**Published**: 2026-08-10  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2608.07118v1  

#### Abstract
Credit assignment in multi-turn agent reinforcement learning operates at two levels: assigning trajectory-level credit to actions and distributing each action's credit across its tokens. In this paper, we introduce FACTOR, which separates these decisions. FACTOR uses checkpoint-calibrated TD residua...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

How Much, Then Where: Credit-Conserving Action-to-Token Allocation for Multi-Turn Agent Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
多回合智能体强化学习的信用分配需同时完成轨迹级动作信用分配、动作内token级信用分配两项任务；现有方法存在动作平均系数缺失导致token级符号翻转、动作代理权重依赖token长度等缺陷。

🚀 提出的新方法与思路
**FACTOR**，它分离轨迹级动作信用分配与动作内token信用分配两项决策：采用checkpoint-calibrated TD residuals为每个动作分配信用，使其 telescoping至轨迹优势；采用feedback-conditioned teacher-student likelihood gaps为每个动作的信用分配至已实现的动作token；引入per-action normalization保留动作平均系数，避免token级符号翻转；搭配action-mean reduction，消除动作的标量代理权重对其token长度的隐式依赖，使每个动作在行为策略裁剪前的内部动作均值代理等于其TD信用。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 两级信用分配 | 分离轨迹级动作信用分配与动作内token信用分配，分别处理两类信用任务 |
| token信用分配 | 防止token级符号翻转，消除动作代理权重对token长度的隐式依赖 |
| 泛化性 | 超参数可直接迁移至更大骨干网络及不同模型族 |
| 性能 | 在ALFWorld、WebShop、ScienceWorld三个环境的所有环境-种子设置下均优于竞争基线 |

2. 核心实验方法和设置
📚 使用的数据集
| 环境 | 用途 |
| ---- | ---- |
| ALFWorld | 多回合智能体强化学习实验环境1 |
| WebShop | 多回合智能体强化学习实验环境2 |
| ScienceWorld | 多回合智能体强化学习实验环境3 |

🎯 实验设置与评估指标
任务：多回合智能体强化学习任务
| 指标 | 含义（箭头方向） |
| ---- | ---- |
| 论文未报告 | 论文未报告具体评估指标及对应的优化方向 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| FACTOR | 本文提出方法 | 针对多回合智能体强化学习两级信用分配问题的新方法 |
| 竞争基线 | 对比方法 | 现有用于多回合智能体强化学习的信用分配方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体实验表格（无对应表号/图号）
💡 结论：论文提出的FACTOR方法在ALFWorld、WebShop、ScienceWorld三个多回合强化学习环境的所有环境-种子设置下均优于竞争基线，在长horizon环境中增益最大，且超参数具备良好的跨骨干、跨模型族泛化性。

4. 关键结论和发现
- 2-3 条主要发现
  1. FACTOR通过分离多回合智能体强化学习的轨迹级动作信用与动作内token信用分配任务，有效提升了算法性能；
  2. TD动作信用是FACTOR性能提升的核心驱动因素，hindsight token分配提供互补增益；
  3. FACTOR的超参数可迁移至更大骨干网络及不同模型族，泛化性良好。
- 方法局限性
论文未报告明确的方法局限性相关内容
- 未来工作
论文未报告明确的未来工作方向相关内容

> ✅ **总结一句话**：论文提出的FACTOR方法通过分离多回合智能体强化学习中轨迹级动作信用与动作内token信用的分配任务，解决了现有信用分配方法的缺陷，在多个多回合强化学习环境中实现了性能提升，且超参数具备良好的泛化性。

</details>

---

### 10. [When GNNs Fail: Quantifying and Overcoming Temporal Correlation Volatility in Time Series](https://arxiv.org/abs/2608.07333v1)

**Authors**: Chen Shao, Yue Wang, Zhenyi Zhu, Zhanbo Huang, Tobias K\"afer, Zonghan Wu, Danai Koutra  
**Category**: cs.LG  
**Published**: 2026-08-10  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2608.07333v1  

#### Abstract
Modeling multivariate time series by representing them as graphs, where individual series act as nodes and pairwise temporal corre- lations serve as edges, has gained significant traction. Recent advances in Graph Neural Networks (GNNs) have demonstrated strong perfor- mance by assuming a static gra...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

When GNNs Fail: Quantifying and Overcoming Temporal Correlation Volatility in Time Series
1. 论文的主要贡献和创新点
✅ 解决的问题
现有的用于多元时间序列预测的Graph Neural Networks (GNNs)及Transformer等模型，假设图拓扑（成对时间相关性）为静态，在图拓扑随时间剧烈变化的动态环境（即高Temporal Correlation Volatility (TCV)场景）下泛化性差、性能退化；诸多流行模型在高TCV场景下表现反而逊于简单的结构无关基线。

🚀 提出的新方法与思路
**Temporal Correlation Volatility (TCV)**：提出模型无关指标TCV，用于量化多元时间序列间潜在关联结构的分布演化，建立了TCV与模型性能退化的关联。
**Graph Layer for Inference in Dynamic Environments (GLIDE)**：提出新型GNN层，包含两个理论驱动的设计机制：1. **Path-based Message Passing**：捕获基于路径的邻域信息；2. **Static and Dynamic Propagation Separation**：通过局部静态近似确定最优动态传播方式，兼顾动态拓扑学习与静态场景鲁棒性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| TCV场景适应性 | 解决现有模型在高TCV多元时间序列预测场景下泛化性差的问题 |
| 静态场景鲁棒性 | 静态拓扑场景下保留模型原有性能 |
| 平均性能提升 | 跨静态和动态场景的平均性能提升最高达45.6% |
| 最大性能增益 | 跨静态和动态场景的最大性能增益达85.7% |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 合成基准数据集 | 验证GLIDE在动态与静态时间序列预测中的性能 |
| 真实世界基准数据集 | 验证GLIDE在动态与静态时间序列预测中的性能 |

🎯 实验设置与评估指标
任务为多元时间序列预测。论文未报告具体评估指标名称及对应箭头含义。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 现有流行模型（如Transformer） | GNN/Transformer类模型 | 假设图拓扑静态，高TCV场景下泛化性差 |
| 简单结构无关基线 | 结构无关方法 | 不依赖图拓扑，高TCV场景下表现优于部分现有模型 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未明确报告具体实验表格（如表N），仅提及：GLIDE在合成与真实世界基准上，跨静态和动态设置的平均性能提升最高达45.6%，最大增益达85.7%。
💡 结论：GLIDE在静态与动态多元时间序列预测场景下均能为模型带来显著性能提升。
（其余实验如效率对比、跨域迁移、鲁棒性测试、消融实验等，论文未明确报告具体内容）

4. 关键结论和发现
- 主要发现1：GNN、Transformer等现有模型在高TCV多元时间序列预测场景下泛化性差，常被简单的结构无关基线超越。
- 主要发现2：TCV是可有效量化多元时间序列潜在关联结构分布变化的模型无关指标，与模型性能退化存在明确关联。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：本文提出量化时间序列关联结构分布演化的TCV指标与适配动态拓扑的GLIDE GNN层，解决了现有模型在高TCV多元时间序列预测中的性能退化问题，兼顾了静态场景的鲁棒性。

</details>

---

### 11. [Cascade: Exploiting SLO-Aware latency budget for fair and high goodput LLM inference serving](https://arxiv.org/abs/2608.06557v1)

**Authors**: Muhammad Adnan, Rohan Mahapatra, Prashant J. Nair, Daniel Berger, Pantea Zardoshti, Rodrigo Fonseca, Esha Choukse  
**Category**: cs.DC  
**Published**: 2026-08-10  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2608.06557v1  

#### Abstract
The reasoning and agentic capabilities of large language models have expanded the range of applications they support, from short interactive exchanges to long, compute-heavy requests. LLM serving platforms today define response-latency service-level objectives, even though requests within the same s...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Cascade: Exploiting SLO-Aware latency budget for fair and high goodput LLM inference serving
1. 论文的主要贡献和创新点
- 解决的问题：现有LLM serving平台针对同一服务级目标（SLO）的请求，未考虑请求间输入长度、生成长度、执行成本、KV缓存状态的巨大差异，导致相同SLO下请求存在不同的延迟余量（延迟预算）；此前的SLO感知调度器仅用deadline进行请求排序，未联合处理调度与内存管理的问题。
- 提出的新方法与思路
**SLO-Aware Per-Request Latency Budget**：Cascade方法定义并估计每请求的延迟预算（即SLO与请求预测剩余服务时间的差值），该预算结合请求特征、KV缓存状态与当前系统负载生成；在此基础上，Cascade的调度器依据请求剩余预算排序，优先处理预算不足的请求；内存管理器利用该预算决定非驻留KV状态的策略，包括从深层存储恢复/预取、保留在HBM或重计算。
- 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 调度与内存管理方式 | 联合优化请求调度与KV缓存管理，而非仅依赖deadline排序 |
| SLO满足度 | 降低SLO违规比例 |
| 系统性能 | 提升满足SLO的goodput |
| 公平性 | 保留不同请求类别的公平性 |
2. 核心实验方法和设置
- 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 三个大语言模型的生产轨迹 | 评估Cascade的LLM inference serving性能 |
- 实验设置与评估指标
任务：LLM推理 serving的性能评估；指标及含义：
| 指标 | 含义 |
| ---- | ---- |
| SLO违规率 | 衡量请求未满足SLO的比例，↓ 越低越好 |
| goodput | 单位时间内满足SLO的请求处理量，↑ 越高越好 |
- 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| vLLM默认FCFS调度器 | 基线方法 | 采用先来先服务的默认调度策略，无SLO感知的延迟预算机制 |
3. 主要实验结果和性能指标
- 定量结果汇总：论文未报告具体的表号、图号或实验数据来源，仅在摘要中提及趋势：在三个大语言模型的生产轨迹上，Cascade相较于vLLM默认FCFS调度器，goodput提升最多2.4x，SLO违规减少40%
💡 结论：在生产环境的真实请求轨迹下，Cascade相较基线调度器实现了显著的性能提升
4. 关键结论和发现
- 主要发现：① SLO感知的每请求延迟预算可有效指导LLM serving的请求调度与KV缓存管理；② Cascade在多组大语言模型生产轨迹上，较vLLM FCFS调度器获得明显的性能增益；③ Cascade可在提升系统性能的同时保持不同请求类别的公平性
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：Cascade通过引入SLO感知的每请求延迟预算，联合优化LLM推理的请求调度与KV缓存管理，在保证公平性的前提下提升满足SLO的goodput并减少SLO违规，性能优于vLLM默认FCFS调度器。

</details>

---

### 12. [AgentPatch: Coarse-to-Fine Weak-Task Repair for Merging Agentic Multimodal Large Language Models](https://arxiv.org/abs/2608.06699v1)

**Authors**: Zibo Shao, Baochen Xiong, Chengdong Xu, Linhui Xiao, Kaichen Li, Haoran Gong, Yan Li, Yaguang Song, Xiaoshan Yang  
**Category**: cs.AI  
**Published**: 2026-08-10  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.06699v1  

#### Abstract
Agentic multimodal large language models (MLLMs) extend multimodal perception and reasoning with planning, tool use, and interaction in dynamic environments. Yet current models are specialized for particular tools or environments, complicating consolidation into a single generalist. We formulate Age...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# AgentPatch: Coarse-to-Fine Weak-Task Repair for Merging Agentic Multimodal Large Language Models
## 1. 论文的主要贡献和创新点
✅ 解决的问题
代理多模态大语言模型（Agentic MLLMs）拓展了多模态感知、推理、规划及工具使用能力，但现有模型多针对特定工具或环境设计，合并为单一通用模型时存在两大痛点：一是不对称能力保留，不同交互复杂度的能力留存不均，产生弱任务性能退化；二是行为关键遗忘，合并过程中丢失关键决策动作会干扰长周期执行。

🚀 提出的新方法与思路
**AgentPatch框架**：一种无需训练的粗到细修复框架，流程为：1）选择稳定的合并后主干模型；2）通过Weak-Task Unique Residual Recovery恢复被稀释的弱任务专属信号；3）应用Agent-Guided Behavior-Critical Patch，在明确的能力保护下恢复关键行为，生成无路由或集成的单一静态检查点。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 弱任务性能 | 缓解合并后的模型出现的弱任务性能退化 |
| 模型结构 | 生成单一静态检查点，无需路由或集成模块 |
| 能力平衡 | 更好平衡弱任务恢复与互补的搜索、代理视觉处理能力 |

## 2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 六组代理和多模态基准 | 测试AgentPatch的性能 |

🎯 实验设置与评估指标
论文未报告具体任务细节与评估指标。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 论文未报告 | 论文未报告 | 论文未报告 |

## 3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告包含表号、图号的具体实验定量数值及详细结果，仅摘要提及在六组代理和多模态基准上的定性结论。
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

## 4. 关键结论和发现
- 主要发现：1. AgentPatch作为无需训练的修复框架，可改善多种合并后Agentic MLLM主干的性能；2. AgentPatch能有效缓解合并模型的弱任务性能退化；3. AgentPatch可平衡弱任务恢复与互补的搜索、代理视觉处理能力。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：AgentPatch是一种无需训练的粗到细修复框架，用于将针对特定工具或环境优化的Agentic MLLMs合并为单一通用模型，缓解合并过程中的弱任务退化与关键行为遗忘问题，实现多方面能力的平衡。

</details>

---

### 13. [Retention-Aware RISC-V ISA Extension and Memory Controller on FPGA for MLC NVM](https://arxiv.org/abs/2608.06725v1)

**Authors**: Mina Ibrahim, Martel Shokry, Lokesh Siddhu, Lars Bauer, Hassan Nassar, Joerg Henkel  
**Category**: cs.AR  
**Published**: 2026-08-10  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.06725v1  

#### Abstract
Non-volatile memory (NVM) technologies, particularly Multi-Level Cell (MLC) NVMs, offer significant potential for increasing memory density. MLC NVMs provide a tradeoff between write latency and retention time, where faster writes/stores result in lower retention and slower writes yield higher reten...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Retention-Aware RISC-V ISA Extension and Memory Controller on FPGA for MLC NVM
1. 论文的主要贡献和创新点
✅ 解决的问题
MLC NVM在写延迟和保留时间之间存在权衡，但现有工作很少在系统层面利用该权衡验证和原型化基于NVM的系统，无法兼顾写性能与数据可靠性。
🚀 提出的新方法与思路
**Retention-Aware Custom NVM Controller**：基于有限状态机（FSM）设计，带有AXI内存映射接口，通过增强突发传输高效管理读写操作，减少延迟。
**Fast-Store RISC-V Instruction Extension**：新增Fast-Store指令，在提升写性能的同时，解决MLC NVM的保留限制。
**Bit-Significance-Aware AXI Slave Peripheral**：支持按位重要性的写操作，将关键位（如MSBs）用慢速高保留写入，非关键位（如LSBs）用快速低保留写入，在不损害数据可靠性的前提下优化性能。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 硬件开销 | 自定义NVM控制器相比传统设计减少30% |
| 流式工作负载写性能 | Fast-Store指令提升性能超过7%，硬件开销低于0.08% |
| AXI外设LUT利用率 | 64x64矩阵时低于3.5%，32x32尺寸下低于1%，适合集成至更大的SoC |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |
🎯 实验设置与评估指标
任务：优化MLC NVM的写操作，平衡写速度与数据保留时间。
| 指标 | 含义 |
| --- | --- |
| 硬件开销 | 衡量额外增加的硬件资源占用，↓越低越好 |
| 流式工作负载写性能 | 衡量写操作的执行效率，↑越高越好 |
| AXI外设LUT利用率 | 衡量外设的资源消耗，↓越低越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 传统NVM控制器 | 基线方法 | 常规NVM读写操作处理架构，无Retention-Aware优化、RISC-V指令扩展及位级写支持 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能**
论文未报告
**效率对比**
论文未报告
**跨域 / zero-shot 迁移**
论文未报告
**鲁棒性 / 扰动测试**
论文未报告
**消融实验**
论文未报告
💡 结论：提出的Retention-Aware方案有效降低NVM系统的硬件开销，提升写性能，且位级AXI外设资源占用低，具备SoC集成可行性。
4. 关键结论和发现
- 主要发现：1. 基于FSM的Retention-Aware自定义NVM控制器可显著减少硬件开销；2. Fast-Store指令在流式工作负载下大幅提升写性能，硬件开销极低；3. 位级AXI外设的LUT资源消耗低，可集成至大型SoC。
- 方法局限性
论文未报告
- 未来工作
论文未报告

> ✅ **总结一句话**：论文针对MLC NVM写延迟与保留时间的权衡痛点，提出Retention-Aware RISC-V ISA扩展、自定义NVM控制器及位级AXI外设，经FPGA原型验证，可有效降低硬件开销、提升写性能，且外设资源占用低可集成至大型SoC。

</details>

---

### 14. [Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing](https://arxiv.org/abs/2608.07437v1)

**Authors**: Jiacheng Miao, Jin Mu, Guanhua Chen, James Zou  
**Category**: cs.AI  
**Published**: 2026-08-10  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2608.07437v1  

#### Abstract
Reliable hypothesis testing is the foundation of many empirical scientific claims. Large language model (LLM) agents are increasingly used to automate this process, as they can inspect datasets, generate code, and produce analyses end-to-end. However, we show that they frequently make subtle inferen...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing
1. 论文的主要贡献和创新点
✅ 解决的问题
现有用于自动化假设检验的LLM代理常出现细微推理错误（即使分析执行正确也会得出错误结论）；现有基准无法捕捉该故障模式，极少评估报告的p值是否符合数据背后的统计假设。

🚀 提出的新方法与思路
**Fisher-R1**：一种用于严格假设检验的开放权重LLM代理，采用合成任务与强化学习方法进行训练，用于解决假设检验中的可靠统计推理问题。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 任务可靠性 | 解决了现有LLM代理在假设检验中易出现的细微统计推理错误 |
| 基准评估 | 构建了覆盖多领域的P-Bench基准，可有效评估LLM代理在假设检验中的统计有效性 |
| 模型性能 | 在P-Bench基准上优于多个强基线（包括GPT-5.4、DeepSeekV4-Pro） |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| P-Bench | 包含425个跨经济学、生物学、医学领域的开放、现实假设检验任务，用于测试LLM代理的假设检验能力 |

🎯 实验设置与评估指标
任务要求：代理仅根据给定的科学假设和数据集，完成统计方法选择、p值计算、结论输出的全流程。
| 指标 | 含义 |
| ---- | ---- |
| 单试验成功率 | 衡量代理完成假设检验任务的成功比例，越高越好 |
| 平均相对改进 | 与对比基线相比，单试验成功率的提升比例，越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| GPT-5.4 | 专有LLM模型 | 对比的强基线模型 |
| DeepSeekV4-Pro | 开放/专有混合模型 | 对比的强基线模型 |
| Fisher-R1-14B的Backbone | LLM模型 | 训练Fisher-R1的基础模型 |
| Fisher-R1-14B | 提出的新模型 | 基于合成任务与强化学习训练的开放权重LLM代理，专门用于可靠假设检验 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能**（P-Bench场景）
论文未报告对应表号，根据论文摘要内容整理结果如下：
| 方法 | 单试验成功率相对改进（vs DeepSeek-V4-Pro） | 最具挑战性任务的相对改进（vs DeepSeek-V4-Pro） |
| ---- | ---- | ---- |
| Fisher-R1-14B | 21% ✅ | 26% ✅ |
| DeepSeek-V4-Pro | - | - |
| GPT-5.4 | 未明确报告具体数值 | 未明确报告具体数值 |
💡 结论：在P-Bench基准上，Fisher-R1-14B的单试验成功率相较于DeepSeek-V4-Pro平均提升21%，在最具挑战性任务上提升达26%，性能优于对比基线模型。

其他实验（效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）：论文未报告

4. 关键结论和发现
- 主要发现：① 当前LLM代理在假设检验任务中存在可靠统计推理能力不足的问题；② 结合合成任务与强化学习训练的Fisher-R1，能显著提升假设检验任务的可靠性；③ 经验证的统计奖励指导的强化学习可有效改进LLM代理的统计推理性能。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：Fisher-R1是经合成任务与强化学习训练的开放权重LLM代理，在新构建的多领域P-Bench基准上大幅提升了假设检验的可靠统计推理能力，表现优于包括GPT-5.4、DeepSeekV4-Pro在内的现有基线模型。

</details>

---

### 15. [Sub-Quadratic Bisimulation Metrics via Approximate Nearest Neighbors: Coverage-Augmented Guarantees and Computable Two-Sided Certificates](https://arxiv.org/abs/2608.06762v1)

**Authors**: Ibne Farabi Shihab, Joyanta Jyoti Mondal  
**Category**: cs.LG  
**Published**: 2026-08-10  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2608.06762v1  

#### Abstract
Bisimulation metrics quantify behavioral similarity in Markov decision processes, but their Wasserstein fixed-point operator updates every state pair and incurs quadratic pairwise work. We give a certificate-carrying sub-quadratic method for MDPs with bounded transition support and a useful low-dime...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Sub-Quadratic Bisimulation Metrics via Approximate Nearest Neighbors: Coverage-Augmented Guarantees and Computable Two-Sided Certificates
1. 论文的主要贡献和创新点
✅ 解决的问题
现有的bisimulation metrics在马尔可夫决策过程（MDP）中计算时，Wasserstein固定点算子需要更新每一对状态，带来二次计算开销；现有方案存在子二次复杂度缺失、全局误差难以控制（未覆盖对保留初始化差距）、缺乏可计算双侧证书等痛点。

🚀 提出的新方法与思路
**Approximate Nearest Neighbor Index Selection**：利用近似最近邻索引选择由精确受限算子更新的状态对，减少需更新的状态对数量，从而降低计算的时间复杂度。
**Monotone Lower and Upper Runs**：通过单调递增的下界序列和单调递减的上界序列，在每一轮迭代中包围精确的bisimulation metric，形成可计算的双侧证书，无需依赖未知的精确metric即可得到误差相关的边界。
**Coverage-Augmented Anytime Bound**：提出的分析结论表明，局部索引的质量无法单独控制全局误差，未覆盖的状态对会保留其初始化的差距；全局误差的上限为$\max(\rho,\varepsilon/(1-\gamma))$（$\rho$依赖未知的精确bisimulation metric）；算法返回可观测的三明治宽度（上下界的差值），诱导的下界聚类和上界聚类的一致性可证明覆盖聚合的精确恢复。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 计算复杂度 | 从二次（$O(|\Scal|^2)$）降为子二次，大幅降低计算开销 |
| 误差控制 | 提供带覆盖增强保证的任何时间误差边界，明确未覆盖对的误差影响 |
| 证书可计算性 | 无需依赖未知精确metric，通过三明治宽度提供可计算的双侧误差证书 |
| 性能效率 | 当覆盖足够的状态对时，可快速逼近精确bisimulation metric的性能上限 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| grouped $|\Scal|=64$ benchmark | 主benchmark性能对比实验 |
| Taxi | 证书可用性测试（嵌入信息不足时的证书表现） |
| 2500-state gridworld | 算法性能与计算开销收益对比实验 |

🎯 实验设置与评估指标
任务：在离散状态MDP环境中计算bisimulation metrics，评估相关性能指标。
| 指标 | 含义 |
| ---- | ---- |
| 与精确bisimulation metric的差距 | ↓ 越低越好 |
| 计算复杂度缩放（时间） | ↓ 越低越好 |
| 证书abstention次数 | ↓ 越少越好 |
| 性能收益（与reward-only metric对比） | ↑ 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| MICo | 基准方法 | 独立训练的基线方法 |
| DBC | 基准方法 | 独立训练的基线方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能（grouped $|\Scal|=64$ benchmark）**
精确受限精化在检索覆盖约一半状态对时，达到了精确bisimulation metric的性能上限；独立训练的MICo和DBC基线在所有检索预算下，性能高于该上限。
💡 结论：本方法的精确受限精化在覆盖部分状态对时即可逼近精确metric性能，显著优于现有基线方法。

**效率对比（时间实验）**
论文未提供具体时间数值，仅提到时间实验验证了本方法具有子二次复杂度，原方法（Wasserstein固定点算子）为二次复杂度。
💡 结论：本方法实现了从二次到子二次的计算复杂度缩放，大幅降低计算开销。

**跨域 / zero-shot 迁移**
论文未报告
**鲁棒性 / 扰动测试**
论文未报告
**消融实验**
论文未报告

4. 关键结论和发现
- 主要发现：1. 本方法通过近似最近邻索引选择更新对+单调上下界迭代，实现了子二次bisimulation metrics计算，同时提供可计算的双侧误差证书，明确了未覆盖对的误差影响；2. 在主benchmark中，本方法的精确受限精化在覆盖部分状态对时即可达到精确metric的性能，显著优于MICo和DBC基线；3. 在2500-state gridworld任务中，本方法用少量计算资源实现了优于reward-only metric的性能。
- 方法局限性：当嵌入信息不充分时，误差证书会abstain（如Taxi环境的表现）；依赖近似最近邻索引的质量，局部索引质量无法单独控制全局误差。
- 未来工作：优化近似最近邻索引的覆盖质量，减少未覆盖对带来的误差影响；进一步降低证书abstain的场景。

> ✅ **总结一句话**：本论文提出了一种带可计算双侧证书的子二次bisimulation metrics计算方法，通过近似最近邻索引和单调上下界迭代，在MDP环境中实现了计算复杂度的降低和性能的提升。

</details>

---

### 16. [Multi-Perspective Triad Interaction Graph Neural Network for Cognitive Distortion Detection](https://arxiv.org/abs/2608.06785v1)

**Authors**: Jun Seo Kim, Hye Hyeon Kim  
**Category**: cs.CL  
**Published**: 2026-08-10  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2608.06785v1  

#### Abstract
Cognitive distortion detection is a key task in computational mental health, yet existing approaches often overlook the psychological structure of distorted thoughts. We propose MTI-GNN (Multi-Perspective Triad Interaction Graph Neural Network), which models Beck's cognitive triad---negative views o...

---

### 17. [Rethinking Unified Memory for NPU-PIM Systems: Dual-View Memory for Dynamic Inference of LLM](https://arxiv.org/abs/2608.06989v1)

**Authors**: Shixin Zhao, Lian Liu, Tianhua Han, Mengdi Wang, Yinhe Han, Ying Wang  
**Category**: cs.AR  
**Published**: 2026-08-10  
**Score**: 28.0  
**Type**: new  
**ArXiv ID**: 2608.06989v1  

#### Abstract
Heterogeneous architectures that combine neural processing unit (NPU) and processing-in-memory (PIM) are increasingly adopted to accelerate LLM inference. Prior work focuses on building a unified memory that allows NPUs and PIM to share data without duplication. However, these designs implicitly ass...

---

### 18. [MiCoPro: End-to-End Mixed Precision HW/SW Co-design with HW-aware Proxy Model](https://arxiv.org/abs/2608.06916v1)

**Authors**: Zijun Jiang, Yangdi Lyu  
**Category**: cs.LG  
**Published**: 2026-08-10  
**Score**: 27.0  
**Type**: new  
**ArXiv ID**: 2608.06916v1  

#### Abstract
Quantized Neural Networks~(QNN) with low-bitwidth data have proven promising in efficient storage and computation on edge devices. To mitigate accuracy degradation while maximizing speedup, layer-wise mixed-precision quantization~(MPQ) becomes a popular solution. However, existing algorithms for exp...

---

### 19. [WNM-3D: A World Navigation Model with 3D Scene Conditioning for Closed-Loop VLN](https://arxiv.org/abs/2608.07267v1)

**Authors**: Yuehao Huang, Yunzi Wu, Xiaotao Zhang, Xinhai Li, Jiankun Dong, Jiajun Lv, Chi Zhang, Chenjia Bai, Yong Liu, Xuelong Li  
**Category**: cs.AI  
**Published**: 2026-08-10  
**Score**: 26.5  
**Type**: new  
**ArXiv ID**: 2608.07267v1  

#### Abstract
Recent vision-language navigation (VLN) systems increasingly adapt pretrained vision-language models (VLMs) into vision-language-action (VLA) policies that map egocentric observations and language instructions directly to navigation actions. Although semantically capable, such action-centric trainin...

---

### 20. [Transformers Struggle to Use Their Emergent World Models: Revisiting the Tower of Hanoi, and the Illusion of Thinking](https://arxiv.org/abs/2608.07077v1)

**Authors**: Devin Pereira, Willem Zuidema  
**Category**: cs.AI  
**Published**: 2026-08-10  
**Score**: 26.0  
**Type**: new  
**ArXiv ID**: 2608.07077v1  

#### Abstract
The Tower of Hanoi is a simple planning puzzle that in prior work has proven challenging for large reasoning models (LRMs). Current models solve the standard formulation of the puzzle, but still struggle with the flat-to-flat variant (where initial and goal states are not restricted to have all ring...

---

### 21. [Learning to Predict Middle-Layer Attention in MLLMs for Visual Token Prunin](https://arxiv.org/abs/2608.06411v1)

**Authors**: Yuyao Sun, Tao Deng, Shuang Li, Deqing Wang, Hao Geng, Minjun Yu  
**Category**: cs.AI  
**Published**: 2026-08-10  
**Score**: 25.5  
**Type**: new  
**ArXiv ID**: 2608.06411v1  

#### Abstract
Multimodal large language models (MLLMs) achieve strong performance across diverse vision-language tasks, but their efficiency is limited by the cost of processing numerous visual tokens. Visual token pruning can reduce this cost, but requires accurate token importance estimates. Recent studies have...

---

### 22. [Beyond Myopic World Models: Long-Horizon End-to-End Training for Direct Future Prediction](https://arxiv.org/abs/2608.07420v1)

**Authors**: Xinyi Li, Zaishuo Xia, Chenjie Hao, Yubei Chen  
**Category**: cs.LG  
**Published**: 2026-08-10  
**Score**: 25.5  
**Type**: new  
**ArXiv ID**: 2608.07420v1  

#### Abstract
World models are expected to support imagination over extended temporal horizons, yet most are still trained through local few-step prediction objectives and deployed by recursively rolling out their own predictions. This creates a fundamental mismatch: few-step losses optimize local transition fide...

---

### 23. [TaskSense: Focusing on What Matters in World Models](https://arxiv.org/abs/2608.06544v1)

**Authors**: SM Mazharul Islam, Manfred Huber  
**Category**: cs.AI  
**Published**: 2026-08-10  
**Score**: 25.0  
**Type**: new  
**ArXiv ID**: 2608.06544v1  

#### Abstract
World models for visual control typically learn compact latent states by reconstructing observations, implicitly encouraging representations to preserve information across the entire visual input. However, task-relevant content often occupies only a small fraction of the observation, while backgroun...

---

### 24. [An AI4AI Framework for Visual Token Pruning](https://arxiv.org/abs/2608.07193v1)

**Authors**: Zhen Liu, Wenli Huang, Wei Song, Yuhan Liu, Zhiqin Yang, Jingwen Fu  
**Category**: cs.LG  
**Published**: 2026-08-10  
**Score**: 25.0  
**Type**: new  
**ArXiv ID**: 2608.07193v1  

#### Abstract
Visual-token pruning can substantially reduce the inference cost of multimodal large language models (MLLMs), yet existing methods largely rely on fixed, handcrafted heuristics and costly expert trial and error. As pruning objectives, budgets, and model architectures diversify, manually navigating t...

---

### 25. [Interpretable Unsupervised Community Detection with LLM-Symbolized Structured Processes](https://arxiv.org/abs/2608.06402v1)

**Authors**: Aoting Zeng, Kai Wang, Jianwei Wang, Yuxiang Sun, Yizhang He, Wenjie Zhang  
**Category**: cs.AI  
**Published**: 2026-08-10  
**Score**: 24.5  
**Type**: new  
**ArXiv ID**: 2608.06402v1  

#### Abstract
Community detection is a fundamental task in graph analytics that aims to identify cohesive groups of entities with similar behaviors or interests. Classic objective-driven methods struggle with complex graph structures, while deep-learning approaches improve performance at the expense of interpreta...

---

### 26. [Shape Your Feed: An LLM-based Agentic System for Conversational Recommendation](https://arxiv.org/abs/2608.06632v1)

**Authors**: Ziyun Xu, Bosen Ding, Yue Zhang, Ji Qi, Qingyuan Song, Jizhou Huang, Liwei Wang, Jefferey Santelli, Yue Weng, Qichao Que, Zhenheng Yang, Junfeng Pan, Linhong Zhu  
**Category**: cs.AI  
**Published**: 2026-08-10  
**Score**: 24.5  
**Type**: new  
**ArXiv ID**: 2608.06632v1  

#### Abstract
Industrial recommendation systems predominantly adopt a passive ranking paradigm that infers user preferences from implicit behavioral signals (e.g., clicks, dwell time) rather than explicit, natural language inputs. As a result, users experience a persistent discrepancy between their explicit inter...

---

### 27. [Solver-Guided Reasoning for Mixed-Equilibrium Strategies](https://arxiv.org/abs/2608.06741v1)

**Authors**: Han Wang, Philippe Beardsell, Boning Li, Aaron Sasmita, Shuai Li, Hongyuan Zha, Baoxiang Wang  
**Category**: cs.LG  
**Published**: 2026-08-10  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2608.06741v1  

#### Abstract
Reasoning in large language models (LLMs) is often grounded in human text, human demonstrations, and human-generated rationales. For equilibrium reasoning in complex games, however, relying on human data can be suboptimal. In fact, human play is often guided by intuition and heuristics and can devia...

---

### 28. [MARS: A Monte Carlo Tree Search-based Adaptive and Responsive Scheduler](https://arxiv.org/abs/2608.06629v1)

**Authors**: Yash Kurkure, Yihe Zhang, Zhiling Lan, Michael E. Papka  
**Category**: cs.DC  
**Published**: 2026-08-10  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2608.06629v1  

#### Abstract
Modern High Performance Computing systems depend on static heuristics and manual administration for job scheduling and reservation management. Deep Reinforcement Learning (DRL) has shown promising scheduling performance but requires historical training data and fixes the optimization goal at trainin...

---

### 29. [Conformal Fusion Under Missing Modalities](https://arxiv.org/abs/2608.07183v1)

**Authors**: Alireza Moayedikia  
**Category**: cs.LG  
**Published**: 2026-08-10  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2608.07183v1  

#### Abstract
Multimodal fusion architectures typically assume all modalities are available at inference, yet sensor failures, acquisition variability, and cost constraints routinely produce incomplete observations. Existing work treats modality absence as a prediction-accuracy problem, leaving a more basic quest...

---

### 30. [KNOWPLAN: Knowledge-Driven AI Agents for Smart Degree Pathway Planning](https://arxiv.org/abs/2608.06530v1)

**Authors**: Shuheng Cao, Weijia Zhang, Jiaqi Wu, Xiyun Hu, Yat Yang, Juqy Chen, Zhaoxiang Feng  
**Category**: cs.AI  
**Published**: 2026-08-10  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2608.06530v1  

#### Abstract
Planning a degree from official university sources requires solving two problems in order. The institution's curriculum must first be reconstructed from catalogs, departmental pages, JSON endpoints, and PDFs that share no schema, and only then can a student-specific path be optimized under prerequis...

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
