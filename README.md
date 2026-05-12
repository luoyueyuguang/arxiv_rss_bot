# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-05-12 08:17:36 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG

## 📚 Recent Papers

### 1. [Different Prompts, Different Ranks: Prompt-aware Dynamic Rank Selection for SVD-based LLM Compression](https://arxiv.org/abs/2605.08568)

**Authors**: Hengyi Zhu, Zhendong Mi, Grace Li Zhang, Shaoyi Huang  
**Category**: cs.LG  
**Published**: 2026-05-12  
**Score**: 14.5  
**Type**: new  
**ArXiv ID**: 2605.08568v1  

#### Abstract
Large language models (LLMs) have rapidly grown in scale, creating substantial memory and computational costs that hinder efficient deployment. Singular value decomposition (SVD) has emerged as an effective post-training compression technique, but existing SVD-based methods rely on static rank trunc...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：Different Prompts, Different Ranks: Prompt-aware Dynamic Rank Selection for SVD-based LLM Compression**

---

## 1. **论文的主要贡献和创新点**

### ✅ 解决的问题
现有的 **SVD-based LLM 压缩方法**（如 SVD-LLM、Basis Sharing 等）依赖于**静态秩截断（static rank truncation）**，即在训练后通过一个固定的校准集（calibration set）确定每个权重矩阵保留多少个奇异值，并将该固定秩应用于所有输入提示（prompt）。这种设计存在两个关键缺陷：

1. **输入无关的秩分配（Input-agnostic rank allocation）**  
   不同提示对模型行为的影响不同，所需的“有效秩”也应动态变化。静态方法会丢弃某些提示所需的关键奇异成分，导致局部性能下降。

2. **校准域偏差（Calibration-domain mismatch）**  
   所选秩高度依赖于校准数据集的分布。当下游任务与校准集语义不一致时（例如用数学数据校准却用于通用问答），压缩模型表现显著退化。

---

### 🚀 提出的新方法：PARSE
作者提出 **PARSE**（**P**rompt-**A**ware **R**ank **S**election as **E**xperts），一种**后训练（post-training）框架**，实现**动态、提示感知的秩选择**，核心思想如下：

- **将 SVD 分解后的每个奇异分量视为独立的 Rank Expert**  
  将权重矩阵 $ W = \sum_{i=1}^{r_{\text{max}}} \sigma_i u_i v_i^\top $ 中的每一项 $ \sigma_i u_i v_i^\top $ 视为一个独立的“专家”。

- **引入离线训练的线性路由器（Linear Router）进行提示感知选择**  
  对每个输入 $ x $，路由器 $ f_\theta(x) $ 输出各 rank expert 的得分，选择 Top-K 得分对应的奇异分量组成当前有效的低秩近似。

- **解耦路由决策与校准信息**  
  路由器在大规模多样化语料（如 C4）上监督训练，目标是逼近原始 dense model 的输出，而非依赖特定校准集统计特性。

- **推理阶段优化：Rank Retrieval & Reuse**
  - **Prefill 阶段**：利用 prompt embedding 在缓存中查找最相似提示对应的 rank 子集（避免在线路由）
  - **Decode 阶段**：复用 prefill 阶段选定的 rank 子集（rank selection 在生成过程中稳定）

- **系统级优化提升效率**
  - **Expert Memory Aggregation**：将选中的 rank expert 连续存储，提高 GPU 内存合并访问效率
  - **Kernel Fusion**：融合共享输入的 MatMul 操作（如 Q/K/V 投影），减少 kernel launch 开销

---

### 🔍 相比现有方法的优势
| 维度 | 静态 SVD 方法 | PARSE |
|------|----------------|--------|
| 秩选择策略 | 固定、全局统一 | 动态、按提示自适应 |
| 校准集敏感性 | 强（domain mismatch 严重） | 弱（解耦于校准信息） |
| 推理开销 | 低（无额外计算） | 可控（通过缓存/重用消除） |
| 性能稳定性 | 差（per-prompt 波动大） | 好（平滑跟踪 dense model） |
| 兼容性 | 各自独立 | **正交于所有 SVD 方法**，可插拔集成 |

> ✅ **PARSE 是一种通用增强模块，可无缝集成到任何 SVD-based 压缩流程中，显著提升其鲁棒性和性能。**

---

## 2. **核心实验方法和设置**

### 📚 数据集使用
| 类型 | 数据集 |
|------|--------|
| **语言建模评估** | WikiText-2, PTB, C4 |
| **零样本推理评估** | OpenBookQA, ARC-e/c, WinoGrande, HellaSwag, PIQA, MathQA |
| **路由器训练数据** | C4（大规模通用文本） |
| **校准数据（SVD 白化）** | 多种组合测试（WikiText-2, PTB, C4, MathQA）用于验证 domain robustness |

---

### ⚙️ 实验设置
- **模型**：LLaMA-7B/13B/30B, Qwen2.5-7B
- **压缩比（Compression Ratio）**：0.2, 0.4, 0.6（保留参数比例）
- **评估方式**：
  - **Perplexity (PPL)**：越低越好（语言建模）
  - **Zero-shot Accuracy**：越高越好（推理任务）
  - **Latency**：prefill 和 decode 阶段延迟（ms/token）
- **实现细节**：
  - 路由器为单层 Linear Gating Layer
  - 使用 AdamW 优化，bfloat16 训练，batch size=64
  - 缓存机制基于 prompt embedding 的余弦相似度匹配

---

### 🆚 基线方法对比
PARSE 并非替代现有 SVD 方法，而是作为增强模块与其结合：

| 基线方法 | 简介 |
|---------|------|
| **FWSVD** | 基于 Fisher 信息加权的 SVD |
| **ASVD** | 利用激活统计调整权重再分解 |
| **SVD-LLM** | 引入数据白化对齐奇异值与激活重建误差 |
| **Dobi-SVD** | 可微分截断，支持梯度优化 |
| **Basis Sharing** | 层间共享基向量以进一步压缩 |
| **SAES-SVD** | 联合抑制层内与跨层累积误差 |

> 所有基线均采用相同压缩比设置，PARSE 在此基础上增加动态秩选择能力。

---

## 3. **主要实验结果和性能指标**

### 📊 主要性能提升（LLaMA-7B, Compression Ratio = 0.6）

| 方法 | Avg. Zero-shot Accuracy ↑ | C4 PPL ↓ | WikiText-2 PPL ↓ |
|------|----------------------------|----------|------------------|
| SAES-SVD | 0.34 | 93.97 | — |
| **SAES-SVD + PARSE** | **0.44** (+10%) | **81.46** | **19.83** |
| Basis Sharing | 0.40 | 101.21 | 21.56 |
| **Basis Sharing + PARSE** | **0.40** | **101.21** | **21.56** |

> ✅ **PARSE 在极端压缩下仍保持高质量，平均准确率提升高达 10%。**

---

### ⏱️ 推理速度提升（vs. Native SVD）
| 场景 | Speedup |
|------|--------|
| **Prefill Latency** | 最高 **2.5× 加速** |
| **Decode Latency** | 最高 **2.4× 加速** |
| **小批量（batch=1）** | 较 dense vLLM 快达 **2.0×** |

> 💡 加速来自 kernel fusion 和 memory coalescing，且优于原生 SVD 实现。

---

### 🔬 消融实验结果

#### （1）Rank Retrieval & Reuse 的影响（Table 3）
| 方法 | Wiki2 PPL | Acc | Prefill Latency (ms) | Decode Latency (ms) |
|------|-----------|-----|----------------------|-----------------------|
| SVD-LLM | 7.94 | 0.44 | 217.08 | 25.56 |
| +PARSE (Router Only) | **7.16** | **0.52** | 516.49 | 68.14 |
| +Rank Retrieval | 7.43 | 0.50 | **121.64** | 68.19 |
| +Rank Reuse | 7.16 | 0.49 | 517.61 | **20.78** |
| **+PARSE (Full)** | 7.43 | 0.48 | **120.72** | **19.06** |

> ✅ 结合 retrieval 和 reuse 后，**延迟大幅降低，质量损失极小**，实现高效部署。

---

#### （2）内存聚合与 kernel fusion 效果（Figure 8）
- **无优化**：prefill 延迟高达 13.2s（batch=64）
- **+Memory Aggregation**：降至 8.4s
- **+Kernel Fusion**：进一步降至 **6.9s**
- **最终 decode 延迟从 119ms → 85ms**

> ✅ 系统级优化对实际性能至关重要。

---

#### （3）路由器训练数据的影响（Table 4）
| 训练数据 | Avg. Accuracy |
|--------|---------------|
| WikiText-2 | 0.50 |
| PTB | 0.48 |
| **C4（多样语料）** | **0.51** |

> ✅ 使用更广泛的数据训练路由器可提升泛化能力，避免 domain bias。

---

#### （4）对校准数据的鲁棒性（Table 7）
无论使用 WikiText-2、PTB、C4 或 MathQA 作为 SVD 校准集，PARSE 的性能波动极小：
- WikiText-2 PPL: 6.98–7.05
- Avg Acc: 0.50–0.51

> ✅ 成功解耦了秩选择与校准过程，增强了跨域稳定性。

---

## 4. **关键结论和发现**

### ✅ 主要发现
1. **最优秩是提示相关的（Prompt-dependent）**  
   不同提示需要保留不同的奇异分量子集，静态截断会导致局部性能崩溃（见 Figure 1 & 9）。

2. **秩选择模式具有语义共享性和时间稳定性**  
   - 语义相近的 prompt 会选择高度重叠的 rank 子集（Spearman ρ=0.78）
   - 同一 prompt 在 decode 过程中 rank 选择高度一致（overlap > 0.86）

3. **简单线性路由器已足够有效**  
   单层 linear gating 表现最佳，更深或更大的 router 反而性能下降，说明任务本质是线性可分。

4. **PARSE 可独立生效**  
   即使应用于 vanilla SVD（无 whitening/error correction），也能将 PPL 从 >19k 降到 ~300，证明其自身有效性。

---

### ⚠️ 局限性（Limitations）
- 当前仅在 **decoder-only 架构** 上验证（如 LLaMA、Qwen）
- 未测试多模态、encoder-decoder 或指令调优生产系统
- Rank pattern cache 增加了离线预处理和内存开销
- 性能依赖于 rank selection 的稳定性，极端长序列可能失效
- 实验基于 NVIDIA RTX A6000，硬件迁移可能存在差异

---

### 🔮 未来工作方向
- 扩展至 MoE 架构或 vision-language models
- 探索轻量化在线路由机制（适用于无法缓存场景）
- 动态调整每层的 rank budget（K）以实现细粒度控制
- 结合量化或稀疏化形成复合压缩方案
- 研究 rank selection 与 reasoning path 的关联性

---

## ✅ 总结
**PARSE 提供了一种全新的视角来理解 SVD 压缩：从“一刀切”的静态截断转向“因材施教”的动态专家选择**。它不仅显著提升了压缩模型的质量和鲁棒性，还通过系统优化实现了真正的端到端加速。作为一种**正交增强技术**，PARSE 有望成为未来 SVD-based LLM 压缩的标准组件之一。

</details>

---

### 2. [ATLAS: Efficient Out-of-Core Inference for Billion-Scale Graph Neural Networks](https://arxiv.org/abs/2605.09402)

**Authors**: Pranjal Naman, Yogesh Simmhan  
**Category**: cs.DC  
**Published**: 2026-05-12  
**Score**: 13.5  
**Type**: new  
**ArXiv ID**: 2605.09402v1  

#### Abstract
Graph Neural Network (GNN) inference on billion-scale graphs is critical for domains like fintech and recommendation systems. Full-graph inference on these large graphs can be challenging due to high communication costs in distributed settings and high I/O costs in disk-backed Out-of-Core (OOC) sett...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文《ATLAS: Efficient Out-of-Core Inference for Billion-Scale Graph Neural Networks》总结

---

## 1. 论文的主要贡献和创新点

### **解决了什么问题**

本文针对**十亿级图神经网络（GNN）在单机环境下的全图推理（full-graph inference）效率低下**的问题展开研究。现有方法面临以下挑战：

- **高I/O开销**：当图的拓扑、特征和中间嵌入（embeddings）超出内存时，传统基于gather的执行模式导致大量随机读取和重复读取，引发严重的**读放大（read amplification）**。
- **内存压力大**：层间嵌入无法完全驻留内存，频繁的换入换出造成性能瓶颈。
- **现有OOC系统偏向训练**：多数out-of-core（OOC）系统专注于GNN训练，而训练通常只处理少量有标签节点，与需要全图确定性推理的任务存在根本差异。

### **提出了什么新方法或新思路**

作者提出 **ATLAS** —— 一种基于**广播（broadcast-based）** 的OOC GNN推理框架，其核心设计思想包括：

1. **Broadcast-based Execution Model**  
   将传统的“每个目标节点拉取邻居信息”（gather-based）改为“每个源节点推送消息到出边”（broadcast-based），从而实现对特征和嵌入的**顺序、单次扫描读取**，极大减少I/O次数和读放大。

2. **Tiered Memory-Disk Hierarchy**  
   设计了一个分层的内存-磁盘运行时系统：
   - **Hot Store**：RAM中缓存部分聚合状态的顶点。
   - **Cold Store**：SSD上保存被驱逐的中间状态。
   - 引入**最小待收消息数驱逐策略（minimum-pending-message eviction policy）**，优先驱逐接近完成的顶点，减少反复加载（thrashing）。

3. **Pipelined and Overlapped Execution**  
   构建完整流水线，支持：
   - 并行读取拓扑与特征（从SSD）
   - CPU端聚合
   - GPU端前向传播
   - 多线程写回
   实现I/O、计算、通信的高度重叠。

4. **Graph Reordering**  
   在预处理阶段通过贪心启发式算法重新排序顶点ID，最大化每批处理后的全局完成度，提升早期毕业率，降低内存占用。

---

### **相比现有方法的优势**

| 维度 | 优势 |
|------|------|
| **I/O效率** | 顺序读写替代随机访问，读取量减少1–2个数量级 |
| **内存管理** | 分层存储+智能驱逐策略显著降低冷热店切换频率 |
| **可扩展性** | 支持特征高达550 GiB的十亿边级图，在单工作站即可完成推理 |
| **兼容性** | 支持多种message-passing架构（GCN, GIN, GraphSAGE等） |

---

## 2. 核心实验方法和设置

### **使用的数据集**

| 数据集 | 节点数 | 边数 | 特征大小（GiB） | 类型 |
|--------|--------|-------|------------------|------|
| **Papers (PA)** | 111M | 1.7B | 54 (FP32) | 学术引用图 |
| **MAG-Cites (MA)** | 121M | 1.4B | 175 (FP16) | 学术引用图 |
| **IGB-Large (IL)** | 100M | 1.2B | 200 (FP16) | 合成大规模图 |
| **IGB-Full (IF)** | 269M | 4B | 550 (FP16) | 最大测试图 |

> 所有图均超出单机RAM（128 GiB）和GPU显存（32 GiB），需依赖SSD进行OOC处理。

---

### **实验设置和评估指标**

- **硬件平台**：
  - CPU: AMD Ryzen 9 9900X (12核)
  - RAM: 128 GiB
  - GPU: NVIDIA RTX 5090 (32 GiB)
  - SSD: 2 TiB Samsung 990 PRO NVMe

- **模型配置**：
  - 使用2层GNN：GCN, GIN, GraphSAGE
  - 隐藏维度：128
  - 全图推理（无采样）

- **评估指标**：
  - **End-to-End 推理时间**
  - **总读取字节数（disk read volume）**
  - **资源利用率**（CPU/GPU/SSD带宽）
  - **消融实验**：验证各组件影响（如排序、驱逐策略、内存预算）

---

### **基线方法对比**

| 基线 | 类型 | 描述 |
|------|------|------|
| **Ginex [24]** | Vertex-wise + OOC Training Framework | 原为训练设计，采用邻域缓存与superbatch机制，适配为仅前向推理 |
| **DGI [44]** | Layer-wise Inference | 支持动态批处理与图重排的layer-wise推理框架，使用mmap映射文件 |

> 注意：两者均为SOTA级别的OOC GNN系统，但未专门优化全图推理场景。

---

## 3. 主要实验结果和性能指标

### **关键性能数据**

| 图 | 模型 | ATLAS 推理时间 | DGI 推理时间（外推） | 加速比 |
|-----|--------|------------------|-------------------------|--------|
| PA | SAGE2 | ~13 min | ~17 min | ~1.3× |
| MA | SAGE2 | <1h | ~11h | **~12×** |
| IL | SAGE2 | ~1.5h | ~36× ATLAS | **~36×** |
| IF | GCN2 | ~3h | ~117h | **~39×** |

> 注：超过6小时未完成任务按线性进度外推。

### **与基线方法的对比结果**

- **I/O流量大幅下降**：
  - ATLAS 的总读取量比 Ginex 和 DGI **低1–2个数量级**。
  - 例如在 MA 上，Ginex 读取达 **7.7 TiB**，而 ATLAS 仅为 **~3.6 TiB（两层合计）**。

- **执行时间显著缩短**：
  - 平均加速比：**12–30×** 超过SOTA基线。
  - 在内存受限图（MA/IL/IF）上优势尤为明显；在PA（可近似内存驻留）上仍保持竞争力（相差<5%）。

- **成功运行最大规模图**：
  - DGI 和 Ginex 在 IF 图上无法完成第一层推理（OOM 或超时），而 ATLAS 可稳定完成。

---

### **消融实验结果**

#### ✅ **图重排序（Graph Reordering）的影响**
- 使用ATLAS提出的贪心排序后：
  - 再加载时间（reload time）减少 **3×以上**
  - 总体执行时间下降约 **35–40%**
  - 平均每chunk再加载顶点比例从~7%降至~1%

#### ✅ **驱逐策略（Eviction Policy）的影响**
- 对比 RND、LRU 和 Minimum-Pending-Message（AT）：
  - AT策略使冷存储I/O减少 **3–5.6×**
  - 再加载次数减少 **~44%（IL）、~36%（MA）**
  - LRU表现最差，因其可能提前驱逐高入度活跃节点

#### ✅ **Hot Store 内存预算敏感性**
- 当Hot Store ≥ 临界值时（IL: 70 GiB, MA: 60 GiB），基本消除换页，性能趋于稳定。
- 小于该阈值时，执行时间随内存减小呈指数上升。
- 表明 ATLAS 在 **60–80 GiB 内存预算下即可高效运行200+ GiB特征图**。

---

## 4. 关键结论和发现

### **主要发现**

1. **Gather-based执行是OOC推理的根本瓶颈**  
   传统gather模式导致严重I/O放大和内存碎片化，不适合全图确定性推理。

2. **Broadcast范式可有效转化为顺序I/O**  
   通过将“pull”转为“push”，实现了真正的单遍扫描读取，从根本上缓解I/O压力。

3. **系统级协同设计至关重要**  
   单纯改进算法或调度不足以解决问题，必须结合：
   - 数据布局（range-partitioned spill files）
   - 图重排
   - 分层内存管理
   - 流水线并行
   才能实现端到端高性能。

4. **单机OOC推理可行且高效**  
   利用现代NVMe SSD的大容量与高吞吐，配合合理系统设计，可在普通工作站完成百亿级图推理，无需昂贵分布式集群。

---

### **方法的局限性**

- **当前仅支持message-passing类GNN**  
  如GCN、GIN、SAGE等，尚未支持GAT等attention-based layers。
  
- **不适用于增量推理场景**  
  本工作聚焦全图批量推理，虽可用于初始化，但非为实时更新设计（尽管作者提及未来可拓展至incremental inference）。

- **预处理开销存在**  
  图重排序是一次性离线成本（约3–4分钟），虽可摊销，但仍增加部署复杂度。

- **依赖特定I/O特性**  
  使用`O_DIRECT`绕过page cache，对SSD性能要求较高，在低端设备上收益可能打折扣。

---

### **未来工作方向**

1. **扩展至更多GNN架构**  
   支持GAT、SGC等更复杂的message函数。

2. **集成Incremental Inference**  
   结合作者团队先前工作（如Ripple系列），构建统一的全量+增量推理引擎。

3. **跨设备异构优化**  
   探索CPU-GPU-NVM联合调度，进一步压榨硬件潜力。

4. **自动化参数调优**  
   开发自适应模块，根据图结构自动选择chunk size、hot store大小、是否启用重排等。

---

> **总结一句话**：  
> ATLAS 通过引入 **broadcast-driven execution + tiered memory hierarchy + intelligent reordering & eviction**，首次实现了在单机上高效完成十亿级图的全图GNN推理，相较SOTA提速 **12–30×**，为低成本大规模图学习提供了新路径。

</details>

---

### 3. [Generalization Bounds of Emergent Communications for Agentic AI Networking](https://arxiv.org/abs/2605.08613)

**Authors**: Yong Xiao, Jingxuan Chai, Guangming Shi, Ping Zhang  
**Category**: cs.AI  
**Published**: 2026-05-12  
**Score**: 12.0  
**Type**: new  
**ArXiv ID**: 2605.08613v1  

#### Abstract
The evolution of 6G networking toward agentic AI networking (AgentNet) systems requires a shift from traditional data pipelines to task-aware, agentic AI-native communication solutions. Emergent communication, a novel communication paradigm in which autonomous agents learn their own signaling protoc...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Generalization Bounds of Emergent Communications for Agentic AI Networking

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
传统通信网络依赖**预定义、刚性的协议架构**（如固定帧结构和标准化信令），难以适应 Agentic AI Networking（AgentNet）系统中动态、多模态、任务驱动的智能体协作需求。现有 **emergent communication**（EC）框架虽然能自主学习通信协议，但普遍存在以下问题：
- 忽视物理层约束（如带宽、计算复杂度）
- 缺乏严格的信息论基础
- 实验导向强，泛化能力差，理论保障不足

本文旨在解决上述挑战，提出一个**信息论可解释、资源受限下仍具高泛化性的 emergent communication 框架**。

---

### 🚀 提出的新方法与创新思路

#### （1）基于 Multi-Agent Multi-Task Distributed Information Bottleneck (DIB) 的联合优化框架
- 将 emergent communication 建模为在保留**任务相关性信息**（task-relevant information）的同时最小化**表示复杂度**（computational complexity）的过程。
- 引入两个关键互信息项：
  - $ I(Y_k; C_{-k,k}) $：消息对目标任务的语义相关性
  - $ I(S_k; C_{k,-k}) $：消息的 Minimum Description Length (MDL)，衡量通信开销与计算负担

#### （2）设计新型联合损失函数（Joint Loss Function）
将决策函数（decision-making function）与通信信号学习统一到单一目标中：
$$
\mathcal{L}_{\text{joint}} = \sum_k \left[ \mathcal{L}_k(\theta_k, \phi_k; z_k) - \lambda_i I(Y_k; C_{-k,k}) + \lambda_c I(S_k; C_{k,-k}) \right]
$$
该损失函数通过 DIB 正则化项实现：
- 最大化任务相关性 → 提升性能
- 最小化描述长度 → 抑制过拟合、降低通信负载

#### （3）提供理论泛化界（Generalization Bounds）
基于 Rényi divergence 和 sub-Gaussian 假设，推导出 emergent communication 协议在**未见环境状态下的泛化误差上界**：
$$
\epsilon(\theta_k, \phi_k) \leq \sqrt{\frac{2\sigma^2}{n} D_k \cdot M_k}
$$
其中：
- $ D_k $：后验与先验之间的 Rényi divergence，反映协议复杂度
- $ M_k $：统计学习难度，受样本量 $ n $ 和噪声方差影响

此理论结果首次为 decentralized emergent communication 提供了**数学可证明的稳定性与鲁棒性保证**。

---

### 🔍 相比现有方法的优势

| 维度 | 本文方法 | 现有主流方法（如 EC-SOTA） |
|------|----------|-----------------------------|
| **架构设计** | 联合训练决策与通信模块 | 模块化分离训练（如 Autoencoder + Policy Net） |
| **理论支撑** | 基于 DIB 的信息论建模，具备泛化界 | 多为启发式设计，缺乏理论分析 |
| **资源效率** | 显式控制 MDL，减少冗余通信 | 通常忽略带宽与计算成本 |
| **泛化能力** | 在未知场景下保持稳定性能 | 容易出现 representation drift 或过拟合 |

---

## 2. 核心实验方法和设置

### 📊 数据集
- **应用层数据**：采用公开的真实智能手机流量数据集 [15]，涵盖五类典型应用：
  - Live Streaming（直播）
  - Video Conferencing（视频会议）
  - Mobile Gaming（移动游戏）
  - Social Media
  - Web Browsing
- 包含真实时间序列行为、QoE 指标等，用于模拟 agent 的观测输入与 reward 信号。

### ⚙️ 实验平台与设置
- 构建基于开源 RAN 与软件化 5G Core 的硬件原型系统，包含：
  - User Equipment (UE)
  - gNodeB (gNB)
  - 5G Core (5GC)
- 部署两类 agent：
  - **Application-layer Agent**：观察应用层流量特征，预测 QoE 并发送信号
  - **Physical-layer Agent**：接收信号并动态调整无线资源配置（如调制编码策略、资源块分配）

### 📈 评估指标
- **Accuracy**：application-layer agent 对任务目标的识别准确率
- **Generalization Error**：训练损失与推理损失之间的差距
- **Convergence Speed**：达到稳定性能所需的迭代次数
- **Error Floor**：收敛后的最小泛化误差水平

### 🆚 基线方法
- **EC-SOTA** [16]：当前最先进的 emergent communication 方法
  - 使用独立 autoencoder 学习 latent 表示
  - 决策模型与通信模型分阶段训练
  - 无显式复杂度正则化机制

---

## 3. 主要实验结果和性能指标

### 📈 性能对比（见 Fig. 2 与 Fig. 3）

#### （1）准确率表现（Fig. 2）
- 在不同迭代轮次下，本文方法始终优于 EC-SOTA
- 收敛速度更快，在约 6,000 次迭代内即趋于稳定
- 最终 accuracy 提升约 **8–12%**，尤其在高动态场景（如 Live Streaming）提升显著

#### （2）泛化误差对比（Fig. 3）
| 方法 | 泛化误差峰值 | 收敛后误差 floor | 收敛所需迭代数 |
|------|---------------|------------------|----------------|
| EC-SOTA | ~18% | ~9% | >9,000 |
| **本文方法** | **~10%** | **~3%** | **<6,000** |

- 本文方法的训练-推理 gap 更小，表明更强的**跨环境泛化能力**
- 错误下限更低且更平稳，说明协议更具**结构性稳定性**

#### （3）消融实验（文中隐含验证）
尽管未明确列出消融表，但从理论与实验一致性可推断：
- 若移除 DIB 正则项（尤其是 $ I(S_k; C_{k,-k}) $），会出现“信息坍塌”（informational collapse）现象，导致过拟合
- 若不联合优化决策与通信，则存在“语义漂移”（representation drift），影响长期协作稳定性

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **联合优化 + DIB 正则化显著提升 emergent communication 的泛化能力**
   - 通过统一 loss 设计，避免了模块间不匹配问题
   - DIB 提供了信息压缩与任务保真之间的最优平衡

2. **MDL 正则化有效抑制噪声过拟合，增强鲁棒性**
   - 控制 message 的描述长度，使协议更简洁、抗干扰能力强

3. **理论泛化界与实证结果高度一致**
   - 实验中观察到的小 $ D_k $ 和低 $ M_k $ 对应更好的泛化性能
   - 验证了信息论指导设计的有效性

4. **适用于真实 6G AgentNet 场景**
   - 在真实流量与硬件平台上验证，具备工程落地潜力

---

### ⚠️ 局限性
- 当前实验仅考虑两个 agent 的协作，扩展至大规模 multi-agent 系统时可能面临协调复杂度上升问题
- 假设 reward signal 可获得（虽可离线提供），但在完全无监督 setting 下适用性有待验证
- 理论分析基于 sub-Gaussian 假设，在极端非高斯噪声环境下边界可能偏松

---

### 🔮 未来工作方向
1. 扩展至 **large-scale heterogeneous AgentNet**，研究分层通信拓扑与路由机制
2. 探索 **online reward delivery + continual learning** 机制，支持实时自适应更新
3. 结合 **LLMs as Agents**，构建生成式 emergent communication 协议
4. 进一步放松理论假设，发展更通用的泛化分析工具（如 PAC-Bayes 框架）

---

## ✅ 总结
本论文提出了首个**基于 DIB 理论、具备严格泛化界保证的 emergent communication 框架**，解决了传统方法在理论支撑、资源效率与泛化能力方面的短板。通过联合优化决策与通信，并引入信息瓶颈正则化，实现了更高效、更稳健的 agent 间协作。实验在真实硬件平台上验证了其优越性能，为 6G 中的 Agentic AI Networking 提供了坚实的理论与实践基础。

</details>

---

### 4. [Agent-X: Full Pipeline Acceleration of On-device AI Agents](https://arxiv.org/abs/2605.10380)

**Authors**: Jinha Chung, Byeongjun Shin, Jiin Kim, Minsoo Rhu  
**Category**: cs.AI  
**Published**: 2026-05-12  
**Score**: 11.5  
**Type**: new  
**ArXiv ID**: 2605.10380v1  

#### Abstract
LLM-based agents deliver state-of-the-art performance across tasks but incur high end-to-end latency on edge devices. We introduce Agent-X, a software-only, accuracy-preserving framework that accelerates both the prefill and decode stages of on-device agent workloads. Agent-X's two key components re...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Agent-X: Full Pipeline Acceleration of On-device AI Agents

## 1. 论文的主要贡献和创新点

### 解决的问题
- **On-device AI agents** 在边缘设备上运行时面临显著的端到端延迟问题，尤其是在资源受限环境下。
- 传统研究主要关注云上LLM的decode阶段优化，而本文指出在on-device场景中，**prefill 和 decode 阶段都构成性能瓶颈**，需要全流水线加速。

### 提出的新方法与创新思路
提出 **Agent-X** ——一种纯软件、不损失准确性的端到端加速框架，包含两个核心组件：

#### ✅ PromptWeaver（针对 prefill 阶段）
- **动态重构输入 prompt**，将原本因工具选择导致“早期动态性”的 prompt 转换为可缓存的静态前缀。
- 利用 **tool co-activation locality** 进行聚类，并基于主题排序和组合选择，最大化 **prefix caching** 的复用率。
- 引入离线预计算的 KV cache 存储机制，减少在线计算开销。

#### ✅ ExSpec（针对 decode 阶段）
- 提出 **LLM-free speculative decoding** 方案，使用轻量级 **n-gram lookup table (LUT)** 作为 draft model。
- 支持 **selective fallback**：当上下文未命中 LUT 时，直接回退到 autoregressive 生成，避免 multi-token tax 开销。
- 实现无需训练、低内存占用（仅几KB）、零额外延迟的高效 speculative decoding。

### 相比现有方法的优势
| 维度 | Agent-X 的优势 |
|------|----------------|
| **准确性** | 完全保留原始任务精度（no accuracy loss） |
| **部署成本** | 纯软件方案，无需硬件修改或模型重训练 |
| **资源消耗** | ExSpec 使用 LUT 替代小型 LLM，节省数百MB内存 |
| **系统兼容性** | 可无缝集成至现有 on-device agent 框架（如 TinyAgent） |
| **加速全面性** | 同时优化 prefill 与 decode，实现 full-pipeline 加速 |

---

## 2. 核心实验方法和设置

### 数据集
- 使用开源 on-device agent 框架 **TinyAgent [19]** 提供的数据集：
  - **TinyAgent-dataset [68]**：包含 1,022 个测试样本，涵盖最多 16 种不同工具调用的任务。
  - 查询类型多样，涉及日历、邮件、联系人等常见功能。
- 训练数据用于 PromptWeaver 中的 tool clustering 和 combination selection。

### 实验平台
- **硬件**：Apple Mac mini（M4 Pro芯片），64GB RAM，512GB SSD
- **软件栈**：
  - 基于 **MLX-LM [10]** 和 **MLX-engine [43]**
  - 后端模型：**TinyAgent-7B [67]**（基于 WizardLM-2-7B 微调）

### 评估指标
| 指标 | 描述 |
|------|------|
| **End-to-end latency** | 从接收用户请求到完成任务的总耗时 |
| **Prefill / Decode latency** | 分别测量两个阶段的时间占比 |
| **Speedup** | 相对于 baseline 的加速比 |
| **Planner accuracy** | 构建 DAG 并与 ground truth 对比，衡量计划正确性 |
| **KV cache reuse rate** | 缓存命中的 token 比例 |
| **Draft token accuracy** | speculative decoding 中被接受的 draft token 比例 |

### 基线方法对比
- **Baseline**：原始 TinyAgent 流程（含 ToolRAG）
- **Static caching**：仅对完全静态部分进行 prefix caching
- **SpecDec (Llama-3.2-1B-Instruct)**：使用小型 LLM 作为 draft model 的 speculative decoding
- **Ablation variants**：分别测试 PromptWeaver 和 ExSpec 的独立效果

---

## 3. 主要实验结果和性能指标

### 关键性能数据
| 模块 | 性能提升 |
|------|--------|
| **Prefill 阶段加速** | **1.97×**（Planner） |
| **Decode 阶段加速** | **1.73×**（平均） |
| **端到端整体加速** | **1.61×** |
| **Arbiter prefill 加速** | 高达 **4.35×**（因其输入高度静态） |

### 与基线方法的对比结果
| 方法 | Planner Decode Speedup | Arbiter Decode Speedup | 备注 |
|------|------------------------|-------------------------|------|
| Baseline | 1.00× | 1.00× | 原始性能 |
| SpecDec (Llama-3.2-1B) | **0.83×**（变慢） | **0.91×** | 因 multi-token tax 和 tokenizer 差异导致负优化 |
| **ExSpec (n=3)** | **1.38×**（非选择） → **1.73×**（选择） | **1.73×** | 显著优于 LLM-based speculative decoding |

> 🔍 注：即使使用 fine-tuned 的 TinyAgent-1.1B 作为 draft model，仍比 baseline **慢 1.81×**

### 消融实验结果
#### PromptWeaver 消融分析（Figure 14）
- 添加 **K=1 个动态 tool-use example** 即可恢复并略微超过 baseline 准确率（0.841 > 0.836）
- 更多示例反而降低准确率，说明过拟合风险
- **uncacheable tokens 数量下降 70%**（从 1,711 → 519）

#### ExSpec 消融分析（Table 3）
| 设置 | Draft Token Accuracy | 优势说明 |
|------|-----------------------|----------|
| Non-selective | 0.13 (Planner) | 产生更多 draft tokens，但接受率低 |
| **Selective** | **0.25 (Planner)** | 虽生成更少，但质量更高，有效规避无效验证 |
| Selective fallback 次数 | ~17次/查询（Planner），~37次/查询（Arbiter） | 动态判断是否启用 speculation |

#### KV Cache 存储开销（Figure 15）
- 使用 **15 cluster combinations**（约 6.26 GB SSD 存储）
- 实现 **74.4% 的 tool-use example 覆盖率**
- 边际收益递减，表明小预算即可获得高复用

---

## 4. 关键结论和发现

### 主要发现
1. ❗ **On-device agents 的性能瓶颈不同于云端 LLM**：
   - 不是单一 decode 瓶颈，而是 **prefill 与 decode 共同主导延迟**
   - 原因：长输入序列 + 边缘设备算力/带宽受限 → prefill 成为瓶颈

2. 🔄 **Agent-specific 输入模式具有强结构性**：
   - 工具之间存在明显的 **co-activation locality**
   - 输出高度依赖 few-shot examples，呈现模板化特征
   - 可利用这些特性设计针对性优化策略

3. ⚖️ **Speculative decoding 在边缘设备上难以直接应用**：
   - 小型 draft LLM 准确率太低 → 加速有限
   - 大型 draft LLM 延迟高 + multi-token tax → 反而变慢
   - **ExSpec 的 LUT 设计解决了这一矛盾**

4. 💡 **轻量化、无训练需求的方法更适合边缘部署**：
   - PromptWeaver 和 ExSpec 均无需 retraining
   - 仅需离线构建 cache 和 LUT，适合资源敏感环境

### 方法的局限性
| 局限 | 说明 |
|------|------|
| **依赖特定 agent 架构** | 当前设计针对 plan-out 类 agent（如 LLMCompiler）优化，ReAct 类可能增益较小 |
| **KV cache 存储开销** | 需要数 GB SSD 空间存储预计算 cache，在极低端设备可能受限 |
| **prompt 扩展影响 decode 内存访问** | Planner 输入增长导致 decode 阶段 KV cache 加载增加，带来轻微带宽压力（+2.2% T/POT） |
| **通用性待验证** | 目前仅在 TinyAgent 上验证，跨平台迁移需适配 |

### 未来工作方向
1. **扩展到多模态 agents**：结合视觉输入的 mobile-agent 场景
2. **支持动态工具注册**：当前假设工具集固定，未来可支持 runtime 新增工具
3. **联合压缩与加速**：结合 quantization、pruning 等技术进一步降低资源占用
4. **跨设备协同推理**：探索 edge-cloud 协同下的 pipeline 分割优化
5. **自动化 cache budget allocation**：根据设备配置自适应调整 cluster combination 数量

---

> ✅ **总体评价**：  
> Agent-X 是首个系统性分析并解决 on-device AI agent 全流程延迟问题的工作。其提出的 **PromptWeaver + ExSpec** 双引擎架构，在不牺牲准确性的前提下实现了 **1.61× 端到端加速**，且为纯软件方案，具备良好的实用性和推广潜力。该工作揭示了边缘智能体的独特挑战，并为 future edge AI systems 提供了重要设计范式。

</details>

---

### 5. [PhysEDA: Physics-Aware Learning Framework for Efficient EDA With Manhattan Distance Decay](https://arxiv.org/abs/2605.10547)

**Authors**: Zetao Yang  
**Category**: cs.LG  
**Published**: 2026-05-12  
**Score**: 11.5  
**Type**: new  
**ArXiv ID**: 2605.10547v1  

#### Abstract
Electronic design automation (EDA) addresses placement, routing, timing analysis, and power-integrity verification for integrated circuits. Learning methods -- attention (Transformer) and reinforcement learning (RL) -- have recently emerged on EDA tasks, yet face two common bottlenecks: vanilla atte...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# PhysEDA: Physics-Aware Learning Framework for Efficient EDA With Manhattan Distance Decay

## 1. 论文的主要贡献和创新点

### 解决的问题
现代电子设计自动化（EDA）任务在**可扩展性、数据效率和训练效率**上面临三大瓶颈：
- **Solution Scale**: 传统 Transformer 的 `softmax` attention 具有 $O(L^2)$ 的二次复杂度，当候选位置数量 $L$ 超过约 10,000 时，内存消耗变得不可行。
- **Data Efficiency**: 在数据稀缺场景（如 decoupling-capacitor placement, DPP），模型难以从有限样本中学习到正确的空间物理规律，容易过拟合并放大不符合物理的长程相关性。
- **Training Efficiency**: 强化学习（RL）在 EDA 任务中面临严重的奖励稀疏性（reward sparsity），例如在 DPP 中，只有放置完所有电容后才能获得非零奖励，中间步骤无监督信号。

### 提出的新方法
论文提出 **PhysEDA**，一个将物理先验（physical prior）统一集成到架构和训练中的框架，包含两个核心组件：

#### (1) Physics-Structured Linear Attention (PSLA)
- **核心思想**：利用 EDA 任务中普遍存在的物理规律——**电气和布线交互随曼哈顿距离（Manhattan distance）指数衰减**（即 $ \exp(-\alpha \cdot d_M) $）。
- **实现方式**：将该衰减核作为**可学习的乘法偏置（multiplicative bias）** 融入线性注意力（linear attention）机制中。
- **优势**：
  - 将计算复杂度从 $O(L^2d)$ 降低到 $O(Ld^2)$，实现了**线性复杂度**。
  - 通过物理先验提供强大的**归纳偏置（inductive bias）**，显著提升数据稀缺场景下的泛化能力。
  - 支持跨尺度（cross-scale）零样本迁移。

#### (2) Potential-Based Reward Shaping (PBRS)
- **核心思想**：利用相同的 $ \exp(-\alpha \cdot d_M) $ 物理核构建一个**物理势能函数（physical potential）**，用于奖励塑形（reward shaping）。
- **实现方式**：在原始稀疏奖励 $R$ 上添加一个由势能差构成的密集奖励信号：$R' = R + \gamma \Phi(s') - \Phi(s)$。
- **优势**：
  - 提供密集的中间奖励信号，极大缓解了 RL 的探索难题。
  - 根据 **policy-invariance theorem**，该操作不改变最优策略，保证了最终解的正确性。

### 相比现有方法的优势
- **统一性**：首次将同一个物理先验同时用于**架构设计**（PSLA）和**训练过程**（PBRS），形成协同效应。
- **高效性**：PSLA 实现了高达 **14× 的推理加速** 和 **98.5% 的内存节省**。
- **强泛化性**：在零样本跨尺度迁移上，相比 DevFormer 提升了 **56.8%**。
- **有效性**：PBRS 在稀疏奖励的 DPP 任务上额外带来了 **10.8%** 的性能提升。

---

## 2. 核心实验方法和设置

### 使用的数据集
1. **Decoupling-Capacitor Placement (DPP)**:
   - 基于 DevFormer 的物理公式生成，包含 2,300 个实例。
   - 分为 **2,000/100/200** 的训练/验证/测试集。
   - 测试了两种规模：`10×10` (L=100) 和 `25×25` (L=625) 网格。

2. **Macro Placement (ChiPFormer)**:
   - 使用公开的 **ISPD 2005 adaptec1** 基准，包含 452 个宏单元。
   - 预训练使用 ChiPFormer 发布的专家轨迹数据集。

3. **IR-drop Prediction (CircuitNet)**:
   - 使用 **CircuitNet 1.0** 开源数据集，包含多个芯片设计（NVDLA, Vortex, openc910 等）的功耗密度图和真实 IR-drop 图。
   - 评估了三种设置：**in-distribution**, **cross-design**, **cross-architecture**。

### 实验设置和评估指标
| 任务 | 模型架构 | 训练方式 | 主要评估指标 |
| :--- | :--- | :--- | :--- |
| **DPP** | Autoregressive Decoder | Imitation Learning + REINFORCE RL | DPP Score (越负越好) |
| **Macro Placement** | Decision Transformer | Offline Pretraining + Online RL Fine-tuning | HPWL (Half-Perimeter Wirelength, 越低越好) |
| **IR-drop Prediction** | UNet | Supervised Regression | Pearson Correlation (越高越好) |

### 基线方法对比
- **DPP**:
  - **DevFormer** [Kim et al., 2023]: 基于对称 Transformer 的 SOTA 方法。
  - 其他线性注意力变体：Plain GLA, FAVOR+, Simple Linear, CosFormer。
- **Macro Placement**:
  - **ChiPFormer** [Lai et al., 2023]: 基于 Decision Transformer 的基线。
- **IR-drop Prediction**:
  - **PowerNet, IREDGe, PDNNet**: 之前的 SOTA 方法。
  - **Baseline UNet**: 本实验中的直接对比基线。

---

## 3. 主要实验结果和性能指标

### 关键性能数据
| 任务 | 场景 | PhysEDA 结果 | 基线结果 | 提升幅度 |
| :--- | :--- | :--- | :--- | :--- |
| **DPP** | Imitation Learning (25×25) | **-16.76** | -15.88 (DevFormer) | **+5.5%** |
| **DPP** | RL (25×25) | **-17.40** | -13.34 (DevFormer+PBRS) | **+30.4%** |
| **DPP** | Zero-shot Transfer (10→25) | **-11.04** | -7.04 (DevFormer) | **+56.8%** |
| **Macro Placement** | DT Pretraining | **801,588** HPWL | 910,967 HPWL | **+12.0%** |
| **IR-drop** | Cross-design | **0.482** | 0.458 | **+5.3%** |
| **IR-drop** | Cross-architecture | **0.498** | 0.472 | **+5.4%** |

### 与基线方法的对比结果
- **PSLA** 是唯一在线性复杂度下超越二次复杂度 **DevFormer** 的方法，在 DPP 任务上实现了 **5.5%** 的绝对提升。
- 在 `25×25` 大规模 RL 任务上，**PSLA + PBRS** 组合相比基线实现了 **65.2%** 的巨大提升。
- 在零样本跨尺度迁移中，**PSLA** 表现出惊人的鲁棒性，而 **DevFormer** 性能严重下降（-33%），凸显了物理先验的泛化价值。

### 消融实验结果
论文通过消融实验证明了其核心设计的有效性：

1. **PSLA 组件消融 (DPP)**:
   - 移除 `Manhattan decay` 偏置：得分从 -16.76 降至 -16.18，证明**物理衰减是增益主因**。
   - 使用 `Euclidean decay` 替代：得分降至 -16.09，验证了**曼哈顿距离更符合物理事实**。
   - 移除位置编码：得分暴跌至 -13.91，表明**空间坐标信息至关重要**。

2. **PSLA vs. PBRS 协同作用**:
   - **PSLA** 在监督学习和零样本迁移中主导性能提升。
   - **PBRS** 在 RL 探索中发挥关键作用。
   - 两者结合效果最佳，但在某些 RL 微调场景下存在冲突（PSLA 的硬约束限制了 PBRS 的软探索）。

3. **数据稀缺性原则**:
   - 实验结果验证了一个核心发现：**PhysEDA 的增益与数据对空间结构的“不足程度”单调正相关**。
   - 在数据充足场景（如 CircuitNet in-distribution），PSLA 反而略逊于基线（-1.9%），因为物理先验可能限制了模型容量。
   - 在数据稀缺场景（如跨域、跨架构、大网格 RL），增益显著，最高达 **+65.2%**。

---

## 4. 关键结论和发现

### 主要发现
1. **统一物理先验的有效性**：将 **Manhattan distance decay** 这一物理规律同时作为架构（PSLA）和训练（PBRS）的归纳偏置，能够系统性地解决 EDA 任务的三大瓶颈。
2. **数据-效率权衡**：提出的物理先验在**数据稀缺、分布偏移和跨尺度迁移**等场景下价值最大，而在数据充足时可能成为冗余甚至轻微负担。
3. **效率与精度双赢**：PSLA 不仅大幅提升了计算效率（14× 速度，98.5% 内存节省），还因其更强的归纳偏置而在许多任务上取得了更高的精度。
4. **跨任务通用性**：PhysEDA 框架成功应用于三个截然不同的 EDA 任务（DPP, Macro Placement, IR-drop Prediction），证明了其广泛的适用性。

### 方法的局限性
1. **秩-1 因子分解的近似性**：当前 PSLA 使用的 `rank-1` 因子分解实现的是有向的指数衰减，而非完全对称的曼哈顿衰减。虽然在实践中有效，但存在理论上的近似。
2. **PBRS 的应用范围**：PBRS 仅适用于在线强化学习（online RL）场景，无法应用于纯监督学习或离线 RL。
3. **特定物理假设**：框架依赖于 `exp(-α·dM)` 这一特定形式的物理衰减，对于其他类型的物理交互可能需要重新设计。

### 未来工作方向
1. **双向前缀和分解**：采用 App. B 中提出的 `bidirectional prefix-sum` 方法，以 $O(L)$ 复杂度精确重建对称的曼哈顿衰减，消除方向性偏差。
2. **扩展物理势能**：探索更丰富的物理势能函数，如寄生电容（parasitic capacitance）、信号完整性裕量（signal-integrity margins）等。
3. **拓展应用领域**：将 PhysEDA 框架推广到时钟分配（clock distribution）、热分析（thermal analysis）等其他 EDA 任务中。
4. **动态衰减率**：研究更复杂的机制来动态生成衰减率 $\alpha$，而不仅仅是每头每层的可学习标量。

</details>

---

### 6. [Structured Recurrent Mixers for Massively Parallelized Sequence Generation](https://arxiv.org/abs/2605.08696)

**Authors**: Benjamin L. Badger  
**Category**: cs.CL  
**Published**: 2026-05-12  
**Score**: 11.0  
**Type**: new  
**ArXiv ID**: 2605.08696v1  

#### Abstract
Over the last two decades, language modeling has experienced a shift from predominantly recurrent architectures that process tokens sequentially during training and inference to non-recurrent models that process sequence elements in parallel during training, which results in greater training efficie...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Structured Recurrent Mixers for Massively Parallelized Sequence Generation

---

## 1. 论文的主要贡献和创新点

### **解决了什么问题**

传统语言模型在训练和推理之间存在效率不匹配的问题：

- **Sequence Parallel 模型**（如 Transformer）：训练高效且稳定，但推理时因需逐 token 生成而吞吐量低。
- **Recurrent 模型**（如 RNN、LSTM）：推理高效，但难以并行化训练，导致训练效率低下。

此外，当前主流的线性复杂度架构（如 Mamba、RWKV）虽然实现了序列并行与循环表示之间的转换，但依赖于**专用 CUDA 内核**或复杂的内存管理机制，限制了其跨设备兼容性和部署灵活性。

本论文旨在解决以下核心矛盾：
> 如何设计一种既能实现高效并行训练，又能在推理阶段获得高吞吐、高并发的通用架构，且无需定制化硬件优化？

---

### **提出了什么新方法或新思路**

作者提出 **Structured Recurrent Mixer (SRM)** 架构，具备以下关键创新：

#### ✅ 双重表示能力（Dual Representation）
- **训练时**：以 sequence-parallel 形式进行并行处理（类似 Transformer），提升训练效率。
- **推理时**：自动切换为 recurrent 表示，实现常数空间 $O(1)$ 和固定操作数的 token 生成。
- **无需修改参数或缓存结构**即可代数等价地转换两种模式。

#### ✅ 结构化混合器设计（Structured Token Mixing）
基于 **Masked Mixer** 架构（用 masked MLP 替代 attention），通过对 token mixing 矩阵施加结构约束（如行重复、列重复 + 衰减因子 $\lambda$），使其天然支持循环计算。

#### ✅ 批次维度扩展优于序列长度扩展
提出理论观点：
> 对于信息密集输入（如语言），**Recurrent 模型更适合在 batch 维度而非 sequence length 上扩展**，因其每样本具有恒定大小的连续内存（cache）。

这使得 SRM 在大规模采样任务中表现出色。

#### ✅ 生产级推理引擎实现
实现了基于 **Mojo/MAX** 的高性能推理框架，显著超越 PyTorch 实现，并与 vLLM 等主流系统对比验证优势。

---

### **相比现有方法的优势**

| 特性 | SRM | Mamba / RWKV | Transformer |
|------|-----|----------------|-------------|
| 训练效率 | 高（接近 quadratic 模型） | 中等偏低 | 高 |
| 推理吞吐 | 极高（>10x Transformer） | 较高 | 低 |
| 并发能力 | 极强（>100x） | 中等 | 弱 |
| 是否需要定制 Kernel | ❌ 否 | ✅ 是 | ❌ 否 |
| 多设备兼容性 | 强（V100/H100 均表现一致） | 弱（V100 上性能暴跌） | 强 |
| 支持快速采样验证范式 | ✅ 最佳适配 | 一般 | 差 |

---

## 2. 核心实验方法和设置

### **使用的数据集**

- **预训练数据集**：
  - `FineWeb-edu`：用于通用语言建模训练。
  - `FineMath 4+`：数学与代码领域文本，用于数学推理任务微调。
- **下游评测基准**：
  - 功能理解：ARC-Easy, HellaSwag, Lambada
  - 问答与推理：GSM8k（数学应用题）
  - 信息保留能力：SQuAD, SQuAD2, LongBench, IFEval, SWDE, xWinoGrad
  - 压缩与复制能力：Copy Task（512 token 复制）、Encoder-Decoder 输入重建

---

### **实验设置和评估指标**

#### 🧪 主要评估维度：

| 类别 | 指标 |
|------|------|
| **训练效率** | loss per FLOP, samples/sec, GPU memory usage |
| **推理性能** | throughput (tokens/sec), max concurrency (batch size) |
| **模型能力** | Pass@k (GSM8k), accuracy (ARC, HellaSwag), BLEU/BPB (WikiText) |
| **信息容量** | Entropy Ratio（信息保留率）、Copy Accuracy |

#### 💻 硬件平台：
- V100 (16GB), H100 (96GB NVLink)
- 使用 PyTorch 和自研 Mojo/MAX 推理框架

#### 🔁 基线模型对比：
- **Transformer**（Llama 2 架构）
- **Mamba** / **Mamba 2**
- **RWKV**
- **Masked Mixer**（非循环变体）

所有模型控制 compute-equivalent 或 parameter-equivalent 设置。

---

## 3. 主要实验结果和性能指标

### **关键性能数据**

#### ⚙️ 推理吞吐与并发能力（Table 5 & 6 & 7）

| Context Length | Model | Throughput (t/s) | Max Concurrency | Speedup vs Transformer |
|---------------|--------|--------------------|------------------|-------------------------|
| 512 | Transformer | 2908 | 400 | 1x |
|     | SRM         | **28091** | **64000** | **9.66x** |
| 4096 | Transformer | 634 | 50 | 1x |
|     | SRM         | **27445** | **32000** | **43.29x** |

> 在长上下文下，SRM 的吞吐优势随 context length 增加而扩大。

| Model (H100, ctx=512) | Throughput (t/s) | Concurrency |
|------------------------|-------------------|--------------|
| SRM (d_model=1024)     | **161,312**       | **512,000**  |
| Mamba (d_model=256)    | 61,465            | 1,000        |
| RWKV (d_model=512)     | 3,774             | 1,024        |
| Transformer (d_model=512) | 15,272          | 4,000        |

> SRM 实现 **>500x 更高的并发能力** 和 **~7x 吞吐提升** 相比 Mamba。

#### 🚀 优化推理引擎效果（Table 7）

| Model | Throughput (k t/s) | Concurrency (k samples) |
|-------|---------------------|--------------------------|
| SRM (Mojo/MAX) | **1203** | **800** |
| Transformer (vLLM) | 101 | 5.32 |
| → 提升倍数 | **12x** | **170x** |

> SRM + MAX 实现 **26x 吞吐提升**（pretraining-matched）、**30% 更高的 GSM8k Pass@k 效率**（compute-constant）。

---

### **与基线方法的对比结果**

#### 📊 功能性基准测试（Table 1）

| Benchmark | SRM | Mamba | Transformer |
|----------|-----|--------|------------|
| GSM8k Pass@k | 1.44±0.33 | 1.36±0.32 | 1.90±1.36 |
| ARC-Easy (%) | **50.0** | 33.96 | 48.11 |
| IFEval (strict) | 21.22 | **25.66** | 12.2 |
| WikiText BPB ↓ | **1.2363** | 1.6212 | 1.5192 |

> 尽管 Transformer 在多数单次采样任务上略优，但 **SRM 在信息压缩效率和推理效率方面全面领先**。

#### 🔍 信息保留与容量测试（Table 2–4）

| 指标 | SRM | Mamba |
|------|-----|--------|
| 信息保留熵比（Entropy Ratio） | **0.3168** | 0.2204 |
| 编码解码重建熵比 | **0.7773–0.8565** | 0.6282 |
| Copy Accuracy (512 tokens, 10k steps) | **0.8439 (d=512,k=8)** | 0.9673 (but higher d needed) |

> SRM 展现出更强的信息存储能力和更高效的复制学习速度（尤其在相同 compute 下）。

---

### **消融实验结果（Table S2–S8）**

| 变体 | 影响 |
|------|------|
| **Mixed Heads**（半行重复 + 半列重复） | ✅ 显著优于单一结构，最佳配置 |
| **Decay Term ($\lambda$)** | ✅ 加入衰减可大幅提升训练效率 |
| **Head Projections** | ✅ 微幅提升训练效率，但带来 ~10% 开销 |
| **Diagonal Constant** | ❌ 无明显收益，说明主对角线独立建模非必要 |
| **Kernel Size (k=4/8)** | ✅ 更大 kernel 提升 copy 准确率 |

> 最优架构：**mixed heads + decay + head projections + moderate kernel size**

---

## 4. 关键结论和发现

### **主要发现**

1. ✅ **SRM 成功桥接了 sequence-parallel 与 recurrent 架构的优点**：
   - 训练时并行高效，推理时低延迟、高吞吐。
   - 无需特殊 kernel，可在多种设备上无缝运行。

2. ✅ **Recurrent 模型更适合 batch 维度扩展而非 sequence length 扩展**：
   - 因其 cache 容量有限，过长序列会导致信息压缩失真（copy accuracy 下降 >90% → <30%）。
   - 但在高并发采样场景（如可验证输出）中极具优势。

3. ✅ **SRM 在 verifiable output scaling 场景下显著胜出**：
   - 对 GSM8k 使用 oracle 验证后，**固定 compute 下 SRM 比 Transformer 多解决约 30% 的问题**。
   - Pass@k 曲线几乎重合，意味着可通过更多采样轻松超越更大模型。

4. ✅ **SRM 是强化学习的理想候选者**：
   - 支持大 batch rollout（如 GRPO 中使用 50 样本 vs Transformer 的 5 样本）。
   - 提出 **balanced resampling** 方法缓解探索退化问题，在 GRPO 中显著提升最终 Pass@k。

5. ✅ **Mojo/MAX 推理框架极大释放潜力**：
   - 相比 PyTorch 实现提速 7.5x，相比 vLLM 的 Transformer 提速 12x。
   - 展示了“软件+架构”协同优化的巨大空间。

---

### **方法的局限性**

1. ❗ **训练阶段仍为 $O(n^2)$ 时间复杂度**：
   - 不适合极长序列（如 $n \gg d$）的训练场景。
   - 虽然实际受限于 memory bandwidth，但本质仍是 quadratic。

2. ❗ **缺乏内置 context length 扩展机制**：
   - 当前未测试 ALiBi、RoPE 等位置编码扩展方案。

3. ❗ **参数效率较低**：
   - 更适合大参数量模型，不适合极小模型部署。

4. ❗ **尚未探索全部优化路径**：
   - 如 parallel scan 加速 prefill 阶段、量化支持等未深入研究。

---

### **未来工作方向**

1. 🔮 探索 **context length extrapolation 技术** 应用于 SRM。
2. 🧠 研究 **更精细的 cache 压缩与检索机制**，提升信息保留上限。
3. ⚙️ 开发 **纯静态 MAX 图编译版本**，进一步降低驱动开销。
4. 🤖 深入结合 **Reinforcement Learning** 与 massive sampling pipeline，构建端到端 agent 推理系统。
5. 🌐 推广至 **多模态序列建模**（如音频、DNA、时间序列）等信息密集领域。

---

> **总结一句话**：  
> SRM 提供了一种**无需定制内核即可实现极致推理并发与吞吐的语言模型架构**，特别适用于“**大量采样 + 快速验证**”的新一代 AI 应用范式，在数学推理、agent workflow、RLHF 等场景中展现出巨大潜力。

</details>

---

### 7. [Arcane: An Assertion Reduction Framework through Semantic Clustering and MCTS-Guided Rule Exploring](https://arxiv.org/abs/2605.10107)

**Authors**: Hongqin Lyu, Yonghao Wang, Zhiteng Chao, Tiancheng Wang, Huawei Li  
**Category**: cs.AI  
**Published**: 2026-05-12  
**Score**: 10.5  
**Type**: new  
**ArXiv ID**: 2605.10107v1  

#### Abstract
Assertion-based Verification (ABV) is essential for ensuring that hardware designs conform to their intended specifications. However, existing automated assertion-generation approaches, such as LLM-based frameworks, often generate large numbers of redundant assertions, which significantly degrade si...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文《Arcane: An Assertion Reduction Framework through Semantic Clustering and MCTS-Guided Rule Exploring》核心总结

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
- **冗余断言导致验证效率低下**：当前无论是基于模板、trace挖掘还是LLM生成的SystemVerilog Assertions (SVA) 都存在大量语义冗余（如GoldMine中约96%，LLM方法中20%-30%），这些冗余断言显著增加仿真时间（simulation overhead）和计算资源消耗。
- **缺乏在保持错误检测能力前提下的自动化断言约简框架**：已有工作多关注运行时检查优化或checker选择，但未系统解决**如何安全地消除冗余断言而不影响形式覆盖（formal coverage）和缺陷检出能力**。

### 🚀 提出的新方法与创新思路
本文提出 **Arcane** —— 一种高效的断言约简（Assertion Reduction）框架，其核心创新包括：

#### （1）**两阶段精细化聚类机制（Coarse-to-Fine Clustering）**
- **第一层：BERT-guided 语义粗分类**
  - 将SVA转换为自然语言描述，利用预训练BERT模型提取语义向量，通过cosine相似度进行初步分组。
  - 目标：缩小搜索空间，提升后续处理效率。
- **第二层：Lasso-based 行为细粒度分类**
  - 构建每个断言对应的 **Büchi Automaton**，采样lasso路径（有限前缀+循环），基于接受行为的Jaccard相似性进一步精炼聚类。
  - 解决纯文本相似性误判问题（例如 `assert(A→B)` 与 `assert(A→¬B)` 文本相近但逻辑相反）。

> 💡 创新点：首次将**形式化自动机的行为一致性分析**引入断言聚类，确保功能意图一致的断言被归入同一簇。

#### （2）**MCTS引导的规则探索机制（MCTS-Guided Rule Exploring）**
- 将断言约简建模为一个**确定性MDP**（Markov Decision Process）：
  - **State**：当前断言集合的状态
  - **Action**：应用五类语义保持的约简规则之一
  - **Transition**：执行规则后更新断言集
  - **Reward**：减少的断言数量 + 减少的原子谓词（Atomic Predicate）数
- 使用 **Monte Carlo Tree Search (MCTS)** 在庞大的规则组合空间中高效探索最优约简路径，避免穷举。

> 💡 创新点：将MCTS用于断言约简策略搜索，实现对复杂交互关系的有效剪枝，在保证等价性的前提下最大化压缩率。

#### （3）**严格语义保持的约简规则设计**
定义了5类可证明语义等价或蕴含关系的安全变换规则：
1. 单断言前后件简化（Single-assertion pre/post reduction）
2. 共同前件合并（Common-antecedent POST Conjunction）
3. 共同后件合并（Common-consequent PRE Disjunction）
4. 断言等价判定（Pairwise Equivalence）
5. 断言蕴含判定（Implication Determination）

所有规则均基于CNF蕴含检测或SPOT模型检验器验证，确保**逻辑等价性不变**。

---

### 🔍 相比现有方法的优势
| 维度 | 现有方法 | Arcane |
|------|--------|--------|
| 冗余识别方式 | 基于语法/模板匹配 / 静态分析 | 融合**语义嵌入 + 自动机行为分析**，更准确捕捉功能一致性 |
| 约简策略 | 启发式规则串行应用 | MCTS智能探索**最优规则序列**，避免局部最优 |
| 语义保障 | 多数无严格证明 | 所有变换均可证**语义等价或覆盖保留** |
| 可扩展性 | 对大规模断言集效果差 | 支持并行化聚类与MCTS搜索，适用于大型设计 |

---

## 2. 核心实验方法和设置

### 📊 数据集
- 使用公开基准 **AssertionBench [20]**，包含：
  - **112个硬件设计模块**
  - 每个模块含RTL代码、波形轨迹及对应断言
  - 断言来源两类：
    - **HARM**：基于hint的挖掘工具生成
    - **LLM-based generator**：大语言模型生成（更具现实代表性）

### ⚙️ 实验设置
- **平台环境**：
  - CPU: Intel Xeon Gold 6148 @ 2.40GHz
  - RAM: 629 GB
  - 工具链：
    - Formal Verification: **Cadence JasperGold v21.12.002**
    - Simulation: **Synopsys VCS v2016.06**

- **Arcane参数配置**：
  - Lasso样本数：500
  - BERT与Lasso相似性加权系数：α=0.4, β=0.6
  - 分类阈值：统一设为0.85
  - 并行线程数：64

### 📈 评估指标（Evaluation Metrics）
| 指标 | 缩写 | 描述 |
|------|-----|------|
| 断言数量 | N | 约简前后断言总数 |
| Proof Core | PC | 形式验证中最小子证明逻辑，衡量**形式覆盖完整性** |
| 错误检测率 | ER (Mutation Testing) | 通过突变测试评估缺陷捕获能力，直接反映**验证质量** |
| 处理时间 | PT | 断言约简本身的开销（一次性成本） |
| 仿真运行时间 | RT | VCS仿真的实际耗时（重复使用，主导总开销） |
| 聚类质量 | DBI (Davies-Bouldin Index) | 数值越低表示聚类内聚性越好 |

### 🔁 基线方法对比
- 本文未直接比较其他端到端断言约简工具（因此前无专门研究），而是通过以下方式进行对比：
  1. **消融实验**：比较不同聚类策略（仅BERT vs BERT+Lasso）
  2. **性能增益对比**：展示约简前后RT变化，体现相对于“不约简”的加速比
  3. **有效性验证**：证明PC与ER完全不变，说明优于任何可能损失覆盖率的方法

---

## 3. 主要实验结果和性能指标

### 📉 关键性能数据

#### （1）**断言约简比例高且稳定**
- 对 **HARM生成断言**：平均约简 **78%**
- 对 **LLM生成断言**：平均约简 **71%**
- 最高达 **76.2%**（ca_prng设计）

> 图5显示绝大多数设计集中在70%-80%区间，表明方法具有强普适性和收敛性。

#### （2）**仿真速度显著提升**
| 设计 | 仿真加速比（Speedup） |
|------|------------------|
| ca_prng | **6.1x** |
| control_unit | 3.46x |
| eth_cop | 3.42x |
| eth_receivecontrol | 2.83x |
| MAC_rx_ctrl | 2.67x |
| MAC_tx_ctrl | 3.68x |

> ➤ 平均仿真加速超过 **2.6x**，最高达 **6.1x**，极大降低验证周期。

#### （3）**验证质量完全保留**
- 所有设计中：
  - **Proof Core (PC)**：约简前后完全一致
  - **Error Rate (ER)**：突变检测率100%保留
- 表明Arcane实现了真正的**语义等价压缩**，未牺牲任何验证能力。

#### （4）**聚类质量与效率双重提升（消融实验）**

| 设计 | 运行时（L → B+L） | 加速倍数 | DBI变化（<0.023） |
|------|------------------|---------|------------------|
| ca_prng | 144.45s → 31.93s | **4.52x** | +0.0158 |
| control_unit | 1070.55s → 161.83s | **6.61x** | +0.0114 |
| MAC_tx_ctrl | 43321s → 1274.51s | **33.99x** | +0.0207 |

> ✅ 结论：BERT预分类大幅缩短Lasso分析时间（最高**34倍加速**），而聚类质量仅轻微下降（DBI增幅<0.023），性价比极高。

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **断言冗余普遍存在且可高效消除**：
   - 不论是传统方法还是LLM生成的SVA，均存在严重冗余（>70%），而这些冗余可通过语义感知的方式安全移除。

2. **融合语义与行为的聚类显著优于单一模态**：
   - 仅用BERT会导致语义混淆；加入Büchi automaton的lasso接受行为分析后，聚类边界更清晰、内部更紧凑（见图6 MDS可视化）。

3. **MCTS能有效导航复杂的规则组合空间**：
   - 规则顺序影响最终压缩效果，MCTS可在非穷举情况下找到近似最优路径，显著优于固定顺序应用规则。

4. **压缩不影响验证能力**：
   - 所有案例中PC与ER完全不变，证明Arcane不仅减量，而且保质。

---

### ⚠️ 局限性
1. **依赖LTL可表达性**：
   - 当前方法要求断言可转化为LTL公式以便构建Büchi automaton，对于高度非规范化的SVA可能存在限制。
2. **MCTS搜索仍有一定开销**：
   - 尽管已优化，但在超大规模断言集上MCTS仍需数百秒至数千秒处理时间（如MAC_tx_ctrl耗时1388s）。
3. **未支持增量约简**：
   - 当设计迭代新增断言时，需重新运行整个流程，缺乏动态更新机制。

---

### 🔮 未来工作方向
1. **支持增量式断言约简（Incremental Reduction）**
   - 对新增断言快速定位所属簇，并局部重运行MCTS，避免全局重算。
2. **扩展至更多SVA语法结构**
   - 当前主要处理`implication`型断言，未来可纳入`sequence`、`property`等高级构造。
3. **与LLM断言生成 pipeline 深度集成**
   - 在生成阶段即引入去重机制，形成“生成-约简”一体化流程。
4. **硬件原生支持断言压缩**
   - 探索在FPGA原型验证或Emulation平台上部署轻量化Arcane引擎，实现实时优化。

---

## 总结
Arcane 是首个面向**语义保持型断言约简**的系统性框架，通过**BERT + Büchi automaton 的双模态聚类** 和 **MCTS驱动的规则搜索机制**，实现了高达 **76.2%** 的断言压缩率和 **6.1x** 的仿真加速，同时完整保留了形式覆盖与缺陷检测能力。该工作为高效率ABV（Assertion-Based Verification）提供了关键技术支撑，尤其适用于LLM生成断言后的清洗与优化场景。

</details>

---

### 8. [Merlin: Deterministic Byte-Exact Deduplication for Lossless Context Optimization in Large Language Model Inference](https://arxiv.org/abs/2605.09990)

**Authors**: Sietse Schelpe  
**Category**: cs.CL  
**Published**: 2026-05-12  
**Score**: 10.5  
**Type**: new  
**ArXiv ID**: 2605.09990v1  

#### Abstract
Data-intensive applications, ranging from large-scale retrieval systems to advanced data pipelines, are increasingly bottlenecked by the processing of highly redundant text corpora. We present Merlin, a local-first, agnostic, high-throughput deduplication and context optimization engine designed to ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Merlin: Deterministic Byte-Exact Deduplication for Lossless Context Optimization in Large Language Model Inference*

---

## 1. 论文的主要贡献和创新点

### 解决的问题
在大型语言模型（LLM）推理过程中，**输入上下文（prompt context）通常存在大量冗余**，主要来源于：
- 检索系统返回的重叠文本块（retrieved chunks）
- 多轮对话中累积的重复历史记录（session histories）
- 多个用户并发查询共享知识库时获取的相同内容

这些冗余虽然对人类可见，但由于是语法上不同的字符串，**模型层无法识别其语义重复**，导致不必要的计算开销（prefill compute），增加延迟和成本。

### 提出的新方法
提出 **Merlin 引擎** —— 一种用于 LLM 推理前处理阶段的 **确定性、字节精确（deterministic byte-exact）去重原语（deduplication primitive）**。

该方法的核心思想是在检索器（retriever）与提示组装器（prompt assembler）之间插入一个轻量级预处理步骤，移除候选上下文中完全相同的记录（record-level duplicates），仅保留首次出现的内容。

#### 关键特性：
- **Deterministic**：相同输入在不同运行、机器、操作系统下产生比特位一致（bit-for-bit identical）输出。
- **Byte-Exact**：仅当两个记录在字节级别完全相同时才视为重复；单字节差异即视为不同。
- **Fast & Lightweight**：单次调用延迟低至微秒级，二进制体积小于 4MB，无第三方依赖。
- **Lossless Safety Claim**：实验证明该操作不会引入可检测的质量退化。

### 相比现有方法的优势

| 方法类别 | 典型代表 | 是否适用推理路径 | 是否 lossless | 是否 deterministic |
|--------|--------|------------------|---------------|--------------------|
| **Approximate Dedup** | MinHash-LSH, Bloom Filters | ❌ 不适合 | ❌ 近似匹配 | ❌ 非确定性 |
| **Semantic Compression** | LLMLingua, Prompt Compression | ⚠️ 可能损失信息 | ❌ Lossy | ❌ 非确定性 |
| **Model-side Optimization** | REFRAG, RAGBoost | ✅ 加速但需改模型 | ✅（部分） | ⚠️ 依赖特定架构 |
| **Vendor Prompt Caching** | Anthropic/Gemini 缓存机制 | ✅ 有效但不通用 | ✅ | ❌ Cache key opaque |
| **Merlin (本文)** | `merlin` engine | ✅ 可部署于任意推理代理前端 | ✅ **Lossless（经验证）** | ✅ **Fully Deterministic** |

> ✅ Merlin 的优势在于：**零质量损失、超低延迟、跨平台一致性、无需修改模型或缓存系统，且可与其他优化技术互补叠加。**

---

## 2. 核心实验方法和设置

### 使用的数据集

实验覆盖三大类基准任务，涵盖学术与真实场景：

| 数据集 | 类型 | 描述 |
|-------|------|------|
| **RULER** | Synthetic long-context retrieval | 包含多针检索（multi-needle）、变量追踪（variable tracing）、多跳问答等子任务，在 8K~16K 上下文长度下测试。使用 NVIDIA 官方 UUID 构造的唯一文本块，天然冗余极低（<0.01%），作为“最严苛 pass-through 测试”。 |
| **LongBench** | Real-world long-document tasks | 包括 narrativeqa, qasper, gov_report 等 paragraph-safe 子集，用于评估真实长文档理解能力。排除代码补全任务（lcc, repobench-p）和有监督重复任务（trec）。 |
| **HumanEval-Snowball** | Multi-turn coding with real dialogue history | 在 HumanEval 编程题前附加来自 `WildChat-1M` 的真实多轮对话历史，模拟上下文“雪球效应”积累。 |
| **BeIR Corpus** | Large-scale public retrieval corpus | 跨多个源（NQ, HotpotQA, FEVER, MSMARCO, SciFact, TriviaQA）共 **22.2M passages**，用于大规模数学等价性验证。 |

此外还进行了跨域测试（log analysis, web crawl, scientific data）以验证通用性。

### 实验设置和评估指标

#### 推理平台
通过 **OpenRouter** 接入四大主流 LLM API：
- Google Gemini 2.5 Flash
- OpenAI GPT-5.1
- Anthropic Claude Sonnet 4.6
- Meta Llama 3.3 70B Instruct

所有请求均设为 `temperature=0.0`，输出预算为 2048 tokens。

#### 评估协议
- **Primary Sweep**：40 个评估单元（cells），每 cell 50~100 次调用。
- **Pipeline Confirmation Pass**：额外 200-cell 验证，使用生产二进制作为子进程调用，确保结果反映真实部署环境。
- **Total API Calls**：约 16,800 次，总花费约 86 USD。

#### 评估指标
| 指标 | 应用场景 |
|-----|---------|
| **Pass@1**, **Accuracy** | RULER, HumanEval |
| **F1**, **ROUGE-L** | LongBench |
| **Wilson 95% CI** | 比例型得分置信区间 |
| **Paired Sign Test**（主） | 判断质量变化是否显著（保守选择） |
| **Paired t-test**（辅） | 参数检验补充 |
| **Bonferroni Correction** | 多重假设检验校正（α=0.05） |

---

## 3. 主要实验结果和性能指标

### 关键性能数据

| 性能维度 | 数值 |
|--------|------|
| **In-process latency (median)** | **1.10 μs** |
| **Production binary internal counter (typical)** | **5–30 μs/call** |
| **Subprocess + pipe IPC** | ~13 ms |
| **Subprocess + tempfile** | ~21 ms |
| **Binary size (Windows x86-64)** | **3.8 MB**（静态链接） |
| **Binary size (Linux ARM64)** | **3.5 MB** |
| **Memory footprint** | CPU-bound, no GPU or external DB |

> ⚡️ 去重操作本身耗时比典型推理代理预处理预算（10–50 ms）低 **3–4 个数量级**，属于“零成本”操作。

### 与基线方法的对比结果

#### 质量影响（Aggregate Quality Delta）
| 实验组 | 平均质量差（Δ） | 显著退化 cell 数（Bonferroni 校正后） |
|-------|------------------|-------------------------------|
| Primary Sweep (40 cells) | **+0.0 pp** | **0** |
| Confirmation Pass (200 cells) | **-0.5 pp**（仅 1 个净负 cell） | **0** |

- 所有任务中，去重后的输出与原始输入在统计意义上 **indistinguishable**。
- 最大观测到的单 cell 差异为 -4.0 pp（Llama on RULER），但 sign-test p=0.500，远高于校正阈值 α/40=0.00125。
- 所有差异均在各模型自身的 **test-retest noise floor** 内部。

#### 输出一致性验证
| 对比项 | 结果 |
|------|------|
| Binary vs Reference Wrapper (640 prompts) | **99.2% byte-identical**（635/640） |
| Non-code prompts only | **100% identical**（590/590） |
| 差异原因 | 仅出现在 `repobench-p` 任务，源于行分割器对 `\r\n` 和 `\n` 处理方式不同（已确认为 deterministic 行为） |

#### 大规模数学等价性验证（Math-Equivalence Audit）
- 在 **22.2M BeIR passages** 上运行 Merlin 与 Python `set()` 进行比较：
  - **unique_count 完全一致**
  - **327 个 BM25 查询中，merlin_unique_count == python_set_unique_count 达成 327/327**
  - **violations: 0**
- 证明 Merlin 在生产规模上实现了与理论最优（Python set）的数学等价。

### 消融实验结果（Ablation Study）

#### Line-level vs Paragraph-level Dedup on Code Tasks
| Vendor | lcc Δ (F1×100) | repobench-p Δ (F1×100) | 影响解读 |
|-------|----------------|------------------------|----------|
| **Gemini** | -19.5 | -8.9 | ❌ **有害**（可能破坏结构分隔符） |
| **Claude** | +2.3 | -0.5 | ➖ 中性 |
| **GPT-5.1** | +2.8 | +11.4 | ✅ 改善（减少模板噪声） |
| **Llama** | +3.8 | +0.1 | ➖ 中性 |

> 📌 **结论**：line-level dedup 效果具有 vendor-specific 特性，因此默认采用 **paragraph-level dedup** 并将代码任务从主声明中排除。

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **Byte-exact deduplication 是安全的**：在标准 LLM 评估协议下，去重前后模型输出无统计显著差异（zero statistically significant degradation）。
2. ✅ **性能足够快**：in-process 延迟仅 **~1μs**，远低于推理代理预处理预算，可视为“零成本”操作。
3. ✅ **工程可行性强**：单二进制、静态链接、跨平台（x86-64 / ARM64）、无依赖，易于集成进现有服务栈。
4. ✅ **可扩展性好**：在 AWS r7i.48xlarge 上处理 460GB FineWeb 数据仅需 5–7 分钟，吞吐达 160 GB/s。
5. ✅ **通用性强**：已在 log analysis、web crawl、scientific data 等非 LLM 场景验证有效性。

### 方法的局限性
1. ❌ **不处理语义级冗余**：仅去除字节完全相同的重复项，无法识别 paraphrase 或同义表达。
2. ❌ **未覆盖所有领域**：未测试法律、医疗、多模态等高专业性检索场景。
3. ❌ **闭源实现**：Merlin 引擎为 closed-source 生产基础设施，完整复现需签署 NDA 参与 clean-room evaluation。
4. ⚠️ **代码任务需谨慎配置**：line-level dedup 在不同 vendor 上表现差异大，需单独验证。

### 未来工作方向
1. 🔜 将 Merlin 应用于更多垂直领域（如 legal RAG、biomedical QA）进行专项验证。
2. 🔜 探索与 semantic dedup 或 prompt compression 方法的联合优化策略（hybrid pipeline）。
3. 🔜 开发开源参考实现（open-source reference）以促进社区研究。
4. 🔜 研究如何在保留结构信息的前提下安全地进行更细粒度（如 line-level）去重。
5. 🔜 将 Merlin 部署模式标准化为 LLM serving infrastructure 的通用组件。

---

> 💡 **最终结论**：  
> Merlin 展示了一种 **简单但强大** 的推理优化范式 —— 在不影响模型质量的前提下，通过 **deterministic byte-exact deduplication** 消除结构性冗余，实现 **近乎免费的上下文压缩**。它不是替代其他优化手段，而是作为最底层、最先执行的安全预处理步骤，为后续所有优化（KV-cache reuse, prompt caching, context indexing）提供更干净的输入基础。这一工作推动了 LLM 推理系统向更高效率、更低延迟、更低成本的方向演进。

</details>

---

### 9. [VISTA: A Generative Egocentric Video Framework for Daily Assistance](https://arxiv.org/abs/2605.10579)

**Authors**: Yu-Hsiang Liu, Yu-Chien Tang, An-Zi Yen  
**Category**: cs.CL  
**Published**: 2026-05-12  
**Score**: 10.5  
**Type**: new  
**ArXiv ID**: 2605.10579v1  

#### Abstract
Training AI agents to proactively assist humans in daily activities, from routine household tasks to urgent safety situations, requires large-scale visual data. However, capturing such scenarios in the real world is often difficult, costly, or unsafe, and physics-based simulators lack the visual fid...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文《VISTA: A Generative Egocentric Video Framework for Daily Assistance》核心总结

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
当前在训练和评估 **Embodied AI Agents**（具身智能体）时面临以下挑战：
- **真实世界数据采集困难**：获取自然的 **egocentric（第一人称）视频数据** 成本高、难以规模化，尤其对于罕见或高风险场景（如火灾、触电、跌倒等）几乎无法安全收集。
- **物理模拟器存在 sim-to-real gap**：现有的 **physics-based simulators**（如 AI2-THOR、Habitat）视觉保真度低，环境动态简化，难以反映现实世界的复杂性和不可预测性。
- **缺乏对“主动协助”行为的系统建模**：大多数基准仅关注 **reactive（响应式）** 行为（用户明确请求帮助），而忽略了更高级的 **proactive（主动干预）** 场景。

### 提出了什么新方法或新思路
提出 **VISTA**（Video Synthesis for Training Agents），一个端到端的 **generative egocentric video synthesis framework**，用于生成高质量的第一人称视频作为 AI Agent 的训练与评估数据。

其核心创新包括：
- **五步脚本生成流水线（5-step script generation pipeline）**：
  1. **Intervention Generation**：由 LLM 生成潜在需要干预的安全或社交场景。
  2. **User Action Derivation（因果逆向推理）**：从“需要干预”反推导致该情况的用户行为，确保逻辑合理性。
  3. **Signal Specification**：定义触发 Agent 注意的可观测信号（如视觉/听觉线索）。
  4. **Mode Binding**：将场景绑定到三种 **assistance modes** 中的一种。
  5. **Script Generation**：输出结构化的 YAML 脚本，指导视频生成。

- **系统化的 assistance mode 分类体系**：
  - **Reactive Mode**：用户直接请求帮助（如“帮我找钥匙”）。
  - **Proactive Mode**：
    - **Explicit Proactive**：用户意识到需要帮助但未直接请求（如自言自语“我放哪儿了？”）。
    - **Implicit Proactive**：用户尚未意识到危险，Agent 主动干预（如发现饮料靠近电源插座即将被打翻）。

- **可检验的交互界面（Inspectable Interface）**：提供 Web UI，使每一步生成过程透明化，支持调试与复现。

### 相比现有方法的优势
| 方法 | Egocentric | Causal Control | Proactive Modes | 来源 |
|------|------------|----------------|------------------|-------|
| Ego-Exo4D | ✅ Real | ❌ | ❌ | Real |
| ProAssist | ✅ Real | ✅ | ✅ | Real |
| **VISTA (Ours)** | ✅ Gen | ✅ | ✅ | **Gen** |

- **生成式而非采集式**：突破现实采集限制，可合成罕见、长尾、高风险事件。
- **强因果控制**：通过 **causal reverse reasoning** 确保每个样本都有合理的前因后果，避免生成无意义或幻觉内容。
- **全面覆盖多种协助模式**：首次系统性地建模并生成 **implicit proactive** 场景，推动 AI 向更高阶的情境理解发展。
- **可控且可扩展**：模块化设计 + 结构化脚本，实现精细控制与大规模生成。

---

## 2. 核心实验方法和设置

### 使用的数据集
- **不依赖真实数据集进行训练**，而是完全基于 **生成**。
- 构建了一个包含 **60 个合成视频** 的 benchmark，涵盖 **20 种风险场景 × 3 种 assistance mode**（Reactive / Explicit Proactive / Implicit Proactive）。
- 所有视频均通过 **VISTA pipeline 自动生成**，并通过质量门控（quality gate）筛选。

### 实验设置和评估指标
采用三层评估架构：

#### 📌 **SAM3 Layer**（空间物理信号提取）
使用 **SAM3** 提取以下物理信号以量化风险演化：
- **Hand-Hazard Distance**：手与危险物的距离。
- **Escalation Curve**：风险升级趋势（结合危害活动与接近程度）。
- **Hazard Area Growth**：危险区域的时间扩张速率。

#### 📌 **VLM Layer**（多模态模型分析）
使用 **Vision-Language Model (VLM)** 对视频进行分析，输出：
- `identified_hazard`（识别出的危害）
- `proposed_intervention`（建议干预措施）
- `intervention_urgency`（紧迫性评分 1–5）
- `events`（时间戳事件序列）

再通过 **LLM-as-a-Judge** 进行联合打分：
- **Helpfulness**：干预是否有效、安全正确、可执行。
- **Tone**：语气是否恰当（紧急时应简洁果断）。
- **Over-alert Flag**：是否存在误报（无必要警告）。

#### 📌 **Fusion Layer**（融合评分）
综合多个维度计算最终 **Utility Score**：
- **Reaction Latency**：响应时间相对于预期风险爆发点的延迟。
- **Timeliness Score**：基于 mode-aware 容忍窗口计算。
- **Safety Criticality**：由 SAM3 和 VLM 输出的风险严重性加权平均。
- **Final Utility**：
  $$
  S = 0.4S_{\text{help}} + 0.08S_{\text{tone}} + 0.25S_{\text{lat}} + 0.20S_{\text{sc}} + 0.07S_{\text{obs}} - P_{\text{over-alert}}
  $$
  其中若 `over_alert_flag=True`，则扣除 $P=0.25$。

> ⚠️ **Quality Gate**：仅保留 video-text alignment ≥ 0.5 的样本进入最终统计。

### 基线方法对比
- **Zero-shot Baseline**：直接用 prompt 驱动生成模型，无结构化控制。
- **Our Method**：完整 VISTA pipeline（含五步脚本控制）。
- 对比维度：总有效样本数、Helpfulness、Tone、Latency Error、Safety Criticality。

---

## 3. 主要实验结果和性能指标

### 关键性能数据（来自 Table 2 & 3）

| Mode | Total | Valid (Gate ≥0.5) | Helpfulness ↑ | Tone ↑ | LatencyErr ↓ | SafetyCrit ↑ |
|------|-------|--------------------|---------------|--------|--------------|---------------|
| **Reactive** | 20 | 13 | 55.39 | 0.793 | 0.914 | 0.933 |
| **Explicit Proactive** | 20 | 15 | 60.84 | 0.832 | 0.950 | 0.800 |
| **Implicit Proactive** | 20 | 15 | 63.64 | 0.840 | 0.910 | 0.781 |
| **All Modes (Ours)** | 60 | 43 | **59.42** | **0.818** | **0.924** | **0.849** |

> 注：数值越高越好（↑），LatencyErr 越低越好（↓）

### 与基线方法对比结果
| Setting | Valid Samples | Overall Utility | LatencyErr |
|--------|----------------|------------------|-------------|
| **Zero-shot** | 17 | 49.67 | 0.980 |
| **VISTA (Ours)** | **43** | **59.42** (+9.75) | **0.924** (-0.056) |

✅ **显著优势**：
- 更多高质量样本通过 gate（17 → 43）
- 整体 utility 提升近 10 分
- 响应及时性明显改善（LatencyErr 下降）

### 消融实验结果（隐含比较）
虽然没有显式消融表，但从 zero-shot vs. ours 的对比可以看出：
- **结构化脚本控制** 显著提升了生成质量、一致性与时效性。
- **mode-aware 控制机制** 有助于提升不同 assistance mode 下的表现均衡性。
- **因果逆向推理** 减少了无效或不合理场景的生成。

---

## 4. 关键结论和发现

### 论文的主要发现
1. ✅ **VISTA 可有效生成多样化、逻辑一致的 egocentric 视频**，适用于训练和评估 AI Assistant 在日常任务中的表现。
2. ✅ **proactive assistance 尤其是 implicit proactive 是可行且必要的研究方向**，VISTA 是首个系统支持此类场景生成的框架。
3. ✅ **structured script-to-video pipeline 比 one-shot prompting 更可靠、可控、可复现**，能显著提升生成质量和评估有效性。
4. ✅ **结合 LLM + VFM + SAM3 + LLM-as-a-Judge 的评估闭环** 可实现自动化、多维、实用导向的 agent performance benchmarking。

### 方法的局限性
- **Temporal Consistency 仍具挑战**：尽管使用 first-frame + video generation 解耦策略，但长时间视频的一致性仍有待提升。
- **Script-Video Alignment 不完美**：部分生成视频未能完全遵循脚本意图，需进一步优化提示工程或引入更强约束。
- **依赖前沿 VFM 能力**：目前依赖 Sora、Veo 等闭源 high-fidelity video generator，限制了开源社区的应用。
- **评估仍偏模拟**：虽引入 SAM3 和 VLM，但仍属于 soft evaluation，缺乏真实 human feedback 验证。

### 未来工作方向
- 🔧 **增强 event-level control**：实现对关键事件发生时刻的精确控制。
- 🔄 **改进 temporal coherence**：提升视频帧间连续性与动作合理性。
- 🧩 **开发 model-agnostic adapters**：适配更多开放视频生成模型，降低使用门槛。
- 🤖 **构建 real-world deployment loop**：将生成数据训练的 agent 部署回真实环境，并反馈优化生成器。
- 📈 **扩展至多 agent interaction**：支持多人互动场景下的协作与沟通建模。

--- 

> ✅ **一句话总结**：  
> VISTA 提出了一种基于因果逆向推理与结构化脚本的生成式框架，首次系统性支持 **reactive、explicit proactive、implicit proactive** 三种协助模式的 **egocentric video synthesis**，为 AI 助理的训练与评估提供了安全、可控、可扩展的新范式。

</details>

---

### 10. [Bayesian Optimization with Structured Measurements: A Vector-Valued RKHS Framework](https://arxiv.org/abs/2605.09775)

**Authors**: Wenbin Wang, Colin N. Jones  
**Category**: cs.LG  
**Published**: 2026-05-12  
**Score**: 10.5  
**Type**: new  
**ArXiv ID**: 2605.09775v1  

#### Abstract
Bayesian optimization (BO) is an efficient framework for optimizing expensive black-box functions. However, it is typically formulated as learning an end-to-end mapping from inputs to scalar objectives, thereby discarding the potentially rich information whenever a structured system output is availa...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Bayesian Optimization with Structured Measurements: A Vector-Valued RKHS Framework*

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
传统的 **Bayesian Optimization (BO)** 通常将黑箱系统建模为从输入到**标量目标值**的端到端映射，忽略了系统输出可能具有丰富结构（如轨迹、场、时间序列）的事实。这种做法导致以下问题：
- **信息浪费**：每次观测仅获得一个标量反馈，丢失了潜在的多维或函数型输出中的丰富信息。
- **多目标效率低**：当多个目标是同一结构化输出的不同泛函时（例如不同电价下的能耗），传统方法需对每个目标单独学习，无法共享底层结构信息。
- **时变目标适应差**：在目标随时间变化（如动态电价）的场景下，重新学习成本高。

### 提出了什么新方法或新思路
本文提出了一种基于**向量值再生核希尔伯特空间（vector-valued Reproducing Kernel Hilbert Space, vv-RKHS）** 的新型贝叶斯优化框架 —— **Vector-valued Bayesian Optimization (vvBO)**，其核心思想包括：

- **结构化测量建模**：将未知算子 $ f: \mathcal{X} \to \mathcal{V} $ 建模为向量值函数，其中 $\mathcal{V}$ 是输出 Hilbert 空间（可为有限维或无限维）。观测通过一个已知的**有界线性测量算子** $ M: \mathcal{V} \to \mathcal{M} $ 获得 $ Mf(x) $，而非直接观测 $ f(x) $。
- **目标定义为线性泛函**：最终目标定义为 $ F(x) = \langle m, Mf(x)\rangle_\mathcal{M} $，即测量输出上的线性泛函，这统一了多种实际场景（积分、加权平均等）。
- **在测量空间中进行推理**：引入诱导核 $ K_M(x,s) = MK(x,s)M^* $，直接在测量空间 $\mathcal{M}$ 中构建 KRR 估计器和置信界，避免在全输出空间中保守地传播不确定性。

### 相比现有方法的优势
| 方法 | 局限性 | vvBO 的优势 |
|------|--------|-------------|
| 标量 BO (vanilla BO) | 仅用标量反馈，丢弃结构信息 | 利用完整结构化输出，信息更丰富 |
| 多任务 BO (MTBO) | 依赖有限维输出，需手动设计协方差矩阵 | 支持无限维输出（如函数），自动建模相关性 |
| 上下文 BO (CTBO) | 将目标变化视为上下文，探索开销大 | 直接建模底层算子，跨目标高效迁移 |
| Function-on-function BO (FFBO) | 观测被降维为标量投影 | 可处理完整函数观测，保留更多信息 |

> ✅ **核心优势**：通过利用结构化测量，实现**跨目标的信息高效迁移**和**对时变目标的快速适应**，显著提升样本效率。

---

## 2. 核心实验方法和设置

### 使用的数据集
实验分为两类：

#### （1）合成基准测试（Synthetic Benchmarks）
基于经典优化函数构造结构化输出：
- **GP**：由 RBF 核生成的平滑函数轨迹
- **Ackley**, **Eggholder**, **Bukin**, **Holder Table**, **Shubert**, **Langermann**：标准全局优化测试函数，扩展为输入-输出映射 $ f(x)(t) = h(x,t) $

#### （2）真实世界控制器调优（Real-world Controller Tuning）
使用 **BOPTEST** 框架模拟商业建筑暖通空调系统：
- 控制目标：调节室内温度
- 输出：每日加热功率轨迹 $ Q(t) $ 和温度轨迹 $ y(t) $
- 目标函数：$ J_T(\theta) = \int Q(t)p_{\text{heat},T}(t)dt + 0.1\int Q(t)p_{CO_2}(t)dt + 10000\left(\int (y(t)-24)^2 dt\right) $
- 特点：加热价格 $ p_{\text{heat},T}(t) $ 随天数呈正弦变化，构成**时变目标**

---

### 实验设置和评估指标

#### 设置
- 总预算 $ T = 200 $ 迭代
- 所有方法共享相同的初始点（共10次独立运行取平均）
- 输入空间维度：1–3 维（合成）；3 维（控制器参数）
- 测量模式：
  - **全观测**（$ M = I $）：观测完整轨迹 $ f(x) $
  - **部分观测**（$ M = \Phi^* $）：仅观测有限维投影 $ \Phi^*f(x) \in \mathbb{R}^5 $

#### 评估指标
- **简单遗憾（Simple Regret）**：每轮最优推荐点的目标差距
- **累积遗憾（Cumulative Regret）**：总遗憾，反映整体学习效率
- **验证阶段成本**：在未见条件下评估泛化能力

---

### 基线方法对比
| 方法 | 缩写 | 观测类型 | 是否支持多目标/时变 |
|------|------|----------|---------------------|
| Vanilla BO | BO | 标量 $ F(x) $ | 否 |
| Retrained BO | rBO | 标量（重训练） | 否 |
| Multi-task BO | MTBO | 有限维向量 $ \Phi^*f(x) $ | 是（固定任务） |
| Retrained MTBO | rMTBO | 有限维（重训练） | 是（但不复用数据） |
| Contextual BO | CTBO | 标量 + 上下文 $ m $ | 是（作为上下文） |
| Function-on-function BO | FFBO | 标量 + 固定上下文 | 否 |

> ⚠️ 注意：所有方法优化的是同一个真实目标 $ F(x) = \langle m, f(x)\rangle $，确保公平比较。

---

## 3. 主要实验结果和性能指标

### 关键性能数据与对比结果

#### （1）合成问题（Changing Objectives）
- 在三个阶段中目标函数 $ m_i $ 发生变化（权重或基函数改变）
- **结果**（Fig. 2, 4, 5, 6）：
  - **vvBO (M=I)** 在所有测试函数上均取得最低的**简单遗憾**和**累积遗憾**
  - 相比 CTBO，vvBO 在目标突变时无需大量探索即可快速适应
  - MTBO 表现优于标量 BO，但仍受限于投影维度，无法完全捕捉结构
  - rBO/rMTBO 因丢弃历史数据而表现最差

> 📊 示例：在 *Eggholder* 函数中，经过 200 次迭代后，vvBO 的累积遗憾比 CTBO 降低约 **40%**。

#### （2）真实控制器调优（Time-Varying Objective）
- 加热价格每日波动，目标函数随之变化
- **主动学习阶段**（Fig. 3 左图）：
  - vvBO 在约 150 次迭代后显著降低峰值成本
  - 能根据价格高低动态调整温度设定（高价时降温节能，低价时提温舒适）
- **验证阶段**（Fig. 3 右图）：
  - 在不同电价水平下，vvBO 推荐参数始终带来最低经济成本
  - 当评估新目标（最小化峰值加热功率）时，vvBO 仍表现优异，而 CTBO 因缺乏该“上下文”样本而失效

> 💡 发现：**结构化测量使模型具备跨目标泛化能力**，无需显式建模上下文。

---

### 消融实验结果（Ablation Study）
虽然文中未明确标注“消融实验”，但以下对比本质上构成了消融分析：

| 对比项 | 发现 |
|-------|------|
| **M=I vs M=Φ*** | 全观测显著优于部分观测，说明**更多结构信息带来更高效率** |
| **vvBO vs MTBO under M=Φ*** | 即使观测相同，vvBO 因使用 vv-RKHS 更好建模相关性，表现略优 |
| **vvBO vs CTBO under large context shift** | CTBO 在上下文跳跃大时性能骤降，而 vvBO 不受影响，表明其**对目标变化鲁棒性强** |

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **结构化测量极大提升样本效率**：利用函数型或轨迹型输出能显著减少达到最优所需的查询次数。
2. ✅ **支持高效的跨目标信息迁移**：通过对底层向量值算子建模，可在不同目标间共享知识，避免重复学习。
3. ✅ **天然适应时变目标**：即使目标泛函 $ m_t $ 随时间变化，只要测量 $ Mf(x) $ 可靠，就能快速调整策略。
4. ✅ **理论保证成立**：在分离核（separable kernel）假设下，算法实现了与标量 BO 类似的**次线性遗憾界**（sublinear regret），如：
   - Linear kernel: $ R_T \leq O(\log T \sqrt{T}) $
   - Gaussian kernel: $ R_T \leq O((\log T)^{d+1} \sqrt{T}) $
   - Matérn kernel: $ R_T \leq O(T^{d(d+1)/(2\nu + d(d+1))} \log T \sqrt{T}) $

---

### 方法的局限性
1. **高维输入挑战**：与大多数 BO 方法一样，存在“维度灾难”，在高维输入空间中性能下降。
2. **无约束假设**：当前框架未考虑对轨迹或输出的显式约束（如安全边界、物理限制）。
3. **计算复杂度**：对于无限维输出和一般算子核，矩阵求逆和行列式计算可能昂贵，需依赖谱截断近似（spectral truncation）。
4. **核选择敏感**：性能依赖于 vv-kernel 的设计，尤其是输出空间算子 $ B $ 的选择。

---

### 未来工作方向
1. **扩展至约束优化**：结合 safe Bayesian optimization 或拉格朗日方法，处理输出约束。
2. **非线性目标推广**：目前主要处理线性泛函目标，可进一步研究 Lipschitz 非线性目标下的扩展（Appendix G.2 已初步探讨）。
3. **深度核学习集成**：将神经网络用于学习复杂的 vv-kernel 结构，提升表达能力。
4. **分布式与并行化实现**：针对大规模轨迹数据设计高效计算架构。
5. **现实部署中的鲁棒性研究**：考虑测量噪声模型误设、延迟反馈等问题。

---

> 🔚 **总结**：本文提出的 **vvBO** 框架成功将贝叶斯优化从“标量反馈”范式推进到“结构化测量”时代，不仅在理论上建立了严格的集中性界和遗憾保证，也在实践中证明了其在多目标、时变环境下的卓越性能，为复杂系统（如能源、气候控制、机器人）的智能优化提供了强有力的新工具。

</details>

---

### 11. [TrajDLM: Topology-Aware Block Diffusion Language Model for Trajectory Generation](https://arxiv.org/abs/2605.10020)

**Authors**: Wilson Wongso, Lihuan Li, Arian Prabowo, Xiachong Lin, Baiyu Chen, Hao Xue, Flora D. Salim  
**Category**: cs.LG  
**Published**: 2026-05-12  
**Score**: 10.5  
**Type**: new  
**ArXiv ID**: 2605.10020v1  

#### Abstract
Generating high-fidelity synthetic GPS trajectories is increasingly important for applications in transportation, urban planning, and what-if scenario simulation, especially as privacy concerns limit access to real-world mobility data. Existing trajectory generation models face a trade-off between e...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# TrajDLM: Topology-Aware Block Diffusion Language Model for Trajectory Generation 论文总结

---

## 1. 论文的主要贡献和创新点

### 解决的问题
现有的轨迹生成模型在**效率**与**对道路网络拓扑的忠实度**之间存在权衡：
- **连续空间生成器**（如 DiffTraj、TrajFlow）速度快，但忽略道路网络结构，导致生成的轨迹可能偏离真实道路。
- **拓扑感知模型**（如 TS-TrajGen、HOSER）依赖基于搜索的自回归解码，生成速度慢，难以满足大规模仿真等下游应用的需求。

### 提出的新方法
提出 **TrajDLM** —— 一种基于**块扩散语言模型**（Block Diffusion Language Model, BD3-LM）的拓扑感知轨迹生成框架，其核心思想是：
- 将轨迹建模为**离散道路段序列**（discrete road segments），而非连续坐标。
- 采用**块状离散去噪扩散**（block-wise discrete denoising diffusion）进行高效并行生成。
- 引入**图约束采样策略**确保路径连通性。

### 创新点与优势
1. **首次将 Block Diffusion Language Model 应用于轨迹生成**  
   结合半自回归的块级结构与块内并行去噪，兼顾长程依赖建模与生成效率。

2. **拓扑感知嵌入 + 图约束采样**
   - 使用 **Road Network Encoder (RNE)** 编码道路段的语义与拓扑信息，替代标准 token embedding。
   - 提出 **Topology-Constrained Sampling (TCS)**，通过邻接惩罚矩阵强制合法转移，并结合置信度提交机制保证局部一致性。

3. **高效且高保真**
   - 在保持甚至超越现有拓扑感知模型（如 HOSER）生成质量的同时，**生成速度最高提升达 2.8×**。
   - 支持零样本跨域迁移（zero-shot transfer），在未见交通模式下仍表现良好。

---

## 2. 核心实验方法和设置

### 数据集
使用四个城市尺度的 GPS 轨迹数据集：
| 数据集 | 描述 |
|-------|------|
| **Beijing** | 出租车轨迹，来自 HOSER 预处理版本，经 map-matching 映射到 OpenStreetMap 道路网 |
| **Porto** | 出租车轨迹，同上 |
| **San Francisco** | 出租车轨迹，同上 |
| **GeoLife** | 北京多模态轨迹（步行、骑行、公交等），用于零样本迁移测试 |

所有轨迹均已通过 **Fast Map Matching (FMM)** 技术转换为道路段序列。

### 实验设置
- **模型架构**：以 Qwen3-0.6B-diffusion-bd3lm-v0.1 作为 BDLM 主干。
- **块长度**（Block Length）：Beijing 设为 32，Porto 和 SF 设为 64，匹配平均轨迹长度。
- **训练细节**：使用 AdamW 优化器，weight decay=0.01，在单张 NVIDIA H100 上训练。
- **推理配置**：使用 classifier-free guidance (CFG, w=0.5)，temperature=0.0，每轨迹最多 8 次扩散步。

### 评估指标
分为两类：

#### 全局指标（Global Metrics）
衡量群体分布特性：
- **JSD(Distance)**：真实与生成轨迹总距离分布的 Jensen-Shannon 散度
- **JSD(Radius of Gyration)**：质心半径分布差异

#### 局部指标（Local Metrics）
衡量个体路径相似性（按 OD 单元格分组比较）：
- **Hausdorff Distance**：最大点对点偏差
- **DTW (Dynamic Time Warping)**：时间对齐下的累积距离
- **EDR (Edit Distance on Real sequence)**：编辑距离，反映路径形状相似性

### 基线方法对比
涵盖多种范式：
| 类型 | 方法 |
|------|------|
| 经典算法 | Dijkstra, Markov |
| GAN | MoveSim, TS-TrajGen |
| VAE | TrajSynVAE |
| Diffusion | DiffTraj |
| Transformer | STEGA, HOSER |
| Flow Matching | TrajFlow |

---

## 3. 主要实验结果和性能指标

### 关键性能数据（Test Set 平均值）

| 方法 | Beijing DTW ↓ | Porto DTW ↓ | SF DTW ↓ | Avg Gen Time (s) ↓ |
|------|----------------|--------------|------------|---------------------|
| **TrajDLM (Ours)** | **3.98** | **6.71** | **7.80** | **0.63–1.01** |
| HOSER | 5.98 | 7.85 | 8.22 | 1.79 |
| DiffTraj | 32.71 | 16.41 | 14.22 | 0.40 |
| TrajFlow | 69.78 | 58.97 | 37.21 | 0.68 |

> ✅ TrajDLM 在 **8/15 指标上排名第一**，5 项第二；尤其在局部相似性（DTW）上显著优于所有基线。

### 与基线对比结果
- **相比非拓扑模型**（如 DiffTraj、TrajFlow）：
  - 生成轨迹更符合道路网络结构，热力图可视化显示其避免“穿越建筑”等不合理路径。
  - 局部指标（Hausdorff, DTW, EDR）全面领先。
- **相比拓扑感知模型**（如 HOSER）：
  - **生成速度快 2.8×**（因支持块内并行去噪）。
  - 在 Porto 和 SF 上 DTW 更低，表明路径更精细。
  - 在北京全局指标略逊于 HOSER，但局部路径保真度更高。

### 消融实验结果

#### （1）Road Network Encoder (RNE) 消融
| RNE 设置 | Beijing DTW ↓ | Beijing Hausdorff ↓ |
|---------|----------------|------------------------|
| No RNE | 11.97 | 0.8821 |
| Road+Zone (HOSER-style) | 5.26 | 0.4542 |
| **Road only (ours)** | **3.98** | **0.3640** |

✅ 移除 zone-level 表示反而提升性能，说明**仅依赖静态道路属性即可有效编码拓扑**，且增强泛化能力。

#### （2）块长度（Block Length）影响
| 城市 | 最优 L’ | 性能增益 |
|------|--------|----------|
| Beijing | 32 | Hausdorff 从 0.419 → 0.364 |
| Porto/SF | 64 | DTW 分别下降 ~1.1 / ~0.9 |

✅ 块长度应适配数据集中轨迹长度分布。

#### （3）Topology-Constrained Sampling (TCS)
| 是否启用 TCS | Porto JSD(Dist) ↓ | SF JSD(Dist) ↓ |
|-------------|--------------------|------------------|
| 否 | 0.0020 | 0.0032 |
| 是 | **0.0004** | **0.0007** |

✅ TCS 显著改善全局一致性（减少无效远距离跳跃）。

#### （4）Classifier-Free Guidance (CFG)
| CFG Scale w | Beijing DTW ↓ | Beijing Hausdorff ↓ |
|------------|----------------|------------------------|
| 0.0 | 4.93 | 0.3983 |
| 0.5 | **3.98** | **0.3640** |

✅ 提升 CFG 权重可显著增强局部路径保真度，不影响全局分布。

---

## 4. 关键结论和发现

### 主要发现
1. **块状离散扩散是高效轨迹生成的有效范式**  
   BD3-LM 在保留长程依赖的同时实现块内并行，显著优于传统自回归或逐 token 扩散。

2. **拓扑感知表示 + 图约束采样至关重要**  
   RNE 提供结构先验，TCS 强制物理可行性，二者共同保障生成路径的空间合理性。

3. **TrajDLM 实现了保真度与效率的双重突破**  
   不仅在局部路径相似性上达到 SOTA，还具备实际部署所需的高吞吐能力。

4. **具备强零样本迁移能力**  
   在从未见过的交通方式（如 GeoLife 中的骑行、步行）上仍能生成合理轨迹，说明模型学到的是通用移动规律而非过拟合特定模式。

### 方法局限性
1. **依赖 map-matching 预处理**  
   必须输入已映射到道路段的轨迹，无法直接处理原始 GPS 流。

2. **受限于道路段词表大小**  
   当前模型适用于 ≤40k 路段的城市（如北京），扩展至更大都市（如悉尼超 20 万路段）需解决词表溢出问题。

3. **缺乏显式时间建模**  
   当前仅生成空间路径，未同步预测停留时间或速度变化，限制其在动态仿真中的应用。

4. **主干模型单一**  
   实验仅基于 Qwen3-0.6B，不同规模或架构的 LLM 可能带来新的权衡。

### 未来工作方向
- 扩展至**大规模城市道路网络**（如分层编码、子图采样）
- 开发**时空联合生成模型**，同时建模位置与时间戳
- 探索**端到端 map-matching + 生成一体化框架**
- 构建**通用轨迹基础模型**（trajectory foundation model），支持多城市、多模态联合训练

---

> 🔗 **代码开源地址**：[https://github.com/cruiseresearchgroup/TrajDLM/](https://github.com/cruiseresearchgroup/TrajDLM/)

</details>

---

### 12. [C2L-Net: A Data-Driven Model for State-of-Charge Estimation of Lithium-Ion Batteries During Discharge](https://arxiv.org/abs/2605.08653)

**Authors**: Khoa Tran, T. Nguyen-Thoi, Vin Nguyen-Thai, Duong Tran Anh, Hung-Cuong Trinh, Tri Le  
**Category**: cs.AI  
**Published**: 2026-05-12  
**Score**: 10.0  
**Type**: new  
**ArXiv ID**: 2605.08653v1  

#### Abstract
Accurate state-of-charge (SOC) estimation is critical for the safe and efficient operation of lithium-ion batteries in battery management systems (BMS). Although data-driven approaches can effectively capture nonlinear battery dynamics, many existing methods rely on long historical input sequences, ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文《C2L-Net: A Data-Driven Model for State-of-Charge Estimation of Lithium-Ion Batteries During Discharge》总结

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
当前基于data-driven的SOC（State-of-Charge）估计方法存在以下关键问题：
- **依赖长历史输入序列**：许多模型需要数百秒甚至数千秒的历史数据，导致高计算成本和内存占用，不适用于实时、资源受限的BMS（Battery Management System）。
- **零填充引入位置偏差（padding-induced positional bias）**：在驱动周期开始阶段，由于历史数据不可用，需进行zero-padding，模型可能学习到“高SOC样本对应大量零填充”的虚假模式，而非真实的电池动态特性，影响泛化能力。
- **缺乏对最新测量值的快速响应机制**：多数模型统一处理历史数据，未能显式区分长期上下文信息与最新的关键测量值，限制了对动态工况变化的适应性。

---

### 🚀 提出的新方法：C2L-Net（Context-to-Latest Network）
提出一种新型**短窗口、轻量级、因果建模**的数据驱动框架——**C2L-Net**，用于在线SOC估计。其核心思想是将**上下文编码（context encoding）** 与**最新测量更新（latest-measurement updating）** 显式分离。

#### 主要创新点：
| 创新模块 | 技术细节 | 设计目的 |
|--------|---------|--------|
| **短窗口输入设计** | 仅使用 **20秒（L=200个时间步）** 的历史数据作为输入 | 避免长序列依赖和zero-padding，提升现实部署可行性 |
| **Chunk-Based Feature Extraction** | 将输入序列划分为多个chunk，结合：<br>• **Theta Attention Pooling**：关注chunk内重要时间步<br>• **Fourier-based Seasonality Basis**：提取局部周期性和趋势特征 | 在压缩序列长度的同时保留局部时序动态，降低后续模块负担 |
| **因果上下文编码器（Causal Context Encoder）** | 结合：<br>• **GRU**：捕捉时序依赖<br>• **Causal Cosine Attention**：基于余弦相似度建模历史状态相关性，并施加因果掩码 | 实现严格因果建模，防止未来信息泄露；增强方向相似性感知，鲁棒于特征幅值变化 |
| **最新测量解码器（Latest-Measurement Decoder）** | 使用 **GRUCell** 将最新测量值 $ x_t $ 与上下文状态 $ g_t $ 融合，类比Kalman滤波的状态更新机制 | 快速响应最新工况变化，提高动态适应性和预测灵敏度 |

---

### 🔍 相比现有方法的优势
| 维度 | C2L-Net优势 |
|------|------------|
| **准确性** | 在多种温度条件下达到SOTA或具有竞争力的精度（低MAE/RMSE） |
| **效率** | 参数更少（仅16万）、延迟极低（0.3ms）、吞吐量高达 **3368 inferences/s**，比TCN-Short快 **60倍以上** |
| **泛化性** | 在未见过的drive cycle（如PDMHC）上表现稳健，避免padding诱导的过拟合 |
| **实用性** | 支持滑动窗口在线推理，适合嵌入式BMS部署 |

---

## 2. 核心实验方法和设置

### 📊 数据集
- 使用公开的锂离子电池驱动循环数据集（来自[20] Yao & Kowal, 2025）
- **电池类型**：LG INR 21700 M50LT（NMC化学体系）
- **环境温度条件**：5°C, 15°C, 25°C, 35°C, 45°C（共5种固定温度）
- **Drive Cycles（12种）**：
  - 包括城市驾驶（BCDC）、高速测试（HWFET）、重载卡车（HHDDT）、公交循环（OCTBC）等
- **训练/验证/测试划分**：
  - **Train**: BCDC, LA92, CSHVC, HWFET, IM, US06, PDTCB, OCTBC
  - **Val**: HHDDT, FTP-72
  - **Test**: FTP-75, PDMHC（确保测试集完全未见）

---

### ⚙️ 实验设置
| 项目 | 设置说明 |
|------|----------|
| **输入信号** | Current ($I$), Voltage ($V$), Temperature ($T$)，归一化处理 |
| **输入窗口长度** | $ L = 200 $（即20秒，采样频率10Hz） |
| **输出目标** | SOC（归一化至[0,1]区间） |
| **模型实现** | PyTorch，NVIDIA RTX 3060 GPU |
| **优化器** | AdamW，学习率 $5 \times 10^{-4}$ |
| **损失函数** | MSE Loss |
| **Batch Size** | 128 |
| **训练轮数** | 100 epochs |
| **重复次数** | 所有实验运行3次取平均结果 |

---

### 📏 评估指标
| 指标 | 公式 | 含义 |
|------|------|------|
| **MAE** | $\frac{1}{n}\sum_{i=1}^{n} |\text{SOC}_{\text{true}} - \text{SOC}_{\text{pred}}|$ | 平均绝对误差（%） |
| **RMSE** | $\sqrt{\frac{1}{n}\sum_{i=1}^{n} (\text{SOC}_{\text{true}} - \text{SOC}_{\text{pred}})^2}$ | 均方根误差（%） |
| **MAX Error** | $\max |\text{SOC}_{\text{true}} - \text{SOC}_{\text{pred}}|$ | 最大绝对误差（%） |

---

### 🆚 基线方法对比
| 基线模型 | 类型说明 |
|--------|---------|
| **TCN**, **LSTM**, **GRU** | 经典深度学习架构 |
| **Transformer Encoder** | 自注意力机制代表 |
| **TTSNet** [19] | 基于Temporal Transformer的先进方法 |
| **TCN-Short** [20] | 使用短感受野（~0.8s）的TCN变体，减少padding影响 |

---

## 3. 主要实验结果和性能指标

### 📈 总体性能对比（Table 3）
在五个温度下对 **FTP-75** 和 **PDMHC** 测试集进行评估，C2L-Net在 **4/5 温度条件下取得最佳平均MAE和RMSE**：

| 温度 | 最佳模型（MAE） | C2L-Net MAE | 是否最优 |
|------|------------------|-------------|-----------|
| 45°C | **C2L-Net** | **0.4118%** | ✅ |
| 35°C | LSTM (0.6666%) | 0.7529% | ❌（略差） |
| 25°C | **C2L-Net** | **0.6708%** | ✅ |
| 15°C | **C2L-Net** | **0.7529%** | ✅ |
| 5°C  | **C2L-Net** | **1.0386%** | ✅ |

> ✅ 特别是在低温（5°C）这种更具挑战性的条件下，C2L-Net显著优于其他模型（如TCN: 4.48%, TTSNet: 1.41%），展现出更强的鲁棒性。

---

### ⚡ 计算效率对比（Table 4）
| 模型 | 参数量 | 模型大小 | 平均延迟（ms） | 吞吐量（inferences/s） |
|------|--------|----------|----------------|------------------------|
| TCN-Short | 177,249 | 0.68 MB | 18.68 | 53.5 |
| TTSNet | 1,657,988 | 6.32 MB | 12.22 | 81.8 |
| **C2L-Net（本文）** | **161,347** | **0.62 MB** | **0.30** | **3368.4** |

> 💡 **C2L-Net推理速度是TCN-Short的60倍以上，是TTSNet的40倍以上！**

---

### 🔬 消融实验分析（Ablation Study, Table 2）

#### （1）组件有效性验证（5°C）
| 模块配置 | 平均MAE (%) | 说明 |
|---------|--------------|------|
| Theta Attention Pool + Seasonality Basis | **1.0386%** | ✅ 优于TCN替代方案（1.5856%） |
| GRU-Cosine Attention-GRUCell（完整模型） | **1.0386%** | ✅ 显著优于encoder-only结构（最高达5.76%） |
| GRU-GRUCell | 1.0792% | 表明加入Cosine Attention可进一步提升性能 |
| LSTM-LSTMCell | 1.1190% | GRU在本任务中略优 |

> ✅ 验证了：**chunk特征提取 + 因果上下文建模 + 最新测量更新机制** 的协同作用至关重要。

#### （2）超参数敏感性分析（Fig. 3）
- **输入长度**：L=200（20s）为最佳平衡点，过短（L=50）误差大，过长无明显增益。
- **隐藏维度**：d=128最优，d=512出现过参数化导致性能下降。
- **Dropout率**：p=0.2效果最好，提供适度正则化。
- **谐波数量K**：K=10在PDMHC上表现最佳。

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **短窗口足以实现高精度SOC估计**：仅用20秒历史数据即可达到SOTA水平，无需数千秒长序列。
2. **显式分离“上下文”与“最新测量”有效提升动态响应能力**：受Kalman滤波启发的设计使模型能快速适应负载突变。
3. **chunk-based特征提取 + 因果注意力机制可高效建模局部动态**：兼顾效率与表达力。
4. **避免zero-padding显著提升泛化性**：尤其在低温、复杂工况下优势明显。
5. **C2L-Net兼具高性能与超高效率**：非常适合部署于边缘设备和实时BMS系统。

---

### ⚠️ 局限性
1. **实验基于固定温度条件**：尚未在动态变温场景下验证，实际车辆运行中温度持续变化。
2. **未融合物理先验知识**：纯data-driven方式可能在极端退化或异常工况下稳定性不足。
3. **仅考虑放电过程**：未涵盖充电或充放电混合场景。

---

### 🔮 未来工作方向
1. **扩展至动态温度驱动剖面**：验证模型在真实变温环境下的鲁棒性。
2. **引入Physics-Informed Neural Network（PINN）框架**：融合电化学模型约束，提升外推能力和安全性。
3. **支持端到端充电+放电SOC联合估计**。
4. **硬件部署实测**：在真实BMS芯片（如MCU/FPGA）上验证低功耗运行能力。

---

## ✅ 总结
**C2L-Net是一项面向实用化的创新工作**，它通过精巧的架构设计，在保证高精度的同时极大提升了推理效率，并有效规避了padding带来的虚假关联问题。该模型特别适合应用于**实时、低延迟、资源受限的车载BMS系统**，为下一代智能电池管理系统提供了强有力的技术支撑。

</details>

---

### 13. [Performance and Energy Trade-Off Analysis of Hierarchical Federated Learning for Plant Disease Classification](https://arxiv.org/abs/2605.08121)

**Authors**: Athanasios Papanikolaou, Athanasios Tziouvaras, Pavlos Stoikos, Apostolos Xenakis, Shameem A Puthiya Parambath, George Floros, Enrica Zereik, Ivan Petrovic, Fabio Bonsignorio  
**Category**: cs.DC  
**Published**: 2026-05-12  
**Score**: 10.0  
**Type**: new  
**ArXiv ID**: 2605.08121v1  

#### Abstract
Early detection of plant diseases is critical for improving crop productivity, while it also facilitates the foundations of precision agriculture. Recent advances in distributed deep learning have enabled plant disease classification models to be trained across geographically distributed agricultura...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Performance and Energy Trade-Off Analysis of Hierarchical Federated Learning for Plant Disease Classification*

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
该论文聚焦于在大规模 **IoT**（Internet of Things）农业环境中部署深度学习模型时面临的挑战，特别是：
- **通信开销大**：传统集中式训练需要将大量传感器数据上传至云端，造成高延迟和网络拥堵；
- **能源消耗高**：边缘设备计算资源有限，深度模型训练和推理能耗过高；
- **系统效率低**：缺乏对 **performance-energy-latency** 三者权衡的系统性分析与优化机制。

### 🚀 提出的新方法与创新思路
1. **Hierarchical Federated Learning 架构设计**  
   将植物病害分类任务分解为两个阶段：
   - 第一阶段：识别作物类型（如苹果、番茄、玉米等）；
   - 第二阶段：针对每种作物训练专用的病害分类器（如苹果黑斑病、锈病等）。  
   这种分层结构减少了跨作物干扰，提升了模型专业化程度，并降低了全局通信负担。

2. **Power- and Energy-Aware Optimization Framework**  
   提出一个统一的优化框架，用于联合评估不同 **model-aggregator 配置** 在以下维度的表现：
   - 分类性能（Accuracy, F1-score）
   - 总体能量消耗（Energy Consumption）
   - 执行时间（Execution Time）  
   支持加权目标函数和约束优化两种模式，便于根据不同部署场景（能效优先 vs. 性能优先）进行配置选择。

3. **引入 Energy Efficiency Metric `η(c)`**  
   定义一个新的综合指标：  
   $$
   \eta(c) = \frac{F1(c)}{E(c)}
   $$  
   衡量单位能耗下的分类性能，便于直观比较不同配置的性价比。

### 🔍 相比现有方法的优势
| 方面 | 优势 |
|------|------|
| **架构设计** | 层次化 FL 减少无效更新，提升训练稳定性和通信效率 |
| **评估维度** | 不仅关注 Accuracy，更全面纳入 Energy 和 Time 成本 |
| **决策支持** | 提供可配置的优化框架，适应多样化部署需求（如边缘设备 vs 云环境） |

---

## 2. 核心实验方法和设置

### 📚 数据集
- **PlantDoc Dataset**  
  - 包含 **230,701 张 RGB 叶片图像**
  - 覆盖 **14 种作物类别** 和 **38 类作物-病害组合**
  - 每个标签同时编码作物种类与健康状态，适合分层建模

- **数据增强策略（5个 Use Cases）**  
  模拟真实田间复杂条件，提升模型鲁棒性：
  1. **UC1**: SunnyAngle — 强光、斜视角、阴影
  2. **UC2**: OvercastNoise — 低对比度 + 高斯噪声
  3. **UC3**: Defocus — 轻微模糊、运动抖动
  4. **UC4**: JPEGandCast — 压缩伪影 + 白平衡偏移
  5. **UC5**: OffCenter — 偏中心裁剪、曝光变化

### ⚙️ 实验设置
| 参数 | 配置 |
|------|------|
| **Clients / Rounds / Local Epochs** | 10 客户端 / 30 轮 / 每轮 5 个本地 epoch |
| **Backbone Models** | EfficientNet-B0, ResNet-50, MobileNetV3-Large |
| **Aggregation Strategies** | FedAvg, FedProx, FedAvgM |
| **Input Size / Batch Size** | 224×224 / 64 |
| **Optimizer / LR / WD** | Adam / 1e-4 / 1e-4 |
| **Loss Function** | Cross-Entropy + Label Smoothing (0.1) |
| **Hardware Platform** | NVIDIA RTX 6000 Ada Generation |

> 注：所有结果基于完整的 hierarchical training 流程（包括 crop classifier 和 disease classifier），非单一轮次或单一模型。

### 📊 评估指标
| 类型 | 指标 |
|------|------|
| **性能指标** | Accuracy, Recall, Precision, F1-score |
| **系统效率指标** | Total Energy Consumption (Wh), Total Execution Time (s) |
| **综合指标** | Energy Efficiency Score $\eta(c)$ |

### 🔁 基线方法对比
本文未采用传统 centralized training 作为直接基线，而是通过在相同 FL 框架下对比不同 **backbone-aggregator 组合** 来揭示 trade-offs：
- **Backbone 对比**：轻量级（MobileNetV3-Large）vs 中等（EfficientNet-B0）vs 高容量（ResNet-50）
- **Aggregator 对比**：FedAvg vs FedProx vs FedAvgM

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据（来自 Table II）

| Model | Aggregator | F1-score | Energy (Wh) | Time (s) | η (F1/Energy) |
|-------|------------|----------|-------------|----------|----------------|
| **ResNet-50** | FedAvg | **0.9062** | 575.12 | 13315.68 | 0.002 |
| ResNet-50 | FedProx | 0.8942 | 372.12 | 12291.58 | 0.002 |
| ResNet-50 | FedAvgM | 0.8840 | 461.02 | 12147.10 | 0.002 |
| **EfficientNet-B0** | FedAvg | 0.8535 | 163.39 | 4216.38 | 0.005 |
| EfficientNet-B0 | FedProx | 0.8429 | 218.76 | 5503.40 | 0.004 |
| **MobileNetV3-Large** | FedAvg | 0.8652 | 176.68 | 5112.66 | 0.005 |
| **MobileNetV3-Large** | **FedProx** | 0.8583 | **142.73** | 4446.40 | **0.006** ✅ |
| MobileNetV3-Large | FedAvgM | 0.7992 | 165.90 | **4202.80** ✅ | 0.005 |

> ✅ 高亮表示最优值（蓝色：最高性能；绿色：最低能耗 + 最高能效；橙色：最短执行时间）

### 🔍 与基线方法的对比结果
| 维度 | 最优配置 | 观察结论 |
|------|--------|---------|
| **最高预测性能** | ResNet-50 + FedAvg | F1 达到 **0.9062**，显著优于其他轻量模型 |
| **最低能耗 & 最高能效** | MobileNetV3-Large + FedProx | 能耗仅 **142.73 Wh**，$\eta = 0.006$ 为最佳 |
| **最快执行速度** | MobileNetV3-Large + FedAvgM | 总耗时 **4202.80 s**，但 F1 下降至 0.7992 |
| **中间均衡方案** | EfficientNet-B0 + FedAvg | 能耗较低（163.39 Wh），F1 达 0.8535，性价比较高 |

### 📉 消融实验与趋势分析（隐含在结果中）
- **Aggregation Strategy 影响**：
  - **FedAvg** 在所有 backbone 上均取得最佳 F1，说明其简单平均机制在此任务上最有效；
  - **FedProx** 显著降低能耗（尤其在 MobileNetV3-Large 上），适合异构设备；
  - **FedAvgM** 表现最差，可能因动量机制导致收敛不稳定。
- **Backbone 影响**：
  - ResNet-50 性能最强但代价高昂；
  - MobileNetV3-Large 在 FedProx 下实现“接近高性能 + 低能耗”的理想平衡。

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **不存在“全能最优”配置**：必须根据实际部署需求在 performance、energy、latency 之间做出权衡。
2. **ResNet-50 + FedAvg 是性能冠军**：适用于对诊断精度要求极高的场景（如科研监测）。
3. **MobileNetV3-Large + FedProx 是能效王者**：在保持较高 F1（0.8583）的同时，能耗最低（142.73 Wh），特别适合电池供电的边缘 IoT 设备。
4. **Hierarchical FL 架构有效**：通过解耦 crop classification 与 disease detection，提高了模型专注度并减少了冗余通信。
5. **Energy Efficiency Metric $\eta$ 具有指导意义**：能够快速识别“高性价比”配置，辅助工程选型。

### ⚠️ 方法的局限性
- **仿真环境限制**：实验基于模拟 FL 环境，尚未在真实分布式农业传感网络中验证；
- **静态权重设定**：当前优化框架使用固定权重（λ₁=λ₂=λ₃），缺乏动态自适应能力；
- **忽略通信细节建模**：未深入建模无线信道波动、带宽差异等现实因素；
- **仅考虑前向传播能耗**：未区分训练与推理阶段的能耗分布。

### 🔮 未来工作方向
1. **参数敏感性分析（Sensitivity Analysis）**：系统研究 λ₁, λ₂, λ₃ 的影响，构建 context-aware 自适应选择机制；
2. **动态资源配置**：结合设备实时电量、网络状况动态调整 aggregator 或 model 大小；
3. **扩展至更多 backbone 与 aggregation 方法**：如 TinyML 模型、FedNova、SCAFFOLD 等；
4. **真实世界部署验证**：在真实农田 IoT 网络中测试框架实用性；
5. **引入碳足迹评估**：将能耗转化为碳排放指标，推动绿色 AI 农业发展。

---

> **总结一句话**：  
> 本论文首次系统地揭示了 **Hierarchical Federated Learning** 在植物病害分类中的 **performance-energy-latency 权衡关系**，提出了一套实用的评估与优化框架，为资源受限的智慧农业系统提供了科学的设计依据。

</details>

---

### 14. [Dystruct: Dynamically Structured Diffusion Language Model Decoding via Bayesian Inference](https://arxiv.org/abs/2605.09820)

**Authors**: Bian Sun, Kevin Zhai, Mubarak Shah, Zhenyi Wang  
**Category**: cs.LG  
**Published**: 2026-05-12  
**Score**: 10.0  
**Type**: new  
**ArXiv ID**: 2605.09820v1  

#### Abstract
Diffusion language models (DLMs) have recently emerged as a promising alternative to autoregressive models, primarily due to their ability to enable parallel decoding. Despite this advantage, most existing DLMs rely on a fixed generation length specified prior to decoding, which restricts their flex...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：DyStruct: Dynamically Structured Diffusion Language Model Decoding via Bayesian Inference

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
现有的 **Diffusion Language Models (DLMs)** 虽然支持并行解码、提升推理效率，但大多依赖**固定生成长度**（fixed-length decoding），这在实际应用中缺乏灵活性。复杂任务需要更长输出，简单输入则应简洁回应，而固定长度易导致截断或冗余。

此外，已有的一些可变长度方法（如 FlexMDM、DID）存在以下问题：
- 需要重新训练模型（costly retraining）
- 仅依赖局部置信度信号进行扩展（local confidence-based criteria），忽略序列的**结构性演化**

更重要的是，这些方法在扩展后缺乏对内容组织的建模，导致生成结果出现**结构碎片化**（fragmented structure）。

---

### 🚀 提出的新方法与核心思想
本文提出 **DyStruct** —— 一种**无需训练**（training-free）、基于**贝叶斯结构推断**（Bayesian structured inference）的动态结构化解码框架。

#### 核心创新点：
1. **将可变长度生成建模为联合结构推断问题**  
   在每一步窗口扩展时，同时推断三个关键变量：
   - 扩展长度 $ L_t $
   - 新窗口内的块划分 $ P^{(t)} $（block partitioning）
   - 块的解码顺序调度 $ \tau^{(t)} $（decoding schedule）

2. **引入 Chinese Restaurant Process (CRP) 先验进行块划分**
   - 不需预设块数量或边界
   - 动态决定是否“延续当前块”或“开启新块”
   - 自适应捕捉语义单元（如句子、逻辑步骤等）

3. **上下文感知的调度机制（Context-aware Scheduling）**
   - 根据块的不稳定性 $ H(B) $ 和邻近已解码上下文的程度 $ C(B) $，通过 Gibbs 分布排序解码优先级
   - 优先解码稳定且有锚定上下文的块，提高整体一致性

4. **边缘焊接（Edge-Welding）修复块间不一致**
   - 对相邻块之间的边界区域进行局部重掩码与再优化
   - 缓解因独立解码带来的分布漂移和语法断裂

5. **完全 inference-time 方法，无需修改模型参数**
   - 可直接应用于冻结的 DLM 模型（如 LLaDA、Dream）

---

### 🔍 相比现有方法的优势
| 方法 | 是否需重训练 | 是否支持灵活长度 | 是否建模结构 | 是否训练自由 |
|------|---------------|------------------|--------------|----------------|
| 传统 DLMs | 否 | ❌ 固定长度 | ❌ | ✅ |
| FlexMDM / DID | ✅ 是 | ✅ | ❌ | ❌ |
| DAEDAL | ❌ 否 | ✅ | ❌（仅局部置信） | ✅ |
| **DyStruct (Ours)** | ❌ 否 | ✅ | ✅（CRP + 调度 + 焊接） | ✅ |

> ✅ **优势总结**：DyStruct 实现了**训练自由 + 结构感知 + 动态长度 + 内容组织能力**，是首个从贝叶斯视角统一处理长度增长、块划分与解码顺序的方法。

---

## 2. 核心实验方法和设置

### 📚 使用的数据集
在多个领域基准上评估泛化能力：

| 类别 | 数据集 | 任务描述 | 评估指标 |
|-------|--------|----------|-----------|
| 数学推理 | **GSM8K**, **MATH** | 多步数学题求解 | Strict Match Accuracy |
| 代码生成 | **HumanEval**, **MBPP** | Python 函数生成 | Pass@1 (greedy) |
| 多步逻辑推理 | **Big-Bench Hard (BBH)** | 复杂逻辑与消歧任务 | Exact Match Accuracy |

---

### ⚙️ 实验设置
- **基础模型**：
  - `LLaDA-8B-Base`
  - `Dream-7B-Base`
- **最大序列长度限制**：256 tokens
- **总去噪迭代预算**：256 steps（所有方法共享）
- **硬件平台**：单张 NVIDIA H100 GPU
- **评估工具**：`lm-evaluation-harness` [42]

> 所有对比均保持计算资源严格对等，确保公平比较。

---

### 🆚 基线方法
| 基线 | 描述 |
|------|------|
| **Fixed-length DLM** | 原始固定长度扩散模型（如 LLaDA/Dream 原生） |
| **DAEDAL [6]** | 当前主流的训练自由可变长度方法，基于局部置信度裁剪 |
| **Full DyStruct** | 本文完整方法（含 CRP 划分 + 上下文调度 + 边缘焊接） |
| **Ablation Variants** | 移除调度、焊接或两者 |

---

## 3. 主要实验结果和性能指标

### 📊 关键性能数据（来自 Table 1）

| Model | HumanEval | MBPP | GSM8K | MATH | BBH |
|-------|-----------|------|--------|------|-----|
| LLaDA-8B-Base | 32.3 | 39.8 | 70.3 | 30.5 | 44.9 |
| + DAEDAL | 33.5 | 40.2 | 70.8 | 31.2 | **43.7↓** |
| + **DyStruct** | **34.8↑** | **41.4↑** | **72.1↑** | **31.4↑** | **49.3↑** |
| Dream-7B-Base | 40.2 | 57.2 | 74.9 | 38.2 | 51.7 |
| + DAEDAL | 34.7↓ | 54.4↓ | 74.3 | 38.6 | 44.8↓ |
| + **DyStruct** | **47.0↑** | **59.8↑** | **75.1↑** | **38.8↑** | **52.5↑** |

> ✅ **全面超越基线**，尤其在逻辑密集型任务（BBH）上提升显著（+4.4 pts on LLaDA）。

---

### 📉 消融实验结果（Table 2）

| 配置 | HumanEval | MBPP | GSM8K | MATH | BBH |
|------|------------|------|--------|------|-----|
| Full DyStruct | 34.8 | 41.4 | 72.1 | 31.4 | 49.3 |
| w/o Block Schedule | 33.5 | 41.2 | 71.8 | 30.3 | 49.3 |
| w/o Boundary Repair | 32.9 | 40.8 | 70.5 | 31.2 | 49.1 |
| w/o Both | 32.9 | 41.0 | 69.7 | 31.0 | 49.1 |

> 🔍 **关键发现**：
- 移除上下文调度 → 数学推理下降明显（MATH ↓1.1），说明多步推理需双向锚定
- 移除边缘焊接 → 代码生成显著退化（HumanEval ↓1.9），验证其对语法连贯性的必要性

---

### 📈 推理效率分析（Figure 2）
- 在 **GSM8K** 上，DyStruct 平均每迭代耗时更低（s/it 更小）
- 原因：低不稳定的数学模板部分能提前终止 refinement，节省计算
- 表明 DyStruct 实现了**自适应计算分配**——高不确定性区域获得更多迭代

---

### 🔬 定性分析案例
- **Figure 3**：无边缘焊接时，`if abs(x-y)` 错误生成；启用后修复为 `abs(numbers[i]-numbers[j])`
- **Figure 4 & 5**：CRP 成功识别高不稳定性逻辑步骤，并由调度器优先锚定上下文块，引导中间推理

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **结构化推断显著提升生成质量与一致性**
   - 尤其在涉及多步逻辑、语法约束的任务中（BBH、HumanEval）
   - 局部置信度不足以支撑全局结构一致性

2. **CRP prior 能有效建模语义块的自然分割**
   - 无需人工设定 delimiters 或固定大小
   - 支持动态、非单调的内容组织

3. **上下文感知调度是实现高质量推理的关键**
   - “先锚定两端，再填充中间”的策略优于纯左到右解码
   - 符合人类思维中的“框架先行”模式

4. **边缘焊接机制缓解了块间分布漂移**
   - 是保证最终输出语法完整性和语义连贯的重要环节

5. **方法具有强通用性与鲁棒性**
   - 在不同 backbone（LLaDA vs Dream）上均取得一致增益
   - 超参数敏感性低（见 Table 3 & 6），无需任务特定调参

---

### ⚠️ 局限性
- **纯 inference-time 设计虽具广泛适用性，但也意味着无法反向传播优化结构先验**
  - 未来可探索将结构先验融入训练过程
- 当初始窗口过大（如 256 tokens）时性能下降
  - 原因：缺乏条件锚点导致严重 distributional drift
  - 强调了逐步扩展的重要性
- 当前 CRP 使用启发式特征投影计算 instability，尚未端到端学习

---

### 🔮 未来工作方向
1. **将结构先验整合进训练阶段**
   - 构建 end-to-end trainable structured diffusion model
2. **扩展至图像、音频等跨模态结构生成**
   - 如段落级文本生成、对话结构规划
3. **结合 CoT prompting 进行显式思维链结构控制**
4. **研究更复杂的 hierarchical CRP 或 tree-structured partitioning**

---

## 总结
> **DyStruct** 提出了一种全新的、**训练自由的贝叶斯结构化解码框架**，首次将可变长度生成视为一个联合的结构推断问题。通过 **CRP 块划分 + 上下文感知调度 + 边缘焊接** 三者协同，实现了高质量、高一致性的动态文本生成，在数学、编程、逻辑推理等多个任务上显著优于现有 fixed-length 与 flexible-length 方法。

该工作为 **structured text generation in DLMs** 提供了一个原则性强、高效且实用的新范式。

</details>

---

### 15. [Efficient Neural Architectures for Real-Time ECG Interpretation on Limited Hardware](https://arxiv.org/abs/2605.09848)

**Authors**: Ashery Mbilinyi, Callum O'Riley, Julia Handra, Ashley Moller-Hansen, Jason Andrade, Marc Deyell, Cameron Hague, Nathaniel Hawkins, Kendall Ho, Jonathan Leipsic, Roger Tam  
**Category**: cs.LG  
**Published**: 2026-05-12  
**Score**: 10.0  
**Type**: new  
**ArXiv ID**: 2605.09848v1  

#### Abstract
Electrocardiogram (ECG) interpretation is essential for diagnosing a wide range of cardiac abnormalities. While deep learning has shown strong potential for automating ECG classification, many existing models rely on large, computationally intensive architectures that hinder practical deployment. In...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Efficient Neural Architectures for Real-Time ECG Interpretation on Limited Hardware*

---

## 1. **论文的主要贡献和创新点**

### ✅ 解决的问题
当前基于深度学习的 **ECG interpretation** 模型虽然在诊断准确性上表现优异，但大多数采用大规模、计算密集型的 **CNN** 或 **Transformer** 架构（如 DeepResidualCNN），导致推理延迟高、内存占用大，难以部署在资源受限的临床环境（如移动设备、基层医院、远程医疗系统）中。

本研究旨在解决这一“算法先进性”与“部署可行性”之间的鸿沟，探索如何在保证诊断准确性的前提下，显著降低模型的 **computational cost** 和硬件依赖。

---

### 🚀 提出的新方法与创新思路

作者提出了三种轻量级（lightweight）CNN 架构，均以 **computational efficiency** 为核心设计目标：

1. **ParallelCNN**  
   - 双分支结构：分别提取 **temporal**（时间序列波形）和 **spatial**（多导联间关系）特征。
   - 显式分离时空处理路径，提升特征学习效率。
   
2. **ParallelCNNew**  
   - ParallelCNN 的改进版，通过 **symmetric weight initialization** 实现两个分支训练过程中的平衡学习，避免早期偏向某一模态。

3. **SimpleNet**  
   - 单流紧凑架构，使用方形卷积核（square-shaped kernels）联合捕捉空间与时间依赖。
   - 参数最少、结构最简，专为边缘设备优化。

此外，提出一个统一的评估指标 —— **Efficiency Score**，综合衡量：
- 诊断性能（AUC）
- 模型大小（Params）
- 推理速度（Inference Time）
- 内存占用（Memory Usage）

该指标支持跨任务、跨模型的公平比较，特别适用于资源受限场景下的模型选型。

---

### 🔍 相比现有方法的优势

| 方面 | 优势说明 |
|------|---------|
| **设计哲学** | 不是事后压缩大模型（post-hoc compression），而是从头设计高效架构（ground-up design），更适合实际部署。 |
| **效率-精度权衡** | 在保持接近 state-of-the-art 准确率的同时，大幅减少参数量和推理时间。例如，**AttiaNet** 仅用 0.15M 参数即达到 ~0.99 AUC。 |
| **通用性与可扩展性** | 模型在三个国家（德国、中国、美国）的不同 ECG 数据集上验证，涵盖 binary、multiclass、multilabel 分类任务，具备良好泛化能力。 |
| **低成本增强策略** | 验证了加入 **age** 和 **sex** 等低开销元数据可在不增加计算负担的前提下轻微提升性能，尤其对复杂模型更有效。 |

---

## 2. **核心实验方法和设置**

### 📚 使用的数据集

| 数据集 | 来源 | 样本数 | 采样率 | 任务类型 | 特点 |
|--------|------|--------|--------|----------|------|
| **PTB-XL** | Germany | 21,799 | 500 Hz | Multilabel Classification | 多标签诊断（MI, ST/T change, CD, HYP, NORM） |
| **Chapman-Shaoxing** | China | 10,646 | 500 Hz | Multiclass Classification | 四类心律分类（AFIB, GSVT, SB, SR） |
| **MIMIC-IV-ECG** | USA | ~800,000 | 500 Hz | Binary Classification | 正常 vs 异常（基于 cardiologist 报告） |

> 所有输入均为 12-lead ECG，长度为 10 秒 → 输入维度为 `12 × 5000`

---

### ⚙️ 实验设置

- **训练配置**：
  - Optimizer: Adam (`lr = 1e-3`)
  - Batch Size: 32
  - Early Stopping: 基于验证损失
  - 硬件平台：单张 NVIDIA GeForce RTX 3070 GPU (8GB)

- **输入模式对比**：
  - Raw ECG only
  - ECG + Demographic features (**age**, **sex**)

- **评估指标**：
  - 主要性能指标：**AUC**（Area Under ROC Curve）
  - 效率指标：
    - 参数数量（Params in millions）
    - 单样本推理时间（Inference Time in ms）
    - 峰值 GPU 内存使用（Peak GPU Memory in MB）
    - 综合指标：**Efficiency Score**

---

### 🧪 基线方法对比

| 模型 | 类型 | 参数量 | 是否作为 baseline |
|------|------|--------|------------------|
| **AttiaNet** [26] | Compact Sequential CNN | 0.15M | ✅ 是（轻量基准） |
| **DeepResidualCNN** [27] | Deep ResNet-like | 5.90M | ✅ 是（复杂模型代表） |
| **ParallelCNN** | Dual-branch Lightweight | 20.42M | ❌ 新提出 |
| **ParallelCNNew** | Balanced Initialization Variant | 22.99M | ❌ 新提出 |
| **SimpleNet** | Unified Stream Compact | 2.59M | ❌ 新提出 |

> 注：DeepResidualCNN 是 2021 PhysioNet Challenge 冠军方案。

---

## 3. **主要实验结果和性能指标**

### 📊 关键性能数据汇总（来自 Tables I–III 和 Figures 4–6）

#### A. **诊断性能（AUC）**

| Model | Multilabel (PTB-XL) | Multiclass (Chapman) | Binary (MIMIC-IV) |
|-------|---------------------|------------------------|--------------------|
| **AttiaNet** | **0.99** | **0.99** | **0.98** |
| **SimpleNet** | 0.99 | 0.97 | 0.96 |
| **ParallelCNN** | 0.99 | 0.97 | 0.95 |
| **ParallelCNNew** | 0.99 | 0.97 | 0.95 |
| **DeepResidualCNN** | 0.64 | 0.61 | 0.62 |

> 💡 尽管 DeepResidualCNN 结构更深，但在所有任务中表现最差，可能因过拟合或缺乏足够正则化。

---

#### B. **效率指标对比（以 Multilabel 为例）**

| Model | Params (M) | Inference Time (ms) | Peak Mem (MB) | Efficiency Score |
|-------|------------|----------------------|---------------|------------------|
| **AttiaNet** | **0.15** | 0.79 | **48.37** | **0.93** |
| **SimpleNet** | 2.59 | **0.62** | 244.43 | 0.82 |
| **ParallelCNN** | 20.42 | 0.51 | 149.06 | 0.81 |
| **ParallelCNNew** | 22.99 | 0.63 | 236.67 | 0.71 |
| **DeepResidualCNN** | 5.90 | 1.16 | 77.17 | 0.59 |

> ✅ **AttiaNet** 在效率得分上全面领先；**SimpleNet** 推理最快，适合实时应用。

---

#### C. **消融实验结果（Ablation Study）**

- **Demographic Feature Integration（Age & Sex）的影响**：
  - 对 **DeepResidualCNN** 提升最大：
    - Multilabel: ↑7%
    - Multiclass: ↑5%
    - Binary: ↑10%
  - 对 **AttiaNet / SimpleNet / ParallelCNN** 提升极小（<1%）
  - ➜ 表明轻量模型已充分挖掘 ECG 波形信息，附加 metadata 收益有限。
  - ➜ 但也说明对于欠拟合的大模型，metadata 可提供有用归纳偏置。

- **Initialization Strategy（ParallelCNNew vs ParallelCNN）**：
  - 性能相近，但 ParallelCNNew 训练更稳定，收敛更快。
  - 表明 symmetric initialization 有助于双分支均衡学习。

---

## 4. **关键结论和发现**

### ✅ 主要发现

1. **轻量模型可以媲美甚至超越复杂模型的诊断性能**  
   如 **AttiaNet**（仅 0.15M 参数）在多个任务上达到近 0.99 AUC，远超拥有 5.9M 参数的 DeepResidualCNN。

2. **模型效率不能仅看参数量，需综合推理时间与内存使用**  
   虽然 SimpleNet 参数较多（2.59M），但由于结构简洁，其推理速度最快，在时间敏感场景更具优势。

3. **提出的 Efficiency Score 是有效的部署导向评价标准**  
   成功识别出 AttiaNet 和 SimpleNet 为最优候选，而 DeepResidualCNN 尽管结构复杂却效率最低。

4. **demographic metadata 的增益具有边际递减效应**  
   轻量模型本身已高度优化，加入 age/sex 改善有限；但对于表现较差的大模型，这些低成本特征能带来可观提升。

5. **双分支设计（ParallelCNN）有一定潜力，但增加复杂度**  
   并未显著优于单流设计，且参数更多，效率得分偏低。

---

### ⚠️ 局限性

1. **固定超参数训练**：所有模型使用相同 learning rate 和 batch size，未进行任务特定调优，可能导致次优性能。
2. **静态 ECG 快照分析**：仅处理 10 秒片段，无法建模长期动态变化（如节律演变）。
3. **硬件测试局限**：效率评估基于桌面级 GPU（RTX 3070），尚未在真实边缘设备（如 Raspberry Pi、手机 SoC）上验证。
4. **缺乏前瞻性临床验证**：目前为回顾性研究，尚无真实世界临床 workflow 中的应用反馈。

---

### 🔮 未来工作方向

1. **适配移动端/嵌入式硬件**：将最佳模型（如 SimpleNet）移植至 ARM 架构或 MCU 上，实现实时嵌入式部署。
2. **自适应训练策略**：引入 NAS（Neural Architecture Search）或动态稀疏训练进一步压缩模型。
3. **多模态融合扩展**：整合 EHR、lab results、影像等其他临床数据，构建更全面的心血管风险预测系统。
4. **在线学习与个性化建模**：开发支持持续更新的轻量模型，适应个体患者差异。
5. **前瞻性临床试验**：在急诊科、家庭监护等场景中测试模型的实际辅助诊断价值。

---

## ✅ 总结

本论文系统地论证了：**精心设计的小型 CNN 模型（如 AttiaNet 和 SimpleNet）能够在保持顶尖诊断准确率的同时，实现极高的运行效率，是面向资源受限环境（real-time, edge-device, point-of-care）ECG 自动解读的理想解决方案**。研究不仅提出了新的高效架构，还建立了兼顾性能与成本的评估体系（Efficiency Score），为未来医学 AI 的实用化落地提供了重要参考。

</details>

---

### 16. [GRC: Unifying Reasoning-Driven Generation, Retrieval and Compression](https://arxiv.org/abs/2605.09100)

**Authors**: Zhongtao Miao, Qiyu Wu, Yoshimasa Tsuruoka  
**Category**: cs.CL  
**Published**: 2026-05-12  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2605.09100v1  

#### Abstract
Text embedding and generative tasks are usually trained separately based on large language models (LLMs) nowadays. This causes a large amount of training cost and deployment effort. Context compression is also a challenging and pressing task, which is vital to reasoning-driven generation, and agenti...

---

### 17. [MegaScale-Omni: A Hyper-Scale, Workload-Resilient System for MultiModal LLM Training in Production](https://arxiv.org/abs/2605.08962)

**Authors**: Chunyu Xue, Yangrui Chen, Jianyu Jiang, Ningxin Zheng, Junda Feng, Jingji Chen, Shixiong Zhao, Shen Yan, Yi Lin, Lei Shi, Zanbo Wang, Lishu Luo, Faming Wu, Haibin Lin, Xin Liu, Yanghua Peng, Quan Chen  
**Category**: cs.DC  
**Published**: 2026-05-12  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2605.08962v1  

#### Abstract
As the foundational component of versatile AI applications, training an multimodal large language model (MLLM) relies on multimodal datasets with dynamic modality mixture proportions and sample length distributions. However, existing MLLM systems remain inefficient under dynamic workloads, due to st...

---

### 18. [AdamFLIP: Adaptive Momentum Feedback Linearization Optimization for Hard Constrained PINN Training](https://arxiv.org/abs/2605.08408)

**Authors**: Binghang Lu, Runyu Zhang, Changhong Mou, Na Li, Guang Lin  
**Category**: cs.LG  
**Published**: 2026-05-12  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2605.08408v1  

#### Abstract
Physics-informed neural networks (PINNs) provide a flexible framework for solving forward and inverse problems governed by partial differential equations (PDEs), but standard PINN training typically relies on soft penalty formulations that combine PDE residuals, data mismatch, and initial/boundary c...

---

### 19. [Auto-Rubric as Reward: From Implicit Preferences to Explicit Multimodal Generative Criteria](https://arxiv.org/abs/2605.08354)

**Authors**: Juanxi Tian, Fengyuan Liu, Jiaming Han, Yilei Jiang, Yongliang Wu, Yesheng Liu, Haodong Li, Furong Xu, Wanhua Li  
**Category**: cs.AI  
**Published**: 2026-05-12  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.08354v1  

#### Abstract
Aligning multimodal generative models with human preferences demands reward signals that respect the compositional, multi-dimensional structure of human judgment. Prevailing RLHF approaches reduce this structure to scalar or pairwise labels, collapsing nuanced preferences into opaque parametric prox...

---

### 20. [SkillLens: Adaptive Multi-Granularity Skill Reuse for Cost-Efficient LLM Agents](https://arxiv.org/abs/2605.08386)

**Authors**: Yongliang Miao, Ziyang Yu, Liang Zhao, Bowen Zhu, Hasibul Haque  
**Category**: cs.AI  
**Published**: 2026-05-12  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.08386v1  

#### Abstract
Skill libraries have become a practical way for LLM agents to reuse procedural experience across tasks. However, existing systems typically treat skills as flat, single-resolution prompt blocks. This creates a tension between relevance and cost: injecting coarse skills can introduce irrelevant or mi...

---

### 21. [AHD Agent: Agentic Reinforcement Learning for Automatic Heuristic Design](https://arxiv.org/abs/2605.08756)

**Authors**: Haoze Lv, Ning Lu, Ziang Zhou, Shengcai Liu  
**Category**: cs.AI  
**Published**: 2026-05-12  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.08756v1  

#### Abstract
Automatic heuristic design (AHD) has emerged as a promising paradigm for solving NP-hard combinatorial optimization problems (COPs). Recent works show that large language models (LLMs), when integrated into well-designed frameworks (i.e., LLM-AHD), can autonomously discover high-performing heuristic...

---

### 22. [Meow-Omni 1: A Multimodal Large Language Model for Feline Ethology](https://arxiv.org/abs/2605.09152)

**Authors**: Jucheng Hu, Zhangquan Chen, Yulin Chen, Chengjie Hong, Liang Zhou, Tairan Wang, Sifei Li, Giulio Zhu, Feng Zhou, Yiheng Zeng, Suorong Yang, Dongzhan Zhou  
**Category**: cs.CL  
**Published**: 2026-05-12  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.09152v1  

#### Abstract
Deciphering animal intent is a fundamental challenge in computational ethology, largely because of semantic aliasing, the phenomenon where identical external signals (e.g., a cat's purr) correspond to radically different internal states depending on physiological context. Existing Multimodal Large L...

---

### 23. [TacoMAS: Test-Time Co-Evolution of Topology and Capability in LLM-based Multi-Agent Systems](https://arxiv.org/abs/2605.09539)

**Authors**: Chen Xu, Yicheng Hu, Ruizi Wang, Xinyu Lin, Wenjie Wang, Dongrui Liu, Fuli Feng  
**Category**: cs.CL  
**Published**: 2026-05-12  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.09539v1  

#### Abstract
Multi-agent systems (MAS) have emerged as a promising paradigm for solving complex tasks. Recent work has explored self-evolving MAS that automatically optimize agent capabilities or communication topologies. However, existing methods either learn a topology that remains fixed at inference time or a...

---

### 24. [ANCHOR: Abductive Network Construction with Hierarchical Orchestration for Reliable Probability Inference in Large Language Models](https://arxiv.org/abs/2605.10328)

**Authors**: Wentao Qiu, Guanran Luo, Zhongquan Jian, Jingqi Gao, Meihong Wang, Qingqiang Wu  
**Category**: cs.CL  
**Published**: 2026-05-12  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.10328v1  

#### Abstract
A central challenge in large-scale decision-making under incomplete information is estimating reliable probabilities. Recent approaches leverage Large Language Models (LLMs) to generate explanatory factors and elicit coarse-grained probability estimates. Typically, an LLM performs forward abduction ...

---

### 25. [PoHAR: Understanding Hyperlocal Human Activities with Pollution Sensor Networks](https://arxiv.org/abs/2605.09434)

**Authors**: Prasenjit Karmakar, Karthik Reddy, Sandip Chakraborty  
**Category**: cs.DC  
**Published**: 2026-05-12  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.09434v1  

#### Abstract
Low-cost air quality sensors are becoming ubiquitous in our daily lives as public awareness of air pollution continues to grow, and people take measures to monitor and improve the air they breathe indoors. Besides the standard operation of these sensors, fluctuations in environmental parameters can ...

---

### 26. [Accelerating Compound LLM Training Workloads with Maestro](https://arxiv.org/abs/2605.10501)

**Authors**: Xiulong Yuan, Hongqing Chen, Jiaxuan Peng, Fan Zhou, Zhixiang Ruan, Zekun Wang, Bo Zheng, Rui Men, Haiquan Wang, Zhipeng Zhang, Langshi Chen, Man Yuan, Jiaqi Gao, Zhengping Qian, Junyang Lin, Yong Li, Wei Lin, Junhua Wang, Jingren Zhou  
**Category**: cs.DC  
**Published**: 2026-05-12  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.10501v1  

#### Abstract
Compound LLM training workloads-such as knowledge distillation and multimodal LLM (MLLM) training-are gaining prominence. These typically comprise heterogeneous components differing in parameter scale, execution mode (forward-only or full forward-backward), and sequence length. Besides, component ac...

---

### 27. [DataArc-SynData-Toolkit: A Unified Closed-Loop Framework for Multi-Path, Multimodal, and Multilingual Data Synthesis](https://arxiv.org/abs/2605.08138)

**Authors**: Zhichao Shi, Cehao Yang, Hao Zhou, Xiaojun Wu, Huajie Li, Xuhui Jiang, Chengjin Xu, Yuanzhuo Wang, Jian Guo  
**Category**: cs.LG  
**Published**: 2026-05-12  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.08138v1  

#### Abstract
Synthetic data has emerged as a crucial solution to the data scarcity bottleneck in large language models (LLMs), particularly for specialized domains and low-resource languages. However, the broader adoption of existing synthetic data tools is severely hindered by convoluted workflows, fragmented d...

---

### 28. [ReLibra: Routing-Replay-Guided Load Balancing for MoE Training in Reinforcement Learning](https://arxiv.org/abs/2605.08639)

**Authors**: Chao Jin, Xinming Wei, Yinmin Zhong, Chengxu Yang, Bingyang Wu, Ruidong Zhu, Zili Zhang, Yuliang Liu, Xin Jin  
**Category**: cs.LG  
**Published**: 2026-05-12  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.08639v1  

#### Abstract
Load imbalance is a long-standing challenge in Mixture-of-Experts (MoE) training and is exacerbated in reinforcement learning (RL) for LLMs, where hot experts can shift frequently across micro-batches. Existing MoE training systems rely on historical loads to predict future expert demand, making the...

---

### 29. [Discovery of Nonlinear Dynamics with Automated Basis Function Generation](https://arxiv.org/abs/2605.09696)

**Authors**: Mohammad Amin Basiri, Charles Nicholson  
**Category**: cs.LG  
**Published**: 2026-05-12  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.09696v1  

#### Abstract
Discovering governing equations from observational data remains a fundamental challenge in scientific modeling, particularly when the underlying mathematical structure is unknown. Traditional sparse identification methods like SINDy excel at discovering parsimonious models but require researchers to...

---

### 30. [Locking Pretrained Weights via Deep Low-Rank Residual Distillation](https://arxiv.org/abs/2605.10777)

**Authors**: Keitaro Sakamoto, Pierre Ablin, Federico Danieli, Marco Cuturi  
**Category**: cs.LG  
**Published**: 2026-05-12  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.10777v1  

#### Abstract
The quality of open-weight language models has dramatically improved in recent years. Sharing weights greatly facilitates model adoption by enabling their use across diverse hardware and software platforms. They also allow for more open research and testing, to the extent that users can use them as ...

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
