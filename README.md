# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-09-15 10:31:26 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [Dynamic HBM Repartitioning for Multi-Turn MoE Serving](https://arxiv.org/abs/2609.13537v1)

**Authors**: Jinpyo Kim, Mingi Kwon, Younghoon Min, Jongryool Kim, Jishen Zhao  
**Category**: cs.DC  
**Published**: 2026-09-15  
**Score**: 130.0  
**Type**: new  
**ArXiv ID**: 2609.13537v1  

#### Abstract
Long-running multi-turn requests accumulate reusable key-value (KV) state. Once this state exceeds a fixed GPU KV-cache allocation, serving systems evict reusable prefixes, repeat prefill work, and may preempt requests. This pressure is particularly acute for Mixture-of-Experts (MoE) models: their e...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Dynamic HBM Repartitioning for Multi-Turn MoE Serving
1. 论文的主要贡献和创新点
✅ 解决的问题
多轮请求累积可复用的键值（KV）状态，当其总量超过GPU固定KV缓存分配时，服务系统会驱逐可复用前缀、重复预填充操作甚至抢占请求；该问题在混合专家（MoE）模型中尤为突出：MoE的专家权重占用了GPU大部分高带宽内存（HBM），且每个token仅激活稀疏子集的专家，而权重与KV缓存间的静态HBM边界，导致服务系统无法在对话增长时利用专家内存保存可复用状态。

🚀 提出的新方法与思路
**VAMP**：该MoE服务框架在运行时调整HBM中权重与KV缓存的边界；当无法满足KV缓存分配需求时，VAMP会对比三种方案的预估未来工作：从主机内存暂存专家权重、驱逐可能需要重新预填充的缓存前缀、抢占并重调度请求；随后通过CUDA虚拟内存管理页重映射（无需复制驻留的KV数据），将有限的专家权重区域转换为KV缓存容量，选择预估惩罚最低的方案执行。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| TTFT p90 | 相较于未修改vLLM降低23.6倍 |
| 请求吞吐量 | 相较于未修改vLLM提升20.7% |
| TPOT | 相较于未修改vLLM上升31.1% |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 2,103-turn recorded SWE-bench agent workload | 作为实验的多轮工作负载，进行5次重放评估 |

🎯 实验设置与评估指标
任务：多轮MoE模型服务性能评估
| 指标 | 含义及方向 |
| --- | --- |
| TTFT p90 | 首次token时间的第90百分位，越低越好 |
| 请求吞吐量 | 单位时间处理的请求总数，越高越好 |
| TPOT | 处理每个输出token的时间，越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 未修改vLLM | MoE serving引擎基准 | 采用固定的HBM边界，不支持动态调整专家权重与KV缓存的内存分配 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：SWE-bench多轮工作负载5次重放的性能结果（场景：Qwen3-Next-80B模型，VAMP采用15%最大专家卸载比，基线为未修改vLLM）**
| 指标 | 未修改vLLM | VAMP | 最优值 |
| --- | --- | --- | --- |
| TTFT p90（s） | 26.1 | 1.10 | 1.10 ✅ |
| 请求吞吐量 | - | 提升20.7% | 提升20.7% ✅ |
| TPOT | - | 上升31.1% | - |
💡 结论：在SWE-bench多轮工作负载场景下，VAMP（15%最大专家卸载比）相较未修改vLLM大幅降低了首次token等待延迟，同时提升了请求处理吞吐量，仅带来单位输出token时间的小幅上升。

1.主benchmark性能（L2/碰撞率等）：论文未报告
2.效率对比（FPS/参数量）：论文未报告
3.跨域/zero-shot迁移：论文未报告
4.鲁棒性/扰动测试：论文未报告
5.消融实验：论文未报告

4. 关键结论和发现
- 在多轮MoE模型服务场景中，静态HBM内存边界限制了内存资源的灵活分配，导致出现高延迟、低吞吐量的问题。
- 提出的VAMP框架通过CUDA页重映射实现HBM动态重分区，无需复制驻留KV数据即可调整内存分配，在实验工作负载下有效优化了核心服务性能。
- 采用15%最大专家卸载比时，VAMP实现了性能与资源利用的较好平衡。
方法局限性：论文未报告明确的方法局限性
未来工作：论文未报告明确的未来工作方向

> ✅ **总结一句话**：VAMP是面向多轮MoE服务的HBM动态重分区框架，通过调整内存边界并选择最优资源分配方案，在无需复制KV数据的情况下大幅降低首次token延迟并提升请求吞吐量。

</details>

---

### 2. [Reason What Matters: Retrieval-Grounded Reasoning for Universal Multimodal Embeddings](https://arxiv.org/abs/2609.15296v1)

**Authors**: Mingzhou Jiang, Peixi Wu, Hang Cheng, Yunhao Zhou, Biao Yang, Wei Yuan, Yun Li, Fan Yang, Wenwu Ou, Honghui He  
**Category**: cs.AI  
**Published**: 2026-09-15  
**Score**: 95.5  
**Type**: new  
**ArXiv ID**: 2609.15296v1  

#### Abstract
Universal multimodal embedding (UME) learns unified representations across modalities, enabling a single model to support diverse retrieval tasks. Recent methods use Chain-of-Thought (CoT) reasoning to better interpret multimodal inputs before generating embeddings for complex retrieval tasks and fu...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

### 论文标题：Reason What Matters: Retrieval-Grounded Reasoning for Universal Multimodal Embeddings
1. 论文的主要贡献和创新点
✅ 解决的问题
现有结合Chain-of-Thought（CoT）推理与GRPO优化的通用多模态嵌入（UME）方法存在两大核心痛点：① GRPO为所有CoT token分配相同优势，未识别能区分正负样本的输入支持性证据；② 每个嵌入生成需完整CoT，推理延迟高，部分轨迹已提供足够证据时仍需继续，降低效率。

🚀 提出的新方法与思路
**Retrieval-aware Self-Distillation (RASD)**：从输入支持的、可区分正样本与检索到的难负样本的证据中构建特权指导；利用在线策略自教师将轨迹级反馈提炼为与检索相关推理的token级监督，优化推理过程的信用分配。
**Retrieval-adaptive Inference (RAI)**：引入检索置信度头估计部分CoT的剩余检索效用，提前停止无效推理轨迹，并通过投机解码加速有用的推理后续，降低推理延迟。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
检索性能 | 在MMEB-V2和MRMR基准上达到SOTA
推理吞吐量 | 为竞争显式CoT的UME方法的 up to 5倍

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
MMEB-V2、MRMR | 评估所提方法的检索性能

🎯 实验设置与评估指标
任务为多模态检索任务；评估指标及含义如下：
指标 | 含义
--- | ---
检索性能 | 越高越好（↑）
推理吞吐量 | 越高越好（↑）

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
竞争显式CoT的UME方法 | 基线方法 | 采用完整CoT生成嵌入，通过GRPO优化但存在信用分配不精准、推理延迟高的缺陷

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能**：论文未报告具体数值，仅说明在MMEB-V2和MRMR上达到SOTA。
**效率对比**：论文未报告具体数值，仅说明推理吞吐量达到竞争显式CoT的UME方法的 up to 5倍。
**跨域 / zero-shot 迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告

4. 关键结论和发现
- 主要发现：1. ReWAM框架有效解决了现有CoT增强UME方法的信用分配与推理效率缺陷；2. RASD的token级监督和RAI的自适应推理是实现检索质量与推理效率平衡的核心；3. 所提方法达成了推理增强的UME在大规模部署中的实用性。
- 方法局限性：论文未提及
- 未来工作：论文未提及

> ✅ **总结一句话**：ReWAM是一种检索-grounded推理框架，通过RASD和RAI模块优化通用多模态嵌入的推理过程，在保持SOTA检索性能的同时大幅提升推理吞吐量，实现了推理增强的通用多模态嵌入在大规模部署中的可行性。

</details>

---

### 3. [BOOST: Concurrent Access to Host Memory and HBM to Accelerate LLM Inference](https://arxiv.org/abs/2609.13592v1)

**Authors**: Anish Saxena, Jae Hyung Ju, Hritvik Taneja, Po-An Tsai, Aamer Jaleel, Christos Kozyrakis, Moinuddin Qureshi  
**Category**: cs.DC  
**Published**: 2026-09-15  
**Score**: 67.5  
**Type**: new  
**ArXiv ID**: 2609.13592v1  

#### Abstract
GPU memory bandwidth and capacity limit throughput in large language model (LLM) inference. The GPU memory system consists of a primary tier of high-bandwidth memory (HBM) and a secondary tier of host memory connected via CPU-to-GPU interconnect. Current serving systems treat the tiers hierarchicall...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：BOOST: Concurrent Access to Host Memory and HBM to Accelerate LLM Inference
1. 论文的主要贡献和创新点
✅ 解决的问题
GPU内存带宽与容量限制LLM推理吞吐量；现有服务系统采用分层内存使用策略，无法充分利用主机内存带宽，预取数据时还会消耗HBM带宽用于写操作，减少需求加载带宽；现有带宽比例放置策略因未感知GPU wave和2MB GPU页大小，无法提供并发访问。

🚀 提出的新方法与思路
**BOOST** 是首个无需内核修改的运行时系统，核心思路是利用内核访问模式实现页分配与运行时数据管理的GPU wave感知，从而达成主机内存与HBM的并发比例访问，提取两者的总带宽加速LLM推理。具体实现：对静态模型权重，采用基于模运算的页放置策略消除访问比例方差；对动态分配的注意力键值（KV）对，使空闲KV页池具备wave感知能力。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| TPOT（Time-per-Output-Token） | 在iso-batch大小下相比HBM-only serving改善4.3%，相比prefetching避免TPOT降低（prefetching使TPOT降6%） |
| 吞吐量 | 在高吞吐量服务场景下平均提升31%，比prefetching高15% |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务：LLM推理服务，评估指标：Time-per-Output-Token (TPOT，↓越低越好)、吞吐量（↑越高越好），实验环境：Grace Hopper系统，BOOST集成至vLLM。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| HBM-only serving | 现有服务策略 | 仅使用HBM提供服务 |
| prefetching | 现有服务策略 | 数据无法适配HBM时，从主机内存预取数据至HBM后使用 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能（场景：iso-batch大小）**
| 方法 | TPOT（↓） |
| ---- | ---- |
| HBM-only serving | 基准值 |
| prefetching | 降低6% |
| BOOST | 改善4.3% ✅ |
💡 结论：在iso-batch场景下，BOOST的TPOT表现优于HBM-only serving和prefetching。

**主benchmark性能（场景：高吞吐量服务）**
| 方法 | 吞吐量（↑） |
| ---- | ---- |
| prefetching | 基准值 |
| BOOST | 平均提升31%，比prefetching高15% ✅ |
💡 结论：在高吞吐量场景下，BOOST的吞吐量显著高于现有策略，性能优势明显。

其他实验（效率对比、跨域迁移等）：论文未报告

4. 关键结论和发现
- 2-3条主要发现：1. 现有分层内存使用与预取策略均无法充分利用主机内存和HBM总带宽，会降低LLM推理性能；2. 通过wave感知的页分配与数据管理，BOOST无需修改内核即可实现主机内存与HBM的并发比例访问；3. BOOST在iso-batch和高吞吐量两种服务场景下均优于HBM-only和预取策略。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：BOOST是首个无需内核修改的LLM推理运行时系统，通过wave感知的数据管理实现主机内存与HBM的并发比例访问，有效提升推理的Time-per-Output-Token和吞吐量，优于现有主流服务策略。

</details>

---

### 4. [DeepSeek-V4-Flash on AMD gfx90a: Correctness Recovery and Inference Performance Engineering](https://arxiv.org/abs/2609.15627v1)

**Authors**: Siming Huang  
**Category**: cs.DC  
**Published**: 2026-09-15  
**Score**: 63.5  
**Type**: new  
**ArXiv ID**: 2609.15627v1  

#### Abstract
We present the enablement, correctness recovery, and performance engineering of DeepSeek-V4-Flash inference on AMD Instinct MI250 GPUs using the gfx90a/CDNA2 architecture. The system integrates native safetensors loading, tensor and expert parallelism, FP4 routed mixture-of-experts computation, FP8 ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

DeepSeek-V4-Flash on AMD gfx90a: Correctness Recovery and Inference Performance Engineering
1. 论文的主要贡献和创新点
✅ 解决的问题
核心痛点：DeepSeek-V4-Flash在AMD Instinct MI250（gfx90a/CDNA2）架构上的初始推理路径存在数值正确性问题（路由式专家W2布局不匹配导致），同时推理性能受多重因素限制，需进行正确性修复与性能优化。
🚀 提出的新方法与思路
**布局修复与正确性校验机制**：针对路由式专家W2布局不匹配导致的数值错误，识别输出排列方式，在权重加载阶段修复布局，并建立固定标记和基于哈希的正确性校验规则，保障推理数值正确性。
**解码性能优化方案**：通过启用packed FP4权重、INT8激活量化、CDNA2点积指令、对等读取全部归约、拓扑感知内核几何的手段提升解码阶段性能。
**预填充性能优化方案**：采用CDNA2 MFMA内核、改进的打包权重复用、减少稀疏注意力开销、增大处理块大小、重新调整专家排序的手段加速预填充阶段性能。
🔍 相比现有方法的优势
论文未报告与现有方法对比的优势维度。

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告使用的具体数据集，仅提及输入提示词长度为4604 token | 对应预填充性能测试的输入样本 |

🎯 实验设置与评估指标
任务：DeepSeek-V4-Flash在AMD Instinct MI250（gfx90a/CDNA2）架构上的自回归解码与预填充推理。
| 指标 | 含义 |
| --- | --- |
| 解码性能（token/s） | 自回归阶段的token生成速率，↑ 越高越好 |
| TTFT（s） | 首token生成时间，↓ 越低越好 |
| 输入token吞吐量（token/s） | 预填充阶段的输入token处理速率，↑ 越高越好 |

⚔️ 基线方法对比
论文未报告基线方法对比的相关内容。

3. 主要实验结果和性能指标
📊 定量结果汇总
仅覆盖论文明确报告的实验，其余标注论文未报告：

**无对应表号：TP4/EP1配置下的自回归解码性能**
| 配置 | 解码性能（token/s，↑） |
| --- | --- |
| TP4/EP1（4个MI250 GCD） | ~74.5 |
💡 结论：在TP4/EP1配置（4个MI250 GCD）下，DeepSeek-V4-Flash自回归解码性能约为74.5 token/s。

**无对应表号：4604-token提示词的预填充性能**
| 指标 | 数值 |
| --- | --- |
| TTFT（s，↓） | 2.061-2.062 |
| 输入token吞吐量（token/s，↑） | ~2234 |
💡 结论：对于4604-token的提示词，推理的首token生成时间约为2.061-2.062秒，对应输入token吞吐量约为2234 token/s。

主 benchmark 性能（L2/碰撞率等）：论文未报告
效率对比（FPS / 参数量）：论文未报告
跨域 / zero-shot 迁移：论文未报告
鲁棒性 / 扰动测试：论文未报告
消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1）DeepSeek-V4-Flash在AMD Instinct MI250（gfx90a/CDNA2）架构上初始推理路径的数值错误源于路由式专家W2布局不匹配，修复布局并加入校验后可解决该问题；2）修正推理路径后，解码与预填充性能可通过架构专属优化手段得到提升；3）该架构上的高效DeepSeek-V4-Flash推理不仅受内存带宽限制，还受FP4执行格式不匹配、低M利用率、每层同步成本的影响。
- 方法局限性：该架构上的高效推理仍受内存带宽、FP4执行格式不匹配、低M利用率、每层同步成本等多重因素限制，论文未报告彻底解决这些限制的方案。
- 未来工作：论文未报告明确的未来工作方向。

> ✅ **总结一句话**：该论文针对DeepSeek-V4-Flash在AMD Instinct MI250（gfx90a/CDNA2）架构上的数值错误问题进行修复，通过工程化优化实现了该模型的高效推理，获得了可观的解码与预填充性能。

</details>

---

### 5. [Self-Orchestrating Language Models: Leveraging Semantic Dependence for Efficient Inference](https://arxiv.org/abs/2609.14850v1)

**Authors**: Tian Jin  
**Category**: cs.AI  
**Published**: 2026-09-15  
**Score**: 59.0  
**Type**: new  
**ArXiv ID**: 2609.14850v1  

#### Abstract
Large language models (LLMs) demonstrate impressive capabilities, but their deployment presents significant efficiency challenges. Autoregressive decoding imposes substantial inference latency and under-utilizes hardware accelerators in low batch size regimes. Discrete diffusion models can generate ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Self-Orchestrating Language Models: Leveraging Semantic Dependence for Efficient Inference
1. 论文的主要贡献和创新点
✅ 解决的问题
1. 自回归解码导致显著的推理延迟，且在低批大小下硬件加速器利用率不足；
2. 离散扩散模型可并行生成，但需要大量去噪步骤才能达到自回归模型的生成质量；
3. 长上下文推理会造成内存瓶颈，对顶尖硬件加速器也构成压力。

🚀 提出的新方法与思路
**PASTA**：利用语义依赖并行化自回归解码，训练模型标注可独立生成的输出块，实现并行解码；
**TIP**：利用语义依赖驱逐KV缓存中的中间推理步骤，在维持生成准确性的同时降低内存消耗；
**Planned Diffusion**：利用语义依赖推导离散扩散的去噪顺序，通过自回归生成指定并行去噪块的计划，平衡并行性与生成质量。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 质量效率平衡 | 实现Pareto最优的质量-效率权衡 |
| 自回归解码优化 | 并行化自回归解码，降低推理延迟并提升低批大小下的硬件利用率 |
| 内存优化 | 减少长上下文推理的内存消耗 |
| 离散扩散优化 | 平衡离散扩散模型的并行性与生成质量，减少所需去噪步骤 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：论文未报告
⚔️ 基线方法对比：论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：提出自组织语言模型的核心思路，即通过让语言模型标注语义依赖来指导自身推理执行策略，针对不同场景设计的三类系统可实现质量与效率的Pareto最优权衡；
- 方法局限性：论文未报告；
- 未来工作：论文未报告。

> ✅ **总结一句话**：本论文提出的自组织语言模型通过引入语义依赖标注，设计三类针对性推理系统，为LLM及离散扩散模型的推理实现了Pareto最优的质量-效率权衡，解决了传统推理中的延迟、内存及生成质量问题。

</details>

---

### 6. [GGUF-Metadata Prediction of Single-Sequence llama.cpp Throughput Across Three Systems](https://arxiv.org/abs/2609.14864v1)

**Authors**: Xinyu Qiu, Chuhong Xu, Bo Su, Ziyao Chen, Ruiyang Xu, Shimeng Dai  
**Category**: cs.AI  
**Published**: 2026-09-15  
**Score**: 55.5  
**Type**: new  
**ArXiv ID**: 2609.14864v1  

#### Abstract
We predict single-sequence model throughput from GGUF metadata using roofline-shaped predictors with quantization-specific scale factors fitted on reference models. The scored cohort comprises 318 phase-depth measurements from 53 host-file configurations on two Apple M4 Max systems and an NVIDIA RTX...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# GGUF-Metadata Prediction of Single-Sequence llama.cpp Throughput Across Three Systems

## 1. 论文的主要贡献和创新点
### ✅ 解决的问题
现有以总参数量为依据预测单序列llama.cpp吞吐量的方法，在三个测试硬件系统（2个Apple M4 Max系统、1个NVIDIA RTX 5080）上的平均绝对百分比误差（MAPE）较高，分别为49.4%、55.3%、51.9%，预测精度无法满足需求，且缺乏适配不同硬件的低误差预测方案。

### 🚀 提出的新方法与思路
**Roofline-shaped predictors with quantization-specific scale factors**：基于GGUF元数据，采用参考模型拟合得到的量化特定尺度因子，构建屋顶型预测器，以预测单序列llama.cpp的吞吐量，核心是将量化参数纳入预测依据，提升不同系统下的预测精度。

### 🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 预测精度 | 主机特定held-out测试中，主动参数解码模型的MAPE（13.1%、14.4%、36.1%）远低于总参数方法；留一主机跨系统测试中，前两个系统的MAPE（11.6%、16.8%）低于P2预填充基线 |
| 硬件泛用性 | 可适配不同硬件系统（Apple M4 Max、NVIDIA RTX 5080）的吞吐量预测，且无需依赖硬件特定的额外校准 |

## 2. 核心实验方法和设置
### 📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 318个相位深度测量（来自2个Apple M4 Max系统、1个NVIDIA RTX 5080的53个主机文件配置） | 用于训练和测试吞吐量预测模型 |

### 🎯 实验设置与评估指标
任务为基于GGUF元数据预测单序列llama.cpp的吞吐量，评估指标为平均绝对百分比误差（MAPE），箭头方向为↓越低越好。

### ⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Total Parameters | 对比基线 | 采用总参数量作为预测吞吐量的依据 |
| P2 prefill baseline | 对比基线 | 基于预填充的P2基线的吞吐量预测方法 |
| Roofline-shaped predictors with quantization-specific scale factors | 提出方法 | 基于GGUF元数据，结合量化特定尺度因子的屋顶型预测器 |

## 3. 主要实验结果和性能指标
### 📊 定量结果汇总
**主机特定held-out集吞吐量预测MAPE（场景：单系统held-out测试）**
| 方法 | 系统1（Apple M4 Max） | 系统2（Apple M4 Max） | 系统3（NVIDIA RTX 5080） |
| --- | --- | --- | --- |
| 主动参数解码模型 | 13.1% ✅ |14.4% ✅ |36.1% ✅ |
| Total Parameters |49.4% |55.3% |51.9% |
💡 结论：主动参数解码模型在主机特定held-out测试场景中，各系统的吞吐量预测MAPE均显著低于总参数方法，预测精度提升明显。

**留一主机跨系统吞吐量预测MAPE（场景：跨系统泛化测试）**
| 方法 | 系统1 | 系统2 | 系统3 |
| --- | --- | --- | --- |
| 主动参数解码模型 | 11.6% ✅ |16.8% ✅ |36.0% |
| P2 prefill baseline |18.7% |22.2% |108.2% |
💡 结论：主动参数解码模型在留一主机的跨系统测试场景中，前两个系统的预测MAPE优于P2预填充基线，第三个系统两者MAPE相近，但P2预填充基线在第三个系统的MAPE过高。

### 其他实验
论文未报告
（主benchmark性能、效率对比（FPS/参数量）、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验均未在论文中提及）

## 4. 关键结论和发现
- 主要发现：1. 基于GGUF元数据和量化特定尺度因子的屋顶型预测器，在单序列llama.cpp吞吐量预测任务上，预测精度显著优于总参数方法和P2预填充基线；2. 该预测器在跨系统（留一主机）场景下仍能保持较好的预测性能；3. 低比特模型的梯子会改变运行时栈的排序；4. GGUF结构对吞吐量预测有帮助。
- 方法局限性：拟合得到的模型效率（fitted efficiencies）不具备通用性。
- 未来工作：论文未报告

> ✅ **总结一句话**：这篇论文提出基于GGUF元数据、结合量化特定尺度因子的屋顶型预测器，实现了llama.cpp单序列吞吐量的低误差预测，验证了该方法在主机特定测试和跨系统测试中的有效性，同时指出该方法的效率模型不具备通用性。

</details>

---

### 7. [MAPS: Memory-Aware Predictive Scheduling Framework for Large Language Model Serving](https://arxiv.org/abs/2609.15359v1)

**Authors**: Tiancheng Zhang, Yulin Chen, Yunfeng Zhao, Shaoyuan Huang, Cheng Zhang, Xiaofei Wang  
**Category**: cs.AI  
**Published**: 2026-09-15  
**Score**: 55.0  
**Type**: new  
**ArXiv ID**: 2609.15359v1  

#### Abstract
The surge of large language model (LLM) applications on personal devices imposes massive, bursty workloads on cloud serving infrastructure. While prefill-decode disaggregation improves throughput and scalability, memory-bound decode instances often suffer from persistent load imbalance, as output le...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

MAPS: Memory-Aware Predictive Scheduling Framework for Large Language Model Serving
1. 论文的主要贡献和创新点
✅ 解决的问题
大型语言模型（LLM）应用在个人设备的激增给云服务基础设施带来大量突发负载；预填-解码分离架构虽提升了吞吐量与可扩展性，但请求到达时输出长度未知，导致内存受限的解码实例存在持续负载不平衡问题。

🚀 提出的新方法与思路
**MAPS框架**：针对分离式LLM服务设计的内存感知预测调度框架。
**设备辅助的投机性输出长度预测**：与云侧预填操作重叠执行，延迟开销可忽略不计。
**不确定性感知校准**：推导目标覆盖率下的输出长度上界，支撑安全调度决策。
**分层全局-本地调度策略**：缓解解码器间队列堆积与解码器内队头阻塞问题。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 平均端到端延迟 | 相比三个现有最优LLM服务系统，平均端到端延迟降低42.6 |
| 尾延迟 | 相比三个现有最优LLM服务系统，尾延迟最多降低84.8 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 两个真实工作负载 | 用于模型评估 |

🎯 实验设置与评估指标
任务为分离式LLM服务的调度性能优化，评估指标定义如下：
| 指标 | 含义 |
| ---- | ---- |
| 平均端到端延迟 | 请求从到达至生成全部输出的平均时间，↓越低越好 |
| 尾延迟 | 高百分位请求的端到端延迟，↓越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 三个现有最优系统 | 基线对比 | 作为参照与MAPS进行性能对比 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告结果对应的表号或图号，仅报告实验在两个真实工作负载和两个LLMs上开展：
MAPS相比三个现有最优系统，将平均端到端延迟降低42.6，尾延迟最多降低84.8。
💡 结论：MAPS在指定实验场景下显著优于现有三个最优LLM服务系统，可有效降低分离式LLM服务的平均端到端延迟和尾延迟。
1. 主benchmark性能：论文未报告
2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：针对分离式LLM服务因输出长度未知导致的解码器负载不平衡问题，MAPS框架通过设备辅助投机预测、不确定性校准和分层调度策略实现有效优化，且在指定实验中性能显著优于三个现有最优系统。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：MAPS是针对分离式LLM服务的内存感知预测调度框架，通过系列优化策略解决了解码器负载不平衡问题，可显著降低LLM服务的平均端到端延迟和尾延迟。

</details>

---

### 8. [Func-R1: Incentivizing Mathematical Function Reasoning in Multimodal Large Language Models](https://arxiv.org/abs/2609.14779v1)

**Authors**: Mingze Yin, Xiaohan Wang, Dian Li, Haichao Yao, Yilin Zhao, Youjun Chen, Gang Liu, Jintai Chen, Yiheng Zhu, Chang-Yu Hsieh, Aimin Pan  
**Category**: cs.CL  
**Published**: 2026-09-15  
**Score**: 54.5  
**Type**: new  
**ArXiv ID**: 2609.14779v1  

#### Abstract
Performing deliberate mathematical reasoning in visual contexts is a hallmark of advanced Multimodal Large Language Models (MLLMs) and requires a sophisticated synthesis of perceptual grounding and symbolic logic. However, in the realm of mathematical functions, our investigation reveals a critical ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Func-R1: Incentivizing Mathematical Function Reasoning in Multimodal Large Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题
在多模态大语言模型（MLLMs）处理视觉语境下的数学函数推理时，存在模态干扰现象，即使先进模型开展文本计算推理，也易忽视或误判关键视觉线索。
🚀 提出的新方法与思路
**Func-R1**：基于显式解耦架构，采用分层后训练框架，逐步识别关键视觉证据并进行深度理论推理。
**Perception-Aligned Theoretic Optimization (PATO)策略**：引导策略更新以内化基础理论特性，同时在推理过程中动态修正异构视觉信息。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 模态干扰问题解决 | 可缓解多模态大语言模型处理数学函数推理时存在的忽视或误判关键视觉线索的模态干扰现象 |
| 模型性能 | 为开源多模态大语言模型中性能最优的模型，在MathVerse函数导向任务上超越GPT-5 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未明确给出具体数据集名称，仅说明在各类benchmarks上开展实验 |
🎯 实验设置与评估指标
任务为视觉语境下的数学函数推理任务，评估指标相关信息论文未报告。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| GPT-5 | 闭源多模态大语言模型 | 先进通用多模态大语言模型 |
| 其他开源多模态大语言模型 | 开源多模态大语言模型 | 作为开源领域的性能对比基线 |
3. 主要实验结果和性能指标
📊 定量结果汇总
因论文未提供定量结果对应的表号、图号等来源信息，故相关内容写为：论文未报告。
4. 关键结论和发现
- 主要发现：1）多模态大语言模型处理视觉语境下的数学函数推理时存在模态干扰现象，易忽视或误判关键视觉线索；2）提出的Func-R1方法及PATO策略可有效提升数学函数推理性能，是开源多模态大语言模型中性能最优的模型，且在MathVerse函数导向任务上超越GPT-5。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。
> ✅ **总结一句话**：Func-R1通过显式解耦架构与分层后训练框架，结合PATO策略，缓解了多模态大语言模型处理数学函数推理时的模态干扰问题，在MathVerse函数导向任务上表现优于GPT-5，是开源多模态大语言模型中的最优模型。

</details>

---

### 9. [SIMT-Aware Lockstep Verification and Functional-Coverage Closure Methodology for an Open-Source RISC-V GPGPU: A UVM 1.2 Environment](https://arxiv.org/abs/2609.13311v1)

**Authors**: Samuel Moussa, Steven Ibrahim, Ahmad Sudky, Ahmad Fawzy, Abanoub Nabil, Alhassan Sayed, Hossam Hassan, Hyung-Min Yoon  
**Category**: cs.AR  
**Published**: 2026-09-15  
**Score**: 52.5  
**Type**: new  
**ArXiv ID**: 2609.13311v1  

#### Abstract
Open-source RISC-V GPGPUs such as Vortex ship with directed-kernel regressions but no reference-model checking, functional-coverage model, or sign-off discipline. This paper presents a UVM 1.2 environment and methodology that closes that gap. The environment wraps a bus-master SIMT DUT with role-inv...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

SIMT-Aware Lockstep Verification and Functional-Coverage Closure Methodology for an Open-Source RISC-V GPGPU: A UVM 1.2 Environment
1. 论文的主要贡献和创新点
✅ 解决的问题：开源RISC-V GPGPU（如Vortex）仅配备定向内核回归，缺失参考模型检查、功能覆盖率模型及签核规范；现有验证方法存在验证维度不足、无法对无fence多核程序进行指令粒度验证、缺少SIMT专属功能覆盖率支持等核心矛盾。
🚀 提出的新方法与思路
**UVM 1.2验证环境**：针对总线主机SIMT DUT构建角色倒置代理，集成Vortex的功能模拟器SimX作为跨DPI-C的每配置黄金模型，通过两类注入合格校验器（双向端状态记分牌、每指令每lane的锁step比较器，遵循5种SIMT对齐规则）生成裁决结果。
**两遍负载值馈送技术**：实现无fence多核程序的指令粒度可验证，5432个指令退休时残余值为零，明确中断时序边界。
**三层功能覆盖率模型**：提出首个公开的SIMT功能覆盖率层（覆盖 divergence depth、bank conflicts、coalescing classes），结合ISA层构建完整覆盖率体系；在机器生成的RTL引用排除项与阻塞豁免完整性门下，达到98.1%的覆盖组分仓覆盖率、94.7%的总覆盖率，ISA层分仓覆盖率为83.1%、加权覆盖率为89.3%；未受激励的D-扩展 elaboration不影响功能分仓，仅降低总覆盖率。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 验证完整性 | 补全了开源RISC-V GPGPU缺失的参考模型检查、锁step校验与签核规范 |
| 程序验证能力 | 支持无fence多核程序的指令粒度验证，退休指令残余值为零 |
| 覆盖率体系 | 提出首个公开的SIMT专属功能覆盖率层，完善了GPU验证的覆盖率框架 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：本方法用于RISC-V GPGPU的签核验证，核心评估指标包括功能相关的覆盖率指标及指令粒度验证的残余值。
| 指标 | 含义 |
| --- | --- |
| 覆盖组分仓覆盖率 | 对应功能覆盖组的分仓完成比例，越高越好 |
| 总覆盖率 | 所有覆盖层的总完成比例，越高越好 |
| 指令粒度验证残余值 | 无fence多核程序指令退休后的残余值，越低越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 定向内核回归 | 现有开源RISC-V GPGPU验证方法 | 仅包含定向测试，缺失参考模型检查、功能覆盖率及签核规范 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告主 benchmark 性能、效率对比、跨域/zero-shot 迁移、鲁棒性/扰动测试、消融实验相关内容。

4. 关键结论和发现
- 主要发现：① 提出的UVM 1.2验证环境成功补全了开源RISC-V GPGPU验证的参考模型检查、锁step校验与功能覆盖率关闭机制；② 该方法发现了多类DUT与参考模型的缺陷，包括JALR LSB ISA偏差、非缩放看门狗常量（上游已修复）、重置Relay X窗口、缺失AXI错误路径、参考模型取指bug，其中JALR偏差与USENIX Security 2026论文FuzzGPU独立发现；③ 两遍负载值馈送技术实现了无fence多核程序的指令粒度验证，5432个指令退休时残余值为零；④ 构建的三层覆盖率模型达到了较高的覆盖水平。
- 方法局限性：论文未报告验证所用的具体数据集细节，未开展消融实验及多维度性能对比，未明确未受激励的D-扩展 elaboration对功能分仓的具体影响程度。
- 未来工作：论文未报告明确的未来工作计划。
> ✅ **总结一句话**：本论文提出的面向开源RISC-V GPGPU的SIMT-aware锁step验证与功能覆盖率关闭的UVM 1.2方法，填补了现有开源GPGPU验证的功能缺口，提供了完整的签核验证机制，发现了多类关键软硬件缺陷。

</details>

---

### 10. [Evaluation Metrics for Safe Reinforcement Learning](https://arxiv.org/abs/2609.15315v1)

**Authors**: Lindsay Spoor, Aske Plaat, Thomas Moerland  
**Category**: cs.AI  
**Published**: 2026-09-15  
**Score**: 52.0  
**Type**: new  
**ArXiv ID**: 2609.15315v1  

#### Abstract
Safe reinforcement learning (RL) is commonly formalized as a Constrained Markov Decision Process (CMDP), in which an agent maximizes expected reward while keeping its expected cumulative cost below a specified safety bound. Existing safe RL benchmarks predominantly report whether an algorithm is saf...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Evaluation Metrics for Safe Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有安全强化学习（RL）基准主要报告算法平均是否安全，遵循基于期望的保证，该惯例不足以可靠描述算法真实安全性：一是无法捕捉安全边界被违反的频率和严重程度；二是未考虑在任务和安全边界上是否一致；三是未考虑训练时行为是否能代表最终收敛策略的行为。

🚀 提出的新方法与思路
**安全RL评估指标**：针对上述不足设计，同时支持跨任务和安全边界的聚合，解决现有评估惯例的缺陷；
**安全层级系统（safety tier system）**：用于系统分类和比较算法在训练时以及最终策略的安全性和可靠性；
**SafeRLEval开源评估套件**：为未来安全RL研究提供可靠的安全表征支持。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 安全边界违反表征 | 同时覆盖违反频率与严重程度，更全面描述安全风险 |
| 跨场景一致性评估 | 考量算法在不同任务、安全边界下的表现一致性 |
| 策略代表性评估 | 区分训练阶段与最终收敛策略的行为差异 |
| 多维度信息整合 | 聚合指标、分布报告、任务/边界特定结果提供互补信息 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 多个安全导航任务 | 开展多场景的安全RL实证安全评估 |

🎯 实验设置与评估指标
任务为安全强化学习下的安全导航任务；评估指标及含义：
| 指标 | 含义（箭头） |
| --- | --- |
| 安全边界违反频率 | 越低越好 ↓ |
| 安全边界违反严重程度 | 越低越好 ↓ |
| 跨任务/安全边界表现一致性 | 越高越好 ↑ |
| 训练-最终策略行为代表性 | 越高越好 ↑ |
| 跨任务/安全边界聚合指标 | 支持多场景下的指标整合 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体定量结果的表号、数值等细节，仅提及聚合指标、分布报告、任务及安全边界特定结果各自揭示其他指标无法提供的互补信息，建议联合报告所有三类结果，而非压缩为单一数值。

4. 关键结论和发现
- 主要发现：①现有安全RL基准仅报告平均安全的惯例无法可靠评估算法真实安全性，存在多维度缺陷；②作者提出的安全RL评估指标、安全层级系统及SafeRLEval套件可解决上述缺陷；③安全RL评估需同时考虑安全风险、场景一致性、策略代表性等多维度信息，不同类型评估结果互补，需联合报告。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出的安全RL评估指标与安全层级系统，结合SafeRLEval开源套件，突破了现有安全RL基准评估惯例无法可靠表征算法真实安全性的局限，建议联合报告多维度互补评估信息以保障评估可靠性。

</details>

---

### 11. [Flattening Every Memory Peak in Long-Context Mixture-of-Experts Training](https://arxiv.org/abs/2609.14306v1)

**Authors**: Shrey Pandit, Xuan-Phi Nguyen, Yiran Zhao, Shafiq Joty  
**Category**: cs.DC  
**Published**: 2026-09-15  
**Score**: 47.5  
**Type**: new  
**ArXiv ID**: 2609.14306v1  

#### Abstract
Training a Mixture-of-Experts (MoE) model at long context or large batch size fails as soon as any one component's peak allocation exceeds device memory, so the target is every peak at once, not the average footprint. Four are left unbounded by the parallelism plans in common use, and each grows dif...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

《Flattening Every Memory Peak in Long-Context Mixture-of-Experts Training》
1. 论文的主要贡献和创新点
✅ 解决的问题：长上下文或大batch size下训练MoE模型时，任一组件的峰值内存分配超过设备内存就会导致训练失败；现有通用并行方案未限制四大内存瓶颈，分别是专家调度（路由矩阵）、词汇投影（token数×词汇量）、梯度检查点边界（层数×序列长度）、优化器状态（参数数量），且瓶颈会随模型、上下文长度、设备数量变化，降低单一瓶颈无法解决训练失败问题。
🚀 提出的新方法与思路
**PipelinedLLEP**：扩展最少负载的专家并行，对每个源贡献到调度块的token数设置上限。
**Ring-DTP**：在词汇投影阶段通过环形拓扑循环激活或权重分片，并将每个logits块折叠为在线log-sum-exp，保证计算精度。
**Selective checkpoint offload (SCO)**：将每个检查点边界的一个长寿命张量保持在CPU内存中，减少GPU峰值内存。
**OffloadStreamAdamW**：将优化器卸载的串行CPU Adam更新转化为桶流水线处理，保证损失和梯度的精确性。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 专家调度峰值内存 | 相比调优FSDP2基线，本方法可降低最多59.3% |
| 词汇投影峰值内存 | 相比调优FSDP2基线，本方法可降低86.6% |
| 优化器步骤速度 | 相比调优FSDP2基线，本方法提升2.05倍 |
| 训练上下文长度 | 相比调优FSDP2基线，本方法可达基线8-32倍的1M上下文长度 |
| 训练吞吐量 | 相比调优FSDP2基线，本方法可达10.4倍吞吐量 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：任务为长上下文MoE模型训练，评估指标如下：
| 指标 | 含义 |
| ---- | ---- |
| 专家调度峰值内存 | ↓ 越低越好 |
| 词汇投影峰值内存 | ↓ 越低越好 |
| 优化器步骤速度 | ↑ 越高越好 |
| 训练上下文长度 | ↑ 越高越好 |
| 训练吞吐量 | ↑ 越高越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 调优FSDP2基线 | 现有分布式训练方案 | 未针对长上下文MoE训练的四大内存瓶颈进行优化 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能**：论文未报告
**效率对比（FPS / 参数量）**：论文报告在120B至667B参数的MoE模型上，本方法训练可达1M上下文长度，为调优FSDP2基线的8-32倍，吞吐量达基线的10.4倍；组件测试中，专家调度峰值内存最多降低59.3%，词汇投影峰值内存降低86.6%，卸载优化器步骤速度提升2.05倍。
**跨域 / zero-shot 迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告

4. 关键结论和发现
- 现有长上下文MoE训练存在四大未受通用并行方案限制的内存峰值瓶颈，单一瓶颈的优化无法解决训练失败问题，且瓶颈随多种因素动态变化
- 所提四种方法仅调整计算与数据移动的顺序和粒度，保证损失与梯度精确性的同时，可有效降低各类内存峰值并提升训练性能
- 在120B至667B参数的MoE模型上，所提方法实现远超调优FSDP2基线的训练上下文长度与吞吐量
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：论文提出四种仅调整计算与数据移动顺序粒度的优化方法，解决了长上下文MoE训练中四大未受限制的内存峰值瓶颈，实现了更长的训练上下文长度与更高的吞吐量。

</details>

---

### 12. [Lexical Prompt Compression for Large Language Models: A Training-Free, Deterministic Pipeline with Empirical Pareto Analysis Across Eleven Task Categories](https://arxiv.org/abs/2609.13154v1)

**Authors**: Shamin Chokshi  
**Category**: cs.CL  
**Published**: 2026-09-15  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2609.13154v1  

#### Abstract
Recent advances in large language models (LLMs) have made prompts increasingly large and complex. Techniques such as chain-of-thought reasoning (Wei et al., 2022) and in-context learning (Brown et al., 2020) frequently push real-world prompts past several thousand tokens, increasing inference cost a...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Lexical Prompt Compression for Large Language Models: A Training-Free, Deterministic Pipeline with Empirical Pareto Analysis Across Eleven Task Categories
1. 论文的主要贡献和创新点
✅ 解决的问题
现有大型语言模型（LLMs）因链思维（chain-of-thought）、上下文学习（in-context learning）等技术生成的提示词规模过大，提升了推理成本与延迟；已有的学习型提示词压缩方法（如LLMLingua、Selective Context）需依赖辅助语言模型，且压缩过程非确定性。核心矛盾为探索无需辅助模型、确定性的提示词压缩方案，同时避免输出质量显著下降。

🚀 提出的新方法与思路
**Lexical Prompt Compression Pipeline**：提出一种训练-free、完全确定性、仅需CPU运行的提示词压缩流程，该流程基于经典词汇NLP技术，包含11个可切换的词汇变换（具体包括停止词移除、填充短语删除、收缩语与缩写替换、基于词性的剪枝、词形还原、WordNet驱动的同义词缩短、命名实体保留等），可配置后实现不同程度的提示词压缩。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 训练依赖 | 训练-free，无需额外训练 |
| 确定性 | 完全确定性，无随机压缩过程 |
| 运行成本 | 仅需CPU运行，无额外硬件需求 |
| 辅助模型需求 | 无需依赖辅助语言模型 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| Dolly-15k | 提供纯英文提示词用于实验 |
| LMSYS-Chat-1M | 提供纯英文提示词用于实验 |
| WildChat-1M | 提供纯英文提示词用于实验 |
| MMLU | 提供纯英文提示词用于实验 |
| GSM8K | 提供纯英文提示词用于实验 |
| HellaSwag | 提供纯英文提示词用于实验 |
（注：以上数据集共提供1242个纯英文提示词，覆盖11个自动推导的任务类别）

🎯 实验设置与评估指标
实验任务：压缩不同配置的提示词后，对比其输出结果与原提示词输出的质量，同时计算压缩比例；共生成18,630对GPT-4o-mini的输出结果用于评估。
| 指标 | 含义（箭头方向） |
|------|------------------|
| Token reduction | 提示词的token减少比例，↑越高越好 |
| BLEU | 输出文本与原输出文本的匹配度，↑越高越好 |
| ROUGE-1/2/L | 输出文本与原输出文本的重叠度，↑越高越好 |
| BERTScore-F1 | 输出文本语义与原输出文本的匹配度，↑越高越好 |
| SentenceBERT cosine similarity | 输出文本语义与原输出文本的余弦相似度，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| LLMLingua | 学习型提示词压缩方法 | 需要辅助语言模型，压缩过程非确定性 |
| Selective Context | 学习型提示词压缩方法 | 需要辅助语言模型，压缩过程非确定性 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（L2/碰撞率等）**：论文未报告
**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot 迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告
（注：论文明确报告的定量结果如下）
- 最激进配置的压缩效果：平均token减少40.3%（标准差σ=9.2），对应BERTScore-F1为0.876
- 停止词仅配置的压缩效果：平均token减少29.6%，对应BERTScore-F1为0.913
- 经验性分析：压缩-保真度的Pareto前沿可按任务类别刻画，其中常识推理（commonsense reasoning）是激进压缩下的系统性失败模式
💡 结论：Lexical Prompt Compression Pipeline的不同配置可在提示词压缩比例与输出质量间实现权衡，且无需训练与辅助模型。

4. 关键结论和发现
- 主要发现：1. 基于经典词汇NLP的训练-free、确定性提示词压缩流程可有效降低提示词规模，同时保持较高的输出保真度；2. 压缩比例与输出质量的权衡可通过不同配置形成经验性Pareto前沿，覆盖11个任务类别；3. 常识推理任务在采用激进压缩时会出现系统性的输出质量下降。
- 方法局限性：激进压缩会导致常识推理任务的性能显著退化。
- 未来工作：论文未报告

> ✅ **总结一句话**：提出的Lexical Prompt Compression Pipeline是一种训练-free、确定性、CPU-only的提示词压缩方案，可在多任务类别中实现不同程度的提示词压缩，无需辅助语言模型即可保持较高的输出质量，且压缩效果可配置以权衡压缩比例与保真度。

</details>

---

### 13. [Bypass Observation: A Conceptual Design of a Non-Intrusive Layer-Wise Semantic Extraction Architecture](https://arxiv.org/abs/2609.13807v1)

**Authors**: Haibin Tong, Jiang Yu  
**Category**: cs.AI  
**Published**: 2026-09-15  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2609.13807v1  

#### Abstract
Large language models reason in high-dimensional hidden-state spaces, while users observe only final outputs. We introduce Bypass Observation, a non-intrusive layer-wise readout architecture that attaches read-only observation heads to selected Transformer layers without feeding their outputs back i...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Bypass Observation: A Conceptual Design of a Non-Intrusive Layer-Wise Semantic Extraction Architecture
1. 论文的主要贡献和创新点
✅ 解决的问题：大语言模型在高维隐藏态空间进行推理，而用户仅能观察到模型的最终输出，存在内部推理过程不可见的痛点。
🚀 提出的新方法与思路：**Bypass Observation架构**，为一种非侵入式层间语义提取的读取架构，在选定的Transformer层附加只读观察头，且不将这些层的输出反馈至 backbone；该架构包含三种变体：跨层共享的LM头、层专属头、层或步自适应头；针对全词汇读取，推导了闭式开销近似，主要由 $V/(12d)$ 控制；同时区分bypass链思维与常规链思维：常规推理token会进入自回归计算，而bypass读取在推理时保持因果外部，仅在强化学习中可提供训练信号；还探讨了该架构在循环式、循环深度Transformer中的应用，迭代式读取可暴露收敛、振荡及潜在停止信号。
🔍 相比现有方法的优势：论文未报告
2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：论文未报告
⚔️ 基线方法对比：论文未报告
3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告
4. 关键结论和发现
- 主要发现：1. Bypass Observation架构可增强大语言模型内部计算过程的可观测性；2. 该架构的bypass读取是隐藏态的部分投影，可能具有误导性；3. 迭代式读取在循环式、循环深度Transformer中可暴露收敛、振荡等信号。
- 方法局限性：该提案为概念性和分析性设计，缺乏系统的经验验证；bypass读取是隐藏态的部分、潜在误导性的投影。
- 未来工作：开展系统的经验验证；进一步探索该架构的各类应用场景。
> ✅ **总结一句话**：Bypass Observation提出了一种非侵入式的层间只读观察头架构，可提升大语言模型内部推理过程的可观测性，推导了全词汇读取的闭式开销近似，区分了bypass链思维与常规链思维，并提及在循环Transformer中的应用潜力，但需系统经验验证。

</details>

---

### 14. [Multimodal deep learning from spectra for small-molecule structure identification: enhancing robustness with mixed-condition training](https://arxiv.org/abs/2609.14360v1)

**Authors**: Bowen Gao, Lei Zhu, Yiying Wang, Wenjie Yu  
**Category**: cs.LG  
**Published**: 2026-09-15  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2609.14360v1  

#### Abstract
In practical molecular characterization, small-molecule structure identification benefits from complementary spectroscopic evidence, but missing, degraded, or mismatched spectra challenge multimodal models. Herein, we incorporate domain knowledge from spectroscopy and chemistry into mixed-condition ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# Multimodal deep learning from spectra for small-molecule structure identification: enhancing robustness with mixed-condition training
1. 论文的主要贡献和创新点
✅ 解决的问题：小分子结构鉴定需依赖多模态光谱证据互补，但实际中常出现光谱缺失、退化或不匹配的问题，给多模态模型带来挑战；现有模型对光谱变化的鲁棒性不足，单模态场景性能较差。
🚀 提出的新方法与思路
**混合条件训练（mixed-condition training）**：结合光谱和化学领域知识，针对每个光谱模态定制扰动，采用化学信息指导的光谱替换策略，覆盖光谱可用性、质量、一致性的各类变化，用于候选结构重排序。
**混合专家（MoE）融合**：作为多模态光谱特征融合策略，与混合条件训练结合，进一步提升模型鲁棒性。
🔍 相比现有方法的优势
维度 | 优势
--- | ---
模型鲁棒性 | 混合条件训练相比完整输入训练，显著提升模型对缺失、退化、不匹配光谱的适应能力
单模态性能 | IR-only、MS/MS-only等单模态场景下的性能大幅提升，接近完整输入的效果
整体增益 | 结合MoE融合的混合条件训练，性能增益更显著

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
Multimodal Spectroscopic Dataset (MSSD) | 模拟用于小分子结构鉴定的质谱（MS）、红外光谱（IR）、1H核磁共振（NMR）及13C核磁共振（NMR）光谱
🎯 实验设置与评估指标
任务：小分子结构鉴定的候选结构重排序，每个样本对应最多128个硬候选结构，在30种预定义条件下评估共79462个测试样本。
指标 | 含义
--- | ---
MRR（均值倒数排名） | 越高越好，衡量候选结构排序的整体性能
R@1（排名1的召回率） | 越高越好，衡量最优候选排在第1位的准确率
⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
vanilla concatenation + 完整输入训练 | 多模态候选结构重排序模型 | 基线组合，使用拼接融合，采用完整光谱数据训练
MoE fusion + 完整输入训练 | 多模态候选结构重排序模型 | 使用MoE融合，采用完整光谱数据训练
vanilla concatenation + 混合条件训练 | 多模态候选结构重排序模型 | 使用拼接融合，采用混合条件数据训练
MoE fusion + 混合条件训练 | 多模态候选结构重排序模型 | 使用MoE融合，采用混合条件数据训练

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未提供对应表格/图号，无法定位具体数值来源，故不列出具体数值。
**主 benchmark 性能**
论文通过二乘二因子对比，发现混合条件训练是模型性能提升的核心来源，结合MoE融合时增益更显著。
💡 结论：混合条件训练可有效提升多模态模型的候选结构重排序性能，MoE融合能进一步放大该增益。

**效率对比**
论文未报告FPS、参数量等效率相关指标。
💡 结论：论文未提供效率相关数据。

**跨域 / zero-shot 迁移**
论文未涉及跨域或zero-shot迁移的相关实验。
💡 结论：论文未开展跨域或zero-shot迁移评估。

**鲁棒性 / 扰动测试**
论文发现混合条件训练大幅提升了IR-only、MS/MS-only单模态场景下的性能，可接近完整输入的性能水平。
💡 结论：混合条件训练有效提升了模型在光谱异常时的鲁棒性，显著改善单模态场景性能。

**消融实验**
论文采用二乘二因子对比（训练方式×融合方式）作为消融实验，评估变量为训练方式（完整输入/混合条件）和融合方式（拼接/MoE），最优组合为MoE融合+混合条件训练。
💡 结论：训练方式对性能的增益大于融合方式，MoE融合在混合条件训练下效果最优。

4. 关键结论和发现
- 主要发现：1. 结合领域知识的混合条件训练是提升小分子结构鉴定多模态模型鲁棒性的核心来源，结合MoE融合可获得额外增益；2. 混合条件训练大幅缩小了单模态场景与完整输入场景的性能差距；3. 针对光谱变化定制的混合条件训练策略有效应对了实际分子表征中的各类光谱挑战。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：这篇论文提出结合光谱与化学领域知识的混合条件训练和MoE融合方法，显著提升了小分子结构鉴定多模态模型在面对光谱缺失、退化等异常情况时的鲁棒性，同时大幅改善了单模态场景下的性能。

</details>

---

### 15. [Navigating Sparse Evidence: Agentic Visual RAG via Explicit Context Selection and Consolidation](https://arxiv.org/abs/2609.15800v1)

**Authors**: Yucheng Shen, Lingyong Yan, Jiulong Wu, Shuaiqiang Wang, Jianmin WU, Dawei Yin, Min Cao  
**Category**: cs.AI  
**Published**: 2026-09-15  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2609.15800v1  

#### Abstract
Visual Retrieval-Augmented Generation (VRAG) empowers models to navigate and answer queries about visually rich documents by retrieving relevant page images as visual evidence and reasoning over their content. However, effectively utilizing this visual evidence is usually impeded by two main challen...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Navigating Sparse Evidence: Agentic Visual RAG via Explicit Context Selection and Consolidation
1. 论文的主要贡献和创新点
✅ 解决的问题
当前视觉检索增强生成（VRAG）存在两大核心挑战：一是回答所需的证据稀疏，可能集中在单页的某一小区域或分散于多个页面；二是现有agentic方法生成答案时，依赖原始探索轨迹或压缩的文本记忆而非明确组织的支持图像，导致答案易受探索噪声影响，且证据支撑的推理轨迹不清晰，这类方法的瓶颈不仅在于证据发现，还在于答案生成前的证据保存与组织环节。

🚀 提出的新方法与思路
**SCoRE（Selection and Consolidation for Robust Evidence）**：是用于显式证据选择与整合的统一agent循环。在探索阶段，仅保留与查询相关的观测及其源指针在维护的文本账本中，既保留早期证据，又控制视觉上下文规模；在终止阶段，重新加载引用的原始图像，整合视觉证据并按逻辑序列进行组织，通过声明-图像链接实现严格的视觉接地。
**训练范式**：结合过滤后的冷启动轨迹蒸馏和证据感知强化学习，其奖励函数推动证据覆盖、整合紧凑性与答案正确性的优化。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
证据组织 | 显式构建支持图像的组织形式，建立声明与图像的明确链接，而非依赖原始探索轨迹或压缩文本记忆
推理可靠性 | 将最终推理与探索试错过程解耦，降低探索噪声对答案的影响
证据管理 | 保留早期证据的同时通过文本账本控制视觉上下文规模，平衡证据完整性与计算效率

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：论文未报告具体任务及评估指标定义
⚔️ 基线方法对比：论文未报告具体基线方法及类型特点

3. 主要实验结果和性能指标
📊 定量结果汇总
主benchmark性能：论文未报告
效率对比（FPS/参数量）：论文未报告
跨域/zero-shot迁移：论文未报告
鲁棒性/扰动测试：论文未报告
消融实验：论文未报告

4. 关键结论和发现
- 主要发现：SCoRE方法通过显式选择与整合视觉证据，将最终推理与探索过程解耦，结合证据感知强化学习可实现对证据覆盖、整合紧凑性及答案正确性的优化；
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：提出SCoRE的统一agent循环及对应训练范式，解决了VRAG中证据稀疏、现有agent方法推理噪声高与证据轨迹不清晰的问题，实现视觉证据的结构化组织与高效利用。

</details>

---

### 16. [TimeThink: Eliciting Compositional Reasoning in Timeseries Large Language Models](https://arxiv.org/abs/2609.13457v1)

**Authors**: Sudarshan Regmi, Arvind Pillai, Yu Yvonne Wu, Yuliang Chen, Bibek Panthi, Tess Z. Griffin, Michael V. Heinz, Lisa Marsch, Nicholas C. Jacobson, Andrew Campbell  
**Category**: cs.AI  
**Published**: 2026-09-15  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2609.13457v1  

#### Abstract
Timeseries multimodal large language models (TS-MLLMs) have recently begun leveraging the reasoning capabilities of large language models (LLMs) for question-answering tasks. However, these models often fail to capture dynamic temporal patterns, providing only implicit reasoning that lacks the under...

---

### 17. [Lightning Weave: Improving the Accuracy-Efficiency Frontier of Reasoning Models through Capability Composition](https://arxiv.org/abs/2609.14708v1)

**Authors**: Yecheng Wu, Song Han, Han Cai  
**Category**: cs.AI  
**Published**: 2026-09-15  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2609.14708v1  

#### Abstract
A core goal of efficient reasoning is to improve the accuracy-efficiency frontier. However, jointly improving reasoning accuracy and inference efficiency can be challenging, as the two objectives can favor different reasoning behaviors. Independently post-trained models already offer distinct streng...

---

### 18. [Unlocking the Unsolvable: Teacher-Guided Curriculum for Data-Efficient RLVR](https://arxiv.org/abs/2609.13997v1)

**Authors**: Yukang Zhu, Zhen Han  
**Category**: cs.CL  
**Published**: 2026-09-15  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2609.13997v1  

#### Abstract
Reinforcement Learning with Verifiable Rewards (RLVR) has shown remarkable success in improving the mathematical reasoning of large language models. Yet problems beyond the model's current capability, where rollouts uniformly fail and no learning signal is produced, are structurally wasted despite m...

---

### 19. [ReH-FUSE: Reliability-Aware Hierarchical Fusion of Experts for Multimodal Emotion Recognition in Conversation](https://arxiv.org/abs/2609.13857v1)

**Authors**: Guan-Hua Wen, Hou-Chiang Tseng, Kuan-Yu Chen  
**Category**: cs.LG  
**Published**: 2026-09-15  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2609.13857v1  

#### Abstract
Multimodal emotion recognition in conversation (ERC) requires adapting to the instance-dependent reliability of different evidence sources. Lexical content may be decisive, vocal expression may provide complementary cues, or accurate recognition may require cross-modal interaction; fixed fusion does...

---

### 20. [T-LoopFormer: Token-Level Elastic-Depth Looped Transformers for Latent Reasoning With Dynamic Routing](https://arxiv.org/abs/2609.15160v1)

**Authors**: Mingqian Yu, Wenpeng Zhang, Peilin Zhao  
**Category**: cs.AI  
**Published**: 2026-09-15  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2609.15160v1  

#### Abstract
Looped Transformers have recently demonstrated strong performance in both reasoning and language tasks by reusing a shared set of parameters across multiple iterations, achieving parameter efficiency without sacrificing representational power. Besides, looped Transformers perform inference directly ...

---

### 21. [TestHallVQA: Exploring LVLMs' Document-Level Reasoning under Redundant Contexts from Scientific Exams](https://arxiv.org/abs/2609.13158v1)

**Authors**: Yongqi Yu, Yu Zhang  
**Category**: cs.CL  
**Published**: 2026-09-15  
**Score**: 41.5  
**Type**: new  
**ArXiv ID**: 2609.13158v1  

#### Abstract
Large Vision--Language Models (LVLMs) are increasingly expected to perform visual question answering (VQA) over planar media. However, existing planar VQA benchmarks typically emphasize isolated challenges: some emphasize long-document understanding with limited reasoning depth, while others require...

---

### 22. [Who Teaches Which Token? Verifier-Gated Multi-Expert On-Policy Distillation for Scientific Reasoning](https://arxiv.org/abs/2609.15404v1)

**Authors**: Xun Xu, Zaixi Zhang  
**Category**: cs.AI  
**Published**: 2026-09-15  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2609.15404v1  

#### Abstract
Multi-teacher on-policy distillation (OPD) is becoming the standard way to integrate specialist capabilities into one model: train experts with RL, then distill them into the student on its own rollouts. Existing recipes assign supervision at the sequence level - each prompt goes to one domain teach...

---

### 23. [SyRHM: Symbolic-Language-Enhanced Reasoning with Associative Retrieval for Zero-shot Harmful Meme Detection](https://arxiv.org/abs/2609.13794v1)

**Authors**: Hanling Wang, Chenlong Wei, Yingjuan Li, Di Wu, Yuchao Zhang, Xiaohui Zhu, Yao Zhu  
**Category**: cs.CL  
**Published**: 2026-09-15  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2609.13794v1  

#### Abstract
Detecting harmful memes is critical for maintaining safe online communities. However, harmful intent is often implicit, arising from visual-textual incongruity and cultural stereotypes, which challenges existing multimodal detectors. We propose SyRHM, a framework that decomposes harmful meme detecti...

---

### 24. [Improving Mathematical Reasoning Capabilities in Large Language Models via Reasoning Process Error Classification](https://arxiv.org/abs/2609.15145v1)

**Authors**: Runa Yoshida, Kosuke Nishida, Kyosuke Nishida  
**Category**: cs.CL  
**Published**: 2026-09-15  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2609.15145v1  

#### Abstract
The reasoning ability of large language models (LLMs) is a critical factor for practical LLM-based applications. To investigate the current reasoning capability of LLMs, we clarify the types of errors that arise in LLMs' reasoning processes on mathematical datasets. We focus on problems where LLMs p...

---

### 25. [Physically Partitioned KVCache Format for CPU--GPU Load Balancing in MoE Inference](https://arxiv.org/abs/2609.14507v1)

**Authors**: Enda Yu, Dezun Dong, Xiangke Liao  
**Category**: cs.DC  
**Published**: 2026-09-15  
**Score**: 38.0  
**Type**: new  
**ArXiv ID**: 2609.14507v1  

#### Abstract
Single-GPU long-context inference with Mixture-of-Experts (MoE) models requires spilling the key-value cache (KVCache) to CPU memory. The spilled KV serves two complementary purposes---transferring to the GPU for attention computation, or computing in-place on the CPU---which demand opposing physica...

---

### 26. [LLM-Enhanced Multi-Agent Reinforcement Learning for Unified Electric Vehicles-Charging Station-Grid Optimization in Public Charging Systems](https://arxiv.org/abs/2609.13805v1)

**Authors**: Yang Zhang, Lindong Xie, Chongyu Wang, Gaojunjie Li, Siqi Bu, Edward Chung  
**Category**: cs.AI  
**Published**: 2026-09-15  
**Score**: 37.0  
**Type**: new  
**ArXiv ID**: 2609.13805v1  

#### Abstract
In the era of the Internet of Things (IoT), coordinating connected electric vehicle (EV) charging scheduling to balance EV charging satisfaction, station profitability, and smart grid stability presents a complex multi-objective challenge. Existing Multi-Agent Reinforcement Learning (MARL) approache...

---

### 27. [A Unified Interconnection Network for Chiplet-Based Scaling of the BrainScaleS Neuromorphic System](https://arxiv.org/abs/2609.13563v1)

**Authors**: Robin Heinemann, Johannes Schemmel  
**Category**: cs.AR  
**Published**: 2026-09-15  
**Score**: 35.5  
**Type**: new  
**ArXiv ID**: 2609.13563v1  

#### Abstract
The BrainScaleS-2 (BSS-2) neuromorphic architecture combines analog emulation of spiking neural network (SNN) primitives with tightly coupled ADCs and digital processing units. These analog SNN primitives are fixed hardware resources that cannot be multiplexed, limiting the emulated network size to ...

---

### 28. [AttnFuse: A Composable DSL for Compiling Attentions to Fused GPU Kernels](https://arxiv.org/abs/2609.13612v1)

**Authors**: Varun Kumar Dasoju, Tian Zhao  
**Category**: cs.LG  
**Published**: 2026-09-15  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2609.13612v1  

#### Abstract
Modern AI systems are built on the Transformer architecture, whose core operation, attention, accounts for the majority of computation and memory cost. Researchers continually propose new attention variants to improve quality, efficiency, or context length, but each variant currently requires expert...

---

### 29. [Trillion-Parameter MoE in a Box: Decoupling Memory Provisioning with High-Bandwidth Flash](https://arxiv.org/abs/2609.15636v1)

**Authors**: Pengfei Xia, Tuo Hao, Shengwei Li, Jinjing Chen, Shiru Wei, Wenjun Zou, Rui Zhang, Hui Zang  
**Category**: cs.AR  
**Published**: 2026-09-15  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2609.15636v1  

#### Abstract
An MoE appliance for trillion-parameter models at low concurrency must host terabytes of weights on one node and serve prefill and decode with fixed resources. Combining operator analysis of two trillion-parameter MoE models, a measured expert routing trace, and agentic serving traces over multiple ...

---

### 30. [El Agente Potente: High-Throughput Agentic Atomistic Simulations](https://arxiv.org/abs/2609.14840v1)

**Authors**: Tsz Wai Ko, Jiaru Bai, Thomas Swanick, Yeonghun Kang, Changhyeok Choi, Angelina Qihong Jiang, Aiwei Yin, Varinia Bernales, Al\'an Aspuru-Guzik  
**Category**: cs.AI  
**Published**: 2026-09-15  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2609.14840v1  

#### Abstract
Foundational machine-learning interatomic potentials (MLIPs) are transforming atomistic simulations by achieving near-ab initio accuracy across large chemical spaces at a fraction of the computational cost. A central challenge in using these tools for high-throughput property calculations is transla...

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
