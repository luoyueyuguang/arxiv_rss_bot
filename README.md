# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-06-05 09:03:42 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG

## 📚 Recent Papers

### 1. [YouZhi: Towards High-Concurrency Financial LLMs via Adaptive GQA-to-MLA Transition](https://arxiv.org/abs/2606.05868)

**Authors**: PSBC LLM Team,  Huawei LLM Team, Ruihan Long, Junjie Wu, Tianan Zhang, Duo Zhang, Yaozong Wu, Jinbin Fu, Chang Liu, Zhentao Tang, Wenshuang Yang, Xin Wang, Zhihao Song, Ning Huang, Wenjing Xu, Shuai Zong, Shupei Sun, Sen Wang, Jing Hu, Bin Wang, Xinyu Wang, Junkui Ju, Zequn Ding, Jie Ran, Man Luo, Shixiong Kai, Linkai Hou, Kaichao Liang, Hu Zhao, Yang Zhao, Shucheng Lin, Wei Yu, Chenghan Jiang, Jingjing Ding, Jiahui Zhang, Tian Jin, Yuhang Zhang, Dong Guo, Wei Sun, Jun Xie, Jianwei Li, Lei Cao, Pei Li, Jiabin Li, Jia Yuan, Rui Yuan, Jing Zhu, Mingxuan Yuan, Zhangcheng Lv, Xin Jiang, Xiuhong Fei, Xiaozhe Ren, Yulong Li, Zhipeng Zhang, Hang Wang, Zhaohui Xu, Rui Zhao, Yibo He, Xinzhuang Niu  
**Category**: cs.CL  
**Published**: 2026-06-05  
**Score**: 12.5  
**Type**: new  
**ArXiv ID**: 2606.05868v1  

#### Abstract
Large language models (LLMs) drive significant financial innovations, yet their high-concurrency deployment is severely bottlenecked by KV cache memory overhead, which inflates infrastructure costs and throttles scalability. To address this, we propose YouZhi-LLM, a highly efficient financial LLM em...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：YouZhi: Towards High-Concurrency Financial LLMs via Adaptive GQA-to-MLA Transition

---

## 1. 论文的主要贡献和创新点

### 解决的问题
当前金融领域的大语言模型（LLMs）在高并发部署场景下面临严重瓶颈，尤其是由 **KV Cache 内存开销** 导致的推理延迟高、吞吐量低、硬件成本高昂。尽管已有金融专用模型（如 BloombergGPT、FinGPT、YiZhao-12B-Chat 等）通过领域预训练提升了金融理解能力，但它们大多沿用标准的 **Grouped-Query Attention (GQA)** 或 **Multi-Head Attention (MHA)** 架构，未从根本上解决 KV Cache 膨胀问题。

此外，现有研究往往将模型能力提升与服务效率视为独立目标，导致在真实生产环境中难以实现“高准确率”与“高并发”的平衡。

### 提出的新方法与新思路
为解决上述问题，本文提出 **YouZhi-LLM**，其核心是构建一个面向高并发金融应用的高效 LLM 框架，包含两大创新：

#### （1）层自适应 GQA-to-MLA 转换算法（Layer-Adaptive GQA2MLA Transition）
- 将现有的 GQA 模型转换为更高效的 **Multi-Head Latent Attention (MLA)** 架构，以大幅压缩 KV Cache。
- 创新地引入 **层自适应 FreqFold 大小选择机制**：不同于 TransMLA 等方法对所有层使用统一的 FreqFold 参数，YouZhi 发现不同网络层对结构变化的敏感度差异显著——浅层适合较大 FreqFold（利于主成分集中），深层则需较小 FreqFold（避免 RoPE 频率近似误差放大）。
- 提出一种分步优化策略，将组合优化问题转化为多轮序列决策过程，在每一步中独立优化单个层的 FreqFold 大小，从而在可接受计算复杂度下逼近全局最优解。

#### （2）面向 MLA 结构的完整后训练流水线（Post-Training Pipeline）
- **阶段一：广义知识蒸馏（Generalized Knowledge Distillation, GKD）**  
  使用原始 GQA 模型作为教师模型，恢复因架构转换而损失的语言建模能力。
- **阶段二：金融领域监督微调（Financial Domain-Specific SFT）**  
  构建高质量、多源融合的金融指令数据集（97万条），注入领域专业知识。
- 数据构造方面提出：
  - 分层数据压缩（Stratified Compression）：按类别、质量、难度三级过滤，保障多样性与代表性；
  - 缺失领域增强（Augmentation for Missing Domains）：基于 DecIF 元分解生成多样化 persona 和任务；
  - 拒绝响应数据构建（Refusal Data Construction）：结合逻辑树剪枝（TreeCut）与 LLM 表达生成，提升合规性；
  - 特定能力数据增强（Self-Instruct + Evol-Instruct）：从少量种子样本扩增特定金融技能（如大小写金额转换）的数据。

### 相比现有方法的优势
| 维度 | 现有方法（如 BloombergGPT, FinGPT） | YouZhi |
|------|------------------------------------|--------|
| 架构效率 | 使用 GQA/MHA，KV Cache 大 | 引入 MLA，KV Cache 显著降低 |
| 结构转换策略 | 固定参数或全模型统一转换 | 层自适应动态调整 FreqFold |
| 后训练设计 | 单一 SFT 或 LoRA 微调 | 双阶段系统化恢复 + 增强 |
| 部署适配性 | 通用推理框架 | 原生集成华为 Ascend + vLLM-Ascend |

> ✅ **优势总结**：YouZhi 实现了“能力不降反升”与“部署效率飞跃”的双重突破，首次在金融 LLM 中达成准确率与并发性的帕累托前沿（见图1）。

---

## 2. 核心实验方法和设置

### 使用的数据集

#### 语言建模评估
- **WikiText-2**：用于评估 perplexity，衡量基础语言建模能力退化情况。

#### 下游任务评估
##### 通用基准（General Benchmarks）
- C-Eval、IFEval、MATH-500、LiveCodeBench (LCB)、HellaSwag (H-Swag)、SST-5、CrossNER

##### 金融领域基准（Financial Benchmarks）
- CFLUE-K/A、FinanceIQ、FinEval、OpenFinData、FPB

##### 真实应用场景
- 移动银行内部数据集：涵盖意图识别（L1/L2 控制器）、槽位填充等六项关键任务。

### 实验设置和评估指标

| 类别 | 设置说明 |
|------|----------|
| **硬件平台** | Huawei Ascend A3 集群 |
| **基础模型** | OpenPangu-7B、Qwen2.5-14B-Instruct 等官方 ModelScope GQA 检查点 |
| **转换配置** | Partial RoPE dimension = 64, KV-LoRA rank = 512 |
| **最终模型** | YouZhi-7B（源自 OpenPangu-7B）、YouZhi-14B（源自 Qwen2.5-14B-Instruct） |
| **推理框架** | vLLM-Ascend（专为 Ascend NPU 优化的 vLLM 分支） |
| **评估指标** | 
| - Perplexity（越低越好） | WikiText-2 上的语言建模性能 |
| - Average Score（越高越好） | 多个 benchmark 的平均得分 |
| - Max Concurrent Requests（越高越好） | 单芯片最大并发请求数 |
| - Throughput (tokens/s) | 总吞吐量 |
| - KV Cache Size | KV 缓存元素数量 |

### 基线方法对比
| 基线类型 | 对比对象 |
|--------|---------|
| **结构转换基线** | TransMLA（统一 FreqFold）、MHA2MLA |
| **金融模型基线** | YiZhao-12B-Chat、DianJin-R1-7B、Qwen3-8B、Qwen3.5-9B |
| **基础模型** | OpenPangu-7B、Qwen2.5-14B-Instruct |

---

## 3. 主要实验结果和性能指标

### 关键性能数据

#### （1）语言建模能力保留（Table 1 & Figure 9）
| 模型 | Orig. PPL | TransMLA PPL | L-Adap. PPL | △PPL Reduction |
|------|-----------|---------------|--------------|----------------|
| Llama3-8B | 6.1 | 25.8 | 12.9 | **-65%** |
| OpenPangu-7B | 14.1 | 50.3 | 37.6 | **-35%** |
| Qwen2.5-7B | 6.8 | 8.4 | 8.3 | -6% |

> 🔍 **发现**：YouZhi 的层自适应算法在多个主流 LLM 上均显著优于 TransMLA，在 Llama3-8B 上甚至减少 **65% 的困惑度退化**。

#### （2）下游任务表现（Table 2 & Table 3）

##### 金融领域平均得分
| 模型 | 平均分数 |
|------|--------|
| YiZhao-12B-Chat | 69.7 |
| DianJin-R1-7B | 69.8 |
| Qwen3.5-9B | 73.1 |
| **YouZhi-7B** | **74.1** |
| **YouZhi-14B** | **78.8** ✅ |

> 📈 YouZhi-14B 在金融 benchmark 上达到 **78.8**，远超现有开源及闭源金融模型。

##### 通用任务保持能力
| 模型 | 平均分数 |
|------|--------|
| OpenPangu-7B | 62.4 |
| Qwen2.5-14B-Instruct | 65.8 |
| **YouZhi-7B** | **66.8** |
| **YouZhi-14B** | **68.0** |

> ✅ 架构转换后仍能维持甚至超越原模型的通用能力。

#### （3）高并发服务能力（Table 4）

| 模型 | Max Concurrent | 提升倍数 | KV Cache Size | Throughput |
|------|----------------|----------|----------------|------------|
| OpenPangu-7B | 95 | 1.00× | 2048 | 3325 tokens/s |
| **YouZhi-7B** | **256** | **2.69×** | **576 (-72%)** | **5865 tokens/s (+1.76×)** |
| Qwen2.5-14B-Instruct | 55 | 1.00× | 2048 | 1740 tokens/s |
| **YouZhi-14B** | **134** | **2.43×** | **576 (-72%)** | **2990 tokens/s (+1.71×)** |

> ⚡️ **核心成果**：KV Cache 减少 **72%**，最大并发请求提升 **2.43~2.69 倍**，直接支撑高流量移动银行服务。

#### （4）真实场景表现（Table 5）
在移动银行六项任务中，YouZhi-7B 与原模型性能持平：
- 意图识别平均准确率：**97.73%**
- 槽位填充平均准确率：**99.05%**

表明模型在实际业务中具备可靠性和稳定性。

### 消融实验结果
- **逐层转换分析（Figure 4）**：验证了浅层偏好大 FreqFold（如8），中深层偏好小 FreqFold（如1），证明层间异质性存在。
- **渐进式转换曲线（Figure 9）**：随着更多层被转换，YouZhi 的层自适应方案始终优于 TransMLA，尤其在前几层差距最大，说明浅层优化收益最高。
- **两阶段训练有效性**：消融显示，仅做 SFT 会导致通用能力下降；加入 GKD 后可有效恢复基础能力，再经 SFT 注入金融知识，实现双赢。

---

## 4. 关键结论和发现

### 主要发现
1. **GQA-to-MLA 转换具有明显的层特异性**：不能采用“一刀切”的 FreqFold 策略，必须进行层自适应优化。
2. **YouZhi 的层自适应算法显著降低 perplexity 退化**，相比统一转换最多减少 **65% 的性能损失**。
3. **MLA 架构带来巨大部署优势**：KV Cache 减少 **72%**，最大并发提升 **2.43~2.69 倍**，极大降低服务成本。
4. **系统化后训练可完全恢复并增强能力**：通过 GKD + SFT 流水线，不仅弥补了架构转换带来的能力损失，还在金融任务上取得 **+7.0% ~ +13.6%** 的增益。
5. **YouZhi 模型位于准确率-效率帕累托前沿**（见图1），实现了“既快又准”。

### 方法的局限性
- **依赖特定硬件生态**：目前深度集成于 **Huawei Ascend** 生态，跨平台迁移可能受限。
- **MLA 算子支持有限**：虽已在 vLLM-Ascend 实现，但在其他推理框架中尚不普及。
- **FreqFold 参数搜索仍需人工干预**：虽然提出自动化选择机制，但初始候选集和超参仍需经验设定。
- **金融数据覆盖仍有边界**：尽管做了增强，某些极端合规或跨境金融场景仍可能存在盲区。

### 未来工作方向
1. **扩展至 MoE 架构**：探索 MLA 与 Mixture-of-Experts 的结合，进一步提升稀疏化效率。
2. **全自动层自适应搜索**：引入强化学习或 NAS 技术自动发现最优 FreqFold 分布。
3. **跨模态金融助手**：将 YouZhi 扩展至支持表格、图表、语音等多模态输入。
4. **开放更多轻量化版本**：发布 YouZhi-1.8B / 4B 等小型模型，推动普惠金融 AI 应用。
5. **构建金融安全护栏体系**：加强拒绝响应、风险预警、审计追踪等合规模块。

---

> ✅ **总体评价**：YouZhi 是首个将 **架构创新**、**训练工程** 与 **硬件部署** 深度协同的金融 LLM 系统性解决方案，标志着金融大模型从“追求精度”迈向“兼顾效率与落地”的新时代。

</details>

---

### 2. [SET: Stream-Event-Triggered Scheduling for Efficient CUDA Graph Pipelines](https://arxiv.org/abs/2606.05495)

**Authors**: Zhengxiong Li, Tsung-Wei Huang, Umit Ogras  
**Category**: cs.DC  
**Published**: 2026-06-05  
**Score**: 12.0  
**Type**: new  
**ArXiv ID**: 2606.05495v1  

#### Abstract
Achieving peak GPU performance remains a significant challenge as the system throughput is constrained by host-device synchronization delays and kernel scheduling overheads, even with aggressive kernel optimizations and batch processing. Furthermore, existing approaches often underutilize hardware r...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：SET: Stream-Event-Triggered Scheduling for Efficient CUDA Graph Pipelines

---

## 1. 论文的主要贡献和创新点

### 解决的问题
现代 GPU 应用（如 AI、科学计算）通常以**任务并行流水线**的形式执行，依赖大量 kernel 启动和内存拷贝操作。尽管已有 **CUDA Graph** 技术用于减少 CPU 端的启动开销，但在实际运行中仍存在显著的性能瓶颈：

- **Kernel gaps**：GPU 时间线上连续 kernel 之间存在空闲间隔（idle intervals），导致硬件利用率不足。
- **Host-device synchronization overheads**：主机端频繁进行同步、参数更新、stream 分配等操作，造成调度延迟。
- **资源利用不充分**：copy engines 和 compute cores 经常处于闲置状态，尤其在小 kernel 或高内存压力场景下。

现有方法（如静态 batching、queue-based 调度）无法有效应对这些细粒度的就绪事件，且容易引入额外的数据竞争或全局锁争用。

---

### 提出的新方法与创新思路

本文提出 **SET (Stream-Event-Triggered Scheduling)** ——一种面向 CUDA Graph 的高效运行时调度框架，其核心创新包括：

#### （1）**Event-chained host-device co-scheduling**
- 利用 **CUDA event callbacks** 实现异步资源释放：每当一个 worker 完成任务后，自动触发 callback 将其返回到可用 worker pool。
- 实现 **O(1) 同步开销**，避免轮询或阻塞等待，显著降低 host-side 调度延迟。

#### （2）**多流任务并行编程模型 + 工作窃取机制（work-stealing）**
- 每个 worker 对应独立的 CUDA stream、graph executable 和设备缓冲区（Mi），实现内存隔离。
- 引入 per-worker job queue，dispatcher 动态从本地队列取任务；若为空，则尝试“偷”其他队列的任务。
- 支持 **runtime 参数更新** 和 **JIT 图重绑定（just-in-time rebinding）**，确保 stolen job 可安全运行于目标 worker 的内存空间。

#### （3）**基于图的执行流与每流缓冲区设计**
- 使用可复用的 CUDA graph executables 表示每个 job。
- 预分配固定数量的内存 slot（batch size 级别），支持跨批次重用，避免频繁内存分配。
- 保证 **memory safety** 与 **per-job ordering**。

---

### 相比现有方法的优势

| 特性 | SET | Static Batching | Queue Model | CUDA Graph |
|------|-----|------------------|-------------|------------|
| 调度粒度 | 细粒度（per-stream completion） | 粗粒度（batch-level sync） | 中等（共享队列） | 单 stream / 固定 graph |
| 同步开销 | O(1)，event-driven | 高（batch 结束同步） | O(b)，需查询共享队列 | 每次 replay 参数更新 |
| 内存安全性 | ✅（隔离 buffer + JIT rebind） | ✅ | ❌（共享 buffer 易冲突） | ✅ |
| 支持动态参数更新 | ✅（placeholder + JIT） | ⚠️（有限支持） | ✅ | ✅ |
| 小 kernel 性能 | 优秀 | 差 | 差（mutex 开销大） | 差 |
| 硬件利用率 | 高（持续重叠 H2D/D2H/kernels） | 中等 | 中等 | 低 |

> ✅ SET 在保持兼容性的同时，实现了更高的吞吐量、更低的调度开销，并能适应多样化的 workload 特征。

---

## 2. 核心实验方法和设置

### 使用的工作负载（Workloads）
共评估了 **6 个代表性真实世界 workload**，涵盖 compute-bound 与 memory-bound 场景：

| Workload | 类型 | 描述 |
|---------|------|------|
| **Sobel** | Image Processing | 图像边缘检测，含多个小 kernel |
| **GEMM** | Compute-bound | 分块稠密矩阵乘法 |
| **Back Propagation (BP)** | ML Training | 单层神经网络反向传播 |
| **KNN** | Memory-bound | 暴力搜索最近邻，kernel 极短 (~10μs) |
| **Hotspot** | Memory-bound | 热仿真求解微分方程，极高 DRAM 带宽占用 |
| **SSSP** | Graph Algorithm | 单源最短路径（Bellman-Ford 变种） |

> 如 Fig. 4 所示，这些 workload 具有广泛的任务长度分布（从 μs 到 ms）和内存访问模式差异。

---

### 实验设置

| 项目 | 配置 |
|------|------|
| **硬件平台** | - Server 1: Intel Xeon Gold 6330 + **RTX 3090** (Ampere)<br>- Server 2: Intel i7-11700 + **RTX 5090** (Blackwell)<br>- CUDA v12.8, Ubuntu 22.04 |
| **编译选项** | `gcc -O2`, C++20 |
| **评估工具** | NVIDIA Nsight Systems Profiler（分析 kernel gaps、timeline、bandwidth usage） |

---

### 评估指标

- **主性能指标**：
  - **Throughput**（单位：img/ms, GFLOPs, tasks/s 等）
- **关键辅助指标**：
  - **Scheduling Overhead (%)** = $ \frac{T_{\text{schedule}}}{T_{\text{measured}}} $
    - 包括 intra-batch 与 inter-batch 开销（见 Eq. 4）
  - **Kernel Gap 分析**：Nsight 中白空间占比
  - **Memory Utilization**：L2/DRAM 带宽使用率

---

### 基线方法对比

对比了 **5 种主流编程模型**：

1. **Synchronous Model**：单 stream 顺序 launch，无优化
2. **Graph Model**：预实例化 CUDA Graph，重复 replay
3. **Static Batching Model**：将多个 job 打包为一个大 graph，batch 级同步
4. **Queue Model**：使用共享 job queue + 多 worker 动态调度
5. **SET (Ours)**：所提 event-triggered + work-stealing 框架

所有 baseline 均采用最佳实践实现，确保公平比较。

---

## 3. 主要实验结果和性能指标

### 关键性能数据汇总（来自 Table 1）

| Workload | Speedup vs Synchronous | vs Graph | vs Batching | vs Queue |
|---------|------------------------|----------|--------------|-----------|
| Sobel   | 2.99× (Ampere) / 1.86× (Blackwell) | ~2.9×     | ~1.17×       | ~1.15×      |
| SSSP    | 2.45× / 3.07×           | ~2.4×     | ~1.11×       | ~1.06×      |
| BP      | 2.34× / 2.78×           | ~2.5×     | ~1.07×       | ~1.01×      |
| GEMM    | 1.58× / 1.39×           | ~1.48×    | ~1.07×       | ~1.01×      |
| KNN     | 2.47× / 2.63×           | ~2.1×     | ~1.15×       | **2.94× / 2.09×** |
| Hotspot | 1.10× / 1.47×           | ~1.4×     | ~1.42×       | ~1.6×       |
| **Average** | **2.15× / 2.20×**       | **2.12× / 2.08×** | **1.18× / 1.15×** | **1.44× / 1.34×** |

> ✅ SET 在 **平均 1.15–1.44× 超越最优 baseline**，最高达 **2.94×**（KNN 上超越 Queue Model）

---

### 调度开销降低效果（Table 2 & Fig. 6）

| 方法 | Avg. Scheduling Overhead (RTX 3090) | Reduction vs Batching | vs Queue |
|------|-------------------------------|--------------------------|---------|
| Batching Model | 45.32% | — | — |
| Queue Model    | 33.36% | — | — |
| **SET**        | **29.83%** | ↓ **54.64%** | ↓ **18.62%** |

- 在 batch size 较小时，三者 overhead 都较高（~45–50%），因硬件未饱和。
- 随着 batch size 增加，SET 的优势显现：
  - Batching 模型出现 **U-shaped overhead 曲线**，因 inter-batch synchronization 导致后期开销回升。
  - Queue 模型因全局 mutex 争用，在大 batch 下性能下降明显（up to 54% overhead）。
  - SET 凭借 per-worker queue 和 event-driven 回收机制，维持最低开销。

> 🔍 **Amdahl’s Law 观察**：随着 Blackwell 架构提升 compute throughput（平均 1.79× faster），调度开销成为更明显的瓶颈 → SET 的价值进一步凸显。

---

### 消融实验与关键观察（隐含分析）

虽然未明确列出消融实验表格，但从设计组件可推断以下关键因素的作用：

| 组件 | 贡献说明 |
|------|--------|
| **Per-worker queues** | 消除共享队列的 mutex 争用，特别利于 KNN 这类高频小任务 |
| **Event callbacks** | 实现 O(1) worker 回收，避免 polling，减少 inter-kernel gaps |
| **Work-stealing + JIT rebind** | 提高负载均衡能力，同时保障 memory safety |
| **Bounded in-flight graphs** | 控制内存使用，允许 runtime 参数更新而不破坏 graph 结构 |

> 💡 在 KNN 和 Hotspot 等极端 workload 上的表现证明了各模块协同的有效性。

---

## 4. 关键结论和发现

### 主要发现

1. **Kernel gaps 是制约 CUDA Graph 性能的关键瓶颈**  
   即使使用 graph replay，intra-batch 与 inter-batch 的调度延迟仍占总时间高达 45% 以上。

2. **传统 batching 方法存在“过犹不及”问题**  
   批处理虽摊薄启动开销，但加剧了 inter-batch 同步成本，反而在大 batch 下性能下降。

3. **SET 实现了真正的细粒度 event-driven 调度**  
   通过 event chaining 与 work-stealing，SET 成功将调度决策推迟到 runtime，并响应 per-stream completion 事件，最大化硬件重叠。

4. **SET 在多样化 workload 上表现稳健**  
   不仅在 compute-heavy（GEMM）上提升明显，在 memory-heavy（Hotspot）和 micro-kernel（KNN）场景也优于所有 baseline。

5. **现代 GPU 架构越来越受调度限制**  
   随着 Blackwell 等新一代 GPU 提升 raw compute 能力，host-side 调度开销成为新的性能墙（bottleneck amplification）。

---

### 方法的局限性

- **依赖 CUDA event callback 机制**：仅适用于支持异步回调的平台。
- **需要预先确定 batch size 和 worker 数量**：动态扩展能力受限。
- **对 highly irregular control flow 支持有限**：假设 DAG 结构相对稳定。
- **未集成 compiler-level fusion 优化**：属于 runtime 层方案，可与其他技术正交结合。

---

### 未来工作方向

1. **与 DSL 编译器（如 TorchDynamo、MLIR）集成**，实现 compile-time graph fusion + runtime SET 调度联合优化。
2. **支持动态 worker 扩展**，适应 runtime workload 变化。
3. **扩展至 multi-GPU 场景**，利用 NCCL + event chaining 实现跨设备流水线。
4. **探索 predictive scheduling**：基于历史执行时间预测最优 dispatch 时机，进一步压缩 gaps。

---

## 总结

✅ **SET 是首个将 event-driven、work-stealing 与 CUDA Graph 相结合的 runtime 框架**，解决了长期存在的 kernel gaps 和调度开销问题。其实验结果显示：

- 平均 **1.15–1.44× 超越 state-of-the-art baseline**
- 调度开销降低 **18–54%**
- 在小 kernel（KNN）、高带宽（Hotspot）等挑战性场景下表现尤为突出

📌 该工作揭示了一个重要趋势：**未来的 GPU 性能突破不仅来自 kernel 优化，更取决于高效的 runtime 调度机制**。SET 为此提供了坚实的基础架构和设计范式。

</details>

---

### 3. [AgentJet: A Flexible Swarm Training Framework for Agentic Reinforcement Learning](https://arxiv.org/abs/2606.04484)

**Authors**: Qingxu Fu, Boyin Liu, Shuchang Tao, Zhaoyang Liu, Bolin Ding  
**Category**: cs.AI  
**Published**: 2026-06-05  
**Score**: 11.5  
**Type**: new  
**ArXiv ID**: 2606.04484v1  

#### Abstract
We present AgentJet, a distributed swarm training framework for large language model (LLM) agent reinforcement learning. Unlike centralized frameworks that tightly couple agent rollouts with model optimization, AgentJet adopts a decoupled multi-node architecture in which swarm server nodes host trai...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：AgentJet: A Flexible Swarm Training Framework for Agentic Reinforcement Learning

---

## 1. 论文的主要贡献和创新点

### **解决了什么问题**

当前主流的 LLM 强化学习（RL）训练框架（如 OpenRLHF、veRL）在处理 **agentic RL**（代理型强化学习）任务时存在以下关键瓶颈：

- **运行时脆弱性（Runtime Fragility）**：训练与推理耦合紧密，外部环境（如浏览器、代码沙箱、API）崩溃会导致整个训练中断。
- **调试摩擦大（Debugging Friction）**：修改 agent 逻辑或 reward 函数需重启整个训练流程，迭代周期长达 5–10 分钟。
- **多模型支持不足**：难以训练异构多智能体系统（heterogeneous multi-agent），即不同 agent 使用不同大小或架构的 LLM。
- **冗余上下文开销**：多轮交互中重复的 system prompt、tool definition 等导致训练计算浪费。
- **多任务训练隔离困难**：混合训练多个依赖冲突的任务（如 AppWorld 和数学推理）时，单体架构难以提供强隔离。

### **提出了什么新方法或新思路**

提出 **AgentJet** —— 一种基于 **swarm 架构** 的分布式 agentic RL 训练框架，其核心创新是 **完全解耦训练与推理平面**，通过 **client-server 范式** 实现灵活、容错、高效的训练。

#### 主要设计思想：

- **Swarm 架构**：
  - **Swarm Server（优化节点）**：部署在 GPU 集群上，负责模型存储、梯度更新、vLLM/SGLang 推理服务。
  - **Swarm Client（采样节点）**：轻量级 CPU 进程，可在任意设备运行，执行 agent 工作流、调用工具、计算 reward。
  - 两者通过 OpenAI 兼容接口通信，实现 **many-to-many 拓扑**，支持动态加入/退出。

- **Timeline Merging 上下文压缩算法**：
  - 自动合并多轮对话中的冗余上下文（如重复的 system prompt、tool schema）。
  - 支持 **token-level** 和 **text-level** 匹配策略，平衡训练效率与推理一致性。

- **自动化研究系统（A3R, Alpha Auto Research）**：
  - 利用 swarm 架构构建全自动科研流水线，支持多阶段自适应实验设计、并行调度、故障恢复。

### **相比现有方法的优势**

| 特性 | AgentJet | 传统框架（如 OpenRLHF） |
|------|---------|------------------------|
| **容错性** | ✅ 客户端失败不影响服务器训练 | ❌ 单点故障导致全盘崩溃 |
| **调试灵活性** | ✅ 热插拔修改 agent 代码（秒级） | ❌ 修改需重启训练（分钟级） |
| **多模型支持** | ✅ 支持非共享参数的异构多模型训练 | ❌ 多数仅支持单一策略模型 |
| **多任务训练** | ✅ 支持“鸡尾酒训练”（cocktail training） | ❌ 难以隔离冲突依赖 |
| **框架兼容性** | ✅ 支持 LangChain、AgentScope、Raw HTTP 等任意 agent 框架 | ❌ 通常绑定特定 agent 库 |
| **训练效率** | ✅ Timeline Merging 加速 1.5–10× | ❌ 无上下文压缩机制 |

---

## 2. 核心实验方法和设置

### **使用的数据集**

- **Werewolves RPG 游戏**：社交推理游戏，用于测试多智能体协作与对抗能力。
- **AppWorld**：交互式编码基准，模拟真实数字任务（如邮件管理、音乐播放器控制）。
- **AIME 数学推理**：自动化的数学问题求解任务，用于测试符号推理能力。
- **DAPO-Math-17k**：大规模数学训练数据集，用于 GRPO 算法训练。
- **自建“Who is the Spy”游戏数据**：由 vibe training 自动生成的模拟数据。

### **实验设置和评估指标**

| 实验类型 | 设置 | 评估指标 |
|--------|------|----------|
| **多智能体训练** | Werewolves 游戏，3×3×1×1×1 配置（狼人/村民/预言家/女巫/猎人） | 成功率（Success Rate, SR） |
| **异构多模型训练** | 不同角色使用独立 LoRA 模型（14B-LoRA） | 最终成功率提升 |
| **鸡尾酒训练（Cocktail Training）** | AppWorld + AIME 混合训练，batch 16+16 | 各任务单独奖励曲线 |
| **Timeline Merging 效果** | AppWorld 多轮任务，启用/禁用 merging | actor-update wall time、LLM 调用次数、reward 曲线 |
| **自动化研究（A3R）** | 自主探索最小稳定 batch size | pass@1、pass@2、mean reward |

### **基线方法对比**

- **Separate Training**：AppWorld 和 AIME 各自独立训练，batch 32。
- **Shared-parameter MARL**：所有 agent 共享同一模型参数。
- **No Timeline Merging**：直接对比上下文压缩前后的训练速度。
- **Manual Research Workflow**：对比人工设计实验 vs A3R 自动化流程。

---

## 3. 主要实验结果和性能指标

### **关键性能数据**

#### （1）Timeline Merging 加速效果（AppWorld）
| 指标 | 无 merging | 有 merging | 提升倍数 |
|------|----------|-----------|---------|
| 平均 actor-update 时间 | 2160 ± 171 秒 | 346 ± 13 秒 | **6.25×** |
| LLM 调用次数/步 | 12.6 ± 1.0 | 11.4 ± 0.7 | ≈10% 减少 |
| 最终 reward | 0.30 | 0.30 | 无损失 |

✅ **结论**：上下文压缩带来显著加速，且不损害训练质量。

#### （2）Werewolves 多智能体训练结果（共享参数）

| 实验 | 可训练角色 | 初始 SR | 最终 SR | 提升 |
|------|------------|--------|--------|------|
| Exp 1 | WW (7B) | 23.0% | 47.2% | +24.2% |
| Exp 2 | WW (14B) | 40.9% | 64.7% | +23.8% |
| Exp 7 | vl/sr/wt/ht (14B) | 23.9% | 41.6% | +17.7% |

✅ **结论**：即使面对 235B 静态对手，小模型也能通过 RL 显著提升表现。

#### （3）异构多模型训练 vs 共享参数

| 配置 | 最终 SR | 优势分析 |
|------|--------|----------|
| 共享参数（3×WW, 14B） | 64.7% | 行为模式趋同，易被识别 |
| 独立参数（3×WW, 各 14B-LoRA） | **66.5%** | 行为更多样，欺骗性更强 |

✅ **结论**：非共享参数训练在社交游戏中更具优势，提升 **1.8%**。

#### （4）鸡尾酒训练 vs 独立训练

| 任务 | 鸡尾酒训练（混合） | 独立训练 | 差距 |
|------|------------------|----------|------|
| AIME | 0.72 | 0.73 | -0.01 |
| AppWorld | 0.58 | 0.68 | -0.10 |

⚠️ **结论**：AppWorld 性能下降明显，因其长工具链轨迹易被短任务稀释；但 **鸡尾酒训练节省了 N 倍训练成本**，适合构建通用 agent。

#### （5）自动化研究（A3R）结果：最小稳定 batch size

| 参数组合 | pass@1 | pass@2 | mean reward |
|--------|--------|--------|-------------|
| bs=16, mr=10000 | 53.33% | 73.33% | 0.5333 |
| bs=16, mr=12000 | **60.00%** | **73.33%** | **0.6000** |

✅ **最终推荐配置**：
- **性价比最高**：`bs=4, mr=12000`
- **性能最优**：`bs=16, mr=12000`

---

## 4. 关键结论和发现

### **主要发现**

1. **Swarm 架构显著提升 agentic RL 的工程鲁棒性**：
   - 客户端崩溃不影响训练进程，支持热替换、热调试。
   - 实现真正的 **fault-tolerant** 和 **live code iteration**。

2. **异构多模型训练优于共享参数**：
   - 在需要行为多样性的任务（如社交游戏）中，独立参数训练能避免模式趋同，提升欺骗性和团队协作效率。

3. **Timeline Merging 是高效多轮训练的关键**：
   - 可实现 **1.5–10× 训练加速**，尤其适用于长上下文、多轮交互场景。

4. **鸡尾酒训练是低成本构建通用 agent 的有效路径**：
   - 虽然单任务性能略低于专用训练，但 **避免了 N+1 的 distillation 流程**，大幅降低总成本。

5. **自动化研究系统（A3R）可行且高效**：
   - 可自主完成超参搜索、消融实验、故障恢复，支持 **multi-day、multi-stage** 科研闭环。

### **方法的局限性**

- **鸡尾酒训练存在梯度稀释风险**：当任务长度差异过大（如 AppWorld vs AIME），短任务可能主导梯度更新。
- **Timeline Merging 可能影响 TI 一致性**：text-level merging 忽略 tokenization drift，在对推理一致性要求极高的场景需谨慎使用。
- **A3R 依赖高质量 prompt 和 agent 能力**：若 leader agent 规划能力弱，可能导致实验设计不合理。

### **未来工作方向**

- **更智能的混合训练调度器**：动态调整各任务的 rollout 预算，避免梯度失衡。
- **跨客户端协同训练机制**：支持更复杂的 multi-agent 协议（如通信、协商）。
- **集成更多 RL 算法**：扩展对 DPO、KTO、ReST 等 offline RL 方法的支持。
- **构建开放的自动化科研平台**：将 A3R 开源，推动 AI 自主科研生态发展。

---

> 🔗 **开源地址**：[https://github.com/modelscope/AgentJet](https://github.com/modelscope/AgentJet)  
> 🌐 **在线评测平台**：[https://benchmark.agentjet.top](https://benchmark.agentjet.top)

</details>

---

### 4. [You Only Index Once: Cross-Layer Sparse Attention with Shared Routing](https://arxiv.org/abs/2606.06467)

**Authors**: Yutao Sun, Yanqi Zhang, Li Dong, Jianyong Wang, Furu Wei  
**Category**: cs.CL  
**Published**: 2026-06-05  
**Score**: 11.0  
**Type**: new  
**ArXiv ID**: 2606.06467v1  

#### Abstract
Long-context inference in modern LLMs is increasingly constrained by decoding efficiency, especially in reasoning-heavy settings where models generate long intermediate chains of thought. Existing sparse attention methods often face a practical efficiency-quality trade-off. Structured block sparse m...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：You Only Index Once: Cross-Layer Sparse Attention with Shared Routing

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
现代大语言模型（LLMs）在长上下文推理任务中面临**解码效率瓶颈**，尤其是在需要生成长链思维（chain-of-thought）的场景下。尽管已有稀疏注意力（sparse attention）方法尝试缓解计算开销，但普遍存在**效率与质量之间的权衡**：
- **Block-sparse attention** 虽然加速明显，但由于粗粒度选择导致显著的质量损失；
- **Token-sparse attention** 更精确，但每层都需要独立进行 top-k 路由（routing），该操作在 GPU 上不规则且昂贵，限制了端到端的加速效果。

此外，KV-cache 存储和 pre-filling 阶段也随上下文增长而成为瓶颈。

### 提出了什么新方法或新思路
本文提出 **Cross-Layer Sparse Attention (CLSA)**，其核心思想是将“共享”从 KV-cache 扩展到 **routing index**，即：
> **只索引一次，缓存一次（You Only Index Once, You Only Cache Once）**

具体设计基于 YOCO 架构（KV-sharing architecture），引入一个轻量级的 **query-aware indexer**，在 self-decoder 阶段为整个序列计算一次 token-level 的 top-k 路由索引，并在所有 cross-decoder 层之间**共享该索引**。

### 相比现有方法的优势
| 维度 | CLSA 的优势 |
|------|-------------|
| **效率** | 显著降低路由开销：top-k 只执行一次，避免逐层重复计算；同时继承 YOCO 在 pre-filling 和 KV-cache 上的优化。 |
| **质量** | 保留 token-sparse attention 的细粒度选择能力，相比 block-sparse 方法更准确。 |
| **系统级收益** | 同时改善三大推理瓶颈：prefill 时间、KV-cache 内存占用、解码延迟。 |

---

## 2. 核心实验方法和设置

### 使用了哪些数据集
- **通用基准测试**：
  - `BBH`（Big-Bench Hard）
  - `MMLU`（Massive Multitask Language Understanding）
  - `HellaSwag`, `WinoGrande`（常识推理）
  - `ARC-Challenge`, `DROP`（阅读理解与推理）
  - `GSM8K`（小学数学题）
  - `HumanEval`（代码生成）
- **长上下文合成任务**：
  - `RULER`：用于评估单针（single-needle）和多针（multi-needle）检索能力，在 16K 和 32K 上下文中测试。
- **语言建模验证集**：
  - `Books`, `ArXiv`, `StarCoder`：用于测量长上下文下的 perplexity（交叉熵损失）趋势。

### 实验设置和评估指标
- **模型规模**：4B 参数统一比较。
- **架构对比**：
  - `Transformer`（标准 dense baseline）
  - `YOCO (Dense)`（dense cross-attention + KV sharing）
  - `YOCO (CLSA)`（本文方法）
- **训练流程**：
  - 分两阶段 dense pretraining（最大长度 8K → 32K）
  - 两阶段 sparse adaptation（warm-up + joint fine-tuning with distillation loss）
- **评估指标**：
  - **任务性能**：准确率（accuracy）
  - **推理效率**：prefill / decode 吞吐量（tokens/s）、端到端生成吞吐量
  - **延迟分析**：每层 latency breakdown（MLP / Attention / Top-k）
  - **注意力稀疏性分析**：Attn. Coverage (%)、Cross-Entropy Loss

### 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| Transformer | Dense | 全注意力，无稀疏化 |
| YOCO (Dense) | KV-sharing | 共享 KV-cache，但 cross-attention 仍为 dense |
| DSA [22] | Dynamic Sparse Attention | 每层独立 token-level top-k |
| IndexCache [1] | Cross-layer Index Reuse | 每 4 层复用一次 index |
| HySparse [11] | Hybrid Sparse | 结合 block-sparse 与全局 attention |

---

## 3. 主要实验结果和性能指标

### 关键性能数据

#### ✅ 任务性能保持甚至提升（Table 2）
| Model | ARC-C | GSM8K | DROP | HumanEval |
|-------|--------|--------|--------|------------|
| Transformer | 0.453 | 0.434 | 0.366 | 0.384 |
| YOCO (Dense) | 0.461 | 0.430 | 0.387 | 0.396 |
| **YOCO (CLSA)** | **0.465** | **0.470** | **0.391** | **0.396** |

→ CLSA 在多个推理密集型任务上表现最佳，且整体能力分布接近 dense baseline。

#### ✅ 长上下文检索鲁棒性强（Table 3）
在 RULER 32K 上：
- CLSA 达到最高平均分，尤其在 **MK1/MK2 多针干扰任务**中表现最优。
- 单针检索性能保持近乎完美（~100%），说明稀疏选择未丢失关键信息。

#### ✅ 几乎无损的语言建模质量（Figure 2）
- 在 Books / ArXiv / StarCoder 上，CLSA 与 dense YOCO 的 validation loss 曲线几乎重合。
- 表明 CLSA 是 **effectively lossless** 的稀疏化策略。

#### ⚡️ 推理效率大幅提升（Figure 3 & Table 12）
在 **128K 上下文** 下：
| 指标 | 提升倍数 |
|------|--------|
| **Decode Throughput** | **7.6× vs Transformer** |
| **End-to-End Throughput** | **17.1× vs Transformer** |
| Prefill Throughput | ~20× 提升（得益于 YOCO 架构） |

#### 🔍 延迟分解显示路由摊销有效（Figure 5–6）
- 在 128K 上，传统 DSA 因频繁 top-k 导致 decode 比 dense Transformer 还慢；
- CLSA 将 **amortized top-k 成本降至 ~0.08ms/layer**，远低于 dense attention 开销（2.11ms）；
- 每层总延迟仅 0.31ms，显著优于其他稀疏方法。

#### 📊 注意力稀疏性分析（Table 4）
- 使用 **2048 个激活 token**（约占 1/16 上下文）即可覆盖约 80% 的 dense attention 质量。
- Cross-Entropy Loss 差异极小（Δ < 0.006），表明少量关键 token 足以维持高质量输出。

---

## 4. 关键结论和发现

### 论文的主要发现
1. **共享 routing index 是可行且高效的**：
   - 不同 decoder 层对重要 token 的关注具有一致性，支持跨层共享 index。
   - 多层蒸馏目标（multi-layer distillation）可有效训练 indexer 学习“共识性”显著 token。

2. **CLSA 实现了效率与质量的双赢**：
   - 在几乎所有下游任务上保持甚至超越 dense baseline 性能；
   - 同时解决 prefill、KV-cache、decode 三大瓶颈，达到全面加速。

3. **稀疏注意力的实际瓶颈在于 routing 开销而非 attention 本身**：
   - 如 Figure 4 所示，未摊销的 top-k 成本可与 dense attention 相当；
   - 只有通过 **amortization across layers** 才能使稀疏化真正带来 wall-clock 加速。

### 方法的局限性
- **依赖于 YOCO 架构**：必须采用 decoder-decoder 结构（self-decoder + cross-decoder），不适用于标准 autoregressive Transformer。
- **indexer 需额外训练**：需通过 distillation 进行 warm-up 和联合微调，增加训练复杂性。
- **固定激活数量**：当前实现使用固定 k=2048，可能无法动态适应不同输入难度。

### 未来工作方向
- 探索 **adaptive sparsity**：根据 query 动态调整 selected token 数量。
- 将 CLSA 思想推广至 **encoder-decoder 模型** 或 **vision-language 模型** 中的长序列处理。
- 结合 **Mamba / RetNet 等 State Space Models**，进一步替代部分 attention 层，构建更高效混合架构。
- 研究 **index compression 与传输优化**，在分布式推理中减少通信开销。

---

> **总结一句话**：  
> CLSA 通过“一次索引、全程复用”的设计理念，在不牺牲模型质量的前提下，实现了对 LLM 长上下文推理全链路（prefill → cache → decode）的高效优化，是迈向高效通用 AI 的一个重要架构进展。

</details>

---

### 5. [GenAutoML: An Agentic Framework for Dynamic Architecture Generation and Optimization in Time-Series Analysis](https://arxiv.org/abs/2606.05860)

**Authors**: Oleeviya Babu Poikarayil, C\'edric Schockaert, Abdulrahman Nahhas, Christian Daase, Mursal Dawodi, Jawid Ahmad Baktash  
**Category**: cs.LG  
**Published**: 2026-06-05  
**Score**: 11.0  
**Type**: new  
**ArXiv ID**: 2606.05860v1  

#### Abstract
Designing neural architectures for time-series forecasting and anomaly detection remains a resource-intensive task that often requires substantial domain expertise. Traditional Automated Machine Learning (AutoML) systems typically rely on static, predefined search spaces, limiting their ability to a...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：GenAutoML: An Agentic Framework for Dynamic Architecture Generation and Optimization in Time-Series Analysis

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
传统 **AutoML** 和 **Neural Architecture Search (NAS)** 在时序分析中面临以下瓶颈：
- **静态搜索空间**：依赖预定义的网络结构模板，缺乏“语义创造力”，无法生成全新的拓扑（如自定义的时间混合层）。
- **部署延迟高**：大型 **Time-Series Foundation Models (TSFMs)**（如 Chronos、MOIRAI）虽然精度高，但参数量巨大（>100M），推理延迟高达数百毫秒，难以部署在 **Edge AI** 场景。
- **非平稳性挑战**：现实工业数据（如电力变压器温度）具有强非平稳性（non-stationarity），导致模型训练不稳定、梯度爆炸。

### 🚀 提出的新方法与创新点
GenAutoML 提出了一种基于 **Agentic AI** 的动态神经架构生成框架，核心创新如下：

#### （1）**Agentic Neural Synthesis with Sandboxed Reflection（语义接口）**
- 利用 **Large Language Model (LLM)** 作为“神经架构师”（Neural Architect），将自然语言需求（如“设计一个轻量级 Inception 模型”）直接转化为可执行的 `PyTorch` 代码。
- 引入 **Sandboxed Reflection Loop**：在隔离环境中模拟前向传播，捕获维度不匹配、通道错误等 `traceback` 错误，并反馈给 LLM 自主修复，实现闭环调试。

#### （2）**Runtime Architectural Injection（运行时注入）**
- 支持 **Just-In-Time (JIT) 动态加载**，通过 `importlib.reload` 实现“热插拔”（hot-swap），无需重启即可将新生成的 `nn.Module` 注入正在运行的 **Optuna** 超参优化流程。
- 配备 **Signature-Aware Runtime** 和 **Shape-Agnostic Projection Head**，自动处理未知签名和输出维度不匹配问题。

#### （3）**Dynamic Reversible Instance Normalization (Dyn-RevIN)（安全护栏）**
- 将 LLM 生成的不可信架构逻辑与数学稳定性解耦，通过 **Dyn-RevIN** 层强制输入输出满足统计平稳性，防止梯度爆炸，提升收敛鲁棒性。

#### （4）**End-to-End Conversational Pipeline**
- 提供对话式 ML 工作流：用户上传数据 → LLM 驱动的 **Pandas DataFrame Agent** 进行 EDA → 用户提出架构需求 → 自动生成并验证模型 → 注入训练流程。

### 🔍 相比现有方法的优势
| 维度 | 传统 NAS / AutoML | TSFMs（如 Chronos） | GenAutoML（本文） |
|------|------------------|--------------------|------------------|
| 架构灵活性 | 固定搜索空间 | 固定模型 | ✅ 动态生成全新拓扑 |
| 推理延迟 | 中等 | ❌ 极高（~987ms） | ✅ 极低（<0.01ms） |
| 参数量 | 中到大 | ❌ >100M | ✅ 轻量级（<1M） |
| 部署场景 | 云端 | 云端 | ✅ Edge AI |
| 数学稳定性 | 依赖人工调参 | 内建稳定 | ✅ 自动化 Dyn-RevIN 护栏 |

---

## 2. 核心实验方法和设置

### 📊 数据集
在三个标准多变量时序基准上进行评估：
- **ETTh1**：电力变压器温度（小时级），高度非平稳
- **ETTm1**：电力变压器温度（分钟级），更高频波动
- **Weather**：气象数据（10分钟粒度），含21维气候特征（温度、湿度、风速等）

### ⚙️ 实验设置
- **任务类型**：
  - **长序列预测**：Lookback=96, Horizon=96
  - **异常检测**：Lookback=60, Horizon=10（无监督重构）
- **数据划分**：严格时间顺序划分（70%训练，10%验证，20%测试），防止泄露
- **预处理**：
  - 使用 **asymmetric regularization** 处理缺失值（训练集双向插值，测试集仅前向填充）
  - Z-Score 归一化（仅在训练集上拟合）

### 📈 评估指标
| 任务 | 主要指标 |
|------|--------|
| 预测 | **MAE**, **RMSE**（越低越好） |
| 异常检测 | **Discrimination Gap** = Anomalous MSE / Clean MSE（越高越好） |
| 效率 | **Inference Latency (ms)**, **Parameter Count**, **Search Cost (GPU time)** |

### 🆚 基线方法对比
| 类别 | 模型 |
|------|------|
| **零样本 Foundation Model** | Chronos-T5-Mini |
| **线性模型** | DLinear |
| **经典深度模型** | LSTM, Conv1D |
| **SOTA Transformer** | iTransformer, TimesNet, CrossFormer |
| **Agent 合成模型** | ResNet, Inception, BiGRU, WaveInterferenceNet |

---

## 3. 主要实验结果和性能指标

### 📉 预测性能（MAE, RMSE）
见 **Table 1**，关键发现：
- **ResNet** 和 **Inception** 在 ETTh1 和 ETTm1 上表现接近甚至优于复杂 Transformer（如 TimesNet）。
- **DLinear** 在所有数据集上仍为最优预测器，体现线性分解的强大基线能力。
- 在 **Weather** 数据上，Transformer 表现差（MAE > 4.8），而 Agent 生成的轻量卷积模型（如 ResNet）显著更优。

### 🚨 异常检测性能（Discrimination Gap）
见 **Table 2**，关键发现：
- **ResNetBlock** 在所有数据集上均取得最高敏感度：
  - ETTh1: **~265x**（远超 TimesNet 的 ~33x 和 DLinear 的 ~8x）
  - Weather: **~921x**（远超 DLinear 的 ~22x）
- **BiGRU** 在 ETTm1 上达到 **~1,228x**，显示跨域鲁棒性。
- 显示：**最佳预测器 ≠ 最佳检测器**（如 BiGRU 是好预测器但弱检测器）。

### ⚡ 推理效率与搜索成本（Table 3）
| 模型 | 参数量 | 推理延迟 | 搜索时间（5 trials） |
|------|--------|----------|------------------|
| DLinear | 52K | <0.01ms | 2m07s |
| Chronos-T5-Mini | 20M | **987.93ms** | N/A（zero-shot） |
| **WaveInterferenceNet (Ours)** | **829K** | **<0.01ms** | **2m01s** |

> 💡 **结论**：WaveInterferenceNet 实现了 **约 100,000× 的相对速度提升**，同时保持竞争力精度。

### 🔬 消融实验结果

#### （1）**Dyn-RevIN 消融（Table 5）**
- **非平稳数据（ETTh1, ETTm1）**：
  - 移除 Dyn-RevIN 导致 MAE 激增（ETTm1 上 BiGRU 从 0.455 → 2.541，↑450%）
  - 证明其对稳定训练至关重要。
- **平稳数据（Weather）**：
  - 移除 Dyn-RevIN 反而提升预测精度（MAE 从 3.787 → 1.426），因其可能掩盖周期信号的全局尺度。
  - 在异常检测中，启用 RevIN 会抑制振幅类故障（Gap 从 ~1146x → ~921x）。

> ✅ **核心结论**：**没有“银弹”方案**，需动态选择是否启用统计硬化。

#### （2）**Sandboxed Reflection 消融（Appendix E）**
- 所有架构最终均 **100% 成功通过验证**。
- 复杂模型（如 WaveInterferenceNet）需最多 **5 次迭代** 才能解决张量广播与矩阵对齐问题。
- 验证了闭环调试机制的有效性与确定性。

#### （3）**可复现性与稳定性（Table 4）**
| 模型 | 平均 MAE | 标准差 σ |
|------|---------|--------|
| DLinear | 0.8780 | **0.7600** |
| **WaveInterferenceNet** | 2.1485 | **0.0000** |

> ✅ WaveInterferenceNet 在不同随机种子下 **零方差收敛**，适合安全关键场景。

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **GenAutoML 可动态生成高性能、轻量级架构**：
   - 在预测任务中接近 SOTA，在异常检测中显著超越。
   - 生成的 **WaveInterferenceNet** 实现 **<0.01ms 推理延迟**，适合边缘部署。

2. **Agentic 框架具备“语义创造力”**：
   - 成功响应抽象指令（如“用波干涉思想设计模型”），生成含 **Hadamard Product** 和三角变换的原创结构。

3. **Dyn-RevIN 是关键稳定机制**：
   - 对非平稳数据不可或缺，但对周期性强的数据可能有害，需智能启用。

4. **确定性优于极致精度**：
   - 放弃追求绝对最低 MAE，转而优先保证 **零方差、快速收敛、低延迟**，更适合工业落地。

### ⚠️ 局限性
1. **生成延迟高**：依赖外部 LLM API（如 Llama 3-70B），单次合成耗时 30–60 秒，不适合实时响应场景。
2. **搜索成本未完全消除**：虽优于传统 NAS，但仍需 Optuna 进行微调。
3. **多模态上下文支持有限**：当前仅处理数值时序，未融合文本日志、天气报告等辅助信息。

### 🔮 未来工作方向
1. **本地化小型 LLM**：部署专用于代码生成的小型本地模型，降低 API 依赖与延迟。
2. **硬件感知合成（Hardware-Aware Synthesis）**：在 prompt 中加入内存、功耗约束，生成真正“Green AI”模型。
3. **多模态提示支持**：允许结合维护日志、操作记录等文本信息，指导架构设计。
4. **自动化 Dyn-RevIN 决策**：开发智能判别器，自动判断何时启用统计硬化。

---

> **一句话总结**：  
> GenAutoML 不是追求“最强预测力”的 NAS，而是面向 **Edge AI 安全部署** 的 **确定性、轻量化、自修复** 架构合成引擎，用 LLM 的创造力 + Dyn-RevIN 的稳定性，重新定义 AutoML 在工业时序中的角色。

</details>

---

### 6. [When Good Enough Is Optimal: Multiplication-Only Matrix Inversion Approximation for Quantized Gated DeltaNet](https://arxiv.org/abs/2606.06034)

**Authors**: Luoming Zhang, Yuwei Ren, Kui Zhang, Tian Liu, Lingjuan Ge, Denghao Li, Matthew Harper Langston, Yin Huang, Weiliang Will Zeng, Liang Zhang  
**Category**: cs.LG  
**Published**: 2026-06-05  
**Score**: 11.0  
**Type**: new  
**ArXiv ID**: 2606.06034v1  

#### Abstract
Matrix inversion in chunk-wise parallel linear attention is a major bottleneck for long-context modeling, particularly on NPUs, where forward-substitution-based methods exhibit limited parallelism and poor hardware utilization. We propose a fast, Matrix Multiplication (MatMul)-based algorithm tailor...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*When Good Enough Is Optimal: Multiplication-Only Matrix Inversion Approximation for Quantized Gated DeltaNet*

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
在基于 **chunk-wise parallel linear attention** 的长上下文建模中，**矩阵求逆（matrix inversion）** 是一个关键瓶颈，尤其是在 **NPU**（Neural Processing Units）等硬件上。传统的 **forward substitution** 方法存在严重的串行依赖，导致并行度低、硬件利用率差，尤其在处理大块（large chunk）时性能下降明显。

此外，在低精度（如 INT8/INT16）量化推理下，高阶 Neumann 展开项会引发数值溢出和动态范围爆炸，进一步限制了高效部署。

### 提出了什么新方法或新思路
本文提出了一种 **仅基于矩阵乘法（MatMul-only）的近似矩阵求逆算法**，专为 Gated DeltaNet 中出现的严格下三角矩阵设计。其核心思想是“**足够好即最优**”（Good Enough Is Optimal），通过以下三个关键技术实现：

1. **低阶截断 Neumann 展开（Low-Order Truncated Neumann Expansion）**  
   利用 Neumann 级数 $(I - A)^{-1} = \sum_{n=0}^{k-1} A^n$，但只保留前 $N$ 项（如 $N=3$）作为初始近似，大幅减少计算量。

2. **结构化对角掩码（Structured Diagonal Masking）**  
   引入对角掩码 $M(N)$，仅保留主对角线附近 $N$ 条子对角线上的值，抑制远离对角线区域因截断产生的大误差和异常值，提升数值稳定性，尤其利于量化。

3. **并行残差校正（Parallel Residual Correction）**  
   将传统迭代式残差更新 $T^{(m+1)} = T^{(m)} + T^{(m)} R^{(m)}$ 重构为可并行化的矩阵幂累加形式 $T \approx T^{(0)} \sum_{s=0}^{S-1} E^s$，消除串行依赖，完全映射到 MatMul 内核执行。

### 相比现有方法的优势
- **更高的硬件效率**：将原本向量密集型、低并行度的 forward substitution 替换为高并行度的 MatMul 操作，显著提升 NPU 利用率。
- **更强的数值鲁棒性**：通过对角掩码控制动态范围，避免高阶项引起的溢出，支持稳定低比特量化（INT8/INT16）。
- **更低的延迟与功耗**：在保持模型准确性的前提下，实现高达 **5× 的 kernel 级加速** 和 **20% 的 decode 层开销降低**。
- **无需块划分（block-wise inversion）**：相比 Huawei CSL (2026) 等限制单个矩阵大小为 16×16 的方法，本方法支持 **64×64 大矩阵直接处理**，减少分块带来的调度开销。

---

## 2. 核心实验方法和设置

### 使用的数据集
- **WikiText-v2**：用于 single-kernel 分析（训练集采样 100 个样本，序列长度 4K）和端到端 PPL 评估（验证集）。
- **下游任务基准**：
  - **MMLU**：多任务语言理解能力
  - **CSR**（Commonsense Reasoning）
  - **RealWorldQA**：多模态视觉问答（结合 Grok-1.5 Vision 发布）

### 实验设置和评估指标

| 类别 | 设置说明 |
|------|--------|
| **模型系列** | Qwen3-Next 和 Qwen3.5 家族（0.8B ~ 80B 参数） |
| **chunk size** | 默认 $k=64$，部分实验测试 32 和 128 |
| **Neumann 阶数** | $N=3$ |
| **残差校正步数** | $S=8$ |
| **量化配置** | W4A16（Decoder 权重 INT4，激活 INT16），部分测试 INT8 矩阵求逆 |
| **硬件平台** | Snapdragon 8 Elite Gen 5（NPU） |

#### 评估指标
- **Single-kernel 准确性**：SNR（信噪比）、MSE
- **端到端准确性**：PPL（困惑度）、MMLU / CSR / RealWorldQA 准确率
- **性能指标**：单 kernel 周期数、decode 层总周期占比、加速比
- **消融实验**：不同 $N$ 与 $S$ 组合下的数值稳定性（是否 NaN）、PPL 表现

### 基线方法对比
- **FLA（Flash Linear Attention）**：当前主流 chunk-wise 并行实现，使用 forward substitution 进行矩阵求逆。
- **Block-wise Inversion（如 GDN Tri-Inverse）**：将大矩阵拆分为多个小矩阵分别求逆，牺牲并行粒度换取数值稳定。
- **Full Neumann Expansion**：展开所有 $k-1$ 项，理论上精确但计算昂贵且易溢出。

---

## 3. 主要实验结果和性能指标

### 关键性能数据

| 指标 | 结果 |
|------|------|
| **Kernel 级加速比** | 最高达 **5.2×**（chunk size=32），平均 **4.2×~5.2×** |
| **Decode 层开销降低** | 从 FLA 的 22.3%~31.4% 下降至 **5.2%~9%**，整体周期减少 **18.1%~24.6%** |
| **最大 chunk 支持** | 成功运行 **64×64** 矩阵求逆（远超 block-wise 方法的 16×16） |
| **量化支持** | 在 **INT16 和 INT8** 下均保持稳定，无精度崩溃 |

### 与基线方法的对比结果

#### ✅ 端到端准确性（Table 2）
在 Qwen3.5 全系列模型上，**PPL 与 FLA 完全一致**，下游任务（MMLU、CSR、RealWorldQA）差异在 ±0.3 以内，表明 **无可观测精度损失**。

#### ✅ 量化场景表现（Table 3）
在 W4A16 量化下：
- FLA 出现明显退化（如 0.8B 模型 RWQA 从 62.35↓至 56.08）
- 本文方法退化更小，**RealWorldQA 保持在 60.39**，显著优于 FLA

#### ✅ 单 kernel 性能（Figure 4）
- 所有 chunk size 下 cycle 数显著低于 FLA
- 加速比随 chunk size 增大仍维持高位（32: 5.2×, 64: 4.2×, 128: 4.6×）

---

### 消融实验结果（Ablation Study）

#### 🔹 组件消融（Table 4）
| 方法 | SNR_mean (dB) | SNR_worst (dB) |
|------|---------------|----------------|
| FP64, N=64 | 178.42 | 96.46 |
| → FP16 | 79.53 | -17.94 |
| → N=3 | 42.13 | -51.11 |
| → +S=8 | 80.35 | -4.24 |
| → +Diagonal Mask | **86.91** | **47.98** |

👉 **结论**：仅靠低阶截断和残差校正无法解决最坏情况下的溢出；**对角掩码是控制极端误差的关键**。

#### 🔹 Neumann 阶数与残差步数组合（Table 5）
| S\N | N=3 | N=4 | N=5 |
|-----|-----|-----|-----|
| S=1 | NaN | NaN | NaN |
| S=4 | NaN | 169.30 | 61.31 |
| S=8 | **8.98** | 9.54 | 66.03 |

👉 **结论**：
- $N=3$ 需至少 $S=6$ 才能收敛
- $N=4$ 虽可用，但在 INT16 下动态范围过大，**量化性能反而更差**
- 最终选择 **N=3, S=8** 达成最佳平衡

#### 🔹 不同 chunk size 适应性（Appendix H/I）
- 对于 32×32 矩阵，$N=4, S=3$ 已足够
- 对于 128×128 矩阵，需采用 **block-wise 分解为 64×64 子块** 处理，否则仍会溢出

---

## 4. 关键结论和发现

### 主要发现
1. **精确求逆非必要**：在 Gated DeltaNet 中，矩阵逆的能量集中在主对角线附近，**低阶 Neumann 近似已捕获 95% 以上结构信息**。
2. **“足够好”优于“完全精确”**：在低精度系统中，追求高阶展开反而引入更多量化噪声，**适度近似 + 残差校正 + 掩码控制** 是更优策略。
3. **MatMul 是硬件友好的通用原语**：将三角求解转化为纯 MatMul 流程，极大提升了 NPU 上的并行性和调度效率。
4. **支持 INT8 矩阵求逆**：实验表明即使将矩阵求逆模块量化至 **INT8**，性能与 INT16 几乎无差别（Table 7），证明该方法对低比特极其友好。

### 方法的局限性
- **不适用于任意矩阵**：仅针对 **strictly lower-triangular** 且谱半径小于 1 的矩阵有效。
- **超大矩阵（>128）仍需分块**：目前最大支持 64×64 单块处理，更大尺寸需结合 block-wise 策略。
- **对 chunk size 敏感**：最优参数 $N/S$ 需根据 chunk size 调整，缺乏完全自适应机制。

### 未来工作方向
- **自动调节 $N$ 和 $S$**：基于输入特征动态调整截断阶数与校正步数，实现 runtime 自适应优化。
- **扩展至其他结构矩阵**：探索对 DPLR（Diagonal-Plus-Low-Rank）等结构的类似加速。
- **端到端编译器集成**：将该算法封装为 Triton 或 TVM 中的高性能 kernel，便于广泛部署。
- **探索稀疏化结合**：结合结构稀疏性进一步压缩计算图，适配更小边缘设备。

---

> **一句话总结**：  
> 本文提出一种 **结构感知、MatMul-only、量化友好的矩阵求逆近似方法**，在 **不牺牲精度的前提下** 实现 **最高 5× kernel 加速** 和 **20% 解码开销降低**，为 **长上下文 LLM 在 NPU 上的高效部署** 提供了实用解决方案。

</details>

---

### 7. [BiasGRPO: Stabilizing Bias Mitigation in High-Variance Reward Landscapes via Group-Relative Policy Optimization](https://arxiv.org/abs/2606.04807)

**Authors**: Saket Reddy, Ke Yang, ChengXiang Zhai  
**Category**: cs.AI  
**Published**: 2026-06-05  
**Score**: 10.5  
**Type**: new  
**ArXiv ID**: 2606.04807v1  

#### Abstract
Mitigating social bias in Large Language Models (LLMs) presents a distinct alignment challenge: unlike verifiable tasks, bias lacks a single ground truth, creating a high-variance, subjective reward landscape. Previous preference-based fine-tuning methods have major trade-offs: Direct Preference Opt...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：BiasGRPO: Stabilizing Bias Mitigation in High-Variance Reward Landscapes via Group-Relative Policy Optimization

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
大型语言模型（LLMs）在预训练过程中会继承来自大规模文本语料的社会偏见（social bias），这些偏见可能在下游应用中导致歧视性行为。现有的偏好微调（preference-based fine-tuning）方法如 **DPO** 和 **PPO** 在处理偏见缓解任务时存在明显缺陷：
- **DPO** 是离线方法，依赖静态的偏好对数据，缺乏探索能力，泛化性差。
- **PPO** 虽然支持在线探索，但其依赖的 **critic model** 在高方差、主观性强的偏见奖励空间中容易产生不稳定的值估计，导致训练不稳定。

### 提出了什么新方法或新思路
本文提出 **BiasGRPO**，一个基于 **Group Relative Policy Optimization (GRPO)** 的偏见缓解框架。其核心思想是：
- 利用 GRPO 替代传统的 DPO 或 PPO，通过在每轮生成一组（group）响应，并以该组的平均奖励作为相对基准来计算优势函数（advantage），从而避免使用 critic model。
- 具体公式为：  
  $$
  A_{i,t} = \frac{r_i - \text{mean}(r)}{\text{std}(r)}
  $$
  其中 $ r_i $ 是第 $ i $ 个 completion 的奖励，$ \text{mean}(r) $ 和 $ \text{std}(r) $ 是整组 completion 奖励的均值和标准差。

### 相比现有方法的优势
- **稳定性更高**：无需 critic model，避免了其在主观任务中的噪声估计问题。
- **保持探索能力**：允许模型在线生成多个 completion，提升泛化性。
- **更适合高方差任务**：在偏见这种缺乏单一“正确答案”的主观任务中，通过组内相对比较提供更清晰的学习信号。
- **模块化设计**：释放了一个高效、轻量（仅 0.1B 参数）且无知识退化的 **custom bias reward model** 和一个涵盖 11 个领域的多样化数据集，便于集成到多目标 RLHF 流程中。

---

## 2. 核心实验方法和设置

### 使用了哪些数据集
- **BiasDPO**（10,000 条）：原始偏见探测问题及偏好对。
- **合成扩展的 BiasDPO**（+8,855 条）：覆盖新增领域如 Age, Disability, Nationality, Physical Appearance, Socioeconomic Status, Sexual Orientation 及交叉领域（Race × Gender 等）。
- **Civil Comments**（10,000 条）：社交媒体评论，用于测试从看似中立提示中诱发的毒性。
- **UnQover**（999 条）：模糊情境下的偏见探测问题，答案应为“无法确定”。

最终构建了一个包含 **20,999 条 prompt** 的综合数据集。

### 实验设置和评估指标
- **基础模型**：Microsoft 的 **Phi-2**（2.7B），未经过 RLHF 或偏见微调，作为“干净起点”。
- **训练方法对比**：
  - **DPO**（含 IPO 变体）
  - **PPO**
  - **GRPO**（即 BiasGRPO）
- **训练参数**：3 轮训练，初始学习率 $10^{-6}$，线性调度。
- **评估指标**：
  - **BOLD**：衡量代表性伤害（representational harm），越低越好。
  - **RealToxicityPrompts (RTP)**：衡量显性敌意（overt hostility），越低越好。
  - **BBQ**：衡量隐式刻板印象（implicit stereotyping），越高越好（正确识别“无法确定”）。
  - **TruthfulQA**：衡量事实准确性，防止知识退化（knowledge degradation），越高越好。

### 基线方法对比
- **DPO/IPO**：离线偏好优化，无探索。
- **PPO**：在线强化学习，依赖 critic。
- **GRPO**：在线但无 critic，使用组内归一化优势。

---

## 3. 主要实验结果和性能指标

### 关键性能数据（见 Table 2）

| Benchmark | Base | DPO | PPO | **GRPO** |
|----------|------|-----|-----|---------|
| **BOLD (↓)** | 0.0293 | 0.0222 | 0.0268 | **0.0140** ✅ |
| **RTP (↓)** | 0.0282 | 0.0234 | 0.0262 | **0.0198** ✅ |
| **BBQ (↑)** | 0.2750 | 0.2823 | 0.2996 | **0.3123** ✅ |
| **TruthfulQA (↑)** | 0.3843 | 0.3941 | 0.3929 | **0.3941** ✅ |

> ✅ GRPO 在所有指标上均优于其他方法。

### 与基线方法的对比结果
- **相比 DPO**：GRPO 显著降低 BOLD 和 RTP 分数（分别下降 52.4% 和 29.8%），同时在 BBQ 上表现更好。
- **相比 PPO**：GRPO 在所有偏见指标上全面超越，尤其在 BOLD 上差距显著（0.0140 vs 0.0268）。
- **训练动态分析**（Figure 3）：
  - DPO 曲线早期饱和，表明泛化受限。
  - PPO 曲线波动剧烈，反映训练不稳定。
  - GRPO 曲线平稳上升，兼具稳定性和持续学习能力。

### 消融实验结果
#### （1）不同 group size 影响（Table 5）
| Group Size (G) | BOLD ↓ | RTP ↓ | BBQ ↑ | TruthfulQA ↑ |
|----------------|--------|-------|-------|-------------|
| G=2            | 0.0243 | 0.0242 | 0.2781 | 0.3868 |
| G=4            | 0.0140 | 0.0198 | 0.3123 | 0.3941 |
| G=8            | **0.0124** | **0.0115** | **0.3781** | **0.4137** |

> 结果显示：**group size 越大，性能越好**，验证了组内归一化机制的重要性。

#### （2）不同 reward model 对比（Table 4）
使用替代的 **stereotype reward model** 进行 GRPO 训练：
- 尽管性能略低于 custom reward model，但仍显著优于 base model。
- 表明 **GRPO 算法本身具有鲁棒性**，只要 reward model 合理即可有效引导优化。

#### （3）Online DPO 对比（Table 7）
- Online DPO 引入了在线探索，但性能仍远逊于 GRPO。
- 支持结论：**性能提升主要来自 group-relative normalization，而非单纯的在线探索**。

#### （4）跨模型验证（Llama 3.2 3B，Table 10）
- GRPO 在 Llama 架构上同样取得最佳性能（除 BBQ 外），证明其方法具有良好的泛化性。

---

## 4. 关键结论和发现

### 论文的主要发现
1. **GRPO 是解决高方差偏见缓解任务的理想框架**：
   - 其 group-relative 机制天然适配偏见任务中“无唯一正确答案”的特性。
   - 即使所有生成结果都带偏见，也能通过相对比较提取正向学习信号（如 least biased completion 得到正 advantage）。
2. **稳定性与泛化性的平衡**：
   - GRPO 成功结合了 DPO 的稳定性和 PPO 的泛化能力，解决了两者在偏见任务中的根本矛盾。
3. **模块化资源的价值**：
   - 发布的 **custom bias reward model**（0.1B）高效且无知识退化，可无缝集成至多目标 RLHF 流程。
   - 扩展的 **11 领域数据集** 提升了训练的多样性和鲁棒性。

### 方法的局限性
- 实验集中在 **3B 规模模型**（Phi-2 和 Llama 3.2），尚未在更大规模模型（如 70B+）上验证效果。
- 固定 group size 设置，未探索自适应或任务感知的动态分组策略。
- 合成数据虽经 Vendi Score 验证语义多样性，但仍可能存在分布偏差。

### 未来工作方向
- 探索 **adaptive group sizing** 策略，根据不同 prompt 动态调整生成数量。
- 将 BiasGRPO 扩展至 **multi-modal models** 或 **larger LLMs**。
- 研究如何将 GRPO 与其他 alignment objectives（如诚实性、帮助性）进行联合优化。
- 开发更细粒度的 bias-specific reward models，支持多维度偏见控制（如种族 vs 性别 vs 宗教）。

--- 

> **总结**：BiasGRPO 通过引入 GRPO 机制，在无需 critic model 的前提下实现了稳定且高效的偏见缓解，为高方差、主观性强的任务提供了新的优化范式，并通过开源数据与模型降低了研究门槛。

</details>

---

### 8. [Beyond tokens: a unified framework for latent communication in LLM-based multi-agent systems](https://arxiv.org/abs/2606.05711)

**Authors**: Yingzhuo Liu  
**Category**: cs.CL  
**Published**: 2026-06-05  
**Score**: 10.5  
**Type**: new  
**ArXiv ID**: 2606.05711v1  

#### Abstract
Multi-agent systems built on large language models (LLMs) have become a prevailing paradigm for tackling complex reasoning, planning, and tool-use tasks. The dominant communication protocol in such systems is natural language: agents exchange messages token-by-token, verbalising their internal reaso...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：Beyond Tokens: A Unified Framework for Latent Communication in LLM-based Multi-Agent Systems**

---

## **1. 论文的主要贡献和创新点**

### **解决了什么问题**
传统基于大语言模型（LLM）的多智能体系统（Multi-Agent System, MAS）依赖**自然语言通信（Natural Language Communication, NL-Comm）**，即智能体之间通过生成和解析文本消息进行协作。然而，这种通信方式存在三大结构性缺陷：

1. **高推理成本（High Inference Cost）**  
   每次通信都需要发送方解码为token、接收方重新编码，带来 $O(L \cdot T \cdot d)$ 的额外计算开销。

2. **离散化过程中的信息损失（Information Loss during Discretization）**  
   高维隐藏状态（~40,000 bits）被压缩为单个token（仅~15 bits），导致大量语义信息（如替代路径、置信度、上下文注意力）丢失。

3. **自然语言的冗余与歧义（Redundancy and Ambiguity）**  
   文本优化于流畅性而非信息密度，易出现模糊指代、礼貌填充等低效表达，且在背景知识不一致时可能导致沟通失败。

为解决这些问题，本文提出对新兴的**潜变量通信（Latent Communication, Latent-Comm）** 进行系统性梳理与统一建模。

---

### **提出了什么新方法或新思路**
作者提出了一个**三轴统一框架（3-Axis Unified Framework）**，用于组织和分类所有潜变量通信方法：

| 轴 | 描述 | 取值示例 |
|----|------|--------|
| **WHAT** | 传输何种连续表示？ | Embedding, Hidden State, KV-Cache, State Delta, Workspace State |
| **WHICH** | 发送方与接收方如何对齐？ | Last→First, All→Corresponding, Hub-and-Spoke, Learned Projection |
| **HOW** | 接收方如何融合接收到的信息？ | Concatenation, Prepend, Math Operation, Cross-Attention, Cache Restoration |

该框架将任意潜变量通信方法唯一地表示为三元组：  
$$ \text{Method} = (\text{WHAT}, \text{WHICH}, \text{HOW}) $$

并基于此框架系统分析了**18种代表性方法（2024–2026年提出）**，归纳出五类设计模式与六项开放挑战。

---

### **相比现有方法的优势**
- ✅ **首次提供统一分类体系**：打破碎片化研究现状，建立共享术语，降低新研究者入门门槛。
- ✅ **揭示设计权衡规律**：例如：
  - KV-Cache 信息最丰富但架构依赖最强；
  - “Last→First” 对同构模型简单有效，“Learned Interaction” 支持异构通信；
  - Concatenation/Prepend 多为训练免费（training-free），而 Cross-Attention 需要训练。
- ✅ **识别未来方向**：明确指出跨架构对齐、安全风险、边缘部署压缩等关键未解决问题。

---

## **2. 核心实验方法和设置**

本文为**综述性论文（survey/synthesis paper）**，其“实验”部分主要为**跨方法比较与实证趋势总结**，而非单一新方法的端到端实现。

### **使用的数据集**
论文汇总了各原始研究中广泛采用的基准套件，主要包括：

| 类别 | 数据集 |
|------|------|
| 数学推理 | GSM8K, MATH, AIME |
| 通用知识 | MMLU, ARC |
| 代码生成 | HumanEval, MBPP, LiveCodeBench |
| 多跳问答 | HotpotQA, 2WikiMultiHopQA, MuSiQue |
| 多模态推理 | MathVista, MMMU, ChartQA |
| 游戏推理 | Game24, Six Fives, Tower of London |
| 竞技游戏环境 | Mahjong, Uno, Honor of Kings（通过 RainbowArena 工具包评测） |

---

### **实验设置和评估指标**
由于各方法使用不同 backbone 和任务，无法直接横向对比。因此作者聚焦于**趋势性指标**：

| 指标 | 定义 |
|------|------|
| **Latency Reduction** | 相较 NL-Comm 的端到端延迟下降倍数 |
| **TTFT Speedup** | Time-To-First-Token 加速比（避免重复 prefill） |
| **Token Savings** | 减少生成的token数量 |
| **Accuracy Gain** | 在各类任务上的准确率提升 |
| **Generality** | 是否支持异构模型、是否需训练 |
| **Training-Free** | 是否可在预训练模型上直接部署 |

---

### **基线方法对比**
主要对比基线为：
- **Natural Language Communication (NL-Comm)**：标准文本通信范式。
- 各方法自身提出的 ablation variants（如是否启用压缩、对齐模块等）。

---

## **3. 主要实验结果和性能指标**

### **关键性能数据（综合报告结果）**

| 方法 | 性能亮点 |
|------|---------|
| **Interlat** | 最高 **24× latency reduction**（长上下文任务） |
| **RelayCaching** | **>80% KV-cache reuse**, **4.7× TTFT speedup** |
| **Agent Memory** | **TTFT speedup 22×–136×**（边缘设备） |
| **SDE** | 在复杂推理任务上达到 **SOTA** |
| **MoT (Mixture of Thoughts)** | ID任务 +0.38%，OOD任务 +2.92% 超越 Avengers |
| **Q-KVComm** | **5–6× KV-cache 压缩率**，精度损失可忽略 |
| **Agent Primitives** | **3–4× 更低 token 使用量和延迟**，仅比单智能体高 1.3–1.6× 开销 |

---

### **与基线方法的对比结果**
- 所有潜变量通信方法在**延迟和token效率**上显著优于 NL-Comm。
- 多数方法在**准确性上持平甚至超越** NL-Comm，尤其在长链推理、多跳任务中表现更优。
- **KV-Cache 类方法**在信息保留和效率上优势最大，已成为主流趋势（18种中有9种使用）。

---

### **消融实验结果（来自原论文引用）**
- **Interlat**：使用 learned projection 可提升异构微调模型间的通信效果。
- **Q-KVComm**：自适应量化策略比均匀量化保留更多语义信息。
- **MoT**：移除 interaction layers 或 router 会导致性能显著下降。
- **RelayCaching**：稀疏重计算（sparse recomputation）对边界误差修复至关重要。

---

## **4. 关键结论和发现**

### **论文的主要发现**
1. **潜变量通信是 NL-Comm 的有力补充**，尤其适用于中间推理信号传递，而最终输出仍可用自然语言保证可解释性。
2. **KV-Cache 正成为事实标准**：因其信息完整性最高，且可复用现有 KV-cache 优化基础设施。
3. **训练免费（training-free）是主流趋势**：18种方法中多数无需训练，便于部署。
4. **长上下文场景收益最大**：避免重复 prefill 带来的延迟节省随 context length 增长而放大。
5. **同构模型主导当前研究**：大多数方法假设 sender 和 receiver 共享相同 backbone。

---

### **方法的局限性**
- 🔒 **缺乏可解释性**：潜变量通道对人类不可读，难以调试、审计或对齐。
- 🔄 **强架构依赖**：尤其是 KV-Cache 方法，难以跨不同维度模型（如 Llama ↔ Qwen）直接使用。
- ⚠️ **安全隐患未被充分研究**：
  - 潜变量通道可能被用于**隐式对抗攻击（latent poisoning）** 或**信息泄露（exfiltration）**。
  - 当前几乎无防御机制研究。
- 💾 **传输开销大**：KV-Cache 尤其占用带宽和内存，限制边缘部署。

---

### **未来工作方向（六大开放问题）**

| 方向 | 描述 |
|------|------|
| **(1) Cross-Architecture Alignment** | 构建通用、训练免费的 O(N) 异构模型对齐机制（如 Vision Wormhole 的 UVC 是初步尝试）。 |
| **(2) Security & Robustness** | 研究潜变量通道的对抗鲁棒性、防御机制、可验证性。 |
| **(3) Compression & Quantization** | 发展更高效的 KV-Cache 压缩技术（如 learned compression, token-level pruning）。 |
| **(4) Theoretical Foundations** | 建立信息论模型，量化潜变量通信的信息增益与速度上限。 |
| **(5) Latent Communication vs. Latent CoT** | 统一“单智能体内潜推理”（Latent Chain-of-Thought）与“多智能体间潜通信”的框架。 |
| **(6) Real-World Deployment** | 面向边缘设备、移动网络（如 5G handover）、低功耗场景优化部署方案。 |

---

> **总结一句话**：  
> 本文通过提出 **WHAT/WHICH/HOW 三轴框架**，为快速发展的 **Latent Communication** 领域建立了首个系统性分类体系，揭示了设计规律，总结了实证趋势，并指明了未来六大关键研究方向，有望成为该领域的奠基性综述。

</details>

---

### 9. [Learned Subspace Compression for Communication-Efficient Pipeline Parallelism](https://arxiv.org/abs/2606.05484)

**Authors**: Paul Janson, Edouard Oyallon, Eugene Belilovsky  
**Category**: cs.LG  
**Published**: 2026-06-05  
**Score**: 10.0  
**Type**: new  
**ArXiv ID**: 2606.05484v1  

#### Abstract
Pipeline parallelism enables training of large language models that exceed single-device memory, yet inter-stage activation communication becomes the dominant bottleneck when trained on low-bandwidth networks. Recent work in this area has proposed using fixed orthogonal projections to compress activ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Learned Subspace Compression for Communication-Efficient Pipeline Parallelism*

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
在低带宽网络环境下进行 **pipeline parallelism** 训练时，跨阶段（inter-stage）的激活值（activations）通信成为主要瓶颈。虽然已有工作（如 **Subspace Networks, SSN**）尝试通过固定正交投影压缩激活值以减少通信量，但存在以下问题：
- 固定子空间无法适应不同 pipeline 阶段的动态特征分布；
- 引入架构修改（architectural modification），需对权重施加低秩约束；
- 导致显著的性能下降，且训练过程复杂。

### ✅ 提出的新方法：**MAPL (Manifold Aware Projection Learning)**

MAPL 是一种基于 **Stiefel 流形约束** 的可学习正交投影方法，用于高效压缩 pipeline 并行中的激活通信。其核心创新包括：

#### （1）**Per-stage 可学习正交投影器**
- 每个 pipeline 阶段独立学习一个正交投影矩阵 $ A_p \in \text{St}(d, r) $，将高维激活压缩到低秩子空间。
- 投影器通过 **SPEL (Spectral Steepest Descent on the Stiefel Manifold)** 算法更新，确保始终满足正交性约束（即保持在 Stiefel 流形上），避免梯度更新导致的“流形逃逸”（manifold escape）问题。

#### （2）**Factorized Anchor Embeddings**
- 引入每阶段可学习的低秩锚嵌入（$ E_{\text{small}} \in \mathbb{R}^{V\times r}, P_p \in \mathbb{R}^{r\times d} $），用于恢复 token-level 的高频信号。
- 仅传输整数 token ID 和低维投影坐标，通信开销极小。

#### （3）**与 Vector Quantization 组合（MAPL+VQ）**
- 在投影后的低秩表示上应用 **Multi-Codebook Residual Vector Quantization (MCVQ)** 进一步压缩。
- 采用 **streaming dictionary synchronization protocol**，异步分批同步码本，摊销通信成本。

### ✅ 相比现有方法的优势
| 特性 | SSN [42] | MAPL（本文） |
|------|----------|------------|
| 是否需要权重低秩约束 | ✅ 是（强制模型适应全局子空间） | ❌ 否（无需修改模型权重结构） |
| 投影是否可学习 | 有限学习（每 ~500 步粗略更新） | ✅ 完全可学习（每步更新） |
| 子空间是否共享 | ✅ 全局共享 | ❌ 每阶段自适应学习 |
| 是否兼容标准优化器 | ❌ 需修改 AdamW | ✅ 支持 Muon / AdamW 混合优化 |
| 压缩后能否移除投影 | ❌ 不可（为架构一部分） | ✅ 可（纯通信机制） |

> 📌 **优势总结**：MAPL 将压缩视为**通信层机制**而非**架构修改**，实现了更高的灵活性、更低的性能损失和更好的压缩-性能权衡。

---

## 2. 核心实验方法和设置

### ✅ 数据集
- **DCLM-10B**：大规模语言建模预训练语料。
- 验证集：从 DCLM 中随机保留 5M tokens。

### ✅ 模型架构与规模
基于 **LLaMA** 架构的 decoder-only Transformer，共三个参数尺度：
- **150M**, **500M**, **1B** 参数
- 上下文长度：2048 tokens
- 词表大小：32,000

### ✅ Pipeline 设置
- Pipeline 阶段数 $ P \in \{4, 8\} $
- 所有方法在相同 token 预算下训练（Chinchilla scaling rule：20 tokens per parameter）

### ✅ 优化配置
- **2D 权重**（Attention, MLP）：使用 **Muon** 优化器
- **1D 参数**（Embedding, Bias, LN）：使用 **AdamW**
- 学习率比例：`lr_adam = 0.5 × lr_muon`
- 全局 batch size：512

### ✅ 评估指标
| 指标 | 描述 |
|------|------|
| **Validation Cross-Entropy Loss** | 主要评估指标，衡量语言建模质量 |
| **Relative Degradation (%)** | 相对于未压缩基线的性能下降百分比 |
| **Zero-Shot Accuracy** | 在 HellaSwag, PIQA, ARC-Easy, ARC-Challenge 上的平均准确率 |
| **Bytes per Token / Compression Ratio** | 通信效率指标（如 4×, 8×, 16× 压缩） |

### ✅ 基线方法对比
| 方法 | 说明 |
|------|------|
| **Uncompressed** | 不压缩激活，作为性能上限 |
| **SSN [42]** | 固定共享低秩子空间，需修改优化器 |
| **SSN (AdamW version)** | 使用 AdamW 替代原版优化器的 SSN 变体 |
| **MAPL** | 本文提出的方法 |
| **MAPL+VQ** | MAPL + 向量量化，进一步提升压缩比 |

---

## 3. 主要实验结果和性能指标

### ✅ 关键性能数据（来自 Table 1）

| Model | Method | Comp. | P=4 Loss | Δ% | P=8 Loss | Δ% |
|-------|--------|--------|---------|-----|---------|-----|
| 150M | Uncompressed | — | 3.13 | — | 3.13 | — |
|      | SSN | 4× | 3.39 | 8.37% | 3.40 | 8.63% |
|      | **MAPL** | 4× | **3.156** | **0.84%** | **3.165** | **1.11%** |
|      | MAPL+VQ | 8× | 3.165 | 1.11% | 3.170 | 1.28% |
| 500M | Uncompressed | — | 2.84 | — | 2.84 | — |
|      | SSN | 6× | 3.09 | 8.92% | 3.12 | 9.90% |
|      | **MAPL** | 6× | **2.79** | **-1.90%*** | **2.84** | **0.00%** |
|      | MAPL+VQ | 12× | 2.92 | 2.75% | 2.88 | 1.49% |
| 1B   | Uncompressed | — | 2.68 | — | 2.68 | — |
|      | SSN | 8× | 3.05 | 13.93% | 3.08 | 15.05% |
|      | **MAPL** | 8× | **2.72** | **1.38%** | **2.73** | **2.02%** |
|      | MAPL+VQ | 16× | 2.76 | 3.01% | 2.74 | 2.30% |

> *注：负值表示优于未压缩基线（可能因正则效应）

📌 **结论**：
- MAPL 在所有尺度下均接近甚至匹配未压缩性能（最大退化 < 2.1%）；
- 显著优于 SSN（最多减少 14% 的性能损失）；
- MAPL+VQ 可达 **16× 压缩比**，仍保持 < 3.1% 的退化。

### ✅ 下游任务零样本准确率（Table 2）
| Model | Config | Avg Accuracy (P=4) | vs Uncompressed |
|-------|--------|---------------------|------------------|
| 150M | Uncompressed | 37.3 | — |
|      | MAPL | 36.7 | -0.6 pt |
| 500M | Uncompressed | 42.0 | — |
|      | MAPL | 41.8 (P=4), 41.6 (P=8) | ~ -0.2~-0.4 pt |
| 1B   | Uncompressed | 44.1 | — |
|      | MAPL | 43.3 (P=4), 42.6 (P=8) | ~ -0.8~-1.5 pt |

📌 **结论**：MAPL 几乎完整保留了下游能力，而 SSN 最多落后 **8.8 个百分点**。

### ✅ 消融实验结果

#### （1）**Stiefel 流形约束必要性（Appendix C）**
| 配置 | Val Loss | Δ% |
|------|----------|-----|
| 固定正交投影 | 3.1673 | 1.19% |
| 可学习但无流形约束（Muon） | 3.2101 | 2.56% |
| **可学习 + SPEL 更新** | **3.1564** | **0.84%** |

> 🔍 证明：若不强制正交性，性能反而更差；**SPEL 至关重要**。

#### （2）**Factorized Anchor 消融（Appendix G）**
| 锚策略 | Val Loss | Δ% |
|--------|----------|-----|
| 无锚 | 3.209 | +2.39% |
| SSN 式静态偏移 | 3.212 | +2.48% |
| 全可学习锚 | 3.149 | +0.47%（性能好但参数多） |
| **Factorized Anchor（本文）** | **3.165** | **+1.11%**（最佳平衡） |

> 🔍 证明：factorized anchor 在性能与参数效率之间取得最优折衷。

#### （3）**学习 vs 固定投影器（Figure 4b）**
- 在 rank=128 下：
  - 固定正交投影保留约 **36% 残差能量**
  - MAPL 学习的投影器保留 **~80% 能量**
> 🔍 说明：学习的投影能更好地捕捉任务相关低秩结构。

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **边界激活具有内在低秩结构**：即使不施加任何约束，pipeline 边界处的残差激活也自然呈现低秩特性（rank ≈ 250/1024）。
2. **每阶段应学习专属子空间**：不同 stage 的主角度分析显示其投影子空间几何差异显著（非邻近 stage 接近正交），支持 per-stage 自适应学习。
3. **MAPL 实现帕累托前沿**：在 **cross-entropy vs. 通信成本** 图中，MAPL 明显优于 SSN，在 16× 压缩下仍接近未压缩性能。
4. **向量量化可组合使用**：结合 VQ 可进一步翻倍压缩比（最高达 16×），且通过 streaming dictionary 协议几乎无额外通信负担。

### ⚠️ 局限性
- 当前实验局限于 **≤1B 参数模型**，更大规模（如 10B+）下的有效性待验证；
- 极端压缩（如 >16×）或加入 VQ 后仍有明显性能下降；
- 实际异构网络环境（延迟、丢包）中的鲁棒性尚未测试。

### 🔮 未来工作方向
- 扩展至 **MoE + Pipeline 混合并行** 场景；
- 探索 **动态调整投影秩 $ r $** 的机制；
- 在真实分布式协作训练（如 Internet-based volunteer training）中部署验证；
- 结合 **activation sparsification** 或 **error feedback** 进一步提升通信效率。

---

## 总结一句话
> **MAPL 提出了一种流形感知的可学习正交投影框架，使 pipeline parallelism 能在极低通信开销下（最高 16× 压缩）几乎无损地训练大模型，突破了传统固定子空间方法的性能瓶颈。**

</details>

---

### 10. [Improving Heart-Focused Medical Question Answering in LLMs via Variance-Aware Rubric Rewards with GRPO](https://arxiv.org/abs/2606.05174)

**Authors**: Arash Ahmadi, Parisa Masnadi, Sarah Sharif, Charles Nicholson, David Ebert, Mike Banad  
**Category**: cs.CL  
**Published**: 2026-06-05  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2606.05174v1  

#### Abstract
Large Language Models (LLMs) have shown strong promise in healthcare applications. Yet deploying general-purpose models in real-world settings remains difficult due to data privacy constraints, inference costs, and limited suitability for edge or on-device use. These challenges motivate the developm...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Improving Heart-Focused Medical Question Answering in LLMs via Variance-Aware Rubric Rewards with GRPO

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
大型语言模型（LLMs）在医疗领域展现出巨大潜力，但在实际临床部署中仍面临诸多挑战：
- **通用模型缺乏临床特异性**：容易生成看似合理但忽略禁忌症、混淆鉴别诊断或表达过度确定性的回答。
- **心脏相关问答尤其敏感**：如胸痛、呼吸困难等症状需要保守建议、恰当的不确定性处理和风险评估。
- **传统监督微调（SFT）的局限性**：SFT将复杂的多维度临床质量压缩为单一目标序列，难以优化涉及正确性、安全性、完整性等多标准的医学回答。

### 🚀 提出的新方法与创新思路
本文提出了一种基于 **Group Relative Policy Optimization (GRPO)** 和 **Variance-Aware Reward Framework** 的新型后训练框架，用于提升面向心脏疾病的医学问答能力。

#### 主要创新点包括：
1. **Variance-Aware Rubric Reward System（方差感知评分奖励系统）**
   - 改进了原始 Rubrics as Rewards (RaR) 中的显式聚合（Explicit Aggregation）和隐式聚合（Implicit Aggregation）策略。
   - 引入连续型分析奖励函数，替代加权二元准则聚合或单个Likert评分，提供更丰富的反馈信号。
   - 设计了两种新型奖励机制：
     - **Complexity-aware Reward**：对复杂评分项（rubric）赋予对数级额外奖励，鼓励模型攻克高难度问题。
     - **Hybrid Reward**：结合连续基础分与离散“完美完成”奖励（perfection bonus），平衡部分正确性和满分激励。

2. **GRPO-based Post-Training Pipeline**
   - 利用 GRPO 进行强化学习后训练，避免使用独立的价值网络（critic），降低内存开销。
   - 采用组内相对优势估计（group-wise relative advantage），增强训练稳定性，特别适用于稀疏、多标准、难自动验证的医疗反馈场景。

3. **结构化输出与合成推理链**
   - 使用 `<reasoning>` 和 `<SOLUTION>` 标签分离推理过程与最终答案，促进多步推理。
   - 在训练数据中引入由 MedGemma-27B 生成的合成推理轨迹（synthetic reasoning traces），提升模型解释能力。

4. **轻量化适配设计**
   - 基于 Qwen3-14B 模型，结合 **LoRA** 和 **4-bit 量化**，实现在单张学术级 GPU（如 NVIDIA RTX 6000 PRO）上完成训练与本地部署，支持隐私保护型边缘计算。

### 🔍 相比现有方法的优势
| 维度 | 本方法优势 |
|------|-----------|
| **训练效率** | 不需训练 critic 模型，节省资源；GRPO 更适合稀疏奖励环境 |
| **反馈质量** | 多准则独立评判 + 方差感知奖励 → 更稳定、信息更丰富的梯度信号 |
| **临床适用性** | 显式建模安全性、完整性、同理心等非事实性标准，符合真实临床评价体系 |
| **可扩展性** | 方法不依赖精确验证器（exact verifier），可用于开放域生成任务 |

---

## 2. 核心实验方法和设置

### 📚 数据集
| 数据集 | 用途 | 描述 |
|-------|------|------|
| **RaR-Medicine** | 训练数据来源 | 包含自然语言问题、参考回答及细粒度 rubric 注释（每个 criterion 含文本描述与正/负分值）。 |
| **Heart-Related Filtering** | 数据筛选 | 使用 MedGemma 构建分类器，过滤出与心脏相关的子集（共 2,204 条），涵盖高血压、心律失常、心梗等主题。 |
| **HealthBench** | 评测基准（held-out） | 包含 5,000 条医生编写的多轮健康对话，附有 262 名医师制定的标准 rubric。从中抽取 **500 条心脏相关样本**作为测试集（seed=42）。 |

### ⚙️ 实验设置
- **模型架构**：
  - 基座模型：`Qwen3-14B-Base`
  - 参数高效微调：LoRA（rank=16），应用于注意力与前馈层
  - 量化：4-bit（QLoRA）
- **训练流程两阶段**：
  1. **Supervised Fine-Tuning (SFT)**：在一半心脏相关数据上进行，教会模型输出结构化格式（reasoning + solution）。
  2. **GRPO Post-Training**：在另一半数据上进行强化学习，每条 prompt 采样 G=6 个响应，基于 rubric 判定生成奖励并更新策略。
- **Judge Model**：
  - 使用 `GPT-OSS-120B` 作为 LLM Judge
  - 对每个 criterion 独立打分（binary decision: present/absent），返回带理由的 JSON 输出
  - 判断过程固定温度、启用重试机制以减少噪声

### 📊 评估指标
- **Accuracy**, **Precision**, **Recall**, **F1**
- 所有结果基于 HealthBench 心脏子集（n=500）
- 报告 95% 置信区间
- 补充分析包括 McNemar 显著性检验、响应延迟测量、消融研究

### 🆚 基线方法对比
| 模型 | 类型 | 参数量级 |
|------|------|---------|
| Qwen3-14B Base | 基线 | 14B |
| MedGemma-27B / -4B / -1.5B | 医疗专用模型 | 27B ~ 1.5B |
| Gemma3-12B, Phi4-14B, Llama-4系列 | 开源小模型 | 12B ~ 17B |
| Llama-3.3-70B | 大模型 | 70B |
| GPT-OSS-120B | 外部强基线 | 120B |
| Kimi-K2 | 最优外部模型 | ~1T |

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据（Table 2 & Fig. 4）

| 模型 | Accuracy | F1 |
|------|----------|-----|
| **Qwen3-14B Base** | 0.362 | 0.532 |
| **GRPO (RaR-EXPLICIT)** | 0.396 (+3.4%) | 0.567 |
| **GRPO (RaR-IMPLICIT)** | 0.412 (+5.0%) | 0.584 |
| **GRPO (HYBRID)** | **0.498** (+13.6%) | **0.665** |
| **GRPO (COMPLEXITY)** | **0.502** (+14.0%) | **0.668** |
| GPT-OSS-120B | 0.508 | 0.674 |
| Kimi-K2 | **0.570** | **0.726** |

> ✅ **核心发现**：
> - GRPO + Variance-Aware Rewards 将 Accuracy 提升 **+38.7%**（相对提升），F1 提升 **+25.7%**
> - 性能接近甚至超越远大于其规模的 GPT-OSS-120B（仅差 0.006 Accuracy）
> - 在本地可部署模型中表现最优

### 🔁 消融实验结果（Ablation Studies）
#### （1）不同 Reward 策略比较（Table 3）
| Reward 类型 | Acc Δ | Acc Δ% | F1 Δ | F1 Δ% |
|------------|--------|--------|-------|--------|
| RaR-EXPLICIT | +0.034 | +9.4% | +0.036 | +6.7% |
| RaR-IMPLICIT | +0.050 | +13.8% | +0.052 | +9.8% |
| **HYBRID** | **+0.136** | **+37.6%** | **+0.133** | **+25.0%** |
| **COMPLEXITY** | **+0.140** | **+38.7%** | **+0.137** | **+25.7%** |

> 💡 发现：
> - 原始 RaR 方法效果有限，因其采用固定权重或整体评分，无法适应临床问题的异质性。
> - 新提出的 **Complexity-aware** 与 **Hybrid** 奖励显著优于 RaR，差异具有统计显著性（McNemar test, p < 10⁻⁵）。

#### （2）Reward 动态分析（Fig. 6）
- 两种新奖励在整个训练过程中均呈现稳定上升趋势（EMA 与线性拟合证实）。
- **Complexity Reward** 绝对值更高，反映其对复杂 rubric 的放大效应。
- **Hybrid Reward** 方差更小，体现其平滑过渡特性。

#### （3）Judge 与 Policy 模型缩放影响
- 使用更强的 judge model（GPT-OSS-120B vs GPT-4o-mini）有助于捕捉细微标准。
- 即使 policy model 较小（14B），也能通过高质量 reward 实现高性能。

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **Variance-Aware Reward Design 是关键**  
   在缺乏精确验证器的医疗领域，传统的 binary 或 Likert 评分不足以支撑有效 RL 训练。引入连续、复杂度感知、保留部分得分信息的奖励函数，可显著提升 GRPO 学习效率。

2. **GRPO 非常适合多标准医学 QA 任务**  
   其基于组内相对优势的设计天然容忍稀疏奖励，并能从多个候选回答中提取差异化信号，非常适合 rubric-based 多维评估场景。

3. **小模型可通过强化学习逼近大模型性能**  
   一个仅 14B 参数的 Qwen3 模型，在经过 GRPO 后训练后，性能媲美 120B 的 GPT-OSS-120B，且可在单卡工作站运行，具备临床边缘部署潜力。

4. **结构化输出 + 推理链注入 提升可控性**  
   分离 reasoning 与 solution 可控地引导模型生成解释路径，便于后续审核与调试。

### ⚠️ 局限性
1. **依赖自动化评判（LLM-as-a-Judge）**
   - 当前评估完全依赖 GPT-OSS-120B 自动打分，尚未纳入真实医生前瞻性评审。
   - 虽然已有研究表明 LLM Judge 与人类评估高度一致，但仍存在偏差风险。

2. **训练成本集中在评判环节**
   - 每个 prompt 平均含数十个 rubric criteria，每次训练需数千次 judge 调用。
   - 尽管 policy 训练本地可行，但评判依赖高速推理平台（如 Groq），限制资源受限团队复现。

3. **应用范围目前局限于心脏病学**
   - 方法虽具通用性，但尚未在其他专科（如肿瘤、神经科）验证泛化能力。

### 🔮 未来工作方向
1. **整合真实医生反馈闭环**
   - 构建人机协同标注系统，逐步替换全自动评判，提高可信度。

2. **跨专科迁移与通用 rubric 框架构建**
   - 探索是否可建立统一的临床 rubric 模板，实现多科室通用训练。

3. **降低评判成本**
   - 探索轻量 judge 模型蒸馏、主动学习选择高价值样本等方式，减少 LLM Judge 调用次数。

4. **结合检索增强生成（RAG）**
   - 将 rubric-guided RL 与外部知识库结合，进一步提升事实准确性与个性化服务能力。

---

> 📌 **一句话总结**：  
> 本文提出一种基于 **Variance-Aware Rubric Rewards + GRPO** 的新范式，成功将小型 LLM（Qwen3-14B）的心脏病问答性能提升近 40%，达到与百B级模型相媲美的水平，同时保持本地可部署性，为安全、可靠、低成本的临床 AI 助手提供了切实可行的技术路径。

</details>

---

### 11. [CarbonSim: A Lifecycle-Aware Framework for Evaluating Carbon Tradeoffs in Hardware Upgrade Decisions](https://arxiv.org/abs/2606.06438)

**Authors**: Kartik Hans, Kaiwen Zhao, Stephen Lee  
**Category**: cs.DC  
**Published**: 2026-06-05  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2606.06438v1  

#### Abstract
As the demand for information and communication technologies (ICT) continues to rise, the environmental impact of computing systems is becoming an increasingly critical concern. Although newer hardware often improves performance and energy efficiency, these gains do not always offset the carbon cost...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*CarbonSim: A Lifecycle-Aware Framework for Evaluating Carbon Tradeoffs in Hardware Upgrade Decisions*

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
随着信息与通信技术（ICT）需求的增长，计算系统的环境影响日益加剧。尽管新一代硬件通常具备更高的 **performance-per-watt**，但频繁更换硬件所带来的 **embodied carbon**（制造、运输、处置等环节的碳排放）可能抵消其运行阶段的节能优势。尤其是在低负载或低碳电网场景下，提前替换旧设备可能导致净碳排放增加。

该论文系统性地探讨了一个关键问题：  
> **在何种 workload 条件、电力结构（grid carbon intensity）和硬件寿命假设下，升级计算硬件才能真正减少全生命周期碳排放？**

### ✅ 提出的新方法与新思路
作者提出了 **CarbonSim** —— 一个面向硬件升级决策的 **lifecycle-aware** 模拟框架，用于评估不同部署策略下的碳权衡（carbon tradeoffs）。

#### 主要创新点：
- **统一建模 operational 与 embodied carbon emissions**  
  同时考虑运行能耗（operational emissions）和硬件制造隐含碳（embodied carbon），突破传统仅关注能效的局限。
  
- **引入两种 embodied carbon accounting 策略**：
  - **Uniform Amortization（均匀摊销）**：将隐含碳在整个生命周期内平均分配。
  - **Front-loaded Lifecycle Attribution（前端集中归因）**：通过指数衰减函数模拟早期高碳排放特性（如生产、运输阶段），更贴近现实。

- **支持 time-varying grid carbon intensity**  
  集成 Electricity Map API 获取实时电网碳强度数据，实现对地理与时间维度的精细建模。

- **可扩展的调度策略接口**  
  支持多种 carbon-aware 调度策略（如 Carbon-Aware、Wait-a-While、Threshold-based Greedy 等），便于研究调度政策对碳足迹的影响。

### ✅ 相比现有方法的优势
| 现有工具 | 局限性 | CarbonSim 的改进 |
|--------|-------|----------------|
| **CloudSim / K8sSim** | 专注于资源调度与性能优化，忽略 embodied carbon | 显式建模全生命周期碳排放 |
| **ACT 工具** | 聚焦于组件设计阶段的碳估算，不适用于运行时决策 | 面向实际部署场景，结合 workload trace 与调度策略进行动态评估 |
| 传统成本模型 | 忽视电网波动与时序因素 | 引入 hourly carbon intensity 变化，提升预测准确性 |

---

## 2. 核心实验方法和设置

### ✅ 数据集与硬件平台
实验基于跨代异构 CPU 平台构建，作为 calibrating point 进行横向比较：

| 硬件型号（年份） | 类型 |
|------------------|------|
| Intel Core Duo (2009) | 老旧平台 |
| Intel Core i7-4770 (2013), i7-4790 (2014) | 中期平台 |
| Apple M1 (2020), M2 (2022) | 新一代平台 |

> ⚠️ 注：这些设备并非完整服务器节点，而是用于提取标准化的 power profile 和 execution behavior。

### ✅ 工作负载（Workload）
选取四类代表性任务以覆盖多样化的计算模式：
- **Matrix Multiplication**（计算密集型）
- **MapReduce**（并行处理）
- **Fibonacci / GetPrime**（轻量递归/算法类）

所有 workload 执行时间、能耗由平台原生工具测量：
- Intel RAPL（Running Average Power Limit）
- macOS `powermetrics`
- 外接 wall-power meter（采样率 1Hz）

### ✅ 地理位置与电网碳强度
选择四个具有显著差异的地区（单位：gCO₂/kWh）：
| 地区 | Grid Carbon Intensity |
|------|------------------------|
| Quebec（加拿大魁北克） | 42（极高可再生能源比例） |
| Spain（西班牙） | 146 |
| California（美国加州） | 242 |
| Queensland（澳大利亚昆士兰） | 579（化石能源主导） |

### ✅ 评估指标
- **Total Lifecycle Emissions** = Operational Emissions + Embodied Emissions
- **Operational Emissions** = `energy × carbon_intensity × T_exec`
- **Execution Time / Performance Overhead**

### ✅ 基线方法对比
- **“new” cluster**：仅使用最新一代机器（M2 2022）
- **“mixed-generation” cluster**：混合使用从 2009 到 2022 年各代机器（每代两台）
- 对比不同 **scheduling policy** 下的表现：
  - Carbon-Aware
  - SLO-Aware
  - Wait-a-While
  - Threshold-based Greedy

---

## 3. 主要实验结果和性能指标

### ✅ 关键性能数据与发现

#### 🔹 图 6 & 表 1：新旧硬件碳足迹对比
- 在相同 workload 下（如 MatrixMulx），**M1/M2 与 i7-2013/2014 的总能耗相近**，表明近年能效提升趋于平缓。
- 尽管新硬件执行更快，但由于 **higher idle power** 和 **high embodied carbon cost**，其 **total lifecycle emissions 并未明显降低**。

#### 🔹 图 7：地理位置影响显著
- 在 **Quebec（42 gCO₂/kWh）**，**embodied emissions 占主导地位（>80%）**，此时继续使用已有旧设备反而更环保。
- 在 **Queensland（579 gCO₂/kWh）**，**operational emissions 主导**，升级至高效硬件可大幅减排（最高达 40%）。

> ✅ 结论：是否应升级硬件，高度依赖于 **location-aware** 因素。

#### 🔹 图 8：accounting model 影响重大
- 使用 **front-loading model** 时，新机器初期碳负担极重（前1–2年占 60%+），导致短期内总排放高于老机器。
- 在 fixed amortization 模型中，排放分布均匀，但依然显示：**新机器不一定更低碳**。

#### 🔹 图 9 & 10：调度策略与性能权衡
| 调度策略 | 碳减排效果（vs “new” cluster） | 性能开销（execution time increase） |
|---------|-------------------------------|------------------------------------|
| Carbon-Aware | ↓ ~25.8% | ↑ ~102.4% |
| Wait-a-While | ↓ ~21.7% | ↑ ~102.4% |
| Greedy     | ↓ ~16.3% | ↑ ~102.4% |

> 💡 关键发现：**mixed-generation clusters + carbon-aware scheduling 可实现最高减排（~25.8%）**，但代价是性能下降约一倍。

#### ✅ 消融实验（Ablation Study）
- 移除 embodied carbon 建模 → 错误推荐“立即升级”
- 忽略 grid variability → 高估碳感知调度收益
- 固定 utilization 假设 → 无法捕捉 bursty workloads 下的真实行为

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **“更新 ≠ 更绿”**  
   新一代硬件虽运行效率更高，但其 **embodied carbon 成本高昂**，尤其在以下场景中，保留旧设备更具环境优势：
   - 工作负载较轻（low utilization）
   - 电网清洁度高（renewable-rich grids）
   - 硬件尚未达到使用寿命终点

2. **硬件升级决策必须是三重感知的**：
   - **workload-aware**：负载特征决定能否发挥新硬件性能
   - **location-aware**：电网碳强度决定 operational vs embodied 的权重
   - **lifecycle-aware**：必须纳入制造与报废全过程碳核算

3. **混合代际集群（mixed-generation clusters）潜力巨大**  
   合理利用老旧设备，在碳感知调度下可实现显著减排（最高 **↓25.8%**），为数据中心提供可持续运维路径。

4. **存在明确的 performance-carbon tradeoff**  
   减排往往伴随性能下降（如 execution time doubling），未来需设计兼顾 SLA 与碳目标的智能 scheduler。

### ✅ 方法局限性
- **未建模可靠性与维护成本**：旧设备故障率上升可能带来额外运维碳成本。
- **依赖 workload profiling 数据**：真实环境中 workload 复杂多变，profile 泛化能力有待验证。
- **简化设施层建模**：冷却、网络、存储等通过 PUE 参数近似，未显式建模。

### ✅ 未来工作方向
1. 将 CarbonSim 集成到 Kubernetes 等容器编排平台，实现实时 carbon-aware scheduling。
2. 使用 benchmark 自动推断 workload profile，减少人工标注依赖。
3. 扩展至 GPU/accelerator 场景，支持 AI 训练等新兴负载。
4. 探索 **dynamic lifespan modeling**，根据设备状态自适应调整 accounting 策略。

---

> 📌 **一句话总结**：  
> *CarbonSim 揭示了“盲目追求硬件更新”的生态陷阱，倡导一种更加理性、系统性的硬件生命周期管理范式——真正的绿色计算，不只是跑得快，更是算得久、用得值。*

</details>

---

### 12. [Latent Reasoning with Normalizing Flows](https://arxiv.org/abs/2606.06447)

**Authors**: Guancheng Tu, Xiangjun Fu, Suhao Yu, Yao Tang, Haoqiang Kang, Lianhui Qin, Yizhe Zhang, Jiatao Gu  
**Category**: cs.CL  
**Published**: 2026-06-05  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2606.06447v1  

#### Abstract
Large language models often improve reasoning by generating explicit chain-of-thought (CoT), demonstrating the importance of intermediate computation. However, textual CoT forces this computation through a discrete, serial, and communication-oriented token stream: each reasoning step must be verbali...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文《Latent Reasoning with Normalizing Flows》总结

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题

传统的 **Chain-of-Thought (CoT)** 推理通过生成显式的文本中间步骤来提升大语言模型（LLM）的推理能力。然而，这种基于离散 token 的推理存在以下问题：

- **低效且冗长**：每个推理步骤都必须以自然语言形式表达，导致高 token 成本。
- **串行依赖强**：每一步必须先“说出”才能继续，限制了并行性和计算效率。
- **语义损失**：文本是低信息密度的媒介，难以捕捉不确定、模糊或未完全成形的中间状态。

现有的**隐式推理（latent reasoning）** 方法尝试用连续向量替代文本推理链，但往往牺牲了 LLM 原有的优势，如：

- 缺乏可微分的概率建模（如扩散模型需迭代去噪）
- 不支持原生的 left-to-right 采样
- 难以进行 likelihood-based 优化和 policy gradient 训练

### 提出了什么新方法或新思路

本文提出 **NF-CoT**（Normalizing Flow Chain-of-Thought），一种新的**连续隐式推理框架**，其核心思想是：

- 将连续的“思维”（continuous thoughts）建模为一个**可逆归一化流（normalizing flow）**，嵌入到 LLM 的因果流（causal stream）中。
- 使用 **STARFlow-style autoregressive normalizing flow** 对连续推理路径建模，使其具备**精确的似然函数（exact likelihood）**。
- 在训练时，将显式 CoT 蒸馏为连续 latent $ e_{1:K} $，再通过浅层 flow 块映射到易采样的空间 $ u_{1:K} $。
- 在推理时，直接从 $ u_{1:K} $ 左到右采样，并与答案生成共享同一个 LLM backbone 和 KV cache。

### 相比现有方法的优势

| 特性 | 显式 CoT | 扩散类隐式推理（如 LaDiR） | NF-CoT ✅ |
|------|----------|----------------------------|---------|
| 连续表示 | ❌ | ✅ | ✅ |
| 可微分似然 | ✅（token-level） | ❌（intractable） | ✅（exact） |
| 左到右采样 | ✅ | ❌（iterative denoising） | ✅ |
| 支持 policy gradient | 仅限 token | 困难 | ✅（latent + token） |
| KV cache 复用 | ✅ | ❌ | ✅ |
| 中间推理成本 | 高 | 中等 | **极低** |

**核心优势总结**：
- **保留了显式 CoT 的建模接口**（采样、评分、解码），但在连续空间中实现。
- **首次实现了对连续推理路径的精确概率建模**，支持监督学习和强化学习联合优化。
- **显著降低中间推理成本**，推理速度远超扩散模型。

---

## 2. 核心实验方法和设置

### 使用的数据集

- **训练数据**：`Ling-Coder`（1.4M 条 Python 指令遵循样本）
- **评估数据集**（均为代码生成任务）：
  - `HumanEval`（Chen et al., 2021）
  - `MBPP`（Austin et al., 2021）
  - `HumanEval+` / `MBPP+`（更严格的测试用例）
  - `LiveCodeBench v6`（Jain et al., 2025）

### 实验设置和评估指标

- **主干模型**：`Qwen3-8B-Base`
- **Latent 设置**：64 个 latent slots，维度 2560
- **评估指标**：
  - `pass@1`：单次采样通过率（平均 over 16 samples）
  - `pass@k`：k 次采样中的最高通过率（k=1~128）
- **采样方式**：
  - 统一使用 vLLM 进行高效解码
  - NF 采样温度与答案温度分别控制

### 基线方法对比

| 类别 | 基线方法 |
|------|--------|
| **自回归模型** | Qwen2.5-Coder, OpenCoder, OlympicCoder, Seed-Coder |
| **扩散语言模型** | Dream, LLaDA, Diffu-Coder, Dream-Coder |
| **循环隐式推理** | Ouro |
| **其他隐式推理** | Soft Thinking, TaH+, LaVAE, **LaDiR**（主要对比基线） |
| **消融变体** | NF-CoT (Dual-Path), NF-CoT (Unified) |

---

## 3. 主要实验结果和性能指标

### 关键性能数据（pass@1 平均）

| 方法 | 平均 pass@1 | 相比 Base 提升 |
|------|-------------|----------------|
| Base Model (Qwen3-8B) | 55.8 | — |
| Standard SFT | ~67.5 | +11.7 |
| LaDiR | 61.6 | +5.9 |
| **NF-CoT (Unified)** | **68.8** | **+13.0** |
| → + RL | **70.1** | **+14.3** |

> ✅ **NF-CoT (Unified)** 在所有方法中表现最佳，平均 pass@1 达 **68.8%**，显著优于 LaDiR（+7.1%）和最强开源模型 OlympicCoder（+0.3%）。

### 与基线方法的对比结果

- **相比 LaDiR**：
  - 在 MBPP+ 上，NF-CoT 的 `pass@1`（72.1）已超过 LaDiR 的 `pass@128`（72.0）。
  - 在 HumanEval+ 上，NF-CoT 从 78.3 提升至 97.5（+19.2），而 LaDiR 仅到 90.2（+17.0）。
- **相比显式 CoT**：
  - 使用相同训练数据，NF-CoT 达到 80.0 pass@1，而 Standard SFT 仅为 67.5，说明性能增益来自**更好的推理路径建模**，而非更多数据。

### 消融实验结果

#### （1）Unified vs Dual-Path

| 方法 | Avg pass@1 |
|------|------------|
| NF-CoT (Dual-Path) | 65.2 |
| **NF-CoT (Unified)** | **68.8** |

✅ **Unified 设计更优**：将 latent 和 answer 放在同一条因果流中，避免了 latent 分布与解码上下文不一致的问题。

#### （2）两阶段训练（Stage 1 Warm-up）

| 方法 | HumanEval | HumanEval+ | LCB v6 |
|------|-----------|------------|--------|
| 完整两阶段 | 84.4 | 78.7 | 23.1 |
| 仅 Stage 2 | 81.5 | 75.5 | 21.4 |

✅ **Stage 1 至关重要**：先冻结 backbone 训练 flow 组件，能稳定训练动态，防止 backbone 过早被随机初始化的 flow 梯度破坏。

#### （3）推理效率对比（HumanEval）

| 方法 | Latent 生成时间 (s) | 总耗时 (s) | FLOPs/sample |
|------|---------------------|------------|--------------|
| LaDiR | 468.2 | 625.3 | 49.3T |
| NF-CoT (Unified) | **173.5** | **325.6** | **19.9T** |

✅ **NF-CoT 快 2.7 倍，便宜 2.5 倍**：因无需迭代去噪，仅需一次左到右采样。

---

## 4. 关键结论和发现

### 论文的主要发现

1. ✅ **连续隐式推理可以兼具高效性与可优化性**：NF-CoT 首次实现了对连续推理路径的**精确概率建模**，支持 likelihood-based 训练和 policy gradient 优化。
2. ✅ **统一架构优于双路径**：将 latent 与 answer 放在同一因果流中，能更好对齐训练与推理分布。
3. ✅ **采样多样性更高**：不同 latent 样本能引导模型走向**不同的正确实现策略**（如递归 vs 动态规划），而非仅表面变化。
4. ✅ **强化学习兼容性好**：在 latent 空间进行 RL 优化，不会导致 `pass@k` 曲线饱和，说明**未坍缩到单一解模式**。
5. ✅ **局部扰动鲁棒性强**：对 latent 添加噪声后，程序功能仍保持正确，说明 latent 控制的是“如何实现”，而非“是否能实现”。

### 方法的局限性

- **任务范围有限**：目前验证集中在**代码生成**，尚未扩展到数学、常识等其他推理任务。
- **依赖显式 CoT 数据**：latent 空间由 VAE 从显式 CoT 蒸馏而来，继承其偏见。
- **固定长度 latent**：64 slots 可能不适合过长或过短的推理过程。
- **latent 不可读**：无法像显式 CoT 那样提供人类可理解的解释。
- **RL 依赖执行反馈**：当前 RL 依赖 unit-test reward，在无明确验证器的任务上难以应用。

### 未来工作方向

- 将 NF-CoT 扩展到**多模态推理**和**数学推理**任务。
- 探索**动态长度 latent 序列**，适应不同复杂度的推理。
- 研究如何让 latent 表示更具**可解释性**或支持**人类干预**。
- 开发适用于非执行类任务的**通用 reward model**，以支持更广泛的 RL 优化。
- 探索与其他 reasoning paradigms（如 Tree of Thoughts）结合的可能性。

---

> **总结**：NF-CoT 是一种**高效、可微、可优化**的隐式推理框架，它通过 normalizing flow 将连续思维纳入 LLM 的原生建模体系，在保持生成质量的同时大幅降低推理成本，为下一代 LLM reasoning 提供了新范式。

</details>

---

### 13. [AsyncWebRL: Efficient Multi-Step RL for Visual Web Agents](https://arxiv.org/abs/2606.05597)

**Authors**: Hao Bai, Rui Yang, Chenlu Ye, Spencer Whitehead, Aviral Kumar, Tong Zhang  
**Category**: cs.LG  
**Published**: 2026-06-05  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2606.05597v1  

#### Abstract
Training vision-language web agents with multi-step RL is compute-intensive, with two dominant forms of inefficiency: idle GPUs in synchronous RL, and trajectories that use more steps and tokens than necessary. We present AsyncWebRL, which addresses both. On the system side, an asynchronous design o...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文《AsyncWebRL: Efficient Multi-Step RL for Visual Web Agents》总结**

---

## **1. 论文的主要贡献和创新点**

### **解决的问题**
训练具备视觉理解能力的网页智能体（Visual Web Agents）通常依赖多步强化学习（multi-step RL），但该过程存在两大计算效率瓶颈：
1. **GPU 利用率低**：传统的同步 RL 框架在 rollout、梯度更新和策略刷新之间存在等待时间，导致 GPU 空闲。
2. **轨迹冗长且低效**：标准的多步 GRPO 算法中使用 `1/|T|`（按轨迹长度归一化）会导致失败轨迹因更长而被低估负梯度，从而鼓励策略生成冗余的“记忆模式”（verbose memory schemas），增加 token 和 step 开销。

### **提出的新方法**
论文提出了 **AsyncWebRL**，一个端到端异步的多步 RL 框架，从系统和算法两个层面进行优化：

#### **系统级创新**
- **Everlasting Rollout Pool**：保持 rollout worker 在迭代边界间持续运行，消除每次重建 rollout pool 的 warm-up 成本。
- **Lightweight Screenshot Handling**：不在共享存储中传输完整图像张量，而是仅传递轻量引用，避免因高分辨率截图导致的数据存储溢出（disk-spill）。
- **Decoupled Importance Sampling**：将 PPO 中的 `T0/Tbehave` 拆分为两个因子：
  - `Tprox/Tbehave`（rollout staleness）
  - `T0/Tprox`（current update）
  并以 `Tprox` 为中心进行 clipping，减少由过时 rollout 引发的 clip 触发，提升训练稳定性。

#### **算法级创新**
- **移除轨迹长度归一化**：将 GRPO 中的 `1/|T|` 替换为常数 `1/k`（k 为 Easy 难度最大步数，本文设为 10）。
  - 这打破了“失败轨迹越长，梯度越弱”的耦合关系，使模型能更有效地从长失败中学习。
  - 结果是轨迹更短、每步 token 更少、memory schema 更紧凑。

### **相比现有方法的优势**
- **速度更快**：相比最快的开源同步框架 WebGym，实现 **2.4–2.9× 的端到端训练吞吐加速**。
- **性能更强**：在 WebGym OOD 测试集上达到新的开源 SOTA，平均成功率从 42.9% 提升至 **45.4%（+5.8% 相对增益）**。
- **尤其擅长复杂任务**：在 Medium 和 Hard 难度子集分别取得 **+42% 和 +48% 的相对提升**。
- **资源更高效**：在相同测试性能下，每步训练时间减少 11–19%，显著降低计算成本。

---

## **2. 核心实验方法和设置**

### **使用的数据集**
- **WebGym**：当前最大的开源多步视觉网页代理训练环境。
  - 包含约 290k 训练任务，覆盖 128k 真实网站。
  - 分为三个难度等级：Easy (10步), Medium (20步), Hard (30步)。
  - 测试集为 **1,167 个 OOD（out-of-distribution）任务**，其网站未出现在训练集中，用于评估泛化能力。

### **实验设置和评估指标**
- **模型架构**：基于 Qwen3-VL-8B 的两个变体：
  - `Qwen3-VL-8B-Instruct`
  - `Qwen3-VL-8B-Thinking`
- **动作空间**：坐标式操作 `{click, type, scroll, go_back, navigate, ANSWER}`，输入为原始截图。
- **奖励机制**：二值奖励，由 GPT-4o 作为 rubric evaluator 判断任务是否完成。
- **评估指标**：
  - 主要指标：**OOD 测试集上的峰值成功率（peak test success rate）**
  - 辅助指标：训练吞吐量（trajectories/hour）、每步响应长度、memory schema 复杂度、clip 触发率等。

### **基线方法对比**
| 方法 | 类型 | 特点 |
|------|------|------|
| **WebGym (sync REINFORCE)** | 同步 RL | 原始开源基线，使用 Filtered BC 目标函数 |
| **AsyncWebRL-RAFT++** | 异步 RL | 使用 RAFT++ 损失函数的异步版本，用于验证系统有效性 |
| **AsyncWebRL (full)** | 异步 RL | 完整方法：异步系统 + Decoupled PPO + `1/k` 归一化 |

---

## **3. 主要实验结果和性能指标**

### **关键性能数据**
| 方法 | Easy | Medium | Hard | **Avg** |
|------|------|--------|------|--------|
| WebGym (sync) | 50.9 | 24.1 | 4.8 | **42.9** |
| AsyncWebRL-RAFT++ | 46.6 | 27.8 | 5.5 | 39.3 |
| **AsyncWebRL (full)** | **52.4** | **34.3** | **7.1** | **45.4** |

- **总体提升**：+5.8% 相对增益（42.9 → 45.4）
- **困难任务提升显著**：
  - Medium: +42% 相对增益（24.1 → 34.3）
  - Hard: +48% 相对增益（4.8 → 7.1）

### **与基线方法的对比结果**
- **训练吞吐量**：
  - AsyncWebRL：约 **3,100 trajectories/hour**
  - WebGym：约 **1,050–1,300 trajectories/hour**
  - **实现 2.4–2.9× 的端到端加速**
- **Off-Policy Gap 控制良好**：
  - 最大 staleness 设为 2，实际训练中平均 off-policy gap ≈ 1.5，最大 ≈ 2.0，远低于上限。
- **Clip 触发率减半**：
  - 使用 Decoupled PPO 后，clip 触发率下降约 50%，显著加快 reward 收敛。

### **消融实验结果**
#### **(1) 移除 `1/|T|` 归一化的影响**
- **性能不变，效率提升**：
  - 测试成功率几乎一致，但：
    - 轨迹长度缩短
    - 每步 token 数减少（从 ~240 降至更低）
    - memory schema 更简洁（generic slot 使用从 34% ↓ 至 11%）
- **计算效率提升**：
  - 梯度更新时间减少 11–15%
  - 总体每步 wall-clock 时间减少 18–19%

#### **(2) Decoupled Importance Sampling 的作用**
- 相比 Coupled 版本：
  - Clip 触发率始终约为一半
  - Reward 上升更快，训练更稳定

#### **(3) 其他验证实验**
- **RAFT++ 也表现出类似 memory drift**：只要使用 `1/|T|`，即使算法不同也会出现冗余 memory 增长。
- **压缩 prompt 无效**：仅修改 prompt 无法阻止 memory 膨胀，说明根源在 loss 设计。
- **延长 horizon 加剧问题**：当 horizon 扩大为 20/40/60 时，memory key 数增长更剧烈，验证了机制预测。

---

## **4. 关键结论和发现**

### **主要发现**
1. **`1/|T|` 是多步 RL 中效率低下的根本原因**：
   - 因失败轨迹普遍更长，`1/|T|` 导致其负梯度被削弱，模型倾向于生成冗长、重复的 memory 内容。
   - 替换为常数 `1/k` 可打破这一循环，显著提升学习效率。

2. **Fully Async 架构可行且高效**：
   - 通过 **everlasting rollout pool** 和 **lightweight screenshot handling**，成功构建首个支持视觉、多步、全异步的开源 RL 框架。
   - 实现高达 **2.9× 的训练加速**，同时保持训练稳定性。

3. **Decoupled PPO 是关键 off-policy 修正**：
   - 将 rollout staleness 与 current update 解耦，使 clipping 更准确地反映当前优化动态，而非 rollout 过时程度。

4. **性能提升集中在高难度任务**：
   - 表明新方法特别有助于克服长 horizon 下的探索与记忆管理挑战。

### **方法的局限性**
- **依赖高质量 rollout infrastructure**：需要稳定的分布式系统支持，部署门槛较高。
- **off-policy gap 需控制**：虽然实验中表现良好，但在更大延迟或更高并发下可能需进一步调整。
- **memory schema 改进依赖 loss 设计**：prompt 层面干预效果有限，仍需算法层面配合。

### **未来工作方向**
- 探索更细粒度的 credit assignment 机制，如 turn-level 或 subgoal-level。
- 将 AsyncWebRL 扩展到其他视觉-语言代理任务（如机器人控制、GUI 自动化）。
- 结合 test-time scaling（如 Thinking 模式）进一步提升推理时表现。
- 研究如何自动选择最优的 `k` 值，而非固定为 Easy horizon。

--- 

> ✅ **总结一句话**：  
> **AsyncWebRL 通过系统级异步设计 + 算法级 `1/k` 归一化修正，首次实现了高效、快速、高性能的视觉网页代理多步 RL 训练，在速度和性能上均创下新的开源 SOTA。**

</details>

---

### 14. [Causal Atlases from Entropic Inference: Bayesian Networks beyond Optimal DAGs](https://arxiv.org/abs/2606.06440)

**Authors**: Hazhir Aliahmadi, Irina Babayan, Greg van Anders  
**Category**: cs.LG  
**Published**: 2026-06-05  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2606.06440v1  

#### Abstract
Data-driven causal relationship identification is pertinent to advancing understanding of complex systems both within and beyond science. Bayesian networks offer a probabilistic method for modelling generic causal relationships via directed acyclic graphs (DAGs). However, typical techniques for cons...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：**Causal Atlases from Entropic Inference: Bayesian Networks beyond Optimal DAGs**

---

## 1. 论文的主要贡献和创新点

### ✅ 解决了什么问题
传统基于优化的 **Bayesian Network**（BN）结构学习方法（如 NOTEARS、DAGMA）通过寻找单一“最优”DAG 来建模因果关系。然而，这种方法存在以下问题：
- 观测数据通常无法唯一确定一个 DAG，多个 **Markov-equivalent** 或同样数据一致的拓扑可能共存。
- 单一优化图会**掩盖结构性模糊性**（structural ambiguity），导致对因果关系的过度自信推断。
- 优化过程中的正则化（如 ℓ₁ 稚度惩罚）可能引入人为偏差，产生不具数据支持的“因果伪影”（causal artifacts）。

### 🆕 提出的新方法与新思路
作者提出一种基于**最大熵推理**（maximum-entropy inference）的因果发现框架，生成**因果图谱集**（Causal Atlases），即一组与数据兼容的 plausible DAGs，而非单一最优图。

#### 核心思想：
- 将图结构学习视为统计物理中的**系综采样问题**（ensemble sampling），构建一个加权图参数上的 **Gibbs 分布**：
  $$
  p(W|X) \propto \exp(-\beta Q(W;X))
  $$
  其中 $ Q(W;X) $ 是评分函数（如数据拟合损失），$ \beta $ 控制温度（探索 vs. 利用）。
- 使用 **Simmering 方法**（基于分子动力学采样）在有限温度下从该分布中采样大量带权有向图（允许循环）。
- 对每个采样图应用**非线性投影**到 DAG 空间（使用 DAGMA 中的 log-det acyclicity characterization），得到最终的 **acyclic ensemble**。
- 由此形成的“因果图谱”自然地量化了边级和图级不确定性。

### ⭐ 相比现有方法的优势
| 方面 | 传统方法（如 DAGMA） | 本文方法 |
|------|------------------------|----------|
| 输出形式 | 单一最优 DAG | **DAG 集合**（Causal Atlas） |
| 不确定性建模 | 无或依赖先验假设 | **隐式熵先验**（entropic prior），由数据支持区域体积决定 |
| 因果伪影风险 | 高（易受优化路径和正则化影响） | 低（多图验证一致性） |
| 可解释性 | 仅提供点估计 | 提供边缘概率、权重变异性、图多样性等诊断工具 |
| 先验依赖 | 显式结构先验（如稀疏性） | **无需预设先验**，结构偏好从数据景观中涌现 |

---

## 2. 核心实验方法和设置

### 📊 使用的数据集
1. **合成两节点系统**（Illustrative Example）
   - 结构：$ X_1 \rightarrow X_2 $
   - 模型：线性 SEM + 高斯噪声
   - 参数：$ a \sim \text{Uniform}([-2,-0.5]\cup[0.5,2]) $, $ \sigma=1 $, $ n=1000 $
   - 目的：可视化能量景观、采样动态与投影行为。

2. **20 节点线性 SEM**（Synthetic Benchmark）
   - 图结构：ER-4 类型随机 DAG（20 nodes，平均度为 4）
   - 边权重：$ W_{ij} \sim \text{Uniform}([-2,-0.5]\cup[0.5,2]) $ if edge exists
   - 数据生成：$ X = (I - W^*)^{-1}Z $, $ Z \sim \mathcal{N}(0,I) $, $ n=1000 $
   - 模型广泛用于 DAG 学习基准（如 DAGMA 设置）

### ⚙️ 实验设置
- **评分函数**：平方损失（squared loss）
  $$
  Q_{\text{data}}(W) = \frac{1}{2n} \|X - XW\|_F^2
  $$
- **总能量函数**：$ E(W;X) = Q_{\text{data}}(W) + h_{\text{det}}(W) $
- **采样方法**：**Simmering** —— 基于分子动力学的有限温采样
  - 引入动量变量，构建哈密顿系统
  - 使用 **Nosé-Hoover Chain (NHC)** 恒温器维持目标温度 $ T = 1/\beta $
- **投影步骤**：
  - 对每个采样图 $ W $，沿 $ h_{\text{det}}(W) $ 的梯度流进行非线性投影至 DAG 空间
  - 投影停止条件：$ h_{\text{det}}(W(T)) \leq \delta $（小阈值）
- **后处理**：
  - 阈值化微小边权重（$ |W_{ij}| < \epsilon $ 视为零）
  - 过滤平凡图（全零图）

### 📏 评估指标
- **边缘边际概率**（Edge Marginal Probability）：
  $$
  P(i \to j) = \frac{1}{M} \sum_{m=1}^M \mathbb{I}(|D^{(m)}_{ij}| > \epsilon)
  $$
- **边权重变异性**（Edge Weight Variability）：
  $$
  \text{Var}(D_{ij}) = \frac{1}{M} \sum_{m=1}^M (D^{(m)}_{ij} - \bar{D}_{ij})^2
  $$
- **图多样性**（Graph Diversity）：
  - 平均成对 **Structural Hamming Distance (SHD)**：
    $$
    \text{SHD} = \frac{2}{M(M-1)} \sum_{1 \leq m < n \leq M} \text{SHD}(D^{(m)}, D^{(n)})
    $$

### 🔀 基线方法对比
- **DAGMA**：当前最先进的连续优化方法，作为单图优化代表。
- 本文方法未直接比较其他贝叶斯方法（如 DiBS、ProDAG），但强调其避免了这些方法中常见的显式先验或变分族限制。

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据

#### （1）两节点系统（Fig. 1）
- 数据驱动的真实关系为 $ X_1 \rightarrow X_2 $
- 优化方法（如 DAGMA）仅恢复一条路径（$ w_1 \neq 0, w_2 = 0 $）
- 本文方法在有限温下采样显示：
  - 多数样本投影到 $ X_1 \rightarrow X_2 $ 轴（magenta）
  - 少量样本投影到反向 $ X_2 \rightarrow X_1 $ 轴（orange）
  - 揭示了**方向不确定性**的存在，尤其在小样本或高噪声下更显著

> ✅ 表明：即使数据偏向某一结构，另一竞争结构仍有一定概率被支持。

#### （2）20 节点线性 SEM（Fig. 2）
- 采样设置：$ T=1 $, 收集 $ 4\times10^4 $ 样本，随机选取 $ 1\times10^4 $ 投影
- 结果特征：
  - **平均 SHD = 40**
  - 平均非零边数 ≈ 119
  - SHD / avg_nonzero_edges ≈ 33.6%，表明图结构具有**高度多样性**

#### 四类典型边模式分析（Fig. 2c–f）：
| 图 | 边特性 | 解释 |
|----|--------|------|
| c | 低边际概率 + 低方差 | 几乎总是缺失，**稳健不存在** |
| e | 低边际概率 + 高方差 | 缺失为主，但部分图中有弱连接，**约束较弱** |
| d | 高边际概率 + 低方差 | 几乎总是存在且强度稳定，**强因果信号** |
| f | 高边际概率 + 高方差 | 经常出现但强度波动大，甚至方向可逆，**因果强度或方向模糊** |

> 💡 特别指出：DAGMA 推断出的某些“强边”（如 $ 12 \to 0 $）在本文图谱中表现为高方差，说明可能是**优化伪影**，并非数据强烈支持。

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **单一最优 DAG 不足以刻画因果结构不确定性**  
   数据往往支持多个拓扑，强行选择“最优”可能导致误导性结论。

2. **最大熵推理能自然涌现出“熵先验”**  
   不需人为设定稀疏性或顺序先验，高频出现的结构是因其在参数空间中占据更大体积（robust configurations）。

3. **因果关系应被视为“系综中的集体特征”**  
   重要边不是因为它在一个图里很强，而是因为它在许多数据一致的 DAG 中持续存在。

4. **传统优化方法可能产生“因果伪影”**  
   某些被选中的边在图谱中变异性极高，说明其存在依赖于特定优化路径，缺乏稳定性。

5. **有限温采样揭示隐藏的模型不确定性**  
   温度参数 $ \beta $ 提供了一个调节“探索-利用”的机制，在低 $ \beta $ 下逼近优化解，在高 $ \beta $ 下揭示潜在替代结构。

---

### ⚠️ 方法的局限性
- **计算成本较高**：相比单次优化，需要运行长时间的动力学轨迹并多次投影。
- **投影可能引入偏差**：虽然使用 log-det 流形几何，但非线性映射可能导致某些区域被过度代表。
- **温度选择敏感**：$ \beta $ 的设定影响采样分布，目前缺乏自动调参策略。
- **尚未处理隐变量或混杂因素**：假设完全观测，未扩展至 latent variable models。

---

### 🔮 未来工作方向
1. **加速采样算法设计**：开发更高效的 MCMC 或变分近似来替代分子动力学。
2. **自适应温度调度**：结合退火或 replica exchange 提升采样效率。
3. **引入因果干预数据**：将 interventional data 整合进 Gibbs 分布以打破 Markov 等价性。
4. **扩展至非线性 SEM 和函数型模型**：利用神经网络表示 $ f_j $，实现灵活的功能因果建模。
5. **构建因果相图**（Causal Phase Diagram）：研究不同数据规模、噪声水平下图谱结构的相变行为。

---

## 总结
> 本文颠覆了传统“找最优 DAG”的范式，提出将因果发现看作**从数据支持的图空间中采样一个最大熵系综**的过程。通过 **Simmering + log-det projection** 构造出“因果图谱”，不仅识别最可能的因果结构，还系统量化了**边存在性、强度、方向乃至整体拓扑的不确定性**。这是一种更具科学诚实性的因果建模方式——承认模糊，而非掩盖它。

</details>

---

### 15. [StepPRM-RTL: Stepwise Process-Reward Guided LLM Fine-Tuning for Enhanced RTL Synthesis](https://arxiv.org/abs/2606.04246)

**Authors**: Prashanth Vijayaraghavan, Apoorva Nitsure, Luyao Shi, Ehsan Degan, Vandana Mukherjee  
**Category**: cs.AI  
**Published**: 2026-06-05  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2606.04246v1  

#### Abstract
Automatic generation of RTL code for digital hardware designs remains challenging due to long-horizon reasoning, multi-step dependencies, and strict correctness constraints in Verilog and VHDL. We present StepPRM-RTL, a novel framework that combines stepwise trajectory modeling, process-reward model...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：StepPRM-RTL: Stepwise Process-Reward Guided LLM Fine-Tuning for Enhanced RTL Synthesis

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
当前基于 **LLM** 的 **RTL code generation** 面临三大挑战：
- **长程依赖（long-horizon reasoning）**：RTL 设计涉及多步骤、跨模块的逻辑决策，传统模型难以维持一致的推理链。
- **中间步骤缺乏监督**：现有方法仅在最终输出上进行正确性验证（outcome-based），无法指导中间设计决策（如 reset 结构、enable 信号协调等）。
- **语义粒度不匹配**：已有 **Process Reward Model (PRM)** 多在 token 级打分，而 RTL 的关键决策通常跨越多个语句或模块，token 级奖励不稳定且语义模糊。

### 🚀 提出的新方法：StepPRM-RTL
提出一个全新的 **推理感知（reasoning-aware）** 框架 **StepPRM-RTL**，其核心创新包括：

| 创新点 | 说明 |
|-------|------|
| **Step-level Process Reward Modeling (StepPRM)** | 首次定义并训练可在**语义有意义的设计步骤级**（而非 token 级）打分的 PRM。每个步骤包含自然语言 rationale 和对应的代码修改（code edit），实现对中间决策的质量评估。 |
| **PRM-Guided MCTS 探索** | 引入 **Monte Carlo Tree Search (MCTS)** 进行结构化搜索，利用 StepPRM 提供的 step-level 奖励引导探索高质量的替代推理路径，生成多样化且高价值的训练轨迹。 |
| **Retrieval-Augmented Fine-Tuning (RAFT) with Reward Weighting** | 在 RAFT 框架中引入 **StepPRM 打分加权的轨迹学习**，使模型更倾向于学习高奖励的推理序列，并结合检索到的设计模式增强上下文理解。 |
| **迭代联合优化闭环** | 构建“轨迹构建 → StepPRM 训练 → MCTS 探索 → RAFT 微调”的迭代循环，持续提升策略模型（policy）和奖励模型（StepPRM）的质量。 |

### 🔍 相比现有方法的优势
- **超越纯监督微调（supervised fine-tuning）**：通过引入过程奖励，解决了长程任务中的信用分配（credit assignment）问题。
- **优于 outcome-only 方法**：提供密集反馈，避免稀疏奖励导致的学习效率低下。
- **优于 token-level PRM**：以语义步骤为单位打分，更符合硬件设计的实际决策流程，稳定性更高。
- **支持跨语言泛化**：在 **Verilog** 和 **VHDL** 上均表现优异，具备良好的通用性。

---

## 2. 核心实验方法和设置

### 📚 数据集
| 数据集 | 描述 |
|-------|------|
| **Verilog-Eval [11]** | 包含 156 个从 HDLBits 提取的 spec-to-Verilog 任务，配备自检 testbench，用于功能正确性评估。 |
| **VHDL-Eval [18]** | 包含 202 个由 Verilog-Eval 翻译而来的 spec-to-VHDL 任务，同样配有验证环境。 |
| **RTL-IR Corpus (in-house)** | 内部构建的数据集，包含 spec、代码及摘要，用于初始轨迹分解和模型预训练。所有生成的 stepwise 轨迹均经过 LLM 辅助生成并人工校验。 |

### 📊 评估指标
| 指标 | 定义 |
|-----|------|
| **Pass@1** | 第一次生成的 RTL 实现能否通过官方 testbench 编译、仿真并通过所有测试用例。衡量**功能正确性**。 |
| **Reasoning Fidelity (%)** | 使用 LLM judge 对比生成的 reasoning trajectory 与基准轨迹的一致性，量化中间推理质量。反映**推理保真度**。 |

### ⚙️ 实验设置
- **基础模型**：`Qwen3-8B-Instruct` 作为主干 LLM。
- **StepPRM 模型**：共享 backbone，输出 scalar 回归头预测 step reward。
- **检索模型**：`Qwen3-Embedding-4B`，用于 RAFT 中检索相似设计模式。
- **MCTS 参数**：每条 spec 执行 50 次模拟，探索常数 `Cuct=1.5`，rollout 深度为 10 步。
- **验证工具**：
  - Verilog：Icarus Verilog
  - VHDL：GHDL + VUnit

### 🆚 基线方法对比
| 类别 | 基线模型 |
|------|---------|
| **Prompt-based** | Vanilla Prompting (GPT-4o), CoDes (GPT-4o) |
| **Fine-tuning based** | RTLCoder (Mistral), CodeV (CodeQwen), VeriThoughts |
| **RAG-enhanced** | RAG-CodeBERT (GPT-4o), RAG-FT (GPT-4o) |
| **消融变体** | No MCTS, Supervised RAFT Only, No PRM |

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据（来自 Table 2）

| Model | Pass@1 (Verilog) | Pass@1 (VHDL) | Reasoning Fidelity (Verilog) | Reasoning Fidelity (VHDL) |
|-------|------------------|---------------|-------------------------------|----------------------------|
| **StepPRM-RTL (Full)** | **0.857** | **0.786** | **82.5%** | **80.2%** |
| RAG-FT (GPT-4o) | 0.719 | 0.531 | — | — |
| VeriThoughts | 0.755 | — | 60.4% | — |
| RTLCoder | 0.625 | — | — | — |
| Vanilla Prompting | 0.543 | 0.285 | — | — |

> ✅ **结论**：StepPRM-RTL 在 **Pass@1** 和 **Reasoning Fidelity** 上全面领先，相比最佳基线（RAG-FT）提升超过 **10%**。

### 🔍 消融实验结果（Ablation Studies）
| 变体 | Pass@1 (Verilog ↓) | Pass@1 (VHDL ↓) | Reasoning Fidelity ↓ |
|------|--------------------|------------------|------------------------|
| **No MCTS (Sampling-Only)** | 0.810 (-4.7pp) | 0.738 (-4.8pp) | ~4–4.5 pp drop |
| **Supervised RAFT Only** | 0.796 (-6.1pp) | 0.721 (-6.5pp) | ~7–8 pp drop |
| **No PRM (Outcome-only reward)** | 0.781 (-7.6pp) | 0.709 (-7.7pp) | 73.1% / 70.8% |

> 🔎 **关键发现**：
- **MCTS 至关重要**：结构化搜索显著减少无效路径，提高采样质量。
- **StepPRM 是核心驱动力**：移除 step-level 奖励后性能大幅下降，证明 outcome-only 奖励不足以支撑复杂 RTL 推理。
- **Reward-weighted RAFT 必不可少**：单纯模仿轨迹而不加权会降低学习效率。

### 📉 超参数敏感性分析（Figure 2）
- **MCTS 模拟次数（Nsim）**：性能随模拟数增加而上升，在 `Nsim=15` 后趋于饱和，表明 StepPRM 能有效引导搜索。
- **Reward Shaping 权重（λsh）**：最优值在 `0.3` 左右；过高（≥0.5）会抑制创造性合理解。

---

## 4. 关键结论和发现

### ✅ 主要结论
1. **Step-level supervision 显著优于 outcome-only 或 token-level 方法**：将 PRM 应用于语义设计步骤，是解决 RTL 长程合成任务的关键突破。
2. **结构化探索（MCTS）+ 密集反馈（StepPRM）= 高质量轨迹生成**：二者结合可有效扩展训练数据多样性，同时保证语义一致性。
3. **RAFT + Reward Weighting 实现高效策略内化**：模型不仅能复用设计模式，还能优先学习“好”的推理路径。
4. **框架具有跨语言泛化能力**：在 Verilog 和 VHDL 上均达到 SOTA，适用于多种 HDL。

### ⚠️ 局限性
- 当前主要针对单文件、中等规模模块（如计数器、FSM），尚未扩展至**多文件、层次化系统级设计**。
- StepPRM 依赖人工标注或强 LLM 生成的 rationale，存在潜在噪声。
- MCTS 增加推理延迟，不适合实时交互场景。

### 🔮 未来工作方向
1. 扩展至 **multi-file hierarchical designs**，支持模块间接口协同设计。
2. 将 **formal verification** 更深度集成进 StepPRM，提供更强的形式化约束信号。
3. 探索 **cross-architecture transfer**：将在 Verilog 上学到的推理轨迹迁移到 VHDL 或 SystemVerilog。
4. 开发轻量级 MCTS 变体，提升推理效率，推动实际部署。

---

## 总结
**StepPRM-RTL** 是首个将 **step-level process reward modeling** 成功应用于 RTL 综合任务的框架，通过融合 **StepPRM、MCTS、RAFT** 三大组件，实现了从“只看结果”到“理解过程”的跃迁。其实验结果充分证明了该方法在功能正确性和推理保真度上的显著优势，为 **AI-assisted hardware design automation** 建立了新的标准范式。

</details>

---

### 16. [MapAgent: An Industrial-Grade Agentic Framework for City-scale Lane-level Map Generation](https://arxiv.org/abs/2606.04513)

**Authors**: Deguo Xia, Zihan Li, Haochen Zhao, Dong Xie, Yuyao Kong, Xiyan Liu, Jizhou Huang, Mengmeng Yang, Diange Yang  
**Category**: cs.AI  
**Published**: 2026-06-05  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2606.04513v1  

#### Abstract
Lane-level maps are critical infrastructure for autonomous driving and lane-level navigation, yet constructing and maintaining standardized lane networks for hundreds of cities remains highly labor-intensive. Recent end-to-end vectorized mapping methods can predict lane geometry and topology directl...

---

### 17. [MIRAGE: Mobile Agents with Implicit Reasoning and Generative World Models](https://arxiv.org/abs/2606.04627)

**Authors**: Zhichao Yang, Yuanze Hu, Haojie Hao, Longkun Hao, Dongshuo Huang, Hongyu Lin, Gen Li, Lanqing Hong, Yihang Lou, Yan Bai  
**Category**: cs.AI  
**Published**: 2026-06-05  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2606.04627v1  

#### Abstract
Mobile agents are increasingly expected to operate everyday applications from screenshots and language goals, where reliable control requires reasoning over screen affordances, multi-step navigation, and future state changes. However, many agents externalize this computation as long textual chains o...

---

### 18. [When Evidence is Sparse: Weakly Supervised Early Failure Alerting in Dialogs and LLM-Agent Trajectories](https://arxiv.org/abs/2606.05414)

**Authors**: Avinash Baidya, Xinran Liang, Ruocheng Guo, Xiang Gao, Kamalika Das  
**Category**: cs.CL  
**Published**: 2026-06-05  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2606.05414v1  

#### Abstract
Early failure alerting requires deciding, while a dialog or agent trajectory is still unfolding, whether to flag it as likely to fail. This is challenging because supervision is typically available only as a trajectory-level success/failure label while alerts must be raised from partial interactions...

---

### 19. [CHASE: Adversarial Red-Blue Teaming for Improving LLM Safety using Reinforcement Learning](https://arxiv.org/abs/2606.05523)

**Authors**: Rahul Markasserithodi, Aditya Joshi, Yuekang Li, Ishmanbir Singh, Chris Yoo, Alan Niu  
**Category**: cs.CL  
**Published**: 2026-06-05  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2606.05523v1  

#### Abstract
Despite advances in safety alignment, prompt-rewriting attacks such as persona modulation, fictional framing and persuasion-based reformulation, can bypass safety filters even on frontier models. Existing defenses either rely on non-scalable human curation or white-box optimisation that overfits to ...

---

### 20. [LatentSkill: From In-Context Textual Skills to In-Weight Latent Skills for LLM Agents](https://arxiv.org/abs/2606.06087)

**Authors**: Aofan Yu, Chenyu Zhou, Tianyi Xu, Zihan Guo, Rong Shan, Zhihui Fu, Jun Wang, Weiwen Liu, Yong Yu, Weinan Zhang, Jianghao Lin  
**Category**: cs.CL  
**Published**: 2026-06-05  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2606.06087v1  

#### Abstract
Agent systems increasingly use textual skills to encode reusable task procedures, but injecting these skills into the prompt at every step incurs substantial context overhead and exposes skill content as plaintext. We present LatentSkill, a framework that converts textual skills into plug-and-play L...

---

### 21. [Dominant-Layer ZO: A Single Layer Dominates Zeroth-Order Fine-Tuning of LLMs](https://arxiv.org/abs/2606.05516)

**Authors**: Wanhao Yu, Ziyan Wang, Zheng Wang, Abeer Matar Almalky, Yihang Zuo, Shuteng Niu, Sen Lin, Adnan Siraj Rakin, Deliang Fan, Li Yang  
**Category**: cs.LG  
**Published**: 2026-06-05  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2606.05516v1  

#### Abstract
Zeroth-order (ZO) optimization enables memory-efficient fine-tuning of large language models (LLMs) using only forward passes, but it remains unclear how useful adaptation is distributed across layers. In this work, we reveal a surprising phenomenon: ZO fine-tuning is sharply dominated by a single d...

---

### 22. [PlanBench-V: A Spatial Planning Map Benchmark for Vision-Language Models](https://arxiv.org/abs/2606.05744)

**Authors**: Minxin Chen, He Zhu, Junyou Su, Wen Wang, Yijie Deng, Wenjia Zhang  
**Category**: cs.CL  
**Published**: 2026-06-05  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2606.05744v1  

#### Abstract
Spatial planning maps are central to territorial governance, translating planning objectives, regulations, and spatial strategies into visual forms for decision-making, public communication, and institutional coordination. Their interpretation, however, requires fine-grained visual perception, spati...

---

### 23. [LLMs Can Leak Training Data But Do They Want To? A Propensity-Aware Evaluation of Memorization in LLMs](https://arxiv.org/abs/2606.06286)

**Authors**: Gianluca Barmina, Peter Schneider-Kamp, Lukas Galke Poech  
**Category**: cs.CL  
**Published**: 2026-06-05  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2606.06286v1  

#### Abstract
Large language models can reproduce training data, but existing memorization evaluations mostly measure whether models can be forced to do so, rather than whether they do so under ordinary use. We introduce PropMe, a propensity-aware framework for memorization evaluation that contrasts prefix-based ...

---

### 24. [Catastrophic Forgetting as Accessibility Collapse: A Three-Level Framework for Knowledge Persistence in Continual Learning](https://arxiv.org/abs/2606.06032)

**Authors**: Ayushman Trivedi, Bhavika Melwani  
**Category**: cs.LG  
**Published**: 2026-06-05  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2606.06032v1  

#### Abstract
Catastrophic forgetting is commonly interpreted as the irreversible erasure of previously acquired knowledge during sequential learning. In this work, we investigate an alternative perspective: that forgetting may arise not from complete destruction of task representations but from a loss of accessi...

---

### 25. [Value-and-Structure Alignment for Routing-Consistent Quantization of Mixture-of-Experts Models](https://arxiv.org/abs/2606.05688)

**Authors**: Hancheol Park, Geonho Lee, Tairen Piao, Tae-Ho Kim  
**Category**: cs.CL  
**Published**: 2026-06-05  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2606.05688v1  

#### Abstract
Mixture-of-Experts (MoE) models scale foundation models efficiently by activating only a subset of experts for each token, but their large number of expert parameters still makes quantization essential for practical deployment. Unlike dense models, however, MoE models are sensitive to routing instab...

---

### 26. [TARPO: Token-Wise Latent-Explicit Reasoning via Action-Routing Policy Optimization](https://arxiv.org/abs/2606.05859)

**Authors**: Liting Zhang, Shiwan Zhao, Xuyang Zhao, Zichen Xu, Jianye Wang, Qicheng Li  
**Category**: cs.CL  
**Published**: 2026-06-05  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2606.05859v1  

#### Abstract
Latent reasoning has emerged as a promising alternative to discrete Chain-of-Thought (CoT) in large language models (LLMs), enabling more expressive reasoning by operating over continuous representations. However, the inherently deterministic nature of continuous representations limits policy explor...

---

### 27. [Flash-WAM: Modality-Aware Distillation for World Action Models](https://arxiv.org/abs/2606.05254)

**Authors**: Arman Akbari, Ci Zhang, Arash Akbari, Lin Zhao, Yixiao Chen, Weiwei Chen, Xuan Zhang, Geng Yuan, Yanzhi Wang  
**Category**: cs.LG  
**Published**: 2026-06-05  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2606.05254v1  

#### Abstract
World-action models (WAMs) jointly generate future video and robot actions through iterative diffusion, achieving strong performance on manipulation benchmarks but requiring tens of denoising steps, a cost that precludes real-time control. Step distillation has emerged as the natural remedy, but off...

---

### 28. [Domain-Adapted Small Language Models with Hybrid Post-Processing: Achieving Cost-Efficient, Low-Latency Multi-Label Structured Prediction via LoRA Fine-Tuning on Scarce Data](https://arxiv.org/abs/2606.05781)

**Authors**: Srinivasan Manoharan, Dilipkumar Nallusamy, Sachin Kumar, Haifeng Wu  
**Category**: cs.LG  
**Published**: 2026-06-05  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2606.05781v1  

#### Abstract
Deploying frontier large language models (LLMs) for domain-specific structured evaluation tasks often incurs substantial latency, cost, and data privacy overhead. We present a hybrid framework that combines a fine-tuned small language model (LLaMA 3.1 8B, with only 2.05% trainable parameters via LoR...

---

### 29. [A Sliced-Wasserstein Framework on Correlation Matrices for EEG Decoding](https://arxiv.org/abs/2606.06104)

**Authors**: Chen Hu, Rui Wang, Jiale Zhou, Jingjun Yi, Shaocheng Jin, Yidong Song, Yefeng Zheng  
**Category**: cs.LG  
**Published**: 2026-06-05  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2606.06104v1  

#### Abstract
Electroencephalography (EEG) offers noninvasive, millisecond resolution recordings of neuronal activity and is widely used in neuroscience and healthcare. Many EEG decoding pipelines rely on covariance descriptors for their robustness to noise, but such representations are sensitive to channel-wise ...

---

### 30. [On the training of physics-informed neural operators for solving parametric partial differential equations](https://arxiv.org/abs/2606.06164)

**Authors**: Nanxi Chen, Chuanjie Cui, Airong Chen, Sifan Wang, Rujin Ma  
**Category**: cs.LG  
**Published**: 2026-06-05  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2606.06164v1  

#### Abstract
Physics-informed neural operators (PINOs) aim to learn solution operators for partial differential equations by using the governing physics as supervision, rather than relying solely on paired input-output simulation data. By incorporating physical constraints into the training objective, PINOs comb...

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
