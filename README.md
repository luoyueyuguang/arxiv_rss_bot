# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-07-28 08:46:11 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [MM-ShiftKV: Decode-Aware Prefill-Stage KV Selection for Multimodal Large Language Models](https://arxiv.org/abs/2607.22586v1)

**Authors**: Jinsong Shu, Chenyang Wu, Zhongle Xie, Baokun Wang, Lidan Shou  
**Category**: cs.AI  
**Published**: 2026-07-28  
**Score**: 108.5  
**Type**: new  
**ArXiv ID**: 2607.22586v1  

#### Abstract
Key-Value (KV) caching is essential for efficient inference in multimodal large language models (MLLMs), yet its memory footprint grows linearly with context length and becomes a major bottleneck due to the large number of visual tokens. Recent prefill-stage KV selection methods estimate KV importan...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

MM-ShiftKV: Decode-Aware Prefill-Stage KV Selection for Multimodal Large Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题
现有prefill-stage KV选择方法假设prefill阶段的查询可代表解码阶段的查询，该假设在多模态大型语言模型（MLLMs）场景下失效——MLLM的解码阶段查询方差远大于prefill阶段，导致KV重要性估计在严格缓存预算下不稳定，微小的排序误差会错误丢弃语义关键的视觉token，进而降低模型的grounding和推理性能，成为MLLM高效推理的瓶颈之一。

🚀 提出的新方法与思路
**Decode-Aware Prefill-Stage KV Selection（MM-ShiftKV）**：这是一种训练-free且严格仅在prefill阶段运行的KV选择方法。它通过构造方差扩展的查询代理，在prefill阶段近似解码阶段的查询行为，进而基于这些代理的聚合注意力质量来估计提示的KV重要性，无需额外训练开销，适配多模态场景的查询特性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| KV重要性估计稳定性 | 针对多模态场景下prefill与解码查询特性不匹配的问题，提升了严格缓存预算下的KV重要性估计精度 |
| 运行与训练特性 | 仅在prefill阶段执行，且为训练-free方法，无额外训练或推理阶段的开销 |
| 性能表现 | 在严格KV缓存预算约束下，相比现有prefill-stage KV选择方法性能更优 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 多模态基准数据集 | 验证MM-ShiftKV的多模态任务性能（论文未报告具体数据集名称） |

🎯 实验设置与评估指标
针对多模态大型语言模型（MLLMs）的预填充阶段KV选择优化，在严格KV缓存预算约束下评估模型的grounding与推理任务性能。
| 指标 | 含义 |
| --- | --- |
| 多模态任务性能（含grounding、推理） | 越高越好（↑）（论文未报告具体指标名称及数值） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 现有prefill-stage KV选择方法 | KV缓存优化方法 | 假设prefill阶段查询代表解码阶段查询，在多模态场景下存在估计不稳定问题（论文未报告具体基线名称及详细特性） |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体的定量实验数据、表号、图号、消融实验、跨域迁移、鲁棒性测试等详细实验结果，仅提及在多模态基准上MM-ShiftKV在严格KV缓存预算下持续优于现有方法。

4. 关键结论和发现
- 主要发现：1. 多模态大型语言模型的解码阶段查询方差显著大于prefill阶段，现有prefill-stage KV选择方法的核心假设（prefill查询等价于解码查询）在该场景下失效，导致KV重要性估计不稳定，损害模型性能；2. 提出的MM-ShiftKV方法通过构造方差扩展的查询代理近似解码查询行为，解决了上述假设失效问题，在严格KV缓存预算下性能优于现有方法。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：MM-ShiftKV是一种训练-free、仅在预填充阶段运行的KV选择方法，通过构造方差扩展的查询代理近似多模态大型语言模型的解码查询行为，解决了现有方法因假设失效导致的KV重要性估计不稳定问题，在严格KV缓存预算下表现优于现有方法。

</details>

---

### 2. [xMIx: High-Performance Serving-Time Platform for Mechanistic Interpretability Apps](https://arxiv.org/abs/2607.22595v1)

**Authors**: Michael Blum, Mark Silberstein, Yaniv David  
**Category**: cs.AI  
**Published**: 2026-07-28  
**Score**: 76.0  
**Type**: new  
**ArXiv ID**: 2607.22595v1  

#### Abstract
Mechanistic interpretability (MI) has emerged as a powerful approach for analyzing and intervening in inference computations, with a growing number of applications such as jailbreak attempt detection, truthfulness evaluation, and hallucination detection. Unfortunately, MI deployment in production mo...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

xMIx: High-Performance Serving-Time Platform for Mechanistic Interpretability Apps
1. 论文的主要贡献和创新点
✅ 解决的问题
现有机制可解释性（MI）框架部署到生产模型服务系统实用性低，核心矛盾在于MI函数与被服务模型无法干净组合，会导致部署拆分、强制请求引流与服务状态重建，还会冲突于生产部署必需的连续批处理、CUDA图执行等性能优化。

🚀 提出的新方法与思路
**xMIx：服务原生MI应用部署框架**，该框架为生产推理服务环境部署MI应用提供解决方案，允许在模型运行时的预定义位置附加MI函数，截获层与残差流中的激活信息；支持根据前序模型层的输出条件调用MI函数；可在单个模型实例中部署多个MI应用，将所有MI应用编译至服务路径，运行时仅动态激活必要的MI部分，无需单独模型实例或替代执行栈，且运行时开销极低。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 部署架构 | 无需单独模型实例或替代执行栈，支持在单个模型实例中部署多个MI应用 |
| 生产兼容性 | 兼容连续批处理、CUDA图执行等生产部署必需的性能优化 |
| 运行开销 | 性能接近原生模型执行，额外开销极小 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 用于评估xMIx在多个MI应用下的性能表现 |

🎯 实验设置与评估指标
任务：将xMIx与vLLM serving系统集成，在三个主要模型及七个不同MI应用上开展性能评估。
| 指标 | 含义 |
| --- | --- |
| 平均令牌间延迟（ITL） | 处理每个令牌的平均间隔时间，↓越低越好 |
| P99令牌间延迟（尾ITL） | 99分位的令牌间延迟，↓越低越好 |
| 平均首令牌时间（TTFT） | 从请求到达至生成第一个令牌的平均耗时，↓越低越好 |
| 平均总令牌吞吐量（TTT） | 单位时间生成的令牌总数，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 原生vLLM执行 | 基准方法 | 无MI函数的原生vLLM模型服务，作为性能基线 |
| 传统MI框架部署 | 对比方法 | 现有MI部署方式，运行时开销高，不兼容生产性能优化 |

3. 主要实验结果和性能指标
📊 定量结果汇总
- 主 benchmark 性能：论文未报告
- 效率对比（FPS / 参数量）：论文未报告
- 跨域 / zero-shot 迁移：论文未报告
- 鲁棒性 / 扰动测试：论文未报告
- 消融实验：论文未报告
（论文摘要报告了性能对比结果，无对应表号）
评估结果：与原生vLLM执行相比，xMIx部署MI应用的性能慢化幅度为：平均ITL 1.3%，P99 ITL 1.2%，平均TTFT 2.6%，平均TTT吞吐量1.6%。
💡 结论：xMIx部署MI应用到vLLM服务环境时，性能接近原生模型执行，仅带来极小的额外开销，有效解决了传统MI框架难以部署至生产系统的性能痛点。

4. 关键结论和发现
- 主要发现：1. 现有传统MI框架因运行时开销高、与生产性能优化不兼容，难以部署到生产模型服务系统；2. xMIx作为服务原生框架，可在单个模型实例中部署多个MI应用，通过动态激活必要的MI部分实现极低运行时开销，兼容生产核心性能优化；3. xMIx与vLLM集成后仅带来极小的性能慢化，性能接近原生模型执行。
- 方法局限性：论文未报告
- 未来工作：论文未报告
✅ **总结一句话**：xMIx是面向生产推理服务环境的服务原生机制可解释性（MI）应用部署框架，支持在单个模型实例中编译多个MI应用，动态激活MI模块仅需极小额外开销，解决了传统MI框架难以部署到生产系统的性能问题。

</details>

---

### 3. [Offline-Online Curriculum RL for Multimodal Reasoning](https://arxiv.org/abs/2607.23700v1)

**Authors**: Wendi Deng, Hang Du, Guoshun Nan, Haokun Tian, Jiaqi Yu, Xinlei Cao, Jaile Li, Jingfeng Chen, Ling Deng, Ting Li, Hao Yang, Jun Liu, Xudong Jiang, Sicong Leng  
**Category**: cs.AI  
**Published**: 2026-07-28  
**Score**: 73.5  
**Type**: new  
**ArXiv ID**: 2607.23700v1  

#### Abstract
Multimodal large language models exhibit capabilities on reasoning tasks, yet often produce flawed intermediate steps while yielding correct final answers. This behavior undermines interpretability and reliability, suggesting reliance on spurious shortcuts rather than faithful reasoning. Although ef...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Offline-Online Curriculum RL for Multimodal Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
多模态大语言模型在推理任务中存在中间步骤有误但最终答案正确的问题，这会破坏模型的可解释性与可靠性，本质是依赖虚假捷径而非忠实推理；现有方法虽探索过步骤级监督，但区分决定性步骤与冗余步骤仍具挑战性。

🚀 提出的新方法与思路
**O²-CritiCuRL**：一种新颖的迭代式离线-在线范式的课程强化学习框架，用于多模态推理任务；离线阶段对带步骤标注的轨迹进行多rollout分析，估计步骤级重要性，以此提炼关键推理步骤并过滤冗余步骤；在线阶段采用渐进式步骤级强化学习策略，通过截断链引导模型推断缺失步骤并优化推理过程，强化模型对关键步骤的关注，克服静态监督的局限性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 多模态推理性能 | 在多模态推理基准上达到state-of-the-art性能 |
| 训练效率 | 优于现有方法 |
| 推理效率 | 优于现有方法 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告具体数据集名称，仅提及使用多模态推理基准 | 用于多模态推理任务的实验评估 |

🎯 实验设置与评估指标
任务为多模态推理任务，论文未报告具体评估指标及指标的优劣方向。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告具体基线方法名称 | - | - |

3. 主要实验结果和性能指标
📊 定量结果汇总
所有实验相关具体数值及对应表格、图表、章节信息均未在论文中报告，具体如下：
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告具体数值，仅提及训练和推理效率优于现有方法
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. 提出的O²-CritiCuRL框架能有效提炼多模态推理的关键步骤、过滤冗余步骤，缓解模型依赖虚假捷径的问题；2. 该框架在多模态推理任务上兼具state-of-the-art性能与更优的训练、推理效率。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出的O²-CritiCuRL是一种迭代离线-在线课程强化学习框架，可增强多模态推理模型的可解释性与可靠性，在达到SOTA性能的同时提升了训练和推理效率。

</details>

---

### 4. [Hybrid Advantage Estimation with Unified Critic for VLM Agentic Reinforcement Learning](https://arxiv.org/abs/2607.23605v1)

**Authors**: Wenxuan Zhang, Yuhui Wang, Donggang Jia, Xiaoqian Shen, Jian Ding, Ivan Viola, J\"urgen Schmidhuber, Mohamed Elhoseiny  
**Category**: cs.AI  
**Published**: 2026-07-28  
**Score**: 64.5  
**Type**: new  
**ArXiv ID**: 2607.23605v1  

#### Abstract
Large Vision-Language Models (VLMs) now act as agents in interactive environments, where success requires coherent reasoning and decision-making across turns. Although end-to-end training in agentic environments can improve such multi-turn decision-making abilities, current methods mainly rely on ei...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# Hybrid Advantage Estimation with Unified Critic for VLM Agentic Reinforcement Learning
## 1. 论文的主要贡献和创新点
### 解决的问题
现有VLM agent在多转向交互环境下的强化学习方法存在两类核心缺陷：其一采用token-wise优化针对拼接的token轨迹，难以适配多转向决策的连贯性需求；其二采用turn-wise优化但转向内信用分配均匀，忽略转向内不同token的贡献差异，均无法同时满足token级与turn级的多层级优化要求。

### 提出的新方法与思路
**HyGAE框架**，属于Actor-Critic架构：首先建立token-wise与turn-wise优化的理论框架，推导得到兼顾两类层级优化的hybrid advantage；进一步证明通过选择合适的折扣因子与学习目标，统一的critic模型可同时估计turn级与token级的价值；最终依托该框架联合优化token级与turn级目标，完成VLM agent的训练。

### 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 多层级优化 | 兼顾token级与turn级的决策优化需求，适配多转向交互的连贯性要求 |
| Critic设计 | 采用统一Critic模型，无需分离设计不同层级的价值估计模块 |
| 性能表现 | 在多转向决策任务中较现有方法取得显著提升 |

## 2. 核心实验方法和设置
### 使用的数据集
论文未报告
### 实验设置与评估指标
任务：在多转向交互环境中开展VLM agent的强化学习任务
| 指标 | 含义 |
| --- | --- |
| 平均成功率 | 多转向决策任务的完成概率，↑越高越好 |
### 基线方法对比
论文未报告

## 3. 主要实验结果和性能指标
### 主benchmark性能
论文未报告
### 效率对比（FPS / 参数量）
论文未报告
### 跨域 / zero-shot迁移
论文未报告
### 鲁棒性 / 扰动测试
论文未报告
### 消融实验
论文未报告

## 4. 关键结论和发现
- 主要发现：hybrid advantage与return的精确解析形式对优化过程至关重要；所提出的HyGAE框架可实现VLM agent的token级与turn级目标的联合优化。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：提出HyGAE Actor-Critic框架，通过统一Critic与混合优势函数联合优化VLM agent的token级与turn级决策目标，适配多转向交互任务的优化需求。

</details>

---

### 5. [PIVOT: Efficient Query-Group Indexing for Token-Level Sparse Attention](https://arxiv.org/abs/2607.24593v1)

**Authors**: Hong Liu, Yuan Cheng, Lin Niu, Yi Su, Yufei Xue, Anmin Liu, Guanghua Yu, Jianchen Zhu  
**Category**: cs.CL  
**Published**: 2026-07-28  
**Score**: 58.5  
**Type**: new  
**ArXiv ID**: 2607.24593v1  

#### Abstract
Token-level sparse attention, as implemented by DeepSeek Sparse Attention (DSA) in production systems, makes the downstream attention efficient but shifts the bottleneck to the indexer that feeds it. To select the top-k tokens for each query, the indexer must still score every preceding token, incur...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：PIVOT: Efficient Query-Group Indexing for Token-Level Sparse Attention
1. 论文的主要贡献和创新点
✅ 解决的问题
Token级稀疏注意力（以DeepSeek Sparse Attention, DSA为生产实现）提升了下游注意力的效率，但将系统瓶颈转移至为其提供输入的索引器；
- 原DSA索引器缺陷：对每个查询扫描所有前序token，序列长度为L时每层计算成本为O(L²)，成为系统核心瓶颈；
- 索引计算冗余缺陷：邻近查询的top-k token高度重叠，索引器得分沿键轴呈长尾分布，逐查询扫描存在大量冗余计算。
🚀 提出的新方法与思路
**PIVOT（Proxy Indexing Via One full-prefix Traversal）**：一种训练-free的DSA索引器替换方案，核心思路为共享分组查询的前缀扫描：将邻近查询划分为组，聚合组内查询生成单个代理查询，执行一次共享的全前缀扫描以获取候选集，再从候选集中为每个查询选择对应的top-k token；包含两个灵活变体：**PIVOT-Reuse**（直接共享代理查询的top-k，追求极致速度）、**PIVOT-Refine**（用组内各查询的索引器重排序候选集，为每个查询生成单独top-k，匹配稠密索引器精度）；统一算法覆盖预fill和解码两个推理阶段，仅分组逻辑不同：预fill阶段采用固定大小的连续查询组，解码阶段采用同一多token预测（MTP）步内的查询组。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 索引成本 | 训练-free，共享前缀扫描将逐查询O(L²)的时间复杂度优化为候选集选择的复杂度，消除索引器瓶颈 |
| 精度匹配 | PIVOT-Refine可匹配稠密DSA索引器的精度 |
| 效率提升 | 长上下文场景下索引加速最高可达4倍，端到端延迟最高降低可达1.6倍 |
| 阶段适配 | 统一算法覆盖预fill与解码全推理流程，适配不同阶段的查询特性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| LongBench | 评估长序列相关任务性能 |
| RULER | 评估长序列推理能力 |
🎯 实验设置与评估指标
任务为token级稀疏注意力索引的精度与效率评估。
| 指标 | 含义（箭头标方向） |
| --- | --- |
| 索引精度 | 与稠密DSA索引器的匹配度，越高越好（↑） |
| 索引加速比 | 索引器的速度提升倍数，越高越好（↑） |
| 端到端延迟降低率 | 推理端到端延迟的下降比例，越高越好（↑） |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| DSA索引器 | 基线方法 | DeepSeek原生的稀疏注意力索引器，逐查询扫描所有前序token，时间复杂度O(L²) |
| 稠密索引器 | 对比方法 | 全量计算所有前序token得分的索引方式，无稀疏性损失但计算成本高 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体实验结果对应表号、图号或章节，仅提及在DeepSeek-V3.2、GLM-5.1模型上，于LongBench、RULER基准上，PIVOT匹配稠密DSA索引器精度，索引加速最高可达4倍，长上下文场景下端到端延迟最高降低可达1.6倍。
💡 结论：论文提及在指定模型与基准上，PIVOT可在保证索引精度的同时显著提升长上下文场景下的稀疏注意力效率。

4. 关键结论和发现
- 核心发现1：邻近查询top-k重叠、索引得分长尾的特性可被有效利用，通过分组共享前缀扫描的策略，解决了token级稀疏注意力索引的O(L²)瓶颈。
- 核心发现2：PIVOT的两个变体可根据速度与精度需求灵活选择，PIVOT-Refine可匹配稠密索引器精度，PIVOT-Reuse实现最大速度。
- 核心发现3：在长序列基准上，PIVOT可同时保证索引精度并大幅降低长上下文场景的端到端延迟。
- 方法局限性：论文未报告极端长序列性能、不同分组大小的影响等细节。
- 未来工作：论文未明确提及未来工作方向。

> ✅ **总结一句话**：PIVOT是一种训练-free的查询分组索引方法，通过共享邻近查询的前缀扫描思路，解决了token级稀疏注意力索引的O(L²)瓶颈，在长上下文场景下可同时保证索引精度并大幅提升效率。

</details>

---

### 6. [KAP: Bridging the Knowledge Selection-Runtime Consumption Gap in LLM Systems](https://arxiv.org/abs/2607.24260v1)

**Authors**: Shuo Wang, Fang Xi, Wenyuan Huang, Qing Wang, Junming Su  
**Category**: cs.LG  
**Published**: 2026-07-28  
**Score**: 56.5  
**Type**: new  
**ArXiv ID**: 2607.24260v1  

#### Abstract
Modern LLM systems increasingly rely on knowledge-selection processes that produce high-value structured priors, such as ranked evidence, graph topology, multimodal alignment, and confidence signals. Yet LLM serving remains fundamentally oblivious to this rich structure: once such signals are serial...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

KAP: Bridging the Knowledge Selection-Runtime Consumption Gap in LLM Systems
1. 论文的主要贡献和创新点
✅ 解决的问题
核心是LLM系统在知识选择阶段生成的结构化知识先验（如排序证据、图拓扑、多模态对齐、置信信号等），被推理服务后端序列化为扁平token序列，导致“知识选择-运行时消费（KSRC）”架构不匹配：推理服务需消耗全量Key-Value（KV）状态，增大KV内存 footprint、解码内存流量与延迟，降低吞吐量，即便推理仅依赖小部分上下文。
🚀 提出的新方法与思路
**Knowledge Access Planning (KAP)**：一种范式转变的执行抽象，将结构化知识先验从被动提示构建的辅助信息升级为一级物理执行构件；建立通用中间表示（IR）—— runtime access plan，编译结构化知识信号以管控物理KV访问，不改变逻辑提示语义、模型权重或训练流程，将LLM推理服务从基于token的上下文消费转向计划驱动的、知识感知的运行时消费。
**GraphSpec**：KAP的实例化实现，是连接结构化知识选择与LLM推理服务后端的编译器-执行器；推导了Phase-boundary Model，用于规划引导执行的正加速 regime。
🔍 相比现有方法的优势
维度 | 优势
--- | ---
上下文消费逻辑 | 从token驱动转向知识感知，无需修改模型权重或训练流程
KV资源效率 | 解耦物理KV消耗与提示长度，避免不必要的全量KV访问
输出适配性 | 适配长上下文任务时维持输出质量稳定
2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
4K-128K长上下文QA workloads | 验证KAP（GraphSpec实现）在长上下文场景下的性能与资源效率
🎯 实验设置与评估指标
任务：在4K-128K的长上下文问答（QA）任务中，评估所提方法的性能与资源效率。
指标 | 含义
--- | ---
答案质量 | 衡量QA任务输出的正确性（越高越好）
提案阶段KV访问占比 | 提案阶段KV访问量与源KV状态的比值（越低越好）
⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
全上下文解码 | 基线方法 | 直接处理全量上下文，消耗全部KV状态，存在KSRC架构不匹配问题
3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告带编号的实验表格，仅提及核心结果：在4K-128K长上下文QA workloads中，GraphSpec维持的答案质量与全上下文解码相当，同时降低了提案阶段的KV访问量。
💡 结论：所提方法可在维持长上下文QA任务输出质量的前提下，降低KV资源消耗。
4. 关键结论和发现
- 核心发现1：KSRC架构不匹配是长上下文LLM服务中资源浪费的核心原因，知识选择阶段的结构化先验未被运行时有效利用。
- 核心发现2：KAP范式（含GraphSpec实现）可在不修改模型的前提下，解耦KV消耗与提示长度，实现长上下文场景下的KV资源高效利用。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出KAP执行抽象范式，通过将结构化知识先验升级为物理执行构件，解决了LLM服务中的KSRC架构不匹配问题，在维持长上下文问答任务输出质量的同时降低KV资源消耗与延迟。

</details>

---

### 7. [Evaluating Fuzz Testing for Reinforcement Learning Agents](https://arxiv.org/abs/2607.24577v1)

**Authors**: Zhibin Kang, Hanmo You, Dong Wang, Haiming Zheng, Junjie Chen  
**Category**: cs.LG  
**Published**: 2026-07-28  
**Score**: 54.0  
**Type**: new  
**ArXiv ID**: 2607.24577v1  

#### Abstract
Reinforcement Learning (RL) agents are increasingly deployed in safety-critical domains such as robotics, autonomous driving, and drone control, where unexpected behaviors may lead to severe real-world consequences. Fuzz testing has recently emerged as a promising method for exploring the vast state...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Evaluating Fuzz Testing for Reinforcement Learning Agents
1. 论文的主要贡献和创新点
✅ 解决的问题：现有RL模糊测试方法的研究因评估设置、基线、指标不统一，难以得出可靠的相对有效性和实用性结论；不同方法各有侧重，缺乏系统的统一评估。
🚀 提出的新方法与思路：本研究是**第一个从有效性、多样性、效率、实用型四个互补视角**，在三个复杂度递增的RL环境（MountainCar, BipedalWalker, CARLA）及统一配置下，系统评估RL模糊测试方法的综合实证研究；同时评估模糊测试生成的崩溃对智能体鲁棒性提升和安全监控的下游实用性。
🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 评估视角 | 采用四个互补视角（有效性、多样性、效率、实用型）系统评估RL模糊测试，而非单一维度 |
| 评估设置 | 在统一配置下进行基准测试，消除了不同研究间评估条件差异导致的结论不可靠问题 |
| 实用性评估 | 首次评估模糊测试生成的崩溃对智能体鲁棒性提升和安全监控的下游价值 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| MountainCar | 用于复杂度较低的RL环境基准测试 |
| BipedalWalker | 用于复杂度中等的RL环境基准测试 |
| CARLA | 用于复杂度较高的RL环境基准测试 |
🎯 实验设置与评估指标
在三个复杂度递增的RL环境中，以随机测试为基线，在统一配置下评估RL模糊测试方法的性能，同时评估生成崩溃的下游实用性。
| 指标 | 含义（箭头标方向） |
|------|-------------------|
| crash发现有效性 | 越高越好（单位时间内发现的crash数量） |
| crash行为多样性 | 越高越好（不同crash的行为差异程度） |
| 效率 | 越高越好（单位时间内的吞吐量） |
| 下游实用性 | 越高越好（生成crash对鲁棒性提升、安全监控的效果） |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 随机测试 | 基线方法 | 作为对比基准 |
| MDPFuzz | 吞吐量导向模糊测试方法 | 侧重高效发现crash |
| SeqDivFuzz | 探索导向模糊测试方法 | 侧重发现多样化crash行为 |
| 其余三种SOTA RL模糊测试方法 | 先进测试方法 | 论文未明确报告具体名称及特点 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告具体表号及对应数值，仅定性说明MDPFuzz在crash发现的有效性上更优，SeqDivFuzz在crash行为多样性上更优。
2. 效率对比：论文未报告具体表号及对应FPS/参数量等数值，仅定性说明MDPFuzz具有更优的效率。
3. 跨域 / zero-shot 迁移：论文未报告相关实验的具体定量结果及表号，仅提及fuzzing生成的crash在安全监控上具有强跨方法泛化性。
4. 鲁棒性 / 扰动测试：论文未报告相关具体指标数值及表号，仅提及模糊测试生成的crash可显著提升智能体鲁棒性。
5. 消融实验：论文未报告消融实验的具体模块配置及指标数值，仅提及可结合互补的fuzzing策略、采用多级多样性分析实现更全面的测试。

4. 关键结论和发现
- 主要发现：① 现有RL模糊测试研究因评估设置、基线、指标不一致，难以得出可靠的相对有效性和实用性结论；② 不同RL模糊测试方法各有侧重，吞吐量导向的MDPFuzz侧重高效crash发现，探索导向的SeqDivFuzz侧重多样化crash发现；③ 模糊测试生成的crash可有效提升智能体鲁棒性，且能实现强跨方法泛化的安全监控。
- 方法局限性：论文未明确报告研究方法的局限性。
- 未来工作：论文指出可结合互补的fuzzing策略、采用多级多样性分析，提升RL安全测试的全面性和实用性。

> ✅ **总结一句话**：这篇论文首次在统一配置下从四个互补视角系统评估RL模糊测试方法，揭示不同方法的优劣特性及fuzzing生成崩溃的实用价值，为RL安全测试提供了可操作的指导。

</details>

---

### 8. [Beyond Block Boundaries: Multi-Block Editing for Diffusion Large Language Models](https://arxiv.org/abs/2607.22663v1)

**Authors**: Xingyu Mou, Zijin Huang, Tianze Zhang, Yuxin Ma, Lanning Wei, Zengfeng Huang, Da Zheng, Lun Du  
**Category**: cs.AI  
**Published**: 2026-07-28  
**Score**: 49.0  
**Type**: new  
**ArXiv ID**: 2607.22663v1  

#### Abstract
Block diffusion has emerged as the dominant paradigm for scaling discrete diffusion language models (dLLMs), because decoding text in fixed-size blocks preserves parallel generation within each block while keeping the quadratic attention cost tractable. However, this efficiency comes with a structur...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Beyond Block Boundaries: Multi-Block Editing for Diffusion Large Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题
Block diffusion是当前离散扩散语言模型（dLLM）的主流缩放范式，其固定大小块解码方案在保留块内并行生成、控制二次注意力成本的同时，存在显著结构缺陷：块末尾生成的token无法获取后续跨块上下文，且块确定后其中的不确定预测会成为后续所有块的不可逆上下文，引发块边界问题——不确定性向块边界累积，早期错误会传播至后续整个生成过程。

🚀 提出的新方法与思路
**Multi-Block Editing (MBE)**：包含三个核心模块：
1. **训练-free解码算法**：通过对选定块重新开启全注意力窗口，对前序块的解码token进行编辑，缓解块不可逆性；
2. **监督微调策略（MBE SFT）**：为模型配备双向注意力掩码，逐步扩展编辑跨度，适配Block diffusion训练与MBE推理间不匹配的注意力机制；
3. **系统优化扩展**：为SGLang扩展多形状CUDA Graph池与细粒度KV缓存控制，让可变长度编辑通行在实际部署中高效运行。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 性能 | 训练-free MBE在LLaDA2.1-Mini的13个benchmarks上表现优于所有现有解码基线；MBE SFT可进一步带来2.7的性能增益 |
| 效率 | 训练-free MBE在性能提升的同时，维持与现有解码基线相当的吞吐量 |
| 长程一致性任务适配 | 在需要强长程一致性的任务（如AIME 2025、ZebraLogic）上提升显著，AIME 2025性能提升+13.3，ZebraLogic提升+5.9 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| LLaDA2.1-Mini（对应13个benchmarks） | 评估模型在各类语言生成任务上的性能 |

🎯 实验设置与评估指标
实验为语言生成任务，评估指标包含生成性能增益、吞吐量等（论文未明确具体指标名称，仅报告性能提升幅度）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Block diffusion原生解码（现有基线） | 解码方法 | 采用固定大小块生成，存在块边界问题，无跨块编辑机制 |
| 训练-free MBE | 新提出训练-free解码方法 | 无需额外微调，通过跨块全注意力窗口编辑前序块token |
| MBE SFT | 新提出微调方法 | 引入双向注意力掩码扩展编辑跨度，适配注意力机制不匹配问题 |

3. 主要实验结果和性能指标
📊 定量结果汇总
（论文未报告具体表格编号及对应场景的详细表格，仅从摘要提取关键结果）
**主benchmark性能（LLaDA2.1-Mini，13 benchmarks）**：
| 方法 | 性能 |
| --- | --- |
| 现有解码基线 | 基线性能 |
| 训练-free MBE | 优于所有现有解码基线 ✅ |
| MBE SFT | 较训练-free MBE进一步提升2.7 |

💡 结论：训练-free MBE的解码性能优于所有现有基线，MBE SFT可进一步提升整体生成性能。

**关键任务性能提升**：
| 任务 | 性能提升幅度 |
| --- | --- |
| AIME 2025 | +13.3 ✅ |
| ZebraLogic | +5.9 ✅ |

💡 结论：MBE在需要强长程一致性的任务上提升效果显著。

**效率对比**：
训练-free MBE维持与现有解码基线相当的吞吐量。
💡 结论：训练-free MBE在提升性能的同时，未牺牲生成效率。

其余实验（跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）：论文未报告。

4. 关键结论和发现
- 主要发现：1. Block diffusion存在块边界问题，早期错误会跨块传播，MBE可有效缓解该问题；2. 训练-free MBE无需微调即可超越所有现有解码基线，且吞吐量相当；3. MBE在需要强长程一致性的任务（如AIME2025、ZebraLogic）上性能提升显著，验证了对长程任务的适配性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出Multi-Block Editing方法，通过训练-free解码与监督微调策略，解决Block diffusion语言模型的块边界问题，提升长程一致性任务性能，且维持原有生成效率。

</details>

---

### 9. [DynaResize: Runtime GPU Reallocation for Disaggregated LLM Post-Training](https://arxiv.org/abs/2607.22614v1)

**Authors**: Hanlin Du, Zhiyuan Yan, Haiquan Chen, Jiarui Fang, Yungang Bao, Sa wang  
**Category**: cs.AI  
**Published**: 2026-07-28  
**Score**: 46.5  
**Type**: new  
**ArXiv ID**: 2607.22614v1  

#### Abstract
RL-based LLM post-training increasingly disaggregates Rollout and Training across separate GPU resources, but static GPU partitioning suffers from severe pipeline bubbles under long-tail rollout latency. We present DynaResize, a runtime GPU reallocation system that dynamically switches GPUs between ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# DynaResize: Runtime GPU Reallocation for Disaggregated LLM Post-Training
1. 论文的主要贡献和创新点
✅ 解决的问题
RL-based LLM post-training采用disaggregated架构，将Rollout与Training部署于独立GPU资源；静态GPU partitioning会因长尾rollout latency引发严重的流水线气泡，且角色切换存在额外开销。

🚀 提出的新方法与思路
**DynaResize**：一种运行时GPU重分配系统，核心设计包括：1. 动态切换GPU在Rollout和Training阶段的分配，平衡两阶段执行时间，且不改变RL语义；2. 将GPU重分配操作分解为细粒度操作；3. 借助communicator reuse、bounded state staging、hysteresis-based resizing技术，移除重分配过程中非启动关键工作的关键路径依赖。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
资源调度方式 | 区别于静态GPU partitioning，可动态适配disaggregated LLM post-training的阶段执行差异，减少流水线气泡
角色切换开销 | 可隐藏角色切换过程中产生的部分额外开销
端到端性能 | 相对最优静态配置具备更优的性能表现

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
论文未报告

⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
因论文提供的信息仅为摘要，未标注任何定量结果对应的表号、图号等来源标识，相关定量性能数据无法定位来源，故论文未报告具体定量结果。
- 主benchmark性能：论文未报告
- 效率对比：论文未报告
- 跨域/zero-shot迁移：论文未报告
- 鲁棒性/扰动测试：论文未报告
- 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：在RL-based LLM post-training的disaggregated架构下，DynaResize的动态GPU重分配机制可有效平衡Rollout与Training阶段的执行时间，缓解静态分区导致的流水线气泡问题；
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：DynaResize是针对disaggregated LLM post-training的运行时GPU重分配系统，通过动态调整GPU分配平衡阶段执行时间，减少流水线气泡与角色切换开销，提升端到端性能。

</details>

---

### 10. [ObsDriveBench: Benchmarking Multimodal Understanding under Adverse Weather with Observability Awareness](https://arxiv.org/abs/2607.23537v1)

**Authors**: Qiao Yan, Yihan Wang, Zhenghao Xing, Jiaqi Xu, Pheng-Ann Heng  
**Category**: cs.AI  
**Published**: 2026-07-28  
**Score**: 45.5  
**Type**: new  
**ArXiv ID**: 2607.23537v1  

#### Abstract
Autonomous driving under adverse weather remains a critical challenge, yet existing vision-language benchmarks mainly evaluate under standard conditions, synthetic corruptions, or single modality. As a result, it remains unclear how vision-language models behave under real-world adverse weather with...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：ObsDriveBench: Benchmarking Multimodal Understanding under Adverse Weather with Observability Awareness
1. 论文的主要贡献和创新点
✅ 解决的问题
1. 现有视觉语言基准主要针对标准条件、合成损坏或单模态场景，未聚焦真实恶劣天气下的多模态自动驾驶场景，无法评估模型在真实环境的表现；
2. 现有基准缺乏可细粒度诊断模型在退化观测下行为的能力维度，难以定位模型在恶劣天气下的具体失效问题；
真实恶劣天气下多模态观测不可靠且跨模态不一致，为自动驾驶场景理解及后续决策带来核心挑战。

🚀 提出的新方法与思路
**ObsDriveBench基准构建**：针对真实恶劣天气自动驾驶的多模态需求，设置可观测性感知、空间可靠性、风险感知决策三个核心能力维度，基于同步相机、LiDAR、雷达输入开展可观测性元标注、场景描述及面向能力的多项选择任务，构建了包含14k训练问题、13k测试问题的多模态基准。
**ObsDrive模型框架**：采用正常天气监督微调结合恶劣天气强化学习的流程，优化模型在恶劣天气下的三类核心能力鲁棒性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 基准设计 | 明确设置三类能力维度，实现模型在退化观测下行为的细粒度诊断，且基于真实多模态输入构建 |
| 模型优化 | 结合正常天气监督微调与恶劣天气强化学习，提升模型在恶劣天气多模态场景下的核心能力鲁棒性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| ObsDriveBench | 用于评估多模态模型在真实恶劣天气自动驾驶场景下的多模态理解与决策能力 |

🎯 实验设置与评估指标
任务为评估多模态模型在真实恶劣天气自动驾驶场景下的多模态理解及相关决策能力。
论文未报告具体评估指标与含义。

⚔️ 基线方法对比
论文未报告具体基线方法的详细信息。

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告

4. 关键结论和发现
- 主要发现
  1. 现有视觉语言模型在真实恶劣天气（雾、雨、雪、低光照）的多模态自动驾驶场景中，存在一致的性能退化；
  2. ObsDrive模型通过正常天气监督微调加恶劣天气强化学习的方式，能够提升模型在可观测性感知、空间可靠性、风险感知决策三个核心能力维度的鲁棒性。
- 方法局限性
  论文未报告
- 未来工作
  论文未报告

> ✅ **总结一句话**：论文提出了面向真实恶劣天气自动驾驶的多模态基准ObsDriveBench，实现模型行为的细粒度诊断，并构建了ObsDrive模型，有效提升了模型在恶劣天气多模态场景下的核心能力鲁棒性。

</details>

---

### 11. [PRESTO: Prefix-Aligned Tree Drafting for Diffusion Speculative Decoding](https://arxiv.org/abs/2607.22634v1)

**Authors**: Zheng Wang, Zhifan Ye, Qi Cheng, Yonggan Fu, Ziyan Wang, Feng Zhu, Haozhe Zhao, Jan Kautz, Pavlo Molchanov, Humphrey Shi, Minjia Zhang  
**Category**: cs.AI  
**Published**: 2026-07-28  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2607.22634v1  

#### Abstract
Diffusion Large Language Models (dLLMs) have emerged as a promising alternative to autoregressive (AR) LLMs, generating tokens in parallel. This makes them effective draft models for speculative decoding (SD), producing an entire block of draft tokens in a single forward pass. Yet existing diffusion...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

PRESTO: Prefix-Aligned Tree Drafting for Diffusion Speculative Decoding
1. 论文的主要贡献和创新点
✅ 解决的问题
现有扩散大语言模型（dLLMs）作为 speculative decoding（SD）的 draft模型时，采用线性 drafting方式，但dLLMs会生成多候选token，形成庞大的解码路径组合空间，导致解码效率和接受长度受限；此外，朴素树 drafting存在次优问题——扩散边际分布（diffusion marginals）是前缀盲的，与基于前缀的自回归（AR）验证不匹配，路径排名不可靠。

🚀 提出的新方法与思路
**Prefix-Aligned Scoring（前缀对齐评分）**：使候选路径的排名与AR验证的前缀性质保持一致，解决扩散边际分布与AR验证之间的前缀不匹配问题，实现合理的路径排序。
**Priority-Based Tree Search（优先级树搜索）**：在树构造过程中优先选择具有高验证潜力的候选路径，以最大化解码过程中的token接受长度，提升整体解码效率。
PRESTO将树基 drafting扩展至扩散 drafter，通过上述两个核心原则解决原有方法的前缀对齐和路径优化痛点。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
端到端吞吐量 | 相比现有专用扩散 drafter SD，平均可达约1.5倍端到端吞吐量加速；相比自 speculative扩散LLMs，平均可达约1.12倍加速（论文仅在摘要中提及该结果，无对应表号）
解码适配性 | 突破线性 drafting的限制，充分利用dLLMs的多候选token结构，拓展解码路径的探索空间

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
论文未报告 | 多样化基准测试

🎯 实验设置与评估指标
任务：扩散 speculative decoding的端到端文本生成任务
指标 | 含义
--- | ---
端到端吞吐量 | 越高越好（↑）

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
现有线性扩散 drafting方法 | 扩散 draft方法 | 采用线性 drafting，未利用dLLMs多候选结构，解码效率与接受长度受限
朴素树 drafting方法 | 树 draft方法 | 未解决扩散边际分布与AR验证的前缀不匹配问题，路径排名不可靠，解码性能次优

3. 主要实验结果和性能指标
📊 定量结果汇总
论文仅在摘要中提及加速比，无对应表号、图号等定位信息，以下为各实验模块情况：
1. 主benchmark性能：论文未报告
2. 效率对比（FPS/参数量）：论文未报告，仅提及端到端吞吐量加速的泛化结论
3. 跨域 / zero-shot迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

💡 结论：PRESTO在多样化基准上可实现扩散 speculative decoding的端到端吞吐量显著提升。

4. 关键结论和发现
- 主要发现：PRESTO通过前缀对齐评分和优先级树搜索，解决了扩散 drafting中扩散边际分布与AR验证的前缀不匹配核心问题，有效利用dLLMs的多候选结构提升了解码效率。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：PRESTO是针对扩散 speculative decoding提出的前缀对齐树 drafting框架，通过前缀对齐评分和优先级树搜索解决原有方法的前缀不匹配问题，实现了显著的端到端吞吐量加速。

</details>

---

### 12. [Reason Before You Retrieve: Agentic Planning for Multi-modal RAG](https://arxiv.org/abs/2607.22643v1)

**Authors**: Tianyu Yang, Shir Simon, Zhenzhen Li, Minhao Cheng, Xiangliang Zhang  
**Category**: cs.AI  
**Published**: 2026-07-28  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2607.22643v1  

#### Abstract
Multimodal retrieval-augmented generation (mRAG) aims to answer image-text queries with external knowledge, but most existing systems still retrieve directly from raw multimodal input over a flat evidence space. This design often struggles with two key challenges: the retrieval target is under-speci...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Reason Before You Retrieve: Agentic Planning for Multi-modal RAG
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多模态检索增强生成（mRAG）系统大多从原始多模态输入的平面证据空间直接检索，存在两个核心痛点：一是检索目标未明确，问题意图需锚定正确的视觉指称物；二是搜索空间结构弱，不同语义的证据在单一全局排序步骤中竞争。

🚀 提出的新方法与思路
**MM-R2（Multimodal Agentic Retrieval Framework）**：核心采用"推理后检索"的策略，首先从图像-问题对构建意图接地的检索状态，捕捉信息需求、接地指称物和检索约束；随后在结构化KnowledgeMap上执行检索，代理先选择相关检索单元，再在单元内发起接地查询。
**MM-R2-Traj**：构建的大规模多步检索过程轨迹数据集，采用监督微调与GRPO结合的两阶段后训练策略，支撑代理的检索规划能力。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 检索逻辑 | 通过意图建模明确检索目标，基于结构化空间检索避免平面证据的无差别竞争 |
| 性能表现 | 在多模态RAG任务的答案准确性上显著优于强基线方法 |
| 可解释性 | 生成可解释、可验证的检索轨迹 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Infoseek | 评估MM-R2在多模态RAG任务上的性能 |
| Encyclopedic VQA | 评估MM-R2在多模态RAG任务上的性能 |

🎯 实验设置与评估指标
任务为多模态检索增强生成（mRAG）任务，核心评估答案准确性。
| 指标 | 含义 |
| --- | --- |
| 答案准确性 | 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 现有强基线多模态RAG系统 | 基线方法 | 从原始多模态输入的平面证据空间直接检索 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表N：主 benchmark 性能（场景：多模态RAG任务）**
论文未报告具体实验的表号、图号及对应数值，仅提及MM-R2在Infoseek和Encyclopedic VQA数据集上显著优于强基线方法。
💡 结论：MM-R2在多模态RAG任务中相比现有强基线提升了答案准确性，同时生成可解释的检索轨迹。
效率对比：论文未报告
跨域/zero-shot迁移：论文未报告
鲁棒性/扰动测试：论文未报告
消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. 现有mRAG系统从原始多模态输入的平面证据空间直接检索的设计，存在检索目标未明确、搜索空间结构弱的核心痛点；2. MM-R2通过"推理后检索"的框架，结合意图接地和结构化KnowledgeMap，可有效解决上述痛点，兼具更高的答案准确性和检索过程可解释性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：MM-R2是一种多模态代理检索框架，通过在检索前推理的策略解决现有多模态RAG系统的核心缺陷，提升答案准确性并生成可解释的检索轨迹。

</details>

---

### 13. [GOTS: Greedy Orthogonal Token Selection for High-Resolution Vision-Language Models](https://arxiv.org/abs/2607.23913v1)

**Authors**: Jun Ling, Tao Huang, Junzhuo Liu, Bowen Tang, Peng Wang  
**Category**: cs.AI  
**Published**: 2026-07-28  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2607.23913v1  

#### Abstract
Modern vision-language models (VLMs) increasingly rely on dynamic or high-resolution visual encoding, producing thousands of visual tokens that substantially increase downstream language-model inference cost. Existing token-reduction methods assess token utility through token-wise importance, query ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

### GOTS: Greedy Orthogonal Token Selection for High-Resolution Vision-Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题
现代视觉语言模型(VLMs)依赖动态或高分辨率视觉编码，产生数千个视觉令牌，大幅增加下游语言模型推理成本；现有视觉令牌减少方法仅通过令牌重要性、查询相关性、覆盖范围、成对多样性或子集级目标评估令牌效用，存在评估视角的局限性。

🚀 提出的新方法与思路
**Greedy Orthogonal Token Selection (GOTS)**：核心思路是将视觉令牌减少转化为所选令牌跨度的互补性评估，而非孤立评分令牌或考虑成对关系，通过评估令牌特征与已保留子集跨度的正交程度实现选择。具体为训练-free且查询无关(query-agnostic)的贪心方法，每一步选择与当前保留跨度正交的残差能量最大的令牌，该规则精确最大化候选添加中的单步增广Gram行列式，为贪心步骤的子集扩展提供精确的局部几何保证。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 主性能表现 | 在Qwen-VL和InternVL家族的五个高分辨率VLM主干及十一个多样化基准上，比最强评估基线实现更高的平均性能保留 |
| 推理效率控制 | 经选择开销考虑后，在OCRBench研究中降低模型端首token时间 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 十一个多样化基准 | 主性能评估 |
| OCRBench | 模型侧首token时间控制研究 |
*注：论文未明确报告其他具体数据集信息*

🎯 实验设置与评估指标
任务为视觉令牌减少以降低高分辨率VLMs的下游语言模型推理成本，评估指标包含平均性能保留、OCRBench下的模型侧首token时间及经选择开销调整后的时间指标。
| 指标 | 含义 |
| --- | --- |
| 平均性能保留 | ↑ 越高越好 |
| 模型侧首token时间 | ↓ 越低越好 |
*注：论文未报告指标的具体阈值或计算方式细节*

⚔️ 基线方法对比
论文未报告基线方法的具体类型、特点等详细信息，仅提及对比最强评估基线。

3. 主要实验结果和性能指标
📊 定量结果汇总
所有实验未提供具体表号、图号及对应数值，因此按要求呈现：
1. 主benchmark性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现
1. GOTS是训练-free、query-agnostic的视觉令牌减少方法，通过正交残差能量选择令牌，为贪心选择步骤提供了精确的局部几何保证。
2. 在多个高分辨率VLM主干及多样化基准上，GOTS的平均性能保留优于最强基线。
3. 经选择开销考虑后，GOTS可在OCRBench上降低模型侧首token时间。
- 方法局限性
论文未报告
- 未来工作
论文未报告

> ✅ **总结一句话**：GOTS是适用于高分辨率VLMs的训练-free、query-agnostic视觉令牌减少方法，能在提升性能保留能力的同时降低下游推理成本。

</details>

---

### 14. [DICE: Detailed Inter-Chiplet End-to-End PHY Modeling for Accurate Chiplet Simulation](https://arxiv.org/abs/2607.24221v1)

**Authors**: Rashid Aligholipour, Stefanos kaxiras, Yuan Yao  
**Category**: cs.AR  
**Published**: 2026-07-28  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2607.24221v1  

#### Abstract
Scaling monolithic multicores is increasingly constrained by power/thermal limits, yield, and rising manufacturing and testing costs. Chiplet designs address these challenges by partitioning large dies into smaller parts (typically multiple core-complex dies and an I/O die) linked via high-bandwidth...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：DICE: Detailed Inter-Chiplet End-to-End PHY Modeling for Accurate Chiplet Simulation
1. 论文的主要贡献和创新点
✅ 解决的问题
当前芯片粒仿真常用简化的固定延迟模型近似芯片粒间链路，忽略了PHY的动态运行时行为，包括通道条件变化、解码迭代收敛、包重传及应用动态等，导致芯片粒间包级时序与IPC等高层性能指标被扭曲，模拟结果偏离实际趋势。

🚀 提出的新方法与思路
**DICE**：是在gem5中实现的运行时PHY建模方法，用于捕获端到端的芯片粒间数据通路细节，涵盖QC-LDPC编码/解码、PAM4调制、lossy-channel传输、基于LLR的解调、adaptive packet重传、芯片粒间PHY级流控等模块。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 链路建模精度 | 可捕捉现有简化模型忽略的PHY动态运行时行为，提升仿真可靠性 |
| 端到端链路表征 | 覆盖芯片粒间数据通路全流程细节，包括编码、调制、传输与流控等核心环节 |
| 性能指标真实性 | 能更准确反映芯片粒间包级时序和IPC等高层性能，避免模拟结果失真 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
论文未报告

⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能（L2/碰撞率等）：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. 忽略芯片粒间PHY的动态运行时行为会扭曲包级时序和IPC等高层性能指标，导致模拟结果偏离实际；2. DICE的端到端详细PHY建模可有效捕获这些现有模型遗漏的关键环节。
- 方法局限性：论文未报告
- 未来工作：论文未报告

✅ **总结一句话**：DICE是一款在gem5中实现的、详细建模芯片粒间端到端PHY运行时行为的仿真方法，解决了现有简化模拟模型精度不足的问题，提升了芯片粒仿真的可靠性。

</details>

---

### 15. [ERUnderstand: Evaluating Vision-Language Models on Structured ER Diagrams](https://arxiv.org/abs/2607.24707v1)

**Authors**: Ali Ansari, Yasmin Mohammadi, Farnoush Nili, Parsa Esmaeilkhani, Longin Jan Latecki, Eduard Dragut  
**Category**: cs.AI  
**Published**: 2026-07-28  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2607.24707v1  

#### Abstract
Entity-Relationship Diagrams (ERDs) are central to conceptual database design, yet they are typically available only as rendered images rather than machine-readable schemas, limiting AI-assisted database engineering. We introduce ERUnderstand, the first large-scale benchmark for structured understan...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

ERUnderstand: Evaluating Vision-Language Models on Structured ER Diagrams
1. 论文的主要贡献和创新点
✅ 解决的问题
ER图是概念数据库设计的核心，但通常以渲染图片形式存在而非机器可读模式，限制了AI辅助数据库工程的发展；目前缺乏针对结构化ER图理解的标准化评估基准，现有视觉语言模型（VLMs）处理ER图时对弱实体、多值属性、N元关系等关键元素性能极差。
现有方法缺陷：
1）基础SOTA VLMs仅对常见ER元素识别F1>0.74，但对弱实体、多值属性、N元关系等元素理解性能极低；
2）推理增强型VLMs虽整体性能提升15-25%，但仍受语言先验和ER图复杂度影响。

🚀 提出的新方法与思路
**ERUnderstand基准构建**：构建包含2960张ER图的大规模标准化基准，数据集来源涵盖教育资源、真实数据库模式、合成示例，覆盖不同领域、符号、复杂度及扩展实体-关系（EER）构造；为每张图配备标准化机器可读表示，用于对VLMs进行细粒度的ER图模式元素理解评估。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
基准属性 | 首个针对结构化ER图理解的大规模标准化评估基准，覆盖多维度ER图场景
评估精度 | 提供细粒度评估框架，结合ER图的标准化机器可读表示，可精准度量模型对各类ER元素的理解性能
模型适配性 | 可用于评估主流基础VLMs及推理增强型VLMs的ER图理解能力

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
ERUnderstand基准数据集 | 包含2960张多样化ER图（来自教育资源、真实数据库模式、合成示例，覆盖不同领域、符号、复杂度、EER构造），为VLMs在结构化ER图理解任务中的性能提供评估数据

🎯 实验设置与评估指标
任务：评估视觉语言模型（VLMs）对结构化ER图中各类模式元素的理解性能
指标 | 含义
--- | ---
F1值 | 衡量模型对ER图元素的识别与理解性能，数值越高越好（↑）

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
SOTA Vision-Language Models (VLMs) | 基础VLMs | 对常见ER元素识别F1>0.74，对弱实体、多值属性、N元关系等关键元素性能极差
推理增强型VLMs | 改进VLMs | 相比基础VLMs整体性能提升15-25%，仍受语言先验和ER图复杂度影响

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能实验**
根据论文摘要的结果：常见ER元素识别F1>0.74，弱实体F1低至0.28，多值属性F1=0.14，N元关系F1=0.07；推理增强模型整体性能较基础VLMs提升15-25%。
💡 结论：现有VLMs仅对常见ER元素识别性能较好，对弱实体、多值属性、N元关系等关键ER构造的理解性能极差，推理增强模型可提升整体性能，但仍受语言先验和图复杂度限制。

效率对比（FPS / 参数量）：论文未报告
跨域 / zero-shot 迁移：论文未报告
鲁棒性 / 扰动测试：论文未报告
消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1）现有SOTA VLMs对常见ER元素的识别性能较好（F1>0.74），但对弱实体、多值属性、N元关系等关键ER构造的理解性能极差；2）推理增强型VLMs可将VLMs在ER图理解上的整体性能提升15-25%，但仍受语言先验和ER图复杂度的负面影响；3）ERUnderstand是首个针对结构化ER图理解的大规模标准化评估基准，填补了该领域的空白。
- 方法局限性：推理增强型VLMs仍受语言先验及ER图复杂度的限制，部分关键ER元素的理解性能极低，无法满足实际应用需求。
- 未来工作：针对ER图中的弱实体、多值属性、N元关系等难识别元素优化VLMs；进一步改进推理增强模型，降低语言先验的影响，提升对不同复杂度ER图的理解能力。

> ✅ **总结一句话**：ERUnderstand是首个针对结构化ER图理解的大规模标准化基准，可有效评估VLMs在ER图结构化元素识别与理解上的性能，为AI辅助数据库工程提供了重要的评估工具，同时揭示了现有VLMs在关键ER构造理解上的性能缺陷。

</details>

---

### 16. [EviBack: Search-Agent Reinforcement Learning via Evidence-Constrained Teacher Backoff](https://arxiv.org/abs/2607.23955v1)

**Authors**: Xiao Ma, Zhiquan Hu, Yi Wei, Chenchen Zhao, Yijun Chen, Jicheng Zhao, Yuming Li Chuang Dai  
**Category**: cs.AI  
**Published**: 2026-07-28  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2607.23955v1  

#### Abstract
Reinforcement learning enables Agentic RAG systems to learn multi-turn search from verifiable outcome rewards, but all- zero rollout groups provide no comparative signal and may hide useful search behavior. We present EviBack, an evidence- constrained Teacher backoff that supplies auxiliary super- v...

---

### 17. [SymStep: Symbolic Step Verification for Logical Reasoning](https://arxiv.org/abs/2607.23055v1)

**Authors**: Aida Usmanova, Rui Gao, Dilshod Azizov, Ricardo Usbeck, Zangir Iklassov  
**Category**: cs.AI  
**Published**: 2026-07-28  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2607.23055v1  

#### Abstract
Chain-of-thought (CoT) prompting can fail severely on constraint-dense logical reasoning tasks, where unverified errors accumulate silently across steps. We introduce SymStep: an LLM makes one atomic claim at a time (DEDUCE: Alice, pet, Cat), then a lightweight constraint propagator checks the claim...

---

### 18. [Two Regimes of Chain-of-Thought Unfaithfulness: Behavioral Detection Fails Where Models Are Wrong](https://arxiv.org/abs/2607.23458v1)

**Authors**: Suramya R. Angdembay, Dikshant Aryal, Nick Rahimi  
**Category**: cs.CL  
**Published**: 2026-07-28  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2607.23458v1  

#### Abstract
Chain-of-thought (CoT) explanations support oversight only if they are faithful: the stated reasoning must actually produce the answer. Auditing black-box (behavioral) detection of unfaithful CoT against FaithCoT-Bench's human annotations, we find answer correctness structures the problem at every l...

---

### 19. [PTStore (Prefix Tensor Store): Distributed Prefix Caching and Replication for High Throughput Inference Serving](https://arxiv.org/abs/2607.22648v1)

**Authors**: Meghana Maghyastha, Robert Underwood, Randal Burns, Bogdan Nicolae  
**Category**: cs.AI  
**Published**: 2026-07-28  
**Score**: 37.5  
**Type**: new  
**ArXiv ID**: 2607.22648v1  

#### Abstract
Inspired by the design of client caching in Content Delivery Networks (CDNs), PTStore distributes and replicates popular tensors that form reusable KV cache prefixes, which are the main technique used by state of art approaches to accelerate inferences. This reduces the latency of accessing the KV c...

---

### 20. [Gleam: Adaptive Network-Efficient CUDA API Remoting for Cross-Device GPU Sharing over LANs](https://arxiv.org/abs/2607.23115v1)

**Authors**: Zhihao Xu, Hao Zhong, Zeting Zhou, Yuhang Xu, Haoyu Tong, Wei Wang, Jinshan Chen, Keqiang He, Chong Zhu, Shengzhong Liu, Fan Wu, Guihai Chen  
**Category**: cs.DC  
**Published**: 2026-07-28  
**Score**: 37.5  
**Type**: new  
**ArXiv ID**: 2607.23115v1  

#### Abstract
This paper aims to enable computation- and communication-efficient GPU sharing across devices within local area networks (LANs), facilitating ubiquitous AI inference on heterogeneous personal devices. We achieve distributed task offloading via CUDA API remoting. However, beyond raw computation, netw...

---

### 21. [Training Language Models to Cooperate with Inference-Time Controllers](https://arxiv.org/abs/2607.23771v1)

**Authors**: Moumita Choudhury, Vanshaj Khattar, Jing Liu, Toshiaki Koike-Akino, Ankush Chakrabarty, Shlomo Zilberstein, Ye Wang  
**Category**: cs.AI  
**Published**: 2026-07-28  
**Score**: 36.0  
**Type**: new  
**ArXiv ID**: 2607.23771v1  

#### Abstract
Large language model (LLM) performance increasingly depends not only on the base model, but also on the inference-time controller used to organize reasoning. Existing post-training methods, however, typically optimize for a single fixed interaction pattern, despite real deployments relying on divers...

---

### 22. [HeraSys: Collaborative Serving of Multiple LLM Workflows via Fine-Grained End-to-End Optimization](https://arxiv.org/abs/2607.22578v1)

**Authors**: Size Li, Zhiqing Tang, Hongrui Liang, Jianxiong Guo, Jiong Lou, Tian Wang, Weijia Jia  
**Category**: cs.AI  
**Published**: 2026-07-28  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2607.22578v1  

#### Abstract
The proliferation of Large Language Models (LLMs) has shifted serving systems from processing isolated requests to orchestrating high-concurrency, multi-tenant agentic workflows. However, existing solutions typically prioritize intra-workflow optimization, largely neglecting the significant potentia...

---

### 23. [Chart Deception in Vision-Language Models: From Vulnerability to Mitigation](https://arxiv.org/abs/2607.22600v1)

**Authors**: Ridwan Mahbub, Mohammed Saidul Islam, Md Tahmid Rahman Laskar, Mizanur Rahman, Mir Tafseer Nayeem, Enamul Hoque  
**Category**: cs.AI  
**Published**: 2026-07-28  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2607.22600v1  

#### Abstract
Information visualizations are widely used to communicate patterns, trends, and outliers, yet deceptive design choices-such as truncated or inverted axes, distorted aspect ratios, inappropriate encodings, and misleading color mappings-can systematically alter interpretation while preserving the unde...

---

### 24. [Verification-Notebook Learning for Source-Aware Multimodal Misinformation Detection](https://arxiv.org/abs/2607.23581v1)

**Authors**: Junyuan Tan  
**Category**: cs.AI  
**Published**: 2026-07-28  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2607.23581v1  

#### Abstract
Multimodal misinformation verification is challenging because misleading signals may come from different parts of a post and require different forms of evidence. LVLMs are well suited to this task, but their verification performance often depends on the inference procedure applied to each instance. ...

---

### 25. [Do Visual Features Improve Other-Initiated Repair Detection? A Dyadic Multimodal Approach](https://arxiv.org/abs/2607.23845v1)

**Authors**: Anh Ngo, Nicolas Rollet, Catherine Pelachaud, Chlo\'e Clavel  
**Category**: cs.AI  
**Published**: 2026-07-28  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2607.23845v1  

#### Abstract
Other-initiated Self-repair, or in short Other-initiated Repair (OIR), is an essential mechanism in conversational interaction, whereby a recipient signals a problem in speaking, hearing, or understanding, prompting the previous speaker to resolve it. In the case of conversational agents, it is esse...

---

### 26. [Learning Sampling Parameters for Diffusion Models](https://arxiv.org/abs/2607.23488v1)

**Authors**: Arisrei Lim, Yossi Gandelsman  
**Category**: cs.LG  
**Published**: 2026-07-28  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2607.23488v1  

#### Abstract
Text-to-image diffusion models expose many inference-time sampling parameters, including prompts, negative prompts, classifier-free guidance scales, and noise schedules. These parameters are typically manually chosen once and then held fixed across prompts and denoising timesteps, even though differ...

---

### 27. [Self-Boosting Vision-Language Models with Noisy Student On-Policy Self-Distillation](https://arxiv.org/abs/2607.23125v1)

**Authors**: Shuai Wang, Daoan Zhang, Zhe Tang, Hao Cheng, Jiaheng Wei  
**Category**: cs.LG  
**Published**: 2026-07-28  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2607.23125v1  

#### Abstract
Post-training enables vision-language models (VLMs) to understand human instructions and perform various downstream tasks. Current post-training methods usually rely on human-annotated data, distillation from external models, reinforcement learning with human feedback, or verifiable answers. This li...

---

### 28. [Test-Time Coverage: Test-Conditioned Data Curation for Deployment-Aware Learning](https://arxiv.org/abs/2607.22697v1)

**Authors**: Nadine Chang, Maying Shen, Shizhe Diao, Jialiang Wang, Jingde Chen, Thomas Breuel, Pavlo Molchanov, Rafid Mahmood, Jose M. Alvarez  
**Category**: cs.AI  
**Published**: 2026-07-28  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2607.22697v1  

#### Abstract
Deployed AI systems are often trained from broad candidate data pools, necessitating data curation towards the deployment test distribution. However, standard data curation methods score training-side criteria rather than directly optimizing deployment match. We introduce TTCov (Test-Time Coverage),...

---

### 29. [Explainable Reinforcement Learning via Physics-Aware Policy Distillation](https://arxiv.org/abs/2607.24672v1)

**Authors**: Shaker Al-Tamari, Waled Kadour  
**Category**: cs.LG  
**Published**: 2026-07-28  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2607.24672v1  

#### Abstract
In safety-critical sectors such as robotics and automotive engineering, the deployment of Deep Reinforcement Learning (DRL) is often hindered by the black-box nature of deep neural networks. This lack of transparency poses significant challenges for regulatory compliance and human-agent trust. This ...

---

### 30. [TRACE: Business Rule-Grounded Reasoning Curriculum for Knowledge-Preserving Parametric Tool Retrieval in Enterprise LLMs](https://arxiv.org/abs/2607.22639v1)

**Authors**: Sai Shruthi Sistla, Ashutosh Hathidara, Christopher Toukmaji, Mayank Shrivastava, Karthikeyan Asokkumar  
**Category**: cs.AI  
**Published**: 2026-07-28  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2607.22639v1  

#### Abstract
Parametric retrieval enables LLMs to retrieve tools implicitly by assigning each API a unique virtual token and training the model to generate it via constrained beam search. Toolsense shows that this regime has two critical drawbacks: it destroys parametric tool knowledge during training, and its b...

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
