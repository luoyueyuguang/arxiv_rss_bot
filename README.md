# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-05-25 09:44:30 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG

## 📚 Recent Papers

### 1. [Fast-dDrive: Efficient Block-Diffusion VLM for Autonomous Driving](https://arxiv.org/abs/2605.23163)

**Authors**: Kewei Zhang, Jin Wang, Sensen Gao, Chengyue Wu, Yulong Cao, Songyang Han, Boris Ivanovic, Langechuan Liu, Marco Pavone, Song Han, Daquan Zhou, Enze Xie  
**Category**: cs.CL  
**Published**: 2026-05-25  
**Score**: 13.0  
**Type**: new  
**ArXiv ID**: 2605.23163v1  

#### Abstract
End-to-end autonomous driving via Vision-Language-Action (VLA) models demands a precarious balance between high-fidelity trajectory planning and efficient inference. Existing paradigms typically fall short: autoregressive (AR) VLAs are memory-bandwidth-bound on edge hardware and prone to exposure-bi...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文《Fast-dDrive: Efficient Block-Diffusion VLM for Autonomous Driving》总结**

---

## **1. 主要贡献和创新点**

### **解决的问题**
现有的端到端自动驾驶 VLA（Vision-Language-Action）模型面临两大挑战：
- **自回归（AR）模型**：推理效率低，在边缘设备上受限于内存带宽（memory-bandwidth-bound），且存在暴露偏差（exposure bias），导致轨迹误差累积。
- **全序列扩散模型（Full-sequence diffusion）**：无法复用 KV Cache，推理延迟高，并存在“逻辑泄漏”（logical leakage），即规划结果可能反向影响感知判断，违背“先感知后规划”的因果顺序。

### **提出的新方法与创新思路**
Fast-dDrive 提出了一种 **块扩散（block-diffusion）VLA 架构**，结合结构化输出先验，实现高效、准确的端到端驾驶决策。其核心创新包括：

#### ✅ **Section-Aware Structured Diffusion (SASD)**
- 利用驾驶 VLA 输出通常为结构化 JSON 的特性，将固定语法标记（如括号、字段名）作为 **Scaffold Token（支架标记）** 预填充并冻结。
- 仅对可变值部分（value tokens）进行扩散去噪，减少约 30% 的解码负担。
- 将扩散块边界与语义节（section）对齐（如 `critical_objects`, `explanation`, `future_meta_behavior`, `trajectory`），在节内双向建模，节间保持严格因果顺序，防止逻辑泄漏。

#### ✅ **Scaffold Speculative Decoding**
- 扩展 Self-Speculative Decoding，自动接受 Scaffold Tokens，无需验证。
- MDM Head 并行生成 Value Tokens 草稿，AR Head 串行验证，显著提升吞吐量，同时保持与纯 AR 相当的生成质量。

#### ✅ **Shared-Prefix Test-Time Scaling**
- 在测试时，利用前三个节的确定性前缀共享 KV Cache，从该缓存中分叉 N 条轨迹采样路径（stochastic rollouts），仅在轨迹节进行随机采样并平均。
- 以极低额外计算成本有效降低预测方差，提升精度。

### **相比现有方法的优势**
| 维度 | AR VLA | Full-Seq Diffusion | Fast-dDrive |
|------|--------|---------------------|------------|
| 推理效率 | 低（1 token/step） | 中（无 KV Cache 复用） | **高（~5 tokens/step）** |
| 结构正确性 | 易出错 | 依赖训练 | **100% 保证（Scaffold）** |
| 因果一致性 | 弱（暴露偏差） | 差（逻辑泄漏） | **强（节间因果）** |
| 可扩展性 | 有限 | 有限 | **支持低成本 test-time scaling** |

---

## **2. 核心实验方法和设置**

### **数据集**
- **WOD-E2E**（Waymo Open Dataset End-to-End）：
  - 包含 4,021 个长尾驾驶场景，每段 20 秒。
  - 使用前 12 秒输入预测未来 5 秒轨迹。
  - 提供 Chain-of-Thought 注释，适配四节结构输出。
- **nuScenes**：
  - 1,000 个城市驾驶场景，标注关键帧（2Hz）。
  - 用于跨数据集泛化能力验证。

### **输入模态**
- **视觉输入**：RGB 相机图像（WOD-E2E 使用三前视图；nuScenes 使用单前视图）。
- **状态输入**：自车状态（位置、速度、加速度、航向角等）。
- **导航指令**：自然语言命令（如 “turn left at next intersection”）。
- **不使用**：LiDAR、雷达、HD Map。

### **评估指标**
#### **规划准确性**
- **ADE@3s / ADE@5s**：3秒和5秒内的平均位移误差（Average Displacement Error）。
- **L2 Error**（nuScenes）：1s、2s、3s 预测点的 L2 距离误差。
- **RFS**（Rater Feedback Score）：人类对齐的信任评分，越高越好。

#### **推理效率**
- **Latency**：单样本墙钟时间（ms）。
- **TPS**（Tokens Per Second）：每秒处理 token 数。
- **Tok/Step**：每次前向传播提交的有效 token 数。

### **基线方法对比**
- **AR 类**：AutoVLA, Poutine-Base, OpenEMMA*, LightEMMA*
- **Diffusion 类**：dVLM-AD（全序列扩散）
- **Backbone**：基于 Qwen2.5-VL-3B，与 AR 基线共享相同主干网络和训练数据。

---

## **3. 主要实验结果和性能指标**

### **关键性能数据**

#### 📊 **WOD-E2E 测试集结果（Table 2）**
| 方法 | Paradigm | RFS↑ | ADE@5s↓ | ADE@3s↓ | TPS↑ |
|------|----------|-------|---------|---------|------|
| AutoVLA | AR | 7.557 | 2.958 | 1.351 | 51.2 |
| dVLM-AD | Diffusion | 7.633 | 3.022 | 1.285 | 35.2 |
| **Fast-dDrive (Scaffold Spec)** | **Block Diffusion** | **7.823** | **2.907** | **1.254** | **210.4** |
| +Inference Scaling (N=4) | Block Diffusion | 7.827 | **2.821** | **1.240** | 114.7 |

> ✅ **Fast-dDrive 实现 SOTA ADE@3s 和 ADE@5s，RFS 接近最高水平。**

#### 📊 **nuScenes 验证集 L2 误差（Table 3）**
| 方法 | L2@1s | L2@2s | L2@3s | Avg. |
|------|-------|-------|-------|------|
| UniAD | 0.20 | 0.42 | 0.75 | 0.46 |
| dVLM-AD | 0.15 | 0.40 | 0.68 | 0.41 |
| **Fast-dDrive** | **0.12** | **0.33** | **0.50** | **0.32** |

> ✅ **Fast-dDrive 将平均 L2 误差降至 0.32m，较基线提升 22%。**

#### ⏱️ **推理效率对比（Table 4，WOD-E2E Val）**
| 方法 | Latency (ms) | TPS | Tok/Step | ADE@5s |
|------|---------------|-----|-----------|--------|
| AR Baseline | 7855 | 51.6 | 1.0 | 2.083 |
| dVLM-AD | 9575 | 35.2 | 2.82 | 3.024 |
| Fast-dDrive (Self-Spec) | 3714 | 109.0 | 2.41 | 1.973 |
| **Fast-dDrive (Scaffold Spec)** | **1919** | **210.4** | **4.90** | **1.982** |
| **+SGLang** | **665** (**11.8×**) | **608.5** | **4.93** | 1.995 |

> ✅ **Scaffold Spec 实现 4.1× 速度提升，集成 SGLang 后达 11.8× 吞吐加速。**

### **消融实验结果（Ablation Study, Table 5）**
| IWL | SNS | ADE@5s↓ | RFS↑ |
|-----|-----|---------|------|
| × | × | 2.028 | 7.735 |
| √ | × | 2.003 | 7.855 |
| × | √ | 2.050 | 7.807 |
| √ | √ | **2.034** | **7.916** |

> 🔍 **IWL（Section-Importance-Weighted Loss）是主要贡献者，显著提升 RFS；SNS 进一步优化噪声调度，二者互补。**

---

## **4. 关键结论和发现**

### **主要发现**
1. **结构化先验可大幅提升效率与准确性**：
   - 冻结 Scaffold Token 不仅保证 100% 结构合法性，还减少 ~30% 解码开销。
   - 节对齐的块扩散在保留全局上下文的同时，恢复了 KV Cache 复用能力。

2. **块扩散优于全序列扩散与 AR**：
   - 在精度上超越 AR 与全序列扩散；
   - 在效率上实现 6× 于全序列扩散、4× 于 AR 的吞吐量。

3. **Scaffold Speculative Decoding 是高效高质量解码的关键**：
   - 自动跳过 Scaffold 验证，大幅减少冗余计算。
   - 结合 SGLang 可进一步释放系统级优化潜力。

4. **Test-Time Scaling 具有高性价比**：
   - 共享前缀 + 多轨迹采样可在 <2× 成本下显著降低 ADE。
   - 适用于安全敏感场景下的不确定性校准。

### **局限性**
- **Schema 依赖性强**：当前方法依赖预定义 JSON Schema，若任务结构变化需手动调整模板。
- **极端低延迟场景受限**：尽管共享前缀降低了开销，但在极高频率控制环路中仍可能受限。
- **开放回路评估为主**：目前实验集中于 open-loop benchmark，尚未在闭环仿真中验证动态响应能力。

### **未来工作方向**
- 支持动态 Schema 或可学习结构模板，增强泛化性。
- 探索闭环部署中的实时适应机制。
- 将 test-time scaling 与不确定性估计结合，实现风险感知决策。
- 扩展至多智能体交互与复杂城市交通流模拟。

---

> **总结**：  
> Fast-dDrive 通过 **结构感知的块扩散架构**，首次实现了 **高精度、高效率、高可解释性** 的统一。它证明了：**当输出具有已知结构时，将该结构显式编码进扩散过程，可在质量和速度上获得双重增益**，为下一代高效 VLA 模型提供了重要范式。

</details>

---

### 2. [AlignedServe: Orchestrating Prefix-aware Batching to Build a High-throughput and Computing-efficient LLM Serving System](https://arxiv.org/abs/2605.23389)

**Authors**: Fengyao Bai, Hongbin Zhang, Zhitao Chen, Jiangsu Du, Zhiguang Chen, Yutong Lu  
**Category**: cs.DC  
**Published**: 2026-05-25  
**Score**: 13.0  
**Type**: new  
**ArXiv ID**: 2605.23389v1  

#### Abstract
High-throughput inference serving is essential for applications built on large language models (LLMs). Existing serving frameworks reduce request-level and batch-level bubbles through batching and scheduling, but often overlook bubbles within each decode iteration. Tokens generated in the same itera...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*AlignedServe: Orchestrating Prefix-aware Batching to Build a High-throughput and Computing-efficient LLM Serving System*

---

## 1. 论文的主要贡献和创新点

### ✅ 解决了什么问题

传统 LLM 推理服务系统（如 vLLM、Orca）虽然通过 **continuous batching** 和批处理调度优化了请求级和批级别（request/batch-level）的流水线气泡（bubbles），但忽略了 **decode 阶段中每个迭代内部的细粒度性能瓶颈**。

具体而言，在同一个 decode 迭代中，不同请求生成 token 所依赖的 **KVCache 长度（即 prefix 长度）不同**，导致计算成本不均。长 prefix 请求成为瓶颈，迫使短 prefix 请求等待，形成 **iteration-level bubbles（迭代级气泡）**，严重降低 GPU 利用率和吞吐量。

---

### 🚀 提出的新方法与创新思路

本文提出 **AlignedServe**，一个全新的高吞吐、计算高效的 LLM 服务框架，其核心创新如下：

#### （1）**Prefix-aware Batching（前缀感知批处理）**
- 将具有相似 **prefix 长度**（即输入 prompt + 已生成 token 数量）的请求分组到同一批次。
- 保证同一批次内所有 token 的 **attention 计算开销相近**，消除因 prefix 长度差异导致的迭代内等待时间，从而 **消除 iteration-level bubbles**。

#### （2）**基于 CPU 内存的 KV Pool 架构**
- 利用大容量 CPU 主存（DRAM）作为 **KVCache 的暂存池（KV Pool）**，解耦 prefill 与 decode 阶段。
- 所有请求在 prefill 完成后，KVCache 被卸载至 CPU 内存，而非直接传给 decode GPU。
- 支持在 CPU 端进行大规模请求缓冲与 prefix-aware 分组，解决内存受限问题。

#### （3）**Batch-level Scheduling（批级别调度）**
- 不再采用传统的 request-level 调度（如 FCFS），而是以 **完整批次为单位进行调度**。
- 引入两个缓冲区：
  - **Candidate Batch Buffer**：存放即将运行的完整批次。
  - **Candidate Requests Buffer**：存放可动态加入当前运行批次的候选请求（如中途匹配的相似 prefix 请求或被驱逐后待重调度的请求）。

#### （4）**GPU-Prefetch-For-GPU 架构（首次提出）**
- 利用 **prefill GPU 作为 decode GPU 的 KVCache 预取中介**。
- KVCache 从 CPU → prefill GPU（via PCIe）→ decode GPU（via NVLink），**利用 NVLink 高带宽显著降低传输延迟**。
- 是首个将 **prefill GPU 用于为 decode GPU 预取 KVCache** 的工作。

---

### 🔍 相比现有方法的优势

| 方面 | 传统方法（如 vLLM, DistServe） | AlignedServe |
|------|-------------------------------|-------------|
| 批处理粒度 | 忽略 prefix 长度，随机混合长短请求 | 按 prefix 长度聚类，减少迭代内不平衡 |
| 气泡控制 | 仅优化 request/batch-level bubbles | 新增 **eliminate iteration-level bubbles** |
| KVCache 管理 | 直接驻留 GPU HBM 或按需换入换出 | 利用 CPU 大内存构建 KV Pool，支持大规模缓冲 |
| 数据传输 | CPU ↔ GPU via PCIe（低带宽） | 引入 **NVLink 中转预取**，降低调度延迟 |
| 调度机制 | request-level continuous batching | **batch-level scheduling + 动态请求注入** |

---

## 2. 核心实验方法和设置

### 📊 使用的数据集

#### 合成工作负载（Synthetic Workloads）
- 控制长短请求比例（短请求 <1k tokens，长请求 1k–8k tokens）。
- 设置不同短请求占比（70% ~ 95%），验证对长请求敏感场景下的鲁棒性。

#### 真实应用工作负载（Application Workloads）
| 数据集 | 描述 |
|--------|------|
| **AzurePublicDataset** | 微软发布的实际 LLM 推理轨迹，涵盖对话与编程任务 |
| **ShareGPT** | 用户与 ChatGPT-4 的多轮对话记录 |
| **LongBench** | 双语长上下文理解评测基准，测试长序列能力 |

---

### ⚙️ 实验设置

- **硬件平台**：
  - 2× Intel Xeon Platinum 8462Y+ CPU
  - 8× NVIDIA H100 GPU（NVLink 连接）
  - 800GB DRAM，PCIe 5.0 连接 CPU-GPU
- **模型**：
  - OPT-2.7B, OPT-6.7B, OPT-13B, OPT-30B（FP16 精度）
- **参数配置**：
  - Quad-tree 管理 prefix 范围：[1, 65536]
  - 最大批大小内存限制 `Bmax` = 40% GPU HBM
  - 最小批请求数 `Kmin` = 36

---

### 🎯 评估指标

| 指标 | 说明 |
|------|------|
| **Decoding Throughput (tokens/s)** | 单位时间内生成的 token 数量，衡量系统吞吐能力 |
| **P99 TPOT (Time Per Output Token)** | 99 百分位的每 token 生成时间，反映延迟稳定性 |
| **TTFT (Time to First Token)** | 首个 token 返回时间，影响用户体验 |
| **消融实验** | 对比是否启用 prefix-aware batching 与 GPU prefetching 的性能差异 |

---

### 🆚 基线方法对比

| 基线 | 特点 |
|------|------|
| **vLLM** | 当前主流服务系统，结合 Sarathi-Serve 与 Orca 技术，FCFS 调度 |
| **DistServe** | 解耦 prefill/decode 架构，类似本文基础架构 |
| **FastGen (DeepSpeed-FastGen)** | 高吞吐推理系统，支持混合 prefill/decode 批处理 |

> 注：未与 LoongServe、HotPrefix 等比较，因其优化目标正交（如长序列并行、共享 prefix 缓存等）。

---

## 3. 主要实验结果和性能指标

### 📈 解码吞吐量（Decoding Throughput）

| 场景 | 性能提升（vs. 基线） |
|------|------------------|
| **合成负载（95% 短请求）** | 较 vLLM 提升 **1.32×**，较 FastGen 提升 **1.85×** |
| **真实负载（AzurePublicDataset）** | 吞吐最高达 **1.98×** 于 vLLM/DistServe/FastGen |
| **ShareGPT / LongBench** | 吞吐提升 **1.35× ~ 1.98×** |

> 图 8 显示，在 OPT-13B 上，AlignedServe 在 ShareGPT 上达到约 700 tokens/s，远超其他系统（~350–500）。

---

### ⏱️ 解码延迟（P99 TPOT）

| 场景 | 延迟降低幅度 |
|------|------------|
| **合成负载** | 延迟降低 **1.74× ~ 3.05×** |
| **真实负载** | 
  - LongBench：降低 **2.1×**
  - ShareGPT：降低 **1.65×**
  - **AzurePublicDataset：最高降低 7.4×**

> 图 10 显示，在 AzurePublicDataset 上，AlignedServe 的 P99 TPOT 仅为 ~50ms，而 DistServe 超过 350ms。

---

### 🔬 消融实验结果（Ablation Study）

#### （1）**GPU Prefetching 与 Prefix-aware Batching 的独立贡献**
- 在 AzurePublicDataset 上：
  - 移除 GPU Prefetching → 吞吐下降 **14.73%**
  - 同时移除两者 → 吞吐再降 **28.51%**（总计下降 >40%）
- 表明两项技术均有显著贡献，且协同效应强。

#### （2）**Prefix-aware vs. FCFS 批处理**
- 在 LongBench 上对比：
  - 使用 prefix-aware batching：>90% 迭代可在 **30ms 内完成 forward computing**
  - 使用 FCFS：仅 <10% 迭代能在 30ms 内完成
- 证明 **prefix-aware batching 显著减少迭代内等待时间**

#### （3）**Batch Switch 开销分析**
- 在 ShareGPT 和 LongBench 上，跨 batch 请求共存的迭代占比：
  - ShareGPT：**≤8.61%**
  - LongBench：**≤12.37%**
- 说明 batch switch 时间短暂，对整体性能影响有限。

#### （4）**KV Pool 内存开销**
- 实际占用：**20GB ~ 250GB**（远低于 800GB 配置上限）
- 表明 CPU 内存资源充足，方案可行。

#### （5）**TTFT 影响**
- 平均 TTFT：
  - ShareGPT：**1.49s**
  - LongBench：**2.54s**
- 最大可达 30s，但可通过启用 **starvation handling 机制** 动态调整，保障 SLO。

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **Iteration-level bubbles 是影响 decode 性能的关键因素**，此前被广泛忽视。
2. **Prefix-aware batching 能有效消除此类气泡**，大幅提升 GPU 利用率与吞吐。
3. **利用 CPU 大内存构建 KV Pool + GPU 预取中转机制**，是实现高效 prefix-aware 分组的可行路径。
4. **NVLink 预取显著降低调度延迟**，优于传统 PCIe 传输。
5. 在真实应用场景下，AlignedServe 实现 **最高 1.98× 吞吐提升** 与 **高达 7.4× 的延迟降低**。

---

### ⚠️ 局限性

1. **引入额外首 token 延迟（TTFT）**：
   - 请求需等待足够相似 prefix 的请求到达才能组批。
   - 尽管平均 TTFT 可接受（<3s），但在极端情况下可能达 30s。
2. **依赖 NVLink 硬件环境**：
   - 若无 NVLink，退化为 PCIe 传输，性能优势减弱。
3. **复杂调度逻辑增加系统实现难度**：
   - 需维护 quad-tree、双缓冲区、动态调度策略等。

---

### 🔮 未来工作方向

1. **动态调整 batching 窗口大小**，平衡吞吐与延迟。
2. **支持异构硬件部署**（如跨节点 NVLink-less 环境）。
3. **结合 shared prefix 优化技术**（如 HotPrefix、BatchLLM），进一步提升缓存效率。
4. **探索更智能的饥饿避免机制**，支持多优先级 QoS。
5. **扩展至多模态 LLM 服务场景**。

---

## 总结

> **AlignedServe 是首个系统性识别并解决 LLM 推理中 iteration-level bubbles 的工作**。它通过 **prefix-aware batching + KV Pool + GPU-Prefetch-For-GPU 架构**，实现了 **高吞吐、低延迟、高资源利用率** 的推理服务，在多种真实负载下显著超越 vLLM、DistServe 和 FastGen 等 state-of-the-art 系统，为下一代 LLM serving 框架提供了重要设计范式。

</details>

---

### 3. [HyperParallel-MoE: Multi-Core Interleaved Scheduling for Fast MoE Training on Ascend NPUs](https://arxiv.org/abs/2605.23764)

**Authors**: Zewen Jin, Congkun Ai, Guangpeng Zhang, Hanbo Zhang, Haoran Wang, Shihan Xiao, Da Lei, Xuefeng Jin, Teng Su, Cheng Li  
**Category**: cs.DC  
**Published**: 2026-05-25  
**Score**: 12.5  
**Type**: new  
**ArXiv ID**: 2605.23764v1  

#### Abstract
Modern Mixture-of-Experts (MoE) models increasingly rely on large-scale AI accelerator clusters for efficient training. Ascend NPUs expose heterogeneous on-chip compute resources, including matrix-oriented AIC units and vector-oriented AIV units with explicit cross-queue synchronization support. How...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：HyperParallel-MoE: Multi-Core Interleaved Scheduling for Fast MoE Training on Ascend NPUs

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题

现代 **Mixture-of-Experts (MoE)** 模型在训练时严重依赖大规模 AI 加速器集群。然而，尽管 Ascend NPU 提供了异构的片上计算资源（如面向矩阵计算的 AIC 单元和面向向量操作的 AIV 单元），现有的训练框架仍以**算子级串行执行**的方式运行 MoE 操作，导致以下问题：

- **硬件利用率低**：AIC 和 AIV 单元交替空闲，无法并行执行。
- **通信与计算重叠不足**：Expert Parallelism (EP) 的 AllToAll 通信延迟中仅有约 61% 能被隐藏，剩余 39% 暴露在关键路径上。
- **同步开销高**：Host-side 集合通信引入全局同步屏障，阻碍细粒度调度。

这些问题限制了 MoE 在 Ascend 平台上的训练效率。

---

### 提出了什么新方法或新思路

本文提出 **HyperParallel-MoE** ——一个面向 Ascend NPU 的编译与调度框架，其核心思想是将 MoE-FFN 的执行从“算子级串行”转变为“**瓦片级异构任务流**”（tile-level heterogeneous taskflow）。

#### 主要创新点：

1. **AIV-driven one-sided communication**
   - 将传统的 Host-driven AllToAll 集体通信转换为由 AIV 单元驱动的设备侧 `put_mem_signal` 通信原语。
   - 每个通信 tile 独立完成远程写入并更新事件计数器，实现通信进度可调度、可重叠。

2. **Dependency-preserving tile task generation**
   - 基于 **Operator Dependency Graph (ODG)** 进行跨算子的瓦片分解。
   - 引入 **SplitSpec** 和 **split propagation** 机制，确保不同算子间的瓦片边界对齐，保持依赖关系正确性。
   - 支持 GMM、SwiGLU、Dispatch、Combine 等算子统一表示为 tile task。

3. **Event-driven static scheduling**
   - 编译阶段生成静态的 **Cube Task Queue (CTQ)** 和 **Vector Task Queue (VTQ)** 执行序列。
   - 使用 `CrossCoreSetFlag` / `CrossCoreWaitFlag` 实现轻量级事件同步，避免运行时动态调度开销。
   - 所有调度决策离线完成，运行时仅需消费预定义的任务流。

4. **Unified runtime with single kernel launch**
   - 整个 MoE-FFN 正反向传播在一个统一的 AscendC kernel 中执行。
   - AIC 和 AIV 工作线程并发消费 CTQ/VTQ，实现通信、矩阵计算、向量计算的细粒度重叠。

---

### 相比现有方法的优势

| 维度 | 现有方法（如 MindSpore 基线） | HyperParallel-MoE |
|------|-------------------------------|------------------|
| 执行模型 | 算子级串行 kernel launch | 瓦片级异构 taskflow |
| 通信机制 | Host-driven collective AllToAll | Device-side one-sided communication |
| 调度方式 | 动态、运行时决定 | 静态编译、预生成 SSC |
| 并发性 | AIC/AIV 交替执行 | AIC/AIV 并发执行 |
| 同步开销 | 全局 barrier | 事件计数器 fine-grained sync |
| 算子复用 | 优化算子易被绕过 | 复用现有优化算子（GMM, SwiGLU） |

> ✅ **优势总结**：在不重写高性能算子的前提下，通过调度层创新，充分挖掘 Ascend NPU 的异构并行潜力。

---

## 2. 核心实验方法和设置

### 使用的模型与配置

- **模型类型**：DeepSeek-V3-style MoE-FFN
- **参数规模**：总参数 ~671B，激活参数 ~37B
- **结构参数**：
  - Sequence Length: 4096
  - Hidden Size: 7168
  - Intermediate Size: 2048
  - Top-k: 8
  - 数据类型: bf16

### 实验平台

- **硬件**：Ascend A3 NPU 集群
- **每设备资源**：
  - 25 个 AIC 单元（矩阵计算）
  - 50 个 AIV 单元（向量/通信）
  - 192MB 片上 L2 Cache
- **并行策略**：
  - DP=32, TP=2, PP=8
  - EP 设置：EP4, EP8, EP16（对应专家总数 32/64/128）

### 评估指标

| 指标 | 描述 |
|------|------|
| **Module Latency** | Dispatch 到 Combine 的端到端延迟（正向 + 反向） |
| **End-to-End Step Latency** | 完整训练 step 的耗时（含 Attention、Dense 层等） |
| **Speedup** | 相对于基线的加速比 |

### 基线方法对比

- **Baseline**：标准的算子逐个执行模式（operator-by-operator）
  - 使用全设备 kernel
  - 使用集体通信 AllToAll
  - AIC/AIV 串行执行
- **HyperParallel-MoE**（完整版）：
  - 包含 one-sided communication
  - Rank-Aware Task Reordering (RATR)
  - Cache-guided GMM interleaving

---

## 3. 主要实验结果和性能指标

### 关键性能数据（模块级延迟）

| EP Setting | Baseline (ms) | HyperParallel-MoE (ms) | Speedup |
|------------|---------------|--------------------------|---------|
| EP4        | 44.2          | 29.6                     | **1.49×** |
| EP8        | 47.1          | 29.9                     | **1.58×** |
| EP16       | 48.9          | 31.1                     | **1.57×** |

> 🔹 在 **balanced routing** 场景下，MoE-FFN 模块延迟最高降低 **1.58×**。

#### 分阶段加速效果：
- **Forward**：1.60× ~ 1.68× 加速
- **Backward**：1.44× ~ 1.53× 加速

说明正反向均受益于 tile-level 重叠。

---

### 端到端训练速度提升

| EP Setting | End-to-End Speedup |
|------------|--------------------|
| EP4        | **1.08×**          |
| EP8        | **1.09×**          |
| EP16       | **1.09×**          |

> 🔸 尽管 MoE-FFN 仅占整个训练流程的一部分，该优化仍带来 **~9%** 的端到端加速。

---

### 消融实验与微基准测试（Microbenchmarks）

#### （1）Tile Interleaving 对 L2 Cache 利用的影响（SwiGLU+Add）

| M (Row Dim) | Serial Latency (μs) | Interleaved Latency (μs) | Speedup | L2 Hit Rate |
|-------------|---------------------|---------------------------|---------|--------------|
| 32K         | 723.29              | 588.38                    | **1.23×** | 5.20% → **25.44%** |

> ✅ 证明 tile interleaving 显著提升 L2 缓存命中率（达 4.9×），减少 HBM 访问。

#### （2）Static vs Dynamic Scheduling 开销对比

| M (Row Dim) | Dynamic Scheduling (μs) | Static Scheduling (μs) | Overhead Ratio |
|-------------|--------------------------|------------------------|----------------|
| 2K          | 413.00                   | 54.00                  | **7.65×**       |
| 32K         | 862.80                   | 588.38                 | **1.47×**       |

> ✅ 动态调度每 task 开销高达 2.36 μs，远超静态调度的 0.1 μs，验证了静态调度的必要性。

---

## 4. 关键结论和发现

### 主要发现

1. **Ascend NPU 的异构性未被现有框架充分利用**  
   当前框架将 AIC/AIV 视为互斥资源，导致严重资源浪费。

2. **Tile-level heterogeneous scheduling 是提升 MoE 效率的关键**  
   将通信、矩阵、向量操作统一为可调度的 tile task，并通过静态编排实现高效重叠。

3. **One-sided communication + event-driven sync 可消除主机同步瓶颈**  
   设备侧通信任务与计算任务共享事件机制，实现真正的细粒度重叠。

4. **静态调度优于动态调度**  
   在稳定训练阶段，编译期生成的 SSC 可显著降低运行时开销，尤其在小 tile 场景下优势明显。

5. **无需重写算子即可获得显著加速**  
   通过封装现有优化算子为 task handler，实现了高性能与灵活性的平衡。

---

### 方法的局限性

1. **依赖稳定的形状和并行配置**  
   若 tensor shape 或 routing 分布剧烈变化，可能需要重新编译 SSC。

2. **当前实现聚焦 MoE-FFN 路径**  
   未覆盖全部模型组件（如 Attention），端到端加速受限于非 MoE 部分。

3. **对 Ascend 架构强依赖**  
   依赖 AIC/AIV 分离队列、事件同步、远程内存访问等特性，难以直接迁移到其他架构（如 GPU）。

---

### 未来工作方向

1. **支持动态 shape 和 adaptive routing 的运行时适配机制**  
   结合 shape bucketing 或轻量级 runtime fallback。

2. **扩展至更多算子和模型结构**  
   将统一调度框架推广至 Attention、Embedding、LayerNorm 等。

3. **探索更复杂的调度策略**  
   如基于 profiling 的自动 tuning、跨 step 的任务流水线。

4. **集成到更高层训练系统**  
   与自动并行、分布式调度器深度协同，构建端到端优化的 MoE 训练栈。

---

> 📌 **总结一句话**：  
> **HyperParallel-MoE 通过“瓦片化 + 静态异构调度 + 设备侧通信”，在不修改算子实现的前提下，将 Ascend NPU 上 MoE-FFN 的训练延迟降低了 1.58×，验证了调度层创新在现代异构 AI 架构中的巨大潜力。**

</details>

---

### 4. [Steered Generation via Gradient-Based Optimization on Sparse Query Features](https://arxiv.org/abs/2605.23040)

**Authors**: Sumanta Bhattacharyya, Pedram Rooshenas  
**Category**: cs.LG  
**Published**: 2026-05-25  
**Score**: 11.5  
**Type**: new  
**ArXiv ID**: 2605.23040v1  

#### Abstract
Latent steering exploits internal representations of Large Language Models (LLMs) to guide generation, yet interventions on dense states can entangle distinct semantic features. In this paper, we investigate attention query activations as a high-fidelity site for precise control, hypothesizing that ...

---

### 5. [Energy per Successful Goal: Goal-Level Energy Accounting for Agentic AI Systems](https://arxiv.org/abs/2605.22883)

**Authors**: Deepak Panigrahy, Aakash Tyagi  
**Category**: cs.AI  
**Published**: 2026-05-25  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2605.22883v1  

#### Abstract
Current AI energy benchmarks measure consumption at the granularity of a single model invocation or training run. For classical single-turn workloads this unit remains coherent. For agentic systems - where a single user goal may trigger multi-step orchestration, tool calls, retries, and failure-reco...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Energy per Successful Goal: Goal-Level Energy Accounting for Agentic AI Systems

---

## 1. 论文的主要贡献和创新点

### **解决了什么问题**

当前主流的 AI 能耗评估方法采用 **Energy-per-inference**（每推理一次的能量消耗）作为度量单位，这在单轮、静态任务（如单次问答）中是合理的。然而，在 **Agentic AI 系统**（代理型 AI）中，一个用户目标（goal）可能触发多步执行流程，包括规划（planning）、工具调用（tool calling）、重试（retry）和失败恢复等动态行为。

在这种场景下，**inference 数量是系统实现细节，而非任务本身的属性**。因此，以“每次推理”为单位进行能耗归一化会严重低估真实成本，尤其是当系统因失败而多次重试时，这些额外开销被完全忽略。

该论文指出，这种“单位错配”（unit misalignment）导致：
- 高估高可靠性系统的能效；
- 掩盖了 **orchestration overhead**（编排开销）的真实影响；
- 无法公平比较不同架构（如线性 vs 多步代理）的能耗表现。

---

### **提出了什么新方法或新思路**

论文提出了一套完整的跨层测量框架 **A-LEMS**（Agentic LLM Energy Measurement System），并引入两个核心概念：

#### ✅ **Energy per Successful Goal (EpG)**  
> 单位：Joules per successful goal (J/goal)

这是新的基本能量计量单位。它将整个工作流（workflow）的所有尝试（包括失败和重试）的总能耗，除以**成功完成的目标数量**。

$$
\text{EpG} = \frac{\sum_{j \in W^+} E_{\text{workflow},j}}{|W^+|}
$$

其中 $W^+$ 是成功完成的工作流集合。

#### ✅ **Orchestration Overhead Index (OOI)**  
> 单位：无量纲比率（×）

用于衡量 **agentic 工作流相对于线性基线的相对能耗开销**：

$$
\text{OOI} = \frac{\text{EpG}_{\text{agentic}}}{\text{EpG}_{\text{linear}}}
$$

- 若 OOI > 1：表示代理模式更耗能（存在 **orchestration tax**）
- 若 OOI < 1：表示代理模式更节能（存在 **orchestration dividend**）

---

### **相比现有方法的优势**

| 维度 | 传统方法（Energy-per-inference） | A-LEMS（EpG + OOI） |
|------|-------------------------------|---------------------|
| **计量单位** | 按实现步骤（inference）计费 | 按最终交付成果（goal）计费 |
| **是否包含失败开销** | ❌ 忽略失败尝试 | ✅ 显式计入所有尝试 |
| **边界定义** | 不明确，常包含前后处理 | ✅ 明确定义 `[t₀, t₁]` 归属窗口 |
| **可复现性** | 缺乏硬件/环境绑定 | ✅ 三哈希协议（Hhw/Henv/Hrun）确保可复现 |
| **适用性** | 仅适用于单步任务 | ✅ 支持多步、带工具调用的 agentic 流程 |

此外，A-LEMS 还提供了：
- 五层观测管道（L0–L4）：从 RAPL 信号到目标级聚合
- 相位分解能力（phase decomposition）：区分 planning、execution、synthesis 和 retry 开销
- 开源可复现的数据查询接口（SQL scripts）

---

## 2. 核心实验方法和设置

### **使用的数据集与任务家族**

共涵盖 **8 类任务家族**，分为两大类：

#### 🔹 **推理任务（Reasoning Tasks）**
| ID | 名称 | 描述 |
|----|------|------|
| FQA | Factual QA | 事实性问答 |
| SciQA | Science QA | 科学类问答 |
| LR | Logical Reasoning | 逻辑推理 |
| GSM8K-B | Basic Arithmetic | 基础算术题（单步） |
| GSM8K-M | Multi-step Arithmetic | 多步数学推理 |

#### 🔹 **工具增强任务（Tool-Augmented Tasks）**
| ID | 名称 | 描述 |
|----|------|------|
| TG:Calc | Single-tool (Calculator) | 使用计算器解决表达式 |
| TG:DB | Single-tool (Database) | 查询数据库获取答案 |
| TG:Seq2 | Tool Chain (DB + File) | 多工具串联任务 |

> 所有任务均来自标准 benchmark（如 GSM8K），每个目标对应一条 prompt-answer 对。

---

### **实验设置**

#### ✅ **两种推理模式**
- **本地推理**：使用 `Ollama/TinyLlama-1B`，通过 RAPL 测量完整 CPU 包能耗
- **远程推理**：使用 `Groq API/llama-3.3-70b`，仅测量客户端侧编排能耗（server-side 不直接测）

#### ✅ **对照设计（Matched Pair Design）**
对每一个目标，分别运行：
- **Agentic 模式**：启用 planning、tool calling、retry 机制
- **Linear 模式**：单次 prompt → 单次 inference，无工具、无分支、无重试

两者在同一 session 内背靠背执行，控制热态、DVFS 等变量。

#### ✅ **失败注入研究（Failure Injection Study）**
人工注入 JSON 解析错误、工具调用失败等，模拟真实系统中的 retry 行为，量化其能耗放大效应。

---

### **评估指标**

| 指标 | 定义 | 用途 |
|------|------|------|
| **EpG** | 总工作流能耗 / 成功目标数 | 绝对能耗基准 |
| **OOI** | EpG_agentic / EpG_linear | 相对编排开销 |
| **Coverage (C)** | RAPL 采样覆盖时间占比 | 验证相位归因精度 |
| **Success Rate** | 成功目标比例 | 衡量系统可靠性 |
| **Phase Power Profile** | 各阶段平均功率（W） | 分析能耗分布 |

---

## 3. 主要实验结果和性能指标

### **关键性能数据**

| 指标 | 数值 | 来源 |
|------|------|------|
| **平均 EpG（代理）** | 888.1 J/goal | 图 7(c), 表 5 |
| **平均 EpG（线性）** | 205.3 J/goal | 图 7(c), 表 5 |
| **平均 OOI** | **4.33×** | 全文核心结果 |
| **最大 OOI** | 7.63×（GSM8K-M） | 表 5 |
| **最小 OOI** | 0.62×（TG:Calc） | 表 5 |
| **采样覆盖率（C）** | 平均 >90%，黄金标准（≥95%）达 90%+ | 图 8(c) |

---

### **与基线方法的对比结果**

| 任务类型 | OOI | 结论 |
|--------|-----|------|
| FQA | 4.65× | 代理更耗能 |
| SciQA | 5.79× | 代理显著更耗能 |
| LR | 4.68× | 逻辑推理开销大 |
| GSM8K-B | 2.75× | 单步算术仍需规划开销 |
| GSM8K-M | **7.63×** | 多步任务编排开销最高 |
| TG:Calc | **0.62×** | 工具调用大幅节能 |
| TG:DB | 0.96× | 接近平价，略优 |
| TG:Seq2 | 1.55× | 多工具协调带来净开销 |

> ⚠️ **关键发现**：对于需要大量 token 生成的任务（如数学推理），**代理反而更耗能**；但对于可用工具替代的任务（如计算、查表），**代理更节能**。

---

### **消融实验结果**

#### ✅ **C1: 测量有效性验证**
- 采样频率稳定在 ~100 Hz（均值 9.71ms）
- 所有 RAPL delta 均为非负，无读取丢失或回绕
- 覆盖率 C ≥ 95% 的样本占绝大多数（>90%）

#### ✅ **C2: 可复现性验证**
- 三哈希协议（Hhw/Henv/Hrun）完整记录每轮运行上下文
- 热漂移、调度策略变化均可追溯

#### ✅ **C3: 边界模型验证**
- 使用 `[t₀, t₁]` 精确界定归属窗口，排除 pre-task 和 post-task 开销
- 线性任务因运行快，post-task 占比更高 → 若不剔除会导致 OOI 被压缩至 1.0

#### ✅ **C4: 区分力验证**
- OOI 在不同任务间呈现合理梯度（简单任务低，复杂任务高）
- 工具任务出现 **OOI < 1**，证明指标不会固定偏向代理不利

#### ✅ **C5: 编排主导性验证**
- 在 **零失败任务子集** 上，OOI 仍高达 **4.9×**
- 说明即使没有 retry，仅 **planning loops、inter-step coordination** 就已造成巨大开销
- retry 仅加剧已有趋势，非根本原因

---

## 4. 关键结论和发现

### **主要发现**

1. ✅ **Energy-per-inference 是错误的计量单位**  
   在 agentic AI 中，它掩盖了 retry、planning、coordination 的真实成本，导致对系统能效的误判。

2. ✅ **EpG 和 OOI 是更合理的计量体系**  
   - EpG 反映“每交付一个有用结果”的真实能耗
   - OOI 提供跨架构的标准化比较尺度

3. ✅ **代理系统通常更耗能（OOI ≈ 4.33×）**  
   主要开销来自：
   - 多轮 planning
   - 中间状态管理
   - retry 循环（失败尝试能耗可达成功尝试的 1.6×）
   - 客户端编排活动（如等待 API 返回期间 CPU 持续活跃）

4. ✅ **但也存在“节能反转”现象（OOI < 1）**  
   当代理可通过调用工具（如 calculator）避免昂贵的 token 生成时，整体能耗更低。

5. ✅ **编排结构是能耗主因，而非推理底座**  
   即使更换模型大小或本地/远程部署，OOI > 1 的趋势依然成立。

---

### **方法的局限性**

| 局限 | 说明 |
|------|------|
| **仅测量本地 CPU 能耗** | GPU、NIC、远程服务器未直接测量（remote 场景下为下界估计） |
| **成功为二元判定** | 不支持部分正确或质量分级评分 |
| **依赖匹配的线性基线** | OOI 无法单独报告，必须有对应的 linear 配对实验 |
| **未标准化远程服务端能耗** | 缺乏统一 API 提供商的 per-request 能耗接口 |

---

### **未来工作方向**

1. **扩展测量范围**  
   将 GPU、网络传输、远程服务器能耗纳入统一归因框架。

2. **建立标准化的远程能耗接口**  
   推动 LLM API 提供商开放 per-call 能耗信号。

3. **发展基于 EpG 的优化技术**  
   如减少 planning 次数、优化 retry 策略、自动路由到工具路径。

4. **构建面向 agentic 的绿色 AI benchmark**  
   使用 EpG 和 OOI 替代传统的 energy-per-token/inference 指标。

5. **探索质量-能耗联合优化空间**  
   引入 soft success 或 reward-weighted EpG，支持连续输出质量建模。

---

> 📌 **一句话总结**：  
> 本文揭示了当前 AI 能耗评估的根本缺陷，并提出 **EpG** 和 **OOI** 作为新一代计量标准——不再问“一次推理花多少电”，而是问“**达成一个目标到底花了多少电？**”

</details>

---

### 6. [ImProver 2: Iteratively Self-Improving LMs for Neurosymbolic Proof Optimization](https://arxiv.org/abs/2605.22885)

**Authors**: Riyaz Ahuja, Tate Rowney, Jeremy Avigad, Sean Welleck  
**Category**: cs.AI  
**Published**: 2026-05-25  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2605.22885v1  

#### Abstract
Formal mathematics libraries are rapidly expanding, creating a growing need to refactor verified proofs for maintainability and to improve training data quality for neural provers. However, scalable proof optimization is hindered by heterogeneous and heuristically specified objectives, scarce data, ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*ImProver 2: Iteratively Self-Improving LMs for Neurosymbolic Proof Optimization*

---

## 1. 论文的主要贡献和创新点

### 解决的问题
该论文针对**形式化数学证明库**（如 Lean 的 Mathlib）快速增长所带来的**代码质量与可维护性挑战**。具体问题包括：
- 形式化证明风格异构、冗长、依赖复杂，影响人类可读性和长期维护。
- 低质量的证明会降低其作为神经定理证明器（neural provers）训练数据的有效性。
- 现有自动化重构方法受限于目标函数多样性、数据稀缺、训练/推理成本高等问题。

### 提出的新方法与创新思路
论文提出了 **ImProver 2**，一个用于在 Lean 4 中进行自动化证明优化的 **neurosymbolic 框架**，其核心创新包括：

#### （1）迭代自改进训练框架（Iterative Self-Improvement）
- 基于 **Iterative Reasoning Preference Optimization (IRPO)** 算法，通过多轮生成、评分、偏好学习实现模型自我提升。
- 引入**回放缓冲区**（replay buffer），混合旧数据与新生成样本，防止模型崩溃（model collapse），确保单调改进。

#### （2）结构化优化指标（Structural Optimization Metrics）
提出并研究了三个超越单纯“缩短长度”的实用化指标：
- **Length**：最小化证明中的 tactic 数量。
- **Dependencies**：最小化显式引用的外部引理数量，鼓励自包含证明。
- **Modularity**：最大化有效“分支目标”（spawned goals）的数量，衡量证明的模块化程度（如 `have`, `calc` 等引入的独立子证明）。

#### （3）神经符号增强（Neurosymbolic Augmentation）
为模型提供来自 Lean 证明环境的丰富上下文，显著提升小模型能力：
- **Context**：提取相关定义、引理及其文档。
- **Chain-of-States (CoS)**：插入每个 tactic 执行前后的 goal state 注释，暴露证明结构。
- **Auto-informalization**：将形式化证明自动翻译为自然语言草图，提供语义抽象层。

### 相比现有方法的优势
- **高效利用小模型**：仅用 **7B 参数模型**即可超越更大规模模型（如 671B DeepSeek-R1）和部分前沿闭源模型（如 GPT-5-mini）。
- **任务专用性强**：相比通用大模型，ImProver 2 在特定结构化指标（尤其是 **Modularity** 和 **Dependencies**）上表现更优。
- **数据效率高**：通过迭代偏好学习，从自身生成的数据中持续学习，减少对大规模标注数据的依赖。
- **开源与可复现**：作者开源了代码与数据，推动社区发展。

---

## 2. 核心实验方法和设置

### 数据集
- 来源于多个公开的 **Lean 4 研究级数学项目**，涵盖不同领域：
  - `Mathlib`, `HepLean`, `ConNF`, `Seymour`, `FLT`, `Foundation`, `Carleson` 等。
- 测试集为 **miniCTX-v2**，包含人工编写的研究级定理。
- 训练/验证集按 80%/20% 划分，并排除与测试文件同源的定理以防止数据泄露。

### 实验设置与评估指标
- **基础模型**：`DeepSeek-R1-Distill-Qwen-7B`。
- **训练方式**：采用 IRPO 进行多轮迭代训练，每轮生成候选证明，基于正确性与指标得分构建偏好对进行微调。
- **评估协议**：
  - 使用 **best@16** 采样策略（即生成 16 个候选，选最优者）。
  - 报告 **平均改进分数**（mean improvement）：`μ(c,x,y) - μ(c,x,y₀)`。
  - 辅助指标：
    - **编译准确率**（Compilation Accuracy）：生成证明能通过 Lean 编译的比例。
    - **改进准确率**（Improved Accuracy）：在编译正确的前提下，指标得分严格提升的比例。

### 基线方法对比
- **同族模型**：DeepSeek-R1 系列（7B, 14B, 671B）。
- **前沿模型**：
  - 闭源：GPT-4o, GPT-5-nano, GPT-5-mini, GPT-5-chat, GPT-5-high。
  - 开源：GPT-oss-120B（稀疏 MoE 模型）。
- **先前系统**：原始 ImProver（基于 GPT-4o 的多步提示系统）。
- 所有模型均在有无 **neurosymbolic scaffold** 的条件下进行比较。

---

## 3. 主要实验结果和性能指标

### 关键性能数据（MiniCTX-v2, best@16 平均改进）

| Model | Length | Modularity | Dependencies |
|-------|--------|------------|--------------|
| **ImProver 2 (7B)** | **0.330** | **0.143** | **0.206** |
| GPT-5-high | 0.660 | 0.120 | 0.208 |
| GPT-5-mini | 0.330 | 0.109 | 0.203 |
| GPT-oss-120B | 0.321 | 0.075 | 0.181 |
| ImProver (GPT-4o) | 0.355 | 0.088 | 0.047 |

> ✅ **结论**：ImProver 2 在 **Modularity** 上领先所有未加 scaffold 的系统，在 **Dependencies** 上与最强闭源模型持平，在 **Length** 上匹配 GPT-5-mini。

### 与基线方法的对比结果
- **参数缩放 vs. 任务专业化**：
  - 尽管更大的 DeepSeek-R1-671B 模型更强，但 **ImProver 2 (7B)** 在所有三项指标上均超过它（尤其 Modularity: 0.143 vs 0.055），表明**任务特定训练可补偿通用规模劣势**。
- **优于开源基线**：
  - 超过 GPT-oss-120B（激活约 5B 参数），说明小而精的密集模型经优化后仍具竞争力。
- **优于前代 ImProver**：
  - 在 **Modularity** 和 **Dependencies** 上大幅领先（0.143 vs 0.088；0.206 vs 0.047），显示迭代训练比单纯提示工程更能捕捉结构性重构行为。

### 消融实验结果
#### （1）神经符号增强（Scaffold）的影响（Table 3）
- 加入 scaffold 显著提升几乎所有模型的表现：
  - DeepSeek-R1-7B 在 Length 上从 0.118 → 0.236（+100%）。
  - GPT-5-high 在 Length 上从 0.660 → 0.875（+32.6%）。
- 表明 **neurosymbolic augmentation 是关键增益来源**，不仅限于小模型。

#### （2）迭代训练进展（Table 2）
- 多数改进发生在前 2–3 轮 IRPO 训练中，之后趋于饱和或轻微回退。
- 显示模型确实从自身生成的高质量样本中学习到了有效的重构模式。

#### （3）准确性权衡分析（Table 4 & 5）
- 优化往往提高 **Improved Accuracy**，但可能降低 **Compilation Accuracy**。
  - 例如 Dependency 优化：改进准确率从 0.037 升至 0.106，但编译准确率从 0.754 降至 0.417。
- 反映了**结构性编辑的风险收益权衡**：更大胆的改写可能带来更高回报，但也更容易出错。

---

## 4. 关键结论和发现

### 主要发现
1. **小模型也能胜任复杂证明重构**：通过 **iterative self-improvement + neurosymbolic augmentation**，7B 模型可在多个指标上媲美甚至超越百B级模型。
2. **结构化指标是可学习的**：**Modularity** 和 **Dependencies** 等非长度类目标可通过偏好学习有效优化，且具有实际意义。
3. **神经符号信息至关重要**：暴露 Lean 内部状态（goal traces）、上下文和非正式化描述，极大提升了模型搜索高质量重构的能力。
4. **任务专业化胜过盲目扩模**：在特定任务上，精心设计的训练流程比单纯扩大模型规模更有效。

### 局限性
- **指标代理性**：所提指标（如 dependency count）是主观“证明质量”的代理，未必完全反映维护者的偏好。
- **缺乏人类偏好研究**：未进行用户调研验证优化后的证明是否更受人类欢迎。
- **单步重写限制**：当前为单步生成，未探索 agent-style 的多步修复或交互式优化。
- **编译稳定性下降**：更强的优化可能导致编译失败率上升，需结合修复机制。

### 未来工作方向
- 将维护者偏好直接建模（如通过 LLM-based reward modeling）。
- 探索训练数据优化对下游定理证明器性能的影响。
- 构建基于 ImProver 2 的 **agentic repair loop**，平衡大胆重构与稳定性。
- 扩展至其他形式化系统（如 Coq, Isabelle）和其他优化目标（如可读性、教学价值）。

--- 

> **总结**：*ImProver 2* 成功展示了如何通过 **迭代学习 + 神经符号增强**，使小型语言模型掌握复杂的、面向结构的形式化证明重构能力，为构建高效、可扩展的自动化数学库维护工具提供了新范式。

</details>

---

### 7. [Convex Optimization for Alignment and Preference Learning on a Single GPU](https://arxiv.org/abs/2605.23244)

**Authors**: Miria Feng, Mert Pilanci  
**Category**: cs.LG  
**Published**: 2026-05-25  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2605.23244v1  

#### Abstract
Fine-tuning large language models (LLMs) to align with human preferences has driven the success of systems such as Gemini and ChatGPT. However, approaches like Reinforcement Learning from Human Feedback (RLHF) remain computationally expensive and complex. Direct Preference Optimization (DPO) offers ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：Convex Optimization for Alignment and Preference Learning on a Single GPU**

---

## **1. 论文的主要贡献和创新点**

### **解决了什么问题**
当前主流的大型语言模型（LLM）对齐技术如 **Reinforcement Learning from Human Feedback (RLHF)** 和 **Direct Preference Optimization (DPO)** 存在以下问题：
- **计算成本高**：需要大量 GPU 资源，尤其是 DPO 需要维护一个冻结的 reference model，显著增加显存开销。
- **训练不稳定**：DPO 的 reward margin 增长不平稳，易出现波动。
- **超参数敏感**：DPO 和 ORPO 对学习率等超参数高度依赖，调参成本大。
- **效率低下**：传统方法在单卡上难以高效运行，限制了其在资源受限场景的应用。

---

### **提出了什么新方法或新思路**
本文提出 **COALA (Convex Optimization for Alignment and Preference Learning Algorithm)**，一种基于凸优化的轻量级偏好对齐框架，核心思想如下：
- **引入 Convex Neural Networks (cvxNN)**：在预训练 LLM 上叠加一个可凸化求解的两层神经网络作为偏好分类器。
- **参考模型无关（reference-free）**：无需 reference model，节省显存并简化流程。
- **使用 ADMM 优化器（CRONOS）**：采用 **Alternating Direction Method of Multipliers (ADMM)** 的变体 CRONOS 进行训练，具备强收敛保证且对超参数鲁棒。
- **理论保障**：证明了 COALA 的损失函数是凸的，可在多项式时间内达到全局最优。

---

### **相比现有方法的优势**
| 维度 | COALA | DPO / ORPO |
|------|--------|------------|
| **显存消耗** | 显著降低（仅需 ~17.6% DPO 的 TFLOPs） | 高（需双模型并行） |
| **训练稳定性** | Reward margin 单调稳定上升 | 波动大，需小学习率控制 |
| **超参数敏感性** | 极低（近似无超参依赖） | 高（需精细调参） |
| **硬件要求** | 可在单张 RTX-4090（24GB VRAM）上运行 | 通常需 A100（40GB）及以上 |
| **理论保证** | 具备全局收敛性证明 | 非凸优化，无全局最优保证 |

---

## **2. 核心实验方法和设置**

### **使用的数据集**
共使用 **4 个数据集**，涵盖教育、情感、通用对话等多个领域：

| 数据集 | 类型 | 样本数（偏好对） | 特点 |
|-------|------|------------------|------|
| **EduFeedback** | 教育问答 | 65,606 | 本文合成的 26,621 场学生-导师对话，通过“交替种群策略”生成偏好对 |
| **UltraFeedback** | 多模型反馈 | 60,917 | GPT-4 对多个开源模型输出打分后二值化 |
| **IMDb** | 情感分析 | 25,000 | 正负影评生成任务 |
| **HelpSteer** | 助手行为对齐 | 7,708 | 包含帮助性、正确性等多属性标注 |

> ✅ **创新数据构建方法**：提出 **Alternating Population Strategy**，从多轮对话中提取多个 `(prompt, chosen, rejected)` 三元组，提升数据利用率。

---

### **实验设置和评估指标**

#### **模型范围**
- 共测试 **6 个模型**：DistilGPT-2, GPT-2, Mistral-7B, Dolphin-2.6-7B, Llama-3.2-3B, Llama-3.1-8B

#### **硬件配置**
| 方法 | GPU | VRAM | 加速框架 |
|------|-----|------|----------|
| COALA | RTX-4090 | 24GB | JAX + XLA |
| DPO/ORPO/SFT | A100 | 40GB | PyTorch + DeepSpeed + LoRA |

> ⚠️ 注：为公平比较，其他方法使用更强硬件，而 COALA 在更弱设备上仍表现更优。

#### **评估指标**
- **AlpacaEval2**：自动评测指令跟随能力（Length-Controlled Win Rate, LC WR%）
- **MT-Bench**：多轮对话质量评分
- **ArenaHard**：更具挑战性的对抗性评测
- **Human Evaluation**：107 名真实用户参与双盲测评，评估实际偏好
- **TFLOPs**：衡量训练总计算量

---

### **基线方法对比**
- **SFT**：监督微调，基础 baseline
- **DPO**：主流偏好优化方法
- **ORPO**：无需 reference model 的改进版 DPO
- （部分实验还包含 SimPO）

---

## **3. 主要实验结果和性能指标**

### **关键性能数据**

#### **AlpacaEval2 结果（LC WR%，Llama-3.1-8B）**
| 方法 | EduFeedback | UltraFeedback | IMDb |
|------|-------------|---------------|------|
| **COALA** | **40.90±0.09** | 38.20±0.11 | **27.64±0.27** |
| DPO | 40.68±0.10 | 38.53±0.47 | 21.79±0.29 |
| ORPO | 23.87±0.60 | 20.58±0.68 | 12.10±0.71 |
| SFT | 10.92±0.20 | 10.75±0.39 | 8.16±0.11 |

✅ **COALA 在多数任务上优于或持平 DPO，远超 ORPO 和 SFT，且方差极小**。

---

#### **人类评估结果（107 名真实用户）**
| 数据集 | COALA | DPO | ORPO | SFT |
|-------|--------|------|------|-----|
| **EduFeedback** | **39.1%** | 28.8% | 15.5% | 16.6% |
| **IMDb** | **42.7%** | 24.8% | 20.1% | 12.4% |

✅ **COALA 在真实人类偏好中取得最高胜率，验证其实际有效性**。

---

#### **计算效率（TFLOPs，EduFeedback 数据集）**
以 Llama-3.1-8B 为例：
- **COALA**: **1,805.39 TFLOPs**
- **DPO**: 10,253.37 TFLOPs
- **ORPO**: 12,352.98 TFLOPs

➡️ **COALA 仅消耗约 DPO 的 17.6% 计算量**，实现同等甚至更优性能。

---

### **消融实验结果**

#### **Stage 1 使用 CRONOS vs AdamW**
| 模型 | CRONOS 准确率 | AdamW 准确率 |
|------|----------------|--------------|
| Llama-8B | **57.68%** | 51.20% |
| Mistral-7B | **57.63%** | 52.95% |
| Dolphin-7B | **62.27%** | 56.33% |

✅ **CRONOS 在分类准确率上全面超越 AdamW，且无需调参**。

#### **SFT 初始化影响**
- 所有方法在 SFT 初始化后性能提升。
- 但 **COALA 即使不依赖强 SFT 初始化，也能快速收敛并保持高性能**，显示其鲁棒性。

---

## **4. 关键结论和发现**

### **主要发现**
1. **凸优化可用于 LLM 偏好对齐**：首次成功将 cvxNN 应用于 LLM 对齐任务，实现理论可解释性和工程高效的统一。
2. **COALA 更快、更稳、更省**：
   - 训练过程 reward margin 单调上升，无需小学习率“护航”。
   - 显著降低 TFLOPs 和 VRAM 占用，支持单卡训练。
   - 对超参数几乎不敏感，降低部署门槛。
3. **真实人类偏好验证有效**：自动评测指标（如 AlpacaEval）可能被“刷分”，而 COALA 在真实人类评估中依然领先，说明其对齐效果更贴近真实需求。
4. **Alternating Population Strategy 提升数据效率**：从多轮对话中提取多个偏好样本，无需外部模型打分，降低成本。

---

### **方法的局限性**
- **表达能力受限**：仅微调顶层 cvxNN，冻结主干模型，可能无法捕捉深层语义变化（如创造性写作风格迁移）。
- **适用场景有限**：更适合事实性、教学性、简洁指令类任务，对复杂推理或风格化生成可能不如全参数微调。
- **推理阶段未深度优化**：本文聚焦训练效率，推理时仍依赖引导采样（guided sampling），未来可进一步集成 beam search 或 lookahead 策略。

---

### **未来工作方向**
1. **扩展至多模态与推理任务**：探索 COALA 在视觉-语言模型（VLM）或数学推理中的应用（如 GRPO 风格）。
2. **动态特征选择机制**：研究如何自适应选择最有效的隐藏层特征输入 cvxNN。
3. **在线对齐与持续学习**：结合 COALA 的稳定性，构建可持续更新的对齐系统。
4. **更高效的推理策略**：开发基于 cvxNN 的批处理引导解码（batched guided decoding）或连续指导尺度（continuous guidance scale）。
5. **跨数据集泛化研究**：在更多领域（如医疗、法律）验证 COALA 的普适性。

---

> 🔚 **总结一句话**：  
> **COALA 是首个将凸优化成功应用于 LLM 偏好对齐的工作，实现了高效、稳定、低成本的单卡训练，在性能、效率和人类偏好上均优于 DPO 等主流方法，为资源受限场景下的模型对齐提供了新范式。**

</details>

---

### 8. [Contrastive Distribution Matching for Amortized Sequential Monte Carlo in Discrete Diffusion](https://arxiv.org/abs/2605.23346)

**Authors**: Jaihoon Kim, Taehoon Yoon, Prin Phunyaphibarn, Seungjun Kim, Morteza Mardani, Minhyuk Sung  
**Category**: cs.LG  
**Published**: 2026-05-25  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2605.23346v1  

#### Abstract
Discrete diffusion models have emerged as powerful frameworks for generating structured categorical data. However, efficiently sampling from reward-tilted distributions remains a fundamental challenge. While Twisted Sequential Monte Carlo (SMC) offers asymptotic exactness for this task, estimating t...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：Contrastive Distribution Matching for Amortized Sequential Monte Carlo in Discrete Diffusion**

---

## 1. **论文的主要贡献和创新点**

### **解决的问题**
离散扩散模型（Discrete Diffusion Models）在生成结构化类别数据（如文本、DNA序列、蛋白质）方面表现出色，但在**奖励对齐（reward alignment）任务**中面临推理效率瓶颈。具体而言：
- **Twisted Sequential Monte Carlo (SMC)** 是一种渐近无偏的采样方法，可用于从奖励倾斜的目标分布中精确采样。
- 然而，在离散空间中，最优的“扭曲函数”（twist function）无法像连续空间那样通过 Tweedie’s formula 高效估计，必须依赖**蒙特卡洛（Monte Carlo, MC）采样**来逼近，导致每次推理时计算开销巨大，尤其当奖励函数本身昂贵（如蛋白质折叠预测）时。

### **提出的新方法：Contrastive Distribution Matching (CDM)**
作者提出 **CDM**，一种用于**摊销（amortize）SMC 推理成本**的新框架，其核心思想是：
- **将学习扭曲函数建模为一个对比学习目标**，通过正样本（来自目标分布）和负样本（来自当前模型分布）进行训练。
- 最小化当前模型分布与目标分布之间的前向 KL 散度，从而实现分布匹配。

### **相比现有方法的优势**
| 方面 | 现有方法（如 Soft Value） | CDM |
|------|------------------------|-----|
| **训练目标** | 回归目标（MSE），直接拟合扭曲函数值 | 对比学习目标，匹配分布 |
| **训练样本来源** | 来自基础模型（reward-agnostic），存在训练-测试分布不匹配 | 正样本来自目标分布，缓解分布偏移 |
| **训练效率** | 每个正样本只能用于一次梯度更新 | 利用扩散前向过程（forward kernel）复用单个干净样本生成多个中间状态样本，显著提升样本效率 |
| **推理开销** | 学习独立网络，推理时需额外前向传播 | 轻量级标量头（scalar head）附加于主干网络，推理开销 < 5% |
| **兼容性** | 通常独立使用 | 可与任何 proposal（包括已微调模型如 d1, DRAKES）结合，实现协同增益 |

---

## 2. **核心实验方法和设置**

### **使用的数据集与任务**
CDM 在四个不同领域的离散扩散任务上进行了验证：
1. **Toxic Text Generation**  
   - 数据集：OpenWebText  
   - 奖励：预训练毒性分类器的毒性得分（主奖励）及多语言分类器得分（heldout 奖励）
2. **Regulatory DNA Sequence Design**  
   - 数据集：Enhancer activity dataset (~700k DNA 序列)  
   - 奖励：Enformer 模型预测的增强子活性（主奖励）及验证集上独立训练的 Enformer 模型得分（heldout 奖励）
3. **Protein Designability**  
   - 模型：DPLM-2（联合生成氨基酸序列与结构）  
   - 奖励：self-consistency RMSD（scRMSD，主奖励）与 TM-score（scTM，heldout 奖励），需调用 ESMFold 进行结构预测，计算昂贵
4. **Diffusion LLM (dLLM) Alignment**  
   - 模型：LLaDA-8B-Instruct  
   - 奖励：Skywork Llama-3.1-8B 的偏好分数（API 调用，非可导）为主奖励，ArmoRM 为 heldout 奖励

### **实验设置与评估指标**
- **评估方式**：在固定墙钟时间（wall-clock time）下比较各方法的**奖励得分（reward ↑）** 和 **heldout 奖励得分**。
- **多样性指标**（用于分析模式崩溃）：
  - 文本生成：Self-BLEU（n=4）、PPL（GPT2-XL）
  - 蛋白质生成：FoldSeek 聚类数（Clusters）、平均成对 TM-score（inner-TM）
- **训练公平性**：所有需要训练的方法（CDM、Soft Value）使用相同的训练时间、超参数和扭曲头架构。

### **基线方法对比**
- **Base**：基础扩散模型
- **Best-of-N (BoN)**：生成 N 个样本选择最高奖励者
- **SMC**：使用 MC 估计扭曲函数（M=1,4）
- **SMC+Grad**：基于梯度的提案优化（仅适用于可导奖励）
- **Soft Value**：回归式学习扭曲函数
- **Fine-tuned Proposals**：d1、DRAKES（作为 proposal 分布与 CDM 结合）

---

## 3. **主要实验结果和性能指标**

### **关键性能数据与对比结果**
#### **总体性能（图 2）**
- 在所有四项任务中，**CDM 在相同墙钟时间内始终优于所有基线**，建立了新的帕累托前沿（Pareto front）。
- **SMC** 性能随 M 增加而提升，但计算成本线性增长，尤其在蛋白质和 dLLM 任务中因奖励昂贵而严重受限。
- **Soft Value** 表现优于 SMC（M=4），但 CDM 仍显著超越。

#### **与微调方法的协同效果（图 3a）**
- 当 CDM 与微调后的 proposal（如 d1、DRAKES）结合时，性能进一步提升，证明其**正交且兼容性强**。
- 例如，在蛋白质生成任务中，“d1 + CDM” 显著优于 “d1 + SMC” 或 “d1 + Soft Value”。

#### **多样性分析（图 3b）**
- 微调方法（d1, DRAKES）普遍存在**模式崩溃**（mode collapse）现象：
  - 文本生成：高 Self-BLEU（重复性高）、高 PPL（质量差）
  - 蛋白质生成：聚类数少、inner-TM 低
- **CDM 与基础 proposal 结合即可维持高多样性**，同时达到相近奖励水平，有效避免模式崩溃。

#### **训练动态对比（图 4）**
- **CDM 训练收敛更快**，在相同训练时间下达到更高奖励。
- 即使 Soft Value 使用更多 MC 样本（M=32），其收敛速度仍慢于 CDM。
- 归因于对比学习中负样本的校准作用，提升了训练稳定性与效率。

### **消融实验结果**
| 实验项 | 发现 |
|-------|------|
| **正样本缓冲区更新频率 `nupdate`**（图 7） | 不同 `nupdate` 下性能稳定，表明缓冲机制鲁棒；增大 `nupdate` 可减少昂贵奖励评估次数，提升训练效率 |
| **训练时 MC 样本数 M**（表 3a） | Soft Value 性能随 M 增加而饱和；CDM 对 M 不敏感，表现稳定 |
| **正样本采样方式**（IS vs SMC）（表 3b） | 使用 SMC 采样正样本优于 IS，因其 resampling 机制缓解了权重退化问题 |

---

## 4. **关键结论和发现**

### **主要发现**
1. **CDM 成功摊销了 SMC 中扭曲函数的推理成本**，将原本依赖 MC 采样的高开销操作转化为一个轻量级神经网络的常数时间前向传播。
2. **对比学习目标比回归目标更高效且鲁棒**，通过正负样本对比实现了更好的分布匹配，缓解了训练-测试分布偏移。
3. **利用扩散模型的闭式前向核（closed-form forward kernel）可极大提升训练效率**，实现单个干净样本在多个时间步上的复用。
4. **CDM 是通用且兼容的框架**，不仅自身性能优越，还能与 proposal 微调方法（如 d1, DRAKES）结合，实现协同增益。
5. **CDM 有助于缓解模式崩溃**，在保持高奖励的同时维持生成多样性。

### **方法的局限性**
- **对复杂奖励建模能力有限**：当前扭曲头架构（MLP/Transformer）可能不足以捕捉极端稀疏或复杂的奖励信号。
- **仍依赖于训练阶段的 SMC 采样**：虽然推理高效，但训练时仍需运行 SMC 获取正样本，若奖励极其昂贵，训练成本仍高。
- **未原生支持二元或类别型奖励**：目前假设奖励为标量，未来可扩展至更丰富的奖励结构。

### **未来工作方向**
- 设计更强大的扭曲函数架构以应对复杂奖励。
- 探索在极稀疏奖励信号下的学习策略。
- 扩展框架以原生支持二元或类别型奖励结构。
- 将 CDM 思想应用于其他基于 SMC 的生成任务或强化学习场景。

--- 

> **项目主页**: [https://cdm-smc.github.io/](https://cdm-smc.github.io/)

</details>

---

### 9. [Convex Low-resource Accent-Robust Language Detection in Speech Recognition](https://arxiv.org/abs/2605.23235)

**Authors**: Miria Feng, William Tan, Mert Pilanci  
**Category**: cs.LG  
**Published**: 2026-05-25  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.23235v1  

#### Abstract
Globalization and multiculturalism continue to produce increasingly diverse speech varieties. Yet current spoken dialogue systems frequently fail on under-represented dialects and accents, often misidentifying the input language and causing cascading failures in downstream dialogue tasks. Addressing...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文核心结论与实验结果总结**

**论文标题**: *Convex Low-resource Accent-Robust Language Detection in Speech Recognition*

---

## **1. 主要贡献和创新点**

### **解决的问题**
当前的语音识别系统（ASR）在处理低资源语言和带有非主流口音（如新加坡英语 Singlish、马来西亚英语等）的语音时表现不佳，常错误识别输入语言，导致下游对话任务出现级联错误。这一问题源于现有语音数据集中对区域方言和口音标注不足，造成模型对多样化语音变体的鲁棒性差。

### **提出的新方法**
作者提出了 **Convex Language Detection (CLD)** 框架，一种基于凸优化的新型语言检测方法，用于提升 ASR 在低资源、多口音环境下的语言识别准确性。

#### **核心创新点**：
- **凸优化重构**：将传统的两层 ReLU 神经网络重新表述为一个等效的凸优化问题（cvxNN），从而保证训练过程中的全局最优解，避免传统深度学习中依赖超参数调优和陷入局部最优的问题。
- **理论可证明的鲁棒性**：通过推导出检测头的 **variation norm** 和 **logit-Lipschitz 常数**，提供了对隐藏特征扰动下分类边距稳定性的**可验证证书（certified robustness）**。
- **高效实现**：使用 JAX 实现多 GPU 并行化的 ADMM（Alternating Direction Method of Multipliers）算法求解凸程序，实现了快速训练和推理，在多项式时间内收敛。

### **相比现有方法的优势**
| 维度 | CLD 方法优势 |
|------|--------------|
| **样本效率** | 在极低资源场景（每类仅 100 个样本）下仍保持高准确率（>97%） |
| **训练效率** | 训练时间仅为传统神经网络（vanilla-NN）的 7.7%，计算量减少 13 倍（TFLOPs） |
| **稳定性** | 不依赖学习率等敏感超参数，训练过程更可靠 |
| **鲁棒性** | 对口音变异具有更强的泛化能力，显著降低误判为邻近语言（如将 Singlish 判为 Bahasa 或 Tamil）的风险 |

---

## **2. 核心实验方法和设置**

### **使用的数据集**
- **Common Voice v23**：作为主要多语言语音转录数据源。
- **National Speech Corpus (NCS)**：首个新加坡英语语料库，用于研究 Singlish。
- **LAHAJA 数据集**：包含来自印度 83 个地区的 12.5 小时多口音印地语语音。
- **音频增强**：采用 time stretching、pitch shift、背景噪声（MUSAN）等方式进行数据增强。

### **实验设置**
#### **任务类型**
- **Binary Classification**：英文 vs 中文，涵盖 5 种子方言，测试不同训练样本规模（100~10,000）的影响。
- **Multiclass Classification**：5 类语言（English, Chinese, Indonesian, Malaysian, Hindi），共 24 种口音，总训练样本约 16,000，按 80-10-10 分割。

#### **评估指标**
- **Detection Accuracy**：语言识别准确率
- **Word Error Rate (WER)** 和 **Character Error Rate (CER)**：衡量最终转录质量
- **Training Time (秒)** 和 **TFLOPs**：评估计算效率
- **消融实验**：分析不同训练样本量下的性能变化

### **基线方法对比**
| 基线模型 | 描述 |
|--------|------|
| **Whisper 默认检测器** | Whisper 内置的语言识别模块 |
| **Fine-tuned Whisper (WSP-SFT)** | 微调 Whisper 的语言检测头 |
| **Vanilla Neural Network (NN)** | 轻量级前馈网络（线性层 + ReLU + Dropout） |
| **Linear SVM / Kernel SVM** | 支持向量机分类器 |
| **k-Nearest Neighbors (KNN)** | 基于距离的最近邻分类 |

所有基线均使用相同的编码器嵌入（encoder embeddings）作为输入。

---

## **3. 主要实验结果和性能指标**

### **关键性能数据**

#### ✅ **低资源二分类任务（English vs Chinese）**
- **CLD 在仅 100 样本/语言时达到 97.42% 准确率**（见 Table D.1）
- 即使在 10,000 样本时，CLD 依然保持最高准确率（96.94%），而传统 NN 表现出严重偏差（如将 88.88% 的中文样本误判为英文）

#### ✅ **多语言多口音分类任务（5 languages, 24 accents）**
| 模型 | Detection Accuracy | WER ↓ | CER ↓ | Training Time (s) | TFLOPs |
|------|--------------------|-------|-------|------------------|--------|
| **CLD (ours)** | **0.9715–0.9806** | **31.74–28.60** | **17.84–15.37** | **64.45** | **14,075** |
| WSP-SFT | 0.7154–0.8033 | 139.37–40.41 | 73.85–21.80 | 1,096.74 | 239,528 |
| Vanilla-NN | 0.7737–0.9605 | 53.84–29.25 | 34.52–15.99 | 840.30 | 183,521 |

> 🔹 CLD 在 MMS-1B 上相较默认检测器提升 **44.78% 准确率**，WER 下降 **12.74%**  
> 🔹 相较 vanilla-NN，训练时间缩短 **92.3%**，计算成本降低 **13 倍**

#### ✅ **特定挑战性口音表现（Min Dong Chinese）**
| 模型 | 准确率（500 样本） |
|------|------------------|
| WSP (baseline) | 9.86% |
| WSP-SFT | 21.13% |
| Vanilla-NN | 25.35% |
| **CLD (ours)** | **88.73%** |

> CLD 在最难识别的闽东语上实现 **3.5 倍以上性能提升**

#### ✅ **混淆矩阵分析（Figure 3）**
- Vanilla-NN 存在明显“英语中心偏见”（English-centric bias），频繁将中文（zh）误判为印尼语（id）
- CLD 展现出强对角主导性，各语言识别均衡，最低准确率仍达 95%

---

## **4. 关键结论和发现**

### **主要发现**
1. **CLD 显著提升了低资源、多方言语音的语言识别鲁棒性**，尤其在样本稀缺（<100）时表现远超现有方法。
2. **凸优化框架有效缓解了传统神经网络对超参数的依赖**，实现稳定、高效的训练。
3. **CLD 可无缝集成到主流 ASR 架构（如 Whisper、MMS）中**，作为即插即用模块，带来高达 29.21% 的性能增益。
4. **人类案例研究表明**，CLD 能有效防止跨语言错误转录（如将英语转成 Bahasa），提升用户体验。

### **方法的局限性**
- 当前 CLD 作为一个独立检测头运行，未与 ASR 编码器联合优化（end-to-end）。
- 虽然支持多语言，但扩展至千种语言的大规模 MMS 场景尚未验证。
- 对极端噪声或非母语者严重语法错误的鲁棒性有待进一步测试。

### **未来工作方向**
- **端到端可微分 CLD**：通过隐式微分（implicit differentiation）或展开 ADMM 迭代，使整个 pipeline 可微，实现编码器与检测头协同优化。
- **应用于多模态智能体模型**：探索 CLD 在 multimodal agentic models 中的作用。
- **更大规模部署**：在云 TPU 和更大 encoder（如 Whisper-large-v3）上验证其扩展潜力。

---

> 📦 **开源信息**：作者已发布 `jaxcld` 包（[PyPI](https://pypi.org/project/jaxcld/)）和 GitHub 代码，便于复现与社区应用。

> 💬 **社会影响声明**：该工作旨在推动语音技术的包容性和公平性，让更多非标准口音用户平等访问语音交互系统，促进全球多样语言群体的技术普惠。

</details>

---

### 10. [The Efficiency Frontier: A Unified Framework for Cost-Performance Optimization in LLM Context Management](https://arxiv.org/abs/2605.23071)

**Authors**: Binqi Shen, Lier Jin, Hanyu Cai, Lan Hu, Yuting Xin  
**Category**: cs.CL  
**Published**: 2026-05-25  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.23071v1  

#### Abstract
Large language models (LLMs) increasingly rely on long-context processing, but expanding context windows introduces substantial computational and financial costs. Existing context reduction approaches, including retrieval and memory compression methods, are typically evaluated using performance and ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：The Efficiency Frontier: A Unified Framework for Cost-Performance Optimization in LLM Context Management

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
当前在大型语言模型（LLM）中，**长上下文处理**虽然提升了任务能力（如多跳推理），但也带来了显著的计算和财务成本。现有的上下文管理策略（如检索、压缩、全上下文提示）通常被**孤立地评估**，仅分别报告性能（如 F1）和效率（如 token 使用量），缺乏统一框架来系统比较不同方法在真实部署条件下的权衡。

这导致：
- 难以判断何时应选择某种策略；
- 忽略了预处理成本的摊销效应（amortization）；
- 缺乏面向实际部署的决策支持。

### 🚀 提出的新方法与创新思路
本文提出 **“效率前沿”（Efficiency Frontier）** ——一个统一的、部署感知的（deployment-aware）评估与优化框架，用于 LLM 上下文管理中的 **cost-performance trade-off** 分析。

#### 核心创新点包括：

1. **三阶段评估框架**：
   - **Stage 1**: 策略内优化（Intra-Strategy Optimization）
   - **Stage 2**: 候选评分与评估（Candidate Scoring）
   - **Stage 3**: 全局最优决策（Global Decision Optimization）

2. **引入摊销成本建模（Amortized Cost Modeling）**  
   定义有效 token 成本为：
   $$
   \text{EffectiveTokens} = T_{\text{stage2}} + \frac{T_{\text{stage1}}}{N}
   $$
   其中 $N$ 是预处理结果可复用的查询次数，体现了现实场景中缓存、共享内存等机制的影响。

3. **参数化效用函数（Parameterized Utility Function）**：
   $$
   \text{EfficiencyScore}(w) = w \cdot \text{F1} - (1 - w) \cdot \log(\text{EffectiveTokens})
   $$
   权衡性能与成本，$w \in [0,1]$ 控制偏好（高 $w$ 偏向准确率，低 $w$ 偏向低成本）。

4. **构建全局效率前沿曲线**  
   扫描 $w$ 可得到一系列最优策略切换点，形成“效率前沿”，揭示不同操作区域下最优策略的选择路径。

### 🔍 相比现有方法的优势
| 维度 | 传统方法 | 本论文（Efficiency Frontier） |
|------|----------|-------------------------------|
| 评估方式 | 孤立报告性能/成本 | 联合建模性能与摊销成本 |
| 决策支持 | 无明确推荐 | 明确给出策略切换边界 |
| 部署相关性 | 忽视复用模式 | 引入 $N$ 参数反映真实系统特性 |
| 可扩展性 | 无法跨策略比较 | 支持异构策略统一比较 |

> 💡 **优势总结**：从“静态打分”转向“动态决策”，使上下文管理策略选择成为可量化、可预测、可部署指导的过程。

---

## 2. 核心实验方法和设置

### 📊 数据集
- **HotpotQA**：一个多跳问答数据集，包含多个文档和干扰项，适合测试上下文选择与压缩能力。
- 实验采样 **5,000 个实例**，固定随机种子（42），确保可复现性。

### ⚙️ 实验设置
- **模型**：使用 **GPT-5.4 mini** 进行推理，平衡推理能力和计算开销。
- **标准化 prompt 和确定性配置**：控制变量，隔离上下文管理策略的影响。
- **评估单位**：以 **每问题平均有效 token 数（Effective Tokens）** 衡量成本。
- **关键参数**：改变复用次数 $N = 1, 20, 100$，模拟不同部署场景。

### 🧪 评估指标
- 主要性能指标：**F1 Score**
- 主要成本指标：**EffectiveTokens**（经摊销后的 token 成本）
- 综合指标：**EfficiencyScore(w)**，用于生成效率前沿

### 🔄 对比的基线方法
涵盖多种典型上下文管理策略：

| 类型 | 方法 |
|------|------|
| **Full-Context Baseline** | Full-Context Prompting（拼接全部上下文） |
| **Oracle Upper Bound** | Oracle Retrieval（仅保留真实支撑文档） |
| **Memory Compression** | LLM-based 压缩（如 2x, 2.5x 压缩率） |
| **Zero-Cost Retrieval** | - TF-IDF（vanilla / query-aware）<br>- Semantic Embedding Retrieval（基于语义相似度检索 top-k） |

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据与对比结果

#### （1）效率前沿分析（Fig. 1 & Fig. 2）
- 不同策略在 $(F1, \text{EffectiveTokens})$ 平面上形成各自的帕累托前沿（Pareto Frontier）。
- 当 $w$ 变化时，最优配置沿前沿连续移动，表明没有单一“最佳”配置适用于所有场景。

#### （2）全局效率前沿随 $N$ 的演化
| 复用程度 $N$ | 最优策略趋势 |
|--------------|-------------|
| $N=1$（无复用） | 轻量级检索（如 TF-IDF QA）占优 |
| $N=100$（高频复用） | Memory Compression 占据更大前沿区域 |

> ✅ **发现**：随着 $N$ 增加，memory compression 因摊销效应变得更具竞争力。

#### （3）关键性能提升（Table I）

| 场景 | 结果 |
|------|------|
| **Balanced Regime (F1 ≈ 0.78)** | - $N=1$: TF-IDF QA → 566 EffectiveTokens<br>- $N=100$: Memory Compression → **424 EffectiveTokens**<br>➡️ **成本降低约 25%** |
| **Near-High Performance (F1 ≈ 0.80)** | - $N=1$: Full-Context → 1308 Tokens<br>- $N=100$: Memory Compression → **584 Tokens**<br>➡️ **成本降低超过 50%** |
| **High-Performance Regime (F1 ≥ 0.82)** | Full-Context 仍是唯一可达方案，但成本 >2× 平衡区配置，体现**收益递减** |

#### （4）消融实验与关键观察
- **Query-aware retrieval vs. Vanilla TF-IDF**：前者显著提升性能而不增加预处理成本，推动帕累托前沿上移。
- **Memory Compression 的门槛效应**：只有当 $N$ 足够大时才优于轻量检索，说明其适用性高度依赖部署模式。
- **Full-Context 的代价高昂**：尽管接近最高 F1，但 token 成本呈非线性增长，存在明显边际效益下降。

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **性能与成本关系是非线性的**  
   提升 F1 从 ~0.78 到 ~0.84 所需 token 成本翻倍以上，验证了“diminishing returns”。

2. **不存在通用最优策略**  
   - **低复用场景（$N=1$）**：轻量检索（如 TF-IDF QA）最优；
   - **高复用场景（$N=100$）**：memory compression 凭借摊销优势胜出；
   - **极致性能需求**：full-context prompting 仍不可替代。

3. **摊销是决定性因素**  
   预处理成本是否值得投入，取决于能否被多次复用。这一洞察对持久化 agent、企业知识库等系统尤为重要。

4. **效率前沿提供实用决策工具**  
   - 支持两种使用模式：
     - 连续扫描 $w$ 获取 trade-off 曲线；
     - 查表式决策（target F1 → 推荐 strategy）。

5. **系统级优化潜力巨大**  
   通过合理策略选择而非单纯扩大上下文，可在保持性能的同时实现 **25%-50% 的 token 成本节约**。

### ⚠️ 方法的局限性

| 局限 | 说明 |
|------|------|
| 任务范围有限 | 当前实验集中在 HotpotQA（多跳 QA），尚未推广至代码生成、对话系统等其他长上下文任务 |
| 成本模型简化 | 仅考虑 token 成本，未纳入延迟、能耗、硬件占用等维度 |
| 效用函数假设固定 | $w$ 为人工设定，未学习真实用户偏好或任务特定权重 |
| 模型选择限制 | 使用 GPT-5.4 mini，可能不完全代表更大模型的行为 |

### 🔮 未来工作方向

1. **拓展任务类型**  
   将框架应用于 agent memory systems、code generation、document reasoning 等更广泛场景。

2. **丰富优化目标**  
   在目标函数中加入 latency、energy consumption、monetary cost 等多维指标，构建多目标效率前沿。

3. **自适应偏好建模**  
   开发 learned preference model 替代固定 $w$，更好捕捉应用特异性需求。

4. **结合领域知识优化压缩**  
   引入 domain-aware representation learning，提升 memory compression 的保真度与效率。

5. **端到端集成至部署 pipeline**  
   将该框架嵌入 LLM serving system，实现实时策略调度与资源分配。

---

## 总结

> **The Efficiency Frontier 框架将 LLM 上下文管理从“容量竞赛”转变为“利用率优化”的科学决策过程。它不仅提供了统一的评估标准，更重要的是揭示了“何时、何地、用何种策略最高效”的实践指南，为构建可持续、经济、高效的 LLM 系统奠定了理论与工程基础。**

--- 

📌 **关键词回顾**：Efficiency Frontier, Cost-Performance Trade-off, Amortized Cost, Deployment-Aware Optimization, Context Management, Token Efficiency, Memory Compression, Retrieval-Augmented Generation (RAG)

</details>

---

### 11. [Enhancing Energy Efficiency in Scientific Workflows through CFD based PIVAEs](https://arxiv.org/abs/2605.23850)

**Authors**: Ali Zahir, Ashiq Anjum, Mark Wilkinson, Jeyan Thiyagalingam  
**Category**: cs.DC  
**Published**: 2026-05-25  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.23850v1  

#### Abstract
The growing complexity and scale of scientific workflows in high performance computing (HPC) environments have led to significant challenges in managing energy consumption without compromising computational performance. Traditional scheduling strategies often fail to account for the complex interpla...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Enhancing Energy Efficiency in Scientific Workflows through CFD based PIVAEs

---

## 1. 论文的主要贡献和创新点

### 解决的问题
该论文针对**高能效科学计算工作流调度中的三大挑战**：
1. **热反馈缺失**：传统调度策略忽略热力学动态（如散热、气流、冷却效率），导致能耗模型脱离物理现实。
2. **合成数据缺乏物理真实性**：现有的生成模型（如VAE、GAN）生成的工作负载数据常违反热力学约束，导致调度策略在实际部署中不可行。
3. **硬件特异性过强**：许多方法仅适用于特定架构（如Hadoop、GPU集群），难以推广到异构HPC环境。

这些问题导致理论调度模型与实际HPC部署之间存在严重脱节，限制了能效优化的实际效果。

---

### 提出的新方法与新思路
提出了一种**基于CFD的Physics-Informed Variational Autoencoder（PIVAE）框架**，用于AI驱动的能效感知任务调度：

- **CFD + PIVAE 耦合建模**：
  - 利用**Computational Fluid Dynamics (CFD)** 模拟HPC系统内部的温度分布、热传导和冷却行为，提供细粒度的热力学反馈。
  - 将CFD输出作为**物理约束嵌入VAE的损失函数中**（即`L_CFD`项），确保生成的合成工作负载数据在热力学上是可行的。

- **物理引导的合成数据生成**：
  - 通过PIVAE生成大量“物理真实”的合成调度配置，扩展训练空间，避免昂贵的真实实验探索。
  - 支持对不同CPU频率调整（5%–20%降频）下的能效权衡进行预测。

- **多调度器联合评估机制**：
  - 在统一框架下评估多种调度策略（FCFS, LAS, LASP, SAS, LYNX, OM-FNN），识别最优操作点（sweet spot）。

---

### 相比现有方法的优势
| 维度 | 传统方法 | 本文方法 |
|------|----------|---------|
| **物理一致性** | 忽略热力学反馈 | 显式建模CFD热行为，保证调度决策的物理可行性 |
| **数据质量** | 统计生成，易违反物理规律 | 物理约束生成，提升泛化性和部署可靠性 |
| **可扩展性** | 多依赖启发式规则或静态模型 | 基于学习的动态建模，支持跨架构适应 |
| **能效-性能平衡** | 单目标优化为主 | 多目标联合优化（TAT vs. Energy） |

> ✅ **核心优势**：首次将**物理建模（CFD）与深度生成模型（VAE）深度融合**，实现“数据驱动 + 物理可信”的智能调度。

---

## 2. 核心实验方法和设置

### 数据集与工作流
使用来自**DiRAC Data Intensive服务（DIaL）** 的真实科学工作流执行轨迹，共5类代表性HPC工作流（WF-1至WF-5）：

| Workflow | 描述 | 资源利用率 |
|--------|------|-----------|
| WF-1: Event Reconstruction | 事件重建 | Mid/Low |
| WF-2: Particle Trajectory Identification | 粒子轨迹识别 | Mid |
| WF-3: Collision Point Detection | 碰撞点检测 | Mid |
| WF-4: Pattern Recognition | 模式识别 | High |
| WF-5: Anomaly Detection | 异常检测 | High |

- 每个工作流实例包含500–900个任务（见Table 2）
- 总共采集超过 **4000条真实执行轨迹** 用于训练PIVAE

---

### 实验设置
- **硬件平台**：
  - 双路Intel Xeon Platinum 8280（56核/112线程）
  - 1.5TB DDR4 ECC RAM，10TB NVMe SSD
  - Proxmox虚拟化管理，Slurm作业调度
  - 功耗监测：Intel RAPL + IPMI/BMC（采样率100ms）
  - 温度监控：LM-Sensors + BMC传感器

- **调度策略对比**：
  - FCFS（基准）
  - Locality-Aware Scheduling (LAS)
  - LAS with Prefetching (LASP)
  - Speculative-Aware Scheduling (SAS)
  - LYNX（预测预取增强型LAS）
  - OM-FNN（基于前馈神经网络的学习型调度）

- **变量控制**：
  - CPU频率调节：正常运行 vs. 降低5%、10%、15%、20%
  - 所有实验在相同资源条件下重复5次，取均值（偏差 < 3%）

---

### 评估指标
| 指标 | 定义 |
|------|------|
| **Turnaround Time (TAT)** | 从任务提交到全部完成的时间（ms） |
| **Energy Consumption** | 总能耗（kWh），由 $ E = \sum(P_{CPU} \cdot t_{exec}) $ 计算 |
| **Power Consumption** | 平均功耗（W） |
| **Thermal Signature** | CPU核心与内存DIMM温度变化（℃） |
| **Uncertainty Quantification** | Bootstrap重采样估计合成数据与真实数据差异的置信区间 |

---

## 3. 主要实验结果和性能指标

### 关键性能数据（来自Table 4与Figure 9）

#### 在 **15% CPU降频** 下的关键表现：
| 指标 | 平均变化 |
|------|---------|
| **Energy Savings** | 达到 **~10%** |
| **TAT Increase** | 仅增加 **~5–6%** |
| **最优调度器（SAS）** | WF-5下能耗从62.38 kWh降至54.65 kWh（↓12.4%），TAT仅↑5.5% |

> 🔍 **发现**：**15% CPU降频是一个“甜点”（sweet spot）** —— 能耗显著下降，而性能损失极小。

---

### 与基线方法的对比结果

| 方法 | TAT 表现 | Energy 表现 | 综合评价 |
|------|--------|------------|---------|
| **FCFS** | 最慢（最长TAT） | 最低瞬时功耗但总能耗高（因延迟长） | 公平但低效 |
| **LAS/LASP** | 中等加速（↓13–21% TAT） | 能耗上升明显（↑79–91%） | 局部优化代价大 |
| **LYNX** | 加速明显 | 能耗最高之一 | 过度推测导致资源浪费 |
| **OM-FNN** | TAT较低 | 能耗较高 | 学习模型未考虑热约束 |
| **SAS + CFD-PIVAE** | TAT ↓37%（WF-5） | 能耗 ↑60%（仍优于多数） | ✅ **最佳能效比** |

> 📊 图5显示：尽管SAS比FCFS多消耗约60%能量，但其TAT缩短近37%，单位时间能效更高。

---

### 消融实验与验证分析

#### （1）CFD约束有效性验证（Algorithm 2）
- 对生成的合成配置施加**热力学可行性检查**（来自CFD模拟）
- 结果：约 **18% 的VAE生成样本被拒绝**，因其违反温度或功率阈值
- ➤ 验证了物理约束的有效过滤作用

#### （2）不确定性量化（Bootstrap Resampling）
- 使用 **B=10,000次重采样** 估计真实与合成数据的能耗差异
- 结果：
  - 平均差值：**+2.03 kWh**（真实 > 合成）
  - 95% CI: [0.715, 3.354]，p-value = 0.0022 → 差异显著
- ➤ 表明PIVAE倾向于预测更节能的操作状态，且统计可靠

#### （3）热图对比（Figure 7）
- 应用CFD-PIVAE优化后：
  - **平均组件温度下降5–7%**
  - 热点区域减少，温度分布更均匀
- ➤ 验证了方法在**降低系统热负荷方面的附加收益**

---

## 4. 关键结论和发现

### 主要发现
1. **存在明确的“能效甜点”**：
   - 将CPU性能适度降低 **15%** 可实现高达 **10%的能量节省**，同时仅带来 **5–6%的TAT增长**。
   - 此外，20%降频虽节能更多（达12.4%），但TAT增幅趋近临界，性价比下降。

2. **物理引导的生成模型优于纯数据驱动方法**：
   - CFD-PIVAE生成的数据不仅统计合理，而且**热力学上可实现**，提升了调度策略的部署成功率。

3. **Speculative-Aware Scheduling（SAS）最具潜力**：
   - 在CFD-PIVAE指导下，SAS实现了最佳的**能效-性能平衡**，尤其适合大规模科学工作流。

4. **热管理应纳入调度决策闭环**：
   - 忽视热反馈的传统调度可能导致局部过热、可靠性下降；本研究表明**主动热感知调度可行且有效**。

---

### 方法的局限性
1. **当前聚焦于CPU密集型工作流**：
   - 内存与I/O密集型任务的影响尚未充分建模（如带宽瓶颈、缓存效应）。
2. **CFD仿真开销较高**：
   - 虽然只在离线阶段运行一次，但仍需高性能计算资源支持。
3. **泛化能力受限于训练场景**：
   - 当前模型在特定HPC集群上训练，迁移到其他架构需重新校准。

---

### 未来工作方向
1. **扩展至Memory/I/O密集型工作流建模**：
   - 将内存带宽、NVMe访问延迟、网络通信成本纳入PIVAE输入特征。
2. **构建端到端自适应调度系统**：
   - 实现在线实时推理与动态调频（DVFS）、任务迁移联动。
3. **集成更多物理场模型**：
   - 如电磁干扰、振动、电源波动等，打造“全物理数字孪生”调度环境。
4. **跨平台迁移学习研究**：
   - 探索如何将在一个HPC系统上学到的知识迁移到另一个异构系统中。

---

> ✅ **总体评价**：  
> 本文开创性地将**物理建模（CFD）与深度生成模型（PIVAE）结合**，提出了一种**可持续、可扩展、物理可信的AI调度框架**，为下一代绿色HPC系统的智能化运维提供了坚实的技术路径。

</details>

---

### 12. [ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning](https://arxiv.org/abs/2605.23454)

**Authors**: Xiaoyuan Li, Keqin Bao, Moxin Li, Yubo Ma, Yichang Zhang, Wenjie Wang, Fuli Feng, Dayiheng Liu  
**Category**: cs.CL  
**Published**: 2026-05-25  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.23454v1  

#### Abstract
Rubric-based rewards offer a promising way to extend reinforcement learning (RL) for large language models beyond tasks with automatically verifiable answers. However, scaling rubric-based RL remains challenging: existing approaches often rely on expert-written rubrics and manually constructed quest...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning

---

## 1. 论文的主要贡献和创新点

### ✅ 解决了什么问题

现有的 **Reinforcement Learning with Verifiable Rewards (RLVR)** 方法虽然在数学、编程等任务上取得了成功，但其依赖于**可自动验证的答案**（如精确匹配、代码执行结果），这导致以下两个核心限制：

1. **任务范围受限**：仅适用于有明确正确答案的任务，难以扩展到开放性、多维度的复杂任务（如医疗咨询、写作、指令遵循）。
2. **奖励信号稀疏且粗粒度**：通常为二元奖励（正确/错误），缺乏对响应质量的细粒度反馈。

此外，已有基于 rubric 的 RL 方法依赖专家手动编写 rubric 和 QA 对，**难以规模化**，且 rubric 多为任务级通用标准，无法适应每个问题的具体需求。

---

### 🚀 提出的新方法：ARES

作者提出 **ARES (Automated Rubric synthEsis for Scalable RL)** ——一个全自动构建大规模 rubric-annotated RL 数据的框架，核心思想是：

> 从原始预训练文档出发，自动生成“问题-参考答案-问题特定加权 rubric”三元组，实现**实例级别的细粒度奖励监督**。

#### 创新点包括：

- **自动化 rubric 合成**：首次将 rubric 与 QA 对**联合生成**（co-generation），确保 rubric 紧密贴合具体问题和答案内容。
- **问题特定的加权 rubric**：每个问题都有定制化的评价标准，并赋予不同重要性权重（positive/negative weights），支持更精细的 reward shaping。
- **可扩展的数据流水线**：完全基于 LLM 自动化处理，无需人工标注，能从任意预训练语料中提取知识并转化为 RL 训练数据。
- **多样性控制机制**：通过引入 domain label 和 persona（如医生、学生、护理者）来引导生成风格和难度，提升数据多样性。

---

### 🔍 相比现有方法的优势

| 维度 | 现有方法（如 WebScale-RL, RaR） | ARES |
|------|-------------------------------|------|
| 是否支持多领域 | ❌ 多集中于数学/编码 | ✅ 覆盖10个广泛领域 |
| 是否使用 rubric 奖励 | ❌ 多为 binary reward | ✅ 支持多维加权 rubric |
| 是否基于文档生成 | ⚠️ 部分支持 | ✅ 所有 QA 和 rubric 均源自源文档 |
| 是否可扩展 | ❌ 依赖人工构造 | ✅ 全流程自动化，易于扩展 |

> ✅ ARES 是目前唯一同时满足 **Multi-Domain、Rubric Rewards、Doc-Grounded、Scalable** 四大特性的 RL 数据构建方案。

---

## 2. 核心实验方法和设置

### 📚 使用的数据集

- **训练数据来源**：
  - 来自三个公开预训练语料库的小规模子集：
    - **DCLM** [Li et al., 2024]
    - **FineWeb-Edu** [Penedo et al., 2024]
    - **FinePDFs** [Kydliček et al., 2025]
  - 经过滤后约 0.1B tokens，最终生成 **101,847 个 rubric-annotated QA 实例**

- **领域分布**（共10类）：
  | Domain | 数量 |
  |---|---|
  | Social Science | 18,878 |
  | Technology & Engineering | 18,321 |
  | Medicine & Health | 13,974 |
  | Travel & Lifestyle | 12,767 |
  | Commerce & Economics | 12,439 |
  | Natural Science | 10,154 |
  | Education | 8,822 |
  | Others | 3,931 |
  | Coding | 1,631 |
  | Math | 930 |

- **平均 rubric 统计**：
  - 每个实例平均含 **10.88 条 criteria**
  - 正向 criteria 占多数（~74%），负向用于惩罚常见错误（如幻觉、遗漏关键信息）

---

### 🧪 实验设置与评估指标

#### 基础模型
- **Qwen3-4B-Base** 作为 backbone 模型
- 所有方法均从零开始训练，无额外 instruction tuning

#### RL 训练配置
- 使用 **Group Relative Policy Optimization (GRPO)** 进行优化
- 每轮采样 G=8 个候选响应
- Batch size: 128，Epochs: 3
- Reward judge 模型：**Qwen3-32B**

#### 评估基准（7个）
| Benchmark | 类型 | 描述 |
|---------|------|------|
| **MMLU-Pro** | 知识推理 | 多任务语言理解，选择题形式 |
| **GSM8K** | 数学推理 | 小学数学应用题 |
| **HumanEval+ / MBPP+** | 编程能力 | 代码生成任务 |
| **HealthBench** | 医疗问答 | 开放式健康咨询，强调事实性和安全性 |
| **WritingBench** | 写作质量 | 评估连贯性、相关性、风格等 |
| **IFEval** | 指令遵循 | 测试是否满足格式、关键词、长度等多种约束 |

> ✅ 最终得分取 **7个 benchmark 的未加权平均分**，反映整体能力。

---

### 🆚 基线方法对比

| 方法 | 类型 | 说明 |
|-----|------|------|
| **CPT** (Continual Pretraining) | LM Objective | 在相同文档上继续预训练（next-token prediction） |
| **NaturalReasoning** | SFT | 在 NaturalReasoning 数据集上微调，强 SFT 基线 |
| **Webscale** | Binary-Reward RL | 使用 binary reward 的 GRPO，类似 WebScale-RL |
| **ARES-SFT** | SFT | 在 ARES 生成的 QA 上进行监督微调 |
| **ARES-RL** (Ours) | Rubric-based RL | 使用 ARES 生成的 rubric 进行 GRPO 训练 |

---

## 3. 主要实验结果和性能指标

### 📊 主要性能结果（Table 4）

| Method | MMLU-Pro | GSM8K | HumanEval+ | MBPP+ | HealthBench | WritingBench | IFEval | **Avg** |
|--------|----------|-------|------------|--------|-------------|--------------|--------|--------|
| CPT | 46.02 | 82.34 | 32.32 | 59.40 | 35.04 | 36.98 | 39.39 | 47.36 |
| NaturalReasoning | 47.96 | 81.50 | 32.93 | 61.15 | 32.94 | 36.77 | 28.15 | 45.91 |
| Webscale | 49.50 | 84.91 | 33.54 | 61.40 | 36.08 | 37.09 | 35.61 | 48.30 |
| ARES-SFT | 50.56 | 85.67 | 31.10 | 61.40 | 35.78 | 37.05 | 46.41 | 49.71 |
| **ARES-RL (ours)** | **49.36** | **86.96** | **34.76** | **63.16** | **41.45** | **38.24** | **54.88** | **52.69** |

> ✅ **ARES-RL 平均得分达 52.69，显著优于所有基线**：
- 超越 CPT：+5.33
- 超越 SFT 基线：+6.78
- 超越 binary-reward RL：+4.39
- 超越同数据下的 SFT（ARES-SFT）：+2.98 → 表明 **rubric-based RL 优于单纯模仿学习**

---

### 🔍 关键发现

- **在多维开放任务上提升最大**：
  - **HealthBench**: +5.37 vs Webscale
  - **IFEval**: +19.27 vs Webscale → 显示 rubric 对复杂约束建模的强大优势
  - **WritingBench**: +1.15 vs Webscale

- **即使在 verifiable 任务上也表现优异**：
  - **GSM8K**: 86.96（SOTA）
  - **HumanEval+**: 34.76
  - **MBPP+**: 63.16
  > 尽管 Math 和 Coding 数据仅占 ~2%，仍取得最佳成绩，表明跨域迁移有效。

- **MMLU-Pro 略低于 ARES-SFT**（49.36 vs 50.56）：
  - 可能因该 benchmark 为选择题，SFT 更直接有效；而 rubric-based RL 更适合开放生成任务。

---

### 🔬 消融实验（Ablation Study）

比较四种 reward 设计策略（使用相同数据和 GRPO 设置）：

| Reward Strategy | Avg Score | 关键观察 |
|----------------|-----------|---------|
| **Blind Judge**（LLM 整体打分） | 49.53 | 信号不稳定，一致性差 |
| **General Rubric**（固定通用 criteria） | 51.79 | 比盲评好，但泛化有限 |
| **Reference Answer**（与参考答案相似度） | 46.25 | 在 HealthBench 得分最高（50.13），但在 IFEval 崩溃至 10.54 → 不稳定 |
| **ARES-RL**（问题特定加权 rubric） | **52.69** | ✅ 综合表现最优，尤其在 IFEval 上领先 +9.22 |

> 💡 结论：**问题特定的 rubric 设计提供了更强的跨任务鲁棒性**，避免了单一参考答案或通用标准带来的偏差。

---

## 4. 关键结论和发现

### ✅ 主要结论

1. **rubric-based RL 显著优于传统 RL 和 SFT**：
   - 特别是在需要多维度评估的任务（医疗、写作、指令遵循）上带来巨大增益。
   - 提供了比 binary reward 更密集、更具诊断性的学习信号。

2. **ARES 实现了高质量、多样化的自动化 rubric 构建**：
   - 无需人工干预即可从原始文本生成 QA + rubric，极大降低构建成本。
   - 支持 domain 和 persona 控制，增强数据可控性与实用性。

3. **问题特定 rubric 优于通用 rubric 或参考答案比较**：
   - 定制化标准更能捕捉每个问题的独特要求，提升训练效率和泛化能力。

4. **开放性任务更适合 rubric-based RL 范式**：
   - 当目标不是“唯一正确答案”，而是“满足多个条件”的高质量输出时，rubric 提供了理想的优化路径。

---

### ⚠️ 局限性（Appendix A）

1. **实验规模受限**：
   - 仅在 **Qwen3-4B-Base** 上验证，尚未扩展到更大模型（如 70B）。
   - Rubric judge 使用 Qwen3-32B，受 GPU 内存限制，更大 judge 可能进一步提升 reward 质量。

2. **潜在偏见风险**：
   - 自动生成的 rubric 可能继承源文档或 LLM 本身的偏见。
   - LLM judge 的判断也可能存在不一致或主观性。

3. **依赖 LLM 生成质量**：
   - 若 generator 或 judge 出现系统性错误（如幻觉），会影响整个 pipeline 的可靠性。

---

### 🔮 未来工作方向

1. **扩展至更大模型和更多领域**
2. **引入人类反馈进行 rubric 校准**（human-in-the-loop validation）
3. **动态调整 rubric 复杂度与训练进度的关系**
4. **探索 rubric 自动生成中的公平性与去偏机制**
5. **将 ARES 应用于 real-world 场景**（如教育辅导、临床决策支持）

---

> 📌 总结一句话：  
> **ARES 成功打通了“从原始知识到细粒度强化学习”的自动化通路，使 LLM 能够在开放、复杂、多维度的任务上接受结构化训练，推动 RL 超越 verifiable domains 的边界。**

</details>

---

### 13. [WeCon: An Efficient Weight-Conditioned Neural Solver for Multi-Objective Combinatorial Optimization Problems](https://arxiv.org/abs/2605.22876)

**Authors**: Xuan Wu, Jinbiao Chen, Yang Li, Lijie Wen, Chunguo Wu, Yuanshu Li, Yubin Xiao, Chunyan Miao, You Zhou, Di Wang  
**Category**: cs.LG  
**Published**: 2026-05-25  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.22876v1  

#### Abstract
Existing neural solvers for Multi-Objective Combinatorial Optimization Problems (MOCOPs) commonly adopt decomposition-based strategies that scalarize an MOCOP into multiple subproblems associated with distinct weight vectors. However, they either inject weights only once during decoding, limiting we...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：WeCon: An Efficient Weight-Conditioned Neural Solver for Multi-Objective Combinatorial Optimization Problems

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
现有的 **Neural Combinatorial Optimization (NCO)** 模型在处理 **Multi-Objective Combinatorial Optimization Problems (MOCOPs)** 时存在以下关键缺陷：

- **Weight-conditioned context modeling 不足**：大多数模型仅在 **Decoder** 中注入权重向量（如 PMOCO），或主要在 **Encoder** 中处理（如 WE-CA），导致：
  - 解码阶段权重信号稀释（weight-signal dilution）
  - 权重与实例特征交互不充分，上下文建模能力弱
- **训练效率低**：基于 **Preference Optimization (PO)** 的训练方法依赖随机采样生成解对，常产生质量相近的“弱信息”偏好对，影响训练有效性。

### 提出了什么新方法或新思路
本文提出 **WeCon** —— 一种高效的 **Weight-Conditioned Neural Solver**，其核心创新包括：

#### （1）编码器设计：Gated Residual Fusion (GRF)
- 在每个 Encoder 层中引入三个注意力模块：
  - **MHSA**（Multi-Head Self-Attention）处理实例特征
  - 双向 **MHA** 实现实例与权重特征的交互
  - **GRF 模块** 自适应融合两者，生成更具区分性的 **weight-conditioned context**
- GRF 通过门控机制控制权重信息注入强度，提升上下文表达能力。

#### （2）解码器设计：Residual Fusion (RF) 模块
- 在 Decoder 中引入 **插件式（plug-and-play）RF 模块**
- 在每一步解码中显式注入权重信号，缓解 **weight-signal dilution**
- 理论分析表明 RF 引入了从权重到决策向量 $q$ 的直接梯度路径，避免信号衰减。

#### （3）高效偏好优化策略：Efficient Preference Optimization (EPO)
- 改进传统 PO 的纯随机采样策略
- 采用 **引导采样（guided sampling）**：在每步决策中仅从 top-$k$ 最大概率节点中选择，确保生成高质量候选解
- 构造出质量差距更大的偏好对，显著提升训练信号的信息量和训练效率。

---

### 相比现有方法的优势

| 方面 | WeCon 优势 |
|------|------------|
| **架构设计** | 同时在 Encoder 和 Decoder 中有效利用权重，实现双向、持续的 weight-conditioned 决策 |
| **推理效率** | 相比 SOTA 模型 POCCO-W，**推理时间减少约 40%**（部分任务达 55%），适用于实时场景（如交通信号控制） |
| **训练效率** | EPO 策略生成更高质量的偏好对，提升训练收敛速度与效果 |
| **通用性** | RF 模块可即插即用，已成功集成至其他架构（如 WeCon-CCO） |

---

## 2. 核心实验方法和设置

### 使用的数据集
在四种典型的 MOCOP 变体上进行实验，涵盖不同目标数、规模和分布：

- **Bi-TSP**：双目标旅行商问题（20–1000 节点）
- **Tri-TSP**：三目标旅行商问题（20–100 节点）
- **Bi-CVRP**：双目标带容量车辆路径问题（20–100 客户）
- **Bi-KP**：双目标背包问题（50–1000 物品）
- **真实世界实例**：来自 TSPLIB 的 KroAB100/150/200
- **大规模测试集**：Bi-TSP500/1000, Bi-KP500/1000（本文生成）

### 实验设置和评估指标

#### 评估指标
- **HyperVolume (HV)**：衡量解集的收敛性与多样性，越高越好（归一化至 [0,1]）
- **Gap**：相对于最强基线（WeCon-CCO-Aug）的 HV 差距
- **Runtime**：单个测试集的总推理时间
- 统计检验：Wilcoxon rank-sum test（1% 显著性水平）

#### 超参数设置
- $k=5$, $c=8$（EPO 中 top-$k$ 和采样比例）
- $L=6$ 层编码器，$M=8$ 注意力头
- $\beta=3.5$（双目标）、$\beta=4.5$（三目标）
- 所有模型训练 200 轮，每轮 100,000 实例，batch size=64
- 使用 Adam 优化器（lr=3e-4）

#### 硬件环境
- CPU: Intel Xeon Gold 6348
- GPU: NVIDIA A800 (80GB)

---

### 基线方法对比

#### 传统启发式算法（6种）
- WS-LKH, WS-DP, MOEA/D, NSGA-II, MOGLS, PPLS/D-C

#### 神经求解器（8种）
- 多模型：DRL-MOA, MDRL, EMNH
- 单模型：PMOCO, CNH, WE-CA, PA-MoE-W, **POCCO-W**（当前 SOTA）

> 注：WeCon 与 POCCO-W 同为单模型、支持任意权重输入的统一求解器。

---

## 3. 主要实验结果和性能指标

### 关键性能数据

| 模型 | HV 性能 | 推理时间（相对 POCCO-W） |
|------|--------|--------------------------|
| **WeCon** | 与 POCCO-W **相当**（HV 差距 < 0.1%） | **减少约 40%**（最高达 55%） |
| **WeCon-Aug** | 在多个任务上 **超越 POCCO-W-Aug** | 仍快 38–55% |
| **WeCon-CCO** | **所有任务中 HV 最高**（SOTA） | 比 WeCon 慢约 1.7× |

#### 典型结果示例（Bi-TSP100）：
- WeCon-Aug HV: **0.7077** vs POCCO-W-Aug: 0.7077（持平）
- 推理时间：WeCon-Aug **12分钟** vs POCCO-W-Aug **59分钟**

#### 大规模实例表现（Bi-TSP1000）：
- WeCon HV: **0.7733** > POCCO-W: 0.7037
- 推理时间：WeCon **9.6分钟** vs POCCO-W **12分钟**

#### 真实世界实例（KroAB200）：
- WeCon-Aug HV: **0.7369** > POCCO-W-Aug: 0.7360
- 推理时间：WeCon-Aug **26秒** vs POCCO-W-Aug **50秒**

---

### 与基线方法的对比结果

| 对比维度 | 结果 |
|---------|------|
| **vs 传统启发式** | WeCon 在所有任务上显著优于 NSGA-II、MOEA/D 等 |
| **vs 神经求解器** | WeCon 在 HV 上接近或超过 POCCO-W，且速度快得多 |
| **vs 多模型方法** | 单一模型实现跨权重泛化，无需重复训练 |
| **vs WE-CA / PMOCO** | 显著缓解 weight-signal dilution，决策更敏感于权重变化（见图6） |

---

### 消融实验结果

#### 消融组件（Bi-TSP100）
| 设置 | HV ↓ | 时间 |
|------|------|------|
| 完整 WeCon | **0.7077** | 12m |
| w/o Encoder（替换为 WE-CA 编码器） | 0.7073 | 11m |
| w/o GRF（移除门控融合） | 0.7075 | 12m |
| w/o RF（移除残差融合） | 0.7070 | 9.8m |
| w/ RL（替换为 REINFORCE） | 0.7074 | 12m |
| w/ PO（原始偏好优化） | 0.7075 | 12m |
| w/ BOPO | 0.7058 | 12m |

> ✅ 所有组件均有贡献，**RF 和 EPO 尤为关键**

#### 超参数敏感性（$k$, $c$）
- 在 $k \in \{4,5,6\}$, $c \in \{6,8,10,12\}$ 范围内，HV 波动极小
- 最优配置 $k=5, c=8$ 表现最佳，说明策略鲁棒

#### 分解技术对比（WS vs TCH）
- **Weighted-Sum (WS)** 在所有尺度上均优于 Tchebycheff (TCH)
- 支持选择 WS 作为默认分解方式

---

## 4. 关键结论和发现

### 主要发现

1. ✅ **同时在 Encoder 和 Decoder 中建模权重是有效的**  
   WeCon 首次实现了在两个阶段都深度整合权重信息，显著提升了 weight-conditioned 决策能力。

2. ✅ **RF 模块有效缓解 weight-signal dilution**  
   可视化显示 WeCon 的节点选择随权重平滑变化，而 WE-CA 几乎不变。

3. ✅ **EPO 显著提升训练效率**  
   引导采样生成高质量解对，使训练更聚焦于有意义的比较。

4. ✅ **WeCon 实现 SOTA 性能与高效率的平衡**  
   在保持与 POCCO-W 相当甚至更优 HV 的同时，**推理速度快 40%+**，适合实际部署。

5. ✅ **WeCon-CCO 进一步提升性能上限**  
   结合 MoE 机制后达到最佳 HV，验证了 RF 的通用性和扩展潜力。

---

### 方法的局限性

- **模型参数量较大**：WeCon 参数约 5.4M，高于 POCCO-W（2.0M），尽管推理更快
- **依赖预定义权重向量**：仍需外部提供偏好方向，未实现完全自主偏好学习
- **多目标数量限制**：实验最多验证到 Tri-TSP，更高维目标尚未测试
- **训练跨尺度泛化可能牺牲特定尺度最优性**：统一模型在个别规模上略逊于专用训练模型

---

### 未来工作方向

1. **引入 Curriculum Learning**：逐步训练以增强跨尺度泛化能力
2. **探索无监督/自监督偏好学习**：减少对人工设定权重的依赖
3. **扩展至更多 MOCOP 类型**：如调度、装箱等复杂工业场景
4. **轻量化设计**：进一步压缩模型以适配边缘设备
5. **结合强化学习探索机制**：提升解的多样性与全局搜索能力

---

> 📌 **总结一句话**：  
> **WeCon 是首个在 MOCOP 中同时实现 SOTA 性能与高推理效率的神经求解器，通过 GRF + RF 架构与 EPO 训练策略，解决了 weight-signal dilution 与低效训练两大瓶颈，为实际应用提供了强有力的新工具。**

</details>

---

### 14. [From Residuals to Reasons: LLM-Guided Mechanism Inference from Tabular Data](https://arxiv.org/abs/2605.22897)

**Authors**: Mohammad R. Rezaei, Rahul G. Krishnan  
**Category**: cs.LG  
**Published**: 2026-05-25  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.22897v1  

#### Abstract
A persistent challenge in machine learning for scientific applications is jointly achieving prediction and understanding. Statistical models excel on structured data but operate as black boxes, while existing interpretability methods are largely inspective: they answer "which features matter?" but d...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：From Residuals to Reasons: LLM-Guided Mechanism Inference from Tabular Data

## 1. 论文的主要贡献和创新点

### 解决的问题
该论文旨在解决机器学习在科学应用中长期存在的“预测”与“理解”的权衡难题。传统统计模型（如 XGBoost）在结构化数据上表现优异，但作为“黑箱”模型，其内部决策机制难以解释。现有的可解释性方法（如 SHAP、TreeSHAP）主要回答“哪些特征重要？”，但无法阐明特征间的交互方式，也无法支持人类专家对模型进行迭代式的理解和修正。

### 提出的新方法：MARICL
作者提出了 **Multi-Agent Residual In-Context Learning (MARICL)**，一种基于大语言模型（LLM）的智能体框架，用于从表格数据中推断出可解释的机制。

**核心思想**：
- **从预测残差入手**：不直接让 LLM 预测目标值（这会迫使 LLM 在整个输出空间搜索），而是先用一个已有的基础模型（base model）进行预测，然后让 LLM 分析这个基础模型的**残差**（residuals）。这样，LLM 的任务被缩小为“这个模型哪里错了？”。
- **生成可执行的修正项**：MARICL 框架包含编码器（Encoder）和解码器（Decoder）两个 LLM 智能体。编码器分析高残差样本，生成结构化的假设；解码器将这些假设转化为**命名的、可执行的符号公式**（named, executable correction terms），例如 `NAD × spermidine` 或 `folinic_acid / (0.5 + folinic_acid)`。
- **迭代式优化**：通过 **Textual Gradient Optimization** 技术，让 LLM 对自己的修正项进行自我批评和迭代优化，逐步完善解释。
- **查询感知聚合**：最终的预测是基础模型和多个修正项的加权和，权重由一个查询感知的门控机制决定，确保修正项只在相关情境下生效。

### 相比现有方法的优势
1.  **兼具准确性和可解释性**：MARICL 不仅提升了预测性能，还提供了人类可读、可编辑的符号公式，揭示了模型失败的根本原因。
2.  **超越事后解释**：不同于 SHAP 等事后归因方法，MARICL 生成的是全局性的、可泛化的机制，而非针对单个样本的局部解释。
3.  **优于端到端 LLM 预测**：相比直接使用 LLM 进行上下文学习（LLM-ICL）来预测目标值，MARICL 的性能显著更优（在细胞自由蛋白合成数据集上，R² 从 0.35 提升至 0.65）。
4.  **实现机制泛化**：通过跨批次实验，证明了学习到的修正公式捕捉到了真实的生物化学机制，而不仅仅是批次特定的噪声。

## 2. 核心实验方法和设置

### 使用的数据集
实验涵盖了九个基准数据集，跨越多个领域：
- **科学/生物医学**：Cell-Free Protein Production (细胞自由蛋白合成), Enzyme Activity (酶活性), Diabetes Progression (糖尿病进展)
- **社会/经济**：Zoo, High School Social Classification, Adult Income
- **其他**：California Housing, Bike Sharing
- **合成数据**：一个具有预设真实公式的合成数据集，用于排除 LLM 先验知识的影响。

### 实验设置和评估指标
- **任务**：回归和分类。
- **评估指标**：
  - 回归任务：R² 和 MAE (Mean Absolute Error)
  - 分类任务：Accuracy 和 Macro F1
- **实验流程**：
  1. 使用基础模型（如 Linear Regression, XGBoost）在训练集上训练。
  2. 计算训练集上的残差，并选取残差最大的前 K% 样本作为上下文提供给 LLM。
  3. MARICL 框架运行，生成并优化修正项。
  4. 在独立的测试集上评估 MARICL 的最终性能。

### 基线方法对比
论文与多种类型的基线方法进行了比较：
- **传统机器学习**：Linear/Logistic Regression, XGBoost
- **可解释模型**：EBM (Explainable Boosting Machine)
- **神经网络模型**：TabPFN
- **LLM 直接方法**：LLM-ICL (In-Context Learning), LLM-LEx
- **符号回归**：PySR, Symbolic Regression
- **残差修正基线**：PySR-on-residuals, MLP-on-residuals

## 3. 主要实验结果和性能指标

### 关键性能数据
- **全面性能提升**：在所有九个基准数据集上，MARICL 均优于其对应的基础模型。
- **显著提升案例**：
  - 在 **Cell-Free Protein** 数据集上，以线性模型为基础时，R² 提升了 **+0.236**。
  - 在 **Adult Income** 分类任务上，以 XGBoost 为基础时，Macro F1 提升了 **+0.108**（相对提升 15.6%）。
- **消融实验结果**：
  - **移除迭代优化**：当禁用 `Textual Gradient Optimization` (`T=0`) 时，性能显著下降，证明了迭代过程的价值。
  - **移除先验知识**：通过匿名化特征名称（如将 "NAD" 改为 "feat_0"）、移除领域上下文提示、使用较小的开源 LLM (Llama-3-8B)，研究发现大约 **50%** 的性能增益来源于数据驱动的推理过程，另一半则来自 LLM 的先验知识。
  - **跨批次泛化实验**：这是最有力的证据之一。在 **Cell-Free Protein** 数据集中，将一个实验批次（plate）上学到的修正公式，直接应用于另一个批次，且**不进行任何重新训练或调用 LLM**。
    - 在**相同试剂方案**的批次间，修正公式在 **92-97%** 的情况下都能提升预测效果。
    - 在**不同试剂方案**的批次间，修正公式几乎全部失效（仅 0-8% 成功）。
    - 这一结果表明，MARICL 学习到的不是随机噪声，而是与特定生化条件相关的**真实机制**。

## 4. 关键结论和发现

### 主要发现
1.  **残差是通往理解的桥梁**：通过将 LLM 的注意力引导到基础模型的系统性错误上，可以有效地从数据中推导出有意义的、可解释的机制。
2.  **MARICL 实现了机制发现**：该方法不仅提高了预测准确性，更重要的是，它生成的符号公式能够反映真实世界的科学原理（如辅因子协同效应、米氏饱和动力学）。
3.  **机制具有可迁移性**：跨批次实验证明，MARICL 学习到的修正项具有真正的泛化能力，其成功边界与已知的生物化学知识一致，而非简单的数据拟合。

### 方法的局限性
1.  **依赖于基础模型的质量**：当基础模型已经非常强大，捕捉了大部分非线性关系时，可用于修正的残差信号就会很弱，MARICL 的提升空间也相应减小。
2.  **在复杂社会系统中效果有限**：在像“高中社交分组”这类受大量未观测混杂因素影响的领域，MARICL 只能做出微小的改进，因为它正确地识别出数据中缺乏可纠正的强结构性模式。
3.  **对高维噪声敏感**：当数据中存在大量无关特征时，可能会干扰 LLM 的假设生成。
4.  **部分收益依赖于 LLM 先验**：约一半的性能增益来自于 LLM 的预训练知识，这意味着在 LLM 完全不了解的全新领域，其效果可能会打折扣。

### 未来工作方向
- 探索如何进一步减少对 LLM 先验知识的依赖，使其成为一个更纯粹的数据驱动发现工具。
- 将 MARICL 框架扩展到更多样化的数据模态和更复杂的科学问题中。
- 研究如何利用 MARICL 生成的机制来指导新的实验设计，形成“预测-发现-验证”的闭环科学探索流程。

</details>

---

### 15. [Accelerating Divisible Load Processing Through Machine Learning: A Practical Framework for Large-Scale Workloads](https://arxiv.org/abs/2605.23247)

**Authors**: Bharadwaj Veeravalli  
**Category**: cs.LG  
**Published**: 2026-05-25  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.23247v1  

#### Abstract
In this paper, we introduce the first machine learning framework for predicting optimal processing times in Single-Level Tree Network (SLTN) architectures for the Divisible Load Theory (DLT) paradigm. Using a feedforward neural network(FNN) with 16 engineered features, we train a model on 100,000 sy...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Accelerating Divisible Load Processing Through Machine Learning: A Practical Framework for Large-Scale Workloads

---

## 1. 论文的主要贡献和创新点

### ✅ 解决了什么问题
该论文针对 **Divisible Load Theory (DLT)** 在 **Single-Level Tree Network (SLTN)** 架构中计算最优处理时间时存在的**高计算开销**问题。传统 DLT 需要显式求解递归方程（如 $ B $、$ S_i $、$ \alpha_i $、$ T^* $），每次系统参数（如处理器速度、链路带宽、负载大小）变化时都需重新计算，导致在动态环境（如云平台、卫星网络）中难以实现实时调度。

### ✅ 提出了什么新方法或新思路
首次提出一种**基于机器学习的端到端预测框架**，使用 **Feedforward Neural Network (FNN)** 直接从系统参数预测 DLT 的最优处理时间 $ T^* $，而无需显式编程或求解任何 DLT 数学公式。

- **核心思想**：将 DLT 优化问题转化为一个监督学习任务，训练神经网络“学习”隐含的数学关系。
- **输入特征**：设计了 16 个工程化特征（如均值、标准差、异质性度量、计算/通信比等），将变长的原始参数（不同 $ n $ 导致不同维度）转换为固定长度表示。
- **模型架构**：采用三层 FNN（128 → 64 → 32 神经元），ReLU 激活 + Dropout 正则化。

### ✅ 相比现有方法的优势
| 维度 | 传统 DLT 方法 | 本文 ML 方法 |
|------|----------------|---------------|
| **推理速度** | 秒级迭代计算 | **<1 毫秒** 推理 |
| **计算开销** | 每次配置变更需重算 | 一次训练，无限次快速推断 |
| **适用场景** | 静态离线分析为主 | 支持实时调度、设计空间探索 |
| **可扩展性** | 复杂扩展（如动态资源）难建模 | 易于扩展至更复杂场景（未来方向） |
| **加速比** | — | 实现 **10–100× 加速** |

> ⚡ 创新亮点：这是**首篇将监督学习用于直接预测 DLT 最优处理时间**的工作，展示了 ML 在经典分布式调度理论中的实用潜力。

---

## 2. 核心实验方法和设置

### 📊 数据集
- **数据来源**：合成生成（synthetically generated）
- **样本数量**：共 100,000 个配置
  - 训练集：80,000
  - 验证集：10,000
  - 测试集：10,000
- **参数范围**：
  - 子节点数 $ n $：3–20
  - 负载大小（load）：1–100 GB
  - 处理器速度 $ w_i $：1–15 GFLOPS/s
  - 链路带宽 $ z_i $：10–150 MB/s
- **标签生成**：通过运行标准 DLT 算法获得真实最优时间 $ T^* $

### 🔧 实验设置
- **模型结构**：
  - 输入层：16 维特征向量（见 Table 1）
  - 隐藏层：3 层（128, 64, 32），ReLU 激活
  - Dropout：率 = 0.2
  - 输出层：单神经元，无激活函数（回归任务）
- **优化器**：Adam ($ \text{lr} = 0.001 $)
- **损失函数**：Mean Squared Error (MSE)
- **训练细节**：
  - Batch size：256
  - Early stopping：patience=10
  - 归一化：z-score（基于训练集统计量）
- **硬件平台**：标准 CPU（非 GPU 加速）

### 🎯 评估指标
| 指标 | 描述 |
|------|------|
| $ R^2 $ (Coefficient of Determination) | 衡量模型解释方差的能力 |
| MAE (Mean Absolute Error) | 平均绝对误差（秒） |
| RMSE (Root Mean Squared Error) | 均方根误差 |
| MAPE (Mean Absolute Percentage Error) | 平均绝对百分比误差 |
| 推理时间 | 单次预测耗时（目标：<1ms） |

### 🆚 基线方法对比
- **Analytical DLT Solver**：作为黄金标准（ground truth），用于生成标签并进行性能比较。
- 未与其他 ML 方法直接对比（因本工作是首创），但在引言中指出：
  - 强化学习（RL）方法（如 [13]）收敛慢、泛化差；
  - 本文方法在精度与速度上全面优于传统数值求解。

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据
| 指标 | 数值 |
|------|------|
| $ R^2 $ | **0.9942**（测试集） |
| MAPE | **7.87%**（整体）；在大负载下可降至 **<5%** |
| MAE | ~50–100 秒（与负载规模无关） |
| 推理时间 | **<1 毫秒**（实现 10–100× 加速） |
| 训练时间 | 约 95 秒（37 个 epoch，CPU 上完成） |

### 🔍 分层误差分析（Stratified Analysis）
- **按系统规模 $ n $**：
  - 所有 $ n=3 $ 到 $ 20 $ 下中位误差稳定在 **5–8%**
  - 表明模型成功泛化至不同网络规模
- **按负载大小**：
  - 小负载（<5 GB）：MAPE 较高（可达 200%），但源于相对误差放大（绝对误差仍小）
  - 大负载（>40 GB）：MAPE **<5%**，适合生产部署
- **按异质性（heterogeneity）**：
  - 一般情况（heterog ≤ 10）：误差均匀分布（0–20%）
  - 极端异质系统（>10）：出现少量高误差异常值（最高达 400%），建议结合 DLT 验证

### ❌ 消融实验（Ablation Study）
文中虽未明确列出消融表格，但通过以下方式验证设计选择：
- **网络宽度**：尝试更宽/窄结构，发现当前配置为最佳权衡（窄则降 3% $ R^2 $，宽则无增益）
- **Dropout 率**：测试 p=0.1, 0.2, 0.3 → p=0.2 效果最优
- **特征工程必要性**：强调使用统计特征而非原始序列的关键作用，解决了变长输入问题

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **神经网络能有效学习 DLT 的数学结构**：
   - 特征重要性分析表明，FNN 隐式捕捉了 **load conservation** 和 **simultaneous finishing constraints**。
   - 各层逐步构建抽象概念：第一层识别瓶颈类型（compute/communication-bound），第二层近似 $ B $ 公式形式，第三层形成类似 $ S_i $ 的累积乘积。

2. **DLT 是 ML 近似的理想候选问题**：
   - 具备“**复杂但规则**”、“**确定且连续**”的特点，使得 ML 可以达到 >95% 准确率的同时实现数量级加速。

3. **实际应用价值显著**：
   - 支持 **real-time scheduling**、**design space exploration**、**cloud resource allocation** 等需要毫秒级响应的应用。
   - 特别适用于 **satellite constellation networks** 等动态拓扑场景。

### ⚠️ 方法的局限性
| 局限 | 说明 |
|------|------|
| **静态假设** | 当前仅支持静态配置，不处理运行时故障、带宽波动或任务动态到达 |
| **忽略结果回传阶段** | 仅建模 root → children 的分发过程，未考虑结果收集（result collection） |
| **未覆盖多级树网络** | 限制在 SLTN，尚未推广到 Multi-Level Tree Network |
| **极端异质系统表现下降** | 在高度不平衡系统中可能出现较大误差，需谨慎使用 |

### 🔮 未来工作方向
1. 扩展至 **Multi-Level Tree Networks** 和其他拓扑（如线性网络、星型网络）
2. 引入 **Graph Neural Networks (GNN)** 显式编码网络拓扑结构
3. 结合 **Physics-Informed Neural Networks (PINNs)** 注入 DLT 约束（如同时完成条件）
4. 探索 **Reinforcement Learning** 或 **Meta-Learning** 应对动态环境
5. 开发 **Hybrid ML+DLT Verification Framework**：对高风险配置（小负载 + 高异质 + 大 $ n $）自动触发精确验证

---

> 💡 **总结一句话**：  
> 本文开创性地证明了 **FNN 可以高效、准确地替代传统 DLT 数值求解器**，在保持接近最优精度的前提下实现 **10–100× 的计算加速**，为大规模分布式系统的实时资源调度提供了全新的数据驱动范式。

</details>

---

### 16. [Non-normal spectral signatures of instability in neural network training dynamics](https://arxiv.org/abs/2605.23476)

**Authors**: Souvik Ghosh  
**Category**: cs.LG  
**Published**: 2026-05-25  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.23476v1  

#### Abstract
Training instabilities in deep networks - loss spikes, oscillatory convergence, and gradient pathologies - are empirically prevalent but lack a rigorous operator-theoretic explanation. We show that the linearized update operators for practically used optimizers are generically non-normal: for Adam, ...

---

### 17. [HawkesLLM: Semantic Uncertainty Propagation in Agentic Text Simulation](https://arxiv.org/abs/2605.23043)

**Authors**: Zewei Deng, Tinghan Ye, Liyan Xie  
**Category**: cs.CL  
**Published**: 2026-05-25  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.23043v1  

#### Abstract
Agentic text-simulation systems write in sequence, with each item becoming possible context for later steps. That makes uncertainty path-dependent: an early ambiguity can affect later outputs. This paper studies this problem with HawkesLLM, a framework that separates temporal influence modeling from...

---

### 18. [Multi-Factor Trust-Driven Secure Communication Model for Cloud-Based Digital Twins](https://arxiv.org/abs/2605.23566)

**Authors**: Deepika Saxena, Ashutosh Kumar Singh  
**Category**: cs.DC  
**Published**: 2026-05-25  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.23566v1  

#### Abstract
Cloud-based Digital Twin (DT) platforms enable real-time monitoring, simulation, and collaborative decision-making across distributed clients. However, ensuring secure and trustworthy communication remains a critical challenge due to heterogeneous client behavior, resource contention, and evolving a...

---

### 19. [FuRA: Full-Rank Parameter-Efficient Fine-Tuning with Spectral Preconditioning](https://arxiv.org/abs/2605.22869)

**Authors**: Yequan Zhao, Ruijie Zhang, Liyan Tan, Niall Moran, Tong Qin, Zheng Zhang  
**Category**: cs.LG  
**Published**: 2026-05-25  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.22869v1  

#### Abstract
Both full fine-tuning (Full FT) and parameter-efficient fine-tuning methods such as LoRA introduce weight updates without accounting for the spectral structure established during pretraining. As a result, noisy gradients from limited fine-tuning data can perturb robust pretrained features. We identi...

---

### 20. [RelPrism: A Multi-Faceted Pre-training Framework with Self-Generated Tasks for Relational Databases](https://arxiv.org/abs/2605.23241)

**Authors**: Jinyu Yang, Cheng Yang, Junze Chen, Zedi Liu, Muhan Zhang, Hanyang Peng, Chuan Shi  
**Category**: cs.LG  
**Published**: 2026-05-25  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.23241v1  

#### Abstract
Relational databases (RDBs) remain the cornerstone of modern data systems and support diverse predictive tasks. Recent relational deep learning (RDL) methods enable end-to-end prediction by converting RDBs into graphs, where rows are represented as nodes and inter-table interactions are represented ...

---

### 21. [Approaching I/O-optimality for Approximate Attention](https://arxiv.org/abs/2605.23751)

**Authors**: P\'al Andr\'as Papp, Aleksandros Sobczyk, Anastasios Zouzias  
**Category**: cs.LG  
**Published**: 2026-05-25  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.23751v1  

#### Abstract
We revisit the I/O complexity of attention in large language models. Given query-key-value matrices $Q,K,V\in\mathbb{R}^{n\times d}$, and a machine with fast memory size $M$, the goal is to compute the "attention matrix" $A=\text{softmax}(Q K ^{\top}/\sqrt{d}) V$ with the minimal number of data tran...

---

### 22. [Complete-muE: Optimal Hyperparameter Transfer and Scaling for MoE Models](https://arxiv.org/abs/2605.23893)

**Authors**: Hongwu Peng, Ohiremen Dibua, Yuanjun Xiong, Yifan Gong, Jianming Zhang, Yan Kang  
**Category**: cs.LG  
**Published**: 2026-05-25  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.23893v1  

#### Abstract
We propose Complete-muE, a framework which targets hyperparameter transfer across dense FFN and any Mixture-of-Experts (MoE) setups in transformer blocks. Existing tools such as $\mu$P (requires fixed architectue) or SDE (requires fixed per-step token count) cannot directly solve the hyperparameter ...

---

### 23. [Parallel Context Compaction for Long-Horizon LLM Agent Serving](https://arxiv.org/abs/2605.23296)

**Authors**: Musa Cim, Burak Topcu, Chita Das, Mahmut Taylan Kandemir  
**Category**: cs.AI  
**Published**: 2026-05-25  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.23296v1  

#### Abstract
Long-horizon LLM agents accumulate growing conversation histories that eventually exceed the model's context window. Context compaction via LLM-based summarization keeps the conversation bounded, but summarization is inherently lossy and the blocking call stalls agent inference for tens of seconds. ...

---

### 24. [One Policy, Infinite NPCs: Persona-Traceable Shared RL Policies for Scalable Game Agents](https://arxiv.org/abs/2605.23652)

**Authors**: Yoosung Hong  
**Category**: cs.AI  
**Published**: 2026-05-25  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.23652v1  

#### Abstract
On a 300-persona life-simulation benchmark, pcsp achieves compositional zero-shot persona identification up to 17x above chance, Spearman rho approx 0.73 semantic-behavioral alignment, and 22x faster inference than an LLM-as-policy baseline. Life simulation games require hundreds to thousands of non...

---

### 25. [OpenSkillEval: Automatically Auditing the Open Skill Ecosystem for LLM Agents](https://arxiv.org/abs/2605.23657)

**Authors**: Jiahao Ying, Boxian Ai, Wei Tang, Siyuan Liu, Yixin Cao  
**Category**: cs.CL  
**Published**: 2026-05-25  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.23657v1  

#### Abstract
Skills, i.e., structured workflow instructions distilled for large language models (LLMs), are becoming an increasingly important mechanism for improving agent performance on real-world downstream tasks. However, as the open-source skill ecosystem rapidly expands, it remains unclear how different mo...

---

### 26. [ThriftAttention: Selective Mixed Precision for Long-Context FP4 Attention](https://arxiv.org/abs/2605.23081)

**Authors**: Joe Sharratt  
**Category**: cs.LG  
**Published**: 2026-05-25  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.23081v1  

#### Abstract
Efficient attention algorithms are critical to mitigate the quadratic cost of attention in long-context workloads. Prior work utilises block-scaled quantisation techniques on Blackwell GPUs to move attention computation to 4-bit precision to accelerate inference. However, these techniques result in ...

---

### 27. [Coupling-Robust Accuracy in Multiphysics Physics Informed Neural Networks via Kronecker-Preconditioned Optimization](https://arxiv.org/abs/2605.23391)

**Authors**: Youngjae Park, Jaemin Kim, Junghwa Hong  
**Category**: cs.LG  
**Published**: 2026-05-25  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.23391v1  

#### Abstract
Physics-informed neural networks (PINNs) for coupled multiphysics systems suffer systematic accuracy degradation as inter-equation coupling strengthens. We provide a theoretical explanation for this phenomenon through neural tangent kernel (NTK) analysis: for linearly coupled systems, we prove that ...

---

### 28. [NeuroNL2LTL: A Neurosymbolic Framework for Natural Language Translation of Linear Temporal Logic](https://arxiv.org/abs/2605.22874)

**Authors**: Paapa Kwesi Quansah, Ernest Bonnah  
**Category**: cs.AI  
**Published**: 2026-05-25  
**Score**: 6.5  
**Type**: new  
**ArXiv ID**: 2605.22874v1  

#### Abstract
Effectively translating between natural language (NL) and formal logics like Linear Temporal Logic (LTL) requires expertise that limits formal verification's reach in safety-critical development. Template-based approaches sacrifice expressiveness for reliability; neural methods achieve fluency but p...

---

### 29. [PathCal: State-Aware Reflection-Marker Calibration for Efficient Reasoning](https://arxiv.org/abs/2605.23074)

**Authors**: Lingyu Jiang, Zirui Li, Shuo Xing, Peiran Li, Tsubasa Takahashi, Dengzhe Hou, Zhengzhong Tu, Kazunori Yamada, Fangzhou Lin  
**Category**: cs.AI  
**Published**: 2026-05-25  
**Score**: 6.5  
**Type**: new  
**ArXiv ID**: 2605.23074v1  

#### Abstract
The emergence of Large Reasoning Language Models (LRMs) has paved the way for tackling complex reasoning tasks through test-time scaling by generating long-form Chain-of-Thought (CoT) trajectories during inference. Meanwhile, these trajectories often contain explicit reflection markers such as ``wai...

---

### 30. [Structure-Guided Entity Resolution: Fine-Tuning LLMs for Robust Name Matching in Complex Linguistic Contexts](https://arxiv.org/abs/2605.23597)

**Authors**: Shivam Chourasia, Hitesh Kapoor, Nilesh Patil  
**Category**: cs.CL  
**Published**: 2026-05-25  
**Score**: 6.5  
**Type**: new  
**ArXiv ID**: 2605.23597v1  

#### Abstract
Matching person names across heterogeneous records is a core challenge in entity resolution, especially within linguistically and culturally complex environments. Variations in naming conventions, inconsistent transliteration across scripts, and frequent data entry errors make it difficult to unify ...

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
