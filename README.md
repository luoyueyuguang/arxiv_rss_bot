# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-05-07 08:11:54 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG

## 📚 Recent Papers

### 1. [Piper: Efficient Large-Scale MoE Training via Resource Modeling and Pipelined Hybrid Parallelism](https://arxiv.org/abs/2605.05049)

**Authors**: Sajal Dash, Feiyi Wang  
**Category**: cs.DC  
**Published**: 2026-05-07  
**Score**: 13.5  
**Type**: new  
**ArXiv ID**: 2605.05049v1  

#### Abstract
Frontier models increasingly adopt Mixture-of-Experts (MoE) architectures to achieve large-model performance at reduced cost. However, training MoE models on HPC platforms is hindered by large memory footprints, frequent large-scale communication across heterogeneous networks, and severe workload im...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：**Piper: Efficient Large-Scale MoE Training via Resource Modeling and Pipelined Hybrid Parallelism**

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
当前在 **HPC 平台**上训练大规模 **Mixture-of-Experts (MoE)** 模型面临三大挑战：
- **高通信开销**：专家并行（Expert Parallelism, EP）引入频繁的 `all-to-all` 通信，在非均匀网络拓扑（如 Dragonfly）下延迟显著。
- **负载不均衡**：路由机制导致部分专家接收更多 token，造成 GPU 利用率低下。
- **资源利用低效**：缺乏平台感知的混合并行策略，难以联合优化内存、计算与通信。

特别是对于 **细粒度 MoE 架构**（如 DeepSeek-MoE），其 tall-and-skinny GEMMs 导致硬件利用率差，激活内存膨胀，进一步加剧瓶颈。

---

### 🚀 提出的新方法与创新思路

作者提出 **Piper**，一个基于资源建模与流水线混合并行的高效 MoE 训练框架，包含以下核心创新：

#### 1) **Analytical and Empirical Resource Modeling**
- 构建数学模型量化 MoE 在不同并行策略下的 **memory、compute、communication 开销**。
- 模型参数化于实测平台特性（带宽、延迟、HBM 容量），用于搜索可行且高效的 `(PP, EP)` 配置。

#### 2) **Pipelined Hybrid Parallelism（核心创新）**
- 将 **Pipeline Parallelism (PP)** 引入 MoE 层内部，构建 **PP × EP 二维设备网格**。
- 每个 pipeline stage 内部执行局部 expert-parallel，将昂贵的 `all-to-all` 限制在拓扑局部组内（如同一节点或 Rosetta 组），实现通信本地化与重叠。

#### 3) **Topology-Aware Hierarchical All-to-All (HALO)**
- 设计面向 **Dragonfly 拓扑**的三层异步 `all-to-all` 算法：
  - Phase I: 节点内交换（利用 GPU-NIC 亲和性）
  - Phase II: 跨节点批量 P2P
  - Phase III: 节点内再分发
- 利用依赖关系并发执行 Phase I 与 II/III，提升 NIC 利用率。

#### 4) **Expert Migration for Load Balancing**
- 动态迁移专家以平衡负载：定期检测负载偏斜，触发最小代价的专家交换。
- 迁移成本可摊销至 <5% 总训练时间，尤其适用于无辅助损失函数的场景。

#### 5) **Trillion-Scale MoE Training Demonstration**
- 成功在 Frontier 超算上训练 **万亿参数级 MoE 模型**，达到 **20% MFU**，远超 X-MoE 报道的 5.23%。

---

### 🔍 相比现有方法的优势

| 方面 | 现有方法（如 X-MoE, DeepSpeed-MoE） | Piper |
|------|-------------------------------|--------|
| 并行策略 | 主要依赖 EP + TP + DP，未系统整合 PP | 显式结合 PP 与 EP，实现通信本地化 |
| 通信优化 | 使用 flat all-to-all（NCCL/RCCL） | HALO 算法，拓扑感知，带宽利用率更高 |
| 负载均衡 | 依赖路由层损失函数或 token dropping | 支持运行时物理迁移专家，更灵活 |
| 平台适配性 | 缺乏系统级建模 | 基于实测建模自动选择最优配置 |
| 可扩展性 | 百亿到千亿参数为主 | 支持 trillion-scale，MFU 更高 |

---

## 2. 核心实验方法和设置

### 📚 数据集与模型
- **未使用传统 NLP 数据集**，而是聚焦于 **真实 MoE 架构的端到端训练模拟与实测**。
- 实验涵盖多个 SOTA MoE 模型（见 Table I）：
  - **DeepSeek-V2/V3**, **Mixtral 8×7B/8×22B**, **Qwen3**, **Kimi K2**, **Llama 4 Maverick**, **Arctic** 等。
- 参数规模从数十亿到 **~1T 参数**。

### ⚙️ 实验设置
- **平台**：**Frontier 超级计算机**（AMD Instinct MI250X GPU，Infinity Fabric，Dragonfly 网络）。
- **并行维度**：组合使用 Pipeline Parallelism (PP)、Expert Parallelism (EP)、Data Parallelism (DP)。
- **微基准测试**（Micro-benchmarking）：
  - 测量单卡 attention 与 FFN GEMM 吞吐（图3、图4）
  - 测试不同规模下 `all-to-all` 带宽与延迟（图5）
- **调度策略**：采用 **1F1B (one-forward-one-backward)** pipeline schedule 降低 bubble。

### 📊 评估指标
| 指标 | 描述 |
|------|------|
| **MFU (Model FLOPs Utilization)** | 实际达到的 TFLOPs 占理论峰值的比例，为核心性能指标 |
| **End-to-End Throughput** | 每秒处理的 tokens 数或每 step 时间 |
| **All-to-All Latency/Bandwidth** | 通信效率的关键衡量 |
| **Memory Usage per GPU** | 是否满足 HBM 容量约束（64GB） |
| **Scaling Efficiency** | 弱扩展下的性能保持率 |

### 🆚 基线方法对比
- **X-MoE**：当前最先进的细粒度 MoE 训练框架，作为主要对比对象。
- **DeepSpeed-MoE / DeepSpeed-TED**：支持多种并行模式，但缺乏平台感知优化。
- **Tutel**：提供高效 dispatch kernel，但不覆盖完整训练策略设计。

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据

| 指标 | 结果 |
|------|------|
| **MFU 提升** | **2–3.5× 高于 X-MoE**（图13） |
| **All-to-All 带宽提升** | **1.2× – 9× 超过 RCCL 实现**（图8） |
| **Trillion-Scale MFU** | 达到 **20% MFU**（X-MoE 最高仅报告 5.23% for 545B） |
| **Weak Scaling 效率** | 从 64 到 1024 GPUs 达到 **73% 缩放效率**（图14） |
| **Expert Migration 开销** | 摊销 < **5% 总训练时间** |

---

### 📊 与基线方法对比结果（图13）

| 模型大小 | Piper 所需 GPU | X-MoE 所需 GPU | MFU 提升倍数 |
|---------|----------------|----------------|---------------|
| 10.1B (Small) | 8 | 256 | ~3.6× |
| 55.2B (Medium) | 32 | 256 | ~3.0× |
| 201.4B (Large) | 80 | 1024 | ~2.8× |
| 545.4B (Super) | 512 | 1024 | ~2.5× |

> ✅ **Piper 用更少 GPU 实现更高吞吐，资源利用率显著优于 X-MoE**

---

### 🔬 消融实验与分析（隐含在文中）

虽然没有显式“ablation study”章节，但通过多组实验揭示关键因素影响：

1. **Pipeline + EP vs 纯 EP**：
   - 图10 显示，随着 EP 增大，单 GPU 内存需求下降，但通信开销剧增；Piper 通过控制 EP 规模（受限于拓扑域）避免跨柜通信。

2. **HALO vs RCCL all-to-all**：
   - 图8 表明，当节点数 ≥16 时，HALO 显著优于 RCCL（最高达 9×），因后者无法有效处理跨柜低带宽链路。

3. **Checkpointing 对 MFU 影响**：
   - 图12 中条形图加阴影表示启用 activation checkpointing，虽降低 MFU，但仍维持在合理水平（如 24.5%-53.8%），说明策略仍有效。

4. **单层吞吐上限分析（图11）**：
   - 单节点训练单层 MoE 层可达 **100+ TFLOPs**，为全模型性能设定了理论天花板。

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **Pipeline Parallelism 可有效缓解 MoE 通信瓶颈**  
   将 PP 应用于 expert-parallel 层，能将 `all-to-all` 局部化，极大减少跨节点通信压力。

2. **平台感知建模至关重要**  
   通用框架（如 DeepSpeed）忽略底层拓扑特征，而 Piper 通过建模 + 微测实现了对 Dragonfly 网络的深度优化。

3. **静态分配不足以应对动态负载偏斜**  
   即使有 load-balancing loss，早期训练阶段仍存在严重不平衡；**expert migration 是低成本补救手段**。

4. **Trillion-Scale MoE 是可行的**  
   在 Frontier 上实现 **20% MFU 的万亿参数 MoE 训练**，验证了 Piper 的可扩展性。

---

### ⚠️ 方法的局限性

| 局限 | 说明 |
|------|------|
| **依赖特定拓扑假设** | HALO 针对 Dragonfly 设计，迁移到其他拓扑需重新调优 |
| **专家迁移需高速互联** | 若专家分布在低速网络节点间，迁移开销不可接受 |
| **未支持稀疏注意力或其他新型结构** | 当前聚焦 FFN 类 MoE，未来可拓展至 attention-MoE |
| **自动化程度仍有提升空间** | 配置搜索依赖人工设定约束条件 |

---

### 🔮 未来工作方向

1. **支持动态调整 PP/EP 比例**（runtime reconfiguration）
2. **集成更智能的 routing 机制**（如 expert-choice + migration 联合优化）
3. **扩展至多模态 MoE 或 MoE-for-Attention 架构**
4. **构建开源工具链**，支持用户输入模型结构自动生成最优并行策略
5. **探索与 MoE 推理系统的协同设计**

---

> 💡 **总结一句话**：  
> **Piper 通过“资源建模 + 流水线混合并行 + 拓扑感知通信”，首次实现了在 HPC 平台上高效、可扩展的 trillion-scale MoE 训练，将 MFU 提升 2–3.5×，为下一代超大规模稀疏模型训练提供了系统性解决方案。**

</details>

---

### 2. [RLearner-LLM: Balancing Logical Grounding and Fluency in Large Language Models via Hybrid Direct Preference Optimization](https://arxiv.org/abs/2605.04539)

**Authors**: Qiming Bao, Juho Leinonen, Paul Denny, Michael J. Witbrock  
**Category**: cs.CL  
**Published**: 2026-05-07  
**Score**: 11.5  
**Type**: new  
**ArXiv ID**: 2605.04539v1  

#### Abstract
Direct Preference Optimization (DPO), the efficient alternative to PPO-based RLHF, falls short on knowledge-intensive generation: standard preference signals from human annotators or LLM judges exhibit a systematic verbosity bias that rewards fluency over logical correctness. This blindspot leaves a...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*RLearner-LLM: Balancing Logical Grounding and Fluency in Large Language Models via Hybrid Direct Preference Optimization*

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
该论文针对 **知识密集型生成任务**（如教育解释生成）中，当前主流对齐方法 **Direct Preference Optimization (DPO)** 存在的根本性缺陷进行了诊断：

- **标准偏好信号存在“逻辑盲区”**：无论是人类标注者还是 LLM-as-a-judge，都表现出显著的 **verbosity bias（冗长偏见）**，即更偏好语言流畅、篇幅较长的回答，而忽视其逻辑正确性。
- 这导致模型虽然输出 **fluent and confident-sounding** 的文本，但在 **逻辑蕴含（NLI Entailment）** 上得分极低（SFT 模型仅 0.05–0.22），形成“**alignment tax**”——即为了提升流畅性而牺牲逻辑严谨性。

### 🚀 提出的新方法：RLearner-LLM 与 Hybrid-DPO
提出 **RLearner-LLM** 框架，通过 **Hybrid Direct Preference Optimization (Hybrid-DPO)** 解决上述问题：

- **核心思想**：用 **双信号奖励机制** 自动构建高质量的偏好对（preference pairs），无需人工标注。
- **Hybrid Reward 公式**：
  $$
  H(E) = 0.5 \cdot S_{\text{NLI}}(E) + 0.5 \cdot S_{\text{verifier}}(E)
  $$
  - $S_{\text{NLI}}$: 来自 DeBERTa-v3 的 NLI 蕴含概率，衡量 **逻辑正确性**。
  - $S_{\text{verifier}}$: 来自 Alpaca-7B 验证器的评分，衡量 **教学质量和语言流畅性**。
- 支持两种变体：
  - **Additive (HA)**：加权平均，召回率高。
  - **Multiplicative-ACR (HM)**：乘积形式 + ACR 门控 + 长度惩罚，精度更高。

### ✅ 相比现有方法的优势
| 维度 | 传统 DPO | RLearner-LLM (Hybrid-DPO) |
|------|----------|----------------------------|
| 偏好信号来源 | 人类或 LLM judge（有 verbosity bias） | 自动化双信号融合（无偏见） |
| 是否需要人工标注 | 是 | 否 |
| 是否解决 alignment tax | 否 | 是，同时提升逻辑性和流畅性 |
| 可扩展性 | 依赖昂贵的人类反馈 | 完全自动化，适合大规模部署 |

---

## 2. 核心实验方法和设置

### 📚 数据集
- **训练数据（SFT Corpus）**：
  - 来源：PeerWise 平台上的本科生生成的 **13,211 个问答对**。
  - 特点：反映真实学习者推理过程，非专家撰写，存在一定质量上限。
- **测试数据**：
  - 五个学术领域，各含 **100 题的保留测试集**：
    - Cardiff Biology
    - Sydney Biology
    - Auckland Law
    - UK Medicine Year 1
    - UK Medicine Year 2

### ⚙️ 实验设置
- **基础模型（Base Architectures）**：
  - `LLaMA-2-13B`
  - `Qwen3-8B`
  - `Gemma 4 E4B-it`（约 4.5B 有效参数）
- **训练流程**：
  1. **SFT**：监督微调，作为起点。
  2. **偏好数据构建**：每个问题生成 3 个候选解释，用 Hybrid Reward 打分，构建偏好对。
  3. **Hybrid-DPO 微调**：基于偏好对进行优化。
- **硬件**：NVIDIA A100 GPU 集群，使用 TRL 和 PEFT 库。

### 📊 评估指标
| 指标 | 含义 |
|------|------|
| **NLI Entailment ($S_{\text{NLI}}$)** | 使用 `cross-encoder/nli-deberta-v3-small` 计算解释是否逻辑蕴含正确答案（核心指标） |
| **Answer Coverage Rate (ACR)** | 正确答案关键词是否被覆盖 |
| **BERTScore (vs Student Reference)** | 文本相似度，衡量风格匹配 |
| **Verifier Score (Ver)** | Alpaca-7B 对解释质量的打分（诊断用途） |
| **BLEU** | 传统 n-gram 匹配指标 |
| **Pairwise Win Rate** | GPT-4o-mini 在盲测中选择哪个模型输出更好 |

### 🔁 基线方法对比
- **SFT Baseline**：仅监督微调模型。
- **DPO v1/v2**：仅基于 verifier 或小规模偏好数据的 DPO 模型（用于展示 alignment tax）。
- **ILearner-LLM (K=5)**：迭代式增强方法，使用 5 轮 refine，计算成本为单次推理的 5 倍（强基线）。
- **GPT-4o-mini**：作为裁判模型，用于 pairwise comparison。

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据（NLI 提升）

| Domain | LLaMA-2-13B (SFT→RLearner) | Qwen3-8B (SFT→RLearner) | Gemma 4 E4B-it (SFT→RLearner) |
|--------|-----------------------------|--------------------------|-------------------------------|
| **Cardiff Biology** | 0.0555 → **0.3209** (**5.8×**) | 0.1959 → 0.1820 | 0.2117 → **0.3505 (+66%)** |
| **Sydney Biology** | 0.0537 → **0.3562 (6.6×)** | 0.1737 → **0.2284 (+31%)** | 0.2469 → 0.2309 |
| **Auckland Law** | 0.2702 → **0.3229 (+19%)** | 0.3191 → 0.2303 | 0.3911 → **0.4377*** (**首次超越 ILearner-LLM**) |
| **UK Medicine Y1** | 0.0860 → **0.4251 (4.9×)** | 0.2457 → 0.2104 | 0.2962 → **0.3910 (+32%)** |
| **UK Medicine Y2** | 0.2319 → **0.3885 (+68%)** | 0.1632 → **0.2009 (+23%)** | 0.1604 → **0.3892 (2.4×)** |

> ✅ **总体表现**：在 **15 个 (architecture, domain) 组合中，11 个实现了 NLI 提升**，最高达 **6.6×**。

### 🆚 与基线方法对比
| 对比项 | 结果 |
|--------|------|
| **vs SFT** | RLearner-LLM (Qwen3) 在盲测中 **赢得 95%** 的比较 |
| **vs ILearner-LLM (K=5)** | Gemma 4 E4B-it 在 **Auckland Law 上首次超越** 迭代式方法（0.4377 > 0.3996） |
| **vs GPT-4o-mini 输出** | RLearner-LLM 输出虽更紧凑、逻辑更强，但在 GPT-4o-mini 判断下 **输掉 95%**，验证了 **verbosity bias 在前沿模型上依然存在** |

### 🔍 消融实验结果（Ablation Studies）

#### (1) **HA vs HM 变体对比**（Table 4）
- 在 11 个可比组合中：
  - **HM 赢得 7 次 NLI 对比**
  - **HA 赢得 4 次**
  - 平均差异仅 **+1.5 pp**，说明 **双信号假设本身是关键**，而非具体组合方式。
- HM 更适合单域、高一致性场景；HA 更适合跨域混合池。

#### (2) **SFT 失败模式分析**（Table 10）
SFT 模型普遍存在以下问题：
- **48–85%** 的输出“流利但空洞”（Verbose-low-NLI）
- **44–69%** 幻觉出虚假 URL
- **12–37%** 完全未锚定正确答案（ACR=0）

Hybrid-DPO 通过 NLI 信号和 ACR 门控有效缓解这些问题。

#### (3) **Tier-B 鲁棒性消融**（Table 12）
- 对训练数据施加更严格过滤（删除低质题、要求高评分）后：
  - 尽管训练样本减少 7×，但 **NLI 提升 48%**（0.3505 → 0.5202）
  - 表明 **高质量偏好数据能显著提升效果**

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **DPO 的根本问题不在算法，而在奖励信号**：标准偏好信号无法捕捉逻辑正确性，导致 verbosity bias 成为系统性缺陷。
2. **Hybrid-DPO 成功打破 alignment tax**：通过融合 NLI 和 verifier 信号，实现了 **逻辑性与流畅性的帕累托前沿提升**。
3. **方法具有良好的可扩展性**：
   - 即使在 **仅 4.5B 参数的 Gemma 模型** 上也能取得显著 NLI 提升。
   - 推理速度更快（如 Gemma 4 E4B-it 达 4.76s/q）。
4. **LLM-as-a-judge 不可靠**：GPT-4o-mini 明显偏好更长输出，即使其逻辑性较差，**呼吁使用 NLI、ACR 等逻辑感知自动指标**。

### ⚠️ 局限性
1. **Auckland Law 上仍落后于迭代方法**（LLaMA-2-13B 版本）：单步 DPO 尚无法完全替代多轮 refine。
2. **NLI 评估可能存在循环风险**：训练和评估使用同一 DeBERTa-v3-small 模型，未来应使用更大模型（如 DeBERTa-large）验证。
3. **SFT 数据来自本科生**：非专家撰写，限制了语言风格和准确性的上限，未来需专家标注数据验证。

### 🔮 未来工作方向
- 引入 **迭代式 Hybrid-DPO**，结合 ILearner-LLM 的 refine 思路。
- 使用 **更强的 NLI 模型** 构建更精细的奖励信号。
- 扩展到更多领域（如物理、工程）和多模态解释生成。
- 探索 **动态权重调整**（如根据领域自动选择 HA/HM）。

---

> 💡 **一句话总结**：  
> **RLearner-LLM 通过 Hybrid-DPO 框架，用自动化双信号奖励解决了 DPO 在知识密集任务中的“逻辑盲区”，在不牺牲流畅性的前提下大幅提升逻辑蕴含能力，且首次在单步推理中超越多轮迭代基线，为教育类 LLM 对齐提供了新范式。**

</details>

---

### 3. [A Queueing-Theoretic Framework for Stability Analysis of LLM Inference with KV Cache Memory Constraints](https://arxiv.org/abs/2605.04595)

**Authors**: Chengyi Nie, Nian Si, Zijie Zhou  
**Category**: cs.LG  
**Published**: 2026-05-07  
**Score**: 11.5  
**Type**: new  
**ArXiv ID**: 2605.04595v1  

#### Abstract
The rapid adoption of large language models (LLMs) has created significant challenges for efficient inference at scale. Unlike traditional workloads, LLM inference is constrained by both computation and the memory overhead of key-value (KV) caching, which accelerates decoding but quickly exhausts GP...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：A Queueing-Theoretic Framework for Stability Analysis of LLM Inference with KV Cache Memory Constraints

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
本论文针对 **Large Language Model (LLM) 推理服务中的稳定性问题**，尤其是在 **GPU 内存受限环境下** 的挑战。传统推理系统建模通常只关注计算资源（compute），而忽略了 **Key-Value (KV) Cache 所带来的内存开销**，这在实际部署中已成为主要瓶颈。

具体而言，当请求到达速率超过系统的有效处理能力时，队列将无界增长，导致延迟飙升、服务质量下降。因此，如何准确预测一个 LLM 服务系统是否“稳定”（即队列不会无限膨胀）是资源规划和调度策略设计的关键前提。

---

### 🚀 提出的新方法与新思路
作者提出了首个 **显式结合计算与 KV Cache 内存约束的排队论框架（queueing-theoretic framework）**，用于分析 LLM 推理系统的稳定性。

#### 主要创新点包括：
- **联合建模计算与内存约束**：不同于以往仅基于计算的排队模型，该框架将每个请求的 KV Cache 占用动态纳入考量，区分 **prompt 阶段** 和 **decode 阶段** 的不同内存增长模式。
- **引入 lifetime cumulative memory usage 概念**：定义了一个函数 $ g(s, o) $ 来量化单个请求在其整个生命周期内的累计 KV Cache 使用量，作为稳定性分析的基础。
- **推导严格的稳定性条件**：
  - 若到达率 $ \lambda > \mu $，则系统必然不稳定（Theorem 4.1）；
  - 若 $ \lambda < \mu(1 - \delta) $，其中 $ \delta = \text{ess sup}_{s,o} (s+o)/M $ 是最大请求对内存占比，则在 work-conserving 调度下系统稳定（Theorem 4.2）。
- **支持多阶段连续批处理（continuous batching）与 chunked prefill**：更贴近 vLLM 等现代推理引擎的实际实现。

---

### 🔍 相比现有方法的优势
| 方面 | 本文方法 | 现有方法 |
|------|--------|---------|
| **资源维度** | 同时考虑 compute 和 **GPU memory (KV Cache)** | 多数仅考虑 compute 或忽略 memory |
| **理论基础** | 给出闭式表达的 **稳定/不稳定边界条件** | 多为启发式调度或仿真验证 |
| **实用性** | 可直接用于估算所需 GPU 数量：$ \lceil \lambda / (\mu \cdot \text{target\_util}) \rceil $ | 缺乏可操作的容量规划工具 |
| **验证方式** | 在真实 GPU 环境中进行端到端实验验证 | 多停留在理论或模拟层面 |

> 💡 总结：这是第一篇将 **KV Cache 内存限制** 正式纳入排队论建模的工作，填补了 LLM 推理系统级分析的空白。

---

## 2. 核心实验方法和设置

### 📚 使用的数据集与工作负载分布
实验未使用单一固定数据集，而是通过控制不同的 **Prefill-Decode (P/D) 比例** 构造多种合成负载，并在一个真实基准上进行了验证：

1. **合成工作负载（Synthetic Workloads）**：
   - **P/D Ratio 1:1**：prefill 和 decode 长度均服从 `Uniform(10, 1600)`
   - **P/D Ratio 2:1**：prefill 更长，`Uniform(10, 2133)` vs `Uniform(10, 1066)`
   - **P/D Ratio 1:2**：decode 更长，`Uniform(10, 1066)` vs `Uniform(10, 2133)`
   - **Mixed 负载**：前半段为 2:1，后半段为 1:2，测试非平稳场景

2. **真实数据集验证**：
   - **LongBench v2**：包含 503 个复杂长上下文任务，具有高度变化且相关的 prefill/decode 长度分布。
   - 使用 80% 数据估计联合分布 $ p(s, o) $ 和处理时间 $ b $
   - 剩余 20% 用于测试，负载设为 20 qps

3. **极端负载补充实验**：
   - **P/D Ratio 8:1**：极长 prompt 场景，研究重尾处理时间下的鲁棒性

---

### ⚙️ 实验设置
- **硬件平台**：8 × NVIDIA A100 GPUs，每卡独立运行一个 replica
- **模型**：Meta-Llama-3-8B
- **推理引擎**：vLLM v1，启用 **chunked prefill**（chunk size = 512）
- **并行方式**：data parallelism（无 tensor/pipeline 并行）
- **负载均衡**：round-robin 分发请求
- **内存单位归一化**：KV Cache 容量 $ M = 131,000 $ tokens
- **batch 处理时间标准化**：以实测 median 或 trimmed mean 作为参数 $ b $

---

### 📊 评估指标
- **理论处理率** $ \mu_{\text{theory}} $：由公式 $ \mu = \frac{M}{b \cdot \mathbb{E}[g(s,o)]} $ 计算
- **实测处理率** $ \mu_{\text{gpu}} $：稳态期间完成请求数 / 时间长度（排除 warm-up 和 termination 阶段）
- **Gap Absolute Percentage (GAP)**：
  $$
  \text{GAP} = \left| \frac{\mu_{\text{theory}} - \mu_{\text{gpu}}}{\mu_{\text{gpu}}} \right| \times 100\%
  $$
- **队列长度演化图**：观察系统在不同 $ \lambda $ 下是否稳定
- **等待时间 CDF**：反映延迟表现

---

### 🔁 基线方法对比
本文并非提出新的调度算法，而是提供一种 **系统级分析框架**，因此没有直接对比其他调度器（如 HuggingFace TGI、Orca 等）。其“基线”实质是：
- 是否已有理论能准确预测稳定边界？
- 是否已有模型同时建模 memory 与 compute？

> ✅ 结论：现有排队模型（如 Li et al., 2025; Yang et al., 2024）均未显式建模 KV Cache，故无法准确预测高内存压力下的稳定性。

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据汇总

#### 表 1：Single-GPU 不同 P/D Ratio 下的 GAP
| P/D Ratio | $ \mu_{\text{gpu}} $ | $ \mu_{\text{theory}} $ | GAP |
|----------|------------------------|----------------------------|-----|
| 1:1      | 3.387                  | 3.263                      | 3.66% |
| 2:1      | 3.650                  | 3.956                      | 8.38% |
| 1:2      | 2.969                  | 2.902                      | 2.25% |
| Mixed    | 3.137                  | 3.385                      | 7.90% |

> ✔️ 所有 GAP < 10%，表明理论预测高度准确。

---

#### 表 2：LongBench v2 上的结果
| $ \mu_{\text{gpu}} $ | $ \mu_{\text{theory}} $ | GAP |
|-----------------------|---------------------------|-----|
| 0.610                 | 0.561                     | 8.03% |

> ✔️ 在真实复杂分布下仍保持良好预测能力，说明建模 **joint distribution $ p(s,o) $** 至关重要。

---

#### 表 3：8-GPU 并行部署结果
| P/D Ratio | $ \mu_{\text{gpu}} $ | $ 8 \times \mu_{\text{theory}} $ | GAP |
|----------|------------------------|----------------------------------|-----|
| 1:1      | 26.710                 | 25.808                          | 3.38% |

> ✔️ 支持横向扩展场景，理论值乘以 GPU 数量即可近似集群吞吐，误差仅 3.38%

---

#### 表 4：8:1 极端 P/D Ratio 下的 trimmed mean 效果
| Estimator | $ \mu_{\text{gpu}} $ | $ \mu_{\text{theory}} $ | GAP |
|----------|------------------------|----------------------------|-----|
| 5% Trimmed | 5.470                | 4.977                      | 9.0% |
| 10% Trimmed| 5.470                | 5.862                      | 7.2% |

> ✔️ 即使在 batch processing time 出现重尾分布时，采用 robust estimator（trimmed mean）仍可获得合理预测。

---

### 📉 动态行为验证
- 当 $ \lambda < \mu $：队列长度有界（如 $ \lambda=3 $ 时上限约 5），系统稳定
- 当 $ \lambda > \mu $：队列长度呈线性增长，系统过载
- 在 $ \lambda = \mu_{\text{gpu}} $ 附近出现典型不稳定系统特征（waiting time CDF 近似线性上升）

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **KV Cache 是决定 LLM 推理稳定性的关键因素之一**，不能仅靠计算建模。
2. 提出的排队论框架能够 **精确预测系统稳定边界**，理论与实测处理率之间的 GAP 普遍低于 10%。
3. 公式 $ \mu = \frac{M}{b \cdot \mathbb{E}[g(s,o)]} $ 可用于指导 **GPU 资源预估**：
   $$
   \text{Required GPUs} \approx \left\lceil \frac{\lambda}{\mu \cdot \rho} \right\rceil,\quad \rho = \text{target utilization (e.g., 90%)}
   $$
4. 模型在 **single-GPU、multi-GPU、stationary/non-stationary、synthetic/real-world** 多种场景下均表现出强健性和泛化能力。
5. 使用 **trimmed mean** 等鲁棒统计方法可提升在重尾处理时间场景下的预测精度。

---

### ⚠️ 方法的局限性
1. **假设 work-conserving 调度**：未考虑某些非抢占式或优先级反转情况。
2. **当前模型适用于 data-parallel 架构**，尚未扩展至：
   - **Tensor Parallelism (TP)**：需测量等效 $ M $ 和 $ b $
   - **Pipeline Parallelism (PP)** 或 **Prefill-Decode Disaggregation**：会改变队列拓扑结构，形成 tandem queues
3. **batch processing time 被简化为常数**：虽然实验证明在高利用率下近似成立，但在极端 P/D 比下仍有波动。
4. **未建模 swapping 到 CPU 的代价**：现实中频繁 swap 会影响性能。

---

### 🔮 未来工作方向
1. 将框架扩展至 **tensor/pipeline parallelism 架构**，建立更通用的集群级稳定性理论。
2. 引入 **dynamic arrival rate estimation**，支持在线 auto-scaling 决策。
3. 结合 **prediction uncertainty**（如输出长度预测不准），构建鲁棒调度策略。
4. 探索 **energy-aware provisioning**，在稳定性基础上优化能耗与成本。
5. 将模型应用于 **multi-tenant serving** 与 **SLA guarantee** 设计。

---

## 总结
> This paper provides a **principled, practical, and empirically validated framework** for analyzing the **stability of LLM inference under KV cache memory constraints**.  
>
> It bridges the gap between **theoretical queueing models** and **real-world GPU serving systems**, offering a powerful tool for **capacity planning, resource provisioning, and system design** — all with **less than 10% prediction error** in diverse settings.

🎯 **一句话总结**：  
本文首次建立了融合 KV Cache 内存限制的 LLM 推理排队模型，给出了严格稳定的充要条件，并在真实环境中验证了其高达 90%+ 的预测准确性，为大规模 LLM 服务部署提供了坚实的理论支撑。

</details>

---

### 4. [CuBridge: An LLM-Based Framework for Understanding and Reconstructing High-Performance Attention Kernels](https://arxiv.org/abs/2605.05023)

**Authors**: Xing Ma, Yangjie Zhou, Wu Sun, Zihan Liu, Jingwen Leng, Yun Lin, Shixuan Sun, Minyi Guo, Jin Song Dong  
**Category**: cs.LG  
**Published**: 2026-05-07  
**Score**: 11.5  
**Type**: new  
**ArXiv ID**: 2605.05023v1  

#### Abstract
Efficient CUDA implementations of attention mechanisms are critical to modern deep learning systems, yet supporting diverse and evolving attention variants remains challenging. Existing frameworks and compilers trade performance for flexibility, while expert-written kernels achieve high efficiency b...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：CuBridge: An LLM-Based Framework for Understanding and Reconstructing High-Performance Attention Kernels**

---

## **1. 论文的主要贡献和创新点**

### **解决的问题**
现代深度学习系统中，**Attention 机制**是性能的关键瓶颈，尤其在大模型（如 LLM）中。随着模型架构演进，出现了大量定制化的 **attention variants**（如 PrefixLM、Sliding Window、ReLU Attention 等），这些变体在算法语义上有所修改（如 masking、normalization、score computation），但高效实现它们需要复杂的 **CUDA kernel 优化**。

现有方法面临两难：
- **通用框架（如 PyTorch）**：灵活但性能差，依赖多 kernel 调用和冗余内存访问。
- **专家库（如 FlashAttention）**：高性能但难以扩展，每个新 variant 都需手动重写。
- **LLM 生成 kernel**：虽有潜力，但在复杂算子（如 attention）上存在 **correctness 不稳定** 和 **performance 落后** 的问题。

### **提出的新方法**
本文提出 **CuBridge**，一个基于 **LLM 的框架**，用于理解并重构高性能 attention kernel，其核心思想是：
> **不从零生成 CUDA 代码，而是以专家编写的高性能 kernel 为参考，通过“lift-transfer-lower”流程进行语义适配**。

#### **核心创新点**
1. **提出 lift-transfer-lower 工作流**：
   - **Lift**：将源 CUDA kernel 提升为可执行的中间表示 **CuIR**，抽象低层语法，显式表达执行编排（execution orchestration）。
   - **Transfer**：在 CuIR 层面对目标语义进行转换，由 LLM 生成目标 CuIR。
   - **Lower**：通过差异分析（IR differencing）和参考引导重建（reference-guided reconstruction），将目标 CuIR 降级回优化的 CUDA 代码。

2. **设计 CuIR（CUDA Intermediate Representation）**：
   - 一种 **Pythonic、可执行** 的中间语言，基于自定义 primitives 显式建模：
     - **Memory**：`alloc`, `copy_async`
     - **Compute**：`gemm_async`, `gemm`
     - **Sync**：`barrier.wait`, `barrier.arrive`
     - **Control**：`bind`, `commit`
   - 保留性能关键的执行结构（如异步流水线、warp specialization），同时屏蔽底层细节。

3. **支持中间验证（Intermediate Verification）**：
   - CuIR 可通过专用执行器运行，确保语义正确性，避免直接操作 CUDA 代码导致的错误。

---

## **2. 核心实验方法和设置**

### **实验设置**
- **硬件平台**：NVIDIA A100（Ampere）、H100（Hopper）
- **LLM 后端**：GPT-5、Claude-3.5-Sonnet、DeepSeek-V3、Qwen-3-235B、Qwen-3-32B
- **测试 attention variants**（共 8 种，均未被标准 FlashAttention 支持）：
  - PrefixLM, Global Sliding Window, Share Question Mask, Causal Blockwise Mask
  - Relative Position, ReLU Attention, Sigmoid Attention
  - 复合变体（PrefixLM + Softcap + Sigmoid）

### **评估指标**
- **Correctness**：输出数值与 PyTorch 参考实现误差 < 1e-2（fp16）
- **Performance**：吞吐量（TFLOPS）
- **Speedup**：相对于基线的加速比

### **基线方法对比**
| 基线 | 类型 | 描述 |
|------|------|------|
| **PyTorch** | 通用框架 | 使用原生算子组合实现，无融合优化 |
| **FlexAttention** | 编译器框架 | 模板化编译，支持有限定制 |
| **Qimeng-Attention** | LLM-based 方法 | 基于 LLM 直接生成 CUDA kernel |
| **FlashInfer** | 专家手工调优库 | 手动优化的高性能推理引擎 |

### **测试模型配置**
基于真实 LLM 架构：
- **Llama2-7B**（MHA, 32/32/128）
- **Qwen2.5-72B**（GQA, 64/8/128）
- **Llama3.1-405B**（GQA, 128/8/128）
- 序列长度：1k, 2k, 4k, 8k，batch size 动态调整保持总 token 数恒定（16k）

---

## **3. 主要实验结果和性能指标**

### **关键性能数据（H100 平台，平均 TFLOPS）**
| 方法 | 平均 TFLOPS | 相对 PyTorch 加速 | 相对 FlexAttention 加速 | 相对 Qimeng-Attention 加速 |
|------|------------|------------------|------------------------|----------------------------|
| **PyTorch** | ~15–30 | 1.00× | — | — |
| **FlexAttention** | ~100–150 | ~6–10× | 1.00× | — |
| **Qimeng-Attention** | ~50–150 | ~3–8× | ~0.8–1.2× | 1.00× |
| **CuBridge** | **~200–600** | **19.82×** | **1.62×** | **4.35×** |

> 数据来源：Figure 6 与 Table 5

### **详细对比结果**
- **相比 PyTorch**：
  - 平均加速 **16.03×**（A100 上 12.69×，H100 上 19.82×）
  - 原因：避免多 kernel 启动、减少全局内存访问、实现完全融合。

- **相比 FlexAttention**：
  - 平均加速 **1.39×**（A100 上 1.18×，H100 上 1.62×）
  - 在 H100 上优势更明显，说明更好利用了新硬件特性（如 TMA、WG-MMA）。

- **相比 Qimeng-Attention（LLM-based）**：
  - 平均加速 **3.33×**（A100 上 2.54×，H100 上 4.35×）
  - 对复杂变体（如 Share Question Mask、Combo）加速可达 **11.47×**（H100）

- **相比 FlashInfer（专家库）**：
  - 在其原生支持的 variant 上性能相当（**1.07×**）
  - 在非原生 variant 上平均加速 **3.49×**（最高达 5.59×）

### **消融实验结果（Ablation Study）**
在 H100 上对 96 个测试用例进行对比：

| 方法 | Pass@1 | Pass@5 | 归一化速度（Vanilla GPT-5 = 1.00×） |
|------|--------|--------|-------------------------------|
| **Vanilla GPT-5** | 0.21 | 0.38 | 1.00× |
| **GPT-5 + ReAct** | 0.41 | 0.58 | 1.23× |
| **CuBridge** | **0.70** | **1.00** | **4.19×** |

> 结论：**CuIR 的引入显著提升了 correctness 和 performance**，证明了结构化 IR 的必要性。

---

## **4. 关键结论和发现**

### **主要发现**
1. **直接使用 LLM 修改 CUDA 代码不可靠**：
   - 专家 kernel 包含复杂异步逻辑（如 `wgmma.commit_group`），LLM 容易出错（见 Figure 2 错误案例）。

2. **CuIR 是成功的关键**：
   - 将执行编排显式化，使 LLM 能在更高层次进行语义推理。
   - 支持中间验证，确保 correctness。
   - 保留原始 kernel 的高性能结构（如 warp specialization、pipeline overlap）。

3. **性能提升源于 schedule-level 优化**：
   - CuBridge 能针对不同 variant 进行 **loop splitting**（如 PrefixLM 中仅对边界块做 mask 检查），而 FlexAttention 等固定模板无法做到。

4. **方法对 LLM 后端鲁棒**：
   - 使用 GPT-5、Claude、DeepSeek-V3 等不同 LLM，性能差异 < 5%
   - 但小模型（如 Qwen-3-32B）无法生成有效 kernel，表明存在 **能力阈值**

### **局限性**
1. **依赖高质量专家 kernel 作为源参考**：
   - 若目标平台（如 FPGA）缺乏优化实现，则无法应用。
2. **当前评估集中在 attention 算子**：
   - 虽在附录中展示了 GEMM+ReduceSum 的扩展性（Table 7），但仍需更多领域验证。
3. **未覆盖所有硬件平台**：
   - 当前仅在 NVIDIA GPU 上验证，对 AMD 或国产芯片支持未知。

### **未来工作方向**
- 扩展到其他高性能算子（如 conv、sparse matmul）
- 探索跨硬件平台的迁移能力
- 结合训练-based LLM 优化（如 CUDA-L1）进一步提升生成质量
- 支持自动探索更优的 execution orchestration 而不仅是复用

---

> **总结**：  
> **CuBridge** 通过 **lift-transfer-lower** 流程和 **CuIR** 中间表示，成功实现了 **高正确性、高性能** 的 attention kernel 自动生成，在多个维度上显著超越现有方法，为 LLM 辅助系统优化提供了新范式。

</details>

---

### 5. [FASQ: Flexible Accelerated Subspace Quantization for Calibration-Free LLM Compression](https://arxiv.org/abs/2605.04084)

**Authors**: Ye Qiao, Yian Wang, Zhiheng Chen, Hyoukjun Kwon, Sitao Huang  
**Category**: cs.LG  
**Published**: 2026-05-07  
**Score**: 11.0  
**Type**: new  
**ArXiv ID**: 2605.04084v1  

#### Abstract
Compressing large language models (LLMs) for deployment on commodity GPUs remains challenging: conventional scalar quantization is limited to fixed bit-widths (e.g., 8/4/3-bit), offers only a few discrete compression points, and typically requires calibration data. We present FASQ (Flexible Accelera...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# FASQ: Flexible Accelerated Subspace Quantization for Calibration-Free LLM Compression 论文总结

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
当前大型语言模型（LLMs）在消费级GPU上部署面临三大挑战：
- **固定比特宽度限制**：传统标量量化（如INT8/4/3-bit）仅提供离散压缩率，无法实现细粒度的大小-质量权衡。
- **依赖校准数据**：主流方法（如GPTQ、AWQ、SmoothQuant）需要代表性校准数据进行参数调整，对专有或领域特定模型不友好。
- **推理开销高**：标量量化需在推理时显式反量化为FP16权重，导致额外内存带宽消耗和延迟，尤其在非标准比特下缺乏优化内核支持。

### 提出了什么新方法或新思路
提出 **FASQ（Flexible Accelerated Subspace Quantization）** ——一种无需校准的后训练压缩框架，基于 **Product Quantization（PQ）** 技术：
- 将权重矩阵划分为多个子向量子空间（subspaces），每个子空间通过k-means聚类生成共享码本（codebook）。
- 权重被表示为低维索引表（`uint8` indices）和紧凑码本（FP16 centroids），推理直接在压缩表示上进行，避免反量化。
- 通过调节两个超参数控制压缩程度：
  - **Sub-vector size (SZss)**：子向量长度
  - **Codebook cardinality (Ks)**：每子空间聚类中心数

该设计暴露了一个**连续的设计空间**，覆盖FP16模型大小的27%-49%，填补了固定比特方案之间的空白。

### 相比现有方法的优势
| 维度 | FASQ优势 |
|------|---------|
| **灵活性** | 支持连续压缩率（非仅3/4/8-bit），可精细调节大小与精度平衡 |
| **免校准** | 仅依赖权重分布上的k-means，无需任何外部校准数据 |
| **高效推理** | 设计专用CUDA内核，实现重建自由（reconstruction-free）推理，显著降低内存流量 |
| **解码加速** | 在RTX 3090上，有效4-bit时达45.2 tok/s，**超越FP16原生性能（43.9 tok/s）**，是唯一能加速decode的压缩方法 |

---

## 2. 核心实验方法和设置

### 使用了哪些数据集
- **零样本任务评估**（Zero-shot Accuracy）：
  - ARC-easy / ARC-challenge
  - HellaSwag
  - PIQA
  - WinoGrande
- **困惑度测试集**：
  - WikiText-2 test set

### 实验设置和评估指标
| 类别 | 设置说明 |
|------|--------|
| **模型** | 主要测试：Meta-Llama-3-8B<br>泛化验证：Qwen3-8B, Qwen3.5-9B-Base<br>可扩展性分析：LLaMA-2 7B/13B |
| **硬件平台** | NVIDIA RTX 3090 GPU |
| **评估指标** | 
| - 压缩率（Size%）：压缩后权重存储大小占FP16原始大小的比例 |
| - 零样本平均准确率（AvgT） |
| - 困惑度（PPL↓） |
| - 端到端推理吞吐（tok/s） |
| - 内存占用（MB） |
| **FASQ配置命名** | `SZss-Ks`，例如`2-256`表示SZss=2, Ks=256 |

### 基线方法对比
| 方法 | 是否需校准 | 特点 |
|------|------------|------|
| **GPTQ** | ✗ | Hessian引导的INT4/3量化 |
| **AWQ** | ✗ | 激活感知权重缩放 |
| **SmoothQuant** | ✗ | 联合W-A量化（W8A8/W6A6/W4A4） |
| **QuIP** | ✗ | 利用不可相干性预处理 |
| **RTN** | ✓ | Round-To-Nearest，无校准基准 |

所有基线均使用官方实现及对应CUDA内核。

---

## 3. 主要实验结果和性能指标

### 关键性能数据

#### 📊 模型压缩与精度表现（Meta-Llama-3-8B）
| 方法 | Size% | AvgT | PPL |
|------|-------|------|-----|
| FP16 | 100.0% | 68.8 | 6.14 |
| **FASQ 2-1024** | **49.0%** | **68.2** | 6.3 |
| SmoothQuant W8A8 | 56.6% | 68.2 | 6.3 |
| **FASQ 2-512** | **41.9%** | **68.0** | 6.48 |
| **FASQ 2-256** | **37.0%** | **67.8** | 6.81 |
| GPTQ-4 | 35.7% | 67.3 | 6.5 |
| AWQ-4 | 35.7% | 67.7 | 6.6 |
| **FASQ 2-128** | **33.2%** | **66.0** | 7.57 |
| AWQ-3 | 30.2% | 64.4 | 8.2 |

> ✅ **关键发现**：
> - FASQ在**更小体积下达到相同甚至更高精度**（如49% vs 56.6% 达成68.2准确率）
> - 在4-bit区域全面优于GPTQ/AWQ，在3-bit区域显著领先
> - 支持低于3-bit的有效压缩（如4-1024达31.1% size, AvgT=66.4），这是标量方法无法触及的区域

#### ⚙️ 推理性能（RTX 3090, Prompt/Gen=128）
| 方法 | Mem (MB) | Decode (tok/s) | Speedup vs FP16 |
|------|----------|----------------|------------------|
| FP16 (Tensor Core) | 15,317 | 43.9 | 1.00× |
| AWQ (4-bit) | 5,463 | 28.1 | 0.64× |
| GPTQ (4-bit) | 6,558 | 20.5 | 0.47× |
| SmoothQuant W8A8 | 8,663 | 16.4 | 0.37× |
| RTN (4-bit) | 8,663 | 10.4 | 0.24× |
| **FASQ (eff. 4-bit)** | **5,975** | **45.2** | **1.03×** ✅ |
| **FASQ (eff. 3-bit)** | **5,482** | **51.8** | **1.18×** ✅ |

> 🔥 **突破性结果**：
> - **首次实现压缩模型解码速度超过FP16原生性能**
> - 内存减少2.56–2.80倍的同时提升吞吐
> - 相比AWQ提速1.6–1.8×，相比GPTQ提速2.2–2.5×，相比RTN提速4.3–5.0×

### 消融实验结果（Ablation Study）

#### 内核优化效果（4096×4096层，RTX 3090）
| 优化步骤 | GEMV Latency (μs) | 提速比 |
|--------|--------------------|--------|
| cuBLAS FP16 | 45 | 1.0× |
| Subspace-stationary LUT | 142 | ↓ |
| + Output-stationary + half2 | 94 | 1.5× |
| + LUT-free + Split-K | **32** | **2.9×↑** |

> ✅ **关键洞察**：
> - **LUT-free GEMV** 和 **Split-K并行** 是实现高性能的关键
> - 内存访问从32MB（FP16权重）降至8MB（索引表），实现4×内存流量下降
> - 无共享内存、无同步屏障设计极大提升occupancy

#### 参数敏感性分析
- **Codebook size (Ks)**：从16→256，GEMV延迟仅从25.3→37.4 μs（+48%），仍快于FP16（45.5 μs），表明质量可自由调优
- **Sub-vector size (SZss)**：SZss=2最优（启用half2向量化），SZss=1性能暴跌至134.7 μs
- **序列长度影响**：Split-K在短序列（L=32）带来4.5×加速，长序列自动关闭不影响效率

---

## 4. 关键结论和发现

### 主要发现
1. **FASQ实现了真正灵活且高效的LLM压缩路径**：
   - 连续压缩空间（27%-49% FP16 size）填补了固定比特间的空缺
   - 免校准特性使其适用于所有闭源或垂直领域模型
2. **重构自由推理架构打破“压缩必慢”魔咒**：
   - 通过定制CUDA内核，FASQ成为**首个在decode阶段超越FP16吞吐的压缩方法**
   - 解码延迟随压缩加深而改善（更高压缩 → 更少内存读取）
3. **产品量化适合现代Transformer结构**：
   - 线性层主导参数量，适合子空间分解
   - 码本开销小（<1%层大小），可忽略不计

### 方法的局限性
- **Prefill阶段较慢**：当前GEMM内核无法利用Tensor Core，prefill延迟远高于cuBLAS（~935ms vs 41ms）
- 对极低比特（<2-bit）支持有限，尚未探索极端低位宽场景
- 当前内核未适配多卡或分布式场景

### 未来工作方向
1. **加速Prefill阶段**：
   - 开发流水线式重建内核，在tile级别恢复FP16并与Tensor Core GEMM协同
   - 探索Triton-based codegen，针对PQ访问模式进行tiling优化
2. **进一步提升压缩效率**：
   - 引入逐层参数分配（per-layer SZss/Ks选择）
   - 后训练码本微调（post-training codebook finetuning）
3. **扩展至其他模态与架构**：
   - 视觉Transformer、MoE模型等更大规模结构
   - 结合稀疏化形成混合压缩策略

--- 

> ✅ **总结一句话**：  
> **FASQ是首个实现免校准、连续压缩、且解码速度超越FP16的LLM压缩框架，重新定义了“压缩即牺牲性能”的传统认知。**

</details>

---

### 6. [Efficient Handwriting-Based Alzheimer,s Disease Diagnosis Using a Low-Rank Mixture of Experts Deep Learning Framework](https://arxiv.org/abs/2605.04079)

**Authors**: Wu Wang, Yuang Cheng, Fouzi Harrou, Ying Sun  
**Category**: cs.LG  
**Published**: 2026-05-07  
**Score**: 10.5  
**Type**: new  
**ArXiv ID**: 2605.04079v1  

#### Abstract
Early and reliable detection of Alzheimer's disease (AD) is crucial for timely clinical intervention and improved patient management. It also supports the evaluation of emerging therapeutic strategies. In this paper, we propose a Low-Rank Mixture of Experts (LoRA-MoE) deep learning framework for Alz...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文核心结论与实验结果总结

## 1. 论文的主要贡献和创新点

### 解决的问题
阿尔茨海默病（Alzheimer’s Disease, AD）的早期诊断对于临床干预和患者管理至关重要。然而，传统诊断方法依赖于昂贵且侵入性的手段（如神经影像学、脑脊液生物标志物），难以实现大规模筛查。此外，现有的深度学习模型在处理高维、异质性强的手写信号时存在以下问题：
- 参数量大，计算成本高；
- 易过拟合，尤其在小样本临床数据上；
- 缺乏对不同认知-运动模式的有效建模机制。

因此，亟需一种**高效、可扩展、参数少且鲁棒性强**的数字生物标志物分析框架。

### 提出的新方法与新思路
本文提出了一种名为 **Low-Rank Mixture of Experts (LoRA-MoE)** 的深度学习架构，用于基于手写信号的AD诊断。其核心思想是结合两种前沿技术：
- **Mixture of Experts (MoE)**：通过多个“专家”子网络分别学习不同的输入模式，并由一个可训练的**gating network**动态路由输入至最相关的专家。
- **Low-Rank Adaptation (LoRA)**：引入低秩矩阵分解来替代全连接层的权重更新，显著减少参数数量。

具体设计如下：
- 所有专家共享一个**shared base network**进行通用特征提取；
- 每个专家配备轻量级的**LoRA adapter**，仅通过低秩矩阵 $ \Delta W = A B $ 实现任务特定的微调；
- 推理时采用 **Top-K routing**（实验中多为 Top-1），激活少数专家以提升效率。

### 相比现有方法的优势
| 维度 | 优势说明 |
|------|--------|
| **参数效率** | 相比标准 MoE，总参数量大幅降低（例如文中示例减少约77.3%）；相比全微调更节省资源。 |
| **训练稳定性** | LoRA 初始化策略（$ B=0 $）确保初始阶段行为由共享主干决定，避免专家早期随机发散。 |
| **泛化能力** | 共享表示促进知识迁移，减轻过拟合；专家专业化增强对复杂模式的捕捉能力。 |
| **推理效率** | 仅激活少量专家即可完成预测，适合部署于边缘设备或便携式健康平台。 |

---

## 2. 核心实验方法和设置

### 数据集
使用公开手写数据集 **DARWIN (Diagnosis AlzheimeR WIth haNdwriting)**：
- 包含 **174 名受试者**：89 名 AD 患者，85 名健康对照（HC）；
- 收集方式：使用压感数位板记录书写过程中的笔尖坐标（200Hz采样率）、压力、空中/纸上运动等；
- 任务类型：共 **25 种手写任务**，涵盖图形绘制、抄写、记忆复述等，全面反映认知-运动功能；
- 特征工程：从原始信号中提取 **450 维手工特征**，分为三类：
  - **Time-related features**（如 total time, air_time）
  - **Movement-related features**（如 mean_speed, gmrt_tremor）
  - **Pressure-related features**（如 pressure_mean, pressure_var）

### 实验设置与评估指标
#### 模型配置
- **Hidden dimension**: 在 [50, 400] 范围内变化；
- **Number of experts**: 设置为 3–10；
- **LoRA rank (r)**: 测试范围为 1–8；
- **Routing strategy**: 主要使用 Top-1；
- **Stacking ensemble**: 引入 **StackMean** 和 **StackMax** 策略聚合多个模型输出，提高鲁棒性。

#### 评估指标
所有任务平均后报告以下指标：
- **Accuracy**
- **Sensitivity (Recall for AD class)**
- **Specificity (Recall for HC class)**
- **Precision**
- **F1-Score**
- **AUC**
- **Training/Inference Time**

#### 基线方法对比
| 方法 | 描述 |
|------|------|
| **MLP** | 多层感知机，作为基础非MoE模型；结构为两层FC + ReLU |
| **Standard MoE** | 传统MoE架构，每个专家为独立完整网络，无参数共享 |
| **LoRA-MoE (Proposed)** | 本文提出的共享主干 + LoRA适配器架构 |

---

## 3. 主要实验结果和性能指标

### 关键性能数据
在最优配置下（hidden dim=300, num_experts=5, LoRA rank=2），LoRA-MoE 表现出卓越性能：

| 模型 | Accuracy | Sensitivity | Specificity | F1-Score | AUC |
|------|----------|-------------|--------------|-----------|-----|
| **LoRA-MoE** | **87.14%** | **88.33%** | **85.88%** | **87.11%** | ~0.94 |
| Standard MoE | 86.29% | 84.72% | 87.94% | 86.24% | 0.9271 |
| MLP | 84.86% | 83.33% | 86.47% | 84.74% | 0.9369 |

> 注：结合 **StackMean/StackMax** 后，AUC 可进一步提升至接近 **0.94**。

### 与基线方法的对比结果
- **优于 Standard MoE**：
  - 尽管 MoE 有一定性能优势，但参数量大、训练不稳定；
  - LoRA-MoE 在更低参数量下达到更高准确率，且训练时间更短。
- **显著优于 MLP**：
  - MLP 缺乏专家分工机制，在建模异质性手写模式时受限；
  - LoRA-MoE 利用专家专业化，在敏感性和F1分数上有明显领先。

### 消融实验结果
#### a) 隐藏维度影响（Hidden Dimension）
- 最优性能出现在中间值（如300），过大反而导致轻微下降；
- LoRA-MoE 对维度变化更稳健，而 MoE 性能波动较大。

#### b) 专家数量影响（Number of Experts）
- LoRA-MoE 在 **5个专家** 时达到峰值性能（Accuracy=87.14%）；
- 超过该数目后性能饱和甚至下降，表明过多专家会引入冗余；
- Standard MoE 随专家增加性能下降更快，显示其优化难度更高。

#### c) LoRA Rank 影响
- **Rank=2** 即可取得最佳性能（Accuracy=85.14%）；
- 更高的 rank 并未带来增益，反而增加训练开销；
- 结论：**低秩足以捕获专家特异性调整**，验证了参数高效的合理性。

#### d) 模型深度影响（Multi-layer）
测试了 5 层和 8 层深层结构：
- 增加深度并未带来一致性能提升；
- LoRA-MoE 和 MoE 的训练时间随层数急剧上升；
- **浅层结构已足够有效**，深层模型引入不必要的复杂性。

#### e) 独立任务预测 vs 投票集成
将每项手写任务视为独立分类任务并采用硬投票融合：
- 所有模型性能均低于主体实验（因信息分散）；
- 但 **MLP-25 ensemble 达到最高 Accuracy (87.43%)**；
- LoRA-MoE ensemble 排名第二（86.86%），仍保持高特异性（90.59%）；
- 表明：**subject-level aggregation 更可靠**，但 task-level ensemble 仍具潜力。

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **LoRA-MoE 是一种高效且强大的AD诊断框架**：
   - 在 DARWIN 数据集上实现了高达 **87.14% 的准确率**；
   - 优于标准 MoE 和 MLP，同时激活参数更少，适合实际应用。

2. ✅ **专家专业化 + 参数高效设计相辅相成**：
   - 共享主干稳定训练，LoRA adapter 实现灵活定制；
   - 仅需极低秩（r=2）即可获得优异性能。

3. ✅ **适度模型规模最优**：
   - 中等隐藏维度（300）、适量专家（5）、低秩（2）构成最佳组合；
   - 过大的模型容量不仅不增益，还增加计算负担。

4. ✅ **stacking ensemble 提升鲁棒性**：
   - StackMean / StackMax 显著改善 AUC 和稳定性；
   - 特别适用于缓解个体模型偏差。

5. ✅ **手写信号是有效的数字生物标志物**：
   - 能够捕捉早期认知-运动退化迹象；
   - 具备非侵入性、低成本、可远程实施的优点。

### 方法的局限性
- **数据集规模有限**：DARWIN 仅含 174 名受试者，限制了模型泛化能力；
- **任务间差异大**：某些任务判别力弱，影响单任务预测可靠性；
- **缺乏跨中心验证**：尚未在其他独立队列中验证；
- **解释性不足**：虽然性能好，但“哪个专家对应哪种病理模式”尚难解读。

### 未来工作方向
1. **扩展至多模态融合**：
   - 整合 speech、drawing dynamics、eye-tracking 等多种数字生物标志物；
   - 构建统一的 LoRA-MoE 多任务诊断系统。

2. **自适应路由机制**：
   - 设计动态选择专家数量或路由路径的方法；
   - 根据输入难度自动调节计算量。

3. **自动化 rank selection**：
   - 开发算法根据任务复杂度自适应分配 LoRA rank；
   - 实现真正的“按需扩展”。

4. **更大规模临床研究**：
   - 在多中心、多样本群体中验证模型有效性；
   - 推动向真实世界医疗场景落地。

5. **探索可解释性机制**：
   - 分析各专家关注的手写特征子集；
   - 提供辅助医生决策的可视化支持。

---

> **总结一句话**：  
> 本文提出的 **LoRA-MoE** 框架通过将 **Mixture of Experts** 与 **Low-Rank Adaptation** 巧妙结合，在保证高性能的同时极大提升了参数效率和训练稳定性，为基于手写的阿尔茨海默病早期筛查提供了一个极具前景的解决方案。

</details>

---

### 7. [CCL-D: A High-Precision Diagnostic System for Slow and Hang Anomalies in Large-Scale Model Training](https://arxiv.org/abs/2605.04478)

**Authors**: Yida Gu, Fakang Wang, Jianhao Fu, Zhenhang Sun, Qianyu Zhang, Hairui Zhao, Xingchen Liu, Yang Tian, Wenjing Huang, Zedong Liu, Yifan Chen, Jinwu Yang, Yueyuan Zhou, Qian Zhao, Haoxu Li, Tao Wang, Feng Yu, Zhan Wang, Guangming Tan, Dingwen Tao  
**Category**: cs.DC  
**Published**: 2026-05-07  
**Score**: 10.0  
**Type**: new  
**ArXiv ID**: 2605.04478v1  

#### Abstract
As training scales grow, collective communication libraries (CCL) increasingly face anomalies arising from complex interactions among hardware, software, and environmental factors. These anomalies typically manifest as slow/hang communication, the most frequent and time-consuming category to diagnos...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：CCL-D: A High-Precision Diagnostic System for Slow and Hang Anomalies in Large-Scale Model Training

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
在大规模模型训练中，**Collective Communication Library (CCL)** 面临由硬件、软件和环境因素复杂交互引发的 **slow/hang anomalies（通信缓慢或挂起异常）**。这类问题是训练中断中最频繁且诊断耗时最长的一类，传统方法如日志分析、堆栈追踪或压力测试往往需要数小时甚至数天才能定位根因，严重影响训练效率。

现有诊断系统存在两大瓶颈：
- **诊断精度低**：无法精确定位到具体的故障 GPU rank。
- **诊断开销高**：依赖离线分析或专家介入，难以实现实时检测。

### 提出了什么新方法或新思路
作者提出 **CCL-D**，一个面向大规模模型训练中 slow/hang 异常的高精度诊断系统。其核心思想是：
- 在 CCL 层面引入细粒度运行时探针（rank-level real-time probe），结合智能决策分析器（intelligent decision analyzer）。
- 利用轻量级分布式追踪框架监控通信流量，并基于 Send/Recv 原语设计跨层指标（cross-layer metrics）进行异常建模。
- 实现对故障 GPU rank 的分钟级自动检测与精准定位。

### 相比现有方法的优势
| 维度 | CCL-D 的优势 |
|------|-------------|
| **精度** | 支持六类 slow/hang 异常分类（H1-H3, S1-S3），可精确定位至具体 rank；而如 RAS、Greyhound 等仅支持部分场景。 |
| **效率** | 检测延迟控制在 5 分钟（hang）和 1 分钟（slow），定位时间 <150ms，远优于 bisect 或 stack analysis 的小时级耗时。 |
| **通用性** | 基于 Send/Recv 的指标设计独立于底层协议（Ring/Tree）、拓扑结构和 CCL 实现（NCCL/R-CCL 均适用）。 |
| **低开销** | 运行时开销 <1%，不影响正常训练流程；采用 host-driven 测量避免占用 GPU 资源。 |

---

## 2. 核心实验方法和设置

### 使用了哪些数据集
论文未直接使用传统“数据集”进行训练任务，而是通过以下方式构建实验负载：
- **训练模型**：BaiLing-5B, Llama2-7B, Llama3.1-8B, BaiLing-80B
- **训练策略**：FSDP 和 3D 并行
- **数据来源**：Alpaca 和 Fineweb-edu 数据集用于驱动训练任务

### 实验设置和评估指标
#### 平台配置
- 单节点：2 × Intel 8469C CPU, 800GB RAM, 8 × Nvidia H20 GPU (96GB HBM3), NVLink 互联
- 网络：4 × ConnectX-7 400G NICs
- 软件栈：CUDA 12.2, NCCL 2.24.3, PyTorch 2.4.0, Megatron 0.9.0
- 规模范围：从 16 到 **4,000 GPU** 集群验证可扩展性

#### 评估指标
| 类别 | 指标 |
|------|------|
| **诊断准确性** | 是否覆盖所有六类异常（Not-Entered-Hang, Inconsistent-Hang, Hardware-Fault, Comp-Slow, Comm-Slow, Mixed-Slow） |
| **诊断效率** | 检测延迟（Detection Latency）、定位延迟（Location Latency） |
| **系统开销** | CPU 使用率、内存占用、通信操作额外耗时、训练步长时间影响 |
| **实际部署效果** | 生产环境中一个月内捕获的异常案例数量及平均诊断时间对比 |

#### 参数设定
- Hang 检测阈值：5 分钟（考虑 checkpoint 等长周期操作）
- Slow 检测窗口：1 分钟
- Slow 判断阈值 $ \theta_{\text{slow}} $：统计学习得出，通常接近 3

### 基线方法对比
选取五种代表性基线进行比较：
| 方法 | 类型 | 特点 |
|------|------|------|
| **Bisection (DL-Rover)** | 离线二分法 | 依赖 NCCL-tests 压力测试，需手动触发，效率极低 |
| **Stack Analysis (XPUTimer + ParaStack)** | 堆栈采样分析 | 依赖函数调用栈，难以捕捉慢速通信或间歇性问题 |
| **NCCL RAS** | CCL 运行时状态监控 | 只记录主机侧操作计数，无法处理 slow 异常 |
| **Greyhound** | 通信迭代监控 | 可检测 comp-slow，但不支持 hang，且需暂停训练 |
| **C4D** | 细粒度时序分析 | 包含接收等待时间等指标，但仍缺乏 kernel-level 可见性 |

---

## 3. 主要实验结果和性能指标

### 关键性能数据
| 指标 | CCL-D 表现 |
|------|-----------|
| **诊断覆盖率** | 覆盖全部六类 slow/hang 异常（H1-H3, S1-S3） |
| **检测延迟** | Hang: ≤5min, Slow: ≤1min（自动化） |
| **定位延迟** | <150ms（毫秒级） |
| **定位准确率** | 在 4,000 GPU 集群上实现近 100% 故障 rank 定位 |
| **运行时开销** | 内存：1184 Bytes/rank；CPU：<0.3%/node；通信延迟增加 <0.45% |
| **生产环境表现** | 部署一年后，在 4,000 GPU 集群上将平均诊断时间从 **74 小时降至 6 分钟** |

### 与基线方法的对比结果（来自 Table 1 & 2）

| 方法 | Hang Detection | Slow Detection | Location Time | 自动化 | 支持 Mixed-Slow |
|------|----------------|----------------|---------------|--------|------------------|
| Bisection | ✅（>30min） | ❌ | >1h | ❌（人工） | ❌ |
| Stack Analysis | ✅（>30min） | ❌ | ~5min | ⚠️（半自动） | ❌ |
| NCCL RAS | ✅（>30min） | ❌ | 10ms | ✅ | ❌ |
| Greyhound | ❌ | ✅（1min） | 1.43s | ✅+❌（需停训） | ❌ |
| C4D | ✅（5min） | ✅（1min） | ~140ms | ✅ | ❌ |
| **CCL-D** | ✅（5min） | ✅（1min） | **~146ms** | ✅ | ✅ |

> ✅ 表示支持，❌ 表示不支持或无效，⚠️ 表示有限支持

### 消融实验结果（隐含在分析中）
虽然没有显式的消融表，但文中多处体现了关键组件的有效性验证：
- **Trace ID + Probing Frame 设计**：相比 naive centralized tracing 方案，延迟降低约 **188×**
- **host-driven 测量机制**：避免 GPU 干扰，保持训练稳定性
- **SendRate/RecvRate 指标有效性**：能有效区分 comp-slow 与 comm-slow，解决了传统 Duration Time 因 NTP drift 不准的问题
- **决策树算法复杂度为 O(N)**：适用于数千 GPU 规模，具备良好可扩展性

---

## 4. 关键结论和发现

### 论文的主要发现
1. **slow/hang 异常具有明确的行为模式**：可通过 Send/Recv 的 count 与 rate 差异建模，无需依赖外部工具或专家经验。
2. **kernel-level 可见性至关重要**：仅靠 host-level 日志或 operation count 无法识别大多数 slow 异常，必须深入通信 kernel 内部。
3. **轻量级、去中心化的 tracing 是可行路径**：通过 Trace ID 与 Probing Frame 实现高效通信标识与测量，兼顾精度与性能。
4. **CCL-D 可实现近实时闭环诊断**：在 4,000 GPU 规模下仍能在 6 分钟内完成检测与定位，显著提升运维效率。

### 方法的局限性
- **依赖 CCL 修改权限**：需要在 CCL 中植入探针逻辑，可能限制在某些封闭系统的应用。
- **对非通信类异常无能为力**：如纯计算错误、梯度爆炸等问题不在本系统关注范围内。
- **当前仅聚焦于 collective communication**：未涵盖 point-to-point 或异步通信场景。
- **root cause 推理仍为间接推断**：虽能定位 fault rank，但最终物理原因（如 GPU memory error）仍需结合其他硬件诊断工具确认。

### 未来工作方向
- 扩展支持更多通信原语（如 AlltoAll, Send/Recv）
- 结合硬件 telemetry（如 NVSMI, ROCm SMI）实现更深层次的根因归因
- 探索与 repair/restart 机制联动，构建端到端自愈系统（self-healing training）
- 支持跨框架统一接口（兼容 PyTorch, TensorFlow, JAX）

--- 

> ✅ **总结一句话**：  
> CCL-D 是首个利用 **kernel-level Send/Recv 行为差异** 实现 **分钟级、高精度、低开销** 的大规模训练 slow/hang 异常诊断系统，在真实 4,000 GPU 集群中验证有效，推动了分布式训练系统的可观测性边界。

</details>

---

### 8. [OSAQ: Outlier Self-Absorption for Accurate Low-bit LLM Quantization](https://arxiv.org/abs/2605.04738)

**Authors**: Zhikai Li, Zhen Dong, Xuewen Liu, Jing Zhang, Qingyi Gu  
**Category**: cs.LG  
**Published**: 2026-05-07  
**Score**: 10.0  
**Type**: new  
**ArXiv ID**: 2605.04738v1  

#### Abstract
Large Language Models (LLMs) have demonstrated remarkable capabilities. However, their massive parameter scale leads to significant resource consumption and latency during inference. Post-training weight-only quantization offers a promising solution by reducing model size and accelerating token gene...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# OSAQ: Outlier Self-Absorption for Accurate Low-bit LLM Quantization 论文总结

---

## 1. 论文的主要贡献和创新点

### 解决的问题
大型语言模型（LLMs）在推理时面临巨大的内存消耗和延迟问题，**post-training weight-only quantization** 是一种有效的压缩方案。然而，LLM 权重中普遍存在**系统性 outlier（异常值）**，这些大数值权重显著影响低比特（如 2-bit 或 3-bit）量化精度，导致性能严重下降。

现有方法（如 GPTQ、AWQ、QuIP）主要依赖**乘法变换**（scaling 和 rotation），通过层间等效变换来缓解 outliers，但其效果有限，尤其在极低位宽下表现不佳。

### 提出的新方法与新思路
本文提出 **Outlier Self-Absorption Quantization (OSAQ)**，引入一种全新的 **additive transformation（加法变换）** 范式用于 outlier 抑制。

- **核心思想**：利用任务损失函数关于某层权重的 Hessian 矩阵具有**低秩一致性**（low-rank consistency）这一性质——即在不同输入下，Hessian 存在一个稳定的 null space（零空间），其中曲率趋近于零。
- 在该 null space 内进行线性组合，构造一个加法扰动 $\Delta W$，使得 $W' = W + \Delta W$，并保证：
  $$
  \Delta w^T H_w \Delta w = 0
  $$
  即该扰动对任务损失的二阶影响为零，从而保持模型性能不变。
- 通过优化目标最小化变换后权重的数值范围（numerical range），有效抑制 outliers。

### 相比现有方法的优势
- ✅ **不依赖层间变换**：无需修改相邻层参数，实现真正的“self-absorption”，无推理开销。
- ✅ **互补性强**：可作为插件（plug-and-play）与 GPTQ、AWQ、QuIP 等方法结合，进一步提升性能。
- ✅ **高效求解**：基于 Softmax-$\infty$ 近似将非光滑的 $l_\infty$ 范数优化转化为可微的 $l_2$ 优化，并推导出**闭式解**（closed-form solution），无需迭代训练或资源密集型优化。
- ✅ **适用于极低位宽**：在 2-bit 量化的极端情况下仍能取得显著增益。

---

## 2. 核心实验方法和设置

### 使用的数据集
- **语言建模任务**：
  - `WikiText2`：用于计算 **Perplexity (PPL)**，衡量语言生成能力。
  - `C4`：大规模预训练语料子集，同样用于 PPL 评估。
- **常识问答任务**：
  - `PIQA`, `ARC`, `WinoGrande`：测试零样本准确率（Zero-shot Accuracy）。
- **综合基准测试**：
  - `MMLU`：多任务理解能力评测。
  - `MT-Bench`：多轮对话与指令遵循能力评估。

### 实验设置和评估指标
- **量化配置**：
  - 主要关注 **weight-only quantization**，位宽包括 W4A16、W3A16、W2A16。
  - 同时评估了 KV-Cache 量化（WKVQuant）和 weight-activation quantization 场景下的兼容性。
- **评估指标**：
  - ↓ Perplexity（越低越好）
  - ↑ Zero-shot Accuracy（越高越好）
  - 推理延迟（Per-token latency）与加速比（Speedup）
- **校准数据**：通常使用 128 个样本，序列长度 2048。

### 基线方法对比
- **主流 weight-only 量化方法**：
  - `RTN`（Random Tensor Network）
  - `GPTQ`（基于 Hessian 的误差补偿）
  - `AWQ`（激活感知缩放）
  - `QuIP`（正交旋转去 outlier）
  - `MagR`（无限范数优化）
  - `OmniQuant`（多方向校准）
- 所有对比均在同一设置下进行，确保公平性。

---

## 3. 主要实验结果和性能指标

### 关键性能数据
#### ✅ 2-bit 量化性能飞跃
- 在 **LLaMA2-7B** 上，`OSAQ+GPTQ` 将 WikiText2 的 PPL 从 **36.8** 显著降低至 **21.2**（↓42.4%）。
- 结合 coordinate descent（记为 `OSAQ+GPTQt`），PPL 进一步降至 **10.6**，接近 3-bit 水平。
- 在 C4 数据集上，PPL 从 33.7 降至 18.3（↓45.7%）。

#### ✅ 3-bit 量化稳定提升
- 在 `W3A16` 设置下，`OSAQ+GPTQ` 在 LLaMA2-13B 上将 WikiText2 PPL 从 **6.44** 降至 **5.72**（↓11.2%）。
- 对比 `AWQ` 和 `QuIP`，OSAQ 均带来一致增益。

#### ✅ 零样本准确率显著提高
| 模型 | 方法 | Avg. Accuracy (3-bit) |
|------|------|------------------------|
| LLaMA3-8B | GPTQ | 63.6% |
| LLaMA3-8B | OSAQ+GPTQ | **65.2%** (+1.6%) |
| LLaMA3-70B | GPTQ | 72.4% |
| LLaMA3-70B | OSAQ+GPTQ | **74.4%** (+2.0%) |

#### ✅ 大规模模型有效性验证
- 在 **Mistral-Large-123B-Instruct** 和 **Llama-3.1-405B-Instruct** 上，`OSAQ+GPTQ` 在 MMLU 上达到 **86.1%**，优于 vanilla GPTQ。

### 与基线方法的对比结果
- 在所有位宽和模型尺度下，**OSAQ + 任一 baseline 均优于原始 baseline**。
- 特别是在 **2-bit** 极端场景下，OSAQ 是唯一能使模型保持可用性的方法之一。
- 图表显示，OSAQ 能显著压缩权重分布，减少 outlier 幅度（见 Figure 4 和 Appendix A）。

### 消融实验结果
#### 🔍 Additive Transformation 对 FP16 性能影响
| 方法 | WikiText2 PPL (LLaMA2-7B) |
|------|----------------------------|
| Baseline (FP16) | 5.47 |
| Baseline + Additive | **5.52** |
| GPTQ | 8.37 |
| GPTQ + OSAQ | **6.75** |

👉 表明 additive transformation 几乎不影响原始浮点性能（仅轻微上升），但极大改善量化后性能。

#### 🔍 Softmax-$\infty$ 近似 vs 直接 $l_2$ 优化
| 方法 | WikiText2 PPL (LLaMA2-7B) |
|------|----------------------------|
| $l_2$ norm only | 7.82 |
| **Softmax-$\infty$ + $l_2$** | **6.75** |

👉 验证了 Softmax-$\infty$ 更好地逼近 $l_\infty$，更有效地抑制峰值 outliers。

#### 🔍 Null Space 稳定性分析
- 计算两个不同 batch 输入下的 null space 对齐程度（via $\text{NN}_2$ 的最大奇异值），结果显示：
  - 层间平均对齐度 > **0.96**，表明 null space 高度稳定。
- 即使在不同数据分布（WikiText2 vs C4）或不同校准集大小（64 ~ 1024）下，null space 依然稳定。

#### 🔍 超参数敏感性分析
- 对尾部能量阈值 $\gamma$、温度系数 $T$、正则项 $\mu_1,\mu_2$ 进行网格搜索（Figure 5），结果表明性能对超参数选择**鲁棒性强**。

---

## 4. 关键结论和发现

### 主要发现
- ✅ **Hessian 的 null space 在不同输入下高度一致**，支持了加法扰动的可行性。
- ✅ **Additive transformation 可以在不损害原始模型性能的前提下有效抑制 outliers**。
- ✅ **OSAQ 是一种通用、高效、无推理开销的插件式模块**，可无缝集成到现有量化流程中。
- ✅ 在 **2-bit 量化**中实现了突破性进展，使极低比特 LLM 部署成为可能。

### 方法的局限性
- ❗ 当前方法主要针对 **weight-only quantization** 设计，在 activation quantization 成为主要瓶颈时增益可能受限（尽管仍有帮助）。
- ❗ 依赖 Hessian 估计，虽然使用 calibration data 且效率高，但在某些极端稀疏或病态结构中可能不稳定。
- ❗ 对 extremely large models（>100B）的 full-layer 应用可能存在内存压力（但可通过分块处理缓解）。

### 未来工作方向
- 🔄 探索 **activation-side 的 outlier self-absorption**，构建统一的 additive 压缩框架。
- 🧠 将 OSAQ 思想扩展至 **其他结构化稀疏或低秩压缩方法** 中。
- ⚙️ 开发硬件友好的实现方式，推动 OSAQ 在边缘设备上的部署。
- 🤖 探索是否可以将 null space 的结构特性用于模型解释性或安全增强。

---

> **总结一句话**：  
> OSAQ 通过挖掘 Hessian 的低秩一致性，提出了一种无需训练、无推理开销的加法变换机制，首次实现了 outlier 的“自我吸收”，在 2-bit 量化中取得了超过 40% 的 PPL 下降，为极低比特 LLM 部署提供了全新且高效的解决方案。

</details>

---

### 9. [SOAR: Real-Time Joint Optimization of Order Allocation and Robot Scheduling in Robotic Mobile Fulfillment Systems](https://arxiv.org/abs/2605.03842)

**Authors**: Yibang Tang, Yifan Yang, Jingyuan Wang, Junhua Chen, Zhen Zhao  
**Category**: cs.AI  
**Published**: 2026-05-07  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2605.03842v1  

#### Abstract
Robotic Mobile Fulfillment Systems (RMFS) rely on mobile robots for automated inventory transportation, coordinating order allocation and robot scheduling to enhance warehousing efficiency. However, optimizing RMFS is challenging due to strict real-time constraints and the strong coupling of multi-p...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：SOAR: Real-Time Joint Optimization of Order Allocation and Robot Scheduling in Robotic Mobile Fulfillment Systems

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
在 **Robotic Mobile Fulfillment Systems (RMFS)** 中，订单分配（Order Allocation）与机器人调度（Robot Scheduling）是两个强耦合、多阶段的决策过程。现有方法面临以下挑战：
- **解耦方法**（Decoupled Methods）：将问题拆分为独立子任务以保证实时性，但牺牲了全局最优性。
- **联合优化模型**（如 MIP）：虽追求全局最优，但计算复杂度高，难以适应动态环境。

因此，如何在满足 **严格实时性要求** 的同时实现 **多阶段联合优化** 是一个尚未有效解决的关键问题。

---

### 🚀 提出的新方法与创新思路

作者提出 **SOAR**（Soft Order Allocation and Robot Scheduling），一种基于 **Deep Reinforcement Learning (DRL)** 的统一框架，用于实现实时联合优化。其核心创新包括：

#### （1）软订单分配机制（Soft Order Allocation）
- 不立即进行硬性分配，而是为每个订单动态计算其与货架（shelf）和工作站（workstation）之间的“匹配度”（matching degree）。
- 将这些软分配信息作为状态输入传递给后续调度模块，从而弥合了订单分配与机器人调度之间的鸿沟。

#### （2）事件驱动的马尔可夫决策过程（Event-Driven MDP）
- 决策由系统异步事件触发（如订单到达、机器人空闲等），而非固定时间步长。
- 实现真正的实时响应，并支持连续、动态的决策流。

#### （3）异构图神经网络建模（Heterogeneous Graph Transformer, HGT）
- 将仓库中不同类型的实体（机器人、货架、工作站、存储位置）建模为异构图。
- 利用 HGT 编码全局状态，融合物理状态与软分配引导信息，提升策略泛化能力。

#### （4）奖励塑形策略（Reward Shaping via p-norm）
- 针对原始目标函数（makespan）稀疏反馈的问题，设计基于 **p-norm 的密集奖励函数**，缓解延迟信用分配问题。
- 引入时间感知的 PPO（Time-Aware PPO）优化算法，考虑实际物理时间间隔对折扣因子的影响。

---

### ⚖️ 相比现有方法的优势

| 维度 | SOAR | 传统方法 |
|------|------|----------|
| **优化方式** | 联合优化（Joint） | 多为解耦（Phased）或静态联合 |
| **实时性** | <100ms 延迟，适合工业部署 | MIP 类方法耗时分钟级 |
| **适应性** | 动态事件驱动，持续学习 | 滚动时域（Rolling Horizon）存在滞后 |
| **性能表现** | 显著优于所有基线 | 局部最优或响应慢 |

> ✅ **核心优势总结**：首次实现了在 **亚百毫秒延迟下** 完成 **订单分配与机器人调度的端到端联合优化**，兼顾了实时性与全局性能。

---

## 2. 核心实验方法和设置

### 📊 数据集

实验涵盖两类场景共 **6 个数据集**：

| 类型 | 描述 |
|------|------|
| **Real-World Dataset** | 来自 **Geekplus** 实际仓库：<br>- 地图规模：40×72 网格<br>- 历史运营数据：31天<br>- 分为 Small / Medium / Large 三种规模 |
| **Synthetic Dataset** | 合成数据模拟波次放单特性：<br>- 地图规模：100×80 网格<br>- 订单 arrival time 符合带扰动的 wave distribution<br>- Item 数量与订单行数服从截断帕累托分布（Truncated Pareto） |

详细参数见附录 A。

---

### 🧪 实验设置与评估指标

#### 评估指标（Metrics）

| 指标 | 定义 | 目标 |
|------|------|-------|
| **Makespan (Obj ↓)** | 所有机器人完成任务的最大时间 → 衡量系统吞吐效率 | 越小越好 |
| **Average Order Completion Time (CompT ↓)** | 平均从订单到达至完成拣选的时间 → 反映服务响应速度 | 越小越好 |
| **Computation Time (Time ↓)** | 单次推理耗时 → 衡量计算效率 | 越低越好 |

#### 基线方法（Baselines）

分为两大类进行对比：

##### （1）Phased Methods（解耦方法）
- **Order Allocation**：
  - SQF（Shortest Queue First）
  - WLB（Work Load Balance）
  - OR Tools（Google CP-SAT 求解器）
- **Robot Scheduling**：
  - Nearest Neighbor
  - Earliest Arrival
  - TSP（Traveling Salesman Problem）
  - PSMDRL（基于 Transformer 的 DRL 方法）

组合形成多种两阶段流水线策略。

##### （2）Joint Methods（联合方法）
- **JOTP**：结合 Kuhn-Munkres 算法与 RL 的联合优化。
- **SABS**：基于模拟退火与束搜索的混合启发式算法。
- **Prod Heuristic**：当前工业现场使用的生产级启发式规则。

---

## 3. 主要实验结果和性能指标

### 🔢 关键性能数据（来自 Table 1）

在真实世界数据集上，SOAR 相比最强基线取得显著提升：

| 指标 | 提升幅度 |
|------|---------|
| **Makespan（全局完工时间）** | ↓ **7.5%** |
| **Average Order Completion Time（平均订单完成时间）** | ↓ **15.4%** |
| **单次决策延迟** | **<100ms**（满足工业实时性要求） |

> 在合成数据集中也表现出一致且更优的结果。

---

### 🔍 与基线方法的对比结果

| 对比维度 | 结果分析 |
|--------|----------|
| **vs. Phased Methods** | 所有解耦方法因缺乏协同，在资源利用率和全局效率上明显落后于 SOAR。例如 WLB+TSP 在 Real-Large 上 CompT 高出约 30%。 |
| **vs. Joint Methods** | JOTP 和 SABS 虽尝试联合优化，但由于依赖滚动时域机制，求解延迟导致决策过时；且无法捕捉长期动态演化趋势，性能反而不如部分解耦方法。 |
| **vs. OR Tools** | 尽管优化质量较高，但平均耗时达 **数分钟级别**，严重不适用于高并发动态环境。 |

✅ **结论**：SOAR 在保持极低延迟的同时，实现了远超各类基线的综合性能。

---

### 🔬 消融实验结果（Ablation Studies）

消融实验验证各组件的有效性（见 Table 2）：

| 模型变体 | Makespan 影响（↑表示恶化） | 分析 |
|--------|--------------------------|------|
| **w/o Soft Allocation** | ↑ ~25–30% | 移除软分配后性能大幅下降，说明其对联合优化至关重要 |
| **w/o HGT** | ↑ ~5–10% | 替换为标准 Transformer 后性能降低，表明 HGT 更能捕捉异构实体间关系 |
| **w/o Bias（无相位偏置）** | ↑ ~5–10% | 移除 phase-specific bias 导致探索效率下降 |
| **Only Bias（仅用偏置）** | ↑ ~15–20% | 仅靠先验知识无法建模复杂全局状态，仍需深度模型支持 |

此外还测试了：
- **Reward Shaping 方式**：`RS-Sum` 和 `RS-Max` 均劣于所提 p-norm 方法。
- **候选货架数量 K**：敏感性分析显示 K=10 时性能最优（U型曲线）。
- **p-norm 参数 p**：p=8 时平衡了稳定性与对瓶颈机器人的关注。

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **软订单分配机制成功打通了订单分配与机器人调度的壁垒**，使两者可在统一框架下协同优化。
2. **事件驱动的 MDP 设计使得系统能够实时响应动态变化**，避免了传统周期性调度带来的延迟。
3. **HGT + Phase-Knowledge Bias 的架构有效融合了领域知识与数据驱动学习**，提升了策略鲁棒性。
4. **p-norm Reward Shaping 显著缓解了稀疏奖励问题**，加速了训练收敛并提高了最终性能。
5. **sim-to-real 部署证实了 SOAR 在真实生产环境中的可行性与优越性**。

---

### ⚠️ 方法的局限性

1. **未集成底层控制模块**：目前仅处理高层调度决策，路径规划、避障等由外部系统完成。
2. **依赖高质量数字孪生平台**：真实部署前需构建高保真仿真环境，增加了前期投入。
3. **对极端异常工况适应性未知**：如大规模通信中断、设备故障等情况下的鲁棒性有待验证。

---

### 🔮 未来工作方向

1. **向端到端系统演进**：将路径规划、冲突检测等低层控制纳入统一学习框架。
2. **引入在线自适应机制**：让模型具备在线微调能力，以应对季节性需求波动或布局变更。
3. **扩展至多类型机器人协作场景**：支持搬运、分拣、打包等不同类型机器人的联合调度。
4. **探索联邦学习架构**：在保护客户隐私的前提下，跨多个仓库共享经验进行协同训练。

---

## 总结

> **SOAR 是首个在 RMFS 中实现“实时 + 全局联合优化”的 DRL 框架**。它通过 **Soft Order Allocation + Event-Driven MDP + HGT + Reward Shaping** 的创新组合，在保证 **<100ms 推理延迟** 的前提下，显著降低了 **makespan（-7.5%）** 与 **平均订单完成时间（-15.4%）**，并通过 **sim-to-real 成功落地**，展现出强大的工业应用潜力。

🔗 开源代码地址：[https://github.com/200815147/SOAR](https://github.com/200815147/SOAR)

</details>

---

### 10. [Constrained Extreme Gradient Boosting for Adapting Reduced-Order Models](https://arxiv.org/abs/2605.04130)

**Authors**: Melika Baghi, Xiao Liu, Kamran Paynabar  
**Category**: cs.LG  
**Published**: 2026-05-07  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.04130v1  

#### Abstract
High-fidelity simulations, such as computational fluid dynamics and finite element analysis, are essential for modeling complex engineering systems but are often prohibitively expensive for tasks including parametric studies, optimization, and real-time control. Projection-based reduced-order models...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：Constrained Extreme Gradient Boosting for Adapting Reduced-Order Models**

---

## **1. 论文的主要贡献和创新点**

### **解决的问题**
高保真仿真（如 CFD 和 FEA）在参数化研究、优化和实时控制等多查询任务中计算成本极高。投影型 Reduced-Order Models (ROMs) 通过将全阶动力学投影到低维子空间来加速计算，但其性能依赖于 Proper Orthogonal Decomposition (POD) 基的代表性。当参数变化时，固定的 POD 基可能不再最优，导致精度下降甚至不稳定。

因此，**如何自适应地为不同参数配置预测最优的 POD 基**成为关键挑战。

### **提出的新方法与创新点**
本文提出了 **Constrained Extreme Gradient Boosting (cXGBoost)**，一种基于集成树模型的 POD 基预测方法，具有以下创新：

- **将 Grassmann 流形上的子空间映射到欧氏空间进行学习**：利用从 Grassmann manifold $ G(r,n) $ 到切空间再到底层欧氏空间 $ \mathbb{R}^{(n-r)\times r} $ 的可逆嵌入（via logarithmic 和 horizontal lifting 映射），使得标准机器学习模型可用于学习参数-子空间关系。
  
- **引入输出约束以保证映射的单射性（injectivity）**：为确保预测向量能有效映射回 Grassmann manifold，必须限制其范数不超过 $ \pi/2 $。该几何约束被显式建模为 **Quadratically Constrained Quadratic Program (QCQP)** 并嵌入到每棵树的分裂过程中。

- **扩展 XGBoost 至受约束的多输出回归场景**：在目标函数中加入对叶节点权重的二次约束，使梯度提升过程始终满足流形重构条件，从而实现“几何感知”的学习。

### **相比现有方法的优势**
| 方法 | 局限性 | cXGBoost 的优势 |
|------|--------|----------------|
| **Grassmann 插值 [7]** | 在非线性或突变区域表现差，无法捕捉复杂依赖 | 能建模非光滑过渡和强非线性变化 |
| **Projected GP [10]** | 假设平滑性，在高频/冲击系统中过平滑 | 决策树天然适合处理不连续性和局部模式 |
| **普通 XGBoost 直接应用** | 无约束可能导致无效子空间预测 | 引入 QCQP 约束保障预测有效性与可逆性 |

> ✅ **核心优势总结**：cXGBoost 是首个将 **XGBoost 与流形几何约束结合**的方法，兼具强大拟合能力与数学严谨性，特别适用于高非线性、参数敏感的动力系统。

---

## **2. 核心实验方法和设置**

### **使用的数据集（四个数值算例）**

| 示例 | 物理问题 | 参数维度 | 数据规模 | 主要特性 |
|------|----------|-----------|---------|----------|
| **Example I**: Flow Around a Cylinder | 二维圆柱绕流（LBM + BGK） | Reynolds 数 ($ Re \in [115, 1500] $) | 42 组模拟，每组 2000 时间步快照 | 非定常涡脱落，随 Re 增加非线性强 |
| **Example II**: Wave Propagation | 双缝干涉波传播（CG2 元素求解波动方程） | 振幅 $ u_1 $, 频率 $ u_2 $ | 36 参数组合，500 快照/组 | 多频叠加、干涉条纹演化 |
| **Example III**: 1D Burgers Equation | 黏性 Burgers 方程 | 初始振幅 $ a $, 黏度 $ v $ | 30 组，101 快照/组 | 非线性对流主导，梯度陡峭化 |
| **Example IV**: Euler-Bernoulli Beam | 受迫梁振动 | 外力频率 $ u_1, u_2 $ | 25 组，100 快照/组 | 线性但多模态耦合，时间振荡复杂 |

所有案例均提取 snapshot matrix 后通过 SVD 得到 POD basis $ \Phi \in \mathbb{R}^{n\times r} $，并将其映射至欧氏空间向量 $ y \in \mathbb{R}^{(n-r)r} $ 作为回归目标。

### **实验设置与评估指标**

#### **训练/测试划分**
- **确定性划分**：按参数索引模 3 分割（如 Example I 中取 $ i \mod 3 = 0 $ 为训练）
- **5-fold Cross-Validation**：进一步验证泛化能力

#### **评估指标**
- **相对重建误差（Relative Reconstruction Error）**：
  $$
  \text{Error} = \frac{\| D_{\text{pred}} - D_{\text{true}} \|_F}{\| D_{\text{true}} \|_F}
  $$
  其中 $ D $ 为原始 snapshot 矩阵，$ D_{\text{pred}} $ 由预测的 POD 基重构得到。

- **统计指标**：均值、标准差、中位数、四分位距（Q25/Q75）、最大最小值

#### **基线方法对比**
- **Interpolation on Tangent Space (z-interpolation)** [7]：经典 Grassmann 插值法，在切空间线性插值后指数映射回流形。

#### **超参数设置**
见原文 Table 6，典型设置如下：
- Boosting stages: 80–120
- Learning rate: 0.2–0.4
- Max depth: 2–4
- L2 正则化项：$ \lambda = 10^{-2} $
- 子采样率：0.7–1.0

---

## **3. 主要实验结果和性能指标**

### **关键性能数据汇总**

| 示例 | 方法 | Mean Error | Median Error | Std | Max Error |
|------|-------|------------|--------------|-----|-----------|
| **I. Cylinder Flow** | Interpolation | 28.0% | 15.9% | 27.0% | 98.9% |
| | **cXGBoost** | **7.46%** | **7.34%** | **1.45%** | **12.8%** |
| **II. Wave Propagation** | Interpolation | 4.84×10⁻³ | 3.65×10⁻³ | 3.59×10⁻³ | 1.24×10⁻² |
| | **cXGBoost** | **1.74×10⁻³** | **1.44×10⁻³** | **9.98×10⁻⁴** | **5.11×10⁻³** |
| **III. Burgers** | Interpolation | 1.22×10⁻² | 6.72×10⁻³ | 1.34×10⁻² | 6.19×10⁻² |
| | **cXGBoost** | **6.10×10⁻³** | **3.90×10⁻³** | **5.92×10⁻³** | **2.78×10⁻²** |
| **IV. Beam** | Interpolation | 2.77×10⁻¹ | 2.98×10⁻¹ | 2.30×10⁻¹ | 7.58×10⁻¹ |
| | **cXGBoost** | **2.37×10⁻¹** | **2.51×10⁻¹** | **1.97×10⁻¹** | **6.31×10⁻¹** |

### **与基线方法的对比结果**
- 在所有四个示例中，**cXGBoost 显著优于传统插值方法**，尤其体现在：
  - **更低的平均与中位误差**（普遍降低 50% 以上）
  - **更小的标准差与最大误差** → 表明更强鲁棒性
  - **误差分布更集中**，极少出现极端偏差（见 Fig. 6, 11, 15, 18）

- 在高非线性区域（如 $ Re > 1200 $ 的圆柱绕流），插值法误差飙升至 >70%，而 cXGBoost 仍稳定在 <15%

- 在双缝波场重建中（Fig. 10），插值法在高频高幅下出现相位错位与条纹模糊，而 cXGBoost 更好保留干涉结构

### **消融实验结果（隐含分析）**
虽然未明确列出消融实验，但从算法设计可推断：
- **约束机制的有效性**：若去除 $ \|y\| < \pi/2 $ 约束，则可能出现不可逆映射，导致预测失败
- **树集成 vs 单棵回归树**：XGBoost 的 boosting 架构显著降低偏差与方差，优于单一决策树
- **QCQP 分裂策略的重要性**：强制在每个候选分裂中求解带约束的叶权重优化问题，是保障几何一致性的核心技术

---

## **4. 关键结论和发现**

### **主要发现**
1. **cXGBoost 能高效且准确地预测参数相关的 POD basis**，尤其在强非线性、多尺度、多频率系统中表现出卓越的泛化能力和稳定性。
2. **将流形几何先验编码进学习框架至关重要**：通过引入 QCQP 约束，确保了预测结果始终落在有效子空间内，避免了“非法”预测。
3. **树模型比 GP 更适合处理非光滑参数依赖**：在存在突变或模式切换的系统（如激波、涡脱落）中，cXGBoost 明显优于假设平滑性的 GP 方法。
4. **统一框架适用于多种物理系统**：从流体、波动到结构动力学，cXGBoost 均展现出良好适应性，表明其具有广泛工程应用潜力。

### **方法的局限性**
- **依赖参考点选择**：当前方法需选定一个基准点 $ p \in G(r,n) $ 进行 tangent space 展开，若参考点远离测试区域，可能影响精度。
- **计算开销略高于简单插值**：尽管远低于全阶仿真，但每次分裂需解 QCQP，训练时间高于无约束 XGBoost。
- **尚未提供不确定性量化**：目前为确定性预测，缺乏置信区间支持风险敏感决策。

### **未来工作方向**
1. **引入不确定性建模**：
   - 使用 **quantile regression XGBoost** 或 **bootstrap ensemble** 提供预测置信区间
   - 支持 UQ（Uncertainty Quantification）和安全关键系统的数字孪生构建

2. **动态参考点选择或局部流形逼近**：
   - 自适应选择最近邻参考点，提升外推能力
   - 结合 clustering + local cXGBoost 实现分区建模

3. **与其他 ROM 技术融合**：
   - 将 cXGBoost 预测的 POD basis 用于 Galerkin projection，构建完全自适应 ROM pipeline
   - 探索与 DMD、autoencoder-based ROM 的协同架构

4. **扩展至更高维参数空间与实时控制闭环测试**：
   - 应用于 aerodynamic shape optimization 或 MPC 控制器中，验证在线性能

---

> 🔚 **总结一句话**：  
> 本文提出的 **cXGBoost** 成功将 **XGBoost 的强大表达能力** 与 **Grassmann manifold 的几何约束** 相结合，实现了对参数化 POD basis 的高精度、鲁棒预测，为下一代自适应 ROM 提供了一种新颖且实用的学习框架。

</details>

---

### 11. [Predict-then-Diffuse: Adaptive Response Length for Compute-Budgeted Inference in Diffusion LLMs](https://arxiv.org/abs/2605.04215)

**Authors**: Michael Rottoli, Subhankar Roy, Stefano Paraboschi  
**Category**: cs.LG  
**Published**: 2026-05-07  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.04215v1  

#### Abstract
Diffusion-based Large Language Models (D-LLMs) represent a promising frontier in generative AI, offering fully parallel token generation that can lead to significant throughput advantages and superior GPU utilization over traditional autoregressive paradigm. However, this parallelism is constrained ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：**Predict-then-Diffuse: Adaptive Response Length for Compute-Budgeted Inference in Diffusion LLMs**

---

## 1. 论文的主要贡献和创新点

### ✅ 解决了什么问题

Diffusion-based Large Language Models (**D-LLMs**) 虽然支持**全并行 token 生成**，显著提升吞吐量和 GPU 利用率，但在推理时必须预先设定固定的输出长度（response length）。这一限制带来了两个严重问题：

- **计算浪费**：当真实响应远短于预设长度时，大量计算资源被用于处理无语义意义的 `<PAD>` tokens。
- **输出截断**：若预设长度不足，则导致输出被截断，需重新以更长长度运行，引入不可预测的延迟峰值。

### 🚀 提出的新方法与新思路

作者提出 **Predict-then-Diffuse** 框架，实现面向 **compute-budgeted inference** 的自适应响应长度控制。其核心是：

- **Adaptive Response Length Predictor (AdaRLP)**：一个轻量级、模型无关的模块，在推理前根据输入 prompt 预测最优响应长度。
- **Data-driven Safety Margin**：为防止预测过低导致截断，基于训练数据中正向误差分布（真实长度 > 预测长度）设定一个统计安全边距（如 95th 百分位），加到预测值上作为最终长度 $L^*$。

该框架无需修改 D-LLM 架构或训练目标，仅在推理前增加一个极低开销的预测步骤。

### 🔍 相比现有方法的优势

| 方法 | 是否需改架构 | 是否支持任意长度 | 是否避免 `<PAD>` 浪费 | 推理延迟是否可预测 |
|------|---------------|------------------|------------------------|--------------------|
| Vanilla D-LLM | 否 | ❌ | ❌ | ✅（但高） |
| Block Diffusion [6] | ✅ | ✅ | ⭕（部分） | ❌（半自回归） |
| Heuristic (e.g., doubling) | ❌ | ✅ | ⭕（多次重试仍耗算力） | ❌（随机重试导致延迟波动） |
| **Predict-then-Diffuse (Ours)** | ❌ | ✅ | ✅ | ✅（单次为主，fallback极少） |

> ✅ **优势总结**：
> - 完全保留 D-LLM 并行优势；
> - 显著减少 FLOP 开销；
> - 输出质量不降；
> - 延迟更稳定，适合生产部署。

---

## 2. 核心实验方法和设置

### 📚 使用的数据集

构建了一个包含 **39,994 条 prompt-response 对** 的混合基准数据集，来源包括：

- **ShareGPT**
- **Alpaca**
- **Dolly-15k**
- **OpenOrca**
- **ELI5**

特点：强调**长文本生成**，输出长度方差大（均值 ~96 tokens，标准差 ~120，峰度 ~107），有效测试自适应能力。

数据按 80/20 划分为训练集与测试集。使用 `GPT2TokenizerFast` 分词并计算长度。

### ⚙️ 实验设置

- **主模型**：LLaDA-8B（Discrete D-LLM）
- **扩散步数**：T = 128
- **最大长度**：$L_{\text{max}} = 4096$
- **硬件平台**：NVIDIA H100 GPU（80GB VRAM）
- **FLOP 测量工具**：DeepSpeed

### 📊 评估指标

| 指标 | 描述 |
|------|------|
| **Total TFLOP** | 整个测试集上的总浮点运算量（含 fallback 重试惩罚） |
| **Savings (%)** | 相对于 Max Response Length 的 FLOP 节省比例 |
| **Fallback Rate (%)** | 因长度不足需重跑的比例 |
| **RMSE / MAE** | 响应长度预测误差（越低越好） |
| **% ≤10% error** | 预测误差在真实长度 10% 内的样本占比 |

### 🆚 基线方法对比

| Baseline | 描述 |
|---------|------|
| **Max Response Length (4096)** | 默认设置，固定最长长度 |
| **Static Response Length (200)** | 固定较短长度，截断则 double 重试 |
| **Mean Doubling Heuristic** | 从数据集均值 (~95) 开始，逐步翻倍直至完整输出 |
| **Oracle** | 理想情况，已知真实长度 $L = k$，下限参考 |

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据（见 Table III）

| 方法 | TFLOP | Savings (%) | Fallback Rate (%) |
|------|-------|-------------|-------------------|
| Max Response Length (4096) | 4.03 | 0.0% | 0.0% |
| Static (200) | 0.054 | 98.6% | 22.1% |
| Doubling Heuristic | 0.027 | 99.31% | — |
| **Predict-then-Diffuse (Ours)** | **0.026** | **99.34%** | **0.1%** |
| Oracle | 0.024 | 99.4% | 0.0% |

> ✅ **结论**：  
> - 我们的方法节省 **99.34% FLOP**，接近理论最优（Oracle）；
> - 仅需 **0.1% fallback**，远低于启发式方法的实际重试频率。

### 🔍 预测器性能比较（Table II）

| 模型 | RMSE | MAE | % ≤10% error |
|------|------|-----|--------------|
| AdaRLP-engineered | 81.6 | 51.6 | 10.5% |
| **AdaRLP-text-only** | **11.4** | **1.7** | **97.5%** |

> 💡 发现：直接将原始 prompt 输入 **CatBoost**（利用其原生文本特征处理能力）效果远优于手工设计特征，说明模型能自动捕捉“写诗”vs.“写小说”等长度相关语义线索。

### 🧪 消融实验与鲁棒性验证

#### 在**双峰分布模拟数据**中的表现：
- 设定 60% 短查询（mean=50）、40% 长报告（mean=3000）
- 结果：启发式方法因频繁翻倍失败而累计成本高昂；
- **Predict-then-Diffuse 保持 19% 的计算优势**

> ✅ 表明本方法对复杂、异构数据更具鲁棒性。

#### 安全边距（Safety Margin）作用：
- 引入 $\delta = \text{Quantile}_{95}\{k - L \mid k > L\}$ 后，fallback 率从 1.43% 降至 **0.1%**
- 仅增加少量 padding 开销，换来极高可靠性

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **D-LLM 的 `<PAD>` tokens 是主要计算瓶颈**  
   - FLOP 成本随序列长度呈 **$O(L^2)$** 增长（注意力主导），实验证实该趋势（$R^2 = 0.9706$）。
   
2. **精准预测响应长度可极大降低推理成本**  
   - Predict-then-Diffuse 实现 **99.34% FLOP 节省**，几乎达到 Oracle 性能。

3. **轻量模型足以胜任长度预测任务**  
   - CatBoost 在仅用原始文本输入的情况下即可实现超高精度（MAE=1.7），无需额外特征工程。

4. **延迟确定性至关重要**  
   - 启发式方法虽平均节省高，但存在**长尾延迟风险**；
   - Predict-then-Diffuse 提供近乎确定性的单次生成体验（99.9% 请求无需重试）。

5. **D-LLM 支持动态 verbosity 自适应**  
   - 如 Fig. 5 所示，同一问题在不同 $L$ 下生成简洁或详细版本，但答案正确性不变；
   - 只要 $L^* \geq k$，性能稳定（参见 Tab. IV：GSM8K 和 HumanEval 指标无明显下降）。

### ⚠️ 方法的局限性

- **破坏批处理（batching）效率**：每个样本使用不同的 $L^*$，难以统一 batching，影响吞吐优化。
  - 当前缓解策略：按预测长度聚类分组 batch。
- **依赖高质量 SFT 数据集**：AdaRLP 训练需要成对的 (prompt, response length) 数据，若 response 不完整会影响预测准确性。
- **极端长尾仍可能 fallback**：尽管概率极低，但遇到超预期长输出仍需回退至 $L_{\text{max}}$。

### 🔮 未来工作方向

1. **高效动态 batching 策略**  
   - 借鉴 vLLM 中的 **PagedAttention** 技术，实现变长序列的内存高效管理。

2. **端到端联合建模预测与生成**  
   - 探索将 AdaRLP 与 D-LLM 联合微调，进一步提升预测一致性。

3. **扩展至 Continuous D-LLMs**  
   - 将框架推广到连续空间扩散模型，研究其长度控制机制。

4. **多模态场景下的响应长度预测**  
   - 应用于图文生成、语音合成等跨模态任务中的输出规模估计。

---

> 🔗 **代码开源地址**：[https://github.com/mchl-labs/predict-then-diffuse](https://github.com/mchl-labs/predict-then-diffuse)

</details>

---

### 12. [From Video-to-PDE: Data-Driven Discovery of Nonlinear Dye Plume Dynamics](https://arxiv.org/abs/2605.04535)

**Authors**: Cesar Acosta-Minoli, Sayantan Sarkar  
**Category**: cs.LG  
**Published**: 2026-05-07  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.04535v1  

#### Abstract
Inferring continuum models directly from video is hampered by two facts: the recorded field is uncalibrated image intensity rather than a physical state, and direct numerical differentiation of noisy frames is unstable. We develop a video-to-PDE pipeline that converts grayscale recordings of an ink ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# From Video-to-PDE: Data-Driven Discovery of Nonlinear Dye Plume Dynamics 论文总结

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
该论文旨在解决**从未经校准的视频数据中直接推断连续介质模型（PDE）** 的挑战。传统方法面临两大难题：
- 视频记录的是图像强度（image intensity），而非物理状态变量（如浓度）；
- 对噪声视频帧进行直接数值微分会导致不稳定。

现有方法（如 optical flow、PIV 或 PINNs）虽能估计流场或隐变量，但通常不输出显式的、可模拟的 PDE 形式，限制了对系统动力学的结构性解释。

### 提出了什么新方法或新思路
作者提出了一套完整的 **video-to-PDE pipeline**，将灰度染料扩散视频转化为可解释、可模拟的偏微分方程（PDE）。其核心创新包括：

- **Weak-form 回归避免时间微分**：采用基于积分形式的 weak-form SINDy 方法，在光滑测试函数上投影，避免对噪声视频数据直接求导。
- **分离结构发现与参数校准**：
  - 首先通过 weak-SINDy 发现候选 PDE 结构；
  - 再用 inverse Physics-Informed Neural Network (iPINN) 和 rollout-based bootstrap 进行系数优化，提升预测能力。
- **引入漂移解耦机制**：利用强度加权质心（intensity-weighted centroid）提取整体平流速度 $v(t)$，将其作为预设项从本征扩散动力学中分离。
- **多阶段不确定性评估**：结合 bootstrap、front-radius 误差、centroid 轨迹等几何诊断工具，全面评估模型鲁棒性和物理合理性。

### 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| **稳定性** | Weak-form 回归显著降低噪声敏感性，优于强形式微分方法（如原始 SINDy/PDE-FIND）。 |
| **可解释性** | 输出简洁、稀疏的 PDE 表达式，支持 Cole-Hopf 变换等解析分析，具备结构可读性。 |
| **预测性能** | 经 rollout 校准后的模型在 held-out frames 上表现更优，尤其在长期演化预测中。 |
| **物理一致性** | 引入正则化约束（如 $\beta > 0$）确保扩散项为正，符合物理直觉。 |

---

## 2. 核心实验方法和设置

### 使用的数据集
- 自建实验数据：顶部视角拍摄的墨水滴在水中二维扩散过程。
- 输入为未经校准的灰度视频帧序列 $I_{\text{gray}}(x, y, t)$，共约 1009 帧，空间分辨率为 $200 \times 200$。
- 数据未经过物理标定（单位为像素坐标），因此恢复的 PDE 参数具有“图像坐标”意义。

### 实验设置和评估指标
#### 数据预处理流程
1. 图像反转并归一化：$u(x, y, t) = 1 - I_{\text{gray}} / 255$，使墨水区域值高、背景值低；
2. 裁剪与重采样至统一网格；
3. 应用 Gaussian 滤波 ($\sigma = 1.0$) 抑制像素级噪声。

#### 方法流程
1. **Drift Estimation**：计算 $u$ 的 intensity-weighted centroid $(x_c(t), y_c(t))$，经 Savitzky-Golay 平滑后微分得漂移速度 $v(t) = (v_x(t), v_y(t))$。
2. **Chronological Split**：按 60%/20%/20% 划分训练/验证/测试集（时间顺序划分）。
3. **Weak-form SINDy**：
   - 构造弱形式回归系统，使用 Gaussian 测试函数；
   - 库函数包含常数项、$u$、$|\nabla u|^2$、$u|\nabla u|^2$、$\Delta u$ 等；
   - 采用 STLSQ（Sequentially Thresholded Least Squares）进行稀疏回归。
4. **iPINN Refinement**：固定 PDE 结构，仅训练非线性梯度项和拉普拉斯项系数，最小化 PDE 残差。
5. **Bootstrap Rollout Calibration**：
   - 使用 chronological block bootstrap 生成多个训练副本；
   - 以 Nelder-Mead 算法最小化 rollout MSE，实现免导数优化；
   - 输出系数的中位数及置信区间。

#### 评估指标
| 指标 | 描述 |
|------|------|
| **rRMSE** | 相对均方根误差：$\sqrt{\sum (u_{\text{pred}} - u_{\text{true}})^2 / \sum u_{\text{true}}^2}$ |
| **Centroid Error (COM RMSE)** | 预测与真实质心轨迹之间的欧氏距离 |
| **Front-radius Error** | 在不同阈值水平 $\gamma = \{0.05, ..., 0.25\}$ 下超水平集面积对应的等效半径误差 |
| **Model Admissibility** | 是否满足 $\beta > 0$、是否保持质心轨迹一致等 |

### 基线方法对比
- **Advection-Diffusion Baseline (A/B)**：标准线性输运模型 $u_t + v \cdot \nabla u = \beta \Delta u$
- **Full Library Models**：包含多项式与梯度交叉项的过完备库（易产生共线性）
- **Learned vs Measured Advection**：比较是否将 $v(t)$ 作为自由参数学习（Mode A）还是固定使用测量值（Mode B）

---

## 3. 主要实验结果和性能指标

### 关键性能数据
最终选定模型为：
$$
u_t + v(t) \cdot \nabla u = 9.005 |\nabla u|^2 + 0.666 \Delta u
$$
此模型在测试集上的表现如下：

| 模型 | Validation rRMSE (%) | Test rRMSE (%) | $\beta$ 符号 | Centroid RMSE |
|------|------------------------|----------------|---------------|----------------|
| 最终选型 (C, bootstrap) | **6.19%** | **~6.2%** | $\beta > 0$ ✅ | < 0.05 ✅ |
| iPINN refined C | 9.38% | — | $\beta > 0$ ✅ | ~0.10 ❌ |
| Weak-SINDy C | 10.98% | — | $\beta < 0$ ❌ | ~0.04 ✅ |
| Advection-Diffusion (A) | 16.45% | — | — | ~0.15 ❌ |

> 注：更低的 rRMSE 表示更好的全场重建精度；centroid RMSE 小表示轨迹保持良好。

### 与基线方法的对比结果
- 所提 nonlinear-gradient 模型（含 $|\nabla u|^2$ 项）显著优于传统 advection-diffusion 模型（rRMSE 从 ~16.5% 降至 ~6.2%）；
- 若允许模型自行学习 advection 系数（Mode A），虽然 pixel-wise rRMSE 可接受，但 centroid 轨迹严重偏离（RMSE > 1.1），说明缺乏物理一致性；
- 使用 measured drift（Mode B）极大提升了轨迹保真度。

### 消融实验结果
#### （1）库函数选择的影响
| Library | Condition Number $\kappa(\Theta)$ | Active Terms | rRMSE (%) |
|--------|-------------------------------|-------------|-----------|
| Full | ~$10^5$ | 多项共线项混杂 | ~11% |
| C: $|\nabla u|^2 + \Delta u$ | 6.36 | $|\nabla u|^2$, $\Delta u$ | 10.98 → **6.19**（经校准） |
| C-alt: $u|\nabla u|^2 + \Delta u$ | 1.91e-2 | $u|\nabla u|^2$ 吸收扩散效应，$\Delta u$ 不稳定 | ~11% |

→ **结论**：$|\nabla u|^2$ 更具识别稳定性，且保留正 $\beta$，优于其他非线性梯度项。

#### （2）不同初始化对 bootstrap 的影响
| 初始化来源 | Model | Val rRMSE (%) | $a$ | $\beta$ |
|----------|-------|----------------|-----|--------|
| Weak-SINDy | C | **6.19** | 9.005 | 0.666 |
| iPINN | C | 9.57 | 2.703 | 0.049 |

→ **结论**：尽管 iPINN 改善了残差，但 rollout 表现不如直接从 weak-SINDy 初始化的 bootstrap，表明 rollout error 是更可靠的优化目标。

#### （3）Front-aware Objective 实验
使用 front-radius 和 growth penalty 的目标函数：
$$
J_{\text{front}} = J_{\text{pix}} + w_f J_{\text{radius}} + w_g J_{\text{growth}}, \quad w_f=5.0, w_g=0.05
$$
得到另一组参数：$a \approx 34.1, \beta \approx 0.536$，front RMSE 更低，但 centroid RMSE 升至 ~0.5，说明存在 trade-off。

---

## 4. 关键结论和发现

### 论文的主要发现
1. **可以从未经校准的视频中发现有效的 PDE 模型**：即使输入仅为图像强度，也能通过合理建模恢复出具有预测能力和解析结构的演化方程。
2. **最优模型为非线性梯度输运方程**：
   $$
   u_t + v(t)\cdot\nabla u = a|\nabla u|^2 + \beta \Delta u,\quad a,\beta>0
   $$
   属于 viscous Hamilton-Jacobi 方程类，可通过 **Cole-Hopf 变换** 化为线性 advection-diffusion 方程：
   $$
   \phi = \exp\left(\frac{a}{\beta} u\right),\quad \Rightarrow\quad \phi_t + v(t)\cdot\nabla\phi = \beta \Delta \phi
   $$
   这揭示了非线性项的本质是“对数变换下的扩散”，具备严格的数学结构和最大值原理。
3. **Pipeline 设计至关重要**：
   - 分离结构发现与参数校准可避免局部最优；
   - 使用 rollout error 而非残差作为优化目标更能反映真实预测性能；
   - 几何诊断（centroid、front radius）比 pixel-wise error 更能体现物理一致性。

### 方法的局限性
1. **参数依赖于图像坐标系**：恢复的系数 $a, \beta$ 与相机分辨率、光照、染料浓度响应相关，不能直接映射到物理单位。
2. **预处理影响梯度估计**：裁剪、平滑、重采样等操作会改变梯度分布，需谨慎控制。
3. **假设漂移场为空间均匀**：当前方法仅提取全局平移速度，无法处理剪切流、涡旋等复杂流动结构。
4. **单次实验验证**：尚未在不同初始条件、流体深度或多重复实验下验证泛化能力。

### 未来工作方向
1. **扩展至空间变化的速度场**：结合 optical flow 或 learned velocity field 替代单一 $v(t)$。
2. **纳入物理约束于训练过程**：例如强制 $\beta > 0$、质量守恒、最大值原理等，嵌入到 loss 中而非事后筛选。
3. **跨实验迁移学习**：探索模型在不同设置下的可迁移性，构建通用染料输运规律。
4. **应用于其他成像场景**：如生物膜生长、火焰传播、医学影像中的病灶扩散等，推广至各类 evolving scalar fields。

--- 

> ✅ **一句话总结**：本文提出一个稳健的 video-to-PDE pipeline，首次从无标定染料视频中发现了具备 Cole-Hopf 可积结构的非线性 PDE，并证明了“结构发现 + rollout 校准 + 几何诊断”的多阶段范式对于视觉驱动建模的重要性。

</details>

---

### 13. [KernelBench-X: A Comprehensive Benchmark for Evaluating LLM-Generated GPU Kernels](https://arxiv.org/abs/2605.04956)

**Authors**: Han Wang, Jintao Zhang, Kai Jiang, Haoxu Wang, Jianfei Chen, Jun Zhu  
**Category**: cs.LG  
**Published**: 2026-05-07  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.04956v1  

#### Abstract
LLM-based Triton kernel generation has attracted significant interest, yet a fundamental empirical question remains unanswered: where does this capability break down, and why? We present KernelBench-X, a benchmark designed to answer this question through category-aware evaluation of correctness and ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：KernelBench-X: A Comprehensive Benchmark for Evaluating LLM-Generated GPU Kernels**

---

## **1. 论文的主要贡献和创新点**

### **解决了什么问题**
当前基于 **LLM** 的 **Triton kernel** 自动生成技术虽有进展，但仍存在两个根本性未解问题：
1. **能力边界不明确**：尚不清楚哪些任务类型能被可靠处理、哪些会失败，以及失败原因。
2. **迭代优化机制理解不足**：不清楚迭代精炼（iterative refinement）在提升编译率、正确性和性能方面的实际效果。

现有基准（如 KernelBench、TritonBench）因缺乏细粒度分类、严谨的正确性验证和硬件效率评估，无法系统回答上述问题。

---

### **提出了什么新方法或新思路**
作者提出 **KernelBench-X**，一个面向 LLM 生成 GPU kernel 的综合性基准测试框架，具备以下三大创新设计：

1. **两阶段正确性协议（Two-Stage Correctness Protocol）**
   - **Call Accuracy**：检查代码是否可导入、编译并通过静态约束（如禁止高阶量化 API）。
   - **Execution Accuracy**：在多种输入分布下（含异常值注入）与参考实现对比输出，确保语义一致性。

2. **15 类任务分类体系（Category-Aware Taxonomy）**
   - 将 176 个任务划分为 **15 个类别**（如 Math、Fusion、Quantization），依据是计算结构而非操作符类型，支持按任务结构分析失败模式。
   - 新增对 **multi-precision** 和 **manual quantization**（W8A8/W4A16）的支持。

3. **超越运行时的硬件效率评估**
   - 引入 **IOU**（I/O Utilization）和 **MFU**（Math Utilization）作为效率代理指标。
   - 报告跨设备性能可移植性（cross-hardware speedup variance）。

---

### **相比现有方法的优势**
| 维度 | KernelBench-X 的优势 |
|------|------------------------|
| **任务组织** | 显式结构化分类，支持归因分析（category-aware） |
| **正确性验证** | 双阶段协议避免“偶然通过”输出比较的假阳性 |
| **评估全面性** | 同时衡量 correctness、efficiency、portability、code quality |
| **数据开放性** | 发布迭代过程中的修复与优化配对（transition pairs），支持后续训练 |

---

## **2. 核心实验方法和设置**

### **使用的数据集**
- **KernelBench-X 自建数据集**：共 **176 个任务**，覆盖 **15 个类别**：
  ```
  Activation, Convolution, Fusion, Index, LinearAlgebra, Loss, Math, MatrixMultiply,
  Normalization, Optimizer, Pooling, Quantization, Random, Reduce, SpatialOps
  ```
- 包含 **multi-precision**（fp16/bf16/int8）变体和 **6 个量化任务**（如 matmul_w8a8）。
- 所有任务提供统一接口描述、参考实现（PyTorch）和约束条件。

---

### **实验设置和评估指标**

#### **硬件平台**
在 **6 种 NVIDIA GPU** 上进行测试：
- RTX 5090, RTX 4090, A100-PCIE-40GB, H20, H800 PCIe, L20  
- 软件栈统一：CUDA 11.8, PyTorch 2.10.0+cu128, Triton 3.6.0

#### **评估指标**
| 指标 | 定义 |
|------|------|
| **Compile Rate (%)** | 成功编译并调用的比例 |
| **Correct Rate (%)** | 语义正确的比例（通过 Execution Accuracy） |
| **Correct/Compile (%)** | 编译成功中真正正确的比例 |
| **Speedup** | 相对于 PyTorch eager 模式的加速比 |
| **IOU / MFU** | 归一化的带宽/算力利用率，`max(IOU, MFU)` 衡量主导瓶颈利用情况 |
| **Maintainability Index (MI)** 和 **Cyclomatic Complexity (CC)** | 代码质量度量 |

---

### **基线方法对比**
评估了 **5 种代表性方法**，涵盖不同设计范式：

| 方法 | 类型 | 是否迭代 | 温度 | 其他设置 |
|------|------|----------|--------|-----------|
| **AutoTriton** | 训练增强型（SFT + RL） | 单次生成 | - | 使用原生提示 |
| **GEAK** | Agent 架构（generator-evaluator-reflector-optimizer） | 是（3轮） | 1.0 | 每轮生成4候选，保留5最优 |
| **KernelAgent** | 多智能体生成-验证-精炼 | 是（最多5轮） | 0.4 | 并行3 worker |
| **Claude** | 通用大模型 | 单次生成 | - | 对比零样本能力 |
| **DeepSeek-Coder** | 通用代码模型 | 单次生成 | - | 零专业化基线 |

所有方法通过统一适配器接入，评估流程一致。

---

## **3. 主要实验结果和性能指标**

### **关键性能数据（来自 Table 1）**

| Method | Compile (%) | Correct (%) | Correct/Compile (%) | Speedup (×) | Score (%) |
|--------|-------------|------------|---------------------|-------------|-----------|
| AutoTriton | 36.4 | 17.0 | 46.9 | 1.35 | 60.7 |
| **GEAK** | **68.8** | **30.7** | 44.6 | 1.15 | 50.0 |
| KernelAgent | 64.2 | 10.8 | 16.8 | 1.41 | 68.1 |
| Claude | 45.5 | 22.7 | 50.0 | 1.26 | 54.2 |
| KernelLLM | 1.7 | 0.0 | 0.0 | — | 0.0 |

> ✅ **亮点**：GEAK 编译成功率最高（68.8%），Correct 最高（30.7%）  
> ❗ **痛点**：即使最强方法也仅约 **30% 正确率**，且 Correct/Compile 比例普遍偏低

---

### **与基线方法的对比结果**

#### **(1) 正确性主要由任务类别决定，而非方法本身**
- **方差解释力分析**显示：
  - 在 **semantic correctness** 上，**category 解释 9.4% 方差**，而 **method 仅解释 3.3%**
  - 即：**任务结构的影响是方法设计的近 3 倍**
- 示例：
  - **Math** 类别：各方法正确率均 >30%，Claude 达 50%
  - **Fusion** 类别：平均正确率仅 10.8%，**72% 任务全方法失败**
  - **Quantization & SpatialOps**：**0% 正确率**（尽管有非零编译率）

#### **(2) 迭代精炼提升正确性，但损害性能**
以 GEAK 为例（Figure 3）：
- 编译率从 **52.3% → 68.8%**
- 正确率从 **18.2% → 30.7%**
- 但平均 **speedup 从 1.58× 下降到 1.44×**
- 新“救活”的 kernel 性能显著更差（round 0→1：1.16× vs 1.58×）

> 🔍 编辑分析表明：多数修改为局部修复（mask fix、dtype cast），极少涉及性能优化重写

#### **(3) 正确 ≠ 高效**
- **46.6% 的正确 kernel 比 PyTorch eager 更慢**
- 中位数 speedup 仅为 **1.0008×**
- 跨设备性能差异巨大：最坏情况下 **max/min speedup ratio 达 21.4×**
  - 如在 L20 上，**76% 的正确 kernel 慢于 PyTorch**；而在 A100 上该比例为 18%

#### **(4) 量化任务完全未解决**
- 所有方法在 **30 个量化任务上全部失败（0/30 success）**
- 尽管部分方法有较高编译率（如 KernelAgent 在 Quantization 编译率达 83.3%）
- 表明问题是**对数值契约（numerical contract）的根本误解**，而非语法错误

---

### **消融实验结果（隐含分析）**
虽然无显式消融表，但通过多维度归因分析实现了类似功能：

| 分析维度 | 发现 |
|---------|------|
| **静态复杂度代理变量 vs 正确性失败相关性** | 中间赋值数、fusion 调用数相关性最高（r≈0.21），但仍较弱 → 说明失败源于**深层语义问题**，非表面复杂度 |
| **类别内 vs 方法间差异** | 同一类中不同方法表现趋同 → 支持“任务结构主导”结论 |
| **迭代前后 kernel 性能变化** | 新增正确 kernel 性能显著低于初始就正确的 kernel → 揭示“修复偏向”（repair bias） |

---

## **4. 关键结论和发现**

### **主要发现（Three Key Insights）**

#### **Insight 1: 正确性边界由全局语义协调决定（Global-Contract Semantic Failure）**
- 当任务需要维护跨维度、内存布局或多程序实例的一致性时（如 reduction、broadcasting），LLM 容易失败。
- 模型能写出局部正确的 Triton idiom，但在组合时违反全局契约（如 padding 后 exp 导致求和偏差）。
- **案例**：`fused_exp_mean` 中 masked lanes 被 pad 为 0 再 exp，导致每个无效元素贡献 `exp(0)=1`，破坏数学意义。

#### **Insight 2: 迭代精炼是“修复偏向”的（Repair-Biased Iterative Refinement）**
- 当前迭代机制依赖显式错误信号（编译错、形状错、输出错），适合修复局部 bug。
- 但性能优化需**计划级决策**（tiling、memory layout、kernel boundary），这些无法从局部反馈中恢复。
- 结果：迭代后集合扩大，但引入大量“正确但慢”的 kernel，拉低整体性能。

#### **Insight 3: 性能有效性仍是未解挑战（Performance as an Unsolved Frontier）**
- 正确性只是第一步，**高效且可移植的 kernel 生成仍远未达成**。
- 当前方法缺乏对硬件行为的理解，生成的 kernel 往往针对特定设备过拟合，缺乏泛化能力。

---

### **方法的局限性**
1. **评估集中于单算子 kernel**，未覆盖端到端模型融合场景。
2. **未包含更多硬件架构**（如 AMD GPU、TPU）。
3. **迭代分析局限于 GEAK**，其他 agent 系统未深入剖析。
4. **量化任务定义严格**，可能排除了一些实用但非手动实现的方案。

---

### **未来工作方向**
论文建议从三个方向突破当前瓶颈：

1. **建模全局张量契约（Global Tensor Contracts）**
   - 开发能推理 parallel reduction semantics、broadcasting alignment 的机制。
   - 引入 symbolic reasoning 或 constraint checking 模块。

2. **显式建模数值精度（Explicit Numerical Precision Modeling）**
   - 将量化视为“近似契约”而非精确等价，训练模型理解 scale、rounding、overflow 的影响。

3. **效率感知生成（Efficiency-Aware Generation）**
   - 在训练或推理中引入 **hardware cost feedback**（如 IOU/MFU、roofline profile）。
   - 探索 **profile-guided hyperparameter search** 或 **hardware-aware RL training**。

4. **发布资源支持社区研究**
   - 开源 [GitHub](https://github.com/BonnieW05/KernelBenchX)
   - 提供 **transition pairs**（修复链、优化事件）用于训练本地修复模型或性能优化 agent。

---

> 📌 **总结一句话**：  
> **KernelBench-X 揭示了 LLM 生成高效 GPU kernel 的真实能力边界——当前方法已部分跨越“可编译”和“语义正确”门槛，但在“全局协调”、“数值契约”和“硬件效率”方面仍面临结构性挑战。**

</details>

---

### 14. [OracleProto: A Reproducible Framework for Benchmarking LLM Native Forecasting via Knowledge Cutoff and Temporal Masking](https://arxiv.org/abs/2605.03762)

**Authors**: Yiding Ma, Chengyun Ruan, Kaibo Huang, Zhongliang Yang, Linna Zhou  
**Category**: cs.AI  
**Published**: 2026-05-07  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.03762v1  

#### Abstract
Large language models are moving from static text generators toward real-world decision-support systems, where forecasting is a composite capability that links information gathering, evidence integration, situational judgment, and action-oriented decision making. This capability is in broad demand a...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# OracleProto: A Reproducible Framework for Benchmarking LLM Native Forecasting via Knowledge Cutoff and Temporal Masking  
**——核心结论与实验结果总结**

---

## 1. 论文的主要贡献和创新点

### ✅ 解决了什么问题

当前对大语言模型（LLM）**原生预测能力（native forecasting capability）** 的评估面临根本性矛盾：

- **前瞻性评估（Prospective Evaluation）**：在事件尚未发生时进行预测，能有效避免信息污染（contamination），但问题集会随时间失效，不可复现，难以重复测试。
- **回溯性评估（Retrospective Evaluation）**：使用已解决的历史事件作为测试题，易于审计和比较，但存在严重风险——模型可能通过预训练数据“记住”答案，而非真正进行推理预测。

这一矛盾导致现有基准（如 FutureX-Past）无法可靠区分“事实回忆”与“真实预测”。

> 🔍 **核心问题**：如何让已发生的事件重新成为有效的、无污染的预测任务？

---

### 🚀 提出的新方法与创新思路

论文提出 **OracleProto** ——一个可复现的、面向数据集级别的 LLM 预测能力评估框架，其核心思想是：

> 通过 **知识截止（Knowledge Cutoff）** 和 **时间掩码（Temporal Masking）** 重建清晰的信息边界，将已解决事件转化为可控的预测样本。

#### 主要技术组件：
| 组件 | 功能说明 |
|------|----------|
| **Knowledge Cutoff-Aligned Sample Admission** | 只保留那些在模型知识截止日期之后才揭晓结果的问题，防止参数化泄露（parametric leakage）。 |
| **Tool-Level Temporal Masking** | 在检索工具层强制注入时间截止，限制模型只能访问截止前的外部信息。 |
| **Content-Level Leakage Detection** | 使用独立的 LLM 检测器对检索结果进行内容级审核，过滤掉隐含未来信息的文本片段。 |
| **Discrete Answer Normalization** | 将自由形式输出标准化为离散标签集合，确保评分一致性。 |
| **Hierarchical Scoring** | 多层级评分体系：从 item-level 到 question-level 再到 model-level，支持稳定性、一致性等多维分析。 |

---

### ⚖️ 相比现有方法的优势

| 对比维度 | 现有方法（如 ForecastBench, FutureX） | OracleProto |
|--------|-------------------------------|-----------|
| **可复现性** | 一次性运行，问题过期即失效 | 数据集级封装，跨时间、跨模型可重放 |
| **防污染能力** | 依赖动态更新或警告使用者 | 主动构建三层防护（参数/工具/内容） |
| **评估粒度** | 整体准确率为主 | 支持质量、稳定性、成本效率等多维量化 |
| **训练可用性** | 仅用于评估 | 可直接作为 SFT/RL 的训练信号来源 |
| **审计透明性** | 黑盒运行 | 提供完整日志、哈希指纹、运行元数据 |

> 💡 **本质突破**：将 LLM 预测从“一次性的竞赛行为”转变为“可积累的数据资产”。

---

## 2. 核心实验方法和设置

### 📚 使用的数据集

- **基础数据源**：`FutureX-Past`（来自 [2,13]）
- **构建后的评估集 `D`**：
  - 包含 **80 个选择题型的已解决事件**
  - 事件揭晓时间范围：**2026-03-11 至 2026-04-14**
  - 类型分布：
    - Yes/No: 37
    - Binary Choice: 3
    - Multiple Choice (Single/Multi): 40 (其中 Multi-answer: 8)

> 所有问题均经过手动零泄漏审计（manual zero-leakage audit），排除题干中隐含结局线索的情况。

---

### 🧪 实验设置

#### 测试模型（共6个）：

| Model | Training Cutoff | Excluded by Cutoff |
|-------|------------------|--------------------|
| DeepSeek-V3.2-Exp | 2025-09-29 | 0 |
| GLM5 | 2026-02-11 | 0 |
| Qwen3.5-Flash | 2026-02-25 | 0 |
| MiniMax M2.5 | 2026-02-12 | 0 |
| Kimi K2.5 | 2026-01-27 | 0 |
| Doubao Seed 2.0 Lite | 2026-03-10 | 0 |

所有模型均满足 $ K_M \leq X_i < T_i $，即知识截止早于预测截止，保证无参数泄露。

#### 推理设置：
- 每个问题独立采样 **3 次（n=3）**
- ReAct 循环上限：**6 轮消息交互**
- 最多允许 **4 次搜索调用（C=4）**
- 搜索引擎：Tavily，每次返回最多 5 条结果
- 时间偏移量 $\delta = 1$ 天 → 预测截止时间为揭晓日前一天

#### 防泄漏机制（三重屏障）：
1. **训练截止准入控制**（Sample Admission）
2. **算法级日期过滤**（Tavily 的 published_date 过滤）
3. **语义级泄露检测器**（Semantic LLM Detector）：使用独立 Qwen3.5-Flash 实例判断每条检索是否包含未来信息

---

### 📊 评估指标

| 指标类别 | 具体指标 | 定义简述 |
|--------|--------|---------|
| **准确性** | Composite Accuracy | 加权平均各题型 bucket 的 exam-mean 得分 |
| | pass@1avg | 单次试验正确率的平均值（严格匹配） |
| | pass_any@n, pass_all@n | 多次试验中至少一次/全部正确的比例 |
| **一致性** | Cohen’s κ, Fleiss’ κ | 控制随机猜测后的准确率校正，衡量一致性 |
| **技能得分** | Format Skill Score (FSS) | 基于 Tversky 相似度，惩罚假阳性更重（α=2.0, β=0.5） |
| **成本效率** | Per-Correct Cost | 总花费 / 正确预测数，单位 USD |
| **泄露风险** | Residual Leakage Rate | 审计中漏检的真实泄露项占比（FN/N） |

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据（基于 80 题 × 3 次 = 240 次预测）

#### 表 1：整体性能汇总

| Model | Composite Accuracy | Total Cost (USD) | Per-Correct Cost (USD) |
|-------|--------------------|------------------|------------------------|
| DeepSeek-V3.2-Exp | **0.6016** | 3.60 | 0.025 |
| GLM5 | 0.6002 | 7.06 | 0.048 |
| Qwen3.5-Flash | 0.5896 | **0.45** | **0.003** |
| MiniMax M2.5 | 0.5494 | 3.21 | 0.024 |
| Kimi K2.5 | 0.5800 | 6.79 | 0.049 |
| Doubao Seed 2.0 Lite | 0.5858 | 0.89 | 0.006 |

> ✅ **观察**：
> - 准确率差距极小（最高 vs 最低仅差 5.2 pp），表明当前主流 LLM 在预测任务上趋于饱和。
> - 成本差异巨大：**Qwen3.5-Flash 成本最低（$0.003/正确预测）**，性价比最优。
> - DeepSeek 和 Qwen 构成 **cost-quality Pareto frontier**，其余模型被支配。

---

#### 表 2：按题型细分表现（Exam Mean）

| Model | Yes/No | Binary | MC-Single | MC-Multi |
|-------|--------|--------|-----------|-----------|
| DeepSeek-V3.2-Exp | **0.6261** | 0.8889 | 0.5938 | **0.2986** |
| GLM5 | 0.6216 | **1.0000** | 0.5729 | 0.2581 |
| Qwen3.5-Flash | 0.6036 | 0.8889 | 0.5833 | 0.2789 |
| Doubao Seed 2.0 Lite | 0.4828 | **1.0000** | **0.6061** | 0.2460 |

> 🔍 **发现**：
> - 所有模型在 **MC-Multi（多选题）** 上表现最弱（0.19–0.30），说明多答案联合预测仍是挑战。
> - Doubao 在 MC-Single 上领先，但在 Yes/No 上大幅落后，显示其泛化不均衡。
> - DeepSeek 在多个 bucket 上保持领先，综合优势明显。

---

#### 表 3：一致性与稳定性分析

| Model | pass@1avg | pass_any@n | pass_all@n | Fleiss’ κ | FSS |
|-------|----------|------------|------------|-----------|-----|
| DeepSeek-V3.2-Exp | 0.5756 | 0.8000 | 0.3500 | 0.3452 | **0.3758** |
| Qwen3.5-Flash | 0.5565 | 0.7500 | **0.3875** | **0.4515** | 0.3433 |
| Kimi K2.5 | 0.5612 | 0.8000 | 0.3000 | 0.2975 | 0.3315 |

> 🔎 **解读**：
> - Qwen 在 **Fleiss’ κ = 0.4515** 上最高，表示其多次预测结果最稳定一致。
> - Kimi 虽然 pass_any@n 高，但 pass_all@n 低，说明输出方差大。
> - FSS 更惩罚假阳性，Qwen 因在 MC-Multi 中选择字母较少而受益。

---

### 🔍 泄露率审计结果（Leakage Rate Audit）

- 审计样本：3 模型 × 30 问题 × 3 次 × 1 检索 = **270 条检索记录**
- 使用独立 Qwen3.5-Flash + 两人标注交叉验证

| 指标 | 数值 |
|------|------|
| **Recall (真实泄露检出率)** | 98.7% |
| **Specificity (非泄露保留率)** | 96.9% |
| **残余泄露率（FN/N）** | **1.1%** |
| **条件泄露穿透率（FN/(TP+FN)）** | **1.3%** |

> ✅ **结论**：相比仅使用工具层过滤（Tavily-only）的 3%-16%，OracleProto 将残余泄露降低一个数量级，达到接近人工审计水平。

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **LLM 预测可以被系统化、数据资产化**  
   OracleProto 成功将“预测”从一次性行为转化为可复现、可审计、可训练的数据对象。

2. **现有 LLM 的预测能力高度接近，但成本差异显著**  
   不同模型准确率相差不足 6 个百分点，但每正确预测的成本相差高达 **16 倍**，凸显效率优化的重要性。

3. **多答案预测仍是薄弱环节**  
   所有模型在 MC-Multi 类别上表现最差，提示需加强组合推理与不确定性建模。

4. **时间掩码 + 内容检测可有效抑制泄露**  
   三重防御机制将残余泄露控制在 **~1%** 水平，远优于单一策略。

5. **框架具备训练潜力**  
   每一条预测轨迹（检索 + 推理 + 输出）天然构成 SFT 或 RL 训练样本，支持持续优化预测能力。

---

### ⚠️ 局限性

1. **依赖外部检索系统**  
   当前框架假设模型可通过工具访问外部信息，不适用于纯自回归闭源模型。

2. **手动审计仍不可避免**  
   题干中的隐含线索（question-side cues）仍需人工筛查，自动化难度高。

3. **披露的知识截止日期不可靠**  
   模型实际训练数据范围未知，依赖厂商声明，存在潜在偏差。

4. **仅适用于选择题型**  
   开放式预测（open-ended forecasting）尚未覆盖，扩展性有待验证。

---

### 🔮 未来工作方向

1. **构建更大规模的可积累预测语料库**  
   整合 ForecastBench、Metaculus 等历史数据，打造“预测版 Common Crawl”。

2. **开发全自动的时间对齐与去偏工具链**  
   自动识别并重写带有后见之明表述的问题文本。

3. **支持开放式预测与概率输出评估**  
   引入 proper scoring rules（如 Brier Score, Log Loss）进行细粒度置信度校准。

4. **推动标准化接口与跨平台兼容性**  
   使 OracleProto 成为通用的 LLM Forecasting SDK。

5. **应用于高风险决策场景的审计追踪**  
   在金融、政策等领域提供“基于何种信息做出判断”的可解释路径。

---

> 📌 **一句话总结**：  
> **OracleProto 不只是一个评测框架，更是通往“可训练、可积累、可审计”的 LLM 预测能力基础设施的第一步。**  
> 代码与数据已开源：[GitHub](https://github.com/MaYiding/OracleProto) | [HuggingFace Dataset](https://huggingface.co/datasets/MaYiding/OracleProto)

</details>

---

### 15. [QKVShare: Quantized KV-Cache Handoff for Multi-Agent On-Device LLMs](https://arxiv.org/abs/2605.03884)

**Authors**: Pratik Honavar, Tejpratap GVSL  
**Category**: cs.AI  
**Published**: 2026-05-07  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.03884v1  

#### Abstract
Multi-agent LLM systems on edge devices need to hand off latent context efficiently, but the practical choices today are expensive re-prefill or full-precision KV transfer. We study QKVShare, a framework for quantized KV-cache handoff between agents that combines token-level mixed-precision allocati...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：QKVShare: Quantized KV-Cache Handoff for Multi-Agent On-Device LLMs

---

## 1. 论文的主要贡献和创新点

### 解决的问题
在边缘设备上的多智能体（multi-agent）LLM 系统中，当一个 agent 向另一个 agent 传递上下文时，接收方通常需要从头重新执行 **prefill** 阶段来重建 KV Cache，或者直接传输高精度（如 FP16）的完整 KV Cache。这两种方式分别导致：
- **Prefill 重计算**：浪费大量延迟（latency）
- **FP16 Cache 传输**：占用过多内存，不利于边缘设备部署

因此，如何高效地在 agent 之间传递 latent context 成为瓶颈。

### 提出的新方法与思路
作者提出 **QKVShare**，一种用于多智能体系统间 **量化 KV-Cache 交接（handoff）** 的框架，其核心创新包括：

#### ✅ Contribution 1: 跨智能体感知的 token 评分机制（Cross-agent-aware token scoring）
扩展了 "Don’t Waste Bits" 中的控制器，在原有基于本地重要性的特征（frequency, quality score, attention variance, entropy）基础上，引入两个新的跨 agent 特征：
- **Downstream Demand Signal**：估计 token 对下游 agent 的重要性
  - Segment-level prior（是否属于共享上下文段）
  - Attention anchor overlap（通过历史注意力模式预测重要性）
- 构建联合重要性得分 $ S(t) = \alpha \cdot I(t) + (1-\alpha) \cdot T(t) $，实现更合理的 bit-width 分配

#### ✅ Contribution 2: 量化 CacheCard 交接协议（Quantized CacheCard handoff）
定义了一种紧凑的数据结构 **CacheCard**，用于封装以下信息进行 agent 间传输：
- 量化后的 K/V tensors（支持 adaptive 或 uniform 量化）
- 每个 token 的 bit-width 分配向量
- 元数据（sequence length、model ID、sender ID、position offset 占位符等）
- 平均比特统计（用于评估压缩率）

#### ✅ Contribution 3: 可测量的原型分析（Measured prototype analysis）
提供了一个可运行的原型，并进行了端到端评估，涵盖：
- 多跳推理准确率（GSM8K）
- Handoff 后的 TTFT（Time To First Token）
- 阶段级延迟分解（stage-level breakdown）

此外，当前实现兼容 HuggingFace Transformers，采用 **dequantize-then-inject** 路径，便于集成与实测。

### 相比现有方法的优势
| 方法 | 局限性 | QKVShare 改进 |
|------|--------|----------------|
| 单 agent 量化（如 KIVI, KVQuant, Don’t Waste Bits） | 不考虑跨 agent 场景 | 显式建模下游需求，优化跨 agent 传输 |
| 多 agent Cache 共享（如 KVCOMM, C2C） | 使用 FP16/BF16，内存开销大 | 引入量化，显著降低传输与存储成本 |
| Q-KVComm（arXiv:2512.17914） | 层粒度量化、仅小模型验证、无 topology-aware 控制器 | **token-level 自适应量化 + 更大模型（Llama-3.1-8B）+ 显式下游感知控制** |

---

## 2. 核心实验方法和设置

### 数据集
- **GSM8K**：数学推理任务，共测试 150~300 道题目
- **合成上下文**：用于 latency 测试，构造名义上 1K、4K、8K context（实际 token 数约为 476 / 1939 / 3877）

### 实验设置
- **模型**：Meta-Llama-3.1-8B-Instruct
- **硬件**：NVIDIA RTX 5070 Ti Laptop GPU（12GB）
- **运行时环境**：
  - QKVShare：PyTorch + HuggingFace Transformers（4-bit weight quantization）
  - Baseline（llama.cpp）：FP16 实现，用于 prefilled cache restore 和 re-prefill 对比

### 评估指标
| 实验编号 | 目标 | 主要指标 |
|---------|------|----------|
| **E1** | 多跳推理准确性（2~5 hop） | GSM8K Exact Match Accuracy (%) |
| **E2** | 控制器有效性消融 | 成对比较胜率（topo vs local vs uniform） |
| **E3** | Handoff 延迟 | TTFT（Time To First Token, ms），阶段分解（create/inject/generate） |

### 基线方法对比
| 方法类别 | 描述 | 使用场景 |
|--------|------|----------|
| **FP16 re-prefill** | 接收方完全重计算 prefill | E3 下界 baseline（最慢） |
| **FP16 cache copy** | 直接复制 FP16 cache 并复用 | llama.cpp 中的最优情况 |
| **Uniform Q4/Q8 share** | 固定位宽量化共享 | E1/E3 静态量化 baseline |
| **Adaptive local** | 仅基于本地重要性分配 bit-width（无下游感知） | E1/E2 对照组 |
| **QKVShare (adaptive topology)** | 完整方法：融合本地 + 下游重要性 | 主要对比方法 |

---

## 3. 主要实验结果和性能指标

### E1: 多跳推理准确率（GSM8K, 150 problems）

| Method | 2-hop | 3-hop | 4-hop | 5-hop |
|-------|-------|-------|-------|-------|
| FP16 share | 81.33 | 76.67 | 75.33 | 72.67 |
| Uniform Q4 | 82.00 | 75.33 | 69.33 | **76.67** |
| Uniform Q8 | 82.67 | 73.33 | 69.33 | 71.33 |
| Adaptive local Q4 | 76.00 | 79.33 | 76.67 | 73.33 |
| **QKVShare topo Q4** | 78.67 | **80.67** | 77.33 | 72.00 |
| Adaptive local Q8 | 76.67 | 80.00 | 82.00 | 83.33 |
| **QKVShare topo Q8** | 76.00 | 79.33 | 82.00 | **82.67** |

> 🔍 **观察**：
> - 在约 **8-bit 预算下**，adaptive 方法明显优于 uniform，且 QKVShare 表现接近甚至略优
> - 在 **4-bit 设置下**，uniform Q4 在 5-hop 出现异常反弹（可能过拟合或噪声），整体稳定性差
> - QKVShare 的 topology-aware 控制器未在所有设置中稳定超越 local-only 控制器

---

### E2: 控制器成对比较（300 problems, ~4-bit budget）

| 比较项 | Both correct | Both wrong | Topo only 正确 | Local only 正确 | 净胜（Net） |
|--------|-------------|------------|----------------|------------------|------------|
| Topo Q4 vs Local Q4 | 223 | 59 | 10 | 8 | **+2** |
| Topo Q4 vs Uniform Q4 | 217 | 50 | 16 | 17 | **-1** |

> 📌 结论：目前证据显示 topology-aware 控制器有微弱优势，但不足以构成“决定性胜利”，仍为开放假设。

---

### E3: Handoff 后 TTFT 延迟（ms）

| Method | 1K context | 4K context | 8K context |
|--------|------------|------------|------------|
| FP16 re-prefill | 150.2 | 565.3 | 1029.7 |
| FP16 cache copy | 21.7 | 26.1 | 26.5 |
| Q4 cache reload | 26.7 | 24.7 | 24.8 |
| **QKVShare uniform Q4 handoff** | **130.7** | **152.5** | **397.1** |

> ✅ **关键优势**：
> - 相比 full re-prefill，TTFT 显著下降：
>   - 1K: ↓13%
>   - 8K: ↓61.4% （397.1 vs 1029.7 ms）
> - 尽管不如 llama.cpp 的原生 cache restore 快（~25ms），但在通用 HF 栈中已大幅优化

#### 阶段延迟分解（median, ms）
| Context | Create Card | Inject | Generate | 总计 |
|--------|--------------|--------|-----------|-----|
| 1K     | 4.4          | 13.8   | 112.4     | 130.7 |
| 4K     | 21.0         | 17.8   | 113.7     | 152.5 |
| 8K     | 71.3         | 92.8   | 232.9     | 397.1 |

> ⚠️ **瓶颈发现**：**Generate 阶段占主导**（>70%），说明当前延迟主要来自接收方的 forward pass，而非 CacheCard 创建或注入本身。

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **量化 KV Cache Handoff 显著优于 re-prefill**  
   - 在边缘设备上避免重复 prefill 可大幅降低 TTFT，尤其在长上下文（8K）下效果显著（↓61%）

2. ✅ **自适应混合精度分配具有潜力**  
   - 在较高 bit budget（~8-bit）下，adaptive 方法明显优于 uniform 量化，误差累积更可控

3. ❓ **Topology-aware 控制器尚未被充分证实优势**  
   - 当前实验未能一致证明其优于 local-only 自适应策略，需更强的消融实验支持

4. 🔍 **当前性能瓶颈不在传输而在生成阶段**  
   - Stage timing 显示，post-injection generation 是最大开销，提示未来应聚焦于 **fused quantized attention kernel** 开发

5. 💡 **CacheCard 是可行的中间表示格式**  
   - 支持灵活 bit-width 分配与元数据携带，适合作为 agent 间 latent state 交换的标准单元

---

### 局限性
| 限制 | 说明 |
|------|------|
| **混合运行时栈** | QKVShare 使用 PyTorch/HF，而 baseline 使用 llama.cpp，导致 latency 对比非“apples-to-apples” |
| **未实现 fused kernel** | 当前依赖 dequantize-then-inject，无法发挥量化 cache 的全部效率潜力 |
| **缺乏密度测量** | 未在相同 runtime 下比较并发 agent 数量（density），影响 memory efficiency 判断 |
| **模型与硬件范围有限** | 所有实验基于单一 GPU 和 Llama-3.1-8B，未覆盖移动 NPU 或异构模型 |
| **拓扑感知优势未定论** | E2 实验证据薄弱，尚不能宣称 topology-aware 分配是必要改进 |

---

### 未来工作方向
1. **开发原生 fused QKVShare kernel**  
   → 实现真正的 quantized cross-agent attention，消除 dequantization 开销

2. **统一运行时进行公平对比**  
   → 将 QKVShare 移植至 llama.cpp 或构建 HF-native baseline

3. **加强控制器消融实验**  
   → 在 ~4-bit 和 ~8-bit 下进行全面 paired testing，验证 topology-aware 是否带来稳定增益

4. **扩展至复杂拓扑结构**  
   → 测试 hierarchical / branching agent graphs，探索 segment-level prior 的泛化能力

5. **探索硬件协同设计**  
   → 结合 Oaken、MLX、QNN 等平台，推动 quantized cache sharing 的端侧落地

---

> ✅ **总体评价**：  
> QKVShare 提出了一条清晰且实用的技术路径——**将量化 KV Cache 作为多 agent 系统间的通信原语**。虽然当前原型仍有工程与实验上的局限，但它为 **on-device agentic systems** 提供了一个重要的系统优化方向：**减少冗余计算，提升上下文传递效率**。下一步的关键在于构建更完整的端到端 pipeline 并给出更强的因果证据。

</details>

---

### 16. [Memory as a Markov Matrix: Sample Efficient Knowledge Expansion via Token-to-Dictionary Mapping](https://arxiv.org/abs/2605.04308)

**Authors**: Kaustubh Pethkar, Ziyang Xiong, Zuofeng Shang, Yingcong Li  
**Category**: cs.LG  
**Published**: 2026-05-07  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.04308v1  

#### Abstract
Continual incorporation of new knowledge is essential for the long-term evolution of large language models (LLMs). Existing approaches typically rely on parameter-update algorithms to mitigate catastrophic forgetting, yet they suffer from fundamental limitations: 1) forgetting is unavoidable as the ...

---

### 17. [GraphPI: Efficient Protein Inference with Graph Neural Networks](https://arxiv.org/abs/2605.04376)

**Authors**: Zheng Ma, Jiazhen Chen, Lei Xin, Ali Ghodsi  
**Category**: cs.LG  
**Published**: 2026-05-07  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.04376v1  

#### Abstract
The integration of deep learning approaches in biomedical research has been transformative, enabling breakthroughs in various applications. Despite these strides, its application in protein inference is impeded by the scarcity of extensively labeled datasets, a challenge compounded by the high costs...

---

### 18. [AxMoE: Characterizing the Impact of Approximate Multipliers on Mixture-of-Experts DNN Architectures](https://arxiv.org/abs/2605.04754)

**Authors**: Omkar B Shende, Marcello Traiola, Gayathri Ananthanarayanan  
**Category**: cs.LG  
**Published**: 2026-05-07  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.04754v1  

#### Abstract
Deep neural network (DNN) inference at the edge demands simultaneous improvements in accuracy, computational efficiency, and energy consumption. Approximate computing and Mixture-of-Experts (MoE) architectures have each been studied as independent routes towards efficient inference, the former by re...

---

### 19. [MP-ISMoE: Mixed-Precision Interactive Side Mixture-of-Experts for Efficient Transfer Learning](https://arxiv.org/abs/2605.04058)

**Authors**: Yutong Zhang, Zimeng Wu, Shangcai Liao, Shujiang Wu, Jiaxin Chen  
**Category**: cs.LG  
**Published**: 2026-05-07  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.04058v1  

#### Abstract
Parameter-efficient transfer learning (PETL) has emerged as a pivotal paradigm for adapting pre-trained foundation models to downstream tasks, significantly reducing trainable parameters yet suffering from substantial memory overhead caused by gradient backpropagation during fine-tuning. While memor...

---

### 20. [Model synthesis and identifiability analysis of stiff chemical reaction systems with inVAErt networks](https://arxiv.org/abs/2605.04134)

**Authors**: Sreejata Dey, Guoxiang Grayson Tong, Jonathan F. MacArt, Daniele E. Schiavazzi  
**Category**: cs.LG  
**Published**: 2026-05-07  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.04134v1  

#### Abstract
We consider the problem of learning data-driven replicas for stiff systems of ordinary differential equations arising in chemical kinetics that can be evaluated with high computational efficiency. We first focus on training emulators for families of reaction equations under varying reaction rates, u...

---

### 21. [Layerwise LQR for Geometry-Aware Optimization of Deep Networks](https://arxiv.org/abs/2605.04230)

**Authors**: Simon Dufort-Labb\'e, Pierre-Luc Bacon, Razvan Pascanu, Simon Lacoste-Julien, Aristide Baratin  
**Category**: cs.LG  
**Published**: 2026-05-07  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.04230v1  

#### Abstract
Geometry-aware optimizers such as Newton and natural gradient can improve conditioning in deep learning, but scalable variants such as K-FAC, Shampoo, and related preconditioners usually impose structural approximations early, often discarding cross-layer interactions induced by the network computat...

---

### 22. [Explaining and Preventing Alignment Collapse in Iterative RLHF](https://arxiv.org/abs/2605.04266)

**Authors**: Etienne Gauthier, Francis Bach, Michael I. Jordan  
**Category**: cs.LG  
**Published**: 2026-05-07  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.04266v1  

#### Abstract
Reinforcement learning from human feedback (RLHF) typically assumes a static or non-strategic reward model (RM). In iterative deployment, however, the policy generates the data on which the RM is retrained, creating a feedback loop. Building on the Stackelberg game formulation of this interaction, w...

---

### 23. [Graph-Augmented LLMs for Swiss MP Ideology Prediction](https://arxiv.org/abs/2605.04643)

**Authors**: Yifei Yuan, Luis Salamanca, Sophia Schlosser, Laurence Brandenberger  
**Category**: cs.CL  
**Published**: 2026-05-07  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.04643v1  

#### Abstract
Approximating the ideological position of Members of Parliament (MPs) is a fundamental task in political science, helping researchers understand legislative behavior, party alignment, and policy preferences. While Large Language Models (LLMs) have shown promising results in estimating MPs' ideologic...

---

### 24. [EdgeRazor: A Lightweight Framework for Large Language Models via Mixed-Precision Quantization-Aware Distillation](https://arxiv.org/abs/2605.04062)

**Authors**: Shu-Hao Zhang, Le-Tong Huang, Xiang-Sheng Deng, Xin-Yi Zou, Chen Wu, Nan Li, Shao-Qun Zhang  
**Category**: cs.LG  
**Published**: 2026-05-07  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.04062v1  

#### Abstract
Recent years have witnessed an increasing interest in deploying LLMs on resource-constrained devices, among which quantization has emerged as a promising lightweight technique that converts full-precision model weights and activations into lower-bit formats. Existing weight quantization approaches c...

---

### 25. [FLUID: Continuous-Time Hyperconnected Sparse Transformer for Sink-Free Learning](https://arxiv.org/abs/2605.04421)

**Authors**: Waleed Razzaq, Yun-Bo Zhao  
**Category**: cs.LG  
**Published**: 2026-05-07  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.04421v1  

#### Abstract
Continuous-time (CT) Transformers improve irregular and long-range modeling over CT-RNNs by exploiting inputs or outputs embeddings with continuous dynamics. However, the core scaled-dot-product-attention (SDPA) mechanism remains inherently discrete. We propose FLUID (Flexible Unified Information Dy...

---

### 26. [Quantile-Free Uncertainty Quantification in Graph Neural Networks](https://arxiv.org/abs/2605.04847)

**Authors**: Soyoung park, Hwanjun Song, Sungsu Lim  
**Category**: cs.LG  
**Published**: 2026-05-07  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.04847v1  

#### Abstract
Uncertainty quantification (UQ) in graph neural networks (GNNs) is crucial in high-stakes domains but remains a significant challenge. In graph settings, message passing often relies on strong assumptions such as exchangeability, which are rarely satisfied in practice. Moreover, achieving reliable U...

---

### 27. [Self-Improvement for Fast, High-Quality Plan Generation](https://arxiv.org/abs/2605.03625)

**Authors**: Robert Gieselmann, Henrike von Huelsen, Mihai Samson, Marie-Christine Meyer, Dariusz Piotrowski, Oleksandr Radomskyi, Justin Okamoto, Turan Gojayev, Michael Painter, Gavin Brown, Federico Pecora, Jeremy L. Wyatt  
**Category**: cs.AI  
**Published**: 2026-05-07  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.03625v1  

#### Abstract
Generative models trained on synthetic plan data are a promising approach to generalized planning. Recent work has focused on finding any valid plan, rather than a high-quality solution. We address the challenge of producing high-quality plans, a computationally hard problem, in sub-exponential time...

---

### 28. [Agent-Based Modeling of Low-Emission Fertilizer Adoption for Dairy Farm Decarbonisation using Empirical Farm Data](https://arxiv.org/abs/2605.03648)

**Authors**: Surya Jayakumar, Kieran Sullivan, John McLaughlin, Christine OMeara, Indrakshi Dey  
**Category**: cs.AI  
**Published**: 2026-05-07  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.03648v1  

#### Abstract
To understand complex system dynamics in dairy farming, it is essential to use modeling tools that capture farm heterogeneity, social interactions, and cumulative environmental impacts. This study proposes an agent-based modeling (ABM) framework to simulate nitrogen management and the adoption of lo...

---

### 29. [Quantifying the human visual exposome with vision language models](https://arxiv.org/abs/2605.03863)

**Authors**: Christian Rominger (University of Graz), Andreas R. Schwerdtfeger (University of Graz), Malay Gaherwar Singh (TU Dresden), Dimitri Khudyakow (TU Dresden), Elizabeth A. M. Michels (TU Dresden), Fabian Wolf (TU Dresden), Jakob Nikolas Kather (TU Dresden, University Hospital Carl Gustav Carus Dresden, National Center for Tumor Diseases Heidelberg), Magdalena Katharina Wekenborg (TU Dresden)  
**Category**: cs.AI  
**Published**: 2026-05-07  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.03863v1  

#### Abstract
The visual environment is a fundamental yet unquantified determinant of mental health. While the concept of the environmental exposome is well established, current methods rely on coarse geospatial proxies or biased self reports, failing to capture the first person visual context of daily life. We a...

---

### 30. [MedFabric and EtHER: A Data-Centric Framework for Word-Level Fabrication Generation and Detection in Medical LLMs](https://arxiv.org/abs/2605.04180)

**Authors**: Tung Sum Thomas Kwok, Qian Qian, Xiaofeng Lin, Dongxu Zhang, Jun Han, Zhichao Yang, Davin Hill, Tamer Soliman, Sanjit Singh Batra, Robert Tillman, Guang Cheng  
**Category**: cs.CL  
**Published**: 2026-05-07  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.04180v1  

#### Abstract
Large Language Models exhibit strong reasoning and semantic understanding capabilities but often hallucinate in domains that require expert knowledge, among which fabrications, the generation of factually incorrect yet fluent statements, pose the greatest risk in medical contexts. Existing medical h...

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
