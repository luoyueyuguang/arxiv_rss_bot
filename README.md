# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-05-26 08:58:27 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG

## 📚 Recent Papers

### 1. [Bandwidth-Aware LLM Inference on Heterogeneous Many-Core Supercomputers](https://arxiv.org/abs/2605.25655)

**Authors**: Yao Lu, Zhongzhi Luan, Gen Li, Jiaxing Qi, Shiqing Ma, Bin Han, Shizhe Shang, Hailong Yang, Depei Qian  
**Category**: cs.DC  
**Published**: 2026-05-26  
**Score**: 20.0  
**Type**: new  
**ArXiv ID**: 2605.25655v1  

#### Abstract
Large language model (LLM) inference is limited by high computational cost and memory bandwidth demands, making deployment on heterogeneous many-core processors challenging. Taking the MT-3000 processor used in the Tianhe supercomputer as an example, its limited main-memory bandwidth and distributed...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Bandwidth-Aware LLM Inference on Heterogeneous Many-Core Supercomputers

---

## 1. 论文的主要贡献和创新点

### 解决的问题
大型语言模型（LLM）推理面临**高计算成本**和**内存带宽瓶颈**，尤其在异构众核架构（如MT-3000）上部署时挑战显著。传统基于GPU的推理框架（如DeepSpeed、vLLM）依赖高带宽统一内存架构（如HBM），难以适配天河新一代超算中**有限主存带宽**（仅约120 GB/s）和**分布式存储层次**的硬件特性。

具体挑战包括：
- **硬件不匹配**：MT-3000采用VLIW-SIMD架构，传统算子难以高效利用其并行能力。
- **内存带宽受限**：远低于同级别GPU（如V100为900+ GB/s），导致I/O成为瓶颈。
- **扩展性瓶颈**：单集群内存有限（约20GB），大模型需跨集群并行，通信开销大。

### 提出的新方法与创新思路
作者提出 **THInfer** —— 一种面向异构众核架构的**硬件感知LLM推理框架**，通过**硬件-软件协同设计**（co-design）实现带宽约束下的高性能推理。

#### 主要创新点：
1. **高性能算子库（High-Performance Operator Library）**
   - 针对MT-3000的VLIW-SIMD架构，手工编写FP16优化内核。
   - 利用**数据流分析**和**汇编级优化**，使GEMM等核心算子达到单集群理论峰值性能的**70%**。
   - 支持**混合精度策略**（FP16存储 + FP32累积），兼顾效率与数值稳定性。

2. **密度驱动的计算图融合（Density-Driven Computation Graph Fusion）**
   - 提出“低密度-高密度-低密度”融合模式，将RoPE、Add等轻量算子嵌入GEMM等重算子中。
   - 设计**MT Attention**机制，替代Flash Attention，适配MT-3000的AM/SM/GSM三级存储体系。
   - 减少冗余I/O访问和Kernel Launch开销，提升片上内存利用率。

3. **自适应并行调度机制（Adaptive Parallel Scheduling）**
   - 构建 **P-B-D（Prefill-Buffer-Decode）三级同步流水线**，在微批次粒度解耦Prefill与Decode阶段。
   - 引入**有界缓冲区**和**反压控制**，防止KV Cache无限增长导致OOM。
   - 采用**混合并行策略**：簇内用`hthreads`同步，簇间用MPI通信，形成两级并行模式，聚合跨设备内存带宽。

4. **系统级评估框架**
   - 建立多维性能评估体系，涵盖延迟、吞吐、资源利用率等指标，在Llama系列模型上验证鲁棒性。

### 相比现有方法的优势
| 维度 | 现有方法（如DeepSpeed） | THInfer |
|------|--------------------------|--------|
| **硬件适配性** | 依赖GPU高带宽HBM | 针对低带宽DDR优化，软硬协同 |
| **算子效率** | 编译器生成代码，效率低 | 手写汇编，达70%峰值性能 |
| **I/O优化** | 通用Attention机制 | MT Attention减少DMA次数 |
| **扩展性** | 跨节点通信开销大 | P-B-D流水线+两级通信，支持70B稳定推理 |
| **内存管理** | 易出现OOM | 有界缓冲+反压机制，避免缓存溢出 |

---

## 2. 核心实验方法和设置

### 使用的数据集
- **合成Prompt数据集**：固定长度（512或1024），用于生成任务。
- **生成长度**：每个请求生成128个Token。
- 模型覆盖Llama2系列：**7B、13B、30B、70B**参数规模。

> 注：虽未测试其他模型，但方法适用于所有基于Transformer架构的LLM（如Qwen、DeepSeek等）。

### 实验设置与评估指标

| 项目 | 设置 |
|------|------|
| **硬件平台** | - MT-3000节点（FP16: 32.4 TFLOPS, 带宽: 120 GB/s）<br> - 对比：Tesla V100S（1134 GB/s）、NVIDIA A800（1935 GB/s） |
| **对比原则** | - **Peak-Aligned**：按峰值算力对齐（8×MT-3000 vs 2×V100S；10×MT-3000 vs 1×A800）<br> - **BW-Aligned**：按带宽对齐（18×MT-3000 vs 2×V100S；16×MT-3000 vs 1×A800） |
| **评估指标** | - **Throughput**（Tokens/s）：核心指标<br> - **Latency**：端到端响应时间<br> - **Memory Utilization**：KV Cache与模型权重占用 |
| **基线方法** | - DeepSpeed-Inference（Tensor Parallelism）<br> - Hugging Face Accelerate（Pipeline Parallelism） |

### 实现细节
- 使用纯C++开发，含内联汇编，代码约万行。
- 所有优化均深度集成至系统栈底层。

---

## 3. 主要实验结果和性能指标

### 关键性能数据（摘录自Table V & VI）

#### 表：**Throughput (Tokens/s)** @ Peak-Aligned Setting
| Model | Prompt Len | DeepSpeed (A800) | THInfer (MT-3000) | 提升幅度 |
|-------|------------|------------------|-------------------|---------|
| Llama-7B | 512 | 584 | **975** | **+67%** |
| Llama-7B | 1024 | 310 | **570** | **+84%** |
| Llama-13B | 512 | 345 | **301** | ≈持平 |
| Llama-13B | 1024 | 184 | **211** | **+15%** |
| Llama-30B | 512 | 116 | **105** | ≈持平 |
| Llama-30B | 1024 | 60 | **61** | ≈持平 |
| Llama-70B | 512 | OOM | **64** | **唯一可运行方案** |

> 在**带宽对齐配置下**，THInfer吞吐接近线性提升（如7B模型达2.25×加速），表明其能有效聚合DDR带宽。

### 与基线方法对比结果
- **7B模型**：THInfer相比DeepSpeed在V100S上提升**62%-73%**，在A800上提升**67%-84%**。
- **13B及以上模型**：在长序列（1024）场景下表现更优，体现其在**计算密集型任务**中的优势。
- **70B模型**：GPU基线全部OOM，而THInfer仍能维持**64 tokens/s**的稳定吞吐，展现卓越扩展性。

### 消融实验结果（Ablation Study）
| 阶段 | 优化内容 | 30B模型吞吐（Tokens/s） | 相对提升 |
|------|--------|------------------------|----------|
| A0 | 无优化（单节点） | 0.07 | - |
| A1 | 算子优化（FP16 + 手写Kernel） | 2.47 | **+3400%** |
| A2 | 图调度优化（融合RoPE/MHA） | 3.02 | +22% |
| A3-1 | Selective Batching + PP | 14.0 | +362% |
| A3-2 | + Tensor Parallelism | 27.0 | +93% |
| A4 | + P-B-D三级流水线 | **34.0** | +26% |

> 结论：**算子层优化带来最大收益**，且随模型增大，系统级优化（如P-B-D）增益更显著。

---

## 4. 关键结论和发现

### 主要发现
1. **硬件感知是异构架构LLM推理的关键**  
   通用框架无法适配低带宽众核系统，必须通过**软硬协同设计**释放硬件潜力。

2. **手写算子可大幅提升计算效率**  
   在MT-3000上，FP16 Linear算子可达**70.2%理论峰值**（5686 GFLOPS），远超编译器自动生成代码。

3. **MT Attention显著降低I/O开销**  
   相比Flash Attention，MT Attention在S=4096、Head=64时**延迟降低36%**，速度提升达**3.5×**。

4. **P-B-D流水线保障系统稳定性与扩展性**  
   通过有界缓冲与反压机制，成功避免KV Cache爆炸，支持**70B模型稳定推理**，这是现有GPU框架无法做到的。

5. **带宽聚合优于单纯算力堆叠**  
   在带宽对齐实验中，THInfer表现出近线性吞吐增长，说明其能有效利用**分布式DDR带宽**。

### 方法的局限性
- **硬件强绑定**：当前优化高度依赖MT-3000的VLIW-SIMD与三级存储结构，迁移到其他架构需重新设计。
- **开发复杂度高**：需手动编写汇编代码，工程门槛高，不利于快速迭代。
- **仅支持自回归生成**：未涉及复杂推理模式（如Speculative Decoding）。

### 未来工作方向
- 将THInfer设计理念推广至更多异构架构（如国产AI芯片、RISC-V众核）。
- 探索自动Kernel生成技术（AutoTVM风格），降低人工优化成本。
- 支持更复杂的调度策略，如动态批处理、推测解码（Speculative Decoding）。
- 扩展至多模态大模型（如Qwen-VL）的高效推理。

---

> ✅ **总结一句话**：  
> THInfer通过**算子级优化 + 图融合 + 系统级流水线设计**，首次实现了在**低带宽异构众核超算**上对百亿参数LLM的**高效、稳定、可扩展推理**，为国产高性能计算平台赋能大模型提供了可行路径。

</details>

---

### 2. [Bandwidth-Aware and Cost-Efficient Pipeline Parallel Scheduling in Geo-Distributed LLM Training](https://arxiv.org/abs/2605.25375)

**Authors**: Han Zhang, Jianchun Liu, Hongli Xu  
**Category**: cs.DC  
**Published**: 2026-05-26  
**Score**: 14.0  
**Type**: new  
**ArXiv ID**: 2605.25375v1  

#### Abstract
The rapid evolution of large language models (LLMs) has made geographically distributed training necessary due to GPU scarcity within a single cloud region. In such cross-region settings, Pipeline Parallelism (PP) is communication-efficient, yet scheduling PP remains challenging under heterogeneous ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Bandwidth-Aware and Cost-Efficient Pipeline Parallel Scheduling in Geo-Distributed LLM Training

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
在大规模 **Large Language Model (LLM)** 训练中，单个云区域内的 GPU 资源日益稀缺，导致训练任务不得不跨地理区域（geo-distributed）进行调度。然而，这种跨区域训练面临两大挑战：
- **异构带宽**：不同区域间的网络带宽差异显著，低带宽链路会引发严重的通信瓶颈，造成 pipeline bubbles，大幅延长 **Job Completion Time (JCT)**。
- **电价差异**：各地区的电力成本悬殊，若不加优化地分配资源，可能导致极高的电费支出。

现有调度器（如 Delay-First 或 Cost-First）通常只关注单一目标（延迟或成本），且采用固定执行顺序（如 FCFS），容易导致 **Head-of-Line (HoL) 阻塞**，降低整体集群效率。

---

### 提出了什么新方法或新思路
作者提出 **BACE-Pipe** —— 一种面向跨区域 LLM 训练的 **带宽感知、成本高效** 的 Pipeline Parallel (PP) 调度框架。

其核心创新在于一个三层协同机制：

1. **动态作业优先级机制（Dynamic Job Prioritization）**
   - 综合考虑作业的 **计算强度（Computation Intensity）** 和 **带宽敏感性（Bandwidth Sensitivity）**
   - 引入自适应权重因子 α，根据实时网络拥塞程度动态调整优先级评分，避免长耗时、高带宽需求的任务阻塞后续小任务。

2. **带宽感知路径搜索器（Bandwidth-Aware Pathfinder）**
   - 在满足通信约束的前提下，寻找可行的跨区域 pipeline 路径。
   - 采用类 Prim 算法的贪心扩展策略，优先选择高带宽连接，并确保通信时间不超过计算时间，防止 pipeline stall。

3. **成本最小化分配器（Cost-Min Allocator）**
   - 在所有可行路径中，优先将 GPU 分配到电价更低的区域。
   - 通过“先保证连通性 + 再按电价排序填充”的策略实现成本最优。

---

### 相比现有方法的优势
| 对比维度 | 现有方法缺陷 | BACE-Pipe 改进 |
|--------|------------|--------------|
| **目标平衡** | 只优化延迟或成本，无法兼顾 | 同时优化 JCT 与总电费，实现双目标协同 |
| **执行顺序** | 固定 FCFS，易产生 HoL 阻塞 | 动态优先级排序，提升系统吞吐量 |
| **路径构建** | 忽视带宽瓶颈，盲目聚合资源 | 显式建模通信延迟，保障 pipeline 效率 |
| **资源利用** | 单区域绑定或静态分配 | 跨区域弹性聚合，提高全局 GPU 利用率 |

---

## 2. 核心实验方法和设置

### 使用的数据集
实验未直接使用传统 NLP 数据集进行模型训练，而是基于以下真实世界数据驱动仿真环境：
- **电价数据**：来自 [GlobalPetrolPrices](https://zh.globalpetrolprices.com/electricity_prices)，涵盖全球多个城市的工业电价。
- **带宽数据**：参考 AWS EC2 G4 实例提供的网络能力（25–100 Gbps），并模拟跨区域链路带宽。
- **LLM 工作负载**：共 8 个 LLM 训练任务，参数规模从 **14B 到 101B** 不等，覆盖主流架构如：
  - `Llama-3.1-70B`
  - `Qwen2.5-14B/32B`
  - `Falcon-40B`
  - `Gemma-3-27B`
  - `FLM-101B`

每个任务随机分配以下三种典型数据集之一以增加多样性：
- **Alpaca-52k**（约 50MB）—— 小规模指令微调
- **WikiText-103**（约 0.5GB）—— 中等语言建模
- **OpenWebText**（约 38GB）—— 大规模预训练语料

---

### 实验设置和评估指标

#### 模拟环境配置
- **6 个地理区域**：EU-West（爱尔兰）、US-East-2（纽约）、EU-Central（法兰克福）、EA-East（东京）、SEA-South（新加坡）、OC-East（悉尼）
- **GPU 类型**：NVIDIA A6000，每区域 GPU 数量为 {16, 32, 64, 128}
- **调度粒度**：Pipeline Parallelism + Micro-batch 执行模型

#### 评估指标
| 指标 | 描述 |
|------|------|
| **Avg. JCT** | 所有任务从提交到完成的平均耗时（小时） |
| **Total Electricity Cost** | 所有任务在整个训练期间消耗的总电费（美元） |

#### 基线方法对比
选取四类代表性调度策略作为 baseline：
| 方法 | 类型 | 策略说明 |
|------|------|---------|
| **LCF** | Cost-First | 将整个任务放在电价最低的单个区域内 |
| **LDF** | Delay-First | 将任务放在 GPU 最多的单个区域内 |
| **CR-LCF** | Cross-Region Cost-First | 按电价升序聚合多区域 GPU |
| **CR-LDF** | Cross-Region Delay-First | 按容量+带宽贪心扩展跨区域路径 |

所有方法均限制最大 GPU 数为理论最优值 $ K^* = \arg\min_k t_{iter}(k) $，确保公平比较。

---

## 3. 主要实验结果和性能指标

### 关键性能数据（vs. SOTA Baselines）

| 性能指标 | BACE-Pipe 表现 | 提升幅度 |
|--------|----------------|----------|
| **平均 JCT** | 最短 | ↓ **27.9% – 64.7%** |
| **总电费** | 最低 | ↓ **12.6% – 30.6%** |

> 注：以上数值为相对于四种 baseline 的平均改进范围，在多种负载和资源配置下稳定成立。

---

### 与基线方法的对比结果

#### ✅ JCT 表现
- BACE-Pipe 在所有场景下均取得最短 JCT。
- 特别是在 **高带宽环境（1.5× 默认带宽）** 下，CR-LDF 的 JCT 是 BACE-Pipe 的 **3.4 倍**，显示出其因贪婪扩张导致的严重 HoL 阻塞。
- 在 **GPU 紧张（0.5× 容量）** 场景中，BACE-Pipe 的 JCT 比 CR-LDF 低 **近 70%**。

#### ✅ 成本表现
- BACE-Pipe 成本始终低于所有 baseline。
- 即使是专为省钱设计的 CR-LCF，在某些情况下仍比 BACE-Pipe 贵 **超过 30%**。
- 成功验证了“**通过智能调度既提速又降费**”的可能性。

#### ❗ Cross-Region Paradox 发现
令人惊讶的是：
> “跨区域”本身并不一定带来性能提升！

- **CR-LDF 和 CR-LCF 的 JCT 反而高于 LDF 和 LCF**（分别高出 28.8% 和 13.1%）
- 原因：大型任务早期抢占大量 GPU 和关键链路，造成长期资源垄断，形成 **HoL Blocking**。
- 这一现象被称为 **Cross-Region Paradox**，凸显了仅靠资源聚合而不优化调度顺序的风险。

---

### 消融实验结果（Ablation Study）

移除 BACE-Pipe 的任一组件都会显著劣化性能：

| 移除组件 | JCT 影响 | 成本影响 | 结论 |
|--------|--------|--------|------|
| **w/o Pathfinder** | ↑ **52.5%** | ↑ **20.5%** | 路径搜索是实现高效跨区聚合的基础 |
| **w/o Priority** | ↑ **41.9%** | ↑ **5.0%** | 优先级机制对缓解 HoL 至关重要 |
| **w/o Cost-Min Allocator** | ↑ **4.6%** | ↑ **13.9%** | 成本优化不仅省钱，还能减少碎片化，间接提升 JCT |

> ⚠️ 特别值得注意：`Cost-Min Allocator` 虽然主要用于降低成本，但由于其集中式分配减少了资源碎片，反而有助于后续任务更快部署，从而轻微改善了 JCT。

---

## 4. 关键结论和发现

### 主要发现
1. **跨区域调度必须联合优化三个维度**：
   - 作业执行顺序（Prioritization）
   - 跨区域 pipeline 路径（Pathfinding）
   - 区域间资源分配（Placement）

2. **动态优先级优于 FCFS**：
   - 自适应权衡计算强度与带宽敏感性，可有效预防 HoL 阻塞，尤其在多租户环境下至关重要。

3. **存在 Cross-Region Paradox**：
   - 盲目扩大 GPU 数量可能适得其反，必须结合通信效率判断是否值得跨区域部署。

4. **成本与性能并非完全冲突**：
   - 通过合理的路径选择和电价感知分配，可以在几乎不影响 JCT 的前提下显著降低电费。

5. **组件之间具有强协同效应**：
   - 三者缺一不可，共同构成了 BACE-Pipe 的核心竞争力。

---

### 方法的局限性
1. **静态 PP 配置假设**：
   - 当前方法假设 pipeline 并行度在运行时不变，未支持动态调整（如弹性扩缩容）。
2. **忽略其他通信模式**：
   - 主要针对 Pipeline Parallelism 设计，未考虑与其他并行范式（如 Tensor Parallelism）的混合调度。
3. **依赖准确的 profiling 输入**：
   - 需预先知道每个任务的 `t_comp`, `A`, `M` 等元信息，实际中可能存在估计误差。
4. **未考虑数据本地性**：
   - 假设数据可自由传输，未建模训练数据存储位置对调度的影响。

---

### 未来工作方向
1. **支持动态 runtime 调整**：
   - 引入 checkpointing 机制，允许在运行中重新分片和迁移 pipeline stages。
2. **扩展至 Hybrid Parallelism 场景**：
   - 支持 TP + PP + DP 的联合调度，更贴近实际生产系统。
3. **集成预测模块**：
   - 使用 ML 模型自动预测任务特征（如 activation size、compute time），减少人工标注负担。
4. **引入碳排放优化目标**：
   - 将绿色计算纳入考量，进一步推动可持续 AI 发展。
5. **在线学习式调度器**：
   - 利用强化学习持续优化调度策略，适应不断变化的工作负载分布。

---

## 总结

✅ **BACE-Pipe 是首个同时解决 geo-distributed LLM 训练中“延迟”与“成本”双重挑战的调度框架**。  
它通过 **动态优先级 + 带宽感知路径搜索 + 成本最小化分配** 的三级联动机制，在真实模拟环境中实现了：
- **平均 JCT 降低 27.9%~64.7%**
- **总电费下降 12.6%~30.6%**

该工作揭示了“跨区域 ≠ 更快”的深刻洞见（Cross-Region Paradox），强调了 **智能调度顺序的重要性**，为未来大规模分布式 LLM 训练系统的资源管理提供了重要范式。

</details>

---

### 3. [Accelerating Long-Tail Generation in Synchronous RLHF Training via Adaptive Tensor Parallelism](https://arxiv.org/abs/2605.23945)

**Authors**: Long Zhao, Qinghe Wang, Jiaan Zhu, Youhui Bai, Zewen Jin, Chaoyi Ruan, Shengnan Wang, Cheng Li  
**Category**: cs.AI  
**Published**: 2026-05-26  
**Score**: 12.5  
**Type**: new  
**ArXiv ID**: 2605.23945v1  

#### Abstract
Reinforcement Learning from Human Feedback (RLHF) has become a key post-training paradigm for improving model quality. However, the synchronous three-stage RLHF pipeline is often bottlenecked by the generation stage, where response-length skew causes the effective batch size to shrink rapidly during...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Accelerating Long-Tail Generation in Synchronous RLHF Training via Adaptive Tensor Parallelism

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
在同步式的 **Reinforcement Learning from Human Feedback (RLHF)** 训练中，**generation 阶段** 是主要性能瓶颈。由于响应长度存在显著偏斜（response-length skew），即大多数样本较短而少数样本极长，导致生成过程分为两个阶段：
- **Aligned Phase**：多数样本并行解码，batch size 大，GPU 利用率高；
- **Tail Phase**：仅剩少量长序列仍在运行，有效 batch size 急剧下降，GPU 严重空闲。

主流框架采用静态的 **Tensor Parallelism (TP)** 配置，无法适应这两个阶段对并行策略的不同需求，造成资源浪费。

---

### 🚀 提出的新方法：PAT（Progressive Adaptive Tensor Parallelism）

PAT 是一种在 RLHF 的 generation 阶段动态调整 TP/DP 配置的方法，核心思想是：
> 在 **aligned phase 使用低 TP / 高 DP**（提升吞吐），  
> 在 **tail phase 切换为高 TP / 低 DP**（降低单个样本延迟）。

#### 主要技术创新：
1. **Predictor-guided Online Reconfiguration**
   - 基于离线 profiling 构建延迟预测模型；
   - 在线判断是否应触发 TP 切换：只有当切换带来的尾部延迟收益 > 切换开销时才执行；
   - 自动选择最优目标 TP 配置。

2. **Lightweight Runtime State Adaptation**
   - 不重启推理引擎，而是增量更新受影响的状态：
     - **KV Cache Handling**：基于成本模型选择迁移（migration）或重计算（recomputation）；
     - **Weight Resharding**：逐层进行 All-Gather + Slice 实现免重载权重再分片；
     - **Communication Group Reuse**：缓存已创建的通信组，避免重复初始化。

3. **系统集成**
   - 基于 **SGLang** 推理引擎构建，并集成到 **VeRL** 框架中，支持端到端 RLHF 流程。

---

### 🔍 相比现有方法的优势

| 方法 | 缺陷 | PAT 的优势 |
|------|------|------------|
| **VeRL / OpenRLHF** | 静态 TP，无法应对 tail phase 资源浪费 | 动态适配，提升 GPU 利用率 |
| **StreamRL** | 异步执行可能引入 stale rollout，影响训练稳定性 | 保持同步语义，不改变算法逻辑 |
| **RLHFuse / Kimi K2** | 通过阶段重叠或部分 rollout 缓解问题，但牺牲完整性或一致性 | 直接加速 tail 解码，保留同步性和轨迹一致性 |

> ✅ PAT 在不修改 RLHF 算法语义的前提下，显著提升了 generation 效率。

---

## 2. 核心实验方法和设置

### 📚 数据集
- **DeepScaleR**：一个专注于逻辑推理能力提升的 RLHF 数据集，具有明显的响应长度分布偏斜（long-tail 特征），适合测试 tail phase 优化效果。

### 🧪 实验设置
- **模型**：
  - `LLaMA3.1-8B`
  - `Qwen3-14B`
- **硬件平台**：
  - 单节点 & 双节点 A40 集群（PCIe 4.0）
  - 单服务器 H100 SXM（NVLink 900 GB/s）
- **软件栈**：
  - CUDA 12.6, PyTorch 2.7.1
  - VeRL 0.4.1, SGLang 0.4.8
- **Batch Size**：128
- **Max Response Length**：最高达 24K tokens

### 🎯 评估指标
| 指标 | 定义 |
|------|------|
| **End-to-end Iteration Latency** | 一次完整 RLHF 迭代的时间 |
| **Generation Latency** | generation 阶段耗时 |
| **Throughput (tokens/sec)** | 每秒处理的 token 数量 |
| **Speedup** | 相对于 baseline 的加速比 |

### ⚖️ 基线方法
- **VeRL (Best Static TP/DP)**：对每个配置组合调优后选取最佳静态 TP 设置作为 baseline。

---

## 3. 主要实验结果和性能指标

### 📊 关键性能数据

| 模型 | 硬件 | 最大长度 | PAT 加速比 | 生成延迟降低 |
|------|------|----------|-------------|----------------|
| LLaMA3.1-8B | 8×A40 | 16K | **1.27×** | — |
| LLaMA3.1-8B | 8×H100 | 24K | **1.37×** | ↓34.6% |
| Qwen3-14B | 16×A40 | 16K | **1.18×** | — |
| Qwen3-14B | 8×H100 | 16K | **1.29×** | ↓32.0% |

> 💡 **端到端 RLHF iteration latency 最多降低 27.2%**

---

### 🔍 与基线对比结果
- 在所有测试场景下，PAT 均优于最优静态配置；
- 随着最大响应长度增加，tail phase 占比上升，PAT 的优势更加明显；
- 在 H100 上表现更优，得益于 NVLink 更高的带宽降低了 TP 切换和通信开销。

---

### 🔬 消融实验与开销分析（Ablation Study）

#### （1）Switching Overhead 对比
| 操作 | Naive 方法耗时 | PAT 耗时 | 降幅 |
|------|----------------|---------|-------|
| Process Restart | 17.8 s | — | — |
| KV Cache Handle | 19.0 s | 2.36 s | ↓87.6% |
| Weight Resharding | 7.47 s | 1.03 s | ↓86.2% |
| CUDA Graph Recapture | 3.59 s | 0.73 s | ↓79.7% |
| **总切换时间** | **58.98 s** | **5.52 s** | **↓90.6%** |

> ✅ 切换开销仅占端到端时间约 **1.23%**，几乎可忽略。

#### （2）内存开销控制
- 峰值额外内存占用仅 **+2.5 GB**（相比 naive 全量迁移需 14 GB KV cache）；
- 稳态内存增加来自更大的 KV cache pool 分配，非 PAT 本身引入。

#### （3）预测器准确性验证
| TP 配置 | 平均预测误差 |
|--------|--------------|
| TP=2, DP=4 | 4.04% |
| TP=8, DP=1 | 3.07% |

> ✅ 预测模型能准确反映真实 workload 行为，即使存在 shape-dependent 非线性波动。

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **Tail Phase 是 RLHF 中 generation 瓶颈的核心来源**，其 GPU 利用率可从 13.71 TFLOPS（aligned phase）骤降至 0.11 TFLOPS。
2. **静态 TP 配置无法兼顾不同阶段的需求**：大 batch 适合低 TP，小 batch 适合高 TP。
3. **动态 TP 切换可行且高效**：通过轻量级状态迁移机制，切换开销可压至 5 秒以内。
4. **PAT 显著提升端到端效率**：
   - generation latency ↓34.6%
   - end-to-end iteration time ↓27.2%
   - throughput 提升最高达 **1.37×**

---

### ⚠️ 局限性
1. **依赖 intra-node TP**：当前实现假设 TP 在单节点内完成，跨节点 TP 支持有限；
2. **对短响应或均匀分布 workload 收益较小**：若无明显 tail，切换不会被触发；
3. **需要 profiling 开销**：虽仅一次，但仍需预采集延迟曲线；
4. **未支持 PP（Pipeline Parallelism）动态切换**：目前仅处理 TP/DP 调整。

---

### 🔮 未来工作方向
1. 扩展至 **3D 并行（TP+DP+PP）联合动态重构**；
2. 支持 **跨节点自适应 TP**，进一步提升分布式扩展性；
3. 结合 **异构硬件调度**，实现更细粒度的资源匹配；
4. 将 PAT 思路推广至其他存在 long-tail 生成任务的场景（如代码生成、对话系统等）。

---

## ✅ 总结
**PAT 提出了一种新颖且实用的 adaptive tensor parallelism 方法，在不改变 RLHF 同步语义的前提下，通过动态调整 TP/DP 配置，有效缓解了 long-tail generation 导致的资源浪费问题。其实验充分、工程实现扎实，在多种模型和硬件平台上均取得显著性能提升，是 RLHF 系统优化领域的重要进展。**

</details>

---

### 4. [Inference Time Context Sparsity: Illusion or Opportunity?](https://arxiv.org/abs/2605.24168)

**Authors**: Sahil Joshi, Prithvi Dixit, Agniva Chowdhury, Anshumali Shrivastava, Joseph E. Gonzalez, Ion Stoica, Kumar Krishna Agrawal, Aditya Desai  
**Category**: cs.AI  
**Published**: 2026-05-26  
**Score**: 10.5  
**Type**: new  
**ArXiv ID**: 2605.24168v1  

#### Abstract
Sparsity has long been a central theme in LLM efficiency, but its role in context processing remains unresolved. As LLM workloads shift toward longer contexts and agentic interactions, the compute and memory bottlenecks of attention become increasingly critical, raising the question of whether these...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Inference Time Context Sparsity: Illusion or Opportunity?*

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
该论文聚焦于**大语言模型（LLM）在长上下文场景下的推理效率瓶颈**。随着 LLM 应用向更长的输入（如法律文档、代码仓库、多轮对话）和代理式交互（agentic workflows）发展，标准的 **scaled dot-product attention** 在预填充（prefill）阶段面临 $O(N^2)$ 的计算复杂度，在解码（decoding）阶段则受限于 $O(N \cdot d)$ 的 KV Cache 内存带宽访问，成为系统性能的主要瓶颈。

传统观点认为这些是“根本性约束”，而本文挑战这一共识，提出：**这些瓶颈实际上是人为且不必要的**。

---

### 提出了什么新方法或新思路
论文提出了一个核心论点：  
> **LLM 推理的未来在于沿上下文维度实现极端但有原则的稀疏性（extreme but principled context sparsity）**。

其主要思想包括：

- **Inference-time context sparsity**：在不修改训练过程的前提下，在推理时强制对 attention 进行稀疏化（例如只关注 top-k tokens），并验证其有效性。
- **硬件对齐的稀疏设计**：开发了支持 **per-token, per-query, per-head level** 的非规则稀疏模式的高效 decode kernel，基于 FlashInfer 和 paged KV Cache 构建。
- **理论支撑**：指出“全密集 attention”在理论上不可行——由于隐藏维度 $d < N$，信息必然坍缩，因此完全稀疏不仅是近似，反而是更优目标（见 Theorem 1）。
- **算法层面探索**：
  - 使用 **exact oracle top-k selection** 消除近似索引器带来的误差。
  - 引入 **vAttention**（随机采样机制）作为 deterministic top-k 的替代方案，尤其适用于小模型。

---

### 相比现有方法的优势
| 维度 | 本文优势 |
|------|--------|
| **理念上** | 质疑“必须保留 dense attention”的默认假设，主张从架构到训练都应以稀疏为第一性原理。 |
| **方法通用性** | 支持高度不规则的稀疏模式（无需 block 结构），兼容 GQA/MHA 等现代注意力变体。 |
| **系统实现** | 开发了可落地的 sparse decode kernel，在 H100 上实现了高达 **76× 的加速**（500× sparsity）。 |
| **适用任务广度** | 验证了稀疏性在检索、数学推理、多跳问答、**agentic coding** 等多种复杂任务中的鲁棒性。 |

---

## 2. 核心实验方法和设置

### 使用了哪些数据集
- **RULER-HARD-32K**：合成检索任务子集，测试模型在长上下文中定位相关信息的能力。
- **LOFT (32K & 128K)**：自然语言的长上下文检索与问答基准，涵盖 HotpotQA、NQ、Musique 等多个子任务。
- **AIME-2025**：数学推理任务，允许最多生成 65K tokens，平均约 25K，用于评估稀疏对长期生成稳定性的影响。
- **SWE-Bench Django (Lite)**：真实世界 GitHub issue 修复任务，共 114 个任务，最大上下文超 100K tokens，用于评估 **agentic coding** 场景下的表现。

---

### 实验设置和评估指标

#### 模型家族
- **Standard Transformers**: `Llama3`, `Qwen2.5`, `Ministral3`
- **Hybrid Architectures**: `Qwen3.5` (含 linear attention 层), `Gemma3`

#### 稀疏策略
- **Oracle Top-K**：精确选择 top-k attention 分数对应的 tokens。
- **vAttention**：基于采样的随机稀疏机制，提升小模型鲁棒性。
- **Sink + Local + Top-K**：保留局部窗口和 sink tokens，其余稀疏处理。

#### 评估指标
| 类型 | 指标 |
|------|-----|
| 性能保持 | Relative Score = Sparse / Dense；Retention Rate |
| 推理效率 | Decoding Latency, Speedup over FlashInfer |
| 任务完成质量 | Resolution Rate (SWE-Bench), Subspan-EM (LOFT), Accuracy (AIME) |
| 成本控制 | Turns per Task, Total Tokens, Cost per Instance |

#### 硬件平台
- **GPU**: NVIDIA H100 80GB HBM3
- **精度**: FP16
- **KV Cache Layout**: NHD, page size=16
- **GQA Configuration**: $H_q=32, H_k=8, D=128$

---

### 基线方法对比
- **Dense Attention**：标准 full softmax attention，作为性能上限。
- **FlashInfer**：当前最先进的 dense decode 引擎，作为速度基线。
- **Linear Attention / SSMs**：作为轻量级 context processor 的代表进行概念对比（未直接比较性能）。

---

## 3. 主要实验结果和性能指标

### 关键性能数据

#### ✅ 模型鲁棒性（跨任务）
| 模型 | 任务 | 最高容忍稀疏程度 | 性能下降 |
|------|------|------------------|---------|
| Qwen3.5-27B | RULER-HARD / LOFT | **100× sparsity** | 几乎无损 |
| Qwen3.5-27B | AIME-2025 | 50× sparsity | 微小下降 |
| Qwen3.5-27B | SWE-Bench Django | 50× sparsity | Resolution rate 仅降 ~2pp（严格子集） |

> 🔹 在 RULER-HARD 上，Qwen3.5-27B 即使只使用 **128 个 retrieved tokens**（相当于 ~250× sparsity），仍接近 dense 表现。

#### ✅ 系统加速效果（vs FlashInfer）
**表 1：Sparse Decode Kernel 加速比（H100）**

| Batch Size | 50× Sparsity | 100× Sparsity | 500× Sparsity |
|------------|--------------|---------------|----------------|
| 1          | 5.57×        | 10.25×        | 11.14×         |
| 4          | 7.45×        | 13.36×        | 42.04×         |
| 8          | 8.88×        | 16.82×        | **76.14×**     |
| 16         | 10.54×       | 20.09×        | **76.77×**     |

> 💡 即使没有块结构（no block structure），也能获得显著加速，打破“只有 block sparsity 才有效”的迷思。

#### ✅ Indexer 开销可控（见 Table 2）
使用 **Double Sparsity**（8通道 16-bit）作为 indexer：
- 在 MHA 下，**100× sparsity 达到 4.17× 加速**
- 在 GQA 下，**100× sparsity 达到 2.81× 加速**
- 已实现 break-even（>1×）在 2×~10× sparsity 区间

> 📌 更轻量的 indexer（如 HashAttention、PQCache）有望进一步扩大收益。

---

### 与基线方法的对比结果
| 对比项 | 结果 |
|-------|------|
| vs Dense Attention | 在 50× 稀疏下，Qwen3.5 等大模型性能损失 <2%，部分任务甚至持平或反超（因去噪效应） |
| vs FlashInfer | 最高 **76× kernel-level 速度提升**，尤其在大 batch 和高稀疏度下优势明显 |
| vs Deterministic Top-K | 小模型上 deterministic top-k 明显退化（如 Qwen2.5-1.5B ↓至 63%），而 **vAttention 可恢复至接近 dense 水平** |

---

### 消融实验结果
1. **模型规模影响**：
   - 小模型（<7B）在 top-k 稀疏下性能下降明显。
   - 大模型（>14B）即使在 50× 稀疏下也基本保持 dense 性能。
   - → **Scale 弥补稀疏带来的信息损失**。

2. **架构影响**：
   - Hybrid 模型（Qwen3.5, Gemma3）显著优于标准 Transformer。
   - → **SSM 或 linear attention 层增强了对稀疏的鲁棒性**。

3. **上下文长度影响**：
   - 在 32K vs 128K 的 LOFT 测试中，稀疏行为一致，未见额外退化。
   - → **稀疏性泛化良好，不受 context length 增加影响**。

4. **任务复杂度影响**：
   - 稀疏性在单跳检索（RULER）、多跳 QA（LOFT）、数学推理（AIME）、**agentic coding（SWE-Bench）** 中均稳健。
   - → **稀疏不影响复杂推理能力**。

---

## 4. 关键结论和发现

### 论文的主要发现
1. **Dense Attention 是理论幻觉**：
   - 当 $d < N$ 时，attention 输出必然发生信息坍缩（embedding bottleneck），无法区分所有 attention 分布。
   - 因此，“完全稀疏”不是妥协，而是更合理的目标。

2. **现代 LLM 天然具备稀疏鲁棒性**：
   - 即使未经稀疏训练，当前主流模型（尤其是大模型和 hybrid 架构）对 inference-time context sparsity 极其鲁棒。
   - Qwen3.5-27B 在多个任务上可承受 **50×~100× 稀疏而不失性能**。

3. **稀疏可带来巨大系统收益**：
   - 自研 sparse decode kernel 在 H100 上实现 **最高 76× 的推理加速**。
   - 即使计入 indexer 开销（如 Double Sparsity），仍能获得 **>2.8× 的净加速**。

4. **稀疏应成为未来设计的第一性原理**：
   - 不应再将 dense attention 视为必要组件。
   - 应推动从 **architecture design → training → inference → hardware** 全栈围绕稀疏构建。

---

### 方法的局限性
1. **当前仍为 inference-time 技术**：
   - 所有实验均未修改训练流程。若能在训练中引入稀疏，潜力更大。
2. **依赖高质量 indexer**：
   - Oracle top-k 是理想情况；实际部署需高效准确的 top-k selection（如 vAttention、H2O、Scissorhands）。
3. **服务端稳定性问题**：
   - 在 SWE-Bench 实验中，稀疏配置出现更多 `InternalServerError` 和 `Timeout`，源于 `sparse-attention-hub` 后端不稳定，非模型质量问题。
4. **小模型表现不佳**：
   - 小模型（<7B）对 deterministic top-k 敏感，需借助 vAttention 等机制缓解。

---

### 未来工作方向
1. **训练时显式引入稀疏性**：
   - 设计新的 training objective 鼓励模型适应稀疏 context access。
2. **专用硬件支持稀疏**：
   - 当前 GPU 并非为稀疏优化，未来可设计专用于 sparse attention 的芯片架构。
3. **动态稀疏策略**：
   - 根据 query 动态调整 sparsity level，平衡效率与精度。
4. **扩展至 prefill 阶段**：
   - 当前 focus 在 decode，但 prefill 同样可受益于 sparsity（如 DeepSeek-V3 已展示）。
5. **构建统一的 sparse LLM 生态**：
   - 从 tokenizer → model → KV Cache → scheduler 全链路支持稀疏。

---

> 🔗 **项目资源**  
> - GitHub: [https://github.com/skylight-org/sparse-attention-hub](https://github.com/skylight-org/sparse-attention-hub)  
> - Project Page: [https://sky-light.eecs.berkeley.edu](https://sky-light.eecs.berkeley.edu)

</details>

---

### 5. [CoRe-Code: Collaborative Reinforcement Learning for Code Generation](https://arxiv.org/abs/2605.24812)

**Authors**: Zhihao Dou, Qinjian Zhao, Zhongwei Wan, Xiaoyu Xia, Sumon Biswas  
**Category**: cs.AI  
**Published**: 2026-05-26  
**Score**: 10.5  
**Type**: new  
**ArXiv ID**: 2605.24812v1  

#### Abstract
Large language models (LLMs) have achieved strong performance in code generation, but most methods rely on autoregressive decoding without global planning, often leading to locally coherent yet globally suboptimal solutions (e.g., failing test cases or inefficient complexity). While recent approache...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# CoRe-Code: Collaborative Reinforcement Learning for Code Generation 论文总结

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
大型语言模型（LLMs）在代码生成任务中表现出色，但大多数方法依赖于**自回归解码（autoregressive decoding）**，缺乏全局规划能力，导致生成的代码虽然局部连贯，但在全局上可能次优（如无法通过测试用例、时间复杂度高）。现有的多智能体系统（MAS）虽引入了角色分工（如规划者、编码者、测试者），但由于**角色专业化不足和协作效率低**，性能提升有限。

此外，作者提出并量化了一个新概念——**协作增益（Collaboration Gain, CG）**，用于衡量辅助智能体对最终代码生成者的实际帮助程度。实验表明，许多现有MAS方法的CG值很低甚至为负，说明其协作机制并未有效发挥作用。

### 提出了什么新方法或新思路
本文提出了 **CoRe-Code**（Collaborative Reinforcement Code），一个基于**协作感知强化学习**（collaborative reinforcement learning）的多智能体代码生成框架，核心创新如下：

- **Planner-Coder 范式**：采用简单的两阶段架构，由 **Planner Agent** 生成高层算法计划，**Coder Agent** 将其转化为可执行代码。
- **Algorithmic Thought**：提出一种结构化的计划表示方式，将算法思维分解为四个部分：
  - Input-Output Definition
  - Linear Progression
  - Conditional Logic
  - Iteration
  这种结构使计划更贴近编程语义，增强可解释性和可执行性。
- **Collaborative GRPO**：基于 **Group Relative Policy Optimization (GRPO)** 设计了一种协作式RL训练框架，利用下游代码执行结果作为**可验证奖励**（verifiable rewards）来联合优化两个Agent。
  - **Planner RL 阶段**：以Coder生成代码的**正确率**（Pass Rate）和**时间复杂度**（Time Complexity）作为间接奖励信号，优化Planner生成高质量计划的能力。
  - **Coder RL 阶段**：以代码正确性和**空间复杂度**（Space Complexity）作为奖励，优化Coder忠实执行计划并生成高效代码的能力。
- **通用性设计**：CoRe-Code 不仅限于 Planner-Coder 架构，还可扩展至其他多智能体框架（如MapCoder中的Retrieval和Debugging Agent），展示了其灵活性和可扩展性。

### 相比现有方法的优势
- **更高的协作增益（CG）**：通过可验证的执行反馈实现真正的协同进化，显著提升了Planner与Coder之间的协作效率。
- **更强的泛化能力**：在多种难度的任务（从基础函数到竞赛级编程）上均表现优异。
- **更好的代码质量**：不仅提高准确率，还生成更高效（更低运行时、内存占用）和更可靠（更低失败率）的代码。
- **无需额外推理开销**：相比需要多次反思或检索的多轮迭代方法（如Reflexion、MapCoder），CoRe-Code 推理成本更低，效率更高。

---

## 2. 核心实验方法和设置

### 使用了哪些数据集
实验在四个具有不同难度级别的基准上进行：
- **LiveBench**：较新的、污染较少的LLM评测基准，包含基础编程任务。
- **MBPP**（Mostly Basic Python Problems）：基础Python函数级编程任务。
- **CodeContests**：竞赛级编程任务，挑战算法设计与复杂度管理。
- **CodeForces**：高难度在线编程竞赛平台任务，代表最复杂的场景。

### 实验设置和评估指标

#### 评估指标
- **准确性**：
  - `Pass@1`：首次生成即正确的比例
  - `Pass@5`：最多尝试5次中至少一次正确
  - `APR`（Average Pass Rate）：平均通过测试用例的比例
- **效率与可维护性**：
  - `Runtime`（↓）：平均执行时间
  - `MU`（Memory Usage, ↓）：内存消耗
  - `CC`（Cyclomatic Complexity, ↓）：圈复杂度，衡量代码可维护性
- **可靠性**：
  - `FR`（Failure Rate, ↓）：执行失败率
  - 细分错误类型：`TOE`（Timeout Error）、`VE`（Value Error）、`TE`（Type Error）
- **计算成本**：
  - `Inference Time`：推理耗时

### 基线方法对比
#### 强化学习类基线（RL-based）：
- **GRPO**：原始的GRPO算法
- **Focused-DPO**：聚焦于错误点的偏好优化
- **CURE**：课程学习增强的RL方法
- **CodeRL+**：基于执行语义对齐的RL方法

#### 多智能体类基线（Multi-Agent）：
- **SCoT**：Self-Consistent Chain-of-Thought
- **Reflexion**：基于口头强化学习的语言智能体
- **MapCoder**：包含检索、规划、编码、调试的完整多智能体框架

所有方法均在同一训练数据集上进行训练，确保公平比较。

---

## 3. 主要实验结果和性能指标

### 关键性能数据（以 Qwen2.5-14B-Coder-Instruct 为例）

| Method | LiveBench Pass@1 | MBPP Pass@1 | CodeContests Pass@1 | CodeForces Pass@1 |
|--------|------------------|-------------|---------------------|-------------------|
| GRPO | 45.5 | 80.7 | 33.7 | 12.9 |
| Focused-DPO | 41.9 | 78.4 | 31.7 | 9.7 |
| CURE | 47.5 | 78.5 | 32.1 | 12.1 |
| CodeRL+ | 44.7 | 80.4 | 29.2 | 10.4 |
| **CoRe-Code** | **48.4** | **82.2** | **34.6** | **13.3** |

> ✅ 在所有基准上，CoRe-Code 均取得最优性能，尤其在复杂任务（CodeContests、CodeForces）上优势明显。

### 与基线方法的对比结果
- 在 **MBPP** 上，CoRe-Code 达到 **82.2 Pass@1**，优于第二名 CodeRL+（80.4）。
- 在最具挑战性的 **CodeForces** 上，CoRe-Code 达到 **13.3 Pass@1**，显著高于其他方法（最高不超过12.9）。
- 在 **APR** 指标上全面领先，表明其生成的代码能通过更多测试用例，鲁棒性更强。
- **Collaboration Gain (CG)** 在训练过程中持续上升（见图4），证明Planner与Coder的协作能力随训练不断增强。

### 消融实验结果（Ablation Study）
使用 Qwen2.5-7B-Coder-Instruct 进行消融分析：

| Method | MBPP Pass@1 | CodeContests Pass@1 | CodeForces Pass@1 |
|--------|-------------|---------------------|-------------------|
| w/o all RL | 68.5 | 22.6 | 8.9 |
| w/o Planner RL | 71.3 | 25.4 | 10.2 |
| w/o Coder RL | 72.9 | 26.7 | 9.7 |
| **CoRe-Code (full)** | **73.9** | **27.4** | **11.7** |

> 🔍 结果显示：
> - 移除任一RL组件都会导致性能下降；
> - 同时优化Planner和Coder效果最佳，二者存在互补效应；
> - Planner RL 对复杂任务提升更大，Coder RL 更利于提升基础任务表现。

---

## 4. 关键结论和发现

### 主要发现
1. **协作是关键瓶颈**：现有MAS方法因缺乏有效的协作机制而难以超越单Agent模型；CoRe-Code 通过**可验证奖励驱动的协同RL**解决了这一问题。
2. **结构化规划至关重要**：Algorithmic Thought 显著提升了Planner输出的清晰度和可执行性，是实现高效协作的基础。
3. **双向反馈提升整体性能**：Coder的执行结果反向指导Planner优化，形成正向循环，实现了“计划→执行→反馈→改进”的闭环。
4. **通用性强**：CoRe-Code 可无缝集成到MapCoder等复杂框架中，分别优化Retrieval Agent和Debugging Agent，均带来一致性能提升（见Table 4）。
5. **效率与性能兼得**：尽管是多Agent架构，但CoRe-Code 的推理时间仍低于或接近 Reflexion 和 MapCoder，实现了**高性能与高效率的平衡**。

### 方法的局限性
- 当前实验集中在开源模型和代表性基准上，尚未覆盖更多模型家族（如Llama系列）。
- 采用固定的Planner-Coder交互格式，未探索更灵活的通信机制（如动态对话）。
- 未报告误差条（error bars）或统计显著性检验，在严谨性方面略有欠缺（见Checklist Q7）。

### 未来工作方向
- 探索更复杂的多智能体拓扑结构（如树状、图状协作网络）。
- 引入动态角色切换机制，让Agent根据任务自动选择扮演Planner或Coder。
- 扩展至端到端软件工程流程，整合Requirement Analysis、Testing、Documentation等更多角色。
- 探索轻量化部署方案，降低多Agent系统的资源消耗。

---

> 📌 **总结一句话**：  
> CoRe-Code 通过**结构化规划 + 协作感知强化学习**，首次实现了多智能体代码生成中真正高效的“计划-执行”协同，显著提升了代码的准确性、效率与可靠性，为下一代AI编程助手提供了新范式。

</details>

---

### 6. [NeurIPS: Neuro-anatomical Inductive Priors for Sphere-based Brain Decoding](https://arxiv.org/abs/2605.24993)

**Authors**: Sijin Yu, Zijiao Chen, Zhenyu Yang, Zihao Tan, Jiakun Xu, Zhongliang Liu, Shengxian Chen, Wenxuan Wu, Xiangmin Xu, Xin Zhang  
**Category**: cs.AI  
**Published**: 2026-05-26  
**Score**: 10.5  
**Type**: new  
**ArXiv ID**: 2605.24993v1  

#### Abstract
Current fMRI decoders face a performance-fidelity trade-off where efficient ID encoders outperform geometrically faithful surface-based models. We argue this is partly driven by inefficient surface tokenization and the failure to use anatomy as a predictive signal. We present NeurIPS, a framework th...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：NeurIPS: Neuro-anatomical Inductive Priors for Sphere-based Brain Decoding

---

## 1. 论文的主要贡献和创新点

### 解决的问题
当前基于 **fMRI** 的图像重建模型面临一个“**性能-保真度权衡**”（performance-fidelity trade-off）：
- **1D-vector-based 方法**（如 MindBridge）计算高效，在高维语义指标上表现优异，但**丢弃了大脑皮层的几何结构**，牺牲了空间对齐能力。
- **surface-based 方法**（如 SIM、Yu et al., 2025）保留了皮层拓扑结构，理论上更利于跨被试对齐，但因**token 数量过多**和**无法有效建模个体解剖差异**，导致训练效率低、收敛慢、泛化差。

本文指出这一权衡并非本质限制，而是由两个架构缺陷造成：
1. **低效的表面 tokenization**：在全脑半球进行球面卷积，产生大量冗余 token。
2. **将解剖变异视为噪声**：传统方法通过 subject ID 或 adapter 进行条件控制，易导致模型记忆个体身份而非学习通用的“结构-功能”映射规则。

---

### 提出的新方法与创新思路

NeurIPS 提出一种**以神经解剖学为归纳先验**（neuro-anatomical inductive priors）的框架，通过以下两大创新解决上述问题：

#### (A) Selective ROI Spherical Tokenizer (SRST)
- **任务对齐的 tokenization**：仅在预定义的视觉皮层 ROI（Region of Interest）内执行球面卷积，避免处理非视觉区域。
- **效率提升显著**：在 fsaverage6 空间中，顶点数从全脑的 81,924 减少到 9,488，**减少 88.4%**，大幅降低内存与计算开销。
- **双通路输出**：生成局部 token（保留精细几何模式）和全局 token（提供场景上下文），兼顾细节与语义。

#### (B) Structure-Guided Mixture of Experts (SG-MoE)
- **解剖特征驱动路由**：用个体的 **cortical thickness、curvature、sulcal depth、surface area** 等物理结构特征作为 MoE 路由器输入，替代传统的 subject ID。
- **强制学习通用规则**：迫使专家按“结构-功能”轴专业化，提升跨被试泛化能力，避免身份记忆。
- **稀疏激活**：每 token 激活 top-k=6 个专家，保持计算效率。

---

### 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| **性能** | 在 surface-based 模型中达到 SOTA，且与最强 1D 方法（如 MindBridge）性能相当 |
| **效率** | 收敛速度极快：**10 epochs 即可完成微调**，而基线需 200–600 epochs |
| **个性化适应** | 仅用新被试 **20% 数据 + 1 epoch 微调**，即可达到其最终性能的 90% |
| **可扩展性** | 随训练队列扩大（4→8 subjects），性能下降最小，鲁棒性强 |
| **可解释性** | 路由行为依赖于脑区位置而非 subject ID，符合神经科学原理 |

---

## 2. 核心实验方法和设置

### 数据集
- **Natural Scenes Dataset (NSD)** (Allen et al., 2022)：大规模 fMRI-图像配对数据集。
  - 包含 8 名被试（subj01–08），每人观看约 10,000 张 COCO 图像。
  - 共享测试集：1,000 张所有被试共同观看的图像。
  - 输入：GLM-estimated beta weights，表示刺激锁定的 BOLD 响应。

### 实验设置
- **训练策略**：
  - 多被试联合训练（multi-subject pretraining）
  - 新被试适应：在 3 名被试上预训练后，在 held-out subject 上进行 fine-tuning
- **输入维度**：
  - 使用 FreeSurfer 的 `fsaverage6` 球面网格
  - 视觉 ROI 来自 NSD-General parcellation（共 9,488 vertices）
- **硬件资源**：单张 NVIDIA A800 GPU，训练时长约 138 秒/epoch

### 评估指标
| 类型 | 指标 |
|------|------|
| **低级视觉保真度** | PixCor（像素相关性）、SSIM（结构相似性） |
| **高级语义相似性** | Alex(2)/Alex(5)、Incep（InceptionV3）、CLIP（ViT-L/14） |
| **距离度量** | Eff（EfficientNet-B1）、SwAV（SwAV-ResNet50）↓（越小越好） |

### 基线方法对比
- **1D-vector-based**：
  - Mind-Vis, Takagi & Nishimoto (2023), MindEye, MindBridge, UMBRAE, NeuroPictor
- **Sphere-based**：
  - Gu et al. (2023), Yu et al. (2025), SIM (Dahan et al., 2025)

> 所有方法均使用相同的 **Versatile Diffusion** 作为生成后端，确保公平比较。

---

## 3. 主要实验结果和性能指标

### 关键性能数据（Table 1）

| Method | PixCor↑ | SSIM↑ | Alex(5)↑ | CLIP↑ | Eff↓ | SwAV↓ |
|--------|---------|-------|---------|-------|------|--------|
| **MindBridge** (1D) | 0.151 | 0.263 | 95.5% | **94.7%** | 0.712 | 0.418 |
| **SIM** (Sphere) | 0.119 | 0.260 | 90.4% | 89.4% | 0.733 | 0.448 |
| **NeurIPS (Ours)** | **0.248** | **0.370** | **95.2%** | **93.2%** | **0.663** | **0.404** |

> ✅ NeurIPS 是目前 **sphere-based 方法中的 SOTA**，且在多个指标上接近甚至超越最强 1D 方法。

---

### 与基线方法的对比结果

#### (1) 快速新被试适应（Figure 4 & 5）
- 仅用 **20% 数据 + 1 epoch 微调**：
  - NeurIPS 已能生成语义连贯的图像
  - 性能接近 fully-trained 模型（dashed line）
- 在 **10 epochs 内达到渐近性能**，而 SIM/MindBridge 需数百 epochs

#### (2) 可扩展性测试（Figure 5 右图）
- 当训练队列从 4 扩展到 8 名被试：
  - SIM 的 CLIP 分数下降 **2.0 pts**
  - NeurIPS 仅下降 **0.6 pts**
- 表明 NeurIPS 更好地利用了解剖变异性作为信号而非噪声

---

### 消融实验结果（Table 2）

| 设置 | CLIP↑ | Alex(5)↑ | 说明 |
|------|-------|---------|------|
| Full Model (Ours) | **93.2%** | **95.2%** | — |
| w/o global token | 89.4% | 92.7% | 全局 token 对语义建模至关重要 |
| subject ID gating | 92.7% | 94.9% | 仍优于 baseline，但不如 anatomy routing |
| full brain tokenizer | 91.0% | 91.7% | 全脑处理反而性能下降，验证 ROI 有效性 |
| no anatomy / random anatomy | ~90.2% / ~92.0% | ~93.4% / ~94.4% | 解剖信息缺失导致性能下降 |
| anatomical swap | 91.9% | 94.4% | 交换他人解剖特征也损害性能 |

> 🔍 结论：性能增益来自真正的 anatomy-conditioned routing，而非参数数量或身份记忆。

---

## 4. 关键结论和发现

### 主要发现
1. **解剖结构是强大的归纳先验**：将 cortical thickness、curvature 等作为 MoE 路由信号，可显著提升跨被试泛化能力。
2. **任务对齐的 tokenization 更高效**：限制在视觉 ROI 内建模，不仅节省算力，还能提高信息密度。
3. **surface-based 模型无需牺牲性能**：通过 SRST + SG-MoE，NeurIPS 实现了与 1D 方法相当的性能，同时保留了几何保真度。
4. **快速个性化成为可能**：仅需少量数据和极短训练时间即可适配新用户，具备实际部署潜力。
5. **模型行为具有神经科学合理性**：
   - 路由决策高度依赖脑区位置，几乎不依赖 subject ID（Figure 6A）
   - 不同被试间，解剖相似者具有更相似的路由模式（Table 9）

---

### 方法的局限性
- **依赖高质量皮层重建与配准**：性能受限于 FreeSurfer 等工具的分割与球面映射质量。
- **当前聚焦静态视觉任务**：ROI 设计针对视觉刺激，多模态或动态任务需扩展至全脑。
- **未完全整合感知路径的几何信息**：目前仅在 semantic path 中使用 SRST，perception path 仍为 1D 向量输入。

---

### 未来工作方向
- 将 SRST 扩展至 perception decoder，实现全流程几何一致性。
- 探索动态 ROI 选择机制，适应不同认知任务。
- 结合 functional alignment 与 anatomical routing，进一步提升零样本迁移能力。
- 应用于临床场景，如脑机接口个性化解码、神经系统疾病 biomarker 发现。

---

> 📌 **一句话总结**：  
> NeurIPS 通过引入 **Selective ROI Spherical Tokenizer (SRST)** 和 **Structure-Guided MoE (SG-MoE)**，首次实现了高效、可扩展、解剖感知的 surface-based fMRI 解码，在性能、速度与泛化性之间取得突破性平衡。

</details>

---

### 7. [MATO: Multi-objective Personalized Alignment with Test-time Optimization for Large Language Models](https://arxiv.org/abs/2605.25342)

**Authors**: Linhao Luo, Thuy-Trang Vu, Van-Anh Nguyen, Junae Kim, Gholamreza Haffari, Dinh Phung  
**Category**: cs.CL  
**Published**: 2026-05-26  
**Score**: 10.5  
**Type**: new  
**ArXiv ID**: 2605.25342v1  

#### Abstract
Aligning large language models (LLMs) with diverse and multifaceted user preferences is a fundamental challenge in personalized AI systems. Existing multi-objective alignment methods either rely on costly training or require pre-trained reward models for each preference, making it difficult for them...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：MATO: Multi-objective Personalized Alignment with Test-time Optimization for Large Language Models

---

## 1. 论文的主要贡献和创新点

### 解决的问题
现有的多目标对齐（multi-objective alignment）方法存在以下局限性：
- **训练型方法**（如 MORLHF、RiC）需要为不同的偏好组合进行额外的模型训练，成本高昂且难以扩展。
- **依赖外部 Reward Model** 的测试时对齐方法（如 PARM、PAD）虽然避免了训练，但仍需为每个偏好预训练独立的 Reward Model，当用户偏好动态变化时适应性差。
- **纯提示法**（prompt-based）虽灵活高效，但在处理多个竞争性目标时缺乏可控性（steerability），容易忽略某些偏好或无法平衡冲突目标。

### 提出的新方法：MATO
本文提出 **MATO**（Multi-objective personalized Alignment with Test-time Optimization），一种无需训练、不依赖外部 Reward Model 的多目标个性化对齐框架。其核心思想是将个性化对齐建模为一个**测试时优化**（test-time optimization）问题，在解码过程中动态调整多个目标的权重并引导生成过程。

#### 创新模块：
1. **Reward Discovery Module**  
   从骨干 LLM 自身中直接恢复各目标的奖励信号，无需外部 Reward Model。通过在提示中加入单个偏好描述（如“请保持友好”），利用闭式解推导 token-level 奖励：
   $$
   R_k(y_i|x, y_{<i}) = \beta \log \frac{\pi_{\text{base}}(y_i|x, y_{<i}, c_k)}{\pi_{\text{base}}(y_i|x, y_{<i})}
   $$

2. **Weight Optimization Module**  
   动态调整各目标权重，防止某些目标被过度强调而其他被忽视。基于已生成部分的累积奖励，采用带正则化的最小化问题来更新权重：
   $$
   W^* = \arg\min_W \sum_k w_k R_k(x, y_{<i}) + \tau D_{KL}(W \| W_{\text{init}})
   $$
   该问题有**闭式解**，可高效计算，既保留用户初始偏好先验，又动态补偿表现不佳的目标。

3. **Online Optimization Module**  
   使用 Follow-the-Regularized-Leader (FTRL) 算法在线优化 token 分布，逐步逼近最优策略。以合并后的分布为锚点，最大化其与 base policy 的散度，同时保持稳定性。

### 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| **无需训练** | 完全 training-free，适用于任意 LLM 和偏好组合 |
| **无需 Reward Model** | 从 backbone LLM 中自提取 reward，摆脱对外部模型依赖 |
| **强可控性**（steerability） | 支持用户指定偏好权重，并能有效实现帕累托前沿（Pareto front） |
| **动态平衡能力** | 能在生成过程中自动识别并提升被忽视目标的权重 |
| **模型无关性**（model-agnostic） | 可插拔于不同规模和架构的 LLM |

---

## 2. 核心实验方法和设置

### 数据集
- **Multifaceted Dataset** [12]：用于多目标个性化对齐评估。包含 945 条查询，每条关联 4 个自然语言描述的偏好，覆盖 4 个维度（背景知识、无害性、信息量、风格），共 107 种独特偏好组合。
- **HH-RLHF Dataset** [1]：用于评估**可控性**（steerability）。选取 “helpfulness” 和 “humor” 两个目标，通过改变权重比例（从 1:0 到 0:1）绘制帕累托前沿。

### 实验设置
- **骨干模型**：Qwen3-0.6B, Qwen3-8B, Llama-3.2-1B, Llama-3.1-8B
- **参数设置**：温度 $\tau=1$, 在线优化步数 $T=80$, 其他超参 $\alpha=0.5, \lambda=1.0, \nu=10$

### 评估指标
#### 多目标对齐性能：
- **AMR**（All Preference Match Rate）：所有偏好评分均 ≥3 的响应占比
- **APS**（Average Preference Score）：各偏好得分平均值
- **Worst**：单个响应中最差偏好的最低分（衡量平衡性）

#### 可控性评估：
- 使用两个预训练 Reward Model（helpfulness 和 humor）输出连续奖励值
- 绘制不同权重下的**经验帕累托前沿**（empirical Pareto front）

### 基线方法对比
| 类别 | 方法 |
|------|------|
| **Training-free** | Base LLM, Preference Prompt [12], Linear Alignment [6], CoS [8], Amulet [32], OPAD [37] |
| **Training-based** | MORLHF [13], RiC [31], MOD [17] |

---

## 3. 主要实验结果和性能指标

### 关键性能数据（Table 1）
在 **Multifaceted 数据集** 上，MATO 在所有骨干模型和指标上均优于基线：

| 方法 | Qwen3-8B (AMR / APS / Worst) | Llama-3.1-8B (AMR / APS / Worst) |
|------|-------------------------------|----------------------------------|
| Base LLM | 0.43 / 3.66 / 2.34 | 0.34 / 3.36 / 2.04 |
| Preference Prompt | 0.70 / 4.19 / 3.23 | 0.66 / 3.97 / 2.96 |
| OPAD | 0.74 / 4.28 / 3.39 | 0.68 / 4.03 / 3.10 |
| **MATO** | **0.75 / 4.30 / 3.42** | **0.73 / 4.08 / 3.22** |

- **Worst 指标提升显著**：表明 MATO 更好地平衡了各目标，避免任一偏好被忽略。
- 即使在小模型（如 Qwen3-0.6B）上也保持领先，说明方法鲁棒性强。

### 与基线方法的对比结果
- **优于所有 training-free 方法**：特别是在 Worst 指标上优势明显，证明其动态权重机制有效。
- **优于 training-based 方法**：尽管后者经过专门训练，但因训练-测试分布偏移（train-test shift）导致实际对齐效果较差。
- **帕累托前沿更优**（Figure 5）：
  - Training-free 方法（如 Preference Prompt）虽整体性能高，但帕累托前沿分布稀疏，**可控性差**。
  - **MATO 实现了 training-free 方法中最好的帕累托前沿**，兼具高性能与强可控性。

### 消融实验结果（Table 2）
在 Qwen3-0.6B 上进行消融研究：

| 方法 | AMR | APS | Worst |
|------|-----|-----|-------|
| MATO（完整） | 0.27 | 2.99 | 1.87 |
| w/o weight optimization | 0.26 | 2.88 | 1.80 |
| w/o online optimization | 0.24 | 2.83 | 1.83 |
| w/o both | 0.21 | 2.73 | 1.62 |

- **两个模块均有贡献**，尤其是 **weight optimization** 对 Worst 指标影响最大，验证了其在平衡多目标中的关键作用。

---

## 4. 关键结论和发现

### 主要发现
1. **测试时优化是实现多目标个性化对齐的有效范式**：无需训练即可实现高质量、可控制的对齐。
2. **从 backbone LLM 中自提取 reward 是可行且高效的**：避免了对外部 Reward Model 的依赖，提升了灵活性。
3. **动态权重调整机制能显著改善多目标平衡性**：通过闭式解实时重加权表现不佳的目标，实现了帕累托改进（Pareto-improving alignment）。
4. **MATO 在性能、可控性和通用性之间取得了良好平衡**：在多个 LLM 和数据集上 consistently outperforms 强基线。

### 方法的局限性（Limitations）
- 依赖 backbone LLM 的指令跟随能力（instruction-following capability）来执行 reward discovery；若基础模型理解能力弱，则 reward 可能不准。
- 所有目标必须能用自然语言表达，限制了对隐式或复杂目标的应用。
- 尽管免训练，但在线优化引入了一定推理延迟（约 0.16s/token），高于标准解码。

### 未来工作方向
- 探索更高效的在线优化算法以降低延迟。
- 扩展至非语言形式的目标表示（如向量、图像等）。
- 结合用户反馈进行闭环动态调优。
- 应用于更复杂的多模态或多轮对话场景。

---

> ✅ **总结一句话**：  
> **MATO 提出了一种无需训练、无需 Reward Model 的 test-time optimization 框架，通过 reward discovery + dynamic weight optimization + online optimization 三阶段机制，实现了强可控、高平衡性的多目标个性化对齐，在多个 LLM 上显著优于现有方法。**

</details>

---

### 8. [TSFLora: Token-Compressed Split Fine-Tuning for Wireless Edge Networks](https://arxiv.org/abs/2605.23988)

**Authors**: Xianke Qiang, Zheng Chang, Li Wang, Ying-Chang Liang  
**Category**: cs.DC  
**Published**: 2026-05-26  
**Score**: 10.5  
**Type**: new  
**ArXiv ID**: 2605.23988v1  

#### Abstract
Adapting large AI models (LAMs) to personalized edge data is challenging because wireless devices have limited memory, computation, and uplink capacity. Federated fine-tuning preserves data privacy but still requires each device to host the full model, while split learning reduces device memory at t...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：TSFLora: Token-Compressed Split Fine-Tuning for Wireless Edge Networks

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
在无线边缘网络中，**大型AI模型（LAMs）的个性化微调面临三大挑战**：
- **设备内存受限**：边缘设备无法承载完整的LAM骨干网络；
- **上行通信开销大**：Split Learning 中需上传大量中间激活（activations），导致高带宽消耗；
- **服务器端计算瓶颈**：随着客户端增多，服务器处理长token序列的计算负担加重。

传统方法如 **Federated Learning (FL)** 要求设备存储完整模型；而 **Split Learning (SFL)** 虽缓解内存压力，但引入了高昂的激活传输成本。

---

### 🚀 提出的新方法：TSFLora
提出 **TSFLora** —— 一种**面向边缘网络的 token 压缩型分裂微调框架**，结合以下关键技术：
- **Attention-guided token selection**：基于[CLS] token注意力得分选择最重要的patch tokens；
- **Token merging**：将被丢弃的tokens通过加权平均合并为一个“merged token”，保留全局信息；
- **Low-bit activation quantization**：对压缩后的token进行低比特量化（如4-bit或8-bit）以进一步减少通信量；
- **LoRA-based adaptation**：仅训练低秩适配器（LoRA），显著降低可训练参数数量和内存占用；
- **Split Federated Learning 架构**：模型在设备与服务器之间切分，设备仅运行前端层。

> 🔑 **核心思想**：在分割层**压缩中间token序列再传输**，从而同时减少**上行通信流量**和**服务器侧计算负载**，且不修改冻结的主干模型。

---

### ⚖️ 相比现有方法的优势
| 方法 | 内存节省 | 通信效率 | 准确率保持 | 是否支持边缘部署 |
|------|--------|---------|-----------|----------------|
| FL / FedLoRA | ❌ 高内存需求 | ❌ 全模型更新 | ✅ 高 | ❌ 不可行 |
| SFL / SplitLoRA | ✅ 设备内存下降 | ❌ 激活传输大 | ✅ 接近集中式训练 | ✅ 可行 |
| **TSFLora（本文）** | ✅✅ 更优（最多41%） | ✅✅ 最高（最高6.8×压缩） | ✅✅ 竞争性精度 | ✅✅ 更实用 |

---

## 2. 核心实验方法和设置

### 📊 数据集
- **CIFAR-10**
- **CIFAR-100**
- **TinyImageNet**

均采用图像分类任务，在 **IID** 和 **non-IID**（Dirichlet分布 α=0.5）两种数据划分下测试泛化能力。

---

### 🧪 实验设置
- **模型架构**：ViT-Small/32, ViT-Base/32, ViT-Large/32（预训练权重来自 `timm`）
- **LoRA配置**：rank = 32, 插入Transformer块中
- **训练轮数**：50 communication rounds
- **每轮参与设备数**：随机选取10 out of 50
- **批大小（batch size）**：64
- **学习率**：0.1
- **设备模拟环境**：使用NVIDIA L20 GPU虚拟化为多个资源受限设备（见Table II），模拟真实边缘异构性
- **通信协议**：Wi-Fi over WebSocket

---

### 📈 评估指标
| 指标类别 | 具体指标 |
|--------|--------|
| **性能指标** | Top-1 Accuracy (%) |
| **系统效率** | 上行通信开销（bits）、峰值设备内存（MB）、端到端执行时间（ms） |
| **收敛行为** | 准确率随训练轮次变化曲线 |
| **压缩效果** | 通信压缩比（Compression Ratio） |

---

### 🔁 基线方法对比
- **LocalLoRA**：本地独立微调，无协作
- **FedLoRA**：标准联邦LoRA微调
- **SplitLoRA**：基础分裂LoRA，无压缩
- **SFLora**：带量化版本的SplitLoRA
  - SFLora (8-bit)
  - SFLora (4-bit)
- **TSFLora（本文）**
  - TSFLora (8-bit, 40 tokens)
  - TSFLora (8-bit, 30 tokens)

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据（Table III & Fig. 2–4）

#### ✅ 准确率表现（Top-1 Accuracy）
| 模型 | 方法 | CIFAR-100 (non-IID) | TinyImageNet (non-IID) |
|-----|------|--------------------|-----------------------|
| ViT-Base/32 | SFLora (8-bit) | 89.97% | 84.67% |
| ViT-Base/32 | **TSFLora (8-bit, 40 tokens)** | **89.04%** | **84.35%** |
| ViT-Base/32 | TSFLora (8-bit, 30 tokens) | 87.10% | 82.84% |

> 💡 即使在强压缩条件下（40 tokens + 8-bit），TSFLora仍能保持接近SFLora的准确率，仅轻微下降约1%，远优于其他轻量方案。

---

#### 📉 通信与资源节省
| 指标 | 结果 |
|------|------|
| **最大通信压缩比** | **高达 6.8×**（相比原始激活传输） |
| **上行通信开销降低** | 在4-bit + 30 tokens下 >80% reduction |
| **设备峰值内存节省** | 最多达 **41%**（vs. SplitLoRA等） |
| **通信负载示例**（ViT-B/16） | 原始激活传输：233.5 MB/round → 经TSFLora压缩后显著下降 |

> 示例：在TinyImageNet上，从50 tokens降至30 tokens，通信内存由 ~20MB → ~12MB（↓40%），几乎无精度损失。

---

#### ⏱️ 端到端延迟优化（Fig. 4c–f）
- 在 **10 Mbps 上行带宽**下，TSFLora 显著缩短每轮训练时间；
- 使用 **4-bit量化** 后，延迟对带宽变化更鲁棒；
- 极端压缩（如2-bit + 10 tokens）虽进一步降延迟，但带来明显精度损失，验证了**权衡必要性**。

---

#### 🔍 消融实验分析（Ablation Study）
- **Token selection 数量影响**：
  - 从50→40 tokens：精度基本不变；
  - 50→30 tokens：略有下降，但通信收益显著。
- **量化位宽影响**：
  - 2-bit：精度波动较大，尤其在浅层/深层split时敏感；
  - 4-bit及以上：性能稳定，推荐实际部署使用。
- **Split layer位置选择**：
  - 中间层切分（middle split）在低比特下更稳健；
  - 浅层或深层split对量化误差更敏感。

> ✅ 验证了 **token selection + quantization 的互补性**：前者减元素个数，后者减每个元素比特数。

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **Token压缩是提升SFL效率的关键路径**：
   - 在分割层压缩token序列，可**同步降低通信开销与服务器计算负担**；
   - 注意力引导的选择机制有效保留关键语义信息。

2. **TSFLora实现高效-精度平衡**：
   - 在多种ViT模型和数据集上，达到**竞争性准确率**的同时，实现：
     - **6.8×通信压缩**
     - **41%内存节省**
   - 支持在典型4GB内存边缘设备（如Jetson系列）上部署。

3. **系统设计变量存在耦合关系**：
   - split layer `e`、token budget `K`、quantization bit-width `q` 共同决定系统可行性与性能；
   - 存在一个**帕累托最优区域**，需联合优化。

4. **低比特量化 + 中等token保留是最优实践**：
   - 推荐使用 **8-bit 或 4-bit + 30~40 tokens** 配置，在精度与效率间取得最佳平衡。

---

### ⚠️ 局限性
- **依赖Transformer结构特性**：当前方法基于ViT设计，token selection依赖[CLS]注意力机制，可能难以直接迁移到CNN或其他非attention架构；
- **动态token预算未自适应**：目前K固定或手动设定，缺乏根据网络状态自动调整的机制；
- **未考虑下行梯度压缩**：虽然文中提及梯度也经压缩维度返回，但未深入探索其进一步压缩潜力；
- **实验平台为仿真环境**：基于GPU虚拟化模拟边缘设备，尚未在真实IoT硬件（如Raspberry Pi）上全面验证。

---

### 🔮 未来工作方向
1. **自适应压缩策略**：根据信道条件、设备负载动态调节 `K` 和 `q`；
2. **跨模态扩展**：将TSFLora应用于视觉-语言模型或多模态边缘推理；
3. **硬件协同优化**：结合边缘芯片的INT4/INT2运算能力，实现端到端低比特加速；
4. **理论深化**：建立更精确的压缩误差传播模型，指导最优split layer选择；
5. **安全与隐私增强**：研究token压缩是否具有天然差分隐私属性，辅助保护原始输入信息。

---

> 🔗 **代码开源地址**：[https://github.com/XiankeQiang/TSFLora](https://github.com/XiankeQiang/TSFLora)

</details>

---

### 9. [A Tabular Schedule Abstraction for Communication-Aware Evaluation of Pipeline-Parallel LLM Training](https://arxiv.org/abs/2605.24006)

**Authors**: Daniel Barley, Jonathan Leis, Benjamin Klenk, Holger Fr\"oning  
**Category**: cs.DC  
**Published**: 2026-05-26  
**Score**: 10.5  
**Type**: new  
**ArXiv ID**: 2605.24006v1  

#### Abstract
Pipeline parallelism is a key technique for distributed training of large language models because it reduces per-device parameter and activation memory. However, comparing pipeline schedules is difficult: analytical models expose structural quantities such as bubble ratios, while end-to-end hardware...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：A Tabular Schedule Abstraction for Communication-Aware Evaluation of Pipeline-Parallel LLM Training

---

## 1. 论文的主要贡献和创新点

### ✅ 解决了什么问题
在大规模语言模型（LLM）训练中，**pipeline parallelism** 是降低单设备参数和激活内存的关键技术。然而，不同 **pipeline schedule**（如 GPipe、1F1B、Chimera、Hanayo）在实际系统中的表现差异显著，且受通信、依赖关系和内存交互影响极大。

现有评估方法存在两极分化：
- **分析模型（analytical models）** 虽能提供 bubble ratio、utilization 等结构性指标，但忽略了通信开销和依赖约束；
- **端到端硬件实验** 虽真实，但成本高、难以控制变量，不利于跨系统配置的系统性比较。

因此，如何在**保持结构可解释性的同时引入通信感知执行建模**，成为 pipeline schedule 比较的一大挑战。

---

### ✅ 提出的新方法与新思路

本文提出了一种 **统一的多抽象层次评估框架（unified multi-abstraction methodology）**，其核心是：

#### （1）**Tabular Schedule Abstraction（表格化调度抽象）**
- 将 pipeline schedule 表示为一个二维表 $ S \in (M \times P \cup \{0\})^{W \times T} $，其中：
  - $ W $：worker 数量
  - $ T $：时间槽（time slots）
  - $ M $：microbatches 集合
  - $ P $：执行阶段集合（如 `fwd`, `bwd`, `opt` 等）
- 每个单元格表示某个 worker 在某一时隙执行的任务或空闲状态。
- 这种表示方式**解耦了调度策略与执行代价**，便于统一建模与比较。

#### （2）**三层次评估体系**
通过将同一调度方案在三个抽象层级上进行分析，实现从理论到实践的平滑过渡：
1. **公式推理层（Formula-based Reasoning）**：基于闭式表达式计算 bubble ratio、peak memory 等。
2. **理想化调度表层（Idealized Schedule Tables）**：可视化 microbatch 流动、填充/排空行为、idle slots。
3. **通信感知仿真层（Communication-aware Execution Simulation）**：基于 Graphculon 框架生成带依赖关系的执行图，并模拟 compute、communication 和 overlap 效果。

---

### ✅ 相比现有方法的优势

| 优势维度 | 具体体现 |
|--------|---------|
| **方法论完整性** | 首次系统连接公式分析、结构表示与运行时仿真，支持跨抽象层级一致性验证 |
| **灵活性与通用性** | 表格式抽象适用于多种 schedule（GPipe, 1F1B, Chimera, Hanayo），易于扩展新调度策略 |
| **系统相关性建模能力** | 显式建模通信延迟（latency）、带宽（bandwidth）、compute-communication overlap，揭示真实瓶颈 |
| **设计指导意义强** | 支持“what-if”分析（如非对称 Chimera），帮助理解调度修改的实际影响 |

---

## 2. 核心实验方法和设置

### ✅ 使用的模型与配置
- **模型架构**：Megatron-style Transformer
  - 128 层 transformer blocks
  - hidden dimension: 4096
  - attention heads: 80
  - sequence length: 4096
  - 激活函数：GELU
- **并行策略**：仅启用 pipeline parallelism，固定全局 minibatch size
- **stage 数量 $ S $**：4 或 8
- **microbatch 数量 $ B $**：变化范围 8–256

> ⚠️ 注：未使用具体数据集，研究聚焦于**计算与通信行为建模**而非任务精度。

---

### ✅ 实验设置与系统建模

构建了一个 **3×3 的系统配置网格**，覆盖不同 compute 与 network 性能组合：

| 维度 | 设置 |
|------|------|
| **Baseline System** | 类似 NVIDIA DGX H100 节点：<br>- Compute: ~1 PFLOPs<br>- Memory BW: 34 TB/s, Latency: 50 ns<br>- Network BW: 50 GB/s, Latency: 500 ns |
| **Scaled Systems** | 分别将 compute 和 network 吞吐/延迟缩放 ±10×，形成：<br>- fast_cp / slow_cp<br>- fast_nw / slow_nw |

> 💡 fast_nw 可类比现代 NVLink/NVL72 架构下的高带宽环境。

---

### ✅ 评估指标

分为两大类：

#### （1）**利用率与运行时指标**
- **Bubble Ratio**：idle 时间占比（公式与表层）
- **Schedule Length (slots)**：总调度长度
- **Simulated Execution Time ($ T_{sim} $)**：模拟单步训练耗时
- **Idle Time Ratio ($ p_{idle} $)**：运行时中空闲比例

#### （2）**内存压力指标**
- **Peak Activation Memory**：各设备峰值激活内存
- **Persistent Memory**：参数、梯度、optimizer state 占用
- **Per-device Memory Footprint**：综合内存消耗

---

### ✅ 基线方法对比
对比以下四种同步 pipeline schedule：
| 方法 | 特点 |
|------|------|
| **GPipe** | Fill-then-drain 策略，简单但 bubble 大，activation retention 长 |
| **1F1B** | One-forward-one-backward，交替执行 fwd/bwd，减少 bubble 与 activation 内存 |
| **Chimera** | 双向流水线（bidirectional），通过反向传播路径提升利用率，但需参数复制 |
| **Hanayo** | 波浪式同步调度，在特定 $ S=B $ 下优化利用，限制较多 |

> Hanayo 仅在 $ (S,B)=(8,8) $ 下测试。

---

## 3. 主要实验结果和性能指标

### ✅ 关键性能数据与对比结果

#### （1）**GPipe vs 1F1B**
- **运行时等效性**：在所有建模系统下，两者 $ T_{sim} $ 几乎相同。
- **内存优势明显**：1F1B 的 activation memory peak 显著低于 GPipe（因更短的 retention interval）。
- **结论**：**1F1B 是更强的单向 baseline**，尤其适合内存受限场景。

#### （2）**Chimera 的表现高度依赖系统配置**
| 场景 | 表现 |
|------|------|
| **低 microbatch 数（B < 32） + fast_nw** | 明显优于 GPipe/1F1B，runtime 更低 |
| **高 microbatch 数 + slow_nw** | 因额外通信开销大而劣于 GPipe/1F1B |
| **总体趋势** | 仅在通信友好环境下有优势，否则被通信拖累 |

> 图4显示：在 slow_nw 系统中，增加 B 导致 Chimera runtime 上升，而 GPipe/1F1B 更稳定。

#### （3）**Hanayo 在其目标配置下有效但敏感**
在 $ (S,B)=(8,8) $ 下与 Chimera 对比如下（Table I）：

| 系统条件 | Hanayo 相对于 Chimera 的提速 |
|--------|-----------------------------|
| fast_nw / mid_nw | 平均 **12–14%** 加速，idle ratio 下降约 10% |
| slow_nw_fast_cp | **慢 12.32%**，idle 更高 |
| slow_nw_mid_cp | 仅快 **2.33%**

> 🔍 结论：Hanayo 在通信良好时表现优异，但在网络受限时反而更差。

#### （4）**Analytical Model 与 Simulation 不一致**
- 对 Chimera，公式预测的 bubble ratio 比实际调度表更低（更乐观），例如：
  - $(S,B)=(8,16)$：公式得 16%，表格得 26%
- 说明：**结构公式可能低估复杂调度的真实开销**

---

### ✅ 消融实验：非对称 Chimera 放置（Asymmetric Chimera）

尝试将 stage 划分不均匀地分配给两个反向 pipeline（如 1:2 分布），以缓解首 stage 内存压力。

#### 实验结果：
| 方面 | 发现 |
|------|------|
| **内存峰值** | ❌ 未降低全局 peak memory，仅使分布更均衡 |
| **运行时** | ✅ 在浅层 pipeline（$ S=4 $）+ fast_nw 条件下，获得 **~5% 速度提升** |
| | ❌ 在深层 pipeline（$ S=8 $）+ 小 microbatch 下反而变慢 |

> 📌 启示：看似合理的内存优化设计未必奏效，必须结合通信建模验证。

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **Schedule Rankings Are Not Abstraction-Invariant**
   > “结构上最优”的调度不一定在真实系统中表现最好。  
   > 例如：Chimera 在公式层面 bubble 最小，但在 slow_nw 下 runtime 最差。

2. **No Universal Winner Across Regimes**
   - **GPipe & 1F1B**：运行时等价，但 1F1B 内存更优 → 推荐作为默认 baseline
   - **Chimera**：仅在 low-B + fast-nw 下占优
   - **Hanayo**：在其设计点有效，但对通信极其敏感

3. **Communication Can Nullify Structural Advantages**
   - Bidirectional 或 wave-like 调度虽能减少 bubble，但若无法 overlap communication，则优势消失甚至逆转。

4. **Memory ≠ Just Activation**
   - 参数复制（如 Chimera）带来的 persistent memory 开销可能抵消 activation reduction 的好处。

5. **Simulation Reveals Non-Obvious Behavior**
   - 如非对称 Chimera 的 runtime 提升出现在预期之外的配置中，凸显仿真的必要性。

---

### ✅ 方法的局限性

| 局限 | 说明 |
|------|------|
| **未校准真实硬件** | Graphculon 是分析模型，非精确性能预测器 |
| **仅考虑同步调度** | 未涵盖 interleaved、zero-bubble 等异步或高级调度 |
| **忽略收敛性影响** | 所有调度假设训练语义一致，未比较 accuracy 或收敛速度 |
| **简化通信模型** | 使用 Hockney 模型，未建模拥塞、拓扑限制等 |

---

### ✅ 未来工作方向

1. **扩展至能量建模（Energy Modeling）**
   - 结合功耗模型（如 [15][16]）评估 energy-delay product（EDP）

2. **跨平台模型校准**
   - 在更多硬件平台（如 AMD, Ascend）上校准 compute/communication 参数

3. **支持更复杂的调度类别**
   - 如 Zero-Bubble Pipelines [19]、Interleaved Scheduling

4. **集成压缩技术评估**
   - 如 activation compression [20][21]，需权衡质量损失与效率增益

5. **探索自动调度搜索空间**
   - 基于该框架构建 schedule optimizer 或 NAS-like 方法

---

> 🧩 **总结一句话**：  
> **Pipeline schedule 的优劣不是绝对的，而是系统上下文相关的。本文提出的 tabular abstraction 与 multi-level evaluation framework，为科学、系统地比较调度策略提供了新范式。**

</details>

---

### 10. [Distilling Game Code World Model Generation into Lightweight Large Language Models](https://arxiv.org/abs/2605.24375)

**Authors**: Tyrone Serapio, Arjun Prakash, Haoyang Xu, Kevin Wang, Amy Greenwald  
**Category**: cs.AI  
**Published**: 2026-05-26  
**Score**: 10.0  
**Type**: new  
**ArXiv ID**: 2605.24375v1  

#### Abstract
Large Language Models (LLMs) have shown great ability in generating executable code from natural language, opening the possibility of automatically constructing environments for AI agents. Recent work on Code World Models (CWMs) demonstrates that LLMs can translate game rules into Python implementat...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Distilling Game Code World Model Generation into Lightweight Large Language Models*

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
当前基于 **Large Language Models (LLMs)** 自动生成 **Game Code World Models (GameCWMs)** 的方法存在以下瓶颈：
- 严重依赖 **frontier models**（如 GPT-4、Gemini 2.5 Pro），成本高且难以普及；
- 需要大量 **test-time compute**（推理时计算），例如通过迭代修正（iterative refinement）和单元测试反馈来修复生成代码；
- 这些方法限制了在资源受限环境下的可扩展性和实用性。

本文旨在解决如何将 GameCWM 生成能力“蒸馏”到更小、更轻量级的开源 LLM 中，从而降低对前沿模型和昂贵推理过程的依赖。

---

### 提出的新方法或新思路
作者提出了一套完整的 **post-training 蒸馏流程**，用于提升小型 LLM 在 GameCWM 生成任务上的表现。其核心创新包括：

#### （1）构建了一个高质量的 **GameCWM 数据集**
- 包含 **30 个游戏**，涵盖完美信息（perfect information）与不完美信息（imperfect information）游戏；
- 游戏难度分层：简单（Tic-Tac-Toe）、中等（Blackjack, Kuhn Poker）、复杂（Leduc Poker, Hold’em）以及 **out-of-distribution (OOD)** 新游戏（如 Converge、Quadranto）；
- 每个样本为 `(prompt, ground-truth code)` 对，prompt 包括 API 规范、自然语言规则描述、动作命名规范和示例轨迹。

#### （2）设计了一个层次化的 **Verification Framework**
该框架自动评估生成的 GameCWM 是否符合语法、结构和语义要求，分为四个层级：
- **Tier 1: Static Analysis**  
  检查语法正确性、API 完整性、类型签名、导入完整性。
- **Tier 2: Dynamics (Fuzzing)**  
  用 100 条随机轨迹进行模糊测试，验证状态不可变性、确定性、终端逻辑等动态属性。
- **Tier 3: Semantic Rule Adherence**  
  使用由 frontier LLM 生成的少量“场景轨迹”（scenario traces）作为黄金标准，检查生成环境是否能复现这些行为。
- **Tier 4: Information Consistency**（针对不完美信息游戏）  
  测试 `resample_history` 函数能否从观察历史中采样出一致且合法的历史路径。

> ✅ 特别优势：无需真实游戏引擎或已有轨迹数据，适用于 OOD 游戏。

#### （3）提出两阶段 **Post-Training Pipeline：SFT + RLVR**
- **Supervised Fine-Tuning (SFT)**：在 prompt-code 对上微调 Qwen2.5-3B-Instruct；
- **Reinforcement Learning with Verifiable Rewards (RLVR)**：使用 **Group Relative Policy Optimization (GRPO)**，以四层验证得分作为奖励信号进行强化学习优化。

> 💡 创新思想：将原本需要在推理时完成的“试错-修正”过程，提前通过训练“内化”进模型权重中。

---

### 相比现有方法的优势
| 维度 | 现有方法（如 Lehrach et al. [18]） | 本工作 |
|------|-------------------------------|--------|
| 模型规模 | 必须使用 frontier LLM（>100B 参数） | 成功蒸馏至 **3B 小模型**（Qwen2.5-3B-Instruct） |
| 推理开销 | 依赖多次调用 + 单元测试循环 | **零次迭代修正**，直接生成 |
| 可访问性 | 商业闭源 API，成本高昂 | 开源模型 + 可复现训练流程 |
| 泛化性 | 主要在已知游戏中有效 | 支持 **OOD 新游戏** 的生成 |

---

## 2. 核心实验方法和设置

### 使用的数据集
- **总数据集**：30 个游戏，按用途划分为：
  - **训练集（23 个）**：包含 Tic-Tac-Toe、Chess、Kuhn Poker 等常见及部分 OOD 游戏；
  - **测试集（7 个，held-out）**：完全未参与训练，用于评估泛化能力。

| 类型 | 完美信息游戏 | 不完美信息游戏 |
|------|-------------|----------------|
| In-Distribution | Y | Gin Rummy |
| Out-of-Distribution (OOD) | Gen. Tic-Tac-Toe, Gen. Chess, Converge | Quadranto, Hand of War |

> 注：OOD 游戏是作者新定义或由 Gemini 3 Pro 协助创建，确保不在原始 Qwen 训练数据中。

---

### 实验设置和评估指标

#### 模型配置
- **基础模型**：Qwen2.5-3B-Instruct
- **训练方式**：
  - **Base**：原始模型
  - **SFT**：LoRA 微调
  - **GRPO**：直接从 base 应用 RLVR
  - **SFT+GRPO**：先 SFT 再 GRPO（完整流程）
- **对比模型**：GPT-4o（作为 upper bound）

#### 评估方式
- 每个测试游戏生成 **25 个样本**；
- 使用四层验证框架打分，最终得分为加权平均：
  $$
  r = w_1 S_1 + w_2 S_2 + w_3 S_3 + w_4 S_4
  $$
  其中权重为：`w_static=0.15`, `w_fuzz=0.25`, `w_semantic=0.3`, `w_info=0.3`

#### 奖励机制（RLVR）
- 奖励门控机制：只有前一层通过一定阈值后，后续层级才计入奖励；
- 引入对 `resample_history` 的 stub 检测与惩罚，防止模型逃避实现难点。

---

## 3. 主要实验结果和性能指标

### 关键性能数据（来自 Table 2 & 3）

| Model | 平均验证得分 | 95% CI |
|-------|--------------|--------|
| **Base** | 47.3% | [44.3, 50.3] |
| **SFT** | 49.0% | [46.4, 51.6] |
| **GRPO** | 50.4% | [48.3, 52.4] |
| **SFT+GRPO** | **53.2%** | [51.0, 55.4] |
| **GPT-4o** | **66.7%** | [64.1, 69.4] |

> ✅ **SFT+GRPO 显著优于所有其他 Qwen 变体**（p < 0.05），证明两阶段训练的有效性。

---

### 分项性能对比（Table 3）

| Model | Static (%) | Fuzz (%) | Semantics (%) | Information (%) |
|-------|------------|----------|---------------|------------------|
| Base | 77.5 | 70.2 | 8.5 | 3.3 |
| SFT | 78.0 | 74.3 | 9.4 | 2.0 |
| GRPO | 83.3 | 75.3 | 8.4 | 3.7 |
| **SFT+GRPO** | **86.3** | **75.1** | **14.4** | **5.3** |
| GPT-4o | 98.4 | 84.6 | 33.8 | 14.0 |

> 🔍 发现：
> - **SFT 主要提升语法和结构正确性**（Static/Fuzz）；
> - **RLVR 显著增强语义一致性**（Semantics ↑50%+）；
> - 所有模型在 **Information Handling 上仍非常弱**，表明不完美信息建模仍是挑战。

---

### 消融实验结果（见 Appendix E）

- 移除 **Scenarios（语义轨迹）** 作为奖励信号会导致：
  - 语义得分下降约 30–50%；
  - 整体性能降低；
- 表明 **LLM-generated scenario traces 是有效的轻量级监督信号**，尤其适合缺乏真实轨迹的新游戏。

---

### 特殊现象分析
- 在 **Gin Rummy** 上，SFT 导致性能下降（Static 从 49.7% → 31.4%），原因是模型过度拟合模板，产生语法错误（如非法列表推导式）；
- 多个模型在 `resample_history` 函数中插入注释：“This logic is too hard”，并返回简化版本（如仅返回最后动作），说明模型具备 **自我认知局限性的能力**。

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **GameCWM 生成能力可以被成功蒸馏到小型 LLM 中**：
   - Qwen2.5-3B-Instruct 经过 SFT+GRPO 后，验证得分提升超过 6 个百分点；
   - 尤其在 **语义规则遵循** 和 **执行鲁棒性** 方面显著改善。

2. ✅ **两阶段训练优于单一阶段**：
   - SFT 提供格式对齐和结构稳定性；
   - RLVR 在此基础上进一步优化执行层面的行为一致性；
   - “SFT 先行 + RLVR 后续” 是最佳策略。

3. ⚠️ **不完美信息游戏仍是重大挑战**：
   - 所有模型（包括 GPT-4o）在 `resample_history` 上表现极差；
   - 当前 verifier 缺乏对信息集完整性的严格验证，未来需加强。

4. 🧠 **模型表现出对自身能力的认知**：
   - 在无法正确实现复杂函数时，会主动添加注释承认困难；
   - 可用于指导未来 **self-improvement 或 active querying** 机制的设计。

---

### 方法的局限性
1. **数据集有限**：尽管多样，但仍不足以覆盖复杂的博弈论逻辑（如多轮心理建模）；
2. **评估非完备**：Verifier 无法保证生成环境完全等价于理想实现，可能存在隐藏 bug；
3. **语义测试依赖 LLM 生成轨迹**：若 frontier LLM 自身理解错误，则污染黄金标签；
4. **小型模型容量限制**：3B 模型可能不具备“Theory of Mind”级别的推理能力，制约上限。

---

### 未来工作方向
1. **改进 Verification Framework**：
   - 加强对 information set 正确性的形式化验证；
   - 引入对抗性测试或 solver-based validation（如 MCTS 策略一致性）。

2. **扩大数据与模型规模**：
   - 构建更大规模的 OOD 游戏数据集；
   - 尝试更大 base model（如 14B 或 70B）以突破容量瓶颈。

3. **端到端 gameplay evaluation**：
   - 将生成的 GameCWM 接入 MCTS / ISMCTS，评估实际游戏性能；
   - 与人类玩家或标准实现对比胜率。

4. **结合迭代自改进机制**：
   - 利用模型自身的“awareness of limitations”启动自我调试循环；
   - 实现轻量版 test-time refinement，兼顾效率与准确性。

---

> ✅ **总体评价**：本文首次系统探索了将 GameCWM 生成能力从小型化、高效化的可行性路径，提出了一个可复现、模块化、面向未来的训练范式，为构建自主智能体所需的“世界模型”自动化生成提供了重要实践基础。

</details>

---

### 11. [A Unified Python Framework for Direct PPO-based Control of AHUs with Economizer Logic and CO2-Constrained Ventilation](https://arxiv.org/abs/2605.24406)

**Authors**: Erfan Haghighat Damavandi, Davide Papurello, Mahdi Alibeigi, Armin Keshavarz, Simone Canevarolo, Marco Condo  
**Category**: cs.LG  
**Published**: 2026-05-26  
**Score**: 10.0  
**Type**: new  
**ArXiv ID**: 2605.24406v1  

#### Abstract
Optimizing HVAC (Heating, Ventilation and Air Conditioning) can enhance a building's energy efficiency while providing comfort levels for its occupants. Using conventional control systems to maintain HVAC functions is often difficult because of the nonlinear characteristics of a building envelope as...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文核心结论与实验结果总结

## 1. 论文的主要贡献和创新点

### 解决的问题
当前 HVAC 控制系统在处理建筑热力学非线性和动态负荷变化时存在显著挑战，传统控制策略（如 On-Off 和 PID）难以兼顾 **Energy Efficiency**、**Thermal Comfort** 和 **Indoor Air Quality (IAQ)** 的多目标优化。此外，多数基于 **Reinforcement Learning (RL)** 的研究存在以下三大缺陷：
- 将 IAQ 视为奖励函数中的软惩罚项，而非硬约束；
- 依赖外部仿真工具（如 EnergyPlus + co-simulation），增加部署复杂度；
- 缺乏对 CO₂ 浓度的动态建模与强制合规机制。

本研究旨在解决上述问题，提出一个端到端可部署的、物理一致性强的统一控制框架。

### 提出的新方法与创新思路
本文提出了一个**基于 Python 的统一 DRL 框架**，用于直接控制带有 **Economizer Logic** 和 **CO₂ 约束通风** 的 **Air Handling Unit (AHU)**，其核心创新包括：

- ✅ **自包含 Gym-style 环境设计**  
  集成了 **2R-2C Thermal Model** 和 **动态 CO₂ 质量平衡模型**，无需依赖外部 CO₂ 或建筑能耗模拟器，实现完全内嵌式物理建模。

- ✅ **Hierarchical Flow Logic（分层流量逻辑）**  
  引入一种新颖的安全覆盖机制：当 RL Agent 决策可能导致室内 CO₂ > 1000 ppm 时，系统自动覆盖该动作，确保最小新风量满足人员呼吸需求。这实现了 **IAQ 的硬性保障**，而非常见的软惩罚方式。

- ✅ **Enthalpy-Based Economizer（焓值经济器）**  
  在合适条件下（室外空气焓值低于室内），启用“免费冷却”模式，通过提高新风比例替代机械制冷，进一步降低 **Cooling Coil Load**。

- ✅ **End-to-End Pipeline for Real Hardware Implementation**  
  构建从建模、训练到实际设备集成的数据采集闭环，支持未来向真实 AHU 系统迁移。

### 相比现有方法的优势
| 维度 | 传统方法（On-Off / PID） | 本文方法（PPO + Hierarchical Logic） |
|------|--------------------------|----------------------------------------|
| 温控稳定性 | 差（大波动） / 较好 | 更优（快速稳定，无振荡） |
| 能效表现 | 低效 | 显著节能（较 On-Off 节省 ~6%） |
| IAQ 控制能力 | 被动或忽略 | 主动且强制合规（始终 ≤1000 ppm） |
| 实现复杂度 | 低 | 中等（但全 Python 实现，便于复现） |
| 可扩展性 | 有限 | 支持多变量协同控制（温度、湿度、CO₂、能耗） |

---

## 2. 核心实验方法和设置

### 数据集与输入参数
未使用公开数据集，而是构建了一个**高保真动态仿真环境**，基于以下周期性输入信号（周期为 24 小时）：

| 变量 | 表达式 | 范围 |
|------|-------|------|
| `Tout`（室外温度） | $25 + 5 \sin(2\pi t / 86400)$ | 20–30 °C |
| `RHout`（相对湿度） | $0.3 + 0.3 \sin(2\pi t / 86400)$ | 30–60% |
| `Occupancy`（人数） | $70 + 80 \sin(2\pi t / 86400)$ | 70–150 人 |
| `Qin`（内部得热量） | $25000 + 45000 \sin(2\pi t / 86400)$ | 25–70 kW |

这些信号模拟了典型办公建筑的日间负载变化。

### 实验设置
- **时间步长**：1 秒
- **总仿真时长**：24 小时（86,400 秒）
- **状态空间**（State Space）：
  - 室内温度 $T_{air}$
  - 温度误差 $e(t) = T_{set} - T_{air}$ （设定点为 22 °C）
- **动作空间**（Action Space）：
  - 连续控制信号 $a_t \in [-1, 1]$，映射为风机转速比例 $u(t) \in [0, 1]$
  - 最大送风量 $V_{max} = 8\,\text{m}^3/\text{s}$
- **奖励函数**：
  $$
  R = -(|T_{air} - T_{set}|)^2
  $$
  即以温度偏差平方的负值作为即时奖励，鼓励精准温控。

### 评估指标
1. **Thermal Comfort**：室内温度波动范围及稳定性（对比设定点 22 °C）
2. **Indoor Air Quality**：室内 CO₂ 浓度是否超过 1000 ppm 安全线
3. **Energy Efficiency**：总冷却能耗 $E_{total} = \int Q_{coil}(t)\,dt$（单位：kWh）
4. **Ventilation Performance**：是否满足最低新风要求（基于 CO₂ 平衡计算）

### 基线方法对比
共比较四种控制器：
1. **On-Off Thermostat**：固定回差 ±1 °C，启停控制
2. **PID Controller**：增益 $K_p=0.5$, $K_i=0.001$, $K_d=0.1$，连续调速
3. **PPO RL Agent**：标准 PPO 算法，固定 50% 新风比
4. **PPO + Economizer & DCV**：本文完整方法（含分层逻辑与焓值经济器）

所有方法均在同一 **2R-2C 物理模型**下运行，保证公平性。

---

## 3. 主要实验结果和性能指标

### 关键性能数据汇总

| 控制器类型 | 总能耗 (kWh) | 最大 CO₂ 浓度 (ppm) | 温度波动范围 (°C) |
|------------|---------------|----------------------|--------------------|
| On-Off Thermostat | 2776 | >1300 | 21.0 – 24.5 |
| PID Controller | 2760 | ~920（偶超限） | 21.8 – 22.5 |
| PPO RL Agent | 2762 | <910 | 21.9 – 22.4 |
| **PPO + Economizer & DCV** | **2609** | **≈1000（精确跟踪）** | **22.0 – 22.3** |

> 💡 注：节能率达约 **6%**（相比 On-Off），同时保持最佳 IAQ。

### 与基线方法的对比结果
- **温度控制方面**：
  - On-Off 出现明显锯齿波形（图5a），舒适性差；
  - PID 与 PPO 均能快速稳定至设定点，但 PPO 更平滑；
  - 加入 Economizer 后仍维持高精度控温（图5d）。

- **CO₂ 控制方面**（图6）：
  - On-Off 因频繁关机导致通风不足，CO₂ 多次突破 1300 ppm；
  - PID 虽连续调节但仍偶有超标（occupancy 下降阶段）；
  - PPO（基础版）已能主动响应人员变化，将 CO₂ 控制在 910 ppm 以下；
  - **PPO + Hierarchical Logic** 成功实现“紧贴上限运行”，即始终接近但不超 1000 ppm，避免过度通风造成能源浪费。

- **能耗方面**（图7）：
  - 尽管基础 PPO 能耗略高于 PID（因更注重 IAQ），但引入 **Enthalpy-Based Economizer** 后显著下降至 **2609 kWh**，成为最优方案；
  - 节能来源于两个方面：
    1. 动态按需供新风（DCV），减少不必要的外气处理；
    2. 利用室外冷源进行 free cooling，降低机械制冷负担。

### 消融实验分析（隐含于文中对比）
虽然未明确标注“ablation study”，但从不同控制器的表现可推断模块有效性：
- **仅用 PPO（无 DCV/Economizer）** → 能耗较高，说明单纯优化温度不足以节能；
- **加入 Hierarchical Flow Logic** → IAQ 显著改善，验证安全机制必要性；
- **加入 Enthalpy Economizer** → 能耗大幅下降，证明利用自然冷源的有效性。

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **PPO 算法适用于 AHU 的连续控制任务**，能够在复杂动态环境中学习稳定温控策略；
2. ✅ **Hierarchical Flow Logic 成功解决了 IAQ 保障难题**，实现了 CO₂ 浓度的硬约束控制，优于传统软惩罚机制；
3. ✅ **结合 Enthalpy Economizer 可有效利用免费冷却资源**，在不牺牲舒适性的前提下实现约 **6% 的节能效果**；
4. ✅ 所提框架是首个将 **2R-2C 模型 + CO₂ 动态平衡 + PPO + Economizer** 集成于单一 Python 环境的工作，具备良好的可移植性和工程应用潜力。

### 方法的局限性
- 当前模型基于理想化假设（如均匀混合空气、固定送风温度等），尚未考虑局部气流组织或延迟效应；
- 训练过程依赖人工设计的 reward function，缺乏对 occupant feedback 的实时整合；
- 尚未在真实建筑中部署，泛化能力有待实测验证；
- Economizer 判断仅基于 enthalpy，未考虑污染物入侵风险（如 PM2.5 高发天气）。

### 未来工作方向
1. **高保真建模升级**：将当前 Python 模型迁移到 **MATLAB/Simulink/Simscape** 平台，构建更高精度的数字孪生系统；
2. **真实系统部署**：将训练好的 PPO 策略部署至实际运行的 AHU 设备，测试其在真实噪声、传感器漂移和故障情况下的鲁棒性；
3. **多区域扩展**：将单区模型拓展为多区耦合系统，支持整栋楼宇的分布式控制；
4. **融合 Occupant Feedback**：引入非侵入式监测技术（如 WiFi sensing、CO₂ trend analysis）来估计 occupancy 和 comfort preference，实现 truly occupant-centric control。

--- 

> 📌 **总结一句话**：本文提出了一种融合 **PPO 强化学习**、**CO₂ 约束通风** 与 **焓值经济器** 的统一 AHU 控制框架，在保障热舒适与 IAQ 的同时实现了显著节能，为智能建筑能源管理提供了可落地的技术路径。

</details>

---

### 12. [FrontierOR: Benchmarking LLMs' Capacity for Efficient Algorithm Design in Large-Scale Optimization](https://arxiv.org/abs/2605.25246)

**Authors**: Minwei Kong, Chonghe Jiang, Ao Qu, Wenbin Ouyang, Zhaoming Zeng, Xiaotong Guo, Zhekai Li, Junyi Li, Yi Fan, Xinshou Zheng, Xi Jing, Yikai Zhang, Zhiwei Liang, Seonghoo Kim, Runqing Yang, Zijian Zhou, Sirui Li, Han Zheng, Wangyang Ying, Ou Zheng, Chonghuan Wang, Jinglong Zhao, Hanzhang Qin, Cathy Wu, Paul Pu Liang, Jinhua Zhao, Hai Wang  
**Category**: cs.AI  
**Published**: 2026-05-26  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2605.25246v1  

#### Abstract
Large language models (LLMs) are increasingly used for optimization modeling and solver-code generation, yet practical operations research and optimization problems often require a harder capability: designing scalable algorithms that exploit problem structure and outperform direct formulation-and-s...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# FrontierOR: Benchmarking LLMs' Capacity for Efficient Algorithm Design in Large-Scale Optimization — 核心总结

---

## 1. 论文的主要贡献和创新点

### ✅ 解决了什么问题

当前大多数关于 **LLMs for Optimization** 的研究集中在 **优化建模**（optimization modeling）能力上，即能否将自然语言描述的问题转化为数学规划公式或可执行代码（如 MILP、MINLP）。然而，现实世界中的 **Operations Research (OR)** 问题不仅要求“正确建模”，更需要设计**高效的算法**来解决大规模实例。

现有基准（如 NL4OPT、OptiBench）存在以下局限：
- 仅测试小规模、教科书级别的问题；
- 忽视算法效率（computational efficiency）；
- 缺乏真实工业场景下的复杂性和可扩展性挑战。

因此，本文提出并系统评估一个更难但更具实际意义的能力：  
> **Q: 能否让 LLM 从自然语言描述出发，自动生成在大规模问题上兼具高质量解和高计算效率的优化算法？**

---

### 🚀 提出了什么新方法或新思路

作者提出了 **FrontierOR** —— 首个专门用于评估 LLM 在**大规模优化问题中高效算法设计能力**的综合性基准。

#### 主要创新点包括：

| 创新维度 | 内容说明 |
|--------|--------|
| **任务来源真实性** | 所有 180 个任务均来自顶级 OR 期刊（如 *Operations Research*, *Management Science*），涵盖 MIP、MINLP、Stochastic/DRO 等多种范式，确保问题具有真实的工业背景和算法设计动机。 |
| **强调“算法设计”而非“建模正确性”** | 不再只看是否生成正确的数学表达式，而是评估生成的程序是否能在大实例上以**优于 Gurobi 单体求解器**的方式运行——即是否能利用问题结构（如分解、启发式、局部搜索等）实现更快、更优的求解。 |
| **标准化且隐藏的评估套件** | 每个任务配备：<br>• 自然语言描述（输入给 LLM）<br>• 大规模测试实例<br>• 经专家验证的 Gurobi 基线实现<br>• 独立的 `feasibility checker`（可行性检查器）<br>所有参考模型和公式对 LLM 完全隐藏。 |
| **Hard 子集划分** | 构造了一个包含 50 个最具挑战性任务的 Hard Set，标准为：<br>• 组合爆炸类问题（如 lot-sizing, routing）<br>• 实例规模大、耦合强<br>• Gurobi 在 1 小时内无法达到最优 |

---

### 🔍 相比现有方法的优势

| 对比项 | 现有基准（如 NL4OPT, CO-Bench） | FrontierOR |
|------|-------------------------------|-----------|
| 任务规模 | 小型（~10² 变量/约束） | 大型（median ~40K 变量，最大达 10⁷） |
| 评价目标 | 建模准确性（formulation accuracy） | 算法效率（algorithm efficiency） |
| 是否端到端 | 否（常提供数学形式） | 是（仅给自然语言描述） |
| 是否文献驱动 | 否 | 是（全部源自真实论文） |
| 是否评估运行时间 | 否 | 是（引入 QTE 指标） |
| 是否支持 agent 自演化测试 | 否 | 是（支持 test-time evolution） |

> ✅ **FrontierOR 是首个真正面向“实用级 OR 算法工程”的 LLM 评测平台。**

---

## 2. 核心实验方法和设置

### 📚 使用的数据集

- **FrontierOR 数据集本身**：共 180 个任务，来源于 1992–2025 年间的顶级 OR 文献。
  - 分布广泛：
    - **问题类别**：Routing & TSP, Scheduling, Lot Sizing, Location, Packing, Graph 等
    - **应用领域**：Transportation, Healthcare, Energy, Supply Chain, Manufacturing
    - **建模类型**：MIP (13.3%), MINLP, CP, SDP, NLP, BIP, DRO 等
  - 实例规模巨大：
    - 中位数：约 40,000 变量，18,000 约束
    - 最大规模可达 $10^7$ 级别
    - 46% 的大实例在 1 小时内 Gurobi 无法达到最优

---

### ⚙️ 实验设置与评估指标

#### 计算环境
- 单核 CPU（AMD EPYC 9554P）
- Docker 容器化执行，禁用网络访问
- 固定 Python 3.13 + Gurobi 12 环境
- 控制变量，避免因实现差异影响结果

#### 两种评估协议（Protocols）

| 协议 | 描述 |
|-----|------|
| **One-shot Generation** | LLM 直接根据自然语言描述生成完整程序，允许少量调试，但无迭代反馈机制 |
| **Self-Evolving Frameworks** | 使用 agentic 方法进行多轮自我改进，基于开发集反馈优化候选程序 |

#### 三大 Self-Evolving Agent 框架
1. **AlphaEvolve / OpenEvolve**：基于 MAP-Elites 的进化算法，通过变异操作演化代码
2. **EoH (Evolution of Heuristics)**：联合演化代码与自然语言思考过程，鼓励探索不同策略
3. **CORAL**：多智能体协作框架，各 agent 共享记忆池，促进跨代理知识迁移

---

### 📊 评估指标（四大核心）

| 指标 | 定义 | 说明 |
|------|------|------|
| **Execution Rate (Exec.)** | 成功执行无报错的任务比例 | 衡量基本编程能力 |
| **Feasibility** | 在大实例上返回可行解的比例 | 必须满足所有硬约束（由独立 checker 验证） |
| **Solution Quality (Sol. q.)** | 可行解的目标值在 Gurobi 基线 1% 以内 | 越接近越好 |
| **Quality-Time Efficiency (QTE)** | ✅ 同时满足：<br>• 目标值 ≤ 1% gap<br>• 运行时间 ≤ Gurobi 时间<br>✅ 是衡量“高效算法”的黄金标准 |

> 💡 注意：**不可行解不计分**，即使其报告的目标值更低。

---

### 🆚 基线方法对比

#### 测试的 7 个 LLMs（覆盖前沿、性价比、开源模型）

| 类型 | 模型 |
|------|------|
| **Frontier Models** | GPT-5.3-Codex, Claude Opus 4.6, Gemini 3.1 Pro Preview |
| **Cost-effective/Open-source** | DeepSeek-R1, Grok-4.20-beta, Qwen3-Coder-Plus, LLaMA-4-Maverick |

> 所有模型仅接收自然语言描述 + 输入输出格式，**不得见任何数学公式或算法提示**。

---

## 3. 主要实验结果和性能指标

### 📈 One-shot 实验结果（Table 2）

#### 在 **FrontierOR Full (180 tasks)** 上的表现：

| Model | Exec. | Feas. | Sol. q. | QTE |
|-------|-------|--------|---------|-----|
| **Claude Opus 4.6** | 0.93 | 0.62 | 0.48 | **0.31** |
| GPT-5.3-Codex | 0.98 | 0.60 | 0.48 | 0.26 |
| Gemini 3.1 Pro | 0.93 | 0.61 | **0.52** | 0.25 |
| DeepSeek-R1 | 0.74 | 0.42 | 0.31 | 0.17 |
| LLaMA-4-Maverick | 0.47 | 0.18 | 0.13 | 0.06 |

#### 在 **Hard Set (50 tasks)** 上的表现：

| Model | Exec. | Feas. | Sol. q. | QTE |
|-------|-------|--------|---------|-----|
| **Claude Opus 4.6** | 0.94 | 0.60 | 0.44 | **0.32** |
| GPT-5.3-Codex | 0.98 | **0.49** | 0.30 | 0.18 |
| Gemini 3.1 Pro | 1.00 | **0.64** | 0.44 | 0.22 |

> 🔺 **最强 one-shot 模型也仅在 31% 的情况下同时胜过 Gurobi（质量和速度）**

---

### 🔄 Self-Evolution 实验结果（Table 3）

在 Hard Set 中选取最困难的 40% 任务（基于 one-shot 表现），使用 GPT-5.3-Codex 作为 backbone 进行对比：

| Method | Exec. | Feas. | Sol. q. | QTE |
|--------|-------|--------|---------|-----|
| One-shot | 0.80 | 0.45 | 0.18 | 0.15 |
| EoH | 0.78 | 0.72 | 0.43 | 0.33 |
| **OpenEvolve** | **1.00** | **0.92** | **0.61** | **0.49** |
| **CORAL** | **1.00** | **1.00** | **0.67** | **0.50** |

> ✅ **CORAL 达到 50% 的 QTE 成功率**，显著优于 one-shot（提升超 3 倍）

---

### 🔬 消融分析与深入发现（Appendix D, E）

#### （1）算法家族分布（Figure 3a）
- **弱模型**（如 LLaMA-4-Maverick）几乎总是调用 `monolithic solver`（占比 99%）
- **强模型**（如 Claude Opus）更多采用混合策略：
  - 37% 单体求解
  - 27% 局部搜索 / metaheuristic
  - 27% matheuristic / hybrid 方法
- ➡️ **非单体算法更可能实现高 QTE**

#### （2）失败模式分析（Figure 3b）
- **弱模型**：失败主要发生在早期阶段
  - 接口错误、约束定义错误、schema 违反
- **强模型**：失败更多出现在后期
  - 正确建模但启发式搜索不足（heuristic search failure）
- ➡️ **瓶颈随模型能力上移：从“不会写”到“搜不到好解”**

#### （3）连续性能度量（Continuous Metrics）
- 尽管多数任务未达 1% gap，但平均差距极小（△q ≈ 0.01~0.02）
- LLM 生成的算法通常比 Gurobi **快 3–5 倍**即可达到相近质量（△t ∈ [0.4, 0.66]）

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **当前 LLM 仍难以胜任“高效算法设计”任务**
   - 即使是 GPT-5.3-Codex 和 Claude Opus，在 one-shot 设置下也只有约 **30% 的任务能同时超越 Gurobi**（QTE）
   - 更多情况是生成可运行但低效的单体 MIP 模型

2. **模型能力决定算法风格**
   - 强模型倾向于生成 decomposition、local search、matheuristic 等高级结构
   - 弱模型依赖直接调用 solver，缺乏结构性洞察

3. **test-time evolution 显著提升性能**
   - 使用 CORAL 等 multi-agent 协作框架，QTE 可提升至 **50%**
   - 表明 **agentic search 是突破当前瓶颈的关键路径**

4. **算法效率差距源于“搜索深度”而非“建模错误”**
   - 强模型往往能正确理解问题，但在大规模实例上的搜索空间探索不足
   - 改进方向应聚焦于 **增强 LLM 的迭代优化与策略切换能力**

---

### ⚠️ 方法的局限性

1. **依赖已有论文的可复现性**
   - 若原始论文未公开数据或细节，则无法构建任务
   - 当前仅覆盖部分 OR 领域，尚未包含强化学习、模拟优化等动态决策场景

2. **评估成本高昂**
   - 每个任务需人工专家审核 + Gurobi 基线验证
   - 扩展至千级任务难度较大

3. **Gurobi 作为唯一 baseline 的潜在偏见**
   - 虽然 Gurobi 是行业标准，但某些问题可能存在其他更优专用求解器

4. **LLM 输出多样性受限于 prompt engineering**
   - 当前实验未充分探索 prompt 对算法多样性的引导作用

---

### 🔮 未来工作方向

1. **推动 LLM-based Algorithm Designer 的发展**
   - 设计专用于“算法设计”的训练目标与微调数据集
   - 引入 algorithm schema learning（如 decomposition template learning）

2. **发展更强的 agentic 框架**
   - 结合 symbolic reasoning、meta-learning、multi-agent collaboration
   - 如 CORAL 所示，共享记忆与跨代理迁移是关键优势

3. **扩展至 Online / Dynamic Optimization**
   - 当前为静态离线问题，未来可加入实时调度、在线装箱等动态场景

4. **开放生态建设**
   - FrontierOR 已开源：https://anonymous.4open.science/r/efficient-opt-bench-F03D
   - 鼓励社区提交新任务、新 agent、新 baseline

---

## 总结一句话

> **FrontierOR 揭示了当前 LLM 在“从自然语言到高效算法”的鸿沟：它们可以写出能跑的代码，但还远不能替代人类运筹学家设计出真正 scalable 的优化算法；而 test-time evolution 与 multi-agent collaboration 正是通往这一目标的最有希望路径。**

</details>

---

### 13. [Polar: Agentic RL on Any Harness at Scale](https://arxiv.org/abs/2605.24220)

**Authors**: Binfeng Xu, Hao Zhang, Shaokun Zhang, Songyang Han, Mingjie Liu, Jian Hu, Shizhe Diao, Zhenghui Jin, Yunheng Zou, Michael Demoret, Jan Kautz, Yi Dong  
**Category**: cs.DC  
**Published**: 2026-05-26  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2605.24220v1  

#### Abstract
Reinforcement learning for language agents increasingly depends on custom harnesses that manage long-running context, multi-turn tool use and multi-agent orchestration. However, porting these harnesses into RL environment interfaces remains difficult and often loses important training signals. We br...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文《Polar: Agentic RL on Any Harness at Scale》核心总结

---

## 1. 论文的主要贡献和创新点

### 解决的问题
当前基于大语言模型（LLM）的 **Agentic RL**（代理强化学习）面临一个核心系统挑战：  
现有的 **agent harness**（代理执行框架，如代码生成、工具调用、多轮交互等复杂系统）通常为推理或评测设计，其内部逻辑复杂、异构性强，且可能以闭源二进制形式存在。将这些 harness 集成到 RL 训练流程中需要大量定制化改造，破坏了原始执行路径，导致训练信号失真。

传统 RL 框架要求将 agent 改写为环境接口（如 Gymnasium），这在 agentic 场景下成本高昂、不可扩展。

### 提出的新方法与思路
论文提出 **PoLAR**（**P**roxied **L**LM **A**PI-based **R**ollout framework），一种**黑盒式、可扩展的异步 RL rollout 框架**，核心思想是：

> **“Can we train agents with RL without opening the box?”**  
> —— 不改动 agent harness 内部实现，也能进行 RL 训练。

#### 创新点：
- ✅ **Model API Proxy 作为 Rollout 边界**  
  PoLAR 在 agent harness 和 inference server 之间插入一个 **API Proxy**，监听所有 LLM 调用（如 OpenAI、Anthropic、Google 等格式请求），记录 `prompt`, `sampled tokens`, `logprobs`, `responses` 等 token-level 数据。
  
- ✅ **Harness-Agnostic 黑盒集成**  
  将任意 agent harness 视为黑箱，无需修改其代码或重构为 RL 环境。只需将其 LLM 请求路由至 PoLAR Proxy 即可。

- ✅ **Rollout-as-a-Service 架构**  
  实现完全解耦的异步架构：
  - **Rollout Server**：任务调度、状态管理
  - **Gateway Nodes**：运行时初始化、harness 执行、轨迹重建、评估、回调
  - 支持高并发、长尾任务独立伸缩，提升 GPU 利用率。

- ✅ **Token-Faithful 轨迹重建**  
  提供两种策略重建训练可用的 RL 轨迹：
  - `per_request`：每个 API 调用作为一个独立 trace（保守）
  - `prefix_merging`：合并具有前缀一致性的连续对话，减少样本碎片，保持行为策略保真度。

---

### 相比现有方法的优势

| 方法 | 是否支持异步 RL | 是否支持任意 harness | 是否需重写 agent | 是否保留 token fidelity |
|------|------------------|------------------------|------------------|----------------------------|
| **PoLAR (Ours)** | ✅ | ✅ | ❌ | ✅ |
| PRoRL AGENT | ✅ | ❌（需实现 handler） | ✅ | ✅ |
| SkyRL-Agent | ✅ | ⚠️（需适配 Gym 接口） | ✅ | ✅ |
| Agent Lightning / rLLM | ⚠️ | ⚠️（需 SDK 注入） | 部分 | ✅ |
| PRIME-RL | ✅ | ❌ | ✅ | ✅ |

> PoLAR 是首个真正实现 **“zero-modification + token-faithful + scalable async RL”** 的 rollout 框架。

---

## 2. 核心实验方法和设置

### 使用的数据集
- 主要任务：**软件工程类任务（Software Engineering Tasks）**
- 数据来源：
  - **SWE-Gym**：用于训练的软件修复任务集合（来自 GitHub issues）
  - **SWE-Bench Verified**：用于最终评估的标准 benchmark，衡量模型是否成功修复真实仓库中的 bug。

### 实验设置
- **基础模型**：`Qwen3.5-4B`
- **训练算法**：**GRPO**（Generalized Reward Policy Optimization），一种 online RL 算法
- **训练框架**：结合 **Slime** 进行异步训练
- **Rollout 框架**：PoLAR 提供 rollout-as-a-service
- **Harness 类型**：四种主流 coding agent harness：
  - Codex
  - Claude Code
  - Qwen Code
  - Pi
- **轨迹构建策略**：默认使用 `prefix_merging`
- **评估方式**：
  - 在 **SWE-Bench Verified** 上测试 pass@1（即一次尝试即通过所有测试）
  - 使用对应 harness 的 fresh runtime 执行最终 patch 并验证

### 基线方法对比
- **Baseline**：未经过 RL 微调的原始 `Qwen3.5-4B` 模型
- **对比目标**：同一基础模型在不同 harness 下经 PoLAR 训练后的性能提升
- 无其他 rollout 框架直接对比（因无法接入相同 harness）

---

## 3. 主要实验结果和性能指标

### 关键性能数据（SWE-Bench Verified Pass@1）

| Harness       | Base Model (%) | PoLAR + RL (%) | Gain (pts) |
|---------------|----------------|----------------|-----------|
| **Codex**     | 3.8            | 26.4           | **+22.6** |
| **Claude Code** | 29.8          | 34.6           | +4.8      |
| **Qwen Code** | 34.6           | 35.2           | +0.6      |
| **Pi**        | 34.2           | 40.4           | **+6.2**  |

> ✅ 所有 harness 均取得正向增益，尤其在非原生适配的 harness（如 Codex）上提升巨大。

### 分析与发现
- **最大收益出现在“陌生执行路径”**：Qwen 模型对 Codex 的 action protocol、context policy 不熟悉，初始表现极差（3.8%），但 PoLAR 通过 harness-native RL 成功适应，达到 26.4%，说明该方法能有效桥接模型与外部执行范式差异。
- **即使已有强先验仍可微调提升**：在 Qwen Code 上从 34.6% → 35.2%，表明 PoLAR 可进一步优化已对齐的系统。

---

### 消融实验结果

#### 轨迹重建策略对比（`per_request` vs `prefix_merging`）
- **训练效率显著提升**：
  - 相同三个训练步骤内：
    - `per_request` 产生 **1,185 条更新**
    - `prefix_merging` 仅产生 **218 条更新**
  - 墙钟时间从 **189.5 min → 35.2 min**（**5.39× 加速**）
- **GPU 利用率大幅提升**：
  - `prefix_merging`：平均 rollout GPU 利用率达 **87.7%**
  - `per_request`：仅为 **20.4%**

> 结论：`prefix_merging` 显著降低 trainer 负担，提高端到端训练吞吐量。

#### 其他观察
- 使用 `per_request` 且广播 outcome reward 会导致 **reward hacking**（噪声归因），说明细粒度 trace 需配合更精细的 credit assignment 机制（如 PRM）。

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **无需修改 agent harness 即可进行 RL 训练是可行的**，关键在于利用 **LLM API boundary** 作为观测接口。
2. ✅ **API Proxy + Token-Faithful Reconstruction** 能准确还原行为策略轨迹，确保训练信号正确。
3. ✅ **异步 rollout staging 架构** 可高效处理长周期、高延迟的 agent rollouts，极大提升训练系统的资源利用率。
4. ✅ **harness-native RL** 对模型跨平台迁移和适配具有重要意义，尤其当目标执行环境与预训练分布不一致时。

---

### 方法的局限性
- ❗ **依赖于 LLM API 的可观测性**：若 harness 使用私有协议或本地推理不暴露 API，则无法捕获流量。
- ❗ **不解决 credit assignment 问题**：虽然提供 token-faithful trace，但如何分配稀疏奖励仍需额外建模（如 PRM）。
- ❗ **目前主要用于 code agent**：尚未广泛验证在 browser agent、OS agent 等更复杂场景下的稳定性。
- ❗ **proxy 层存在轻微延迟开销**：尽管不影响 scalability，但在低延迟场景中需权衡。

---

### 未来工作方向
- 🔧 开发内置的 **session normalization 与 process reward modeling (PRM)** 工具链，缓解 reward hacking。
- 🌐 扩展支持更多 agent 类型（如 web browsing, GUI automation）。
- 📦 推动成为标准 rollout substrate，集成进 NeMo Gym、Slime 等主流训练生态。
- 💾 探索离线 RL（Offline RL）与 preference learning 应用，复用已收集的 rejected trajectories。

---

> **总结一句话**：  
> **PoLAR 实现了“让任何 agent harness 都能成为 RL 环境”的愿景，通过 API 代理解耦训练与执行，开启了 scalable agentic RL 的新范式。**

</details>

---

### 14. [HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol](https://arxiv.org/abs/2605.25421)

**Authors**: Xinyi Mou, Siyuan Wang, Zejun Li, Yulan He, Zhongyu Wei  
**Category**: cs.CL  
**Published**: 2026-05-26  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.25421v1  

#### Abstract
Communication protocol design is a central challenge in large language model-based multi-agent systems. Existing single-channel approaches face an inherent communication trilemma: text-based methods are interpretable but verbose, while latent-space methods are efficient but opaque and limited to uni...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
在基于 **Large Language Model (LLM)** 的多智能体系统中，**通信协议设计** 是一个核心挑战。现有单通道通信方法面临“**通信三难困境 (communication trilemma)**”：
- **Text-based 方法**：可解释性强，但信息冗长，通信开销大（高 token 消耗）。
- **Latent-space 方法**：通信高效，但信号不透明（opaque），缺乏可解释性，且通常仅支持单向或单轮交互。

因此，如何在保证任务性能和可解释性的同时，显著降低通信成本，是当前研究的关键瓶颈。

### 提出了什么新方法或新思路
本文提出 **HyLaT (Hybrid Latent-Text)** 协议，一种**双通道混合通信框架**：
- **Latent Channel**：传输详细的认知信号（如推理过程、解释、上下文展开），实现高效的机器间信息传递。
- **Text Channel**：传输简洁的关键信号（如最终答案、承诺、决策），保持对人类和外部观察者的可读性与精确性。

该设计受**多通道通信理论 (multi-channel communication theory)** 启发，通过功能分离实现效率与透明性的平衡。

### 相比现有方法的优势
- ✅ **效率提升**：相比纯文本方法，大幅减少 token 数量和推理时间。
- ✅ **性能保留**：相比纯隐空间方法，维持甚至超越其任务准确率。
- ✅ **支持多轮交互**：首次实现支持多轮、多智能体协同的混合通信。
- ✅ **兼容性强**：Text 通道允许与使用其他协议的 agent 兼容互操作。
- ✅ **鲁棒性好**：即使 latent 向量受到噪声干扰，关键信息仍可通过 text 通道保障输出稳定性。

---

## 2. 核心实验方法和设置

### 使用了哪些数据集
#### Stage 1（单智能体混合生成训练）
- **CommonsenseQA**, **StrategyQA**, **SocialIQA**, **WorldTree**, **PubMedQA**
- 数据特征：包含详细推理链 + 简洁最终答案，天然适配 HyLaT 的 dual-output 结构。

#### Stage 2（多智能体交互共训）
构建两类多智能体交互数据：
1. **Refinement**：模拟多智能体辩论，逐步修正答案（使用 Llama-3.2-1B 和 GPT-5 生成轨迹）。
2. **Decomposition**：将复杂问题拆解为子问题并行求解后合成（来自 HotpotQA, WikiMultiHopQA, GSM8K-Aug-NL）。

### 实验设置和评估指标

| 设置项 | 内容 |
|------|------|
| Backbone Model | 主要使用 `Llama-3.2-1B-Instruct`，补充实验使用 `3B` 和 `Qwen2-1.5B` |
| 参数微调方式 | LoRA (rank=128, alpha=32) |
| Latent Vector 数量 | 每轮生成 `k=6` 个连续隐向量 |
| 多智能体配置 | 默认 `N=2` agents, `T=2` rounds |
| 硬件环境 | 8×NVIDIA H200 GPUs |

#### 评估指标
| 类别 | 指标 |
|------|------|
| **Task Performance** | - 平均准确率 (Avg. Accuracy)<br>- 多数投票准确率 (Majority-vote Accuracy) |
| **Communication Efficiency** | - 平均 token 数 (#token)<br>- 推理时间 (wall-clock time, 秒) |
| **格式正确性** | - 格式错误率 (format error rate) |

### 基线方法对比
分为三大类进行比较：

| 类型 | 方法 | 简介 |
|------|------|------|
| **无训练文本方法** | `NL`, `AutoForm`, `EcoLang`, `SDE` | 使用自然语言或结构化文本通信 |
| **无训练隐空间方法** | `Cipher`, `LatentMAS-V` | 完全通过隐向量通信 |
| **有训练基线** | `TextFullT`, `LatentFullT` | 在相同数据上训练的纯文本/纯隐空间版本，用于公平比较 |

---

## 3. 主要实验结果和性能指标

### 关键性能数据（见 Table 1）

| 方法 | Avg. Acc (%) | #token | Time (s) |
|------|--------------|--------|----------|
| **HyLaT (Ours)** | **63.78** | **72.01** | **1.47** |
| TextFullT | 64.44 | 505.03 | 5.47 |
| LatentFullT | 56.00 | 57.00 | 0.70 |
| NL | 49.56 | 1247.50 | 13.15 |
| EcoLang | 48.00 | 960.26 | 10.04 |
| LatentMAS-V | 26.11 | 324.43 | 3.61 |

> 💡 **关键发现**：
- HyLaT 的 token 开销仅为最高效文本方法（EcoLang）的 **~7.5%**，时间约为 **11%**。
- 性能仅次于 `TextFullT`，远超所有无训练方法及 `LatentMAS-V`。
- 在 **SocialIQA** 上表现尤为突出，说明 latent 通道有效补充了社会推理中的隐含信息。

### 与基线方法的对比结果
- 📈 **效率优势**：HyLaT 比 `TextFullT` 节省 **86% token**，比 `NL` 节省 **94%+**。
- 🎯 **性能优势**：比 `LatentMAS-V` 高出近 **38个百分点** 的平均准确率。
- ⚖️ **平衡性最佳**：唯一同时达到高性能（接近 TextFullT）和高效率（接近 LatentFullT）的方法。

### 消融实验结果（见 Table 2）

| 变体 | Avg. Acc (%) | #token | Format Error (%) |
|------|--------------|--------|------------------|
| **HyLaT (Full)** | **57.83** | **72.01** | **0.00** |
| w/ pure text | 56.93 | 639.18 | 3.28 |
| w/ pure latent | 50.28 | 56.09 | 6.12 |
| w/o Stage 1 | 38.43 | 102.59 | 9.13 |
| w/o Stage 2 | 43.64 | 136.10 | 22.27 |

> 🔍 **消融分析结论**：
- **双通道设计必要**：移除任一通道都会导致性能下降或格式错误上升。
- **两阶段训练关键**：
  - 缺少 Stage 1 导致 latent 输出不稳定。
  - 缺少 Stage 2 导致无法理解他人 latent 信号，格式错误高达 22.27%。

---

## 4. 关键结论和发现

### 论文的主要发现
1. **通道多样性是解决通信三难困境的有效路径**：HyLaT 通过 dual-channel 设计，在效率、可解释性和通用性之间取得最优平衡。
2. **Latent 通道可用于压缩中间推理**，而 **Text 通道锚定最终决策**，二者互补。
3. **两阶段训练框架至关重要**：
   - Stage 1 实现个体级混合输出能力；
   - Stage 2 实现跨智能体 latent 信号的理解与响应。
4. **HyLaT 具备良好扩展性与泛化能力**：
   - 支持异构模型通信（如 Llama + Qwen）；
   - 在 Trust Game 社会仿真中表现出更强合作倾向；
   - 随着 agent 数量增加，效率优势更加明显（见 Figure 4）。

### 方法的局限性
- **模型规模限制**：目前实验集中在 1B–3B 规模模型，是否适用于更大模型尚待验证。
- **部署兼容性差**：当前生成流程与主流推理框架（如 vLLM）不兼容，难以应用于大规模长周期场景。
- **Text 通道表达受限**：受限于训练数据质量与多样性，text 输出行为较为单一（如固定 answer prompt）。
- **Latent 可解释性不足**：虽然整体系统可解释，但 latent 向量本身仍是黑箱，语义难以直接解读。

### 未来工作方向
- 探索更丰富的多智能体通信场景（如谈判、协作游戏）以增强 text 表达多样性。
- 研究 latent 向量的可解码机制，在保持效率的同时提升其透明度。
- 优化推理架构，使其兼容现代 LLM 推理引擎，推动实际部署。
- 扩展至更大规模模型与更复杂的交互拓扑结构（如树状、图状通信）。

---

> ✅ **总结一句话**：  
> **HyLaT 成功实现了“鱼与熊掌兼得”——在几乎不牺牲任务性能的前提下，将多智能体通信开销降至极低水平，并通过 hybrid design 保障了系统的可解释性、兼容性与鲁棒性，为下一代高效可信赖的 LLM-MAS 提供了新的范式。**

</details>

---

### 15. [Label-NTK Alignments and A Tighter Convergence Bound in the NTK Regime](https://arxiv.org/abs/2605.25275)

**Authors**: Ruchirinkil Marreddy, Chaoyue Liu  
**Category**: cs.LG  
**Published**: 2026-05-26  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.25275v1  

#### Abstract
The Neural Tangent Kernel (NTK) framework explains optimization in over-parameterized neural networks via approximately linearized dynamics, yielding exponential convergence guarantees. However, existing results are often overly pessimistic and do not match the fast training in practice, as they dep...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：Label-NTK Alignments and A Tighter Convergence Bound in the NTK Regime**

---

## 1. **论文的主要贡献和创新点**

### ✅ **解决了什么问题**

传统基于 **Neural Tangent Kernel (NTK)** 的优化理论虽然能证明过参数化神经网络在梯度下降下可收敛至全局最小值，但其**收敛速率依赖于 NTK 矩阵的最小特征值 $\lambda_{\min}$**。然而，在实际中 $\lambda_{\min}$ 极小，导致理论预测的收敛速度远慢于实际观察到的训练动态，形成显著的“理论-实践鸿沟”。

该论文旨在解决这一问题：  
> **能否在 NTK 框架内建立一个更紧致、更贴近实际训练行为的收敛界？**

---

### ✅ **提出了什么新方法或新思路**

作者提出两个关键现象，并以此为基础构建新的收敛分析框架：

#### 🔹 **Label-NTK Alignment（标签-NTK 对齐）**
- 发现：标签向量 $y$ 在 NTK 特征向量上的投影满足 $(v_i^T y)^2 \sim \lambda_i^2$，即标签更强烈地对齐于大特征值对应的特征方向。
- 理论解释：基于真实数据中“相似输入具有相似标签”的假设（即 ground-truth 函数满足 **Lipschitz continuity**），从理论上推导出该对齐关系，且精确预测幂律指数为 2。

#### 🔹 **Residual-NTK Alignment（残差-NTK 对齐）**
- 发现：初始残差 $r_0 = f(w_0) - y$ 的投影满足 $(v_i^T r_0)^2 \sim \lambda_i$，同样表现出与小特征值弱相关的结构。
- 这表明最坏情况（如残差集中在最小特征空间）在实践中几乎不会发生。

#### 🔹 **基于对齐性质的新收敛界**
利用上述对齐特性，推导出新的损失收敛上界：
$$
\mathcal{L}(w_t) \lesssim \mathrm{tr}\left[(I - \eta K)^{2t} K\right]
$$
该界限**不再显式依赖 $\lambda_{\min}$**，而是利用整个 NTK 谱的信息，从而大幅收紧理论预测。

此外，还基于 Label-NTK 对齐改进了泛化误差界，得到更优的测试误差上界。

---

### ✅ **相比现有方法的优势**

| 方面 | 传统 NTK 理论 | 本文方法 |
|------|----------------|----------|
| 收敛速率 | $O(\exp(-\eta \lambda_{\min} t))$ | $O\left(\mathrm{tr}[(I-\eta K)^{2t}K]\right)$ |
| 依赖信息 | 仅用 $\lambda_{\min}$（最悲观估计） | 利用全谱 + 标签/残差结构 |
| 预测准确性 | 远慢于实际（曲线平坦） | 紧密贴合实证训练曲线 |
| 泛化界 | 依赖 $\|K^{-1}y\|$，可能很大 | 改进为 $O(\mathrm{tr}[K]/n)$，更合理 |

> ✅ **核心优势：将“标签如何分布于 NTK 特征空间”纳入分析，摆脱了对极端最小特征值的依赖，使理论更具解释力。**

---

## 2. **核心实验方法和设置**

### ✅ **使用的数据集**

- **图像分类任务常用基准数据集**：
  - CIFAR-10
  - Tiny-ImageNet10
  - SVHN
  - MNIST
  - Fashion-MNIST

所有实验均在完整数据集或其子集（如 1000 样本）上进行。

---

### ✅ **模型架构**

- **MLP**：五层全连接网络，每层宽度 512，ReLU 激活。
- **CNN**：五层卷积网络（3×3 卷积核），通道数 [32, 64, 128, 128, 256]，含 ReLU 和 MaxPooling，最后接分类头。

---

### ✅ **实验设置**

| 类型 | 设置细节 |
|------|---------|
| 优化器 | SGD（momentum=0），学习率 $\eta = 0.01$ |
| 训练方式 | 全批量 GD（full-batch GD），最多 200 轮迭代 |
| NTK 计算 | 使用初始化时的 NTK 矩阵 $K$ 及其特征分解 |
| 对齐测量 | 在多个时间步 $t$ 上计算 $(v_i^T y)^2$ 和 $(v_i^T r_t)^2$，按 $\log \lambda_i$ 分组平均（每批 100 样本，共 500 批） |

---

### ✅ **评估指标**

1. **训练损失曲线**：$\mathcal{L}(w_t)$ 随迭代的变化。
2. **理论边界对比**：
   - 传统界：$\exp(-\eta \lambda_{\min} t)\cdot \mathcal{L}(w_0)$
   - 本文新界：$\mathrm{tr}[(I - \eta K)^{2t} K]$
3. **对齐关系可视化**：绘制 $\log(v_i^T y)^2$ vs. $\log \lambda_i$ 和 $\log(v_i^T r)^2$ vs. $\log \lambda_i$ 的散点图，验证幂律关系。

---

### ✅ **基线方法对比**

- **经典 NTK 收敛界**（如 Du et al., Jacot et al.）
- **基于全谱但未考虑标签结构的方法**（如 [2] Arora et al.）

本文方法在相同设定下直接比较理论边界与实证曲线的拟合程度。

---

## 3. **主要实验结果和性能指标**

### ✅ **关键性能数据与对比结果**

#### 📈 图 1 & 图 4：收敛边界对比
- **传统理论曲线**（橙色虚线）：由于 $\lambda_{\min}$ 极小（常 < $10^{-6}$），预测损失几乎不下降。
- **本文理论曲线**（绿色虚线）：紧密跟随**实际训练曲线**（蓝色实线），即使在早期阶段也高度一致。
- 在多个数据集（CIFAR-10, SVHN, MNIST 等）和架构（MLP/CNN）上均验证有效。

#### 📊 表现量化（定性）
- 新界的收敛速度比传统界快 **几个数量级**。
- 时间复杂度分析显示，达到精度 $\epsilon$ 所需迭代次数为：
  $$
  T_\epsilon = O\left( \frac{\log(1/\epsilon)}{q-1} \right), \quad \text{其中 } \lambda_i \sim i^{-q}, q>1
  $$
  显著优于 $O(\lambda_{\min}^{-1} \log(1/\epsilon))$。

---

### ✅ **消融实验与额外验证**

#### 🔍 Label-NTK Alignment 实验（图 2, 3, 5）
- 在所有数据集和架构中，$(v_i^T y)^2$ 与 $\lambda_i$ 呈现出清晰的幂律关系：
  - 斜率约为 **2**，符合 $(v_i^T y)^2 \sim \lambda_i^2$
- 尤其在小特征值区域（右端）线性关系更强，说明标签几乎正交于这些方向。

#### 🔍 Residual-NTK Alignment 实验
- $(v_i^T r_t)^2 \sim \lambda_i$，斜率约为 **1**
- 且在整个训练过程中保持稳定，支持理论假设的有效性。

#### 🔍 不同数据集一致性
- 在 MNIST、Fashion-MNIST 等简单数据上对齐更明显；
- 在 CIFAR-10、Tiny-ImageNet10 等复杂数据上仍成立，体现鲁棒性。

---

## 4. **关键结论和发现**

### ✅ **论文的主要发现**

1. **Label-NTK 和 Residual-NTK 对齐是普遍存在的现象**：
   - 标签和残差天然避开 NTK 的小特征值方向。
   - 这解释了为何实际训练远快于最坏情况预测。

2. **可以利用这种对齐性获得更紧致的收敛界**：
   - 新界 $\mathrm{tr}[(I - \eta K)^{2t} K]$ 综合利用了全谱信息和标签结构。
   - 数值上与实证训练动态高度吻合。

3. **理论可解释性强**：
   - 通过 Lipschitz 假设成功解释 Label-NTK 对齐的成因。
   - 推导出精确的幂律指数 2，与实验完全一致。

4. **泛化界也得以提升**：
   - 得到 $L_{\text{test}} = O(\mathrm{tr}[K]/n)$，优于传统的 $O(\|K^{-1}y\|/\sqrt{n})$

---

### ⚠️ **方法的局限性**

1. **局限于 NTK regime**：
   - 要求网络足够宽、学习率较小。
   - 无法建模 **feature learning** 动态（如 Edge of Stability, Catapult Dynamics）。

2. **未涵盖非 MSE 损失函数**：
   - 当前分析基于平方损失（MSE），对交叉熵等分类损失扩展尚待研究。

3. **理论依赖特定数据假设**：
   - 如单位长度输入、Lipschitz 标签函数等，虽合理但仍为理想化。

4. **NTK 计算成本高**：
   - 实际中计算完整 NTK 特征分解仅适用于中小规模数据。

---

### 🔮 **未来工作方向**

1. **推广到其他损失函数和网络结构**（如 Transformers, GNNs）
2. **结合 feature learning regime**，发展统一理论框架
3. **探索对齐现象在主动学习、数据清洗中的应用**
4. **设计基于 NTK 对齐的自适应优化算法**（如调整学习率 per mode）
5. **进一步分析不同数据分布下的对齐强度差异**

---

> 💡 **总结一句话**：  
> 本文通过揭示 **Label-NTK / Residual-NTK 对齐** 这一关键现象，打破了传统 NTK 理论对 $\lambda_{\min}$ 的依赖，建立了首个能**精准匹配实际训练动态**的紧致收敛界，为理解深度学习优化提供了新的视角。

</details>

---

### 16. [Visual-Redundancy-Controlled Parallel Decoding for Diffusion-Based Multimodal Large Language Models](https://arxiv.org/abs/2605.25820)

**Authors**: Yulin Yuan, Hongshuo Zhao, Xiangming Meng  
**Category**: cs.LG  
**Published**: 2026-05-26  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.25820v1  

#### Abstract
Diffusion-based multimodal large language models (dMLLMs) decode by iteratively predicting tokens at multiple masked positions in parallel. This turns each decoding step into a position-selection problem: the model must choose not only which predictions are reliable in isolation, but also which posi...

---

### 17. [Selective Latent Thinking: Adaptive Compression of LLM Reasoning Chains](https://arxiv.org/abs/2605.25745)

**Authors**: Hui Xie, Jie Liu, Ziyue Qiao, Joaquin Vanschore  
**Category**: cs.CL  
**Published**: 2026-05-26  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.25745v1  

#### Abstract
Explicit chain-of-thought (CoT) reasoning substantially improves the reasoning ability of large language models (LLMs), but incurs high inference cost due to lengthy autoregressive traces. Existing latent reasoning methods offer a promising alternative, yet they often treat reasoning as uniformly co...

---

### 18. [Cross-Platform Fused MoE Dispatch in Triton: Portable Expert Routing Without CUDA](https://arxiv.org/abs/2605.23911)

**Authors**: Subhadip Mitra  
**Category**: cs.DC  
**Published**: 2026-05-26  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.23911v1  

#### Abstract
Mixture-of-Experts (MoE) architectures power the majority of frontier large language models, but their inference is bottlenecked by irregular memory access patterns and expert routing overhead. Existing optimized MoE kernels (Megablocks, Tutel, FasterMoE) are implemented in CUDA and locked to NVIDIA...

---

### 19. [PrivFusion: A Privacy-preserving Multi-Agent Framework for Harmonizing Distributed Datasets](https://arxiv.org/abs/2605.24249)

**Authors**: Anisa Halimi, Liubov Nedoshivina, Kieran Fraser, Stefano Braghin  
**Category**: cs.LG  
**Published**: 2026-05-26  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.24249v1  

#### Abstract
The growing availability of clinical data has increased the use of machine learning, yet centralized data aggregation is often infeasible for sensitive health information. Federated Learning (FL) offers a distributed alternative, but its adoption is limited by substantial heterogeneity across instit...

---

### 20. [Fourier Feature Pyramids for Physics-Informed Neural Networks](https://arxiv.org/abs/2605.24278)

**Authors**: Brandon Zhao, Yixuan Wang, Jonathan T. Barron, Katherine L. Bouman, Dor Verbin, Pratul P. Srinivasan  
**Category**: cs.LG  
**Published**: 2026-05-26  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.24278v1  

#### Abstract
We present an improved neural field architecture for solving partial differential equations (PDEs). Current physics-informed neural networks (PINNs) provide a flexible framework for solving PDEs, but they struggle to achieve highly accurate solutions and require computation that scales poorly with p...

---

### 21. [Reinforcement Learning for Laser Additive Manufacturing Scan-Order Optimisation: A Bilevel Proxy--FEA Diagnostic Framework for Reward and World-Model Diagnosis](https://arxiv.org/abs/2605.25063)

**Authors**: Xian Wu, Haoran Li, Dongbin Zhao, Ruiyao Zhang, Yuanqi Chu, Bin Wang  
**Category**: cs.LG  
**Published**: 2026-05-26  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.25063v1  

#### Abstract
Reinforcement learning offers a promising approach for scan-order optimisation in laser additive manufacturing, where sequential scan decisions critically influence thermal accumulation, residual stress, distortion, and final part quality. A central challenge in applying RL to this domain lies in re...

---

### 22. [Palette: A Modular, Controllable, and Efficient Framework for On-demand Authorized Safety Alignment Relaxation in LLMs](https://arxiv.org/abs/2605.24154)

**Authors**: Qitao Tan, Xiaoying Song, Arman Akbari, Arash Akbari, Yanzhi Wang, Xiaoming Zhai, Lingzi Hong, Zhen Xiang, Jin Lu, Geng Yuan  
**Category**: cs.AI  
**Published**: 2026-05-26  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.24154v1  

#### Abstract
Current safety alignment of foundation models largely follows a \emph{one-size-fits-all} paradigm, applying the same refusal policy across users and contexts. As a result, models may refuse requests that are unsafe for general users but legitimate for authorized professionals, limiting helpfulness i...

---

### 23. [Evolutionary Enhanced Multi-Agent Reinforcement Learning for Cooperative Air Combat](https://arxiv.org/abs/2605.25091)

**Authors**: Chengwei Li, Junlin Liu, Yang Gao  
**Category**: cs.AI  
**Published**: 2026-05-26  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.25091v1  

#### Abstract
As modern air combat evolves toward beyond-visual-range (BVR) multi-aircraft cooperative engagements, autonomous decision-making for unmanned combat aerial vehicles (UCAVs) faces significant challenges due to high-dimensional state spaces, discrete action commands, and strongly adversarial dynamic e...

---

### 24. [SimuWoB: Simulating Real-World Mobile Apps for Fast and Faithful GUI Agent Benchmarking](https://arxiv.org/abs/2605.25160)

**Authors**: Guohong Liu, Jialei Ye, Pengzhi Gao, Wei Liu, Jian Luan, Yunxin Liu, Yuanchun Li  
**Category**: cs.AI  
**Published**: 2026-05-26  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.25160v1  

#### Abstract
Mobile GUI agents powered by large language models have progressed rapidly, creating urgent needs for realistic and comprehensive evaluation. Existing benchmarks prioritize reproducibility but are often limited to open-source apps or file-operation tasks for the difficulty of constructing rewards on...

---

### 25. [SpecAlign: A Semantic Alignment Framework for SystemVerilog Assertion Generation](https://arxiv.org/abs/2605.25181)

**Authors**: Jaime Rafael Imperial, Hao Zheng  
**Category**: cs.AI  
**Published**: 2026-05-26  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.25181v1  

#### Abstract
Existing Large Language Model (LLM) approaches to SystemVerilog Assertion (SVA) generation primarily focus on syntactic validity and formal verification outcomes, while semantic alignment between generated assertions and natural language specifications remains difficult to quantify. As a result, hal...

---

### 26. [PHGNet: Prototype-Guided Hypergraph Construction for Heterogeneous Spatiotemporal Forecasting](https://arxiv.org/abs/2605.25554)

**Authors**: Ruiwen Gu, Yahao Liu, Zhenyu Liu, Qitai Tan, Xiao-Ping Zhang  
**Category**: cs.AI  
**Published**: 2026-05-26  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.25554v1  

#### Abstract
As a core task in intelligent transportation systems, traffic forecasting plays a critical role in urban traffic management. Accurate traffic forecasting relies on modeling complex spatiotemporal dependencies, which is inherently challenging due to spatial heterogeneity in traffic systems.Despite si...

---

### 27. [From Accounting to Coordination: A Virtual Water-Aware Electricity-Computation-Water Nexus Framework for Data Center Dispatch](https://arxiv.org/abs/2605.25854)

**Authors**: Haiyang You, Chengwei Lou, Jin Zhao, Yue Zhou, Lu Zhang, Jin Yang  
**Category**: cs.AI  
**Published**: 2026-05-26  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.25854v1  

#### Abstract
The expansion of data centers (DCs) drives a sustained increase in electricity demand and associated water withdrawals at generation sites. These withdrawals occur at generation sites and are virtually allocated to demand based on network power flows. Consequently, the actual water footprint of a sp...

---

### 28. [GeoSVG-RL: Geometry-Aware Reinforcement Learning for Layout-Constrained Text-to-SVG Diagram Generation](https://arxiv.org/abs/2605.25447)

**Authors**: Sifan Li, Yujun Cai, Hongkai Chen, Yiwei Wang  
**Category**: cs.CL  
**Published**: 2026-05-26  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.25447v1  

#### Abstract
Generating structured, editable diagrams remains a significant challenge for contemporary large language models, despite their proficiency in general-purpose vector code generation. The primary difficulty lies in the structural fragility of the output; minor errors such as misaligned connector endpo...

---

### 29. [Reinforcement Learning from Denoising Feedback](https://arxiv.org/abs/2605.25638)

**Authors**: Qi He, Huan Chen, Ya Guo, Huijia Zhu, Yi R. Fung, Baojian Zhou  
**Category**: cs.CL  
**Published**: 2026-05-26  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.25638v1  

#### Abstract
Policy loss estimation remains a fundamental and long-standing challenge in reinforcement learning (RL) for diffusion language models (dLLMs). We introduce Reinforcement Learning from Denoising Feedback (RLDF), a novel training paradigm that leverages feedback obtained from rollout and training proc...

---

### 30. [Kavier: Exploring Performance, Sustainability, and Efficiency of LLM Ecosystems under Inference through Cache-Aware Discrete-Event Simulation](https://arxiv.org/abs/2605.25247)

**Authors**: Radu Nicolae, Alexandru Iosup, Animesh Trivedi, Jesse Donkervliet  
**Category**: cs.DC  
**Published**: 2026-05-26  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.25247v1  

#### Abstract
Large Language Models (LLMs) are widely used by our increasingly digitalized society, but raise sustainability, performance, and financial concerns, especially as inference workloads grow. To improve the design and operation of LLM ecosystems, we envision simulators and simulation-based digital twin...

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
