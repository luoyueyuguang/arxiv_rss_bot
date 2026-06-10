# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-06-10 09:12:40 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG

## 📚 Recent Papers

### 1. [Density Field State Space Models: 1-Bit Distillation, Efficient Inference, and Knowledge Organization in Mamba-2](https://arxiv.org/abs/2606.10932)

**Authors**: Chirag Shinde  
**Category**: cs.CL  
**Published**: 2026-06-10  
**Score**: 12.5  
**Type**: new  
**ArXiv ID**: 2606.10932v1  

#### Abstract
We present Density Field State Space Models (DF-SSM), a framework for compressing SSMs to a 1-bit scaffold with int8 low-rank correction. Applied to Mamba-2 1.3B, we achieve a 278 MB model (9.7x smaller than the 2.7 GB FP16 teacher) that runs at 21.4x faster inference on GPU (batch=1, relative to th...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：**Density Field State Space Models: 1-Bit Distillation, Efficient Inference, and Knowledge Organization in Mamba-2**

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
当前大型语言模型（LLM）参数量大、内存占用高，难以部署在边缘设备（如手机、嵌入式系统）上。尽管已有量化方法（如 4-bit 或更低），但在极端压缩下通常导致显著性能下降，且训练成本高昂。

此外，**State Space Models**（SSMs）虽具备固定大小的隐藏状态（无 KV cache 膨胀），适合长序列建模，但其权重压缩研究远不如 Transformer 成熟。

### 🚀 提出的新方法：**Density Field State Space Models (DF-SSM)**

作者提出了一套完整的从 FP16 教师模型蒸馏到超低比特 SSM 的流程，核心包括三个阶段：

1. **Density Field Weights (DFW) 训练**
   - 使用 17-level 量化（-1 到 +1）结合量化感知蒸馏（quantization-aware distillation）
   - 引入**退火机制**（annealing）：从连续权重平滑过渡到离散二值化，避免“质量悬崖”（quality cliff）

2. **冻结的 1-bit 支架 + int8 LoRA 修正**
   - 主干权重被**确定性舍入为 1-bit**（称为 scaffold），并**冻结**
   - 使用一个小型的 **int8 低秩适配器**（LoRA, rank=16）来恢复因量化损失的信息
   - LoRA 并非简单纠正单个权重重塑误差，而是学习输入加权输出误差的补偿

3. **高效推理实现**
   - **GPU 推理**：利用 `cuBLAS INT8 tensor cores` 处理 scaffold 矩阵乘法；自定义 CUDA kernel 实现 SSM 和卷积操作；通过 CUDA graph 捕获消除内核启动开销
   - **CPU 推理**：基于 AVX-512 VNNI 指令实现 bit-packed 权重展开与加速
   - 所有 LoRA 参数和 embedding 层均实现 **lossless int8 量化**

### 🔍 相比现有方法的优势

| 方面 | DF-SSM 的优势 |
|------|----------------|
| **压缩效率** | 达到 **9.7× 压缩比**（2.7GB → 278MB），其中 scaffold 占 155MB（1-bit） |
| **推理速度** | GPU 上 **21.4× 加速**（batch=1），CPU 上达 2.9× 加速 |
| **训练成本** | 蒸馏仅需 **32M tokens / 6 小时 / 单块 A100**，远低于从头训练的 BitMamba-2（150B tokens） |
| **性能保留** | 在多个下游任务中接近 BitMamba-2（1.58-bit 模型），差距仅 2–4 个百分点 |
| **架构新颖性** | 首次将 **混合精度思想**（binary scaffold + int8 LoRA）引入 SSM 压缩，区别于统一低比特训练 |

---

## 2. 核心实验方法和设置

### 📚 数据集与训练配置

- **教师模型**：Mamba-2 1.3B（FP16，2.7GB）
- **蒸馏数据**：**32M tokens**（来自预训练语料子集）
- **DFW 训练**：
  - 序列长度：512
  - Batch size：4
  - 学习率：3e-4，余弦衰减
  - 退火参数 α 从 0→1 over 12.3M tokens
- **LoRA 微调**：
  - Rank：16
  - 所有 48 层的 `in_proj` 和 `out_proj`
  - 训练 20M tokens，学习率 1e-3

### 📊 评估指标

| 类别 | 指标 |
|------|------|
| **通用能力** | Perplexity (PPL) |
| **下游任务** | BoolQ, PIQA, HellaSwag, WinoGrande, ARC-easy（准确率 %） |
| **推理效率** | 吞吐量（tokens/s），GPU/CPU 对比 |
| **知识组织分析** | 因果干预（causal intervention）、类别聚类、logit lens 分析等 |

### ⚔️ 基线方法对比

| 方法 | 架构 | 精度 | Tokens | 总大小 | 备注 |
|------|------|-------|--------|--------|------|
| **Bi-Mamba** | Mamba-1 | 1-bit | 105B | — | 从头训练 |
| **BitMamba-2** | Mamba-2 | 1.58-bit | 150B | ~300MB+ | 当前最强 1.x-bit SSM |
| **QLoRA** | Transformer | NF4 (4-bit) + LoRA | ~1B | — | 类似架构理念，但更高位宽 |
| **本工作 (DF-SSM)** | Mamba-2 | **1-bit scaffold + int8 LoRA** | **32M (distill only)** | **278MB** | 本文方案 |

> 注：比较不包含教师模型的预训练成本（300B+ tokens），仅关注蒸馏阶段效率。

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据

#### ✅ 模型大小与压缩比

| 组件 | 精度 | 大小 | 占比 |
|------|------|------|------|
| Scaffold（投影层） | 1-bit | 155 MB | 56% |
| Embedding + LM Head | int8 | 103 MB | 37% |
| LoRA Correction | int8 | 12 MB | 4% |
| 其他（conv, norm, SSM param） | FP16/FP32 | 8 MB | 3% |
| **总计** | — | **278 MB** | — |
| 教师模型（FP16） | FP16 | 2,688 MB | — |
| **压缩比** | — | **9.7×** | — |

#### ✅ 推理速度（A100 GPU, batch=1）

| Batch Size | FP16 (mamba-ssm) | DF-SSM | Speedup |
|------------|------------------|--------|---------|
| 1 | 14 tok/s | **299 tok/s** | **21.4×** |
| 8 | 116 tok/s | 647 tok/s | 5.6× |
| 32 | 482 tok/s | 1,963 tok/s | 4.1× |
| 512 | — | 5,081 tok/s | 接近 HBM 带宽极限 |

> 💡 加速来源：
> - 8× 减少内存加载（bit-packed weights）
> - INT8 tensor core 更高吞吐
> - CUDA graph 消除 launch overhead
> - 固定状态缓存避免重复计算

#### ✅ 下游任务表现（Accuracy %）

| Task | Random | DF-SSM | Teacher (FP16) | BitMamba-2 | Retention |
|------|--------|--------|---------------|-------------|-----------|
| BoolQ | 50.0% | **60.8%** | 64.2% | 62.4% | 94.7% |
| PIQA | 50.0% | **67.1%** | 73.2% | 68.8% | 91.7% |
| HellaSwag | 25.0% | **41.4%** | 59.9% | 45.6% | 69.1% |
| WinoGrande | 50.0% | **54.7%** | 60.9% | 52.8% | 89.8% |
| ARC-easy | 25.0% | **50.2%** | 64.1% | — | 78.3% |

> 🔹 DF-SSM 在四项任务中保留教师模型 **78–95% 的性能**
> 🔹 在 WinoGrande 上甚至超过 BitMamba-2（+1.9 pp）
> 🔹 HellaSwag 表现较弱，归因于多步推理能力不足 + 蒸馏数据有限

#### ✅ 消融实验（Table 4）

| 配置 | PPL | 说明 |
|------|-----|------|
| 教师模型（FP16） | 14.3 | 原始高质量模型 |
| 仅 scaffold（无 LoRA） | 101.5 | 性能崩溃 |
| scaffold + LoRA (FP16) | 49.2 | 显著恢复 |
| scaffold + LoRA (int8) | **49.1** | **lossless 量化**
| scaffold + LoRA (int4) | 52.9 | 开始退化 |

> ✅ 表明：**LoRA 是关键修复组件**，且 **int8 量化可完全无损**

---

## 4. 关键结论和发现

### 🧠 主要发现

#### 🔹 发现一：SSM 内部存在 **三阶段处理流程**（Three-Phase Processing）

通过对 445 个事实提示（across 19 categories）进行系统分析，识别出三个明确的功能阶段：

| 阶段 | 层数 | 功能 | 证据 |
|------|------|------|------|
| **分类（Categorize）** | L0–L3 | 识别问题类型（intent classification） | 类别聚类峰值出现在 L3 |
| **检索（Recall）** | L25–L35 | 提取具体事实 | 因果干预显示 L32–L36 是知识定位窗口 |
| **格式化（Format）** | L36–L47 | 输出结构生成 | 所有类别表示趋于一致，准备输出 token |

#### 🔹 发现二：早期分类是 **语法驱动而非语义驱动**

- 早期层（L2）的分类效果取决于模板一致性：
  - **Tier 1（模板相同）**：如 *“The capital of [X] is”* → continents/currencies 分离明显（+0.55）
  - **Tier 3（模板多样）**：如 physics/medical/music → 几乎无法聚类
- 表明模型先识别句式结构，再激活对应的知识路径

#### 🔹 发现三：存在 **抽象意图空间**（Abstract Intent Space）

- 在 L0–L3，虽然可以高精度分类问题类型（94%），但通过 **logit lens** 投影后输出的是无意义 token（如 "dust", "undle"）
- 直到 L27 之后才出现可读词汇（如 "located", "author"）
- 说明：**语义尚未对齐词汇空间**，存在一个独立的抽象表征阶段

#### 🔹 发现四：**结构先于强度**（Structure Precedes Strength）

- 尽管模型整体 PPL 较差（49.2 vs 教师 14.3），且很少输出正确答案（top-1 accuracy 低）
- 但其内部知识组织高度有序：
  - 知识集中在 **L32–L36 的 5 层窗口**
  - 可用 **10–16 维 PCA 子空间** 完美区分 10 个首都城市
  - 因果干预响应一致
- 暗示：**表征结构可能独立于事实强度发展而来**

---

### ⚠️ 方法的局限性

| 限制 | 说明 |
|------|------|
| **依赖教师模型** | 必须有一个高质量 FP16 教师，无法从零开始训练 |
| **PPL 仍较高** | 49.2 vs 教师 14.3，仍有约 3.4× 差距，可通过更长 LoRA 训练改善 |
| **HellaSwag 表现弱** | 多跳推理能力受限，可能因蒸馏数据不足 |
| **解释性结果泛化性未知** | 三阶段结构是否适用于其他 SSM 架构或规模尚待验证 |
| **“1-bit”标签需澄清** | 实际为混合精度：核心 scaffold 是 1-bit，embedding 和 LoRA 仍是 int8 |

---

### 🔮 未来工作方向

1. **追踪结构演化过程**：在从头训练的不同 checkpoint 中观察三阶段是否逐步形成
2. **探索更高效的蒸馏策略**：如分层蒸馏、动态 LoRA 分配
3. **扩展至其他架构**：应用于 Transformer、Diffusion Models（如 SDXL → ~1GB）
4. **提升 factual recall**：结合知识编辑技术（如 MEMIT）注入强事实记忆
5. **轻量化部署优化**：进一步支持移动端 ONNX/TFLite 导出与推理

---

## ✅ 总结

该论文提出了 **DF-SSM**——一种面向 Mamba-2 的极高压缩比蒸馏框架，在 **仅 32M tokens 和单卡 A100 上 6 小时训练** 内，实现了：

- **278MB 模型大小**（9.7× 压缩）
- **21.4× GPU 推理加速**
- **下游任务性能接近 1.58-bit 从头训练模型**

更重要的是，首次对 SSM 进行了系统的可解释性分析，揭示了：
- **三阶段信息处理机制**
- **语法优先的早期分类行为**
- **抽象意图空间的存在**
- **结构可能先于事实强度形成**

这不仅推动了高效部署技术的发展，也为理解 SSM 内部工作机制提供了全新视角。

</details>

---

### 2. [Sim2Schedule: A Simulator-Guided LLM Framework for Autonomous Open-Pit Mine Scheduling](https://arxiv.org/abs/2606.10286)

**Authors**: Mustavi Ibne Masum, Thiago Eustaquio Alves de Oliveira, Mahzabeen Emu  
**Category**: cs.AI  
**Published**: 2026-06-10  
**Score**: 11.5  
**Type**: new  
**ArXiv ID**: 2606.10286v1  

#### Abstract
Open-pit mine scheduling is a critical process for maximizing economic return under complex geotechnical and operational constraints. While Mixed-Integer Linear Programming (MILP) provides mathematically optimal baselines, its exponential computational complexity and inability to adapt in real time ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Sim2Schedule: A Simulator-Guided LLM Framework for Autonomous Open-Pit Mine Scheduling

---

## 1. 论文的主要贡献和创新点

### ✅ 解决了什么问题

**Open-pit mine scheduling (OPPS)** 是一个复杂的组合优化问题，目标是在满足地质、工程和运营约束的前提下，最大化项目的净现值（NPV）。传统方法如 **Mixed-Integer Linear Programming (MILP)** 虽然能提供数学最优解，但存在以下问题：

- **计算复杂度高**：随着矿块数量增加，求解时间呈指数增长，难以应对大规模实例。
- **缺乏实时适应性**：无法在动态环境中快速响应设备故障、品位变化等现实扰动。
- **输出不可解释**：原始求解器输出需后处理才能被矿场规划师理解。

此外，现有 MILP 模型常忽略关键物理现实，例如：
- 允许部分开采即加工（违反实际爆破流程）
- 忽略斜坡稳定性要求的严格空间前序关系
- 固定产能下限导致矿末期无解

### 🚀 提出的新方法与创新思路

本文提出 **Sim2Schedule** —— 一种基于 **Large Language Model (LLM)** 和 **定制化模拟器** 协同工作的零样本（zero-shot）自主调度框架，其核心思想是：

> 将 LLM 视为决策代理（decision-making agent），而将领域知识（geotechnical precedence, capacity limits, extraction-processing coupling）完全编码进一个轻量级模拟器中，由模拟器在每一步生成合法动作集并引导 LLM 进行选择。

#### 主要创新点包括：

| 创新维度 | 内容说明 |
|--------|--------|
| **LLM 应用范式创新** | 首次将 LLM 用于长期战略性的块体开采序列规划（long-horizon OPPS），而非仅限于短期任务（如卡车调度） |
| **Simulator-in-the-loop 架构** | 模拟器负责约束验证与状态演化，LLM 专注价值推理，实现“感知-决策”分离，提升鲁棒性和可解释性 |
| **零样本闭源部署** | 不依赖云服务、无需 fine-tuning 或 retraining，在本地安全环境中运行，保障数据隐私 |
| **新型 MILP 基准模型** | 提出更贴近现实的 MILP 公式，引入：<br>• 动态产能下限机制（dynamic lower bound）<br>• 显式 3D 前序块集合构造<br>• 辅助二元变量确保严格开采-加工耦合 |

### 🔍 相比现有方法的优势

| 维度 | Sim2Schedule (LLM + Simulator) | 传统 MILP | 启发式方法（Greedy/Random） |
|------|-------------------------------|----------|-----------------------------|
| **可扩展性** | ✅ 线性时间增长 `O(N)` | ❌ 指数级 `O(2^N)` | ✅ 快速但质量差 |
| **实时适应性** | ✅ 支持在线调整与干预 | ❌ 批处理模式，黑盒运行 | ✅ 可即时执行 |
| **可解释性** | ✅ 输出结构化日志，支持逐周期审计 | ❌ 输出为变量向量，需解析 | ⚠️ 动作可见但逻辑不透明 |
| **解决方案质量** | ✅ 达到 MILP 最优解的 **94%-99% NPV** | ✅ 全局最优（理论上） | ❌ 显著低于最优 |
| **部署成本** | ✅ 本地运行，无需专家建模 | ❌ 依赖专业软件与调参 | ✅ 简单易实现 |

---

## 2. 核心实验方法和设置

### 📊 数据集与仿真环境

- 使用合成的 **3D block-structured grid** 矿体模型，包含不同规模的测试实例：
  - 区块数：18, 27, 36, 45
  - 时间周期：最多 15 期
- 每个区块包含属性：`ore_tonnage`, `waste_tonnage`, `grade`, `revenue`, `cost`
- 统一设定：每个区块质量为 50 吨
- 经济参数：
  - 加工收入：\$100/吨
  - 开采成本：\$10/吨
  - 折现率：`r = 0.1`

### ⚙️ 实验设置

| 组件 | 设置详情 |
|-----|---------|
| **LLM 模型** | 两个开源模型：<br>• **GPT-OSS (20B)**<br>• **DeepSeek-R1 (14B)**<br>均通过 Ollama 在本地部署 |
| **提示设计** | 结构化 prompt：<br>• 系统指令定义角色与目标（maximize NPV）<br>• 每轮输入当前 mine state 与可行动作列表<br>• 强制输出 JSON 格式动作 |
| **模拟器功能** | • 实时维护 mine state<br>• 自动识别可行动作（extract/process）<br>• 执行动作并更新资源容量与时间步 |
| **MILP 求解器** | Gurobi Optimizer v13.0.0，设置相对最优容忍度 5%（大实例） |

### 🎯 评估指标

| 指标 | 定义 |
|------|------|
| **NPV** | 净现值，主目标函数 |
| **Optimality Gap** | `(NPV_MILP - NPV_agent) / NPV_MILP` |
| **Execution Time** | 总运行时间（秒），对数尺度比较 |
| **Operational Transparency** | 是否输出可读调度日志 |
| **Constraint Satisfaction** | 是否满足所有 geotechnical 与 operational 约束 |

### 🆚 基线方法对比

| 方法 | 描述 |
|------|------|
| **MILP** | 新提出的增强型公式，作为黄金标准基准 |
| **Greedy Heuristic** | 每步选择即时 NPV 最高的动作 |
| **Random Agent** | 从可行集中随机选动作 |
| **LLM (No Context)** | 不提供实时 mine state 的消融版本 |

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据

#### 表格：不同方法在各规模下的 NPV 与耗时对比（节选自 Table 4）

| Method | N=18 | N=27 | N=36 | N=45 |
|-------|------|------|------|------|
| **MILP**<br>NPV (\$) / Time (s) | 24,650 / 3,248 | 25,694 / 437 | 25,694 / 3,200 | 25,664 / 12,603 |
| **GPT-OSS (Context)**<br>NPV (\$) / Time (s) | 24,083 / 1,528 | 24,279 / 1,314 | 25,631 / 1,620 | 25,369 / 1,880 |
| **NPV Ratio** | 97.7% | 94.5% | 99.75% | 98.85% |
| **Speedup vs MILP** | ~2x | ~0.3x | ~2x | ~6.7x |

> 注：N=27 时 MILP 因较快找到近似解而耗时较短；N=45 时 MILP 已无法收敛至全局最优（终止间隙 5–6%）

#### 图表观察（Fig. 6–7）：
- **LLM (with context)** 的 NPV 显著优于 Greedy 和 Random，接近 MILP 曲线
- **LLM (no context)** 与 Greedy 表现几乎一致，说明上下文输入至关重要
- 随着区块数增加，MILP 时间急剧上升，而 LLM 增长平缓

### 🔁 消融实验结果

#### （1）**上下文刷新频率的影响（Fig. 11）**

- **Refresh Size = 1**（只保留最新状态）效果最好（NPV \$12,455）
- **Full History** 反而导致性能下降（NPV \$11,988）
- ➤ 表明 LLM 更关注局部状态变化，过长的历史会引入噪声

#### （2）**是否提供环境上下文（Table 3）**

| 方法 | Period 10 NPV (\$) |
|------|-------------------|
| LLM (Context) | 19,455.93 |
| LLM (No Context) | 19,062.21 |
| Greedy | 19,062.21 |

➤ 证明：**没有实时环境反馈时，LLM 退化为 Greedy 策略**

#### （3）**调度序列可视化（Fig. 9）**

- Gantt 图显示：GPT-OSS 与 DeepSeek 在相同实例上生成了**完全相同的开采顺序**
- 且整体结构高度匹配 MILP 的优先级策略（先剥岩后采高品位区）
- ➤ 表明该框架具有良好的策略一致性与复现能力

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **Sim2Schedule 能高效逼近 MILP 最优解**  
   在多种规模下恢复 **94%~99% 的 MILP NPV**，同时将计算时间控制在合理范围内。

2. **Simulator-in-the-loop 架构有效分离职责**  
   模拟器处理硬约束，LLM 专注长期价值判断，避免 LLM “幻觉”违反物理规则。

3. **零样本 LLM 具备强泛化能力**  
   无需 fine-tuning，仅靠预训练推理 + 结构化 prompt 即可在复杂工业场景做出高质量决策。

4. **实时上下文是性能关键**  
   提供动态 mine state 显著优于静态或无上下文设置，使 LLM 能进行前瞻性规划。

5. **线性可扩展性优于传统优化器**  
   对大规模问题（如 N=45），LLM 方法速度可达 MILP 的 **6倍以上**，适合实际部署。

6. **操作透明性显著提升**  
   每一步输出结构化日志（如 Fig. 10），便于工程师监控、调试和干预。

### ⚠️ 局限性

- **仍存在小幅度 optimality gap**：平均落后 MILP 约 1–6%，尚未达到理论最优
- **依赖良好 prompt engineering**：若提示不当可能导致行为偏差
- **未考虑不确定性**：当前模型假设品位、价格等均为确定值，未集成概率推理
- **LLM 推理延迟较高**：尽管总时间可控，但单步响应慢于纯启发式算法

### 🔮 未来工作方向

1. **引入不确定性建模**：将地质品位波动、市场价格变化纳入 simulator state
2. **多智能体协作架构**：多个 LLM 分别负责开采、运输、加工子系统协同优化
3. **强化学习微调**：利用历史调度数据对 LLM 进行 RLHF 微调以进一步缩小差距
4. **真实矿山验证**：在实际大型 block model 上测试框架有效性
5. **Prompt 自动优化**：研究自动化 prompt tuning 方法以降低人工设计成本

---

## ✅ 总结一句话

> **Sim2Schedule 成功将 LLM 从“文本生成器”转变为“自主工业决策代理”，通过 simulator-guided 架构实现了在开放坑矿调度这一经典 NP-hard 问题上的高性能、高可解释性与强可扩展性的统一，为复杂系统的智能化调度提供了新范式。**

</details>

---

### 3. [PADD: Path-Aligned Decompression Distillation for Non-Router Teacher to Guide MoE Student Learning](https://arxiv.org/abs/2606.10369)

**Authors**: Xinyue Peng, Yi Qian, Jiaojiao Lin, Wenjian Shao, Yanming Liu  
**Category**: cs.CL  
**Published**: 2026-06-10  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2606.10369v1  

#### Abstract
As large language models (LLMs) continue to scale, it becomes increasingly challenging to grow model capacity under fixed computation budgets. We propose Path-Aligned Decompression Distillation (PADD), a framework for distilling knowledge from dense teachers without explicit routing into mixture-of-...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文《PADD: Path-Aligned Decompression Distillation for Non-Router Teacher to Guide MoE Student Learning》核心总结

---

## 1. 论文的主要贡献和创新点

### 解决的问题
该论文针对 **dense-to-MoE 知识蒸馏中的结构性挑战**，解决了以下四个核心问题：
- **Router Cold Start**：MoE 学生模型的路由机制在训练初期缺乏监督信号，导致路由决策随机，专家功能同质化。
- **Capacity Gap**：当 MoE 学生的激活参数远小于 dense 教师时，难以吸收教师细粒度的 logits 输出。
- **Path Rupture**：离散的路由选择破坏了 chain-of-thought 的连续性，造成梯度不稳定。
- **Expert Homogenization**：传统负载均衡仅控制激活频率，忽略专家质量，导致专家趋于同质。

### 提出的新方法：PADD
提出 **Path-Aligned Decompression Distillation (PADD)**，一个四阶段统一框架，将 dense 教师的知识与推理路径对齐地蒸馏到 MoE 学生中：

#### 四个阶段概述：
| 阶段 | 名称 | 功能 |
|------|------|------|
| **Stage I** | Neuron-Cluster-Based Expert Initialization and Warmup | 基于教师 FFN 神经元聚类初始化学生专家，并通过 warmup 赋予其差异化功能 |
| **Stage II** | Online Adaptive Distillation | 在前向传播中动态调整教师温度，根据学生路径表现提供平滑监督 |
| **Stage III** | PR-GRPO Path-Refined Policy Optimization | 引入路由偏移抑制机制，稳定策略梯度更新 |
| **Stage IV** | Reward-Augmented Load Balancing | 结合激活频率与专家性能奖励，提升高质量专家的优先级 |

### 相比现有方法的优势
- **无需 MoE-to-MoE 匹配**：可直接从无路由的 dense 教师指导 MoE 学生，避免 MoE-to-MoE 蒸馏的兼容性问题。
- **端到端联合优化**：将知识蒸馏、策略学习、负载均衡整合为单一训练流程，实现协同优化。
- **更强的泛化能力**：相比固定温度蒸馏，PADD 更好地保留了非数学任务的通用能力。
- **更高的效率-性能平衡**：在相同推理成本下，MoE 学生可超越 dense 教师。

---

## 2. 核心实验方法和设置

### 数据集
- **训练数据**：`DeepScaleR`（大规模数学推理数据集，含 AIME、AMC、MATH500 等竞赛题）
- **评估数据集（未参与训练）**：
  - 数学推理：`AIME24`, `AMC23`, `MATH500`, `Minerva`, `OlympiadBench`
  - 非数学泛化：`MMLU-Pro`（多学科理解）、`MultiPL-E` / `LiveCodeBench v6`（代码生成）、`HumanEval` / `MBPP`

### 实验设置
- **模型对**：
  - **Qwen 家族**：Qwen2.5-Math-7B (dense teacher) → Qwen3-30B-A3B (MoE student, 3.3B active / 30.5B total)
  - **DeepSeek 家族**：DeepSeek-Math-7B → DeepSeek-V2-Lite (2.4B active / 16B total)
- **训练流程划分**：
  - `DA`: 聚类统计（10%）
  - `DB`: 专家 warmup（20%）
  - `Dc`: 主训练（65%）
  - `Dp`: 评估（5%）
- **评估协议**：Pass@1 准确率，AIME24 平均 32 次采样以增强稳定性

### 基线方法对比
| 基线 | 描述 |
|------|------|
| **Base** | 未经训练的预训练 MoE 学生 |
| **Dense-GRPO** | 与学生激活参数相当的 dense 模型进行 GRPO 训练 |
| **MoE-Vanilla-GRPO** | MoE 学生仅用 GRPO，无蒸馏 |
| **RSPO** | 加入路由偏移加权的 GRPO |
| **GSPO** | 序列级重要性比率剪裁的 GRPO 变体 |
| **Online KD** | 固定温度的在线知识蒸馏 + GRPO |
| **Teacher (GRPO)** | 教师模型经 GRPO 微调后的上限参考 |

---

## 3. 主要实验结果和性能指标

### 关键性能数据（Table 1）
| 方法 | Qwen 家族 (Avg) | DeepSeek 家族 (Avg) |
|------|------------------|---------------------|
| Teacher (GRPO) | 77.7% | 58.1% |
| Base | 72.9% | 37.2% |
| Dense-GRPO | 53.5% | 45.6% |
| Online KD | 73.6% | 46.7% |
| RSPO | 77.2% | 54.3% |
| **PADD (Ours)** | **80.2%** | **55.2%** |

> ✅ **PADD 在 Qwen 家族上超越教师 2.5 个百分点，在 DeepSeek 上接近教师（差距仅 2.9%）**

### 与基线方法的对比优势
- **vs. Vanilla-GRPO**：+8.8% (Qwen), +8.4% (DeepSeek) → 显示蒸馏机制的关键作用
- **vs. Online KD**：+6.6% (Qwen), +8.5% (DeepSeek) → 显示自适应蒸馏优于固定温度
- **vs. RSPO/GSPO**：+3.0%/+3.9% (Qwen) → 显示 PR-GRPO 和 reward-augmented load balancing 的增益
- **vs. Dense-GRPO**：+26.7% (Qwen), +9.6% (DeepSeek) → 显示 MoE 架构在相同激活参数下的表达优势

### 消融实验结果（Ablation Study）
| 移除阶段 | Qwen Avg ↓ | 主要影响 |
|---------|------------|----------|
| **w/o Stage I** | -6.1% | 最大降幅，验证专家初始化对缓解 cold start 至关重要 |
| **w/o Stage II** | -5.1% | 固定温度无法应对 capacity gap，尤其在 OlympiadBench 下降 9.9pt |
| **w/o Stage III** | -2.6% | 路由跳跃加剧，Minerva 下降 3.8pt，显示 PR-GRPO 对路径连续性的保护 |
| **w/o Stage IV** | -1.5% | 尽管影响较小，但在后期减缓专家同质化，提升长期分工 |

> 📊 完整消融见 Appendix E，所有组件均被证明必要。

---

## 4. 关键结论和发现

### 主要发现
1. **MoE 学生可在相同推理成本下超越 dense 教师**：PADD 成功实现了“知识解压缩”，将紧凑但专业的 dense 教师知识扩展至更广的 MoE 专家空间。
2. **结构先验至关重要**：Stage I 的神经元聚类与 warmup 显著提升了专家专业化程度（NMI 提升 130%），是解决 router cold start 的根本手段。
3. **动态路径对齐蒸馏有效**：Online Adaptive Distillation 根据学生路径质量动态调节监督强度，避免过拟合错误路径。
4. **PR-GRPO 显著提升路由稳定性**：
   - 路由偏移（Router-shift）从 Vanilla-GRPO 的 ~0.35 降至 **0.18–0.21**
   - ECDF 曲线左移且尾部更轻，表明高波动样本大幅减少
5. **泛化能力强**：在非数学任务上（Table 2），PADD 接近甚至超过 Base 模型，显著优于其他 RL 方法（如 Online KD 导致更大退化）。

### 方法的局限性
- **依赖高质量教师的模块化结构**：若 dense 教师内部表示高度纠缠，则 Stage I 的聚类效果受限。
- **训练开销增加**：因需在线查询教师，训练时间增加约 **20–32%**（见 Table 6），但推理成本不变。
- **领域迁移需重新初始化**：跨领域应用需重新运行 Stage I 的聚类与 warmup。
- **不适用于从零构建 MoE**：PADD 假设学生已是预训练 MoE，而非从 dense checkpoint 转换而来。

### 未来工作方向
- 扩展至更大规模教师（如 34B/70B），探索离线索引或渐进式蒸馏。
- 自动化聚类质量诊断与鲁棒化流程（如 GMM+BIC 自动选簇数）。
- 将 PADD 思路应用于 vision 或 multimodal MoE 模型。
- 探索多教师协作蒸馏，融合多个 domain-specialized 教师的知识。

---

> 🔚 **总结**：PADD 提供了一种**原则性强、高效实用**的 dense-to-MoE 蒸馏范式，成功弥合了架构鸿沟，在保持低推理成本的同时，使 MoE 学生不仅匹配、甚至超越其 dense 教师，为大规模语言模型的经济化扩展提供了新路径。

</details>

---

### 4. [RATrain: A Resource-Aware Training Runtime for Large Language Models on Bandwidth-Constrained Heterogeneous Supercomputing Platforms](https://arxiv.org/abs/2606.10415)

**Authors**: Yao Lu, Shiqing Ma, Zhongzhi Luan, Gen Li, Jiaxing Qi, Bin Han, Hailong Yang, Depei Qian  
**Category**: cs.DC  
**Published**: 2026-06-10  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2606.10415v1  

#### Abstract
Production heterogeneous supercomputing platforms are increasingly used to host large language model (LLM) training workloads. However, existing GPU-oriented training runtimes typically rely on high-bandwidth device memory, fast interconnects, and mature collective communication libraries, making th...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：RATrain: A Resource-Aware Training Runtime for Large Language Models on Bandwidth-Constrained Heterogeneous Supercomputing Platforms**

---

## 1. **论文的主要贡献和创新点**

### **解决了什么问题**
当前主流的 **LLM training runtime**（如 Megatron-LM、DeepSpeed）是为 **GPU集群** 设计的，依赖以下假设：
- 高带宽设备内存（HBM）
- 快速互联（NVLink/NVSwitch）
- 成熟的集合通信库（NCCL）

然而，在 **带宽受限的异构超级计算平台**（如 MT-3000）上，这些假设不成立：
- 显式的内存层次（SM/AM/GSM/DDR）
- 每计算集群仅 **20GB 可用 DDR 内存**
- 跨集群通信带宽受限（约 3.7GB/s）

这导致传统策略（如 TP-heavy、ZeRO-3、activation checkpointing）在 MT-3000 上暴露显著开销，例如：
- **Intra-layer communication** 进入关键路径
- **Activation recovery** 在 backward 时发生，造成延迟
- **Gradient synchronization 和参数更新** 集中在 step boundary，形成“finalization tail”

因此，论文提出：**dense LLM training 应建模为 training-state lifecycle scheduling 问题，而非粗粒度的 step-end 处理。**

---

### **提出了什么新方法或新思路**

论文提出 **RATrain** —— 一种面向带宽受限异构超算平台的资源感知训练运行时，其核心思想是：

#### ✅ **Training-State Lifecycle Scheduling**
将标准非交错 1F1B 训练中的状态操作（梯度同步、参数更新、权重预取、激活恢复）分解为 **层级别（layer-level）和阶段本地（stage-local）可调度的任务**。

具体机制包括：

1. **Layer-wise State Pipeline**
   - 将 GradSync、UpdateShard、PrefetchW 等任务按层拆解
   - 利用 backward 执行时间长于 forward 的特性，创建 **stage-local scheduling window**
   - 在后续 backward 或空闲窗口中重叠执行 GradSync，避免集中处理

2. **Next-Iteration Update-Prefetch Scheduling**
   - 参数更新和下一轮权重视图预取（PrefetchW）提前调度
   - 确保在下一 forward 访问前完成准备，避免阻塞

3. **Forward-Side Activation Recovery (FSR)**
   - 不再等到 backward 到达才恢复激活值
   - 在 forward 完成后、backward 到来前的空闲窗口中提前恢复
   - 减少 backward 关键路径上的计算压力

4. **MT-3000-aware Execution Backend**
   - 实现高效的 FP16 GEMM 和 **memory-resident Attention Backward**
   - 显式管理 DDR ↔ GSM ↔ AM ↔ SM 数据移动
   - 优化 tile schedule 以适应有限的 AM/SM 容量

5. **Resource-Aware Configuration Planner**
   - 基于模型结构、平台资源、执行代价构建统一 profile
   - 搜索满足 20GB DDR 约束且预测 step time 最小的配置
   - 输出 PP/DP/ZeRO 组合、micro-batch 设置、调度提示等

---

### **相比现有方法的优势**

| 方面 | 传统 GPU-style 方法 | RATrain |
|------|------------------------|--------|
| **状态调度粒度** | Step-end 集中处理 | Layer-level & stage-local 分散调度 |
| **通信与计算重叠** | 有限，集中在边界 | 充分利用 backward/slack 窗口 |
| **激活恢复时机** | Backward-time，阻塞关键路径 | Forward-side 提前恢复 |
| **参数准备** | 同步等待 | 提前 prefetch，避免 forward stall |
| **资源配置** | 固定启发式 | 基于代价模型搜索最优 |
| **平台适配性** | 强依赖高带宽 | 显式建模低带宽、显存约束 |

> ✅ **核心优势**：在不改变训练语义的前提下，通过细粒度生命周期调度，显著降低暴露开销，提升端到端效率。

---

## 2. **核心实验方法和设置**

### **使用了哪些数据集**
- 使用 **English C4** 固定 token 流进行训练
- 所有对比实验保持相同的数据顺序、全局 batch 语义、学习率调度、优化器设置

### **实验设置**
- **硬件平台**：真实 MT-3000 异构超算平台
- **序列长度**：默认 2048
- **每集群可用内存**：限制为 20GB
- **模型规模**：
  - LLaMA-2-7B / 13B / 70B
  - Baichuan2-13B
  - Qwen2.5-32B

### **评估指标**
| 指标 | 描述 |
|------|------|
| `tokens/s` | 吞吐量，主性能指标 |
| `step time` | 单步耗时 |
| `scaling efficiency` | 扩展效率（相对于理想线性加速） |
| `peak memory` | 峰值内存占用 |
| `loss trajectory` | 正确性验证，最大相对偏差 |
| `planner prediction error` | 规划器预测准确性 |

### **基线方法对比**
所有基线均基于相同的 MT-3000 operator backend 和通信实现，仅调度策略不同：
- **TP-heavy**：高张量并行度
- **ZeRO-3-heavy**：重度状态分片
- **Backward Ckpt**：传统 backward-time 激活恢复
- **Full-save**：保存全部激活（常 OOM）
- **Tuned PP/DP/ZeRO**：手动调优但无 RATrain 调度机制
- **Baseline-1F1B**：语义等价的标准 1F1B 运行作为正确性基准

---

## 3. **主要实验结果和性能指标**

### **关键性能数据**

| 模型 | 方法 | Tokens/s | Step Time (s) | Speedup vs Best Baseline |
|------|------|----------|--------------|----------------------------|
| LLaMA-2-13B | **RATrain** | **12,191.13** | 688.09 | 1.00× |
| | TP-heavy | 10,149.20 | 826.53 | 1.20× slower |
| | ZeRO-3-heavy | 11,684.48 | 717.93 | 1.04× slower |
| | Backward Ckpt | 8,952.21 | 937.04 | 1.36× slower |

| Qwen2.5-32B | **RATrain** | **5,267.52** | 1,592.51 | 1.00× |
| | TP-heavy | 4,363.01 | 1,922.66 | 1.21× slower |
| | Backward Ckpt | 3,879.06 | 2,162.54 | 1.36× slower |

> 🔺 **最高达到 1.35× 端到端加速比**

---

### **与基线方法的对比结果**

- **TP-heavy 表现差**：因引入 intra-layer collectives，受限于低跨集群带宽
- **ZeRO-3-heavy 无收益**：ZeRO-2 已满足内存需求，ZeRO-3 带来额外 view materialization 开销
- **Full-save 导致 OOM**：在 20GB 限制下不可行
- **Backward Ckpt 显著变慢**：恢复延迟暴露在关键路径
- **Tuned PP/DP/ZeRO 接近 Backward Ckpt**：缺乏细粒度调度无法突破瓶颈

> ✅ **结论**：仅靠并行策略调优无法替代 RATrain 的生命周期调度机制。

---

### **消融实验结果（Ablation Study）**

在 Qwen2.5-32B 上关闭各组件，结果归一化至 Full RATrain：

| 变体 | Step Time (×) | Exposed Tail (×) |
|------|---------------|------------------|
| Full RATrain | 1.00× | 1.00× |
| -FSR | 1.33× | 1.01× |
| -Update-Prefetch | 1.04× | 2.31× |
| -Layer-wise State Pipeline | 1.03× | 4.59× |

- **FSR 影响最大**：移除后 step time 增加 33%，说明提前恢复对性能至关重要
- **State Pipeline 对尾部影响最大**：移除后尾部开销放大 4.59×，证明其有效消除 finalization tail

---

## 4. **关键结论和发现**

### **论文的主要发现**

1. **LLM training on bandwidth-constrained platforms 是系统级耦合问题**
   - 关键瓶颈在于 **critical-path execution、parallelism、training-state lifecycle、platform resource** 的耦合
   - 单纯优化算子（如 GEMM）不足以解决问题

2. **Training-state lifecycle scheduling 是有效范式**
   - 将状态操作视为具有明确生命周期的运行时对象
   - 在 layer-level 和 stage-local 粒度进行调度，可显著减少暴露开销

3. **RATrain 实现高效且可行的大模型训练**
   - 支持从 7B 到 70B 的 dense LLM 在 20GB/cluster 限制下运行
   - LLaMA-2-7B 在 1024 集群上达到 **112,790.55 tokens/s**，扩展效率 **97.0%**

4. **规划器准确可靠**
   - 预测 step time 误差仅 **2.33% ~ 2.94%**（平均 2.67%）
   - 可有效指导配置搜索，降低试错成本

5. **训练语义完全保留**
   - 1.028B token 正确性测试中，与 Baseline-1F1B 的最大相对 loss 偏差仅为 **0.081%**
   - 证明调度未改变数学语义

---

### **方法的局限性**

- **依赖精确的执行剖面（execution profile）**：若底层 operator 性能波动大，规划器效果可能下降
- **调度复杂性增加**：需维护多个任务队列和依赖关系，调试难度高于传统 runtime
- **目前聚焦 dense LLM**：对 MoE 架构支持尚未验证
- **平台特异性较强**：虽通用思想可迁移，但 MT-3000-aware backend 需重新适配其他架构

---

### **未来工作方向**

1. **支持更复杂的并行组合**：如结合 MoE、interleaved 1F1B
2. **动态自适应调度**：根据运行时负载动态调整任务优先级
3. **跨平台泛化**：将 lifecycle scheduling 思想推广至其他异构架构（如 NPU、AI 芯片）
4. **集成编译器优化**：与 MLIR/TVM 等编译栈结合，实现端到端自动优化
5. **容错与弹性训练支持**：增强在大规模集群下的鲁棒性

---

> 📌 **总结一句话**：  
> RATrain 通过 **training-state lifecycle scheduling** 范式，在不改变训练语义的前提下，成功将 LLM 训练从 GPU-centric runtime 转向适用于 **带宽受限异构超算平台** 的资源感知运行时，实现了高达 **1.35× 的端到端加速** 和良好的可扩展性与正确性。

</details>

---

### 5. [Hasse Diagrams for Attention: A Partial Order Framework for Designing Transformer Masks](https://arxiv.org/abs/2606.09951)

**Authors**: Chentao Li, Han Guo  
**Category**: cs.LG  
**Published**: 2026-06-10  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2606.09951v1  

#### Abstract
During the training of large Transformer models, attention masks regulate the scope and direction of information flow across a sequence. Numerous mask variants exist, and operators such as FlexAttention already support arbitrary attention masks. Nevertheless, a systematic formal analysis of the info...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Hasse Diagrams for Attention: A Partial Order Framework for Designing Transformer Masks*

---

## 1. 论文的主要贡献和创新点

### ✅ 解决了什么问题

该论文旨在解决 **Transformer 模型中 attention mask 设计缺乏系统性理论指导** 的问题。尽管已有大量 attention mask 变体（如 causal mask、sliding window、two-stream attention 等），但其设计多依赖经验或直觉，缺乏统一的数学框架来分析和生成这些 mask。

具体而言，论文关注以下挑战：
- 如何形式化任意 attention mask 所诱导的信息流结构？
- 如何系统地合并多个训练任务（如自回归预测、双向建模）到一个统一的计算图中？
- 能否从任务定义出发，**构造性地推导出最优的 attention mask**？

---

### 🚀 提出了什么新方法或新思路

论文提出了一套完整的 **基于偏序关系（partial order）和 Hasse 图的理论框架**，用于建模和设计 Transformer 的 attention mask。

#### 主要创新点包括：

1. **将多层 Transformer 的信息流收敛为 Hasse 图**
   - 证明：在足够深度下，任意 attention mask 经过残差连接和多层堆叠后，其可达性矩阵（reachability matrix）会收敛为一个满足自反性和传递性的 **preorder**。
   - 进一步通过等价类划分，导出一个 **偏序集合（poset）**，并用其 **Hasse diagram** 表示模型的信息流拓扑结构。
   - 这是首次对任意 mask 下的信息流进行 **代数结构化建模**。

2. **将并行训练任务的设计转化为“最小公共超图”问题**
   - 将每个训练任务表示为其对应的 Hasse diagram。
   - 定义“节点等价性”（node equivalence）：若两个节点具有相同的输入和上游依赖结构，则可合并。
   - 提出 **Minimal Common Supergraph Criterion**，给出构造最小合并任务的方法。
   - 由此实现从任务族到最优合并训练方案的 **完全构造性推导流程**。

3. **设计两种新型 attention mask**
   - **Block Two-Stream Attention**：支持块级生成（block generation），首次实现训练与推理一致的 block autoregressive 模式，无需近似。
   - **Butterfly Attention**：实现全监督、高密度标签下的双向 attention，且 **不依赖 mask token**，避免信息泄露风险。

---

### 🔍 相比现有方法的优势

| 方面 | 传统方法 | 本文方法 |
|------|--------|---------|
| **mask 设计方式** | 手工设计、启发式调整 | 数学驱动、构造性生成 |
| **理论基础** | 缺乏统一框架 | 建立在 preorder / poset / Hasse diagram 上的严格理论 |
| **任务融合能力** | 需逐任务验证信息泄漏 | 自动保证信息流隔离与共享一致性 |
| **可扩展性** | 难以组合复杂任务 | 支持任意任务族的系统合并 |

> 💡 **核心优势**：将 attention mask 设计从“艺术”变为“工程”，提供了一个标准 pipeline 来从任务定义直接生成合法且高效的 mask 结构。

---

## 2. 核心实验方法和设置

> ⚠️ 注意：本论文为 **理论导向的研究**，未在真实语言模型上进行端到端训练或大规模性能评测。其实验部分体现为 **案例研究（case studies）**，即通过形式化推导展示框架的应用过程与结果。

### 📚 使用的数据集

- 并未使用具体 benchmark 数据集（如 GLUE、WikiText 等）。
- 所有分析基于 **抽象序列样本 $ C = (w_1, w_2, \dots, w_n) $**，其中每个 token 已嵌入并带有位置编码。
- 在 case study 中引入了两类增强 token：
  - **Mask tokens** $ m_1,\dots,m_l $：用于 Block Two-Stream Attention。
  - **Aggregated tokens** $ w'_k $：定义为邻居平均值，用于 Butterfly Attention。

---

### ⚙️ 实验设置和评估指标

#### 方法论流程（适用于所有 case study）：

1. **定义任务族 $ \mathcal{T} = \{T_1, \dots, T_m\} $**
   - 每个任务包含输入映射 $ W_k $、标签映射 $ Y_k $ 和初始 mask $ M_k $
2. **为每个子任务构建 Hasse diagram**
   - 利用 reachability matrix $ R $ 导出等价类与偏序关系
3. **计算节点等价类**
   - 使用 Definition 3.5 的 node equivalence 判断是否可合并
4. **构造最小公共超图（minimal common supergraph）**
   - 应用 Theorem 3.7 得到最小合并任务 $ T^* $
5. **导出最终 attention mask 矩阵 $ M^* $**

#### 评估方式（非数值型）：
- **正确性验证**：检查是否满足各子任务的信息流约束（无信息泄露）
- **效率性分析**：比较节点数量，衡量参数共享程度
- **新颖性展示**：是否能生成已有方法无法覆盖的新结构

---

### 🆚 基线方法对比

| 方法 | 是否被涵盖 | 说明 |
|------|-----------|------|
| **Causal Attention** | ✅ 是 | 被证明为 autoregressive task family 的 minimal merged task |
| **BERT-style MLM** | ❌ 否 | 不适用（需 mask token + 双向 attention） |
| **XLNet Two-Stream Attention** | ✅ 启发来源 | 本文推广其思想，提出更系统的 Block Two-Stream 版本 |
| **FlexAttention** | ✅ 兼容 | 所得 mask 可直接插入支持 FlexAttention 的框架（如 Qwen3） |

> ✅ 本文框架不仅能复现经典结构（如 causal attention），还能发现新结构。

---

## 3. 主要实验结果和性能指标

由于是理论工作，性能指标以 **结构特性与功能实现** 为主：

### ✅ 关键成果与结构特性

| 新机制 | 功能特点 | 结构优势 |
|-------|----------|----------|
| **Block Two-Stream Attention** | - 支持块级生成<br>- 训练时预测整个 block<br>- 实现训练-推理一致性 | - 首次无需近似即可完成 block generation<br>- 使用两组链式结构 + 分支连接 |
| **Butterfly Attention** | - 全监督双向 attention<br>- 每个位置都能作为预测目标<br>- 不允许任何位置访问自身 token | - 实现 100% supervision density<br>- 信息流呈“蝴蝶形”：<br>  &nbsp;&nbsp;– 前向链：$ C[T_{n},1] \to \cdots \to C[T_{n},n-1] $<br>  &nbsp;&nbsp;– 后向链：$ C[T_{1},2] \to \cdots \to C[T_{1},n] $<br>  &nbsp;&nbsp;– 中心预测边连接两者 |

---

### 🔬 消融实验（Ablation Study）

论文未提供传统意义上的消融实验（如 ablation on accuracy vs. layers），但在理论层面进行了 **结构必要性分析**：

- **深度的影响**：
  - 若 mask 不满足 $ A = R $（即单层不可达全部路径），则需要更深网络才能达到稳定信息流。
  - 提出 **sparse minimal merged task** 概念：可用稀疏 mask 替代 dense mask，只要最终 Hasse diagram 相同。

- **等价类合并的有效性**：
  - 在 causal attention 案例中，证明标准自回归训练正是 minimal merged task，说明当前实践已是最优。
  - 在 block 与 butterfly 场景中，展示了非平凡的合并结构，表明框架可超越现有设计。

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **Transformer 的信息流天然形成偏序结构**
   - 多层堆叠 + 残差连接 ⇒ 收敛至 preorder ⇒ 可导出 poset ⇒ 可视化为 Hasse diagram。
   - 这为理解 attention mask 提供了全新的代数视角。

2. **训练任务的并行化 = 最小公共超图构造问题**
   - 多任务学习不再是“拼凑”，而是图论中的优化问题。
   - 提出的 **Minimal Common Supergraph Criterion** 提供了唯一最优解的存在性与构造方法。

3. **可构造性设计 pipeline 成功应用**
   - 从任务定义 → 单任务 Hasse 图 → 节点等价类 → 合并图 → 最终 mask，全过程可自动化。
   - 成功推导出两种全新 attention 结构，验证了框架的创造力。

---

### ⚠️ 方法的局限性

| 局限 | 说明 |
|------|------|
| **仅处理 dense training tasks 的合并** | 当前理论主线基于 dense mask 推导；sparse 版本需后续简化（Definition 3.8） |
| **未考虑非 attention 模块影响** | 忽略 FFN、LayerNorm 对信息流的潜在扰动（假设为 position-wise 不改变图结构） |
| **尚未集成到实际训练流程** | 缺少在真实 LLM 上的训练效率、收敛速度、下游任务表现等实证验证 |
| **未处理动态长度或流式输入** | 假设序列长度固定，难以直接扩展至无限上下文场景 |

---

### 🔮 未来工作方向（作者明确提出）

1. **扩展至线性 attention 机制**
   - 分析 KDA、GDN 等线性注意力变体是否也产生偏序结构。
   - 若成立，可将本框架推广至 Mamba、RetNet 等架构。

2. **结合具体训练目标设计新 attention 机制**
   - 探索 MAE（Masked Autoencoder）类任务的家庭定义。
   - 构造适用于图像、语音、代码等多模态任务的最优合并策略。

3. **开发自动 mask 生成工具**
   - 基于本框架构建 DSL（领域专用语言）让用户声明任务族，自动生成最优 mask 矩阵。
   - 与 FlexAttention 等运行时系统集成，实现“prompt-to-mask”自动化。

---

## 总结

| 维度 | 评价 |
|------|------|
| **理论价值** | ⭐⭐⭐⭐⭐ | 首次建立 attention mask 的代数语义模型 |
| **实用性潜力** | ⭐⭐⭐⭐☆ | 可指导新型 mask 设计，尤其适合复杂任务组合 |
| **创新性** | ⭐⭐⭐⭐⭐ | 将图论、偏序理论引入 attention 设计，范式转变 |
| **实证充分性** | ⭐⭐☆☆☆ | 缺乏真实训练数据支撑，仍属理论探索阶段 |

> 📌 **一句话总结**：  
> 本文提出了一个基于 **Hasse diagram** 的形式化框架，将 Transformer 的 attention mask 设计从经验工程转变为 **可构造的数学问题**，不仅解释了现有方法的本质，还发现了 **Block Two-Stream Attention** 和 **Butterfly Attention** 两类新结构，为下一代 attention 机制的设计提供了坚实基础。

</details>

---

### 6. [Bellman-Taylor Score Decoding for Markov Decision Processes with State-Dependent Feasible Action Sets](https://arxiv.org/abs/2606.10979)

**Authors**: Yi Chen (Lucy), Rushuai Yang (Lucy), Qiang Chen (Lucy),  Dongyan (Lucy),  Huo  
**Category**: cs.AI  
**Published**: 2026-06-10  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2606.10979v1  

#### Abstract
Many Markov decision processes (MDPs) in operations research have feasible actions that are state dependent and defined implicitly by various operational constraints. These features make it difficult to use standard deep reinforcement learning (DRL) algorithms, whose action interfaces typically assu...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Bellman-Taylor Score Decoding for Markov Decision Processes with State-Dependent Feasible Action Sets

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
许多运筹学（OR）中的 **Markov Decision Process (MDP)** 存在**状态依赖的可行动作集**（state-dependent feasible action sets），其动作空间通常由容量、兼容性、整数性等约束隐式定义，且维度高、组合性强。这导致标准的 **Deep Reinforcement Learning (DRL)** 算法难以直接应用，因为它们通常假设动作空间是固定的有限集合或简单的欧几里得空间。

现有方法如动作掩码（masking）、动作嵌入（embedding）或优化层（optimization layer）往往需要问题特定的设计，限制了通用性和可复用性。

---

### 提出了什么新方法或新思路
本文提出了一种新的动作接口框架：**Bellman-Taylor Score Decoding (BTSD)**，其核心思想是：

- 将策略学习从原始的复杂动作空间转移到一个**连续的欧几里得分数空间**（latent score space）。
- 引入一个**动作解码器**（action decoder），将学到的分数向量映射为满足所有约束的可行自然动作。
- 解码器基于对最优 **action-value function** 的 **Taylor 展开近似**，其中分数被解释为“后决策系统配置”对未来价值的边际影响（marginal-value score）。

该框架构建了一个**隐变量 MDP**（latent-score MDP），使得标准的连续动作 DRL 算法（如 PPO）可以直接应用，而无需通过解码器进行梯度反传。

---

### 相比现有方法的优势
| 方面 | BTSD 优势 |
|------|----------|
| **通用性** | 不依赖固定动作目录或显式枚举，适用于任意由约束定义的动作集。 |
| **可行性保障** | 动作可行性完全由解码器保证，策略网络无需处理约束。 |
| **训练简便性** | 无需对优化解码器进行微分（no differentiation through optimizer），避免了不可导或不稳定的梯度估计。 |
| **理论支持** | 提供了性能界分析，将最优性差距分解为**结构性逼近误差**和**算法学习误差**。 |
| **即插即用** | 可与标准 DRL 算法（如 PPO、SAC、DQN）结合，无需定制架构或训练流程。 |

---

## 2. 核心实验方法和设置

### 使用了哪些数据集 / 问题实例
论文在两类典型运筹学问题上进行了验证：

1. **库存控制问题**（Inventory Control）
   - 多地点库存系统，允许跨地调拨（transshipment）。
   - 调拨接收过程存在损耗（非线性），用于测试不同阶数解码器的效果。

2. **排队网络控制问题**（Queueing Network Control）
   - 多类客户、多服务池的动态路由问题（multi-class, multi-pool queueing system）。
   - 应用于住院患者溢出管理等场景。
   - 实验规模包括：
     - 小型：2×2 网络（可计算精确最优解）
     - 中型：5×5 网络（更接近实际复杂度）

---

### 实验设置和评估指标

#### 评估指标
- **相对最优性差距**（Optimality Gap）：与最优值或最佳基准的相对成本差异。
- **Bellman Regret**：$ \mathbb{E}[Q^*(s,a_\pi(s)) - V^*(s)] $，衡量策略选择动作的次优程度。
- **最优动作一致率**（Action Agreement Rate）：策略选择的动作与最优动作的一致比例。
- **平均累积折扣成本**（Average Discounted Cost）

#### 训练细节
- 使用 **Proximal Policy Optimization (PPO)** 作为主干算法。
- 解码器实现为一个整数规划（Integer Program）求解器，在前向传播中调用。
- 所有实验均基于模拟环境生成轨迹。

---

### 基线方法对比
| 类别 | 基线方法 |
|------|--------|
| **经典启发式** | cu rule, modified cu rule, max-weight rule, modified max-weight rule |
| **DRL 基线** | 
| - Vanilla PPO/SAC/DQN | 使用动作掩码和投影机制处理可行性 |
| - Atom-PPO | 将组合动作分解为序列原子动作（sequential atomic actions） |
| - MIP-based lookahead | 结合价值函数近似与数学规划进行每步优化（Harsha et al., 2025） |

---

## 3. 主要实验结果和性能指标

### 关键性能数据

#### （1）小型排队网络（2×2） vs 最优解（Table 2）
| 设置 | BTSD-PPO 成本 | 最优成本 | 相对差距 |
|------|----------------|-----------|---------|
| 平衡负载（ρ=(0.90,0.90)） | ~1226–1317 | ~1210–1285 | **1.1% – 2.5%** |
| 非平衡负载（ρ=(0.95,0.85)） | ~1198–1278 | ~1185–1264 | **1.1% – 1.3%** |

✅ **结论**：在小规模可精确求解的问题上，BTSD-PPO 接近最优，验证了方法的有效性。

---

#### （2）中型排队网络（5×5） vs 各类基线（Table 3）
| 指标 | BTSD-PPO 表现 | 改进幅度 |
|------|---------------|----------|
| 平均成本 | **最低**（在全部9个案例中均最优） | 比最佳基线提升 **4.0% – 23.7%** |
| 最佳基线表现 | MIP 或 modified cu 在部分案例中较强，但不稳定 |
| Atom-PPO | 明显劣于 BTSD-PPO，说明局部决策无法捕捉全局耦合 |

✅ **结论**：BTSD-PPO 在中等规模系统中显著优于传统启发式和先进 DRL 方法。

---

#### （3）消融实验：BTSD 对不同 DRL 主干的提升效果（Table 4）
| DRL Backbone | Vanilla 成本 | BTSD 成本 | 成本降低 |
|--------------|-------------|----------|----------|
| PPO | 397.2 | 222.2 | **+44.1%** |
| SAC | 417.0 | 230.2 | **+44.8%** |
| DQN | 393.1 | 228.9 | **+41.8%** |

✅ **结论**：性能提升来自 **BTSD 框架本身**，而非特定 DRL 算法；BTSD 显著增强了各类算法的表现。

---

#### （4）库存问题中高阶解码器的作用（Table 1）
| 接收损耗参数 $ p $ | 一阶解码器最优性差距 | 二阶解码器最优性差距 |
|---------------------|------------------------|------------------------|
| 0.0 | 1.0% | 0.2% |
| 0.5 | 10.5% | 0.4% |
| 0.75 | 11.4% | 0.6% |

✅ **结论**：当系统动态高度非线性时，**高阶 Taylor 展开**能显著改善性能，验证了框架的灵活性。

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **BTSD 是一种通用且有效的动作接口**，成功桥接了标准 DRL 算法与具有状态依赖、组合性、约束性动作空间的运筹学 MDP。
2. ✅ 解码器诱导的策略本质上是一种**学习得到的状态依赖索引规则**（learned index-based dispatching rule），超越了手工设计的 max-weight 或 $ c\mu $ 规则。
3. ✅ 性能增益主要来源于 **动作表示的重构**，而非特定 DRL 算法的选择。
4. ✅ 理论分析表明，最优性差距可分解为：
   - **结构性误差**：由 Taylor 近似的残差振荡（oscillation）决定；
   - **学习误差**：由 DRL 算法在隐空间中的优化质量决定。
5. ✅ 高阶解码器可在强非线性系统中进一步压缩结构性误差。

---

### 方法的局限性
1. **额外计算开销**：每次动作选择需调用一次优化求解器（如 IP/MIP），增加推理延迟。
2. **近似本质**：一阶 Taylor 近似在曲率大的区域可能失效，尽管高阶可缓解但会增加维度。
3. **依赖显式模型结构**：要求能够定义“后决策配置” $ \phi_s(a) $ 和转移函数 $ \mathcal{T}_s(\cdot,\cdot) $，在纯数据驱动场景中可能受限。
4. **解码器非光滑性**：可能导致策略更新的方差增大（虽不影响梯度计算）。

---

### 未来工作方向
1. **扩展到 Average-Cost MDP**：将框架推广至长期平均成本准则，替换 discounted continuation value 为 relative value function。
2. **数据驱动的 post-action 表示学习**：在未知动态的情况下，从数据中学习合适的 $ \phi_s(a) $ 表示。
3. **离线强化学习（Offline RL）集成**：利用历史数据训练 BTSD 策略，提高样本效率。
4. **加速解码器求解**：探索近似解码器或 warm-start 技术以减少实时计算负担。

---

> **总结一句话**：  
> **Bellman-Taylor Score Decoding 提供了一个“解耦学习与可行性”的通用框架，使标准 DRL 算法能在复杂的运筹学 MDP 中高效、准确地学习高质量策略，兼具理论清晰性与实证优越性。**

</details>

---

### 7. [ReasonAlloc: Hierarchical Decoding-Time KV Cache Budget Allocation for Reasoning Models](https://arxiv.org/abs/2606.11164)

**Authors**: Wenhao Liu, Hao Shi, Yunhe Li, Weizhi Fei, Xiangyuan Wang, Mengzhe Ruan, Hanxu Hou, Peisong Wang, Linqi Song, Shuang Qiu  
**Category**: cs.AI  
**Published**: 2026-06-10  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2606.11164v1  

#### Abstract
Long chain-of-thought (CoT) trajectories in large language model (LLM) reasoning cause severe inference bottlenecks due to rapid key-value (KV) cache growth. Current decoding-time compression methods mitigate this issue via token eviction, but typically assume a uniform budget distribution across al...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：ReasonAlloc: Hierarchical Decoding-Time KV Cache Budget Allocation for Reasoning Models**

---

## 1. **论文的主要贡献和创新点**

### ✅ **解决了什么问题**

大型推理模型（如基于强化学习或 Chain-of-Thought 的 LLM）在执行复杂任务时会产生**长推理轨迹（long CoT trajectories）**，导致解码阶段 Key-Value (KV) cache 快速增长，造成严重的内存瓶颈和推理吞吐下降。

现有 **decoding-time KV cache 压缩方法**（如 SnapKV、R-KV）通常采用**均匀预算分配策略**（uniform budget across layers and heads），即每一层、每个注意力头保留相同数量的 token。然而，这种假设忽略了不同层和头在推理过程中对 KV cache 的实际需求差异。

此外，虽然已有非均匀分配方法（如 PyramidKV），但它们多为**静态设计，适用于 prompt 预填充阶段（prefill phase）**，无法适应自回归生成中动态变化的上下文重要性。

---

### 🚀 **提出了什么新方法或新思路**

本文提出 **ReasonAlloc** —— 一种**无需训练、即插即用**的分层 KV cache 预算分配框架，将 decoding-time KV 压缩重新定义为一个**两级资源分配问题**：

#### （1）**离线层间预分配（Offline Layer-wise Preallocation）**
- 在推理前通过轻量级校准，分析各层对 KV cache 的真实需求。
- 发现并建模了一种架构驱动的非线性需求模式——“**Reasoning Wave**”：
  - **浅层（High Demand）**：需要大量缓存以感知全局语义；
  - **中间层（Low & Oscillating）**：局部逻辑推理，需求较低；
  - **深层（Spiking Demand）**：输出前进行整体验证，需求突然上升。
- 该分布具有**跨任务稳定性**（task-invariant），主要由模型架构决定。

#### （2）**在线头内动态重分配（Online Head-wise Dynamic Routing）**
- 在解码过程中每 Δ 步动态调整每层内部各 attention head 的预算。
- 基于实时的 **importance-redundancy 评分**（如 R-KV 中的 $ s = \alpha I + (1-\alpha)R $）进行动态路由。
- 引入**鲁棒化操作符（robustification operator）**防止某些 head 因短暂低分被永久“饿死”。

> 🔁 **整体流程**：先确定每层应得多少总预算（layer-wise），再决定这些预算如何在该层的不同 head 之间分配（head-wise）。

---

### ⚖️ **相比现有方法的优势**

| 特性 | 传统方法（如 R-KV） | Pyramid-RKV | ReasonAlloc |
|------|--------------------|-------------|--------------|
| 是否训练自由 | 是 | 是 | 是 ✅ |
| 是否支持非均匀分配 | ❌（默认均匀） | ✅（但静态） | ✅✅（动态+分层） |
| 层级分配是否动态 | ❌ | ❌（固定衰减） | ✅（离线校准 + 可选在线 fallback） |
| 头级分配是否动态 | ❌ | ❌ | ✅（在线刷新） |
| 插件兼容性 | — | — | ✅（可包装任何 token eviction policy） |
| 推理开销 | — | — | ➕ 极小（仅每 128 步一次向量化计算） |

> ✅ **核心优势**：在极小额外开销下，显著提升压缩场景下的推理准确率，尤其在**小预算（128–512 tokens）条件下表现突出**。

---

## 2. **核心实验方法和设置**

### 📚 **使用的数据集**

- **MATH-500**：从 MATH 数据集中抽取的 500 道数学题，涵盖代数、几何等，用于评估复杂数学推理能力。
- **AIME 2024**：美国邀请数学考试真题，难度更高，更贴近竞赛水平，测试长程逻辑连贯性。

---

### 🧪 **实验设置与评估指标**

#### ✅ 模型
- **DeepSeek-R1-Distill-Llama-8B**（简称 R1-Llama-8B）
- **DeepSeek-R1-Distill-Qwen-14B**（R1-Qwen-14B）
- **AceReason-14B**

均为专为推理优化的 distillation 或 RL 微调模型，擅长生成长 CoT。

#### ✅ 评估指标
- **pass@1**：在温度 0.6、top-p 0.95 下采样 8 次，取平均 pass@1 分数。
- 所有结果均在严格相同的 token scoring policy（R-KV 的 $ s = \alpha I + (1-\alpha)R $）下比较，确保公平。

#### ✅ 缓存预算范围
- 测试多个 KV cache 预算：128, 256, 512, ..., 3072 tokens
- 最大生成长度达 16K–32K tokens，模拟极端长上下文场景。

#### ✅ 实现细节
- 刷新间隔 △ = 128
- 注意力质量阈值 $ p = 0.93 $
- 层平滑指数 $ \gamma = 0.5 $，头平滑指数 $ \beta = 0.5 $
- 层裁剪范围：$[0.25B, 2B]$，头最小保障：$ \mu = 0.25 $

---

### 🔁 **基线方法对比**

| 方法 | 类型 | 特点 |
|------|------|------|
| **FullKV** | 无压缩 | 不删除任何 token，作为上限参考 |
| **SnapKV** | 静态重要性筛选 | 基于 attention score 保留 token，无冗余惩罚 |
| **R-KV** | 当前 SOTA 解码时压缩 | 使用 importance + redundancy 联合打分，**但预算均匀分配** |
| **Pyramid-RKV** | 本文构建强基线 | 将 PyramidKV 的单调递减预算应用于 R-KV，代表“静态非均匀”方案 |

> 💡 所有方法共享相同的 token 评分机制（R-KV），仅预算分配方式不同，凸显 ReasonAlloc 的增益来自其**分层分配机制本身**。

---

## 3. **主要实验结果和性能指标**

### 📈 **关键性能数据（来自 Table 2 和 Figure 3）**

#### 在 **MATH-500 @ 512 tokens** 上的表现（R1-Llama-8B）：
| 方法 | 准确率 |
|------|--------|
| FullKV | 89.20% |
| SnapKV | 63.62% |
| R-KV（Uniform） | 76.48% |
| **ReasonAlloc（Ours）** | **82.50%** ✅ |

> ➕ 相比 R-KV 提升 **+6.02%**，接近 FullKV 表现。

#### 在 **AIME 2024 @ 256 tokens** 上的表现（R1-Llama-8B）：
| 方法 | 准确率 |
|------|--------|
| FullKV | 50.42% |
| SnapKV | 1.25% |
| R-KV | 10.42% |
| **ReasonAlloc** | **20.00%** ✅ |

> ➕ 提升近 **翻倍**，显示其在极紧预算下的强大保真能力。

---

### 📊 **与基线方法的对比结果**

- **全面超越所有 baseline**，尤其是在 **small-to-medium budget（128–1024）区间**。
- 相比 **Pyramid-RKV**（静态非均匀）也明显占优：
  - MATH-500 @512: 79.40% vs. **82.50%**
  - AIME-2024 @1024: 39.17% vs. **49.17%**
- 表明：“Reasoning Wave” ≠ 单调递减，**静态规则不适用于 decoding 动态过程**。

---

### 🔍 **消融实验结果（Ablation Study on AIME 2024）**

| 配置 | 256 | 512 | 1024 | 2560 |
|------|-----|-----|------|-------|
| R-KV（Baseline） | 10.42 | 28.33 | 45.42 | 51.67 |
| + Layer-only | 13.32 | 30.83 | 42.50 | **55.00** |
| + Head-only | 17.50 | 31.66 | 45.82 | 52.50 |
| **ReasonAlloc（Full）** | **20.00** | **32.08** | **49.17** | **53.34** |

#### 结论：
- **Head-wise 动态路由**在小预算下贡献最大（+7.08% @256），保护关键 head 不被饿死。
- **Layer-wise 预分配**在中高预算下更有效，捕捉全局结构。
- **两者结合效果最优且最稳定**，体现分层设计的必要性。

---

## 4. **关键结论和发现**

### 🎯 **主要发现**

1. **KV cache 需求是高度异质的**：
   - 层间存在稳定的“**Reasoning Wave**”模式，非单调，受架构主导。
   - 层内 head 间差异巨大（有的需 500 tokens，有的 <50），静态均分浪费严重。

2. **静态非均匀分配（如 Pyramid）不适合 decoding**：
   - 它们为 prefill 设计，在自回归生成中会误删关键路径，导致性能下降。

3. **分层动态分配显著提升压缩效率**：
   - ReasonAlloc 在几乎零推理开销下，大幅提升 accuracy，尤其在资源受限场景。

4. **方法通用性强**：
   - 支持多种底层 scoring policy（SnapKV、R-KV 等），即插即用。
   - 提供 fallback 机制应对 task-dependent 架构（Appendix C）。

---

### ⚠️ **局限性**

- **依赖离线校准集**：虽仅需少量样本，但仍需一次前处理。
- **未探索完全端到端学习式分配**：目前仍为 heuristic-based，未来可引入轻量适配器实现 learnable allocation。
- **主要验证于数学推理任务**：在其他类型推理（如符号逻辑、规划）中的泛化性有待进一步验证。

---

### 🔮 **未来工作方向**

1. **自动化 threshold $ p $ 调整**：当前 $ p=0.93 $ 手动设定，未来可动态感知任务复杂度自适应选择。
2. **扩展至 MoE 架构**：在专家选择层面引入类似的 budget routing 思想。
3. **结合 token merging / quantization**：形成多维度 KV 压缩 pipeline。
4. **部署优化**：针对边缘设备进一步降低 head-wise routing 的延迟波动。

---

## ✅ 总结一句话

> **ReasonAlloc 通过“离线层波建模 + 在线头流动态调度”的分层预算分配机制，在几乎无推理开销的前提下，显著提升了长链推理模型在低 KV cache 预算下的准确性，打破了传统均匀或静态非均匀分配的局限，为高效服务推理型 LLM 提供了实用的新范式。**

</details>

---

### 8. [Alignment Defends LLMs from Property Inference Attacks](https://arxiv.org/abs/2606.10217)

**Authors**: Pengrun Huang, Chhavi Yadav, Ruihan Wu, Kamalika Chaudhuri  
**Category**: cs.LG  
**Published**: 2026-06-10  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2606.10217v1  

#### Abstract
Large language models (LLMs) are increasingly fine-tuned on domain-specific datasets that may contain sensitive, dataset-level properties. Recent work has shown that such dataset-level information can be effectively extracted through property inference attacks, posing a confidentiality risk. Existin...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Alignment Defends LLMs from Property Inference Attacks*

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
大型语言模型（LLMs）在特定领域（如医疗、金融）中常通过**domain-specific 数据集进行 fine-tuning**，这些数据可能包含敏感的**dataset-level 属性**（例如患者性别比例、疾病发生率）。近期研究表明，攻击者可通过 **property inference attacks** 从模型输出中推断出这些全局统计属性，造成隐私泄露。

传统防御方法（如 re-sampling、differential privacy）通常需要修改训练数据或重新训练模型，在实际部署场景中不适用，尤其当原始数据不可访问时。

---

### 🚀 提出的新方法与创新思路
本文提出一种全新的防御范式：**基于 alignment 的 post-training 防御机制**，无需修改训练数据或重新训练模型。

#### 核心思想：
利用 LLMs 独有的 **post-training alignment 机制**（如 RLHF），将模型的输出分布“重塑”为一个预设的目标属性比例 $ r_t $（例如公开先验或平衡分布），从而切断模型行为与真实训练数据分布之间的关联。

#### 具体实现方式：
- **适配两种主流 preference optimization 框架作为防御工具**：
  1. **DPO (Direct Preference Optimization)**  
     构造偏好对 $(x, y^+, y^-)$，根据当前生成样本的属性比例 $\hat{r}$ 与目标 $r_t$ 的偏差来决定偏好方向。
  2. **GRPO (Group Relative Policy Optimization)**  
     设计特定奖励函数：若样本满足目标属性且当前比例偏低，则给予高奖励；反之则低奖励，通过 on-policy 更新逐步逼近目标比例。

> 🔍 创新点总结：
> - **首次将 alignment 技术用于防御 property inference attacks**。
> - 实现了 **post-training、data-free 的隐私保护机制**。
> - 不依赖 inference-time 控制（如 temperature scaling），更具实用性。

---

### ⚖️ 相比现有方法的优势

| 方法 | 是否需原始数据 | 是否需重训练 | 是否影响 utility | 可扩展性 |
|------|----------------|--------------|------------------|----------|
| **Subsampling** | 是 | 是 | 显著下降 | 差 |
| **Temperature Scaling** | 否 | 否 | 下降明显（尤其高温） | 中等 |
| **Differential Privacy** | 是 | 是 | 性能损失大 | 差 |
| **本文方法 (DPO/GRPO)** | ❌ 否 | ❌ 否 | ✅ 几乎无损 | ✅ 强 |

> ✅ 优势总结：
> - **实用性强**：适用于已部署模型，无需接触原始数据。
> - **保持 utility**：fine-tuned 模型的任务性能基本不受影响。
> - **双重防护潜力**：不仅防御 generation-based 攻击，也能间接削弱 shadow-model 攻击。

---

## 2. 核心实验方法和设置

### 📚 使用的数据集

| 数据集 | 任务描述 | 目标属性 | 真实比例范围 |
|--------|---------|--------|-------------|
| **ChatDoctor** | 医疗问答对话 | 患者性别（女性比例） | {0.3, 0.5, 0.7} |
| **MedCalc-Bench** | 医学计算推理 | 是否提及 “CKD-EPI” 方程 | {0.03, 0.05, 0.07} |

此外还设置了 **multi-class 设置**：同时控制多个诊断相关属性（如消化系统疾病、精神障碍）的比例。

---

### ⚙️ 实验设置

#### 模型配置：
- **Qwen-2.5-7B-Instruct** on MedCalc-Bench
- **LLaMA-1-7B** on ChatDoctor（复现 Huang et al. [9] 设置）

#### Fine-tuning 模式：
1. **QA Mode**：仅预测答案部分
2. **CC Mode**：完整生成指令 + 输入 + 输出序列

#### 对抗攻击类型：
1. **Generation-based Attack**  
   - 攻击者用固定 prompt 查询模型，统计生成文本中标记为某属性的比例。
2. **Shadow-model-based Attack**  
   - 训练多个 shadow models（不同属性比例）
   - 提取 word-frequency 特征（关键词出现频率）
   - 训练 meta-regressor 来预测目标模型的属性比例

#### 防御目标：
使攻击者估计的属性比例接近预设目标 $ r_t $：
- ChatDoctor: $ r_t = 0.5 $
- MedCalc: $ r_t = 0.05 $

---

### 📊 评估指标

| 类别 | 指标 | 描述 |
|------|------|------|
| **攻击有效性** | MAE<sub>true</sub> = $|\hat{r} - r_{\text{true}}|$ | 越大越好 → 表示难以恢复真实比例 |
| | MAE<sub>target</sub> = $|\hat{r} - r_t|$ | 越小越好 → 表示成功对齐到目标 |
| **模型效用** | ChatDoctor: **F1**（BERTScore）<br>MedCalc: **Accuracy** | 衡量任务性能是否保留 |

#### 基线方法对比：
1. **No Defense**：无任何防御
2. **Subsampling**：训练前下采样使属性比例匹配 $r_t$
3. **Temperature Scaling**：调整解码温度以扰动输出
4. **DPO** & **GRPO**：本文提出的 alignment 防御

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据（来自 Table 1 和 Table 2）

#### ✅ 在 **MedCalc (CC 模式)** 上的结果：
| 方法 | MAE<sub>gen</sub> | MAE<sub>shadow</sub> | Acc. | MAE<sub>target</sub> ↓ |
|------|--------------------|------------------------|-------|------------------------|
| No Defense | 0.0104 | 0.0092 | 0.3741 | 0.0169 |
| DPO | 0.0155 | 0.0139 | 0.3678 | **0.0089** |
| GRPO | **0.0117** | **0.0133** | **0.3701** | **0.0066** |

> 💡 结论：GRPO 在对齐精度上最优，且 utility 几乎无损。

#### ✅ 在 **ChatDoctor (CC 模式)** 上的结果：
| 方法 | MAE<sub>gen</sub> | MAE<sub>shadow</sub> | F1 | MAE<sub>target</sub> ↓ |
|------|--------------------|------------------------|-------|------------------------|
| No Defense | 0.0354 | 0.0332 | 0.8407 | 0.1429 |
| DPO | 0.1738 | 0.0692 | 0.8421 | 0.0434 |
| GRPO | 0.1357 | 0.0823 | 0.8410 | **0.0353** |

> 💡 结论：
> - DPO 和 GRPO 显著提升 MAE<sub>true</sub>（即更难恢复真实比例）
> - GRPO 对齐效果最好（MAE<sub>target</sub> 最低）
> - 模型 utility（F1）保持稳定甚至略有上升

#### ✅ 多属性对齐（Table 3）：
| 方法 | Average MAE<sub>true</sub> ↑ | Average MAE<sub>target</sub> ↓ |
|------|-------------------------------|--------------------------------|
| No Defense | 0.0182 | 0.0571 |
| DPO | 0.0233 | 0.0204 |
| GRPO | **0.0308** | **0.0199** |

> ✅ 成功扩展至 multi-class 场景，GRPO 表现最佳。

---

### 🔍 消融实验与额外分析

#### （1）对抗 prompt 泛化能力（Table 4 & B.1）
使用未见过的 adversarial prompts 测试泛化性：

| 方法 | MAE<sub>true</sub> ↑ | MAE<sub>target</sub> ↓ |
|------|------------------------|------------------------|
| No Defense | 0.0422 | 0.1406 |
| DPO | **0.1172** | **0.0575** |
| GRPO | 0.0757 | 0.0862 |

> ✅ DPO 泛化更强，说明其构造偏好对的方式更具鲁棒性。

#### （2）关键词-属性相关性减弱（Table 5）
| 方法 | "his" correlation ↓ | "female" correlation ↓ |
|------|----------------------|-------------------------|
| No Defense | -0.9324 | +0.7951 |
| GRPO | -0.6627 | +0.1504 |
| DPO | +0.5414 | -0.4494 |

> ✅ 所有方法均显著降低 keyword-attribute correlation，验证了防御可破坏 shadow attack 的特征基础。

#### （3）词频分布可视化（Figure 1 & 2）
- 经过 DPO/GRPO 对齐后，“female”、“his” 等词的频率不再随真实比例变化。
- DPO 引起更剧烈的词频跳跃，与更强的泛化能力一致。

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **Alignment 是有效的 post-training 防御手段**  
   - DPO 和 GRPO 均能有效抵御 generation-based 和 shadow-model-based property inference attacks。
   - 尤其是 **GRPO 因其 on-policy 更新机制，在对齐目标比例方面表现最优**。

2. **良好的 utility-confidentiality trade-off**  
   - 防御后模型的任务性能（F1 / Accuracy）几乎不变。
   - 相比 subsampling 或 temperature scaling，本方法对 utility 影响极小。

3. **具备跨 prompt 泛化能力**  
   - 即使面对未参与训练的 adversarial prompts，仍能维持较高防御强度。
   - DPO 在泛化性上优于 GRPO。

4. **间接削弱 shadow-model attacks**  
   - 虽然未直接优化 word-frequency 特征，但由于改变了属性比例，导致关键词与属性的相关性大幅下降。

---

### ⚠️ 方法的局限性

1. **无法完全消除 keyword-attribute correlation**  
   - 如 “her” 在某些情况下仍保持强相关（Table 5），表明仍有改进空间。

2. **依赖于属性分类器 $P(\cdot)$ 的准确性**  
   - 当前使用 GPT-4o 进行 labeling，可能存在误差或偏见。

3. **假设条件限制**  
   - 方法有效性依赖于“alignment 主要是 reweighting 而非彻底改变语言模式”的假设，极端情况下可能失效。

4. **仅针对 black-box 攻击设计**  
   - 若攻击者拥有模型权重（white-box），可能开发新的攻击策略。

---

### 🔮 未来工作方向

1. **探索更精细的 reward shaping 机制**  
   - 显式建模并打乱 keyword-attribute 关联，增强对 shadow attacks 的抵抗力。

2. **结合 differential privacy 与 alignment**  
   - 构建 hybrid defense，兼顾个体级与分布级隐私保护。

3. **自动化目标比例选择机制**  
   - 动态选择最优 $r_t$ 以最大化混淆效果，同时最小化 utility 损失。

4. **应用于其他 sensitive 属性**  
   - 如种族、收入水平、政治倾向等社会敏感属性的防护。

5. **研究 alignment 的逆向风险**  
   - 探讨该技术是否可能被滥用以掩盖训练数据中的 bias（如人为隐藏性别不平等）。

---

> 📌 **总体评价**：  
> 本文开创性地将 **LLM alignment 技术转化为隐私防御工具**，提出了实用、高效、无需重训练的解决方案。实验充分，结果可信，为 LLM 隐私保护提供了新视角，具有重要的理论价值和应用前景。

</details>

---

### 9. [PL-KKT-hPINN: Enforcing Nonlinear Equality Constraints on Neural Networks via Piecewise-Linear Projection](https://arxiv.org/abs/2606.10682)

**Authors**: Fateme Mohammad Mohammadi, Hector Budman, Joshua L. Pulsipher  
**Category**: cs.LG  
**Published**: 2026-06-10  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2606.10682v1  

#### Abstract
While physics-informed neural networks (PINNs) have shown strong potential for process modeling, physical equations are only enforced as soft constraints during training, and thus, they do not guarantee constraint satisfaction at inference. We propose a framework, called piecewise-linear Karush--Kuh...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：PL-KKT-hPINN: Enforcing Nonlinear Equality Constraints on Neural Networks via Piecewise-Linear Projection

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
传统的 **Physics-Informed Neural Networks (PINNs)** 将物理约束作为软约束（soft constraints）加入损失函数中，虽然提升了模型的物理一致性，但在训练和推理阶段**无法保证约束被严格满足**。此外，软约束方法存在以下问题：
- 损失项之间权重难以平衡，导致优化困难；
- 在低数据场景下容易过拟合或产生非物理解；
- 对于非线性等式约束（如化学反应动力学、质量守恒），传统硬约束方法计算成本高。

而现有的硬约束方法（如 OptNet、AdaNP）通常依赖迭代求解或动态投影过程，导致：
- 推理速度慢；
- 架构复杂，难以并行化；
- 难以嵌入标准深度学习框架。

### 提出了什么新方法或新思路
本文提出了一种新的框架：**Piecewise-Linear Karush-Kuhn-Tucker hard-constrained PINNs (PL-KKT-hPINN)**，其核心思想是：
- 将**非线性等式约束** $ g(x, y) = 0 $ 近似为多个局部的**分段线性等式约束**；
- 在每个子区域上构造基于 **KKT 条件** 的闭式正交投影层（closed-form orthogonal projection）；
- 利用指示函数（indicator functions）选择当前输入所在区域对应的投影操作；
- 最终输出为各区域投影结果的加权和，实现全局非线性约束的近似强制执行。

该方法继承了 KKT-hPINN 的高效性，并将其从仅支持线性约束扩展到**非线性等式约束**。

### 相比现有方法的优势
| 特性 | PL-KKT-hPINN | 软约束 PINN | KKT-hPINN | AdaNP / Picard-KKT-hPINN |
|------|--------------|------------|-----------|----------------------------|
| 是否严格满足约束 | ✅ 是（至近似精度） | ❌ 否 | ✅ 是（仅限线性） | ✅ 是 |
| 投影是否可微且闭式 | ✅ 是 | N/A | ✅ 是 | ⚠️ 依赖迭代 |
| 是否需要调参（如 loss weights） | ❌ 否 | ✅ 是 | ❌ 否 | ❌ 否 |
| 是否支持非线性约束 | ✅ 是 | ✅ 是（软） | ❌ 否 | ✅ 是 |
| 是否具有静态网络结构 | ✅ 是 | ✅ 是 | ✅ 是 | ❌ 否（动态深度） |
| 是否易于并行计算 | ✅ 是（并行投影） | ✅ 是 | ✅ 是 | ❌ 否（串行迭代） |

> ✅ **优势总结**：  
> - **非迭代、静态架构**，适合实时应用；  
> - **无需超参数调节**，避免 loss weighting 的敏感性；  
> - **保持预测精度的同时显著降低约束违反**；  
> - **天然具备正则化效果**，在低数据场景表现更鲁棒。

---

## 2. 核心实验方法和设置

### 使用的数据集
实验基于一个典型的化工系统——**连续搅拌釜反应器 (Continuous Stirred-Tank Reactor, CSTR)** 的稳态建模任务，通过求解机理方程生成仿真数据。

#### 反应体系：
$$
\mathrm{A + 2B \rightleftharpoons C}
$$

#### 输入输出定义：
- **1D case**: 输入 $ x = [C_{A0}] $（进料浓度），温度固定 $ T = 350K $
- **2D case**: 输入 $ x = [C_{A0}, T] $，两者均变化
- 输出 $ y = [C_A, C_B, C_C] $：三种组分的出口浓度

#### 强制施加的物理约束：
1. **物种 A 的摩尔平衡**（非线性）：
   $$
   g_1 = C_{A0} - C_A + r_A \cdot \tau = 0,\quad r_A = -k_f C_A C_B + k_r C_C
   $$
2. **总质量守恒**（线性）：
   $$
   g_2 = C_{A0} + C_{B0} + C_{C0} = C_A + C_B + C_C
   $$

> 注：$ k_f, k_r $ 由 Arrhenius 方程决定，引入强非线性。

---

### 实验设置和评估指标

#### 模型结构
所有模型采用相同的 NN 主干：
- 2 个隐藏层，每层 32 个神经元；
- 激活函数：ReLU；
- 训练算法：Adam，学习率 $10^{-4}$，共 1000 轮；
- 数据划分：60% 训练，20% 验证，20% 测试。

#### 基线方法对比
| 方法 | 类型 | 描述 |
|------|------|------|
| **Standard NN** | 黑箱模型 | 不含任何物理约束 |
| **Soft-constrained PINN** | 软物理约束 | 将 $g_1, g_2$ 加入 loss 作为 penalty 项，权重 $\mu = [0.01, 0.05]$ |
| **KKT-hPINN** | 硬约束（仅线性） | 仅能处理线性约束 $g_2$ |
| **PL-KKT-hPINN** | 本文方法 | 处理 $g_1$(非线性)+$g_2$(线性) 的联合硬约束 |

#### 评估指标
1. **Test RMSE**：测试集上的预测误差（衡量准确性）
2. **Mean Constraint Violation**：平均绝对约束违反值（衡量物理一致性）
3. **Inference Time / Computation Cost**：推理耗时与区域数量的关系
4. **Data Efficiency**：不同训练样本量下的性能变化

---

## 3. 主要实验结果和性能指标

### 关键性能数据

#### （1）预测精度（Test RMSE）
| 方法 | 1D case (RMSE) | 2D case (RMSE) |
|------|----------------|----------------|
| Standard NN | ~0.012 | ~0.014 |
| PINN | ~0.012 | ~0.014 |
| PL-KKT-hPINN | **~0.011** | **~0.013** |

> ✅ **结论**：PL-KKT-hPINN 在保持甚至略优预测精度的同时实现了硬约束满足。

#### （2）约束违反程度（Constraint Violation）
| 方法 | 非线性约束 $g_1$ 违反（训练+推理） |
|------|------------------------------------|
| Standard NN | $10^{-2} \sim 10^{-1}$ |
| PINN | $10^{-3} \sim 10^{-2}$ |
| PL-KKT-hPINN | **$10^{-6} \sim 10^{-5}$** |

> 🔺 **提升幅度**：相比 PINN 下降 **3–4 个数量级**！

#### （3）消融实验：线性化区域数的影响（Number of Regions）
- 当区域数增加时：
  - 约束违反持续下降，趋近于 piecewise-linear approximation error；
  - Test RMSE 也略有改善（因搜索空间受限，减少过拟合）；
  - 推理时间呈**线性增长**（因并行投影数量增加）；
- 区域太少（如 2 个）会导致近似失效，性能严重退化。

> 图5 和 图6 显示：约 20–30 个区域即可达到良好平衡。

#### （4）低数据场景下的鲁棒性（Data Efficiency）
- 在训练样本少于 200 的情况下：
  - Standard NN 出现明显过拟合，RMSE 快速上升；
  - PL-KKT-hPINN 因约束限制了可行输出空间，表现出更强的泛化能力；
  - 在最小样本量下，PL-KKT-hPINN 的 RMSE 比 NN 低 **30–50%**。

> 📌 **说明**：约束起到了“结构正则化”作用。

#### （5）与 PINN 的直接比较
- PINN 经过 Pareto 前沿调参后仍无法达到 PL-KKT-hPINN 的约束满足水平；
- 所有模型预测误差相近，但 **PL-KKT-hPINN 在约束满足上有压倒性优势**；
- PL-KKT-hPINN 无需反复调参，一次训练即得稳定结果。

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **PL-KKT-hPINN 成功将 KKT-hPINN 扩展至非线性约束领域**，通过分段线性近似 + 局部闭式投影的方式，在不牺牲效率的前提下实现了对非线性等式的近似硬约束；
2. ✅ **在预测精度相当的情况下，约束违反比标准 NN 和 PINN 降低数个数量级**；
3. ✅ **在低数据 regime 下更具鲁棒性**，验证了约束作为正则化的有效性；
4. ✅ **无需调节惩罚权重**，解决了 PINN 中常见的 loss balancing 问题；
5. ✅ **架构静态、非迭代、可并行化**，更适合工业部署。

### 方法的局限性
1. ❗ **近似误差来源于 piecewise-linear 表示**，若函数高度非线性或梯度剧烈变化（如高温区 Arrhenius 项），需更多区域才能精确逼近；
2. ❗ **当前仅适用于等式约束**，未涵盖不等式约束（如操作边界、稳定性条件）；
3. ❗ **指示函数虽非可微，不影响训练，但可能影响某些基于梯度的下游任务**（如优化中的 sensitivity analysis）；
4. ❗ **区域划分目前为均匀网格**，未自适应捕捉高曲率区域，可能导致资源浪费或精度不足。

### 未来工作方向
1. ✅ 探索更高效的 **piecewise-linear 表示方式**，例如基于 **Linear Decision Trees** 或自适应分区；
2. ✅ 设计针对 **非线性不等式约束** 的扩展版本；
3. ✅ 充分利用 **并行结构** 实现 GPU 加速，缓解多区域带来的计算开销；
4. ✅ 将 PL-KKT-hPINN 应用于更复杂的动态系统或多尺度建模任务；
5. ✅ 结合不确定性量化（如 Bayesian NN）构建可信的物理一致代理模型。

---

> 💡 **总体评价**：  
> PL-KKT-hPINN 是一类兼具**理论严谨性、工程实用性与计算高效性**的新型 hPINN 框架，为在深度学习中融合复杂非线性物理规律提供了重要路径，尤其适用于**数据稀缺、安全性要求高的化工过程建模与优化**场景。

</details>

---

### 10. [From Senses to Decisions: The Information Flow of Auditory and Visual Perception in Multimodal LLMs](https://arxiv.org/abs/2606.10147)

**Authors**: Wish Suharitdamrong, Muhammad Awais, Xiatian Zhu, Sara Atito  
**Category**: cs.AI  
**Published**: 2026-06-10  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2606.10147v1  

#### Abstract
Multimodal Large Language Models (MLLMs) can listen and see, but how do audio and visual signals actually travel through the network to shape an answer? Despite their growing role in research and real-world applications, the internal pathways through which audio and visual tokens influence the final...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# From Senses to Decisions: The Information Flow of Auditory and Visual Perception in Multimodal LLMs  
**论文核心总结**

---

## 1. 论文的主要贡献和创新点

### ✅ 解决了什么问题
本文首次系统性地研究了 **Audio-Visual Large Language Models (AVLLMs)** 中音频与视觉信息如何在模型内部流动并最终影响决策的问题。尽管 AVLLMs 在多模态任务中表现优异，但其内部的信息流机制（即：音频和视觉信号如何被处理、整合并传递到输出）长期缺乏可解释性分析。

具体而言，论文聚焦以下开放问题：
- 音频和视觉信息是否遵循与 VLMs/VideoLLMs 相同的流动路径？
- 多个独立的音视频输入是如何被路由和整合的？
- 是否存在冗余的 token？能否在信息传递完成后丢弃以提升效率？

### ✅ 提出了什么新方法或新思路
作者采用 **mechanistic interpretability** 中的 **Attention Knockout** 方法，对 AVLLMs 进行因果干预分析，追踪信息流动路径。主要创新包括：

- **首次将信息流分析扩展至 AVLLMs**：结合音频与视觉双模态，揭示跨模态信息如何协同作用。
- **提出“信息聚合点”（aggregation point）概念**：指出在不同输入配置下，信息通过特定位置（如 question 或 reference token）汇聚，并非直接流向预测。
- **验证 token discard 可行性**：证明一旦信息完成转移，原始 multimodal 和部分 text tokens 可安全移除，不影响甚至轻微提升性能。

### ✅ 相比现有方法的优势
| 方面 | 优势 |
|------|------|
| **可解释性深度** | 超越传统注意力可视化，使用因果干预揭示真实信息流而非表象注意力模式（如 attention sinks）。 |
| **通用性** | 结论在多个模型（Qwen2.5-Omni、Video-SALMONN2 Plus）、规模（3B/7B）和数据集上一致成立。 |
| **效率潜力** | 揭示 token discard 的可行性，为后续高效推理提供理论基础，优于仅依赖输入压缩的方法。 |

---

## 2. 核心实验方法和设置

### 📚 使用的数据集
| 数据集 | 类型 | 任务描述 |
|--------|------|----------|
| **AV-SpeakerBench** [33] | 单个 audio-visual 视频 | 多选问答（MCQ），强调跨模态锚定（anchor-target design），需联合听觉与视觉理解。 |
| **AV-Odyssey** [14] | 多个交错音视频项 | 匹配任务：一个参考项 vs 四个候选项（图像↔音频），测试多输入处理能力。 |
| **WorldSense** [17] | 音视频视频（补充） | 更广泛的识别、推理与理解任务，用于跨数据集泛化验证。 |

### ⚙️ 实验设置
- **模型**：
  - 主要模型：`Qwen2.5-Omni`（3B 和 7B）
  - 对比模型：`Video-SALMONN2 Plus`（3B 和 7B）
- **输入结构**：
  - **单音视频视频**：`[system][video][audio][question] → answer`
  - **多交错输入**：`[candidates][question][reference][options] → answer`
- **方法**：**Attention Knockout**
  - 定义源集合 $S$（key）与目标集合 $T$（query）
  - 在选定层阻断 $T \leftarrow S$ 的注意力连接
  - 测量预测概率变化 $\Delta p = (p_{\text{knockout}} - p_{\text{base}})/p_{\text{base}}$
  - 使用滑动窗口（$k=7$ 层）定位信息流发生的网络深度
- **评估指标**：
  - 准确率（Accuracy）
  - $\Delta p$ 曲线趋势（负值大表示关键路径）
  - 推理延迟（Prefill Latency）

---

## 3. 主要实验结果和性能指标

### 🔢 关键性能数据与对比

#### ✅ 单音视频场景下的信息流（AV-SpeakerBench）
| 发现 | 性能表现 |
|------|---------|
| **信息流路径**：`Modalities → Question → Last` | 与 VLMs/VideoLLMs 一致，形成单一顺序路径 |
| **任务依赖调制**：视觉主导任务（如 Visual Recognition）主要依赖 video；语音识别类任务均衡利用 audio 和 video | $\Delta p$ 显示对应模态贡献显著 |
| **后期 attention 不可靠**：第31层出现 video attention spike，实为 **attention sink**（高激活伪影），mask 后准确率不变甚至略升 | 表1：mask video/audio 后 Accuracy 从 42.24 → 42.52 |

#### ✅ 多交错输入场景（AV-Odyssey）
| 发现 | 性能表现 |
|------|---------|
| **并行路径结构**：存在两条独立路径：<br>1. `Candidates + Question → Reference → Last`<br>2. `Candidates → Option Letters → Last` | 最终预测由 last token 整合两个路径信息 |
| **late-positioned aggregation**：reference 成为聚合点，类似 question 在单视频中的角色 | mask reference → last 导致性能大幅下降 |
| **选项竞争机制**：correct/incorrect option tokens 均参与最后决策竞争 | block incorrect option → last 提升正确率 |

#### ✅ Token Discard 实验（关键效率发现）
| 设置 | 数据集 | Acc 变化 | 推理延迟降低 |
|------|--------|----------|--------------|
| Discard Video (L=26) | AV-SpeakerBench | ±0.50 | ↓ ~199 ms |
| Discard Audio (L=26) | AV-SpeakerBench | ↑ +0.97 | ↓ ~56 ms |
| Discard Ques (L=29) | AV-SpeakerBench | ↑ +0.25 | ↓ ~8.7 ms |
| **Discard All** | AV-SpeakerBench | ≈持平 | **↓ ~199 ms** |
| **Discard All** | AV-Odyssey | ↑ +2.00 (A→I) / +1.05 (I→A) | **↓ ~28 ms** |

> ✅ **结论**：token discard 几乎无损精度，且可带来推理加速，尤其在大规模输入时更明显。

---

## 4. 关键结论和发现

### 🎯 主要发现（Findings）

> **Finding 1**:  
> **Attention allocation is not a reliable indicator of information flow**. Late-layer video attention spikes are caused by **attention sinks**, not meaningful information transfer. Real audio-visual information does **not** reach deep layers.

> **Finding 2**:  
> For **single audio-visual videos**, information flows through a **sequential pathway**:  
> `Modalities → Question → Last`.  
> The relative contribution of audio vs. visual is **task-dependent**, and integration occurs at mid-layers.

> **Finding 3**:  
> For **multiple interleaved audio-visual inputs**, information flows through **two parallel paths**:
> 1. `Candidates + Question → Reference → Last`
> 2. `Candidates → Option Letters → Last`  
> Integration happens independently at the last token.

> **Finding 4**:  
> **Multimodal and text tokens can be discarded after their information is transferred**, with minimal impact on accuracy or even slight improvement. This enables **more efficient inference** across tasks and models.

---

### ⚠️ 方法的局限性
- **局限于 MCQ 任务**：所有实验基于单 token 输出的 multiple-choice 问答，未涵盖 open-ended generation（如 captioning）或对话任务。
- **依赖 Attention Knockout 假设**：该方法假设阻断注意力即阻断信息流，可能忽略其他潜在路径（如 MLP 层传播）。
- **未覆盖所有 AVLLM 架构变体**：虽验证多种模型，但仍集中于主流架构，极端设计可能不适用。

---

### 🔮 未来工作方向
1. **Efficiency via Internal Token Compression**：基于 token discard 发现，开发动态压缩策略，在 LLM 内部层自动移除冗余 token。
2. **Modality Steering**：探索如何主动调节模型对 audio/video 的依赖比例，优化在某一模态被低估的任务上的表现。
3. **Understanding Visual Bias**：结合 counterfactual analysis，探究为何 AVLLMs 存在 **visual bias**，并在信息流路径中定位偏差来源。
4. **Extension to Open-ended Generation**：将信息流分析拓展至生成式任务（如 captioning），检验是否存在不同的路由机制。

---

## 总结
本论文是首个对 AVLLMs 内部信息流进行系统性 mechanistic interpretability 分析的工作。它揭示了：
- 音视频信息通过 **mid-layer 聚合点**（question/reference）间接影响预测；
- 注意力热点常为 **sink artifacts**，不可靠；
- 存在 **任务驱动的模态权重分配**；
- 并提出了 **token discard for efficiency** 的新范式。

这些发现不仅增强了我们对 AVLLMs 工作机制的理解，也为下一代更高效、可控、可解释的多模态模型设计奠定了基础。

</details>

---

### 11. [Self-Distillation Policy Optimization via Visual Feedback: Bridging Code and Visual Artifacts](https://arxiv.org/abs/2606.10334)

**Authors**: Haoyu Dong  
**Category**: cs.AI  
**Published**: 2026-06-10  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2606.10334v1  

#### Abstract
Code-generating large language models (LLMs) increasingly produce visual artifacts such as charts, web pages, and slides by writing programs that are executed by non-differentiable renderers, committing to code before observing the render. As a result, otherwise executable code often yields artifact...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Self-Distillation Policy Optimization via Visual Feedback: Bridging Code and Visual Artifacts*

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
当前基于 **Code-generating LLMs** 在生成可视化内容（如图表、网页、幻灯片）时面临“**代码-视觉鸿沟**”（code-vision gap）：
- 模型必须在**未看到渲染结果前提交代码**；
- 即使语法正确，生成的代码常导致视觉缺陷，例如：
  - 元素重叠（overlap）
  - 文本被裁剪（clipping）
  - 对齐错误（misalignment）
  - 颜色对比度低（low contrast）
  - 内容溢出（overflow）

现有方法存在以下局限：
- **Inference-time visual reflection**（如 render-critique-revise）需要多次调用 renderer 和 VLM，推理成本高；
- **Visual-reward RL**（如 GRPO/DPO）仅提供**稀疏的标量奖励信号**，缺乏对具体缺陷位置的定位能力。

---

### 🚀 提出的新方法：**Visual-SDPO**

提出一种新的自蒸馏策略优化框架 —— **Visual-SDPO**（Visual Self-Distillation Policy Optimization），其核心思想是：

> 利用**渲染后的视觉反馈作为特权上下文**（privileged context），由一个与学生共享权重的教师模型进行监督，将视觉理解“蒸馏”回不依赖 renderer 的学生策略中。

#### 主要创新点：

1. **Visual-Feedback Self-Distillation**
   - 教师模型接收原始输入 `x` + 渲染图像/结构化诊断 `v`；
   - 学生只接收原始输入 `x`；
   - 教师不对代码重新生成，而是对学生的输出序列进行**重新打分**（rescore）；
   - 通过 token-level KL 散度实现知识迁移。

2. **Visual-Grounded Code Credit Weighting**
   - 引入空间感知机制，将检测到的视觉缺陷（如重叠区域）映射回生成该元素的**代码语句**；
   - 为每个 token 分配加权系数，放大与缺陷相关的代码部分的梯度信号；
   - 权重公式：  
     $$
     w_t = 1 + (\alpha - 1) \cdot \text{resp}(s(t)),\quad \text{其中 } \text{resp}(s) = \max_{\text{defect}} \text{IoU} \times \text{severity}
     $$

3. **结合 GRPO 序列级奖励**
   - 加入 GRPO（Group Relative Policy Optimization）目标，形成联合训练目标：
     $$
     \mathcal{L}(\theta) = \mathcal{L}_{\text{VSDPO}} + \beta \cdot \mathcal{L}_{\text{GRPO}}
     $$
   - GRPO 提供执行成功性和整体视觉质量的全局锚定信号，增强训练稳定性。

---

### 🔍 相比现有方法的优势

| 维度 | 传统方法（如 GRPO） | Visual-SDPO |
|------|---------------------|-------------|
| 反馈密度 | 稀疏（scalar reward） | 密集（token-level + spatially grounded） |
| 定位能力 | 无 | 支持缺陷到代码语句的追溯 |
| 推理开销 | 无额外开销（RL） | **无额外推理成本**（student 不需 renderer） |
| 训练效率 | 需大量 rollout | 更**样本高效**（约仅需 GRPO 29% 的 rollout 数量） |
| 多任务统一性 | 通常单领域 | 在 chart/web/slide 上使用**统一 backbone** 成功 |

---

## 2. 核心实验方法和设置

### 📚 数据集

分别在三个领域独立训练与评估，**不跨域混合数据**：

| 领域 | 训练数据 | 评估基准 |
|------|----------|-----------|
| **Chart** | Chart2Code-160K（可执行子集） | ChartMimic (Direct Mimic) |
| **Web/UI** | WebCode2M + WebSight | Design2Code |
| **Slide** | AeSlides-7k（instruction-only） | AeSlides eval split（aspect ratio, whitespace, collision, imbalance） |

---

### ⚙️ 实验设置

- **Backbone**: 统一使用 **Qwen3-VL-8B-Instruct**
- **视觉信号通道**（two-channel design）：
  1. **Image Channel**：教师接收渲染图像截图（若失败则传错误日志）
  2. **Rubric Channel**：轻量级预训练模块提取结构化缺陷表（JSON格式），作为补充上下文
- **缺陷检测与映射**：
  - **Region-to-code mapping** 采用两种方式：
    - **Runtime introspection**（优先）：hook 渲染器记录每条语句生成的区域（matplotlib / playwright / python-pptx）
    - **VLM-based mapping**（备用）：用 Qwen3-VL 自动识别责任语句
- **训练流程**：
  - 可选 warm-start：先在有标签数据上做 SFT
  - 主阶段：联合优化 $\mathcal{L}_{\text{VSDPO}} + \beta \mathcal{L}_{\text{GRPO}}$

---

### 🎯 评估指标

| 领域 | 主要指标 |
|------|---------|
| **ChartMimic** | Overall = (Low + High)/2<br>- Low: 四项低级指标 F1 平均值（Text, Layout, Chart-Type, Color）<br>- High: GPT-4o judge 得分 |
| **Design2Code** | Overall = 五项低级指标算术平均（CLIP, Block-Match, Text, Position, Color） |
| **AeSlides** | Avg = 四项可验证规则得分平均（aspect ratio, whitespace, collision, imbalance） |

---

### 🆚 基线方法对比

所有方法共用相同 backbone 与训练数据，公平比较：

| 基线 | 描述 |
|------|------|
| **Zero-shot** | 原始 Qwen3-VL-8B-Instruct 直接推理 |
| **+SFT** | 在对应训练集上进行监督微调 |
| **+OPSD** | 使用参考代码作为特权信息的自蒸馏（reference-code privileged teacher） |
| **+GRPO (visual reward)** | 使用视觉相似性等 scalar reward 进行 GRPO 优化 |

---

## 3. 主要实验结果和性能指标

### 📊 表格汇总关键性能（提升均为相对于 zero-shot 的绝对增益 △）

#### Table 1: ChartMimic 结果

| Method | Exec (%) | Low (%) | High (%) | **Overall (%)** | △ |
|--------|----------|--------|----------|------------------|----|
| Zero-shot | 81.7 | 62.9 | 72.9 | 67.9 | — |
| +SFT | 90.3 | 69.9 | 77.2 | 73.6 | +5.7 |
| +OPSD | 92.3 | 73.9 | 80.1 | 77.0 | +9.1 |
| +GRPO | 92.9 | 72.6 | 79.7 | 76.2 | +8.3 |
| **+Visual-SDPO (Ours)** | **92.7** | **74.8** | **82.3** | **78.6** | **+10.7** |

> ✅ 超越最强单信号基线（OPSD）+1.6 pts；超越零样本超 10 pts。

---

#### Table 2: Design2Code 结果

| Method | CLIP | Block | Text | Position | Color | **Overall** | △ |
|--------|------|-------|------|----------|-------|------------|----|
| Zero-shot | 85.4 | 50.2 | 78.1 | 71.9 | 74.7 | 72.1 | — |
| +SFT | 87.1 | 59.6 | 82.3 | 77.2 | 78.8 | 77.0 | +4.9 |
| +OPSD | 87.4 | 62.3 | 82.9 | 78.4 | 81.8 | 78.6 | +6.5 |
| +GRPO | 88.3 | 64.5 | 83.3 | 78.7 | 85.1 | 80.0 | +7.9 |
| **+Visual-SDPO (Ours)** | **89.2** | **69.7** | **84.9** | **82.4** | **86.8** | **82.6** | **+10.5** |

> ✅ 最大增益来自 **Position (+3.7)** 和 **Block-Match (+5.2)**，说明 region-to-code mapping 对布局类缺陷特别有效。

---

#### Table 3: AeSlides 结果

| Method | **Avg** | △ |
|--------|--------|----|
| Zero-shot | 49.5 | — |
| +SFT | 52.8 | +3.3 |
| +GRPO | 58.2 | +8.7 |
| **+Visual-SDPO (Ours)** | **60.7** | **+11.2** |

> ✅ 尽管 GRPO 已带来显著提升，Visual-SDPO 仍能进一步增益 +2.5 pts，表明 token-level credit assignment 在规则对齐任务中仍有价值。

---

### 🔬 消融实验发现

- **非单调增益模式**：在某些任务中，单独使用 OPSD 或 GRPO 可能略优于另一方，但两者结合（即 Visual-SDPO）始终最优。
- **Credit Weighting 至关重要**：
  - 若取消 `resp(s)` 加权（设 α=1），性能明显下降；
  - 缺陷相关语句获得更强梯度更新，显著改善视觉质量。
- **训练效率优势**：
  - Visual-SDPO 在**更少 rollout 数量下达到甚至超过 GRPO 的最终性能**；
  - 平均仅需 GRPO 所需 rollout 数量的 **~29%**，大幅降低训练成本。

---

## 4. 关键结论和发现

### ✅ 主要结论

1. **Visual-SDPO 是首个将视觉反馈用于 self-distillation 中的 token-level credit assignment 框架**，实现了从像素缺陷到代码语句的责任追溯。
2. **密集、局部化的监督信号显著优于稀疏标量奖励**，尤其在修复具体视觉瑕疵方面更具针对性。
3. **教师利用渲染图像或结构化 rubric 作为特权上下文，可在无需修改推理架构的前提下，将视觉理解注入学生策略**。
4. **Visual-Grounded Code Credit Weighting 有效缓解了 uniform KD 导致的策略漂移问题**，确保梯度集中在真正影响视觉输出的代码部分。
5. **在 chart、web、slide 三大任务上，使用统一 backbone 实现一致且显著的性能突破（+10+ pts）**，展现出良好的泛化性和实用性。

---

### ⚠️ 局限性

1. **依赖 renderer instrumentation 或 VLM mapping**：
   - Runtime introspection 需要对特定工具链（如 matplotlib）进行插桩；
   - VLM-based mapping 虽通用但增加计算负担。
2. **静态映射限制**：
   - 当前方法适用于一次性渲染任务，难以处理多步交互式 UI 流程。
3. **缺陷检测模块为外部组件**：
   - 缺陷检测器和 rubric extractor 是预定义或预训练的，可能成为瓶颈。

---

### 🔮 未来工作方向

1. **扩展至大规模 chart-RL 训练范式**，探索更大规模视觉反馈训练潜力；
2. **引入 differentiable rendering 作为第三种视觉反馈通道**，实现端到端可导优化；
3. **将 region-to-code mapping 扩展到动态、多步交互场景**，支持复杂前端调试；
4. **探索自动化的缺陷检测与 credit assignment pipeline**，减少对外部模块依赖。

--- 

> 💡 **一句话总结**：  
> **Visual-SDPO 开创性地将渲染后的视觉缺陷“反向追踪”至源代码语句，并通过加权自蒸馏机制实现高效、精准的策略优化，在保持零推理开销的同时，全面超越现有 RL 与蒸馏方法。**

</details>

---

### 12. [WebChallenger: A Reliable and Efficient Generalist Web Agent](https://arxiv.org/abs/2606.10423)

**Authors**: Jayoo Hwang, Xiaowen Zhang, Vedant Padwal  
**Category**: cs.CL  
**Published**: 2026-06-10  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2606.10423v1  

#### Abstract
Autonomous web navigation remains challenging for LLM agents, and the strongest generalist systems rely on proprietary reasoning models whose inference cost is prohibitive for the repetitive tasks where such agents would be most useful. We argue this gap stems not from insufficient model capability ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# WebChallenger: A Reliable and Efficient Generalist Web Agent 论文总结

## 1. 论文的主要贡献和创新点

### 解决的问题
当前基于 **LLM** 的通用网页代理（generalist web agent）在执行长周期、复杂的网页导航任务时仍显著落后于人类表现。尽管模型本身具备强大的推理能力，但现有框架存在以下三大认知鸿沟：
- **注意力分散**：将整个网页（如可访问性树或截图）作为扁平化输入，导致关键信息被无关内容稀释。
- **缺乏持久记忆**：每次会话都从零开始，无法复用对网站结构和交互模式的认知。
- **缺乏程序性熟练度**：每个原子操作都需要重新观察和推理，无法将常见多步交互（如下拉选择、表单填写）封装为自动化流程。

此外，最先进的系统依赖昂贵的专有模型（如 GPT-4o, GPT-5），推理成本高昂，难以用于需要重复执行的自动化场景。

### 提出的新方法和新思路
论文提出了 **WebChallenger**，一个通过架构设计而非模型规模来提升性能的通用网页代理框架。其核心是 **PageMem**——一种从 **DOM** 确定性构建的结构化页面表示。

在此基础上，实现了三个模拟人类认知优势的机制：
1. **分而治之的观察管道 (Divide-and-Conquer Observation Pipeline)**：
   - 将页面分解为具有摘要的语义区域（`PageSection`）。
   - 代理首先浏览摘要以筛选相关区域，然后仅对这些区域进行详细处理，生成信息密集的观察结果。

2. **轻量级探索与记忆系统 (Lightweight Exploration and Memory System)**：
   - 在任务执行前，通过一次离线探索遍历整个目标网站。
   - 构建 **WebsiteMem**，持久存储所有页面的 `PageMem`、导航路径和交互元素行为（如点击后展开的下拉菜单项）。
   - 支持书签（bookmarks）和对隐藏元素的上下文感知。

3. **复合动作工作流 (Compound Action Workflows)**：
   - 将常见的多步交互（如搜索、下拉选择、表单提交）抽象为单一的高级代理动作。
   - 工作流内部自动处理中间状态变化（如输入框填充、下拉列表展开），无需代理重新决策。

### 相比现有方法的优势
- **高效且低成本**：使用开源、小规模模型（`GLM-4-32B`, `Qwen2.5-VL-7B`）即可达到接近专有前沿模型的性能，推理成本仅为后者的极小一部分。
- **强泛化能力**：所有机制均基于通用的 `PageMem` 抽象，无需针对特定网站进行适配（site-specific adapters）。
- **架构驱动的性能提升**：证明了通过精心设计的观察、记忆和行动架构，可以极大地释放现有 **LLM** 的潜力，而无需依赖更大的模型或微调。

## 2. 核心实验方法和设置

### 使用的数据集
在四个公开的网页导航基准测试上进行了评估，覆盖了多样化的任务类型：
- **WebArena**：包含 812 个任务，模拟论坛、维基等常见网站类型，结合程序化和 **LLM** 评估。
- **VisualWebArena**：基于 WebArena 架构，但包含 910 个需要视觉推理的任务。
- **Online-Mind2Web**：包含 300 个任务，跨越 136 个真实世界网站，采用人工评估。
- **WorkArena**：包含 330 个企业级任务，要求代理处理复杂的用户界面。

### 实验设置和评估指标
- **模型**：使用 `GLM-4-32B-0414` 作为主 **LLM** 控制器，`Qwen2.5-VL-7B-Instruct` 作为辅助的 **VLM** 用于图像描述。在 `VisualWebArena` 上使用 `Qwen3-VL-4B-Instruct`。
- **训练**：**Zero-shot** 设置，未对任何模型进行微调。
- **评估指标**：主要成功率为（success rate %），即代理正确完成任务的比例。
- **预处理**：在运行推理前，先对所有基准测试的网站进行一次性的离线探索，构建 `WebsiteMem`。
- **计算成本**：实验总电力成本估计约为 23 美元，展示了其经济性。

### 基线方法对比
与两类强大的基线进行了比较：
- **专有模型基线 (Proprietary Models)**：如 `GenericAgent` (GPT-4o, Claude 3.5 Sonnet), `WALT` (GPT-5), `ScribeAgent` 等。
- **开源模型基线 (Open-Source Models)**：包括经过微调的模型如 `Agent-as-Annotators`, `Mobile-Agent-v3.5`, `WebDreamer`，以及其他零样本方法如 `Tree Search`。

## 3. 主要实验结果和性能指标

### 关键性能数据
WebChallenger 在所有四个基准测试上均取得了使用开源模型的最佳成绩（SOTA）：
- **WebArena**: **56.3%**
- **VisualWebArena**: **48.7%**
- **Online-Mind2Web**: **51.0%**
- **WorkArena**: **70.9%**

### 与基线方法的对比结果
- **超越开源基线**：在 `WebArena` 上，以 56.3% 的成绩大幅超过最强的微调开源基线 `Mobile-Agent-v3.5` (48.4%)，领先 7.9 个百分点，并超过了使用 `GPT-4o` 作为规划器的 `ScribeAgent` (53.0%)。
- **逼近专有模型**：在 `WorkArena` 上，70.9% 的成绩不仅远超其他开源方法，甚至超过了 `Claude 3.5 Sonnet` (56.4%) 和 `GPT-4o` (45.5%) 这些专有模型的骨干。
- **泛化能力强**：在 `Online-Mind2Web` 上取得 51.0% 的成绩，表明该框架能够利用跨网站的通用结构模式，而非依赖特定站点的适应。

### 消融实验结果
在 `WebArena-lite` 子集上进行了消融研究，量化了各组件的贡献：
- **移除观察管道 (`-observation pipeline`)**：平均成功率下降 **17.6** 个百分点（至 41.2%），影响最大。这证明了“分而治之”策略对于处理复杂页面至关重要。
- **移除复合动作 (`-compound actions`)**：平均成功率下降 **9.7** 个百分点（至 49.1%）。在涉及复杂表单的 `CMS` 环境中影响尤为显著（-20.0%）。
- **移除记忆 (`-memory`)**：平均成功率下降 **7.6** 个百分点（至 51.2%）。在 `Maps` 环境中影响较小，因其交互相对简单。

**效率分析**：
- 移除观察管道虽然减少了总 **token** 数，但使单次提示的 **token** 数激增 4.75 倍，且步骤数从 7.2 增加到 11.26，说明其用计算换来了性能和效率。
- 移除复合动作导致总 **token** 数和步骤数显著增加，证明了工作流在提高代理决策效率方面的关键作用。

## 4. 关键结论和发现

### 主要发现
1. **模型能力已足够，关键在于架构**：当前的 **LLM** 已经具备解决许多常见网页任务所需的智能，性能瓶颈不在于模型本身的知识或推理能力，而在于标准框架未能提供有效的“脚手架”（scaffolding）来支持**选择性注意**、**持久记忆**和**程序性熟练度**。
2. **架构设计优于模型堆料**：WebChallenger 通过巧妙的架构设计，在不使用更大模型或微调的情况下，性能远超许多依赖专有模型的系统，证明了**架构创新**的巨大潜力。
3. **PageMem 是成功的关键**：统一的 `PageMem` 表示是实现跨网站泛化和集成三大机制的基础，它将原始的 **DOM** 转化为代理可以有效推理的语义层次结构。

### 方法的局限性
- **依赖手工设计的启发式规则**：框架中的组件（如 `DOM` 分区、可点击元素识别、探索规则、工作流）都是手动设计的，编码了关于网页组织方式的先验知识。在严重偏离常规模式的网站上，性能可能会下降。
- **顺序调用开销大**：为了实现精细化控制，框架使用了大量的顺序 **LLM** 调用，这增加了单个任务的墙钟时间（wall-clock time），如果使用昂贵的专有模型API，成本会很高。
- **内存实例化较基础**：本文采用了最小化的内存实现，更高级的记忆机制（如在线工作流学习）留待未来研究。
- **未评估对抗性鲁棒性**：所有评估都在良性任务上进行，系统对恶意网页内容（如弹窗攻击）的鲁棒性未知。

### 未来工作方向
- 探索更高级的内存机制，例如基于 `WebsiteMem` 实现 **Agent Workflow Memory** 或 **SkillWeaver** 中提出的在线学习和技能提炼。
- 研究如何减少顺序 **LLM** 调用的数量，以降低延迟和成本。
- 增强框架对非标准网页布局和动态内容的适应能力。
- 评估并增强代理在对抗性环境下的安全性和鲁棒性。

</details>

---

### 13. [UniSVQ: 2-bit Unified Scalar-Vector Quantization](https://arxiv.org/abs/2606.10520)

**Authors**: Haoyu Wang, Haiyan Zhao, Xingyu Yu, Zhangyang Yao, Xu Han, Zhiyuan Liu, Maosong Sun  
**Category**: cs.CL  
**Published**: 2026-06-10  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2606.10520v1  

#### Abstract
Post-training quantization at the 2-bit level enables low-cost deployment and inference acceleration for large language models (LLMs). Scalar quantization (SQ) and vector quantization (VQ) are two primary quantization methods, however, the former suffers from significant performance degradation, and...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文《UniSVQ: 2-bit Unified Scalar-Vector Quantization》核心总结**

---

## **1. 论文的主要贡献和创新点**

### **解决的问题**
大型语言模型（LLMs）在部署时面临高昂的计算和存储成本。**Post-training quantization (PTQ)** 是一种主流压缩技术，尤其在极低比特（如 2-bit）量化中，存在以下挑战：
- **Scalar Quantization (SQ)**：虽然计算高效，但性能退化严重，尤其是在处理权重分布中的 **outliers** 时。
- **Vector Quantization (VQ)**：性能优越，但引入额外的 **codebook 存储开销** 和复杂的解码过程，影响推理吞吐。

UniSVQ 旨在解决这一矛盾：**如何在保持 SQ 高效性的同时，获得接近 VQ 的重建精度？**

---

### **提出的新方法与创新思路**
论文提出了 **UniSVQ**，一个统一的 2-bit 量化框架，其核心思想是：

> **将量化网格（quantization grid）参数化为整数格点的仿射变换（affine transform），从而桥接 SQ 与 VQ。**

具体创新包括：
- **Linear-constrained quantization grid**：  
  量化值定义为 $ \mathcal{Q}(w) = A \cdot w_{\text{int}} + B $，其中 $ A \in \mathbb{R}^{d\times d}, B \in \mathbb{R}^d $ 是可学习参数。这使得 codebook 具有结构化形式，避免了传统 VQ 中无结构 codebook 带来的存储和访问瓶颈。
- **与优化内核兼容**：该仿射变换可提前作用于激活值，从而复用高度优化的 **integer Matmul kernels**（如 GPTQ 中使用的），提升推理效率。
- **Block-wise fine-tuning**：通过最小化重建误差（MSE loss）对 $ A $ 和 $ B $ 进行逐层微调，实现数据驱动的量化误差补偿。

---

### **相比现有方法的优势**
| 维度 | 优势 |
|------|------|
| **性能** | 显著优于 SOTA SQ 方法（如 GPTQ、SpinQuant、OSTQuant），接近甚至超越部分 VQ 方法（如 AQLM、QuIP#） |
| **效率** | 仅需每权重矩阵 **20 个额外浮点参数**（$4\times4 + 4$），codebook 存储减少约 **64倍**，支持高效推理 |
| **灵活性** | 支持从 2-bit 扩展到更高 bit-width（如 3-bit），无需重新设计 codebook 结构 |
| **通用性** | 在 Qwen 和 Llama 系列模型上均表现优异，具备良好架构泛化能力 |

---

## **2. 核心实验方法和设置**

### **使用的数据集**
- **校准与微调数据**：从 **RedPajama** 数据集中随机采样 1,024 条序列（长度 2,048）用于 Hessian 计算和 fine-tuning。
- **评估任务**：
  - **PPL（Perplexity）**：在 **WikiText-2** 和 **C4** 上评估语言建模能力。
  - **Zero-shot QA 准确率**：在多个下游任务上测试，包括：
    - ARC-Easy / ARC-Challenge (AC, AE)
    - BoolQ (BQ)
    - HellaSwag (HS)
    - PIQA (PQ)
    - WinoGrande (WG)

评估工具：`LM-Evaluation-Harness`

---

### **实验设置与评估指标**
- **量化位宽**：主要为 **2-bit**，并在 Llama-3-8B 上验证 **3-bit** 可扩展性。
- **量化粒度**：vector dimension $ d = 4 $，即每次量化 4 个连续权重。
- **预处理**：应用 **Randomized Hadamard Transform (RHT)** 抑制 outliers，使权重分布更接近各向同性高斯分布。
- **量化算法**：采用 **LDLQ** 进行误差补偿量化。
- **Fine-tuning 设置**：
  - Batch size: 16
  - Learning rate: 5e-5
  - Epochs: 最多 5 轮，早停阈值 3
  - 数据划分：训练/验证 = 7:1

---

### **基线方法对比**
#### **Scalar Quantization Baselines**
- **GPTQ**：经典 PTQ 方法，直接量化原始权重。
- **QuIP**：基于 RHT 的正交变换方法。
- **SpinQuant**：使用可学习正交变换。
- **OSTQuant**：引入 QSUR 指标优化量化网格。

#### **Vector Quantization Baselines**
- **AQLM**：基于聚类的 VQ，使用两级 1-bit codebook。
- **QuIP#**：基于数学最优 E8 lattice codebook 的 VQ 方法。
- （附录中还对比了 **Qtip**，使用卷积码结构）

所有方法均使用相同校准数据，确保公平比较。

---

## **3. 主要实验结果和性能指标**

### **关键性能数据（以 Qwen-3-32B 为例）**
| 方法 | WikiText PPL ↓ | 平均 Zero-shot Accuracy ↑ | 相对 FP16 性能 (%) |
|------|----------------|----------------------------|--------------------|
| FP16 (Full Precision) | 7.61 | 78.01 | 1.00 |
| GPTQ (SQ) | 1.38E4 | 36.09 | 0.46 |
| OSTQuant (SQ) | 14.79 | 68.29 | 0.88 |
| QuIP# (VQ) | 9.04 | 76.30 | 0.98 |
| **UniSVQ (Proposed)** | **9.26** | **76.15** | **0.98** |

> ✅ UniSVQ 在 PPL 和准确率上均显著优于所有 SQ 方法，并达到与 QuIP# 相当的水平。

---

### **与其他模型规模的结果汇总**
- 在 **Qwen-3-4B 到 32B** 和 **Llama-3-8B-Instruct** 上一致取得：
  - **平均 zero-shot 准确率提升 5–15 pts** 超过最强 SQ 方法
  - **PPL 接近或优于 VQ 方法**
  - **性能相对 FP16 达到 87–98%**

例如，在 Llama-3-8B 上：
- UniSVQ 平均准确率达 **67.62%**，远超 GPTQ（37.50%）、QuIP（38.70%）
- 仅次于 QuIP#（69.72%），优于 AQLM（59.84%）

---

### **消融实验结果**

#### **(1) 是否进行 fine-tuning**
| 方法 | Qwen-3-8B 平均准确率 | 相对性能 |
|------|------------------------|----------|
| UniSVQ (完整) | 67.95 | 0.92 |
| w/o fine-tuning | 66.99 | 0.90 |
| w/o orthogonal init | 61.00 | 0.82 |

✅ 表明 fine-tuning 显著提升性能，且随机正交初始化优于数学最优 D4 lattice 初始化（因后者破坏协方差结构）。

#### **(2) 向量维度 $ d $ 的影响**
| $ d $ | 是否 fine-tune | 平均准确率 |
|-------|---------------|------------|
| 4 | 否 | 66.99 |
| 8 | 否 | 67.34 |
| 4 | 是 | **67.95** |

➡️ 增加维度带来边际收益，但不如 fine-tuning 明显，且增加计算复杂度 $ O(Nnd) $，故选择 $ d=4 $ 更优。

#### **(3) 是否使用 RHT 预处理**
| 方法 | WikiText PPL | 平均准确率 |
|------|--------------|------------|
| UniSVQ (完整) | 20.04 | 63.42 |
| w/o RHT | 8314.12 | 39.06 |

❌ 移除 RHT 导致性能崩溃至随机水平，说明其对保证权重近似高斯分布至关重要。

#### **(4) 量化器隔离实验（Weight-level MSE & SNR）**
| 方法 | MSE ↓ | SNR (dB) ↑ |
|------|------|-----------|
| GPTQ | 1.12e-3 | -3.45 |
| SpinQuant | 1.06e-3 | -3.06 |
| **UniSVQ** | **7.40e-4** | **8.48** |

✅ UniSVQ 实现更低 MSE 和更高信噪比，证明其量化网格更优。

---

## **4. 关键结论和发现**

### **主要发现**
1. **结构化 codebook 可兼顾性能与效率**：  
   通过将 VQ 的 codebook 参数化为仿射变换，UniSVQ 成功融合了 SQ 的高效性和 VQ 的表达力。
   
2. **fine-tuning 对性能至关重要**：  
   数据驱动地优化仿射参数能有效补偿量化误差，尤其在非均匀权重和激活分布下。

3. **RHT 是必要前提**：  
   它确保权重满足“incoherence”性质，使线性约束量化网格有效。

4. **d=4 是精度与效率的最佳平衡点**：  
   更高维度增益有限，而 fine-tuning 带来的提升更为显著。

5. **UniSVQ 推理更快、内存更省**：  
   在 Llama-3-8B 上：
   - **吞吐量达 101.65 token/s**，比 FP16 快 **1.68×**
   - **峰值 GPU 内存降至 3.87 GB**，减少 >75%
   - 优于 AQLM 和 QuIP#，接近 GPTQ 水平

---

### **方法的局限性**
1. **仅限 weight-only quantization**：未考虑 activation 或 KV-cache 量化，限制端到端推理优化潜力。
2. **依赖 RHT 和 LDLQ 流程**：虽有效，但增加了预处理复杂性。
3. **仿射变换与 GEMM 内核的协同优化尚未深入探索**：当前实现可能未完全释放硬件加速潜力。

---

### **未来工作方向**
- 扩展至 **activation-aware quantization** 和 **KV-cache 压缩**
- 探索 **multi-head 自适应量化** 或 **layer-specific affine 参数共享**
- 将 UniSVQ 思路应用于 **训练时量化（QAT）**
- 进一步优化 CUDA kernel 以更好支持仿射去量化操作

--- 

> 📌 **总结一句话**：  
> **UniSVQ 通过结构化的仿射量化网格，在几乎不增加额外参数的前提下，实现了 2-bit 量化中 VQ 级别的精度与 SQ 级别的推理效率，为 LLM 极低比特部署提供了实用且高效的解决方案。**

</details>

---

### 14. [Pushing the Limits of LLM Tool Calling via Experiential Knowledge Integration and Activation](https://arxiv.org/abs/2606.10875)

**Authors**: Yupu Hao, Zhuoran Jin, Huanxuan Liao, Kang Liu, Jun Zhao  
**Category**: cs.CL  
**Published**: 2026-06-10  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2606.10875v1  

#### Abstract
Large language models (LLMs) rely on tool use to act as autonomous agents, yet often fail in multi-step execution due to insufficient tool-related knowledge and ineffective knowledge activation. Therefore, we present a systematic study on how knowledge influences tool-use performance, covering the s...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Pushing the Limits of LLM Tool Calling via Experiential Knowledge Integration and Activation

## 1. 论文的主要贡献和创新点

### 解决的问题
当前 Large Language Models (LLMs) 在执行多步工具调用（tool calling）任务时，常因缺乏足够的**工具相关经验知识**（experiential knowledge）以及无法有效激活这些知识而导致失败。现有方法大多聚焦于 prompt 设计、API 文档规范或监督对齐，隐含假设模型已具备充分的执行能力，忽略了实际中模型在参数约束、场景化操作模式和错误恢复策略等方面的缺失。

### 提出的新方法与思路
作者提出了 **KATE (Knowledge-Augmented Tool Execution)** 框架，系统性地研究了经验知识在工具执行中的获取、激活与内化全过程，并提出以下创新：

- **知识获取阶段**：构建并比较了四种不同粒度的经验知识形式：
  - **Instance-level**：`Scenario Trajectory Knowledge (ST)` 和 `Experience Summary Knowledge (ES)`
  - **Intent-level**：`Script-Style Intent Clustering Knowledge (SIC)` 和 `Textual-Style Intent Clustering Knowledge (TIC)`
  
  发现**实例级知识**（尤其是执行轨迹）比抽象意图级知识更有效。

- **知识激活阶段**：
  - 推翻传统“加深推理深度”（depth-based prompting）的有效性，发现其收益递减。
  - 提出通过**扩大推理宽度**（width-based parallel sampling with aggregation）来更有效地激活潜在知识。

- **知识内化阶段**：
  - 在训练时通过 post-training 将知识注入数据中，进一步提升性能。
  - 发现 **Reinforcement Learning (RL)** 在知识内化方面优于 Supervised Fine-Tuning (SFT)。

### 相比现有方法的优势
- **系统性视角**：首次从 acquisition → activation → internalization 全流程分析经验知识的作用。
- **高效且可扩展**：仅需高质量的 instance-level 知识即可取得显著增益，无需复杂知识构造。
- **更强的泛化能力**：KATE 在多种模型规模（如 Qwen3-8B 和 Qwen3-32B）和任务设置下均实现 SOTA 性能。
- **训练效率高**：直接使用 RL 而非先 SFT 再 RL 可获得更好收敛效果。

---

## 2. 核心实验方法和设置

### 使用的数据集
| 数据集 | 描述 |
|-------|------|
| **BFCL-V3** | 多轮交互式工具使用基准，涵盖 Base、Miss Func、Miss Param、Long Context 四种复杂场景。 |
| **AppWorld** | 面向编程代理的多步任务基准，采用基于状态的程序化评估方式，提供 Task Goal Completion (TGC) 和 Scenario Goal Completion (SGC) 指标。 |

### 实验设置与评估指标
- **模型**：Qwen3-8B、Qwen3-32B；部分实验也测试了 Llama3.2-3B-Instruct。
- **评估指标**：
  - BFCL-V3：各子任务准确率及平均得分。
  - AppWorld：TGC 和 SGC。
- **知识检索机制**：
  - 使用 `all-MiniLM-L6-v2` 编码器进行向量检索。
  - 设置相似度阈值 `p=0.5`，保留 Top-K 结果。
- **推理配置**：
  - 温度：inference 为 0，parallel sampling 为 1。
  - 并行采样数（sampling size）设为 4。
- **训练细节**：
  - 采用 LoRA 进行参数高效微调。
  - SFT 学习率 3e-5，训练 3 轮。
  - RL 使用 GRPO 方法，学习率相同，共 7 轮。

### 基线方法对比
| 基线方法 | 简介 |
|--------|------|
| **FC (Function Calling)** | 默认工具调用格式，无额外增强。 |
| **Prompt** | 使用 BFCL-V3 自带提示模板。 |
| **Memp** | 基于过程记忆的通用框架，支持技能复用。 |
| **ReAct** | 经典的推理+行动范式，在 AppWorld 中作为主要基线。 |

---

## 3. 主要实验结果和性能指标

### 关键性能数据（来自 Table 1 & Table 2）

#### 在 BFCL-V3 上的表现（Qwen3-8B）
| Method | Base | Miss F. | Miss P. | Long C. | **Average** |
|--------|------|--------|--------|---------|------------|
| FC | 43.0 | 30.0 | 31.0 | 27.0 | 32.75 |
| Prompt | 38.0 | 38.0 | 28.0 | 17.0 | 30.25 |
| Memp | 52.0 | 25.0 | 36.0 | 31.0 | 36.00 |
| **KATE (Ours)** | **59.0** (+16.0) | **41.0** (+11.0) | **41.0** (+10.0) | **40.0** (+13.0) | **46.00** (+13.25) |

> ✅ KATE 相比 FC 提升 **+13.25** 分，相比 GPT-5（37.75）也有明显优势。

#### 在 AppWorld 上的表现（Qwen3-32B）
| Method | TGC (Test-N) | SGC (Test-N) | TGC (Test-C) | SGC (Test-C) | **Average** |
|--------|--------------|--------------|---------------|---------------|-------------|
| ReAct | 16.7 | 1.8 | 6.2 | 1.4 | 6.52 |
| ReAct + ST | 27.4 | 1.8 | 8.6 | 0.0 | 9.45 |
| Memp | 22.6 | 5.4 | 9.1 | 1.4 | 9.62 |
| **KATE (Ours)** | **32.7** | **10.7** | **7.4** | **0.7** | **12.87** |

> ✅ KATE 在多数指标上领先，尤其在 Test-N 上表现突出。

### 与基线方法的对比结果
- KATE 在 BFCL-V3 上全面超越 FC、Prompt 和 Memp。
- 即使是强大的 GPT-5 和 GPT-4.1，在特定任务上也被 KATE 超越。
- 在 AppWorld 上，KATE 显著优于 ReAct 和 ReAct+ST，但在极端复杂的 Test-C 场景下略逊于 Memp —— 因为当任务超出模型推理能力时，parallel sampling 可能引入噪声。

### 消融实验结果（Ablation Study）
| 消融变体 | 描述 | 性能影响 |
|----------|------|----------|
| **→ w/o PS**（无 parallel sampling） | 移除并行采样 | 性能下降明显，说明**知识激活机制至关重要**。 |
| **→ w/o Exp**（无经验知识） | 仅有 parallel sampling | 性能有限，表明**任务特定知识不可替代**。 |
| **→ PS-Con.**（替换为 self-consistency） | 使用多数投票聚合 | 在 Qwen3-32B 上表现稳健，甚至优于 LLM-based aggregation。 |

> 🔍 发现：self-consistency 更稳定，适合结构化输出；LLM-based aggregation 更灵活但易受上下文长度干扰。

---

## 4. 关键结论和发现

### 主要发现
1. **Instance-level 知识最有效**：简单的执行轨迹（ST）就能带来最大性能提升，远胜于抽象的 intent-level 知识。
2. **推理宽度 > 推理深度**：增加 reasoning width（parallel sampling）比加深 reasoning depth（prompt hinting）更能有效激活模型内部潜藏的知识。
3. **知识内化进一步提效**：post-training 特别是 RL，能将外部知识更好地“固化”进模型参数中，带来额外增益。
4. **组合不等于更好**：盲目堆叠多种知识类型可能导致冗余或冲突，**选择性集成与激活机制更重要**。

### 方法的局限性
- **知识库规模受限**：实验仅在小规模知识库上验证，大规模知识检索的影响尚未探索。
- **文本模态限制**：目前仅适用于纯文本工具调用，未扩展到 multimodal 场景（如图像、语音接口）。
- **极端复杂任务挑战**：对于严重超出模型能力的任务（如 AppWorld Test-C），parallel sampling 可能失效，需更强训练或更高质知识支持。

### 未来工作方向
- 扩展至 **multimodal tool use** 场景。
- 构建更大规模、动态更新的 **procedural memory bank**。
- 探索更智能的 **adaptive knowledge routing** 机制，自动判断何时使用何种知识。
- 结合 **memory replay** 或 **lifelong learning** 框架，实现持续的知识积累与演化。

---

> 📌 **总结一句话**：  
> KATE 证明了——**高质量的实例经验 + 宽度优先的推理激活 + 强化学习驱动的内化训练**，是突破 LLM 工具调用极限的关键路径。

</details>

---

### 15. [A Systematic Approach for Selecting Trajectories for Data Augmentation](https://arxiv.org/abs/2606.10938)

**Authors**: Adam Nordling  
**Category**: cs.LG  
**Published**: 2026-06-10  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2606.10938v1  

#### Abstract
Trajectory data augmentation is a promising approach to mitigate data scarcity in machine learning applications, but its utility has been limited by the complexity of preserving spatio-temporal coherence. Although prior work demonstrated the viability of geometric perturbation, it relied on naive ra...

---

### 16. [ActiveMem: Distributed Active Memory for Long-Horizon LLM Reasoning](https://arxiv.org/abs/2606.10532)

**Authors**: Yunhan Jiang, Wenbin Duan, Shasha Guo, Liang Pang, Xiaoqian Sun, Huawei Shen  
**Category**: cs.AI  
**Published**: 2026-06-10  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2606.10532v1  

#### Abstract
Memory is essential for enabling large language model (LLM) agents to handle long-horizon reasoning tasks. Existing memory mechanisms are largely centralized, typically organizing retrieved information and interaction history within a single model context. This design imposes a fundamental trade-off...

---

### 17. [Early-Token Confidence Predicts Reasoning Quality in Multi-Agent LLM Debate](https://arxiv.org/abs/2606.10307)

**Authors**: Ali Keramati, Justin Cheok, Jacob Horne, Mark Warschauer  
**Category**: cs.CL  
**Published**: 2026-06-10  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2606.10307v1  

#### Abstract
Evaluating reasoning quality in multi-agent LLM systems is challenging, especially for open-ended tasks without reference answers. We investigate whether intrinsic confidence signals, token-level log-probabilities from decoding, can predict reasoning quality as assessed by LLM-as-judge evaluation. U...

---

### 18. [Small Data, Big Noise: Adversarial Training for Robust Parameter-Efficient Fine-Tuning](https://arxiv.org/abs/2606.10610)

**Authors**: Eitan Cohen, Idan Simai, Uri Shaham  
**Category**: cs.CL  
**Published**: 2026-06-10  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2606.10610v1  

#### Abstract
Parameter-Efficient Fine-Tuning (PEFT) has become essential for adapting foundation models to downstream NLP tasks. However, current PEFT methods often struggle with robustness to noise and performance degradation on limited training data. We propose SDBN (Small Data Big Noise), a unified framework ...

---

### 19. [Operator Fusion for LLM Inference on the Tensix Architecture](https://arxiv.org/abs/2606.09879)

**Authors**: Qingbo Wu, Ke Li, Wenzhu Wang, Jie Yu, Ruian Zhang, Lili Liu  
**Category**: cs.LG  
**Published**: 2026-06-10  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2606.09879v1  

#### Abstract
This study addresses on-device inference bottlenecks of Transformer models on Tenstorrent's Tensix architecture and proposes an operator fusion strategy that enhances data locality. RMSNorm is fused with matrix multiplication in self-attention and in the FFN, enabling back-to-back execution of memor...

---

### 20. [MODIP: Efficient Model-Based Optimization for Diffusion Policies](https://arxiv.org/abs/2606.10825)

**Authors**: Zakariae El Asri, Philippe Gratias-Quiquandon, Nicolas Thome, Olivier Sigaud  
**Category**: cs.LG  
**Published**: 2026-06-10  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2606.10825v1  

#### Abstract
Diffusion policies (DPs) have emerged as expressive policy representations for robot learning, often used with imitation learning methods such as behavioral cloning (BC). However, while their success has largely been confined to BC, direct reinforcement learning (RL) fine-tuning remains challenging ...

---

### 21. [READER: Robust Evidence-based Authorship Decoding via Extracted Representations](https://arxiv.org/abs/2606.10794)

**Authors**: Jiaxu Liu, Sunnan Mu, Dong Huang, Liuyin Wang, Jing Shao, Jie Zhang  
**Category**: cs.AI  
**Published**: 2026-06-10  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2606.10794v1  

#### Abstract
As agentic applications increasingly route user tasks through official and third-party LLM APIs, provenance becomes an operational question: which model generated a given black-box response? We study Dynamic Black-Box LLM Provenance: identifying the source LLM from generations elicited by query-vary...

---

### 22. [REAL: A Reasoning-Enhanced Graph Framework for Long-Term Memory Management of LLMs](https://arxiv.org/abs/2606.10694)

**Authors**: Keer Lu, Liwei Chen, Guoqing Jiang, Zhiheng Qin, Yunhuai Liu, Wentao Zhang  
**Category**: cs.CL  
**Published**: 2026-06-10  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2606.10694v1  

#### Abstract
Large Language Models (LLMs) are increasingly expected to interact with users over long time horizons. However, due to their finite context window, LLMs cannot retain all past interactions, making long-term memory management essential for storing, updating, and retrieving historical information beyo...

---

### 23. [Mobility Anomaly Generation using LLM-Driven Behavior with Kinematic Constraints](https://arxiv.org/abs/2606.10314)

**Authors**: Yueyang Liu, Joon-Seok Kim, Andreas Z\"ufle  
**Category**: cs.AI  
**Published**: 2026-06-10  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2606.10314v1  

#### Abstract
Although the study of human trajectory anomalies is critical for advancing spatial data mining, empirical research remains severely hindered by a pervasive lack of ground-truth datasets. Despite the availability of several real-world and simulated human trajectory collections, these datasets exclusi...

---

### 24. [The Order Matters: Sequential Fine-Tuning of LLaMA for Coherent Automated Essay Scoring](https://arxiv.org/abs/2606.10327)

**Authors**: Ali Keramati, Mark Warschauer  
**Category**: cs.CL  
**Published**: 2026-06-10  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2606.10327v1  

#### Abstract
Automated Essay Scoring (AES) systems must judge interdependent discourse elements (e.g., lead, claim, evidence, conclusion), yet most approaches treat these in isolation, harming coherence and generalization. We investigate task-aware fine-tuning of LLaMA-3.1-8B for AES using parameter-efficient Lo...

---

### 25. [TENP: Trapezoidal Expert Neuron Pruning For Mixture-of-Experts](https://arxiv.org/abs/2606.09885)

**Authors**: Jiangyang He, Shaolin Zhu, Deyi Xiong  
**Category**: cs.LG  
**Published**: 2026-06-10  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2606.09885v1  

#### Abstract
Mixture-of-Experts large language models (LLMs) scale efficiently through sparse activation, yet their deployment is fundamentally constrained by the large static parameter footprint of experts. Existing compression approaches either remove entire experts, disrupting routing topology and harming per...

---

### 26. [Integrating Out, Twice:The Open-System Case That Neural-Network Ensemble Theory Is Missing](https://arxiv.org/abs/2606.09950)

**Authors**: Jin Lei  
**Category**: cs.LG  
**Published**: 2026-06-10  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2606.09950v1  

#### Abstract
Averaging a neural network over its random parameters and marginalizing a Gaussian sector are the same operation, the Schur complement of the eliminated block, and when that block is closed it returns a covariance and its inverse. That is all a network ensemble produces, the closed case. The open ca...

---

### 27. [DUET -- Dual User Embedding Transformers for Offsite Conversion Prediction](https://arxiv.org/abs/2606.10243)

**Authors**: Reazul Hasan Russel, Mingwei Tang, Rostam Shirani, Xinlong Liu, Navid Madani, Leo Ding, Yawen He, Xiangyu Wang, Mustafa Acar, Ashish Katiyar, Yuhai Li, Alan Yang, Metarya Ruparel, Derek Qiang Xu, Rupert Wu, Rui Yang, Liang Tao, Xinyi Zhao, Larry Zhang, Sri Reddy, Rob Malkin  
**Category**: cs.LG  
**Published**: 2026-06-10  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2606.10243v1  

#### Abstract
Offsite conversion rate (OCVR) prediction is an important ranking problem in computational recommendation systems. This task presents a modeling challenge: click signals are abundant and exhibit short temporal horizons, whereas conversion signals are inherently sparse, long-delayed, and frequently u...

---

### 28. [Flash-GMM: A Memory-Efficient Kernel for Scalable Soft Clustering](https://arxiv.org/abs/2606.10896)

**Authors**: Gal Bloch, Ariel Gera, Matan Orbach, Ohad Eytan, Assaf Toledo  
**Category**: cs.LG  
**Published**: 2026-06-10  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2606.10896v1  

#### Abstract
We present \textbf{Flash-GMM}, a fused Triton kernel for efficient computation of Gaussian Mixture Models (GMMs) over large-scale data in a single GPU pass. By eliminating the need to materialize the full responsibility matrix in GPU memory, Flash-GMM achieves a \textbf{20$\times$} speedup over exis...

---

### 29. [COGENT: Continuous Graph Emulators with Neural Ordinary Differential Equations for Long-Term Physical Forecasting](https://arxiv.org/abs/2606.11162)

**Authors**: Zesheng Liu, Maryam Rahnemoonfar  
**Category**: cs.LG  
**Published**: 2026-06-10  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2606.11162v1  

#### Abstract
In this work, we present COGENT, a continuous graph emulator with Neural Ordinary Differential Equations for long-term physical forecasting on irregular geospatial meshes. COGENT encodes a finite history of system states and associated forcing fields and external forcings with a graph-based history ...

---

### 30. [Beyond Static Evaluation: Co-Evolutionary Mechanisms for LLM-Driven Strategy Evolution in Adversarial Games](https://arxiv.org/abs/2606.10389)

**Authors**: Haoran Li, Zengle Ge, Ziyang Zhang, Xiaomin Yuan, Yui Lo, Qianhui Liu, Bocheng An, Dongke Rong, Jiaqun Liu, Annan Li, Jianmin Wu, Dawei Yin, Dou Shen  
**Category**: cs.AI  
**Published**: 2026-06-10  
**Score**: 6.5  
**Type**: new  
**ArXiv ID**: 2606.10389v1  

#### Abstract
Recent advances in LLM-driven code evolution have enabled automated discovery by iteratively generating and improving programs. However, applying these methods to adversarial multi-agent games introduces a fundamental challenge: the evaluation landscape shifts as strategies improve, causing fixed ev...

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
