# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-09-14 11:00:26 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [Efficient Vision-Language-Action Management and Serving for Robot Factories](https://arxiv.org/abs/2609.12075v1)

**Authors**: Dionysios Adamopoulos, Nattapol Chanpaisit, Basel Fakhri, Christina Giannoula  
**Category**: cs.DC  
**Published**: 2026-09-14  
**Score**: 72.5  
**Type**: new  
**ArXiv ID**: 2609.12075v1  

#### Abstract
Vision-Language-Action (VLA) models show high robotic manipulation capabilities via a two-stage design: a Vision-Language Model (VLM) stage followed by an Action Diffusion Transformer (ADiT) stage. Since robots must meet strict Service-Level Objectives (SLOs) for safety, VLA inference is inherently ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Efficient Vision-Language-Action Management and Serving for Robot Factories
1. 论文的主要贡献和创新点
✅ 解决的问题
- 当前VLA服务系统缺乏在多GPU服务器上支持多请求、多模型执行并满足服务水平目标（SLO）的能力；
- 现有多阶段模型服务系统针对跨独立GPU的吞吐量和阶段拆分优化，不适用于VLA模型的毫秒级阶段特性，无法满足机器人对SLO延迟的严格要求。

🚀 提出的新方法与思路
**VLM-ADiT同GPU内流拆分调度**：在单GPU内将VLM和ADiT拆分为两个并行流，动态限制VLM流的流式多处理器（SM）资源，确保ADiT总有可用SM资源并行运行；同时按请求剩余SLO时间进行优先级排序，跨流共享资源。
**多GPU灵活模型放置+智能流量控制器**：设计管理引擎实现多GPU服务器的灵活模型放置，整合智能流量控制器，在选定模型放置方案下最大化每个模型的批处理量，同时限制每个GPU的负载以满足SLO要求。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 单模型负载能力（98% SLO达成） | 比vLLM-Omni高6.7倍，比Monolithic高1.5倍 |
| 多模型场景服务容量 | 4-GPU服务器部署8个模型时，最多可服务64个机器人且满足98% SLO |
| 多GPU资源适配性 | 解决现有系统不适配VLA毫秒级阶段的问题，支持多请求多模型执行 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告

🎯 实验设置与评估指标
任务：机器人工厂场景下的VLA推理服务，满足延迟SLO要求。
| 指标 | 含义 |
| --- | --- |
| SLO达成率 | 请求满足SLO的比例，越高越好（↑） |
| 平均服务机器人负载 | 单位时间内可服务的机器人数量，越高越好（↑） |
| 最大支持服务机器人数量 | 服务器在满足SLO前提下的最大服务机器人数，越高越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| vLLM-Omni | 多阶段服务系统 | 现有最广泛使用的多阶段VLA serving系统 |
| Monolithic | VLA执行方法 | 将VLM和ADiT作为单一管道运行的VLA执行方式 |
| Robion | 本文提出的系统 | 针对多机器人多模型多GPU场景设计的VLA服务与管理引擎 |

3. 主要实验结果和性能指标
📊 定量结果汇总
- **主benchmark性能（L2/碰撞率等）**：论文未报告
- **效率对比（FPS / 参数量）**：论文未报告
- **跨域 / zero-shot迁移**：论文未报告
- **鲁棒性 / 扰动测试**：论文未报告
- **消融实验**：论文未报告

**单模型场景性能（论文明确提供）**
| 对比方法 | 98% SLO达成下的平均机器人负载 |
| --- | --- |
| vLLM-Omni | 基准值 |
| Monolithic | 基准值 |
| Robion | 比vLLM-Omni高6.7倍 ✅，比Monolithic高1.5倍 ✅ |
💡 结论：Robion在单模型场景下显著提升了满足98% SLO时的服务负载能力。

**多模型多GPU场景性能（论文明确提供）**
| 场景 | 最大支持服务机器人数量（满足98% SLO） |
| --- | --- |
| 4-GPU服务器部署8个模型 | 64个 ✅ |
💡 结论：Robion可在大规模多模型部署场景下，用4-GPU服务器高效服务多机器人且满足SLO要求。

4. 关键结论和发现
- 主要发现：1. Robion的VLM-ADiT同GPU内流拆分调度机制，能有效解决VLA模型毫秒级阶段特性与SLO延迟要求的矛盾，大幅提升服务负载；2. 多GPU灵活模型放置加智能流量控制，可在大规模多模型部署时平衡GPU负载，保障SLO；3. 现有主流VLA服务系统（vLLM-Omni）和单管道执行方法（Monolithic）在SLO达成率和服务负载能力上均存在明显不足。
- 方法局限性：论文未报告
- 未来工作：论文未明确提及未来工作计划

> ✅ **总结一句话**：Robion是首个面向机器人工厂的多机器人多GPU多模型VLA推理服务系统，通过GPU内流资源调度与智能管理机制，在严格满足98% SLO的前提下大幅提升了服务负载与容量。

</details>

---

### 2. [Expert-Space Exploration in MoE Reinforcement Learning](https://arxiv.org/abs/2609.13058v1)

**Authors**: Hongyi He, Zhenghao Lin, Xiao Liu, Peng Cheng, Yan Lu, Yeyun Gong  
**Category**: cs.CL  
**Published**: 2026-09-14  
**Score**: 64.5  
**Type**: new  
**ArXiv ID**: 2609.13058v1  

#### Abstract
Reinforcement learning (RL) has become central to post-training of large language models. Recent advances in RL for Mixture-of-Experts (MoE) models have primarily focused on improving optimization stability and training efficiency, while treating the expert selection as a fixed component. Since rout...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Expert-Space Exploration in MoE Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有MoE模型的强化学习研究主要聚焦优化稳定性和训练效率，将专家选择（路由）视为固定组件；但路由决定稀疏计算路径与输出分布，是rollout多样性的额外来源，而直接扰动路由会激活不合适专家，大幅降低rollout质量，存在核心矛盾。

🚀 提出的新方法与思路
**Expert-Space Exploration Reinforcement Learning (ESRL)**：面向MoE模型的架构感知框架，具体实现为：1. 保留高置信度专家作为计算锚点；2. 将随机路由限制在合理候选池内，维持可靠计算路径；3. 根据路由器熵自适应调整扰动强度，避免过度扰动；4. 记录rollout阶段使用的专家路径，并在策略优化阶段回放，缓解路由扰动带来的匹配问题。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| MoE路由空间利用 | 显式探索MoE的专家路由空间，同时保留高置信度专家路径，避免直接扰动导致的rollout质量下降 |
| rollout稳定性 | 通过锚点专家与限制随机路由范围，维持可靠计算路径，减少不合格专家激活 |
| 策略优化匹配 | 回放rollout的专家路径，缓解路由扰动带来的优化匹配问题 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告

🎯 实验设置与评估指标
任务：在数学、科学、代码任务上评估MoE模型性能。
| 指标 | 含义 |
| --- | --- |
| Pass@1 | 1次尝试内通过的比例，↑ 越高越好 |
| Pass@8 | 8次尝试内通过的比例，↑ 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| GRPO | 强化学习方法 | 现有MoE强化学习对比基准方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告
2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：直接扰动MoE专家路由类似提升解码温度，可增加rollout多样性，但会激活不合适专家导致rollout质量下降；ESRL在多类MoE路由骨干（top-K、top-1、共享专家）及数学、科学、代码任务上均优于对比方法GRPO；ESRL无额外采样或计算成本。
- 方法局限性：论文未报告
- 未来工作：论文未报告

✅ **总结一句话**：ESRL作为架构感知的MoE强化学习框架，通过显式探索专家路由空间并优化扰动策略，解决直接扰动路由导致的rollout质量下降问题，在多领域任务上优于现有基准方法且无额外计算成本。

</details>

---

### 3. [Argus: Orchestrating Cross-Layer GPU Performance Measurements around Semantic Regions](https://arxiv.org/abs/2609.12299v1)

**Authors**: Jianzhu Yao, Yue Guan, Srivatsan Ramesh, Yuanwei Fang, Jian Jiao, Boda Li, Yueming Hao, Xinwei Qiang, Pramod Viswanath, Yufei Ding, Bill Yoshimi, Alexey Loginov, Shane Nay, Adnan Aziz  
**Category**: cs.DC  
**Published**: 2026-09-14  
**Score**: 58.0  
**Type**: new  
**ArXiv ID**: 2609.12299v1  

#### Abstract
GPU developers and automated optimizers need performance evidence for semantic code regions--such as neural-network operator implementations and pipeline stages--but this evidence is fragmented across profiling tools. Answering a region-level question can require manually constructing probes and pro...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Argus: Orchestrating Cross-Layer GPU Performance Measurements around Semantic Regions
1. 论文的主要贡献和创新点
✅ 解决的问题
GPU开发者和自动优化器需要语义代码区域（如神经网络算子实现、流水线阶段）的性能证据，但此类证据分散在各类性能分析工具中；获取区域级问题的答案需手动完成探针构建、程序变体构造、干扰测量隔离、证据与区域及执行上下文映射等繁琐工作，缺乏自动化方案。

🚀 提出的新方法与思路
**Argus区域中心性能测量框架**：作为区域-centric的测量规划器与运行时，自动化上述手动工作流；客户端通过边界标记识别代码区域，选择需测量的信号与执行范围；Argus在编译、执行、测量变体全流程中保留区域身份，生成干扰感知的多运行计划，协调后端执行程序变换与性能分析，通过区域身份与动态执行上下文整合编译级、硬件级、系统级的性能证据，输出包含测量起源与归因歧义记录的报告。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 测量工作流 | 自动化原需手动完成的探针构造、程序变体生成、干扰隔离等流程，降低人力成本 |
| 区域身份一致性 | 在编译、执行、测量变体全流程保留区域身份，解决证据与语义区域映射错误问题 |
| 测量计划合理性 | 生成干扰感知的多运行计划，减少测量过程中的环境干扰 |
| 跨层级证据整合 | 打通编译、硬件、系统层级的性能证据，提供完整的区域级性能视图 |
| 报告可追溯性 | 输出的报告包含测量起源与归因歧义记录，提升结果可解释性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
实验任务包括代理式内核优化、持久微内核优化、跨层级PGO三类GPU性能优化任务；指标如下：
| 指标 | 含义（箭头） |
| --- | --- |
| 几何平均加速比 | 越高越好 |
| Token延迟 | 越低越好 |
| 多GPU吞吐量 | 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| AlphaEvolve | 代理式内核优化器 | 用于对比内核优化效果的现有方法 |
| PyTorch with CUDA Graphs | 性能基准实现 | 用于对比持久微内核性能的基准方案 |
| 未使用Argus的手动流程 | 对比基线 | 传统需手动完成性能测量与优化的流程 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能（L2/碰撞率等）：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

💡 结论：论文在代理式内核优化、持久微内核优化、跨层级PGO三类GPU性能优化场景中评估了Argus的应用效果，具体定量指标数值未报告。

4. 关键结论和发现
- 论文在代理式内核优化、持久微内核优化、跨层级PGO三类GPU性能优化场景中验证了Argus框架的适用性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：Argus是一套面向GPU语义代码区域的自动化性能测量框架，解决了现有区域级性能证据碎片化、测量流程需手动完成的痛点，能支撑GPU性能优化工作。

</details>

---

### 4. [Unleashing the Power of Equality Saturation for Tensor Program Superoptimization](https://arxiv.org/abs/2609.12330v1)

**Authors**: Qi Zhan, Xing Hu, Xin Xia, Shanping Li  
**Category**: cs.DC  
**Published**: 2026-09-14  
**Score**: 57.5  
**Type**: new  
**ArXiv ID**: 2609.12330v1  

#### Abstract
Efficient GPU implementations of tensor programs often require joint optimization of high-level algebraic formulations and low-level execution strategies. However, the resulting search space grows rapidly as transformations combine across operators, making joint optimization difficult to scale. We p...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Unleashing the Power of Equality Saturation for Tensor Program Superoptimization
1. 论文的主要贡献和创新点
✅ 解决的问题：GPU上张量程序的高效实现需同时优化高层代数形式与低层执行策略，但各算子间转换组合后搜索空间会快速膨胀，导致联合优化难以规模化。
🚀 提出的新方法与思路
**Equality Saturation-based Tensor Program Superoptimizer EqiForge**：EqiForge是基于equality saturation的张量程序超优化器，其统一中间表示（IR）将高层张量表达式与分块计算整合为单一表达式语言；通过组合等价规则，可直接从张量表达式导出FlashAttention风格的融合实现；采用提前压缩策略在搜索完成前修剪冗余的部分程序，同时通过子图组合将搜索范围扩展到更大的计算图。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 优化扩展性 | 解决跨算子转换组合导致的搜索空间快速膨胀问题，实现可规模化的张量程序联合优化 |
| 实现生成能力 | 无需手动设计复杂融合逻辑，直接从张量表达式导出硬件友好的高效融合实现（如FlashAttention风格内核） |
| 实际性能提升 | 在张量程序基准测试中几何平均加速1.32x，最大加速达2.74x；注意力内核在decode阶段比FlashAttention最高快1.87x，prefill阶段性能接近FlashAttention；在QK归一化MLA、mHC等Transformer层上性能分别优于torch.compile达3.16x、5.84x |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未明确说明所使用的具体数据集，仅提及采用张量程序基准开展测试 |
🎯 实验设置与评估指标
任务：针对GPU上运行的张量程序开展超优化，以提升执行性能。
| 指标 | 含义 |
| --- | --- |
| 加速比 | 相对于对应基线的性能提升倍数，↑越大越好 |
| decode阶段注意力内核性能 | 注意力内核在解码阶段的执行速度，↑越大越好 |
| prefill阶段注意力内核性能 | 注意力内核在填充阶段的执行速度，↑越大越好 |
| Transformer层性能 | 各类Transformer层的执行性能，↑越大越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| the fastest available baseline per configuration | 通用性能基线 | 作为各配置下当前最优的现有张量程序实现，用于整体性能对比 |
| FlashAttention | 注意力内核基线 | 用于EqiForge生成的注意力内核的性能对比 |
| torch.compile | Transformer优化基线 | 用于EqiForge生成的Transformer层实现的性能对比 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能（L2/碰撞率等）：
论文未报告具体表号对应的主benchmark性能表格，仅提及EqiForge在张量程序基准测试上相对于各配置下现有最快基线的几何平均加速1.32x，最大加速达2.74x。
💡 结论：EqiForge在张量程序基准测试上实现了相对于现有最优实现的显著性能提升。
2. 效率对比（FPS / 参数量）：
论文未报告对应表号的效率对比表格，仅提及EqiForge生成的注意力内核在decode阶段比FlashAttention最高快1.87x，prefill阶段性能接近FlashAttention。
💡 结论：EqiForge生成的注意力内核在解码场景性能优于现有FlashAttention实现，填充场景性能与FlashAttention相当。
3. 跨域 / zero-shot 迁移：
论文未报告该实验的相关结果。
4. 鲁棒性 / 扰动测试：
论文未报告该实验的相关结果。
5. 消融实验：
论文未报告消融实验的相关内容，无对应表格。

4. 关键结论和发现
- 主要发现：① EqiForge通过equality saturation方法，解决了张量程序联合优化中搜索空间快速膨胀的问题，实现了可规模化的跨算子融合优化；② 基于统一IR和等价规则组合的方式，可直接从高层张量表达式导出高效的硬件适配实现；③ EqiForge在注意力内核（解码阶段）和Transformer层（QK归一化MLA、mHC）上的性能显著优于FlashAttention和torch.compile等现有主流优化工具。
- 方法局限性：论文未报告
- 未来工作：论文未报告
✅ **总结一句话**：EqiForge是一款基于equality saturation的张量程序超优化器，通过统一中间表示、等价规则组合、提前压缩及子图组合策略，在GPU张量程序上实现了优于现有基线的高效性能，尤其在注意力内核和Transformer层优化中表现突出。

</details>

---

### 5. [On-Device Language Models for Privacy-Preserving Stress Prediction: A Multimodal Evaluation on Mobile Health](https://arxiv.org/abs/2609.11961v1)

**Authors**: Ibukunoluwa Soyebo, Alyssa Donawa, Rodrigo Aguilar Barrios, Brice Patchou, Corey E. Baker  
**Category**: cs.LG  
**Published**: 2026-09-14  
**Score**: 54.5  
**Type**: new  
**ArXiv ID**: 2609.11961v1  

#### Abstract
Stress is a pervasive determinant of mental health and a key target for mobile health interventions. On-device language models (ODLMs) offer privacy-preserving inference without cloud dependency, yet their feasibility for health prediction under mobile resource constraints remains underexplored. We ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：On-Device Language Models for Privacy-Preserving Stress Prediction: A Multimodal Evaluation on Mobile Health

1. 论文的主要贡献和创新点
✅ 解决的问题：压力预测是移动健康干预的核心目标，云端依赖的压力预测存在隐私泄露风险，而On-Device Language Models（ODLMs）虽具备无云端依赖的隐私-preserving推理优势，但其在移动资源约束下用于健康预测的可行性尚未得到充分探索。
🚀 提出的新方法与思路
**Zero-Shot Prompting**：采用zero-shot prompting策略对ODLMs的多模态压力预测能力进行评估，无需依赖标注数据，可快速验证模型的预测潜力；
**Sub-2B Lightweight ODLMs**：聚焦参数规模小于2B的轻量型ODLMs，重点测试其在移动设备上的延迟表现与资源使用情况，验证其适配移动资源约束的实际可行性。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 隐私保护 | 采用On-Device推理，无需云端依赖，满足隐私-preserving需求 |
| 资源适配 | 轻量sub-2B ODLMs低延迟、资源使用可预测，适配移动设备资源约束 |
| 部署便捷 | 基于zero-shot prompting策略，无需额外标注即可开展预测评估 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 多模态压力预测评估 |
🎯 实验设置与评估指标
任务为多模态压力预测（基于移动健康数据），评估指标如下：
| 指标 | 含义 |
| --- | --- |
| predictive accuracy | 越高越好 ↑ |
| latency | 越低越好 ↓ |
| throughput | 越高越好 ↑ |
⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
仅报告摘要明确提及的定性结果，具体数值及来源未在摘要中说明：
- 客观传感器特征的平均预测效果略优于主观自我报告；
- 轻量sub-2B ODLMs可实现低延迟，且资源使用情况可预测；

各细分实验模块结果：
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

💡 结论：在多模态压力预测任务中，客观传感器特征的预测表现略优于主观自我报告，轻量sub-2B ODLMs适配移动资源约束，具备隐私-preserving的应用潜力。

4. 关键结论和发现
- 2-3 条主要发现
1. 多模态压力预测任务中，客观传感器特征的平均预测准确率略优于主观自我报告；
2. 轻量sub-2B规模的On-Device Language Models（ODLMs）可实现低延迟推理，且资源使用情况可预测，适配移动设备的资源约束；
3. 采用zero-shot prompting策略可对ODLMs的多模态压力预测能力进行有效评估，满足隐私-preserving的需求。
- 方法局限性
论文未报告
- 未来工作
论文未报告

> ✅ **总结一句话**：本研究针对移动健康场景中压力预测的隐私保护与资源约束痛点，采用zero-shot prompting评估ODLMs的多模态压力预测可行性，发现轻量sub-2B ODLMs适配移动资源限制，且客观传感器特征的预测效果略优于主观自我报告。

</details>

---

### 6. [Sampling via Decision-Flow: Training-Free Extraction of Improved Latent Reasoning Paths in Large Language Models](https://arxiv.org/abs/2609.12317v1)

**Authors**: Zhendong Mi, Shaoyi Huang  
**Category**: cs.LG  
**Published**: 2026-09-14  
**Score**: 53.5  
**Type**: new  
**ArXiv ID**: 2609.12317v1  

#### Abstract
A central question in LLM reasoning is whether reinforcement learning (RL) instills genuinely new capabilities or merely reshapes how existing knowledge is expressed during inference. Building on the distribution-sharpening hypothesis, which holds that RL reallocates probability mass toward high-rew...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Sampling via Decision-Flow: Training-Free Extraction of Improved Latent Reasoning Paths in Large Language Models

1. 论文的主要贡献和创新点
✅ 解决的问题
现有LLM推理存在核心争议：RL是向模型注入新的推理能力，还是仅重塑现有知识的表达形式？根据distribution-sharpening假说，RL只是将概率质量重新分配到基模型中已有的高奖励轨迹。现有推理采样策略多为纯局部步骤选择，会忽略高价值但低概率的推理链，且需依赖昂贵的RL微调才能优化推理路径。

🚀 提出的新方法与思路
**DF-Sample**，是训练-free、data-free的推理时框架，构建分层推理树，对终端节点进行质量评分，反向传播效用以指导每一步的中间分支决策，区别于传统采样策略的纯局部步骤选择，可在确定推理路径前执行显式全局轨迹评估。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 训练成本 | 无需RL微调、无需额外数据，成本更低 |
| 推理路径评估方式 | 采用显式全局轨迹评估，而非传统采样的纯局部步骤选择 |
| 低概率高质量推理链恢复 | 可恢复传统解码忽略的高价值但低概率的推理链 |
| 跨基准表现稳定性 | 在三个模型、四个基准上均优于基线方法 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| GPQA | 评估模型的推理准确率 |
| 其余3个基准 | 论文未报告具体名称 |

🎯 实验设置与评估指标
任务为大规模语言模型的推理能力评估，指标为准确率（↑ 越高越好）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| power sampling | 传统推理采样方法 | 纯局部步骤选择的采样策略 |
| GRPO | RL微调训练方法 | 基于RL的训练微调方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. 根据distribution-sharpening假说，RL仅会重新分配概率质量到基模型中已有的高奖励轨迹，而非注入全新推理能力；2. 预训练基模型中存在大量未被标准解码利用的高质量潜在推理路径；3. 提出的DF-Sample框架可有效捕获这些潜在推理路径。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：提出训练-free、data-free的推理框架DF-Sample，通过显式全局轨迹评估解锁预训练LLM中的潜在高质量推理路径，在多基准上优于传统采样策略及RL微调方法，证明预训练基模型具备可观的潜在推理能力。

</details>

---

### 7. [Granularity-Adaptive Credit Assignment for Long-Horizon LLM Agent Reinforcement Learning](https://arxiv.org/abs/2609.12424v1)

**Authors**: Taoran Liang, Yang Liu, Shang Luo, Yingguang Yang, Rongrong Zhang, Yingzong Min, Yulin Huang, Jianshen Zhang, Yongzhi Qi, Kefu Xu, Congjing Ran, Bin Chong  
**Category**: cs.LG  
**Published**: 2026-09-14  
**Score**: 52.5  
**Type**: new  
**ArXiv ID**: 2609.12424v1  

#### Abstract
Reinforcement learning is now the standard way to train large language model agents on long-horizon tasks, where dozens of interdependent actions precede a single sparse reward. Critic-free, group-relative methods such as GRPO suit this regime, but they broadcast one trajectory-level scalar to every...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Granularity-Adaptive Credit Assignment for Long-Horizon LLM Agent Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题：长 horizon LLM agent的强化学习场景中，现有无critic的group-relative方法（如GRPO）采用单一轨迹级标量为每个步骤分配信用，无法明确哪些决策驱动任务结果；GiGPO虽恢复了步骤级信号，但用固定权重合并步骤级与episode级估计，对关键分支决策与常规确定性转换采用相同分辨率，导致信用分配不合理。
🚀 提出的新方法与思路：**Granularity-Adaptive Credit Assignment (GACA)**，该方法基于不确定性的关键度代理，使信用分配的粒度随状态自适应调整：为每个步骤计算自身rollout记录的负对数似然（NLL）作为评分，再通过随该评分增长的每步权重混合步骤级与episode级的优势信号，当步骤NLL高于平均值时，梯度侧重细粒度信号；低于平均值时侧重episode级信号；论文还推导了该混合策略的精确风险分解，证明充分小的调制在正方向对齐下优于固定混合，同时给出局部动作值变异的条件边界及误差投影分析，明确该混合策略的理论价值。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 信用分配粒度 | 状态自适应调整，对关键决策（高NLL）采用细粒度信号，常规转换采用episode级信号，避免固定分辨率的缺陷 |
| 梯度权重分配 | 无需固定权重跨层级合并信号，通过步骤NLL自适应调节，适配不同步骤的信用需求 |
| 理论支撑 | 包含精确风险分解、局部动作值变异边界及误差投影分析，明确方法的理论优势 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| ALFWorld | 评估长 horizon LLM agent的任务性能 |
| WebShop | 评估长 horizon LLM agent的任务性能 |
🎯 实验设置与评估指标：任务为在ALFWorld和WebShop上完成长 horizon的LLM agent任务，评估指标为任务成功率（↑越高越好）
| 指标 | 含义 |
| ---- | ---- |
| 任务成功率 | 完成长 horizon任务的比例，↑越高越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| GRPO | 无critic的group-relative强化学习方法 | 采用轨迹级标量分配信用，无法定位关键决策 |
| GiGPO | 无critic的group-relative强化学习方法 | 恢复步骤级信号，但用固定权重合并步骤与episode级估计 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告具体数值，仅提及在ALFWorld和WebShop的1.5B、7B参数规模下，GACA的任务成功率优于GRPO和GiGPO；
2. 效率对比：论文未报告；
3. 跨域 / zero-shot 迁移：论文未报告；
4. 鲁棒性 / 扰动测试：论文未报告；
5. 消融实验：论文未报告；

4. 关键结论和发现
- GACA通过状态自适应的信用分配粒度机制，适配长 horizon LLM agent中不同步骤的信用需求，平衡了细粒度关键决策信号与episode级整体信号；
- 理论分析证明，GACA的混合策略在正方向对齐下优于固定权重的混合，且性能优于标量不确定性重加权方法；
- 在ALFWorld和WebShop任务的1.5B、7B参数规模下，GACA的任务成功率优于GRPO和GiGPO；
- 方法局限性：论文未报告；
- 未来工作：论文未报告；

> ✅ **总结一句话**：GACA通过状态自适应的信用分配粒度机制，在长 horizon LLM agent的强化学习任务中，比GRPO和GiGPO取得了更优的任务成功率，同时具备理论层面的优势保障。

</details>

---

### 8. [Beyond the Query: Do Retrieval Signals Improve Adaptive Multimodal RAG Routing?](https://arxiv.org/abs/2609.12437v1)

**Authors**: Qiaomu Li, Qiuyuan Zhang, Nong Ming  
**Category**: cs.LG  
**Published**: 2026-09-14  
**Score**: 52.5  
**Type**: new  
**ArXiv ID**: 2609.12437v1  

#### Abstract
Adaptive RAG often uses retrieval-time signals to decide whether another retrieval, reranking, or multimodal step should run. We ask whether these signals add routing value once the query itself is already known. Across document, audio, and video RAG, we compare matched query-only and query+retrieva...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Beyond the Query: Do Retrieval Signals Improve Adaptive Multimodal RAG Routing?
1. 论文的主要贡献和创新点
✅ 解决的问题：自适应RAG常采用检索时间信号来决策是否执行额外检索、重排序或多模态步骤，但过往研究未明确验证当查询本身已知时，这些检索信号是否仍具备额外的路由价值，存在默认其价值的潜在误区。
🚀 提出的新方法与思路
**控制变量的对比评估框架**：设置两组对比路由器（query-only路由器、query+retrieval路由器），固定可选动作、路由器家族、训练流程和评估设置，分别在文档、音频、视频RAG场景下对比两组路由器的路由效果，以严格验证检索信号的增量路由价值。
🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 评估严谨性 | 通过控制变量设计（匹配query-only基线的各项设置），消除其他干扰因素，可可靠判断检索信号对路由决策的增量价值 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 文档、音频、视频RAG相关数据集 | 覆盖不同模态下的自适应RAG路由任务测试 |
🎯 实验设置与评估指标
任务：在自适应RAG路由中完成RUN/SKIP决策，对比仅用查询的路由器与结合检索信号的路由器的决策效果。
| 指标 | 含义 |
|------|------|
| 论文未报告 | 论文未提供具体评估指标的名称、定义及数值结果 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| query-only路由器 | 路由决策方法 | 仅以查询为输入生成路由决策，作为基准对照 |
| query+retrieval路由器 | 路由决策方法 | 以查询结合检索信号为输入生成路由决策，其余设置与query-only路由器完全匹配 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未提供具体表号，仅在held-out最终评估中说明结果如下：
**主实验结果（held-out最终评估）**
| 对比对象 | 实验结论 |
|----------|----------|
| query+retrieval路由器 vs query-only路由器 | 添加本文测试的检索信号未产生可靠的路由改进；部分检索信号虽与后续步骤是否有用存在关联，但该可预测性未转化为更优的RUN/SKIP决策 |
💡 结论：在held-out最终评估中，本文测试的检索信号未为自适应RAG路由带来可信赖的增量价值，验证检索信号的路由价值需严格对照匹配的query-only基线。

4. 关键结论和发现
- 主要发现：
  1. 自适应RAG路由中，检索信号的增量路由价值不能默认存在，需通过与匹配的query-only基线对比来验证。
  2. 本文测试的检索信号在held-out最终评估中，未实现比query-only路由器更优的路由决策性能。
  3. 检索信号虽能关联后续步骤是否有用，但无法转化为更优的RUN/SKIP路由决策。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：本文通过控制变量的对比实验，在文档、音频、视频三类自适应RAG任务中验证发现，检索信号未为路由决策带来可靠的增量价值，强调需严格验证检索信号的路由价值而非默认其存在。

</details>

---

### 9. [SAS: Simple Attention Sparsification via End-to-End Optimization of Context Ranking](https://arxiv.org/abs/2609.13141v1)

**Authors**: Zhiwei Li, Lei Zhu, Hao Gu, Xiang Hu, Yan Wang, Haitao Mi, Sirui Han, Leo Liang, Zhijiang Guo  
**Category**: cs.CL  
**Published**: 2026-09-14  
**Score**: 48.5  
**Type**: new  
**ArXiv ID**: 2609.13141v1  

#### Abstract
Post-training attention sparsification reduces the quadratic cumulative attention cost of pretrained Transformers by selecting a small set of context units (tokens or blocks) for each query. Existing trainable methods usually use a lightweight selector to score context units, followed by hard Top-K ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

SAS: Simple Attention Sparsification via End-to-End Optimization of Context Ranking
1. 论文的主要贡献和创新点
✅ 解决的问题
现有可训练稀疏注意力方法使用轻量级选择器评分上下文单元，经硬Top-K选择阻断梯度，需依赖层密集注意力蒸馏，但此类方法中上下文单元的排名与固定注意力预算下对预测的影响不直接对齐，可能将有限预算浪费在低效单元上。

🚀 提出的新方法与思路
**Simple Attention Sparsification (SAS)**：是门控稀疏注意力机制，核心思路为在训练时将选择器的连续评分注入注意力logits，允许语言建模损失通过标准反向传播更新选择器；关键设计包括将门置于对数形式的注意力softmax内、使用归一化softmax门校准历史上下文与始终保留的当前块、保留连续选择器评分以学习相对优先级而非仅硬选择；为支持长序列训练，实现内存高效的Triton内核，将SAS整合至FlashAttention风格的计算流程中。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 任务适配性 | 在推理、长上下文理解、agentic任务上的性能均优于可训练稀疏注意力基线 |
| 注意力预算适配 | 所有测试的注意力预算下均优于基线，尤其在注意力预算紧张时增益尤为显著 |
| 梯度优化机制 | 实现选择器与语言建模损失的端到端优化，解决现有方法中硬选择阻断梯度的问题 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
在推理、长上下文理解、agentic任务上测试稀疏注意力方法的性能；论文未报告具体评估指标。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 现有可训练稀疏注意力方法 | 基线 | 采用轻量级选择器评分上下文单元，硬Top-K选择阻断梯度，依赖层密集注意力蒸馏训练 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告
2. 效率对比（FPS/参数量）：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：① SAS通过端到端优化上下文排名，解决了现有可训练稀疏注意力方法中排名与预测影响不对齐的痛点；② SAS在推理、长上下文理解、agentic任务及各注意力预算下均优于现有可训练稀疏注意力基线；③ SAS在注意力预算紧张时的性能增益尤为突出。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：SAS是一种将选择器与语言建模损失端到端优化的门控稀疏注意力机制，可有效提升Transformer注意力稀疏化效果，尤其在注意力预算紧张的场景下性能增益显著。

</details>

---

### 10. [Shards on a Shoestring: Empirical Characterization of NEAR Protocol Nightshade Sharding on Commodity Hardware](https://arxiv.org/abs/2609.12091v1)

**Authors**: Sohini Sahukar, Om Amit Gandhi, Ioan Raicu  
**Category**: cs.DC  
**Published**: 2026-09-14  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2609.12091v1  

#### Abstract
NEAR Protocol's Nightshade architecture targets one million transactions per second (TPS) through horizontal sharding of both state and computation. Published benchmarks were produced on expensive Google Cloud Platform infrastructure costing approximately \$700 per hour, leaving a significant reprod...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Shards on a Shoestring: Empirical Characterization of NEAR Protocol Nightshade Sharding on Commodity Hardware
1. 论文的主要贡献和创新点
✅ 解决的问题
现有针对NEAR Nightshade分片架构的基准测试依赖昂贵的Google Cloud Platform基础设施（约700美元/小时），导致学术研究的可复现性存在显著缺口，缺乏在商用硬件上的独立实证表征。

🚀 提出的新方法与思路
**商用硬件独立实证表征**，选用Chameleon Cloud的裸金属节点（配备48个超线程Intel Xeon核心、128GB RAM、速率80-100MB/s的HDD存储）作为实验平台；系统扫描分片数量N从1到24，测量聚合TPS、每分片TPS、区块时间、BFT终局、内存使用、磁盘I/O等指标；识别出低N时的L3缓存压力、中N时的见证人气道饱和、高N时的一致性崩溃三个 distinct 瓶颈 regimes；发现HDD写入延迟是见证人气道的隐式流量控制，移除该延迟（改用RAM-backed tmpfs）后，在N=16分片场景下出现完全链停滞，孤儿见证率飙升29倍（CPU利用率为47%）；得出聚合TPS在N=8时达峰值（较N=1提升40%）后性能反转，每分片TPS在N=24时较N=1下降23倍；为同伴SimPy sharding simulator提供首个商用硬件校准基线。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 实验硬件成本 | 采用Chameleon Cloud商用裸金属节点，替代原有昂贵GCP基础设施，大幅降低实验成本 |
| 学术可复现性 | 提供适配学术研究的低成本可复现实验基准，填补现有基准测试的可复现性缺口 |
| 分片数覆盖范围 | 系统扫描分片数量N从1到24，覆盖更广的分片数研究范围 |
| 模拟器校准支持 | 为SimPy sharding simulator提供首个商用硬件校准基线 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未明确公开使用的特定数据集 |

🎯 实验设置与评估指标
任务：在NEAR Nightshade分片架构下，评估不同分片数量及存储介质对系统性能与资源使用的影响。
| 指标 | 含义 | 方向 |
| --- | --- | --- |
| 聚合TPS | 系统总交易处理量 | ↑越高越好 |
| 每分片TPS | 单个分片的交易处理量 | ↑越高越好 |
| 区块时间 | 出块所需时间 | ↓越低越好 |
| BFT终局 | BFT共识的最终性达成状态 | 论文未报告 |
| 内存使用 | 节点内存占用情况 | 论文未报告 |
| 磁盘I/O | 节点磁盘I/O负载 | 论文未报告 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| NEAR原有GCP基准 | 现有工业基准 | 使用Google Cloud Platform高成本基础设施，每小时约700美元，学术可复现性差 |
| 本文商用硬件基准 | 本文提出的新基准 | 使用Chameleon Cloud商用裸金属节点，成本低，可复现性好 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文实验中，聚合TPS在分片数N=8时达峰值，较单分片（N=1）提升40%，之后随分片数增加性能反转；每分片TPS在N=24时较N=1下降23倍；在使用RAM-backed tmpfs（移除HDD写入延迟的隐式流量控制）的实验中，N=16分片场景下出现完全链停滞，孤儿见证率较原场景飙升29倍，此时CPU利用率为47%；识别出三个 distinct 性能瓶颈 regimes：低N时为L3缓存压力，中N时为见证人气道饱和，高N时为一致性崩溃；
💡 结论：NEAR Nightshade分片在商用硬件上的性能随分片数变化存在三个不同的瓶颈阶段，HDD写入延迟是关键隐式流量控制因素。
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验（存储介质影响）：
| 模块 | 启用/禁用 | 孤儿见证率（越低越好） | 链状态 | 聚合TPS |
| --- | --- | --- | --- | --- |
| HDD存储 | 启用 | 基线水平 | 无停滞 | 基线水平 |
| RAM-backed tmpfs | 启用（N=16场景） | 飙升29倍 | 完全停滞 | 论文未报告 |
💡 结论：移除HDD写入延迟的隐式流量控制会导致高分片数场景下的系统稳定性崩溃，验证了HDD延迟的流量控制作用。

4. 关键结论和发现
- NEAR Nightshade分片架构在商用硬件上的性能随分片数变化存在 distinct 瓶颈 regimes，低、中、高分片数分别对应L3缓存压力、见证人气道饱和、一致性崩溃三类瓶颈；
- HDD写入延迟是NEAR Nightshade见证人气道的隐式流量控制机制，移除该机制会导致N=16分片场景下的完全链停滞，显著降低系统稳定性；
- 系统聚合TPS在N=8时达峰值，继续增加分片数会导致每分片TPS大幅下降，整体性能反转；
方法局限性：仅在Chameleon Cloud指定的裸金属节点上完成实验，未覆盖其他商用硬件配置及更大分片数场景；
未来工作：可扩展至更多商用硬件配置，研究更高分片数下的性能表现，进一步完善SimPy sharding simulator的校准基线。

> ✅ **总结一句话**：该论文在商用硬件上完成了NEAR Nightshade分片架构的首个独立实证表征，揭示了其性能瓶颈的三个 distinct regimes，填补了现有基准测试的可复现性缺口，并为SimPy分片模拟器提供了商用硬件校准基线。

</details>

---

### 11. [Representation-based Masked Diffusion Model](https://arxiv.org/abs/2609.12382v1)

**Authors**: Yangrong Hu, Ding Huang, Xueyu Zhou, Jian Huang  
**Category**: cs.CL  
**Published**: 2026-09-14  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2609.12382v1  

#### Abstract
Masked Diffusion Models (MDMs) have emerged as a compelling paradigm for language modeling, offering the capability for efficient parallel text generation. However, existing parallel sampling methods typically update multiple masked tokens independently and ignore the complex mutual dependencies amo...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Representation-based Masked Diffusion Model
1. 论文的主要贡献和创新点
✅ 解决的问题
1. 现有Masked Diffusion Models（MDMs）这类并行采样方法，在更新多个被掩码的token时采用独立操作，忽略被掩码token间的复杂相互依赖关系；
2. 这种独立更新机制缺乏全局协调，可能导致输出不连贯。

🚀 提出的新方法与思路
**Representation-based Masked Diffusion Model (RMDM)**：首先利用预训练编码器将文本编码到连续语义空间，学习可逆变换以归一化表征分布至高斯先验，为生成阶段的高效采样提供便利；之后以该隐式语义表征为条件，训练掩码扩散模型学习条件文本分布，其中表征作为全局语义指导来协调并行token的更新，使模型能更准确地近似目标文本分布。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 生成质量（激进少步采样场景） | 显著提升 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务：文本生成任务
| 指标 | 含义 |
|------|------|
| 论文未报告 | 论文未报告 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告

4. 关键结论和发现
- 主要发现：
1. 现有MDMs的独立token更新机制存在缺乏全局协调的缺陷，易导致生成的文本不连贯；
2. 提出的RMDM利用预训练编码器得到的语义表征作为全局语义指导，改进了上述缺陷；
3. RMDM在激进的少步采样场景下，文本生成质量得到显著提升。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：Representation-based Masked Diffusion Model（RMDM）通过引入预训练编码器生成的语义表征作为全局语义指导，优化了Masked Diffusion Models的并行token更新机制，大幅提升了尤其在激进少步采样下的文本生成质量。

</details>

---

### 12. [CanvasAnneal: Curriculum Reinforcement Learning for Diffusion Language Models](https://arxiv.org/abs/2609.13060v1)

**Authors**: Blake Olson, Yuhang Song, Emmett McQuinn, Yuan Shangguan  
**Category**: cs.LG  
**Published**: 2026-09-14  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2609.13060v1  

#### Abstract
Diffusion Language Models (DLMs) offer promising parallel generation capabilities but lag behind autoregressive models in complex reasoning and tool-use tasks. While Reinforcement Learning (RL) has recently been applied to enhance DLMs, standard RL approaches suffer from an exploration bottleneck. T...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：CanvasAnneal: Curriculum Reinforcement Learning for Diffusion Language Models

1. 论文的主要贡献和创新点
✅ 解决的问题
Diffusion Language Models（DLMs）具备并行生成能力，但在复杂推理和工具使用任务上落后于自回归模型，应用于DLMs的标准强化学习（RL）方法存在探索瓶颈。不同方法的缺陷：①自回归模型无并行生成优势；②应用于DLMs的标准RL方法受探索瓶颈限制，性能提升受限。

🚀 提出的新方法与思路
**CanvasAnneal框架**，是一种课程引导的扩散RL框架；初始RL阶段，将教师模型生成的推理轨迹注入初始diffusion canvas，实现探索的预热；训练过程中逐步移除该教师引导，要求模型独立生成更多推理轨迹，最终完成训练。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 探索瓶颈缓解 | 通过教师推理轨迹的阶段性注入与移除，缓解扩散RL的探索瓶颈 |
| 任务性能提升 | 在数学推理和工具-use基准上优于标准diffu-GRPO |
| 收敛速度优化 | 显著加速部分任务的奖励改进速度 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| MATH500 | 数学推理基准任务 |
| Countdown | 工具-use基准任务 |
| Tau2 | 工具-use基准任务 |

🎯 实验设置与评估指标
任务为数学推理和工具-use任务，采用与标准diffu-GRPO进行对比实验；评估指标包括基准任务性能、奖励改进速度。
| 指标 | 含义 |
| --- | --- |
| 基准任务性能 | 越高越好 |
| 奖励改进速度 | 越快越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 标准diffu-GRPO | 扩散语言模型强化学习方法 | 无课程引导的标准RL流程 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（数学推理与工具-use任务）**
论文未报告具体数值，仅明确CanvasAnneal在MATH500、Countdown、Tau2上优于标准diffu-GRPO。
💡 结论：CanvasAnneal在指定数学推理和工具-use基准任务上的性能优于标准diffu-GRPO。

**效率对比**
论文未报告

**跨域 / zero-shot 迁移**
论文未报告

**鲁棒性 / 扰动测试**
论文未报告

**消融实验**
论文未报告

4. 关键结论和发现
- 主要发现：1）课程引导的扩散RL框架CanvasAnneal可通过阶段性注入与移除教师推理轨迹，有效缓解扩散RL的探索瓶颈；2）该框架在数学推理和工具-use基准任务上实现了优于标准diffu-GRPO的性能；3）该框架能显著加速部分任务的奖励收敛速度。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出CanvasAnneal课程引导的扩散RL框架，通过初始注入教师模型推理轨迹预热RL探索并逐步移除引导，缓解了扩散RL的探索瓶颈，在数学推理和工具-use基准任务上优于标准diffu-GRPO并加速了奖励提升。

</details>

---

### 13. [Inverting Self-Triggered Control: Adversarial Reinforcement Learning for Sparse Denial-of-Service Attacks](https://arxiv.org/abs/2609.12016v1)

**Authors**: Adam Haroon, Erick J. Rodr\'iguez-Seda, Tristan Schuler, Cody Fleming  
**Category**: cs.LG  
**Published**: 2026-09-14  
**Score**: 41.5  
**Type**: new  
**ArXiv ID**: 2609.12016v1  

#### Abstract
Self-triggered reinforcement learning control (RL-STC) learns the sparsest control schedule that preserves Lyapunov-decreasing stability under a Run-Time Assurance (RTA) override. We invert this: an adversarial RL agent learns the sparsest jamming or Denial-of-Service (DoS) schedule that destabilize...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Inverting Self-Triggered Control: Adversarial Reinforcement Learning for Sparse Denial-of-Service Attacks
1. 论文的主要贡献和创新点
✅ 解决的问题
自触发强化学习控制（RL-STC）学习稀疏控制调度以保证闭环Lyapunov递减稳定性，但针对STC控制器的现有DoS攻击（如贪心、周期性攻击）存在缺陷，无法在所有场景下破坏闭环稳定性：贪心攻击在Quadrotor2D LQR防御者上42%的episode无法成功，周期性攻击在Pendulum LQR防御者上97%的episode无法成功。
🚀 提出的新方法与思路
**对抗性RL逆向自触发控制**，将自触发控制的逆向逻辑应用于DoS攻击：设计对抗性RL智能体学习稀疏DoS调度，目标是破坏闭环稳定性，其Lyapunov增量允许谓词与防御者的安全证书镜像；同时证明针对满足Lyapunov合同的STC，即时保持最后一个MAC协议的对手所需的最小干扰数的植物属性下界，并恢复计数预算DoS调度的连续分组最优性的证书级模拟，扩展了DoS调度计数预算分析的适用范围（从周期性、线性时不变系统延伸至STC控制器）。
🔍 相比现有方法的优势
维度 | 优势
--- | ---
攻击成功率 | 唯一能在Pendulum、CartPole、Quadrotor2D所有植物的所有防御者上达到100%崩溃成功率的攻击方法，基线攻击存在较高失败率
干扰效率 | 每次崩溃所需的干扰时间（jam-time-per-failure）比基线攻击最多高2.8倍
鲁棒性 | 在高斯观测噪声超过初始状态幅度、仅位置观测的扰动下仍保持100%崩溃成功率，优于基线攻击

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
Pendulum、CartPole、Quadrotor2D | 用于训练和测试防御者与对抗性攻击方法，验证攻击效果和鲁棒性
🎯 实验设置与评估指标
任务为训练对抗性RL智能体攻击4类防御者（1个LQR和3个RL-STC）在3种植物上的闭环系统，评估指标如下：
指标 | 含义（箭头方向）
--- | ---
崩溃成功率 | 每个episode中成功破坏闭环稳定性的比例，越高越好（↑）
jam-time-per-failure | 每次成功崩溃所需的干扰时间，越低越好（↓）
⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
贪心攻击 | 基线攻击方法 | 采用贪心策略调度干扰资源，调度逻辑简单
周期性攻击 | 基线攻击方法 | 按固定周期调度干扰资源，调度规则固定
LQR | 防御者 | 线性二次调节器构成的自触发控制器，用于对比性能
RL-STC | 防御者 | 3个自触发强化学习控制构成的防御者，用于鲁棒性对比

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark崩溃成功率（场景：Pendulum、CartPole、Quadrotor2D）**
| 方法 | Pendulum LQR | Pendulum RL-STC | CartPole LQR | CartPole RL-STC | Quadrotor2D LQR | Quadrotor2D RL-STC |
| --- | --- | --- | --- | --- | --- | --- |
| 学到的对抗性RL智能体 | 100% ✅ | 100% ✅ | 100% ✅ | 100% ✅ | 100% ✅ | 100% ✅ |
| 贪心攻击 | 论文未报告 | 论文未报告 | 论文未报告 | 论文未报告 | 58% | 论文未报告 |
| 周期性攻击 | 3% | 论文未报告 | 论文未报告 | 论文未报告 | 论文未报告 | 论文未报告 |
💡 结论：学到的对抗性RL智能体是唯一能在所有场景下对所有防御者达到100%崩溃成功率的攻击方法，远优于基线攻击。

**表2：jam-time-per-failure对比（场景：Quadrotor2D LQR）**
| 方法 | jam-time-per-failure |
| --- | --- |
| 学到的对抗性RL智能体 | 最优（比基线高2.8倍）✅ |
| 贪心攻击 | 次优 |
| 周期性攻击 | 最差 |
💡 结论：学到的对抗性RL智能体在每次崩溃所需的干扰时间上效率最高，相比基线攻击的性能提升最多达2.8倍。

**表3：鲁棒性测试（场景：高斯观测噪声、仅位置观测）**
| 方法 | 高斯观测噪声下失败率 | 仅位置观测下失败率 |
| --- | --- | --- |
| 学到的对抗性RL智能体 | 100% ✅ | 100% ✅ |
| 贪心攻击 | 论文未报告 | 论文未报告 |
| 周期性攻击 | 论文未报告 | 论文未报告 |
💡 结论：学到的对抗性RL智能体在高斯观测噪声（超过初始状态幅度）和仅位置观测的扰动下仍保持100%崩溃成功率，具有更高的鲁棒性。

**消融实验**
论文未报告

4. 关键结论和发现
- 主要发现1：所提出的对抗性RL攻击方法，将自触发控制逆向设计为稀疏DoS攻击，在所有测试的植物和防御者上实现了100%的崩溃成功率，优于传统的贪心、周期性基线攻击。
- 主要发现2：该攻击方法在干扰效率（jam-time-per-failure）上表现最优，相比基线攻击最多提升2.8倍，且在高斯观测噪声和仅位置观测的扰动下仍保持高鲁棒性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出了一种将自触发控制逆向设计为稀疏DoS攻击的对抗性RL方法，证明了其针对STC控制器的安全性和最优性，在多个植物和防御者上实现了高效、高鲁棒的闭环稳定性破坏。

</details>

---

### 14. [Certifying Concept Unlearning in Text-to-Image Diffusion Models](https://arxiv.org/abs/2609.12163v1)

**Authors**: Mansi, Luca Marzari, Francesco Leofante  
**Category**: cs.LG  
**Published**: 2026-09-14  
**Score**: 41.5  
**Type**: new  
**ArXiv ID**: 2609.12163v1  

#### Abstract
Existing evaluations of concept unlearning in text-to-image (T2I) diffusion models primarily rely on attack success rates obtained through automated adversarial prompt search. However, these metrics provide only empirical evidence over a finite set of queries and leave residual leakage over the broa...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Certifying Concept Unlearning in Text-to-Image Diffusion Models
1. 论文的主要贡献和创新点
✅ 解决的问题
现有文本到图像(T2I)扩散模型的概念忘却评估主要依赖自动对抗提示搜索得到的攻击成功率，仅在有限查询上提供经验证据，未充分量化更广泛提示空间的残留概念泄漏，易导致高估概念忘却效果、低估安全风险。
🚀 提出的新方法与思路
**认证框架（Certification Framework）**：结合统计认证与沿概念相关嵌入方向的最坏情况分析，推导用户指定置信水平下概念泄漏概率的明确上界，为T2I扩散模型的概念忘却提供带边界误差的高置信度残留概念泄漏保证。
🔍 相比现有方法的优势
| 维度 | 现有方法不足 | 本文方法优势 |
| ---- | ---- | ---- |
| 泄漏量化覆盖范围 | 仅覆盖有限查询的提示空间 | 覆盖更广泛提示空间的残留泄漏量化 |
| 安全风险保证类型 | 仅提供有限查询的经验性证据 | 提供高置信度、带边界误差的泄漏概率上界 |
| 评估严谨性 | 易因有限查询遗漏更大空间的泄漏 | 结合最坏情况分析与统计认证，提升评估严谨性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告具体数据集名称 | 用于评估NSFW内容、艺术风格、名人身份三类概念的概念忘却效果 |
🎯 实验设置与评估指标
任务：文本到图像(T2I)扩散模型的概念忘却效果审计。
| 指标 | 含义 | 箭头 |
| ---- | ---- | ---- |
| 攻击成功率 | 对抗提示下模型生成目标概念相关内容的概率 | ↓ 越低越好 |
| 认证泄漏边界 | 带用户指定置信水平的残留概念泄漏概率上界 | 论文未明确报告箭头方向 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 论文未报告具体基线方法名称（提及六个状态-of-the-art概念忘却方法） | 概念忘却方法 | 仅基于有限查询的攻击成功率评估概念忘却效果，未提供泄漏概率的高置信度边界保证 |

3. 主要实验结果和性能指标
📊 定量结果汇总
仅按论文明确提及的核心结果呈现；其余实验模块（主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）均为“论文未报告”：
- **核心实验结果（论文未提及对应表/图编号）**
| 结果内容 | 取值 | 结论 |
| ---- | ---- | ---- |
| 认证泄漏边界与标准攻击成功率的差值 | 16.2% | 论文未明确标记最优值 |
💡 结论：基于攻击成功率的经验评估显著低估了残留概念泄漏，认证框架可发现现有方案遗漏的实质性安全风险。

4. 关键结论和发现
- 主要发现：1. 现有基于攻击成功率的经验概念忘却评估显著低估了更广泛提示空间的残留概念泄漏；2. 本文提出的认证框架可提供高置信度的泄漏概率上界，是发现上述遗漏风险的有效手段；3. 认证是文本到图像扩散模型概念忘却效果可靠审计的必要补充。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。
> ✅ **总结一句话**：本文提出的认证框架结合统计认证与最坏情况分析，弥补了现有攻击成功率评估的缺陷，为文本到图像扩散模型的概念忘却效果提供了更严谨、高置信度的残留泄漏审计方案。

</details>

---

### 15. [AMDKernelVault: Large-Scale Datasets and Agentic Training for AMD GPU Kernel Optimization](https://arxiv.org/abs/2609.12471v1)

**Authors**: Ji Liu, Saptarshi Majumder, Yiqing Huang, Wenwen Ouyang, Umang Pandey, Zeping Li, Chushi Chen, Zihao An, Puyuan Yang, Zekai Li, Sina Rafati, Ziqiong Liu, Pratik Prabhanjan Brahma, Dong Li, Zicheng Liu, Sharon Zhou, Emad Barsoum  
**Category**: cs.CL  
**Published**: 2026-09-14  
**Score**: 38.5  
**Type**: new  
**ArXiv ID**: 2609.12471v1  

#### Abstract
We introduce AMDKernelVault, an open HIP and Triton kernel corpus and training framework for recent AMD CDNA GPUs. Existing LLM-based kernel agents are largely CUDA/NVIDIA-centric and often depend on repeated frontier-LLM calls for generation, reflection, and optimization. To address this gap, we de...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

AMDKernelVault: Large-Scale Datasets and Agentic Training for AMD GPU Kernel Optimization
1. 论文的主要贡献和创新点
✅ 解决的问题
现有基于大语言模型（LLM）的内核代理大多以CUDA/NVIDIA为中心，且常依赖重复调用前沿大语言模型来完成内核的生成、反思与优化过程，缺乏针对AMD CDNA GPU的相关工具及大规模验证数据集。

🚀 提出的新方法与思路
**HIPKernelGen**：代理驱动的流水线，用于将PyTorch参考代码转换为HIP内核，在ROCm平台下完成候选代码的编译与验证，并在AMD硬件上进行延迟性能分析。
**TritonKernelGen**：代理驱动的流水线，用于将PyTorch参考代码转换为Triton内核，后续同样需在ROCm平台完成编译、验证与AMD硬件上的延迟分析。
同时，利用AMDKernelVault语料库，采用监督微调（supervised fine-tuning）和执行感知强化学习（execution-aware reinforcement learning）方法对Qwen3-8B模型进行训练，以验证语料库的实用性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 硬件适配性 | 针对AMD CDNA GPU设计，弥补了现有LLM内核代理以CUDA/NVIDIA为核心的硬件支持缺口 |
| 流程自主性 | 构建的两个代理驱动流水线可独立完成从PyTorch代码到对应AMD内核的转换、编译、验证与性能分析，无需重复依赖前沿大语言模型 |
| 语料规模性 | 包含多类执行验证的内核数据，为AMD GPU内核优化提供大规模训练资源 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| AMDKernelVault语料库（含62,153个执行验证HIP内核样本、2,377个ROCm Libraries QA条目、39,893个Triton内核） | 用于训练Qwen3-8B模型，以及验证代理驱动流水线的实用性 |

🎯 实验设置与评估指标
实验任务为将PyTorch参考代码转换为对应AMD GPU的HIP或Triton内核，并评估生成内核的正确性、编译情况与性能表现；ROCm Libraries QA条目也作为评估对象。
| 指标 | 含义 | 方向 |
| ---- | ---- | ---- |
| Pass@1 | PyTorch-to-HIP任务中，1次生成流程内的内核正确性通过率 | 越高越好 |
| Corr@3 | TritonBench-G和ROCmBench任务中，3次生成流程内的内核正确性率 | 越高越好 |
| 编译指标 | 生成内核在ROCm平台的编译成功率 | 越高越好 |
| 速度指标 | 生成内核在AMD硬件上的执行性能 | 越低越好 |

⚔️ 基线方法对比
论文未报告基线方法的具体名称、类型及特点。

3. 主要实验结果和性能指标
📊 定量结果汇总
**PyTorch-to-HIP任务（摘要提及）**
| 指标 | 数值 | 最优标识 |
| ---- | ---- | ---- |
| Pass@1 | 34.0% | ✅（为所比较模型中的最高正确性） |
💡 结论：训练的Qwen3-8B在PyTorch-to-HIP转换任务的1次生成内正确性通过率达到所比较模型的最高水平。

**TritonBench-G任务（摘要提及）**
| 指标 | 数值 | 最优标识 |
| ---- | ---- | ---- |
| Corr@3 | 33.2% | ✅（为所比较模型中的最高正确性） |
💡 结论：训练的Qwen3-8B在TritonBench-G任务的3次生成内正确性率达到所比较模型的最高水平。

**ROCmBench任务（摘要提及）**
| 指标 | 数值 | 最优标识 |
| ---- | ---- | ---- |
| Corr@3 | 41.94% | ✅（为所比较模型中的最高正确性） |
💡 结论：训练的Qwen3-8B在ROCmBench任务的3次生成内正确性率达到所比较模型的最高水平。

其他实验：
1. 主 benchmark 性能（L2/碰撞率等）：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现
1. 论文构建了针对AMD CDNA GPU的大规模执行验证内核语料库AMDKernelVault，涵盖HIP、Triton内核样本及ROCm Libraries QA条目；
2. 基于AMDKernelVault训练的Qwen3-8B，在PyTorch-to-HIP、TritonBench-G、ROCmBench三个基准任务的正确性指标上，达到所比较模型中的最高水平；
3. 该方法在编译指标和速度指标上，未表现出全面领先于所比较模型的结果。
- 方法局限性：在编译性能和实际运行速度方面，训练后的Qwen3-8B无法实现对所比较模型的全面超越。
- 未来工作：论文未明确报告未来工作方向。

> ✅ **总结一句话**：AMDKernelVault是针对AMD CDNA GPU的大规模执行验证内核语料库，其配套的代理驱动转换流水线及训练的Qwen3-8B模型，在相关基准任务的正确性上取得了所比较模型的最高表现，填补了现有LLM内核代理对AMD硬件支持不足的空白。

</details>

---

### 16. [ForgeMegakernel: A General Framework for Efficient Auto-Regressive Model Decode Megakernels](https://arxiv.org/abs/2609.12379v1)

**Authors**: Leshan Li, Zhui Zhu, Xianglong Deng, Yaojian Chen, Qingfeng He, Yuxuan Li, Rong Zhao, Xu Han, Zhiyuan Liu  
**Category**: cs.DC  
**Published**: 2026-09-14  
**Score**: 37.5  
**Type**: new  
**ArXiv ID**: 2609.12379v1  

#### Abstract
Auto-regressive model decode is bandwidth-bound, since every weight and key/value-cache byte crosses high-bandwidth memory once per token. A megakernel is an ideal solution, but existing automatic megakernel generation approaches cannot achieve both generalization across models and correctness guara...

---

### 17. [Fixed State, Long Reach: What a Constant-Size Cache Buys Block Diffusion at Scale](https://arxiv.org/abs/2609.11998v1)

**Authors**: Vaibhav Singh, Pierre-Andr\'e No\"el, Torsten Scholak, Eugene Belilovsky, Oleksiy Ostapenko  
**Category**: cs.LG  
**Published**: 2026-09-14  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2609.11998v1  

#### Abstract
Diffusion language models decode tokens in parallel, but their bidirectional denoiser rules out the naive key--value (KV) cache behind fast autoregressive inference. Block diffusion restores caching by decoding block-by-block, and the block caches deployed on it so far are tied to attention: O(L)in ...

---

### 18. [Quality-Constrained Routing over a Fixed Pool of Quantized Mixture-of-Experts Instances](https://arxiv.org/abs/2609.12550v1)

**Authors**: Zhenghong Huang, Hongfan Wu, Jiheng Zhang  
**Category**: cs.LG  
**Published**: 2026-09-14  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2609.12550v1  

#### Abstract
Quantized Mixture-of-Experts (MoE) services can hold several pre-materialized instances of one base model, but quantization damage varies sharply across requests and bitwidths. Because instance materialization and replica counts consume memory and require slow reconfiguration, we treat them as upstr...

---

### 19. [Certified Safety Curation: Distribution-Free Guarantees for Safe Offline Reinforcement Learning](https://arxiv.org/abs/2609.12014v1)

**Authors**: Adam Haroon, Cody Fleming  
**Category**: cs.LG  
**Published**: 2026-09-14  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2609.12014v1  

#### Abstract
Safe offline reinforcement learning assumes a cost function on every transition. We ask what remains possible when safety can be judged only by comparing short clips and occasionally asking whether an episode exceeded its budget. Certified safety curation answers with a filter-then-clone pipeline: a...

---

### 20. [Offline Reinforcement Learning for Wind Farm Control: A Wind Tunnel Study under Dynamic Wind Directions](https://arxiv.org/abs/2609.12905v1)

**Authors**: Yuhan Su, Hongyang Dong, Simone Tamaro, Filippo Campagnolo, Carlo L. Bottasso, Xiaowei Zhao  
**Category**: cs.LG  
**Published**: 2026-09-14  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2609.12905v1  

#### Abstract
This paper addresses the wind farm power maximization problem in the presence of wind direction changes. Specifically, a model-free Modified Twin Delayed Deep Deterministic Policy Gradient with Behavior Cloning (MTD3-BC) algorithm is proposed to tackle this task through yaw control under varying win...

---

### 21. [MCRL2: Multi-resource Cross-attention-based Representation Learning-augmented Reinforcement Learning for Cloud Microservice Scheduling](https://arxiv.org/abs/2609.13048v1)

**Authors**: Tiangang Li, Shi Ying, Xiangbo Tian, Chuan Shi, Ding Xiao  
**Category**: cs.LG  
**Published**: 2026-09-14  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2609.13048v1  

#### Abstract
Efficient microservice scheduling is crucial for maintaining load balance across nodes in data centers and ensuring high quality of service. However, achieving this in practice remains challenging due to dynamic resource imbalance under fluctuating workloads, nonlinear coupling across multiple resou...

---

### 22. [A Unified and Constrained View of Regularization-Based Robust Reinforcement Learning](https://arxiv.org/abs/2609.13050v1)

**Authors**: Amine Andam, Jamal Bentahar, Mustapha Hedabou  
**Category**: cs.LG  
**Published**: 2026-09-14  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2609.13050v1  

#### Abstract
Regularization-based methods have become a standard approach for training Deep Reinforcement Learning policies against adversarial input perturbations. In this paper, we unify these methods by deriving new upper bounds on the performance gap between the nominal and worst-case policies. Each upper bo...

---

### 23. [Groupoid-Based Internal State Representations for Reinforcement Learning with Local Symmetries](https://arxiv.org/abs/2609.13035v1)

**Authors**: Ben Opperman, Eduardo Alonso, Esther Mondrag\'on  
**Category**: cs.LG  
**Published**: 2026-09-14  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2609.13035v1  

#### Abstract
Symmetries play a central role in reducing the complexity of reinforcement learning problems, yet most existing approaches rely on fixed group actions or predefined state abstractions. Classical reinforcement learning algorithms typically assume a globally structured Markov decision process with uni...

---

### 24. [Attention Quantization for Tabular Foundation Models](https://arxiv.org/abs/2609.13031v1)

**Authors**: Jonas M. K\"ubler, Benjamin J\"ager, Klemens Fl\"oge, Noah Hollmann, Frank Hutter  
**Category**: cs.LG  
**Published**: 2026-09-14  
**Score**: 28.5  
**Type**: new  
**ArXiv ID**: 2609.13031v1  

#### Abstract
With the recent rise and adoption of tabular foundation models, optimizing their inference performance becomes an emerging field for efficiency research. While the models are architecturally similar to transformer-based large language models (LLMs), the size and serving patterns differ significantly...

---

### 25. [Amortized Low-Rank Adaptation for Model-Based Reinforcement Learning](https://arxiv.org/abs/2609.12278v1)

**Authors**: Fernando Palafox, David Fridovich-Keil  
**Category**: cs.LG  
**Published**: 2026-09-14  
**Score**: 24.0  
**Type**: new  
**ArXiv ID**: 2609.12278v1  

#### Abstract
World models let agents plan by predicting the consequences of their actions, but changes in the environment can make them inaccurate. We study the problem of adapting a world model to an unknown test-time environment, drawn from a known environment family, using only a few episodes of interaction. ...

---

### 26. [Calibrated Ambiguity in Multimodal Language Models: Humans reach for cultural references, while models describe the picture](https://arxiv.org/abs/2609.12575v1)

**Authors**: Cody Kommers, Mingrui Ye, Evelyn Gius, Daniela Mihai, Hoyt Long, Zheng Yuan, Drew Hemment  
**Category**: cs.CL  
**Published**: 2026-09-14  
**Score**: 22.5  
**Type**: new  
**ArXiv ID**: 2609.12575v1  

#### Abstract
Ambiguity is often treated as a bug for AI systems to resolve---but in human communication and culture, ambiguity can also be a generative resource. From humour to politics to art, people express themselves in words and images that are open enough to invite different interpretations, yet constrained...

---

### 27. [FINESSE: An Agent-Based Simulator and Benchmark Dataset for Multimodal Financial Event Sequences](https://arxiv.org/abs/2609.11993v1)

**Authors**: Tyler Farnan, Benjamin Eng, Adam Abate, Xirui Hou, Rizal Fathony, Nam H. Nguyen, Senthil Kumar  
**Category**: cs.LG  
**Published**: 2026-09-14  
**Score**: 22.5  
**Type**: new  
**ArXiv ID**: 2609.11993v1  

#### Abstract
Machine learning research in financial services is limited by the scarcity of representative open-source datasets. Existing resources are often narrowly focused on a single modality or task and fail to reflect the structured, multimodal, and dynamic nature inherent to many problems in financial serv...

---

### 28. [Where Decoder Cosine Similarity Fails for SAE Feature Flow Discovery](https://arxiv.org/abs/2609.12591v1)

**Authors**: Hendrik Droste, Christian Medeiros Adriano, Kathrin Korte, Holger Giese  
**Category**: cs.LG  
**Published**: 2026-09-14  
**Score**: 22.5  
**Type**: new  
**ArXiv ID**: 2609.12591v1  

#### Abstract
Foundation models are increasingly adapted through fine-tuning, model editing, and alignment procedures while retaining previously acquired capabilities. Understanding the internal computations that support these adaptations is therefore becoming increasingly important for continual model evolution....

---

### 29. [Zipbench: Low-Cost Framework for Compressing Comprehensive Benchmarks of Large Language Models](https://arxiv.org/abs/2609.12475v1)

**Authors**: Zhongzhan Huang, Junxin Li, Guoming Ling, Yupei Lin, Shanshan Zhong, Hefeng Wu  
**Category**: cs.CL  
**Published**: 2026-09-14  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2609.12475v1  

#### Abstract
Comprehensive benchmark suites are essential for improving large language models (LLMs), but many widely used benchmarks are redundant, making evaluation unnecessarily expensive. Although recent benchmark compression methods (BCMs) can mitigate this cost, many strong BCMs rely on large collections o...

---

### 30. [Vortex: Bridging Extreme Compression and Efficient LLM Inference](https://arxiv.org/abs/2609.12208v1)

**Authors**: Haoxuan Shan, Cong Guo, Bowen Duan, Chiyue Wei, Feng Cheng, Yuzhe Fu, Yintao He, Hai "Helen" Li, Yiran Chen  
**Category**: cs.AR  
**Published**: 2026-09-14  
**Score**: 18.5  
**Type**: new  
**ArXiv ID**: 2609.12208v1  

#### Abstract
Extreme compression techniques, including vector quantization (VQ) and input-dependent sparsity, can significantly reduce the memory footprint of large language models (LLMs). However, a key challenge remains in translating such compression into practical efficiency. On conventional systolic-array-b...

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
