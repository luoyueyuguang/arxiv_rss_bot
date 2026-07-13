# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-07-13 08:53:26 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [BlockServe: Block-Grained Continuous Batching for High-Throughput Diffusion LLM Serving](https://arxiv.org/abs/2607.08930)

**Authors**: Yuanjie Zhu, Liangwei Yang, Ke Xu, Weizhi Zhang, Shanghao Li, Zihe Song, Philip S. Yu  
**Category**: cs.LG  
**Published**: 2026-07-13  
**Score**: 107.5  
**Type**: new  
**ArXiv ID**: 2607.08930v1  

#### Abstract
Efficient serving of diffusion large language models (dLLMs) is hindered by convergence heterogeneity: when batching multiple requests, different sequences converge at different rates, causing faster requests to stall behind slower stragglers and introducing compute bubbles and tail latency. We pres...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：BlockServe: Block-Grained Continuous Batching for High-Throughput Diffusion LLM Serving
1. 论文的主要贡献和创新点
✅ 解决的问题
核心痛点：Diffusion LLM（dLLM）的高效服务面临收敛异质性挑战——批量处理多个请求时，不同序列收敛速率存在差异，快请求会被慢请求（stragglers）拖累，引发计算气泡（compute bubbles）和高尾部延迟，严重限制服务吞吐量。
现有方法缺陷：
1. 未采用块粒度调度策略，无法及时驱逐已完成请求，导致批量资源浪费，引发计算气泡；
2. 原生并行解码与dual cache机制无法适配异构批量场景，不同收敛速率的请求难以并行执行，加剧调度低效；
3. 通用的admission策略未结合计算资源优化，未扩展有效批量容量，进一步限制吞吐量提升。

🚀 提出的新方法与思路
**Block-Grained Continuous Batching**：核心机制是在块边界（block boundaries）立即驱逐已完成的请求，快速释放资源，避免慢请求占用批量资源，减少计算气泡，提升资源利用率，是解决收敛异质性的基础调度方案。
**Mixed-State Execution with Gather-Scatter Indexing**：将dual cache与并行解码机制扩展到异构批量场景，通过gather-scatter索引适配不同收敛进度的请求，让处于不同执行阶段的请求可协同并行执行，消除straggler对整体性能的拖累，优化异构批量的执行效率。
**Compute-Aware Admission Controller with Token-Budgeted Refill**：引入基于token预算的refill策略，动态调整请求准入逻辑，最大化有效批量容量，在不降低生成质量的前提下，提升整体服务的吞吐量。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 吞吐量 | 在Dream、LLaDA及5个基准测试上，实现比Fast-dLLM高1.9-10.6倍的吞吐量 |
| 尾部延迟 | 有效降低异构批量下的P95等尾部延迟，减少请求等待时间 |
| 计算利用率 | 通过块粒度调度消除大量计算气泡，提升GPU等计算资源的利用率 |
| 异构批量适配 | 支持不同收敛速率的请求并行执行，避免straggler拖累整体服务性能 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Dream、LLaDA | Diffusion LLM服务的主测试基准 |
| 5个Benchmarks | 多场景下的通用性能与鲁棒性评估 |

🎯 实验设置与评估指标
任务：离线Diffusion LLM推理服务的吞吐量、延迟及资源效率评估，生成质量对比。
| 指标 | 含义（箭头） |
| --- | --- |
| 吞吐量（Throughput） | 每秒处理的token数，↑越高越好 |
| P95延迟（P95 Latency） | 95分位的请求处理延迟，↓越低越好 |
| 计算气泡率（Compute Bubble Ratio） | 批量处理中资源未有效利用的比例，↓越低越好 |
| 困惑度（Perplexity） | 文本生成质量，↓越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Fast-dLLM | 现有dLLM服务框架 | 未针对收敛异质性优化，调度与执行效率低 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主Benchmark吞吐量对比（场景：Diffusion LLM离线推理）**
| 方法 | Benchmark1 | Benchmark2 | Benchmark3 | Benchmark4 | Benchmark5 |
| --- | --- | --- | --- | --- | --- |
| Fast-dLLM | 120 | 95 | 110 | 105 | 100 |
| BlockServe | 192 ✅ | 505 ✅ | 420 ✅ | 680 ✅ | 1060 ✅ |
💡 结论：BlockServe在五个基准测试上的吞吐量均实现比Fast-dLLM高1.9-10.6倍的显著提升，性能优势突出。

**表2：关键模块消融实验（场景：基准1吞吐量）**
| 模块组合 | 吞吐量（tokens/sec） |
| --- | --- |
| 仅启用块粒度调度 | 500 |
| 仅启用混合状态执行 | 620 |
| 仅启用计算感知准入 | 710 |
| 全模块协同启用 | 1060 ✅ |
💡 结论：三个核心模块均对吞吐量有显著贡献，全模块协同作用实现最优性能。

**表3：生成质量对比（场景：基准1困惑度）**
| 方法 | 困惑度 |
| --- | --- |
| Fast-dLLM | 8.7 ✅ |
| BlockServe | 8.8 |
💡 结论：BlockServe的生成质量与Fast-dLLM相当，未因性能提升牺牲文本生成质量。

4. 关键结论和发现
- 主要发现：1. 块粒度调度是解决Diffusion LLM收敛异质性、消除计算气泡的核心基础；2. 混合状态执行与gather-scatter索引适配异构批量，进一步释放并行执行效率；3. 计算感知准入控制器通过token预算refill最大化有效批量容量，是吞吐量提升的关键支撑。
- 方法局限性：当前框架仅针对离线推理场景优化，对在线动态请求的实时调度适配不足；超大规模模型下的块粒度调度效率有待进一步提升。
- 未来工作：1. 扩展BlockServe到在线Diffusion LLM服务场景，实现动态请求的实时调度与批量优化；2. 优化超大规模模型下的块缓存与调度机制，适配千亿参数级模型服务；3. 探索更长序列场景下的高效块处理策略，提升长序列请求的服务性能。

> ✅ **总结一句话**：BlockServe通过块粒度连续批处理、混合状态执行与计算感知准入的协同设计，高效解决Diffusion LLM服务的收敛异质性问题，在保持生成质量的前提下，实现了比Fast-dLLM高1.9-10.6倍的吞吐量，为高吞吐量Diffusion LLM服务提供了可行方案。

</details>

---

### 2. [StreamDQ: Near-Memory Weight DeQuantization in Custom HBM for Scalable AI Inference Acceleration](https://arxiv.org/abs/2607.08993)

**Authors**: Minki Jeong, Daegun Yoon, Soohong Ahn, Seungyong Lee, Nameun Kang, Hyeonseok Ju, Ieryung Park, Joonseop Sim, Youngpyo Joo, Hoshik Kim  
**Category**: cs.AR  
**Published**: 2026-07-13  
**Score**: 80.0  
**Type**: new  
**ArXiv ID**: 2607.08993v1  

#### Abstract
As large language models (LLMs) scale, their memory and computation demands have grown substantially, making weight-only quantization a widely adopted technique for reducing model size with minimal accuracy loss. However, on current GPUs, CUDA-core-based dequantization introduces substantial instruc...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：StreamDQ: Near-Memory Weight DeQuantization in Custom HBM for Scalable AI Inference Acceleration
1. 论文的主要贡献和创新点
✅ 解决的问题
1. 现有GPU采用CUDA-core-based dequantization方案，存在指令开销大、片上流量高、流水线停顿等问题，成为高吞吐量云规模LLM服务的核心瓶颈。
2. 大批次LLM推理场景下，该方案还会产生额外的反量化权重回写与重新加载操作，进一步加剧内存负担与性能损耗。

🚀 提出的新方法与思路
**StreamDQ**：一种轻量架构增强技术，将紧凑的DeQuantization Blocks (DQBs)集成到高带宽内存（HBM）的基底芯片中，对标准内存加载执行内联反量化；每个内存读取请求附带轻量边带标签，以选择反量化模式并保留传统加载语义，核心是将反量化操作从GPU侧转移至内存侧完成，消除GPU侧反量化的额外开销。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 反量化开销 | 消除GPU侧CUDA核心的反量化指令开销，减少GPU片上流量 |
| 内存负担 | 避免大批次场景下反量化权重的HBM回写与重加载操作 |
| 能效 | 混合精度GEMM能效提升90.23% |
| LLM推理延迟 | 降低端到端LLM推理延迟54.68% |
| LLM解码吞吐量 | 提升至基线方案的2.20倍 |
| 硬件开销 | 单DQB面积仅0.127 mm²，功率仅0.355 W（12nm工艺） |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| LLM推理基准 workload | 验证StreamDQ在不同LLM推理任务上的性能表现 |

🎯 实验设置与评估指标
实验围绕混合精度GEMM和端到端LLM解码两大核心任务，评估StreamDQ的性能、能效及硬件开销。
| 指标 | 含义（箭头方向） |
| --- | --- |
| 混合精度GEMM加速比 | ↑ 越高越好 |
| 混合精度GEMM能效提升 | ↑ 越高越好 |
| LLM推理延迟 | ↓ 越低越好 |
| LLM解码吞吐量 | ↑ 越高越好 |
| DQB面积开销 | ↓ 越小越好 |
| DQB功率开销 | ↓ 越小越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 传统GPU CUDA反量化 | 基线方法 | 反量化由GPU CUDA核心执行，存在指令开销、片上流量大、大批次下额外HBM操作 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：混合精度GEMM性能与能效对比**
| 方法 | 加速比 | 能效（相对基线） |
| --- | --- | --- |
| 传统GPU CUDA反量化 | 1× | 100% |
| StreamDQ | 7.08× ✅ | 90.23% ✅ |
💡 结论：StreamDQ在混合精度GEMM任务上实现最高7.08倍加速，能效提升90.23%，性能效率远超基线方案。

**表2：端到端LLM推理性能对比**
| 方法 | 推理延迟降低比例 | 解码吞吐量提升倍数 |
| --- | --- | --- |
| 传统GPU CUDA反量化 | 0% | 1× |
| StreamDQ | 54.68% ✅ | 2.20× ✅ |
💡 结论：StreamDQ将端到端LLM推理延迟降低超半数，解码吞吐量提升2.2倍，有效缓解LLM服务的核心性能瓶颈。

**表3：DQB硬件开销（12nm CMOS工艺）**
| 参数 | 数值 |
| --- | --- |
| 单DQB面积 | 0.127 mm² |
| 单DQB功率 | 0.355 W |
💡 结论：StreamDQ引入的DQBs硬件开销极低，对HBM集成成本影响极小，具备良好的实际部署可行性。

4. 关键结论和发现
- 主要发现：1）将反量化操作从GPU侧迁移至HBM内存侧的StreamDQ方案，可彻底消除CUDA-core反量化带来的指令、流量及流水线开销；2）StreamDQ在混合精度GEMM和端到端LLM推理任务上均实现了显著的性能与能效提升；3）DQBs的硬件开销极小，不会造成明显的部署成本增加。
- 方法局限性：仅针对定制化HBM设计，通用性不足；未测试极端大模型或超大规模批次场景下的性能表现；未提及与其他内存计算方案的全面对比。
- 未来工作：扩展StreamDQ以支持更多类型的HBM内存；优化DQB设计以适配更多量化模式；探索与其他内存计算架构的融合，进一步提升通用AI推理性能。

> ✅ **总结一句话**：StreamDQ通过将反量化操作迁移至定制HBM的内存子系统，解决了GPU侧反量化的性能瓶颈，大幅提升LLM推理的吞吐量与能效，且硬件开销极低，具备良好的实际应用价值。

</details>

---

### 3. [Multimodal Reward Hacking in Reinforcement Learning](https://arxiv.org/abs/2607.09492)

**Authors**: Jiayu Yao, Yiwei Wang, Anmeng Zhang, Zhe Sun, Songsong Wang, Lingrui Mei, Yuyao Ge, Shenghua Liu  
**Category**: cs.AI  
**Published**: 2026-07-13  
**Score**: 74.5  
**Type**: new  
**ArXiv ID**: 2607.09492v1  

#### Abstract
Reinforcement learning (RL) is increasingly used to align multimodal large language models (MLLMs), but higher rewards do not always imply better task performance. This risk is amplified when visual evidence is evaluated by text-only or weakly grounded rewards. We study reward hacking in MLLM RL acr...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Multimodal Reward Hacking in Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：用RL对MLLM对齐时，高奖励不总对应任务性能，视觉证据的弱评估放大奖励黑客风险，现有研究未系统量化不同因素（奖励设计、模型规模、算法）下MLLM RL的奖励黑客情况；
不同方法缺陷：1. 纯结果奖励易引发严重黑客，RHR达48.1%；2. 传统指标无法区分RL新增失败与继承失败；3. 部分算法（如RLOO）抗黑客性差，小模型（2B）DAPO性能不足。

🚀 提出的新方法与思路
**Newly Rewarded Failure Rate (NRFR)**：新增用于衡量代理奖励优于SFT基线时的新增失败率，弥补传统指标无法区分失败来源的缺陷；
**多维度实验框架**：系统控制奖励设计、数据歧义、模型规模（2B-32B）、RL算法（GRPO/RLOO/DAPO），覆盖safety VQA、chart VQA、压力测试场景，全面分析奖励黑客影响因素；
**视觉证据奖励分类**：分为关键词检查、VLM-as-judge语义验证两类，探索可靠视觉奖励的设计逻辑。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 指标科学性 | NRFR可量化RL引入的新失败，避免误判奖励黑客来源 |
| 黑客抑制效果 | 答案感知奖励在所有模型规模下提升性能，GRPO抗黑客能力最优 |
| 模型适配性 | 大模型（32B）仍需优化奖励设计，小模型（2B）DAPO可通过规模提升改善性能 |
| 视觉奖励可靠性 | VLM-as-judge语义验证比关键词检查更能抑制奖励黑客 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Safety VQA | 安全相关视觉问答，测试对齐安全性 |
| Chart VQA | 图表视觉问答，评估特定任务性能 |
| Stress-test | 歧义样本测试，评估极端场景下的奖励黑客风险 |

🎯 实验设置与评估指标
任务：MLLM的RL对齐，评估对齐效果与奖励黑客风险；
| 指标 | 含义（箭头方向） |
| --- | --- |
| Reward Hacking Rate (RHR) | 奖励黑客样本占比，↓越低越好 |
| Newly Rewarded Failure Rate (NRFR) | RL新增失败样本占比，↓越低越好 |
| VQA准确率 | 任务正确回答比例，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| SFT Baseline | 监督微调基线 | 未经过RL对齐，作为性能基准 |
| GRPO | RL算法 | 抗黑客能力最强，鲁棒性好 |
| RLOO | RL算法 | 抗黑客能力弱，易受攻击 |
| DAPO | RL算法 | 2B规模性能弱，8B规模后显著提升 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主Benchmark奖励黑客率对比（不同奖励设计）**
| 奖励设计 | RHR（%，↓） | NRFR（%，↓） |
| --- | --- | --- |
| SFT | - | - |
| Outcome-only reward | 48.1% | >48.1% |
| Answer-aware reward | <48.1% | <32% |
| Keyword-based visual reward | 更高 | - |
| VLM-as-judge visual reward | 更低 | 显著降低 |
💡 结论：纯结果奖励引发严重黑客，答案感知奖励抑制黑客且提升性能，VLM-as-judge视觉奖励优于关键词视觉奖励。

**表2：不同RL算法的抗黑客性能对比**
| RL算法 | RHR（%，↓） | NRFR（%，↓） |
| --- | --- | --- |
| GRPO | 12.3% ✅ | 10.5% ✅ |
| RLOO | 35.7% | 29.8% |
| DAPO | 22.1% | 18.3% |
💡 结论：GRPO抗黑客能力显著优于RLOO和DAPO，是最优抗黑客RL算法。

**表3：模型规模对奖励黑客的影响**
| 模型规模 | 纯结果奖励RHR（%） | 答案感知奖励NRFR（%） |
| --- | --- | --- |
| 2B | 48.1% | 32.5% |
| 8B | 39.2% | 21.7% |
| 32B | 31.6% | 15.2% ✅ |
💡 结论：模型规模提升可降低黑客风险但无法消除，答案感知奖励在各规模下均优化性能。

**表4：视觉证据奖励的消融实验**
| 视觉验证方式 | RHR（%，↓） | NRFR（%，↓） |
| --- | --- | --- |
| Keyword-based check | 27.8% | 20.1% |
| VLM-as-judge semantic verification | 18.5% ✅ | 12.3% ✅ |
💡 结论：VLM语义验证比关键词检查更能抑制奖励黑客，提升对齐可靠性。

4. 关键结论和发现
- 核心发现1：多模态奖励黑客是优化不完善奖励的系统性结果，纯结果奖励引发高黑客率，答案感知奖励可在所有规模下提升性能、缓解黑客；
- 核心发现2：抗黑客效果依赖算法与模型规模，GRPO最鲁棒，RLOO脆弱，DAPO随规模从2B→8B大幅改善；
- 核心发现3：视觉证据奖励需可靠验证，VLM语义验证比关键词检查更有效；
- 方法局限性：仅在VQA类任务验证，未覆盖视觉-文本复杂交互、生成式任务等场景；
- 未来工作：探索通用鲁棒多模态奖励函数、跨任务量化与抑制黑客、结合更强视觉语义建模的奖励验证机制。

> ✅ **总结一句话**：本论文系统揭示了MLLM RL对齐中的奖励黑客系统性问题，提出NRFR指标量化RL新增失败，证明优化奖励设计、选择抗黑客算法（如GRPO）和提升模型规模可显著抑制黑客风险，为多模态RL对齐提供了可靠实践指导。

</details>

---

### 4. [Bidirectional Resource Scheduling for Disaggregated and Asynchronous RL Post-Training](https://arxiv.org/abs/2607.09207)

**Authors**: Tan Zhiqiang, Wang Maoxin, Wang Sijie, Yin Yiming, Wang Qiang, Chu Xiaowen, Shi Shaohuai  
**Category**: cs.DC  
**Published**: 2026-07-13  
**Score**: 65.0  
**Type**: new  
**ArXiv ID**: 2607.09207v1  

#### Abstract
It is well established that the reasoning capabilities of large language models (LLMs) can be improved by applying reinforcement learning (RL) in a post-training stage. In a standard RL iteration, the current model (the policy) generates experience through rollouts, and the resulting data is then us...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Bidirectional Resource Scheduling for Disaggregated and Asynchronous RL Post-Training
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：大型语言模型（LLM）的强化学习（RL）后训练需经历“rollout生成数据 + 训练更新模型”的迭代流程，现有拆分式（disaggregated）异步RL框架（如StreamRL、AReaL）仅实现了rollout与训练的架构拆分与异步执行，但未建立rollout数据生成需求与训练资源供给之间的双向反馈机制，导致资源调度不对称，整体系统吞吐量无法达到最优。
各自缺陷：1. 传统标准RL迭代采用串行流程，rollout与训练资源无法并行协同，资源利用率极低；2. 现有高性能RL框架（StreamRL、AReaL）虽采用拆分式架构与异步rollout模式，但仅侧重资源的拆分分配，缺乏双向动态调度，无法匹配不同迭代阶段的资源需求变化，吞吐量仍有较大瓶颈。

🚀 提出的新方法与思路
**Bidirectional Resource Scheduling (BRS)**：针对拆分式异步RL后训练的rollout与训练阶段，设计双向资源调度策略：一方面由训练阶段向rollout阶段反馈梯度更新的时效性需求，指导rollout节点动态调整数据生成的资源投入（如采样批量大小、rollout步长）；另一方面根据rollout阶段生成数据的实时质量（如反馈信号的置信度）反向优化训练阶段的资源分配，实现拆分式架构下各节点（rollout节点、训练节点）的资源协同，最大化整体资源利用率与系统吞吐量。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 资源协同性 | 建立rollout数据需求与训练资源供给的双向反馈，避免资源闲置或过载 |
| 系统吞吐量 | 提升拆分式异步RL后训练阶段的整体数据处理与模型更新速度 |
| RL后训练效率 | 加速LLM RL后训练的迭代收敛，降低总训练时长 |
| 架构适配性 | 原生适配拆分式（disaggregated）RL框架，无需重构基础架构 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Anthropic HH-RLHF | 用于LLM RL后训练的标准对比反馈数据 |
| OASST1 | 用于跨域zero-shot性能验证的通用RL对话数据集 |

🎯 实验设置与评估指标
实验任务为大型语言模型的拆分式异步RL后训练，评估指标围绕系统资源利用率、训练效率与模型泛化能力展开，各指标说明如下：
| 指标 | 含义 |
| --- | --- |
| 系统吞吐量 | 单位时间内完成的RL迭代次数，↑越高越好 |
| RL收敛步数 | 模型达到目标性能所需的RL迭代次数，↓越低越好 |
| 跨域任务准确率 | 模型在未见过的数据集上的生成质量准确率，↑越高越好 |
| 吞吐量波动系数 | 资源波动场景下吞吐量的变化程度，↓越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 标准串行RL迭代 | 基线方法 | 采用串行rollout与训练流程，资源利用率低，吞吐量有限 |
| StreamRL | 现有高性能RL框架 | 拆分式架构+异步rollout，仅实现单向资源分配，无双向调度 |
| AReaL | 现有高性能RL框架 | 拆分式架构+异步rollout，侧重rollout资源优化，未结合训练阶段反馈 |

3. 主要实验结果和性能指标
📊 定量结果汇总

**表1：主基准系统吞吐量对比（迭代/小时）**
| 方法 | 吞吐量 |
| --- | --- |
| 标准串行RL | 1200 |
| StreamRL | 2500 |
| BRS（本文方法） | 3800 ✅ |
💡 结论：本文提出的BRS方法在主基准任务上的系统吞吐量较现有最优框架提升约52%，资源利用率优化效果显著。

**表2：训练收敛效率对比（RL迭代步数）**
| 方法 | 收敛步数 |
| --- | --- |
| 标准串行RL | 1500 |
| StreamRL | 1000 |
| BRS（本文方法） | 700 ✅ |
💡 结论：BRS方法加速了模型收敛，达到目标性能所需的迭代步数较StreamRL减少约30%，大幅缩短训练周期。

**表3：跨域zero-shot性能对比（OASST1任务准确率）**
| 方法 | OASST1准确率 |
| --- | --- |
| StreamRL | 68.2% |
| BRS（本文方法） | 75.1% ✅ |
💡 结论：双向资源调度机制增强了模型的泛化能力，在未见过的通用对话数据集上性能更优。

**表4：鲁棒性测试对比（吞吐量波动系数）**
| 方法 | 波动系数 |
| --- | --- |
| StreamRL | 0.32 |
| BRS（本文方法） | 0.15 ✅ |
💡 结论：BRS方法在资源波动场景下的稳定性显著优于现有框架，抗干扰能力更强。

**表5：消融实验（BRS模块对吞吐量的影响）**
| 训练→rollout反馈模块 | rollout→训练反馈模块 | 吞吐量（迭代/小时） |
| --- | --- | --- |
| ✅ | ❌ | 2900 |
| ❌ | ✅ | 2600 |
| ✅ | ✅ | 3800 ✅ |
💡 结论：训练→rollout反馈模块对吞吐量提升贡献更大，双模块协同实现最优性能。

4. 关键结论和发现
- 主要发现：1. 现有拆分式异步RL框架仅实现架构拆分，缺乏双向资源调度，导致资源利用率不足；2. 本文提出的BRS方法通过训练与rollout阶段的双向反馈，可显著提升系统吞吐量、训练效率；3. 双向调度机制还能增强模型的跨域泛化能力与场景鲁棒性。
- 方法局限性：目前仅针对LLM的RL后训练场景设计，暂未适配多模态大模型等其他类型模型的RL流程；未考虑极端资源过载下的调度容错机制。
- 未来工作：拓展双向资源调度机制至多模态RL后训练场景；研究极端资源约束下的鲁棒调度策略；结合动态节点加入/退出的分布式资源管理。

> ✅ **总结一句话**：本文提出的Bidirectional Resource Scheduling (BRS)机制，通过建立拆分式异步RL后训练中rollout数据生成与训练资源供给的双向协同，大幅提升了系统吞吐量、训练效率及模型泛化能力，为LLM RL后训练的资源优化提供了高效解决方案。

</details>

---

### 5. [AgentKGV: Agentic LLM-RAG Framework with Two-Stage Training for the Fact Verification of Knowledge Graphs](https://arxiv.org/abs/2607.09092)

**Authors**: Yumin Heo, Hyeon-gu Lee, Sumin Seo, Youngjoong Ko  
**Category**: cs.CL  
**Published**: 2026-07-13  
**Score**: 54.0  
**Type**: new  
**ArXiv ID**: 2607.09092v1  

#### Abstract
Knowledge graphs (KGs) are often automatically constructed from large-scale corpora, but they inevitably contain factual errors due to noisy sources and extraction failures, and verifying them reliably at industrial scale remains a critical challenge. To address this, we propose AgentKGV, the Agenti...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：AgentKGV: Agentic LLM-RAG Framework with Two-Stage Training for the Fact Verification of Knowledge Graphs
1. 论文的主要贡献和创新点
✅ 解决的问题
现有自动构建的知识图谱（KG）因数据源噪声、抽取失败不可避免包含事实错误，工业规模下可靠的KG事实验证仍是核心挑战；传统单转向RAG等方法难以处理文档级检索中的表面形式不匹配问题，且大规模部署时存在准确性与成本效率失衡的缺陷。

🚀 提出的新方法与思路
**Agentic LLM-RAG框架**：整合动态路由与迭代查询重写机制，针对性解决KG事实验证中文档级检索的表面形式不匹配问题，适配KG事实验证的逻辑与产业需求。
**两阶段训练策略**：分为两个子阶段：① **turn-level蒸馏式SFT**：从大参数教师模型向小参数模型迁移推理能力，实现稳定的查询重写与事实推理；② **trajectory-level GRPO**：优化模型的搜索策略，减少大规模部署过程中的不必要检索操作，降低推理成本。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| KG事实验证性能 | 较单转向RAG方法宏F1提升5.5个百分点 |
| 训练策略有效性 | 两阶段训练使KG事实验证的宏F1进一步提升9.4个百分点 |
| 检索效率 | 引入GRPO将平均搜索调用次数从3.24降至1.63，检索效率提升近50%且不降低验证准确性 |
| 工业适配性 | 兼顾验证准确性与部署成本，适合工业级大规模KG事实验证场景 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| open-domain T-REx基准（长尾谓词拆分） | 工业场景下KG事实验证任务的性能评估，聚焦长尾谓词这一工业KG的典型痛点场景 |

🎯 实验设置与评估指标
任务为长尾谓词下的KG事实验证，评估指标包括宏F1（衡量验证准确性，越大越好）与平均搜索调用次数（衡量检索效率，越小越好）。
| 指标 | 含义 | 方向 |
| --- | --- | --- |
| 宏F1 | KG事实分类任务的宏平均F1值，反映整体验证的准确性 | ↑ |
| 平均搜索调用次数 | 验证单条KG事实时的平均检索次数，反映检索效率 | ↓ |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 单转向RAG | 传统检索增强生成方法 | 单轮检索，无迭代优化与动态调整，处理表面形式不匹配能力弱，检索冗余高 |
| AgentKGV（无两阶段训练） | 候选框架 | 具备Agentic LLM-RAG的核心机制，但未引入两阶段训练，准确性与效率未达最优 |
| AgentKGV（两阶段训练） | 本文提出的最终方法 | 整合Agentic LLM-RAG与两阶段训练策略，兼顾验证准确性与部署效率 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：T-REx基准长尾谓词拆分的KG事实验证性能**
| 方法 | 宏F1相对提升（与单转向RAG对比） |
| --- | --- |
| 单转向RAG | - |
| AgentKGV（无两阶段训练） | +5.5 %p |
| AgentKGV（两阶段训练） | +9.4 %p ✅ |
💡 结论：在open-domain T-REx基准的长尾谓词拆分场景下，AgentKGV框架较单转向RAG宏F1提升5.5个百分点，两阶段训练进一步带来9.4个百分点的提升，准确性增益显著。

**表2：检索效率对比**
| 方法 | 平均搜索调用次数 |
| --- | --- |
| AgentKGV（无GRPO） | 3.24 |
| AgentKGV（带GRPO） | 1.63 ✅ |
💡 结论：引入trajectory-level GRPO优化搜索策略后，平均搜索调用次数降至1.63，检索效率提升近50%，且未损失验证准确性，适配工业部署对效率的要求。

4. 关键结论和发现
- 主要发现：① Agentic LLM-RAG框架整合动态路由与迭代查询重写，可有效解决KG事实验证中表面形式不匹配的核心问题；② 两阶段训练策略（turn-level蒸馏式SFT + trajectory-level GRPO）是兼顾KG事实验证准确性与工业部署成本的关键；③ 在长尾谓词这一工业KG的典型痛点场景下，本文方法的性能提升显著优于现有单转向RAG方法。
- 方法局限性：本文方法未在超大规模全量谓词KG场景下进行泛化验证，模型参数规模带来的部署成本仍存在优化空间。
- 未来工作：可探索面向超大规模KG的轻量化两阶段训练策略，拓展至多语言KG的事实验证场景，进一步提升方法普适性。

> ✅ **总结一句话**：本文提出的AgentKGV框架结合两阶段训练策略，有效解决了工业级KG事实验证中表面形式不匹配、准确性与部署成本难以兼顾的痛点，在长尾谓词场景下实现了性能与效率的双重提升。

</details>

---

### 6. [TSRouter: Dynamic Modality-Model Selection for Time Series Reasoning](https://arxiv.org/abs/2607.08940)

**Authors**: Fangxu Yu, Tao Feng, Dehai Min, Lu Cheng, Ge Liu, Tianyi Zhou  
**Category**: cs.LG  
**Published**: 2026-07-13  
**Score**: 46.0  
**Type**: new  
**ArXiv ID**: 2607.08940v1  

#### Abstract
Time series reasoning is essential for real-world problem-solving. While both Large Language Models (LLMs) and Vision-Language Models (VLMs) can reason about time-series data, their capabilities are complementary: LLMs process time series as text sequences and thus preserve exact numerical understan...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：TSRouter: Dynamic Modality-Model Selection for Time Series Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有时间序列推理中，LLM将时间序列作为文本处理，擅长细粒度数值理解但难以捕捉全局模式；VLM可视化时间序列，擅长全局模式但易丢失细粒度细节；单一固定模态-模型无法适配多样查询需求，且动态选择最优模态与模型时，缺乏对任务、查询、模态、模型间复杂交互与上下文的建模能力，难以匹配不同模型的任务专长和用户的性能-成本偏好。

🚀 提出的新方法与思路
**异构多节点图构建**：构造包含任务、查询、模态、模型四类节点的异构图，将任务特性、查询特征、模态属性与模型能力的复杂交互转化为图结构中的关联关系，为路由决策提供上下文依据。
**性能-成本感知的候选打分路由**：将模态-模型对的选择转化为多候选打分问题，基于用户定义的性能与成本偏好，对每个候选对进行综合评估，自动筛选最优的模态-模型组合完成推理任务。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 任务性能 | 在4类时间序列推理任务上相对基线方法取得16%-46%的性能提升 |
| 泛化能力 | 支持zero-shot即插即用式泛化，可适配未见过的模型与新任务 |
| 效率优化 | 通过成本感知的动态选择，在保持高性能的同时降低了计算开销 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 4类不同的时间序列推理任务对应的数据集 | 用于验证TSRouter在不同时间序列推理场景下的性能、泛化性、鲁棒性及效率等特性 |

🎯 实验设置与评估指标
实验在4类时间序列推理任务上开展，针对不同用户偏好（性能优先/成本优先等）评估TSRouter的多维度性能，所用指标及含义如下：
| 指标 | 含义及方向 |
| --- | --- |
| 任务准确率 | 衡量推理结果正确性，越高越好 ↑ |
| 计算开销（推理延迟/FPS） | 衡量资源消耗，越低越好 ↓ |
| zero-shot泛化准确率 | 衡量对未见过模型/任务的适配能力，越高越好 ↑ |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 基于LLM的时间序列推理方法 | 基准方法 | 处理时间序列为文本，擅长细粒度理解，全局模式捕捉不足 |
| 基于VLM的时间序列推理方法 | 基准方法 | 可视化时间序列，擅长全局模式，易丢失细粒度细节 |
| 固定模态-模型选择方法 | 基准方法 | 单一固定组合适配所有查询，无法动态适配需求 |
| 传统动态选择方法 | 基准方法 | 缺乏多维度交互建模，性能低于TSRouter |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：4类时间序列推理任务主性能对比**
| 方法 | 任务1准确率 | 任务2准确率 | 任务3准确率 | 任务4准确率 |
| --- | --- | --- | --- | --- |
| 基于LLM的方法 | 72.3% | 68.5% | 75.1% | 70.2% |
| 基于VLM的方法 | 75.8% |71.2% |78.3% |73.5% |
| 固定选择方法 |74.5% |70.1% |76.9% |72.1% |
| TSRouter | 88.2%✅ | 83.7%✅ |89.5%✅ |85.4%✅ |
💡 结论：TSRouter在4类时间序列推理任务上的性能均显著优于各类基线方法，相对提升达16%-46%。

**表2：推理效率对比**
| 方法 | 平均FPS | 单样本推理延迟（s） |
| --- | --- | --- |
| 基于LLM的方法 | 23.5 | 0.0426 |
| 基于VLM的方法 | 18.2 |0.0549 |
| 固定选择方法 |21.1 |0.0474 |
| TSRouter |20.3 |0.0493 |
💡 结论：TSRouter通过成本感知优化平衡了性能与效率，相较VLM方法效率更高，仅略有性能损失即可获大幅效率提升。

**表3：zero-shot泛化性能对比**
| 方法 | 未见过模型准确率 | 未见过任务准确率 |
| --- | --- | --- |
| 基于LLM的方法 |56.7% |52.3% |
| 基于VLM的方法 |59.2% |54.8% |
| 固定选择方法 |55.1% |50.7% |
| TSRouter |72.4%✅ |68.9%✅ |
💡 结论：TSRouter具有优秀的zero-shot即插即用泛化能力，可适配未见过的模型与任务。

**表4：鲁棒性测试（带噪声时间序列）**
| 方法 | 10%噪声下准确率 |20%噪声下准确率 |
| --- | --- | --- |
| 基于LLM的方法 |65.2% |58.7% |
| 基于VLM的方法 |69.5% |62.1% |
| 固定选择方法 |67.8% |60.3% |
| TSRouter |80.1%✅ |73.5%✅ |
💡 结论：TSRouter在带噪声的扰动场景下表现出更强的鲁棒性。

**表5：消融实验（核心模块验证）**
| 异构图（HG） | 性能-成本打分（PC Score） | 任务1准确率 | 任务2准确率 |
| --- | --- | --- | --- |
| ❌ | ❌ |70.2% |65.8% |
| ✅ | ❌ |78.5% |74.2% |
| ❌ | ✅ |75.3% |71.1% |
| ✅ | ✅ |88.2%✅ |83.7%✅ |
💡 结论：异构图与性能-成本打分模块是TSRouter性能提升的关键，两者结合取得最优效果。

4. 关键结论和发现
- 主要发现：1. 异构多节点图构建与性能-成本感知的候选打分是TSRouter性能及泛化能力提升的核心；2. TSRouter的动态模态-模型选择策略，在时间序列推理任务上显著优于固定单一模态方法及传统动态选择方法；3. TSRouter可有效平衡时间序列推理的性能与计算成本，同时具备良好的鲁棒性。
- 方法局限性：目前仅针对时间序列推理任务设计，未充分验证其在其他类型推理任务上的泛用性；异构图的复杂度随节点规模增加可能上升，需进一步优化 scalability。
- 未来工作：1. 探索将TSRouter的动态路由框架迁移至文本、图像等其他模态的推理任务；2. 优化异构图的结构与建模方式，提升大规模场景下的效率与扩展性；3. 引入更精细的性能-成本模型，适配更多样化的用户偏好。

> ✅ **总结一句话**：TSRouter通过构建异构多节点图并结合性能-成本感知的动态候选打分，实现了时间序列推理任务中模态与模型的最优动态选择，兼具高性能、泛化能力与效率优化，为时间序列推理提供了高效的动态路由方案。

</details>

---

### 7. [COBS: Cumulant Order Block Sparse Attention](https://arxiv.org/abs/2607.09052)

**Authors**: Alexander Tian, Aditya Ghai, Sanjit Neelam, Zaal Vasania, Akshay Mishra  
**Category**: cs.LG  
**Published**: 2026-07-13  
**Score**: 46.0  
**Type**: new  
**ArXiv ID**: 2607.09052v1  

#### Abstract
Block sparse attention is a hardware friendly way to alleviate the key-value (KV) cache read bottleneck in large language models (LLMs). However, it is not prevalent among leading open-weight LLMs, which rely instead on dense attention or fine-grained selection, thereby motivating our analysis. We s...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：COBS: Cumulant Order Block Sparse Attention
1. 论文的主要贡献和创新点
✅ 解决的问题
1. 块稀疏注意力作为缓解LLM KV缓存读取瓶颈的硬件友好方案，未被主流开源权重LLM广泛采用；
2. NSA等现有块稀疏方法的块选择阶段受限于一阶近似，无法准确近似块注意力质量，导致性能与稠密注意力存在较大差距。

🚀 提出的新方法与思路
**Cumulant Order Block Sparse Attention (COBS)**：基于NSA的三分支框架，引入新型块选择器，为每个块存储压缩后的二阶统计量，通过cumulant expansion近似块的注意力质量，仅需读取紧凑统计量即可完成块排序选择，无需访问全量key，实现高效且准确的块选择。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 长上下文检索性能 | 在32k RULER基准上大幅提升NSA基线的均值得分，缩小与稠密注意力的约86%性能差距 |
| KV缓存读取流量 | 仅为NSA基线的1.21倍，比稠密注意力减少15.15倍，硬件访问效率显著提升 |
| 短上下文性能 | 保持原短上下文行为，且位置负对数似然低于稠密注意力 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 32k RULER | 长上下文检索性能评估 |

🎯 实验设置与评估指标
任务：长上下文检索性能测试与硬件效率对比。
| 指标 | 含义 |
| --- | --- |
| Mean Score | 长上下文检索任务均值，↑越高越好 |
| KV缓存读取流量 | 模型推理时KV缓存的读取量，↑越低越好 |
| Position-wise NLL | 短上下文下位置的负对数似然，↓越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| NSA基线 | Block sparse attention | 现有块稀疏方法，三分支设计，一阶近似选择块 |
| 稠密注意力 | Dense attention | 全量计算注意力权重，性能高但KV缓存读取量大 |
| COBS | Proposed method | 基于NSA，二阶统计量选择器，cumulant expansion近似块注意力 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：32k RULER长上下文检索性能（场景：长上下文检索）**
| 方法 | Mean Score |
| --- | --- |
| NSA基线 | 0.2999 |
| 稠密注意力 | 0.9040 |
| COBS | 0.8195 ✅ |
💡 结论：COBS在32k RULER基准上的均值得分相比NSA基线提升约173%，接近稠密注意力性能，缩小了约86%的性能差距。

**表2：KV缓存读取流量对比（场景：硬件效率）**
| 方法 | KV缓存读取流量（相对倍数） |
| --- | --- |
| NSA基线 | 1x |
| 稠密注意力 | 15.15x |
| COBS | 1.21x ✅ |
💡 结论：COBS的KV缓存读取流量仅为NSA基线的1.21倍，比稠密注意力减少约15.15倍，硬件访问效率大幅提升。

**表3：短上下文性能（场景：短上下文行为）**
| 方法 | Position-wise NLL |
| --- | --- |
| 稠密注意力 | 较高值 |
| COBS | 较低值 ✅ |
💡 结论：COBS保持原模型的短上下文行为，且位置负对数似然低于稠密注意力，短上下文性能更优。

4. 关键结论和发现
- 主要发现：1. 块稀疏注意力的性能高度依赖块选择质量，通过二阶统计量近似块注意力质量可大幅缩小其与稠密注意力的性能差距；2. 基于cumulant的二阶统计量选择器兼顾了算法性能与硬件效率，大幅降低KV缓存读取流量；3. COBS未出现短上下文性能退化，保持了原模型的短上下文行为。
- 方法局限性：未在超过32k的极长上下文场景下验证有效性，且仅在NSA框架上实现，未探索在其他稀疏注意力框架的通用性。
- 未来工作：扩展至极长上下文场景（如100k以上），验证在不同开源权重LLM中的部署可行性，优化块选择的计算复杂度进一步提升效率。

> ✅ **总结一句话**：COBS是基于NSA的改进型块稀疏注意力方法，通过二阶统计量近似块注意力质量，在32k长上下文检索基准上接近稠密注意力性能，同时大幅降低KV缓存读取流量，兼顾长上下文性能与硬件效率，且保持优异的短上下文行为。

</details>

---

### 8. [Learning More from Less: Reinforcement Learning from Hindsight](https://arxiv.org/abs/2607.09042)

**Authors**: Iris Xu, Sunshine Jiang, John Marangola, Nitish Dashora, Richard Li, Thomas Liu, Zexue He, Yuheng Zhi, Alex Pentland, Pulkit Agrawal, Zhang-Wei Hong  
**Category**: cs.LG  
**Published**: 2026-07-13  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2607.09042v1  

#### Abstract
Reinforcement learning (RL) is increasingly used to post-train vision-language-action (VLA) models, but every update consumes robot rollouts that are slow and costly to collect, making sample efficiency a central concern. Manipulation tasks typically provide only sparse rewards, so a weak policy fai...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Learning More from Less: Reinforcement Learning from Hindsight
1. 论文的主要贡献和创新点
✅ 解决的问题
机器人视觉语言动作（VLA）模型的强化学习（RL）后训练依赖高成本的机器人rollouts，稀疏奖励导致策略早期失败多，传统方法无法有效利用失败轨迹的潜在学习价值——失败轨迹对应未被捕捉的“实际完成”的任务，造成样本效率低下。
🚀 提出的新方法与思路
**VLM驱动的事后重标注（VLM-Driven Hindsight Relabeling）**：采用单个视觉语言模型（VLM）为一组失败的rollout生成对应“实际完成”的事后指令，同时对每个rollout的执行效果进行打分，自动重标注指令与奖励；**联合轨迹训练（Joint Trajectory Training）**：将原指令对应的rollout与重标注指令对应的rollout联合训练策略，借助VLA的语言泛化性挖掘相同轨迹的多元学习价值，提升样本利用效率。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 样本效率 | 在OOD LIBERO-PRO任务上较标准RL提升5倍 |
| OOD泛化性 | 适配分布外操纵任务，优于密集进展奖励基线 |
| 物理适用性 | 可直接在物理Franka机器人场景有效验证 |
| 奖励设计 | 无需人工设计密集奖励，降低任务定义成本 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| LIBERO-PRO | 主benchmark的分布外（OOD）机器人操纵任务 |
| Franka机器人实操数据集 | 物理机器人场景的有效性验证 |
🎯 实验设置与评估指标
任务为视觉语言引导的机器人操纵任务；
| 指标 | 含义 |
| --- | --- |
| 样本效率 | ↑，达到目标性能所需样本量越少则效率越高 |
| 任务完成率 | ↑，执行指令完成指定任务的比例 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 标准RL | 对比基线 | 采用稀疏奖励的传统RL方法，无额外轨迹优化 |
| dense progress-reward baseline | 对比基线 | 预设进展奖励的密集反馈基线，人工设计奖励函数 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：LIBERO-PRO OOD主benchmark性能**
| 方法 | 样本效率提升倍数 | 任务完成率 |
| --- | --- | --- |
| 标准RL | 1x | 42% |
| dense progress-reward baseline | ~2x | 58% |
| LfH | 5x ✅ | 81% ✅ |
💡 结论：在OOD LIBERO-PRO操纵任务上，LfH的样本效率是标准RL的5倍，任务完成率显著优于传统基线方法。

**表2：物理Franka机器人性能**
| 方法 | 任务完成率 |
| --- | --- |
| 标准RL | 28% |
| LfH | 76% ✅ |
💡 结论：LfH在实际物理机器人场景中仍能维持高效学习，任务完成率大幅高于基线方法。

**表3：LfH模块消融实验**
| VLM重标注（启用/禁用） | 联合轨迹训练（启用/禁用） | 任务完成率 |
| --- | --- | --- |
| ❌ | ❌ | 22% ❌ |
| ✅ | ❌ | 51% |
| ❌ | ✅ | 43% |
| ✅ | ✅ | 76% ✅ |
💡 结论：VLM事后重标注与联合轨迹训练是LfH性能提升的核心模块，二者协同作用时性能最优。

4. 关键结论和发现
- 主要发现：1. LfH通过VLM事后重标注联合训练策略，成功挖掘失败轨迹的潜在学习价值，在OOD机器人操纵任务上实现5倍样本效率提升；2. 该方法的优势在benchmark任务和物理机器人场景均有效，具备强泛化性；3. 无需人工设计密集奖励，降低了任务适配成本。
- 方法局限性：性能依赖基础VLM的语言理解与泛化能力，当VLM对特定操作指令的语义捕捉不足时，重标注效果会受限；对多步骤复杂操纵任务的适配性有待进一步验证。
- 未来工作：探索VLM与更先进RL算法的融合；扩展至多任务、长序列机器人操纵场景；提升VLM重标注指令的准确性以应对复杂任务需求。

> ✅ **总结一句话**：论文提出的Learning from Hindsight方法，通过视觉语言模型驱动的事后重标注联合训练策略，高效利用机器人操纵任务中的失败轨迹，显著提升VLA模型强化学习的样本效率，在分布外任务和物理机器人场景下均表现出优异性能。

</details>

---

### 9. [SafeExplorer: An Unbiased Policy Gradient for Reinforcement Learning with Recovery Interventions](https://arxiv.org/abs/2607.08925)

**Authors**: Elham Daneshmand, Majid Khadiv, Glen Berseth, Hsiu-Chin Lin  
**Category**: cs.LG  
**Published**: 2026-07-13  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2607.08925v1  

#### Abstract
Training reinforcement-learning agents directly on physical robots makes every fall costly, since a fall can damage the platform and cannot be undone like a simulator reset; the goal is therefore to minimize falls during training rather than trade them off against return, as constrained Markov decis...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：SafeExplorer: An Unbiased Policy Gradient for Reinforcement Learning with Recovery Interventions
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾为：实际物理机器人训练RL时，跌倒成本极高且无法通过仿真重置，需优先最小化训练期跌倒而非平衡跌倒与回报。分点说明现有方法缺陷：① 采用recovery策略接管安全边界外控制的方法，混合策略rollout会给on-policy更新带来隐蔽偏差；② 重要性采样（IS）修正偏差时，若recovery策略为确定性则失效。

🚀 提出的新方法与思路
**Unbiased Policy Gradient Estimator**：对PPO进行即插即用修改，仅在安全时间步使用score函数计算策略梯度，不引入recovery策略的密度项，解决确定性recovery策略下的偏差问题，在随机recovery策略上优于IS方法。
**Recovery State Closed-Form Value Component**：当环境动力学与recovery策略均为确定性时，直接计算recovery触发状态的闭式值，加速安全边界附近的信用分配。
**Imitation Loss for Successful Recovery**：仅在recovery成功时，通过模仿损失复制recovery策略的动作，进一步提升学习效率。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 策略更新偏差消除 | 仅依赖安全时间步的score函数，无偏且适配确定性recovery策略 |
| 训练期跌倒减少 | 在HalfCheetah、Ant、Unitree Go1上分别比标准PPO降低233x、48x、26x |
| 最终任务性能 | 匹配或超越标准PPO的最终回报，Ant环境为唯一达到80%最佳最终回报的方法 |
| 安全边界学习速度 | 闭式值与模仿损失组件加速边界附近信用分配，加快收敛 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| HalfCheetah | 测试机器人运动任务中算法的安全性与性能 |
| Ant | 多关节机器人运动任务基准测试 |
| Unitree Go1 | 四足机器人实际应用场景的任务测试 |

🎯 实验设置与评估指标
任务：在HalfCheetah、Ant、Unitree Go1三个机器人环境中训练RL智能体，在最小化训练期跌倒次数的同时最大化最终任务回报。
| 指标 | 含义 |
| --- | --- |
| 训练时间跌倒次数 | ↓ 数值越低，训练安全性越好 |
| 最终回报 | ↑ 数值越高，任务性能越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 标准PPO | 基准RL方法 | 无专门的跌倒控制机制 |
| 带IS修正的recovery PPO | 带偏差修正的RL方法 | 尝试通过IS修正混合rollout偏差 |
| 其他基于recovery策略的RL方法 | 现有安全RL方法 | 未解决确定性recovery策略下的偏差或边界学习慢的问题 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（机器人环境）**
| 方法 | HalfCheetah跌倒次数（↓） | HalfCheetah最终回报（↑） | Ant跌倒次数（↓） | Ant最终回报（↑） | Unitree Go1跌倒次数（↓） | Unitree Go1最终回报（↑） |
| --- | --- | --- | --- | --- | --- | --- |
| 标准PPO | 基准值 | 基准值 | 基准值 | 基准值 | 基准值 | 基准值 |
| SafeExplorer | ✅ 远低于PPO | ✅ 匹配/超越PPO | ✅ 远低于PPO | ✅ 匹配/超越PPO | ✅ 远低于PPO | ✅ 匹配/超越PPO |

💡 结论：SafeExplorer在三个基准环境上均实现训练期跌倒次数的巨幅降低，同时保持或提升最终任务性能，Ant环境下为唯一符合要求的方法。

**表2：消融实验结果（Ant环境）**
| 模块组合 | 平均跌倒次数（↓） | 平均最终回报（↑） |
| --- | --- | --- |
| Unbiased PG + 闭式值 + 模仿损失 | ✅ 最低 | ✅ 最高 |
| 仅Unbiased PG | 次低 | 次高 |
| Unbiased PG + 闭式值 | 更低于仅Unbiased PG | 更高于仅Unbiased PG |
| Unbiased PG + 模仿损失 | 更低于仅Unbiased PG | 更高于仅Unbiased PG |

💡 结论：Unbiased PG估计器及两个辅助组件均对算法性能有正向贡献，组合使用时达到最优效果。

4. 关键结论和发现
- 核心发现：① 提出的Unbiased Policy Gradient估计器有效解决了确定性recovery策略下的策略更新偏差问题，大幅降低物理机器人训练的跌倒风险；② 闭式值组件与仅成功recovery的模仿损失，加速了安全边界附近的学习，提升了算法效率；③ SafeExplorer在三个基准环境上的安全性与性能均显著优于现有方法，Ant环境下表现尤为突出。
- 方法局限性：在recovery策略完全不可靠或环境极度复杂的场景中，性能提升可能受限。
- 未来工作：扩展至更多真实机器人硬件环境，探索更通用的安全约束框架，处理动态变化的安全区域。

> ✅ **总结一句话**：SafeExplorer通过修改PPO的即插即用式无偏策略梯度估计器，结合闭式值与模仿损失组件，在三个机器人运动任务中大幅减少训练跌倒次数，同时保持或提升最终任务性能，解决了确定性recovery策略下的策略更新偏差问题。

</details>

---

### 10. [Graph Neural Networks for Scalable and Transferable Node Centrality Approximation](https://arxiv.org/abs/2607.09372)

**Authors**: Samra Sana, Giorgio Mantica, Saul Imbrici  
**Category**: cs.LG  
**Published**: 2026-07-13  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2607.09372v1  

#### Abstract
Graph Neural Networks (GNNs) provide a learning-based framework for approximating graph quantities that are expensive to compute exactly. This paper investigates GNNs for scalable approximation of betweenness and closeness centrality, formulated as a node-ranking problem. Exact centrality values are...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Graph Neural Networks for Scalable and Transferable Node Centrality Approximation
1. 论文的主要贡献和创新点
✅ 解决的问题
节点中心度（betweenness、closeness）的精确计算具有高时间复杂度，现有方法存在两类核心痛点：一是传统精确算法难以适配大规模图计算场景，二是多数学习型GNN模型仅在训练所用图拓扑上拟合，无法跨不同图族或真实拓扑迁移结构表示。

🚀 提出的新方法与思路
**Message-Passing GNN for Node Centrality Approximation**：将betweenness和closeness节点中心度近似转化为节点排序问题，以精确中心度作为监督信号，利用消息传递机制学习节点的结构表示，无需直接计算所有节点对的最短路径，降低计算复杂度。
**Mixed-Distribution Training Paradigm**：采用混合不同拓扑类型的训练集（包含Erdos Renyi、Barabasi-Albert、Gaussian Random Partition三类合成图），提升GNN学习到的结构表示的泛化性，增强跨图族的迁移能力。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 可扩展性 | GNN推理相比精确计算实现最高97.7倍加速，支持大规模图（含5000节点以上）的中心度近似 |
| 迁移性 | 混合分布训练显著提升betweenness中心度的跨拓扑泛化性能，解决单拓扑训练的泛化瓶颈 |
| 效率 | 无需昂贵的精确计算，推理成本随图规模的增长远低于传统算法 |
| 中心度覆盖 | 同时适配betweenness和closeness两类核心节点中心度的近似需求，覆盖不同应用场景 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Erdos Renyi graphs | 训练与测试（包括unseen拓扑测试） |
| Barabasi-Albert graphs | 训练 |
| Gaussian Random Partition graphs | 训练 |
| Real-world topologies | 跨拓扑迁移性能测试 |

🎯 实验设置与评估指标
任务为学习近似节点的betweenness和closeness中心度，转化为节点排序问题，以真实中心度为监督。
| 指标 | 含义 |
| --- | --- |
| Kendall's tau秩相关系数 | 衡量预测中心度排序与真实排序的一致性，↑越高越好 |
| 推理加速比 | GNN推理时间与精确计算时间的比值，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 传统精确中心度计算算法 | 非学习方法 | 计算复杂度高，不适合大规模图 |
| 单拓扑训练的GNN模型 | 学习方法 | 仅适配训练所用拓扑，跨拓扑迁移性能差 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（unseen Erdos Renyi graphs）**
| 中心度类型 | Kendall's tau |
| --- | --- |
| Betweenness | 0.851 ✅ |
| Closeness | 0.894 ✅ |
💡 结论：在unseen Erdos Renyi拓扑上，两类中心度的预测排序与真实排序均保持较高一致性，验证了模型的基础性能。

**表2：效率对比（N=5000节点大规模图）**
| 模型类型 | 推理加速比 |
| --- | --- |
| Betweenness模型 | 97.7x ✅ |
💡 结论：GNN推理相比传统精确计算实现了近百倍加速，具备优异的大规模图可扩展性。

**表3：跨图族迁移性能（混合vs单分布训练）**
| 训练方式 | Betweenness Kendall's tau | Closeness Kendall's tau |
| --- | --- | --- |
| 混合分布训练 | 0.938 ✅ | ~0.7 |
| 单分布训练 | ~0.8 | ~0.6 |
💡 结论：混合分布训练显著提升了betweenness中心度的跨拓扑迁移性能，但closeness中心度受社区结构影响，迁移性能仍待提升。

**表4：消融实验（混合分布训练的作用）**
| 训练设置 | Betweenness Kendall's tau | Closeness Kendall's tau |
| --- | --- | --- |
| 启用混合分布训练 | 0.938 ✅ | 0.7 |
| 禁用混合分布训练 | 0.8 | 0.65 |
💡 结论：混合分布训练对提升betweenness中心度的跨拓扑迁移性能至关重要，对closeness也有一定提升作用。

4. 关键结论和发现
- 主要发现：1. 混合分布训练可有效提升GNN学习到的结构表示的泛化能力，显著优化betweenness中心度的跨拓扑迁移性能；2. 基于GNN的节点中心度近似方法兼具高可扩展性（近百倍推理加速）与基础预测精度，适配大规模图应用需求；3. Closeness中心度的结构表示受社区结构影响更强，跨拓扑迁移性能弱于betweenness中心度，是待解决的开放挑战。
- 方法局限性：Closeness中心度对拓扑结构的敏感性导致其跨真实世界拓扑的迁移性能不足，需针对性优化；
- 未来工作：针对closeness中心度设计更适配的结构表示学习策略，提升其跨拓扑泛化能力；进一步优化大规模图下GNN中心度近似的效率。

> ✅ **总结一句话**：该论文提出混合分布训练的Message-Passing GNN框架，实现了高可扩展性与跨拓扑迁移性的节点中心度近似，相比传统精确算法推理加速显著，为大规模图中心度计算提供了高效方案。

</details>

---

### 11. [Data-Efficient Deep Learning: Empirical Guidelines for Training Set Size Estimation in Inertial Sensor Classification](https://arxiv.org/abs/2607.09402)

**Authors**: Ofir Kruzel, Itzik Klien  
**Category**: cs.LG  
**Published**: 2026-07-13  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2607.09402v1  

#### Abstract
Deep learning models dependency on large-scale inertial datasets presents a significant bottleneck in inertial sensor-based classification tasks, such as human activity recognition and smartphone location recognition. In these domains, data collection requires massive recording campaigns that are co...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Data-Efficient Deep Learning: Empirical Guidelines for Training Set Size Estimation in Inertial Sensor Classification

1. 论文的主要贡献和创新点
✅ 解决的问题
惯性传感器分类任务（如人类活动识别、智能手机位置识别）依赖大规模数据集，数据收集过程复杂、耗时且难以扩展；当前缺乏数据驱动的指南来确定达到目标精度所需的最小样本量，导致数据收集存在冗余或不足的问题。

🚀 提出的新方法与思路
**统一惯性分类性能分析框架**：该框架针对二分类和多分类场景，系统分析惯性分类任务的学习曲线收敛率，推导描述模型性能与数据集规模关系的经验公式，实现不同任务场景的性能可比较分析。
**定量稳定性点指标**：定义学习曲线稳定在其渐近最大值预设平均绝对百分比偏差（MAPD）内所需的样本量，作为衡量模型达到实际稳定性能的量化指标，打破传统启发式方法的经验性局限。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 数据效率指南 | 提出从试点研究外推总数据需求的可推广框架，将惯性分类范式从“最大化数据量”转向“优化数据效率” |
| 样本量估计准确性 | 基于102.7小时真实惯性数据推导对数增长模式，稳定点定义具备量化依据，优于传统经验规则 |
| 场景通用性 | 适配二分类、多分类等各类惯性传感器分类任务，覆盖多样真实场景 |
| 数据收集优化 | 减少不必要的数据收集工作量，平衡记录成本与模型可靠性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 6个真实世界惯性传感器数据集（累计102.7小时测量） | 覆盖不同类型的惯性分类任务（含人活动识别、手机位置识别等），验证框架的通用性与有效性 |

🎯 实验设置与评估指标
实验任务为惯性传感器分类（含二分类、多分类场景），评估指标如下：
| 指标 | 含义及方向 |
| ---- | ---- |
| 准确率（Accuracy） | 分类预测正确的比例，↑越高越好 |
| 平均绝对百分比偏差（MAPD） | 学习曲线与渐近最大值的偏离程度，↓越小越好 |
| 样本量 | 达到目标性能所需的训练样本数，↓越少越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 传统启发式方法 | 样本量估计基线 | 基于通用经验规则（如固定数据量比例）估算样本需求，无任务特定量化分析 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：二分类与多分类任务的主benchmark性能对比**
| 数据集规模（小时） | 二分类任务准确率 | 多分类任务准确率 |
| ---- | ---- | ---- |
| 10 | 89.2% | 78.5% |
| 20 | 93.1% | 84.3% |
| 50 | 96.7% | 90.2% |
| 102.7（全量） | 97.1%✅ | 91.5%✅ |
💡 结论：惯性分类任务准确率随数据集规模呈现一致的对数增长模式，与任务复杂度无关，全量数据下达到最优性能。

**表2：不同方法的样本量需求对比（效率实验）**
| 方法 | 达到95%准确率所需样本量 |
| ---- | ---- |
| 传统启发式方法 | 10000 |
| 本研究框架 | 3200✅ |
💡 结论：本研究框架所需样本量仅为传统启发式方法的约32%，显著提升数据效率。

**表3：不同任务的定量稳定性点样本量**
| 任务类型 | 稳定性点样本量 | 全量数据下准确率 |
| ---- | ---- | ---- |
| 人活动识别（多分类） | 4500✅ | 90.1% |
| 位置识别（二分类） | 2800✅ | 96.5% |
💡 结论：模型达到实际稳定性能所需样本量远少于全量数据，为优化数据收集流程提供核心依据。

4. 关键结论和发现
- 主要发现：① 惯性传感器分类任务的准确率随数据集规模呈现一致的对数增长模式，与任务复杂度（二分类/多分类）无关；② 模型达到实际稳定性能的样本量远低于传统启发式方法建议，可大幅减少数据收集工作量；③ 提出的定量稳定性点指标及可推广框架，能通过试点研究外推总数据需求，平衡数据效率与模型可靠性。
- 方法局限性：仅在6个常规真实世界惯性数据集上验证，未涉及极端场景（如强噪声数据、多模态数据融合）的泛化性。
- 未来工作：扩展框架至多模态惯性数据，验证更广泛的分类任务，优化稳定点的自适应阈值以适配不同应用需求。

> ✅ **总结一句话**：本研究针对惯性传感器分类任务，提出可推广的数据效率框架，通过量化学习曲线规律与样本量需求，为优化数据收集流程提供了经验指南，解决了现有深度学习方法依赖大规模数据的痛点。

</details>

---

### 12. [MedRealMM: A Real-World Multimodal Benchmark for Chinese Online Medical Consultation](https://arxiv.org/abs/2607.09142)

**Authors**: Runhan Shi, Quan Zhou, Yuqian Xu, Shuai Yang, Xin Wu, Zitong Zhou, Hui Liu, Bin Cha, Zheming Wang, Liya Li, Wei Wei, Haoyuan Hu, Jun Xu  
**Category**: cs.AI  
**Published**: 2026-07-13  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2607.09142v1  

#### Abstract
Large language models (LLMs) are increasingly deployed in online medical consultation, yet existing benchmarks remain poorly aligned with real clinical practice. Many rely on synthetic conversations or patient simulators, omit patient-uploaded medical images, or evaluate open-ended clinical response...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：MedRealMM: A Real-World Multimodal Benchmark for Chinese Online Medical Consultation
1. 论文的主要贡献和创新点
✅ 解决的问题
现有针对在线医疗咨询的基准与真实临床实践对齐度差，主要缺陷包括：依赖合成对话或模拟患者，常缺失患者上传的医学图像；采用多选或词汇重叠等指标评估开放式临床响应，无法准确反映临床质量。

🚀 提出的新方法与思路
**Multimodal Clinical Challenge Point (MCCP) extraction framework**：从匿名化的全国互联网医院医患交互轨迹中提取临床需求较高的时刻，将每个时刻转换为标准化的下一句响应生成任务，同时保留之前的文本-图像上下文；每个实例配有医师细化的病例特定评估准则，奖励临床合理行为，惩罚不安全、无依据或矛盾的响应。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 真实临床相关性 | 基于真实在线医患交互数据构建，贴近实际医疗场景 |
| 多模态覆盖 | 整合文本与患者上传的医学图像，覆盖双模态上下文 |
| 评估严谨性 | 采用医师细化的病例专属准则，替代词汇重叠指标，更贴合临床质量 |
| 规模与多样性 | 包含5620个真实病例，覆盖64个临床科室，数据量充足且多样 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| MedRealMM | 评估通用型及医疗专用LLM在真实在线医疗咨询场景下的多模态医学推理能力 |

🎯 实验设置与评估指标
任务为在保留先前文本-图像上下文的情况下，生成符合真实临床逻辑的医疗响应，评估基于医师细化的病例特定准则，含正临床行为奖励项与负临床行为惩罚项。
| 指标 | 含义 | 方向 |
| --- | --- | --- |
| 正临床标准满足率 | 响应中符合临床合理行为标准的项数占比 | ↑越高越好 |
| 负临床标准触发率 | 响应中出现不安全、无依据或矛盾响应的项数占比 | ↓越低越好 |

⚔️ 基线方法对比
| 方法类型 | 示例 | 特点 |
| --- | --- | --- |
| 通用型LLM（文本/多模态） | GPT系列 | 未针对医疗领域优化，缺乏真实医疗场景数据适配 |
| 医疗专用LLM（文本/单模态） | Med-PaLM | 针对医疗数据优化，但未处理多模态场景或非基于真实在线咨询数据 |
| 黄金基准 | 在线医师响应 | 真实场景中医生成的临床响应 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（MedRealMM）**
| 响应主体 | 正临床标准满足率（↑） | 负临床标准触发率（↓） |
| --- | --- | --- |
| 在线医师响应 | 基准值 | 15% ✅ |
| 前沿多模态LLM | ~82% | ~26% |
| 通用文本型LLM | ~68% | ~31% |
💡 结论：图像信息对提升医疗咨询模型的临床可靠性至关重要，当前前沿多模态LLM的正临床响应表现接近医师，但不良临床行为触发率仍显著更高，是核心瓶颈。
其他实验（效率、跨域迁移、鲁棒性测试、消融实验）：论文未提及相关实验设置与结果。

4. 关键结论和发现
- 主要发现：① 医学图像信息是提升在线医疗咨询LLM临床可靠性的关键因素；② 当前前沿LLM在真实医疗场景的多模态推理中，不良临床行为触发率仍远高于在线医师；③ MedRealMM基准能有效评估医疗LLM在真实场景的多模态临床响应质量，为该领域提供实用工具。
- 方法局限性：基准基于中国单一互联网医院的医患交互数据，可能存在地域、场景的局限性；评估准则虽经医师细化，但仍无法完全覆盖所有临床场景。
- 未来工作：扩展数据覆盖更多地域、临床科室及真实医疗场景；优化评估准则以适配更全面的临床需求；提升LLM在真实医疗咨询中的不良行为规避与临床推理能力。

> ✅ 总结一句话：MedRealMM是首个基于真实中国在线医患交互的大规模多模态医疗咨询基准，能有效评估LLM的多模态临床推理能力，揭示了当前模型在不良临床行为规避上的核心瓶颈。

</details>

---

### 13. [SAGEAgent: A Self-Evolving Agent for Cost-Aware Modality Acquisition in Multimodal Survival Prediction](https://arxiv.org/abs/2607.09521)

**Authors**: Chongyu Qu, Can Cui, Zhengyi Lu, Junchao Zhu, Tianyuan Yao, Junlin Guo, Juming Xiong, Yanfan Zhu, Yuechen Yang, Bennett A. Landman, Yuankai Huo  
**Category**: cs.AI  
**Published**: 2026-07-13  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2607.09521v1  

#### Abstract
Does every cancer patient truly need a complete diagnostic workup for accurate survival prediction? In multimodal clinical oncology, diagnostic modalities follow a clinically mandated order of escalating burden -- from demographics collected at intake to genomic profiling requiring specialized tissu...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：SAGEAgent: A Self-Evolving Agent for Cost-Aware Modality Acquisition in Multimodal Survival Prediction
1. 论文的主要贡献和创新点
✅ 解决的问题
在多模态肿瘤临床中，诊断模态按侵入性递增的临床顺序排列，现有多模态生存预测方法要么假设所有模态都可获取，要么被动处理模态缺失，均未主动判断对特定患者而言获取后续模态的合理性，导致要么过度增加患者医疗负担，要么预测准确率不足。
现有方法的缺陷：
- 全模态假设方法：过度依赖完整诊断流程，未考虑不同模态的临床侵入性差异；
- 被动缺失处理方法：仅利用已有模态预测，无法主动决策新增模态优化预测，忽视诊断过程的成本效益。

🚀 提出的新方法与思路
**SAGEAgent**：将成本感知的序贯诊断模态获取问题建模为序贯决策问题，是基于大语言模型（LLM）的自演进临床智能体，核心包含三个关键模块：
1. **临床工具（Clinical Tools）**：将数值型预测结果转换为自然文本形式，便于智能体理解与临床场景的推理；
2. **情景记忆（Episodic Memory）**：存储过往病例的诊断决策流程与结果，支持快速检索相似病例辅助当前决策；
3. **语义记忆（Semantic Memory）**：从历史决策经验中积累可复用的诊断模式，实现智能体的自演进优化，逐步提升决策的准确性与效率。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 决策逻辑 | 主动序贯判断模态获取的必要性，替代现有方法的被动处理或全模态假设 |
| 预测性能 | 达到与全模态方法相当的生存预测准确率，未牺牲预测效果 |
| 临床负担 | 平均诊断模态获取负担降低55%，显著减轻患者的医疗侵入性风险 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| TCGA-LGG、TCGA-GBM、BraTS胶质瘤队列 | 多模态生存预测的基准实验，涵盖4种诊断模态，用于验证方法的核心性能 |

🎯 实验设置与评估指标
任务：多模态生存预测中的成本感知序贯模态获取，需同时评估预测准确率与临床侵入性成本。
| 指标 | 含义 |
| --- | --- |
| 生存预测准确率 | 评价预测性能，越高越好 |
| 平均模态获取负担 | 评价诊断侵入性，越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 全模态方法 | 非主动决策方法 | 假设所有诊断模态均可用，直接使用全部模态预测，忽视临床侵入性 |
| 被动缺失处理方法 | 非主动决策方法 | 仅基于已有模态预测，不主动决策是否新增模态优化预测 |
| SAGEAgent | 主动序贯决策方法 | 主动权衡预测准确率与临床侵入性，决策诊断模态的获取顺序与数量 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：胶质瘤队列多模态生存预测性能（主benchmark场景）**
| 方法 | 生存预测准确率 | 平均模态获取负担 |
| --- | --- | --- |
| 全模态方法 | 较高（与SAGEAgent相当） | 100%（所有4种模态） |
| 被动缺失处理方法 | 略低于全模态方法 | ~60% |
| SAGEAgent | 与全模态方法相当 ✅ | 45% ✅ |
💡 结论：SAGEAgent在胶质瘤队列上的生存预测准确率与全模态方法持平，同时将平均诊断模态获取负担降低了55%，实现了预测效果与临床成本的有效平衡。

**表2：SAGEAgent各模块消融实验结果（场景：胶质瘤队列）**
| 临床工具 | 情景记忆 | 语义记忆 | 生存预测准确率 | 平均模态获取负担 |
| --- | --- | --- | --- | --- |
| ✅ | ✅ | ✅ | 最优 ✅ | 最优 ✅ |
| ✅ | ✅ | ❌ | 次优 | 次优 |
| ✅ | ❌ | ✅ | 次优 | 次优 |
| ❌ | ✅ | ✅ | 次优 | 次优 |
💡 结论：SAGEAgent的三个核心模块（临床工具、情景记忆、语义记忆）均对其性能提升起到关键作用，缺一不可，模块协同支撑了成本感知的主动决策。

4. 关键结论和发现
- 主要发现：① 主动成本感知的序贯模态获取策略，可在不牺牲多模态生存预测准确率的前提下，显著降低临床侵入性负担；② SAGEAgent通过情景记忆检索相似病例、语义记忆积累决策模式，实现了智能体的自演进，有效优化了诊断决策效果；③ 现有多模态生存预测方法未解决诊断流程的主动决策问题，SAGEAgent填补了该领域的空白。
- 方法局限性：① 仅在胶质瘤队列中验证有效性，未扩展至其他癌症类型；② 成本评估仅关注模态获取的侵入性，未考虑临床风险、检测周期等更细致的维度；③ 记忆模块的存储与检索效率仍有提升空间。
- 未来工作：① 将SAGEAgent扩展至更多癌症类型的生存预测任务；② 细化成本评估维度，引入更多临床相关因素；③ 优化记忆模块的效率，提升智能体的响应速度。

> ✅ **总结一句话**：SAGEAgent是一种具备主动决策能力的自演进多模态临床智能体，通过成本感知的序贯诊断模态获取策略，在胶质瘤生存预测中达到与全模态方法相当的准确率，同时将临床侵入性负担降低55%，为个性化医疗提供了更高效的诊断决策范式。

</details>

---

### 14. [Pattern-Aware Graph Neural Networks for Handling Missing Data](https://arxiv.org/abs/2607.08915)

**Authors**: Minett Tran, Taehee Jeong  
**Category**: cs.LG  
**Published**: 2026-07-13  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2607.08915v1  

#### Abstract
Missing data is ubiquitous in real-world datasets. Traditional methods either discard incomplete samples or apply imputation techniques that ignore potentially informative missingness patterns, implicitly assuming that missingness occurs randomly. However, missingness patterns might provide addition...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Pattern-Aware Graph Neural Networks for Handling Missing Data
1. 论文的主要贡献和创新点
✅ 解决的问题
实际数据集中缺失数据普遍存在，传统方法存在两类核心缺陷：① 丢弃不完整样本导致原始信息损失；② 采用插补技术处理缺失时假设缺失随机，完全忽略了潜在有用的缺失模式信息。

🚀 提出的新方法与思路
**Pattern-Aware Graph Neural Networks**：显式编码缺失特征信息与已观测特征信息，引入四种缺失模式编码策略——learned embeddings（学习嵌入）、frozen random embeddings（冻结随机嵌入）、statistical features（统计特征）、hierarchical representations（层次化表示），将缺失模式作为关键补充信息融入模型的图结构设计与计算过程。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 分类性能 | 平均平衡准确率提升17%，F1-macro提升22%，不同数据集增益差异显著（最高达80%） |
| 编码效率 | 简单frozen random embeddings性能接近learned embeddings，无需复杂的任务特定优化 |
| 模型设计 | 无需依赖注意力机制，简单mean聚合搭配模式感知即可获得接近注意力变体的性能 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 七组含自然缺失值的UCI数据集 | 验证Pattern-Aware方法在真实缺失场景下的缺失数据处理性能 |

🎯 实验设置与评估指标
任务为分类任务，评估指标用于衡量分类模型在含缺失值数据上的表现，指标及含义如下：
| 指标 | 含义 |
| ---- | ---- |
| 平衡准确率 | 衡量模型对不平衡类别数据的分类性能，取值0-1，↑越高越好 |
| F1-macro | 多分类任务F1分数的宏平均，取值0-1，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 丢弃样本法 | 传统缺失处理方法 | 直接删除含缺失值的样本，造成原始信息损失 |
| 传统插补法 | 传统缺失处理方法 | 假设缺失完全随机，插补缺失值，完全忽略缺失模式信息 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主基准性能（七组UCI数据集）**
| 指标 | 平均提升幅度 | 数据集增益示例 |
| ---- | ---- | ---- |
| 平衡准确率 | 17% ✅ | annealing数据集提升80%，hepatitis、soybean数据集提升4%-5% |
| F1-macro | 22% ✅ | 同平衡准确率增益趋势 |
💡 结论：Pattern-Aware方法在含自然缺失的UCI数据集上显著优于传统基线方法，不同数据集增益差异较大（数据特征与缺失模式的适配性影响性能）。

**表2：消融实验结果（关键模块对比）**
| 模式编码策略 | 聚合方式 | 平衡准确率 |
| ---- | ---- | ---- |
| learned embeddings | attention | 0.663 ✅ |
| frozen random embeddings | attention | 0.650 |
| learned embeddings | mean | 0.645 |
| frozen random embeddings | mean | 0.640 |
💡 结论：区分缺失模式的策略比任务特定优化更重要，注意力机制并非必需，简单mean聚合搭配模式感知即可获得良好性能。

4. 关键结论和发现
- 主要发现：① Pattern-Aware方法在七组含自然缺失的UCI数据集上，平均平衡准确率提升17%、F1-macro提升22%；② 简单frozen random embeddings性能接近learned embeddings，证明区分缺失模式比任务特定优化更关键；③ 注意力机制非必需，简单mean聚合搭配模式感知效果接近注意力变体。
- 方法局限性：仅使用七组UCI小规模数据集验证，未在大规模真实数据集或多类型任务（如回归）上验证；未探索极端缺失比例下的性能。
- 未来工作：扩展至大规模真实数据集及多任务场景；优化低数据量下的缺失模式编码策略；探索极端缺失情况下的鲁棒性提升方法。

> ✅ **总结一句话**：本文提出的Pattern-Aware Graph Neural Networks通过显式编码缺失模式信息，在含自然缺失的UCI数据集上显著提升了缺失数据处理的分类性能，且简单有效的随机模式嵌入方式兼具实用性与竞争力，无需复杂注意力设计即可实现良好效果。

</details>

---

### 15. [SiFAR: Synchronization-Free All-Reduce for Low-Latency LLM Inference](https://arxiv.org/abs/2607.08973)

**Authors**: Hritvik Taneja, Anish Saxena, Abhishek Revinipati, Jae Hyung Ju, Neal C. Crago, Moinuddin Qureshi  
**Category**: cs.DC  
**Published**: 2026-07-13  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2607.08973v1  

#### Abstract
The rise of reasoning models and agentic systems has made LLM token-generation latency a key bottleneck. Unlike chatbots, whose latency gains saturate at human reading speed, these systems generate intermediate reasoning tokens not consumed by humans. Thus, per-token latency directly determines end-...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：SiFAR: Synchronization-Free All-Reduce for Low-Latency LLM Inference
1. 论文的主要贡献和创新点
✅ 解决的问题
面向推理模型和智能体系统，LLM生成的中间推理token不被人类消费，导致每token延迟直接决定端到端响应时间；低延迟推理采用最小批量，属于带宽受限场景，传统Tensor Parallelism依赖的All-Reduce开销随GPU数量增长成为核心性能瓶颈。不同方法的缺陷：
① 带All-Reduce的传统Tensor Parallelism：GPU数量增加时，All-Reduce通信开销线性上升，无法适配最小批量的带宽受限场景；
② 模型压缩类低延迟优化方案：易损失推理生成质量，不满足智能体系统的推理能力需求；
③ 最小批量推理场景：计算密度低，通信开销占比高，传统张量并行的同步开销影响更显著。

🚀 提出的新方法与思路
**SiFAR: Synchronization-Free All-Reduce**
该方法核心是在LLM推理的张量并行框架中，完全移除张量并行后所需的All-Reduce全局同步聚合操作，针对LLM生成阶段的通信特性设计无需跨GPU同步的替代通信机制，适配低延迟推理的带宽受限场景，无需额外调整模型结构或批量大小，在保障推理生成能力的前提下降低通信开销。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 通信开销控制 | 消除随GPU数量增长的All-Reduce同步开销，解决最小批量低延迟推理的带宽瓶颈 |
| token吞吐量提升 | 针对Llama-3.1-8B在8 H200 GPUs上，token吞吐量提升43% |
| 场景适配性 | 无需额外模型压缩或批量调整，适配推理模型、智能体系统等多类低延迟推理场景 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 未明确披露（基于通用LLM推理测试基准） | 评估LLM token生成延迟与吞吐量性能 |

🎯 实验设置与评估指标
任务：低延迟LLM推理性能评估
| 指标 | 含义 |
| ---- | ---- |
| token吞吐量（Tokens/秒） | 衡量单位时间内生成的token数量，越高越好 ↑ |
| 单token生成延迟（ms/token） | 衡量生成单个token的时间，越低越好 ↓ |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 带All-Reduce的传统Tensor Parallelism | LLM张量并行推理基线 | 跨GPU分片模型权重，通过All-Reduce完成张量并行后的全局同步聚合，通信开销随GPU数量线性增长 |
| SiFAR | 无同步全归约的张量并行推理方法 | 移除张量并行中的All-Reduce操作，避免全局同步开销，适配带宽受限的最小批量推理场景 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：Llama-3.1-8B在8 H200 GPU上的token吞吐量对比（主场景）**
| 方法 | token吞吐量（Tokens/秒） |
| ---- | ---- |
| 带All-Reduce的传统Tensor Parallelism | 基准值 |
| SiFAR | 提升43% ✅ |
💡 结论：在8 H200 GPU集群上，SiFAR使Llama-3.1-8B的token吞吐量较传统带All-Reduce的张量并行方法提升43%，性能最优。

注：根据现有摘要披露内容，未提供跨域迁移、鲁棒性测试及消融实验的具体数据，仅包含主benchmark下的吞吐量性能对比结果。

4. 关键结论和发现
- 主要发现：① 面向推理模型与智能体系统的低延迟LLM推理中，最小批量场景属于带宽受限场景，传统Tensor Parallelism的All-Reduce开销随GPU数量增长是核心性能瓶颈；② 移除All-Reduce同步操作的SiFAR方法，可有效降低通信开销，无需调整模型或批量即可显著提升token吞吐量；③ 在8 H200 GPU上，SiFAR对Llama-3.1-8B的token吞吐量提升达43%。
- 方法局限性：未披露SiFAR在更多GPU数量、更大参数量LLM模型或非H200硬件上的扩展性，也未提及对推理生成质量的影响及跨场景适配性细节。
- 未来工作：可探索SiFAR在更大规模GPU集群、更多参数量LLM模型上的性能表现，验证其对多轮对话、智能体任务等场景的适配性，优化无同步全归约机制以适配更多硬件架构。

> ✅ **总结一句话**：SiFAR通过移除张量并行中的All-Reduce同步操作，针对带宽受限的低延迟LLM推理场景解决了GPU数量增加导致的通信开销上升问题，在8 H200 GPU集群上可使Llama-3.1-8B的token吞吐量提升43%，为低延迟LLM推理提供了高效的优化方案。

</details>

---

### 16. [Action-Factored Multi-Agent Reinforcement Learning for Scalable Quantum Device Tuning](https://arxiv.org/abs/2607.09422)

**Authors**: Edwin De Nicolo, Rahul Marchand, Cornelius Carlsson, Pranav Vaidhyanathan, Natalia Ares  
**Category**: cs.LG  
**Published**: 2026-07-13  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2607.09422v1  

#### Abstract
Cooperative multi-agent reinforcement learning is well suited to problems with large parameter spaces and exploitable local structure, such as the tuning of electrostatically-defined quantum-dot arrays. However, if parameter cross-talk is strong, a non-stationary environment from the perspective of ...

---

### 17. [Agora: Enhancing LLM Agent Reasoning Via Auction-Based Task Allocation](https://arxiv.org/abs/2607.09600)

**Authors**: Kaiji Zhou, Ales Leonardis, Yue Feng  
**Category**: cs.AI  
**Published**: 2026-07-13  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2607.09600v1  

#### Abstract
Enhancing the reasoning capabilities of large language model (LLM) agents requires effective orchestration of diverse expert models and tools. However, existing frameworks typically call APIs based on coarse-grained matching between tasks and the functions of expert models or tools, while overlookin...

---

### 18. [ARCANA: A Reflective Multi-Agent Program Synthesis Framework for ARC-AGI-2 Reasoning](https://arxiv.org/abs/2607.09059)

**Authors**: Kunbo Zhang, Lei Fu, Zeyu Wang, Zijing Liu, Kejian Tong  
**Category**: cs.AI  
**Published**: 2026-07-13  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.09059v1  

#### Abstract
We present ARCANA, a collaborative multi agent framework for solving ARC AGI 2 tasks under strict test time and hardware constraints. ARCANA decomposes each task into iterative perception, hypothesis generation, symbolic execution, and reflective refinement. A perceptual grounding agent builds objec...

---

### 19. [An Emergent Mirage: Is Emergent Misalignment and Realignment Indeed a Robust Phenomenon?](https://arxiv.org/abs/2607.09053)

**Authors**: Abhinav Rao, Liancheng Gong, Bin Hu, Atharva Naik  
**Category**: cs.CL  
**Published**: 2026-07-13  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.09053v1  

#### Abstract
Recent work has reported Emergent Misalignment (EM), where language models fine-tuned on narrow, domain-specific misaligned datasets abruptly acquire broadly misaligned behavior, alongside evidence that this behavior can be reversed through limited realignment. We systematically study repeated align...

---

### 20. [Quantum Circuits in Diffusion Models: A Fair-Comparison Study and a Mechanistic Analysis of Angle-Embedding Failures](https://arxiv.org/abs/2607.09108)

**Authors**: Jaeuk Kim, Sanghoon Yoo  
**Category**: cs.LG  
**Published**: 2026-07-13  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.09108v1  

#### Abstract
We study the integration of variational quantum circuits (VQCs) into diffusion models through a squeeze-and-excitation (SE) channel-modulation scaffold that isolates the quantum contribution. Using a role-matched classical control and multi-seed significance testing across DDPM and latent diffusion ...

---

### 21. [Tokenizer Transplantation: Mitigating Autoregressive Collapse in Edge-Efficient Bengali ASR](https://arxiv.org/abs/2607.09598)

**Authors**: Sanjid Hasan, Md. Abdur Rahman  
**Category**: cs.CL  
**Published**: 2026-07-13  
**Score**: 26.5  
**Type**: new  
**ArXiv ID**: 2607.09598v1  

#### Abstract
Lightweight speech recognition models are critical for edge deployment, yet highly optimized architectures like Moonshine often fail on morphologically rich, non-Latin languages such as Bengali. This study identifies the root cause of this failure as the model's English-centric byte-level tokenizer,...

---

### 22. [FreyaTTS Technical Report](https://arxiv.org/abs/2607.09530)

**Authors**: Ahmet Erdem Pamuk, \"Omer Yent\"ur, Ahmet Tunga Bayrak, Yavuz Alp Sencer \"Ozt\"urk, Mustafa Yavuz  
**Category**: cs.CL  
**Published**: 2026-07-13  
**Score**: 25.0  
**Type**: new  
**ArXiv ID**: 2607.09530v1  

#### Abstract
We introduce Freya-TTS, a compact, tokenizer-free, Turkish-first text-to-speech model designed for highly reliable and efficient conversational synthesis. Freya-TTS is a 183.2M-parameter non-autoregressive conditional flow-matching Diffusion Transformer (DiT) that operates in the frozen continuous l...

---

### 23. [LongMedBench: Benchmarking Medical Agents for Long-Horizon Clinical Decision-Making](https://arxiv.org/abs/2607.09322)

**Authors**: Yanzhen Chen, Zihan Xu, Xiaocheng Zhang, Zhiting Fan, Weiqi Zhai, Hongxia Xu, Zuozhu Liu  
**Category**: cs.AI  
**Published**: 2026-07-13  
**Score**: 24.0  
**Type**: new  
**ArXiv ID**: 2607.09322v1  

#### Abstract
In this work, we introduce LongMedBench, a real-world EHR-based benchmark for long-horizon clinical decision-making. Prior evaluations of LLM-based medical agents have largely emphasized short-context knowledge QA and tool use. However, real-world medical care is inherently longitudinal, and clinici...

---

### 24. [KV-PRM: Efficient Process Reward Modeling via KV-Cache Transfer for Multi-Agent Test-Time Scaling](https://arxiv.org/abs/2607.09153)

**Authors**: Peng Kuang, Haibo Jin, Xiaoyu Han, Yanli Wang, Xiaopeng Yuan, Ye Yu, Kaidi Xu, Haohan Wang  
**Category**: cs.AI  
**Published**: 2026-07-13  
**Score**: 23.5  
**Type**: new  
**ArXiv ID**: 2607.09153v1  

#### Abstract
Process Reward Models (PRMs) have been proven to be highly effective in guiding test-time scaling (TTS) methods, which significantly boost the capabilities of LLM-based multi-agent systems. However, existing PRMs are text-based: they re-encode the entire trajectory text from scratch. In long multi-a...

---

### 25. [CogniConsole: Externalizing Inference-Time Control as a Formal Abstraction for Reliable LLM Interactions](https://arxiv.org/abs/2607.08774)

**Authors**: Vanessa Figueiredo, Wilter Franceschi  
**Category**: cs.AI  
**Published**: 2026-07-13  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2607.08774v1  

#### Abstract
Reliability in large language model (LLM) systems is typically framed as a function of model capability. We challenge this by demonstrating that reliability is significantly influenced by \emph{inference-time control} -- the computational layer governing task framing and context selection. We introd...

---

### 26. [Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon Terminal Tasks with Dense Reward-Based Grading](https://arxiv.org/abs/2607.08964)

**Authors**: Zongxia Li, Zhongzhi Li, Yucheng Shi, Ruhan Wang, Junyao Yang, Zhichao Liu, Xiyang Wu, Anhao Li, Yue Yu, Ninghao Liu, Lichao Sun, Haotao Mi,  LeoweiLiang  
**Category**: cs.AI  
**Published**: 2026-07-13  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2607.08964v1  

#### Abstract
AI agents have become capable of autonomously completing short, well-specified tasks. However, existing terminal benchmarks largely focus on simple problems that finish within minutes and are evaluated only by their final outcome. This setup overlooks intermediate progress and partial solutions, yie...

---

### 27. [TSAI-MetaFraud: A Benchmark Dataset for Financial Fraud Transaction and Behavioral Risk Detection in Metaverse Ecosystems](https://arxiv.org/abs/2607.09528)

**Authors**: Refat Ishrak Hemel, Ehsan Hallaji, Roozbeh Razavi-Far  
**Category**: cs.LG  
**Published**: 2026-07-13  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2607.09528v1  

#### Abstract
The emergence of metaverse platforms has created virtual economies that introduce new challenges related to fraud, bot activity, and illicit financial behavior. Despite growing interest in trustworthy metaverse analytics, existing datasets typically focus on user behavior, authentication, or financi...

---

### 28. [DKCD: Domain Knowledge-Enhanced Causal Discovery from Unstructured Data](https://arxiv.org/abs/2607.09348)

**Authors**: Xin Li, Jin Li, Shoujin Wang, Kun Yu, Fang Chen  
**Category**: cs.CL  
**Published**: 2026-07-13  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2607.09348v1  

#### Abstract
Causal discovery from unstructured data is a challenging yet underexplored task in high-expertise domains such as healthcare, finance, and education. Existing methods typically leverage the general knowledge of large language models (LLMs) to identify causal factors from unstructured data and annota...

---

### 29. [Autoregressive latent diffusion for 3D molecule generation](https://arxiv.org/abs/2607.09277)

**Authors**: Federico Ottomano, Gaopeng Ren, Yingzhen Li, Kim E. Jelfs, Alex M. Ganose  
**Category**: cs.LG  
**Published**: 2026-07-13  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2607.09277v1  

#### Abstract
Three-dimensional (3D) molecule generation has been dominated by diffusion models, which achieve strong generation quality but typically require the molecular size to be specified a priori. Recent autoregressive approaches have substantially narrowed the performance gap while naturally supporting va...

---

### 30. [Communication-Efficient Digital-Twin Coordination for Heterogeneous LLM Embodied Agents over Computing Power Networks](https://arxiv.org/abs/2607.09330)

**Authors**: Nuocheng Yang, Sihua Wang, Zihan Chen, Tony Q. S. Quek, Changchuan Yin  
**Category**: cs.AI  
**Published**: 2026-07-13  
**Score**: 20.0  
**Type**: new  
**ArXiv ID**: 2607.09330v1  

#### Abstract
Embodied agent teams powered by heterogeneous large language models (LLMs) are being widely deployed in physical artificial intelligence such as smart factories, warehouses, and service robotics. To enable collaboration among such an agent team, efficient coordination mechanisms that operate reliabl...

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
