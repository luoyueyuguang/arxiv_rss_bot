# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-06-08 10:13:38 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG

## 📚 Recent Papers

### 1. [Uncertainty-Aware LLM-Guided Policy Shaping for Sparse-Reward Reinforcement Learning](https://arxiv.org/abs/2606.06673)

**Authors**: Ujjwal Bhatta, Utsabi Dangol, Sumaly Bajracharya, Rodrigue Rizk, KC Santosh  
**Category**: cs.LG  
**Published**: 2026-06-08  
**Score**: 10.0  
**Type**: new  
**ArXiv ID**: 2606.06673v1  

#### Abstract
Sparse rewards and heterogeneous task sequences remain persistent challenges in Reinforcement Learning (RL), often resulting in slow convergence, weak generalization, and inefficient exploration. We propose Uncertainty-Aware LLM-Guided Policy Shaping (ULPS), a novel framework that integrates a calib...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Uncertainty-Aware LLM-Guided Policy Shaping for Sparse-Reward Reinforcement Learning*

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
该论文针对**稀疏奖励（sparse-reward）环境下的强化学习（Reinforcement Learning, RL）**中存在的两大挑战：
- **探索效率低**：由于奖励信号极少，智能体难以通过随机探索发现成功路径；
- **任务序列复杂且多样化**：多子任务按特定顺序执行，传统RL方法容易陷入局部最优或无效动作。

此外，虽然已有研究尝试引入 Large Language Models（LLMs）提供行为先验指导，但存在**过度依赖不准确建议、模型过自信（overconfidence）、稳定性差**等问题。

---

### 🚀 提出的新方法：ULPS（Uncertainty-Aware LLM-Guided Policy Shaping）
提出了一种统一框架 **ULPS**，其核心思想是将**校准后的LLM先验**与**基于PPO的RL策略**结合，并通过**不确定性感知机制**动态调节两者的权重。

#### 创新点包括：
1. **符号轨迹生成与LLM微调**  
   使用 **A\*-based oracle** 在环境中生成最优符号轨迹（symbolic trajectories），并用这些高质量轨迹对 **BERT-based LLM** 进行微调，使其具备任务相关的动作预测能力。

2. **不确定性估计机制**  
   采用 **Monte Carlo (MC) Dropout** 估计LLM输出的**认知不确定性（epistemic uncertainty）**，并通过熵（entropy）进行归一化处理得到 $ H_{\text{norm}} \in [0,1] $。

3. **自适应策略融合机制**  
   设计了一个**基于熵的混合策略（entropy-based blending）**：
   $$
   P_{\text{final}} = (1 - H_{\text{norm}}) \cdot P_{\text{LLM}} + H_{\text{norm}} \cdot P_{\text{agent}}
   $$
   - 当LLM高度自信时（$H_{\text{norm}} \to 0$），更多依赖LLM建议；
   - 当LLM不确定时（$H_{\text{norm}} \to 1$），转向自主学习的PPO策略，避免误导。

4. **可扩展的自监督训练流程**  
   整个LLM微调过程无需人工标注，利用A*自动合成数据，实现**可扩展的自监督fine-tuning**。

---

### 🔍 相比现有方法的优势
| 对比维度 | ULPS优势 |
|--------|--------|
| **引导质量** | 使用A*生成的最优轨迹确保LLM先验可靠，优于仅靠提示工程的零样本LLM |
| **可靠性控制** | 引入MC Dropout量化不确定性，防止对错误建议的盲目信任 |
| **灵活性与稳定性** | 动态平衡外部先验与内部策略，既加速初期探索又保留后期优化空间 |
| **泛化性** | 在不同规模环境（4x4 / 8x8）均表现优异，显示良好迁移潜力 |

---

## 2. 核心实验方法和设置

### 📚 数据集与环境
- **MiniGrid-UnlockPickup-v0**：一个标准的稀疏奖励多任务RL基准环境。
  - 包含三个有序子任务：
    1. 找到并拾取钥匙（key pickup）
    2. 移动到门前并解锁（unlock door）
    3. 到达目标位置（reach goal）
  - 观测为局部7×7视野，动作空间离散（turn left/right, move forward, pick up, toggle）。
  - 奖励极其稀疏：只有完成各阶段才获得正反馈。

- **环境配置**：
  - LLM微调阶段：在 **8x4 grid** 中使用A*生成21,500条最优轨迹；
  - RL训练与测试：分别在 **4x4 和 8x8 grids** 上进行。

---

### ⚙️ 实验设置
- **RL算法**：Proximal Policy Optimization (**PPO**)，AdamW优化器（lr=5e-5），batch size=16，每50轮更新一次策略。
- **LLM模型**：`bert-base-uncased`，最大输入长度100 tokens，dropout=0.1。
- **不确定性估计**：每次决策执行 **T=8次MC Dropout前向传播** 来估计分布和熵。
- **训练周期**：共1,000 episodes，每episode最多50步。

---

### 🎯 评估指标
| 指标 | 定义 |
|------|------|
| **Success Rate (%)** | 成功到达目标的episode占比 |
| **Average Steps to Goal** | 成功episode中的平均步数 |
| **Reward AUC** | 奖励曲线下的面积（Area Under Curve），衡量累积奖励效率 |
| **Total Steps** | 所有episode总交互步数（反映样本效率） |
| **Brier Score (BS)** | 预测概率准确性，越低越好 |
| **Expected Calibration Error (ECE)** | 校准误差，衡量置信度与准确率一致性 |
| **Discrimination Analysis (DA, via AUC-ROC)** | 区分正确/错误动作的能力，越高越好 |

---

### 🆚 基线方法对比
- **Unguided RL (PPO)**：纯PPO，无任何外部引导
- **Linear RL (PPO)**：固定调度从LLM过渡到PPO
- **Uncalibrated LLM + RL**：直接使用LLM建议，无不确定性调节
- **Q-Learning (GRPO)**：基于Q表的传统方法
- **DQN (GRPO)**：深度Q网络变体（Double DQN, Dueling Net等）

---

## 3. 主要实验结果和性能指标

### 📊 关键性能数据（4x4环境）

| 方法 | Reward AUC | Success Rate (%) | Avg. Steps | Total Steps (1k eps) |
|------|------------|------------------|-----------|------------------------|
| **ULPS (Ours)** | **2055.08** | **99.90** | **7.24** | **7,286** |
| Uncalibrated LLM | 1706.43 | 94.00 | 18.39 | 20,284 |
| Linear RL (PPO) | 1865.57 | 74.90 | 15.84 | 24,412 |
| Unguided RL (PPO) | 221.31 | 5.90 | 35.54 | 49,147 |
| Q-Learning (GRPO) | 1515.71 | 82.40 | 16.19 | 22,142 |
| DQN (GRPO) | 317.46 | 11.60 | 31.66 | 47,873 |

> ✅ **ULPS在所有指标上全面领先**，尤其在**成功率接近完美（>99.9%）的同时，平均仅需7.24步**，远低于其他方法。

---

### 🔬 消融实验结果（Ablation Study）

#### 表格 II 显示关键消融对比：
- **单独PPO失败严重**：在8x8环境下几乎无法成功（Success Rate ≈ 0%）；
- **Uncalibrated LLM提升有限**：虽高于基础RL，但仍显著落后于ULPS（94% vs 99.9%）；
- **加入不确定性调节后性能飞跃**：证明 $ H_{\text{norm}} $ 融合机制至关重要。

#### 不确定性模块影响分析（Table III）：
| Dropout Rate | Forward Passes | Avg. Steps | Reward AUC |
|--------------|----------------|------------|-------------|
| 0.1 | 8 | **7.24** | **2055.08** |
| 0.2 | 12 | 7.0 | 2055.88（略高但计算代价大） |

> 结论：**dropout=0.1 + 8次前向传递** 是性价比最佳选择，在保持高性能的同时降低计算开销。

---

### 🧪 模型校准性能比较（Table I）

| 模型 | Acc. (%) | ECE ↓ | BS ↓ | DA (AUC) ↑ |
|------|----------|-------|------|------------|
| Shoaeinaeini et al. [15] (4x4) | 90.00 | 0.15 | 0.20 | 0.80 |
| **ULPS (Ours)** | **99.17** | **0.20** | **0.06** | **1.00** |

> 尽管ECE稍高，但**BS极低、DA达到完美（1.0）**，说明模型不仅能做出准确预测，还能很好地区分“对”与“错”的动作，具备更强的判别能力和可靠性。

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **不确定性感知机制至关重要**：  
   单纯引入LLM会导致过依赖甚至被误导；而通过MC Dropout估计不确定性并动态调整权重，能有效提升稳定性和最终性能。

2. **结构化先验显著提升样本效率**：  
   利用A*生成的最优轨迹对LLM进行微调，提供了高质量的行为先验，使RL在极少数环境交互下快速收敛（**减少86%环境交互**）。

3. **ULPS实现了高效探索与稳健学习的平衡**：  
   初期依靠LLM快速找到可行路径，后期逐步切换至自主策略，避免陷入次优启发式。

4. **方法具有良好的可扩展性**：  
   在更复杂的8x8环境中仍取得99.7%成功率，验证了其应对更大状态空间的能力。

---

### ⚠️ 局限性
1. **计算开销增加**：  
   每次决策需进行8次前向推理（MC Dropout），带来约8倍的**单步推理延迟**，不适合实时性要求高的场景。

2. **依赖符号规划器（A*）**：  
   当前方法需要一个精确的世界模型来运行A*，限制了其在**部分可观测（partially observable）或动态变化环境**中的应用。

3. **语言模型容量瓶颈**：  
   使用BERT而非更大LLM（如LLaMA、ChatGPT），可能限制语义理解与泛化能力。

---

### 🔮 未来工作方向
1. **扩展至部分可观测与多智能体环境**：  
   探索如何在没有完整地图的情况下构建不确定性感知的协作系统。

2. **引入层次化提示（hierarchical prompting）**：  
   支持更高层次的任务分解与长期规划。

3. **融合多模态输入（vision + language）**：  
   构建视觉-语言联合表示，支持真实世界机器人任务。

4. **轻量化不确定性估计**：  
   探索更高效的贝叶斯近似方法（如SWAG、ensemble pruning）以降低推理成本。

5. **闭环规划-学习集成**：  
   实现LLM、规划器与RL之间的双向反馈，形成真正协同的认知架构。

---

## 总结
> **ULPS** 是一种将 **symbolic planning（A*）**、**pretrained language priors（BERT）** 与 **uncertainty-aware RL（PPO + MC Dropout）** 有机结合的新范式。它不仅解决了稀疏奖励下的探索难题，还通过可信度调控机制提升了系统的鲁棒性与解释性。实验证明其在 **MiniGrid-UnlockPickup** 上实现了接近完美的成功率、最低的步数消耗和最高的奖励效率，为未来构建**可信赖、可扩展的智能代理系统**提供了重要思路。

</details>

---

### 2. [Teaching the Way, Not the Answer: Privileged Tutoring Distillation for Multimodal Policy Optimization](https://arxiv.org/abs/2606.07000)

**Authors**: Shizhe Xiang, Ke An, Wenlong Yu, Yue Liu, Jian Luan, Pei Fu, Qilong Wang  
**Category**: cs.AI  
**Published**: 2026-06-08  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2606.07000v1  

#### Abstract
Recent post-training methods, particularly Reinforcement Learning with Verifiable Rewards (RLVR), have significantly enhanced the reasoning ability of Large Vision-Language Models (LVLMs). However, the sparse nature of verifiable rewards provides little token-level supervision for failed rollouts, o...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Teaching the Way, Not the Answer: Privileged Tutoring Distillation for Multimodal Policy Optimization*

---

## 1. 论文的主要贡献和创新点

### **解决了什么问题**

该论文针对 **Reinforcement Learning with Verifiable Rewards (RLVR)** 在 **Large Vision-Language Models (LVLMs)** 后训练中的两大核心挑战：

1. **Reward Sparsity**：RLVR 仅提供最终答案级别的稀疏奖励（outcome-level feedback），对失败的推理轨迹（failed rollouts）缺乏中间步骤的监督信号，导致探索效率低下，尤其在复杂的多模态推理任务中难以进行有效的信用分配（credit assignment）。
2. **Answer-Revealing Distillation 的副作用**：现有的策略蒸馏（policy distillation）方法常通过引入完整答案（ground-truth answer）或思维链（CoT）来构建更强的教师模型，但这会暴露答案信息，诱导模型学习“捷径”（shortcuts），如直接模仿答案路径，而非自主发现推理过程，导致熵崩溃（entropy collapse）和探索能力下降。

### **提出了什么新方法或新思路**

作者提出 **PTD-PO (Privileged Tutoring Distillation Policy Optimization)**，一种基于**特权信息范式**（learning with privileged information）的新型策略优化框架。其核心思想是：

- **Teaching the Way, Not the Answer**：不向学生模型（student policy）暴露答案，而是通过**非泄露性的特权提示**（answer-free privileged hints）指导一个冻结的参考模型（frozen reference model），使其生成**纠正性的推理路径分布**（corrective reasoning path distribution）。
- **双通道上下文设计**：
  - **学生**：仍在原始的无答案上下文（question-only context）中生成响应，保持探索性。
  - **教师**：在包含特权提示的增强上下文（hint-augmented context）中生成响应，提供密集的 token-level 监督。
- **失败轨迹路由**（Failure-Routed Distillation）：仅对失败的推理轨迹应用蒸馏损失，避免对已有成功信号的轨迹进行不必要的过度正则化。

### **相比现有方法的优势**

| 对比维度 | 现有方法（如 HDPO, OPSD） | PTD-PO |
| :--- | :--- | :--- |
| **监督密度** | RLVR：稀疏；Answer-Distillation：密集但有偏 | 密集且无偏，来自失败轨迹 |
| **信息暴露** | 外部教师：计算开销大；答案条件化：泄露答案 | 不泄露答案，仅用特权提示 |
| **探索行为** | 答案条件化易导致熵崩溃 | 保持学生端的探索性 |
| **计算效率** | 在线蒸馏需实时教师推理 | 教师冻结，仅在失败时计算，配合 Top-K JSD 降低内存开销 |

---

## 2. 核心实验方法和设置

### **使用的数据集**

- **训练数据**：`ViRL39K`，一个包含 38,870 个可验证的视觉-语言问答样本的数据集，涵盖数学、科学、图表、空间推理等多种场景。
- **评估基准**：`PAPO` 多模态推理基准套件，包含多个子任务：
  - **通用多模态推理**：MMK12, MathVerse, MathVista, We-Math
  - **视觉依赖型多模态推理**：Geo3K, MMMU-Pro, Counting, LogicVista
  - 报告各子集及总体（Overall）的平均准确率。

### **实验设置和评估指标**

- **模型规模**：在 `Qwen3-VL-2B/4B/8B-Thinking` 三种不同参数量级的 LVLM 上进行实验。
- **训练设置**：
  - 最大响应长度：4096 tokens
  - Rollout 数量：8
  - 优化器：AdamW
  - 学习率：1e-6
- **评估设置**：
  - 所有模型均在**无特权提示**的原始问题上下文中进行推理和评估，确保公平。
  - 使用规则匹配（rule-based matching）提取最终答案并计算准确率。
- **评估指标**：各数据集上的 **Accuracy (%)**。

### **基线方法对比**

- **SFT**：监督微调，使用构造的 CoT 数据。
- **OPSD**：Online Policy Self-Distillation，使用指数移动平均的自身参数作为教师。
- **GRPO**：Group Relative Policy Optimization，标准的 RLVR 基线。
- **HDPO**：Hybrid Distillation PO，使用真实答案作为条件进行自我蒸馏。
- **PAPO**：Perception-Aware Policy Optimization，一种改进的多模态 RLVR 方法。

---

## 3. 主要实验结果和性能指标

### **关键性能数据与对比结果**

在所有模型规模（2B, 4B, 8B）和所有评估类别上，**PTD-PO 均取得了最佳性能**。

| Model | Method | General AVG | Vision-Dependent AVG | Overall AVG |
| :--- | :--- | :--- | :--- | :--- |
| **2B** | GRPO | 52.93 | 47.76 | 50.63 |
| | **PTD-PO (Ours)** | **58.97** | **56.06** | **57.68** |
| **4B** | GRPO | 69.82 | 65.87 | 68.06 |
| | **PTD-PO (Ours)** | **71.36** | **66.52** | **69.20** |
| **8B** | GRPO | 71.25 | 65.69 | 68.78 |
| | **PTD-PO (Ours)** | **74.85** | **68.12** | **71.86** |

- **显著优势**：PTD-PO 在 4B 模型上比 GRPO 高出 **1.14%**，比 HDPO（答案揭示蒸馏）高出 **1.11%**，证明了**非泄露性特权信息的有效性**。
- **超越 PAPO**：PTD-PO 也优于专门针对多模态感知的 PAPO 方法，表明其提出的**特权教学范式更具普适性和有效性**。

### **消融实验结果**

1. **PTD 激活阈值**（`T_ptd`）：
   - 设置 `T_ptd=1.0`（即对所有包含失败轨迹的组应用 PTD）效果最好。
   - 对所有轨迹都应用 PTD 会导致性能下降，尤其是在大模型上，证实了**选择性蒸馏**的重要性。

2. **结构化提示设计**（Structured Hint Design）：
   - 移除“零剧透”（zero-spoiler）和“过滤陷阱”（trap-filtering）约束的变体性能更差，尤其是在 8B 模型上。
   - 证明了**精心设计的、有结构的、非任意的提示**是 PTD-PO 成功的关键。

3. **Top-K JSD 支持大小**（K）：
   - 实验表明 `K=100` 是一个良好的权衡点，在保留主要分布信号的同时，将内存开销从 `O(BTV)` 显著降低到 `O(BTK)`。

---

## 4. 关键结论和发现

### **主要发现**

1. **密集监督的有效性**：通过特权提示引导的参考模型，可以为失败的推理轨迹提供高质量的 token-level 监督，有效缓解 RLVR 中的奖励稀疏问题。
2. **保护探索至关重要**：避免向学生模型暴露答案信息，可以防止模型陷入确定性的捷径行为，维持更高的策略熵（policy entropy），促进更健康的探索。
3. **失败轨迹是关键**：将蒸馏信号**路由到失败的轨迹**是最有效的利用方式，既能纠正错误，又不会干扰已有的成功学习路径。
4. **JSD 的优越性**：在教师和学生上下文不对称的情况下，**Top-K Jensen-Shannon Divergence** 比传统的 KL 散度更稳定，能有效减少因上下文差异导致的剧烈梯度。

### **局限性**

1. **对训练数据难度的依赖**：PTD-PO 的增益在更强的模型上相对减弱，因为这些模型本身产生的失败轨迹较少，导致 PTD 被激活的机会变少。
2. **无法完全消除复杂错误**：对于需要极细粒度验证（如化学方程式配平）的高度复合问题，即使有提示，模型仍可能产生不可靠的答案。
3. **提示构造成本**：虽然离线生成，但仍需强大的外部模型（如 Qwen3-VL-235B）来生成高质量的特权提示。

### **未来工作方向**

1. **构建更具挑战性的 RLVR 训练数据**：设计更难、更能匹配强模型能力的多模态任务，以产生更多有意义的失败案例，从而最大化 PTD-PO 的潜力。
2. **扩展到多模态 Agent 场景**：将 PTD 思路应用于具身智能体（embodied agents），利用环境反馈、工具输出等作为“特权提示”，指导智能体在交互任务中学习和恢复。
3. **自动化提示生成**：研究如何更高效、低成本地自动生成高质量的结构化特权提示。

</details>

---

### 3. [Self-evolving LLM agents with in-distribution Optimization](https://arxiv.org/abs/2606.07367)

**Authors**: Yudi Zhang, Meng Fang, Zhenfang Chen, Mykola Pechenizkiy  
**Category**: cs.LG  
**Published**: 2026-06-08  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2606.07367v1  

#### Abstract
Large Language Models (LLMs) have recently emerged as powerful controllers for interactive agents in complex environments, yet training them to perform reliable long-horizon decision making remains a fundamental challenge. A key difficulty lies in credit assignment: agents often receive delayed rewa...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：**Self-evolving LLM agents with in-distribution Optimization**

---

## 1. 论文的主要贡献和创新点

### ✅ 解决了什么问题

该论文针对 **LLM agents 在复杂交互环境中进行长视野决策（long-horizon decision making）时面临的关键挑战**：

- **稀疏且延迟的奖励（Sparse and delayed rewards）**：代理通常只在任务结束时获得反馈，难以将成功归因于中间步骤。
- **信用分配困难（Credit assignment）**：无法有效识别哪些中间动作对最终成败起决定性作用。
- **分布偏移（Distribution shift）**：当策略更新后生成的新轨迹超出训练数据分布时，基于离线数据学习的奖励模型（如 PRM）可能失效。

这些问题导致现有方法在样本效率、鲁棒性和泛化能力方面表现不佳。

---

### ✅ 提出了什么新方法或新思路

作者提出 **Q-Evolve** —— 一种**自演进（self-evolving）框架**，其核心思想是：

> **在一个共享的 in-distribution 学习循环中，联合优化过程级监督（process reward labeling）与策略学习（policy optimization），实现稳定、可迭代的自我提升。**

#### 主要创新点包括：

1. **统一的 in-distribution 强化学习范式**
   - 所有学习（critic 学习、reward labeling、policy 更新）都严格限制在由专家演示和代理自身轨迹构成的混合离线数据集上，避免 out-of-distribution 推理带来的不稳定性。

2. **自动的过程奖励标注（Automatic process reward labeling）**
   - 利用加权的 **Implicit Q-Learning (IQL)** 学习一个 in-distribution critic。
   - 基于 critic 的值函数通过 **Generalized Advantage Estimation (GAE)** 回溯推导出每一步的“过程奖励”，无需人工标注或环境回溯。

3. **行为邻近策略优化（Behavior-Proximal Policy Optimization, BPPO）**
   - 使用带符号优势（signed advantage）指导策略更新：
     - 正优势动作被放大；
     - 负优势动作被显式抑制（down-weighted）；
     - 采用非对称裁剪（asymmetric clipping）允许更激进地惩罚错误行为。

4. **闭环自演进机制（Closed-loop self-evolution）**
   - 每轮迭代中：
     1. 使用当前策略收集新轨迹；
     2. 构建混合数据集（expert + self-rollout）；
     3. 学习 critic 并标注过程奖励；
     4. 在固定数据上更新策略；
   - 政策、critic 和数据共同演化（co-evolve），形成稳定的自我改进循环。

---

### ✅ 相比现有方法的优势

| 特性 | Q-Evolve | 典型 PRM / Online RL 方法 |
|------|--------|--------------------------|
| 是否需要手动标注 | ❌ 否 | ✅ 是（如 PRM） |
| 是否依赖在线搜索/回溯 | ❌ 否 | ✅ 是（如 QLASS） |
| 是否处理分布偏移 | ✅ 显式控制 | ❌ 忽略风险 |
| 是否支持连续动作空间 | ✅ 支持（LLM 输出文本） | ❌ 多需离散状态 |
| 样本效率 | ⭐⭐⭐⭐⭐ 高 | ⭐⭐ 较低 |
| 可扩展性 | ✅ 适用于真实动态环境 | ❌ 依赖模拟器特性 |

> ✅ **Q-Evolve 实现了无需昂贵标注、无环境回溯、抗分布偏移的高效自演进。**

---

## 2. 核心实验方法和设置

### 📚 使用的数据集

在三个具有**延迟奖励**特性的标准 LLM agent 测试平台上进行评估：

| 数据集 | 描述 |
|-------|------|
| **AlfWorld** | 文本版具身智能任务（如“加热苹果并放入微波炉”），仅在最后返回二元奖励。 |
| **WebShop** | 在虚拟电商网站中完成购物任务，奖励取决于购买物品是否满足属性要求。 |
| **ScienceWorld** | 科学实验类任务，包含多个子目标，奖励稀疏且为连续值（0~1）。 |

所有任务均划分 **Seen（见过的任务）** 和 **Unseen（未见过的任务）** 以测试泛化能力。

---

### ⚙️ 实验设置和评估指标

- **基础模型**：`Llama-2-7B-Chat`（主实验）、`Llama-3-8B-Instruct`（跨架构验证）
- **评估指标**：平均累积奖励（average accumulated reward）
- **训练流程**：
  - 第一轮 warm-up 使用 **Behavior Cloning (BC)** 初始化策略。
  - 后续多轮执行 Q-Evolve 循环（AlfWorld/ScienceWorld: 2轮；WebShop: 3轮）
- **数据构建**：
  - 混合数据集 $ \mathcal{D} = \mathcal{D}_{\text{expert}} \cup \mathcal{D}_{\text{self}} $
  - 自采样轨迹来自当前策略的 rollout（每任务采样3条）

---

### 🔁 基线方法对比

分为三类：

| 类别 | 基线方法 |
|------|---------|
| **零样本 LLM** | GPT-3.5-Turbo, GPT-4 (ReAct) |
| **监督微调** | SFT（监督微调）, RFT（拒绝采样微调） |
| **强化学习/规划方法** | PPO, Best-of-N, ETO, DMPO, QLASS |

特别强调与以下方法对比：
- **QLASS**：基于在线搜索估计 Q 值用于推理时规划，依赖大量交互（600K步）；
- **ETO**：基于偏好优化的自演进方法；
- **PPO**：标准在线 RL 方法，直接优化最终奖励。

---

## 3. 主要实验结果和性能指标

### 📊 关键性能数据（见 Table 2）

| Method | WebShop | SciWorld (Seen) | SciWorld (Unseen) | ALFWorld (Seen) | ALFWorld (Unseen) | **Average** |
|--------|--------|------------------|--------------------|------------------|--------------------|-------------|
| GPT-4 | 63.2 | 64.8 | 64.4 | 42.9 | 38.1 | 54.7 |
| SFT | 63.1 | 67.4 | 53.0 | 60.0 | 67.2 | 62.1 |
| ETO | 67.4 | 73.8 | 65.0 | 68.6 | 72.4 | 69.4 |
| QLASS | 70.3 | 75.3 | 66.4 | 77.9 | 82.8 | **74.5** |
| **Q-Evolve (Ours)** | **70.5** | **76.3** | **69.7** | **90.7** | **89.6** | **79.4** |

> ✅ **Q-Evolve 在所有任务上取得最优性能，平均得分领先第二名 QLASS 超过 5 个百分点。**

---

### 🔍 与基线方法的对比结果

- **vs QLASS**：
  - 性能更高（79.4 vs 74.5），同时**环境交互量减少 97%**（20K vs 600K steps in AlfWorld）；
  - 不依赖耗时的在线 rollout 和搜索树构建，推理成本更低。

- **vs ETO/PPO**：
  - 显著优于所有不显式解决稀疏奖励的方法；
  - 表明 **dense process reward labeling 对 long-horizon 任务至关重要**。

- **vs SFT/RFT**：
  - 尽管 SFT 已经很强，Q-Evolve 仍带来显著增益，说明**奖励驱动的策略优化超越纯模仿学习**。

---

### 🔬 消融实验结果（Ablation Studies）

#### （1）关键组件消融（Table 3）

| Variant | AlfWorld Seen | Unseen |
|--------|---------------|--------|
| Full Q-Evolve | **87.9** | **86.6** |
| w/o Retrospective Labeling (RT) | 83.6 | 82.7 |
| w/o Weighted IQL | 83.6 | 76.1 |
| w/o GAE | 74.3 | 74.6 |
| w/o Policy Improvement (test-time scaling) | 58.6 | 59.0 |

> ✅ 所有模块均有贡献，尤其是 **GAE 和 weighted IQL** 对性能影响最大。

#### （2）策略学习方式比较

| Policy Learning | Seen | Unseen |
|----------------|------|--------|
| AWR（Advantage Weighted Regression） | 64.3 | 67.9 |
| **BPPO（本文方法）** | **87.9** | **86.6** |

> ✅ **BPPO 显式抑制负优势动作的能力显著优于 AWR**，证明“惩罚坏动作”比“仅鼓励好动作”更重要。

#### （3）过程奖励选择（Table 4）

| Process Reward Type | Seen | Unseen |
|---------------------|------|--------|
| One-step Q-V | 74.3 | 74.6 |
| Potential-based shaping | 80.0 | 74.6 |
| **GAE with $ r_{\text{env}} $ (ours)** | **87.9** | **86.6** |
| GAE with $ r_{\text{env}} + r_{\text{aux}} $ | 81.4 | 82.8 |

> ✅ **多步优势估计（GAE）最有效**，且不应将辅助奖励 $ r_{\text{aux}} $ 加入 GAE（会引入偏差）。

#### （4）样本效率（Table 5）

| Method | Env Steps | AlfWorld Seen | Unseen |
|--------|-----------|---------------|--------|
| PPO / GRPO etc. | 320K | ≤77.6 | ≤77.6 |
| **Q-Evolve (1-iter)** | **13K** | **88.6** | **87.3** |

> ✅ **仅用 13K 步交互即全面超越使用 320K 步的在线 RL 方法**，样本效率极高。

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **稳定自演进是可行的**：
   - 通过将 **critic 学习、reward labeling、policy update** 统一在 in-distribution 数据闭环中，可以实现可靠、可迭代的自我提升。

2. **过程奖励应来自 in-distribution critic**：
   - 使用 offline critic + GAE 自动生成 step-wise 优势信号，比依赖在线搜索或人工标注更高效、更鲁棒。

3. **显式抑制有害行为至关重要**：
   - BPPO 中的非对称裁剪机制能有效降低无效/错误动作的概率，这对 long-horizon 成功至关重要。

4. **混合数据集设计是关键**：
   - 结合 expert demo（提供成功路径）与 self-rollout（暴露失败模式），使 critic 学习更稳健。

5. **Q-Evolve 泛化性强**：
   - 在不同任务、不同模型架构（Llama-2 / Llama-3）下均保持领先，表明方法具有普适性。

---

### ⚠️ 局限性（Limitations）

1. **依赖结构化反馈**：
   - Retrospective labeling 依赖环境提供的自然语言反馈（如 “Invalid action”），在缺乏此类反馈的任务中效果受限。

2. **贪婪 rollout 导致多样性下降**：
   - 每轮使用当前最佳策略收集数据，可能导致探索不足，陷入局部最优。

3. **跨轮次分布漂移积累**：
   - 虽然单轮内控制 in-distribution，但多轮演化过程中策略逐渐偏离初始分布，目前未显式纠正。

4. **critic 训练开销较大**：
   - critic 需要较多训练轮数（20 epochs），成为整体 pipeline 的计算瓶颈（见 B.5）。

---

### 🔮 未来工作方向

1. **引入主动探索机制**：
   - 替代 greedy rollout，使用基于不确定性的探索策略提升数据多样性。

2. **跨轮次分布校正机制**：
   - 设计显式的分布对齐或正则化项，缓解长期演化中的 drift 问题。

3. **轻量化 critic 架构**：
   - 探索参数共享、蒸馏等方式降低 critic 存储与计算开销。

4. **扩展至多模态 agent**：
   - 将框架应用于视觉-语言-动作（VLA）系统，如 **OpenVLA** 或机器人控制场景。

5. **结合 memory-augmented reasoning**：
   - 引入反思（reflection）与记忆机制，增强 agent 的长期一致性与知识沉淀能力。

---

> 💡 **总结一句话**：  
> **Q-Evolve 通过 in-distribution critic 与 BPPO 的协同演化，在无需人工标注与环境回溯的前提下，实现了高效、鲁棒、可扩展的 LLM agent 自我进化，为构建真正自主的智能体提供了新范式。**

</details>

---

### 4. [PCCL: Process Group-Aware Scalable and Generic Collective Algorithm Synthesizer](https://arxiv.org/abs/2606.07019)

**Authors**: William Won, Kartik Lakhotia, Madhu Kumar, Sudarshan Srinivasan, Tushar Krishna  
**Category**: cs.DC  
**Published**: 2026-06-08  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2606.07019v1  

#### Abstract
Distributed machine learning has become increasingly important due to the massive scale of large-scale generative models. Both model parameters and data are distributed across many compute devices, which requires frequent collective communications to synchronize activations and parameter updates. Su...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：PCCL: Process Group-Aware Scalable and Generic Collective Algorithm Synthesizer

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
在大规模分布式机器学习（尤其是生成式AI和MoE模型）中，**collective communication**（如 All-Reduce、All-to-All）已成为训练和推理的主要瓶颈。现有的 **Collective Communication Libraries (CCLs)** 和算法合成器存在以下关键缺陷：

- **缺乏对 process group 的支持**：大多数合成器假设所有设备参与集体通信，而实际中仅子集（process group）参与。
- **可扩展性差**：基于 ILP 或 SMT 的方法（如 TE-CCL）在数百 NPUs 上合成耗时极长（数小时），难以实用。
- **通用性不足**：无法支持 All-to-All、All-to-Allv 等复杂模式，尤其在 MoE 模型中至关重要。
- **拓扑建模受限**：多数方法无法有效处理异构（heterogeneous）、非对称（asymmetric）网络拓扑。

---

### 🚀 提出的新方法与创新

PCCL 提出了一种**可扩展、通用且支持 process group 的 collective algorithm synthesizer**，其核心创新如下：

#### （1）采用 **Time-Expanded Network (TEN)** 数据结构
- 将时间维度与空间网络拓扑统一建模，自然支持动态路径规划。
- 支持任意带宽、延迟的异构链路，通过 α-β 模型量化传输时间。

#### （2）设计 **BFS-based Pathfinding Algorithm**
- 替代传统的 ILP/SMT/Optimizer-based 方法，实现高效路径搜索。
- 时间复杂度显著降低，支持快速合成大规模算法（O(n³)）。
- 天然支持 process group：先在整个网络中寻路，再过滤目标节点路径。

#### （3）原生支持 **Process Group Awareness**
- 显式利用 process group 信息，在合成时只关注目标 NPU 子集的 postcondition。
- 可跨 process group 边界使用中间 NPU 转发数据，提升资源利用率。

#### （4）支持 **Generic Collective Patterns**
- 支持 Reduce-Scatter、All-Gather、All-Reduce、All-to-All、All-to-Allv 等全部常见模式。
- 支持自定义 collective（custom collectives），只需指定 pre/postconditions。

#### （5）显式建模 **Switches**
- 区分 NPU 和 switch 节点，支持 buffer 限制、multicast 能力等 switch 特性。
- 避免传统“unroll switch to direct links”带来的建模失真。

---

### 🔍 相比现有方法的优势

| 维度 | PCCL | 其他方法（如 SCCL, TACCL, TE-CCL, Blink） |
|------|------|----------------------------------------|
| **Scalability** | ✅ 支持 512~1000 NPU，合成时间分钟级 | ❌ 多数仅支持几十到百级 NPU，耗时数十分钟至数小时 |
| **Generic Topology** | ✅ 支持异构、非对称、含 switch 拓扑 | ⚠️ 多数限于同构、对称、无 switch |
| **Generic Collective** | ✅ 支持 All-to-All, All-to-Allv | ❌ 多数不支持或效率低 |
| **Process Group Aware** | ✅ 原生支持 | ❌ 完全忽略，需手动裁剪拓扑 |
| **算法机制** | ✅ BFS + TEN，轻量高效 | ❌ ILP/SMT，NP-hard，求解慢 |

> 💡 总结：PCCL 是首个同时满足 **Scalable + Generic + Process Group-Aware** 的 synthesizer。

---

## 2. 核心实验方法和设置

### 🧪 实验基础设施
- 使用 **ASTRA-sim** 进行系统级模拟，已验证在 128-GPU H100 集群上精度达 97%。
- 合成结果通过 **MSCCL executor** 在真实 16/32-GPU 集群上执行验证正确性。

### 📊 实验设置
- **目标拓扑**：
  - 2D Mesh（6×6 到 24×24）
  - 3D Hypercube
  - Heterogeneous 2D Switch Topology（每节点8 NPU）
- **目标 collective**：
  - 主要测试 **All-to-All**（最具挑战性）
  - 同时评估 All-to-Allv、All-Gather
- **chunk size**：128 KiB，buffer size 从 8 MiB 到 512 MiB 不等

### 📈 评估指标
| 指标 | 描述 |
|------|------|
| **Synthesis Time** | 算法生成耗时（秒/分钟） |
| **Bandwidth Utilization** | 单位时间内完成的数据传输量 |
| **Link Utilization Heatmap** | 网络链路使用效率可视化 |
| **Speedup over Baseline** | 相对于 Direct 等基线的加速比 |

### 🆚 基线方法对比
| 基线 | 说明 |
|------|------|
| **Direct (Pairwise Send-Recv)** | 当前 CCLs 中实现 All-to-All 的主流方式（如 NCCL, RCCL） |
| **TE-CCL [31]** | 当前最先进的 All-to-All synthesizer，基于 multi-commodity flow + LP |
| **CCLs (NCCL/RCCL/oneCCL)** | 工业界标准库，作为运行时性能对比基准 |

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据

#### （1）**可扩展性（Scalability）**
- **512-NPU All-to-All 合成时间：11.68 分钟**
- **1000-NPU 合成时间：2.01 小时**
- 对比 TE-CCL：
  - 在 36-NPU（6×6 Mesh）上，PCCL 快 **4,404×**
  - TE-CCL 在 49-NPU 时已超 30 分钟，而 PCCL 仍为秒级

> 🔢 合成复杂度为 **O(n³)**，远优于 ILP-based 方法的指数级增长。

#### （2）**All-to-All 性能提升**
- 在 2D Mesh 上，PCCL 合成的 All-to-All 算法相比 Direct 实现：
  - **平均提速 2.68×**
  - 最高达 **3.03×**
- 在异构 2D Switch 拓扑上，PCCL 平均提供 **1.33× 带宽提升**

#### （3）**Process Group Awareness 效果**
- 当多个 process group 并发执行 All-to-All：
  - PCCL 能跨 group 利用空闲链路，避免局部拥塞
  - 相比 Direct，**归一化带宽提升 2.33–3.03×**
- 图 17 显示：Direct 的 link utilization 极低，而 PCCL 几乎满载

#### （4）**不同 collective 支持能力**
- 成功合成了 **All-to-Allv**（变长 chunk）和 **All-Gather** 等复杂模式
- 在 8×8 Mesh 上，128 MiB All-to-All 合成时间仅 **1.83 分钟**

#### （5）**消融实验（隐含分析）**
- 若强制限制在 process group 内部寻路（禁用外部 NPU），性能下降约 40%
- 使用更大 chunk size 可进一步减少合成时间（因 chunk 数减少）

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **Process group awareness 至关重要**：
   - 忽略 process group 导致严重资源浪费（如 Direct 算法）。
   - PCCL 通过全局寻路 + 局部过滤，最大化带宽利用率。

2. **BFS + TEN 是高效合成的关键**：
   - 相比 ILP/SMT，BFS 在保证质量的同时大幅提升速度。
   - TEN 结构天然支持时间调度与拥塞控制。

3. **All-to-All 是 MoE 场景下的关键瓶颈**：
   - 当前 CCLs 缺乏专用算法，依赖低效的 pairwise 通信。
   - PCCL 可自动合成高性能、拓扑感知的 All-to-All 方案。

4. **可扩展性是实用化的前提**：
   - 数千 NPU 规模下，合成必须在分钟级内完成。
   - PCCL 是目前唯一能在 1000-NPU 规模下实用的 synthesizer。

---

### ⚠️ 方法的局限性
1. **未直接集成到生产级 CCL**：
   - 当前输出需转换为 MSCCL/MSCCL++ IR 才能执行。
   - 尚未嵌入 NCCL/RCCL 等主流库。

2. **静态合成假设**：
   - 合成过程为离线（offline），不支持 runtime 动态调整。
   - 对频繁变化的 workload 适应性有限。

3. **switch 建模仍简化**：
   - 虽支持 buffer 和 multicast，但未考虑更复杂的 QoS 或优先级机制。

---

### 🔮 未来工作方向
1. **Online Synthesis & Adaptation**：
   - 结合 workload profiling，实现运行时动态重合成。
2. **Integration with Production CCLs**：
   - 将 PCCL 作为 compiler backend 集成进 NCCL、RCCL。
3. **Support for Dynamic Process Groups**：
   - 支持 runtime 创建/销毁 process group 的场景。
4. **Co-design with Scheduling Systems**：
   - 与 Kubernetes、Slurm 等协同，实现 topology-aware job placement + collective synthesis 联合优化。

---

> 🏁 **总结一句话**：  
> **PCCL 是首个真正实现 scalable、generic 且 process group-aware 的 collective algorithm synthesizer，为未来十万级 NPU AI 集群的通信优化提供了坚实基础。**

</details>

---

### 5. [Spatiotemporal Imputation with Graph-Informed Flow Matching](https://arxiv.org/abs/2606.06682)

**Authors**: Zepeng Zhang, Aref Einizade, Jhony H. Giraldo, Olga Fink  
**Category**: cs.LG  
**Published**: 2026-06-08  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2606.06682v1  

#### Abstract
Missing data is a common challenge in spatiotemporal systems, arising in applications such as air quality monitoring and urban traffic management. Traditional machine learning approaches, like recurrent and graph neural networks, rely on iterative propagation, which tends to accumulate errors over t...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Spatiotemporal Imputation with Graph-Informed Flow Matching*

---

## 1. 论文的主要贡献和创新点

### 解决的问题
该论文针对**spatiotemporal imputation**（时空数据插补）中的常见挑战：  
- 传统基于 RNN 和 GNN 的模型依赖迭代传播，容易导致**误差累积**和**信息瓶颈**；  
- 扩散模型（diffusion models）虽能非自回归生成，但通常依赖**problem-agnostic Gaussian prior**（无问题先验的高斯分布），且采样过程需要大量迭代去噪步骤，效率低、鲁棒性差。

### 提出的新方法：GiFlow
作者提出 **GiFlow**（Graph-Informed Flow Matching），一种基于 **Flow Matching** 框架的新型生成式时空插补方法，其核心创新在于：

#### ✅ 创新点一：图感知先验（Graph-Informed Prior）
- 不再使用标准高斯先验，而是通过**自适应时空滤波**（adaptive spatiotemporal filtering）从可观测信号中构建一个结构化、任务相关的先验分布。
- 先验构造方式为：  
  $$
  \mathbf{X}_0 = e^{-T_n \mathcal{L}_s} \mathbf{X} \odot \mathbf{M} \cdot e^{-T_t \mathcal{L}_t}
  $$
  其中 $\mathcal{L}_s$ 和 $\mathcal{L}_t$ 分别为空间与时间图拉普拉斯，$T_n, T_t$ 为可学习的滤波因子。
- 这种 prior 更接近目标分布 $p_1$，从而显著**缩短生成轨迹**，降低传输成本（transport cost）。

#### ✅ 创新点二：混合向量场建模（Hybrid Vector Field Model）
- 向量场参数化结合了：
  - **Spatial Attention**：捕捉节点间空间相关性；
  - **Temporal Attention**：建模时间序列动态；
  - **Spatiotemporal Propagation**：通过 GNN 在时空域进行多层消息传递。
- 实现对时空依赖关系的联合建模。

#### ✅ 相比现有方法的优势
| 特性 | GiFlow | Diffusion Models | RNN/GNN Models |
|------|--------|------------------|----------------|
| 是否依赖高斯先验 | ❌（使用图感知先验） | ✅ | ✅ |
| 是否需多次采样平均 | ❌（确定性推断） | ✅ | ❌ |
| 推理效率 | ⭐ 高（单次前向传播） | 低（数十步迭代） | 中等 |
| 错误传播风险 | 极低 | 无 | 易积累 |

> ✔️ **理论保证**：论文证明该图感知先验下的 transport cost 不高于标准高斯先验（Theorem 3.2），并分析了滤波因子与感受野的关系（Proposition 3.1）。

---

## 2. 核心实验方法和设置

### 使用的数据集
| 数据集 | 类型 | 节点数 | 时间步 | 采样频率 | 描述 |
|-------|------|--------|--------|----------|------|
| **Air-36** | 空气质量 | 36 | 8760 | 每小时 | 北京PM2.5监测数据 |
| **AQI** | 空气质量 | 437 | 8760 | 每小时 | 中国43城空气质量数据 |
| **PeMS08** | 交通流量 | 170 | 17856 | 每5分钟 | 加州高速公路车流数据 |
| **Synthetic** | 合成数据 | 50 | 3000 | — | 基于图谱平滑生成 |

### 实验设置
- **缺失模式**：
  - **Point Missing**：随机掩盖 $p$ 比例的数据点；
  - **Block Missing**：连续掩盖某节点的一段时序块，直到达到 $p$ 比例。
- **训练/验证/测试划分**：70%/10%/20%
- **窗口长度**：24个时间步
- **优化器**：Adam，EMA 参数平滑
- **ODE 求解器**：Euler 方法，20 步

### 评估指标
- **MAE**（Mean Absolute Error）
- **RMSE**（Root Mean Squared Error）
- **MAPE**（Mean Absolute Percentage Error）

### 对比的基线方法
| 类别 | 方法 |
|------|------|
| 非参数法 | Mean-S, Mean-T, Linear, KNN, FP |
| RNN-based | BRITS, SAITS |
| GNN/Transformer-based | SPIN, GRIN, OPCR |
| Diffusion-based | PriSTI |
| Consistency Model | CoSTI |

---

## 3. 主要实验结果和性能指标

### 关键性能表现（以 Air-36 和 AQI 为例）

#### 表格：Air-36 上 Point Missing ($p=20\%$) 性能对比（部分）
| Model       | MAE ↓     | RMSE ↓    | MAPE ↓     |
|-------------|-----------|-----------|------------|
| BRITS       | 14.23     | 24.64     | 31.42      |
| GRIN        | 9.94      | 19.09     | 21.95      |
| PriSTI      | 10.29     | 19.66     | 21.91      |
| **GiFlow**  | **9.54**  | **18.10** | **21.27**  |

> ✅ GiFlow 在所有指标上均取得最优。

#### 表格：Block Missing 下的表现更凸显优势
| Model       | MAE ↓     | RMSE ↓    | MAPE ↓     |
|-------------|-----------|-----------|------------|
| Linear      | 33.03     | 52.53     | 81.95      |
| BRITS       | 17.78     | 28.16     | 32.19      |
| **GiFlow**  | **14.76** | **25.33** | **28.95**  |

> 🔍 在存在连续缺失块的情况下，仅依赖局部时间信息的方法性能严重下降，而 GiFlow 凭借全局时空建模能力保持领先。

#### PeMS08 数据集结果（Point Missing）
| Model       | MAE ↓     | RMSE ↓    | MAPE ↓     |
|-------------|-----------|-----------|------------|
| OPCR        | 12.77     | 19.88     | 8.67       |
| PriSTI      | 13.02     | 20.08     | 8.79       |
| **GiFlow**  | **12.66** | **19.83** | **8.43**   |

> ✅ 在交通数据上同样实现 SOTA 性能。

---

### 消融实验结果（Ablation Studies）

#### （1）不同先验设计的影响（Air-36, Point Missing）
| Model           | Transport Cost ↓ | MAE ↓     |
|------------------|------------------|-----------|
| FM-Gauss         | 299.62           | 12.79     |
| TFM (temporal only) | 123.39         | 10.12     |
| GFM (spatial only)  | 115.05         | 9.75      |
| **GiFlow (full)**   | **104.29**     | **9.54**  |

> 📌 结论：
> - 图感知先验显著降低 transport cost；
> - 空间滤波比时间滤波贡献更大；
> - 联合建模效果最佳。

#### （2）组件移除实验
| 变体                         | MAE ↑     | ΔMAE |
|------------------------------|-----------|------|
| Full GiFlow                  | 9.54      | —    |
| w/o spatial attention        | 10.05     | +0.51 |
| w/o temporal attention       | 9.87      | +0.33 |
| w/o spatiotemporal propagation | 10.40   | +0.86 |

> 📌 信息传播机制（spatiotemporal propagation）影响最大，说明跨时空的消息传递至关重要。

---

### 效率与敏感性分析

#### 推理速度对比（单位：分钟）
| Model     | Air-36 | AQI   | PeMS08 |
|----------|--------|-------|--------|
| PriSTI   | 9.30   | 43.12 | 7.46   |
| CoSTI    | 0.37   | 8.41  | 3.63   |
| **GiFlow** | **0.28** | **2.47** | **0.99** |

> ⚡ GiFlow 是目前最快的生成式方法之一，尤其在大规模数据上优势明显。

#### 不同 Euler Steps 的权衡
| Steps | MAE ↓     | 推理时间 (秒) |
|-------|-----------|---------------|
| 1     | 9.87      | 1.58          |
| 5     | 9.81      | 4.60          |
| 20    | **9.54**  | 17.15         |

> ✅ 即使只用 5 步也能超越多数基线，具备良好的**效率-精度权衡**。

---

## 4. 关键结论和发现

### 主要发现
1. **图感知先验有效提升性能**：相比 Gaussian prior，利用时空滤波构造的 prior 更贴近真实数据分布，显著减少生成路径长度和 transport cost。
2. **GiFlow 实现 SOTA 性能**：在多种数据集、缺失模式和缺失率下，全面优于 RNN、GNN、Transformer 和扩散模型。
3. **高效推理**：无需多轮采样，支持快速确定性生成，适用于大规模实时系统。
4. **自适应感受野机制**：滤波参数 $T_n, T_t$ 随缺失率增加而增大，表明模型自动扩展感受野以应对更高不确定性，符合理论预期（Proposition 3.1）。

### 方法的局限性
- **图结构依赖性强**：若输入图质量差（如阈值过高或过低），性能会下降（见 Table 6）。虽然对中等扰动鲁棒，但仍需合理构建邻接矩阵。
- **滤波因子需离线优化**：$T_n, T_t$ 在训练阶段通过最小化重构误差优化，在推理时固定，缺乏在线自适应能力。
- **当前为确定性模型**：默认输出唯一解，若需不确定性估计，需额外注入噪声。

### 未来工作方向
- 将 filtering factors 设为条件变量，实现动态调整；
- 扩展至多变量信号或多模态融合场景；
- 探索与其他快速生成框架（如 Consistency Models）结合的可能性；
- 应用于更广泛的时空预测任务（forecasting, anomaly detection）。

---

> 💡 **一句话总结**：  
> GiFlow 通过引入**图感知先验 + Flow Matching** 框架，解决了传统方法中“先验不匹配”与“生成低效”的双重难题，在精度与速度上实现了双重突破，是面向现实世界时空数据修复的一项重要进展。

</details>

---

### 6. [Structure-Preserving Correction Learning for Sparse Bayesian Inference in Brain Source Imaging](https://arxiv.org/abs/2606.07196)

**Authors**: Marco Morik, Xiao Ruiting, Shinichi Nakajima, Stefan Haufe, Ismail Huseynov  
**Category**: cs.LG  
**Published**: 2026-06-08  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2606.07196v1  

#### Abstract
Classical sparse Type-II Bayesian methods for M/EEG brain imaging support joint estimation of source and noise hyperparameters, but rely on fixed iterative update rules. Although these updates are principled and interpretable, their dynamics cannot be adapted from data. We propose to learn the updat...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：Structure-Preserving Correction Learning for Sparse Bayesian Inference in Brain Source Imaging**

---

## 1. **论文的主要贡献和创新点**

### ✅ **解决了什么问题**
在 M/EEG 脑源成像中，**稀疏贝叶斯学习（Sparse Bayesian Learning, SBL）** 是一种经典的 Type-II 贝叶斯方法，用于联合估计源活动和噪声超参数。然而，传统方法依赖固定的迭代更新规则（如 EM、MacKay 或 convex-bounding），这些规则虽然具有理论依据且可解释，但其动态过程无法从数据中自适应调整。

此外，尽管深度学习方法（如 DeepSIF）能提升重建速度和精度，但它们通常将整个推理过程黑箱化，牺牲了模型的**可解释性和物理一致性**。

> **核心挑战**：如何在保留经典贝叶斯推断结构的前提下，利用数据驱动的方式优化其更新机制？

---

### 🚀 **提出了什么新方法或新思路**
本文提出了一种 **“结构保持的修正学习”（Structure-Preserving Correction Learning）框架**，结合了模型驱动与数据驱动的优点：

- 将经典的 **convex-bounding solver** 进行**展开（unfolding）**，构造成一个可训练的神经网络架构，每一层对应一次原始算法的迭代。
- 在 log-domain 中对超参数更新进行稳定表示，并引入**可学习的修正项（correction terms）** 来增强原始更新规则。
- 所有变体在初始化时完全复现原始 solver，确保训练前即具备正确的行为。

#### 提出三种渐进式表达能力更强的修正机制：
1. **Bias-only Correction (Bias CB)**  
   每层添加可学习的偏置向量，实现层特定但输入无关的修正。
   
2. **Residual MLP Correction (Deep CB)**  
   使用共享的 pointwise MLP 学习输入相关的修正，泛化性强，适用于不同传感器/源空间配置。

3. **Attention-Augmented Residual Correction (Deep Attn. CB)**  
   引入跨源注意力机制，使每个源的更新可以感知其他源的状态，捕捉全局上下文依赖。

> 🔍 关键思想：不替代原有贝叶斯机制，而是通过**残差式修正**来微调其行为 —— “**Learn corrections, not replacements**”。

---

### ⭐ **相比现有方法的优势**
| 维度 | 优势 |
|------|------|
| **可解释性** | 完全保留原始 Bayesian 结构，修正项具有明确语义，非黑箱模型 |
| **灵活性** | 可以端到端训练，适应复杂噪声模式和真实数据分布 |
| **泛化性** | 特别是 Deep CB 和 Deep Attn. CB，因参数共享，能推广到未见的 sensor/source 配置（zero-shot） |
| **收敛性** | 显著加速收敛，尤其在早期迭代中提供强修正 |
| **性能** | 在多项指标上超越传统 SBL 和端到端深度模型（如 DeepSIF） |

---

## 2. **核心实验方法和设置**

### 📚 **使用的数据集**
由于体内真实脑源活动不可知，实验主要基于**合成数据集**，并辅以真实世界数据的零样本验证：

#### 合成数据生成流程：
- 使用 **fsaverage 模板大脑** 构建前向模型（lead-field matrix `L`）
- 源空间为 **ico3 mesh（1284 sources）**，固定方向
- 模拟 **spatiotemporal sparse sources**，数量服从 `U(5,20)`，时间信号按 delta/theta/alpha/mu/beta 频带随机生成
- 添加 **异方差高斯噪声（heteroscedastic noise）**，每通道 SNR ~ `U(5,30) dB`

#### 验证设置（Out-of-Distribution Generalization）：
| 设置名称 | 描述 |
|--------|------|
| **Train Cap, Ico3** | 训练与标准测试环境一致 |
| **Things Cap, Ico3** | 新的传感器布局（THINGS-EEG），更长的时间窗口（600 vs 100 步） |
| **Things Cap, Ico4** | 更细粒度源空间（5124 sources），检验 zero-shot 推广能力 |

#### 真实数据验证：
- 使用公开数据集 **THINGS-EEG2** 进行零样本（zero-shot）测试
- 分析单次试验（single-trial）与平均试次（trial-averaged）下的视觉诱发响应定位

---

### 📊 **评估指标**
| 指标 | 公式/说明 | 目标 |
|------|----------|-------|
| **rMSE**（相对均方误差） | $\frac{\|\hat{X} - X^*\|^2}{\|X^*\|^2}$ | ↓ 越小越好 |
| **EMD**（Earth Mover’s Distance） | 最优传输距离，衡量预测与真值的空间分布差异 | ↓ |
| **F1-score** | 支持集恢复准确率（thresholded RMS amplitude） | ↑ |
| **LE**（Localization Error） | 真实峰值到最近预测峰值的平均欧氏距离 | ↓ |
| **Inference Time** | 单样本推理耗时 | ↓ |

---

### 🔁 **基线方法对比**
| 方法 | 类型 | 是否可解释 | 是否支持 joint (γ, λ) 学习 |
|------|------|------------|-----------------------------|
| **sLORETA** | 线性最小范数解 | ✅ | ❌ |
| **Convex Bounding (I)** | 经典 SBL，固定噪声 | ✅ | ❌ |
| **Convex Bounding (I,A)** | 经典 SBL，联合学习 γ 和 λ | ✅ | ✅ |
| **DeepSIF** | 端到端深度网络 | ❌ | ✅（隐式） |
| **Bias CB / Deep CB / Deep Attn. CB** | 本文方法 | ✅ | ✅ |

---

## 3. **主要实验结果和性能指标**

### 📈 **关键性能数据（Train Cap, Ico3 setting，5 seeds 平均）**

| 方法 | rMSE ↓ | EMD ↓ | F1 ↑ | LE ↓ | Time (s) ↓ |
|------|--------|--------|------|--------|------------|
| Convex Bounding (I) | 0.410 | 0.0122 | 0.535 | 0.0056 | 0.0048 |
| Convex Bounding (I,A) | 0.434 | 0.0130 | 0.522 | 0.0060 | 0.0046 |
| sLORETA | 24.373 | 0.0291 | 0.038 | 0.0251 | 0.0010 |
| DeepSIF | 0.796±0.007 | 0.0403±0.0018 | 0.331±0.009 | 0.0104±0.0001 | 0.0003±0.0001 |
| **Deep CB (I)** | **0.344±0.006** | **0.0105±0.0002** | **0.594±0.008** | **0.0048±0.0000** | 0.0027 |
| **Deep Attn. CB (I)** | **0.323±0.002** | **0.0102±0.0002** | **0.608±0.003** | **0.0045±0.0000** | 0.0071 |

> ✅ 所有提出的修正学习方法均显著优于经典 convex bounding 和 DeepSIF；其中 **Deep Attn. CB 表现最佳**

---

### 🔍 **与基线方法的对比结果**
- **vs. 经典 SBL**：
  - 所有修正版本在 rMSE、EMD、F1 上均有明显提升（约 10–20%）
  - **Deep Attn. CB** 将 EMD 降低至 0.0102（原为 0.0122），F1 提升至 0.608（原为 0.535）
  - 收敛更快（见下图）

- **vs. DeepSIF**：
  - DeepSIF 在 rMSE 上表现尚可，但在 EMD 和 F1 上远差于本文方法 → **无法有效恢复稀疏结构**
  - 本文方法更具空间特异性，重建更聚焦

- **Joint Learning (I,A) vs. Known Noise (I)**：
  - 即使同时学习噪声 λ，性能下降极小（如 Deep CB: rMSE 0.344 → 0.348）
  - 表明所提 joint learning 框架非常鲁棒

---

### 🔧 **消融实验结果**
#### （1）修正机制的有效性（图 8 & 表 3）
- **Bias CB**：有一定改进，但受限于输入无关性，泛化能力弱
- **Deep CB**：MLP 引入输入依赖后，性能跃升，且可在 Things Cap Ico4 上 zero-shot 推广
- **Deep Attn. CB**：进一步引入跨源交互，在大多数设置下达到最优

#### （2）收敛行为分析（图 4）
- **Deep Attn. CB** 在前几层快速逼近最优解，收敛速度远超传统方法
- 加入 **stochastic deep supervision** 后，中间层稳定性大幅提升，避免梯度弥散

#### （3）修正项演化趋势（图 8, C.3）
- 早期层修正幅度大（尤其是 joint setting），后期逐渐趋于零
- 说明网络主要在初始阶段“纠偏”，后期回归经典更新路径
> 💡 **结论**：学习的是**瞬态修正**，而非永久改变动力学 —— 符合“结构保持”的设计初衷

---

## 4. **关键结论和发现**

### ✅ **主要发现**
1. **修正学习有效提升了 SBL 性能**：  
   在不破坏原有贝叶斯结构的前提下，通过学习残差修正项，显著改善了重建质量、定位精度和支持集恢复能力。

2. **结构保持 ≠ 性能妥协**：  
   本文方法既保留了经典算法的可解释性与物理一致性，又获得了接近甚至超越端到端深度模型的经验性能。

3. **注意力机制带来额外增益**：  
   允许源之间相互参考的 attention 模块能更好地建模分布式源之间的关系，尤其在复杂场景中表现突出。

4. **联合学习噪声是可行且稳健的**：  
   即使在未知异方差噪声下，joint (γ, λ) learning 几乎无性能损失，增强了实用性。

5. **零样本迁移成功**：  
   在 THINGS-EEG2 数据上的 zero-shot 应用表明，该框架能迁移到真实 EEG 场景，恢复合理的视觉皮层激活模式。

---

### ⚠️ **局限性**
1. **假设限制**：
   - 当前仅支持 **fixed-orientation sources** 和 **diagonal covariance models**
   - 不支持自由朝向偶极子或 full noise covariance

2. **依赖合成数据训练**：
   - 缺乏真实的 ground truth，导致模型可能过拟合训练分布（如 sparsity level）
   - 在极端稀疏情况（1–3 sources）下性能略有下降

3. **计算开销较高**：
   - 展开 25 层的训练成本高（最多达 15 小时/模型）
   - 虽然推理快（<0.1s/sample），但训练需大量 GPU 时间（项目总计 ~2000 GPU 小时）

---

### 🔮 **未来工作方向**
1. **扩展至 MEG 和自由朝向建模**
2. **引入更复杂的噪声结构**（如时空相关噪声）
3. **探索 correction learning 在其他 Type-II 贝叶斯模型中的应用**（如 ARD、RVM）
4. **轻量化设计**：减少层数或使用循环结构以降低训练成本
5. **在线自适应修正**：让模型在实际应用中持续微调修正策略

---

## ✅ 总结一句话
> 本文提出了一种**结构保持的修正学习框架**，通过在展开的经典 SBL solver 上叠加可学习的残差修正项，在不牺牲可解释性的前提下，实现了更优的脑源成像重建性能与更快的收敛速度，为**可解释深度学习与物理模型融合**提供了典范路径。

</details>

---

### 7. [Sparsely gated tiny linear experts](https://arxiv.org/abs/2606.07414)

**Authors**: Simon Schug  
**Category**: cs.LG  
**Published**: 2026-06-08  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2606.07414v1  

#### Abstract
Sparsity allows scaling model parameters without proportionally increasing computational cost. While mixture of experts (MoE) models are made increasingly sparse, individual experts typically remain large and dense. Here, we demonstrate that further increasing sparsity by shrinking each expert to co...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文《Sparsely gated tiny linear experts》核心总结

## 1. 主要贡献和创新点

### 解决的问题
当前大型语言模型（LLMs）中的 **Feedforward layers** 是计算开销的主要来源之一。传统的密集前馈网络（如 MLP 或 SwiGLU）在每次前向传播中激活所有参数，导致计算成本随模型规模线性增长。虽然 **Mixture of Experts (MoE)** 架构通过稀疏激活专家实现了更高的计算效率，但单个专家通常仍是大型且密集的模块，限制了进一步优化的空间。

此外，这些非线性、高维的结构也增加了模型的“黑箱”特性，使得 **interpretability**（可解释性）变得困难。

### 提出的新方法：sgatlin
本文提出了一种全新的前馈层设计——**sparsely gated linear neurons (sgatlin)**，其核心思想是将 MoE 中的“专家”缩小到极致：**每个专家仅由一个线性神经元构成**。

- **Sparse Gating**: 使用一个高效的 **gating network** 从大量可用的线性神经元中选择一小部分（top-k）进行激活。
- **Linear Neurons**: 移除了传统 MoE 中对专家输出施加的非线性激活函数（如 ReLU, GeLU），使被选中的子电路成为纯粹的线性变换。
- **Efficient Routing**: 利用 **product-top-k** 机制实现高效路由，在亚线性时间内完成大规模神经元集合上的选择。

### 相比现有方法的优势
| 特性 | 传统 MLP/SwiGLU | 传统 MoE | sgatlin |
|------|------------------|----------|--------|
| **计算密度** | 高（全激活） | 中等稀疏 | 极高稀疏（<0.1% 参数激活/token） |
| **计算效率** | 低 | 中 | 高（参数扩展不显著增加 FLOPs） |
| **可解释性** | 差（非线性混合） | 中等（专家仍复杂） | 高（线性组合 + 明确的门控标识） |
| **结构透明度** | 黑箱 | 灰箱 | 接近白箱 |

> ✅ **关键洞见**：移除非线性反而提升了性能，因为 **top-k 路由本身已足以引入必要的非线性行为**，而线性化极大增强了分析能力。

---

## 2. 核心实验方法和设置

### 数据集
- **主语言建模任务**：`SlimPajama-627B`（6270亿 token 的清洗文本语料）
- **可解释性研究**：`TinyStories`（专为小模型设计的儿童故事数据集，用于可控分析）

### 实验设置
- **模型架构**：Decoder-only Transformer
- **上下文长度**：2048 tokens（SlimPajama），1024 tokens（TinyStories）
- **训练方式**：Autoregressive Language Modeling
- **评估指标**：
  - **Perplexity**（困惑度）作为主要性能指标
  - **Compute Sparsity**（每 FLOP 对应的参数数）衡量效率
  - **Normalized Indirect Effect (NIE)** 衡量因果干预效果

### 基线方法对比
| 方法 | 类型 | 描述 |
|------|------|------|
| `MLP` | Dense | 标准 GeLU 激活的前馈层 |
| `SwiGLU` | Dense | 当前主流的门控前馈结构 |
| `MoE` | Coarse-grained | 如 GPT-OSS 中使用的 MoE，专家较大 |
| `PEER` | Fine-grained MoE | 极细粒度 MoE，专家为单神经元，但保留非线性 |

> 所有模型在相同 **FLOP 预算下进行 isoflop 比较**，确保公平性。

---

## 3. 主要实验结果和性能指标

### 关键性能数据（SlimPajama 上的语言建模）

| FLOP Budget | 最佳架构 | Test Perplexity |
|------------|---------|----------------|
| 1e17       | sgatlin | ~40            |
| 6e17       | sgatlin | ~25            |
| 1e18       | sgatlin | ~22            |
| 6e18       | sgatlin | **~18.2**      |

> 📈 **结论**：在所有计算预算下，**sgatlin 均优于或至少持平于其他架构**，尤其在高预算下优势明显。

### 与基线方法对比结果
- 在同等 FLOP 下，**sgatlin 实现了最高的 compute sparsity**（即更多参数未被激活，节省计算）。
- 图 3 显示，随着模型规模扩大，**sgatlin 的 perplexity 下降最快**，表明其更有效地利用了额外参数。
- 相比 PEER，尽管两者都使用单神经元专家，**sgatlin 因移除非线性和改进门控机制表现更好**。

### 消融实验结果（Ablation Study）
在 6e18 FLOP 预算下的 1.2B 模型上测试：

| 变体 | Test Perplexity | 相对变化 |
|------|----------------|----------|
| **sgatlin (原版)** | **18.1910** | — |
| + ReLU 激活 | 21.0880 | ↑ +15.9% |
| + GeLU 激活 | 20.8445 | ↑ +14.6% |
| + Swish 激活 | 20.6424 | ↑ +13.5% |
| 替换为 PEER 路由器 | 18.2964 | ↑ +0.58% |

> 🔍 **关键发现**：
> - 添加任何非线性都会**显著降低性能**，验证了“无需非线性”的反直觉假设。
> - 自定义 gating network 比 PEER 更优，说明轻量化设计有效。

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **稀疏 + 线性 = 高效且可解释**  
   将专家缩小至单一线性神经元，并结合稀疏门控，不仅能提升计算效率，还能自然形成**语义结构化的 feedforward circuits**。

2. ✅ **门控机制本身提供足够非线性**  
   top-k 选择操作已能捕捉复杂的输入依赖关系，无需再对神经元输出应用非线性函数。

3. ✅ **可解释性突破**  
   - 每个 feedforward circuit 由唯一的 **gating weights 向量唯一标识**。
   - 不同 circuit 之间的相似性可通过 **cosine distance** 度量。
   - 实验显示，相似 gating weights 对应的 circuits 处理语义相近的内容（如名字、代词聚类）。
   - **因果干预实验证明**：修改特定位置的 gating weights 可影响 factual recall 输出，说明知识存储在这些线性子电路中。

4. ✅ **形成语义度量空间**  
   利用 UMAP 对 gating weights 降维可视化，发现明显的语义聚类（如人名、动词时态、“be” 动词变体等）。

### 局限性
- 当前工作聚焦于 **feedforward layers 的稀疏化**，attention mechanism 仍保持 dense，未来可探索整体稀疏化。
- 实验基于理想化的 **isoflop 设置**，实际硬件（如 GPU）对稀疏计算支持有限，可能影响 wall-clock 时间表现。
- 可解释性分析目前在 **TinyStories 小模型上验证**，需扩展到更大规模模型以确认普适性。

### 未来工作方向
- 将 sgatlin 思路推广至 **encoder-decoder 或多模态模型**。
- 结合 **sparse attention** 技术，构建端到端的超稀疏 Transformer。
- 开发基于 sgatlin 的新型 **interpretability tools**，例如自动发现“事实回路”或编辑模型知识。
- 探索 **理论层面的意义**：由于整个 forward pass 在固定 gating 下变为 affine transformation，这为理解 LLM 内部机制提供了新的数学框架。

---

> 💡 **总体评价**：  
> 该论文提出了一个简洁而强大的新范式——**sgatlin**，它不仅在语言建模任务上实现了**计算效率与性能的双重提升**，更重要的是打开了通往**真正可解释的大模型架构**的大门。其“极简主义”设计理念（tiny linear experts + sparse gating）可能对未来模型设计产生深远影响。

</details>

---

### 8. [Explicit Evidence Grounding via Structured Inline Citation Generation](https://arxiv.org/abs/2606.07130)

**Authors**: Anar Yeginbergen, Amelie W\"uhrl, Anna Rogers, Rodrigo Agerri  
**Category**: cs.CL  
**Published**: 2026-06-08  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2606.07130v1  

#### Abstract
As AI systems become more widely adopted, the demand for factual and faithful generation grows. Properly attributing information through citations becomes, therefore, crucial. This work introduces FullCite, a framework that, in contrast to most previous works, generates structured inline citations l...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Explicit Evidence Grounding via Structured Inline Citation Generation*

---

## 1. 论文的主要贡献和创新点

### 解决的问题
随着大型语言模型（LLMs）在高风险领域（如医学、法律、科学）的广泛应用，生成内容的**事实准确性**和**可追溯性**变得至关重要。然而，当前大多数基于检索增强生成（RAG）的系统仅提供粗粒度的**文档级引用**（document-level citations），缺乏对支持声明的具体文本证据（即细粒度证据跨度）的精确标注。这导致用户难以验证生成内容是否真正由检索到的证据支撑。

此外，现有方法在以下方面存在不足：
- 引用格式不统一或不可靠；
- 模型倾向于依赖参数化知识而非检索上下文；
- 对长上下文中的中间信息处理能力弱（lost-in-the-middle）；
- 在二元问题（yes/no）上常省略引用。

### 提出的新方法：FullCite
本文提出 **FullCite**，一个用于生成**结构化内联引用**（structured inline citation）的框架，其核心创新在于：
- **联合生成文档标识符和原文证据片段**：每个声明后紧跟 `{doc_id: <id>, snippet: <verbatim text>}` 形式的引用，实现从“文档”到“具体句子”的双重归因。
- 支持三种不同的引用生成策略：
  1. **Prompt-based generation**：通过提示引导模型输出结构化引用；
  2. **Constrained decoding over citation grammar**：使用有限状态自动机约束解码过程，确保格式正确性和原文一致性；
  3. **Posthoc span alignment**：先自由生成答案，再通过相似度匹配将生成的引用近似对齐到最接近的原文片段。

### 相比现有方法的优势
| 维度 | 现有方法局限 | FullCite改进 |
|------|----------------|-------------|
| 引用粒度 | 多为文档级引用，无法定位具体证据 | 同时支持文档级 + 细粒度证据跨度引用 |
| 结构可靠性 | 依赖模型指令遵循能力，易出错 | 可通过约束解码或事后对齐提升结构合规性 |
| 评估全面性 | 缺乏对证据跨度准确性的量化 | 提出 Snippet-F1、ROUGE-L、chrF++ 等多维度评估 |
| 透明度与可信度 | 用户难判断引用真实性 | 显式展示原文片段，增强可解释性和信任 |

---

## 2. 核心实验方法和设置

### 使用的数据集
实验基于三个涵盖不同领域的问答基准：

| 数据集 | 领域 | 特点 |
|--------|------|------|
| **BioASQ** | 生物医学 | 包含 PubMed 文档及黄金证据位置，原生支持细粒度标注 |
| **ASQA** | 通用领域 | 聚焦模糊事实类问题，原始仅有文档级标注 |
| **ExpertQA** | 多领域（32个） | 专家标注的知识源，覆盖 yes/no、factoid、list、summary 四种题型 |

> 注：ASQA 和 ExpertQA 原始无细粒度证据标注，作者使用 GPT-5.4-mini 自动提取原子证据片段，并人工审核过滤不适合的任务实例（约剔除 500/350 条），以保证评估有效性。

### 实验设置
- **模型**：选用两个开源大模型进行测试：
  - Qwen3-8B
  - Gemma-3-12B-it
- **超参数**：温度=0.7，top-p=0.95，最大输出长度=1500 tokens
- **引用格式要求**：必须严格符合 `{doc_id: ..., snippet: ...}` 结构，snippet 长度限制在 20–512 字符之间

### 评估指标
从三个维度综合评估引用质量：

| 指标类别 | 具体指标 | 描述 |
|---------|----------|------|
| **Document-level** | Doc-F1 | 衡量引用文档集合与黄金文档的重合程度 |
| **Snippet-level** | Snippet-F1, ROUGE-L, Jaccard F1, chrF++ | 评估生成证据片段与黄金片段的表面匹配度 |
| **Claim-Citation Faithfulness** | Semantic Similarity (all-MiniLM-L6-v2), LLM-as-a-Judge (GPT-5.4), Human Evaluation | 判断引用是否语义上支持其所附的声明 |

### 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| **Generate-then-Retrieve** | Posthoc | 先生成答案，再用 BM25 + Sentence Transformer 检索支持文档/片段 |
| **ReClaim (Xia et al., 2025)** | Constrained | 使用两阶段模型强制生成声明与证据，但未强调文档归属 |

---

## 3. 主要实验结果和性能指标

### 关键性能数据（来自 Table 2）

| 方法 / 模型 | ASQA – Doc-F1 | ASQA – Snippet-F1 | ASQA – Similarity |
|------------|---------------|--------------------|-------------------|
| Prompt-based (Qwen3-8B) | 33.87 | 12.80 | 56.55 |
| **FullCite (Posthoc, Qwen3-8B)** | **80.98** | **61.87** | **52.17** |
| FullCite (Constrained, Qwen3-8B) | 74.59 | 55.11 | 51.60 |
| Generate-then-Retrieve | 93.74 | 75.07 | 42.93 |

| 方法 / 模型 | BioASQ – Doc-F1 | BioASQ – Snippet-F1 | BioASQ – Similarity |
|------------|------------------|---------------------|----------------------|
| Prompt-based (Qwen3-8B) | 58.08 | 6.18 | 64.89 |
| **FullCite (Posthoc, Qwen3-8B)** | 49.25 | **24.23** | 56.75 |
| FullCite (Constrained, Qwen3-8B) | 43.37 | 17.35 | 53.53 |

| 方法 / 模型 | ExpertQA – Doc-F1 | ExpertQA – Snippet-F1 | ExpertQA – Similarity |
|------------|--------------------|-----------------------|------------------------|
| Prompt-based (Qwen3-8B) | 56.42 | 5.56 | 64.61 |
| **FullCite (Posthoc, Qwen3-8B)** | 53.92 | **28.44** | 56.82 |
| FullCite (Constrained, Qwen3-8B) | 65.80 | 27.23 | 53.54 |

> ✅ **关键观察**：
> - 所有模型在 **Doc-F1 上表现较好**，说明识别相关文档相对容易；
> - **Snippet-F1 普遍偏低**（baseline 平均 ~10%），表明精确定位证据跨度仍是巨大挑战；
> - **Posthoc 策略带来最大增益**：在 ASQA 上 Snippet-F1 从 12.80 提升至 61.87（+49.07 pts）；
> - Constrained 解码虽能提高结构合规性，但性能提升有限且可能降低语义连贯性。

### 与其他方法的对比结果
| 方法 | Doc-F1 | Snippet-F1 | 优势分析 |
|------|--------|-----------|---------|
| Generate-then-Retrieve | 最高（~94% in ASQA） | 中等（~75%） | 文档召回强，但生成与引用脱节，**语义相似度最低（42.93）** |
| ReClaim | —— | 最高 BioASQ 达 43.96 | 专注证据生成，但忽略文档归属，**无法衡量完整归因能力** |
| **FullCite (posthoc)** | 高 | 显著优于 prompt-based | **唯一同时报告 Doc-F1 和 Snippet-F1 且保持合理语义一致性的框架** |

### 消融实验与关键发现
#### （1）引用策略影响
- **Posthoc > Constrained > Prompt-based** 在证据识别上有明显优势；
- 但更强的结构控制（constrained）可能导致语义退化（Qwen 表现下降）；
- Gemma 更稳定，在 constrained 设置下仍维持高 similarity。

#### （2）引用遗漏与偏差现象
- **Primacy Bias**：在 BioASQ（固定5篇文档）中，**81.8% 的引用集中在前两篇文档**（见 Figure 3），反映 LLM “lost-in-the-middle” 问题严重；
- **Yes/No 问题引用率最低**：模型倾向直接回答而不提供依据，尤其在 baseline 设置中；
- **引用覆盖率低**：多数响应只引用少数文档，未能覆盖全部黄金文档。

#### （3）下游任务性能（Table 3）
- 在 BioASQ 上，posthoc 设置平均提升 **+19.85 ROUGE-L 分数**；
- 尽管 baseline 在 yes/no 问题上 macro-F1 更高，但这源于**跳过引用机制**，并非真实性能优势；
- 引用有助于提升短小、可验证答案的质量，对开放性摘要帮助较小。

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **LLMs 能有效识别相关文档，但在精准定位支持证据方面表现极差**  
   → Doc-F1 ≫ Snippet-F1 是普遍现象，凸显当前系统“知其然不知其所以然”。

2. ✅ **Posthoc 对齐策略显著提升证据识别精度**  
   → 容忍轻微表述差异并通过 Jaccard 相似度重建引用，是实用有效的折中方案。

3. ✅ **FullCite 是目前唯一兼顾文档级与证据级归因的平衡框架**  
   → 在 Doc-F1、Snippet-F1 和 semantic similarity 三者间取得最佳权衡。

4. ⚠️ **系统性偏见广泛存在**：
   - **Primacy bias**：偏好前列文档，忽视中后部信息；
   - **Citation omission**：尤其在 yes/no 问题中逃避引用责任。

5. 🔍 **表面相似 ≠ 真实支持**  
   → 即使 claim 与 citation 语义高度相似，也可能只是“看起来合理”，未必构成逻辑支撑。

### 方法的局限性
- **依赖外部标注质量**：ASQA/ExpertQA 的细粒度标注为自动生成，可能存在噪声；
- **未解决根本性建模缺陷**：FullCite 不缓解 primacy bias 或 yes/no 忽略引用的问题；
- **评估指标仍有局限**：自动指标（如 ROUGE-L）不能完全替代人类判断是否“真正支持”；
- **模型规模限制**：仅在两个开源模型上验证，结果是否泛化至更大闭源模型未知；
- **缺乏训练机制探索**：未尝试 fine-tuning 或 instruction-tuning 专门优化联合引用任务。

### 未来工作方向
1. 设计更鲁棒的训练目标，显式优化 **joint document + span attribution**；
2. 开发机制强制模型处理长上下文中所有文档，缓解 **primacy bias**；
3. 构建针对 binary questions 的专用引用激励机制；
4. 探索结合 retrieval 与 generation 的端到端可微架构；
5. 建立更大规模、高质量的人工标注细粒度引用数据集（如 VerbatimQA++）；
6. 发展能区分“表面相似”与“实质支持”的新型评估范式（beyond similarity）。

---

> 📌 **总结一句话**：  
> **FullCite 揭示了一个关键现实——让 LLMs “说出来源”并不难，但让它“准确指出哪句话支撑这个说法”仍然极具挑战。迈向真正可信的 attributed QA，必须超越文档检索，聚焦于细粒度证据跨度的识别与验证。**

</details>

---

### 9. [GenPO++: Generative Policy Optimization with Jacobian-free Likelihood Ratios](https://arxiv.org/abs/2606.06967)

**Authors**: Ke Hu, Shutong Ding, Panxin Tao, Jingya Wang, Ye Shi  
**Category**: cs.LG  
**Published**: 2026-06-08  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2606.06967v1  

#### Abstract
Generative policies provide expressive and multimodal action distributions, making them attractive for reinforcement learning (RL) in complex continuous-control tasks. Among them, flow-based policies are especially appealing because they generate actions through deterministic transport maps. However...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：GenPO++: Generative Policy Optimization with Jacobian-free Likelihood Ratios

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
在基于 likelihood 的 on-policy 强化学习（如 PPO）中，**flow-based 和 diffusion-based 生成式策略**虽然能表达复杂的多模态动作分布，但在实际应用中面临一个核心瓶颈：  
**如何高效且准确地计算已执行动作在新旧策略下的概率密度比（likelihood ratio）**。

现有方法存在以下两类缺陷：
- **FPO** 使用 ELBO 替代真实 likelihood ratio，导致更新目标有偏（biased），影响训练稳定性。
- **GenPO** 通过引入 dummy action 扩展动作空间以实现精确逆变换和密度估计，但带来了额外的计算开销和维度膨胀问题。

### 提出了什么新方法或新思路
本文提出 **GenPO++**，一种可逆的高阶生成式策略优化框架，其核心思想是：
> 利用 **ODE 求解器的历史状态（solver-history states）作为辅助记忆**，替代 GenPO 中独立的 dummy action，在不改变原始动作维度的前提下实现**精确可逆性**和**无 Jacobian 的 likelihood ratio 计算**。

具体技术路径包括：
- 构造一个基于高阶 Adams-Bashforth 风格的 **reversible ODE solver**，利用前一步的状态 $x_{i-1}$ 与当前状态 $x_i$ 共同构成增广变量 $(x_i, x_{i-1})$。
- 该构造使得前向传播和反向恢复都可在闭式下完成（closed-form inversion）。
- 更重要的是，该映射的 **log-determinant 仅依赖于固定的求解器系数**，与神经网络参数无关，从而实现了 **Jacobian-free 的精确 likelihood ratio 计算**。

### 相比现有方法的优势
| 维度 | GenPO++ | FPO | GenPO |
|------|--------|-----|-------|
| **Likelihood Ratio 准确性** | ✅ 精确 | ❌ 近似（ELBO） | ✅ 精确 |
| **是否扩展动作空间** | ❌ 否 | ❌ 否 | ✅ 是（dummy action） |
| **计算效率（训练时间）** | ⭐ 高 | 中等 | 低（需 Jacobian 反向传播） |
| **适用于 fine-tuning** | ✅ 是 | ✅ 是 | ❌ 困难（破坏原策略结构） |
| **训练稳定性** | ✅ 高（精确 ratio） | ❌ 易崩溃（偏差累积） | ✅ 高 |

---

## 2. 核心实验方法和设置

### 使用的数据集与任务
实验覆盖三大类场景，验证 GenPO++ 在不同 setting 下的有效性：

#### （1）IsaacLab 大规模仿真控制任务（从零学习）
- 包括 8 个高维连续控制任务：
  - `Ant`, `Humanoid`（locomotion）
  - `Open-Drawer`（manipulation）
  - `Anymal-D-Rough`, `Go2-Rough`, `G1-Rough`, `H1-Rough`, `Digit-LocoManip`（rough terrain locomotion & whole-body control）

#### （2）Robomimic 操控任务（在线微调）
- 对预训练的 flow-matching 策略进行 online fine-tuning：
  - `CAN`
  - `BOX CLEANUP`
  - `THREADING`

#### （3）真实世界灵巧手操作任务
- 在 **RobotEra Xhand** 平台上部署，执行“旋转并拧松螺母”任务（nut-bolt disassembly），测试 sim-to-real 能力。

---

### 实验设置和评估指标

| 设置项 | 描述 |
|-------|------|
| **Rollout 与 更新架构** | 基于 RSL-RL 框架统一实现，确保公平比较 |
| **Policy Architecture** | Flow Matching + Neural ODE Solver |
| **Flow Steps** | 默认 5 步（见 Table 2） |
| **Optimizer** | PPO-style clipped surrogate objective |
| **评估指标** | - Average Episodic Return（主指标）<br>- Training Stability（方差、崩溃情况）<br>- Wall-clock Time / Learning Efficiency<br>- Zero-noise 与 Random-noise Sampling Success Rate（fine-tuning） |

---

### 基线方法对比
- **Gaussian PPO**：标准高斯策略 baseline
- **FPO**：使用 ELBO 替代 likelihood ratio
- **GenPO**：使用 dummy action 实现精确 likelihood
- **PolicyFlow**：近似重要性采样方法

所有方法共享相同的 critic 结构、rollout 协议和环境配置。

---

## 3. 主要实验结果和性能指标

### 关键性能数据与对比结果

#### （1）IsaacLab 任务表现（图 3 & 图 11）
- **GenPO++ 在全部 8 个任务上达到最优或次优性能**，显著优于 FPO 和 PolicyFlow。
- 特别是在复杂任务如 `Humanoid` 和 `Digit-LocoManip` 上，FPO 表现出较大方差甚至训练崩溃，而 GenPO++ 保持稳定上升。
- **训练效率方面（Table 1）**：
  | Method | Training Time (min) on Humanoid |
  |--------|-------------------------------|
  | PPO | 13.25 |
  | FPO | 72.06 |
  | GenPO | 132.30 |
  | **GenPO++** | **20.78** |

  → GenPO++ 的训练时间仅为 GenPO 的约 **1/6**，接近 PPO 水平，远快于其他生成式策略方法。

#### （2）Robomimic 微调任务（图 5）
- 在三个操控任务上，GenPO++ 均能有效提升预训练策略的表现：
  - `CAN`：保持 high zero-noise 性能的同时提升随机策略鲁棒性
  - `BOX`：快速收敛至高性能
  - `THREADING`：最终成功率最高，尤其在 random-noise 下优势明显
- 表明 **精确的 likelihood ratio 有助于更稳定的策略改进**。

#### （3）真实世界部署（图 6 & 图 7）
- 成功将 GenPO++ 策略部署到 **RobotEra Xhand** 灵巧手上，完成多种几何形状螺栓的拆卸任务（图 13）。
- 在仅有本体感知（proprioception）输入、无接触信号或物体位姿的情况下仍具鲁棒性。
- 模拟训练中引入的 domain randomization 和 GenPO++ 的表达能力共同支撑了 sim-to-real 成功。

---

### 消融实验结果（图 4 & 图 9）

#### （1）历史系数 $\theta$ 的影响（图 4）
- 测试不同 $\theta \in [0.5, 0.85]$ 对 `Humanoid` 任务的影响。
- 结果显示 GenPO++ 在较宽范围内性能稳定，说明对超参不敏感。
- 当 $\theta$ 接近 1 时可能因偏离原始 flow 轨迹而导致性能下降（理论分析见 Appendix D）。

#### （2）Flow Steps 数量的影响（图 9）
- 在 `G1-Rough` 上测试不同 flow steps（5, 8, 16）。
- 发现适度步数（如 5）即可取得良好性能，增加步数并未带来单调提升，反而增加内存和梯度计算负担（类似 BPTT 效应）。

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **精确的 likelihood ratio 对 on-policy 生成式策略至关重要**：避免 ELBO 偏差带来的训练不稳定。
2. ✅ **无需 dummy action 也能实现精确可逆性**：利用 ODE solver 的历史状态作为辅助变量，是一种更优雅、高效的解决方案。
3. ✅ **Jacobian-free likelihood computation 显著提升效率**：log-det 由固定系数决定，避免反复计算神经网络 Jacobian。
4. ✅ **GenPO++ 在表达力、稳定性、效率之间取得了良好平衡**：既保留了 flow policy 的多模态建模能力，又具备类似 PPO 的训练效率。

---

### 方法的局限性
- **引入超参数 $\theta$**：需要手动调节历史修正强度；过大可能导致轨迹失真，过小则影响数值稳定性。
- **局限于 deterministic flow policy**：目前未直接支持随机扩散过程（stochastic diffusion）。
- **对 solver order 敏感**：当前基于二阶风格设计，更高阶扩展尚待研究。

---

### 未来工作方向
- 设计 **自适应调整 $\theta$ 的机制**，根据策略变化动态控制历史修正强度。
- 将 GenPO++ 扩展至 **更高阶可逆求解器** 或 **implicit solver** 以进一步提高精度。
- 探索与其他生成模型（如 rectified flow, stochastic interpolants）结合的可能性。
- 应用于更大规模的 real-world 多任务 manipulation 和 mobile manipulation 场景。

--- 

> **一句话总结**：  
> **GenPO++ 通过将 ODE 求解器的历史状态作为隐式记忆，构建了一个无需 dummy action、无需显式 Jacobian 计算、却能实现精确 likelihood ratio 的可逆 flow policy 框架，在性能、效率和稳定性上全面超越现有生成式 on-policy RL 方法。**

</details>

---

### 10. [$\alpha$-PFN: Fast Entropy Search via In-Context Learning](https://arxiv.org/abs/2606.07134)

**Authors**: Herilalaina Rakotoarison, Steven Adriaensen, Tom Viering, Carl Hvarfner, Samuel M\"uller, Frank Hutter, Eytan Bakshy  
**Category**: cs.LG  
**Published**: 2026-06-08  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2606.07134v1  

#### Abstract
Information-theoretic acquisition functions such as Entropy Search (ES) offer a principled exploration-exploitation framework for Bayesian optimization (BO). However, their practical implementation relies on complicated and slow approximations, i.e., a Monte Carlo estimation of the information gain....

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：$\alpha$-PFN: Fast Entropy Search via In-Context Learning

---

## 1. 论文的主要贡献和创新点

### ✅ 解决了什么问题
传统的 **Entropy Search (ES)** 及其变体（如 **PES**、**MES**、**JES**）是基于信息论的 **acquisition function**，在 **Bayesian Optimization (BO)** 中具有理论优势，能够实现非短视（non-myopic）、噪声鲁棒的全局优化。然而，这些方法依赖复杂的 **Monte Carlo 采样** 和手工设计的近似方案，导致：

- 计算开销大，运行缓慢；
- 数值不稳定，易引入误差；
- 难以扩展到高吞吐或大规模场景。

这限制了它们在实际应用中的广泛使用。

---

### ✅ 提出了什么新方法或新思路
本文提出 **$\alpha$-PFN**（alpha-Prior-data Fitted Network），一种通过 **In-Context Learning** 快速近似 Entropy Search 的两阶段 **amortization** 策略：

1. **第一阶段：训练 Base-PFN**
   - 一个 **Prior-data Fitted Network (PFN)** 被训练为条件模型，能预测后验分布 $p(y|x, D_{\text{trn}}, I)$，其中 $I$ 是关于最优解的信息（如 $x^*$、$f^*$ 或两者）。
   - 该模型学会在给定最优位置/值条件下进行贝叶斯推断。

2. **第二阶段：训练 $\alpha$-PFN**
   - 利用 Base-PFN 生成“真实”的信息增益目标（information gain），训练另一个 PFN 直接输出 acquisition value。
   - $\alpha$-PFN 学习的是期望信息增益的分布，其均值即为 PES/MES/JES 的 acquisition 函数。
   - 推理时仅需一次前向传播即可完成 acquisition 评估，无需任何采样。

> 💡 核心思想：将原本需要多次 MC 采样的复杂计算过程，“蒸馏”进一个可快速推理的神经网络中。

---

### ✅ 相比现有方法的优势
| 维度 | 传统 ES 方法（PES/MES/JES） | $\alpha$-PFN |
|------|-------------------------------|--------------|
| **计算效率** | 依赖大量 MC 采样，慢（分钟级） | 单次前向传播，快（秒级） |
| **实现复杂度** | 手工设计近似，代码复杂 | 端到端学习，模块化 |
| **可扩展性** | 难以处理高维、大数据量 | 支持 up to 16D 和 100 次迭代 |
| **Fully Bayesian 兼容性** | 需对超参数再采样，额外开销 | 天然支持，训练时集成超参数不确定性 |
| **泛化能力** | 固定先验假设强 | 可适配不同 prior（理论上） |

> ⚡ 最大优势：**加速超过 50x，最高达 72x**，同时保持与 state-of-the-art ES 方法相当甚至更优的优化性能。

---

## 2. 核心实验方法和设置

### 📚 使用的数据集
实验覆盖两类典型 BO 场景：

#### （1）合成函数（Synthetic Functions）
- Branin (2D)
- Hartmann (4D, 6D)
- Ackley (5D, 8D)

#### （2）真实世界 HPO 任务
- **LCBench**：7D 超参优化任务（car, FashionMNIST, MiniBooNE, higgs, segment）
- **HPO-B**（FixedHPO-B 版本）：8D–16D 黑盒优化搜索空间（ID=5527, 5891, 7609, 5965, 5971）

> 注：所有任务均为黑箱函数优化，目标是最小化 inference regret 或最大化最终性能。

---

### 🔧 实验设置和评估指标

| 设置项 | 描述 |
|-------|------|
| **初始设计** | $d$ 个均匀采样点（$d$: 维度） |
| **BO 迭代次数** | 合成函数：100 次；HPO-B：50 次 |
| **重复次数** | 合成函数 & LCBench：30 seeds；HPO-B：5 seeds |
| **评估指标** | - **Inference Regret**: $f(x^*) - f(\hat{x}^*)$，越低越好<br>- **Accuracy / Best Performance**（LCBench）：越高越好<br>- **Average Rank**（HPO-B）：跨 seed 的平均排名，越低越好 |
| **硬件环境** | 使用 BoTorch 的 `optimize_acqf` 进行 acquisition 优化 |

---

### 🆚 基线方法对比
| 方法 | 类型 | 是否 Fully Bayesian |
|------|------|---------------------|
| **GP-MCMC + JES** | Ground truth ES 实现 | ✅（NUTS 采样） |
| **GP-MCMC + MES-GIBBON** | MES 变种，支持并行查询 | ✅ |
| **GP-MCMC + PES** | 经典 PES 实现 | ✅ |
| **EI (Expected Improvement)** | 经典 myopic 方法 | ❌（作为参考） |

> 所有 GP 基线均来自 **BoTorch** 库，并采用相同 GP prior 以便公平比较。

---

## 3. 主要实验结果和性能指标

### 📊 关键性能数据（见 Table 1 及 Figure 3）

#### （1）优化性能（Optimization Quality）
- 在大多数任务上，$\alpha$-PFN 与对应的 GP-MCMC 基线表现 **相当甚至更好**：
  - 在 **LCBench** 上，JES-$\alpha$-PFN 表现最稳定，尤其在 Higgs 上优于基线。
  - 在 **Ackley 5D** 和 **Hartmann 6D** 上，所有 $\alpha$-PFN 变体均优于 GP。
  - 在 **HPO-B** 上，虽然部分任务略逊于 GP（如 MES-$\alpha$-PFN），但总体排名接近。

> ✅ 结论：$\alpha$-PFN **没有显著性能损失**，且在某些任务上有提升。

#### （2）计算效率（Runtime Speedup）
| 方法 | 平均加速倍数（Speedup ×） | 最高可达 |
|------|--------------------------|---------|
| MES-$\alpha$-PFN | 2.4x – 31.3x | 65x |
| JES-$\alpha$-PFN | 4.0x – 37.6x | 58.7x |
| PES-$\alpha$-PFN | 5.0x – 31.5x | **72.4x** |

> 🔥 在 HPO-B 的高维任务中，普遍实现 **>30x 加速**，最大达 **72.4x**。

#### （3）消融实验结果（Ablation Studies）

##### ✅ **Trace Generation Ablation**（图 5）
- 对比两种训练数据生成方式：
  - **Uniform Sampling**：上下文点随机分布
  - **Clustered Traces**（Algorithm 1）：模拟真实 BO 轨迹，点聚集在局部最优附近
- 发现：随着维度增加（如 8D Ackley），**clustered traces 显著提升性能**
- 结论：**训练分布需贴近推理时的实际 BO 行为**，否则存在 domain shift 问题

##### ✅ **Noise Robustness Ablation**（图 4）
- 测试 OOD（out-of-distribution）噪声场景：训练噪声 $\sigma_n=0.316$，测试时设为 $\sigma_n=0.5$
- 结果：$\alpha$-PFN 与 GP 基线 **退化趋势一致**，无额外失败模式
- 结论：$\alpha$-PFN 对噪声具有一定鲁棒性，未因学习而过度拟合训练分布

##### ✅ **Qualitative Comparison**（图 6）
- 在 1D 设置下可视化 JES acquisition：
  - $\alpha$-PFN 输出平滑、稳定
  - MC-based 方法因采样方差导致估计波动大
- 结论：$\alpha$-PFN 学会了对 MC 噪声进行建模与平均，提供更可靠的 acquisition 曲面

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **$\alpha$-PFN 成功实现了 Entropy Search 的高效替代**：
   - 通过两阶段 amortization，将复杂的 MC 采样过程压缩为单次前向传播。
   - 在多个 benchmark 上达到与 GP-MCMC 相当甚至更优的优化性能。

2. **极致的速度提升使其适用于高吞吐 BO 场景**：
   - 加速 **>50x**，使得原本不实用的 JES/PES 等方法变得可行。
   - 尤其适合在线、实时、资源受限的应用。

3. **天然支持 Fully Bayesian Setting**：
   - 训练时即可集成超参数不确定性，避免推理时重复采样。
   - 比传统方法更“贝叶斯”。

4. **训练策略至关重要**：
   - 使用 **clustered trace generation** 显著缓解 domain shift，提升高维泛化能力。

---

### ⚠️ 局限性
1. **一次性训练成本高**：
   - 需预训练 Base-PFN 和三个 $\alpha$-PFN 模型，总耗时约 **52 H200 GPU-hours + 192 L40S GPU-hours**。
   - 不适合频繁更换 prior 的场景。

2. **泛化依赖 prior 匹配**：
   - 当测试函数严重偏离训练 prior 时（如极高噪声、非平稳函数），性能可能下降。
   - 当前模型仅训练至 6D，却成功外推至 16D，说明有一定泛化能力，但仍有限。

3. **无法灵活切换 acquisition function**：
   - 每个 $\alpha$-PFN 模型专用于一种 ES 变体（PES/MES/JES），不能动态切换。

---

### 🔮 未来工作方向
1. **开发通用 prior 或自适应 prior 的 PFN 架构**  
   → 如结合 Whittle et al. (2026) 的 **Distribution Transformers** 实现 on-the-fly prior adaptation。

2. **扩展至其他 Monte Carlo-based acquisition functions**  
   → 如 q-EI、Thompson Sampling、BO by GIBBON 等。

3. **更大规模训练（更高维、更多 context size）**  
   → 已有研究表明 PFN 可扩展至 500D（Yu et al., 2026），值得探索。

4. **轻量化部署与边缘计算集成**  
   → 利用其快速推理特性，推动 BO 在移动端、嵌入式系统中的应用。

5. **安全 BO、约束优化等扩展场景**  
   → 探索如何将 safety constraints 编码进 PFN 输入中。

---

## 总结一句话
> $\alpha$-PFN 将原本缓慢复杂的 Entropy Search **“编译”成了一个快速神经网络**，实现了 **速度提升 >50x 且性能不降**，为信息论 BO 方法的大规模落地提供了全新路径。

</details>

---

### 11. [TA-RAG: Tone-Aware Retrieval-Augmented Generation for Peer-Support Health Communication](https://arxiv.org/abs/2606.06794)

**Authors**: Yong-Bin Kang, Anthony McCosker  
**Category**: cs.CL  
**Published**: 2026-06-08  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2606.06794v1  

#### Abstract
Retrieval-augmented generation (RAG) successfully grounds large language model (LLM) outputs in trusted documents, but factual grounding alone is insufficient for sensitive peer-support health communication. In domains such as HIV peer support, responses must also be accessible, stigma-free, empathe...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：TA-RAG: Tone-Aware Retrieval-Augmented Generation for Peer-Support Health Communication

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
传统的 **Retrieval-Augmented Generation (RAG)** 虽然能通过检索可信文档生成事实准确的回答，但在**敏感的健康领域（如HIV同伴支持）中存在明显不足**。这些系统通常只关注**相关性和事实性**，而忽略了回应的**语调（tone）**，可能导致输出显得冷漠、技术化、带有污名化语言或缺乏共情，从而影响用户的信任感、理解力和情感接受度。

在同伴支持场景中，沟通不仅是信息传递，更是情感支持的过程，因此需要响应具备：
- 无污名化（stigma-free）
- 可读性强（readable）
- 面向特定受众（recipient-appropriate）
- 富有同理心（empathetic）

### 提出了什么新方法或新思路
本文提出 **TA-RAG（Tone-Aware RAG）**，一种轻量级、基于 prompt 的 RAG 框架，将“语调控制”显式嵌入到生成流程中，无需对 LLM 进行微调。

其核心创新在于：
- 将“tone”操作化为四个可独立控制的模块：
  1. **Stigma-free rewriting (Cstig)**：依据 UNAIDS 术语指南替换污名化表达。
  2. **Readability adjustment (CRead)**：调整语言复杂度至目标可读水平（如八年级）。
  3. **Recipient adaptation (CReci)**：根据接收者身份（如同伴支持者 vs 政策制定者）调整语气风格。
  4. **Empathy rephrasing (CEmph)**：增强对用户情绪的关注与共情表达。
- 在标准 RAG 流程后增加一个 **tone adjustment layer**，采用顺序式 prompt-based 重写机制。
- 整个框架是**模块化、无需训练、易于部署于资源有限社区组织**的设计。

### 相比现有方法的优势
| 维度 | 传统 RAG | TA-RAG |
|------|--------|-------|
| 事实性 | ✅ 强 | ✅ 强 |
| 语调控制 | ❌ 缺乏 | ✅ 显式建模四维 tone |
| 可解释性 | 中等 | 高（每步可控） |
| 实现成本 | 低 | 极低（仅需 prompts + 规则） |
| 适用场景 | 通用问答 | 敏感健康沟通（如 HIV 同伴支持） |

> ✅ **优势总结**：TA-RAG 在不牺牲事实性的前提下，显著提升了健康对话中的社会适宜性、安全性和支持性，且实现方式轻量、灵活、可扩展。

---

## 2. 核心实验方法和设置

### 使用的数据集
| 组件 | 数据来源 | 描述 |
|------|---------|------|
| **整体 RAG Corpus C** | [HOLA Quality of Life Report](https://napwha.org.au/ausqol/) | 澳大利亚 HIV 患者生活质量报告，作为知识源 |
| **Cstig 评估数据 Dstig** | 基于 UNAIDS Terminology Guidelines [22] 自动生成 | 包含 105 条规则，每条生成 5 句含禁用词句子，共 525 条样本 |
| **CRead / CReci 评估数据 S** | 从 HOLA 文档自动生成 | 100 个问题及其原始回答，用于测试可读性与受众适配 |
| **CEmph 评估数据** | Empathy in Text-based Mental Health Support Dataset | 选取 100 条高共情 Reddit 回应，并由 LLM 生成对应的非共情版本作为输入 |

### 实验设置
- **模型**：默认使用 `gpt-4o-mini` 作为 backbone LLM。
- **评估方式**：**组件级测试（component-level evaluation）**，分别验证每个 tone 控制模块的有效性。
- **流程**：
  1. 先生成基础 RAG 回答（draft）
  2. 依次应用 Cstig → CRead → CReci → CEmph
  3. 对比处理前后在目标维度上的提升及语义保留情况

### 评估指标
| 模块 | 主要指标 | 辅助指标（语义保持） |
|------|--------|------------------|
| **Cstig** | ReplaceRate（正确替换比例） | SemSim（语义相似度）、ContPreserve（BERTScore Recall） |
| **CRead** | Flesch-Kincaid Grade Level、Zero-shot ARA（自动可读性评分） | SemSim、ContPreserve |
| **CReci** | PeerAlign（LLM-as-rater 打分，基于 NAPWHA 标准） | SemSim、ContPreserve |
| **CEmph** | EmScore（LLM-as-rater 对共情打分） | SemSim、ContPreserve、MRL（相对长度变化） |

> 📌 注：所有 prompts 和评估数据将在论文被接受后开源至 GitHub。

---

## 3. 主要实验结果和性能指标

### 关键性能数据汇总

| 模块 | 性能提升 | 语义保持 |
|------|--------|----------|
| **Cstig** | ReplaceRate = **0.89** | SemSim = **0.89**, ContPreserve = **0.98** |
| **CRead** | FK ↓ from 17.1 → 11.5<br>ARA ↓ from 3.4 → 2.2（达初中水平） | SemSim = **0.94**, ContPreserve = **0.94** |
| **CReci** | 平均 PeerAlign ↑ from **3.54 → 4.42**（+0.88）<br>最高达 Qwen: 2.86 → 4.56 | SemSim = **0.82**, Recall = **0.93** |
| **CEmph** | 平均 EmScore ↑ from **1.74 → 4.79**（+3.05）<br>最大提升超 3 分 | Recall = **0.86**, SemSim = **0.52**（因扩展较多） |

### 与基线方法的对比结果
- **无显式 tone 控制的 RAG** 作为 baseline，在以下方面表现较差：
  - 使用过时/标签化术语（如 “HIV patients” 而非 “people living with HIV”）
  - 可读性过高（平均 FK=17.1，相当于大学以上水平）
  - 缺乏共情表达（平均 EmScore < 2）
  - 不符合同伴支持交流规范（PeerAlign ≈ 3.5）

- TA-RAG 各模块均带来**显著改进**，尤其在 **empathy 提升上效果最突出（+3.05）**，说明 prompt-based 共情重构有效。

### 消融实验结果（隐含分析）
虽然未进行正式消融实验，但作者通过对不同模块输出的分析揭示了以下规律：
- **局部编辑型模块**（Cstig, CRead）：
  - 改动小，语义保留强（SemSim > 0.89）
  - MRL 变化小（~ ±0.1）
- **生成型模块**（CReci, CEmph）：
  - 改动大，引入更多风格转换和内容扩展
  - CEmph 的 MRL 增加 **1.69±2.23**，导致 SemSim 下降（r = -0.59），但关键概念仍保留（Recall=0.86）

> 🔍 发现：**越具创造性的 tone 调整，语义相似度越低，但内容保留仍较高**，表明 BERTScore Recall 更适合衡量此类任务的内容一致性。

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **Prompt-based tone control 是可行且有效的**：无需 fine-tuning 即可在 RAG 中实现多维度语调调控。
2. ✅ **四类 tone 组件均能显著改善对应通信质量**，同时**保持关键内容不变**（ContPreserve ≥ 0.86）。
3. ✅ **Empathy 和 recipient adaptation 的提升空间最大**，也最能体现 TA-RAG 的价值。
4. ⚠️ **公式类可读性指标（如 FK）在医疗文本中可能失真**：因医学术语多音节，即使简化后 FK 仍偏高；建议结合 LLM-based ARA 使用。
5. 🔁 **tone adjustment 的顺序设计合理**：先去污名 → 再简化 → 适配受众 → 最后加共情，确保最终输出的情感基调不受早期修改破坏。

### 方法的局限性
- **依赖高质量规则和指南**：如 Gs（UNAIDS）、Gp（NAPWHA）的质量直接影响 Cstig 和 CReci 效果。
- **LLM-as-rater 存在校准偏差**：不同 evaluator 模型打分范围不同（如 Qwen 初始仅 1.22），需谨慎解读绝对分数。
- **未进行端到端人类用户研究**：当前仅为组件级验证，尚未在真实 peer supporter 或患者群体中测试可用性。
- **顺序固定，缺乏动态调节机制**：tr（可读阈值）、te（共情阈值）需手动设定，未来可考虑反馈驱动优化。

### 未来工作方向
1. **开展 end-to-end 用户研究**：与 trained peer supporters 合作，在真实场景中评估 TA-RAG 输出的接受度和支持效果。
2. **探索 adaptive tone routing**：根据用户历史行为或情绪状态动态选择 tone 组件组合。
3. **集成多模态输入**：结合语音语调、文本情感等信号进一步优化 tone 生成。
4. **扩展至其他敏感健康领域**：如 mental health、addiction recovery、LGBTQ+ health 等，验证泛化能力。

---

> ✅ **总体评价**：TA-RAG 是首个系统性将“语调”纳入 RAG 设计的轻量框架，为构建**安全、包容、富有支持性的 AI 健康助手**提供了重要范式，具有较强的实践意义和社会价值。

</details>

---

### 12. [Making the Most of Limited Data: Score-Aware Training for Text-to-Music Generation](https://arxiv.org/abs/2606.07387)

**Authors**: Yun-Chen Cheng, Tzu-Hung Huang, Chih-Pin Tan  
**Category**: cs.LG  
**Published**: 2026-06-08  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2606.07387v1  

#### Abstract
State-of-the-art text-to-music generation systems rely on massive proprietary datasets and industrial-scale compute, making it impossible to disentangle architectural contributions from resource advantages. We propose \textit{score-aware training}, which treats audio-caption alignment score as a dir...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Making the Most of Limited Data: Score-Aware Training for Text-to-Music Generation*

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
当前最先进的 **text-to-music generation**（TTM）系统严重依赖大规模专有数据集和工业级算力，导致学术界难以复现或区分模型架构改进与资源差异带来的性能提升。本文在 **ICME 2026 ATTM Grand Challenge** 的约束条件下（固定数据源、≤500M 参数），探索如何在有限数据下最大化训练效率。

核心挑战包括：
- 数据中音频-文本对齐质量参差不齐；
- 训练时使用的信息密集型 caption 与推理时简洁 prompt 存在分布差距；
- 小规模数据易导致过拟合。

---

### 🚀 提出的新方法：Score-Aware Training 框架

作者提出一种以 **caption alignment score** 为核心信号的全流程训练策略，包含四个互补组件：

#### （1）Segment-Level Filtering（段级过滤）
- 使用 **CLAP score** 对每个音频片段进行打分；
- 设定阈值将片段分为高、中、低三档，丢弃低分段（score < 0.2）；
- 每个文件保留6个高质量段落，优先选择高分段。

> ✅ 动机：去除严重错位样本，避免污染训练信号。

#### （2）CLAP-Conditioned Beta Noise Timestep Schedule（基于 CLAP 分数的噪声调度）
- 在 **flow matching** 中，不再均匀采样噪声时间步 $ t \sim U[0,1] $；
- 改为使用 **Beta 分布** $ P(t|S) = \text{Beta}(t; \alpha(S), \beta(S)) $，其中：
  - $ \alpha(S) = 1 + \lambda(1 - S) $，$ \lambda=1.0 $
  - 高分样本 → 接近 uniform 分布（全阶段学习）
  - 低分样本 → 偏向高噪声阶段（$ t \to 1 $），仅用于粗粒度语义建模

> ✅ 动机：低质量数据仍可作为“隐式正则化器”，防止过拟合，且不影响精细音质生成。

#### （3）Two-Stage Caption Procedure（两阶段文本训练）
- **Stage 1（Pretrain）**：使用信息密集的原始 caption（含 BPM、调式、结构等）建立音乐理解；
- **Stage 2（Fine-tune）**：用 LLM 将 caption 重写为简洁风格（只保留 genre/instrument/mood），匹配推理时输入格式。

> ✅ 动机：缓解训练-推理间的 **distribution gap**，提升实际 prompt 下的表现。

#### （4）REPA Auxiliary Loss（表示对齐损失）
- 引入 **Representation Alignment (REPA)** 辅助损失，从预训练模型中迁移语义知识：
  - **CLAP REPA**：对齐全局音频-文本语义空间；
  - **MuQ REPA**：对齐音乐细粒度特征（如音色、乐器）；
- 不引入额外训练数据，仅通过冻结编码器提供监督信号。

> ✅ 动机：利用已有大规模判别模型的知识，增强生成模型的表示能力。

---

### 🔍 相比现有方法的优势
| 方面 | 传统做法 | 本文方法 |
|------|----------|-----------|
| 数据利用 | 统一处理所有样本 | 根据 CLAP score 差异化处理 |
| 噪声调度 | 固定或均匀采样 | 动态调整，低分样本导向 high-noise regime |
| 文本条件 | 单一 caption 格式 | 两阶段训练桥接分布鸿沟 |
| 表示学习 | 端到端从零学习 | 利用 CLAP/MuQ 进行知识蒸馏 |

> 💡 核心思想：**不是更多数据，而是更聪明地使用数据。**

---

## 2. 核心实验方法和设置

### 📚 数据集
- 主要使用 **MTG-Jamendo dataset** 的一个 CC-license 子集（由 ICME 2026 ATTM Challenge 提供）；
- 包含约 5,500 条带标签音乐片段；
- 验证集：1,000 个样本，每条随机抽取 10 秒段落计算 CLAP score。

---

### ⚙️ 实验设置
- **模型架构**：基于 **FluxAudio** 的 Diffusion Transformer（DiT），采用 conditional flow matching；
- **Latent Codec**：使用冻结的 **ACEStep 1.5** 编码器将 48kHz 波形压缩为 25Hz 的连续 latent；
- **参数量**：最终模型约 **450M 可训练参数**，符合 Efficiency Track 要求；
- **双文本条件输入**：
  - **T5 encoder**：提供 token-level 序列表示（cross-attention）
  - **CLAP encoder**：提供 global semantic embedding（adaptive layer norm）

---

### 📊 评估指标
| 指标 | 含义 | 趋势 |
|------|------|-------|
| **CLAP Score** | 生成音频与文本描述之间的语义相似度（越高越好 ↑） |
| **FAD** (Frechet Audio Distance) | 生成音频与真实音频在 CLAP 特征空间的距离（越低越好 ↓） |
| **CCS** (Content Consistency Score) | 多次生成的一致性度量（越高越好 ↑） |
| **MOS** (Mean Opinion Score) | 专家主观评分（Audio Quality, Musicality, Prompt Adherence） |

---

### 🔁 基线方法对比
- 官方 Baseline（未明确细节，但同赛道其他队伍参与比较）；
- 自建 Base Model（关闭所有 score-aware 组件）；
- 多种消融配置（见下文）；

> 所有模型均从头训练，无外部数据注入。

---

## 3. 主要实验结果和性能指标

### 📈 客观评价结果（Objective Phase）
| 模型（Setting 1） | CLAP Score | FAD | CCS |
|------------------|------------|-----|-----|
| 本文提交模型 | **0.295** | **0.495** | **0.804** |

👉 在客观评估中 **排名第二**（两个赛道总评），显著优于多数基线。

---

### 👂 主观评价结果（Human Evaluation / MOS）
| 指标 | 得分 |
|------|------|
| **MOS_all** | 3.119 |
| **MOS_expert** | 3.044 |

👉 在 **Efficiency Track** 的主观测试中 **排名第三**。

---

### 🔍 消融实验结果（Ablation Study on Smaller Scale）

> 使用 FluxAudio-S 在 2,000 训练样本上训练 20k 步，验证集 100 样本。

| 配置 | CLAP Score ↑ | FAD ↓ | 说明 |
|------|-------------|--------|------|
| Base（全关） | 0.2755 | 0.2856 | 基线严重过拟合 |
| + CLAP REPA (normal) | **0.2930** | **0.2767** | 显著提升对齐与泛化 |
| + CLAP REPA (aggressive) | 0.2890 | 0.2620 | FAD 更优，CLAP 略降 |
| + MuQ REPA | 0.1921 | 0.5864 | 性能下降，收敛慢 |
| + Beta Schedule (λ=0.2) | 0.2788 | 0.2941 | 小幅提升 CLAP |
| + Beta Schedule (λ=1.0) | 0.2746 | 0.2902 | 泛化更好，训练更稳 |
| + Beta Schedule (λ=2.0) | 0.2587 | 0.2995 | 过于激进，损害性能 |

#### 关键发现：
- **CLAP REPA** 是最有效的单一改进（+0.018 CLAP），兼具正则化效果；
- **Beta Noise Schedule** 明显抑制过拟合（验证 loss 下降 ~0.1），是强隐式正则化；
- **MuQ REPA** 理论合理但需更长训练周期，在短训中表现不佳；
- **Caption Rewriting Fine-tuning** 提升 CLAP score +0.013，有效弥合分布差距。

---

## 4. 关键结论和发现

### ✅ 主要结论
1. **数据质量管理比数据数量更重要**：即使在小数据场景下，通过精细化管理样本质量（filtering + score-aware scheduling），也能取得接近工业级系统的性能。
2. **Score-Aware Training 是高效训练的关键范式**：
   - 利用 CLAP score 作为统一质量信号，贯穿 filtering、noise scheduling、representation learning；
   - 实现“劣质数据再利用”而非简单丢弃。
3. **REPA 显著提升语义对齐能力**：
   - CLAP REPA 成功迁移预训练语义知识，提升 CLAP score 并降低 FAD；
   - 证明 representation alignment 是小数据下的有效策略。
4. **两阶段 caption 训练桥接了训练-推理鸿沟**：
   - 先学细节，再适配简洁 prompt，兼顾知识积累与实用性能。

---

### ⚠️ 局限性
1. **MuQ REPA 未能充分发挥作用**：
   - 因训练周期不足未完全收敛；
   - 当前评估指标（如 CLAP）无法充分反映其对 timbre/instrumentation 的增益。
2. **CLAP Score 的局限性**：
   - 作为 alignment proxy 可能存在偏差，不能完全代表人类感知；
   - 未来可结合多种 score（如 MuQ、human annotation）构建多维质量信号。
3. **Beta Schedule 超参数敏感**：
   - λ 设置影响大，最佳值（λ=0.2）与最终选用（λ=1.0）不一致，因工程延迟未能更新。

---

### 🔮 未来工作方向
1. **延长 MuQ REPA 训练周期**，验证其长期收益；
2. **扩展 Score-Aware 框架至其他信号**：如 human ratings、diversity scores、acoustic clarity；
3. **动态调整 filtering threshold 和 noise schedule**，实现在线质量估计与自适应训练；
4. **探索多模态 feedback loops**：让生成结果反哺 caption 重写或数据清洗。

---

## 总结

> 🏁 本文展示了在 **有限数据与算力限制下**，如何通过 **score-aware training** 框架实现高性能 text-to-music generation。其核心在于将 **数据质量信号（CLAP score）融入整个训练流程**，实现了对低质量数据的有效利用、对齐误差的控制以及训练动态的优化。最终模型在 ICME 2026 ATTM Challenge 中取得优异成绩，证明了 **算法设计 > 资源堆砌** 的可行性路径。

</details>

---

### 13. [Drifting Models for Surrogate Flow Modeling](https://arxiv.org/abs/2606.07481)

**Authors**: Chris R. Jung, Markus D\"orr, Natalie J\"ungling, Jennifer Niessner, Adam T. M\"uller, Nicolaj C. Stache  
**Category**: cs.LG  
**Published**: 2026-06-08  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2606.07481v1  

#### Abstract
While Computational Fluid Dynamics (CFD) provides high-fidelity flow fields for optimizing indoor environments, its computational cost limits rapid exploration. To solve this problem generative surrogates offer better distribution modeling than deterministic networks, but iterative sampling is slow....

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Drifting Models for Surrogate Flow Modeling*

---

## 1. 论文的主要贡献和创新点

### 解决的问题
传统 **Computational Fluid Dynamics (CFD)** 虽然能提供高保真度的室内气流场预测，但其计算成本高昂，难以支持快速设计探索或实时通风控制。现有的数据驱动 surrogate 模型中：
- **确定性模型**（如 FNO）推理快，但倾向于输出平滑的期望值，无法捕捉复杂的多模态流动分布；
- **生成式模型**（如 diffusion models）虽能建模复杂物理分布，但依赖迭代采样（multi-step sampling），推理速度慢。

因此，亟需一种既能保持高精度、又能实现**单步快速生成**的 CFD surrogate 方法。

### 提出的新方法与创新思路
本文首次将新兴的 **generative drifting 框架**引入流体力学领域，并提出以下三项关键技术改进：

1. **Latent-space drifting via a learned VAE**  
   在一个由 VAE 学习得到的紧凑 latent space 中进行 drifting，而非原始像素空间。这提升了生成质量并避免了预训练特征不匹配问题。

2. **Label-aware positive masking**  
   针对混合边界条件的 batch 数据，引入二值兼容性掩码，确保生成样本仅向“相同 inlet/outlet/geometry”配置的真实样本靠拢，防止不同流态间的错误平均。

3. **Spatial-conditioning variant**  
   提出两种 conditioning 方式：
   - **Label-based**: 使用离散 ID 编码入口/出口位置，适用于固定配置；
   - **Spatial**: 使用三通道 binary mask 显式编码几何布局（inlet, outlet, obstacles），具备泛化到未见房间结构的潜力。

### 相比现有方法的优势
- **推理速度快两个数量级**：相比需要 1000 步采样的 Latent Diffusion Model（LDM），drifting 模型仅需 **NFE=1** 单步前传；
- **精度接近 diffusion 模型**：在 field accuracy 和 flow consistency 上表现优异，尤其 label-based variant 几乎达到 diffusion 基线水平；
- **结构一致性好**：在 vorticity 和 divergence 等物理量上偏差小，保留了关键流动结构；
- **具备泛化潜力**：spatial-conditioning 设计为未来处理任意几何提供了可行路径。

---

## 2. 核心实验方法和设置

### 数据集
- 共 **2,025 组二维稳态 CFD 模拟数据**，使用 Simcenter STAR-CCM+ 求解器基于 RANS k-ε 湍流模型生成；
- 计算域为 1.5 m × 1.5 m 的方形房间，含一个 0.1 m 宽 inlet 和 outlet，位于对墙；
- 考察三种几何构型：
  - 无障碍空房间
  - 中心障碍物（直径 0.25 m）
  - 偏移障碍物
- 每种构型下系统扫描 15 个 inlet 位置、15 个 outlet 位置、3 种 inlet velocity（0.1, 0.2, 0.3 m/s）；
- 输出插值至 **64×64 均匀网格**，随机保留 10% 作为测试集。

### 实验设置
- **VAE 架构**：编码器将 64×64 速度场压缩为 4×4×16 latent 向量，解码器重建；
- **Backbone**：采用轻量级 **Diffusion Transformer (DiT)** 作为 drifting 网络主干；
- **Drifting field**：基于核函数的吸引-排斥机制，维护 memory bank 存储负样本；
- **Baseline**：Latent Diffusion Model（LDM），同样作用于 4×4 latent space，使用 1000 步 cosine schedule + DDIM 采样；
- **硬件平台**：NVIDIA A100-SXM4 GPU，batch size=1，测量推理延迟。

### 评估指标
分为两大类：

#### Field Accuracy（场精度）
| 指标 | 描述 |
|------|------|
| **nRMSE ↓** | Range-normalized RMSE，归一化均方根误差 |
| **R² ↑** | 决定系数，衡量解释方差比例 |
| **Cosine Similarity ↑** | 向量场方向一致性，针对非零速度区域 |

#### Flow-Structure Consistency（流动结构一致性）
| 指标 | 描述 |
|------|------|
| **Divergence Gap ↓** | 预测与真实散度之间的绝对差异 |
| **Relative Divergence** | 预测/真实散度比值，反映结构性缩放 |
| **Vorticity Gap ↓** | 涡量幅值差距 |
| **Relative Vorticity** | 涡量相对比值 |

---

## 3. 主要实验结果和性能指标

### 定量结果（来自 Table 1，基于无障碍测试数据）

| 类别 | 指标 | Diffusion (baseline) | Drifting (label) | Drifting (spatial) |
|------|------|------------------------|------------------|--------------------|
| **Field Accuracy** | nRMSE ↓ | **0.0592±0.0204** | 0.0684±0.0209 | 0.1076±0.0453 |
|                  | R² ↑    | **0.8476±0.1228** | 0.8019±0.1152 | 0.4251±0.4783 |
|                  | Cos. Sim. ↑ | **0.8108±0.0576** | 0.7772±0.0661 | 0.7846±0.1122 |
| **Flow-Struct. Consistency** | Div. Gap ↓ | 0.4503±0.0849 | **0.4224±0.0842** | 0.4680±0.3316 |
|                              | Rel. Div. | 8.0713±2.1104 | **7.5579±1.6388** | 8.2887±5.4017 |
|                              | Vort. Gap ↓ | 0.2895±0.1290 | **0.2634±0.1312** | 0.5519±0.4618 |
|                              | Rel. Vort. | 1.1635±0.0820 | **1.1449±0.0861** | 1.3127±0.2789 |

### 推理速度对比（Table 2）

| Model | Conditioning | NFE | Latency (ms) |
|-------|--------------|-----|---------------|
| Diffusion | label-based | 1000 | **1870.2 ± 77.1** |
| Drifting | label-based | 1 | **6.74 ± 0.36** |

👉 **结论**：drifting 模型推理速度比 diffusion 快约 **277 倍**（近两个数量级），且标准差极低，稳定性强。

### 定性分析（Figure 1 & 2）
- 在无障场景中，label-based drifting 成功恢复主流拓扑（主射流、角落回流区），误差分布与 diffusion 相当；
- spatial-conditioning variant 能捕捉基本流动结构（如绕柱分离、尾迹位置），但在速度尺度和旋转结构上有局部过预测现象，与较高的 relative vorticity 指标一致；
- 两种 drifting 变体在 jet 边界处均有峰值误差，推测源于 VAE 的空间压缩损失。

### 消融实验（隐含分析）
尽管未明确列出消融表，但从设计对比可看出：
- **Label-aware masking** 对混合 batch 条件至关重要，防止跨条件干扰；
- **Latent-space drifting** 是保证结构完整性的基础；
- **Spatial encoding** 虽当前性能较弱，但展示了对新几何的适应能力，是长期发展方向。

---

## 4. 关键结论和发现

### 主要发现
1. **Conditional drifting 模型可在单步内生成高质量 flow field**，其精度接近需千步迭代的 diffusion 模型；
2. **Latent-space drifting + label-aware masking 构成了高效物理条件生成的有效范式**；
3. **Label-based drifting 在精度上优于 spatial variant，但后者具备更强泛化潜力**；
4. **推理效率优势显著**：NFE=1 的结构特性使得 drifting 成为 real-time CFD surrogate 的理想选择，尤其适合需要低延迟的应用（如实时调控）；
5. 所提方法在 **divergence 和 vorticity 等物理结构诊断上表现良好**，说明其不仅拟合像素，也尊重流体动力学规律。

### 局限性
1. 当前实验局限于 **2D 稳态 flow** 和固定分辨率网格，尚未扩展至 transient 或 3D 场景；
2. **VAE 的 16× 空间压缩** 导致细节丢失，尤其是在 jet 边界等高频区域；
3. **Spatial-conditioning variant 性能下降明显**，可能由于 binary mask 表达能力有限或 encoder 不够强大；
4. 数据集规模较小（仅 2k+ 样本），限制了 kernel-based drifting field 的统计有效性；
5. 尚未与 deterministic surrogate（如 FNO）直接比较，缺乏全面基准覆盖。

### 未来工作方向
1. **优化 latent resolution 和 patch size**，缩小与 diffusion 的精度差距；
2. **增强 spatial interface**：尝试 cross-attention 或更丰富的几何编码方式（如 point clouds, meshes）；
3. **扩展至 transient 3D flows**，验证 drifting 在时空联合建模中的潜力；
4. **结合 physics-informed learning**，进一步提升物理一致性；
5. **部署于 real-time 控制闭环系统**，验证其在实际 IAQ 管理中的实用性。

---

> ✅ **总结一句话**：  
> 本文成功将 **generative drifting** 引入 CFD surrogate 建模，提出了一种高精度、单步生成、条件可控的 flow prediction 框架，在保持接近 diffusion 模型精度的同时，实现 **>100× 推理加速**，为实时流体仿真开辟了新路径。

</details>

---

### 14. [When to Think Deeply: Inhibitory Deliberation for LLM Reasoning](https://arxiv.org/abs/2606.06745)

**Authors**: Zhixuan He, Yue Feng  
**Category**: cs.CL  
**Published**: 2026-06-08  
**Score**: 6.5  
**Type**: new  
**ArXiv ID**: 2606.06745v1  

#### Abstract
Reasoning Large Language Models can improve problem-solving performance through deliberative inference, but invoking slow reasoning for every input is computationally expensive and often unnecessary. We propose IDPR, a framework for response-conditioned inhibitory deliberation. IDPR first generates ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*When to Think Deeply: Inhibitory Deliberation for LLM Reasoning*

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
当前的 **Reasoning LLM** 虽然能通过 **deliberative inference** 显著提升复杂任务（如数学推理）的表现，但始终启用慢速推理（slow reasoning）会导致极高的计算开销（token cost），且在许多简单输入上并不必要。因此，一个关键问题是：**何时应调用慢速推理？**

传统方法通常基于输入（input-only）进行路由决策（如预测问题难度），忽略了实际生成的快速答案（fast answer）本身所携带的重要信号。

### ✅ 提出的新方法：IDPR（Inhibitory Deliberative Problem Reasoning）
IDPR 是一种 **response-conditioned inhibitory deliberation** 框架，其核心思想受认知科学中的“双过程理论”启发：

- **Fast Policy** $ \mathcal{T}_f $：首先生成一个简洁、直觉性的答案 $ y_f $，作为“预优势响应”（prepotent response）。
- **Inhibition Controller**：观察问题 $ x $、快答 $ y_f $ 及其相关证据 $ c_f $（如置信度、logit margin、可解析性、生成成本等），判断是否应**抑制**该快答并转而调用慢推理。
- **Slow Policy** $ \mathcal{T}_s $：仅当控制器认为慢推理预期收益足够高时才被激活。

> 💡 **关键创新**：路由决策是 **response-conditioned** 的——不是“这个问题难不难”，而是“这个具体快答值不值得被抑制”。

### ✅ 相比现有方法的优势
| 对比维度 | 传统方法（如 FrugalGPT, RouteLLM） | IDPR |
|--------|-------------------------------|------|
| 路由依据 | 仅基于输入 $ x $ | 基于 $ x, y_f, c_f $（含快答内容与质量信号） |
| 决策粒度 | 输入级 | 响应级（fine-grained） |
| 控制机制 | 预路由（pre-routing） | 抑制控制（inhibitory control） |
| 生物学类比 | 无 | 类似人类前额叶的“反应抑制”机制 |

IDPR 更精准地识别出那些**看似合理但错误**的快答，从而实现更有针对性的慢推理调用。

---

## 2. 核心实验方法和设置

### 📚 数据集
- **GSM8K**：小学数学应用题，用于评估多步算术推理能力。
- **MoT（Mixture-of-Thoughts）中的数学子集**：更难的数学推理问题。
- 构建了一个包含 **5,000 条测试样本** 的独立 hold-out 测试集（平衡来自两个来源），另有 2,000 条验证集用于阈值校准。

### ⚙️ 实验设置
- **Fast Policy**：`Qwen2.5-Math-7B`，训练为输出简短、可解析的答案（answer-only）。
- **Slow Policy**：`OpenR1-Distill-7B`，支持 chain-of-thought 推理，生成详细解题过程后给出最终答案。
- **Inhibition Controller**：
  - 输入：$ e_f = (x, y_f, c_f) $
  - 特征 $ c_f $ 包括四类 fast-side evidence（见下表）
  - 输出三个头：预期质量增益 $ \Delta Q $、慢推理成本 $ C_s $、纠正概率 $ p_{\text{corr}} $
  - 最终切换分数（switch score）：  
    $$
    S_x = \Delta Q - \lambda_{\text{inf}} C_s
    $$
  - 若 $ S_x \geq \tau $，则抑制快答并调用慢策略。

#### Fast-side Evidence 特征类别
| 类别 | 示例特征 |
|------|---------|
| Confidence | 平均 log-probability, logit margin |
| Parseability | 答案格式、候选数量、是否可解析 |
| Generation Cost | 快答 token 数、延迟、吞吐量 |
| Degeneracy | 重复率、截断标志 |

### 📊 评估指标
| 指标 | 含义 |
|------|------|
| **Accuracy** | 主要指标，正确率 |
| **Slow Call Rate** | 调用慢推理的比例 |
| **Avg. Tokens** | 平均生成 token 数（衡量成本） |
| **Corrective Precision** | 在被路由到慢推理的例子中，快错慢对的比例（越高说明路由越精准） |
| **Cost-aware Utility** | 综合考虑准确性和成本的效用函数：  
$ U(y,x) = \sigma A(y,x) - \lambda_{\text{tok}} C(y) - \rho F(y) $ |

### 🔁 基线方法（Same-Budget Baselines）
所有基线与 IDPR 使用相同的 **8.20% 慢调用预算**：
- **Always-Fast**：始终返回快答
- **Random Same-k**：随机选择 8.20% 的样本调用慢推理
- **Low Avg LogProb Same-k**：选置信度最低（平均 log-prob 最小）的样本
- **Low Logit Gap Same-k**：选 logit margin 最小的样本

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据（Test Set, 5,000 examples）

| Method | Slow Rate | Accuracy | ▲Acc. | Utility | Avg. Tokens | Corr. Prec. |
|--------|-----------|----------|-------|---------|-------------|--------------|
| Always-Fast | 0.00% | 47.90% | — | 0.4789 | 5.26 | — |
| Random Same-k | 8.20% | 46.76% | -1.14 | 0.4517 | 517.91 | 13.41% |
| Low Avg LogProb | 8.20% | 48.22% | +0.32 | 0.4646 | 582.68 | 21.22% |
| Low Logit Gap | 8.20% | 47.84% | -0.06 | 0.4571 | 714.73 | 11.46% |
| **IDPR (Ours)** | **8.20%** | **48.92%** | **+1.02** | **0.4731** | **519.42** | **27.07%** |

> ✅ **核心结果**：在仅调用 **8.20%** 慢推理的情况下，IDPR 将准确率从 47.90% 提升至 **48.92%**（+1.02），显著优于所有基线。

### 🔍 对比分析
- **vs Random Routing**：随机调用反而降低准确率（↓1.14），说明盲目调用慢推理有害。
- **vs Confidence-based**：最强置信度基线仅达 48.22%，落后 IDPR **0.70 个百分点**。
- **Corrective Precision**：IDPR 达到 **27.07%**，远高于其他方法，表明其能更有效识别“可纠正”的错误快答。

### 🔬 消融实验结果

#### （1）按数据源拆分（Source-wise Analysis）
| Subset | Method | Acc (▲) | Slow Rate |
|--------|--------|--------|----------|
| GSM8K | Always-Fast | 60.20% | — |
|         | IDPR     | **60.96% (+0.76)** | 6.68% |
| MoT (harder) | Always-Fast | 35.60% | — |
|              | IDPR        | **36.88% (+1.28)** | 9.72% |

> ✅ IDPR 在更难的 **MoT 子集上增益更大**，且自动分配更多慢调用资源，体现其自适应性。

#### （2）控制器与快策略变体（Table 3）
| Fast Policy | Controller | Acc | Slow Rate | Corr. Prec. |
|------------|------------|-----|-----------|--------------|
| Answer-only | Deterministic-scan | **48.92%** | 8.20% | **27.07%** |
| Answer-only | Sampled-fast | 48.78% | 7.78% | 25.71% |
| GRPO-refined | Deterministic-scan | 48.74% | 8.96% | 26.12% |

> ✅ 最佳配置仍是基础版：**Answer-only Fast + Deterministic-scan Controller**，说明增益主要来自抑制控制机制本身，而非策略微调。

#### （3）阈值校准影响
- **Accuracy-first threshold**（验证集优化）：调用 8.20% → 准确率 +1.02
- **Fixed-rate threshold**：仅调用 2.10% → 准确率 +0.30
- 两者 **corrective precision 相近**（~27%），说明固定阈值“太保守”，召回不足。

> ✅ 阈值校准决定了系统的 **accuracy-cost trade-off**，是部署中的关键环节。

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **Response-conditioned inhibition 更优**：相比仅依赖输入的路由机制，结合快答及其质量信号的抑制控制能更精准识别需慢推理的案例。
2. **IDPR 实现高效增益**：以 **8.20% 的慢调用率** 实现 **+1.02% 绝对准确率提升**，且 **corrective precision 达 27.07%**，显著优于随机与置信度过滤方法。
3. **智能资源分配**：系统自动将更多慢推理资源分配给更难的问题（如 MoT），体现出自适应性。
4. **阈值决定行为模式**：控制器提供排序能力，而阈值决定实际调用量，二者共同塑造系统表现。

### ⚠️ 局限性
1. **慢推理仍昂贵**：尽管调用稀疏，但每次调用带来数百 token 开销，**cost-aware utility 低于 Always-Fast**。
2. **依赖模型对选择**：效果受限于所选 fast/slow model pair 的性能差异。
3. **需重新校准**：当模型、解码策略或数据分布变化时，抑制阈值可能需要重新调整。
4. **认知类比非生物学主张**：IDPR 是计算类比，不模拟完整的人类认知控制机制。

### 🔮 未来工作方向
1. **更强的 Fast/Slow Policies**：集成更大规模或更先进的 reasoning models。
2. **跨分布鲁棒性**：改进在分布外（OOD）任务上的泛化与校准能力。
3. **更丰富的控制器架构**：引入记忆、工具调用或多轮交互增强决策。
4. **扩展至 Agentic Reasoning**：应用于规划、行动、环境反馈等更复杂的 agent 场景。
5. **动态成本感知**：实时估计并优化 token/time/cost 多维代价。

---

> 🧠 **一句话总结**：  
> **IDPR 提出了一种类人脑的“先直觉、再抑制”机制，通过 response-conditioned 控制器智能决定“何时深入思考”，在极低慢推理调用率下实现了最有效的准确率提升，为构建高效、可控的 reasoning LLM 系统提供了新范式。**

</details>

---

### 15. [Evidence-Grounded Ensemble Diagnosis of 802.11 Packet Captures: A Multi-Stage Pipeline with Deterministic Reliability Scoring](https://arxiv.org/abs/2606.06871)

**Authors**: Jerome Henry, Swadhin Pradhan, Miroslav Popovic  
**Category**: cs.LG  
**Published**: 2026-06-08  
**Score**: 6.5  
**Type**: new  
**ArXiv ID**: 2606.06871v1  

#### Abstract
Diagnosing 802.11 packet captures requires expert protocol knowledge, is slow, inconsistent across engineers, and unscalable. LLM-based approaches sound plausible but fabricate protocol events absent from captures (especially truncated traces), produce uncalibrated confidence scores, and suffer eval...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Evidence-Grounded Ensemble Diagnosis of 802.11 Packet Captures: A Multi-Stage Pipeline with Deterministic Reliability Scoring

---

## 1. 论文的主要贡献和创新点

### 解决的问题
该论文针对 **802.11 packet capture**（PCAP）诊断中存在的三大典型失败模式，提出了一种系统性解决方案：

1. **幻觉完成（Hallucinated Completion）**  
   当捕获不完整（如握手过程被截断），LLM 常常虚构并不存在的协议事件（例如推断“密码错误”导致失败），从而产生误诊。

2. **置信度未校准（Uncalibrated Confidence）**  
   LLM 自我报告的置信度高度集中于 0.95 左右（71% 的案例精确为 0.95），无法反映真实诊断难度，因此不具备决策参考价值。

3. **黄金参考偏见（Golden Reference Bias）**  
   若黄金参考（golden reference）由同一 LLM 协助生成，则评估时会偏向该模型的表达风格，而非诊断正确性，造成循环偏见。

---

### 提出的新方法：PROBE 管道
作者提出了 **PROBE**（Protocol Reasoning Over evidence-Based Ensembles），一个五阶段多级诊断管道，其核心创新包括：

#### （1）确定性的 PCAP 到文本归一化（PCAP-to-text Normalization）
- 将二进制 PCAP 转换为结构化、可验证的文本表示（基于 PDML）。
- 保留帧号、时间戳、协议类型、状态码、RSSI、EAPOL 握手状态等关键字段。
- 所有 LLM 输出均可通过帧号进行机械验证，实现 **frame-level verifiability**。

#### （2）多运行、多候选集成（Multi-run, Multi-candidate Ensemble）
- 每个 capture 运行 `N` 次，每次生成 `M` 个候选诊断（共 `N×M` 个）。
- 不同运行采用不同分析视角（root cause focus / protocol sequence / evidence-first）。
- 可选引入跨模型第二意见（cross-model second opinion，如 Llama 3.3 与 Sonnet 并用）。

#### （3）判决感知证据框架（Verdict-Aware Evidence Framework）
- 定义四类严格判决（verdict）：
  - `CONFIRMED_ISSUE`
  - `PLAUSIBLE_ISSUE`
  - `INSUFFICIENT_EVIDENCE`
  - `NO_ISSUE_FOUND`
- “支持性证据”的定义随判决动态变化：
  - 对 `INSUFFICIENT_EVIDENCE`，缺失预期帧本身即为支持证据。
  - 避免因“无失败帧”而错误惩罚正确诊断。

#### （4）基于证据的调和机制（Evidence-Grounded Reconciliation）
- 引入独立的 **reconciler**（如 Claude Opus）对所有候选进行调和。
- 调和器直接访问原始 PCAP 文本，逐项验证候选中的主张。
- 不依赖多数投票，而是基于证据有效性选择最优诊断。

#### （5）确定性可靠性评分（Deterministic Reliability Scoring）
- 构建复合可靠性分数 `C`，由三个可观测信号组成：
  - **E**（Evidence Validity）：证据是否真实存在且逻辑一致。
  - **S**（Stability）：不同运行间的关键帧与判决一致性。
  - **A**（Agreement）：跨模型（如 Sonnet vs Llama）的一致性。
- 完全不依赖 LLM 自我置信度，实现 **model-agnostic confidence**。

---

### 相比现有方法的优势

| 维度 | 现有方法缺陷 | PROBE 改进 |
|------|--------------|-----------|
| **诊断质量** | 多数投票放大保守判决（如将故障判为“无问题”） | 调和机制恢复少数正确诊断，避免误判 |
| **可靠性评估** | 依赖 LLM 自报置信度，不可靠 | 使用确定性指标，可解释、可路由 |
| **评估公平性** | 黄金参考受特定模型影响，存在偏见 | 提出 assertion-based 评估，剥离叙事风格 |
| **处理不完整捕获** | 易于幻觉失败 | 显式支持 `INSUFFICIENT_EVIDENCE` 判决 |

---

## 2. 核心实验方法和设置

### 数据集
- **87 个企业级 Wi-Fi 捕获文件**，共 **104 个 capture-reviewer 配对**。
- 包含多种协议失败场景：
  - EAPOL 握手失败
  - 关联拒绝
  - DHCP 故障
  - 漫游异常
  - 去认证事件
- 所有黄金参考均来自真实网络支持工单，确保问题真实性。

---

### 实验配置（Configurations）
| 配置 | 描述 |
|------|------|
| **A**: SME only | 仅人类专家标注 |
| **B**: Sonnet one-shot | 单次 Sonnet 调用 |
| **D**: Ensemble 3×3 | 3 次运行 × 3 候选，多数投票 |
| **E**: + Second Opinion | 加入 Llama 3.3 第二意见 |
| **C**: One-shot + Reconcile | 单次 Sonnet + Opus 调和 |
| **F**: Full PROBE | 完整管道：3×3 Ensemble + Llama + Opus 调和 |

---

### 评估指标
1. **Key Frame Precision & Recall**  
   关键帧识别准确率（直接影响根因判断）。

2. **Relevant Frame Precision & Recall**  
   上下文帧覆盖情况。

3. **加权 F1（Weighted F1, Wt F1）**  
   - 关键帧权重 `w_key = 5`
   - 相关帧权重 `w_rel = 1`
   - 错误预测惩罚 `w_fp = 1`
   - 公式：  
     $$
     \text{Wt F1} = \frac{(1+\beta^2) \cdot P_w \cdot R_w}{\beta^2 \cdot P_w + R_w},\quad \beta=1
     $$

4. **完美关键帧匹配率（Perfect Key Match Rate）**  
   预测关键帧集合完全等于黄金标准的比例。

5. **False Negative Rate**  
   在已知故障捕获中，错误判断为“无问题”或“证据不足”的比例。

---

## 3. 主要实验结果和性能指标

### 性能对比（Wt F1）

| 配置 | Wt F1 | 关键说明 |
|------|--------|---------|
| A (SME only) | 0.871 | 人类专家基线 |
| B (Sonnet one-shot) | 0.912 | 单次 LLM 超越人类 |
| D (Ensemble 3×3) | 0.842 | **低于人类基线！** 多数投票失败 |
| E (Ensemble + 2nd Op.) | 0.845 | 第二意见无显著提升 |
| C (One-shot + Reconcile) | 0.964 | 调和机制极大提升 |
| **F (Full PROBE)** | **0.957** | 接近最优，具备可靠性信号 |

> ✅ **关键发现**：**调和（reconciliation）是决定性因素**，而非集成规模。

---

### 消融实验结果

#### （1）集成无调和反而有害
- 多数投票倾向于保守判决（如 `NO_ISSUE_FOUND` 或 `INSUFFICIENT_EVIDENCE`）。
- 在确认故障的捕获中，**50% 的真实故障被错误分类为“无问题”或“证据不足”**。
- Config D 和 E 的 Wt F1 下降至 0.842，**低于单次 LLM（0.912）和人类（0.871）**。

#### （2）调和机制显著提升鲁棒性
- Config C 和 F 的 Wt F1 达到 0.964 和 0.957，**自动接受率达 96%**。
- 最坏情况下的 Wt F1 仍超过 0.70（Config F 第二差为 0.706）。
- 调和器能从少数正确候选中恢复诊断，即使多数投票失败。

#### （3）自报置信度无效
- 71% 的 LLM 自报置信度为 **恰好 0.95**，与实际难度无关。
- AUROC 仅为 0.57，接近随机猜测。
- ❌ **不应用于任何自动化决策**。

#### （4）确定性可靠性评分虽未校准，但有用
- 复合得分范围广（0.075–0.625），但与正确性相关性弱（ρ ≈ 0.09）。
- 原因：调和器太强，几乎所有输出都正确（仅 4% 错误），缺乏方差。
- **建议用途转变**：从“质量门控”转为“困难度标识”——低分案例应送人审阅以丰富数据集。

---

## 4. 关键结论和发现

### 主要发现

1. ✅ **调和优于多数投票**  
   在诊断任务中，多数投票会放大保守偏差；**基于证据的调和才是提升质量的关键**。

2. ✅ **集成的价值在于多样性而非投票**  
   集成的意义不是为了“投票选出最佳”，而是为调和器提供多样假设，尤其是那些被忽略的“少数正确观点”。

3. ✅ **“无证据”本身就是证据**  
   通过 `verdict-aware evidence rules`，系统能合理利用“缺失帧”作为支持 `INSUFFICIENT_EVIDENCE` 的依据，避免误判。

4. ✅ **LLM 自报置信度不可信**  
   必须构建外部、确定性可靠性指标，不能依赖模型自我评估。

5. ✅ **黄金参考需去风格化**  
   提出 **assertion-based evaluation**，将黄金参考拆解为可验证事实（如关键帧、协议类型、根因），剥离叙事风格，实现模型无关评估。

---

### 局限性

1. **数据集偏差**  
   当前数据集 **100% 为确认故障**（CONFIRMED_ISSUE），无法测量假阳性率（幻觉问题）和 `INSUFFICIENT_EVIDENCE` 的准确率。

2. **极端案例仍难处理**  
   存在极少数捕获（如 `2E:91`）连 PROBE 也难以诊断（Wt F1=0.231），人类专家同样表现不佳。

3. **成本较高**  
   调和步骤（Opus）占总成本 73–89%，每捕获约 $0.48，适合高价值场景。

4. **依赖高质量归一化**  
   若 PCAP 文本化丢失结构信息（如帧嵌套关系），可能影响诊断。

---

### 未来工作方向

1. **扩展黄金数据集**  
   加入正常捕获（NO_ISSUE_FOUND）和系统性截断捕获（INSUFFICIENT_EVIDENCE），完善四类判决评估。

2. **构建 assertion-level 标注**  
   由 SME 提取每个案例的“事实核心”，实现完全去偏见的模型无关评估。

3. **集成协议原生表示**  
   使用如 **PLUME** 的协议感知嵌入替代文本化输入，提升结构理解。

4. **推广至其他领域**  
   PROBE 架构适用于任何具有 **确定性数据源 + 多重解释空间 + 可追溯证据** 的诊断任务，如：
   - 5G NAS/RRC 信令分析
   - 工业控制协议（Modbus, OPC-UA）
   - 安全日志分析
   - 医疗影像报告生成

---

> **总结一句话**：  
> PROBE 表明，**可靠诊断不靠“更强的模型”，而靠“更优的架构”** —— 分离假设生成与证据验证，用调和代替投票，用确定性指标替代幻觉置信，是构建可信 LLM 诊断系统的正确路径。

</details>

---

### 16. [From Sampled Outcomes to Capability Distributions: Rethinking Supervision for LLM Routing](https://arxiv.org/abs/2606.06924)

**Authors**: Guannan Lai, Haoran Hu, Long Chen, Zhenguo Li, Han-Jia Ye  
**Category**: cs.LG  
**Published**: 2026-06-08  
**Score**: 6.5  
**Type**: new  
**ArXiv ID**: 2606.06924v1  

#### Abstract
Existing LLM routing methods typically treat a model's single response to a query as its capability label for training routers. However, because LLM generation is inherently stochastic, such single-shot supervision provides only a noisy observation of a query-model pair's behavior rather than a reli...

---

### 17. [DyCon: Dynamic Reasoning Control via Evolving Difficulty Modeling](https://arxiv.org/abs/2606.07108)

**Authors**: Tengyao Tu, Yulin Li, Hui-Ling Zhen, Libo Qin, Zhoujun Wei, Jinghua Piao, Zhuotao Tian, Yong Li, Min Zhang  
**Category**: cs.AI  
**Published**: 2026-06-08  
**Score**: 6.0  
**Type**: new  
**ArXiv ID**: 2606.07108v1  

#### Abstract
Recent advances in Large Reasoning Models (LRMs) demonstrate remarkable performance improvements by iteratively reflecting, exploring, and executing complex tasks, yet suffer from inefficiencies due to redundant reasoning, known as "overthinking". Existing methods to mitigate this issue either rely ...

---

### 18. [Improving Cross-Lingual Factual Recall via Consistency-Driven Reinforcement Learning](https://arxiv.org/abs/2606.06586)

**Authors**: Jonathan von Rad, Louis Arts, George Burgess, Eleftheria Kolokytha, Harry O'Donnell, Ektor Oikonomidis Doumpas, Eduardo Sanchez, Yao Lu, Pontus Stenetorp  
**Category**: cs.CL  
**Published**: 2026-06-08  
**Score**: 6.0  
**Type**: new  
**ArXiv ID**: 2606.06586v1  

#### Abstract
Large language models (LLMs) trained predominantly on English data encode substantial world knowledge, yet often fail to express it reliably in other languages, a phenomenon known as cross-lingual factual inconsistency. To study and address this, we introduce PolyFact, a large-scale parallel multili...

---

### 19. [CRAFT: A Unified Counterfactual Reasoning Framework for Tabular Question Answering and Fact Verification](https://arxiv.org/abs/2606.06842)

**Authors**: Chenshuo Pan, Yu Zhao, Jie Zhang, Changzai Pan, Zhenhe Wu, Jiayi Liang, Yujie Mao, Shuangyong Song, Yongxiang Li, Zhongjiang He  
**Category**: cs.CL  
**Published**: 2026-06-08  
**Score**: 6.0  
**Type**: new  
**ArXiv ID**: 2606.06842v1  

#### Abstract
Table reasoning remains challenging for large language models (LLMs), particularly in tasks that require multi-step inference over long and structured tables. Existing approaches predominantly rely on single-direction reasoning, which limits their ability to explore alternative hypotheses across tas...

---

### 20. [Beyond Rubrics: Exploration-Guided Evaluation Skills for Reward Modeling](https://arxiv.org/abs/2606.07040)

**Authors**: Xing Yue, Linjuan Wu, Daoxin Zhang, Yongliang Shen, Weiming Lu  
**Category**: cs.CL  
**Published**: 2026-06-08  
**Score**: 6.0  
**Type**: new  
**ArXiv ID**: 2606.07040v1  

#### Abstract
Open-ended reward modeling requires judges that can follow subtle, domain-specific preferences when verifiable answers are unavailable. Existing rubric-based methods often address this by generating criteria online for each query, but the extra generation step can add inference overhead and produce ...

---

### 21. [Elmes*: Automated Construction of Fine-Grained Evaluation Rubrics for Large Language Models in Long-Tail Educational Scenarios](https://arxiv.org/abs/2606.06546)

**Authors**: Tao Liu, Ye Lu, Ruohua Zhang, Siyu Song, Wentao Liu, Aimin Zhou, Hao Hao  
**Category**: cs.LG  
**Published**: 2026-06-08  
**Score**: 6.0  
**Type**: new  
**ArXiv ID**: 2606.06546v1  

#### Abstract
Evaluating large language models (LLMs) for education requires measuring how models teach, not only what they know. Existing benchmarks emphasize domain-general correctness or depend on manually designed rubrics that scale poorly to long-tail pedagogical scenarios. We introduce Elmes*, an end-to-end...

---

### 22. [A Rolling-Window Framework for Churn Prediction and Behavioral Driver Identification](https://arxiv.org/abs/2606.06776)

**Authors**: Muhammad Jawad Mufti, Omar Hammad, Haitham Saleh, Muqaddas Gull  
**Category**: cs.LG  
**Published**: 2026-06-08  
**Score**: 6.0  
**Type**: new  
**ArXiv ID**: 2606.06776v1  

#### Abstract
Customer churn prediction is a central task in customer analytics, particularly in non-contractual, pay-per-use service environments where disengagement is not explicitly observed and must be inferred from behavioral inactivity. Existing churn prediction approaches often rely on simplified temporal ...

---

### 23. [Constructing VAE Latent Spaces with Prescribed Topology](https://arxiv.org/abs/2606.07058)

**Authors**: Jilles S. van Hulst, Jakub M. Tomczak, W. P. M. H. Heemels, Duarte J. Antunes  
**Category**: cs.LG  
**Published**: 2026-06-08  
**Score**: 6.0  
**Type**: new  
**ArXiv ID**: 2606.07058v1  

#### Abstract
Variational autoencoders (VAEs) learn low-dimensional latent representations of high-dimensional data. When the data lies on a manifold with non-Euclidean topology, the standard Gaussian prior introduces a topological mismatch that degrades reconstruction quality and prevents faithful representation...

---

### 24. [TabSwift: An Efficient Tabular Foundation Model with Row-Wise Attention](https://arxiv.org/abs/2606.07345)

**Authors**: Si-Yang Liu, Han-Jia Ye  
**Category**: cs.LG  
**Published**: 2026-06-08  
**Score**: 6.0  
**Type**: new  
**ArXiv ID**: 2606.07345v1  

#### Abstract
Tabular foundation models, exemplified by TabPFN, perform prediction via in-context learning, inferring test labels directly from labeled training examples. They have demonstrated competitive performance, particularly on small-to-medium datasets. However, recent tabular foundation models often impro...

---

### 25. [CoMetaPNS: Continually Meta-learning Personalized Neural Surrogates for Cardiac Electrophysiology Simulations](https://arxiv.org/abs/2606.07488)

**Authors**: Ryan Missel, Xiajun Jiang, Linwei Wang  
**Category**: cs.LG  
**Published**: 2026-06-08  
**Score**: 6.0  
**Type**: new  
**ArXiv ID**: 2606.07488v1  

#### Abstract
Personalized virtual heart simulations face challenges in model personalization and computational cost. While neural surrogates offer state-of-the-art solutions, they typically address either efficient personalization or training generalizable models. Recent work reframes this by learning the proces...

---

### 26. [DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive Search and Rubric-Grounded Reasoning](https://arxiv.org/abs/2606.07299)

**Authors**: Lingyong Yan, Can Xu, Yukun Zhao, Wenxuan Li, Qingyang Chen, Jiulong Wu, Wenli Song, Xiangnan Li, Weixian Shi, Yiqun Chen, Xuchen Ma, Yuchen Li, Jiashu Zhao, Shuaiqiang Wang, Jianmin Wu, Dawei Yin  
**Category**: cs.AI  
**Published**: 2026-06-08  
**Score**: 5.5  
**Type**: new  
**ArXiv ID**: 2606.07299v1  

#### Abstract
Deep Research (DR) has emerged as a new agentic paradigm to tackle complex, open-ended research tasks, demanding systems that can iteratively frame problems, acquire evidence, verify sources, and synthesize long-form reports. In practice, however, current DR systems are constrained by four interrela...

---

### 27. [Clairvoyant: Predictive SJF Scheduling to Mitigate Head-of-Line Blocking in Serial LLM Backends](https://arxiv.org/abs/2606.07248)

**Authors**: Aravind Sundaresan  
**Category**: cs.DC  
**Published**: 2026-06-08  
**Score**: 5.5  
**Type**: new  
**ArXiv ID**: 2606.07248v1  

#### Abstract
Serial LLM inference backends -- such as Ollama -- process requests one at a time under FCFS admission, causing Head-of-Line Blocking (HOLB) under mixed workloads at high utilisation: short factual queries can be delayed by minutes behind long generation jobs. While cloud-scale deployments mitigate ...

---

### 28. [Skip a Layer or Loop It? Learning Program-of-Layers in LLMs](https://arxiv.org/abs/2606.06574)

**Authors**: Ziyue Li, Yang Li, Tianyi Zhou  
**Category**: cs.LG  
**Published**: 2026-06-08  
**Score**: 5.5  
**Type**: new  
**ArXiv ID**: 2606.06574v1  

#### Abstract
Large language models (LLMs) perform inference by following a fixed depth and order, non-recurrent execution of all layers. We reveal the wide existence of training-free, flexible, dynamic program-of-layers (PoLar), where pretrained layers can be packed as modules and then skipped or looped to form ...

---

### 29. [Federated Foundation Models over Vehicular Networks](https://arxiv.org/abs/2606.06786)

**Authors**: Kasra Borazjani, Fardis Nadimi, Payam Abdisarabshali, Owen Palinski, Allan Salihovic, Dinh Nguyen, Minghui Liwang, Seyyedali Hosseinalipour  
**Category**: cs.LG  
**Published**: 2026-06-08  
**Score**: 5.5  
**Type**: new  
**ArXiv ID**: 2606.06786v1  

#### Abstract
This paper presents a forward-looking vision for integrating the emerging multi-modal multi-task federated foundation models (M3T FedFMs) into vehicular networks, with the goal of unifying the expressive power of multi-modal multi-task foundation models (M3T FMs) with the privacy-preserving and dist...

---

### 30. [Accelerating Reproducible Research in Synthetic EHR Generation](https://arxiv.org/abs/2606.06990)

**Authors**: Jalen Jiang, Chufan Gao, Ethan Rasmussen, Stephen Z. Xie, Jimeng Sun  
**Category**: cs.LG  
**Published**: 2026-06-08  
**Score**: 5.5  
**Type**: new  
**ArXiv ID**: 2606.06990v1  

#### Abstract
The generation of high-fidelity synthetic Electronic Health Records (EHR) is crucial for advancing medical research while preserving patient privacy. However, head-to-head comparison of existing generative models is hindered by disjointed codebases, incompatible data loaders, conflicting library dep...

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
