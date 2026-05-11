# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-05-11 08:50:59 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG

## 📚 Recent Papers

### 1. [Sparse Attention as a Range Searching Problem: Towards an Inference-Efficient Index for KV Cache](https://arxiv.org/abs/2605.06763)

**Authors**: Mohsen Dehghankar, Abolfazl Asudeh  
**Category**: cs.LG  
**Published**: 2026-05-11  
**Score**: 15.5  
**Type**: new  
**ArXiv ID**: 2605.06763v1  

#### Abstract
Sparse attention improves LLM inference efficiency by selecting a subset of key-value entries, but at the cost of potential accuracy degradation. In particular, omitting critical KV entries can induce substantial errors in model outputs. Existing methods typically operate under fixed or adaptive tok...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Sparse Attention as a Range Searching Problem: Towards an Inference-Efficient Index for KV Cache

## 1. 论文的主要贡献和创新点

### 解决的问题
传统 **sparse attention** 方法在加速大语言模型（LLM）推理时，通常采用固定数量（top-k）或近似检索策略（如 ANN）来选择 KV Cache 中的关键条目。然而，这些方法存在两个核心缺陷：
- **False Negatives（假阴性）**：可能遗漏对当前查询至关重要的关键条目，导致生成质量显著下降。
- **静态预算限制**：固定的 token 数量无法适应不同 decoding 步骤中动态变化的“重要 token”数量。

本文指出，在长文本推理任务中，**遗漏一个关键 token 就可能导致严重的错误（error spikes）**，因此保证 **zero false negatives（零假阴性）** 是稀疏注意力机制可靠性的关键维度。

### 提出的新方法与新思路
作者提出将 **sparse attention 问题重新形式化为计算几何中的 halfspace range searching 问题**，并基于此设计了一个名为 **Louver** 的新型索引结构。

#### 核心思想
- **问题转化**：给定查询向量 $q$ 和阈值 $T$，寻找所有满足 $(q, k) \geq T$ 的 key 向量 $k$，等价于在一个 d 维空间中查找位于某个半空间（halfspace）内的所有点。
- **理论保障**：range searching 天然要求 **100% recall（完全召回）**，从而从理论上保证了 **zero false negatives**。

#### Louver 的设计亮点
1. **子空间分解（Subspace Decomposition）**：将 d 维 key 空间划分为 S 个连续的子空间，独立构建索引，提升并行性和剪枝能力。
2. **PCA Tree 分组与球包围盒（Bounding Ball）**：在每个子空间内，使用平衡 PCA Tree 对 keys 进行分组，并用中心-半径的球体（bounding ball）包围每组。通过判断球体是否与查询半空间相交，实现高效剪枝。
3. **双阶段过滤机制**：
   - **Filter Phase**：仅使用轻量级的球体-半空间相交测试，快速排除大量无关 group。
   - **Exact Check Phase**：仅对未被剪枝的候选 keys 执行精确的点积计算。
4. **增量更新（Dynamic Updates）**：新生成的 keys 存入缓冲区，定期批量构建新 group 并追加到索引，避免重建开销。GPU 上可并发执行，隐藏延迟。
5. **硬件优化**：提供针对 CPU（AVX/FP16）和 GPU（CUDA fused kernels）的深度优化实现。

### 相比现有方法的优势
| 维度 | 传统方法（如 top-k, ANN） | Louver |
|------|------------------------|-------|
| **召回率** | 可能存在 false negatives | **理论与实践均保证 zero false negatives** |
| **预算灵活性** | 固定或启发式自适应 | **完全由 query-dependent 阈值驱动，动态适应** |
| **理论基础** | 启发式或近似算法 | **基于严格的 range searching 理论框架** |
| **性能** | 可能因误删而精度下降 | **在匹配甚至超越 dense attention 精度的同时大幅加速** |

---

## 2. 核心实验方法和设置

### 数据集
- **长上下文理解任务**：
  - **LongBench v1**：多任务 QA 基准，涵盖 NarrativeQA, Qasper, HotpotQA 等。
  - **RULER**：合成基准，用于测试 needle-in-a-haystack (NIAH) 和 variable tracking (VT) 能力。
- **长输出推理任务**：
  - **AIME 2024**：30 道数学竞赛题，评估链式思维（chain-of-thought）推理能力。
  - **MATH-500**：精选的 500 道数学问题，测试复杂推理。

### 实验设置与评估指标
- **模型**：Llama-3.1-8B-Instruct, DeepSeek-R1-Distill-Llama-8B, Qwen2.5 系列等。
- **硬件**：NVIDIA A100, RTX 5090, AMD Threadripper 等。
- **评估指标**：
  - **准确性**：F1 分数（LongBench）、准确率（Accuracy）。
  - **效率**：每步 attention 延迟（latency）、速度提升倍数（speedup）。
  - **召回率**：Recall@k（恢复真实 top-k keys 的比例）。
  - **内存**：GPU 内存占用、CPU-GPU 数据传输时间。

### 基线方法对比
| 类别 | 方法 |
|------|------|
| **Dense Attention** | FlashAttention-2, Torch Eager/SDPA |
| **Eviction-based** | H2O, StreamingLLM |
| **Fixed-budget Retrieval** | Quest |
| **Adaptive-budget** | Twilight |
| **KV Offloading (CPU Retrieval)** | RetrievalAttention (HNSW), InfLLM (IVF), MagicPIG (LSH), PQCache (PQ) |

---

## 3. 主要实验结果和性能指标

### 关键性能数据
1. **准确性（Accuracy）**
   - 在 **LongBench**（10% KV 保留率）上，Louver 达到 **41.8% Avg F1**，优于 FlashAttention-2（41.7%）及所有基线。
   - 在 **RULER**（32k 上下文）上，Louver 在 VT 任务上达到 **74.0** 准确率，远超 H2O（52.0）和 Quest（60.0），接近 dense attention（84.0）。
   - 在 **MATH-500** 上，Louver 达到 **62.0%** 准确率，**超过 dense attention 基线（58.0%）**。

2. **推理速度（Latency & Speedup）**
   - 在 40k 上下文长度下，相比 dense 实现：
     - **GPU 上最高达 15.3× 加速**（vs. Torch Eager）。
     - **CPU 上最高达 10.3× 加速**（vs. Torch SDPA）。
   - 延迟随上下文增长呈 **次线性（sub-linear）** 增长，而 dense 和 Twilight 呈线性增长。

3. **召回率（Recall）**
   - Louver 在所有设置下均实现了 **≥99.9% 的完美召回率**。
   - 相比之下，ANN 方法（如 InfLLM, MagicPIG）召回率仅为 60–93%，其他 sparse 方法常低于 40%。

4. **KV Cache Offloading 性能**
   - 在 CPU offloading 设置下，Louver 平均 F1 达到 **38.9%**，远超最佳基线 InfLLM（26.2%）。
   - 检索延迟极低（**0.07ms/step**），且能剪枝超过 75% 的 keys。

### 消融实验结果
- **子空间数量（S）**：增加 S 显著提升剪枝效率。当 S=16 时，仅需扫描 16.3% 的 keys，获得 2.42× 加速。
- **分组策略**：**Contiguous grouping**（按位置连续分组）效果最好，优于随机或 PCA 分组，说明利用了 key 的局部性。
- **阈值选择（Threshold Oracle）**：`sample-max` 和 `sample-gap` 策略最稳定，CoV（变异系数）最低（~8.5%）。

---

## 4. 关键结论和发现

### 主要发现
1. **False Negatives 是稀疏注意力精度下降的首要原因**：实验证明，即使只遗漏一个相关 token，也可能引发严重错误。
2. **Halfspace Range Searching 是解决该问题的理想框架**：它天然支持动态阈值和零假阴性召回，完美契合 LLM 推理需求。
3. **Louver 实现了精度与效率的双重突破**：
   - 在多个基准上 **匹配甚至超越 dense attention 的精度**。
   - 同时实现了高达 **15.3× 的 GPU 加速**，性能优于 FlashAttention。
4. **动态重要性是普遍现象**：attention score 分布在不同 decoding 步骤间剧烈波动（wide vs. narrow tails），固定预算方法必然失效。

### 方法的局限性
- **GPU 内存开销**：Louver 引入了额外的索引元数据（如球心、半径），增加了约 25–28% 的 GPU 内存占用（相对于原始 KV Cache）。这是为换取零假阴性和高性能所付出的代价。
- **设计目标侧重检索正确性与低延迟**，而非极致压缩。

### 未来工作方向
- **消除索引元数据开销**：探索使用实际 keys 作为 group 代表（类似 HNSW 的导航节点），避免存储额外的 d 维向量。
- **扩展至 Prefilling 阶段**：目前聚焦于 decoding，未来可优化 prefilling 阶段的稀疏 attention。
- **更智能的阈值预测**：开发更鲁棒、自适应的 threshold oracle，减少对采样或固定预算的依赖。
- **与其他技术结合**：与量化（quantization）、分页（PagedAttention）等技术进一步融合，构建端到端高效的 LLM 推理系统。

> **代码已开源**：https://github.com/UIC-InDeXLab/Louver

</details>

---

### 2. [HexiSeq: Accommodating Long Context Training of LLMs over Heterogeneous Hardware](https://arxiv.org/abs/2605.07569)

**Authors**: Yan Liang, Youhe Jiang, Ran Yan, Binhang Yuan, Wei Wang, Chuan Wu  
**Category**: cs.DC  
**Published**: 2026-05-11  
**Score**: 14.5  
**Type**: new  
**ArXiv ID**: 2605.07569v1  

#### Abstract
Long-context training of large language models (LLMs) is commonly distributed with Context Parallelism (CP) and Head Parallelism (HP), but existing training systems largely assume homogeneous GPU meshes. This paper extends CP and HP to heterogeneous GPU clusters with mixed GPU models and non-uniform...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：HEXISEQ: Accommodating Long Context Training of LLMs over Heterogeneous Hardware

---

## 1. 论文的主要贡献和创新点

### 解决的问题
当前大规模语言模型（LLMs）的**长上下文训练**通常依赖于 **Context Parallelism (CP)** 和 **Head Parallelism (HP)** 进行分布式计算。然而，现有系统大多假设使用**同构 GPU 集群**（即所有设备具有相同的算力、内存和通信带宽），这在实际生产环境中并不现实。

现实中，AI 加速器快速迭代（如从 A100 到 H100 再到 B200），导致数据中心普遍存在**异构硬件集群**（混合不同代际的 GPU，如 H100、A100、A800、L40S）。在这种环境下，传统对称的 CP/HP 分布策略会导致以下问题：

- **C1: 算力与内存不匹配**  
  更快的 GPU 被较慢的 GPU 拖累，而高内存设备无法充分利用其容量来处理更长序列分片。

- **C2: 通信带宽非均匀**  
  跨节点的 RDMA/InfiniBand 带宽远低于节点内的 NVLink，导致 Ring Attention 或 All-to-All（A2A）操作被最慢链路阻塞。

### 提出的新方法：HEXISEQ
为解决上述挑战，本文提出 **HEXISEQ** ——一个支持在异构硬件上进行**完全非对称 CP-HP 分区**的长上下文训练系统。

#### 核心创新点：
1. **非对称调度抽象（Asymmetric Schedule Abstraction）**
   - 允许 A2A 组具有不同的基数（cardinality）
   - 支持跨组和跨 rank 的**非均匀序列分片**（sequence shards）
   - 实现基于设备能力的**加权注意力头分配**

2. **运行时机制支持**
   - **异构 Ragged A2A**：通过 per-rank split tables 实现非均匀的数据重分布。
   - **子环 KV 交换（Sub-ring KV Exchange）**：将 Ring Attention 分解为多个子环任务，适配不同设备持有的非连续 head 范围，并通过批量异步传输实现通信与计算重叠。

3. **层级化调度器（Hierarchical Scheduler）**
   将复杂的联合优化问题分解为三个阶段：
   - **Stage I**: 基于拓扑图聚类生成带宽感知的 A2A 分组（super-node 抽象）
   - **Stage II**: 在组间按聚合能力分配全局序列长度（compute-proportional, sqrt-compute 等策略）
   - **Stage III**: 在组内通过 coordinate descent 细化每个 rank 的序列分片和 head 数量，寻找局部最优

4. **形式化建模与约束优化**
   将异构 CP-HP 调度建模为一个受**设备内存**和**通信带宽**约束的最小化迭代延迟问题：
   $$
   T^* = \arg\min_{T \in \mathcal{S}} T_{iter}(T) \quad \text{s.t. } \text{Mem}(d; T) \leq m_d, \forall d \in D
   $$

### 相比现有方法的优势
| 对比维度 | 现有方法（USP, Ulysses, Ring Attention） | HEXISEQ |
|--------|--------------------------------------|-------|
| 并行结构 | 对称 CP/HP 网格，固定 A2A 组大小 | 完全非对称，动态适应硬件拓扑 |
| 序列分配 | 所有 rank 持有等长序列分片 | 按设备算力/内存加权分配 |
| 注意力头分配 | 均匀分布 | 按设备能力差异化分配 |
| 通信优化 | 忽视跨节点瓶颈 | 显式对齐高带宽域（如 NVLink 内部） |
| 适用场景 | 同构集群 | 异构混合集群 |

---

## 2. 核心实验方法和设置

### 数据集
- 使用 **OpenWebText2** 文本语料，经 Megatron-LM 工具打包成固定长度样本用于训练。

### 模型与工作负载
- **物理测试床实验**：
  - 模型规模：3B、7B、13B 参数的 GPT-style decoder-only 模型
  - 上下文长度：8K ~ 256K tokens
  - 全局 batch size：8

- **大规模模拟实验**：
  - 模型规模：13B 和 70B
  - 上下文长度：最高达 **1024K tokens**
  - 集群规模：32 ~ 128 GPUs
  - GPU 类型：涵盖 H100、A100、A800、L40S 四代设备

### 硬件配置
- **真实测试床**（Mixed H100/A100）：
  - H100 节点：NVLink @ 450 GB/s
  - A100 节点：NVLink @ 300 GB/s
  - 跨节点通信：RDMA @ 25 GB/s

- **模拟集群多样性**：
  - Simulation 1: 32-GPU（三代混合）
  - Simulation 2: 64-GPU（四代混合）
  - Simulation 3: 128-GPU（四代混合，更大比例旧设备）

### 评估指标
- 主要指标：**吞吐量（Throughput）**，单位为 **Tokens Per Second (TPS)**
- 性能提升以 **Speedup** 表示，相对于最强 baseline 的加速比
- 调度开销：Hierarchical Scheduler 的运行时间

### 基线方法对比
- **Ring Attention** [34]
- **Ulysses** [17]（代表 A2A-based HP）
- **USP** [8]（统一序列并行框架，枚举所有合法 (CP, HP) 因子组合取最优）

> 注：所有 baseline 均允许在其参数空间中选择最佳配置作为“最强对手”。

---

## 3. 主要实验结果和性能指标

### 物理测试床性能（Mixed H100/A100, 最多 16 GPUs）
- **平均吞吐提升**：**1.11×**
- **峰值吞吐提升**：**1.19×**
- 在多种模型（3B/7B/13B）、上下文长度（16K~256K）下均优于最强 baseline
- 随着上下文增长，优势更加明显：
  - 例如，在 7B 模型 + Setting 1 中，提速从 16K 的 1.08× 提升至 32K 的 **1.17×**

### 大规模模拟性能（32–128 GPUs, 多达四代 GPU 混合）
- **平均吞吐提升**：**1.36×**
- **最大吞吐提升**：**1.72×**
- 在 **Simulation 2（64-GPU, 四代混合）** 中增益最大，说明更多硬件多样性带来更大调度灵活性
- 即使在 **70B 模型 + 1024K 上下文** 下仍保持领先，表明方法可扩展性强

### FLOP-Comparable 同构 vs 异构对比
- 构造两个总 FLOPs 相当的对比组：
  - Sim 4: 48 H100 + 8 A100（异构） vs 152 A100（同构）
  - Sim 5: 52 H100 + 4 A100 + 8 A800（异构） vs 168 A100（同构）
- 结果：HEXISEQ 在异构集群上的吞吐量**仅比最强同构 baseline（Ulysses）低约 0.5%**
- **关键结论**：合理调度下，异构集群可以接近甚至媲美同构集群的训练效率

### 调度器开销分析
- 在 128 GPU 规模下，调度耗时 **9.0 秒**
- 在 1024 GPU 规模下，耗时 **444.0 秒（约 7.4 分钟）**
- 相对于数小时乃至数天的训练过程，调度开销**完全可接受**

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **异构硬件可用于高效长上下文训练**  
   通过非对称 CP-HP 分区，HEXISEQ 成功释放了异构集群中的闲置算力与内存资源。

2. ✅ **非对称调度显著优于对称设计**  
   在真实与模拟环境中，HEXISEQ 始终超越 USP、Ulysses 和 Ring Attention 等主流方案。

3. ✅ **调度收益随上下文长度增加而增大**  
   更长的序列提供了更大的并行粒度，使得异构调度的空间更大、收益更高。

4. ✅ **异构集群可达近似同构性能**  
   在总 FLOPs 可比的情况下，HEXISEQ 能达到与最强同构系统几乎相当的吞吐量，证明其**有效吸收了硬件异构性带来的性能损失**。

### 方法的局限性（Limitations）
1. **关注点局限于 Attention 内部结构**  
   HEXISEQ 专注于优化 CP 和 HP 层面的调度，而将 DP、TP、PP 等外层并行策略视为外部输入，未实现端到端联合优化。

2. **依赖准确的性能建模**  
   虽然成本模型已验证有效，但在极端复杂网络环境或新型硬件上可能需要重新校准。

3. **尚未部署于超大规模真实集群**  
   当前实测仅限于最多 16 GPU 的测试床；更大规模的效果依赖模拟器推断。

### 未来工作方向
1. **联合优化外层并行策略**  
   将 DP、TP、PP 与 CP-HP 进行协同调度，构建统一的异构感知训练栈。

2. **扩展至推理与微调场景**  
   探索 HEXISEQ 在 LLM inference、fine-tuning 中的应用潜力。

3. **支持动态资源变化**  
   在云环境中应对节点故障、抢占、弹性伸缩等动态事件下的自适应调度。

4. **集成编译器级优化**  
   与 Triton、CUDA Graph 等底层技术结合，进一步降低非对称通信的运行时开销。

--- 

> 🔚 **总结一句话**：  
> **HEXISEQ 首次实现了面向异构硬件的非对称 CP-HP 联合调度，在真实与模拟环境中均显著提升了长上下文 LLM 训练吞吐，并证明了异构集群可达到接近同构系统的训练效率，为低成本、可持续的大模型训练开辟了新路径。**

</details>

---

### 3. [A Scalable Recipe on SuperMUC-NG Phase 2: Efficient Large-Scale Training of Language Models](https://arxiv.org/abs/2605.07726)

**Authors**: Ajay Navilarekal Rajgopal, Nikolai Solmsdorf  
**Category**: cs.DC  
**Published**: 2026-05-11  
**Score**: 13.5  
**Type**: new  
**ArXiv ID**: 2605.07726v1  

#### Abstract
Large Language Models (LLMs) continue to demonstrate superior performance with increasing scale, yet training models with billions to trillions of parameters requires staggering computational resources, e.g. a one-trillion-parameter GPT-style model requires an estimated 120 million exaflops. This ch...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：A Scalable Recipe on SuperMUC-NG Phase 2: Efficient Large-Scale Training of Language Models

---

## 1. 论文的主要贡献和创新点

### ✅ 解决了什么问题
本论文致力于解决在 **SuperMUC-NG Phase 2** 这类基于 Intel Data Center GPU Max 1550 加速器的高性能计算（HPC）系统上，如何高效地进行 **大规模语言模型（LLM）训练** 的挑战。具体包括：
- 如何在有限的 per-device 内存下容纳数十亿至万亿参数的模型；
- 如何协调 **tensor parallelism**、**pipeline parallelism** 和 **sharded data parallelism** 以实现高吞吐量；
- 如何在生产级 HPC 系统中实现可复现、无需定制内核的端到端训练流程。

### 🚀 提出的新方法或新思路
提出了一套 **可扩展的大规模训练“配方”（scalable recipe）**，其核心是：
- **自动化并行策略搜索**：采用 **Bayesian Optimization（BO）** 自动探索最优的并行配置（如 PP、TP、MBS、GAS），减少人工调参成本；
- **组合式并行策略优化**：结合 **tensor parallelism**（单节点内）、**pipeline parallelism** 和 **ZeRO-based sharded data parallelism**，实现三维并行（3D parallelism）；
- **生产环境友好设计**：完全使用公开可用的软件栈（Megatron-DeepSpeed v2.4、PyTorch 2.8.0、Intel Extension for PyTorch），不依赖定制 kernel 或硬件修改，确保方法可被广泛复现。

### 🔍 相比现有方法的优势
| 方面 | 优势 |
|------|------|
| **可复现性** | 不依赖专有代码或定制优化，任何用户均可在 SuperMUC-NG Phase 2 上直接复现结果 |
| **效率** | 实现了接近理论峰值 10% 的 per-tile bf16 FLOPs 利用率，达到 57 TFLOPs/s per-tile |
| **扩展性** | 在 128 节点（1024 tiles）上实现了 93% 的 weak scaling 效率和 82% 的 strong scaling 效率 |
| **通用性** | 方法适用于不同规模模型（3.6B、20B、175B），具有良好的泛化能力 |

---

## 2. 核心实验方法和设置

### 📚 使用的数据集
- 本文未使用真实自然语言数据集进行完整训练，而是通过 **合成数据 benchmarking** 来评估系统性能。
- 所有实验均使用 **bf16 precision**，运行 **10 个训练步** 以稳定吞吐量测量，避免收敛影响。

### ⚙️ 实验设置
| 组件 | 配置 |
|------|------|
| **硬件平台** | SuperMUC-NG Phase 2：<br>• 128 节点（最多）<br>• 每节点 4× Intel Data Center GPU Max 1550<br>• 每加速器 2 tiles → 共 8 tiles/节点<br>• 总计 1024 tiles 参与最大实验 |
| **互联网络** | NVIDIA/Mellanox HDR InfiniBand fat-tree 结构（400 Gbit/s/node） |
| **存储系统** | DAOS tier（约 1 PB 可用空间，写带宽 >750 GB/s） |
| **软件栈** | • Megatron-DeepSpeed v2.4<br>• DeepSpeed 0.16.9<br>• PyTorch 2.8.0<br>• Intel Extension for PyTorch 2.8.0<br>• SLES + SLURM 环境 |
| **功耗限制** | GPU 加速器限制为 450W（低于标称 600W），反映实际生产条件 |

### 🎯 评估指标
| 指标 | 定义 |
|------|------|
| **Per-tile throughput** | 单 tile 实现的有效 TFLOPs/s，衡量计算利用率 |
| **Weak scaling efficiency** | 增大 global batch size 同时增加资源，保持 per-tile 负载不变下的效率 |
| **Strong scaling efficiency** | 固定 global batch size 下增大并行度的效率 |
| **Bubble overhead** | Pipeline parallelism 中由于 micro-batch 数不足导致的空闲时间 |
| **FLOP utilization** | 实际达到的 FLOPs 占理论峰值的比例（bf16） |

### 🔁 基线方法对比
- 对比的是 **不同并行策略组合下的性能表现**，而非与其他框架（如 ColossalAI）直接比较；
- 主要参照 **[5] Optimizing distributed training on Frontier** 的方法论，在异构平台上复现其可扩展性分析；
- 强调与传统全复制数据并行（data parallelism only）相比，引入 **ZeRO 分片** 显著降低内存压力。

---

## 3. 主要实验结果和性能指标

### 📊 关键性能数据
| 模型规模 | 最优配置 | Per-tile Throughput | 达到理论峰值比例 |
|----------|-----------|----------------------|--------------------|
| **175B 参数模型** | PP=16, TP=8, MBS=3, GAS=100 | **57 TFLOPs/s per-tile** | **~10% of theoretical peak bf16 FLOPs** |

| 扩展模式 | 节点数 | Tiles 数 | Scaling Efficiency |
|--------|--------|---------|---------------------|
| **Weak Scaling** | 128 | 1024 | **93%** |
| **Strong Scaling** | 128 | 1024 | **82%** |

> 注：弱扩展效率接近理想值，表明系统能有效维持 per-tile 利用率；强扩展效率下降主要源于通信开销占比上升。

### 🆚 与基线方法的对比结果
- **Tensor Parallelism 跨节点性能显著下降**：
  - 当 TP ≤ 8（单节点内）时，throughput 较高；
  - TP = 16（跨节点）时，因 all-reduce 通信延迟增加，throughput 明显下降 → **建议将 TP 限制在单节点内**。
- **Pipeline Parallelism 受 micro-batch 数量影响大**：
  - Throughput 随 micro-batch 数 $ M $ 增加而提升，直到饱和；
  - 固定 $ M $ 时，增加 PP 导致 bubble 增大，throughput 下降；
  - 若保持 $ \text{PP}/M $ 恒定，则 throughput 稳定 → **推荐平衡 PP 与 M 的比例**。

### 🔍 消融实验结果
虽然没有明确标注“ablation study”，但以下实验本质上构成消融分析：

| 实验 | 发现 |
|------|------|
| **固定 PP=1，仅改变 TP**（Sec 4.1） | TP 超过 8（跨节点）后性能骤降，说明 intra-node 通信远优于 inter-node |
| **固定 TP，调节 PP 与 M 的关系**（Sec 4.2） | Throughput 主要由 $ \text{PP}/M $ 决定，验证了 pipeline bubble 的理论模型 |
| **Bayesian Optimization 搜索最优配置**（Sec 5） | 自动化搜索找到最佳组合（PP=16, TP=8, MBS=3, GAS=100），避免手动试错，且避免 OOM 配置 |

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **Tensor Parallelism 应限制在单节点内**（TP ≤ 8）：
   - 跨节点 TP 会因高频 all-reduce 操作引发严重通信瓶颈；
   - 推荐优先使用 **intra-node tensor parallelism + inter-node data/pipeline parallelism**。

2. **Pipeline Parallelism 成功率取决于 micro-batch 数量**：
   - 至少需要足够多的 micro-batches 来填充 pipeline，减少 bubble；
   - 推荐保持 $ \text{PP}/M $ ≤ 1，并适当使用 interleaved scheduling。

3. **自动化参数搜索可行且高效**：
   - 使用 **Bayesian Optimization** 可快速收敛到高性能配置；
   - DeepHyper 支持异步调度，适合 HPC 环境中的 job submission 模式。

4. **高弱扩展效率证明系统可扩展性强**：
   - 在 128 节点上实现 **93% weak scaling efficiency**，说明该配方可推广至更大规模；
   - 强扩展效率 82% 表明仍有一定通信开销，但在合理范围内。

5. **端到端使用公开软件栈即可实现高效训练**：
   - 无需修改框架或编写 custom kernel；
   - 所有结果均可在标准 LRZ 环境下复现，极大提升了方法的实用性与普及性。

### ⚠️ 方法的局限性
| 局限性 | 说明 |
|--------|------|
| **未测试超过 175B 的模型** | 尽管提到 trillion-parameter 模型需求，但实验最大只到 175B |
| **依赖特定硬件架构** | 多 tile 架构（每 GPU 分为 2 tiles）和 Xe Link 互联对性能有重要影响，可能难以直接迁移到其他平台 |
| **功耗受限** | GPU 被限制在 450W（非满频运行），实际算力未达峰值，结果反映的是“可持续生产性能”而非极限性能 |
| **缺乏真实任务评估** | 仅评估吞吐量，未报告下游任务 accuracy 或收敛速度 |

### 🔮 未来工作方向
1. **能量效率分析**（Energy Efficiency Analysis）：
   - 当前未量化能耗，未来可在相同 FLOPs 下比较不同并行策略的能耗差异。
2. **支持更大规模模型训练**（Trillion-parameter scale）：
   - 结合 MoE（Mixture of Experts）等稀疏结构进一步扩展。
3. **跨平台迁移研究**：
   - 验证该“配方”是否适用于其他基于 GPU 或 AI 加速器的 HPC 系统。
4. **集成 Checkpointing 与 Fault Tolerance**：
   - 在长时间训练中增强容错能力，适应生产级长周期作业需求。

---

## ✅ 总结一句话
本论文提出了一种 **无需定制代码、完全基于公开软件栈的可复现大规模语言模型训练方案**，在 SuperMUC-NG Phase 2 上实现了高达 **57 TFLOPs/s per-tile** 和 **93% weak scaling efficiency**，为下一代 exascale 系统上的 LLM 训练提供了实用蓝图。

</details>

---

### 4. [Star Elastic: Many-in-One Reasoning LLMs with Efficient Budget Control](https://arxiv.org/abs/2605.07182)

**Authors**: Ali Taghibakhshi, Ruisi Cai, Saurav Muralidharan, Sharath Turuvekere Sreenivas, Aditya Vavre, Ameya Sunil Mahabaleshwarkar, Bilal Kartal, Sheldon Liang, Marcin Chochowski, Zijia Chen, Akhiad Bercovich, Ran Zilberstein, Ran El-Yaniv, Yonatan Geifman, Daniel Korzekwa, Yoshi Suhara, Oluwatobi Olabiyi, Ashwath Aithal, Nima Tajbakhsh, Pavlo Molchanov  
**Category**: cs.LG  
**Published**: 2026-05-11  
**Score**: 12.0  
**Type**: new  
**ArXiv ID**: 2605.07182v1  

#### Abstract
Training a family of large language models (LLMs), either from scratch or via iterative compression, is prohibitively expensive and inefficient, requiring separate training runs for each model in the family. In this paper, we introduce Star Elastic, a novel LLM post-training method that adds N neste...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Star Elastic: Many-in-One Reasoning LLMs with Efficient Budget Control

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
- **训练成本高昂**：传统 LLM 家族（如 Llama-3.1）需要为每个模型大小独立训练，导致计算和存储资源浪费。
- **推理效率低下**：静态架构在推理时无法根据任务阶段（思考 vs. 回答）动态调整模型容量，造成资源分配不均。
- **缺乏弹性支持**：现有压缩方法（如剪枝、蒸馏）难以支持混合架构（Mamba-Attention-MoE）的弹性嵌套（elastic nesting），且不支持量化下的零样本切片（zero-shot slicing）。

### 🚀 提出的新方法：Star Elastic
Star Elastic 是一种针对 **hybrid Mamba-Transformer-MoE 架构** 的新型后训练（post-training）方法，实现“**Many-in-One**”的弹性推理 LLM。其核心思想是：
- 在单次训练中，从一个父模型生成多个嵌套子模型（nested submodels），共享权重。
- 引入可学习的 **router** 自动决定不同预算下的最优子网络结构。
- 支持 **弹性预算控制（elastic budget control）**，在推理时对“思考”和“回答”阶段使用不同大小的子模型。
- 扩展至量化领域，通过 **Quantization-Aware Distillation (QAD)** 生成支持零样本切片的 FP8 和 NVFP4 弹性检查点。

### 🔍 相比现有方法的优势
| 维度 | Star Elastic | 传统方法 |
|------|------------|--------|
| **训练成本** | 单次训练生成多个模型，节省高达 **360× token 成本**（vs. 从头预训练），**7× 节省**（vs. 最先进压缩） | 每个模型需单独训练或压缩 |
| **推理效率** | 支持动态 per-phase 模型选择，提升准确率-延迟帕累托前沿（Pareto frontier） | 静态架构，资源固定 |
| **架构灵活性** | 支持 SSM、embedding、MoE、FFN 多维度弹性嵌套，支持异构层配置 | 多数仅支持单一维度压缩 |
| **部署效率** | 所有变体共享一个参数空间，内存占用仅为最大模型大小（如 58.9GB vs. 分离存储 126.1GB） | 每个模型独立存储，线性增长 |
| **量化兼容性** | 支持 FP8 PTQ 和 NVFP4 QAD，保留零样本切片能力 | 通常破坏嵌套结构 |

---

## 2. 核心实验方法和设置

### 📚 数据集
- **重要性估计与知识蒸馏数据**：使用训练 Nemotron Nano v3 父模型的开源数据。
- **评估基准（多任务推理与知识测试）**：
  - **AIME-2025**, **GPQA**（研究生级科学问答）
  - **LiveCodeBench v5**（代码生成）
  - **MMLU-Pro**（大学水平多任务理解）
  - **IFBench**（指令遵循）
  - **Tau Bench**（航空、零售、电信行业推理）

### ⚙️ 实验设置
- **基础模型**：NVIDIA Nemotron Nano v3 MoE (30B 参数, 激活参数 3.6A)
- **目标变体**：通过 Star Elastic 生成 **23B (2.8A)** 和 **12B (2.0A)** 嵌套模型
- **训练流程**：
  - **两阶段训练**：
    1. **短上下文阶段**（8k seq len, 100B tokens）：均匀采样预算，平衡各子模型训练信号
    2. **长上下文阶段**（49k seq len, 60B tokens）：非均匀采样（30B:23B:12B = 0.5:0.3:0.2），防止大模型退化
  - **优化器**：AdamW，学习率 1e-4（模型），1e-2（router）
  - **Gumbel-Softmax 温度**：从 1.0 退火至 0.05
- **评估工具**：vLLM（BF16/FP8/NVFP4），NeMo-Skills 库测延迟

### 🆚 基线方法对比
- **独立训练模型**：同规模社区模型（如 Qwen3-30B）
- **压缩方法**：Minitron、Sheared LLaMA 等结构化剪枝 + 蒸馏方法
- **弹性框架**：Nemotron Elastic [1]（仅支持 Mamba-Attention，无 MoE）
- **量化方法**：Post-Training Quantization (PTQ)

---

## 3. 主要实验结果和性能指标

### 📊 关键性能数据

#### ✅ 准确率表现（Table 1）
| 模型 | AIME-2025 | GPQA | MMLU-Pro | 平均 |
|------|-----------|------|----------|------|
| **Nano v3 Elastic-30B** | **88.54** | **72.10** | **78.63** | — |
| **Nano v3 Elastic-23B** | 85.63 | 69.82 | 76.07 | — |
| **Nano v3 Elastic-12B** | 78.54 | 57.39 | 68.28 | — |
| **Qwen3-30B (3.3A)** | 80.00 | 70.83 | 81.11 | — |

> 所有嵌套模型均匹配或超越同等规模独立训练模型。

#### ✅ 推理效率提升（Figure 1 右 & Table 2）
- **弹性预算控制（Elastic Budget Control）** 显著改善准确率-延迟权衡：
  - 最高 **+16% 准确率** 或 **1.9× 更低延迟**
  - 最优策略：**Ms→ML**（小模型思考，大模型回答），如 **23B → 30B**
- **吞吐量提升**（H100, BF16）：
  | 模型 | Max Batch | Speedup |
  |------|---------|--------|
  | 30B | 36 | 1× |
  | 23B | 108 | **1.8×** |
  | 12B | 224 | **2.4×** |

#### ✅ 训练与部署成本节约
- **训练 token 成本**：
  - 相比从头预训练：**360× 节省**
  - 相比 SOTA 压缩方法：**7× 节省**
- **部署内存**（Table 3）：
  - 存储 12B+23B+30B 三个变体：
    - **Star Elastic**：**58.9 GB**
    - **分离存储**：**126.1 GB**
  - 内存节省超 **50%**

#### ✅ 量化弹性模型表现（Table 4 & 14）
| 变体 | FP8 恢复率 | NVFP4 恢复率 |
|------|-----------|-------------|
| 30B | 98.69% | 97.79% |
| 23B | 99.03% | 99.15% |
| 12B | 100.26% | 97.10% |

- **FP8**：PTQ 即可，精度损失极小
- **NVFP4**：需 QAD 恢复精度，成功保留嵌套结构与零样本切片能力
- **硬件适配性增强**：12B NVFP4 可在 RTX 5080 上运行（BF16 OOM）

### 🔬 消融实验结果
| 实验 | 发现 |
|------|------|
| **两阶段训练** | 第二阶段长上下文训练显著提升复杂推理能力（如 6B 模型 AIME-2025 +19.8%） |
| **预算采样策略** | 非均匀采样（偏重 30B）防止大模型退化，提升挑战性任务表现 |
| **宽度 vs. 深度压缩** | 宽度压缩性能更优（98.1% 基线性能），深度压缩仅适用于极端延迟场景 |
| **数据混合** | 70% reasoning + 30% pretraining 最优，优于纯推理数据 |
| **缓存状态复用**（Appendix） | KV/SSM 缓存跨嵌套模型移植相似度高达 0.95，精度损失 <1%，验证缓存复用可行性 |

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **弹性嵌套可行且高效**：Star Elastic 成功将弹性嵌套扩展到 **hybrid Mamba-Attention-MoE 架构**，首次实现 MoE 模型的多尺寸零样本提取。
2. **弹性预算控制提升推理效率**：通过在“思考”和“回答”阶段使用不同大小模型（如 23B→30B），显著优化准确率-延迟权衡。
3. **训练成本大幅降低**：相比从头训练，节省 **360× token 成本**；相比压缩方法，节省 **7× 成本**。
4. **部署更轻量灵活**：所有变体共享一个检查点，内存占用仅为最大模型，支持即时零样本切片。
5. **量化兼容性强**：通过 QAD 成功构建 FP8/NVFP4 弹性检查点，进一步缩小部署体积并提升吞吐。

### ⚠️ 局限性
- 当前最小压缩比约 **2.5×**（30B → 12B），尚未探索极端压缩（如 10×）。
- 缓存状态复用依赖推理框架支持（如 vLLM），目前仍需重新计算缓存。
- 路由器未实现任务自适应选择（如自动识别数学题用大模型），仍需手动指定预算。

### 🔮 未来工作方向
- 探索 **极端压缩比**（如 10×）以适配边缘设备。
- 开发 **任务感知路由机制**，根据输入类型自动选择最优模型配置。
- 推动 **推理框架支持缓存复用**，释放 Star Elastic 的全部潜力。
- 将方法扩展至更多架构（如纯 Transformer-MoE）和模态（多模态 LLM）。

---

> **总结**：Star Elastic 提供了一种高效、灵活、低成本的 LLM 家族构建范式，不仅解决了训练与部署成本问题，还通过弹性预算控制开辟了新的推理优化路径，是迈向“智能按需分配”的重要一步。

</details>

---

### 5. [StreamPhy: Streaming Inference of High-Dimensional Physical Dynamics via State Space Models](https://arxiv.org/abs/2605.07384)

**Authors**: Panqi Chen, Yifan Sun, Shikai Fang, Xiao Fu, Lei Cheng  
**Category**: cs.LG  
**Published**: 2026-05-11  
**Score**: 12.0  
**Type**: new  
**ArXiv ID**: 2605.07384v1  

#### Abstract
Inferring the evolution of high-dimensional and multi-modal (e.g., spatio-temporal) physical fields from irregular sparse measurements in real time is a fundamental challenge in science and engineering. Existing approaches, including diffusion-based generative models and functional tensor methods, t...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文《StreamPhy: Streaming Inference of High-Dimensional Physical Dynamics via State Space Models》总结**

---

## **1. 论文的主要贡献和创新点**

### **解决的问题**
该论文针对**高维、多模态物理场（如时空动态场）在稀疏且不规则观测下的实时流式推断**这一挑战。传统方法面临以下问题：
- **Diffusion-based models**（如SDIFT）依赖全时间序列进行离线训练和迭代采样，无法支持在线流式推理。
- **Functional tensor methods**（如LRTFR、CATTE）虽能建模连续域，但通常为批处理模式，难以高效更新；且表达能力受限于张量秩，导致内存开销大、泛化能力弱。

### **提出的新方法与创新思路**
作者提出了 **StreamPhy**，一个端到端的流式推断框架，其核心由三部分构成：

1. **Data-adaptive Observation Encoder**  
   - 基于**注意力机制**设计编码器，将任意数量、不规则分布的观测点映射为固定维度的隐状态表示。
   - 引入**可学习查询向量 `q`** 和 **cross-attention**，实现对重要观测的选择性聚合。
   - 采用**随机掩码策略**模拟缺失模式，增强鲁棒性。

2. **HiPPO-based Structured State Space Model (SSM)**  
   - 利用 **HiPPO理论** 构建具有长期记忆能力的状态转移矩阵 $A$ 和输入投影 $b$。
   - 支持**不规则时间间隔的离散化更新**，适用于真实世界异步采样的场景。
   - 实现**常数级内存增长与线性时间复杂度**，适合长期序列建模。

3. **Functional Tensor Feature-wise Linear Modulation (FT-FiLM) Decoder**  
   - 提出一种新型函数式解码器，通过**特征级仿射调制**（scale & shift）融合动态状态 $X_t$ 与空间表征 $u_n$。
   - 在理论上证明其表达力强于传统的 Functional Tucker Model（FTM），闭包可达整个连续函数空间 $C(\Omega)$。
   - 允许低秩隐状态生成高质量全场重建，显著提升效率。

### **相比现有方法的优势**
| 维度 | StreamPhy | Diffusion-based (e.g., SDIFT) | Functional Tensor (e.g., LRTFR, CATTE) |
|------|-----------|-------------------------------|----------------------------------------|
| 推理模式 | ✅ 流式在线 | ❌ 离线全序列依赖 | ⚠️ 部分支持增量但需重放 |
| 表达能力 | 高（FT-FiLM） | 高但误差传播风险 | 受限于张量秩 |
| 计算效率 | $O(T)$ 时间，低延迟 | $O(T^4)$ 后验采样开销大 | 中等，依赖高秩逼近 |
| 内存占用 | 小（紧凑状态） | 大（存储完整轨迹） | 较大（因子函数参数多） |

---

## **2. 核心实验方法和设置**

### **使用的数据集**
在三个代表性物理系统上进行验证：
1. **Turbulent Flow**  
   - 尺寸：48×918×1（时间×空间点×通道）
   - 数据量：500训练 + 100测试，每帧含918个不规则空间观测
2. **Ocean Sound Speed**  
   - 尺寸：24×5×38×76（四维时空张量）
   - 数据来源：HYCOM海洋模型输出
   - 训练/测试：950 / 50，仅使用10%空间点模拟稀疏观测
3. **Active Matter**  
   - 尺寸：24×256×256（二维空间演化）
   - 数据量：900 / 28，同样稀疏采样

### **实验设置与评估指标**
- **采样模式**：
  - **Uniform Sampling**：均匀分布在时空域中的稀疏观测（比例 $p \in \{1\%, 3\%, 5\%\}$）
  - **Slab Sampling**：集中观测整片切片（如无人机沿轨迹扫描），更具挑战性
- **评估指标**：
  - **VRMSE**（Variance-scaled Root Mean Squared Error）：尺度不变的重建误差度量  
    $$
    \text{VRMSE} = \frac{\sqrt{\frac{1}{N}\sum_i (\hat{y}_i - y_i)^2}}{\text{std}(y)}
    $$
- **硬件平台**：NVIDIA RTX 4090 GPU

### **基线方法对比**
| 类型 | 方法 |
|------|------|
| **Diffusion-based** | SDIFT [16] |
| **Attention-based** | Senseiver [30] |
| **Tensor-based** | LRTFR [14], OFTD [12], CATTE [13] |

---

## **3. 主要实验结果和性能指标**

### **关键性能数据（见 Table 1）**
| 方法 | 平均 VRMSE（越小越好） |
|------|------------------------|
| **StreamPhy (MH)** | **0.0696 ~ 0.1067** |
| StreamPhy (SH) | 0.0954 ~ 0.2094 |
| SDIFT | 0.1466 ~ 0.4231 |
| CATTE | 0.0850 ~ 0.6563 |
| OFTD | 0.1470 ~ 0.7387 |
| Senseiver | 0.1248 ~ 0.3052 |

> ✅ **StreamPhy (MH)** 在所有任务和采样条件下均取得最优表现，平均比SOTA提升至少 **48%**（以VRMSE计）。

### **与基线方法的对比结果**
- 在 **slab sampling** 下，所有基线性能明显下降（尤其SDIFT），而 **StreamPhy保持稳定**，显示其对非均匀、局部聚集观测的强大鲁棒性。
- 定性可视化（Fig. 4–5）表明，StreamPhy 能更准确恢复涡旋结构、声速梯度等复杂动态细节。

### **消融实验结果（Table 2）**
| 变体 | 描述 | 性能变化 |
|------|------|----------|
| **w/o SSM** | 移除SSM模块（即无历史状态建模） | VRMSE ↑ 超过 **10倍**，说明SSM对长程依赖至关重要 |
| **w/o mask** | 关闭训练时的随机掩码机制 | 性能下降约30–50%，尤其在slab下更严重，体现其对缺失鲁棒性的贡献 |
| **with FTM** | 用Functional Tucker替代FT-FiLM | 明显劣于原版，验证了FT-FiLM更强的表达能力 |

> 🔍 所有组件均为必要，共同支撑高性能。

### **推理速度对比（Table 3）**
| 方法 | 单记录推理时间（秒） | 加速比 |
|------|--------------------|--------|
| **StreamPhy (MH)** | **0.0325 – 0.0498s** | — |
| SDIFT | 0.84 – 5.21s | **20× ~ 100× 更快** |

> 💡 原因：
> 1. StreamPhy 是端到端直接映射；
> 2. SDIFT 需多步 posterior sampling，复杂度达 $O(T^4)$；
> 3. FT-FiLM 允许使用极紧凑隐状态（如64维 vs. SDIFT的2304维）。

---

## **4. 关键结论和发现**

### **主要发现**
1. **SSM 是实现高效流式物理场推断的理想架构**：结合 HiPPO 的结构化设计，可在有限内存下捕捉长期依赖。
2. **FT-FiLM 显著超越传统 functional tensor 模型**：理论证明其具备通用逼近能力，实践上实现更高保真重建。
3. **注意力+掩码机制有效应对不规则观测**：使模型对任意采样模式具有强适应性和鲁棒性。
4. **StreamPhy 实现精度与效率双赢**：不仅精度领先，且推理速度快数十倍，真正满足实时应用需求。

### **方法的局限性**
- **未显式嵌入物理先验**：当前为纯数据驱动，缺乏PDE约束或守恒律引导，可能影响外推能力和长期稳定性。
- **SSM 参数固定**：过渡矩阵 $A$ 和 $b$ 来自 HiPPO-LegS 设计，未探索可学习或自适应形式。
- **尚未扩展至多物理场耦合系统**：目前聚焦单一物理量演化。

### **未来工作方向**
1. **融合物理知识**：将 PDE 残差作为正则项引入训练，发展 **Physics-informed StreamPhy**。
2. **可学习 SSM 结构**：探索参数化的 $A(X_t), b(s_t)$ 形式，进一步提升建模灵活性。
3. **跨场景迁移学习**：利用预训练策略，在不同但相关的物理系统间共享表示。
4. **部署优化**：面向边缘设备轻量化，支持传感器网络上的分布式流式推断。

---

> 📌 **总结一句话**：  
> **StreamPhy 通过“注意力编码 + SSM 动态建模 + FT-FiLM 高表达解码”的协同设计，首次实现了高维物理场在稀疏不规则观测下的高效、准确、真正意义上的流式推断，为环境监测、流体力学、结构健康诊断等实时系统提供了强大工具。**

</details>

---

### 6. [Stochastic Transition-Map Distillation for Fast Probabilistic Inference](https://arxiv.org/abs/2605.07661)

**Authors**: George Rapakoulias, Peter Garud, Lingjiong Zhu, Panagiotis Tsiotras  
**Category**: cs.LG  
**Published**: 2026-05-11  
**Score**: 11.0  
**Type**: new  
**ArXiv ID**: 2605.07661v1  

#### Abstract
Diffusion models achieve strong generation quality, diversity, and distribution coverage, but their performance often comes with expensive inference. In this work, we propose Stochastic Transition-Map Distillation (STMD), a teacher-free framework for accelerating diffusion model inference while pres...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：Stochastic Transition-Map Distillation for Fast Probabilistic Inference**

---

## **1. 论文的主要贡献和创新点**

### **解决的问题**
扩散模型（Diffusion Models）在生成质量、多样性和分布覆盖方面表现出色，但其推理过程通常依赖于对连续时间随机微分方程（SDE）的数值积分，导致**推理速度慢、计算成本高**。现有的加速方法（如 distillation 和 flow matching）大多专注于**确定性推理**，牺牲了生成过程中的随机性，限制了其在需要概率采样的下游任务（如逆问题求解、后验采样、能量模型微调）中的应用。

---

### **提出的新方法：Stochastic Transition-Map Distillation (STMD)**

- **核心思想**：  
  STMD 是一种**无需预训练教师模型**（teacher-free）的框架，旨在加速扩散模型的推理，同时**保留完整的概率采样能力**。不同于传统的基于 score 或 ODE 的 distillation 方法，STMD 直接学习**反向 SDE 的完整转移映射（transition map）**，即从噪声状态 $ x_t $ 到数据状态 $ x_0 $ 的条件分布 $ p(x_0|x_t) $。

- **关键技术路径**：
  - 引入 **Conditional Mean Flow** 模型来参数化 SDE 的转移过程。
  - 通过回归目标直接学习平均速度场（mean velocity），从而实现单步或少数几步的**随机采样器**。
  - 不依赖轨迹模拟、缓存或双层优化（bi-level optimization），训练更高效且可扩展。

---

### **相比现有方法的优势**

| 对比维度 | 现有方法（如 Consistency Models, DDIM Distillation） | **STMD** |
|--------|---------------------------------------------|---------|
| **是否需要教师模型** | 需要预训练扩散模型作为教师 | ✅ **无需教师模型**（teacher-free） |
| **推理模式** | 多为确定性生成（给定噪声输入，输出唯一） | ✅ 支持**完全随机采样** |
| **学习目标** | 学习 ODE 流图（flow map） | ✅ 学习 SDE 的**转移核（transition kernel）** |
| **训练复杂度** | 需要轨迹模拟或双层优化 | ✅ 仅需简单回归目标，无需轨迹缓存 |
| **理论保障** | 多数缺乏 Wasserstein 收敛分析 | ✅ 提供了 **Mean Flow 在 2-Wasserstein 距离下的收敛界** |

> 📌 **创新亮点**：首次将 Mean Flow 思想推广到**条件随机设置**，并用于学习扩散过程的**完整转移结构**，而非仅学习去噪均值。

---

## **2. 核心实验方法和设置**

### **使用的数据集**
- **MNIST**：手写数字图像，用于验证基础生成能力。
- **CIFAR-10**：32×32 彩色自然图像，评估生成质量和多样性。
- **CelebA**：人脸图像数据集，用于高分辨率生成与图像修复（inpainting）任务。

---

### **实验设置**
- **网络架构**：
  - MNIST / CIFAR-10：基于 **U-Net** 架构，使用 `diffusers` 工具箱实现。
  - CelebA：采用 **latent DiT**（Diffusion Transformer）架构，结合 VAE 编码器。
- **训练细节**：
  - 所有模型从零开始训练（scratch training），不使用预训练权重。
  - 使用相同的 backbone 进行公平比较。
  - 优化器：Adam，EMA decay = 0.9995。
  - 训练设备：单张 RTX 5090 GPU。
- **推理步骤**：
  - 控制总函数评估次数（NFE）以公平对比效率。
  - 支持灵活配置 `ninf`（外循环步数）和 `nmf`（Mean Flow 内部步数）。

---

### **评估指标**
| 数据集 | 主要指标 | 说明 |
|-------|--------|------|
| MNIST | **Fréchet Distance (FD)** in classifier latent space | 因 FID 在 MNIST 上不可靠，改用自定义分类器的倒数第二层特征计算 FD |
| CIFAR-10 | **FID-10K** | 使用 10K 生成样本与测试集计算 Fréchet Inception Distance |
| CelebA | **FID-10K**（无条件生成）、视觉质量（inpainting） | 报告 FID 并展示修复效果 |

---

### **基线方法对比**
- **Vanilla Mean Flow (Geng et al., 2025a)**：原始 Mean Flow 模型，用于 ODE 推理加速。
- **DDPM Baseline (Ho et al., 2020)**：标准扩散模型，作为生成质量基准。
- 所有方法使用相同网络结构和训练迭代次数，确保比较公平。

---

## **3. 主要实验结果和性能指标**

### **关键性能数据**

| 方法 | 数据集 | NFE | 指标 | 结果 |
|-----|--------|-----|------|------|
| **STMD** | MNIST | 2–8 | FD-10K | 显著优于 DDPM，在低 NFE 下接近 vanilla Mean Flow |
| **STMD** | CIFAR-10 | 2–8 | FID-10K | 在 NFE=8 时达到约 30；与 vanilla Mean Flow 相当 |
| **STMD** | CelebA | 8 | FID-10K | 达到 **8.28**（ninf=4, nmf=2） |
| **STMD** | CelebA (inpainting) | 50 steps | 视觉质量 | 成功恢复遮挡区域，细节自然 |

> 🔍 图3b 和 图4b 显示：**STMD 在极低 NFE（如 2–4 步）下即可实现高质量生成**，性能与 vanilla Mean Flow 相当，但支持**全随机采样**。

---

### **与基线方法的对比结果**
- **vs. Vanilla Mean Flow**：
  - 生成质量相近（FID/FD 差异小），但 **STMD 支持随机性**，适用于更多场景。
  - 训练更简单（无需 teacher model）。
- **vs. DDPM**：
  - 在相同 NFE 下，**STMD 明显优于 DDPM**，尤其在低步数时优势显著。
  - 实现了“**一步或几步内完成高质量生成**”。

---

### **消融实验（隐含分析）**
虽然未明确列出消融表，但从设计中可推断以下关键因素的影响：
- **Conditioning on $ s-r, s, t $** 而非 $ r,s,t $：显著提升模型性能（见第5节描述）。
- **使用 Conditional Mean Flow**：是实现转移核建模的关键，替换为普通回归会丢失结构信息。
- **无需 teacher model**：避免了 teacher-student 不匹配问题，提升训练稳定性。

---

## **4. 关键结论和发现**

### **主要发现**
1. ✅ **STMD 成功实现了快速且概率性的扩散推理**：可在 1–4 步内生成高质量样本，同时保持采样多样性。
2. ✅ **无需教师模型即可训练**：降低了部署门槛，提升了可扩展性。
3. ✅ **理论上有保障**：首次给出了 **Mean Flow 在 2-Wasserstein 距离下的收敛证明**，并扩展至条件设置，为方法提供了坚实理论基础。
4. ✅ **通用性强**：不仅适用于无条件生成，还可自然扩展至 **inpainting、inverse problems** 等任务（见 Appendix C）。

---

### **方法的局限性**
- **依赖闭式桥接分布（bridge distribution）**：当前方法利用了 VP-SDE 下的解析形式 $ p(x_{t'}|x_0, x_t) $，可能难以直接迁移到其他 SDE 类型。
- **高维 Lipschitz 假设**：收敛分析中假设映射是 Lipschitz 的，在极端高维或复杂流形上可能不成立。
- **尚未挑战 SOTA FID**：由于训练迭代有限，未追求极致性能，而是侧重**方法有效性验证**。

---

### **未来工作方向**
1. 将 STMD 扩展到 **其他 SDE 类型**（如 sub-VP、VE-SDE）。
2. 设计专门针对 **inverse problems** 的条件推理算法（当前仅提供简单示例）。
3. 探索 **更高效的采样策略**（如自适应 $ \Delta s $）。
4. 应用于 **视频生成、3D 生成等序列化任务**，利用其转移映射建模能力。

---

> ✅ **总结一句话**：  
> **STMD 提出了一种无需教师模型、支持全随机采样的快速扩散推理框架，通过 Conditional Mean Flow 学习 SDE 转移核，在理论和实验上均验证了其有效性，为高效概率生成开辟了新路径。**

</details>

---

### 7. [FastOmniTMAE: Parallel Clause Learning for Scalable and Hardware-Efficient Tsetlin Embeddings](https://arxiv.org/abs/2605.06982)

**Authors**: Ahmed K. Kadhim, Lei Jiao, Rishad Shafik, Ole-Christoffer Granmo, Mayur Kishor Shende  
**Category**: cs.LG  
**Published**: 2026-05-11  
**Score**: 10.5  
**Type**: new  
**ArXiv ID**: 2605.06982v1  

#### Abstract
Embedding models in natural language processing (NLP) increasingly rely on deep architectures such as BERT, while simpler models such as Word2Vec provide efficient representations but limited interpretability. The Tsetlin Machine (TM) offers an alternative logic-based learning paradigm. Omni TM Auto...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*FastOmniTMAE: Parallel Clause Learning for Scalable and Hardware-Efficient Tsetlin Embeddings*

---

## 1. 论文的主要贡献和创新点

### ✅ 解决了什么问题
- **训练效率低下**：现有的 Tsetlin Machine-based Embedding 模型（如 Omni TM-AE）虽然具备良好的可解释性和逻辑基础，但其训练过程存在严重的串行依赖（尤其是 `class_sum` 计算），导致训练速度极慢，限制了在大规模 NLP 任务中的应用。
- **硬件不匹配**：传统 GPU 架构为浮点密集型运算优化（如 FMA、Tensor Cores），而 TM 主要依赖简单的逻辑操作（AND/OR/XOR），在 GPU 上执行效率低，资源利用率差。

### ✅ 提出的新方法与新思路
- **FastOmniTMAE**：提出一种并行化的 Omni TM-AE 改进架构，通过以下两个关键设计提升效率：
  1. **去中心化更新机制**：移除全局 `class_sum` 计算，改为基于每个子句输出的局部更新概率（local update probability），实现 clause-level 的独立评估与更新。
  2. **两阶段并行流程**：将训练解耦为“评估”和“更新”两个阶段，支持高度并行执行，打破原有顺序瓶颈。

- **专用 SoC-FPGA 加速器设计**：
  - 首次实现了 **TM-based embedding 模型在 FPGA 上的全训练加速**（而非仅推理）。
  - 设计了一个可复用的 IP 核心（TMAE Training Accelerator IP），适配从资源受限（Zybo/Zynq-7000）到高性能平台（ZCU104/UltraScale+）。

### ✅ 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| **训练速度** | 在 CPU 上比 Omni TM-AE 快 **5×以上**；在 FPGA 上实现高达 **7.08× 的加速比**。 |
| **嵌入质量** | 保持与 Omni TM-AE 相当甚至更优的 embedding 质量（Spearman/Kendall 相似度）。 |
| **硬件效率** | 充分利用 FPGA 的逻辑并行能力，在小硬件足迹下完成高效训练，适合边缘部署。 |
| **可扩展性** | 支持多引擎并行实例化（如 ZCU104 上部署 12 个引擎），适应不同规模需求。 |

---

## 2. 核心实验方法和设置

### 📚 使用的数据集
| 类型 | 数据集 | 描述 |
|------|--------|------|
| **训练数据** | **1 Billion Word Dataset** | 包含约 40k 词汇，用于生成 token 的上下文文档。每 token 使用 1k~2k 示例进行训练。 |
| **分类任务** | 自定义二分类标签集 | 对 100 个目标 token 构造正负样本（是否出现在文档中）。 |
| **语义相似度** | RG65, MTurk287, MTurk771, WordSim353, MEN | 人类标注的词对相似度评分，用于评估 embedding 的语义捕捉能力。 |
| **聚类可视化** | 手动划分语义组词汇 | 如 food, geography, vehicle 等类别，使用 t-SNE 可视化 embedding 分布。 |

### ⚙️ 实验设置与评估指标

#### 单运行多环境基准（Single-Run Multi-Environment Benchmark）
- **平台**：NVIDIA DGX H100（8×GPU, 2TB RAM）
- **隔离环境**：使用 DevContainer 分别运行 FastOmniTMAE 和 Omni TM-AE
- **评估任务**：
  - **分类性能**：Precision, Recall, F1-score（100 epochs）
  - **语义相似度**：Spearman ρ 和 Kendall τ 相关系数
  - **聚类分析**：t-SNE 可视化语义分组聚集情况

#### 多硬件基准测试（Multi-Hardware Benchmark）
- **目标**：跨异构平台比较训练性能
- **设备**：
  - CPU：Core i5, Core i9, DGX H100 Host CPU
  - GPU：Intel Iris Xe, NVIDIA H100（CUDA）
  - FPGA：ZCU104（UltraScale+）、Zybo（Zynq-7000）
- **后端实现**：
  - CPU：C 实现
  - FPGA：HDL 实现（SoC-FPGA）
  - OpenCL：Intel GPU
  - CUDA：NVIDIA GPU
- **评估指标**：
  - 训练时间（秒）
  - 加速比（vs. 同平台本地 CPU）
  - RG65 上的 Spearman 相关性（embedding 质量）

#### 基线方法对比
| 模型 | 说明 |
|------|------|
| **Omni TM-AE** | 原始模型，作为主要对比基线 |
| **Word2Vec** | 浅层神经网络 embedding 模型 |
| **FastText** | 支持 subword 信息的 Word2Vec 变体 |
| **GloVe** | 基于共现矩阵的静态 embedding |
| **BERT**（间接提及） | 引言中指出当前主流但不可解释的深度模型 |

---

## 3. 主要实验结果和性能指标

### 🔢 关键性能数据汇总

#### （1）分类性能（Figure 4）
| 指标 | FastOmniTMAE | Omni TM-AE |
|------|--------------|------------|
| **平均 F1-score** | > 0.6（稳定） | 初始 ~0.58 → 最终降至 0.56 |
| **训练时间（100 epochs）** | **310 秒** | **1709 秒** |
| **加速比** | **5.5× 更快** | — |

> 💡 **发现**：Omni TM-AE 因 `class_sum` 抑制更新率，后期学习停滞；而 FastOmniTMAE 持续学习，性能更优且更快。

#### （2）语义相似度（Table 1）
| 模型 | 平均 Spearman ρ | 平均 Kendall τ |
|------|------------------|---------------|
| **FastText** | 0.550 | 0.382 |
| **Omni TM-AE** | 0.543 | 0.390 |
| **FastOmniTMAE (CPU)** | **0.537** | **0.392**（最高） |
| **FastOmniTMAE (CUDA)** | 0.532 | 0.389 |

> ✅ 在 RG65 数据集上，FastOmniTMAE 达到 **ρ = 0.656**，是所有模型中的最佳单数据集表现。

#### （3）多硬件性能对比（Table 2）

| 平台 | 配置 | 时间（秒） | 加速比 | RG65 ρ |
|------|------|-----------|--------|--------|
| **ZCU104 (FPGA)** | 12 engines | **119.9** | **7.08×** | 0.696 |
| **Zybo (FPGA)** | 2 engines | 657.4 | 5.58× | **0.669** |
| **Core i9 (CPU)** | 单线程 | 57.7 | 1.00× | 0.680 |
| **DGX H100 (CUDA)** | H100 GPU | 493.1 | 0.18× | 0.681 |

> ⚠️ **关键发现**：尽管 H100 是顶级 GPU，但由于架构不匹配，**CUDA 版本比 CPU 还慢近 6 倍**。

#### （4）消融实验与分析
- **移除 `class_sum` 不影响 embedding 质量**：实验证明，只要训练足够轮次，无需全局收敛信号即可获得高质量 embedding。
- **状态分布 ≠ 收敛指标**：虽然 negated literals 在高状态区形成清晰分布，但目前尚无明确映射表明该分布能可靠预测 embedding 性能（无法用于 early stopping）。

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **并行化 clause training 显著提升效率**：
   - 移除 `class_sum` 的全局同步开销，使训练速度提升 **5–7×**，同时维持甚至提高分类与语义相似度性能。
   
2. **GPU 不适合 TM 训练**：
   - 尽管 GPU 具备强大算力，但其针对浮点运算优化，对 TM 所需的位级逻辑操作支持薄弱，导致实际性能远低于 CPU。

3. **FPGA 是 TM 训练的理想平台**：
   - 利用 FPGA 的细粒度并行性和逻辑灵活性，可构建高效的 SoC 加速器。
   - 在资源受限的 Zybo 板上仍能实现良好性能（0.669 ρ），证明了方法的可扩展性与实用性。

4. **embedding 质量更多取决于数据丰富度而非收敛行为**：
   - 大规模数据集（如 1B Word）即使短周期训练也能产生强 embedding，而小数据集难以弥补信息不足。

### ⚠️ 局限性
- **缺乏可靠的收敛判据**：尚未建立 automaton state 分布与 embedding 质量之间的定量关系，难以自动判断何时停止训练。
- **FPGA 开发门槛较高**：虽然提供了 IP 核心，但部署仍需一定的硬件设计经验。
- **当前仅支持静态 embedding**：未涉及动态或上下文敏感表示（如 BERT-style）。

### 🔮 未来工作方向
1. **开发基于 state distribution 的 convergence metric**，实现自适应训练终止。
2. **探索动态 embedding 架构**，结合 TM 的逻辑优势与上下文建模能力。
3. **进一步优化 FPGA 资源利用**，尤其是在 BRAM 和带宽分配方面。
4. **推广至其他模态**：如图像、音频等领域的 embedding 学习。
5. **开源工具链建设**：提供完整的编译、映射与部署流程，降低使用门槛。

---

> 🏁 **总结一句话**：  
> **FastOmniTMAE 通过并行化 clause learning 和 FPGA 加速，首次实现了高效、可扩展且硬件友好的逻辑型 embedding 训练，在保持高可解释性的同时显著超越原生 TM 模型的训练效率，为绿色 AI 与边缘智能提供了新路径。**

</details>

---

### 8. [GASim: A Graph-Accelerated Hybrid Framework for Social Simulation](https://arxiv.org/abs/2605.07692)

**Authors**: Xuan Zhou, Yanhui Sun, Hantao Yao, Allen He, Yongdong Zhang, Wu Liu  
**Category**: cs.AI  
**Published**: 2026-05-11  
**Score**: 10.0  
**Type**: new  
**ArXiv ID**: 2605.07692v1  

#### Abstract
Large-scale social simulators are essential for studying complex social patterns. Prior work explores hybrid methods to scale up simulations, combining large language models (LLM)-based agents with numerical agent-based models (ABM). However, this incurs high latency due to expensive memory retrieva...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文《GASim: A Graph-Accelerated Hybrid Framework for Social Simulation》核心总结

---

## 1. 论文的主要贡献和创新点

### 解决的问题
传统的大规模社会模拟框架（如 HiSim）采用 **LLM-based agents** 与 **numerical Agent-Based Models (ABM)** 结合的混合范式来降低计算成本。然而，这类方法存在两大瓶颈：
- **高延迟的 LLM 内存检索**：核心代理（core agents）依赖 LLM 进行记忆提取，导致昂贵的推理开销。
- **顺序执行的 ABM 瓶颈**：普通代理（ordinary agents）通过串行方式更新观点，时间复杂度随代理数量线性增长。

这些问题严重制约了大规模社会模拟的效率和可扩展性。

---

### 提出的新方法与创新思路
作者提出 **GASim** —— 一种图加速的混合多智能体框架，通过引入三个核心模块实现高效仿真：

#### （1）**Graph-Optimized Memory (GOM)**  
为解决核心代理的记忆检索瓶颈，GOM 构建了一个稀疏的 **memory graph**，将记忆项作为节点，并基于内容相似性、关键词和观点值建立边。检索过程被建模为一个在图上的优化问题，使用轻量级的 **graph propagation algorithm** 替代 LLM 推理，显著减少延迟。

#### （2）**Graph Message Passing (GMP)**  
针对普通代理的顺序执行问题，GMP 将 ABM 观点更新转化为图神经网络中的并行消息传递。利用 **Graph Attention Network (GAT)** 在单次前向传播中完成所有代理的观点更新，实现 O(1) 时间复杂度下的批量处理。

#### （3）**Entropy-Driven Grouping (EDG)**  
传统方法基于静态网络度数划分核心/普通代理，无法捕捉动态涌现的意见领袖。EDG 利用局部邻域内的 **信息熵（information entropy）** 动态识别处于多元化信息环境中的代理，将其划分为核心代理，从而更真实地反映社会影响力演化。

---

### 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| **效率** | 实现端到端 **9.94× 加速**，token 消耗降至基线的 **<20%** |
| **准确性** | 在趋势对齐任务上优于所有基线，尤其在几何一致性（Fréchet distance）方面表现最佳 |
| **动态适应性** | EDG 能够动态识别新兴意见领袖，提升模拟的真实性 |
| **可扩展性** | 支持百万级代理模拟，适用于现实世界复杂社交场景 |

---

## 2. 核心实验方法和设置

### 数据集
构建了三个主题驱动的真实社交媒体数据集，均来自公开平台爬取：
| 数据集 | 来源 | 主题 | 用户数 | 帖子数 | 时间跨度 |
|--------|------|-------|--------|--------|----------|
| **Politics** | X (Twitter) | 特朗普与“通俄门”事件 | 9,135 | 12,404 | 2017年5月–12月 |
| **Business** | X (Twitter) | 新疆棉争议 | 9,150 | 14,494 | 2021年3月–7月 |
| **Education** | Sina Weibo | 阿里巴巴数学竞赛作弊疑云 | 11,454 | 135,528 | 2024年6月–11月 |

每条数据包含匿名用户ID、描述、粉丝数、推文内容、发布时间及由 `gpt-4o-mini` 打分生成的 **opinion value ∈ [-1, +1]**。

---

### 实验设置
- **代理总数**：10,000
- **核心代理数量**：Top-K = 100（由 EDG 动态选择）
- **LLM 模型**：Llama-3.1-8B-Instruct（本地部署）
- **嵌入模型**：Bge-small-en-v1.5
- **硬件配置**：40 vCPU, 2× NVIDIA vGPU-48GB, 180 GB RAM
- **训练策略**：GMP 在前10步真实数据上训练，在完整30步模拟中测试（避免数据泄露）

---

### 评估指标
从统计与几何两个维度评估模拟趋势与真实舆论的一致性：

| 指标 | 类型 | 含义 |
|------|------|------|
| **ΔBias ↓** | 统计 | 平均绝对偏差，衡量整体偏移 |
| **ΔDiv ↓** | 统计 | 偏差方差，衡量稳定性 |
| **Corr. ↑** | 统计 | Pearson相关系数，衡量线性趋势一致性 |
| **F. ↓** | 几何 | Fréchet distance，衡量曲线形状与时序对齐程度 |

此外，在 **LoCoMo** 基准上评估记忆检索能力，使用 **LLM-as-a-Judge** 判断答案正确性。

---

### 基线方法对比
#### 社会模拟基线：
- **传统 ABM**：HK (Hegselmann-Krause), RA (Deffuant), Lorenz
- **纯 LLM 方法**：SOD (Simulating Opinion Dynamics)
- **混合框架**：HiSim（当前最优）

#### 记忆架构基线：
- A-Mem, LangMem, Zep, Mem0, Mem0g

---

## 3. 主要实验结果和性能指标

### 性能加速效果（Table 2）
| 方法 | T_core (min) | T_ordi (min) | T_total (min) | Speedup |
|------|--------------|-------------|----------------|---------|
| HiSim | 316.33 | 84.13 | 401.84 | 1× |
| **GASim (Ours)** | **19.30** | **3.06** | **40.43** | **9.94×** |

- **GOM 单独带来 16.39× 加速**（核心代理阶段）
- **GMP 单独带来 27.49× 加速**（普通代理阶段）

---

### Token 消耗对比（Figure 3）
- 在 10,000 代理规模下：
  - **GASim**: ~61,771 tokens
  - **HiSim**: ~316,944 tokens (**仅为其 1/5**)
  - **全LLM非混合框架**: ~24.3M tokens (**仅为其 1/400**)

> ✅ 显著降低成本，适合长期运行的大规模模拟。

---

### 趋势对齐性能（Table 3）
在所有数据集上，GASim 在四项指标中均取得 **最优或次优** 表现：

| 方法 | ΔBias ↓ | ΔDiv ↓ | Corr. ↑ | F. ↓ |
|------|--------|--------|--------|-----|
| HiSim | 0.1069 | 0.0167 | -0.003 | 0.1622 |
| **GASim** | **0.0700** | **0.0074** | **0.4261** | **0.1349** |

- **平均 ΔDiv 下降 29.05%**
- **平均 Corr. 提升 26.89%**
- **F. 最低** → 更好保持真实舆论曲线的形态与时序

> 🔍 可视化显示 GASim 成功捕捉长期趋势演变，而其他方法易陷入震荡或极端偏移。

---

### 记忆检索性能（Table 4）
在 LoCoMo 基准上的总体准确率：
| 方法 | Overall Accuracy (%) |
|------|------------------------|
| Mem0 | 66.80 |
| Mem0g | 68.44 |
| **GOM (Ours)** | **71.56** ✅ |

尤其在 **Single-Hop**, **Multi-Hop**, **Temporal** 问答上领先约 **10%**，表明其图结构能有效支持跨轮次、时间敏感的信息整合。

---

### 消融实验结果（Table 5）
在 Politics 数据集上的消融研究验证各模块贡献：

| 方法 | ΔBias | ΔDiv | Corr. | F. |
|------|------|------|------|-----|
| Full GASim | **0.0700** | **0.0074** | **0.4261** | **0.1349** |
| w/o GOM | 0.0771 (+10%) | 0.0089 (+20%) | 0.2942 (-30.96%) | 0.1406 |
| w/o GMP | 0.1027 (+46.7%) | 0.1346 (+1717%) | -0.0989 | 0.2291 |
| w/o EDG | 0.0872 (+24.6%) | 0.0109 (+47.3%) | 0.2528 | 0.1391 |

> 📌 结论：**GMP 对性能影响最大**，其次是 GOM 和 EDG；三者协同作用不可替代。

---

## 4. 关键结论和发现

### 主要发现
1. **图结构是加速社会模拟的关键**：  
   - GOM 用图传播替代 LLM 检索，实现高效且准确的记忆访问。
   - GMP 利用 GAT 实现并行观点更新，突破 ABM 顺序瓶颈。

2. **动态分组机制更符合现实社会动力学**：  
   - EDG 基于信息熵识别“信息枢纽”，比静态度数更能反映意见领袖的涌现特性。
   - 实证分析显示 EDG 选出的核心代理有 **94.1% 处于 top 20% in-degree 区间**（见 Appendix A.3），说明其有效性。

3. **混合范式 + 图加速 = 高效与保真兼得**：  
   - 不仅速度快、成本低，还能更好拟合真实舆论趋势，尤其是在长期演化中表现出更强鲁棒性。

---

### 局限性
1. **LLM 生成文本缺乏真实性**：合成 opinion labels 可能继承 LLM 自身偏见。
2. **忽略多模态信息**：当前仅处理文本交互，未考虑图像、视频等在舆论传播中的重要作用。

---

### 未来工作方向
- 引入 **multimodal LLMs** 支持图文联合推理
- 探索 **causal discovery** 机制以增强解释性
- 将 GASim 应用于政策模拟、危机预警等实际决策场景
- 开发更细粒度的 **agent heterogeneity modeling**，如情绪建模、群体极化检测

---

> 💡 **总结**：GASim 是首个将 **graph acceleration** 深度融入混合社会模拟框架的工作，通过 GOM、GMP 和 EDG 的协同设计，在效率、成本与真实性之间实现了卓越平衡，为下一代大规模社会模拟系统提供了新范式。代码已开源：[https://github.com/Jasmine0201/GASim](https://github.com/Jasmine0201/GASim)

</details>

---

### 9. [SpecBlock: Block-Iterative Speculative Decoding with Dynamic Tree Drafting](https://arxiv.org/abs/2605.07243)

**Authors**: Weijie Shi, Qiang Xu, Fan Deng, Yaguang Wu, Jiarun Liu, Yehong Xu, Hao Chen, Jia Zhu, Jiajie Xu, Xiangjun Huang, Jian Yang, Xiaofang Zhou  
**Category**: cs.CL  
**Published**: 2026-05-11  
**Score**: 10.0  
**Type**: new  
**ArXiv ID**: 2605.07243v1  

#### Abstract
Speculative decoding accelerates LLM inference by drafting a tree of candidate continuations and verifying it in one target forward. Existing drafters fall into two camps with opposite weaknesses. Autoregressive drafters such as EAGLE-3 preserve dependence along each draft path but call the drafter ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **SpecBlock: Block-Iterative Speculative Decoding with Dynamic Tree Drafting**  
**核心结论与实验结果总结**

---

## 1. **论文的主要贡献和创新点**

### **解决的问题**
大型语言模型（LLM）推理受限于内存带宽，传统的 **speculative decoding** 虽能通过小模型（drafter）预测多个候选 token 来加速，但存在两类极端方法的权衡问题：

- **Autoregressive drafters**（如 EAGLE-3）：逐层生成，路径依赖性强，接受长度高，但每层调用一次 drafter，**drafting 成本高**（占迭代延迟的 ~30%）。
- **Parallel drafters**（如 Medusa）：单次前向预测多个位置，成本低，但各位置独立预测，缺乏路径依赖，导致验证树中大量路径不连贯，**接受率低**。

本文旨在打破这一“**要么高成本高接受，要么低成本低接受**”的困境。

---

### **提出的新方法：SpecBlock**
SpecBlock 是一种 **block-iterative drafter**，结合了上述两种范式的优点：

#### **核心机制**
1. **块内依赖建模（Within-block Dependence）**
   - 每次 drafter 前向生成一个包含 `K` 个 token 的 **block**。
   - 引入 **layer-wise shift**：将前一位置的隐藏状态显式传递到每一解码器层，增强块内左到右的依赖，避免注意力稀释。

2. **跨块迭代扩展（Cross-block Iteration）**
   - 后续 block 可从先前 block 中任意位置启动，继承其隐藏状态，实现路径延续。
   - 支持多次 block 扩展，形成动态增长的验证树。

3. **动态树构建（Dynamic Tree Drafting）**
   - 引入 **co-trained rank head**：预测目标 token 在每个位置的排名（分桶），决定该位置的分支数（branching width）和是否作为后续 block 的起点。
   - 实现 **per-position 动态分配验证预算**，而非固定拓扑。

4. **训练策略优化**
   - **Valid-prefix Curriculum Learning**：一旦 block 内某位置预测错误，后续位置的损失被屏蔽，防止在错误上下文中训练，提升训练效率。

5. **部署时自适应更新**
   - **Cost-aware serving-time adaptation**：基于验证器反馈的信号（目标 token 是否被 drafter 预测到），由一个 bandit 决策是否更新 drafter，并选择更新范围（仅输出头 or 全模型），确保更新带来的吞吐增益大于更新成本。

---

### **相比现有方法的优势**
- **高效且准确**：在保持较高接受长度的同时，大幅降低 drafting 成本。
- **动态适应性**：支持在线轻量级更新，应对分布偏移。
- **优于 EAGLE-3 和 Parallel 方法**：在速度和成本之间取得更优平衡。

---

## 2. **核心实验方法和设置**

### **使用的数据集**
- **训练数据**：
  - `UltraChat-200K` 和 `ShareGPT`，用于生成与目标模型一致的训练样本。
- **评估基准**（覆盖多任务场景）：
  - **对话**：MT-Bench
  - **代码**：HumanEval
  - **数学竞赛**：MATH-500
  - **指令遵循**：Alpaca
  - **问答**：Natural Questions (NQ)
  - **翻译**：WMT-23

---

### **实验设置与评估指标**
- **目标模型**：
  - `Llama-3.1-8B-Instruct`
  - `Qwen3-8B`
  - `Qwen3-32B`
- **硬件**：单张 NVIDIA A100-80GB GPU，batch size = 1。
- **参数配置**：
  - `K = 4`（每 block 4 个 token）
  - `M = 2`（最多 2 个 block，最大深度 8）
  - drafter 为 2 层 Transformer 解码器。

#### **评估指标**
| 指标 | 含义 |
|------|------|
| **Speedup (Spd)** | 相比 vanilla autoregressive decoding 的加速比 |
| **Throughput (tokens/s)** | 每秒处理 token 数 |
| **Accepted Length (T)** | 每次验证平均接受的 token 数 |
| **Drafting Cost (TD%)** | drafter 占每次迭代延迟的百分比 |

---

### **基线方法对比**
| 方法 | 类型 | 特点 |
|------|------|------|
| **SpS** | 标准 speculative sampling | 使用小型预训练模型 |
| **Medusa** | Parallel drafter | 多头并行预测 |
| **ParallelSpec** | Parallel drafter | MASK token + 分组因果掩码 |
| **Falcon** | Blockwise drafter | 半自回归块，静态树 |
| **EAGLE-3** | Autoregressive drafter | 当前最优，逐层生成 |
| **SpecBlock+OSD** | Online adaptation | 基于 OSD 的全量更新 baseline |

---

## 3. **主要实验结果和性能指标**

### **关键性能数据（来自 Table 1）**
在 `Llama-3.1-8B` 上，`T=0` 时：

| 方法 | Speedup (Spd) | Accepted Length (T) | Drafting Cost (TD%) |
|------|---------------|---------------------|---------------------|
| **EAGLE-3** | 3.59× | 5.89 | 31% |
| **SpecBlock** | **3.92×** | 4.41 | **16%** |
| **SpecBlock+adapt** | **4.23×** | 4.54 | 15% |

> ✅ **SpecBlock 相比 EAGLE-3**：
> - **平均加速提升 8–13%**
> - **drafting 成本降至 EAGLE-3 的 44–52%**
> - **cost-aware adaptation 进一步提升至 11–19%**

在 `Qwen3-32B` 上，SpecBlock 的 drafting 成本优势更明显（11% vs 24%），表明其在大模型上更具可扩展性。

---

### **消融实验结果（Table 2）**
在 `Llama-3.1-8B` 上进行 ablation study：

| 移除组件 | Speedup (Spd) | Accepted Length (T) | 影响说明 |
|---------|---------------|---------------------|----------|
| **完整 SpecBlock** | 3.21× | 4.41 | 基线 |
| **- layer-wise shift** | 2.95× | 4.02 | 最大影响，块内依赖断裂 |
| **- prefix broadcast** | 2.99× | 4.13 | 位置锚定能力下降 |
| **- valid-prefix mask** | 3.06× | 4.23 | 错误前缀干扰训练 |
| **- rank-guided branching** | 3.13× | 4.25 | 固定分支浪费预算 |

> ✅ **layer-wise shift 贡献最大**，是保持高接受长度的关键。

---

### **自适应更新效果**
| 方法 | Speedup | T | 说明 |
|------|--------|----|------|
| **SpecBlock+adapt** | 3.24× | 4.54 | 动态选择更新 |
| **- cost-aware bandit** | 3.14× | 4.54 | 总是更新，成本更高 |
| **- head-only action** | 3.00× | 4.58 | 强制全量更新，收益低 |

> ✅ **cost-aware bandit** 通过跳过弱信号和优先执行 head-only 更新，显著降低成本，同时保持高吞吐。

---

## 4. **关键结论和发现**

### **主要发现**
1. **SpecBlock 实现了 drafting 效率与接受长度的最佳平衡**：
   - 通过 **block-iterative** 设计，以极低的 drafter 调用次数（2 次 vs EAGLE-3 的 7 次）实现接近的接受长度。
2. **layer-wise shift 是保持块内依赖的核心**：
   - 显式状态传递比纯注意力更能维持长距离一致性。
3. **rank head 实现了动态预算分配**：
   - 不确定位置多分支，确定位置少分支，提升验证效率。
4. **cost-aware adaptation 显著提升长期性能**：
   - 在分布偏移场景下，通过轻量级更新恢复接受长度，且不牺牲实时性。

---

### **方法的局限性**
1. **rank head 的预测精度有限**：
   - 当前四分桶分类器仍有 ~10–15% 的误判，导致部分位置分支过多或过少。
2. **块大小 K 固定**：
   - `K=4` 在训练时确定，无法在推理时调整，限制了灵活性。
3. **对短任务收益有限**：
   - 如 HumanEval 和 MT-Bench，因流量不足，自适应更新难以收敛。

---

### **未来工作方向**
1. **更精细的 rank prediction**：
   - 使用连续值或更多分桶，提升预算分配精度。
2. **动态块大小支持**：
   - 探索可变 `K` 或条件扩展机制。
3. **跨任务迁移学习**：
   - 构建通用 drafter，减少对特定领域微调的依赖。
4. **硬件协同优化**：
   - 结合 CUDA 流调度、内存复用等技术进一步压缩延迟。

---

> **总结**：  
> **SpecBlock** 通过 **block-iterative drafting + layer-wise shift + rank-guided tree + cost-aware adaptation**，在 **保持高接受长度的同时，将 drafting 成本降低一半以上**，是 speculative decoding 领域的重要进展。其设计思想对 LLM 推理系统优化具有广泛指导意义。

</details>

---

### 10. [Target-Aware Data Augmentation for SAT Prediction](https://arxiv.org/abs/2605.06931)

**Authors**: Eshed Gal, Uri Ascher, Eldad Haber  
**Category**: cs.LG  
**Published**: 2026-05-11  
**Score**: 10.0  
**Type**: new  
**ArXiv ID**: 2605.06931v1  

#### Abstract
Learning-based approaches to NP-hard problems have shown increasing promise, but their progress is fundamentally constrained by the high cost of generating labeled training data. In domains such as Boolean satisfiability (SAT), standard pipelines rely on solver-in-the-loop labeling, which scales poo...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：Target-Aware Data Augmentation for SAT Prediction**

---

## **1. 论文的主要贡献和创新点**

### **解决的问题**
- **NP-hard 问题中的数据瓶颈**：在 Boolean Satisfiability (SAT) 等组合优化任务中，传统机器学习依赖 **solver-in-the-loop labeling**（即生成公式后调用 SAT 求解器标注 SAT/UNSAT），该过程随着实例规模增大呈指数级增长，严重限制了训练数据的可扩展性。
- **合成数据的质量问题**：已有生成方法（如随机生成、planted-SAT）虽避免求解器调用，但生成的数据分布与真实基准（benchmark）不一致，导致下游模型泛化能力差。

### **提出的新方法与新思路**
- **Target-Aware, Solver-Free 数据生成框架**：
  - **无需调用 SAT 求解器**：通过“逆向构造”方式，先设计满足/矛盾的“证书”（certificate），再生成符合该证书的 CNF 公式，从而**保证标签正确性**。
    - **SAT 实例**：先采样一个满足赋值 $ x^* $，然后围绕 $ x^* $ 构造子句，确保每个子句至少有一个文字为真。
    - **UNSAT 实例**：嵌入一个由 $ w $ 个变量构成的完全极小矛盾核（所有 $ 2^w $ 种极性组合均出现），再添加与目标分布对齐的“填充子句”。
  - **目标感知（Target-Aware）**：生成过程中匹配目标 benchmark 的统计特性（如子句宽度分布、变量出现频率、**slack 分布**），使合成数据更贴近真实任务分布。
- **Linear-Programming-aware GNN (LPGNN)**：
  - 将 CNF 转换为 binary linear feasibility problem $ Ax \geq b $，引入 slack 变量得到等价系统 $ Az = b $。
  - 在 GNN 中注入 **LP residual** $ r^{(l)} = A z^{(l)} - b $，并通过 $ A^\top r^{(l)} $ 将约束违反信号反向传播到节点空间，增强模型对代数可行性的感知。

### **相比现有方法的优势**
| 维度 | 传统方法 | 本文方法 |
|------|--------|---------|
| **数据生成效率** | 依赖求解器，时间随规模指数增长 | **构造即标签**，复杂度 $ O(mk) $，近线性 |
| **数据质量** | 随机生成或简单种植，分布失配 | **目标对齐**，保留 benchmark 结构特性 |
| **模型架构** | 通用 GNN（如 GIN） | **优化感知**，显式利用 LP 残差信号 |
| **可扩展性** | 受限于求解器速度 | 支持大规模、高通量数据生成 |

---

## **2. 核心实验方法和设置**

### **使用的数据集**
- **主数据集**：**G4SATBench** [Li et al., 2024]
  - 包含 Easy、Medium、Hard 三个难度级别的 3-SAT 实例。
  - 每类训练集 1600 实例，测试集 200 实例。
  - clause-to-variable ratio $ \alpha \approx 4.27 $，接近相变点（phase transition）。
- **OOD 评估集**：SR family（random 3-SAT-like instances）用于跨分布泛化测试。

### **实验设置与评估指标**
#### **评估任务**
- **SAT/UNSAT 分类准确率（Accuracy）**
- **Constraint Satisfaction Rate (CSR)**：对 SAT 实例，预测赋值满足的子句比例（越高越好）
- **Violated Clause Ratio ($ k/m $)**：对 UNSAT 实例，预测赋值违反的子句数占总子句数的比例（越低越好）

#### **训练策略**
- 使用生成的 synthetic data 进行训练，逐步增加训练量（从 250 到 80k 实例）。
- 模型在 G4SATBench 的 test set 上评估。

#### **基线方法对比**
- **数据生成基线**：
  - **Naive**：暴力枚举所有赋值（仅适用于小规模）
  - **CaDiCaL**：标准 generate-and-test 流程，调用求解器标注
  - **Generic data**：普通随机生成（无目标对齐）
- **模型基线**：
  - **GIN**：基础 GNN 架构（用于消融实验）
  - **NLocalSAT** [Zhang et al., 2020]
  - **QuerySAT** [Ozolins et al., 2022]

---

## **3. 主要实验结果和性能指标**

### **关键性能数据**

#### **(1) 数据生成效率（Table 1 & Figure 4）**
| 变量数 $ n $ | CaDiCaL (ms) | 本文方法 (ms) | **加速比** |
|-------------|--------------|----------------|-----------|
| 15          | 0.66         | 0.54           | 1.2×      |
| 100         | 8.98         | 3.64           | 2.5×      |
| 250         | 4,080        | 9.32           | **438×**  |
| 500         | ~$ 10^8 $   | 19.3           | **~$ 10^6 $×** |
| 1000        | ~$ 10^{16} $| 39.0           | **~$ 10^{14} $×** |

> ✅ **结论**：本文方法在大规模下实现 **orders-of-magnitude 加速**，且复杂度近线性。

#### **(2) Slack 分布对齐效果（Figure 1）**
- 生成的 SAT 和 UNSAT 实例的 **slack 分布** 与 G4SATBench 高度一致。
- 表明生成过程成功捕捉了 benchmark 的代数结构特征。

#### **(3) 模型性能随训练数据量的缩放（Figure 2, Table 2）**
- **LPGNN 在 Medium 3-SAT 上的表现**：
  | 训练量 | CSR (%) ↑ | $ k/m $ (%) ↓ |
  |-------|----------|---------------|
  | 250   | 94.4     | 6.2           |
  | 2k    | 98.2     | 2.4           |
  | 10k   | 99.0     | 1.6           |
- **跨模型验证（Table 2）**：NLocalSAT 和 QuerySAT 同样受益于 target-aware synthetic data，表明该数据具有**通用增强能力**。

#### **(4) 分类准确率提升（Figure 3）**
- 在 Easy 3-SAT 上，随着训练数据从 250 增加到 10k，分类准确率从 ~50%（随机水平）提升至 **64%**。

#### **(5) 消融实验（Table 4）**
| 模型 | Accuracy (%) | CSR (%) | $ k/m $ (%) |
|------|--------------|---------|-------------|
| GIN（无残差） | 60.5         | 93.1    | 8.2         |
| **LPGNN（完整）** | **64.0**     | **94.2**| **7.5**     |

> ✅ **结论**：**LP residual 显著提升所有指标**，验证了优化感知机制的有效性。

#### **(6) 与 Generic Data 对比（Figure 6）**
- 使用 generic synthetic data 训练时，性能始终接近随机水平。
- 使用 target-aware data 时，性能随数据量稳定上升。
> 🔍 **关键发现**：**数据分布对齐比数据量本身更重要**。

---

## **4. 关键结论和发现**

### **主要发现**
1. **数据瓶颈是制约 SAT 学习的关键因素**，而非模型容量。
2. **Solver-free + target-aware 生成策略** 可高效构建高质量 labeled data，**消除对求解器的依赖**。
3. **合成数据若与目标分布对齐**，能显著提升 GNN 的预测性能，并支持良好缩放。
4. **LPGNN 架构通过注入 LP residual**，有效利用代数可行性信号，优于纯结构化 GNN。
5. **数据与模型协同设计** 是推动 combinatorial reasoning 学习的核心范式。

### **方法的局限性（Limitations）**
- **无法复现复杂逻辑依赖**：合成数据难以模拟工业级 SAT 实例中的隐藏社区结构（hidden community structures）和精确逻辑依赖。
- **存在 synthetic-to-real gap**：尽管在 benchmark 上表现优异，但在高度结构化的现实场景中可能泛化受限。
- **过度拟合生成模式风险**：模型可能学习生成算法的规律而非真正的 hardness 特征。

### **未来工作方向**
- 扩展生成框架以建模更复杂的结构（如工业电路、密码分析实例）。
- 将 target-aware 思想推广至其他 NP-hard 问题（如 MaxSAT、MILP、TSP）。
- 探索 **self-supervised 或 weakly supervised** 学习范式，进一步降低标注成本。
- 结合生成模型与强化学习，实现闭环的 SAT solver 自我改进。

---

> 📌 **一句话总结**：  
> 本论文提出了一种 **target-aware、solver-free 的 SAT 数据生成框架** 与 **LP-aware GNN 架构**，实现了**数量级的速度提升**和**性能增益**，强调了在 NP-hard 问题中，“**数据为中心**”（data-centric）的方法与模型设计同等重要。

</details>

---

### 11. [Echo: KV-Cache-Free Associative Recall with Spectral Koopman Operators](https://arxiv.org/abs/2605.06997)

**Authors**: Anupama Sridhar, Alexander Johansen  
**Category**: cs.LG  
**Published**: 2026-05-11  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.06997v1  

#### Abstract
Long chain-of-thought reasoning and agentic tool-calling produce traces spanning tens of thousands of tokens, yet Transformer KV caches grow linearly with sequence length, creating a memory bottleneck on commodity hardware. State-space models offer constant-memory recurrence but suffer a memory clif...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Echo: KV-Cache-Free Associative Recall with Spectral Koopman Operators

---

## 1. 论文的主要贡献和创新点

### **解决了什么问题**

- **Transformer 的 KV-Cache 内存瓶颈**：在长链推理（chain-of-thought）和智能体工具调用（agentic tool-calling）等任务中，序列长度可达数万 token，而标准 Transformer 的 KV-Cache 随序列长度线性增长，在消费级硬件上造成严重内存瓶颈。
- **SSM 的“记忆悬崖”（Memory Cliff）问题**：虽然 State Space Models（如 Mamba）提供常数内存和线性推理时间，但其固定大小的递归状态导致信息压缩损失，当事实与查询之间的干扰项（distractor gap）超过一定长度时，检索准确率急剧下降。

### **提出了什么新方法或新思路**

提出 **Echo** 架构，一种无需 KV-Cache 的关联检索方案，核心是 **Spectral Koopman Attention (SKA)**，作为注意力层的即插即用替代模块。

- **将内容寻址检索重新建模为核岭回归（Kernel Ridge Regression）**：
  - 检索任务被形式化为从 key-value 序列中预测 query 对应的 value。
  - SKA 在 O(r²) 固定内存中累积 sufficient statistics（Gram 矩阵 G、协方差矩阵 M 和 C），直接求解闭式岭回归解 $ B^* = C_o G^{-1} $，无需维护 KV-Cache。

- **引入谱 Koopman 动态系统机制**：
  - 利用 Koopman 算子理论，从 key 序列中拟合一个线性动力学系统 $ A_w = L^{-1} M L^{-T} $。
  - 通过 **幂迭代滤波器（power-iterated filter）** 放大具有持久性特征（persistent modes, $ |\lambda| \approx 1 $）的绑定，抑制瞬态噪声（$ |\lambda| < 1 $），实现对长期依赖的鲁棒检索。

- **完整架构设计**：
  - **SSM 主干**：大部分层仍使用 Mamba-2 进行局部序列处理。
  - **SKA 替代注意力**：在关键位置插入 SKA 层，提供全局检索能力。
  - **Spectral Koopman MLP**：替换 SwiGLU，使用受谱约束的动力学系统，减少参数量并保持梯度流。

### **相比现有方法的优势**

| 方面 | 传统方法（SSM+Attention） | Echo (SKA) |
| :--- | :--- | :--- |
| **内存复杂度** | KV-Cache 为 O(Td)，随上下文线性增长 | 所有组件均为 O(1) 推理状态，内存恒定 |
| **检索能力** | 依赖 Attention，存在内存瓶颈 | 完全消除 KV-Cache，同时解决 SSM 的 memory cliff |
| **计算效率** | Attention 推理为 O(T²d) | SKA 训练为 O(Tr²/S + r³)，推理为 O(r³)，远低于 Attention |
| **梯度传播** | Softmax Attention 存在熵相关的有效秩瓶颈 | SKA 的 Jacobian 为满秩，梯度流更稳定，训练更高效 |

---

## 2. 核心实验方法和设置

### **使用的数据集**

1. **Multi-Query Associative Recall (MQAR)**：合成基准，测试模型在多个 key-value 对和不同干扰项长度下的检索能力。
2. **合成迁移任务（Synthetic Transfer Experiments）**：
   - **Needle-in-a-Haystack (NIAH)**：在长文本中定位单个事实。
   - **Tool-Trace Retrieval**：从工具调用历史中检索结果。
   - **Multi-hop Composition**：多跳推理。
   - **System Prompt Recall**：跨长距离回忆系统提示。
   - **Common Word Identification**：识别高频词。
3. **语言建模基准（180M 规模）**：
   - **FineWeb-Edu**：用于从头训练。
   - **WikiText-103**：困惑度评估。
   - **零样本评测套件**：HellaSwag, PIQA, ARC-Easy/Challenge, WinoGrande, LAMBADA。

### **实验设置和评估指标**

- **模型规模**：
  - **小规模**：~1M 参数，用于控制变量和消融研究。
  - **中等规模**：50M 参数，用于 MQAR 微调。
  - **大规模**：180M 参数，用于从头语言建模训练。
- **评估指标**：
  - **检索任务**：准确率（Accuracy）。
  - **语言建模**：困惑度（Perplexity）、零样本准确率。
  - **内存**：峰值生成内存，验证 O(1) 推理状态。

### **基线方法对比**

- **Pure SSM (Mamba-2)**：仅使用 SSM，无全局检索能力。
- **SSM + Attention**：混合架构，部分层使用因果注意力。
- **其他 SSM 变体**：如 Mamba-3 等。

---

## 3. 主要实验结果和性能指标

### **关键性能数据**

#### **MQAR (50M 参数规模)**
- **Pure Mamba-2**：在所有配置下准确率均约为 **3%**（接近随机猜测）。
- **Mamba-2 + Attention**：在大多数配置下达到 **100%**，但在最大干扰项（4096 tokens）和少量 KV 对（M=4）时略有下降。
- **Mamba-2 + SKA (Echo)**：在**所有测试配置下均达到 100% 准确率**，包括 4096 tokens 干扰项和 32 个 KV 对。

#### **合成迁移任务（~1M 参数）**
- **平均准确率**：
  - Pure SSM：54.4%
  - SSM + Attention：76.2%
  - **SSM + SKA (Echo)**：**81.1%** （最高）
- **长度泛化（NIAH, 最长 4096 tokens）**：
  - Pure SSM：降至 **2.0%**
  - SSM + Attention：降至 **5.0%**
  - **SSM + SKA (Echo)**：仍保持 **65.1%** 的高准确率。

#### **语言建模（180M 参数）**
- 在 10B tokens 上从头训练，性能超越同规模甚至更大模型：
  - **HellaSwag**：**44.0**，超过参数量两倍的 GPT-2 345M (42.7)。
  - **LAMBADA**：**39.8**，优于 Mamba-370M (~36)。
- **数据效率**：Echo-50M（3B tokens）已能匹敌在 30 倍更多数据上训练的 Pythia-160M 和 Mamba-130M。

### **与基线方法的对比结果**

- **在检索任务上**：Echo 显著优于纯 SSM 和 SSM+Attention 混合模型，尤其是在长距离和高难度场景下。
- **在通用语言理解上**：Echo 不仅没有牺牲通用能力，反而在多个零样本基准上达到或超过了同规模的最佳模型。
- **在内存效率上**：Echo 维持 O(1) 推理内存，而 SSM+Attention 的 KV-Cache 随上下文线性膨胀。

### **消融实验结果**

- **移除前缀掩码（prefix masking）**：实验表明，即使不使用掩码策略，SKA 依然能取得高性能，证明性能增益主要来自**谱算子本身**，而非数据预处理技巧。
- **禁用幂滤波器（K=0）**：此时 SKA 退化为标准岭回归。启用 K≥1 后性能提升，证明**谱选择性滤波**对于放大持久模式、抑制噪声至关重要。
- **梯度流分析**：理论和实验证明，SKA 的 Jacobian 是满秩的，避免了 Attention 中因 softmax 导致的梯度秩瓶颈，解释了其更高的数据效率。

---

## 4. 关键结论和发现

### **主要发现**

1. **SSM 的 memory cliff 是结构性缺陷，非容量问题**：即使增大模型规模，纯 SSM 在长距离检索上也无法突破性能瓶颈。
2. **Echo 成功弥合了效率与能力的鸿沟**：通过 SKA，Echo 在**不牺牲 SSM 常数内存优势的前提下**，完全恢复了甚至超越了 Attention 的长程关联检索能力。
3. **闭式动态系统建模优于隐式优化**：相比于让 Attention 通过梯度下降隐式学习回归解，SKA 直接计算闭式解，并利用动力学系统的谱特性进行显式过滤，是一种更高效、更鲁棒的机制。
4. **架构影响数据效率**：Echo 在仅 10B tokens 上的训练效果即可媲美在 100B tokens 上训练的模型，表明其梯度传播机制更优。

### **局限性**

- **扩展性验证不足**：目前最大的实验模型为 180M 参数，尚未在十亿（Billion-scale）以上参数规模验证其有效性。
- **自然语言检索差距**：当前的合成基准具有清晰的事实/干扰项结构，而真实自然语言更模糊。需要在 RULER、BABILong 等更具挑战性的自然语言检索基准上进一步测试。
- **计算开销**：O(r³) 的 Cholesky 分解和谱归一化是当前瓶颈，尽管绝对值小，但仍有优化空间。

### **未来工作方向**

- **内核融合与近似计算**：将 Cholesky 分解和后续矩阵乘法融合到自定义 Triton 内核中，并探索近似分解以降低延迟。
- **大规模验证**：在十亿参数级别上训练和评估 Echo，验证其在大型语言模型中的潜力。
- **更复杂的自然语言任务**：在 agentic workflows、长文档问答等真实应用场景中部署和测试 Echo。
- **理论深化**：进一步探索 Koopman 算子与 in-context learning 之间更深层的联系。

</details>

---

### 12. [EnvSimBench: A Benchmark for Evaluating and Improving LLM-Based Environment Simulation](https://arxiv.org/abs/2605.07247)

**Authors**: Yi Liu, TingFeng Hui, Wei Zhang, Li Sun, Ningxin Su, Jian Wang, Sen Su  
**Category**: cs.AI  
**Published**: 2026-05-11  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.07247v1  

#### Abstract
Scalable AI agents training relies on interactive environments that faithfully simulate the consequences of agent actions. Manually crafted environments are expensive to build, brittle to extend, and fundamentally limited in diversity. A promising direction is to replace manually crafted environment...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：EnvSimBench: A Benchmark for Evaluating and Improving LLM-Based Environment Simulation

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
当前基于 LLM 的环境模拟（LLM-based environment simulation）被广泛用于训练可扩展的 AI Agent，其核心假设是 LLM 能够准确模拟环境反馈。然而，这一能力从未被系统地定义、衡量或验证。实践中，LLM 模拟常出现以下三种失败模式：
- **Hallucination**：虚构不存在的状态转移；
- **Logical Inconsistency**：响应内部字段逻辑冲突；
- **State Drift**：因缺乏持久记忆导致状态在多轮中逐渐漂移。

这些问题会污染 Agent 的奖励信号，反而增加构建成本，违背了“低成本生成环境”的初衷。

### 提出的新方法与新思路
本文提出 **EnvSimBench**，一个用于评估和改进 LLM 环境模拟能力的基准框架，并引入 **Environment Simulation Ability (EnvSim Ability)** 这一概念作为可量化的研究目标。

核心创新在于将传统的 **POMDP（Partial Observable MDP）** 设置重构为 **Fully Observable MDP**：
- 在每一步显式提供当前状态 `s`、动作 `a` 和该动作的实现代码 `code(a)`；
- 要求模型预测下一状态 `s'` 和观测输出 `o`；
- 所有标签由外部 Python 执行器程序化生成，确保无 LLM 干扰。

这种设计使得每个样本独立、可验证，从而隔离了状态追踪错误，使评估聚焦于真正的“状态转移推理”能力。

此外，作者提出了 **Constraint-Driven Simulation Pipeline**：
- 显式注入环境 Schema 和 Transition Logic；
- 使用结构化推理轨迹进行监督微调（SFT）；
- 构建专用的小型模拟模型（4B 参数），替代昂贵的大模型。

### 相比现有方法的优势
| 维度 | 传统方法 | EnvSimBench |
|------|--------|-------------|
| 可靠性 | 依赖对话历史，易累积误差 | 全可观测输入，单步独立验证 |
| 评估方式 | 依赖 LLM 判断，存在循环验证风险 | 程序化标签，客观、免 LLM |
| 成本 | 使用大模型（如 GPT-4）推理成本高 | 小模型（4B）即可超越所有前沿 LLM |
| 合成效率 | 合成成功率低 | 提升合成 yield 达 **+6.8%**，成本降低 **>90%** |

---

## 2. 核心实验方法和设置

### 数据集
- **来源**：从 **EnvScaler** 中选取 191 个工具交互式环境（tool-interactive environments）；
- **采样方式**：使用 GPT-4o-mini 作为 Agent 收集多轮执行轨迹；
- **处理流程**：
  - 提取 `(s, a, s', o)` 四元组；
  - 剔除初始无前状态的 step 0；
  - 预处理为自包含的单轮预测任务；
- **最终数据集**：**400 个样本**，覆盖 **167 个不同环境**，具有程序化真值标签。

### 评估维度（Three-Axis Stratification）
为了精细诊断性能瓶颈，样本按三个正交轴分层：
1. **Action Outcome**：动作成功与否（Success/Failure）
2. **State-Change Complexity (|△|)**：状态变更字段数
   - No-Change (`|△|=0`)
   - Simple (`|△|∈{1,2}`)
   - Medium (`|△|∈{3..6}`)
   - Difficult (`|△|∈{7..12}`)
3. **Argument Cardinality**：输入参数数量（0 vs ≥1）

同时应用 **多样性规则**：优先选择来自不同 `env_id` 的样本，避免集中在少数环境中。

### 评估指标
- **Feedback Match (FM)**：预测的 `o` 是否与真实 `o` 完全字符串匹配；
- **Config Match (CM)**：将预测的状态变更操作应用于 `s` 后是否能复现真实的 `s'`；
  - 更严格且更能反映真实推理能力。

### 基线方法对比
- **Frontier LLMs**（7 个）：
  - DeepSeek-V3.2, Qwen3.5-397B-A17B, GPT-5.4, Gemini-3.1-Pro-Preview, Claude-Sonnet-4.6, MiniMax-M2.7, GLM-5
- **Specialized Small Model**：
  - 基于 Qwen3-4B-Base 进行 Full-parameter SFT 得到的 **Full-Balance2**

---

## 3. 主要实验结果和性能指标

### 关键性能数据（Overall CM/FM）

| Model | FM (%) | CM (%) |
|-------|--------|--------|
| Qwen3.5-397B-A17B (**Best Frontier**) | 69.0 | **42.3** |
| GLM-5 (**Best FM**) | **80.5** | 41.0 |
| **Full-Balance2 (Ours)** | **79.5** | **45.3** ✅ |

👉 **结论**：仅 4B 参数的小模型通过针对性训练，在 **CM 上超越所有大模型（+3.0 pp）**，FM 接近最优水平。

---

### 核心发现：State-Change Cliff（状态变化断崖）

#### 发现描述
所有模型在 `|△| ≤ 2` 时表现尚可，但一旦需要同时更新 **≥3 个状态字段**，CM 性能急剧下降；当 `|△| ≥ 5` 时，几乎所有模型 CM 接近 **0%**。

| |△| | Average CM (Across Models) |
|-----|--------------------------|
| 0   | ~100%                    |
| 1   | 36–72%                   |
| 2   | 8–28%                    |
| 3   | ~24%                     |
| 4   | ~17%                     |
| 5   | ≤4%                      |
| ≥5  | ≈0%                      |

📌 **这是一个普遍存在的“能力断崖”，与模型规模无关** —— 即使最强的大模型也无法克服。

#### 示例分析（verify_otp, |△|=5）
- 地面真值需更新 5 个字段（跨 3 个子对象），包括运行时生成的时间戳；
- 所有模型均未能正确预测时间戳；
- 多数模型遗漏辅助字段或完全输出 `△=0`；
- GPT-5.4 是唯一预测出全部主字段值的模型，但仍因 key 错误导致 CM=0。

---

### 消融实验结果（Ablation Studies）

#### （1）训练数据组成的影响（Data Composition）
| 策略 | CM (Overall) | 特点 |
|------|--------------|------|
| Change-only | 47.5% | 在变更类上强，但在 Failure/No-change 上 FM=0% ❌ |
| Balance | 43.8% | 加入非变更样本，提升泛化 |
| **Balance2 (ours)** | **45.3%** ✅ | 按真实分布加权复杂变更样本，达到最佳 |

✅ 结论：**数据构成比总量更重要**，平衡覆盖各难度层级才能有效提升 EnvSim Ability。

#### （2）是否加入推理链（Reasoning-Augmented Traces）
- 加入结构化推理轨迹后，CM 反而下降（35.0% → 30.3%）；
- 在简单任务上造成噪声干扰；
- 在困难任务上有轻微增益（6% → 10%）；
- 推测：需更大数据量（≥20K）或条件路由机制才有效。

#### （3）参数高效微调 vs 全参微调
| 方法 | CM (Overall) | 优势 |
|------|-------------|------|
| LoRA | 31.8% | 资源节省 |
| **Full-parameter SFT** | **35.0%** ✅ | 更好保留序列推理能力，尤其在 Simple 阶段显著领先 |

---

### 下游验证：集成至 EnvScaler 合成流水线
| 指标 | 原始流水线（大模型 Ensemble） | 使用 Full-Balance2 替代 |
|------|-------------------------------|------------------------|
| 成功合成环境数 | 191 | **204** ✅（↑+6.8%） |
| 参数量级 | 数百亿～千亿 | **4B**（↓>90x） |
| 成本 | 高昂 | 极低 |

✅ 表明：**专业化小模型在实际部署中更具性价比和可靠性**。

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **EnvSim Ability 是一项独立且未被充分认识的能力**：
   - 不同于通用推理或指令遵循；
   - 本质更接近 **program execution** 而非语言生成。

2. ✅ **普遍存在 “State-Change Cliff”**：
   - 当 `|△| ≥ 3` 时，所有前沿 LLM 的 CM 急剧下降；
   - `|△| ≥ 5` 时几乎完全失效；
   - 该现象与模型大小无关，揭示了一个根本性能力缺口。

3. ✅ **FM 与 CM 存在严重脱钩（Decoupling）**：
   - 多达 **60–100% 的 CM 失败案例仍能通过 FM**；
   - 意味着 Agent 接收到正确的反馈字符串，但环境状态已静默损坏；
   - 这种“无声腐败”对训练极为危险。

4. ✅ **小型专用模型可超越大模型**：
   - 经过合理数据构造和全参微调的 4B 模型，在 CM 上超过所有大模型；
   - 成本降低 >90%，合成成功率提升 +6.8%；
   - 证明 **specialization > scale** 在此任务中成立。

---

### 局限性
1. **样本量限制**：
   - Difficult 组样本少（n≈4–6 per |△|），统计波动大；
   - 小样本下 CM 波动可达 ±25pp。

2. **训练数据与下游测试存在分布重叠**：
   - 合成质量过滤器与训练数据共享分布，存在潜在的循环验证风险。

3. **高 |△| 样本稀缺**：
   - 缺乏足够 `|△| ≥ 5` 的训练样本，难以突破“断崖”。

4. **Benchmark 设计可进一步细化**：
   - 当前 Difficult 组混杂了两种类型：
     - **异构多字段更新**（难）
     - **批量均匀操作**（相对容易，如连续日期添加）
   - 应在未来版本中分开评估。

---

### 未来工作方向
1. **构建更大规模的 EnvSimBench++**：
   - 扩展样本数量，增强统计稳健性；
   - 引入更多高复杂度、高 |△| 的场景。

2. **开发专门针对 EnvSim Ability 的预训练策略**：
   - 如在预训练阶段注入代码执行与状态变迁任务。

3. **探索动态推理控制机制**：
   - 对复杂状态变更启用更强的 reasoning 模式（如 Chain-of-Thought + Execution）；
   - 对简单任务保持轻量推理。

4. **推动语义等价匹配指标**：
   - 当前 FM 依赖精确字符串匹配，未来应引入 **semantic equivalence metrics** 来缓解格式差异带来的误判。

5. **开放平台建设**：
   - 作者已开源项目：[GitHub - cookieApril/EnvSimBench](https://github.com/cookieApril/EnvSimBench)
   - 鼓励社区共建更鲁棒、多样化的 LLM 模拟生态系统。

---

> 🔚 **总结一句话**：  
> EnvSimBench 揭示了 LLM 在环境模拟中的“阿喀琉斯之踵”——**无法可靠处理多个并发状态更新**，并提供了首个可量化、可优化的路径，标志着从“盲目信任 LLM 模拟”走向“科学诊断与工程改进”的转折点。

</details>

---

### 13. [SAGE: Hierarchical LLM-Based Literary Evaluation through Ontology-Grounded Interpretive Dimensions](https://arxiv.org/abs/2605.07102)

**Authors**: Tianyu Wang, Nianjun Zhou  
**Category**: cs.CL  
**Published**: 2026-05-11  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.07102v1  

#### Abstract
Evaluating literary quality requires assessing interpretive dimensions such as cultural representation, emotional depth, and philosophical sophistication that resist straightforward computational measurement. We introduce SAGE, a hierarchical evaluation framework that decomposes literary quality int...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：SAGE: Hierarchical LLM-Based Literary Evaluation through Ontology-Grounded Interpretive Dimensions

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
传统自然语言处理中的自动评估指标（如BLEU、ROUGE、BERTScore）主要依赖于**lexical similarity**或**embedding similarity**，适用于机器翻译、摘要等任务，但无法捕捉文学作品中深层次的**interpretive dimensions**，例如文化表征、情感心理深度和哲学思辨。这些维度是文学批评的核心，却难以通过表面文本特征衡量。

此外，当前对**LLM生成叙事文本**的质量评估缺乏理论驱动的、系统性的框架，尤其在区分模式复现能力（pattern-reproducible skills）与立场要求能力（stance-requiring skills）方面存在空白。

### 提出了什么新方法或新思路
本文提出 **SAGE**（Systematic Assessment of Generative Excellence），一个基于本体论解构的**分层文学质量评估框架**，其核心创新如下：

- **六层分层架构**（Six-layer Hierarchy）：
  - **L1–L3**：基于规则的计算指标，评估词汇质量、叙事结构和主题内容。
  - **L4–L6**：基于LLM的解释性分析，聚焦三大高阶维度：
    - **L4: Cultural Representation**（文化表征）
      - IPD: Intersectional Power Dynamics
      - CVP: Cultural Voice & Perspective
      - CSP: Cultural Specificity
      - CPC: Cultural Pattern Complexity
    - **L5: Emotional-Psychological Representation**（情感心理表征）
      - AC: Affective Complexity
      - PI: Psychological Interiority
      - EG: Emotional Granularity
      - ENC: Emotional-Narrative Coherence
    - **L6: Existential-Philosophical Representation**（存在-哲学表征）
      - LP: Life Philosophy (Weltanschauung)
      - MR: Moral Reflection (phronesis)
      - HC: Human Condition (conditio humana)
      - ME: Meaning Exploration (hermeneutica)

- **双轨评估架构**（Dual-Track Architecture）：
  - **迭代评估器**（Iterative Evaluator）：进行五轮自我反思（self-reflection），逐步修正偏见、验证证据充分性和层级边界。
  - **独立验证器**（Independent Validator）：提供交叉验证，检测幻觉（hallucination）、投影偏见（projection bias）并评估推理质量。

- **双模态评估设计**（Dual-Mode Evaluation）：
  - **Content-Limit Mode**：仅输入故事文本，测试模型从文本中直接推断解释性维度的能力。
  - **Title-Limit Mode**：仅输入标题和作者，测试模型能否综合学术共识与批评话语进行元批判评估。

### 相比现有方法的优势
| 维度 | SAGE优势 |
|------|--------|
| **理论基础** | 明确锚定于文学理论（Bourdieu, Said, Sedgwick, Heidegger等），实现“ontology-grounded”评估 |
| **可靠性** | 多轮自省+独立验证机制显著提升评估一致性（>94% inter-rater agreement） |
| **可扩展性** | 可用于大规模自动化开放文本生成评估，支持无专家标注场景 |
| **细粒度区分力** | 能够识别不同生成模型在特定维度上的系统性短板（如哲学深度不足） |

---

## 2. 核心实验方法和设置

### 使用的数据集
共评估 **100篇短篇小说**，分为三类以测试判别效度：

| 类别 | 数量 | 特征 |
|------|-----|------|
| **Canonical Literature** | 50 | 学术公认经典作品（如Kafka, Joyce, Hemingway, Borges等），涵盖多种流派与文化背景 |
| **Pulp Fiction** | 30 | 商业杂志出版的通俗小说（如Lovecraft, Burroughs），代表技术娴熟但缺乏深层批判性的叙事 |
| **LLM-Generated Stories** | 20 | 来自Hugging Face `lars76/story-evaluation-llm` 数据集，按人类评分分为高质量（n=10）、中等（n=5）、低质量（n=5）三层 |

所有文本长度控制在2,000–8,000词之间，确保形式一致。

### 实验设置和评估指标

#### 评估流程
每篇故事在两个模式下分别评估三个解释性层次（L4–L6），总计：
- **600次评估**（100 stories × 3 layers × 2 modes）
- 每次评估由**迭代评估器**完成5轮自省，并由**独立验证器**进行单轮交叉验证

#### 评估指标
| 指标 | 定义 |
|------|------|
| **Score Convergence Rate** | 第4轮到第5轮得分变化 < 0.3 的比例，反映稳定性 |
| **Inter-Rater Agreement (IRA)** | 迭代评估器与独立验证器之间的平均绝对差（MAD），阈值为 < 0.5 |
| **Effect Size (Cohen’s d)** | 不同类别间差异效应大小，用于判断判别强度 |
| **Mode Invariance** | Content-Limit 与 Title-Limit 模式下的平均得分差异，检验评估鲁棒性 |
| **Cross-Layer Correlation** | 各层得分间的Pearson/Spearman相关系数，检验维度独立性 |

#### 基线方法对比
本文未直接对比传统NLG指标（如BLEU），而是指出其在文学评价中“correlate only weakly with human judgments”。相反，SAGE的目标是超越这些表面相似性指标，构建一种**测量级可靠**（measurement-grade reliability）的解释性评估体系。

---

## 3. 主要实验结果和性能指标

### 关键性能数据

| 指标 | 结果 |
|------|------|
| **总评估成功率** | 600/600 (100%) |
| **JSON解析成功率** | 100% |
| **得分收敛率**（R4→R5） | **98.8%** |
| **独立验证者一致性**（MAD < 0.5） | **>94%** |
| **平均IIR差异** | **<0.3**（极佳一致性） |
| **模式不变性最大差异** | **|Δ| ≤ 0.05**（近乎完美） |

> ✅ 表明SAGE具有高度稳定、可重复、跨信息源一致的评估能力。

### 与基线方法的对比结果
虽然没有显式运行BLEU/BERTScore作为基线，但文中明确指出：
> “Such metrics might capture lexical patterns or sentence-level coherence but would miss the symbolic weight of transformation as alienation, the psychological complexity of Gregor's interiority, or the existential critique of modern life.”

而SAGE能够系统地区分以下三类作品：
- **Canonical > Pulp > LLM**，且所有两两比较均显著（p < 0.001）

| 层级 | Canonical | Pulp | LLM | Can vs LLM (Δ) | Cohen’s d |
|------|----------|------|-----|---------------|-----------|
| **L4: Cultural** | 3.96 | 3.83 | 2.55 | +1.41 | **2.68** |
| **L5: Emotional** | 4.15 | 4.04 | 3.36 | +0.79 | **1.68** |
| **L6: Existential** | 3.95 | 3.68 | 2.59 | +1.36 | **2.40** |
| **Overall** | 4.02 | 3.85 | 2.83 | +1.19 | —— |

> 🔺 所有d > 1.5，属于“very large effect”，说明SAGE具备强大判别力。

### 消融实验结果（隐含分析）

尽管未设正式消融实验，但通过多轮迭代机制的设计可视为一种过程性消融：

- **Round-by-Round Score Trajectories** 显示大多数维度在第3–4轮即趋于稳定，表明**多轮自省有效减少波动**。
- **独立验证器发现的偏差类型** 包括：
  - 投影偏见（projection bias）
  - 幻觉（hallucination）
  - 层级越界（layer boundary violation）
  - 推理不充分（insufficient evidence）

这反过来证明了双轨架构的必要性。

---

## 4. 关键结论和发现

### 论文的主要发现

1. **文学质量是多维且可分解的**
   - 三大解释性维度（文化、情感、存在-哲学）之间呈中等相关（Pearson r = 0.649–0.683），既非完全独立也非冗余，支持“multidimensional”观点。
   - 各维度内部也表现出正交性（orthogonality），例如：
     - Hemingway: 高AC（情感复杂）但低PI（心理内省）
     - Camus: 高LP（人生哲学）但低MR（道德反思）

2. **当前LLM生成文本在“立场性能力”上存在根本缺陷**
   - 在**情感表达**（L5）上表现尚可（d=1.68），因该维度可通过训练数据中的模式学习。
   - 但在**文化权力批判**（L4）和**哲学深度**（L6）上差距巨大（d≈2.4–2.7），表明这些需要“critical stance”、“original engagement”的能力难以通过统计模仿获得。

3. **模式不变性揭示LLM具备双重评估路径**
   - Content-Limit 与 Title-Limit 得分几乎一致（max Δ=0.05），说明LLM既能做文本分析，也能整合学术共识，二者导向相同判断。
   - 暗示LLM已将部分“critical knowledge”内化为其推理结构的一部分。

4. **情感表达是最易被AI模仿的文学品质**
   - 即使是LLM生成文本，在L5上平均得分为3.36，接近Pulp Fiction（4.04）和Canonical（4.15）水平。
   - 支持“affective patterns are more learnable from training data”这一假设。

### 方法的局限性

| 局限 | 说明 |
|------|------|
| **语言与文化单一性** | 数据集全为英语短篇小说，限制跨语言泛化能力 |
| **模型依赖性** | 全部实验基于GPT-5-mini，尚未验证是否适用于其他LLM家族 |
| **外部效度待验证** | 当前一致性为LLM-to-LLM，尚未与人类专家评分进行对比 |
| **低层未集成** | L1–L3仍为独立模块，未与L4–L6形成端到端联合评估 |
| **静态评估** | 缺乏对动态创作过程（如multi-agent协作）的评估支持 |

### 未来工作方向

1. **跨模型比较**：在不同LLM家族（如Llama、Mistral、Claude）上测试SAGE，分离框架可靠性与模型特异性行为。
2. **人类专家基准测试**：引入专业文学评论家评分，建立外部效度。
3. **多语言与多元文化扩展**：纳入非西方文学传统（如中国古典小说、非洲口头叙事）以检验理论普适性。
4. **纵向评估演进**：跟踪新一代LLM在SAGE各维度上的进步轨迹，观察“capability profile”是否改变。
5. **应用于教育与创作辅助**：将SAGE用作写作反馈工具，帮助作者识别文本在文化/哲学层面的薄弱环节。

---

> 📌 **一句话总结**：  
> SAGE首次实现了**理论驱动、高信度、可扩展**的LLM-based文学质量评估，揭示了当前AI叙事在**文化批判与哲学深度**上的系统性短板，为下一代生成模型的发展提供了精准诊断路径。

</details>

---

### 14. [A Flexible Adaptive Stable Clustering Algorithm for Archive-Scale Online Mass Spectrometry](https://arxiv.org/abs/2605.07424)

**Authors**: Shao Shi, Xin Yang, Huiran Feng, Jianhuai Ye, Tianlong Hu, Yaling Zeng, Tzung-May Fu, Lei Zhu, Huizhong Shen, Chen Wang, Shu Tao  
**Category**: cs.LG  
**Published**: 2026-05-11  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.07424v1  

#### Abstract
Modern online mass spectrometry generates multi-terabyte data streams critical for understanding Earth's environmental systems. However, extracting actionable chemical insights from these repositories is impeded by a computational bottleneck: existing clustering methods force a compromise among scal...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文核心结论与实验结果总结  
**论文标题**: *A Flexible Adaptive Stable Clustering Algorithm for Archive-Scale Online Mass Spectrometry*

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
现代在线质谱技术（如 AMS、CIMS、SPMS）能够以亚秒级频率采集大气气溶胶的化学组成，产生多太字节（multi-terabyte）级别的连续数据流。然而，从这些海量、未标注、高度混合的光谱中提取可操作的化学洞察面临三大瓶颈：

- **Scalability（可扩展性）**：传统聚类算法（如层次聚类、谱聚类）具有 $O(N^2)$ 或更高复杂度，无法处理千万量级的数据。
- **Flexibility（灵活性）**：多数算法依赖特定距离度量（如欧氏距离），难以适配环境质谱特有的双极性（positive/negative ion）、非欧式流形结构。
- **Stability（稳定性）**：基于启发式的算法（如 ART-2A）对输入顺序敏感，导致“算法融合”（algorithmic blending）——不同化学类别边界重叠，产生计算伪影。

这三者共同构成了一个“算法四难困境”（algorithmic quadrilemma），限制了对大气老化路径和超稀有排放源的自动识别。

### 提出了什么新方法或新思路
作者提出 **Flexible Adaptive Stable Clustering (FASC)**，一种基于动力系统理论的新型无监督聚类框架，其核心创新包括：

- **架构解耦设计**：将相似性核函数（similarity kernel）与优化逻辑分离，使算法支持任意对称有界核函数（metric-agnostic），实现真正的灵活性。
- **密度增强相似性选择规则（DASS）**：在分配阶段引入局部密度项 $\lambda \phi(n_j)$ 到决策函数中，优先保留高密度化学流形，防止过度分割。
- **双阈值动态约束机制**：
  - `Tintra`：保证簇内紧凑性（angular compactness）
  - `Tinter`：强制簇间分离，避免边界重叠
- **Lyapunov引导的块坐标优化**：确保算法收敛到确定性的固定点或有界极限环，实现**顺序无关**（permutation-invariant）的稳定输出。

### 相比现有方法的优势
| 维度 | FASC | 传统方法（如 K-means, ART-2A, DBSCAN） |
|------|------|----------------------------------------|
| **Scalability** | 严格线性时间 $O(N)$ 和内存 $O(N)$ | 多为 $O(N^2)$ 或更差 |
| **Flexibility** | 支持任意相似性核（如 dual-cosine） | 限于 Bregman divergence 或特定哈希 |
| **Adaptivity** | 自主发现异构结构，无需预设簇数 | 需指定 $K$ 或全局 $\epsilon$ 参数 |
| **Stability** | 确定性收敛，抗输入顺序扰动 | 易受初始化/顺序影响，存在算法融合 |

FASC 是首个同时满足 **FAS**（Flexibility, Adaptivity, Stability）三项高标准且具备线性可扩展性的聚类算法。

---

## 2. 核心实验方法和设置

### 使用了哪些数据集
1. **MNIST 手写数字数据库** ($N=70,000$, $D=784$)  
   - 用于量化验证：提供绝对 ground truth（0–9 类），测试算法在高维空间中识别连续流形的能力。
   
2. **25 million 单粒子质谱数据集（SPMS）**  
   - 来自深圳南方科技大学 2021 年 4 月采集的真实大气颗粒物数据（共 12,371,204 个粒子，每个含正负双极性 TOF 谱）
   - 特征维度 $D \sim 600$，经峰提取、归一化后构建稀疏向量
   - 用于真实场景下的大规模挖掘与拓扑分析

### 实验设置和评估指标

#### 评估策略采用三级验证体系：
1. **Quantitative Ground-Truth Benchmarking**（基于 MNIST）
   - 指标：
     - **Cluster Purity**（分类准确率）
     - **Adjusted Rand Index (ARI)**：校正随机匹配后的聚类一致性
     - **Normalized Mutual Information (NMI)**：衡量分布间统计依赖
   - 设置：允许 $K_{\text{max}} = 1000$，远大于真实类别数（10），检验抗过分割能力

2. **Topological Validation of Ambient Data**（基于 SPMS）
   - 使用 **t-SNE** 和 **UMAP** 进行低维嵌入可视化
   - 嵌入完全独立于聚类过程（unsupervised embedding），仅用于后验叠加标签验证连续性
   - 测试嵌入在 wide-ranging hyperparameters 下的鲁棒性（如 perplexity 15–3000）

3. **Algorithmic Separation Analysis**
   - 构建簇间相似性热图，检测是否出现跨阈值的“blending pairs”
   - 对比 FASC 与 ART-2A 在相同预算下的边界分离情况

#### 基线方法对比
- **Prototype-based**: K-means, Mini-Batch K-means
- **Density-based**: DBSCAN, HDBSCAN
- **Graph-based**: Affinity Propagation, Spectral Clustering
- **Specialized MS tools**: Falcon, msCRUSH
- **Legacy atmospheric standard**: ART-2A

---

## 3. 主要实验结果和性能指标

### 关键性能数据

| 指标 | 结果 |
|------|------|
| **Runtime Scaling** | 实证运行时间随 $N$ 严格线性增长（$R^2 > 0.99$） |
| **Memory Footprint** | 峰值内存 ~247 GB，呈线性增长，适用于标准 HPC 节点 |
| **Throughput** | > 4,500 spectra/sec（单线程主导下）；完整 25M 数据仅需 **1.5 小时** |
| **Convergence Speed** | 41 次迭代即达稳定状态；前 16 次迭代去除 >80% 异常值 |

### 与基线方法的对比结果

#### 在 MNIST 上的表现（$K_{\text{max}}=1000$, cosine kernel）
| 方法 | Cluster Purity | ARI | NMI |
|------|----------------|-----|-----|
| **FASC (T=0.9)** | **99.51%** | **0.9975** | **0.9881** |
| K-means ($K=10$) | 60.37% | 0.4426 | 0.5375 |
| K-means ($K=1000$) | 95.41% | 0.9029 | 0.8902 |

> ✅ FASC 在相同容量下显著优于 K-means，证明 DASS 规则有效抑制了碎片化。

#### 在 SPMS 数据上的表现
- 成功解析出 **Secondary Inorganic Aerosol (SIA) backbone**：
  - 占总谱数 **52.7%**（主要分布在 Clusters 1, 19, 23）
  - 揭示从硝酸盐丰富交通混合物 → 高度氧化有机硫酸盐的连续老化梯度
- 同时识别出超稀有排放源（<0.2% abundance）：
  - 工业锌富集羽流（Cluster 34）
  - 钒/VO⁺标记的残余油燃烧信号（Cluster 13, 1.25%）

#### 算法融合（Algorithmic Blending）对比（见 Fig. 4）
- **ART-2A**：存在大量红色热点，表明多个簇中心落入彼此接受区域（violence < 0.8），形成虚假连接网络
- **FASC**：所有簇间相似性均低于 $T_{\text{inter}}=0.8$，实现数学上严格的分离

### 消融实验结果（隐含分析）
- **阈值调节实验**（Fig. S10–S11）：
  - 当 $T = 0.7$：最大化召回率，揭示连续混合态（如 K-rich 涂层硫酸盐，占 22.2%）
  - 当 $T ≥ 0.9$：触发“拓扑相变”，将连续流形分裂为离散“群岛”，用于提取纯净 tracer
- **容量预算实验**：
  - 即使 $K_{\text{max}} = 1000$，FASC 也未产生冗余簇，说明 DASS 具备内在密度过滤功能

---

## 4. 关键结论和发现

### 论文的主要发现
1. **FASC 实现了 FAS 三角平衡**：
   - 首次在一个算法中统一了 **灵活性、适应性和稳定性**，突破了传统聚类方法必须妥协的设计范式。

2. **动力系统框架保障确定性收敛**：
   - 通过 Lyapunov 函数驱动和块坐标更新，消除顺序依赖，彻底解决 ART 类算法长期存在的“算法融合”问题。

3. **双阈值机制是内部有效性保障**：
   - $T_{\text{intra}}, T_{\text{inter}}$ 不仅是参数，更是**先验几何约束**，直接编码了簇内紧致、簇间分离的物理期望。

4. **可在同一数据集中同步解析宏观演化路径与微观稀有信号**：
   - “SIA backbone” 代表主流大气老化过程
   - “ultra-rare tracers”（如工业 Cu/Zn 粒子）被精准分离，丰度低至 **<0.2%**

5. **具备真正的 archive-scale 处理能力**：
   - 在标准 HPC 上完成 25M 光谱聚类仅需 **1.5 小时**，为未来城市尺度环境监测提供了可行基础设施。

### 方法的局限性
- **依赖合理定义的相似性核**：虽然支持任意核函数，但最终效果仍取决于领域专家能否设计出反映化学意义的度量（如 dual-cosine）。
- **批处理架构限制实时性**：当前版本为 batched streaming，尚不支持完全在线增量学习。
- **Fréchet mean 计算成本较高**：对于非常规度量空间，求解广义质心可能较慢（尽管总体仍保持线性趋势）。

### 未来工作方向
- 开发原生 Python/C++ 实现以进一步提升效率
- 探索与 deep representation learning 结合（如用 autoencoder 提取 latent features 后再聚类）
- 将 FASC 应用于其他高通量传感器数据（如 single-cell metabolomics, remote sensing）
- 构建自动化 pipeline，实现从 raw spectra → cluster atlas → 化学注释的端到端分析平台

---

> 📌 **一句话总结**：FASC 通过将动力系统理论引入大规模质谱数据分析，首次实现了兼具 **线性可扩展性、度量灵活性、结构自适应性和数学稳定性** 的聚类框架，为环境大数据挖掘提供了坚实可靠的数字基础设施。

</details>

---

### 15. [Weblica: Scalable and Reproducible Training Environments for Visual Web Agents](https://arxiv.org/abs/2605.06761)

**Authors**: O\u{g}uzhan Fatih Kar, Roman Bachmann, Yuanzheng Gong, Anders Boesen Lindbo Larsen, Afshin Dehghan  
**Category**: cs.AI  
**Published**: 2026-05-11  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.06761v1  

#### Abstract
The web is complex, open-ended, and constantly changing, making it challenging to scale training data for visual web agents. Existing data collection attempts remain limited to offline trajectories for supervised fine-tuning or a handful of simulated environments for RL training, thus failing to cap...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：WEBLICA: Scalable and Reproducible Training Environments for Visual Web Agents

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
现有的视觉 Web Agent 训练面临以下挑战：
- **训练数据难以规模化**：基于真实网站的离线轨迹（offline trajectories）缺乏交互性，无法支持强化学习（RL）所需的探索与试错。
- **模拟环境泛化能力差**：现有的合成环境（如 WebArena）仅覆盖少数人工定义的领域，无法反映真实 Web 的多样性。
- **在线训练不稳定**：直接在 live web 上训练易受超时、bot detection 和页面动态变化影响，导致训练不可复现。

### 提出了什么新方法或新思路
本文提出 **WEBLICA**（Web Replica），一个用于构建可扩展且可复现的视觉 Web Agent 训练环境的框架，包含两个互补机制：

1. **HTTP-level Caching（WEBLICA-CACHE）**
   - 在 HTTP 层级记录并回放真实网站的浏览会话。
   - 自动识别并过滤 volatile parameters（如时间戳、session token），实现确定性的网络隔离回放。
   - 保留真实网站的视觉状态和交互行为，同时避免 live web 的不稳定性。

2. **LLM-based Environment Synthesis（WEBLICA-SYNTH）**
   - 利用 LLM（Claude Code）自动生成具有特定导航能力、网站类别和视觉风格的交互式网页。
   - 支持按需生成多样化任务（如表单填写、日期选择、地图交互等），覆盖更广泛的 Web 导航技能。
   - 所有环境本地部署，极大提升训练速度（action-to-screenshot 时间缩短至 50–150ms）。

### 相比现有方法的优势
| 维度 | 传统方法 | WEBLICA |
|------|--------|---------|
| **真实性** | 合成环境存在 sim-to-real gap | 缓存真实网站 + LLM 接地于现实模式 |
| **多样性** | 覆盖有限 domain | 千级 domain、百种视觉风格 |
| **可复现性** | Live web 不可复现 | 完全离线、网络隔离 |
| **训练效率** | 受限于网络延迟 | 本地服务 + 动画跳过，提速 30–40% |
| **支持 RL** | 多为 SFT 数据 | 支持大规模 RL 训练 |

---

## 2. 核心实验方法和设置

### 使用的数据集
- **WEBLICA-CACHE**：基于 InstaV3 数据集中的任务，在 146K 真实网站上进行 HTTP 缓存，最终保留 **15.6K 可解任务**。
- **WEBLICA-SYNTH**：通过 LLM 自动生成：
  - **310 个高阶能力站点**（如 form input, date selection）
  - **2500 个细粒度能力站点**（共 144 类 capability groups）
  - 总计 **44,227 个训练任务** 和 **500 个验证任务（WEBLICA-val）**

### 实验设置和评估指标
- **模型架构**：基于 Qwen3-VL 系列 VLM，输入为原始截图（1280×720），输出为坐标动作（coordinate-based actions），无需 set-of-marks 或 DOM 访问。
- **训练流程**：
  1. **SFT Warm-Start**：使用 LLM-judge 过滤出的 51.7K 成功轨迹进行监督微调。
  2. **RL Training**：采用 Dr. GRPO 算法，结合 **LLM-as-Judge Reward**（GPT-4o 判断任务是否完成）。
- **评估方式**：
  - **Pass@k**：运行 k 次独立尝试，报告成功概率（总步数 = k × max_steps）。
  - **测试时计算扩展性分析**：比较不同 `k`（1, 2, 4, 8）下的性能提升。
  - **消融实验**：分析 SFT、RL、环境类型的影响。

### 基线方法对比
| 类型 | 基线模型 |
|------|--------|
| **API-only** | OpenAI CUA, Gemini CUA, Yutori Navigator |
| **Open-weight** | Qwen3-VL-Instruct-8B, UI-TARS-1.5-7B, GLM-4.1V-9B-Thinking, Fara-7B, MolmoWeb-8B |

---

## 3. 主要实验结果和性能指标

### 关键性能数据（Table 1）

| Model | Total Steps | Online-Mind2Web | DeepShop | WebTailBench | Avg. | WEBLICA-val |
|-------|-------------|------------------|----------|---------------|------|--------------|
| Qwen3-VL-Instruct-8B | 30 | 28.6 | 24.1 | 21.8 | 24.8 | 56.9 |
| MolmoWeb-8B | ≥100 | 35.3 | 42.3 | 49.5 | 42.4 | — |
| **WEBLICA-8B (k=1)** | **30** | **39.2** | **34.2** | **33.5** | **35.6** | **70.6** |
| **WEBLICA-8B (k=2)** | **60** | **50.3** | **45.4** | **47.0** | **47.6** | **79.0** |
| **WEBLICA-8B (k=4)** | **120** | **60.5** | **55.9** | **60.3** | **58.9** | **84.7** |
| **WEBLICA-8B (k=8)** | **240** | **68.8** | **65.8** | **72.2** | **68.9** | **88.6** |

> 注：所有 pass@k 结果均使用相同策略重复 k 次，而非 selective retry。

### 与基线方法的对比结果
- **超越同规模开源模型**：
  - 在仅 **30 步**下，WEBLICA-8B 平均得分 **35.6%**，超过 MolmoWeb-8B（42.4%）所需步数的 3 倍以上。
  - 在 **60 步**即反超其平均表现（47.6% vs 42.4%）。
- **媲美闭源 API 模型**：
  - 以 **120 步**达到 **58.9%**，接近 Gemini CUA（60.8%）；
  - 以 **240 步**达 **68.9%**，已优于 OpenAI CUA（36.2% @100步）近一倍。

### 消融实验结果（Figure 4b & Figure 5）

#### 环境类型消融（Figure 4b）
- **Synth-only** 在大多数基准上优于 **Cache-only**：
  - Online-Mind2Web: 39.2% vs 35.3%
  - WebTailBench: 33.5% vs 30.2%
- 表明 LLM 合成环境能有效捕捉通用导航模式，并提供更强泛化能力。

#### 训练阶段消融（Figure 5）
- **SFT + RL** 组合效果最佳，在所有模型尺寸下均显著优于单独阶段。
- 小模型（2B）对 SFT 初始化依赖更强；大模型（8B）仍受益于 SFT，但边际收益递减。

#### 视觉定位能力保持（Table 2）
| Model | MMBench-GUI | ScreenSpot-v2 | ScreenSpot-Pro |
|-------|-------------|----------------|----------------|
| Qwen3-VL-Instruct-8B | 82.85 | 93.95 | 54.71 |
| **WEBLICA-8B** | **83.74** | **94.50** | **55.28** |

> 表明训练后视觉 grounding 能力未退化，甚至略有提升，说明性能增益来自导航策略优化而非感知增强。

---

## 4. 关键结论和发现

### 主要发现
1. **可复现的大规模 RL 训练是可行的**：通过 HTTP 缓存 + LLM 合成，可在完全离线环境中训练视觉 Web Agent。
2. **合成环境可有效驱动泛化**：尽管存在 sim-to-real gap，但 LLM 生成的多样化任务足以让模型学到通用导航策略。
3. **RL 显著释放推理潜力**：相比 base model，RL 训练使模型能更有效地利用额外测试时计算（更多步骤/尝试）。
4. **无需 DOM 或辅助标注也能高性能**：纯基于截图和坐标动作的设计不影响最终性能，反而增强泛化性。

### 方法的局限性
- **缓存环境静态化**：无法反映网站随时间的变化，也无法处理需要实时更新的内容（如新闻、股票）。
- **合成环境保真度限制**：虽覆盖主流交互模式，但在复杂 JS 行为、动画逻辑等方面仍有差距。
- **单轮任务设定**：当前任务均为一次性目标，未涉及多轮对话、用户反馈修正或个性化记忆。
- **依赖强 LLM 工具链**：环境生成依赖 Claude Opus 等高级 coding agent，成本较高。

### 未来工作方向
- 构建动态更新的缓存机制，支持“版本化”网页快照。
- 引入更强的 generative model 提升合成网站的真实性和复杂度。
- 扩展到 multi-turn、human-in-the-loop 的交互范式。
- 探索 long-horizon RL 和 error recovery 轨迹注入。
- 将框架推广至 Mobile 和 Desktop GUI 环境，迈向通用 Computer Use Agent。

--- 

> **总结一句话**：  
> WEBLICA 成功构建了一个**可扩展、可复现、高效**的视觉 Web Agent 训练基础设施，使得在数千个多样化环境中进行 RL 训练成为可能，其训练出的 **WEBLICA-8B** 模型在多项 benchmark 上超越同类开源模型，并逼近闭源 API 模型表现。

</details>

---

### 16. [Efficient Data Selection for Multimodal Models via Incremental Optimization Utility](https://arxiv.org/abs/2605.07488)

**Authors**: Jinhao Jing, Qiannian Zhao, Chao Huang, Zhan Su  
**Category**: cs.AI  
**Published**: 2026-05-11  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.07488v1  

#### Abstract
The scaling of Large Multimodal Models (LMMs) is constrained by the quality-quantity trade-off inherent in synthetic data. Previous approaches, such as LLM-as-a-Judge, have proven their effectiveness in addressing this but suffer from prohibitive computational costs and lack of interpretability. To ...

---

### 17. [A Reproducible Multi-Architecture Baseline for Token-Level Chinese Metaphor Identification under the MIPVU Framework](https://arxiv.org/abs/2605.07170)

**Authors**: Yufeng Wu  
**Category**: cs.CL  
**Published**: 2026-05-11  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.07170v1  

#### Abstract
Metaphor is pervasive in everyday language, yet token-level computational identification of metaphor-related words in Chinese under the MIPVU framework remains under-explored relative to English. This paper presents a reproducible multi-architecture baseline for token-level metaphor identification o...

---

### 18. [Dual-Agent Co-Training for Health Coaching via Implicit Adversarial Preference Optimization](https://arxiv.org/abs/2605.07011)

**Authors**: Da Long, Lingyi Fu, Diya Michelle Rao, Jasmine Ruales Carrera, Yang Bai, Shandian Zhe  
**Category**: cs.LG  
**Published**: 2026-05-11  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.07011v1  

#### Abstract
Motivational-interviewing-based health coaching is an effective approach for improving mental health and promoting healthy behavior change. However, the scarcity of trained human coaches and the high cost of coaching services make such support inaccessible to many people who could benefit from it. T...

---

### 19. [PACEvolve++: Improving Test-time Learning for Evolutionary Search Agents](https://arxiv.org/abs/2605.07039)

**Authors**: Minghao Yan, Bo Peng, Benjamin Coleman, Ziqi Chen, Zhouhang Xie, Shuo Chen, Zhankui He, Noveen Sachdeva, Weili Wang, Ed H. Chi, Shivaram Venkataraman, Wang-Cheng Kang, Derek Zhiyuan Cheng, Beidou Wang  
**Category**: cs.LG  
**Published**: 2026-05-11  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.07039v1  

#### Abstract
Large language models have become drivers of evolutionary search, but most systems rely on a fixed, prompt-elicited policy to sample next candidates. This limits adaptation in practical engineering and research tasks, where evaluations are expensive, and progress depends on learning task-specific se...

---

### 20. [Adaptive Domain Decomposition Physics-Informed Neural Networks for Traffic State Estimation with Sparse Sensor Data](https://arxiv.org/abs/2605.08028)

**Authors**: Eunhan Ka, Ludovic Leclercq, Satish V. Ukkusuri  
**Category**: cs.LG  
**Published**: 2026-05-11  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.08028v1  

#### Abstract
Traffic state estimation from sparse fixed sensors is challenging because physics-informed neural networks (PINNs) tend to over-smooth the shockwaves admitted by the Lighthill-Whitham-Richards (LWR) model. This study proposes Adaptive Domain Decomposition Physics-Informed Neural Networks (ADD-PINN),...

---

### 21. [HMACE: Heterogeneous Multi-Agent Collaborative Evolution for Combinatorial Optimization](https://arxiv.org/abs/2605.07214)

**Authors**: Yuping Yan, Jirui Han, Fei Ming, Yuanshuai Li, Yaochu Jin  
**Category**: cs.AI  
**Published**: 2026-05-11  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.07214v1  

#### Abstract
Large Language Models have recently emerged as a promising paradigm for automated heuristic design for NP-hard combinatorial optimization problems. Despite this progress, existing LLM-based methods typically rely on monolithic workflows constrained by rigid templates, thereby restricting memory-guid...

---

### 22. [Confidence-Aware Alignment Makes Reasoning LLMs More Reliable](https://arxiv.org/abs/2605.07353)

**Authors**: Kejia Chen, Jiawen Zhang, Yihong Wu, Kewei Gao, Jian Lou, Zunlei Feng, Mingli Song, Ruoxi Jia  
**Category**: cs.AI  
**Published**: 2026-05-11  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.07353v1  

#### Abstract
Large reasoning models often reach correct answers through flawed intermediate steps, creating a gap between final accuracy and reasoning reliability. Existing alignment strategies address this with external verifiers or massive sampling, limiting scalability. In this work, we introduce CASPO (Confi...

---

### 23. [Topology-Enhanced Alignment for Large Language Models: Trajectory Topology Loss and Topological Preference Optimization](https://arxiv.org/abs/2605.07172)

**Authors**: Yurui Pan, Ke Xu, Bo Peng  
**Category**: cs.CL  
**Published**: 2026-05-11  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.07172v1  

#### Abstract
Alignment of large language models (LLMs) via SFT and RLHF/DPO typically ignores the global geometry of the representation space, relying instead on local token likelihoods or scalar scores. We view generation as tracing a semantic trajectory in hidden space and propose a topology-enhanced alignment...

---

### 24. [Learning Agent Routing From Early Experience](https://arxiv.org/abs/2605.07180)

**Authors**: Yimin Wang, Jiahao Qiu, Xuan Qi, Xinzhe Juan, Jingzhe Shi, Zelin Zhao, Hongru Wang, Shilong Liu, Mengdi Wang  
**Category**: cs.CL  
**Published**: 2026-05-11  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.07180v1  

#### Abstract
LLM agents achieve strong performance on complex reasoning tasks but incur high latency and compute cost. In practice, many queries fall within the capability boundary of cutting-edge LLMs and do not require full agent execution, making effective routing between LLMs and agents a key challenge. We s...

---

### 25. [Rethinking Dense Sequential Chains: Reasoning Language Models Can Extract Answers from Sparse, Order-Shuffling Chain-of-Thoughts](https://arxiv.org/abs/2605.07307)

**Authors**: Yi-Chang Chen, Feng-Ting Liao, Da-shan Shiu, Hung-yi Lee  
**Category**: cs.CL  
**Published**: 2026-05-11  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.07307v1  

#### Abstract
Modern reasoning language models generate dense, sequential chain-of-thought traces implicitly assuming that every token contributes and that steps must be consumed in order. We challenge both assumptions through a systematic intervention pipeline--removal, masking, shuffling, and noise injection--a...

---

### 26. [GLiGuard: Schema-Conditioned Classification for LLM Safeguard](https://arxiv.org/abs/2605.07982)

**Authors**: Urchade Zaratiana, Mary Newhauser, George Hurn-Maloney, Ash Lewis  
**Category**: cs.CL  
**Published**: 2026-05-11  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.07982v1  

#### Abstract
Ensuring safe, policy-compliant outputs from large language models requires real-time content moderation that can scale across multiple safety dimensions. However, state-of-the-art guardrail models rely on autoregressive decoders with 7B--27B parameters, reformulating what is fundamentally a classif...

---

### 27. [Breaking the Illusion: When Positive Meets Negative in Multimodal Decoding](https://arxiv.org/abs/2605.06679)

**Authors**: Yubo Jiang, Yitong An, Xin Yang, Abudukelimu Wuerkaixi, Xuxin Cheng, Fengying Xie, Zhiguo Jiang, Cao Liu, Ke Zeng, Haopeng Zhang  
**Category**: cs.LG  
**Published**: 2026-05-11  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.06679v1  

#### Abstract
Vision-Language Models (VLMs) are frequently undermined by object hallucination, generating content that contradicts visual reality, due to an over-reliance on linguistic priors. We introduce Positive-and-Negative Decoding (PND), a training-free inference framework that intervenes directly in the de...

---

### 28. [Physics-based Digital Twins for Integrated Thermal Energy Systems Using Active Learning](https://arxiv.org/abs/2605.06756)

**Authors**: Umme Mahbuba Nabila, Paul Seurin, Linyu Lin, Majdi I. Radaideh  
**Category**: cs.LG  
**Published**: 2026-05-11  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.06756v1  

#### Abstract
Real-time supervisory control of thermal energy distribution systems requires digital twins that are accurate, interpretable, and uncertainty-aware, yet remain data and computationally efficient. High-fidelity simulations alone are costly, while purely data-driven surrogates often lack robustness. T...

---

### 29. [ADKO: Agentic Decentralized Knowledge Optimization](https://arxiv.org/abs/2605.07863)

**Authors**: Lucas Nerone Rillo, Zhanhong Jiang, Nastaran Saadati, Aditya Balu, Baskar Ganapathysubramanian, Chinmay Hegde, Soumik Sarkar  
**Category**: cs.LG  
**Published**: 2026-05-11  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.07863v1  

#### Abstract
We present Agentic Decentralized Knowledge Optimization (ADKO), a framework for collaborative black-box optimization across autonomous agents that achieves sample efficiency, privacy preservation, heterogeneous-objective handling, and communication efficiency. Each agent maintains a private Gaussian...

---

### 30. [Self-Play Enhancement via Advantage-Weighted Refinement in Online Federated LLM Fine-Tuning with Real-Time Feedback](https://arxiv.org/abs/2605.07977)

**Authors**: Seohyun Lee, Wenzhi Fang, Dong-Jun Han, Seyyedali Hosseinalipour, Christopher G. Brinton  
**Category**: cs.LG  
**Published**: 2026-05-11  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.07977v1  

#### Abstract
Recent works have advanced feedback-based learning systems, whereby a foundation model is able to intake incoming feedback (e.g., a user) to self-improve, creating a self-loop system of training. However, existing works are limited in needing to consider an offline setup to allow for such feedback-b...

---

## 🔧 Configuration

This bot is configured to look for papers containing the following keywords:
- kv cache, offload, State Space, SSM, framework, System, Generation, Video, Linear, LLM, RL, RLHF, Inference, Training, Attention, Pipeline, MOE, Sparse, Quantization, Speculative, Efficient, Efficiency, Framework, Parallel, Distributed, Kernel, Decode, Decoding, Prefill, Throughput, Fast, Network, Hardware, Cluster, FP8, FP4, Optimization, Scalable, Communication

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
