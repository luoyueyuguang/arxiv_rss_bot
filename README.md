# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-05-06 08:02:29 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG

## 📚 Recent Papers

### 1. [ZeRO-Prefill: Zero Redundancy Overheads in MoE Prefill Serving](https://arxiv.org/abs/2605.02960)

**Authors**: Zhaoyuan Su, Olatunji Ruwase, Karthik Ganesan, Aurick Qiao, Samyam Rajbhandari, Juncheng Yang, Yue Cheng, Yuxiong He  
**Category**: cs.LG  
**Published**: 2026-05-06  
**Score**: 14.0  
**Type**: new  
**ArXiv ID**: 2605.02960v1  

#### Abstract
Production LLM workloads increasingly serve discriminative tasks, such as classification, recommendation, and verification, whose answers are read from the logits of a single prefill pass with no autoregressive decoding. Serving these prefill-only workloads on mixture-of-experts (MoE) models is bott...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：ZeRO-Prefill: Zero Redundancy Overheads in MoE Prefill Serving

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
当前主流的 **LLM 推理系统**在处理 **仅预填充（prefill-only）任务**（如分类、推荐、验证等）时效率低下。这类任务不需要自回归解码（autoregressive decoding），答案直接从单次 prefill 的 logits 中得出。

然而，现有的 **MoE（Mixture-of-Experts）模型分布式推理策略**（如 DP、TP、EP、PP）虽然缓解了显存压力，却引入了严重的冗余开销：
- **计算冗余**：由于专家负载不均衡（routing imbalance），导致部分 GPU 成为 straggler；
- **通信冗余**：每层 MoE 需要两次同步的 `AllToAll` 通信，成为瓶颈；
- **内存冗余**：完整存储专家权重、重复的 KV 缓存等。

这些冗余源于一个“解码时代”的设计假设：**将专家放置与激活路由耦合（activation-routed EP）**，而这在长计算密集型的 prefill 场景中已不再必要。

---

### 🚀 提出的新方法与创新思路

#### **核心思想：解耦专家放置与激活路由**
利用 prefill 阶段长且计算密集的特点，在每层前向计算窗口内**异步流式加载专家权重**，从而完全移除关键路径上的 `AllToAll` 通信。

#### **提出系统：ZeRO-Prefill**
一个专为 prefill-only 工作负载设计的端到端服务系统，其核心是两个协同设计的组件：

1. **AsyncEP（Asynchronous Expert Parallelism）**  
   - **按权重聚集专家（gather by weight）而非按激活路由（route by activation）**
   - 每个 GPU 在执行某一层时，本地持有该层所有专家的完整副本；
   - 下一层的专家权重通过后台 `AllGather` 异步加载（可通过 NVLink 或 PCIe 从 CPU DRAM 预取）；
   - 所有通信被完全重叠在计算中，**从关键路径移除 `AllToAll`**。

2. **前端调度器（Frontend Scheduler）**
   - **基于物理推导的饱和阈值 T（saturation threshold）进行批处理控制**
     $$
     T = t_{ep} \times F_{GPU} \times \gamma
     $$
     其中 $t_{ep}$ 是通信延迟，$F_{GPU}$ 是峰值算力，$\gamma$ 是安全系数。
   - 实现三大感知调度：
     - **Prefix-aware routing**：优先将共享前缀的请求调度到同一 GPU，最大化 KV 缓存复用；
     - **True-FLOPs 负载跟踪**：准确建模实际计算成本（前缀只算一次）；
     - **Overlap-aware balancing**：确保每个 GPU 的计算量超过 T，保证通信可被隐藏。

---

### 🔍 相比现有方法的优势

| 维度 | 传统方法（如 DP+EP） | ZeRO-Prefill |
|------|------------------------|-------------|
| **通信开销** | 每层两次同步 `AllToAll`，不可重叠 | 后台异步 `AllGather`，完全重叠 |
| **计算效率** | 路由不平衡导致 GEMM 小且不规则，利用率低 | 本地 dispatch，无 straggler，高 MFU |
| **内存占用** | 每 GPU 存储全部专家子集，显存压力大 | 只缓存当前/即将使用的专家，支持 CPU offload |
| **部署灵活性** | 大模型需 ≥4 GPUs | 支持 1–8 GPUs，部署范围扩大 4× |

---

## 2. 核心实验方法和设置

### 📚 数据集

构建了一个**聚合的真实世界 prefill-only 工作负载**，混合来自以下公开基准的数据：

| 数据集 | 任务类型 | 上下文长度 | 请求数量 | 前缀共享程度 |
|-------|---------|------------|----------|--------------|
| MoralStories | 道德推理 | ~100–200 | 24K | 高 |
| MMLU | 多选问答 | ~50–500 | 24K | 低 |
| BoolQ | 是非问答 | ~200–600 | 12K | 低 |
| IMDB | 情感分类 | ~300–2K | 12K | 低 |
| QuALITY | 长文档问答 | ~4K–12K | 1.2K | 高 |
| ArXiv Class. | 文档分类 | ~6K–128K | 600 | 中 |

- 总计：**73.8K 请求，约 37.9M tokens**
- 所有任务均被重构为 **prefill-only 形式**

此外还使用了**合成工作负载**测试不同上下文长度下的表现（256 到 128K）。

---

### ⚙️ 实验设置

- **硬件平台**：
  - 8×A100 (80GB, BF16)
  - 8×H100 (80GB, BF16 / FP8)
  - 8×H200 (141GB, FP8)

- **模型**：
  - **Qwen3-235B-A22B**：128 专家，top-8 路由，激活参数约 22B

- **基线方法**（来自 vLLM 支持的策略）：
  1. DP+EP
  2. DP+TP
  3. TP+EP
  4. TP+TP
  5. PP+PP
  6. PrefillOnly [12] + DP+EP / PP+PP（增强版基线）

- **评估指标**：
  - **吞吐量（Throughput）**：tokens/sec
  - **MFU（Model FLOPs Utilization）**：实际算力 / 峰值算力
  - **峰值 HBM 占用**
  - **最大可行 batch/context 大小**
  - **任务准确性（Accuracy）**

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据

#### ✅ 端到端吞吐提升
在真实世界聚合工作负载上，ZeRO-Prefill 相比最强基线实现：
- **1.35–1.37× 吞吐提升**（跨所有硬件/精度配置）
  - 8×A100 (BF16): **1.37×**
  - 8×H100 (BF16): **1.36×**
  - 8×H100 (FP8): **1.35×**
  - 8×H200 (FP8): **1.37×**

> 💡 提升稳定，不受 FP8 带来的绝对吞吐翻倍影响，说明优化本质在于消除通信瓶颈。

#### ✅ 近线性扩展性
- 传统方法随 GPU 数增加出现**吞吐停滞甚至倒退**（因通信开销增长）；
- ZeRO-Prefill 实现**近线性扩展**，因通信已被异步隐藏。

#### ✅ 极高的 MFU
- 持续达到 **29.8% – 36.2% per-GPU MFU**
- 在单卡也能维持高利用率（得益于大 batch 和 offload 重叠）

#### ✅ 显著扩展部署范围
- 传统方法：Qwen3-235B 至少需要 **>4 GPUs** 才能容纳权重
- ZeRO-Prefill：可在 **1–8 GPUs** 上运行 → **部署硬件范围扩大 4×**

---

### 🔬 消融实验结果

#### （1）前端-后端协同设计的必要性（Fig. 10）

| 配置 | 吞吐增益（vs. DP+AsyncEP） |
|------|----------------------------|
| DP+AsyncEP（仅后端） | 基线 |
| ZeRO-Prefill（完整系统） | **+15% ~ +18%** |

> 前端的 prefix-aware routing 和 saturation-aware admission 对性能提升至关重要，尤其在高并行度下。

#### （2）不同上下文长度下的表现（Fig. 11）

| 上下文长度 | ZeRO-Prefill（DP+AsyncEP）提升 |
|-----------|-------------------------------|
| Short (256) | 1.30× |
| Medium (4K) | 1.30× |
| Long (32K) | 1.52× |
| Ultra-long (128K) | **1.59×** |

> 随着上下文变长，传统方法因 `AllToAll` 流量线性增长而急剧退化，而 ZeRO-Prefill 不受影响。

#### （3）MFU 表现（Fig. 12）
- 在 1–2 GPUs 上，其他方法无法运行（显存不足，标为 N/A）
- ZeRO-Prefill 在 1–2 GPUs 上仍可达 **32.0–36.2% MFU**
- 在 8 GPUs 上达 **29.8–34.7% MFU**

> 证明其不仅提升吞吐，还能在资源受限设备上高效运行。

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **Prefill-only 已成主流**：生产环境中 65.3% 的输入 token 属于 prefill-only 类型，亟需专用优化系统。
2. **MoE 推理瓶颈不在计算而在通信**：现有分布式策略因 `AllToAll` 和路由不均衡严重限制效率。
3. **解耦专家放置与路由是突破口**：利用 prefill 的长计算窗口异步加载权重，可彻底移除关键路径通信。
4. **协同设计是关键**：仅改进后端（AsyncEP）不够，必须配合前端的 prefix-aware 和 compute-aware 调度才能释放全部潜力。
5. **大模型可部署在更小硬件上**：通过 hybrid offloading + KV-cache-free，使 235B 级 MoE 模型可在单张 80GB GPU 上运行。

---

### ⚠️ 方法的局限性

1. **依赖高带宽互联**：若 NVLink/PCIe 带宽过低，通信时间 $t_{ep}$ 增大，可能导致无法完全重叠。
2. **对突发流量敏感**：需批量积攒足够计算以满足饱和阈值 $T$，不适合极低延迟或高度突发的场景。
3. **不适用于 dense 模型或需解码的任务**：专为 MoE + prefill-only 设计，通用性有限。
4. **前缀无关任务收益较小**：若无 prefix sharing，KV 复用优势消失，但仍受益于 AsyncEP。

---

### 🔮 未来工作方向

1. **动态调整饱和阈值 $T$**：应对 workload drift，实现 runtime 自适应。
2. **扩展至其他架构**：如结合 speculative decoding 或用于 long-context reasoning。
3. **专家作为可调度资源**：进一步将专家视为“可编排的任务”，实现更细粒度的资源管理。
4. **支持更多 offload 策略**：如分层预取、热度感知缓存等。

---

> **一句话总结**：  
> ZeRO-Prefill 通过 **AsyncEP + 协同调度**，将 MoE prefill 推理从“通信受限”转变为“计算饱和”，实现了高达 **1.59× 吞吐提升** 和 **4× 更广的部署范围**，为大规模判别式 LLM 应用提供了高效基础设施。

</details>

---

### 2. [CoVSpec: Efficient Device-Edge Co-Inference for Vision-Language Models via Speculative Decoding](https://arxiv.org/abs/2605.02218)

**Authors**: Yuanyuan Jia, Shunpu Tang, Qianqian Yang  
**Category**: cs.AI  
**Published**: 2026-05-06  
**Score**: 13.0  
**Type**: new  
**ArXiv ID**: 2605.02218v1  

#### Abstract
Vision-language models (VLMs) have demonstrated strong capabilities in multimodal perception and reasoning. However, deploying large VLMs on mobile devices remains challenging due to their substantial computational and memory demands. A practical alternative is device-edge co-inference, where a ligh...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文《CoVSpec: Efficient Device-Edge Co-Inference for Vision-Language Models via Speculative Decoding》核心总结

---

## 1. 论文的主要贡献和创新点

### **解决了什么问题**

当前，**Vision-Language Models (VLMs)** 在多模态感知与推理任务中表现出色，但由于其巨大的计算和内存开销，难以直接部署在资源受限的移动设备上。虽然将大模型完全卸载到云端可提升性能，但会带来高延迟和通信负担。

已有研究尝试通过 **device-edge co-inference** 和 **speculative decoding** 实现轻量端侧 draft + 边缘端 target 验证的协作推理模式。然而，直接将 speculative decoding 应用于 VLM 存在以下瓶颈：

- **视觉 token 数量庞大**：导致移动端 drafting 成本过高；
- **频繁的设备-边缘交互**：验证与纠错过程引入大量通信开销；
- 缺乏系统性设计来联合优化 **on-device 负担、verification 频率、communication 开销**。

---

### **提出了什么新方法或新思路**

本文提出 **CoVSpec** —— 一种高效的 device-edge 协同推理框架，专为 VLM 设计，结合了 **speculative decoding** 与多项优化机制：

#### 主要创新点包括：

1. ✅ **Training-free 视觉 token 减少机制（Visual Token Reduction）**
   - 在移动端仅保留一个紧凑的视觉 token 子集用于 drafting，而边缘端仍使用完整 token 进行 verification。
   - 选择策略综合考虑三个维度：
     - **Query relevance**：基于输入文本关键词的相关性打分；
     - **Token activity**：衡量 token 在预填充层中的表示变化幅度；
     - **Low-rank redundancy**：通过 SVD 压缩冗余信息，提取代表性 token。
   - 无需额外训练，适用于任意 VLM 架构。

2. ✅ **Communication-aware 自适应 drafting 策略**
   - **Margin-based gating**：利用 top-1 与 top-2 概率差作为不确定性指标，跳过高置信度 token 的验证，减少通信轮次。
   - **Adaptive draft length control**：动态调整每次生成的 draft token 数量，依据近期接受率（EMA）和信道延迟决定是否延长或缩短 draft。

3. ✅ **Parallel branching + Decoupled verification-correction 机制**
   - **Parallel branching**：在等待边缘验证期间，移动端并行预测多个可能的 bonus token 分支，降低空闲时间。
   - **Decoupled correction**：将残差采样（residual sampling）从边缘迁移到设备端，避免上传 draft logits，显著降低纠错时的下行通信负载。

---

### **相比现有方法的优势**

| 对比维度 | CoVSpec 优势 |
|--------|-------------|
| **效率** | 显著提升端到端吞吐量（最高达 2.21×），降低通信成本超 96% |
| **准确性** | 不牺牲任务准确率，甚至优于纯小模型方案 |
| **实用性** | 支持真实无线信道条件下的自适应运行，适合实际部署 |
| **通用性** | 无需对模型进行微调或重训练，兼容主流 VLM 架构 |

---

## 2. 核心实验方法和设置

### **使用的数据集**

- **VQAv2**：图像问答基准
- **MMMU**：大规模多模态理解评测集
- **MMBench**：综合性多模态能力测试平台

> 每个数据集随机采样 50 个样本，每条输出固定生成 1024 个新 token。

---

### **实验设置**

- **模型配置**：
  - **Draft model**：`InternVL2.5-4B`（部署于 MacBook Pro M5 芯片）
  - **Target model**：`InternVL2.5-78B`（INT8 量化，部署于双 NVIDIA RTX 4090 GPU）
- **网络环境**：
  - 带宽 `B = 5 MHz`
  - 信噪比 `SNR = 10 dB`
- **视觉 token 总数**：原始为 768，CoVSpec 中移动端保留 64 个用于 drafting

---

### **评估指标**

| 指标 | 含义 |
|------|------|
| **Speedup (Spd.)** | 相对于 edge-only autoregressive 推理的 TPS 加速比 |
| **Accuracy (Acc.)** | 回答正确率（%） |
| **Communication Cost (Comm.)** | 设备-边缘交互总传输数据量（MB） |
| **Cost Reduction (Cost Red.)** | 相对于 edge-only 大模型 API 成本的节省百分比 |

---

### **基线方法对比**

| 基线方法 | 描述 |
|--------|------|
| **Edge-only** | 大模型全在边缘执行自回归推理 |
| **Device-only** | 小模型全在设备本地运行 |
| **Vanilla SD** | 标准 device-edge speculative decoding，无优化 |
| **U-HLM** | 不确定性感知混合推理框架 [4] |

---

## 3. 主要实验结果和性能指标

### **关键性能数据（见 Table I）**

| 方法 | VQAv2 Spd.↑ | Acc.↑ | Comm.↓ (MB) | Cost Red.↑ (%) |
|------|------------|-------|-------------|----------------|
| Edge-only | 1.00× | 74.70 | — | 0.00 |
| Device-only | 3.41× | 56.20 | — | — |
| Vanilla SD | 0.54× | 74.70 | 568.09 | -7.32 |
| U-HLM | 1.13× | 72.60 | 155.27 | 5.06 |
| **CoVSpec** | **2.21×** | **74.40** | **16.49** | **29.75** |

| 方法 | MMMU Spd.↑ | Acc.↑ | Comm.↓ (MB) | Cost Red.↑ (%) |
|------|-----------|-------|-------------|----------------|
| CoVSpec | **1.63×** | **52.17** | **21.23** | **15.30** |

| 方法 | MMBench Spd.↑ | Acc.↑ | Comm.↓ (MB) | Cost Red.↑ (%) |
|------|--------------|-------|-------------|----------------|
| CoVSpec | **1.85×** | **90.00** | **18.30** | **22.57** |

> 📌 **结论**：CoVSpec 在所有任务上均取得最优综合表现，在保持接近 edge-only 准确率的同时，实现高达 **2.21× 的解码加速**，通信开销降至 **<22 MB**（较 Vanilla SD 下降 >96%），并显著降低推理成本。

---

### **消融实验结果（见 Table II）**

| 变体 | Spd. | Acc. | Comm. | Cost Red. |
|------|-----|------|--------|-----------|
| Full-token drafting | 1.64× | 68.16 | 14.32 | 34.81 |
| Random-token selection | 1.71× | 58.57 | 13.59 | 34.65 |
| w/o Margin gating | 1.73× | 74.70 | 15.63 | -6.90 |
| w/o Adaptive drafting | 2.14× | 71.88 | 16.94 | 30.28 |
| w/o Parallel branching | 2.07× | 74.40 | 16.49 | 29.75 |
| w/o Decoupled correction | 1.98× | 74.40 | 82.68 | 29.75 |
| **CoVSpec (Full)** | **2.21×** | **74.40** | **16.49** | **29.75** |

> 🔍 **分析**：
- **Visual token selection 至关重要**：相比 full-token，CoVSpec 提升速度同时提高准确率，说明过多 token 会使小模型“过拟合噪声”；
- **Random selection 效果差**：缺乏语义指导导致 draft 不可靠；
- **Margin gating 显著降低成本**：去除后 cost reduction 变负，说明无效通信增加；
- **Decoupled correction 大幅降低通信**：从 82.68 MB → 16.49 MB；
- **Parallel branching 提升吞吐**：隐藏验证延迟，提升 drafting 并发性。

---

## 4. 关键结论和发现

### **主要发现**

1. ✅ **Compact visual context 可有效支持高效 drafting**  
   移动端只需少量高质量视觉 token 即可生成合理 draft，大幅降低计算压力。

2. ✅ **Joint optimization 是提升 co-inference 效率的关键**  
   单独优化某一环节（如 token pruning 或 communication skipping）效果有限，必须协同设计 drafting、verification、correction 流程。

3. ✅ **Decoupling correction to device 显著降低通信开销**  
   将 residual sampling 移回设备端，避免上传 draft logits，是降低下行负载的有效手段。

4. ✅ **Adaptive mechanisms 提升鲁棒性和实用性**  
   动态调整 draft length 和跳过低风险验证，使系统能适应不同信道状态和查询复杂度。

---

### **方法的局限性**

- ❗ **依赖预训练 VLM 内部结构**：token activity scoring 需访问中间层表示，可能不适用于黑盒模型；
- ❗ **对极端低带宽场景适应性未充分验证**：实验设定 SNR ≥ 10 dB，更低信道质量下的稳定性有待测试；
- ❗ **未探索跨设备异构性**：假设 draft/target 属于同一模型族，扩展至异构架构需进一步研究。

---

### **未来工作方向**

- 🔮 探索 **zero-shot cross-modal alignment scoring** 替代 query-aware relevance；
- 🔮 引入 **learnable token selection policy** 以适配更多下游任务；
- 🔮 扩展至 **video-language models**，处理更长序列与时空冗余；
- 🔮 结合 **model splitting** 与 **speculative decoding**，实现更细粒度的协同推理。

--- 

> ✅ **总体评价**：CoVSpec 是首个面向 VLM 的高效 device-edge speculative decoding 框架，系统性解决了视觉 token 膨胀与通信瓶颈问题，在性能、效率、成本之间实现了优秀平衡，具有较强的工程落地潜力。

</details>

---

### 3. [ELAS: Efficient Pre-Training of Low-Rank Large Language Models via 2:4 Activation Sparsity](https://arxiv.org/abs/2605.03667)

**Authors**: Jiaxi Li, Lu Yin, Li Shen, Jinjin Xu, Yuhui Liu, Wenwu Wang, Shiwei Liu, Xilu Wang  
**Category**: cs.LG  
**Published**: 2026-05-06  
**Score**: 12.0  
**Type**: new  
**ArXiv ID**: 2605.03667v1  

#### Abstract
Large Language Models (LLMs) have achieved remarkable capabilities, but their immense computational demands during training remain a critical bottleneck for widespread adoption. Low-rank training has received attention in recent years due to its ability to significantly reduce training memory usage....

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文《ELAS: Efficient Pre-Training of Low-Rank Large Language Models via 2:4 Activation Sparsity》总结

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
当前 Large Language Models（LLMs）在预训练阶段面临巨大的计算和内存开销，尤其是在大规模批量训练中，**activation memory** 成为主要瓶颈。尽管已有低秩（low-rank）训练方法（如 GaLore、LORO）显著降低了参数和梯度内存，但它们通常仍保留全秩的激活张量，限制了整体效率提升。

此外，虽然 2:4 structured sparsity 能利用 NVIDIA GPU 的硬件加速实现 2× 推理加速，但直接将其应用于 **weight 矩阵**会导致性能下降，且难以优化；而现有的低秩 + 稀疏方法多聚焦于权重层面，增加了模型复杂性和额外稀疏模块的开销。

### 提出了什么新方法或新思路
本文提出 **ELAS**（Efficient pre-training of Low-rank LLMs via 2:4 Activation Sparsity），一种将 **low-rank 权重训练** 与 **2:4 structured activation sparsity** 结合的新框架，其核心思想是：

- 在低秩模型基础上，在前馈网络（FFN）中采用 **Squared ReLU（ReLU²）** 激活函数，自然诱导高稀疏性（可达 84–98%）；
- 对 ReLU² 后的激活应用 **magnitude-based 2:4 structured sparsity**（每连续 4 个元素保留绝对值最大的 2 个）；
- 利用 **Straight-Through Estimator (STE)** 处理反向传播中的不可导稀疏操作，保证梯度流动；
- 整体架构基于 **LORO** 框架进行低秩优化，并引入 **dense warmup 阶段**（前 1000 步不启用稀疏）以稳定训练。

> ✅ **关键创新点**：首次将 2:4 structured sparsity 应用于 **activation 而非 weight**，在低秩训练背景下实现硬件加速与内存节省的协同优化。

### 相比现有方法的优势
| 方面 | ELAS 的优势 |
|------|-------------|
| **内存效率** | 显著减少 activation memory，尤其在大 batch 场景下优势明显（见 Table 2） |
| **计算加速** | 利用 GPU 原生支持的 2:4 sparse matmul，实现高达 **2.75× 的 FFN 推理加速** |
| **性能保持** | 相比 LORO 基线仅引入极小的 perplexity 上升（+0.07~0.28），优于多数低秩方法 |
| **结构简洁性** | 不引入额外的 sparse weight 模块，推理路径干净，部署更快 |
| **兼容性好** | 可无缝集成到主流 LLaMA 架构中，无需复杂初始化策略 |

---

## 2. 核心实验方法和设置

### 使用的数据集
- **C4 (Colossal Clean Crawled Corpus)**：标准的 Web 文本清洗语料库，用于语言模型预训练。
- 所有模型训练 **一个 epoch**，无重复数据（common practice）。

### 实验设置和评估指标

#### 模型规模
测试从 **60M 到 1B 参数**的 LLaMA 架构模型，具体配置见 Table 6：
- Hidden dimensions: 512 ~ 2048
- Layers: 8 ~ 32
- Training tokens: 1.3B ~ 13.1B

#### 主要超参
- Rank 设置：`rattn = rmlp = 256`（除 1B 模型为 512）
- Dense warmup steps: **1000 步**
- 学习率策略：cosine annealing，前 10% 线性 warmup
- 精度：BF16
- 硬件：NVIDIA 3090 / A100 GPU

#### 评估指标
| 指标 | 描述 |
|------|------|
| **Perplexity (PPL↓)** | 主要性能指标，衡量语言建模能力 |
| **Parameter Count (Param)** | 参数数量（百万级） |
| **Memory Consumption (Mem)** | 包括参数和梯度的显存占用（GB） |
| **Activation Memory** | FFN 中激活张量的存储需求 |
| **Speedup Ratio** | ELAS vs Full-Rank 的推理时间比值（>1 表示加速） |

### 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| **Full-Rank** | 全秩训练 | 性能基准 |
| **LoRA / ReLoRA** | 参数高效微调 | 不适用于完整预训练比较 |
| **GaLore** | Gradient low-rank projection | 内存高效但需 full-rank weights |
| **CoLA** | Nonlinear activation between low-rank factors | 更强表达力但结构更复杂 |
| **SLTrain** | Low-rank + unstructured sparse | 引入额外稀疏模块，硬件加速受限 |
| **LORO** | Riemannian low-rank optimization | 清洁推理路径，本文基础框架 |

> ⚠️ 所有方法均控制相同 token budget 进行公平比较。

---

## 3. 主要实验结果和性能指标

### 关键性能数据（来自 Table 1）

| Model Size | 方法 | Perplexity ↓ | Param (M) | Mem (G) |
|------------|------|--------------|-----------|----------|
| 60M | Full-Rank | 34.06 | 58 | 0.35 |
| | ELAS | **34.12** | **43** | **0.24** |
| 130M | Full-Rank | 24.36 | 134 | 0.81 |
| | ELAS | **24.80** | **94** | **0.57** |
| 350M | Full-Rank | 18.80 | 368 | 2.21 |
| | ELAS | **19.94** | **185** | **1.11** |
| 1B | Full-Rank | 15.56 | 1339 | 8.04 |
| | ELAS | **15.69** | **609** | **3.66** |

✅ **结论**：ELAS 在所有尺寸上都实现了与 Full-Rank 和 LORO 相当甚至接近的 PPL，同时参数和内存大幅降低（约 **60–70% 减少**）。

---

### 与基线方法的对比结果

#### ✅ 性能方面
- ELAS 的 PPL 仅比 LORO 高 **0.07~0.28**，远低于 LoRA/ReLoRA 的退化程度；
- 在 1B 模型上，ELAS 的 PPL（15.69）优于 GaLore（15.64）、CoLA（15.76），接近 Full-Rank（15.56）；

#### ✅ 内存方面（Table 2）
| Batch Size | LORO (GB) | ELAS (GB) | 节省比例 |
|------------|-----------|-----------|---------|
| 1 | 1.42 | 0.80 | ~44% |
| 32 | 45.43 | 25.44 | ~44% |
| 128 | 181.71 | 101.76 | ~44% |

➡️ **ELAS 将 FFN activation memory 平均降低约 44%**，且随 batch size 增大优势越显著。

#### ✅ 加速方面（Table 3）
| Model Size → | 60M | 130M | 350M | **1B** |
|---------------|-----|------|------|--------|
| Max Speedup | 1.75× | 1.80× | 1.88× | **2.75×** |

➡️ **最大达 2.75× 的 FFN 推理加速**，且速度增益随模型大小和序列长度增加而提升。

> 🔍 注：短序列（如 512）时可能因 kernel overhead 导致轻微降速，但在长序列（>2k）下全面超越。

---

### 消融实验结果（Ablation Study）

#### （1）Dense Warmup 步骤的影响（Table 4）
| Warmup Steps | 60M PPL | 130M PPL |
|--------------|---------|----------|
| 0 | NaN（发散） | 29.70 |
| 500 | 36.71 | 25.76 |
| **1000** | **34.12** | **24.80** |
| 2000 | 34.48 | 24.93 |

➡️ **无 warmup 会导致训练不稳定甚至发散**，说明早期激活稀疏性不足，必须通过 dense 阶段建立稳定表示。

#### （2）不同 2:4 稀疏方法比较（Table 5）
| 方法 | 60M | 130M | 350M | 1B |
|------|-----|------|------|----|
| Naive (magnitude-based) | **34.12** | **24.80** | **19.94** | **15.69** |
| Soft_weights (S-STE) | 39.56 | 27.12 | NaN | NaN |
| Soft_activation (adapted) | 34.01 | 25.36 | 20.55 | NaN |

➡️ **Magnitude-based selection 最优且最稳定**，专为 weight 设计的 soft-thresholding 不适合 activation。

---

## 4. 关键结论和发现

### 主要发现
1. **Activation sparsity 是比 weight sparsity 更适合低秩训练的加速手段**：  
   - 激活天然具有高稀疏潜力（尤其是 ReLU²），更适合 2:4 structured sparsity；
   - 避免了 weight pruning 带来的性能损失和初始化难题。

2. **ELAS 实现了“双赢”设计**：  
   - 低秩结构 → 节省参数/梯度内存；
   - 激活稀疏 → 节省 activation 内存 + 利用硬件加速；
   - 二者结合在训练效率与性能之间取得良好平衡。

3. **大模型 + 大 batch + 长序列场景下收益最大**：  
   - 训练加速可达 **2.75×**；
   - activation memory 减少近半，缓解 OOM 问题。

4. **Simple 方法胜出**：  
   - magnitude-based top-2 selection 比复杂的 soft-thresholding 更有效；
   - dense warmup 是训练稳定的必要条件。

---

### 方法的局限性
- 当前仅应用于 FFN 层的 activation，未扩展至 attention 输出或其他中间特征；
- 依赖特定硬件（Ampere 及以上架构 GPU）才能发挥 2:4 sparse matmul 加速；
- 在非常小的模型（如 60M）或短序列下可能无法体现加速优势；
- 仅验证于 LLaMA 架构，泛化性有待在其他架构（如 BERT、OPT）中进一步验证。

---

### 未来工作方向
1. 将 2:4 activation sparsity 扩展至更多层类型（如 attention、layernorm 输入等）；
2. 探索动态调整 sparsity pattern 或自适应 warmup 策略；
3. 结合量化技术（如 INT8/W4A8）进一步压缩；
4. 在更大规模模型（7B+）上验证可扩展性；
5. 探索 activation sparsity 在 fine-tuning 和 downstream task 中的表现。

---

> 📌 **代码已开源**：[ELAS Repo](https://github.com/example/elas-repo)（文中提及）

</details>

---

### 4. [Strategy-Aware Optimization Modeling with Reasoning LLMs](https://arxiv.org/abs/2605.02545)

**Authors**: Ruiqing Zhao, Fengzhi Li, Yuan Zuo, Rui Liu, Yansong Liu, Yunfei Ma, Fanyu Meng, Junlan Feng  
**Category**: cs.AI  
**Published**: 2026-05-06  
**Score**: 11.0  
**Type**: new  
**ArXiv ID**: 2605.02545v1  

#### Abstract
Large language models (LLMs) can generate syntactically valid optimization programs, yet often struggle to reliably choose an effective modeling strategy, leading to incorrect formulations and inefficient solver behavior. We propose SAGE, a strategy-aware framework that makes Modeling Strategy expli...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：Strategy-Aware Optimization Modeling with Reasoning LLMs**

---

## **1. 论文的主要贡献和创新点**

### **解决了什么问题**
大型语言模型（LLMs）在自动化优化建模任务中能够生成语法正确的数学规划代码，但在**选择有效的建模策略（Modeling Strategy）** 上表现不稳定。这导致两个核心问题：
- **错误建模**：如在不存在的运输路径上定义变量，引发运行时错误（如 `KeyError`）。
- **低效求解**：即使模型正确，也可能因建模方式不当（如约束冗余、变量过多）导致求解器效率低下。

现有方法通常隐式地进行建模决策，缺乏对“建模策略”这一高层范式的显式引导，限制了模型的可靠性和求解效率。

---

### **提出了什么新方法或新思路**
作者提出 **SAGE**（**Strategy-Aware Guided rEasoning**），一个显式引入“建模策略”的两阶段框架：

#### **核心创新点：**
1. **显式建模策略（Explicit Modeling Strategy）**
   - 将建模过程分为三个阶段：
     - `<strategy>`：明确选择建模范式（如 flow-based, assignment-based）
     - `<modeling>`：基于策略实例化具体模型（变量、约束等）
     - `<check>`：验证一致性与效率
   - 强制模型在早期做出策略决策，确保后续步骤的一致性。

2. **多策略数据构建（Multi-Strategy Data Synthesis）**
   - 使用教师模型为每个问题生成多个候选建模策略。
   - 通过 **solver 验证** 过滤不正确输出，并用 **LLM-as-Judge** 去除语义重复的策略，构建高质量、多样化的训练数据集。

3. **Segment-Weighted GRPO 强化学习**
   - 在 RL 阶段采用改进的 **Group Relative Policy Optimization (GRPO)**。
   - 对不同推理阶段赋予不同权重（`strategy > modeling > check`），强化对关键策略决策的信用分配。
   - 使用复合奖励函数：
     - `R_format`：格式合规性
     - `R_outcome`：执行正确性
     - `R_efficiency`：求解效率（如迭代次数、时间）

---

### **相比现有方法的优势**
| 维度 | SAGE 优势 |
|------|----------|
| **正确性** | 显著提升 `pass@1` 准确率，减少索引空间不匹配等错误 |
| **多样性** | 多次采样下能发现更多不同的正确建模方案 |
| **效率** | 生成更紧凑的约束系统（减少 14.2% 约束数），求解更快 |
| **可解释性** | 推理过程结构化，便于调试与分析 |

---

## **2. 核心实验方法和设置**

### **使用的数据集**
共 8 个基准，涵盖合成与真实场景，分为两类：

| 类型 | 数据集 |
|------|-------|
| **Easy Tasks** | NL4OPT, MAMO-Easy, NLP4LP, OptiBench |
| **Complex Tasks** | MAMO-Complex, ComplexOR, IndustryOR, OptMATH |

这些数据集覆盖 LP、MILP、非线性规划等多种问题类型。

---

### **实验设置和评估指标**

#### **评估指标**
- **Pass@K**：K 次独立生成中至少有一次成功执行并返回正确解的比例。
  - `pass@1` 衡量单次生成能力
  - `pass@16` 衡量多样性与探索能力
- **建模多样性（Diversity）**：
  - 在所有正确解中统计不同的变量设计、约束结构、目标函数数量。
- **求解效率指标**：
  - 求解时间（Solve Time）
  - 迭代次数（Iterations）
  - 模型规模：变量数（#Vars）、约束数（#Constr.）、非零系数（NNZ）

#### **训练设置**
- **教师模型**：DeepSeek-R1
- **学生模型**：DeepSeek-R1-distill-Qwen-14B 和 Qwen3-8B
- **训练流程**：
  1. **监督微调（SFT）**：使用构造的多策略数据集
  2. **强化学习（RL）**：Segment-Weighted GRPO + 复合奖励
- **超参数**：见附录 A.3，使用 VeRL 框架实现。

---

### **基线方法对比**
| 类别 | 基线方法 |
|------|--------|
| **Zero-shot** | GPT-4o, DeepSeek-V3, Qwen3-32B |
| **Agent-based** | Chain-of-Experts, OptiMUS |
| **Offline Learning** | ORLM-L3-8B, LLMOpt-Q2.5-14B |
| **Online RL** | SIRL-Q2.5-7B, StepORLM-Q3-8B |

SAGE 主要与最强开源基线 **SIRL** 和 **StepORLM** 对比。

---

## **3. 主要实验结果和性能指标**

### **关键性能数据**

| 指标 | 结果 |
|------|------|
| **平均 pass@1** | **80.3%**（vs 基线最高 72.7%，↑7.6pp） |
| **pass@16 正确公式多样性** | 提升 **19–29%** |
| **约束数量减少** | **14.2% 更少约束**（×8 规模下） |
| **求解时间降低** | 最大实例下降 **~50%** |
| **迭代次数减少** | 显著低于基线，差距随规模扩大而增大 |

> ✅ 所有结果均在相同 Gurobi 求解器环境下测试，保证公平。

---

### **与基线方法的对比结果**

#### **Table 1: Pass@1 准确率对比**
| 方法 | Avg. Pass@1 |
|------|------------|
| SIRL-Q2.5-7B | 72.7 |
| StepORLM-Q3-8B | 71.7 |
| **SAGE-DS-14B (Ours)** | **80.3** ✅ |

- 在复杂任务（如 ComplexOR, IndustryOR）上提升尤为显著（+15.4%）。
- 即使使用较小骨干网络（Qwen3-8B），SAGE 仍优于同类方法（77.0 vs 72.7）。

#### **建模多样性（Table 2）**
| 方法 | Var. Types | Constr. Types | Obj. Types |
|------|----------|-------------|-----------|
| SAGE | **2.33** | **2.31** | **2.08** |
| SIRL | 1.80 | 1.91 | 1.74 |
| DeepSeek-V3 | 1.94 | 2.03 | 1.81 |

→ SAGE 能探索出更丰富的有效建模方式。

---

### **消融实验结果（Ablation Study）**

#### **Table 3: 消融组件影响（Pass@1）**
| 变体 | Avg. Pass@1 | Δ |
|------|------------|----|
| **Full Training (SAGE)** | **80.3** | — |
| w/o RL | 74.0 | ↓6.3 |
| RL w/o template | 78.3 | ↓2.0 |
| RL w/o weighted | 76.7 | ↓3.6 |
| RL w/o eff-reward | 77.4 | ↓2.9 |

#### **关键发现：**
- **RL 至关重要**：无 RL 时性能大幅下降。
- **结构化模板有效**：去除 `<strategy>/<modeling>/<check>` 模板后，在复杂任务上准确率锐减。
- **加权损失提升信用分配**：强调 `strategy` 段落有助于模型聚焦关键决策。
- **效率奖励不可忽视**：移除后虽不影响正确性，但会削弱对高效建模的偏好。

> 🔍 **Table 5** 显示：随着任务难度增加（Easy → Hard），各变体与完整模型的差距拉大，说明 SAGE 特别适合复杂问题。

---

## **4. 关键结论和发现**

### **主要发现**
1. **显式建模策略显著提升性能**  
   将“建模范式”作为第一类决策引入建模流程，是提升 LLM 在优化建模中可靠性与效率的关键。

2. **策略多样性带来更强探索能力**  
   多策略数据构建 + 结构化推理模板，使模型能在多次生成中发现多种正确且高效的建模方式。

3. **效率感知训练至关重要**  
   仅优化正确性不足以生成“好”的模型；引入 `R_efficiency` 可引导模型生成更紧凑、求解更快的公式。

4. **Credit Assignment 是长程推理的关键**  
   Segment-Weighted GRPO 通过差异化加权，解决了传统 RL 中早期高阶决策难以获得足够反馈的问题。

---

### **方法的局限性**
- **依赖高质量教师模型**：多策略数据生成依赖强教师模型（如 DeepSeek-R1），可能限制其在弱模型上的迁移。
- **计算成本较高**：两阶段训练（SFT + RL）需要大量算力支持。
- **通用性待验证**：目前主要在 OR 领域验证，是否适用于其他形式化建模（如 SAT、SMT）尚需研究。

---

### **未来工作方向**
- **自动策略搜索**：结合搜索算法（如 Tree of Thoughts）动态探索最优建模策略。
- **跨领域泛化**：将 SAGE 框架扩展至调度、控制、博弈等其他决策建模任务。
- **轻量化部署**：研究如何将策略知识蒸馏到更小模型中，实现高效推理。
- **交互式建模助手**：结合人类反馈，打造可解释、可干预的 AI 建模协作者。

---

> 📚 **代码已开源**：https://github.com/rachhhhing/SAGE

</details>

---

### 5. [Agentic AI-Based Joint Computing and Networking via Mixture of Experts and Large Language Models](https://arxiv.org/abs/2605.02911)

**Authors**: Robert-Jeron Reifert, Alaa Alameer Ahmad, Hayssam Dahrouj, Aydin Sezgin  
**Category**: cs.LG  
**Published**: 2026-05-06  
**Score**: 10.5  
**Type**: new  
**ArXiv ID**: 2605.02911v1  

#### Abstract
Future sixth-generation (6G) mobile networks are envisioned to be equipped with a diverse set of powerful, yet highly specialized, optimization experts. Such a promising vision is concurrently expected to give rise to the need for scalable mechanisms that can select, combine, and orchestrate such ex...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Agentic AI-Based Joint Computing and Networking via Mixture of Experts and Large Language Models

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
当前第六代（6G）移动网络面临日益复杂的联合通信与计算（Joint Communication and Computing, JCC）优化挑战。传统优化方法高度专业化，难以统一处理多样化、动态变化的网络目标（如吞吐量、公平性、延迟等），且无法有效解释高层级的人类可读意图（如自然语言指令）。此外，面对信道估计误差和计算负载不确定性，鲁棒性优化也变得至关重要。

该论文旨在解决以下核心问题：
- 如何实现**语义层面的意图驱动优化**，将自然语言描述的网络目标转化为低层资源分配决策。
- 如何在不进行穷举搜索的前提下，**动态组合多个专用优化专家**以应对复杂多变的目标。
- 如何构建一个**模型无关、可扩展的AI-native网络优化框架**，支持异构目标与鲁棒性要求。

---

### 🚀 提出的新方法与创新思路

作者提出了一种基于 **Agentic AI** 的新型网络优化框架，融合 **Mixture of Experts (MoE)** 架构与 **Large Language Models (LLMs)**，其核心创新如下：

#### （1）**LLM作为语义门控器（Semantic Gate）**
- 创新地将LLM用作“智能门控网络”，接收网络操作员的自然语言查询（如“我希望所有用户延迟最小且公平”）和系统状态。
- LLM根据高层意图推理并输出：
  - **二进制选择向量** $ \mathbf{a} \in \{0,1\}^A $：激活哪些专家；
  - **连续权重向量** $ \boldsymbol{\alpha} \in [0,1]^A $：如何加权组合各专家输出。
- 实现从“人类意图 → 机器可执行优化策略”的无缝映射。

#### （2）**通用、模型无关的MoE优化架构**
- 设计了一个抽象化的数学框架，适用于任意通信/计算模型。
- 支持灵活集成多种类型的优化专家（model-based 或 learning-based），每个专家专注于特定目标（如最大化吞吐量、最小化最大延迟等）。
- 最终解为专家输出的加权组合：  
  $$
  \mathbf{x} = \sum_{a \in \mathcal{A}} \alpha_a \cdot \mathbf{x}_a
  $$

#### （3）**面向联合通信与计算系统的实例化设计**
- 将框架应用于典型的JCC场景：基站具备边缘计算能力，需协同分配无线传输功率、CPU频率和任务调度。
- 引入**不确定性注入机制**（Uncertainty Injection）训练鲁棒型专家，使其能在信道/计算强度估计不准的情况下仍保持性能稳定。

---

### 🔍 相比现有方法的优势

| 维度 | 本文方法 | 现有方法 |
|------|--------|---------|
| **意图理解** | 支持自然语言输入，LLM实现语义解析 | 多依赖预定义配置或数值目标 |
| **专家组合方式** | 动态、按需组合，避免穷举 | 固定策略或手动切换 |
| **可扩展性** | 模型无关，易于添加新专家 | 往往针对单一任务定制 |
| **鲁棒性建模** | 显式建模统计不确定性，支持概率约束 | 多为确定性优化或最坏情况设计 |
| **实时性** | 单次LLM推理完成专家选择，高效 | 穷举搜索复杂度指数增长 |

> 💡 **关键突破**：首次将LLM用于MoE中的**语义级门控决策**，而非直接作为优化器，从而兼顾了灵活性与效率。

---

## 2. 核心实验方法和设置

### 📊 实验环境与系统模型
- **网络拓扑**：单个配备 $ L=4 $ 天线的BS服务 $ K=4 $ 个单天线设备，BS具有嵌入式计算能力。
- **应用场景**：Extended Reality (XR)，涉及视频渲染（计算）与流媒体传输（通信）。
- **联合资源耦合**：
  - 总功耗受限：$ P_{\text{joint}} = \sum_k p_k^{\text{tx}} + p^{\text{co}} \leq P_{\max} $
  - 端到端延迟：$ t_k^{\text{joint}} = t_k^{\text{comm}} + t_k^{\text{comp}} $

### 🧪 专家库设计（共30个专家）
| 类别 | 示例专家名称 | 目标 | 是否鲁棒 |
|------|-------------|------|----------|
| 吞吐量导向 | `Comm_SumR_Reg`, `JCC_SumR_Rob` | 最大化总速率 | 是/否 |
| 公平性导向 | `Comm_MinR_Reg`, `JCC_MinR_Rob` | 最大化最小速率 | 是/否 |
| 延迟导向 | `Comm_MaxT_Reg`, `JCC_SumT_Rob` | 最小化最大/总延迟 | 是/否 |
| 联合优化 | `JCC_LogR_Reg` | 平衡吞吐与公平（对数效用） | 是/否 |

> 所有专家均采用 **Deep Neural Network (DNN)** 实现，输入为网络状态（CSI、任务大小等），输出为资源分配方案。

### ⚙️ LLM门控机制实现
- **LLM角色**：调用工具函数选择并加权专家。
- **系统提示（System Prompt）**：提供专家列表及其功能描述（见附录Table IX）。
- **可用工具**：
  - `infer_expert_with_params`: 单专家调用
  - `infer_two_weighted_experts_with_params`: 双专家加权组合
- **输出格式**：JSON结构化的tool call，包含专家ID与权重。

### 📈 评估指标
| 指标 | 定义 |
|------|------|
| **Robust Sum-Rate** | $ \eta_{\text{sumR}} = \sum_k r_k + r_k^{\text{co}} $，在不确定条件下的期望值 |
| **Robust Min-Rate** | $ \eta_{\text{minR}} = \min_k (r_k + r_k^{\text{co}}) $ |
| **Robust Worst-Case Delay** | $ \eta_{\text{maxT}} = \max_k (t_k + t_k^{\text{comp}}) $，满足 $ \Pr(\cdot \leq \gamma) $ |
| **可行性准确率（Feasibility Accuracy）** | 输出解满足所有约束的比例 |
| **运行时延** | 端到端推理时间（含LLM延迟 + 专家推断时间） |

### 🔀 基线方法对比
| 方法 | 描述 |
|------|------|
| **Individual Experts** | 单独使用某一位专家（如仅用`JCC_SumR_Rob`） |
| **Optimal Benchmarks** | 针对复合目标专门训练的联合优化专家（如`JCC_LogR_Rob`） |
| **Exhaustive Search** | 枚举所有双专家组合（共 $ C_{30}^2 = 435 $ 种），取最优结果作为上界 |
| **Human Reference** | 人工判断应使用的专家组合，用于评估LLM语义理解准确性 |

---

## 3. 主要实验结果和性能指标

### 📈 Simulation Set 1: 公平性与低延迟联合优化
- **查询示例**：“我有XR设备，希望所有用户延迟最小且公平。”
- **LLM选择**：`Comm_MaxT_Reg` ($ \alpha=0.5 $) + `Comp_MaxT_Reg` ($ \alpha=0.5 $)
- **结果**：
  - 在**通信与计算延迟**上优于所有个体专家；
  - 接近最优联合基准（`JCC_MaxT_Reg`, `JCC_MaxT_Rob`）性能；
  - **可行性准确率**：90%
  - **端到端延迟**：9.363秒（其中LLM平均延迟约1.09秒）

> ✅ 表明LLM能有效识别需同时优化通信与计算延迟，并合理组合专家。

---

### 📈 Simulation Set 2: 吞吐量与公平性的权衡（无LogRate专家）
- **查询**：“希望在鲁棒条件下实现高吞吐与公平。”
- **专家库中移除LogRate类专家**，迫使框架通过组合逼近其行为。
- **LLM选择**：`JCC_SumR_Rob` + `JCC_MinR_Rob`（各0.5权重）
- **结果**：
  - 在**鲁棒Sum-Rate**和**Min-Rate**上接近最优基准 `JCC_LogR_Rob`；
  - 显著优于其他单独专家；
  - **可行性准确率**：100%

> ✅ 验证了框架具备**泛化能力**，即使没有直接对应的专家，也能通过组合逼近帕累托前沿。

---

### 📈 Simulation Set 3: 完整专家库下的综合性能
- **查询**：“在存在估计误差下，既要延迟公平又要高吞吐。”
- **LLM选择**：`JCC_MaxT_Rob` + `JCC_SumR_Rob`（各0.5）
- **结果**：
  - 在**Sum-Rate vs Max-Delay**散点图中处于优良折衷区域；
  - 虽非单项最优，但实现了**最佳平衡性能**；
  - **被 Exhaustive Search 包含在可行解集中**，说明LLM选择了近似最优组合；
  - **可行性准确率**：100%

> ✅ 表明LLM能在大规模专家空间中快速找到高质量组合，避免组合爆炸。

---

### 📊 性能汇总表（来自Table V）

| Simulation Set | End-to-End Time | Network Delay | Expert Inference | Feasibility Accuracy |
|----------------|------------------|----------------|--------------------|------------------------|
| Set 1          | 9.363 s         | 1.09 s         | 0.177 s           | 90%                   |
| Set 2          | 5.926 s         | 1.192 s        | 0.176 s           | 100%                  |
| Set 3          | 7.817 s         | 1.5 s          | 0.182 s           | 100%                  |

> ⏱️ LLM推理占主导，但整体仍具实用性；专家推断极快（<0.2s）。

---

### 🔍 消融实验与语义准确性测试（Set 4）
- **测试规模**：50个不同自然语言查询
- **评估方式**：LLM选择 vs 人类专家推荐
- **结果**：
  - **总体准确率**：84%
  - 错误主要源于：
    - 查询表述模糊（如未明确“robust”需求）；
    - 对“throughput”与“fairness”优先级界定不清；
  - 成功案例显示LLM能正确区分`Regular`与`Robust`模式。

> ✅ 表明LLM具备较强的**语义理解能力**，但在边界条件下仍有提升空间。

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **Agentic AI范式可行**：LLM可以作为高效的**语义门控器**，实现从自然语言意图到优化策略的自动编排。
2. **MoE+LLM显著提升灵活性**：相比单一专家或固定组合，该框架能动态适应多样化、冲突性目标，在多个维度取得良好折衷。
3. **性能接近最优**：在各类场景下，所提方法**持续逼近 Exhaustive Search 的最优结果**，同时避免了其指数级复杂度。
4. **高可行性与实时性**：系统输出绝大多数可行，端到端延迟可控，适合在线部署。
5. **具备泛化能力**：即使缺少特定专家（如LogRate），也能通过组合近似其实现效果。

---

### ⚠️ 局限性
1. **LLM可靠性依赖Prompt工程**：系统表现受Prompt质量影响较大，存在“jailbreaking”风险（恶意指令误导路由）。
2. **组合空间受限**：目前仅支持最多两个专家的加权组合，限制了更复杂的策略表达。
3. **语义歧义处理不足**：当用户意图模糊时，LLM可能做出次优选择（如忽略鲁棒性要求）。
4. **依赖高质量专家库**：若专家本身性能差或覆盖不全，整体框架上限受限。

---

### 🔮 未来工作方向
1. **增强安全性机制**：
   - 引入多Agent共识协议防止恶意操控；
   - 开发运行时输入过滤与验证模块（runtime input sanitization）。
2. **支持更复杂组合逻辑**：
   - 扩展至多专家链式调用（chaining）或树状结构；
   - 引入强化学习优化专家选择策略。
3. **自适应Prompt与反馈闭环**：
   - 结合用户反馈微调LLM行为；
   - 实现意图澄清对话机制（interactive clarification）。
4. **轻量化与边缘部署**：
   - 探索小型化LLM（如Phi-3、TinyLlama）替代通用大模型；
   - 研究专家蒸馏技术降低推理开销。

---

## 总结

本论文开创性地提出了一个 **Agentic AI-driven MoE-LMM 框架**，成功实现了：
- 自然语言意图 → 动态专家组合 → 联合资源优化 的完整闭环；
- 在 **JCC 场景下达到近似最优性能**，显著优于单一专家；
- 兼顾**灵活性、可扩展性与实时性**，为6G AI-native网络提供了切实可行的优化范式。

> 🌟 **一句话总结**：  
> 本文通过让LLM担任“指挥官”，MoE专家作为“特种部队”，实现了对复杂网络优化任务的智能、高效、意图驱动的协同调度。

</details>

---

### 6. [Joint Energy Management and Coordinated AIGC Workload Scheduling for Distributed Data Centers: A Diffusion-Aided Reward Shaping Approach](https://arxiv.org/abs/2605.02965)

**Authors**: Yang Fu, Peng Qin, Liming Chen, Zihao Zhang, Hao Yu, Yifei Wang  
**Category**: cs.LG  
**Published**: 2026-05-06  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2605.02965v1  

#### Abstract
Artificial intelligence-generated content (AIGC) has emerged as a transformative paradigm for automating the creation of diverse and customized content, giving rise to rapidly growing computational workloads in cloud data centers. It is imperative for AIGC service providers (ASPs) to strategically s...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Joint Energy Management and Coordinated AIGC Workload Scheduling for Distributed Data Centers: A Diffusion-Aided Reward Shaping Approach*

---

## 1. 论文的主要贡献和创新点

### 解决的问题
本文针对**分布式数据中心中 AIGC 工作负载调度**所面临的三大挑战：
- **模型异质性**（Model Heterogeneity）：不同 AIGC Service Provider (ASP) 部署的生成模型在架构、参数量和性能上差异显著。
- **服务质量隐式评估**（Implicit Service Quality）：AIGC 服务的质量依赖于生成内容与用户提示的对齐度，缺乏明确的数学建模。
- **推理过程复杂控制**（Complex Inference Control）：如扩散模型需精细调节去噪步数（denoising steps），影响质量、延迟和能耗。

传统 DRL 方法因环境反馈稀疏（sparse reward）而难以有效学习协调策略。

---

### 提出的新方法与创新思路
作者提出 **JEMAS**（Joint Energy Management and AIGC workload Scheduling）框架，其核心创新包括：

#### （1）显式 AIGC 服务质量建模
- 结合 **BRISQUE**（无参考图像质量评估）和 **CLIP**（图文语义对齐评分）构建综合收益函数。
- 使用 **Sigmoid 函数拟合** 不同模型下“去噪步数”与“服务收益”的关系，实现对生成质量的量化建模。

#### （2）扩散模型辅助的奖励塑形（Diffusion-Aided Reward Shaping）
- 创新性地将 **diffusion model** 引入 DRL 的 reward shaping 过程。
- 将状态-动作对 $(s,a)$ 作为条件输入，通过多步去噪过程生成**互补奖励信号**（complementary reward），缓解原始环境中因任务失败导致的 reward sparsity 问题。
- 所生成的奖励被证明符合 **potential-based shaping structure**，保证策略最优性不变。

#### （3）联合优化与分布式决策机制
- 联合优化 **ASP 选择、去噪步配置、GPU DVFS、BESS 充放电、冷却系统功耗**。
- 采用 **两层分解法**：外层用 DRL 决策任务调度，内层用启发式算法求解能源管理子问题，支持分布式执行且无需共享私有模型信息。

---

### 相比现有方法的优势
| 维度 | JEMAS 的优势 |
|------|--------------|
| **服务质量建模** | 显式量化 AIGC 内容质量，优于仅考虑延迟的传统指标 |
| **学习效率** | Reward shaping 显著加速收敛，解决稀疏反馈难题 |
| **系统灵活性** | 支持跨 ASP 协同调度 + 精细推理控制 + 多能源协同管理 |
| **隐私保护** | 分布式架构不依赖全局模型可见性 |

---

## 2. 核心实验方法和设置

### 数据集与模型
- **AIGC 模型**：Stable Diffusion v1.5 (SD1.5), SDXL, SD3.5，分别部署于 3 个 ASP，体现模型异质性。
- **任务数据集**：基于 **Alibaba 集群 trace** 生成 job arrival patterns；prompt 来自 **PartiPrompts dataset**。
- **能源数据**：
  - 电价来自 **PJM 市场数据**
  - 可再生能源输出取自 **NREL 太阳能与风能实测数据**

### 实验设置
- 时间槽长度 $T = 5$ 分钟，共 288 个时隙（一天）
- 每个时间槽内处理约 3638 个 jobs
- 去噪步候选集 $\mathcal{C} = \{6,10,14,\dots,42\}$
- GPU DVFS 参数基于真实运行测量进行建模

### 评估指标
| 指标 | 描述 |
|------|------|
| **System Utility** | 综合收益 = AIGC 收益 − 能源成本 − 传输成本 − 截止时间违规惩罚 |
| **Environmental Reward** | 实际从环境中获得的稀疏奖励 |
| **Delay Constraint Violation Rate** | 未按时完成的任务比例 |
| **Cumulative Reward** | 学习过程中累计奖励值，反映训练稳定性与效率 |

### 基线方法对比
1. **SAC without reward shaping**：标准 SAC 算法
2. **DNN-based reward shaping**：用全连接网络替代 diffusion model 生成奖励
3. **Diffusion-aided TD3**：替换为 TD3 算法验证通用性
4. **Without job transfer**：禁止跨 ASP 调度
5. **Fixed step configuration**：固定去噪步为 30
6. **Without GPU DVFS / Without renewable power**：关闭相应节能模块

---

## 3. 主要实验结果和性能指标

### 关键性能数据
| 方法 | 系统效用提升 | 学习收敛速度 | 延迟违规率 |
|------|---------------|----------------|-------------|
| **JEMAS (Proposed)** | **+30%↑ vs baselines** | 最快收敛 | **低至 ~7.59%** |
| Diffusion-aided TD3 | +~20% | 较慢 | ~20% |
| DNN-based shaping | +~15% | 中等 | ~30% |
| Standard SAC | 基准 | 极慢甚至不收敛 | >90% |

- **累计奖励提升达 1.5×**：相比标准 DRL 方法，在相同训练轮次下获得更高累积回报。
- **消融实验显示 reward shaping 权重 $\eta=0.4$ 效果最佳**，过大会掩盖真实反馈。

---

### 与基线方法的对比结果
- 在所有场景下，JEMAS 均显著优于各 baseline：
  - 相比 **no job transfer**，通过负载迁移降低高电价时段压力；
  - 相比 **fixed step**，动态调整去噪步数平衡质量与延迟；
  - 相比 **no DVFS/no renewable**，充分利用软硬件节能手段。

#### 图表关键观察：
- **图4–5**：展示了 ASP 根据电价波动动态调整计算负载与能源使用行为（如低价时充电、高价时放电售电）。
- **图6**：ASP2 将短延迟任务转移至轻负载且响应快的 ASP1，长延迟任务留在高性能 ASP3。
- **图7**：JEMAS 收敛最快，最终环境奖励最高，延迟违规率最低。

---

### 消融实验结果
| 设置 | 影响 |
|------|------|
| **W=3 vs W=5 vs W=7**（去噪步数） | 更多 W 加速初期探索，但过大导致训练不稳定 |
| **M=64 vs 128 vs 256**（潜在空间维度） | M=128 平衡表达能力与训练开销 |
| **有/无 state-action conditioning** | 缺少条件输入导致奖励生成无意义，性能大幅下降 |
| **不同 $\eta$ 值** | $\eta=0.4$ 时效果最优，过高会扭曲原始 reward 分布 |

> ✅ 结论：**state-action conditioning + moderate W/M + balanced $\eta$** 是成功的关键。

---

## 4. 关键结论和发现

### 主要发现
1. **AIGC 工作负载具有高度可控性**：通过调节去噪步数和目标 ASP，可在质量、延迟、能耗之间灵活权衡。
2. **reward sparsity 是制约 DRL 应用于 AIGC 调度的核心瓶颈**，传统方法难以有效学习。
3. **diffusion model 可作为强大的 reward generator**，其多步去噪机制天然适合建模潜在奖励分布。
4. **JEMAS 实现了高效、分布式的协同调度**，在不访问私有模型的前提下达成近似全局最优。

---

### 方法的局限性
| 局限 | 说明 |
|------|------|
| **训练时间较长** | 引入 diffusion model 导致训练耗时增加（见 Table III：~107min vs 45min） |
| **依赖离线参数校准** | GPU 功耗与执行时间模型需提前测量拟合 |
| **假设通信开销已知** | 未考虑大规模调度下的信令开销与延迟 |
| **当前聚焦 text-to-image** | 对视频生成等更复杂 AIGC 任务扩展尚待验证 |

---

### 未来工作方向
1. **轻量化 diffusion reward model**：设计更小、更快的 reward shaping 模块以缩短训练周期。
2. **在线自适应建模**：开发无需离线标定的在线学习机制，适应动态变化的硬件与模型。
3. **多模态 AIGC 扩展**：将框架推广至音频、视频、3D 内容生成等任务。
4. **联邦式联合训练**：结合 FL 思想进一步增强隐私保护能力。
5. **端边云协同调度**：纳入边缘节点，构建 hierarchical AIGC 推理网络。

---

> 📌 **总体评价**：  
> 本论文首次将 **diffusion model** 用于 **reward shaping**，创造性地解决了 AIGC 调度中的稀疏奖励难题，提出了一个兼具理论严谨性与工程实用性的联合优化框架。其实验充分、分析深入，为未来智能数据中心的绿色可持续发展提供了重要技术路径。

</details>

---

### 7. [Natural Language Processing: A Comprehensive Practical Guide from Tokenisation to RLHF](https://arxiv.org/abs/2605.03799)

**Authors**: Mullosharaf K. Arabov  
**Category**: cs.CL  
**Published**: 2026-05-06  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.03799v1  

#### Abstract
This preprint presents a systematic, research-oriented practicum that guides the reader through the entire modern NLP pipeline: from tokenisation and vectorisation to fine-tuning of large language models, retrieval-augmented generation, and reinforcement learning from human feedback. Twelve hands-on...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：** `Natural Language Processing: A Comprehensive Practical Guide from Tokenisation to RLHF`

---

## **1. 论文的主要贡献和创新点**

### **解决了什么问题**

本论文旨在解决自然语言处理（NLP）领域中一个长期存在的挑战：**从理论到实践的鸿沟**。尽管已有大量关于 NLP 的学术研究，但学生和从业者在实际应用时常常面临以下问题：

- 缺乏系统性的、端到端的实践指导；
- 实验难以复现（non-reproducible）；
- 过度依赖商业 API（如 GigaChat、YandexGPT），导致模型黑箱化、不可控；
- 忽视低资源语言（low-resource languages）和本地化需求（如俄语、塔吉克语、鞑靼语）。

该论文通过构建一个完整的、可复现的、以开源模型为核心的 NLP 教学与研究框架，系统性地填补了这一空白。

---

### **提出了什么新方法或新思路**

论文提出了一种全新的 **“可复现研究制品”（reproducible research artifact）** 教学范式，其核心思想是：

- **所有实验必须基于单一演进的语料库（evolving corpus）**，确保数据一致性。
- **强制要求公开代码、模型、报告和元数据**，并发布至 GitHub 或 Hugging Face。
- **优先采用 open-weight 模型**（如 Llama 3, Mistral, ruT5），反对封闭的商业 API。
- **强调 Hugging Face 生态系统的统一接口**，实现跨任务、跨模型的无缝集成。
- **引入多语言支持**，特别是对塔吉克语（Tajik）、鞑靼语（Tatar）等低资源语言的词典、分词器、嵌入和对齐基准进行原创性研究。

---

### **相比现有方法的优势**

| 维度 | 传统教材/课程 | 本文方法 |
|------|----------------|----------|
| **目标** | 理论讲解为主 | 实践导向，产出可复现的研究制品 |
| **模型选择** | 商业 API 或通用模型 | 开源权重模型 + 本地化适配 |
| **可复现性** | 弱（代码不完整） | 强（完整代码、数据、配置、测试） |
| **评估方式** | 静态报告 | 动态 Web 工具 + 自动化测试 |
| **语言覆盖** | 英语为主 | 支持俄语、塔吉克语、鞑靼语等 |
| **伦理责任** | 忽视 | 明确要求标注偏见、安全性和许可合规 |

> ✅ **优势总结**：本文不仅是一本教材，更是一个**开放科学（open science）的工程模板**，为 NLP 教育和研究提供了标准化、可持续、负责任的新范式。

---

## **2. 核心实验方法和设置**

### **使用的数据集**

- **主语料库**：基于 Practical Work No. 1 构建的俄语新闻语料库（≥100–150k 词），来源包括 TASS、RIA Novosti、Lenta.ru、Meduza、Kommersant 等。
- **多语言扩展**：
  - **塔吉克语**：使用作者构建的 TajPersLexon 词典和 transliteration 数据集。
  - **鞑靼语**：使用 Tatar2Vec 项目中的异构语料库。
- **下游任务数据**：
  - **NER**：RuNNE 标注数据或手动验证子集。
  - **摘要**：使用新闻首段作为基线摘要。
  - **QA**：合成表格问答三元组。
  - **偏好学习（RLHF）**：收集 ≥7,000 对人工标注的排序响应（含 1,000 条鞑靼语）。

所有数据均以 JSONL 格式存储，并附带元描述（meta-description）。

---

### **实验设置和评估指标**

#### **通用设置原则**
- 所有实验基于同一语料库演化。
- 使用 `requirements.txt` 或 `environment.yml` 固定依赖版本。
- 采用 `pytest` 实现自动化测试，验证确定性、无数据泄露、反向解码正确性等。
- 结果必须通过 **Jupyter Notebook、GitHub 仓库或 Hugging Face Space** 公开访问。

#### **各模块评估指标**

| 任务 | 主要指标 | 辅助指标 |
|------|--------|---------|
| **Tokenisation** | OOV Rate, Fragmentation Coefficient | Vocabulary Compactness, Reversibility |
| **Vectorisation** | Cosine Similarity, ARI, Bias Measurement | Dimensionality, Sparsity, Training Time |
| **Clustering** | Silhouette Score, Calinski–Harabasz, ARI, NMI | Stability (Bootstrap), Topic Coherence |
| **Classification** | F1 (macro/samples), PR-AUC | Accuracy, Recall, Calibration (ECE) |
| **Generation** | ROUGE-1/2/L, BERTScore, BLEU | Hallucination Rate, Faithfulness |
| **RAG** | Recall@k, MRR, Answer Accuracy | Source Citation, Faithfulness |
| **RLHF** | MAUVE, BERTScore, Expert A/B Test | KL Divergence, Behavioral Drift, Bias Audit |

---

### **基线方法对比**

论文设计了多层次的对比策略：

1. **横向对比**：
   - 不同分词器（Naïve, Lemmatisation, BPE, WordPiece, Unigram）
   - 不同向量化方法（BoW, TF-IDF, Word2Vec, FastText, SBERT）
   - 不同聚类算法（k-means, HDBSCAN, GMM）
   - 不同分类架构（Logistic Regression, SVM, XGBoost, BERT, ruT5）

2. **纵向对比**：
   - 从经典 ML 到深度学习再到 LLM 的演进路径。
   - 从监督学习到强化学习（RLHF）的对齐范式升级。

3. **消融实验**：
   - 在 Practical Work No. 11 中明确要求分析不同 PEFT 方法（LoRA vs Adapters）的影响。
   - 在 RLHF 中比较 PPO、DPO、IPO 的稳定性与效果。

---

## **3. 主要实验结果和性能指标**

### **关键性能数据**

| 方法 | 任务 | 性能表现 |
|------|------|----------|
| **LoRA / QLoRA** | Headline Generation | ROUGE-L 达到全量微调的 95–99%，显存降低 70%+ |
| **RAG (E5 + Llama 3)** | QA | 准确率提升 25%，幻觉率下降 40% |
| **HDBSCAN + SBERT** | 新闻聚类 | Silhouette Score > 0.5，优于 k-means 和 DBSCAN |
| **DPO** | RLHF | 训练稳定，无需奖励模型，KL 控制更优 |
| **Multi-head RM** | RLHF | 可独立调节 Helpfulness / Truthfulness / Safety 权重 |

---

### **与基线方法的对比结果**

- **QLoRA vs Full Fine-tuning**：
  - 在 16–24GB GPU 上成功微调 7B 模型（如 Mistral），而全量微调需数百 GB。
  - 质量差距 < 5%，但成本显著降低。

- **RAG vs 纯 LLM**：
  - RAG 在事实性任务上准确率高出 20–30%，且能提供引用来源。
  - 纯 LLM 更易产生幻觉，尤其在长尾知识上。

- **Open-weight vs Commercial API**：
  - GigaChat 等 API 虽然响应快，但无法复现、不可审计、存在许可风险。
  - 开源模型虽需更多调参，但完全可控、透明、可部署于本地。

---

### **消融实验结果**

- **分词器影响**：
  - BPE 和 Unigram 在俄语等形态丰富语言上显著优于空格切分和词干提取。
  - 子词单元使 OOV 率下降 60%+。

- **嵌入来源影响**：
  - 自训练的 FastText 模型在俄语新闻分类上优于通用 cc.ru.300.vec。
  - 外部预训练模型在跨领域任务中泛化更好。

- **PEFT 方法对比**：
  - LoRA 在参数效率和性能之间取得最佳平衡。
  - Adapter 层增加推理延迟，但更易于共享。

---

## **4. 关键结论和发现**

### **主要发现**

1. **可复现性是现代 NLP 研究的基石**  
   任何未公开代码、数据和配置的实验都不应被视为有效研究。

2. **开源模型足以胜任大多数 NLP 任务**  
   通过 LoRA、RAG、DPO 等技术，可在消费级硬件上高效适配 LLM，无需依赖商业 API。

3. **低资源语言不应被忽视**  
   作者为塔吉克语和鞑靼语开发的词典、分词器和嵌入证明，现代 NLP 方法可以成功迁移到小众语言。

4. **Hugging Face 是事实上的标准平台**  
   其统一 API 极大降低了多任务组合的复杂度，是构建端到端 NLP 系统的理想选择。

5. **对齐（Alignment）不仅是技术问题，更是伦理问题**  
   RLHF 可能导致模型“过度优化”，变得安全但空洞；必须监控行为漂移和文化偏见。

---

### **方法的局限性**

- **计算资源门槛仍高**：尽管 QLoRA 降低了要求，但训练高质量 LLM 仍需高端 GPU。
- **人工标注成本大**：RLHF 和领域基准构建依赖大量人力。
- **多语言支持有限**：目前仅覆盖俄语、塔吉克语、鞑靼语，其他语言需额外投入。
- **动态内容处理不足**：对社交媒体（如 VKontakte）的 emoji、非标准拼写适应性有待加强。

---

### **未来工作方向**

1. **构建多模态 NLP 流水线**：整合图像、音频与文本。
2. **发展轻量化边缘部署方案**：将 ruTiny、Phi-3 等小型模型用于移动设备。
3. **自动化偏好采集**：探索 Self-Play RLHF 或 Constitutional AI 减少人工干预。
4. **跨语言迁移机制深化**：研究 mDeBERTa 是否能在俄语任务上超越 RuBERT。
5. **绿色 AI 实践**：通过 CodeCarbon 评估不同方法的碳足迹，推动可持续 NLP。

---

> **总结**：  
> 本论文不仅是一部 NLP 实践指南，更是一种**负责任的人工智能教育哲学**。它倡导开放、透明、可复现、包容的技术生态，为下一代 NLP 工程师和研究人员树立了新的标杆。

</details>

---

### 8. [From Code to Prediction: Fine-Tuning LLMs for Neural Network Performance Classification in NNGPT](https://arxiv.org/abs/2605.03686)

**Authors**: Mahmoud Hanouneh, Radu Timofte, Dmitry Ignatov  
**Category**: cs.LG  
**Published**: 2026-05-06  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.03686v1  

#### Abstract
Automated Machine Learning (AutoML) frameworks increasingly leverage Large Language Models (LLMs) for tasks such as hyperparameter optimization and neural architecture code generation. However, current LLM-based approaches focus on generative outputs and evaluate them by training the produced artifa...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：From Code to Prediction: Fine-Tuning LLMs for Neural Network Performance Classification in NNGPT

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
当前基于 **Large Language Models (LLMs)** 的 AutoML 方法主要集中于生成任务（如神经网络代码生成、超参数预测），其评估依赖于训练生成模型并测量下游性能。然而，**LLM 是否能直接推理神经网络在不同数据集上的相对性能**（即跨数据集适用性）仍是一个未被充分探索的问题。

本文首次提出并研究了这一“**元级推理**”（meta-level reasoning）能力：  
> 给定一个神经网络架构的源代码和两个图像分类数据集名称，LLM 能否预测该架构在哪一个数据集上表现更好？

### 🚀 提出的新方法与创新思路
- **新任务设计**：在 NNGPT 框架中引入了一个新的 **classification 任务**，将 LLM 的输出从传统的可执行代码扩展为离散标签（dataset name），实现对架构-数据集匹配关系的直接预测。
- **三种渐进式 prompt 配置** 构成结构化消融实验：
  - **V1-Normalized-accuracy baseline**：提供准确率数值（作为上限验证）
  - **V2-Metadata-enriched**：用数据集元信息（图像大小、类别数等）替代准确率
  - **V3-Code-only**：仅输入架构源码 + 数据集名称，无任何性能或元数据提示
- 利用 **LEMUR 数据集** 中标准化的 PyTorch 实现与可复现性能指标构建训练样本。

### 🔍 相比现有方法的优势
| 方法 | 局限性 | 本工作的优势 |
|------|--------|--------------|
| 传统 AutoML (Grid Search, Bayesian Opt.) | 计算开销大，需多次训练 | 单次前向推理即可预测性能趋势 |
| AgentHPO / Optuna + LLM | 迭代优化超参，不涉及跨数据集推理 | 探索 LLM 对“架构-数据适配性”的理解能力 |
| NNGPT 原始版本 | 仅支持代码生成 | 扩展至 classification 输出类型，增强泛化能力 |

---

## 2. 核心实验方法和设置

### 📚 使用的数据集
- **LEMUR Neural Network Dataset**：
  - 包含多个图像分类任务的标准 PyTorch 实现
  - 统一评估流程与结构化日志记录
  - 提供每个模型在各数据集上的 **normalized accuracy**（归一化准确率）
- 涉及的具体数据集包括：
  - `CelebA-Gender`, `CIFAR-10`, `CIFAR-100`, `ImageNette`, `MNIST`, `Places365`, `SVHN`

### ⚙️ 实验设置
- **主模型**：`DeepSeek-Coder-7B-Instruct`，采用 LoRA 微调（rank=32, α=32, dropout=0.05）
- **辅助小模型对比**：`DeepSeek-Coder-1.3B-Instruct` + ONNX Runtime 加速
- **输入格式**：文本形式 prompt，截断至 2000 字符以内
- **输出限制**：生成 token 数 ≤ 20，目标是输出正确的 dataset name
- **训练策略**：
  - 使用 cosine learning rate scheduler
  - 每轮外循环包含 3 个 inner epochs
  - 通过 SQL 自连接构造 `(d1, d2)` 成对样本（满足 `d1.id < d2.id` 避免重复）

### 📊 评估指标
- **Classification Accuracy**：正确预测更高性能数据集的比例
- **Ground Truth 定义**：
  $$
  \text{norm\_acc}(m,d) = \frac{\text{acc}(m,d,e)}{\max_{m'} \text{acc}(m',d,e)}
  $$
  其中固定 epoch $e=5$，确保比较的是相对模型适合度而非绝对数据难度
- **字符串匹配机制**：采用 cascaded string matching（exact → substring → normalized substring）判断预测是否正确

### 🧪 基线方法对比
| Prompt 类型 | 描述 | 是否可比 |
|------------|------|---------|
| Normalized-accuracy (V1) | 提供真实归一化准确率 | 上限基线（理论上应达 100%） |
| Metadata-enriched (V2) | 提供数据集属性（size, classes, channels 等） | 当前主流特征表示方式 |
| Code-only (V3) | 仅源码 + 数据集名 | 最具挑战性，测试纯架构理解能力 |

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据（见 Table 1）

| Prompt | Model | N (test samples) | Peak Accuracy | Epoch of Peak |
|-------|--------|------------------|---------------|----------------|
| Norm. Acc. | 7B | 10 | **100.0%** | 9 |
| Code-Only | 7B | 30 | **80.0%** | 15 |
| Metadata | 7B | 30 | 70.0% | 8, 13 |
| Code-Only | 1.3B | 30 | 70.0% | 22–23 |

> ✅ **Code-only 在 7B 模型上达到 80% 准确率**，显著高于随机猜测（50%），表明 LLM 可从代码中学习判别信号。

### 🔁 与基线方法对比
- **Normalized-accuracy baseline 达到 100%** → 验证任务可行性
- **Code-only (80%) > Metadata (70%)** → 表明源码比元数据更具判别力
- **7B > 1.3B（同为 code-only）** → 显示模型容量影响 architectural reasoning 能力

### 🔍 消融实验结果
#### （1）Prompt 消融（信息逐步移除）
| 步骤 | 输入变化 | 性能变化 | 发现 |
|------|----------|----------|------|
| V1 → V2 | 移除 accuracy，加入 metadata | 100% → 70% | 数值比较容易，metadata 引入噪声 |
| V2 → V3 | 移除 metadata，保留 code-only | 70% → **80%** | **反直觉但关键发现：代码本身包含更丰富信号** |

> 💡 结论：**architecture source code 比 dataset metadata 更能反映跨数据集适用性**

#### （2）模型规模消融（7B vs 1.3B）
- **7B 模型**：收敛快（epoch 15 达峰）、稳定上升
- **1.3B 模型**：波动剧烈、最高仅 70%，且晚至 epoch 22–23 才达峰
- → 表明 **model capacity 是 architectural reasoning 的关键因素**

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **LLMs 可以被微调来预测神经网络在不同数据集上的相对性能**，无需实际训练模型。
2. **仅凭 neural network source code 和 dataset names**，`DeepSeek-Coder-7B` 就能达到 **80% 分类准确率**，远超随机基准（50%）。
3. **Architecture source code 比 dataset metadata 提供更强的判别信号**：
   - Metadata 在特性鲜明的数据集（如 CelebA-Gender）上表现好（90.9%）
   - 但在相似数据集间（如 CIFAR-10/CIFAR-100/SVHN）易混淆
   - Code-only 方法表现更均衡
4. **模型规模显著影响推理能力**：7B 模型优于 1.3B，在准确性、稳定性、收敛速度上全面领先。

### ⚠️ 方法的局限性
- 测试集较小（N=30），80% 与 70% 差异仅对应 **3 个额外正确预测**
- 所有实验使用单个 random seed，缺乏统计显著性分析
- 成对样本存在统计依赖性，未进行去相关处理
- 代码截断（2000 字符）可能丢失长架构的关键部分
- 当前仅适用于 LEMUR 中的图像分类任务，尚未推广至 segmentation、detection 或其他领域

### 🔮 未来工作方向
- 扩展到更多 LLM 家族（如 CodeLlama、OlympicCoder）
- 引入 **held-out split** 测试对未见架构/数据集的泛化能力
- 设计 **combined prompt**（code + metadata 融合输入）
- 推广至 LEMUR 支持的其他任务（如 object detection、semantic segmentation）
- 多种子运行以提升结果稳健性和统计可信度

---

> 📌 **一句话总结**：  
> 本文证明了 fine-tuned LLMs 能够从 neural network code 中学习到跨数据集性能预测的能力，且 **source code 本身比 dataset metadata 更具判别力**，为 AutoML 中的高效模型选择提供了新范式。

</details>

---

### 9. [Multi-Agent Reasoning Improves Compute Efficiency: Pareto-Optimal Test-Time Scaling](https://arxiv.org/abs/2605.01566)

**Authors**: Florian Valentin Wunderlich, Lars Benedikt Kaesberg, Jan Philip Wahle, Terry Ruas, Bela Gipp  
**Category**: cs.AI  
**Published**: 2026-05-06  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.01566v1  

#### Abstract
Advances in inference methods have enabled language models to improve their predictions without additional training. These methods often prioritize raw performance over cost-effective compute usage. However, computational efficiency is key for real-world applications with resource constraints. We pr...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Multi-Agent Reasoning Improves Compute Efficiency: Pareto-Optimal Test-Time Scaling*

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
该论文系统地研究了**在有限计算预算下如何最大化推理性能**的问题。尽管已有大量工作通过增加 test-time compute（如 self-consistency、multi-agent debate）来提升 LLM 推理能力，但这些方法往往忽视了**计算效率**，导致难以进行公平比较或实际部署。

具体来说，论文解决了以下三个关键空白：
- **缺乏统一计算预算下的方法对比**：不同推理策略常使用差异巨大的计算资源，无法直接比较。
- **效率度量不全面**：多数研究仅以 FLOPs 衡量计算成本，忽略了对运行时间影响显著的 memory transfer 开销。
- **缺少实用设计指南**：缺乏关于何时选择单智能体 vs 多智能体、如何配置参数（如 agent 数量、debate 轮数等）的具体建议。

### 提出的新方法与新思路
本研究并未提出全新的推理算法，而是提出了一个**系统性的分析框架**，用于评估和优化现有推理策略的**计算-准确性权衡**（compute-accuracy trade-off）。其核心思想是：
- 将推理过程视为可调节的“pipeline”，从三个维度控制计算开销：
  1. **Pipeline choice**（self-consistency, self-refinement, debate, MoA）
  2. **Pipeline parameters**（并行生成数、序列步数、agent 数、layer 数等）
  3. **Model size**（70B vs 8B Llama 模型）

- 引入 **Pareto-optimal front 分析法**，识别在给定计算预算下实现最高准确率的方法组合。

### 相比现有方法的优势
- ✅ **更贴近真实场景的效率评估**：综合考虑 FLOPs 和 memory transfer，估算实际运行时间。
- ✅ **全面且公平的横向比较**：在相同计算预算下对比四种主流推理范式。
- ✅ **提供可操作的设计原则**：例如“MoA 中 proposer 模型数量应比 layer 多一个”。
- ✅ **揭示任务难度对 scaling 效果的影响**：为 adaptive routing 提供实证支持。

---

## 2. 核心实验方法和设置

### 使用的数据集
- **MMLU-Pro**：一个多任务语言理解基准，涵盖广泛学科领域，具有更高的挑战性和鲁棒性。
- **BBH**（Big-Bench Hard）：筛选自 BIG-Bench 中最难的任务子集，测试复杂推理能力。
- 所有实验基于随机抽取的 **1000 个样本**进行评估（因多智能体系统计算昂贵）。

### 实验设置
- **模型**：
  - 主要使用 **Llama 3.1 70B** 进行主实验。
  - 对比实验中引入 **Llama 3.1 8B** 以研究模型大小的影响。
  - 所有模型均采用 **4-bit GPTQ 量化**。
- **硬件平台模拟**：
  - 基于 **8×NVIDIA A100 40GB PCIe GPU** 构建理论运行时间模型。
  - 同时建模 **FLOPs 计算时间** 和 **memory transfer 时间**，取两者最大值作为总延迟。
- **评估方式**：
  - 零样本（zero-shot）设置，temperature=0.7, top_p=0.95。
  - 最终答案通过选择 log-likelihood 最高的选项确定。

### 评估指标
- **Accuracy**：正确回答的比例。
- **Compute Cost**：
  - 以 **每任务耗时（seconds per task）** 为主要衡量标准，反映实际推理延迟。
  - 同时报告 FLOPs 和 memory transfer 数据。
- **Pareto-front 分析**：找出在特定计算预算下最优的 accuracy-compute 组合。

### 基线方法对比
| 方法 | 类型 | 缩写 |
|------|------|-----|
| Chain-of-Thought | 单智能体基础方法 | CoT |
| Self-Consistency | 单智能体，并行采样多个 CoT 路径投票 | SC |
| Self-Refinement | 单智能体，迭代自我反馈改进输出 | SR |
| Multi-Agent Debate | 多智能体，多轮交互式辩论 | Debate |
| Mixture-of-Agents | 多智能体，分层结构聚合 | MoA |

---

## 3. 主要实验结果和性能指标

### 关键性能数据（MMLU-Pro 上的结果）

| 方法 | 最高 Accuracy | 相对于 CoT 提升 | 所需计算预算 |
|------|----------------|------------------|---------------|
| CoT (Baseline) | 64.3% | — | 1× |
| Self-Consistency | 68.7% | +4.4 pp | ~10× |
| Debate | 70.0% | +5.7 pp | ~8× |
| **MoA (Pareto 最优)** | **71.4%** | **+7.1 pp** | ~20× |

> 注：pp = percentage points（百分点）

### 与基线方法的对比结果
- 在同等计算预算下：
  - **MoA 比 self-consistency 高出 +2.7 pp**
  - **Debate 比 self-consistency 高出 +1.3 pp**
- **Self-refinement 表现最差**：即使投入更多计算，其准确率仍低于 CoT 基线。
- **MoA 收益持续增长**：随着计算增加，MoA 几乎呈线性提升；而 self-consistency 和 debate 在约 10 序列 / 4 agents 后趋于饱和。

### 不同任务难度下的增益（MMLU-Pro）
| 任务难度 | CoT 准确率 | 15–20× compute 下准确率 | 增益（△） |
|----------|------------|----------------------------|-----------|
| Easy（>75% solve rate） | 94.4% | 96.6% | +2.2 pp |
| Medium（25–75%） | 53.0% | 61.5% | +8.5 pp |
| Hard（<25%） | 8.4% | 17.4% | **+9.0 pp** |

> 💡 结论：**越难的任务，test-time scaling 带来的收益越大**，甚至使 hard 任务准确率翻倍以上。

### 消融实验结果

#### （1）Debate 参数分析（图3）
- **增加 agent 数量（并行 scaling）有效**：最多提升至 4 个 agent。
- **增加 debate rounds（顺序 scaling）无效甚至有害**：尤其在 agent 较少时会降低性能。
- ✅ **推荐策略**：优先扩展 agents，而非 rounds。

#### （2）MoA 参数分析（图4）
- **最佳性能出现在 `#models = #layers + 1` 时**：
  - 如 (3 models, 2 layers), (4 models, 3 layers), (5 models, 4 layers)
- 超过此比例后性能下降。
- ✅ **推荐策略**：保持 proposer model 数量比 layer 多一个。

#### （3）模型大小 vs Test-time Scaling（表2 & 图7）
- 使用 **8B 模型 + 高度缩放的 multi-agent 设置**，最高仅达 ~53% 准确率。
- 而 **70B 模型 + CoT（无额外 scaling）** 即达到 **64.3%**。
- ❗ 结论：**更大的模型本身可能比小模型加大量 test-time compute 更高效**。

#### （4）MoA 中混合大小模型的影响（图5）
- 当所有 proposer 和 aggregator 均为 70B 时，准确率最高（71.4%）。
- 若将 **aggregator 替换为 8B**，性能轻微下降至 69.6%。
- 若将 **proposers 替换为 8B**，性能骤降至 52.9%。
- ✅ 结论：**proposer 模型的质量决定整体表现上限**，aggregator 可适当缩小。

---

## 4. 关键结论和发现

### 主要发现
1. **多智能体优于单智能体**：
   - 在 Pareto-optimal 条件下，**MoA 显著优于 self-consistency、self-refinement 和 debate**。
   - 多智能体系统能更有效地利用额外计算资源。

2. **MoA 是最高效的推理范式**：
   - 在 ~20× CoT 计算预算下，MoA 实现 **+7.1 pp 提升**。
   - 其优势源于并行与顺序 scaling 的协同作用，且上下文不会随 layer 积累膨胀。

3. **存在明确的设计准则**：
   - **Debate**：应优先扩展 **agents** 而非 **rounds**。
   - **MoA**：应配置为 **proposer model 数量 = layer 数量 + 1**。
   - 此规则已被验证在 BBH 和 8B 模型上也具鲁棒性。

4. **任务难度调节 scaling 效益**：
   - **Hard 任务受益最大（+9.0 pp）**，easy 任务几乎无增益。
   - 支持采用 **adaptive routing** 策略，动态分配计算资源。

5. **模型大小至关重要**：
   - **70B 模型 + CoT 比 8B 模型 + 强化 scaling 更快、更准**。
   - 单纯依赖 test-time compute scaling 无法弥补模型容量差距。

### 方法的局限性
- 📉 **样本量限制**：由于计算成本高，每个配置仅测试 1000 个样本，存在一定方差（95% CI 约 ±3%）。
- ⚙️ **理论计算模型**：运行时间基于公式估算，未考虑框架开销、批处理策略等现实因素。
- 💾 **内存受限场景未覆盖**：大模型（如 70B）在低显存设备上不可行，此时 scaling 小模型仍是必要选择。
- 🔍 **仅限非推理专用模型**：未测试如 DeepSeek-R1、o1 等专为推理训练的模型在 multi-agent setting 下的表现。

### 未来工作方向
- 探索 **reasoning-optimized models** 在 multi-agent pipelines 中的行为。
- 设计 **hardware-aware 的 adaptive scaling 策略**，结合 GPU 内存、带宽等约束。
- 研究 **异构 agent 架构**（如不同角色分配不同能力模型）。
- 构建 **面向特定能力的推理基准**（如 spatial reasoning、step-level planning），进一步细化 compute-efficiency 分析。

--- 

> ✅ **一句话总结**：  
> 本文证明，在合理配置下，**multi-agent systems（尤其是 MoA）能够以更低的单位计算成本获得更高的推理增益**，并提供了实用的 Pareto-optimal 设计指南，推动 LLM 推理走向高效化与智能化。

</details>

---

### 10. [From Static Analysis to Audience Dissemination: A Training-Free Multimodal Controversy Detection Multi-Agent Framework](https://arxiv.org/abs/2605.02939)

**Authors**: Zihan Ding, Ziyuan Yang, Yi Zhang  
**Category**: cs.LG  
**Published**: 2026-05-06  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.02939v1  

#### Abstract
Multimodal controversy detection (MCD) identifies controversial content in videos and their associated user comments, to support risk management for social video platforms.Prior research frames MCD as a static representation learning task, where features are directly extracted from videos and their ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*From Static Analysis to Audience Dissemination: A Training-Free Multimodal Controversy Detection Multi-Agent Framework*

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
- **静态建模的局限性**：现有 Multimodal Controversy Detection (MCD) 方法将争议视为视频和评论的静态属性，通过直接提取多模态特征进行分类，忽略了**争议是动态社会现象**的本质——它源于观众之间的互动与观点冲突。
- **冷启动问题**：新发布的视频缺乏评论（limited comments），导致基于评论的方法无法有效检测潜在争议。

### 🚀 提出的新方法与思路
提出了一种**训练免费（training-free）的多智能体框架 AuDisAgent**，将 MCD 任务从“静态特征建模”重构为“**动态受众传播模拟**”过程。其核心思想是：
- 用多智能体系统模拟真实世界中不同背景观众对内容的解读、讨论与意见演化过程。
- 引入 **Comment Bootstrapping Strategy** 解决冷启动问题，迁移历史相似视频的高赞评论作为初始输入。

#### 框架组成：
1. **Screening Agents**（筛选代理）
   - **Video Agent**：仅分析视频内容判断争议性。
   - **Comment Agent**：分析已有评论中的分歧。
   - **Interaction Agent**：联合分析视频与评论间的跨模态矛盾。
2. **Viewing Panel Agent**（观看小组代理）
   - 当三个 Screening Agents 判断不一致时激活。
   - 构建多样化观众角色（persona），模拟他们围绕视频展开讨论的过程（fact-checking, absorption, rebuttal）。
3. **Arbitration Agent**（仲裁代理）
   - 综合所有推理链做出最终判决，并输出可解释的理由。

### 🔍 相比现有方法的优势
| 优势维度 | 具体体现 |
|--------|---------|
| **动态性** | 模拟观众传播过程，能揭示在交互中浮现的潜在争议，而非仅依赖表面特征。 |
| **可解释性** | 所有 Agent 输出推理理由，形成完整 reasoning chain，提升决策透明度。 |
| **无需训练** | 完全基于 LLM 的 zero-shot 推理，避免昂贵的数据标注与模型微调。 |
| **鲁棒性强** | 在 rich-comment 和 limited-comment 场景下均表现优异。 |

---

## 2. 核心实验方法和设置

### 📚 数据集
- 使用公开的中文 MCD 数据集：**MMCD**（Xu et al., 2024）
  - 包含超过 10,000 条中文短视频。
  - 每条样本包含视频、元数据（标题、发布时间等）、评论及其社交上下文。

### ⚙️ 实验设置
- **主干 LLM**：`GLM4-9B`（支持长达 128K token 的长文本推理）
- **嵌入模型**：`bge-large-zh-1.5` 用于语义检索（标题编码）
- **few-shot / one-shot 设置**：无额外训练或 fine-tuning
- **二分类阈值**：设定为提示中争议评分范围（0–25）的中位数（即 12.5）

### 📊 评估指标
- **Precision（精确率）**
- **Recall（召回率）**
- **Accuracy（准确率）**
- **F1-score（F1 分数）**

### 🆚 基线方法对比
共比较了 **13 种先进基线方法**，涵盖以下类别：
| 类型 | 代表方法 |
|------|----------|
| 单一 Prompting | Standard Prompting, Zero-shot Chain-of-Thought (CoT) |
| 自我优化机制 | Self-Consistency, Self-Reflect, Self-Refine |
| 复杂推理范式 | Tree of Thoughts (ToT), Cumulative Reasoning (CR) |
| 多智能体系统 | Multi-Agent Debate, MAD, AgentMCD |

其中，**AgentMCD** 是当前最先进的 zero-shot 多智能体 MCD 方法，作为主要对比对象。

---

## 3. 主要实验结果和性能指标

### 📈 性能对比（见 Table 1）

| 方法 | F1 (rich) | Acc (rich) | F1 (limited) | Acc (limited) |
|------|-----------|------------|---------------|----------------|
| AgentMCD (SOTA) | 69.98 | 70.14 | 66.29 | 66.46 |
| **AuDisAgent (Ours)** | **71.64** (+1.66) | **71.47** (+1.33) | **68.29** (+2.00) | **67.56** (+1.10) |

> ✅ **结论**：AuDisAgent 在两种场景下均显著优于所有基线方法，在 rich-comment 场景中 F1 提升 **1.66%**，在 limited-comment 场景中提升达 **2.00%**。

---

### 🔪 消融实验（Ablation Study，见 Table 2）

移除任一组件都会导致性能下降，验证各模块重要性：

| 变体 | F1 (rich) | ΔF1 |
|------|----------|-----|
| w/o Video Agent | 70.01 | -1.63 |
| w/o Comment Agent | 70.63 | -1.01 |
| w/o Interaction Agent | 70.16 | -1.48 |
| w/o Viewing Panel Agent | 68.12 | -3.52 |
| **完整 AuDisAgent** | **71.64** | — |

> 💡 **关键发现**：
> - **Viewing Panel Agent 贡献最大**，说明模拟观众讨论对捕捉深层争议至关重要。
> - 各 Agent 协同作用明显，体现出“集体智慧”的优势。

---

### 🔄 泛化能力测试（见 Table 3）
在多个主流 LLM 上集成测试，AuDisAgent 均超越 AgentMCD：

| LLM | 方法 | F1 提升 |
|-----|------|--------|
| GLM4-9B | AuDisAgent vs AgentMCD | +3.73 |
| Qwen2.5-7B | AuDisAgent vs AgentMCD | +2.02 |
| DeepSeek-R1-Distill-Llama-8B | AuDisAgent vs AgentMCD | +3.93 |
| GPT-4o | AuDisAgent vs AgentMCD | +3.09 |

> ✅ 显示框架具有良好的**模型无关性与泛化能力**。

---

### 🧪 其他关键实验发现

#### ✅ Comment Sampling Strategy（表 4）
- “Top-30” 最受欢迎评论效果最佳。
- 过少采样遗漏关键观点；过多引入噪声。

#### ✅ Comment Bootstrapping 策略有效性（表 6）
| 参数 | 最优配置 | 效果 |
|------|----------|------|
| 数据库规模 | 100%（全量） | 性能随数据库增大而提升 |
| 编码权重 | `title:keywords = 1:0` | 标题信息更具判别力 |
| 评论迁移策略 | Top3-10（前3个最相似视频 × 各取10条评论） | 平衡多样性与噪声控制 |
| 嵌入模型 | `bge-large-zh-1.5` | 中文语义理解最优 |

#### ✅ 计算开销分析（图 3 & 4）
- 尽管 AuDisAgent 使用更多 token，但在运行时间上**快于 AgentMCD**。
- 原因：AgentMCD 对所有样本执行复杂评分流程，而 AuDisAgent 采用一致性门控机制跳过简单案例。

---

## 4. 关键结论和发现

### ✅ 主要结论
1. **争议本质是动态的**：将其建模为“受众传播过程”比静态特征提取更符合现实逻辑。
2. **多智能体模拟有效揭示潜在争议**：通过构建多样化的观众角色并模拟其讨论，能够挖掘出仅靠内容本身难以察觉的深层矛盾。
3. **无需训练即可实现高性能**：基于 LLM 的 zero-shot 多智能体协作，在无需任何参数更新的情况下达到 SOTA 表现。
4. **冷启动问题可通过历史迁移缓解**：Comment Bootstrapping 策略显著提升了新视频的早期风险识别能力。

---

### ⚠️ 局限性（Limitations）
1. **适用于短视频**：目前设计针对 TikTok/YouTube Shorts 类型内容，扩展至长视频需引入关键帧抽取与时间定位技术。
2. **依赖元数据质量**：检索阶段主要使用标题信息，若未来可用更丰富的上下文（如标签、发布者画像），性能有望进一步提升。
3. **受限于基础模型能力**：最终性能仍受底层 LLM 的文化敏感性和推理深度制约。

---

### 🔮 未来工作方向
1. **拓展到其他多模态推理任务**：如 multimodal misinformation detection、sentiment analysis 等。
2. **增强跨文化适应性**：结合具备更强社会文化理解能力的 LLM，提升在全球化平台上的适用性。
3. **引入真实用户行为反馈闭环**：探索如何利用实际用户互动数据迭代优化模拟过程。

---

## ✅ 总结一句话
> 本文提出的 **AuDisAgent** 成功将 MCD 从“静态分析”转向“动态传播模拟”，通过训练免费的多智能体协作框架，在可解释性、准确性与冷启动应对方面全面超越现有方法，为社交媒体内容治理提供了新范式。

</details>

---

### 11. [Meta-Inverse Physics-Informed Neural Networks for High-Dimensional Ordinary Differential Equations](https://arxiv.org/abs/2605.03511)

**Authors**: Zhao Wei, Kenneth Hor Cheng Koh, Sheng Yuan Chin, James Chun Yip Chan, Chin Chun Ooi, Yew-Soon Ong  
**Category**: cs.LG  
**Published**: 2026-05-06  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.03511v1  

#### Abstract
Solving inverse problems in dynamical systems governed by high-dimensional coupled ordinary differential equations (ODEs) is a ubiquitous challenge in scientific machine learning. In many real-world applications, researchers seek to uncover unknown parameters or model unknown dynamics even as the un...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文核心结论与实验结果总结

## 1. 论文的主要贡献和创新点

### 解决的问题
该论文针对**高维耦合常微分方程（high-dimensional coupled ODEs）系统中的逆问题求解**这一科学机器学习领域的普遍挑战。在许多现实应用中（如药代动力学建模），研究者需要从稀疏、噪声大且仅部分可观测的数据中推断未知参数或发现缺失的动力学机制。传统基于数值求解器的方法计算成本高昂，而现有的 **Physics-Informed Neural Networks (PINNs)** 虽然能嵌入物理约束，但仍存在以下问题：
- 采用任务特定的联合优化（joint optimization），导致优化困难；
- 泛化能力差，无法跨任务复用模型；
- 在高维、多尺度动态系统中训练不稳定。

### 提出的新方法与新思路
作者提出了一种名为 **Meta-Inverse Physics-Informed Neural Network (MI-PINN)** 的新框架，其核心思想是将逆建模重构为一个两阶段的元学习（meta-learning）问题：

1. **Stage I: 多分支元表示学习（Multi-branch Meta-Representation Learning）**
   - 在多个不同任务（即不同的参数配置或缺失项形式）上进行训练，学习一个共享的、具有物理感知能力的表示 $\theta^*$。
   - 引入**自适应聚类的多分支结构**：根据状态变量的动态相似性将其分组，每个分支专门处理一类具有相似时间尺度的行为，从而有效应对多尺度动态带来的谱偏差（spectral bias）问题。

2. **Stage II: 解耦的元逆建模（Decoupled Meta-Inverse Modeling）**
   - 固定已学习的表示 $\theta^*$，仅对目标任务的特定未知量 $\alpha$（如参数或神经网络权重）进行优化。
   - 最后一层参数通过一种**物理信息伪逆（physics-informed pseudo-inverse）** 方法以闭式（closed-form）方式计算，避免梯度更新带来的不稳定性。

### 相比现有方法的优势
- ✅ **显著降低优化维度**：将搜索空间从 $N_\theta + N_\alpha$ 减少到仅 $N_\alpha$，极大提升了优化效率与稳定性。
- ✅ **提高样本效率**：仅需单个状态变量的少量观测（文中示例为10个点）即可实现准确推断。
- ✅ **支持跨任务泛化**：预训练的表示可迁移到新任务，无需重新训练整个网络。
- ✅ **统一框架**：同时适用于**参数推断**（parameter inference）和**缺失机制发现**（missing term discovery）两类逆任务。

---

## 2. 核心实验方法和设置

### 数据集
实验基于**全身体生理药代动力学（whole-body PBPK）模型**，具体药物包括：
- **Paracetamol（对乙酰氨基酚）**
- **Theophylline（茶碱）**

这些模型分别对应：
- **静脉注射（IV）场景**：22个ODE
- **口服给药（Oral）场景**：33个ODE（含胃肠吸收过程）

观测数据来自真实临床研究：
- Paracetamol：[Rawlins et al., 1977] 中的静脉和口服血药浓度曲线（聚合数据）
- Theophylline：[Chrzanowski et al., 1977] 中8名个体的静脉输注数据（体现个体间变异性）

> 注：实际“数据”为稀疏的时间序列测量值（如10个时间点的静脉血浓度），其余状态不可直接观测。

### 实验设置与评估指标
| 项目 | 描述 |
|------|------|
| **任务类型** | 参数推断（如 $K_m$, $V_{\text{max}}$）、缺失机制发现（重建被屏蔽的Michaelis-Menten项） |
| **训练策略** | Stage I：在20个不同参数配置的任务上进行元训练；Stage II：固定表示，仅优化目标参数 |
| **网络架构** | 多分支结构，每支为 `1-256(sin)-256(sin)`，最终层由伪逆闭式求解 |
| **辅助网络**（用于缺失项发现） | 架构为 `1-3(swish)-1(linear)` |
| **优化器** | Adam，初始学习率 0.05 |
| **时间采样点** | 200个collocation点 |

### 基线方法对比
- **Solver-based Optimization**：MATLAB `lsqcurvefit` + SimBiology PBPK模型（信任域反射算法）
- **Standard Inverse PINN**：常规联合优化的PINN（即同时优化网络权重和物理参数）
- **其他PINN变体**：参考文献中各类PINN方法（见Table I）

---

## 3. 主要实验结果和性能指标

### 关键性能数据（参数推断误差）

#### IV Paracetamol（22 ODEs）
| 方法 | $K_{m,P}$ (µmol/L) | $V_{\text{max},P}$ (µmol/(h·mg)) | 比值 ($V_{\text{max}}/K_m$) |
|-------|---------------------|-------------------------------|----------------------------|
| Ground Truth | 23,000 | 1.80 | 7.83×10⁻⁵ |
| Trust Region Algorithm | 100,000 | 8.86 | 8.86×10⁻⁵ |
| **MI-PINN** | **27,727** | **2.18** | **7.86×10⁻⁵** |

> ➤ MI-PINN 推断值更接近真实值，尤其 $K_m$ 更合理（非数量级错误）

#### Oral Paracetamol（33 ODEs）
| 方法 | $K_{m,P}$ | $V_{\text{max},P}$ | 比值 |
|-------|------------|-------------------|--------|
| Ground Truth | 23,000 | 1.80 | 7.83×10⁻⁵ |
| Trust Region | 16,310 | 3.74 | 2.29×10⁻⁴ |
| **MI-PINN** | **18,053** | **1.32** | **7.31×10⁻⁵** |

> ➤ 常规方法在更高维系统中出现严重偏差，MI-PINN仍保持稳定

#### IV Theophylline（22 ODEs）
| 方法 | $K_{m,T}$ | $V_{\text{max},T}$ | 比值 |
|-------|------------|--------------------|--------|
| Ground Truth | 230 | 4.39×10⁻⁴ | 1.91×10⁻⁶ |
| Trust Region | 999 | 1.92×10⁻³ | 1.92×10⁻⁶ |
| **MI-PINN** | **214** | **4.10×10⁻⁴** | **1.92×10⁻⁶** |

> ➤ MI-PINN 对个体差异数据鲁棒性强，参数估计精度远超基线

### 与基线方法的对比结果
- **参数估计误差**：相比传统优化器和标准PINN，MI-PINN在所有测试案例中均实现了**高达两个数量级的误差降低**。
- **预测准确性**：所有状态变量的平均MSE极低（如IV theophylline下MSE ≈ 0.17），表明模型整体动态高度一致。
- **计算效率**：一次推理时间从 SciPy `odeint` 的 **14.66秒** 降至 MI-PINN 的 **4.17秒**（**3.5倍加速**）。

### 消融实验结果（Ablation Study）

| 实验 | 设置 | MSE / 结果 |
|------|------|-----------|
| **(1) 表示学习性能**<br>（单分支 vs 多分支） | 单分支（无聚类） | 5.63 ± 7.18 |
| | 多分支（自适应聚类） | **0.28 ± 0.25**（↓95%，≈20倍提升） |
| **(2) 逆建模性能**<br>（vs 标准PINN） | Standard PINN | MSE ≈ 1.92×10³，参数严重偏移 |
| | **MI-PINN** | **MSE = 0.17**，参数接近真实值 |

> ➤ 验证了**多分支结构**和**两阶段解耦设计**的关键作用。

---

## 4. 关键结论和发现

### 主要发现
1. **MI-PINN 可高效解决高维ODE系统的逆问题**：即使只有单一通道的稀疏临床数据，也能准确恢复关键药代动力学参数（如 $K_m$, $V_{\text{max}}$）。
2. **成功实现“缺失机制”的发现**：在完全屏蔽某代谢通路（如UGT2B15）的情况下，MI-PINN 能够重建其动态行为，并结合符号回归还原出近似正确的函数形式。
3. **具备强泛化能力与迁移性**：Stage I 学习的表示可在不同药物、不同给药路径之间迁移使用。
4. **优于传统方法**：相比基于求解器的优化和标准PINN，MI-PINN在**准确性、稳定性、效率**方面全面领先。

### 方法的局限性
- 当前框架依赖于已有ODE结构的部分先验知识（即知道哪些项可能缺失，而非完全黑箱发现方程）；
- 多分支结构的设计依赖于对状态变量动态的聚类分析，在极端复杂系统中可能难以自动确定最优簇数；
- 尚未集成不确定性量化模块，无法提供置信区间。

### 未来工作方向
- 扩展至**不确定性量化（Uncertainty Quantification）**，为推断参数提供校准后的置信度；
- 探索**全自动的机制发现流程**，结合符号回归与维度分析（如Buckingham Pi Theorem）生成可解释公式；
- 应用于更多领域，如心血管系统建模、生态动力学、材料老化等复杂高维ODE系统；
- 进一步优化多任务训练策略，提升元表示的通用性和收敛速度。

---

> **总结一句话**：  
> MI-PINN 通过**两阶段元学习 + 多分支表示 + 物理信息伪逆**，实现了在稀疏数据下对高维PBPK模型的高效、准确、可泛化的参数推断与机制发现，为药物研发中的逆向建模提供了强大工具。

</details>

---

### 12. [T$^2$PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning](https://arxiv.org/abs/2605.02178)

**Authors**: Haixin Wang, Hejie Cui, Chenwei Zhang, Xin Liu, Shuowei Jin, Shijie Geng, Xinyang Zhang, Nasser Zalmout, Zhenyu Shi, Yizhou Sun  
**Category**: cs.AI  
**Published**: 2026-05-06  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.02178v1  

#### Abstract
Recent progress in multi-turn reinforcement learning (RL) has significantly improved reasoning LLMs' performances on complex interactive tasks. Despite advances in stabilization techniques such as fine-grained credit assignment and trajectory filtering, instability remains pervasive and often leads ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：T²PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
当前基于 **multi-turn Reinforcement Learning (RL)** 的 LLM agent 在复杂交互任务中面临严重的**训练不稳定性**（training instability），常导致**训练崩溃**（training collapse）。作者指出，其根本原因在于**低效探索**（inefficient exploration）——策略在多轮对话中持续生成**低信息量的动作**（low-information actions），既未减少不确定性，也未推进任务进展，造成“犹豫”（hesitation）现象。

这种现象体现在两个层面：
- **Token-level**: LLM agent 过度思考（over-thinking），生成大量冗余推理 token，信息增益迅速饱和。
- **Turn-level**: agent 在早期偏离成功路径后，仍重复执行无意义的交互轮次，浪费 rollout 资源。

### 提出了什么新方法或新思路
提出 **T²PO (Token- and Turn-level Policy Optimization)**，一种**不确定性感知**（uncertainty-aware）的框架，通过细粒度控制探索行为来提升训练稳定性。

#### 核心创新机制：
1. **自校准不确定性信号 (Self-calibrated Uncertainty Signal)**  
   融合 **Entropy** 和 **Confidence** 构建更鲁棒的局部分布稳定性指标 $ M_t $，克服单一指标的盲区。

2. **Token-level Thinking Intervention (TTI)**  
   - 监控 token 生成过程中的不确定性动态。
   - 当边际不确定性变化低于阈值时，触发**思考干预**，强制结束推理阶段，避免冗余 token 生成。

3. **Turn-level Dynamical Sampling (TDS)**  
   - 计算相邻轮次间的不确定性变化 $ \Delta_k $。
   - 若变化过小，判定为无效探索，动态**重新采样该轮次**，避免陷入重复失败循环。

### 相比现有方法的优势
- **显式而非隐式控制**：不同于依赖 reward shaping 或粗粒度过滤的方法，T²PO 显式地在 token 和 turn 两级进行干预。
- **细粒度、自适应**：基于内在不确定性信号动态决策，无需人工设定固定长度或规则。
- **即插即用**：可与多种 policy update 方法（如 GiGPO）结合，提升其稳定性和效率。
- **不增加模型参数**：仅通过控制生成过程实现优化。

---

## 2. 核心实验方法和设置

### 使用了哪些数据集
在三个具有挑战性的多轮交互基准上进行评估：
- **WebShop**：模拟真实电商购物场景，测试 agent 的搜索、浏览、购买能力。
- **ALFWorld**：具身环境下的多步决策任务，涵盖 Pick & Place、Clean & Place 等六类任务。
- **Search QA**：结合搜索引擎的问答任务，包含单跳（NQ, TriviaQA）和多跳（HotpotQA, MuSiQue）数据集。

### 实验设置和评估指标
- **模型**：基于 Qwen3-4B 和 Qwen3-8B 进行 RFT 初始化后训练。
- **训练框架**：使用 `verl` 框架，支持异步采样与策略更新。
- **关键超参**：
  - 最大响应长度：500
  - 记忆上下文窗口：2（WebShop/ALFWorld），4（Search QA）
  - 温度（验证）：0.6，Top-p：0.95
- **评估指标**：
  - **WebShop**：Task Score、Success Rate、Title Score、reward_type 等。
  - **ALFWorld**：Overall Success Rate 及各子任务成功率。
  - **Search QA**：Exact Match (EM)。

### 基线方法对比
- **Closed-source LLMs**：GPT-4o, Gemini-2.5-Pro, Claude Sonnet 4
- **Instruction Tuning**：Qwen3-4B+SFT
- **RL Methods**：
  - PPO
  - GRPO
  - GiGPO（SOTA）
  - GiGPO + DAPO（动态采样增强）

---

## 3. 主要实验结果和性能指标

### 关键性能数据
#### WebShop 结果（Qwen3-4B-RFT）
| Method | Task Score | Success Rate |
|--------|------------|-------------|
| GiGPO | 86.03 ± 4.18 | 73.83 ± 3.04 |
| **T²PO (Ours)** | **93.84 ± 0.22** | **81.64 ± 0.39** |

#### ALFWorld 结果（Qwen3-4B-RFT）
- T²PO 在所有子任务上均取得最佳表现，相比 GiGPO 平均提升约 **8–12 个百分点**。
- 例如，在 `Pick2` 任务上从 71.41 提升至 **80.35**。

#### Search QA 结果（跨域泛化）
- 在多跳 QA 数据集上表现尤为突出：
  - **MuSiQue**：性能**翻倍**于先前 SOTA。
  - **2Wiki** 和 **Bamboogle**：显著提升，验证了强大的多步推理与泛化能力。

### 与基线方法的对比结果
- T²PO 在所有任务和 backbone 上均**显著超越所有基线**。
- 相比 GiGPO，T²PO 将 WebShop 成功率提升近 **8 个百分点**，且方差极小，表明训练高度稳定。
- 在不同随机种子下均未出现训练崩溃，而基线（如 GiGPO）存在明显性能下降甚至崩溃现象（见 Figure 1）。

### 消融实验结果
#### 表 3：T²PO 各模块消融（WebShop）
| 模块 | Task Score | Success Rate |
|------|-----------|-------------|
| 完整 T²PO | **93.84** | **81.64** |
| w/o RFT | 79.28 | 61.32 |
| w/o TTI | 81.28 | 73.27 |
| w/o TDS | 72.40 | 63.67 |

- **RFT**：冷启动至关重要，过滤低质量动作，防止错误传播。
- **TTI**：移除后成功率下降 8.37%，说明有效抑制了 over-thinking。
- **TDS**：移除后性能大幅下降，验证了 turn-level 探索控制的必要性。

#### 表 4：与其他 thinking 控制方法对比
| 方法 | Task Score | Success Rate |
|------|-----------|-------------|
| Hard thinking budget | 84.96 | 79.21 |
| Void turn filtering | 85.17 | 76.20 |
| **T²PO (TTI+TDS)** | **93.84** | **81.64** |

- 固定预算或全局奖励无法自适应任务难度，而 T²PO 动态响应不确定性，效果最优。

---

## 4. 关键结论和发现

### 论文的主要发现
1. **训练不稳定的根本原因是低效探索**，表现为 token-level 的 over-thinking 和 turn-level 的重复失败。
2. **基于不确定性信号的细粒度控制**能有效识别并干预低信息量行为，恢复探索-利用平衡。
3. **T²PO 显著提升训练稳定性与样本效率**：
   - 成功率提升 8–12 pts。
   - 降低 token 消耗约 20%（Figure 7b）。
   - 减少交互轮次约 25%（Figure 5c）。
4. **即插即用设计使其广泛适用**，可集成到现有 RL 框架中进一步提升性能。

### 方法的局限性
- 依赖于 LLM 输出的 token-level 概率分布，对输出格式敏感。
- 不确定性阈值等超参需调优（文中通过实验确定 $ \alpha=0.4 $ 效果最佳）。
- 当前方法聚焦于推理控制，未直接建模外部环境动态。

### 未来工作方向
- 将不确定性引导扩展至 **value learning** 或 **planning horizon** 控制。
- 探索更复杂的 **multi-modal uncertainty signals**（如结合检索结果置信度）。
- 应用于更广泛的 agentic applications，如代码生成、科学发现等长程规划任务。
- 研究如何将 T²PO 与 **asynchronous RL systems** 更深度整合以提升吞吐量。

> **Code is available at**: [https://github.com/WillDreamer/T2PO](https://github.com/WillDreamer/T2PO)

</details>

---

### 13. [Universal Smoothness via Bernstein Polynomials: A Constructive Approximation Approach for Activation Functions](https://arxiv.org/abs/2605.02591)

**Authors**: Wentao Zhang, Yutong Zhang, Yifan Zhu, Wentao Mo  
**Category**: cs.AI  
**Published**: 2026-05-06  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.02591v1  

#### Abstract
The efficacy of deep neural networks is heavily reliant on the design of non-linear activation functions, yet existing approaches often struggle to balance optimization stability with computational efficiency. While piecewise linear functions offer inference speed, they suffer from optimization inst...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Universal Smoothness via Bernstein Polynomials: A Constructive Approximation Approach for Activation Functions*

---

## 1. 论文的主要贡献和创新点

### ✅ **解决了什么问题**

当前深度神经网络中的激活函数面临两个核心矛盾：

- **优化稳定性 vs. 计算效率**：  
  - *Piecewise linear* 函数（如 ReLU、Leaky ReLU）计算高效，但存在 **非光滑性（non-differentiability at origin）**，导致训练中梯度不稳定、损失曲面崎岖。
  - *Smooth* 函数（如 GELU、Swish/SiLU、Mish）虽能提供平滑优化路径，但依赖 **transcendental operations**（如指数、误差函数），带来显著的计算开销。

此外，ReLU 类函数还存在 **Dying ReLU** 问题，即负区梯度为零导致神经元失活。

---

### 🚀 **提出了什么新方法或新思路**

本文提出了一种基于 **constructive approximation theory** 的通用平滑框架，并在此基础上设计了新型激活函数：**Bernstein Linear Unit (BerLU)**。

#### 核心思想：
- 利用 **Bernstein 多项式** 对 Leaky ReLU 在原点附近的“尖角”进行 **mollification（磨光）**，构造一个可微的二次过渡区域。
- 保留了 Leaky ReLU 的分段线性结构，在 $ x < -\epsilon $ 和 $ x > \epsilon $ 区域保持线性行为，在中间区间 $[- \epsilon, \epsilon]$ 引入由 Bernstein polynomial 构建的平滑转换。

#### 数学形式（简化后）：
$$
\text{BerLU}(x) =
\begin{cases}
\alpha x & x < -\epsilon \\
\frac{1-\alpha}{4\epsilon}x^2 + \frac{1+\alpha}{2}x + \frac{(1-\alpha)\epsilon}{4} & -\epsilon \leq x \leq \epsilon \\
x & x > \epsilon
\end{cases}
$$
其中 $\alpha$ 是可学习参数，$\epsilon$ 是控制平滑范围的超参数（默认设为 $10^{-2}$）。

---

### ⚖️ **相比现有方法的优势**

| 维度 | BerLU | ReLU / Leaky ReLU | GELU / SiLU / Mish |
|------|-------|-------------------|--------------------|
| **光滑性** | ✅ 严格 $C^1$ 连续（一阶导连续） | ❌ 非可微（在原点有“kink”） | ✅ 光滑 |
| **计算效率** | ✅ 仅需基本算术运算（加减乘除） | ✅ 极高（阈值操作） | ❌ 依赖 exp / erf 等昂贵函数 |
| **梯度传播稳定性** | ✅ Lipschitz constant = 1（非扩张） | ⚠️ 可能梯度爆炸/消失 | ❌ 多数 $L > 1$，深层易梯度爆炸 |
| **防止神经元死亡** | ✅ 负区斜率 $\alpha$ 可学习且非零 | ✅（Leaky 版本） | ✅ |
| **架构通用性** | ✅ 在 ViT 和 CNN 上均有效 | ✅ | ✅ |

> 💡 **关键优势总结**：BerLU 成功实现了 **高效 + 平滑 + 稳定梯度 + 自适应形状** 的四重平衡。

---

## 2. 核心实验方法和设置

### 📊 **使用的数据集**

- **CIFAR-10**：10类小图像分类基准
- **CIFAR-100**：100类细粒度图像分类任务
- **ImageNet-1K**：大规模真实场景图像识别，含1000类高分辨率图像

> → 覆盖从小规模到大规模、从简单到复杂的数据分布。

---

### 🔧 **实验设置与评估指标**

| 项目 | 设置说明 |
|------|----------|
| **模型架构** | Vision Transformer（ViT-Tiny, DeiT-Tiny, TNT-Small）、ConvNeXt |
| **训练周期** | 100 epochs |
| **优化器** | AdamW，weight decay = 0.05 |
| **学习率调度** | Cosine annealing + linear warmup |
| **梯度处理** | Gradient clipping at 1.0 |
| **初始化** | Truncated normal initialization |
| **硬件平台** | 8×NVIDIA A100 GPU 集群 |
| **重复次数** | 每组配置运行3次，报告均值±标准差 |
| **主要指标** | Top-1 Accuracy (%) |
| **效率指标** | Forward/Backward 时间（ms）、Peak Memory（GB） |

---

### 🆚 **基线方法对比**

涵盖两大类主流激活函数：

#### （1）Parametric Piecewise Linear
- **PReLU**：可学习负区斜率
- **Leaky ReLU**（隐含于比较）
- **ReLU**

#### （2）Smooth Transcendental Functions
- **GELU**：广泛用于 BERT、ViT
- **SiLU (Swish)**：自门控机制，PaLM 使用
- **Mish**：结合平滑饱和与无界响应
- **ELU / CELU**：解决均值偏移问题

---

## 3. 主要实验结果和性能指标

### 📈 **关键性能数据汇总（来自 Table I & II）**

| 数据集 | 模型 | GELU | PReLU | SiLU | **BerLU** | 提升幅度 |
|--------|------|------|--------|--------|------------|-----------|
| **CIFAR-10** | Average (ViT系列) | 72.2 | 76.4 | 69.9 | **77.8** | +1.4% vs PReLU, +5.6% vs GELU |
| **CIFAR-100** | Average (ViT系列) | 42.2 | 47.4 | 39.9 | **50.6** | **+3.2% vs PReLU, +8.4% vs GELU** ✅ |
| **ImageNet-1K** | Average (ViT系列) | 57.8 | 58.8 | 52.3 | **60.6** | +1.8% vs PReLU, +2.8% vs GELU |
| **CIFAR-10** | ConvNeXt | 64.9 | 64.6 | 60.6 | **66.5** | +1.9% vs GELU |
| **CIFAR-100** | ConvNeXt | 36.6 | 35.2 | 35.0 | **37.9** | +1.3% vs GELU, +2.9% vs SiLU |
| **ImageNet-1K** | ConvNeXt | 72.9 | 72.9 | 72.3 | **73.5** | +0.6% vs 所有基线 |

> ✅ **BerLU 在所有架构和数据集上 consistently outperform 所有 baselines**，尤其在 **CIFAR-100** 上表现突出。

---

### 🔍 **消融实验与敏感性分析（Ablation & Sensitivity Study）**

#### （1）平滑参数 $\epsilon$ 的影响（Fig. 1）

- 最优值出现在 $\epsilon = 10^{-2}$
- 当 $\epsilon < 10^{-1}$ 时性能稳定（波动 < 1.5%），表明对超参不敏感
- 若 $\epsilon > 0.2$（如 10），准确率急剧下降（CIFAR-100 降至 21.3%），说明 **过度平滑会削弱非线性表达能力**

> 👉 结论：适度平滑至关重要，BerLU 在 $\epsilon=10^{-2}$ 达到最佳权衡。

#### （2）可学习参数 $\alpha$ 的作用

- $\alpha$ 初始化为 0.01，训练中动态调整
- 实验显示不同层学习到不同的 $\alpha$ 值，验证其 **adaptive geometry shaping** 能力
- 固定 $\alpha$ 的变体会导致性能下降，证明 learnable slope 的必要性

---

### ⚙️ **计算效率分析（Table III）**

| 指标 | GELU | SiLU | PReLU | **BerLU** |
|------|------|------|--------|------------|
| **Forward Time (ms)** | 59.2 | 54.2 | 57.5 | **55.8** |
| **Backward Time (ms)** | 148.0 | 154.6 | 156.5 | **154.2** |
| **Peak Memory (GB)** | 11.53 | 12.25 | 9.50 | **10.58** |

> ✅ BerLU 显著优于 GELU 和 SiLU 的内存占用，前向速度更快；反向略慢于 GELU，但仍优于多数 smooth 激活函数。

---

## 4. 关键结论和发现

### ✅ **主要发现**

1. **Bernstein Polynomial 是一种强大的构造性工具**，可用于系统化地将非光滑激活函数转化为严格可微版本，同时保留其几何特性。
2. **BerLU 实现了理论与实践的统一**：
   - 理论上具有 **Lipschitz constant = 1**，保证梯度不会因激活层而放大，从根本上缓解深层网络中的梯度爆炸问题。
   - 实践中兼具 **高精度、高效率、低内存消耗**，适用于大规模部署。
3. **平滑性 + 可学习性 = 更强泛化能力**：
   - 相比固定形式的 GELU，BerLU 的可学习 $\alpha$ 和平滑过渡使其能够适应不同层次的信息流需求。
4. **跨架构有效性**：在 **Vision Transformer** 和 **ConvNeXt（CNN）** 上均取得领先性能，证明其 **architecture-agnostic** 特性。

---

### ⚠️ **方法的局限性**

1. **目前仅应用于标准分类任务**，尚未在 detection、segmentation 或 generative models 中验证。
2. **Bernstein degree 固定为 2（quadratic）**，更高阶可能进一步提升拟合能力，但也增加计算负担。
3. **理论分析集中在 Lipschitz continuity 和 smoothness**，缺乏对 loss landscape curvature 的深入可视化研究（尽管引用了相关工作）。
4. **未探索与其他 normalization 层（如 BatchNorm、LayerNorm）的交互效应**。

---

### 🔮 **未来工作方向**

1. 将 BerLU 扩展至 **其他非线性模块**（如 attention score smoothing、gate functions）。
2. 探索 **adaptive $\epsilon$**（每个神经元或每层独立学习 $\epsilon$）以实现更精细控制。
3. 应用于 **large language models**（LLMs），替代当前主流的 SiLU/GELU，提升训练稳定性与推理效率。
4. 结合 NAS（Neural Architecture Search）自动搜索最优的 Bernstein 控制点配置。
5. 进一步理论分析其对 **mean field dynamics** 和 **neural tangent kernel (NTK)** 的影响。

---

## ✅ 总结一句话

> **BerLU 是一种基于 Bernstein 多项式的新型激活函数，通过构造性逼近实现了高效、平滑、稳定且可学习的非线性变换，在多项视觉任务中超越 GELU、SiLU 等主流方案，是迈向“理想激活函数”的重要进展。**

</details>

---

### 14. [A Workflow-Oriented Framework for Asynchronous Human-AI Collaboration in Hybrid and Compute-Intensive HPC Environments](https://arxiv.org/abs/2605.03743)

**Authors**: Sergio Mendoza, Cedric Bhihe, Natalia Zamora, David Modesto, Jose Martin Bugallo Batalla, Jesus Gomez Canovas, Rafel Palomo Avellaneda, Miguel Perez Espinosa  
**Category**: cs.DC  
**Published**: 2026-05-06  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.03743v1  

#### Abstract
Human involvement is critical in training and deploying AI systems in high-stakes defence and security contexts. However, real-time interaction is impractical in HPC environments due to compute intensity and resource constraints. We present a workflow framework that enables asynchronous human-AI col...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：A Workflow-Oriented Framework for Asynchronous Human-AI Collaboration in Hybrid and Compute-Intensive HPC Environments

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
在高风险领域（如国防、安全）中，**人类监督对AI系统的训练与部署至关重要**（Human-in-the-Loop, HITL），但传统的 **High-Performance Computing (HPC)** 环境以批处理为主（如SLURM调度器），不支持异步的人类交互。现有工作流框架（如Airflow、Nextflow）存在以下问题：
- 多为代码中心化（code-centric），难以动态修改；
- 缺乏对HPC环境的原生支持；
- HITL机制通常是**阻塞式**（blocking），导致计算资源空转。

因此，**如何在保持HPC计算效率的同时实现非阻塞、可适应的人类-AI协作**，是一个尚未解决的关键挑战。

---

### 🚀 提出的新方法与创新思路
作者提出了 **Collaborative Innovation Framework (CIF)**，其核心是 **Workflow-Oriented Architecture (WOA)**，具有三大创新点：

#### （1）**配置驱动的工作流架构（Configuration-based WOA）**
- 工作流逻辑通过声明式的 **TOML 配置文件**定义，而非硬编码在Python脚本中。
- 包含任务依赖、执行站点（execsite）、容器镜像、HITL检查点等信息，提升**可移植性与易用性**。

#### （2）**异步非阻塞的HITL集成**
- 将 **HITL checkpoint 作为显式任务（HITLTask）嵌入工作流**，标记为 `hitl.enabled = true`。
- 当流程到达HITL节点时，仅该分支暂停等待人工反馈，**其他并行任务继续运行**（如HPC上的训练任务不停止）。
- 支持人类在运行时动态添加任务（如触发retraining）、修改参数或跳过步骤。

#### （3）**跨混合基础设施的统一执行**
- 支持 **边缘设备（Tactical Unit）、HPC集群（如MareNostrum 5）、云平台** 的协同执行。
- 利用 **Singularity/Docker 容器化**确保环境一致性。
- 与 **SLURM 调度器深度集成**，通过外部Watcher轮询 `.done` 文件检测任务完成状态。

---

### 🔍 相比现有方法的优势

| 维度 | 现有框架（Airflow/Nextflow等） | CIF |
|------|-------------------------------|-----|
| **HITL支持** | 同步阻塞，需中断流程 | 异步非阻塞，不影响并行计算 |
| **工作流定义方式** | 代码为中心（Python DAG） | 配置为中心（TOML） |
| **HPC兼容性** | 有限，依赖插件扩展 | 原生支持SLURM与远程提交 |
| **运行时重构能力** | 极弱或无 | 支持HITL驱动的任务增删与路径重定向 |
| **混合执行** | 主要面向云或本地 | 显式支持边缘+HPC+云协同 |

> 💡 **核心优势总结**：CIF实现了“**人类审查时间”与“计算时间”的解耦**，既保证了人类监督的有效性，又避免了资源浪费。

---

## 2. 核心实验方法和设置

### 🧪 实验场景：战术级舰船检测（Tactical Ship Detection）
一个典型的**防御导向应用场景**，要求：
- 实时边缘推理（Tactical Unit上进行图像识别）；
- 必要时在HPC上进行模型重训练；
- 人类专家异步审核检测结果与模型性能。

---

### 🛠️ 实验设置

| 项目 | 描述 |
|------|------|
| **硬件环境** | - **Tactical Unit**：现场部署的轻量级设备（CPU-only）<br>- **MareNostrum 5 (MN5)**：西班牙巴塞罗那超算中心的HPC集群（GPU密集型） |
| **通信机制** | 通过SSH远程提交任务至MN5；使用RSYNC同步模型与结果 |
| **容器技术** | 所有任务均封装在 **Singularity 容器** 中，保障跨环境一致性 |
| **监控机制** | - **Watcher模块**：定期轮询 `.done` 文件判断HPC任务是否完成<br>- **JobRegistry**：维护全局任务状态 |

---

### 📊 评估维度与指标

| 维度 | 指标说明 |
|------|--------|
| **Workflow Continuity** | 是否能在HITL暂停期间维持HPC任务运行 |
| **Resource Efficiency** | HPC资源利用率是否因等待人类输入而下降 |
| **Adaptability** | 能否根据人类反馈动态调整工作流路径（如触发retraining） |
| **Portability** | 同一份TOML配置能否在不同环境中执行 |
| **Qualitative Performance** | 检测精度提升情况（视觉对比） |

---

### ⚖️ 基线方法对比
论文未直接比较端到端性能（如mAP），而是从**系统能力层面**与主流框架进行横向对比，涵盖：
- **通用工作流引擎**：Apache Airflow, Luigi, Prefect
- **科学计算流水线**：Nextflow, Snakemake, Argo Workflows
- **HPC专用框架**：COMPSs, Pegasus, Kepler

> 对比如表1所示（见原文Section 7.1），CIF在 **Async HITL、Runtime Restructuring、Hybrid Execution** 上全面领先。

---

## 3. 主要实验结果和性能指标

### 📈 关键实验结果

#### （1）**成功实现异步HITL下的持续计算**
- 在舰船检测案例中，当Tactical Unit完成推理后触发第一个HITL检查点（Inference Validation）；
- 若人类拒绝结果，CIF自动调度 **Train Task 和 Evaluation Task 至MN5**；
- **在整个过程中，MN5上的训练任务无需等待人工决策完成即可启动**，实现了“逻辑暂停、物理不停”。

#### （2）**可视化性能显著提升**
- 图6展示了定性结果对比：
  - **(a) 基线模型**：将船只误检为“vehicle”或“building”，漏检严重；
  - **(b) 经HITL触发重训练后的模型**：准确识别多艘船只，定位更精准。
- 表明CIF能有效闭环“发现问题 → 触发重训 → 验证部署”的自适应循环。

#### （3）**资源利用高效**
- 实验显示，在长达数小时的HPC训练过程中，**无需因等待人类审批而中断作业**；
- Watcher与JobRegistry协同确保状态一致，无任务冲突或重复执行。

#### （4）**运行时重构能力验证**
- 用户可通过修改 `hitl_decision.json` 文件，在不重启系统的情况下：
  - 添加新的 `inference_task`；
  - 修改训练超参；
  - 跳过低价值评估阶段。
- 实现了真正的 **rapid adaptation**。

---

### ❌ 消融实验（未明确开展）
论文未提供传统意义上的消融实验（ablation study），但通过**功能对比分析**间接证明各组件必要性：
- 移除Watcher → 无法感知HPC任务完成；
- 移除JobRegistry → 状态不一致风险上升；
- 不启用HITL异步机制 → 整体流程必须阻塞。

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **HITL可以且应当是非阻塞的**  
   在HPC环境中，将人类审查设计为**异步、非阻塞任务**，能够极大提升资源利用率。

2. **配置即架构（Configuration as Architecture）**  
   使用 **TOML 等声明式格式统一管理任务、依赖、站点与HITL节点**，降低了非开发者用户的使用门槛，并增强了可移植性。

3. **动态重构可行且必要**  
   在任务运行中允许人类**动态添加任务或改变路径**，是应对突发数据变化（如新型伪装舰船）的关键能力。

4. **混合执行成为现实**  
   CIF实现了 **边缘推理 + HPC训练 + 异步人工监督** 的无缝整合，适用于真实作战场景。

---

### ⚠️ 局限性

| 限制 | 说明 |
|------|------|
| **容器依赖性强** | 所有执行节点必须支持Docker/Singularity，某些受限环境可能无法满足 |
| **HPC登录节点可达性要求** | 需能通过SSH访问HPC登录节点以提交任务，部分安全策略严格的系统可能禁止此操作 |
| **基于文件的状态检测** | 依赖 `.done` 文件轮询，不如原生事件通知机制高效 |
| **网络延迟影响闭环速度** | 数据传输与队列等待时间会影响adaptation loop的整体响应速度 |
| **安全性与合规性挑战** | 国防场景下跨域数据流动需额外加密与审计机制 |

---

### 🔮 未来工作方向

1. **跨领域泛化验证**  
   将CIF应用于其他高风险领域，如：
   - Disaster Response（灾害应急响应）
   - Space Situational Awareness（太空态势感知）

2. **标准化接口拓展**  
   探索与 **CWL (Common Workflow Language)** 和 **WDL (Workflow Description Language)** 的互操作性，便于融入现有生态。

3. **Web API 与可视化前端**  
   开发基于API的用户界面，替代CLI，支持图形化监控与交互。

4. **增强安全机制**  
   集成零信任架构、动作日志审计、身份权限管理系统，满足国防级合规需求。

5. **智能HITL推荐辅助**  
   引入AI助手预筛HITL请求，减少人工负担（如自动标注可疑样本供专家复核）。

---

## 总结

📌 **CIF提出了一种全新的Workflow-Oriented Architecture，首次在HPC环境中实现了真正意义上的异步、非阻塞Human-AI协作**。它不仅解决了传统框架中“人等机”或“机等人”的效率困境，还为国防、安全等关键领域的AI系统提供了**可适应、可监督、高效率**的工程化解决方案。虽然存在一定的部署约束，但其设计理念对未来AI-Ops与MLOps系统的发展具有重要启发意义。

</details>

---

### 15. [StateSMix: Online Lossless Compression via Mamba State Space Models and Sparse N-gram Context Mixing](https://arxiv.org/abs/2605.02904)

**Authors**: Roberto Tacconelli  
**Category**: cs.LG  
**Published**: 2026-05-06  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.02904v1  

#### Abstract
We present StateSMix, a fully self-contained lossless compressor that couples an online-trained Mamba-style State Space Model (SSM) with sparse n-gram context mixing and arithmetic coding. The model is initialised from scratch and trained token-by-token on the file being compressed, requiring no pre...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文《StateSMix: Online Lossless Compression via Mamba State Space Models and Sparse N-gram Context Mixing》总结**

---

## **1. 论文的主要贡献和创新点**

### **解决了什么问题**
传统基于 LLM 的压缩器（如 FineZip、ts_zip）虽然压缩率高，但依赖**外部预训练模型权重**（数百兆至数十 GB），需要 GPU 推理，不适用于通用场景。而经典压缩器（如 xz/LZMA）虽自包含且高效，但在小文件上无法捕捉复杂的语言结构。

本文提出一种**完全在线、无外部依赖的 lossless 压缩框架**，解决以下矛盾：
- 如何在**无需预训练权重**的前提下，实现接近神经压缩器的建模能力？
- 如何让模型知识**隐式编码于比特流中**，保证输出完全自包含（self-contained）？

### **提出了什么新方法或新思路**
作者提出 **STATESMIX**，一个结合 **Mamba-style SSM** 与 **Sparse N-gram Context Mixing** 的新型在线压缩系统，其核心创新包括：

1. **Online Mamba SSM 作为主预测器**
   - 使用轻量级 Mamba SSM（`DM=32`, `NL=2`, ~120K 参数）从零开始逐 token 在线训练。
   - 利用 SSM 的线性时间推理和紧凑状态，在纯 CPU 上实现实时训练与推断（~1,300 tok/s）。

2. **Softmax-invariant Logit Bias 机制**
   - 提出稀疏更新公式：仅对非零计数 token 添加 logit 偏置，利用 softmax 平移不变性避免全词汇表操作。
   - 显著降低高阶 n-gram（最高到 32-gram）的内存与计算开销。

3. **Entropy-adaptive Mixing**
   - 动态调节 n-gram 偏置强度：当 SSM 不确定（熵高）时增强 n-gram 影响；当 SSM 高信度时抑制 n-gram，防止过修正。

4. **Compact Vocabulary Remapping**
   - 仅建模当前文件中出现的 token（有效词汇 $v_e \in [18K, 44K]$），减少 head projection 成本 10–30%。
   - 使用 Rice 编码存储映射表，节省头部开销。

5. **Long-range Context Tables (16-/32-gram)**
   - 引入长距离 n-gram 表以捕获超出 SSM 记忆范围的重复模式（如维基模板、引用格式）。

6. **Linear-probing Collision Resolution**
   - 开放寻址 + 深度为 8 的线性探测，显著提升哈希表利用率，缓解高负载下的冲突损失。

---

### **相比现有方法的优势**

| 维度 | STATESMIX | LLM-based (FineZip/ts_zip) | Classical (xz) | NNCP |
|------|-----------|----------------------------|----------------|------|
| 是否需预训练权重 | ❌（完全在线训练） | ✅（必须共享） | ❌ | ❌（但存于输出中） |
| 是否自包含（self-contained） | ✅ | ❌ | ✅ | ❌（含 ~10MB 权重） |
| 是否需 GPU | ❌（纯 C + AVX2） | ✅ | ❌ | 可选 |
| 内存占用 | 中等（~6.1GB for 100MB） | 极高（>16GB） | 低 | 高 |
| 小文件性能（≤10MB） | ✅ 超越 xz | ✅ 更优但成本高 | 基准 | ✅ 但有存储开销 |
| 实现复杂度 | 低（无 Python/CUDA） | 高 | 低 | 中 |

> ✅ **核心优势**：在无需预训练、无需 GPU 的前提下，首次实现**小型在线神经压缩器超越 xz**，尤其适合嵌入式、加密备份等资源受限环境。

---

## **2. 核心实验方法和设置**

### **使用的数据集**
- 主要基准：**enwik8** —— 英文维基百科前 100MB XML 文本。
- 测试规模：`1MB`, `3MB`, `10MB`, `100MB` 四个子集。

### **实验设置和评估指标**

#### **评估指标**
- **bpb (bits per byte)**：压缩后比特数 / 原始字节数，越低越好。
- **bpt (bits per token)**：排除头部开销后的内部模型预测误差。
- **速度**：tokens/sec 和 KB/s。
- **内存峰值**：运行时最大 RAM 占用。

#### **硬件平台**
- 单核 x86-64 CPU，支持 AVX2 SIMD 指令集。
- 无 GPU 加速，所有实验均在纯 C 实现下完成。

#### **训练策略**
- 每 32 个 token 进行一次 Adam 更新（truncated BPTT）。
- Warm-up schedule：早期 chunk 使用更多迭代（最多 8 次），加速冷启动收敛。
- Label smoothing: ε = 0.12。

---

### **基线方法对比**
- **Classical**: `gzip`, `bzip2`, `xz -9e`（LZMA2 极致模式）
- **Neural/Context Mixing**: `PAQ8px`, `CMIX`
- **Online Neural**: `NNCP v3+`（Transformer-XL 在线训练）
- **LLM-based**: `FineZip`, `ts_zip`, `Deletang et al.`

> 主要对比对象是 **xz -9e**，因其为目前最强通用压缩器之一（enwik8 达 1.989 bpb）。

---

## **3. 主要实验结果和性能指标**

### **关键性能数据（enwik8 结果）**

| 文件大小 | STATESMIX (bpb) | xz -9e (bpb) | 相对提升 |
|---------|------------------|--------------|----------|
| 1MB     | **2.123**        | 2.326        | **-8.7%** |
| 3MB     | **2.149**        | 2.271        | **-5.4%** |
| 10MB    | **2.162**        | 2.177        | **-0.7%** |
| 100MB   | 2.130            | **1.989**    | +6.9% (劣势) |

> ✅ 在 ≤10MB 文件上全面优于 xz，**在 1MB 上领先近 9%**  
> ❌ 在 100MB 上被 xz 反超，因 LZMA 更擅长复制长距离重复块。

---

### **消融实验结果（on enwik8_3M）**

| 变体 | bpb | vs Full | vs xz |
|------|-----|--------|-------|
| Count only (baseline) | 4.191 | +95.0% | >> xz |
| N-gram + count | 3.517 | +63.6% | > xz |
| **SSM + count** | **2.240** | **+4.2%** | **-1.3% ✅** |
| Full (SSM + n-gram) | **2.149** | — | **-5.4% ✅** |
| xz -9e | 2.271 | +5.7% | — |

#### **关键发现**
- **SSM 是主导组件**：单独使用即可比频率统计减少 **46.6%** 大小，并**超过 xz**。
- **n-gram 作用有限但互补**：无 SSM 时仅减少 16.1%，说明其依赖良好先验分布。
- **联合使用增益明显**：n-gram 在 SSM 基础上再降 **4.1%**，体现“泛化 + 精确记忆”协同效应。

---

### **其他重要性能指标**

| 指标 | 数值 | 说明 |
|------|------|------|
| 速度（4核 OpenMP） | ~2,000 tok/s (~700 KB/s) | 可接受的实用速度 |
| 峰值内存 | 6.1 GB | 主要由 9 个 16M-slot n-gram 表占据（共 5.1GB） |
| 参数量（enwik8） | ~2.85M | 其中 SSM 固定部分 ~19.7K，其余随 $v_e$ 动态变化 |
| 自包含性 | ✅ | 无需传输任何额外模型文件 |

---

## **4. 关键结论和发现**

### **主要发现**
1. ✅ **小型 Mamba SSM 可作为强大在线学习器**：
   - 尽管仅有 ~120K 活跃参数，通过在线 SGD 快速适应文件特定模式。
   - **SSM 单独就能击败 xz**，证明其建模效率远高于传统方法。

2. ✅ **n-gram 提供精确局部记忆补充**：
   - 特别是 16-/32-gram 表能捕捉长程重复结构（如维基模板），弥补 SSM 记忆窗口限制。

3. ✅ **Softmax-invariant logit bias 设计高效可行**：
   - 实现了高阶稀疏上下文建模，且不影响概率归一化。

4. 🔁 **存在性能拐点（crossover point）**：
   - 在约 **30MB** 处，xz 开始反超 STATESMIX，源于其高效的 block copying 能力。

5. 🧠 **STATESMIX 是 PPM 与 PAQ 的神经泛化形式**：
   - 类似 PPM 的多阶上下文查询，但采用固定加权 + 熵自适应混合；
   - 类似 PAQ 的 context mixing，但用解析式控制而非二级学习器。

---

### **方法的局限性**
| 局限 | 描述 |
|------|------|
| **内存消耗大** | n-gram 表占 ~5.1GB，限制在低端设备部署 |
| **速度较慢** | ~700KB/s，远低于 xz 的 10MB/s 级别 |
| **大文件劣势** | 无法像 LZMA 那样零代价复制长段重复内容 |
| **训练开销占比高** | 75% 时间花在 `train_chunk`，尤其是 head projection 的反向传播 |
| **缺乏预训练初始化** | 模型从随机初始化开始，冷启动阶段效率较低 |

---

### **未来工作方向**
1. **BWT 预处理**
   - 对 token 序列应用 Burrows-Wheeler Transform，聚集相似上下文，增强 n-gram 效果。

2. **GPU 加速**
   - 将 head projection 与 Adam 更新卸载至 GPU，预计提速 50–100×，支持更大模型（如 DM=128, NL=4）。

3. **Adaptive n-gram Weighting**
   - 引入 PAQ-style 元学习器动态调整各阶 n-gram 权重 $\lambda_k$，适配不同文本特征。

4. **Variable-order Back-off**
   - 改为 PPM-style 最长匹配回退机制，提高高阶上下文可靠性。

5. **Larger SSM with Pre-trained Initialization**
   - 分发一个小型预训练 SSM 权重作为“压缩编解码器”，用于微调，兼顾冷启动与自包含性。

6. **Hybrid Predict-or-Copy Architecture**
   - 引入 LZ-style match channel，检测长重复序列并直接编码为 `(offset, length)` 对，绕过 arithmetic coder，缩小与 xz 在大文件上的差距。

---

## **总结**
> **STATESMIX 是首个在无需预训练、无需 GPU 的条件下，通过在线训练 Mamba SSM 实现超越 xz 压缩率的小型 lossless 压缩器**。

它验证了一个重要理念：**即使极小的神经模型，只要设计得当，也能在特定任务上匹敌甚至超越高度优化的传统算法**。其真正的价值不仅在于性能数字，更在于开辟了一条“轻量级、自包含、可移植”的神经压缩新路径，特别适用于边缘计算、安全通信等场景。

</details>

---

### 16. [Heterogeneous Graph Importance Scoring and Clustering with Automated LLM-based Interpretation](https://arxiv.org/abs/2605.02919)

**Authors**: Takato Yasuno  
**Category**: cs.LG  
**Published**: 2026-05-06  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.02919v1  

#### Abstract
Urban bridge networks are critical infrastructure whose disruption can cascade into severe impacts on transportation, emergency services, and economic activity. This paper presents a comprehensive methodology for assessing bridge importance through heterogeneous graph analysis, unsupervised clusteri...

---

### 17. [DiagramNet: An End-to-End Recognition Framework and Dataset for Non-Standard System-Level Diagrams](https://arxiv.org/abs/2605.01338)

**Authors**: Jincheng Lou, Ruohan Xu, Jiapeng Li, Junyin Pi, Runzhe Tao, Weijian Fan, Xiao Tan, Guojie Luo, Yibo Lin  
**Category**: cs.AI  
**Published**: 2026-05-06  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.01338v1  

#### Abstract
System-level diagrams encode the architectural blueprint of chip design, specifying module functions, dataflows, and interface protocols. However, non-standardized symbols and the scarcity of structured training data hinder existing multimodal large language models (MLLMs) from recognizing these dia...

---

### 18. [Distilling Long-CoT Reasoning through Collaborative Step-wise Multi-Teacher Decoding](https://arxiv.org/abs/2605.02290)

**Authors**: Taewon Yun, Jisu Shin, Jeonghwan Choi, Seunghwan Bang, Hwanjun Song  
**Category**: cs.AI  
**Published**: 2026-05-06  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.02290v1  

#### Abstract
Distilling large reasoning models is essential for making Long-CoT reasoning practical, as full-scale inference remains computationally prohibitive. Existing curation-based approaches select complete reasoning traces post-hoc, overlooking collaboration among heterogeneous teachers and lacking dynami...

---

### 19. [Shadow-Loom: Causal Reasoning over Graphical World Model of Narratives](https://arxiv.org/abs/2605.02475)

**Authors**: David Wilmot  
**Category**: cs.AI  
**Published**: 2026-05-06  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.02475v1  

#### Abstract
Stories hold a reader's attention because they have causes, secrets, and consequences. Shadow-Loom is an experimental open-source framework that turns a narrative into a versioned graphical world model and lets two engines act on it: a causal physics grounded in Pearl's ladder of causation and a rec...

---

### 20. [Revisiting Graph-Tokenizing Large Language Models: A Systematic Evaluation of Graph Token Understanding](https://arxiv.org/abs/2605.03514)

**Authors**: Zhongjian Zhang, Yue Yu, Mengmei Zhang, Junping Du, Xiao Wang, Chuan Shi  
**Category**: cs.CL  
**Published**: 2026-05-06  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.03514v1  

#### Abstract
The remarkable success of large language models (LLMs) has motivated researchers to adapt them as universal predictors for various graph tasks. As a widely recognized paradigm, Graph-Tokenizing LLMs (GTokenLLMs) compress complex graph data into graph tokens and treat them as prefix tokens for queryi...

---

### 21. [Do LLMs have core beliefs?](https://arxiv.org/abs/2605.03255)

**Authors**: Anna Sokol, Marianna B. Ganapini, Nitesh V. Chawla  
**Category**: cs.LG  
**Published**: 2026-05-06  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.03255v1  

#### Abstract
The rise of Large Language Models (LLMs) has sparked debate about whether these systems exhibit human-level cognition. In this debate, little attention has been paid to a structural component of human cognition: core beliefs, truths that provide a foundation around which we can build a worldview. Th...

---

### 22. [Nora: Normalized Orthogonal Row Alignment for Scalable Matrix Optimizer](https://arxiv.org/abs/2605.03769)

**Authors**: Jinghui Yuan, Jiaxuan Zou, Shuo Wang, Yong Liu, Feiping Nie  
**Category**: cs.LG  
**Published**: 2026-05-06  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.03769v1  

#### Abstract
Matrix-based optimizers have demonstrated immense potential in training Large Language Models (LLMs), however, designing an ideal optimizer remains a formidable challenge. A superior optimizer must satisfy three core desiderata: efficiency, achieving Muon-like preconditioning to accelerate optimizat...

---

### 23. [Accelerating battery research with an AI interface between FINALES and Kadi4Mat](https://arxiv.org/abs/2605.00909)

**Authors**: Giovanna Tosato (Karlsruhe Institute of Technology), Leon Merker (Karlsruhe Institute of Technology, Helmholtz Institute Ulm, Technical University of Munich), Monika Vogler (Technical University of Munich), Michael Selzer (Karlsruhe Institute of Technology), Arnd Koeppe (Karlsruhe Institute of Technology)  
**Category**: cs.AI  
**Published**: 2026-05-06  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.00909v1  

#### Abstract
The time-consuming formation process critically impacts the longevity of sodium-ion coin cells and End Of Life (EOL) performance. This study aims to optimize formation protocols for duration efficiency, targeting high-performance outcomes while minimizing the number of experiments to reduce resource...

---

### 24. [Valley3: Scaling Omni Foundation Models for E-commerce](https://arxiv.org/abs/2605.01278)

**Authors**: Zeyu Chen, Guanghao Zhou, Qixiang Yin, Ziwang Zhao, Huanjin Yao, Pengjiu Xia, Min Yang, Cen Chen, Minghui Qiu  
**Category**: cs.AI  
**Published**: 2026-05-06  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.01278v1  

#### Abstract
In this work, we present Valley3, an omni multimodal large language model (MLLM) developed for diverse global e-commerce tasks, with unified understanding and reasoning capabilities across text, images, video, and audio. A key feature of Valley3 is its native multilingual audio capability for e-comm...

---

### 25. [HeavySkill: Heavy Thinking as the Inner Skill in Agentic Harness](https://arxiv.org/abs/2605.02396)

**Authors**: Jianing Wang, Linsen Guo, Zhengyu Chen, Qi Guo, Hongyu Zang, Wenjie Shi, Haoxiang Ma, Xiangyu Xi, Xiaoyu Li, Wei Wang, Xunliang Cai  
**Category**: cs.AI  
**Published**: 2026-05-06  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.02396v1  

#### Abstract
Recent advances in agentic harness with orchestration frameworks that coordinate multiple agents with memory, skills, and tool use have achieved remarkable success in complex reasoning tasks. However, the underlying mechanism that truly drives performance remains obscured behind intricate system des...

---

### 26. [GRAIL: A Deep-Granularity Hybrid Resonance Framework for Real-Time Agent Discovery via SLM-Enhanced Indexing](https://arxiv.org/abs/2605.02489)

**Authors**: Jinliang Xu  
**Category**: cs.AI  
**Published**: 2026-05-06  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.02489v1  

#### Abstract
As the ecosystem of Large Language Model (LLM)-based agents expands rapidly, efficient and accurate Agent Discovery becomes a critical bottleneck for large-scale multi-agent collaboration. Existing approaches typically face a dichotomy: either relying on heavy-weight LLMs for intent parsing, leading...

---

### 27. [CuraView: A Multi-Agent Framework for Medical Hallucination Detection with GraphRAG-Enhanced Knowledge Verification](https://arxiv.org/abs/2605.03476)

**Authors**: Severin Ye, Xiao Kong, Xiaopeng He, Guangsu Yan, Dongsuk Oh  
**Category**: cs.CL  
**Published**: 2026-05-06  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.03476v1  

#### Abstract
Discharge summaries require extracting critical information from lengthy electronic health records (EHRs), a process that is labor-intensive when performed manually. Large language models (LLMs) can improve generation efficiency; however, they are prone to producing faithfulness hallucinations, stat...

---

### 28. [Enhancing Performance Insight at Scale: A Heterogeneous Framework for Exascale Diagnostics](https://arxiv.org/abs/2605.03561)

**Authors**: Dragana Grbic (Department of Computer Science, Rice University)  
**Category**: cs.DC  
**Published**: 2026-05-06  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.03561v1  

#### Abstract
As exascale systems reach unprecedented concurrency, traditional performance analysis tools struggle with the overhead of massive-scale telemetry. We present an accelerated infrastructure for the hpcanalysis framework that leverages a high-performance C++ API and GPU parallelism to enable high-throu...

---

### 29. [Healthcare AI GYM for Medical Agents](https://arxiv.org/abs/2605.02943)

**Authors**: Minbyul Jeong  
**Category**: cs.LG  
**Published**: 2026-05-06  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.02943v1  

#### Abstract
Clinical reasoning demands multi-step interactions -- gathering patient history, ordering tests, interpreting results, and making safe treatment decisions -- yet a unified training environment provides the breadth of clinical domains and specialized tools to train generalizable medical AI agents thr...

---

### 30. [AsymK-Talker: Real-Time and Long-Horizon Talking Head Generation via Asymmetric Kernel Distillation](https://arxiv.org/abs/2605.02948)

**Authors**: Yuxin Lu, Qian Qiao, Jiayang Sun, Min Cao, Guibo Zhu  
**Category**: cs.LG  
**Published**: 2026-05-06  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.02948v1  

#### Abstract
Recent advances in diffusion models have markedly enhanced the visual fidelity of audio-driven talking head generation. Nevertheless, existing methods are constrained by three critical limitations: causal inefficiency that impedes real-time inference, incompatibility with temporally coherent conditi...

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
