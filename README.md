# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-08-04 08:17:15 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [Practical Online KV Cache Compaction for LLM Agents: An Empirical Study](https://arxiv.org/abs/2608.00902v1)

**Authors**: Yujian Liu, Jiabao Ji, Li An, Rohit Jain, Gungor Polatkan, Siyu Zhu, Shiyu Chang  
**Category**: cs.CL  
**Published**: 2026-08-04  
**Score**: 86.0  
**Type**: new  
**ArXiv ID**: 2608.00902v1  

#### Abstract
LLM agents accumulate long trajectories of reasoning steps, tool calls, and environment feedback, making the KV cache a major inference bottleneck. KV cache compaction can reduce this cost, but most prior methods assume a static context where future queries are known or can be approximated offline. ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Practical Online KV Cache Compaction for LLM Agents: An Empirical Study
1. 论文的主要贡献和创新点
✅ 解决的问题
LLM代理会积累包含推理步骤、工具调用、环境反馈的长轨迹，使得KV缓存成为推理瓶颈；现有KV缓存压缩方法基于静态上下文假设，依赖已知或离线近似的未来查询，无法适配代理所需的在线压缩场景（压缩时未来信息相关性未知，需使用便宜代理查询），这是核心痛点；多数先验KV缓存压缩方法不具备适配LLM代理在线压缩的能力。

🚀 提出的新方法与思路
**适配代理的在线压缩方法**：将token eviction (TE)和attention matching (AM)两种KV缓存压缩方法进行适配，以处理LLM代理的回合级轨迹压缩，无需依赖已知或离线近似的未来查询。
**代理查询源对比研究**：对比边界、重复预填充、延迟未来生成查询等多种便宜代理查询源，评估其在在线压缩中的效果，发现代理查询源的选择是实用在线KV压缩的核心设计。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
场景适配性 | 适配LLM代理的在线动态压缩需求，无需依赖已知或离线近似的未来查询
压缩效率 | 可将KV缓存降低80%
鲁棒性 | 在不完善代理查询源下，TE相比AM更具鲁棒性
推理效率 | TE方法可实现优于无压缩基线的吞吐量

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
BrowseComp-Plus | 用于LLM代理在线KV缓存压缩的主benchmark实验
WideSearch | 用于LLM代理在线KV缓存压缩的主benchmark实验

🎯 实验设置与评估指标
任务为LLM代理的在线KV缓存压缩任务，评估压缩方法的任务性能与推理效率。
指标 | 含义（箭头方向）
--- | ---
任务准确率 | 保留的LLM代理任务执行准确率（↑ 越高越好）
KV缓存压缩率 | KV缓存减少的比例（↑ 越高越好）
吞吐量 | 单位时间内处理的请求数量（↑ 越高越好）

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
No Compaction | 基线方法 | 不进行任何KV缓存压缩操作的基准
Adapted TE | 压缩方法 | 适配LLM代理场景的token eviction压缩方法
Adapted AM | 压缩方法 | 适配LLM代理场景的attention matching压缩方法

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能（BrowseComp-Plus、WideSearch）**
论文未报告具体表号，结果显示：延迟压缩（使用代理未来查询）的Adapted TE方法，在两款数据集上保留了大部分任务准确率，同时将KV缓存降低80%。
💡 结论：在LLM代理的在线KV缓存压缩场景，延迟压缩并使用代理未来查询的Adapted TE方法，可在保留任务性能的同时大幅降低KV缓存开销。

**效率对比**
论文未报告具体表号，结果显示：Adapted TE方法的吞吐量优于无压缩基线。
💡 结论：适配代理的TE压缩方法可在降低KV缓存的同时提升推理效率。

**鲁棒性测试（不完善代理查询源）**
论文未报告具体表号，结果显示：Adapted TE相比Adapted AM更具鲁棒性。
💡 结论：TE在代理在线压缩场景下对不完善代理查询源的鲁棒性优于AM。

**跨域/zero-shot迁移、消融实验**
论文未报告相关实验结果。

4. 关键结论和发现
- 在线KV缓存压缩中，立即压缩代理轨迹会损害性能，延迟压缩以使用代理的未来查询可恢复大部分性能差距。
- 适配代理场景的TE方法，在保留大部分任务准确率的同时，将KV缓存降低80%，且在不完善代理查询下比AM更鲁棒。
- 代理查询源的选择是实用型在线KV压缩的核心设计。
方法局限性：论文未报告
未来工作：论文未报告

> ✅ **总结一句话**：该论文针对LLM代理的在线KV缓存压缩痛点，适配TE与AM为代理场景的在线压缩方法，通过选用合适的代理查询源，实现了低KV缓存开销、高吞吐量且保留任务性能的压缩效果，开展了相关实证研究。

</details>

---

### 2. [Energy-Efficient LLM Serving via Disaggregated Attention--FFN and Flexible Frequency Scaling](https://arxiv.org/abs/2608.01891v1)

**Authors**: Cunchen Hu, Liangliang Xu, Tian Liu, Min Lyu, Yongkun Li, Sa Wang, Shuo Quan, Yanan Yang, Wenda Tang, Yiduo Wang, Fu Yu, Jie Wu  
**Category**: cs.DC  
**Published**: 2026-08-04  
**Score**: 78.5  
**Type**: new  
**ArXiv ID**: 2608.01891v1  

#### Abstract
Large language model (LLM) serving spans diverse applications with stringent service-level objectives (SLOs), often requiring GPUs to run at maximum frequencies and increasing energy consumption. Existing energy-management approaches adapt GPU frequencies only at the request or inference-phase level...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Energy-Efficient LLM Serving via Disaggregated Attention--FFN and Flexible Frequency Scaling

1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：LLM serving需满足严格服务水平目标（SLO），常导致GPU运行在最高频率，能耗显著升高；现有能耗管理方法仅在请求或推理阶段调整GPU频率，未考虑Attention和FFN在频率敏感性上的算子级差异；且推理阶段的A/F最优能耗频率具有可变性，算子级独立A/F频率控制会带来大搜索空间与高通信开销，现有方案未解决该问题。

🚀 提出的新方法与思路
**AFlex框架**：一种联合优化LLM serving的资源配置与GPU频率缩放的框架，包含全局调度器和算子级局部动态电压与频率缩放（DVFS）控制器，用于确定Attention（A）和Feed-Forward Network（FFN）的资源分配及对应的GPU频率；同时引入带动态微批次深度与自适应请求批处理的交错A/F流水线，以减少流水线气泡。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 能源效率 | 仅在摘要中提及可较现有SOTA disaggregated serving降低最多49%的能耗 per token，较现有频率缩放系统降低最多48%的能耗 per token，未提供对应表号等来源定位 |
| 服务合规性 | 满足TTFT（首包时间）和TPOT（每输出token时间）服务水平目标（SLO） |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Production Conversation traces | 用于评估框架在对话类LLM serving场景下的性能 |
| Coding traces | 用于评估框架在编码类LLM serving场景下的性能 |

🎯 实验设置与评估指标
任务为LLM serving，使用NVIDIA A800 GPU，测试模型为Qwen3-32B、Mixtral-8×7B；评估指标为：能耗 per token（↓越低越好）、TTFT（↓越低越好）、TPOT（↓越低越好）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 现有SOTA disaggregated serving | 基准对比方法 | 仅在请求或推理阶段调整GPU频率，未考虑算子级A/F的频率敏感性差异 |
| 现有频率缩放系统 | 基准对比方法 | 未针对A/F算子级特性优化频率控制策略 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告带明确表号的任何定量实验结果，所有提及的性能数值均来自论文摘要，未提供对应实验的表号、图号等来源定位；其余实验（主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）论文未报告相关内容。

4. 关键结论和发现
- 主要发现：1. LLM serving中，Attention和FFN的能耗最优频率存在差异，且随推理阶段、 workload、系统配置变化；2. 现有仅在请求或推理阶段调整GPU频率的方法、算子级独立A/F频率控制方式，存在能耗高、搜索空间大、通信开销高的问题；3. 提出的AFlex框架可缓解上述问题，在满足SLO的同时降低LLM serving能耗。
- 方法局限性：论文未报告明确说明的方法局限性。
- 未来工作：论文未报告明确说明的未来工作方向。

> ✅ **总结一句话**：AFlex是一种针对LLM serving的联合优化资源配置与GPU频率缩放的框架，可在满足TTFT和TPOT服务水平目标的前提下，降低LLM serving的能耗。

</details>

---

### 3. [TRAM: Enhancing Multimodal Reasoning with Trajectory-Derived Auxiliary Memory](https://arxiv.org/abs/2608.01922v1)

**Authors**: Kang Liu, Zijing Wang, Yongkang Liu, Mengjie Zhao, Xiaocui Yang, Shi Feng, Yifei Zhang, Daling Wang  
**Category**: cs.CL  
**Published**: 2026-08-04  
**Score**: 65.5  
**Type**: new  
**ArXiv ID**: 2608.01922v1  

#### Abstract
Multimodal Large Reasoning Models (MLRMs) have achieved strong performance on tasks requiring visual understanding and multi-step inference. However, as reasoning trajectories grow, models may become less effective at using information established earlier in the context, increasing the risk of reaso...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

TRAM: Enhancing Multimodal Reasoning with Trajectory-Derived Auxiliary Memory
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多模态大推理模型（MLRMs）在长推理轨迹场景下，难以有效利用之前建立的信息，增加了推理错误风险；现有主流方法主要通过维持推理过程中的视觉 grounding 解决该问题，但忽略了推理生成的任务特定关系、约束和中间结论等推理派生信息的衰减，影响模型推理正确性。

🚀 提出的新方法与思路
**TRAM（Trajectory-derived Auxiliary Memory）模块**：该方法为训练-free方法，在标准解码框架基础上新增来自模型自身推理轨迹的辅助记忆路径；TRAM将已完成的推理整合为紧凑的潜在记忆，通过快、慢循环流在线更新该记忆，再通过轻量残差路径将记忆反馈到选定的解码器层。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 训练成本 | 无需额外训练，属训练-free方法 |
| 推理信息利用 | 跨推理阶段保留并整合推理派生信息，解决长轨迹下该类信息衰减问题 |
| 任务适配性 | 适用于数学、科学、通用视觉推理三类任务 |
| 模型适配性 | 可适配多种MLRM变体 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 多模态推理性能测试（共8个基准） |

🎯 实验设置与评估指标
任务为数学、科学、通用视觉推理任务，具体评估指标论文未明确给出相关说明：
| 指标 | 含义 |
| --- | --- |
| 论文未报告 | 论文未明确说明指标的具体类型及方向 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未明确列举具体基线方法 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能
论文未报告
2. 效率对比（FPS / 参数量）
论文未报告
3. 跨域 / zero-shot 迁移
论文未报告
4. 鲁棒性 / 扰动测试
论文未报告
5. 消融实验
论文未报告

4. 关键结论和发现
- 主要发现：① 多模态推理正确性不仅与图像属性相关，更取决于推理轨迹是否跨阶段保留并整合推理派生信息；② TRAM作为训练-free方法，可提升MLRMs在数学、科学、通用视觉推理任务上的性能；③ TRAM可适配多种MLRM变体。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：TRAM是训练-free的辅助记忆增强方法，通过利用模型自身推理轨迹派生的记忆信息，提升多模态大推理模型在长推理场景下的视觉推理性能，解决了长轨迹下推理派生信息衰减的问题。

</details>

---

### 4. [How Hard Does It Think? Analyzing Step-Aware Reasoning Energy in LLM Chain-of-Thought Trajectories](https://arxiv.org/abs/2607.28674v1)

**Authors**: Hui Wei, Junda Wu, Sheldon Yu, Sizhe Zhou, Yizhu Jiao, Ming Zhong, Bowen Jin, Tong Yu, Shijia Pan, Jiawei Han, Julian McAuley  
**Category**: cs.AI  
**Published**: 2026-08-04  
**Score**: 63.5  
**Type**: new  
**ArXiv ID**: 2607.28674v1  

#### Abstract
Understanding how computational effort is allocated across individual chain-of-thought (CoT) reasoning steps remains an open challenge: existing interpretability methods rely on output-level signals or collapse processing depth into a single trajectory-level scalar, leaving step-wise effort opaque. ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

How Hard Does It Think? Analyzing Step-Aware Reasoning Energy in LLM Chain-of-Thought Trajectories
1. 论文的主要贡献和创新点
✅ 解决的问题
现有LLM可解释性方法存在两方面缺陷：一是依赖输出级信号，无法揭示推理过程内部的细节；二是将处理深度简化为单轨迹级标量，导致步骤级的计算投入（effort）处于不透明状态。

🚀 提出的新方法与思路
**Step-Aware Reasoning Energy (SARE)**，是一个几何框架：通过计算相邻Transformer层中token隐状态的Gram矩阵之间的Centered Kernel Alignment (CKA)，在单个Chain-of-Thought（CoT）步骤的粒度上量化计算投入，无需特征向量对齐或集群对应即可捕捉token间的关系结构；同时将该推理能量与推理的语义演进关联，把CoT轨迹建模为潜在语义状态的转换过程。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 信号粒度 | 提供CoT推理步骤级的计算投入量化，避免现有方法的输出级或轨迹级信号的局限 |
| 结构捕捉 | 基于CKA捕捉token间的关系结构，无需特征向量对齐或集群对应 |
| 语义关联 | 关联推理能量与推理的语义演进，建模为潜在语义状态转换，更贴合推理本质 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 六个推理基准 | 用于评估SARE在推理步骤级计算投入量化上的有效性 |

🎯 实验设置与评估指标
任务：在三个开放权重LLMs上，分析CoT轨迹的步骤级推理能量及SARE特征的预测性能。
| 指标 | 含义 |
| --- | --- |
| 论文未报告 | 论文未明确报告具体指标的定义及方向 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 输出级置信度基线 | 输出级信号基线 | 依赖模型输出层的置信信号，而非内部步骤级的几何动态信息 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（推理任务）**
论文未报告
💡 结论：论文未报告相关结果，无法得出对应结论。

**表2：效率对比（FPS/参数量）**
论文未报告
💡 结论：论文未报告相关结果，无法得出对应结论。

**表3：跨域/zero-shot迁移性能**
论文未报告
💡 结论：论文未报告相关结果，无法得出对应结论。

**表4：鲁棒性/扰动测试性能**
论文未报告
💡 结论：论文未报告相关结果，无法得出对应结论。

**表5：消融实验结果**
论文未报告
💡 结论：论文未报告相关结果，无法得出对应结论。

仅明确的定性实验结果：在六个推理基准和三个开放权重LLMs上的实验发现：
1. 推理能量在不同步骤类型间分布高度非均匀，存在轨迹级指标无法察觉的阶段式转换；
2. 错误CoT轨迹在关键推理节点的推理能量系统性低于正确轨迹；
3. SARE-based特征在多数设置下匹配或优于输出级置信度基线的性能。

4. 关键结论和发现
- 主要发现：
  1. LLM-CoT推理的步骤级计算投入（能量）呈非均匀分布，存在阶段式转换特性，现有轨迹级指标无法捕捉该特性；
  2. 错误推理轨迹在关键推理节点的计算投入显著低于正确推理轨迹，可作为判断推理正确性的潜在信号；
  3. SARE能够有效捕捉LLM-CoT的内部几何动态，其生成的特征携带了超出表面输出信号的预测信息，性能优于或匹配传统输出级置信度信号。
- 方法局限性：论文未报告明确的局限性内容。
- 未来工作：论文未报告明确的未来工作方向。

> ✅ **总结一句话**：本文提出的SARE几何框架，实现了LLM-CoT推理步骤级计算投入的量化，揭示了推理过程中内部动态的非均匀性与预测价值，弥补了现有可解释性方法在步骤级信号捕捉上的不足。

</details>

---

### 5. [Does Accuracy Equal Evidence? Reasoning Faithfulness under KV Cache Compression](https://arxiv.org/abs/2608.01631v1)

**Authors**: Mengting Ai, Jingrui He, Yue Guo  
**Category**: cs.CL  
**Published**: 2026-08-04  
**Score**: 62.5  
**Type**: new  
**ArXiv ID**: 2608.01631v1  

#### Abstract
KV cache compression is commonly evaluated by final-answer accuracy, implicitly assuming that preserving the answer also preserves the reasoning that supports it. We test this assumption for large reasoning models and show that it can fail: under compression, correct answers and the validity of thei...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

《Does Accuracy Equal Evidence? Reasoning Faithfulness under KV Cache Compression》
1. 论文的主要贡献和创新点
✅ 解决的问题
现有KV缓存压缩方法普遍以最终答案准确率为核心评估标准，默认假设保留答案即可同步保留支撑答案的推理过程，但该假设在大型推理模型中不成立：压缩后正确答案与对应可见支持理由的有效性会以不同速率被保留，存在答案-证据差距，现有评估维度未覆盖推理保真度的损失。

🚀 提出的新方法与思路
**受控固定追踪重放协议**：固定推理内容不变，隔离验证压缩操作是否能保留已有追踪中的可用信息，用于独立评估压缩对推理过程的影响。
**多维度评估框架**：除最终答案准确率外，新增答案链一致性、扰动保真度两个评估维度，全面衡量压缩后推理的完整性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 评估全面性 | 现有方法仅评估最终答案准确率，本研究新增推理过程相关指标，覆盖答案与推理的双重保留情况 |
| 问题定位精准性 | 通过覆盖保留的量化对照实验，明确压缩失败源于推理追踪内容的丢失，而非KV内存减少本身，为优化提供了明确方向 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 数学推理任务数据集 | 用于数学推理任务评估 |
| 科学QA任务数据集 | 用于科学问答任务评估 |
| 临床计算任务数据集 | 用于临床计算任务评估 |
| 长上下文检索任务数据集 | 用于长上下文检索任务评估 |

🎯 实验设置与评估指标
在数学推理、科学QA、临床计算、长上下文检索四个任务上开展KV压缩方法的评估，评估指标如下：
| 指标 | 含义（箭头） |
| ---- | ---- |
| 最终答案准确率 | 越高越好（↑） |
| 答案链一致性 | 越高越好（↑） |
| 扰动保真度 | 越高越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Token-eviction类KV压缩方法（共十种） | KV缓存压缩方法 | 可保持竞争性最终答案准确率，但会严重损害答案链一致性与扰动保真度 |
| 覆盖保留的量化控制方法 | KV缓存压缩方法 | 受压缩操作影响较小，推理相关指标下降幅度远小于token-eviction方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体定量数值及对应表号、图号，仅给出定性实验结果：
- 针对各个子实验（主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）：论文未报告具体内容。
- 核心定性结论：Token-eviction类方法存在答案-证据差距，即能维持高答案准确率但推理保真度大幅下降；覆盖保留的量化方法受压缩影响更小，证明答案-证据差距源于推理追踪内容丢失而非KV内存减少本身。

💡 结论：KV缓存压缩中，答案准确率与推理证据保真度的保留速率存在差异，token-eviction方法的缺陷是推理内容丢失导致的。

4. 关键结论和发现
- 主要发现：
① KV缓存压缩中存在“答案-证据差距”，即最终答案准确率与支撑答案的推理证据保真度保留速率不同；
② Token-eviction类KV压缩方法可在保持高答案准确率的同时，严重损害推理过程的有效性；
③ 压缩失败的核心原因是推理追踪内容的丢失，而非KV内存减少本身，覆盖保留的量化方法可缓解该问题。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本研究揭示了现有KV缓存压缩评估仅依赖最终答案准确率的不足，通过设计多维度评估和对照实验，证明答案与推理证据的保留存在不同步问题，为KV缓存压缩的推理保真度优化提供了新方向。

</details>

---

### 6. [DART: Decoded Attention over Recurrent States for Efficient Long-Context Sequence Modeling](https://arxiv.org/abs/2608.02032v1)

**Authors**: Yixiao Qian, Song Chen, Pengkai Wang, Jiaxu Liu, Shengze Cai, Chao Xu  
**Category**: cs.LG  
**Published**: 2026-08-04  
**Score**: 58.0  
**Type**: new  
**ArXiv ID**: 2608.02032v1  

#### Abstract
Modern language models are built primarily from Transformers, recurrent models, and their hybrid architectures. Transformers rely on token-level attention memories, while recurrent models such as state space models (SSMs) and linear attention maintain compact recurrent states. These architectures ar...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

DART: Decoded Attention over Recurrent States for Efficient Long-Context Sequence Modeling
1. 论文的主要贡献和创新点
✅ 解决的问题
- Transformer架构依赖token级注意力记忆，在长上下文场景下存在缓存开销大的缺陷。
- 循环模型（如状态空间模型SSMs、线性注意力）虽采用紧凑的循环状态，但通常与Transformer单独或层间交替使用，不存在共享的记忆表示可同时支持循环压缩和注意力式检索。

🚀 提出的新方法与思路
**Decoded Attention over Recurrent States (DART)**：保留Mamba-2分块扫描产生的分块状态贡献作为分块状态记忆；从该分块状态记忆中解码token条件的键与值；对解码得到的键值对执行State-Memory Attention (SMA)计算；通过门控残差连接将SMA的检索输出与原生Mamba-2的输出结合；训练层面重用Mamba-2的分块扫描逻辑，且将SMA实现为FlashAttention风格的计算，支持实用的模型训练。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 推理缓存开销 | 大幅降低长上下文下的长度依赖推理缓存 |
| 序列处理能力 | 相比Mamba-2，提升关联召回和检索性能，同时保持通用语言模型的质量 |
| 训练可行性 | 兼容现有Mamba-2的分块扫描实现，SMA采用FlashAttention风格设计，具备实用训练条件 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告具体使用的数据集信息 |

🎯 实验设置与评估指标
任务：长上下文序列建模相关的通用语言建模、关联召回与检索任务。
| 指标 | 含义 |
| ---- | ---- |
| 论文未报告 | 论文未报告具体的评估指标及对应评价方向 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Mamba-2 | 循环状态空间模型 | 原生的循环序列建模基线方法，基于紧凑循环状态实现序列处理 |
| 匹配注意力基线 | Transformer类基线 | 与DART匹配的注意力类序列建模基线，用于对比性能 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**推理缓存节省对比**
| 指标 | DART结果 | 匹配注意力基线结果 |
| ---- | ---- | ---- |
| 长度依赖推理缓存 | 大幅降低 | 基准值 |
💡 结论：论文指出，在块大小S=256、状态大小N=128的场景下，DART相比匹配注意力基线大幅减少了长度依赖的推理缓存。
其他实验：主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验，论文未报告相关内容。

4. 关键结论和发现
- 主要发现：1）现有Transformer与循环模型的架构设计未兼顾循环压缩和注意力式检索的需求，缺乏共享记忆表示；2）DART通过复用Mamba-2的分块循环状态，结合解码注意力设计的SMA，在降低推理缓存的同时提升了关联召回与检索性能，且未损失通用语言建模质量。
- 方法局限性：论文未报告具体的方法局限性信息。
- 未来工作：论文未报告具体的未来工作方向。

> ✅ **总结一句话**：DART是一种用于高效长上下文序列建模的新方法，通过复用Mamba-2的分块循环扫描逻辑并结合解码注意力设计，大幅降低了长上下文下的推理缓存开销，同时提升了关联召回与检索能力并保持了通用语言建模的质量。

</details>

---

### 7. [Attend to Your Own Thoughts: Breaking the Barrier for Post-Training Quantization of Reasoning LLMs through the Lens of 1.58-Bit Quantization](https://arxiv.org/abs/2608.01078v1)

**Authors**: Shigeng Wang, Chao Li, Yangyuxuan Kang, Jiawei Fan, Anbang Yao  
**Category**: cs.CL  
**Published**: 2026-08-04  
**Score**: 56.5  
**Type**: new  
**ArXiv ID**: 2608.01078v1  

#### Abstract
We propose ScaleQ-1.58, a scalable ternary post-training quantization (PTQ) framework for reasoning LLMs. Its core insight stems from an empirical finding: although modern LLMs are typically trained to exhibit chain-of-thought reasoning capabilities, in the PTQ regime, even the latest CAT-Q method b...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Attend to Your Own Thoughts: Breaking the Barrier for Post-Training Quantization of Reasoning LLMs through the Lens of 1.58-Bit Quantization
1. 论文的主要贡献和创新点
✅ 解决的问题
现代LLM经训练具备思维链推理能力，但在推理LLM的后训练量化（PTQ）阶段，采用忽略模型推理过程的传统校准方案时，即使是基于学习型可微分三元化的最新CAT-Q方法，在挑战性数学和编码任务上仍会出现性能崩溃。
🚀 提出的新方法与思路
**Attend to Your Own Thoughts (AYOT)**：一种简单的校准方法，在三元化过程中，使用预训练的高精度目标LLM在适当校准样本集上生成的推理轨迹和最终答案作为上下文输入，与对应的问题一同参与校准；ScaleQ-1.58是将AYOT与CAT-Q集成形成的可扩展三元PTQ框架，用于推理LLM。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 校准token成本 | 仅需4M校准token，对比BitNet b1.58 2B4T，Qwen3-4B三元化时绝对增益达8.97%，校准token需求仅为其1/1,000,000 |
| 架构泛化性 | 可良好泛化于dense和MoE架构，性能随模型规模增大而提升（最高支持235B参数） |
| 任务泛化性 | 可覆盖数学、编码、科学逻辑推理、常识推理、基础语言生成等不同难度的各类任务 |
| 性能扩展性 | 性能随校准token数量增加而持续提升，且AYOT可泛化至其他量化位宽 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告具体数据集名称，仅提及使用适当的校准样本集 | 用于生成推理轨迹及作为校准的参考样本 |
🎯 实验设置与评估指标
任务为数学、编码等推理类任务；论文未明确报告具体评估指标名称，仅提及性能表现（含绝对增益、相对性能比例等），指标方向论文未说明。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| CAT-Q | 学习型可微分三元化方法 | 现有三元量化方法，采用忽略模型推理过程的传统校准方案时，在挑战性推理任务上会出现性能崩溃 |
| BitNet b1.58 2B4T | 现有1.58-bit量化方法 | 性能参考基线，需大量校准token |
| ScaleQ-1.58 | 提出的量化框架 | 集成AYOT与CAT-Q的三元PTQ框架，适配推理LLM量化 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体实验对应的表号、图号，仅在摘要中提及相关结果：
- Qwen3-1.7B经ScaleQ-1.58三元量化后，在4个数学和编码任务上的平均性能达到BitNet b1.58 2B4T的90.52%以上。
- Qwen3-4B经ScaleQ-1.58三元量化后，相对BitNet b1.58 2B4T的绝对增益为8.97%，校准token需求仅为其1/1,000,000。
- ScaleQ-1.58可泛化至dense和MoE架构，性能随模型规模增大而提升（最高支持235B参数）。
- ScaleQ-1.58可泛化至不同难度的数学、编码、科学逻辑推理、常识推理、基础语言生成等任务，性能随校准token数量增加而持续提升，且AYOT可泛化至其他量化位宽。
💡 结论：ScaleQ-1.58框架结合AYOT校准方法，在大幅降低推理LLM三元量化的校准token需求的同时，保持了良好的性能与泛化性。

4. 关键结论和发现
- 主要发现
1. 推理LLM的PTQ中，忽略模型推理过程的传统校准方案会导致性能崩溃，需引入推理轨迹作为校准上下文优化。
2. ScaleQ-1.58框架具备优异的校准成本效率、架构泛化性、任务泛化性，性能随校准规模提升。
3. AYOT校准方法通用性强，可适配其他量化位宽。
- 方法局限性：论文未报告相关内容。
- 未来工作：论文未报告相关内容。

> ✅ **总结一句话**：论文提出的ScaleQ-1.58框架，通过引入基于高精度LLM推理轨迹的AYOT校准方法，实现了低校准成本、高泛化性的推理大语言模型三元后训练量化。

</details>

---

### 8. [Start Classifying: Categorical Critics for LLM Reinforcement Learning](https://arxiv.org/abs/2608.02181v1)

**Authors**: Zhijian Zhou, Long Li, Xuan Zhang, Zongkai Liu, Yulei Qin, Ke Li, Xing Sun, Xiaoyu Tan, Chao Qu, Yuan Qi  
**Category**: cs.LG  
**Published**: 2026-08-04  
**Score**: 55.5  
**Type**: new  
**ArXiv ID**: 2608.02181v1  

#### Abstract
Proximal Policy Optimization (PPO) for large language models typically trains its critic by mean-squared-error (MSE) regression on scalar value targets. Although scalar MSE is statistically valid for estimating the conditional expected return, sparse binary rewards in reinforcement learning with ver...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# Start Classifying: Categorical Critics for LLM Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
传统用于大语言模型近端策略优化（PPO）的批评者采用标量均方误差（MSE）回归训练，在带可验证奖励的强化学习（RLVR）场景中，因稀疏二元奖励导致批评者的优化与校准至关重要，小的价值误差会直接扭曲PPO使用的标量优势，影响训练效果；单纯增大输出头或采用二元分类的批评者，无法解释性能提升的核心原因。

🚀 提出的新方法与思路
**HL-Gauss PPO**：将传统PPO的标量MSE批评者头替换为基于离散价值支持的分类预测器，采用经平滑HL-Gauss目标训练的交叉熵损失优化；其输出解码为标量期望后用于标准广义优势估计（GAE）与PPO计算，演员更新逻辑保持不变，并非分布式方法。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 批评者校准 | 降低Brier score与校准误差 |
| 优势质量 | 生成更对称、更低方差的优势信号 |
| 任务性能 | 在数学推理、工具增强数学、Search-R1任务及Qwen2.5、Qwen3模型上，优于传统强PPO与DAPO基线方法 |
| 方法兼容性 | 无需调整原有PPO的演员训练流程 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 数学推理、工具增强数学、Search-R1 | 性能基准测试 |
| 推理前缀集合 | 批评者的校准与优势相关评估 |

🎯 实验设置与评估指标
任务：LLM的带可验证奖励的强化学习（RLVR）
| 指标 | 含义（箭头） |
| ---- | ---- |
| Brier score | 评价批评者预测准确性（↓越低越好） |
| 校准误差 | 衡量批评者校准程度（↓越低越好） |
| 任务性能 | 衡量模型在目标任务上的表现 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 传统PPO | 基线方法 | 采用标量MSE损失训练批评者 |
| DAPO | 强基线方法 | 现有针对LLM的强化学习基线方法 |
| one-hot批评者 | 控制实验方法 | 用于验证性能增益来源 |
| two-hot批评者 | 控制实验方法 | 用于验证性能增益来源 |
| Bernoulli two-bin批评者 | 控制实验方法 | 用于验证性能增益来源 |

3. 主要实验结果和性能指标
📊 定量结果汇总
（注：论文未提供具体表号、图号及定量数值，仅定性报告以下内容）
1. 主benchmark性能：HL-Gauss PPO在数学推理、工具增强数学、Search-R1任务的Qwen2.5、Qwen3模型上，持续优于强PPO与DAPO基线方法；论文未报告具体性能数值。
2. 消融实验：控制实验结果显示，单纯增大输出头或采用二元分类的批评者无法解释HL-Gauss PPO的性能增益，证明其优势源于分类式价值学习的设计。
3. 批评者校准与优势指标：HL-Gauss PPO可降低Brier score与校准误差，生成更对称、更低方差的优势信号；论文未报告这些指标的具体数值。
4. 效率对比：论文未报告
5. 跨域/zero-shot迁移：论文未报告
6. 鲁棒性/扰动测试：论文未报告

💡 结论：HL-Gauss PPO在多个LLM强化学习任务上相比传统PPO及现有强基线实现了性能提升，核心优势来自分类式批评者的设计而非输出头或二元分类的简单调整。

4. 关键结论和发现
- 主要发现：① HL-Gauss PPO通过替换分类式批评者，可有效提升LLM在RLVR场景下的性能；② 该方法能优化批评者校准质量、生成更高质量的优势信号；③ 性能增益源于分类式价值学习设计，而非单纯的输出头或二元分类调整。
- 方法局限性：论文未报告方法的效率、跨域/zero-shot迁移能力、鲁棒性/扰动测试等方面结果，也未覆盖更多LLM模型或RLVR任务场景。
- 未来工作：探索分类式批评者在更多LLM RLVR场景的应用，进一步优化HL-Gauss目标函数及训练流程。

> ✅ **总结一句话**：论文提出HL-Gauss PPO方法，以基于离散价值支持的分类式批评者替代传统标量MSE批评者，在数学推理等多个任务的Qwen系列模型上提升了LLM强化学习的性能，同时优化了批评者的校准与优势质量。

</details>

---

### 9. [LongChart VQA: A Comprehensive Benchmark for MLLMs with Complex Multi-Chart Reasoning](https://arxiv.org/abs/2608.01328v1)

**Authors**: Ziyan Xiao, Yinghao Zhu, Wenting Zhang, Heaju Kim, Lequan Yu  
**Category**: cs.CL  
**Published**: 2026-08-04  
**Score**: 54.5  
**Type**: new  
**ArXiv ID**: 2608.01328v1  

#### Abstract
Multimodal large language models (MLLMs) are rapidly evolving with expanded context windows and stronger reasoning capabilities, enabling multi-chart understanding and multi-step inference. These abilities are increasingly important as MLLMs are adopted in complex agentic tasks. However, existing be...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：LongChart VQA: A Comprehensive Benchmark for MLLMs with Complex Multi-Chart Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多模态大语言模型（MLLMs）相关基准多侧重单图表感知，简单图表间连接无法评估MLLMs的复杂多图表推理能力；而MLLMs的上下文窗口扩展和推理能力提升，使得多图表理解与多步骤推理在复杂智能体任务中愈发重要，亟需适配的评估基准。

🚀 提出的新方法与思路
**潜在图支持的合成流水线**：设计由潜在图支撑的合成流水线，以此构建LongChart基准，该基准的VQA数据集平均包含6.5张图像与31.2个问题，用于评估MLLMs的复杂多图表推理能力。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 评估范围 | 突破现有基准仅覆盖单图表感知的局限，针对复杂多图表场景设计，可评估MLLMs的多步骤、多图表推理能力 |
| 数据集特性 | VQA集平均包含6.5张图像与31.2个问题，适配多图表、复杂推理的评估需求 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| LongChart | 作为评估MLLMs复杂多图表推理能力的专用基准 |

🎯 实验设置与评估指标
任务为多图表视觉问答（VQA），评估指标论文未明确报告具体名称。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 10个state-of-the-art MLLMs | 多模态大语言模型 | 代表当前最优水平的MLLMs |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未提供具体实验对应的表号及各项性能的具体数值，仅报告核心趋势：随着计算复杂度增加，MLLM在LongChart基准的多图表VQA任务中准确率下降，且不同模型间表现差异显著。
除上述趋势外，主benchmark性能具体数值、效率对比、跨域/zero-shot迁移、鲁棒性扰动测试、消融实验等相关内容，论文未报告。

4. 关键结论和发现
- 主要发现：① MLLMs在复杂多图表VQA任务中，准确率随计算复杂度提升而下降，模型间表现差异明显；② 推理模式、辅助工具、对图像扰动的鲁棒性是影响MLLMs多图表推理性能的关键因素；③ 现有SOTA MLLMs在复杂多图表推理能力上存在不足，需针对性研究改进。
- 方法局限性：论文未报告。
- 未来工作：探索提升MLLMs复杂多图表推理能力的方向。

> ✅ **总结一句话**：LongChart是针对MLLMs复杂多图表推理的综合基准，其VQA集平均含6.5张图像与31.2个问题，通过评估10个SOTA MLLMs，揭示了MLLM准确率随计算复杂度增加而下降的核心趋势，为后续多图表推理研究提供了评估基础与方向。

</details>

---

### 10. [Native Multilingual Chain-of-Thought Reasoning in Low-Resource Southeast Asian Languages](https://arxiv.org/abs/2608.00533v1)

**Authors**: Sean Gip Lim, William Chandra Tjhi, Hai Leong Chieu  
**Category**: cs.CL  
**Published**: 2026-08-04  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2608.00533v1  

#### Abstract
Large Language Models have achieved substantial progress in reasoning capabilities. Yet in low-resource native settings, many suffer from cross-lingual collapse, reverting to English during intermediate steps that require complex logical reasoning. This presents a cold-start bottleneck for policy op...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Native Multilingual Chain-of-Thought Reasoning in Low-Resource Southeast Asian Languages
1. 论文的主要贡献和创新点
✅ 解决的问题
大型语言模型在低资源原生东南亚语言场景中存在两大核心痛点：一是跨语言崩溃，即需复杂逻辑推理的中间步骤会退化为英语；二是标准微调易引发跨语言表示漂移，导致灾难性遗忘，形成策略优化的冷启动瓶颈。

🚀 提出的新方法与思路
**Onramp-Sequence Cross-Distillation (OSCD)**：一种后训练算法，在生成式训练rollout过程中，通过集成翻译agent循环将高资源推理轨迹投影至低资源词汇子空间，确保动态生成的参考样本能稳定且高效地用于微调；同时耦合参考语言与目标语言推理轨迹的联合嵌入语义对齐，弥合成对跨语言表示差距。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 跨语言推理稳定性 | 缓解低资源东南亚语言下LLM推理时向英语退化的跨语言崩溃问题 |
| 微调稳定性 | 避免标准微调导致的跨语言表示漂移引发的灾难性遗忘 |
| 推理效能 | 提升低资源东南亚语言的数学推理性能 |
| 语言去偏效果 | 联合嵌入语义对齐组件可提升推理的语言去偏性能 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| AIME25 | 数学推理综合评估 |
| HMMT25 | 数学推理综合评估 |

🎯 实验设置与评估指标
任务：低资源东南亚语言的原生数学思维链推理
| 指标 | 含义 |
| ---- | ---- |
| 整体数学推理性能 | 越高越好 |
| 语言去偏性能 | 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 翻译-only基线 | 对照方法 | 仅采用翻译方式构建的基线方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告明确对应表号的实验结果。

4. 关键结论和发现
- 主要发现
  1. 本文提出的OSCD后训练算法可有效解决低资源原生东南亚语言场景下LLM的跨语言崩溃问题，同时避免标准微调的灾难性遗忘问题；
  2. OSCD中的联合嵌入语义对齐组件对提升低资源语言推理的语言去偏效果具有重要作用；
  3. OSCD适用于低资源东南亚语言的数学推理任务，可带来性能提升。
- 方法局限性
论文未报告
- 未来工作
论文未报告
> ✅ **总结一句话**：本文提出OSCD后训练算法，通过集成翻译agent循环与联合嵌入语义对齐，实现低资源东南亚语言的原生思维链推理，缓解跨语言崩溃与微调灾难性遗忘，提升数学推理及语言去偏性能。

</details>

---

### 11. [Cross-Task Dissociation in Frontier Vision-Language Model Theory of Mind](https://arxiv.org/abs/2608.00261v1)

**Authors**: Kejia Zhang, Youran Sun, Chugang Yi, Haizhao Yang  
**Category**: cs.CL  
**Published**: 2026-08-04  
**Score**: 52.5  
**Type**: new  
**ArXiv ID**: 2608.00261v1  

#### Abstract
Do frontier vision-language models present a coherent Theory-of-Mind (ToM) profile across tasks, matching the same human reference group, or does that profile fragment from one paradigm to the next? We evaluate a shared panel of nine frontier VLMs on two psychology-derived benchmarks: the Keysar Dir...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Cross-Task Dissociation in Frontier Vision-Language Model Theory of Mind
1. 论文的主要贡献和创新点
✅ 解决的问题
现有研究未系统验证前沿视觉语言模型（VLM）的心理理论（ToM）能力是在不同心理学任务范式间保持连贯、匹配人类参照组，还是会在不同范式下碎片化、与人类参照组的匹配度不一致，本研究聚焦解决这一核心矛盾。

🚀 提出的新方法与思路
**多范式ToM评估框架**：构建基于心理学来源的ToM多任务评估框架，选取Keysar Director Task（含自我中心干扰的视觉视角采择任务）与Frith-Happé animated triangles（采用Castelli rubric评分的纯运动意图归因任务），对9个前沿VLM进行统一评估，并对比典型发展成人（TD）、高功能自闭症成人（HF-ASD）、儿童三类人类参照组的表现。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| ToM评估范式 | 采用心理学衍生的双任务评估框架，覆盖视觉视角采择与意图归因两类核心ToM能力 |
| 评估对象 | 针对9个前沿VLM进行统一评估，避免单模型评估的偏差 |
| 参照组设计 | 引入多类人类参照组，细化ToM表现的参照维度 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| Keysar Director Task | 评估前沿VLM的视觉视角采择（含自我中心干扰）能力 |
| Frith-Happé animated triangles | 采用Castelli rubric评分，评估前沿VLM的纯运动意图归因能力 |

🎯 实验设置与评估指标
任务：评估9个前沿VLM在两类心理学衍生ToM任务上的表现，与多类人类参照组对比。
| 指标 | 含义 |
| ---- | ---- |
| 自我中心错误率（Keysar Task） | 无思维链（chain-of-thought）时，模型在视觉视角采择任务中出现自我中心错误的试验占比，越低越好 ↓ |
| ToM profile与参照组距离（三角形任务） | 模型的ToM profile与TD、HF-ASD人类参照组均值的距离，距离越小越接近该参照组 |

⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
**Keysar Director Task实验**
论文未提供该实验相关的表号，定量结果如下：无思维链时，9个前沿VLM在该任务的自我中心错误表现类儿童，模型间差异显著，思维链可挽救部分模型的表现。
💡 结论：无思维链时前沿VLM在Keysar Director Task上呈现类儿童的自我中心错误特征，思维链对部分模型表现有提升作用。

**Frith-Happé动画三角形实验**
论文未提供该实验相关的表号，定量结果如下：前沿VLM整体对意图归因不足，ToM profile距HF-ASD均值的距离是距TD均值的三倍多，仅Goal-Directed、Random模型接近TD；无模型在两个任务上均最接近TD，同一模型在两任务间的ToM表现与人类参照组的匹配度冲突。
💡 结论：前沿VLM在不同ToM任务间存在跨任务解离，在Frith-Happé任务上更接近HF-ASD，且无模型在两类任务上均匹配典型发展成人的ToM表现。

其余实验（效率对比、跨域/zero-shot迁移、鲁棒性测试、消融实验）：论文未报告

4. 关键结论和发现
- 2-3条主要发现
  1. 前沿VLM的ToM能力存在跨任务解离，无模型在Keysar Director Task与Frith-Happé动画三角形任务上均匹配典型发展成人的ToM表现，同一模型在两任务上的表现与人类参照组的匹配度冲突。
  2. 在Keysar Director Task中，无思维链时前沿VLM呈类儿童的自我中心错误特征，模型间差异显著，思维链可提升部分模型的表现。
  3. 在Frith-Happé动画三角形任务中，前沿VLM整体意图归因不足，ToM profile更接近高功能自闭症成人（HF-ASD）的表现，仅少数特定模型接近典型发展成人（TD）。
- 方法局限性：仅评估了9个前沿VLM在两个心理学衍生ToM任务上的表现，未覆盖更多ToM范式或模型，结果的泛化性有待验证。
- 未来工作：可扩展更多ToM任务与模型，进一步探究跨任务解离的根源，开发提升VLM ToM能力一致性的方法。

> ✅ **总结一句话**：本文系统评估9个前沿VLM在两类心理学ToM任务上的表现，揭示其ToM能力存在跨任务解离，凸显多范式评估对准确衡量VLM ToM能力的重要性。

</details>

---

### 12. [Distill What the Student Can See: Fisher-Projected On-Policy Distillation for Vision-Language Models](https://arxiv.org/abs/2608.01263v1)

**Authors**: Leyan Xue, Feng Xiong, Mingjun Ma, Changqing Zhang  
**Category**: cs.LG  
**Published**: 2026-08-04  
**Score**: 52.5  
**Type**: new  
**ArXiv ID**: 2608.01263v1  

#### Abstract
On-policy distillation (OPD) samples trajectories from the current student policy and minimizes token-level divergence between student and teacher next-token distributions at prefixes along those trajectories. This aligns the distillation states with the student's own generation distribution. Howeve...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Distill What the Student Can See: Fisher-Projected On-Policy Distillation for Vision-Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题：现有On-policy distillation（OPD）假设完整的教师分布是适配学生能力的蒸馏目标，但在视觉语言推理任务中，教师的修正依赖紧凑学生无法表征的视觉区分；目标缩放研究显示，当蒸馏目标接近完整教师分布时，学生实现的指定分布转换更少，下游性能更差。
🚀 提出的新方法与思路：**Fisher-Projected On-Policy Distillation (FP-OPD)**，该方法仅蒸馏学生可实现的教师修正：通过连续视觉扰动估计学生的局部视觉切线空间，以学生的Fisher度量将中心化的教师-学生对数概率差投影至该空间，得到容量感知的蒸馏目标；该方法保留标准OPD框架，在学生轨迹上采用全词汇反向KL进行优化。
🔍 相比现有方法的优势：
| 维度 | 优势 |
| ---- | ---- |
| 蒸馏目标适配性 | 仅针对学生可表征的视觉内容进行蒸馏，解决了标准OPD假设完整教师分布适合学生能力的缺陷 |
| 下游性能提升 | 在8B-to-2B蒸馏场景下，平均分数相对预训练学生提升2.77，相对标准OPD提升1.60 |
2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：任务为视觉语言推理；
| 指标 | 含义 |
| ---- | ---- |
| 平均多模态基准分数 | 越高越好 |
⚔️ 基线方法对比：
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 预训练学生模型 | 基线方法 | 未经过蒸馏的紧凑视觉语言模型 |
| 标准OPD | 现有蒸馏方法 | 采用完整教师分布作为蒸馏目标的On-policy蒸馏方法 |
| FP-OPD | 提出的蒸馏方法 | 容量感知的Fisher投影OPD蒸馏方法 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（8B-to-2B蒸馏场景）**
| 方法 | 相对预训练学生平均分数提升 | 相对标准OPD平均分数提升 |
| ---- | ---- | ---- |
| 标准OPD | 1.17 | - |
| FP-OPD | 2.77 ✅ | 1.60 ✅ |
💡 结论：在8B-to-2B的紧凑视觉语言模型蒸馏场景下，FP-OPD在全部7个评估的多模态基准上均实现了性能提升，整体优于标准OPD和预训练学生模型。
效率对比：论文未报告
跨域/zero-shot迁移：论文未报告
鲁棒性/扰动测试：论文未报告
消融实验：论文未报告
4. 关键结论和发现
- 核心发现1：标准OPD基于完整教师分布的蒸馏目标在视觉语言推理任务中存在缺陷，教师修正依赖学生无法表征的视觉区分会导致学生下游性能下降。
- 核心发现2：仅蒸馏学生可实现的教师修正（FP-OPD）能有效适配学生容量，提升紧凑视觉语言模型的多模态性能。
- 核心发现3：在8B-to-2B蒸馏场景下，FP-OPD的平均多模态性能优于预训练学生和标准OPD。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：FP-OPD通过将教师与学生的对数概率差投影到学生的局部视觉切线空间，仅蒸馏学生可表征的内容，在8B-to-2B的视觉语言模型蒸馏任务中，相较于标准OPD和预训练学生取得了更优的多模态基准性能。

</details>

---

### 13. [Exploring More to Solve More: Boosting Diversity in Text Diffusion Models via Entropy-Based Guidance](https://arxiv.org/abs/2608.00024v1)

**Authors**: Jingwei Zhang, Haoyu Lei, Zijin Feng, Jiacheng Sun, Farzan Farnia  
**Category**: cs.CL  
**Published**: 2026-08-04  
**Score**: 52.0  
**Type**: new  
**ArXiv ID**: 2608.00024v1  

#### Abstract
Although diffusion models have revolutionized continuous domains like image synthesis through high quality generations and controllable guidance mechanisms, bringing this controllability to the discrete, sequential nature of text remains an open challenge. Meanwhile, current sampling strategies and ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# Exploring More to Solve More: Boosting Diversity in Text Diffusion Models via Entropy-Based Guidance
## 1. 论文的主要贡献和创新点
### ✅ 解决的问题
现有扩散模型在连续领域（如图像合成）凭借高质量生成和可控引导机制实现了突破，但将这种可控性应用到离散序列性质的文本领域仍是开放挑战；当前采样策略和引导方法仅调整token似然，未捕捉更广泛的语义格局，导致保真度与多样性之间的平衡次优。
### 🚀 提出的新方法与思路
**Semantic-Aware Kernel Entropy (SAKE) guidance**，是一种训练无关的引导方法，它在捕获跨token语义交互和相对token位置的核格拉姆矩阵上计算二阶Rényi熵，通过在嵌入空间线性化该目标，推导得到可处理的引导信号，动态调整采样分布——当存在冗余时展平分布以鼓励探索，当多样性不足时锐化分布以提升保真度。
### 🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 保真度-多样性帕累托前沿 | 优于温度缩放和离散引导基线，实现更优的平衡 |
| 推理密集型任务多样本性能 | 在代码、数学生成等推理密集型任务上的多样本性能得到提升 |

## 2. 核心实验方法和设置
### 📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

### 🎯 实验设置与评估指标
用于评估文本扩散模型在保真度与多样性的平衡，以及代码、数学生成等推理密集型任务的多样本性能。
| 指标 | 含义 |
| --- | --- |
| 保真度-多样性帕累托前沿 | 衡量生成样本的保真度与多样性之间的平衡程度，值越优则帕累托前沿更靠外（无明确箭头方向） |
| 推理密集型任务多样本性能 | 衡量代码、数学等推理密集型文本生成任务中多生成样本的表现，值越高性能越好 |

### ⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 温度缩放 | 采样策略 | 通过调整采样分布温度平衡保真度与多样性 |
| 离散引导基线 | 引导方法 | 仅调整token似然，未捕捉更广泛语义格局，导致保真度与多样性平衡次优 |

## 3. 主要实验结果和性能指标
所有实验项因未在论文中提供具体信息，均报告如下：
1. 主benchmark性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

## 4. 关键结论和发现
- 主要发现：
1. SAKE引导方法能够在文本扩散模型的保真度与多样性之间实现更优的平衡，优于温度缩放和离散引导基线；
2. SAKE引导方法在代码、数学生成等推理密集型任务的多样本性能上优于温度缩放和离散引导基线；
3. SAKE是训练无关的引导方法，通过动态调整采样分布，解决了文本扩散模型中探索与保真的平衡问题。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出训练无关的Semantic-Aware Kernel Entropy (SAKE)引导方法，通过计算核格拉姆矩阵上的二阶Rényi熵动态调整文本扩散模型的采样分布，在保真度与多样性的平衡及代码、数学生成等推理密集型任务的多样本性能上优于温度缩放和离散引导基线，改善了现有文本扩散模型可控性差、保真度与多样性平衡不佳的问题。

</details>

---

### 14. [From Chains to Trees: Parent-Conditioned Drafting for Semi-Autoregressive Speculative Decoding](https://arxiv.org/abs/2608.02123v1)

**Authors**: Zixian Li, Tong Li, Chi Xie, Xiaohui Song, Haonan Lu  
**Category**: cs.CL  
**Published**: 2026-08-04  
**Score**: 46.5  
**Type**: new  
**ArXiv ID**: 2608.02123v1  

#### Abstract
Speculative decoding accelerates LLM inference only when drafted continuations survive target-model verification. Semi-autoregressive drafters such as DSpark predict an entire token block with one backbone forward and refine it with a lightweight Markov head. However, DSpark decodes this block as a ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

### 论文：From Chains to Trees: Parent-Conditioned Drafting for Semi-Autoregressive Speculative Decoding
1. 论文的主要贡献和创新点
✅ 解决的问题
现有半自回归draft方法（如DSpark）采用线性单链生成draft块，若生成过程出现早期不匹配，会导致剩余后缀失效，从而限制大draft块的推理收益。

🚀 提出的新方法与思路
**Parent-Conditioned Drafting Tree（PCTree）**：利用预训练的马尔可夫头，为每个具体父节点分别对备选子节点打分，将固定的验证预算分配给最可能的路径，从而将DSpark的线性draft转换为树状结构，同时保留其一次并行的主干网络前向传播，无需额外训练。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 改动性质 | 仅做推理层改动，无额外主干前向传播 |
| 训练需求 | 无需额外训练，复用预训练模型参数 |
| draft结构 | 避免早期不匹配导致的后缀失效 |
| 推理收益 | 在多模型多基准上取得优于DSpark的加速效果 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 9个基准（含GSM8K） | 评估不同LLM在各类生成任务的性能与效率 |

🎯 实验设置与评估指标
任务为LLM半自回归推测解码的推理效率与生成质量评估。
| 指标 | 含义 |
| --- | --- |
| 相对AR加速比 | 数值越高（↑），LLM推理速度越快 |
| 平均接受长度 | 数值越高（↑），draft块的有效生成长度越长 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| DSpark | 半自回归draft方法 | 线性单链draft结构，依赖一次并行主干前向 |
| PCTree | 本文提出的方法 | 树状parent-condition draft结构，无额外主干前向与额外训练 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能（无明确表号）**
Qwen3-{4B,8B,14B}在9个基准、B=7的设置下，PCTree相对匹配DSpark的加速增益范围为3.1%至29.5%。
💡 结论：PCTree在多模型多基准上的基础加速收益显著优于DSpark。

**效率对比（无明确表号）**
Qwen3-4B GSM8K在B=16的设置下，PCTree的平均接受长度从DSpark的9.41提升至11.16，三运行平均AR加速比从6.14×提升至6.60×。
💡 结论：针对具体任务，PCTree可大幅提升draft块的有效生成长度与推理速度。

跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验：论文未报告。

4. 关键结论和发现
- 主要发现1：半自回归drafter（如DSpark）已学习的条件结构可支持多个父节点一致的备选延续，无需额外训练或主干前向传播即可利用。
- 主要发现2：通过推理层改动实现的PCTree，可将线性draft转为树状结构，避免早期不匹配导致的后缀失效，提升推测解码效率。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：PCTree是仅需推理层改动的半自回归推测解码方法，无需额外训练，即可将DSpark的线性draft转为树状结构，在多模型多基准上显著提升LLM推理速度与draft块有效生成长度。

</details>

---

### 15. [CoRe-GNN: Multilevel Message passing on Coarsened graphs](https://arxiv.org/abs/2608.02128v1)

**Authors**: Antonin Joly, Nicolas Keriven, Aline Roumy  
**Category**: cs.LG  
**Published**: 2026-08-04  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2608.02128v1  

#### Abstract
Training Graph Neural Networks on large graphs is challenged by the memory cost of storing all node representations across layers. We show that several existing scalable approaches can be written as structured modifications of the GNN propagation matrix, providing a unified perspective that exposes ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

CoRe-GNN: Multilevel Message passing on Coarsened graphs
1. 论文的主要贡献和创新点
✅ 解决的问题
大图上训练GNN面临存储所有层节点表示的内存成本痛点；现有可扩展GNN方法的缺陷具有互补性：graph coarsening有谱保证但聚类节点表示统一，Cluster-GCN支持高效批量处理但丢失长程信息，二者均源于图分组分解的不足。

🚀 提出的新方法与思路
**CoRe-GNN**：在每层并行执行两种传播：1）粗化的簇间项，用于捕获长程结构；2）局部簇内项，用于保留节点级判别性；证明该方法继承graph coarsening的近似保证，引入基于簇的批量处理方案，可扩展到百万节点级大图。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 近似保证 | 继承graph coarsening的谱近似保证 |
| 信息保留 | 同时捕获长程结构与节点级判别性 |
| 可扩展性 | 基于簇的批量处理可适配百万节点级大图 |
| 性能表现 | 在各类节点分类基准上优于graph coarsening和Cluster-GCN |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告具体数据集名称，仅提及覆盖同质性、异质性、大规模、长程图类型的节点分类基准 | 用于节点分类任务的性能评估 |

🎯 实验设置与评估指标
任务：节点分类；论文未报告具体评估指标细节。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| graph coarsening | 图粗化基线 | 用低秩近似替换GNN传播矩阵，有谱保证，但为聚类节点分配统一表示 |
| Cluster-GCN | 基于簇的GNN基线 | 将传播矩阵限制为簇内连接，支持高效批量处理，但丢失长程信息 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未提供带具体表号、图号的定量结果数值，仅提及CoRe-GNN在覆盖同质性、异质性、大规模、长程图的节点分类基准上，性能优于graph coarsening和Cluster-GCN基线，在长程任务上达到竞争力准确率，同时保持内存效率。

4. 关键结论和发现
- 主要发现：① graph coarsening和Cluster-GCN的缺陷是图分组分解的互补性表现；② CoRe-GNN并行执行簇间和簇内传播，兼顾近似保证与节点级判别性；③ CoRe-GNN的簇式批量处理适配百万节点级大图。
- 方法局限性：论文未明确报告方法的局限性细节。
- 未来工作：论文未提及未来工作方向。

> ✅ **总结一句话**：CoRe-GNN通过并行执行粗化的簇间传播与局部簇内传播，结合现有两种可扩展GNN方法的优势，在保持内存效率的同时，在各类节点分类基准上性能优于graph coarsening和Cluster-GCN，尤其在长程任务上表现出色。

</details>

---

### 16. [An Embedded RISC-V Evaluation of Kolmogorov--Arnold Networks in Hard-Constrained Recurrent Physics-Informed Models](https://arxiv.org/abs/2608.00737v1)

**Authors**: Enzo Nicolas Spotorno, Josafat Leal Filho  
**Category**: cs.LG  
**Published**: 2026-08-04  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2608.00737v1  

#### Abstract
Hard-constrained recurrent physics-informed networks (HRPINNs) embed known dynamics inside a recurrent numerical integrator and restrict a neural branch to learning only the residual dynamics that the first-principles model does not capture. Kolmogorov--Arnold Networks (KANs) have been proposed as p...

---

### 17. [Upper-Expectile Multi-Step Q-Learning for Off-Policy Reinforcement Learning](https://arxiv.org/abs/2608.02034v1)

**Authors**: Abdelghani Ghanem, Mounir Ghogho  
**Category**: cs.LG  
**Published**: 2026-08-04  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2608.02034v1  

#### Abstract
Multi-step returns accelerate reward propagation in off-policy reinforcement learning, but couple the evaluation of each decision to the suboptimal logged actions that follow it, inducing a pessimistic bias that grows with the horizon. We propose Expectile $n$-step Q-learning (ENQ), which replaces t...

---

### 18. [Efficiency and Cost Alignment in Batched LLM Serving via Resource-Fair Scheduling](https://arxiv.org/abs/2608.02244v1)

**Authors**: Dayi Yao, Zijie Zhou  
**Category**: cs.DC  
**Published**: 2026-08-04  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2608.02244v1  

#### Abstract
This paper studies a resource-allocation inefficiency in batched large language model (LLM) serving: heterogeneous requests that share a decode batch impose max-driven computational costs on one another. Because the wall-clock cost of a batch step is largely governed by the largest active KV-cache f...

---

### 19. [Diffusion Policy with Behavioral Advantage Correction for Offline Reinforcement Learning](https://arxiv.org/abs/2608.02332v1)

**Authors**: Botao Dong, Longyang Huang, Ning Pang, Hongtian Chen  
**Category**: cs.LG  
**Published**: 2026-08-04  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2608.02332v1  

#### Abstract
In offline reinforcement learning (RL), the distribution shift between behavioral data and the learned policy can lead to erroneous \emph{Q}-value estimation, thereby misguiding the direction of policy optimization. To address this issue, we develop a behavioral advantage corrected policy evaluation...

---

### 20. [DiffusionGemma Technical Report](https://arxiv.org/abs/2608.00146v1)

**Authors**: DiffusionGemma Team, Adrien Ali Ta\"iga, James Assiene, Daniele Calandriello, Rahma Chaabouni, Jo\~ao Gante, Tamara von Glehn, Nate Keating, Chris Knutsen, Martin Kukla, Tianlin Liu, Ivan Lobov, Ofir Nabati, Jo\~ao Gabriel Oliveira, Nicolas Perez-Nieves, Nastasia Prutianova, Bobak Shahriari, Jean Tarbouriech, Pavel Tyletski, \c{C}a\u{g}lar \"Unl\"u, Cindy Wu, Glenn Cameron, Jerome Connor, Sertan Girgin, Maarten Grootendorst, Alon Levkovitch, Eliya Nachmani, Omar Sanseviero, Piotr Stanczyk, Quentin Berthet, Andrew Campbell, Cl\'ement Crepy, Valentin De Bortoli, Arnaud Doucet, Romuald Elie, Alexandre Galashov, Klaus Greff, Alexis Jacq, David Ruhe, Yu-Han Wu, Sebastian Flennerhag, Brendan O'Donoghue, George Scrivener, Shantanu Thakoor  
**Category**: cs.CL  
**Published**: 2026-08-04  
**Score**: 37.0  
**Type**: new  
**ArXiv ID**: 2608.00146v1  

#### Abstract
We introduce DiffusionGemma, an experimental open-weight language model that uses discrete diffusion to generate text at exceptionally high speed. Rather than decoding one token at a time, DiffusionGemma iteratively refines blocks of 256 tokens in parallel, avoiding the sequential decoding bottlenec...

---

### 21. [SeDeM: Selective Decompression of Hidden-State Memories for Long-Context Question Answering](https://arxiv.org/abs/2608.00311v1)

**Authors**: Maryam Haghifam, Jason Cong, Yizhou Sun  
**Category**: cs.CL  
**Published**: 2026-08-04  
**Score**: 36.0  
**Type**: new  
**ArXiv ID**: 2608.00311v1  

#### Abstract
Long-context inference with large language models (LLMs) is costly: self-attention during prefill scales quadratically with sequence length, and the key-value (KV) cache grows with the number of processed tokens. Larger context windows also do not ensure reliable evidence use. Context compression re...

---

### 22. [GeoArbiter: Verifiability-Guided Grounding for Remote-Sensing Multimodal LLMs](https://arxiv.org/abs/2608.00877v1)

**Authors**: Xuechen Li  
**Category**: cs.LG  
**Published**: 2026-08-04  
**Score**: 36.0  
**Type**: new  
**ArXiv ID**: 2608.00877v1  

#### Abstract
Remote-sensing multimodal large language models (MLLMs) often assert facts that imagery cannot establish, such as a facility's identity or function. Coordinate-keyed geographic retrieval can supply this missing knowledge, improving fMoW land-use accuracy by 12.06--17.19 points across three open MLLM...

---

### 23. [S$^4$R: Selective Sampling, Subspaces, and Sparse Reconstruction for Compressed Long-Context KV Caching](https://arxiv.org/abs/2608.00528v1)

**Authors**: Jialong Han, You Wu, Kewei Tu  
**Category**: cs.CL  
**Published**: 2026-08-04  
**Score**: 35.5  
**Type**: new  
**ArXiv ID**: 2608.00528v1  

#### Abstract
The growth of context window lengths in Large Language Models (LLMs) significantly enhances their long-context capabilities but incurs prohibitive memory costs due to the Key-Value (KV) cache. Although low-rank compression of KV cache is a promising remedy, existing methods face a dilemma: offline a...

---

### 24. [Cultural Awareness is Represented but Not Decoded: Tracing Mythological Knowledge across 18 Open-Source LLMs](https://arxiv.org/abs/2608.02486v1)

**Authors**: Iaroslav Chelombitko, Ekaterina Chelombitko, Mika H\"am\"al\"ainen  
**Category**: cs.CL  
**Published**: 2026-08-04  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2608.02486v1  

#### Abstract
Open-source LLMs reliably name Zeus, Jupiter, and Thor, but recover their counterparts in less-represented traditions like Finnish, Slavic, Egyptian, or Chinese mythology far less consistently. We ask where inside the model this cultural default is produced. On a parallel cross-cultural substrate of...

---

### 25. [Obshazard-bench: Benchmarking Multimodal Foundation Models for Real-Time Disaster Intelligence from Raw Earth Observation Streams](https://arxiv.org/abs/2608.00012v1)

**Authors**: Fengxiang Wang, Qiuyang Yu, Yueying Li, Mingshuo Chen, Chengchi Fei, Kaiyi Xu, Lixin Gu, Wangxu Wei, Junchao Gong, Lipeng Ma, Jiong Wang, Fenghua Ling, Wenlong Zhang, Xue Yang, Wenjing Yang, Ben Fei, Long Lan  
**Category**: cs.CL  
**Published**: 2026-08-04  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2608.00012v1  

#### Abstract
Multimodal Large Language Models (MLLMs) are increasingly used to interpret Earth observation data, yet their capability to support real-world disaster emergency response remains insufficiently evaluated. Existing remote sensing benchmarks largely rely on static, post-hoc, and expert-processed produ...

---

### 26. [AReaL-DTE: Sparse Policy-Weight Transfer for Online Agentic Reinforcement Learning](https://arxiv.org/abs/2608.00455v1)

**Authors**: Yingqi Peng, Jiawei Zhang, Wenhao Zhou, Ruida Xu, Ran Yan, Wei Dong, Yi Gao, Zhiqiang Ding, Tongkai Yang, Binhang Yuan  
**Category**: cs.DC  
**Published**: 2026-08-04  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2608.00455v1  

#### Abstract
Online agentic reinforcement learning implemented with micro-services separates policy training from rollout generation, improving scalability and modularity while potentially making frequent policy-weight synchronization a critical systems overhead. Shared storage naturally connects these services ...

---

### 27. [DEFT: Joint Task Placement and DVFS for Energy-Efficient Multi-GPU Runtimes](https://arxiv.org/abs/2608.02122v1)

**Authors**: Jing Chen, Miquel Pericas  
**Category**: cs.DC  
**Published**: 2026-08-04  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2608.02122v1  

#### Abstract
Energy efficiency has become a first-order concern in modern high-performance computing systems, as it directly determines achievable throughput under fixed power budgets. Although Dynamic Voltage and Frequency Scaling (DVFS) provides an effective mechanism for reducing GPU energy consumption, exist...

---

### 28. [Evaluating VLMs on Multimodal Aristotelian Persuasion Tasks](https://arxiv.org/abs/2608.01238v1)

**Authors**: Khondoker Ittehadul Islam  
**Category**: cs.CL  
**Published**: 2026-08-04  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2608.01238v1  

#### Abstract
Vision Language Models (VLMs) have demonstrated exceptional performance across various tasks. However, they have not yet been thoroughly evaluated on more complex tasks. The Persuasion Model, conceived by Aristotle, resembles a triangle shape, which highlights its inherent challenges related to pers...

---

### 29. [RestoreKV: Recovering Full-Cache Behavior Under Aggressive Query-Agnostic KV Cache Eviction](https://arxiv.org/abs/2608.01247v1)

**Authors**: Changwoo Baek, Seungjun Shin, Kyeongbo Kong  
**Category**: cs.CL  
**Published**: 2026-08-04  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.01247v1  

#### Abstract
Query-agnostic KV cache eviction compresses a context once and reuses the resulting cache for arbitrary future queries, but performance can collapse under tight budgets. Existing methods primarily improve which original KV pairs are retained. We introduce RestoreKV, which complements this selection-...

---

### 30. [From Cloud to Crowd: Democratizing LLM Service with Decentralized Edge Collaboration for RAG](https://arxiv.org/abs/2608.00922v1)

**Authors**: Jiaxing Li, Hengzhi Wang, Feng Wang, Chi Xu, Danyang Song, Ruixiao Zhang, Edith C. H. Ngai, Jiangchuan Liu  
**Category**: cs.DC  
**Published**: 2026-08-04  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.00922v1  

#### Abstract
The rapid advancement of large language models (LLMs) has increased demand for scalable and cost-effective deployment, especially for mobile and edge devices. Cloud-hosted LLMs are powerful but expensive and difficult to scale due to vendor lock-in and high resource needs, resulting in high expenses...

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
