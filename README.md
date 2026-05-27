# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-05-27 09:00:38 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG

## 📚 Recent Papers

### 1. [Semantic-aware Token Selection and Resource Optimization for Communication-efficient Split Federated Fine-tuning in Edge Intelligence](https://arxiv.org/abs/2605.26120)

**Authors**: Xianke Qiang, Zheng Chang, Geyong Min  
**Category**: cs.DC  
**Published**: 2026-05-27  
**Score**: 11.5  
**Type**: new  
**ArXiv ID**: 2605.26120v1  

#### Abstract
Deploying large Transformer-based vision models on resource-limited mobile devices at network edge is severely constrained by hardware limitations and dynamic wireless environments. While federated learning (FL) enables collaborative training without sharing raw data, strictly local fine-tuning of s...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Semantic-aware Token Selection and Resource Optimization for Communication-efficient Split Federated Fine-tuning in Edge Intelligence

## 1. 论文的主要贡献和创新点

### 解决的问题
本文针对在**边缘智能（Edge Intelligence）** 场景下，基于Transformer的大规模视觉模型（如ViT）在资源受限的移动设备上进行联邦微调时面临的两大挑战：
- **计算资源不足**：即使采用参数高效微调技术（如LoRA），本地微调仍对边缘设备内存和算力要求过高；
- **通信开销巨大**：传统Split Federated Learning（SFL）需要上传高维中间激活（activations），导致上行链路带宽消耗严重，尤其在动态无线环境中成为瓶颈。

### 提出的新方法与创新思路
作者提出 **ST-SFLora** ——一种**语义感知的分拆式联邦LoRA微调框架**，其核心创新包括：

#### （1）语义感知的Token选择机制（Semantic-aware Token Selection）
- 利用Vision Transformer中[CLS] token的**自注意力权重**作为衡量patch token语义重要性的指标；
- 在客户端仅保留注意力得分最高的前 $K_m$ 个token，并将剩余低分token通过加权平均合并为一个“merged token”，以保留全局上下文；
- 实现从**bit-level压缩**到**semantic token-level压缩**的范式转变，契合6G任务导向通信趋势。

#### （2）新型系统级度量：语义传输效率（Semantic Transmission Efficiency, STE）
- 定义STE为单位时间传递的有效语义信息量：
  $$
  \text{STE} = \frac{\sum_{m \in \mathcal{U}} f_m(K_m)}{\max_{m \in \mathcal{U}} T_m}
  $$
  其中分子是所有客户端保留的累计语义信息，分母是最大上行延迟（由最慢客户端决定）；
- STE首次显式量化了**语义保真度与通信延迟之间的权衡**，指导联合优化。

#### （3）联合资源优化问题建模与求解
- 构建混合整数非凸优化问题，联合优化：
  - 整型变量：每个客户端选择的token数量 $K_m$
  - 连续变量：上行功率 $p_m$ 和带宽分配 $W_m$
- 在严格的**延迟约束**和**能量预算**下最大化STE；
- 设计交替优化算法（Alternating Optimization）分解为三个子问题迭代求解，保证收敛性和实用性。

### 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| **通信效率** | 显著减少activation上传量（可降至原始的1/3以下），远优于传统bit-level压缩方法 |
| **客户端负载** | 客户端仅需执行轻量级前向传播，无需反向传播或额外评分网络，极大降低计算与内存需求 |
| **系统适应性** | 动态响应信道变化与设备异构性，实现弹性参与和鲁棒训练 |
| **理论支撑** | 引入STE指标提供统一优化目标，具有明确物理意义 |

---

## 2. 核心实验方法和设置

### 数据集
实验在三个主流图像分类数据集上进行，涵盖通用与细粒度任务：
- **ImageNet100**：ILSVRC-2012的100类子集，用于通用物体识别；
- **Oxford Flowers-102**：102种花卉类别，存在显著尺度、姿态和光照变化；
- **CUB-200-2011**：200种鸟类细粒度分类，需捕捉细微判别特征。

同时考虑两种数据分布：
- **IID**：数据均匀划分；
- **non-IID**：使用Dirichlet分布（浓度参数 $\alpha=0.5$）模拟高度异构场景。

### 实验设置
- **网络架构**：ViT-S/16、ViT-B/16、ViT-L/16；
- **LoRA配置**：rank=16，应用于服务器侧编码器层；
- **客户端规模**：100个移动设备，每轮按泊松分布随机激活部分参与；
- **通信环境**：
  - 覆盖半径5–500米；
  - 总带宽 $W_{\text{tot}} = 50$ MHz；
  - 最大发射功率 0.2 W；
  - 路径损耗指数 2.5，噪声谱密度 -174 dBm/Hz；
- **硬件模拟**：GPU频率 [1.0, 1.5] GHz，核心数 [4, 6]。

### 评估指标
- **模型性能**：Top-1 Accuracy（IID/non-IID）
- **资源消耗**：
  - 客户端GPU Memory Usage（GB）
  - 上行通信量（MB）
  - 通信延迟与能耗
- **系统效率**：Semantic Transmission Efficiency (STE)

### 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| **LocalLoRA** | 本地训练 | 不聚合，无隐私保护 |
| **FedLoRA** | Federated Learning | 客户端微调LoRA并上传更新 |
| **SplitLoRA** | Split Learning | 序列化协作，上传完整activation |
| **SFLora** | Split Federated Learning | 并行SFL + LoRA，上传完整activation |
| **ST-SFLora-Full** | 本文变体 | 冻结客户端参数，不选token |
| **ST-SFLora (Ours)** | 本文方法 | 语义感知token选择 + 联合资源优化 |

---

## 3. 主要实验结果和性能指标

### 关键性能数据（摘自Table I）

| Backbone | Method | ImageNet100 (non-IID) | Flowers-102 (non-IID) | CUB-200-2011 (non-IID) |
|----------|--------|------------------------|------------------------|-------------------------|
| ViT-B/16 | FedLoRA | 52.49% | 57.95% | 21.53% |
| ViT-B/16 | SplitLoRA | 89.47% | 99.29% | 80.65% |
| ViT-B/16 | SFLora | 89.09% | 98.69% | 79.84% |
| ViT-B/16 | **ST-SFLora (Ours)** | **85.81%** | **96.43%** | **73.69%** |

> 尽管精度略有下降，但**ST-SFLora在极端资源限制下仍显著优于FL类方法**，且接近SFL类方法。

### 客户端资源消耗对比（Table II）

| Method | GPU Mem. (GB) | Communication (MB) |
|--------|---------------|--------------------|
| LocalLoRA / FedLoRA | 9.0 | 335.3 (model broadcast) |
| SplitLoRA / SFLora | 2.3 | ~58.2 (full activation) |
| **ST-SFLora (top-K)** | **1.4** | **~16 (K=64)** |

- **内存减少84.4%**（从9.0 → 1.4 GB）；
- **通信量减少约72%**（从58.2 → 16 MB）；
- 完全消除模型广播开销。

### 消融实验结果（Fig. 8b）
比较不同组件对STE的影响（固定 $E_{\text{max}}=0.8J$）：
- **完整方案（Full）**：STE ≈ 43.45（最优）
- **移除Token Selection**：STE ↓ 至 ~35.2（降幅最大）
- **移除Bandwidth Allocation**：STE ↓ 至 ~38.1
- **移除Power Control**：STE ↓ 至 ~40.5

> 表明**token selection是提升STE最关键的因素**，三者协同作用显著。

### 其他关键观察
- **收敛速度快**：联合优化算法通常在5次以内外层迭代即收敛（Fig. 8a）；
- **资源-语义平衡**：随着 $W_{\text{tot}}$ 或 $E_{\text{max}}$ 增加，所选token数 $K_m$ 自适应增加（Fig. 8c）；
- **可视化验证**：所选token集中在对象轮廓、纹理等判别区域，背景被有效屏蔽（Fig. 9）；
- **精度-压缩权衡**：当 $K \geq 128$ 时，准确率已接近全token基线（Fig. 10）。

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **语义感知token选择可行且高效**：利用Transformer自身注意力机制即可实现高质量token筛选，无需引入额外模块；
2. ✅ **STE是一个有效的系统级优化目标**：能统一协调语义保留与通信成本，在真实边缘环境中找到最佳操作点；
3. ✅ **联合优化显著提升系统效率**：通过动态调整 $K_m$, $p_m$, $W_m$，可在严苛资源约束下维持较高模型性能；
4. ✅ **ST-SFLora实现最低客户端开销**：在所有对比方法中，其GPU内存和通信消耗最小，适合部署于低端移动设备。

### 方法的局限性
- **依赖预训练模型的注意力质量**：若注意力未能准确反映语义重要性（如某些domain shift场景），可能误删关键token；
- **当前策略为静态排序+阈值截断**：未引入可学习的选择机制，灵活性有限；
- **假设CSI完美反馈**：实际中信道状态获取本身有开销和误差；
- **仅适用于Vision Transformer类结构**：难以直接推广至CNN或其他模态。

### 未来工作方向
- 探索**可学习的token selection策略**（如轻量子网络）进一步优化效率-性能边界；
- 扩展至**多模态与NLP任务**（如BERT-based文本分类）；
- 结合**语义编码技术**（Semantic Communication）实现端到端语义传输；
- 研究**异步与容错机制**以支持更不稳定的真实边缘网络环境。

--- 

> **总结一句话**：  
> **ST-SFLora首次将语义感知token选择引入Split Federated Learning，通过定义STE指标并联合优化token、功率与带宽，在保障模型性能的同时实现了极致的客户端资源节省，为大规模Vision Transformer在边缘设备上的高效微调提供了新路径。**

</details>

---

### 2. [SIKA-GP: Accelerating Gaussian Process Inference with Sparse Inducing Kernel Approximations for Bayesian Deep Learning](https://arxiv.org/abs/2605.26509)

**Authors**: Wenyuan Zhao, Rui Tuo, Chao Tian  
**Category**: cs.LG  
**Published**: 2026-05-27  
**Score**: 11.5  
**Type**: new  
**ArXiv ID**: 2605.26509v1  

#### Abstract
Gaussian processes (GPs) provide a principled Bayesian framework for uncertainty estimation, but their computational complexity severely limits scalability to large datasets. We propose SIKA-GP, which accelerates GP inference using sparse inducing kernel approximations based on a dyadic ordered temp...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：SIKA-GP: Accelerating Gaussian Process Inference with Sparse Inducing Kernel Approximations for Bayesian Deep Learning

---

## 1. 论文的主要贡献和创新点

### 解决的问题
传统的 **Gaussian Process (GP)** 虽然在不确定性估计方面具有理论优势，但由于其推理复杂度为 $O(N^3)$（$N$ 为训练样本数），难以扩展到大规模数据集。尽管已有稀疏变体如 **Sparse GP (SGP)** 和 **Deep Kernel Learning (DKL)** 改善了可扩展性，但在高维特征空间或需要大量 inducing points 时，计算开销仍然显著。

此外，将 GP 集成到现代深度学习架构（如 Vision 和 Transformer）中仍面临效率瓶颈。

### 提出的新方法与思路
本文提出 **SIKA-GP**（Sparse Inducing Kernel Approximation for GP），一种基于 **dyadic ordered template basis** 的稀疏诱导核近似方法，用于加速 GP 推理。其核心思想包括：

- 利用 **Laplace kernel** 的 Markov 性质，在 dyadic 网格上构建一组具有闭式表达的 compactly supported 基函数。
- 将 GP 表示为等效的 **Bayesian Neural Network (BNN)** 形式，其中激活函数由这些稀疏基函数构成。
- 引入 **Tensorized Sparse Indexing (TSI)** 算法，实现高效的 GPU 并行化前向传播，仅需激活 $O(\log M)$ 个基函数（$M$ 为 inducing points 数量）。

该方法天然支持嵌入到 **Bayesian Deep Learning (BDL)** 架构中，如 **DGP**（Deep GP）和 **DKL**。

### 相比现有方法的优势
| 方面 | SIKA-GP 的优势 |
|------|----------------|
| **计算复杂度** | 推理复杂度从 $O(M)$ 或 $O(M^{1+\epsilon})$ 降至 $O(\log M)$，训练和推理均显著加速 |
| **集成能力** | 可无缝嵌入 BNN 架构，兼容现代深度模型（CNN、ResNet、Transformer） |
| **稳定性** | 固定的 dyadic 网格避免了 inducing points 学习带来的优化不稳定问题 |
| **可扩展性** | 支持深层结构（deep architectures）和高维特征，适用于 vision 和 language 任务 |

---

## 2. 核心实验方法和设置

### 使用的数据集
| 类型 | 数据集 |
|------|--------|
| **回归任务** | UCI 数据集：Gas, Kin40K, Protein |
| **图像分类** | MNIST, CIFAR-10, CIFAR-100 |
| **语言建模** | CLINC150（intent classification + OOD detection） |

### 实验设置
- **模型架构**：
  - **DGP-SIKA**：堆叠两层 SIKA-GP 构成 Deep GP。
  - **DKL-SIKA**：使用 CNN / ResNet / DistilBERT 提取特征，最后一层接 SIKA-GP。
- **Inducing Points**：固定在 dyadic 网格上，数量 $M = 2^L + 1$，默认 $L=7 \Rightarrow M=129$。
- **优化方式**：采用 **Variational Inference (VI)**，使用 Adam 优化 ELBO。
- **MC Sampling**：训练时使用 10–20 个样本，测试时使用 20 个样本进行不确定性估计。

### 评估指标
| 指标 | 含义 |
|------|------|
| **RMSE / ACC** | 预测准确性（回归 / 分类） |
| **NLPD / NLL** | 负对数预测密度 / 负对数似然，衡量概率校准 |
| **ECE** | Expected Calibration Error，分类置信度校准误差 |
| **AUROC / AUPRC** | OOD 检测性能 |
| **Train/Infer Time** | 每轮训练时间和单次推理时间，评估效率 |

### 基线方法对比
| 基线 | 描述 |
|------|------|
| **SVGP** | 经典稀疏变分 GP，学习 inducing points |
| **KISS-GP / SKI** | 结构化核插值方法，利用网格结构加速 |
| **DAK** | Deep Additive Kernel，基于密集核近似的 BNN-GP 混合模型 |
| **SVDKL** | Standard Deep Kernel Learning 实现 |

---

## 3. 主要实验结果和性能指标

### 关键性能数据与对比结果

#### ✅ 在 UCI 回归任务上的表现（Table 2）
| Dataset | 方法 | RMSE ↓ | NLPD ↓ | Time (s/epoch) ↓ |
|--------|------|--------|--------|------------------|
| Gas | DGP | 0.54 | 1.09 | 19.43 |
|       | **DGP-SIKA** | **0.53** | **1.07** | **2.79** ($\sim$7× faster) |
| Kin40K | DGP | 0.09 | 0.07 | 33.25 |
|        | **DGP-SIKA** | **0.09** | **0.07** | **15.76** ($\sim$2× faster) |

> **结论**：保持预测精度的同时，训练速度提升 2–7 倍。

#### ✅ 图像分类任务（Table 3）
| Dataset | 方法 | ACC (%) ↑ | ECE (%) ↓ | Train Time (s/epoch) ↓ |
|--------|------|-----------|------------|-------------------------|
| CIFAR-10 | DAK | 94.53 | 4.34 | 35.04 |
|          | **DKL-SIKA** | **94.78** | **4.06** | **17.26** ($\sim$2× faster) |
| CIFAR-100 | DAK | 76.61 | 5.55 | 102.57 |
|           | **DKL-SIKA** | **76.94** | **4.31** | **36.31** ($\sim$3× faster) |

> **结论**：不仅更快，且在准确率和校准性上略有提升。

#### ✅ 语言模型任务（CLINC150, Table 4 & 5）
| 指标 | SVDKL | DAK | **DKL-SIKA** |
|------|-------|-----|-------------|
| **AUROC (OOD)** | 0.8413 | 0.8486 | **0.8590** |
| **NLL (ID)** | 0.26 | 0.26 | **0.24** |
| **Time (min/epoch)** | 9.35 | 6.22 | **3.41** |

> **结论**：首次将高效 GP 成功应用于 Transformer-based language model，在 OOD 检测和不确定性估计上表现更优，训练速度快 2 倍以上。

### 消融实验结果（Ablation Studies）

#### 🔹 不同 kernel 的比较（Table 6）
| Kernel | ACC (%) | ECE/NLL ↓ | Train/Infer Time ↓ |
|--------|--------|----------|--------------------|
| RBF (DAK) | 77.43 | 5.36 / 0.98 | 37.38 / 9.78 |
| Laplace (DAK) | 76.13 | 4.18 / 0.99 | 35.62 / 9.66 |
| **Laplace (SIKA)** | **76.61** | **3.45 / 0.94** | **20.08 / 7.07** |

> **发现**：虽然 Laplace kernel 表达能力弱于 RBF，但结合 SIKA 后反而提升了校准性和效率，说明深度结构弥补了先验限制。

#### 🔹 不同 dyadic level $L$ 的影响（Table 7）
| $L$ | $M$ | Active Bases | ACC ↑ | ECE ↓ | NLL ↓ |
|-----|-----|--------------|--------|--------|--------|
| 1 | 3 | 3 | 92.59 | 5.79 | 0.420 |
| 2 | 5 | 4 | 94.56 | 4.17 | 0.279 |
| 7 | 129 | 9 | 94.76 | 4.10 | 0.281 |
| 10 | 1025 | 12 | 94.78 | 4.06 | 0.270 |

> **发现**：即使 $M$ 增加到上千，每输入仅激活 $L+2 \approx 12$ 个基函数，性能趋于稳定，验证了稀疏性的有效性。

---

## 4. 关键结论和发现

### 主要发现
1. **SIKA-GP 实现了近乎对数级的推理加速**：通过稀疏激活机制，将传统 GP 的 $O(M)$ 复杂度降低至 $O(\log M)$，极大提升了可扩展性。
2. **无需牺牲性能即可获得显著加速**：在多个 benchmark 上，SIKA-GP 在 RMSE、ACC、NLL、ECE 等指标上与基线持平甚至更好。
3. **天然适配现代深度学习架构**：成功应用于 CNN、ResNet 和 Transformer，展示了其在 vision 和 NLP 中的通用性。
4. **支持更多 MC sampling**：由于前向代价低，可在训练和测试中使用更多 MC 样本，从而获得更可靠的不确定性估计（见 Appendix D.1）。

### 方法的局限性
1. **Kernel 限制**：当前方法依赖于 **Laplace kernel** 的 Markov 结构，无法直接推广到任意 kernel（如 RBF）。不过可通过 DKL 框架缓解此问题。
2. **固定网格设计**：inducing points 固定在 dyadic 网格上，缺乏自适应能力，可能在某些非均匀分布数据上不如可学习 inducing points 灵活。

### 未来工作方向
1. **扩展至其他 kernel 类型**：探索如何将类似稀疏结构应用于 Matérn、RBF 等更广义的 kernel。
2. **自适应或混合网格**：研究动态调整 dyadic level 或结合可学习 inducing points 的 hybrid 方法。
3. **与参数高效微调结合**：集成 LoRA、Adapter 等技术，进一步降低大模型下的贝叶斯推理成本。
4. **部署优化**：针对边缘设备优化 TSI 算法，实现实时不确定性感知推理。

---

> 📌 **代码与复现**：作者已开源代码：https://github.com/warrenzha/sika-gp  
> 所有实验均可复现，支持 PyTorch + GPyTorch 框架。

</details>

---

### 3. [UnityMAS-O: A General RL Optimization Framework for LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2605.26646)

**Authors**: Yiqun Chen, Wei Yang, Erhan Zhang, Shijie Wang, Qi Liu, Zechun Niu, Bin Zhang, Haitao Li, Rui Li, Lingyong Yan, Jinyuan Feng, Biqing Qi, Xiaochi Wei, Yan Gao, Yi Wu, Yao Hu, Jiaxin Mao  
**Category**: cs.AI  
**Published**: 2026-05-27  
**Score**: 10.0  
**Type**: new  
**ArXiv ID**: 2605.26646v1  

#### Abstract
LLM-based multi-agent systems decompose complex tasks into interacting roles, but most remain manually orchestrated by prompts, tools, and control rules, while agents are rarely optimized through a unified reinforcement learning interface. Existing RL post-training frameworks mainly target single-po...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：UnityMAS-O: A General RL Optimization Framework for LLM-Based Multi-Agent Systems**

---

## **1. 论文的主要贡献和创新点**

### **解决了什么问题**
当前基于 LLM 的 Multi-Agent Systems (MAS) 虽然在复杂任务分解、角色协作方面展现出潜力，但其优化机制存在严重瓶颈：
- 多数系统依赖**手动编排**（prompt、工具调用、控制规则），缺乏统一的 **Reinforcement Learning (RL)** 优化接口。
- 现有 RL 后训练框架（如 TRL、OpenRLHF、verl）主要面向**单策略优化**，无法直接支持多智能体系统的结构化交互、角色级信用分配（credit assignment）和灵活的参数共享配置。

因此，**如何将任意用户定义的 LLM-MAS 工作流转化为可训练的 MARL 系统**，成为一个未被充分解决的问题。

---

### **提出了什么新方法或新思路**
论文提出 **UnityMAS-O**，一个通用的 RL 优化框架，用于 LLM-based Multi-Agent Systems。其核心创新在于引入了四个一级抽象对象（first-class abstractions）：

| 抽象对象 | 描述 |
|--------|------|
| **Logical Agent Roles** | 定义逻辑上的智能体角色（如 Planner、Coder、Verifier），独立于物理模型参数。 |
| **Graph-Structured Trajectories** | 将整个工作流执行过程建模为图结构轨迹，支持顺序、并行、迭代等复杂流程。 |
| **User-Defined Reward Functions** | 支持在角色级（role-level）、回合级（turn-level）、全流程级（trajectory-level）定义奖励信号。 |
| **Explicit Agent-Model Mappings** | 显式定义逻辑角色到物理 LLM 实例的映射关系 `φ: V → M`，支持全共享、全分离、部分共享三种参数共享模式。 |

该设计实现了**逻辑角色与物理模型的解耦**，使得同一工作流可在不同参数共享策略下进行训练和比较。

---

### **相比现有方法的优势**
| 维度 | Standard verl-style RL | UnityMAS-O |
|------|------------------------|-----------|
| **优化单位** | 单一策略轨迹（policy-centered） | 图结构多智能体工作流（multi-agent workflow） |
| **角色建模** | 隐含在环境逻辑中 | 作为一级对象显式定义 |
| **模型分配** | 单策略或手动定制 | 显式映射，支持全/部分/独立共享 |
| **奖励接口** | 单一响应或轨迹级奖励 | 角色级、回合级、全流程级奖励 |
| **运行时架构** | Rollout 与更新围绕单一模型 | 中央控制器 + 模型本地 Worker Group 的星型拓扑 |

此外，UnityMAS-O 构建在 **Ray + verl** 之上，支持异构分布式执行，实现：
- 异步 Rollout
- 结构化轨迹记录
- 模型本地缓冲与优势计算
- 分布式 PPO-style 更新

---

## **2. 核心实验方法和设置**

### **使用的数据集**
- **Retrieval-Augmented QA / Agentic Search**:
  - **Natural Questions (NQ)**：单跳开放域问答，测试检索与答案生成能力。
  - **HotpotQA**：多跳推理问答，强调证据聚合与中间状态管理。
- **Reflective Code Generation**:
  - 基于 **DeepCoder** 数据设定，约 24K 编程题-测试对，来自 TACO-Verified、PrimeIntellect SYNTHETIC-1 和 LiveCodeBench v5。

---

### **实验设置和评估指标**

#### **工作流模板（见 Figure 3）**
| 名称 | 类型 | 描述 |
|------|------|------|
| **Workflow A**: Parallel Retrieval | Search | 并行检索多个证据后生成答案 |
| **Workflow B**: Retrieve-Extract-Answer | Search | 检索 → 提取证据 → 回答 |
| **Workflow C**: Iterative Search Loop (M-ASK) | Search | 迭代搜索-摘要-更新循环 |
| **Workflow D**: Reflective Verification Loop | Code | Plan → Code → Verify → Reflect，最多三轮 |

#### **评估指标**
| 任务 | 主要指标 | 辅助指标 |
|------|----------|----------|
| QA/Search | **Normalized Answer F1** | 训练前后提升幅度 |
| Code | **Held-out Test All-Passed Rate**（最终程序通过所有测试的比例） | 训练最终通过率、平均验证轮次 |

#### **模型设置**
- 主要使用 **Qwen3-family** 模型（0.5B ~ 14B）
- 参数共享模式包括：
  - **Full Sharing**：所有角色共享一个模型
  - **Partial Sharing**：相关角色组共享
  - **Full Separation**：每个角色独立模型

#### **基线方法对比**
- **无 RL 训练的原始工作流**（Before RL）
- 不同参数共享策略下的 UnityMAS-O 变体（如 3B shared vs 4x3B independent）
- 与近期 MARL 方法对比（如 M-ASK、MAO-ARAG），但本文更侧重框架通用性而非 SOTA 性能竞争

---

## **3. 主要实验结果和性能指标**

### **关键性能数据**

#### **QA 任务结果（Table 3 & Appendix A）**
| Dataset | Workflow | Model Size | Before RL | Best After RL | Abs. Gain | Rel. Gain |
|--------|---------|------------|-----------|---------------|-----------|-----------|
| NQ | QD-Answer | 0.5B | 0.022 | **0.445** | +0.424 | +1943% |
| NQ | QD-Answer | 14B | 0.328 | **0.594** | +0.267 | +81% |
| HotpotQA | M-ASK | 1.5B | 0.127 | **0.525** | +0.398 | +313% |
| HotpotQA | M-ASK | 7B | 0.254 | **0.573** | +0.319 | +126% |

> ✅ 所有设置均显著提升，小模型增益尤为巨大（如 0.5B 模型提升超 10 倍）

#### **Code 任务结果（Table 4 & Figure 6）**
| Setting | Before RL | Best After RL | Abs. Gain | Rel. Gain |
|--------|-----------|----------------|-----------|-----------|
| 3xQwen3-4B | 0.255 | **0.686** | +0.431 | +169% |
| 3xQwen3-8B | 0.290 | **0.738** | +0.448 | +154% |

> ✅ 在严格的 **all-passed** 指标下仍取得大幅提升

---

### **与基线方法的对比结果**
- **相比未训练的工作流**：所有任务、所有模型规模均实现显著提升，证明 MARL 能有效优化多智能体协作行为。
- **相比固定参数共享的 RAG 方法**（如 M-ASK）：
  - UnityMAS-O 支持更灵活的参数共享配置
  - 在相同 M-ASK 工作流下复现并验证了 turn-level F1 奖励的有效性
  - 支持跨任务迁移（从 QA 到 Code）

---

### **消融实验结果**
#### **(1) 参数共享的影响（Figure 5）**
- 在 HotpotQA M-ASK 3B 设置下对比：
  - **4x3B Independent**：收敛更快，最高达 **0.529**
  - **3B Shared**：收敛较慢但最终达到 **0.522**
- 表明：**即使多个角色共享同一 LLM 参数，UnityMAS-O 仍能有效训练**，实现接近独立模型的性能，显著降低资源开销。

#### **(2) 执行效率提升（Figure 7）**
- 在 Code 任务中，训练后平均验证轮次下降：
  - 3xQwen3-8B：从 ~2.5 → **1.68** @ step 1850
  - 3xQwen3-4B：从 ~2.5 → **1.76** @ step 2350
- 表明：MARL 不仅提升最终正确率，还优化了内部决策效率（更早终止）。

---

## **4. 关键结论和发现**

### **主要发现**
1. **多智能体 RL 可显著提升手动设计的工作流性能**，尤其在小模型和严格评估指标下效果更明显。
2. **逻辑角色与物理模型的解耦是可行且有效的**，支持在同一框架下研究不同参数共享策略的权衡。
3. **奖励设计至关重要**：
   - QA 任务中采用共享 F1 + 节点格式惩罚
   - Code 任务中采用 verifier-score delta 奖励，实现增量改进
4. **UnityMAS-O 是任务无关的优化基底**（optimization substrate），可应用于 QA、Code、Math、Embodied Agent 等多种任务。

---

### **方法的局限性**
1. **当前实现基于 PPO-style**，尚未集成其他 MARL 算法（如 QMIX、COMA）。
2. **中央控制器可能成为瓶颈**，在极大规模并发工作流下需进一步优化调度。
3. **奖励函数仍需人工设计**，自动奖励建模（reward modeling）未被纳入。
4. **目前实验集中在可验证任务**（有明确 reward signal），对开放式任务的支持有待验证。

---

### **未来工作方向**
1. **扩展至更多任务领域**：
   - 正在进行 ALFWorld（embodied agent）、WebShop（web interaction）、SWE-bench（software engineering）的实验。
2. **支持更多 RL 算法**：如 off-policy 方法、multi-objective RL。
3. **自动化奖励设计**：结合 RM 或人类反馈。
4. **动态工作流调整**：允许 RL 在训练过程中修改图结构或角色定义。
5. **更大规模部署**：探索在千卡集群上的弹性调度与容错机制。

---

## **总结**
**UnityMAS-O** 是首个将“用户定义的 LLM-MAS 工作流”作为 RL 优化单元的通用框架。它通过四大一级抽象和星型分布式架构，实现了：
- ✅ 多智能体轨迹的端到端优化
- ✅ 灵活的参数共享配置
- ✅ 精细的角色级信用分配
- ✅ 高效的异构分布式训练

其实验结果表明，**即使是简单的 MARL 微调，也能让原本表现平庸的多智能体系统实现质的飞跃**，为构建可进化的 LLM-MAS 提供了坚实基础。

> 🔗 **开源地址**：[https://github.com/chenyiqun/UnityMAS-O](https://github.com/chenyiqun/UnityMAS-O)

</details>

---

### 4. [MicroSpec: Accelerating Speculative Decoding with Lightweight In-Context Vocabularies](https://arxiv.org/abs/2605.26444)

**Authors**: Zhiyang Chen, Daliang Xu, Yinyuan Zhang, Chenghua Wang, Mengwei Xu, Yun Ma  
**Category**: cs.CL  
**Published**: 2026-05-27  
**Score**: 10.0  
**Type**: new  
**ArXiv ID**: 2605.26444v1  

#### Abstract
Large language models typically employ vocabularies of over 100k tokens, which creates a major computational bottleneck at the final linear projection layer when performing speculative decoding. Current methods for vocabulary pruning depend on either fixed or coarse-grained sub-vocabularies, requiri...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：MicroSpec: Accelerating Speculative Decoding with Lightweight In-Context Vocabularies

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
大型语言模型（LLMs）通常拥有超过10万的 **vocabulary** 大小（如 Llama-3 为 128k，Qwen-2 为 152k），这导致在 **speculative decoding (SD)** 中，draft 模型的最后一层线性投影（即 **LM head**）成为显著的计算瓶颈。尽管已有方法尝试通过 **vocabulary pruning** 来缓解该问题，但它们大多依赖于静态或粗粒度的子词表策略，需要保留约 30k 的活跃词汇才能维持 draft 质量，难以实现高效加速。

### 🚀 提出的新方法：MicroSpec
MicroSpec 是一种**无需训练**（training-free）的技术，其核心思想是利用语言生成中的**强时间局部性**（temporal locality）——即下一个 token 很可能出现在当前上下文中或为其直接延伸。

#### 创新点：
- **动态构建轻量级上下文敏感词表**：每一步解码时，仅从历史 token 和近期高概率候选中构建一个极小的活跃词表（平均 <3k tokens），远小于现有方法（27k–32k）。
- **系统-算法协同设计**：为解决稀疏内存访问带来的硬件效率问题，提出：
  - **异步 gather**（asynchronous gathering）：将稀疏权重加载与模型计算流水线并行化。
  - **GPU 驻留状态管理**（GPU-resident state management）：完全在 GPU 上维护滑动窗口状态，避免 CPU-GPU 同步开销。

### 🔍 相比现有方法的优势
| 维度 | MicroSpec | 现有方法（如 FR-Spec、CORAL、DynaSpec） |
|------|-----------|----------------------------------------|
| 是否需要额外训练 | ❌ 无 | ✅ 需要（如训练 router） |
| 活跃词表大小 | **<3k**（减少 >40×） | ~27k–32k |
| 推理延迟降低 | 平均 **51.6%** draft inference latency ↓ | 最多仅 20–30% |
| 端到端加速 | **1.12–1.32×** 超越 EAGLE-2 | 通常 <1.2× |
| 兼容性 | 插件式增强（plug-and-play），可集成至 EAGLE/Medusa 架构 | 通常需修改架构或训练 |

---

## 2. 核心实验方法和设置

### 📚 数据集与任务（Benchmarks）
使用 **SpecBench** 基准测试套件，涵盖六类任务：
- **MT**（Machine Translation）
- **Conv.**（Multi-turn Conversation）
- **RAG & QA**
- **Math**（Mathematical Reasoning）
- **Summ.**（Summarization）
- **Code**（HumanEval 用于代码生成）

最大生成长度设为 1024 tokens，采用 greedy sampling。

### ⚙️ 实验设置
- **模型**：
  - `Llama-3-8B-Instruct`
  - `Llama-3.2-1B-Instruct`
  - `Qwen-2-7B-Instruct`
- **硬件**：单张 NVIDIA H20Z GPU
- **超参数**：
  - `Kpre = Kver = 3`（prefill 和 verify 阶段取 top-k）
  - `Wmax = 3072`（滑动窗口最大长度）

### 📊 评估指标
| 指标 | 定义 |
|------|------|
| **End-to-end Speed (tokens/s)** | 包括 prefill 和 decoding 的总吞吐量 |
| **Average Acceptance Length** | 每步被 target model 成功验证的 draft token 数量，反映 draft 质量 |
| **Draft Inference Latency** | draft 模型生成过程耗时 |
| **Speedup over AR** | 相对于自回归 baseline 的加速比 |

### 🆚 基线方法对比
| 方法 | 类型 | 是否训练 | 活跃词表大小 |
|------|------|----------|----------------|
| **EAGLE-2** | Full vocabulary | ❌ | 128k |
| **FR-Spec** | Static pruning (高频词) | ❌ | 32k |
| **CORAL** | Router-based clustering | ✅（1-layer FFN） | 32k |
| **DynaSpec** | Cluster routing + KMeans | ✅（MLP router） | 27k |
| **MicroSpec (Ours)** | Context-aware dynamic | ❌ | **<3k** |

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据（Llama-3-8B-Instruct）

| 方法 | Avg. Speed (tokens/s) | Speedup vs AR | Avg. Accept Length |
|------|------------------------|---------------|---------------------|
| AR (Baseline) | 172.6 | 1.00× | 1.00 |
| EAGLE-2 | 336.9 | 1.93× | 3.80 |
| FR-Spec | 369.7 | 2.12× | 3.62 |
| CORAL | 359.9 | 2.06× | 3.92 |
| DynaSpec | 378.1 | 2.17× | 3.78 |
| **MicroSpec (Ours)** | **392.7** | **2.25×** | **3.59** |

> ✅ 在所有任务上均达到最高速度，平均比 EAGLE-2 快 **1.12–1.32×**

### 🔁 更快的小模型表现更优
在 `Llama-3.2-1B-Instruct` 上：
- EAGLE-2 加速有限（仅 1.05×），因 full-vocabulary LM head 成为主要瓶颈。
- **MicroSpec 达到 1.35× 加速**，显著优于 FR-Spec (1.17×)、DynaSpec (1.20×)。

### ⏱️ Draft Time 分析
- MicroSpec 将 **draft inference latency 平均降低 51.6%**（vs EAGLE-2），相比 FR-Spec 也降低了 **20.3%**。
- 显著减少了 LM head 投影的计算开销。

### 🔬 消融实验（Ablation Study）

| 配置 | Avg. Speed (tokens/s) | 说明 |
|------|------------------------|------|
| Ctx. Only | 313.3 | 仅用 prompt 上下文 → 覆盖不足 |
| Ext. Only | 351.4 | 仅用当前 step 候选 → 缺少全局语义 |
| Ctx. + Ext. (× Async.) | 364.1 | 动态词表有效，但未优化系统 → 受限于 Indexed GEMM |
| **Ctx. + Ext. (√ Async.)** | **394.6** | 完整方法，系统优化释放全部潜力 |

> 💡 结论：**动态词表 + 异步 gather** 共同作用，缺一不可。

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **语言生成具有强烈的时间局部性**：绝大多数正确 token 出现在最近上下文中，因此可以安全地将活跃词表压缩至 <3k。
2. **静态词表剪枝存在根本局限**：无法适应实例级上下文变化，必须保留大量词汇以覆盖长尾 token。
3. **极致稀疏 ≠ 性能损失**：MicroSpec 在大幅缩小词表的同时，仍保持接近 full-vocabulary 的 acceptance length（3.59 vs 3.80），打破了“词表大小 vs 接受率”的传统权衡。
4. **系统优化至关重要**：若不进行异步 gather 和 GPU 驻留管理，动态稀疏机制的实际收益会被内存访问延迟抵消。

### ⚠️ 局限性
- 当前方法假设 target model 不剪枝，仅优化 draft model —— 若目标也受限于大词表，则整体收益受限。
- 滑动窗口机制对极长上下文（>8k）的有效性尚未充分验证。
- 所有实验基于单卡环境，分布式场景下的扩展性有待研究。

### 🔮 未来工作方向
- 将 MicroSpec 思路应用于 **target model 的 early-exit 或 partial decoding**。
- 探索更智能的候选流构造方式（如引入 attention-based filtering）。
- 支持 **streaming generation** 场景下的持续状态压缩。
- 结合 **quantization** 或 **sparsity-aware kernel** 进一步提升硬件利用率。

---

## ✅ 总结
MicroSpec 通过**无需训练的动态上下文词表剪枝 + 系统级协同优化**，成功解决了大词表 LLM 在 speculative decoding 中的 LM head 瓶颈问题。其实现了：
- **<3k 的活跃词表**（较现有方法小 10 倍以上）
- **高达 2.25× 的端到端加速**
- **插件式兼容主流 SD 框架（如 EAGLE）**

该工作展示了“**算法洞察 + 系统工程**”结合的巨大潜力，为高效 LLM 推理提供了新的范式。

</details>

---

### 5. [FAB-Bench: A Framework for Adaptive RAG Benchmarking in Semiconductor Manufacturing](https://arxiv.org/abs/2605.26476)

**Authors**: Jingbin Qian (FutureFab.AI), Congwen Yi (FutureFab.AI), Min Xia (FutureFab.AI), Wen Wu (FutureFab.AI), Jun Zhu (FutureFab.AI), Jian Guan (FutureFab.AI)  
**Category**: cs.CL  
**Published**: 2026-05-27  
**Score**: 10.0  
**Type**: new  
**ArXiv ID**: 2605.26476v1  

#### Abstract
Retrieval-Augmented Generation (RAG) has become critical for knowledge-intensive applications, yet evaluating its performance in vertical domains remains difficult due to domain complexity, diverse context scales, and heavy reliance on expert assessments that are costly, inconsistent, and non-scalab...

---

### 6. [MobileExplorer: Accelerating On-Device Inference for Mobile GUI Agents via Online Exploration](https://arxiv.org/abs/2605.26546)

**Authors**: Runxi Huang, Liyu Zhang, Shengzhong Liu, Xiaomin Ouyang  
**Category**: cs.AI  
**Published**: 2026-05-27  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2605.26546v1  

#### Abstract
Mobile graphical user interface (GUI) agents enable AI models to autonomously operate smartphones on behalf of users. However, most existing systems focus primarily on optimizing task accuracy and rely on cloud-hosted models for inference, which introduces privacy concerns and network-dependent late...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：MobileExplorer: Accelerating On-Device Inference for Mobile GUI Agents via Online Exploration**

---

## **1. 论文的主要贡献和创新点**

### **解决了什么问题**
当前大多数 Mobile GUI Agent 系统依赖于云端运行的 **VLM**（Vision-Language Models）进行推理，虽然提升了任务准确率，但也带来了严重的**隐私风险**和**网络延迟**。此外，**完全在设备端部署**（on-device deployment）的 GUI Agent 仍面临以下挑战：
- **VLM 推理延迟高**：在资源受限的移动设备上，视觉模型推理耗时长（如 MAI-UI-2B 在 Galaxy S24 上需约 40 秒）。
- **交互效率低**：现有系统采用串行的“感知-推理-操作”流程，在 VLM 推理期间设备处于空闲状态，造成时间浪费。
- **动态界面适应难**：移动端界面频繁弹窗、内容变化，导致多轮推理累积延迟严重。

### **提出了什么新方法或新思路**
提出 **MobileExplorer**，一种全新的**全设备端部署的视觉型 Mobile GUI Agent 框架**，其核心思想是：
> 利用 VLM 长推理时间窗口，**并行执行轻量级的在线探索**（online exploration），主动探测 UI 元素以收集任务相关上下文信息，并将这些信息转化为结构化提示注入后续推理步骤。

#### **关键技术组件**：
- **Task Relevance-driven Exploration**  
  使用轻量级文本嵌入模型（如 Sentence-BERT）计算候选 UI 元素与任务描述之间的语义相似度，优先探索语义相关且可点击的元素。
  
- **Two-level Rollback Mechanism**  
  设计两级回滚机制确保探索后能可靠恢复原始 UI 状态：
  - **Level-1**：深度限制的 `Back` 回溯 + 基于 **pHash**（perceptual hash）的状态验证；
  - **Level-2**：若 Level-1 失败，则返回 Home 并重放历史动作轨迹重建初始状态。

- **Exploration-Augmented Reasoning**  
  将探索过程中发现的 UI 路径和元素总结为简洁的文本提示（contextual hints），附加到下一推理步的 prompt 中，增强决策准确性。

### **相比现有方法的优势**
| 维度 | 现有方法 | MobileExplorer |
|------|--------|----------------|
| **部署方式** | 多数依赖云推理 | 完全 on-device，保护隐私 |
| **时间利用** | 推理期间空闲 | 利用推理延迟进行并行探索 |
| **知识获取** | 依赖离线构建的知识库或静态树 | 在线实时探索，适应动态环境 |
| **鲁棒性** | 易受弹窗、状态漂移影响 | 双重回滚机制保障状态一致性 |

---

## **2. 核心实验方法和设置**

### **使用的数据集**
- **AndroidWorld Benchmark** [13]：一个面向真实智能手机界面的任务导向型 GUI 交互基准，支持闭环交互（通过 ADB 控制真实应用），涵盖音频录制、笔记管理、费用添加等多类任务。
  - 总共 116 个任务，按难度分为：
    - Easy: 52.6%
    - Medium: 31.0%
    - Hard: 16.4%

- **自定义现实场景任务集**：用于评估复杂 UI、弹窗干扰和资源动态下的表现，包括：
  - 复杂 UI 密集页面（如 Trip.com 页面平均含 48 个可交互元素）
  - 弹窗干扰（alarm, message, call, app notification）
  - 资源竞争（后台播放视频/音乐影响 CPU/Memory）

### **实验设置**
- **设备平台**：
  - Samsung Galaxy S24（手机）
  - NVIDIA Jetson AGX Orin（边缘设备）
  - MacBook Air M4（笔记本）
- **模型实现**：
  - 使用 `llama.cpp` + Q8 量化部署 VLM（主要基于 4B 规模的 STEP-UI 或 MAI-UI）
  - Agent 与模型通过 vLLM 提供的 API 通信
  - 在 Termux 中运行本地推理模拟真实 on-device 场景

### **评估指标**
| 指标 | 定义 |
|------|------|
| **Success Rate (%)** | 成功完成任务的比例 |
| **Average Steps** | 完成任务所需的平均交互步数 |
| **Step Latency** | 单步从截图到动作执行的时间 |
| **End-to-End Latency (s)** | 整体任务完成时间（所有 step latency 之和） |
| **Hint-Follow Rate** | 模型是否采纳探索生成的提示 |

### **基线方法对比**
- **M3A Agent**：标准 VLM-based 顺序推理 Agent
- **T3A Agent**：基于 accessibility tree 的 LLM 推理 Agent
- **Input-pruning VLM agent**：通过裁剪截图或 token 减少输入开销
- **Offline Exploration Agent**：依赖预先构建的 UI 知识图谱（如 GUI-Explorer, LLM-Explorer）

---

## **3. 主要实验结果和性能指标**

### **关键性能数据**
| 方法 | Success Rate (%) | Avg. Steps | End-to-End Latency (s) |
|------|------------------|-----------|-------------------------|
| **MobileExplorer** | **50.9%** | **9.24** | **185.82** |
| M3A (Baseline) | 46.55% | 10.93 | 220.89 |
| T3A (Qwen3-4B) | ~30% | — | — |
| Input-Prune | ~45% | ~10.5 | ~210 |

> ✅ **相对提升**：
> - 成功率最高达 **50.9%**，相较 M3A 提升 **9.3% 绝对值**（~5% 相对提升）
> - 平均减少 **15.5% 的交互步数**
> - **端到端延迟降低 15.9%**，在某些配置下可达 **23% 的延迟压缩**

### **与基线方法的对比结果**
- MobileExplorer 在 AndroidWorld 上取得当前最优成功率（SOTA），显著优于其他 on-device 和 cloud-based 方法。
- 相比 input-pruning 方法，MobileExplorer 不牺牲视觉细节即可提速，避免因过度裁剪导致 grounding 错误。
- 相比 offline exploration 方法，MobileExplorer 无需预训练知识库，适应性强，尤其适合未见过的应用。

### **消融实验结果（Ablation Study）**
| 变体 | Success Rate | End-to-End Latency |
|------|-------------|--------------------|
| Full MobileExplorer | **50.9%** | **185.82s** |
| w/o Task Relevance Selection | 42.2% | ↑ |
| w/o Two-level Rollback | 39.7% | ↑↑ |
| w/o Exploration Alignment | 47.4% | ↑ |

> 🔍 发现：
> - **任务相关性选择** 对性能至关重要，随机探索效果差。
> - **双层回滚机制** 是系统鲁棒性的关键，缺失时失败率大幅上升。
> - **探索-推理对齐** 有效过滤无关信息，防止噪声干扰。

---

## **4. 关键结论和发现**

### **主要发现**
1. **VLM 推理延迟是一个可被利用的时间窗口**，而非纯粹开销。MobileExplorer 成功将“等待时间”转化为“探索时间”，实现了**计算与交互的并行化**。
2. **轻量级在线探索 + 结构化提示注入** 能显著提升每步推理质量，减少试错行为，从而缩短整体任务路径。
3. **双层回滚机制** 极大增强了在真实动态环境中探索的安全性和可靠性，解决了传统 backtracking 不可逆的问题。
4. 方法在多种设备（手机、Jetson、MacBook）上均有效，具备良好的跨平台兼容性。

### **方法的局限性**
- **探索深度受限**：由于必须在单步推理时间内完成，探索路径较短，难以覆盖深层嵌套菜单。
- **依赖 accessibility tree**：虽然比纯视觉解析快，但在 accessibility 支持不佳的应用中可能失效。
- **提示注入策略较简单**：目前使用模板化摘要，未来可引入更智能的 summarization 策略。

### **未来工作方向**
- 开发**自适应探索策略**，根据任务复杂度动态调整探索深度与广度。
- 探索 **exploration 与 reasoning 的更深层次协同机制**，例如让 VLM 参与指导探索方向。
- 扩展至 **multi-app 跨应用任务** 和 **long-horizon planning** 场景。
- 结合 **SLM**（Small Language Model）进一步优化端侧推理效率。

---

> 📽️ **演示视频**：https://youtu.be/thK7MJmdlvM  
> 💻 **代码开源计划**：论文接受后将公开源码（见 footnote 1）

</details>

---

### 7. [RAPNet: Accelerating Algebraic Multigrid with Learned Sparse Corrections](https://arxiv.org/abs/2605.26854)

**Authors**: Yali Fink, Ido Ben-Yair, Lars Ruthotto, Eran Treister  
**Category**: cs.LG  
**Published**: 2026-05-27  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2605.26854v1  

#### Abstract
The scalable solution of large sparse linear systems is a bottleneck in scientific computing and graph analysis. While algebraic multigrid (AMG) offers optimal linear scaling, its performance is severely constrained by the trade-off between the sparsity and convergence quality of coarse-grid operato...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：RAPNet: Accelerating Algebraic Multigrid with Learned Sparse Corrections

---

## 1. 主要贡献和创新点

### **解决的问题**
在科学计算和图分析中，求解大规模稀疏线性系统 $Ax = b$ 是一个核心瓶颈。**代数多重网格 (AMG)** 虽然具有最优的线性复杂度，但其性能受限于粗网格算子（coarse-grid operators）的**稀疏性与收敛质量之间的权衡**：
- 经典的平滑聚合（Smoothed Aggregation, SA）能提升收敛速度，但会导致**算子密度显著增加**（stencil growth），带来高昂的并行通信和计算开销。
- 非 Galerkin 方法通过稀疏化来缓解此问题，但仍需先计算稠密的 Galerkin 算子 $R A P$，无法从根本上避免计算瓶颈。

### **提出的新方法**
作者提出了 **RAPNet** —— 一种基于图神经网络（GNN）的框架，用于学习对 AMG 中粗网格算子的**稀疏加法修正**（sparse additive corrections）。

#### **核心思想与创新**
- **学习稀疏修正而非稠密算子**：RAPNet 不直接学习稠密的 $P$ 或 $R$，而是在经典未平滑聚合（unsmoothed aggregation）提供的稀疏结构基础上，学习增量式的 $\Delta P, \Delta R, \Delta A_{l+1}$，从而保持极低的算子复杂度。
- **仅在 setup 阶段执行神经推理**：所有 GNN 推理发生在求解器构建阶段（setup phase），一旦层次结构被增强，后续的 solve 阶段完全由标准 AMG 迭代组成，保留了 AMG 的高效性和可预测性。
- **层级式训练策略（Level-wise Training）**：
  - 将整个 AMG 层次视为一系列相邻层级对 $(l, l+1)$。
  - GNN 在每一对上独立操作，并通过隐藏状态混合机制传递跨层级依赖。
  - 该设计实现了**尺度不变性**（scale-invariance），允许模型在小图上训练，在百万节点大图上推理，甚至处理更深的层次。

### **相比现有方法的优势**
| 方面 | RAPNet | 其他神经加速方法 |
|------|--------|------------------|
| **稀疏性保证** | ✅ 结构上强制稀疏 | ❌ 多数为稠密注意力或全连接层 |
| **推理效率** | ✅ 仅 setup 阶段一次前向传播 | ❌ 每次迭代都需要 GNN 推理 |
| **可扩展性** | ✅ 支持深层层次和大规模图 | ❌ 多数限于两层或小规模 |
| **多 RHS 支持** | ✅ setup 后支持任意右端项 $b$ | ❌ 很多方法绑定特定 $b$ |

---

## 2. 核心实验方法和设置

### **使用的数据集**
实验覆盖了多种类型的稀疏矩阵来源：
1. **几何图（Geometric Graphs）**  
   - 2D/3D 单位方块/立方体上的随机点 Delaunay 三角剖分。
2. **复杂网络拓扑**
   - **Watts-Strogatz 图**：具有“小世界”特性的图。
   - **Temporal Barabasi-Albert (TBA) 图**：动态扩展的无标度网络，用于超拉普拉斯（supra-Laplacian）分析。
   - **Social Hub 图**：合成社交网络，含高度连接的枢纽节点。
3. **PDE 离散化系统**
   - **各向异性扩散 (Anisotropic Diffusion)**：非对称、强方向性扩散张量。
   - **对流-扩散 (Advection-Diffusion)**：非对称主导问题，挑战性强。

> 所有测试实例均达到 **10万至100万变量（Vars）级别**，部分超过百万。

### **实验设置与评估指标**

#### **评估方式**
- **作为独立求解器（Standalone Solver）**：运行 AMG V-cycle 直到相对残差降至 $10^{-6}$。
- **作为预处理器（Preconditioner）**：嵌入 GMRES(2) 迭代法中。

#### **主要评估指标**
- **迭代次数（Iteration Count）**：达到收敛所需的平均迭代数（越少越好）。
- **收敛率（Convergence Rate）**：是否稳定收敛（见 Table 12）。
- **Setup 时间**：构建增强型 AMG 层次所需时间。
- **算子复杂度（Operator Complexity）**：衡量粗网格算子总非零元与细网格之比（越接近1越好）。

#### **基线方法对比**
- **AGG**：基础未平滑聚合 AMG，最稀疏但收敛慢。
- **SpSA (Sparsified Smoothed Aggregation)**：经典非 Galerkin 方法，先平滑再稀疏化，代表当前高性能 AMG 基线。

---

## 3. 主要实验结果和性能指标

### **关键性能数据（来自 Table 1）**

| 实验类别 | 方法 | 平均迭代数（Standalone） | 平均迭代数（GMRES Precond） |
|---------|------|--------------------------|----------------------------|
| **3D Geometric** | AGG | 145±18 | 42±5 |
| | SpSA | 65±8 | 32±2 |
| | **RAPNet** | **71±6** | **34±2** |
| **Watts-Strogatz** | AGG | 446±135 | 472±434 |
| | SpSA | 689±380 | 450±452 |
| | **RAPNet** | **317±59** | **123±22** |
| **Temporal Barabasi-Albert** | AGG | 106±13 | 28±3 |
| | SpSA | 90±152 | 25±25 |
| | **RAPNet** | **85±45** | **44±7** |
| **Social Hub** | AGG | 61±166 | 13±4 |
| | SpSA | 978±115 | 34±94 |
| | **RAPNet** | **18±12** | **9±1** |
| **3D Advection-Diffusion** | AGG | 906±285 | 80±28 |
| | SpSA | 875±324 | 42±9 |
| | **RAPNet** | **62±15** | **38±5** |

> ✅ **RAPNet 在几乎所有任务中显著减少迭代次数**，尤其在复杂图和非对称 PDE 上优势明显。

### **与基线方法的对比结果**
- **收敛速度**：
  - RAPNet 的迭代次数普遍低于 AGG 和 SpSA，特别是在高连通性图（如 Social Hub）上，SpSA 因 stencil growth 导致严重退化，而 RAPNet 仍保持高效。
  - 在 3D 对流-扩散问题中，RAPNet 作为独立求解器仅需约 60 次迭代，远优于 AGG (~900) 和 SpSA (~875)。
- **稳定性**（Table 12）：
  - AGG 和 SpSA 在多个 Advection-Diffusion 实例上发散（diverge），而 RAPNet **100% 成功收敛**。
- **Setup 效率**（Table 2）：
  - RAPNet 的 setup 时间显著低于 SpSA，尤其是在高连通图上（如 Social Hub, 300K vars）：
    - SpSA: **973 秒**
    - RAPNet: **0.76 秒**（GPU）
  - 即使在 CPU 上运行（Table 11），RAPNet 的 setup 时间也仅为十几到几十秒，具备实用价值。

### **消融实验结果（Table 3）**
在 3D 几何图上的 ablation study 显示：
| 变体 | 128K vars 迭代数 | 512K vars 迭代数 |
|------|------------------|------------------|
| 完整 RAPNet | 59±5 | 71±6 |
| w/o $\Delta P, \Delta R$ | 99±10 | 113±13 |
| w/o $\Delta A_{l+1}$ | 83±7 | 98±11 |
| w/o mixing（无层级状态传递） | 68±6 | 81±8 |

> 🔍 结果表明：
> - 所有组件（$\Delta P, \Delta R, \Delta A_{l+1}$ 和状态混合）都对性能有贡献。
> - 缺少任一组件都会导致收敛变慢，验证了设计的有效性。

---

## 4. 关键结论和发现

### **主要发现**
1. **成功打破稀疏性-收敛性权衡**：RAPNet 通过 GNN 学习稀疏修正，在不牺牲稀疏性的前提下，实现了媲美甚至超越 SpSA 的收敛速度。
2. **真正实现“一次性学习，多次使用”**：神经网络仅参与 setup，solve 阶段完全传统化，适合部署于高性能计算环境。
3. **卓越的泛化能力**：
   - 在 **4000 节点的小图上训练**，可在 **百万级大图上推理**。
   - 在 **2D 结构化网格上训练**，可推广至 **3D 非结构化复杂域**。
4. **在最难问题上表现最佳**：对于高连通图和强非对称 PDE（如 advection-dominated flow），RAPNet 显著优于传统方法，且稳定性更高。

### **局限性**
1. **未优化 Smoother 参数**：当前框架固定使用阻尼 Jacobi 平滑，未学习最优 damping factor 或更高级的 smoother。
2. **未学习聚合过程本身**：节点聚类（aggregation）仍采用经典启发式算法，未由 GNN 学习生成。
3. **缺乏理论保证**：尽管实验效果优异，但目前没有关于所生成预处理器的收敛性理论证明（非 Galerkin 理论仅适用于小扰动）。
4. **依赖初始 AGG 结构**：性能上限受制于初始未平滑聚合的质量。

### **未来工作方向**
- 将 GNN 扩展至学习 **node clustering / aggregation policy**。
- 探索 **自适应 smoother 设计**，联合优化平滑与插值。
- 引入 **理论分析工具**，为 learned non-Galerkin cycles 提供收敛性保障。
- 应用于更多物理场耦合系统（如 Navier-Stokes, Maxwell 方程等）。

--- 

> 📌 **总结一句话**：  
> **RAPNet 是首个将 GNN 与 AMG 完美结合的方法——它用一次 setup 阶段的轻量级神经推理，换取了在整个 solve 过程中对收敛速度的大幅提升，同时严格保持稀疏性与可扩展性，为机器学习赋能科学计算提供了新范式。**

</details>

---

### 8. [Totoro$^+$: An Adaptive and Scalable Edge Federated Learning System](https://arxiv.org/abs/2605.26323)

**Authors**: Cheng-Wei Ching, Xin Chen, Taehwan Kim, Jian-Jhih Kuo, Dilma Da Silva, Liting Hu  
**Category**: cs.DC  
**Published**: 2026-05-27  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.26323v1  

#### Abstract
Federated Learning (FL) is an emerging distributed machine learning (ML) technique that enables in-situ model training and inference on decentralized edge devices. We propose Totoro$^+$, a novel scalable FL system that enables massive FL applications to run simultaneously on edge networks. The key i...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文《Totoro+: An Adaptive and Scalable Edge Federated Learning System》核心总结

---

## 1. 主要贡献和创新点

### 解决的问题
本文针对**边缘计算环境下的联邦学习（Federated Learning, FL）系统**在大规模部署时面临的两大核心挑战：

- **可扩展性瓶颈（Scalability Bottleneck）**：传统 FL 系统依赖中心化的参数服务器（Parameter Server），当同时运行大量 FL 应用时，该服务器成为单点瓶颈，导致训练延迟高、负载不均。
- **适应性差（Poor Adaptivity）**：边缘网络具有动态性（如节点频繁加入/离开）、带宽受限、链路不稳定等特点，现有系统难以快速适应这些变化。

### 提出的新方法与创新思路
作者提出了 **Totoro+**，一个全新的、完全去中心化的边缘联邦学习系统，其核心创新在于以下三点：

#### （1）基于 DHT 的 P2P 多环结构（Locality-aware P2P Multi-ring Structure）
- 利用 **Distributed Hash Table (DHT)** 构建一个自组织的 P2P 覆盖网络（Overlay Network）。
- 将全局大环划分为多个“多环”（multi-ring），每个环对应一个地理或管理上的“边缘区”（edge zone），支持本地化控制和管理隔离。
- 实现了 `O(log N)` 跳数内的高效路由，解决了大规模下模型分发与梯度聚合的效率问题。

#### （2）发布/订阅式的森林抽象（Publish/Subscribe-based Forest Abstraction）
- 每个 FL 应用独立构建一棵**动态结构的数据流树（dataflow tree）**，用于模型广播和梯度聚合。
- 引入 **Advertise-Discover Tree (AD Tree)**，实现 FL 应用的自动广告与发现，无需外部协调。
- 所有数据流树与 AD Tree 构成一个“森林”，实现了真正的“多主多工”（many masters / many workers）架构，彻底消除中心化协调器。

#### （3）基于博弈论的路径规划模型（Game-theoretic Path Planning Model）
- 将路径选择建模为一个**拥塞博弈（Congestion Game）**，考虑节点间的资源竞争。
- 设计了一个分布式、逐跳的路由算法，利用 Bandit 反馈学习最优路径。
- **理论保证**：该算法能收敛到 **e-approximate Nash Equilibrium**，确保系统稳定性和公平性。

### 相比现有方法的优势
| 维度 | 传统系统（如 OpenFL, FedScale） | Totoro+ |
|------|-------------------------------|--------|
| 架构 | Centralized / Hierarchical | Fully Decentralized |
| 参数服务器 | 单一共享 | 每应用专用 |
| 可扩展性 | 随应用数增长而下降 | 线性扩展，无瓶颈 |
| 适应性 | 固定路径，难应对动态 | 动态重规划，抗 churn 和拥塞 |
| 应用发现 | 依赖外部机制 | 内置 AD Tree 支持 |

---

## 2. 核心实验方法和设置

### 使用的数据集
- **语音识别任务**：`Google Speech` 数据集（目标准确率 53.0%）
- **图像分类任务**：`FEMNIST` 数据集（目标准确率 75.5%）
- **真实世界边缘拓扑**：`EUA Dataset`（澳大利亚 95,271 个基站位置，模拟边缘节点分布）

### 实验设置
- **平台**：500 台 AWS EC2 `t2.medium` 节点（每台 2 vCPU, 4GB RAM）
- **模拟规模**：通过 JVM 模拟最多 100,000 个边缘节点
- **网络分区**：将节点按地理位置划分为多个“边缘区”
- **对比基线**：
  - **OpenFL**：Intel 开源的集中式 FL 框架
  - **FedScale**：Symbiotic Lab 开发的大规模 FL 基准框架
- **Totoro+ 配置**：测试不同 `fanout`（8, 16, 32）对性能的影响

### 评估指标
| 指标类别 | 具体指标 |
|---------|--------|
| **可扩展性** | 数据流树分布、主节点负载均衡、`O(log N)` 路由跳数验证 |
| **FL 性能** | **Time-to-Accuracy**（达到目标准确率所需总训练时间） |
| **适应性** | 累积包延迟（Cumulative Packet Latency）、Nash Regret、故障恢复时间 |
| **开销** | CPU/Memory 开销、通信成本（TCP/UDP 流量） |

---

## 3. 主要实验结果和性能指标

### 关键性能数据与对比结果

#### （1）训练速度显著提升（Time-to-Accuracy）
在并发运行 5~20 个 FL 应用时，Totoro+ 相比基线大幅加速：

| 任务 | 数据集 | 并发应用数 | Totoro+ 加速比（vs OpenFL） | Totoro+ 加速比（vs FedScale） |
|------|--------|------------|-----------------------------|------------------------------|
| 语音识别 | Google Speech | 20 | **13.0× ~ 14.0×** | **12.4× ~ 13.5×** |
| 图像分类 | FEMNIST | 20 | **5.0× ~ 10.3×** | **5.6× ~ 11.5×** |

> ✅ **结论**：随着并发应用数增加，Totoro+ 的优势越明显，因其并行处理能力避免了中心调度队列。

#### （2）可扩展性优异
- **主节点负载均衡**：在 1000 节点区域中创建 2000 棵数据流树，99.5% 的节点作为根节点不超过 3 次，表明负载高度分散。
- **路由效率**：模型分发与梯度聚合的跳数随节点数呈 `O(log N)` 增长，在百万级节点下仍保持低延迟。

#### （3）通信成本低
- 当数据流树数量增加 10 倍时，Totoro+ 的额外网络流量仅增加：
  - **TCP**: 1.19×
  - **UDP**: 1.29×
- 远低于传统系统因广播带来的指数级增长。

#### （4）强适应性与鲁棒性
- **动态路径规划**：相比 Bandit-based 方法，Totoro+ 的累积延迟更低，且 Nash Regret 更快收敛，证明其能有效应对拥塞。
- **故障恢复**：
  - 单棵树中同时失败 128 个节点，恢复时间线性增长（约 1.5 秒）。
  - 多棵树同时失败，恢复时间稳定，支持并行修复。

#### （5）资源开销可控
- **CPU 开销**：DHT 相关操作引入的额外 CPU 开销极小，适合资源受限边缘设备。
- **内存开销**：训练期间内存使用平稳，无持续增长。

---

## 4. 关键结论和发现

### 主要发现
1. **去中心化是解决大规模边缘 FL 的关键**：通过 DHT + 发布/订阅机制，Totoro+ 成功将“单主多工”转变为“多主多工”，从根本上解决了可扩展性瓶颈。
2. **内置的应用发现机制至关重要**：AD Tree 实现了 FL 应用的自主广告与发现，提升了系统的自治能力。
3. **博弈论路径规划优于传统 Bandit 方法**：考虑节点间资源竞争的模型更符合现实边缘网络，能实现更优的负载均衡与稳定性。
4. **系统具备良好的弹性与容错性**：支持动态节点加入/退出，并能在主节点或工作节点失效后快速恢复。

### 方法的局限性
- **安全与信任问题未深入探讨**：当前设计假设节点是合作的，未充分考虑恶意节点发起的攻击（如虚假应用广告、梯度污染）。
- **逻辑节点映射策略需手动配置**：异构资源节点到逻辑 P2P 节点的映射规则需要预设，缺乏自动化决策。
- **理论分析基于理想化假设**：如 Nash Equilibrium 的收敛性依赖于某些平滑性和独立性假设，在极端非稳态环境下可能受影响。

### 未来工作方向
1. **增强安全性**：引入可信认证机构（如 CA）对节点和应用进行身份验证，防止恶意行为。
2. **支持多播（Multicast）**：扩展当前逐跳单播模型为多播，进一步提升通信效率。
3. **开放社区平台集成**：探索在众包式 FL 平台（crowdsourcing-based FL）中的应用，结合激励机制。
4. **支持非独立同分布（Non-IID）数据场景**：允许应用层自定义数据过滤、客户端选择等策略以应对数据异构性。

---

> **总结**：Totoro+ 是一个面向未来超大规模边缘联邦学习的系统级创新，它通过 **DHT + 发布/订阅 + 博弈论路由** 的三重设计，实现了前所未有的可扩展性、适应性和效率，为构建真正去中心化、自治化的边缘智能基础设施提供了坚实基础。

</details>

---

### 9. [From Norms to Indicators (N2I-RAG): An Agentic Retrieval-Augmented Generation Framework for Legal Indicator Computation](https://arxiv.org/abs/2605.26926)

**Authors**: Youssef Al Mouatamid, Marie Bonnin, Jihad Zahir  
**Category**: cs.AI  
**Published**: 2026-05-27  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.26926v1  

#### Abstract
Computing legal indicators from normative texts is a key task in legal monitoring and policy evaluation, but presents significant challenges due to the complexity, scale, and interpretive nature of legal language, as well as the variability in available document quality. Existing natural language pr...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：From Norms to Indicators (N2I-RAG)

## 1. 论文的主要贡献和创新点

### 解决的问题
本论文旨在解决**法律指标（legal indicator）自动化计算中的可靠性、可解释性和可追溯性不足**的问题。传统方法依赖专家手动分析，效率低且难以扩展；而现有的 NLP 和 LLM 方法虽然能辅助法律文本处理，但存在以下缺陷：
- **高幻觉风险（hallucination）**：LLM 可能生成无事实依据的结论；
- **缺乏可解释性**：模型输出为“黑箱”，无法追踪推理过程；
- **检索僵化**：标准 RAG 流程固定，难以动态优化查询与证据筛选。

这些问题在需要高度准确性和问责制的法律领域尤为致命。

---

### 提出的新方法：N2I-RAG 框架
作者提出 **N2I-RAG（From Norms to Indicators - Retrieval-Augmented Generation）**，一个基于**多智能体系统（multi-agent system）的 RAG 架构**，用于从规范性法律文本中自动、透明地计算法律指标。

#### 核心创新点：
1. **Agentic RAG 架构设计**
   - 引入多个专业化 **LLM-based Agents**，各司其职，形成闭环推理流程：
     - `Metadata Retriever`：提取查询相关的元数据（如国家、时间）
     - `Context Retriever`：基于语义向量检索相关法律条文
     - `Context Grader`：评估检索结果的相关性与特异性
     - `Query Disambiguator`：重写模糊或泛化的用户提问
     - `Generator Agent`：基于上下文生成自然语言回答
     - `Groundedness Grader`：验证每项声明是否被原文支持
     - `Answer Relevance Grader`：检查答案是否回应原始问题
     - `Binary QA Agent`：将最终输出转化为 0/1 二元标签，填入评估网格

2. **强调 Traceability 与 Interpretability**
   - 所有中间决策均附带**显式解释（explanation）**，确保每一步都可审查；
   - 最终输出不仅给出判断，还提供完整证据链，实现**端到端可追溯**。

3. **模块化控制机制抑制幻觉**
   - 通过 `Grading` 和 `Validation` 类 Agent 构建反馈回路，主动识别并过滤不可靠信息；
   - 将开放生成任务转化为受控的信息抽取 + 验证流程。

---

### 相比现有方法的优势
| 维度 | 传统方法 / 基础 RAG | N2I-RAG |
|------|---------------------|--------|
| 幻觉控制 | 弱，依赖单一生成步骤 | 强，多级验证机制 |
| 可解释性 | 差，“黑箱”输出 | 高，每个环节均有解释 |
| 检索灵活性 | 固定检索策略 | 支持查询重写与自适应检索 |
| 输出标准化 | 多样化文本 | 结构化二元指标（0/1），便于政策比较 |
| 泛化能力 | 依赖训练数据 | 基于检索，对新法域更具适应性 |

> ✅ **优势总结**：N2I-RAG 在保持 LLM 强大语言理解能力的同时，通过**结构化代理协作与验证机制**，实现了更可靠、可审计的法律分析框架。

---

## 2. 核心实验方法和设置

### 数据集构建（Dataset Construction）
- 名称：**French Marine Environmental Law Corpus**
- 来源：联合国粮农组织 FAOLEX 数据库
- 覆盖范围：非洲法语行政国家及法国，共 **15 个国家**
- 内容类型：法律、法规、指令等环境类文件（扫描件与数字版混合）
- 总数：**10,596 篇法律文章**
- 主题聚焦：两个禁令（ban）作为案例研究：
  - 塑料袋禁令（Plastic Bags Ban）
  - 底拖网捕捞禁令（Bottom Trawling Ban）
- 额外引入三个干扰主题以测试检索鲁棒性（如海岸建设、鲸鱼狩猎等）

> 文档预处理流程：
> - 使用 **Visual-Language Model (VLM)** 进行 OCR，提升低质量扫描件的文本恢复；
> - 分段为法律条文，并添加标准化元数据（管辖权、发布日期、修订日期、机构来源等）；
> - 使用 **BGE-M3** 模型进行嵌入编码，存入 **ChromaDB** 向量数据库供语义搜索。

---

### 实验设置

#### 模型选择
本地运行三种主流开源 LLM，验证框架通用性（LLM-agnostic）：
- **Llama3.2:3B**
- **Qwen3:8B**
- **Mistral-Nemo:12B**

#### 实现工具
- 框架编排：LangChain + LangGraph
- LLM 执行：Ollama
- 向量检索：ChromaDB + BGE-M3，top_k=10

#### 生成参数
- 确定性任务（评分、二分类）：temperature = 0
- 创造性任务（查询重写）：temperature = 0.9

---

### 评估指标（Evaluation Metrics）
采用标准分类指标，但赋予法律意义解读：

| 指标 | 法律含义 |
|------|---------|
| **Accuracy** | 整体正确率 |
| **Recall (Sensitivity)** | 是否漏判有效法律 → 影响合规诊断完整性 |
| **Specificity** | 是否误报不存在的法律 → 控制假阳性（false positive），避免误导监管 |
| **Precision** | 报告“有法”的情况中有多少是真的 |
| **F1-Score** | 精确率与召回率平衡，反映系统稳健性 |
| **Balanced Accuracy** | (Sensitivity + Specificity)/2，适用于类别不平衡场景 |
| **FPR / FNR** | 错误类型分析，尤其关注法律后果严重的 false positive |

---

### 基线方法对比
测试三种配置以验证组件有效性：
1. **Full Pipeline**：完整 N2I-RAG 框架（所有 agents 激活）
2. **Without-Hallucination Control**：移除 `Groundedness Grader`, `Answer Relevance Grader` 等验证模块
3. **Baseline (Retrieval-only)**：仅使用 ChromaDB 向量检索 + 直接生成，无 agent 控制

> 对比目的：验证 multi-agent 控制机制的实际增益。

---

## 3. 主要实验结果和性能指标

### 全局性能表现（Across Models）
使用 **Mistral-Nemo:12B** 时达到最优性能：

| 指标 | Full Pipeline | Without-Hall | Baseline |
|------|---------------|--------------|----------|
| **Balanced Accuracy** | **0.933** | 0.661 | 0.646 |
| **F1-Score** | **0.943** | 0.714 | 0.469 |
| **Specificity** | **0.919** | 0.564 | 0.723 |
| **Recall** | **0.947** | 0.758 | 0.584 |

> ⬆️ **关键发现**：加入 N2I-RAG 框架后，Mistral-Nemo 的 Balanced Accuracy 提升近 **30%**，F1 提升超 **20%**，说明架构本身显著增强性能。

不同模型均受益于该框架，证明其 **LLM-agnostic 特性**。

---

### 按禁令拆分的结果（Table 4）

#### 塑料袋禁令（Plastic Bag Ban）
| 配置 | Accuracy | F1-Score | Balanced Acc. |
|------|----------|-----------|----------------|
| Full | 0.975 | 0.980 | **0.981** |
| Without-Hall | 0.843 | 0.855 | 0.842 |
| Baseline | 0.777 | 0.809 | 0.768 |

#### 底拖网禁令（Bottom Trawling Ban）
| 配置 | Accuracy | F1-Score | Balanced Acc. |
|------|----------|-----------|----------------|
| Full | 0.872 | 0.865 | **0.876** |
| Without-Hall | 0.782 | 0.753 | 0.778 |
| Baseline | 0.564 | 0.553 | 0.567 |

> 🔍 **观察**：
> - 完整框架在两个任务上均大幅领先；
> - “Without-Hall”版本虽优于纯检索，但仍明显劣于全框架 → 表明 **验证 agents 至关重要**；
> - 在底拖网任务中，baseline 几乎失效（Balanced Acc ≈ 0.57），凸显复杂法律背景下简单 RAG 的局限。

---

### 消融实验（Ablation Study）结论
- **验证模块缺失导致 specificity 显著下降**：
  - 如底拖网任务中，specificity 从 0.837（Full）降至 0.535（Without-Hall）；
  - 意味着系统更容易“虚构”法律存在（high false positive rate），这在法律应用中是灾难性的。
- **multi-agent 协作提升了 factual consistency 和 decision stability**；
- 框架性能提升不依赖单一强大 LLM，而是来自**流程设计本身的结构性优势**。

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **Agentic RAG 显著优于传统 RAG 和纯检索方法**  
   多智能体协同机制有效减少了 hallucination，提高了 legal indicator 计算的准确性与可信度。

2. ✅ **Traceability 与 Interpretability 可工程化实现**  
   每个 agent 输出解释，使得整个推理链条透明可视，满足法律系统的问责需求。

3. ✅ **框架具有良好的跨模型迁移能力（LLM-agnostic）**  
   不同规模的 LLM 均能在 N2I-RAG 下获得性能提升，表明其价值在于**架构设计而非特定模型能力**。

4. ✅ **验证机制是降低 false positive 的关键**  
   移除 `Groundedness Grader` 和 `Answer Relevance Grader` 导致 specificity 断崖式下跌，突显这些模块在法律场景中的必要性。

5. 📌 **错误主要源于数据而非模型技术缺陷**
   - **Data gaps**：某些处罚条款存在于未收录的实施细则中（如科特迪瓦）；
   - **Transitional misinterpretation**：将阶段性实施误解为临时限制（如刚果民主共和国）；
   > → 表明当前瓶颈更多在于**法律文本的完整性与可访问性**，而非 AI 自身能力极限。

---

### 方法的局限性
1. **依赖高质量文档获取与 OCR 能力**  
   尽管使用 VLM 提升 OCR 效果，但严重损坏或非标准格式文档仍可能影响输入质量。

2. **法律解释的边界挑战**  
   当前框架擅长识别明确规则，但在处理隐含义务、比例原则、司法裁量等高级法律推理时仍有局限。

3. **二元输出简化现实复杂性**  
   将法律判断压缩为 0/1 可能忽略部分“部分合规”或“有条件禁止”的中间状态。

4. **领域依赖性强**  
   当前验证集中于海洋环境法，推广至其他法律领域需重新校准指标定义与 agent prompt。

---

### 未来工作方向
1. **拓展至多语言、多法域（multilingual & multi-jurisdictional）场景**  
   支持全球范围内法律 observatory 的统一监测。

2. **整合实时数据源与动态更新机制**  
   实现法律变化的持续跟踪与指标自动刷新。

3. **增强对过渡期、例外条款、层级规范的理解能力**  
   引入图结构（Knowledge Graph）建模法律体系内部关系。

4. **构建更大规模的标注 legal indicator dataset**  
   推动社区共建 benchmark，促进可复现研究。

5. **探索 human-in-the-loop 机制**  
   允许专家介入修正 agent 决策，形成人机协同法律分析闭环。

---

> 💡 **总体评价**：  
> N2I-RAG 成功搭建了从**自然语言法律文本**到**结构化法律指标**之间的可信桥梁，为建立**透明、可扩展的 Legal Observatory** 提供了坚实的技术基础。它不仅是技术上的进步，更是迈向 **Explainable Legal AI** 的重要一步。

</details>

---

### 10. [Provably Communication-Efficient and Privacy-Preserving Federated Graph Neural Networks](https://arxiv.org/abs/2605.26243)

**Authors**: Zhishuai Guo, Wenhan Wu, Chen Chen, Lei Zhang, Olivera Kotevska, Ravi K Madduri  
**Category**: cs.LG  
**Published**: 2026-05-27  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.26243v1  

#### Abstract
Graph neural networks (GNNs) achieve strong performance on relational data, but real-world graphs are often distributed across organizations that cannot share raw data due to privacy and policy constraints. Existing federated GNN methods either ignore cross-client links, leading to degraded accuracy...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：Provably Communication-Efficient and Privacy-Preserving Federated Graph Neural Networks**

---

## **1. 论文的主要贡献和创新点**

### **解决的问题**
现有的 **Federated GNN**（FedGNN）方法面临三大挑战：
- **建模精度低**：忽略跨客户端边（cross-client edges），导致无法捕捉全局图结构，影响模型性能。
- **通信开销高**：频繁交换节点嵌入（node embeddings）造成大量通信负担。
- **隐私泄露风险**：即使不共享原始数据，交换的中间嵌入仍可能通过推理攻击（如 attribute inference attack）泄露敏感信息。

此外，传统 **Differential Privacy**（DP）在嵌入发布场景下因最坏情况下的 L2 敏感度过高而变得“空洞”（vacuous），难以在实用噪声水平下提供有意义的隐私保障。

---

### **提出的新方法：CE-FedGNN**
作者提出了 **CE-FedGNN**（Communication-Efficient and Privacy-preserving Federated GNN），其核心创新包括：

#### ✅ **1. 通信高效的联邦训练框架**
- 引入 **moving-average estimator** 来持续跟踪并复用节点表示，避免每轮都交换嵌入。
- 只在必要时（如边界节点更新后）**异步、稀疏地**交换聚合后的节点嵌入，显著降低通信频率。
- 将通信复杂度从 $ O(T) $ 降至 $ O(T^{3/4}) $，同时保持 $ O(1/\sqrt{T}) $ 的收敛速率。

#### ✅ **2. 基于 Metric-DP 的隐私保护机制**
- 采用 **Metric Differential Privacy**（metric-DP）替代标准 DP，以嵌入空间中的 L2 距离作为距离度量。
- 隐私预算 $ \epsilon(p) $ 依赖于语义邻域内的距离 $ p $，而非最坏输入扰动，从而在中等噪声水平下仍能提供**非空洞的隐私保证**。
- 利用 **Rényi DP 组合定理** 分析多轮通信下的累积隐私损失，并考虑了“公开队列威胁模型”（public-cohort threat model），即对手知道每轮哪些客户端参与更新。

#### ✅ **3. 收敛性与隐私性的联合理论分析**
- 首次为联邦 GNN 提供了 **带噪声嵌入发布的收敛性分析**，证明在注入高斯噪声的情况下，优化误差仅温和增长。
- 显示嵌入扰动对性能的影响小于模型参数或梯度扰动，支持 metric-DP 设计的有效性。

---

### **相比现有方法的优势**
| 方面 | CE-FedGNN | 现有方法（如 FedAvg, Swift-FedGNN, FedGCN） |
|------|----------|---------------------------------------------|
| **跨客户端建模** | 显式建模，利用 stale 但平滑的嵌入 | 忽略或仅初始化时共享 |
| **通信效率** | $ O(T^{3/4}) $，大幅减少通信轮次 | $ O(T) $ 或更高 |
| **隐私保护** | 提供 (ε, δ)-metric-DP 保证 | 多数无显式隐私机制；若加 DP 则效用严重下降 |
| **理论保障** | 收敛 + 隐私双重可证 | 多为启发式设计，缺乏严格分析 |

---

## **2. 核心实验方法和设置**

### **使用的数据集**

#### 🔹 合成反洗钱（AML）数据集（基于 Altman et al. [4]）
- 模拟银行间交易网络，包含合法与非法资金流动模式。
- 包括三种规模（Small/Medium/Large）和两种欺诈比例（High Illicit / Low Illicit）。
- 客户端数量：4–32，模拟多机构协作场景。

#### 🔹 引用网络基准数据集
- **Cora**, **Citeseer**, **PubMed**, **MSAcademic**
- 图结构清晰，常用于 GNN 性能测试。
- 数据被划分为多个客户端进行联邦学习。

---

### **实验设置与评估指标**

| 设置项 | 描述 |
|-------|------|
| **GNN 架构** | AML任务使用 **GIN** 和 **PNA**；引用网络使用 **GCN** |
| **消息传递层数** | 2层 |
| **邻居采样** | Hop-1 和 Hop-2 采样大小分别为 100（AML）和 10（引用网络） |
| **通信间隔 $ K $** | 默认 32，研究不同 $ K $ 对性能影响 |
| **总迭代数 $ T $** | AML: 30k；引用网络: 2k |
| **评估指标** | 平均 **Macro F1 Score**（跨客户端平均） |

---

### **基线方法对比**
| 基线方法 | 特点 |
|--------|------|
| **SC-GIN/PNA** | 单客户端训练，不协作 |
| **FedAvg-GIN/PNA** | 仅交换模型参数，忽略跨客户端边 |
| **Swift-GIN/PNA** | 偶尔访问全局图，通信较少但建模不完整 |
| **FedGCN-GIN/PNA** | 初始化时共享一次嵌入，后续不再更新 |
| **FedGNN-ST** | 共享过时嵌入（stale），无 moving average |
| **FedSage+** | 局部生成缺失节点，计算开销大 |
| **FedPUB** | 加权聚合更新，需全批量训练，不可扩展 |

---

## **3. 主要实验结果和性能指标**

### **关键性能数据（来自 Tables 1 & 2）**

#### ✅ **表1：AML 数据集上的平均 F1 分数**
| 方法 | HI-Small | HI-Medium | HI-Large | LI-Medium | LI-Large |
|------|---------|-----------|----------|------------|-----------|
| SC-GIN | 0.1526 | 0.3572 | 0.3459 | 0.0746 | 0.0227 |
| FedAvg-GIN | 0.4103 | 0.5421 | 0.6235 | 0.0068 | 0.0000 |
| Swift-GIN | 0.3873 | 0.5689 | 0.6339 | 0.0061 | 0.1294 |
| **CE-FedGNN-GIN** | **0.4916** | **0.6024** | **0.6461** | **0.0828** | **0.1917** |
| **CE-FedGNN-PNA** | **0.6623** | **0.6517** | **0.7114** | **0.2918** | **0.3158** |

> 💡 在所有设置下，尤其是 **LI（低欺诈率）** 场景中，CE-FedGNN 显著优于其他方法，且未崩溃至零预测。

#### ✅ **表2：引用网络上的平均 F1 分数**
| 方法 | Cora | Citeseer | PubMed | MSAcademic |
|------|------|----------|--------|------------|
| FedAvg | 0.1868 | 0.2189 | 0.2855 | 0.2759 |
| Swift | 0.4296 | 0.4023 | 0.6181 | 0.8003 |
| FedGNN-ST | 0.4345 | 0.3972 | 0.6347 | 0.8168 |
| **CE-FedGNN** | **0.4701** | **0.4343** | **0.6517** | **0.8497** |

> 💡 CE-FedGNN 在所有四个标准图数据集上均达到最优性能，验证其泛化能力。

---

### **消融实验结果（Ablation Study, Table 5）**

| 消融配置 | HI-Medium | LI-Medium |
|--------|-----------|-----------|
| 完整 CE-FedGNN | **0.6517** | **0.2918** |
| 移除全局嵌入共享 | 0.5037 | 0.2614 |
| 使用 stale 嵌入（无 moving average） | 0.5382 | 0.1129 |
| 移除梯度 moving average | 0.6457 | 0.3535 |

> 🔍 发现：
> - **moving-average 对嵌入估计至关重要**，尤其在 LI-Medium 上，移除后性能暴跌。
> - 全局嵌入共享是提升性能的关键组件。
> - 梯度 moving average 在多数情况下有益，但在某些不平衡任务中可能略有波动。

---

## **4. 关键结论和发现**

### **主要发现**
1. ✅ **CE-FedGNN 实现了通信效率与建模能力的平衡**：
   - 通过 moving-average 机制有效复用嵌入，允许更长的本地训练周期（$ K=1024 $ 仍有效）。
   - 通信次数减少的同时，准确率高于所有基线。

2. ✅ **Metric-DP 提供了实用且非空洞的隐私保障**：
   - 在 $ \sigma_0 = 0.5 \sim 1.0 $ 的噪声水平下，仍能实现 $ \epsilon < 25 $ 的 (ε,δ)-metric-DP 保证（见 Table 6 & 7）。
   - 相比之下，标准 DP 在相同噪声下会给出 $ \epsilon > 1000 $ 的无意义界限。

3. ✅ **方法对噪声具有鲁棒性**：
   - 如 Figure 2 所示，在 moderate 噪声下性能下降有限，甚至强于 FedAvg。
   - 支持“以可控隐私代价换取可用性”的实际部署策略。

4. ✅ **抵抗属性推断攻击能力强**：
   - AIA 实验显示，重构特征的 MSE 远高于最近邻基线，说明聚合嵌入比原始特征更难逆向。

---

### **局限性**
1. **假设跨客户端边属性可共享**：虽然节点特征保密，但边属性（如交易金额、时间）需双方可见，这在某些场景中可能受限。
2. **moving-average 参数需调优**：平滑系数 $ \gamma $ 和 $ \beta $ 影响性能稳定性。
3. **未完全解决动态图问题**：虽然适用于动态交易流，但未明确处理图拓扑随时间剧烈变化的情况。
4. **metric-DP 依赖距离选择**：$ p $ 的选取（如 k-th nearest neighbor）会影响隐私声明的实际含义。

---

### **未来工作方向**
1. 结合 **secure aggregation** 或 **anonymous shuffling** 进一步增强隐私，引入 subsampling amplification。
2. 扩展到 **dynamic and streaming graphs**，支持实时更新。
3. 探索 **adaptive communication scheduling**，根据嵌入漂移程度决定何时发送更新。
4. 将 metric-DP 应用于更多类型的图表示学习任务，如 link prediction、community detection。

---

> 📌 **总结一句话**：  
> **CE-FedGNN 是首个兼具可证明通信效率、建模准确性与形式化隐私保障的 Federated GNN 框架，通过 moving-average 估计与 metric-DP 的结合，在真实与合成图数据上实现了 SOTA 性能与稳健的隐私-效用权衡。**

</details>

---

### 11. [Generalist Graph Anomaly Detection via Prototype-Based Distillation](https://arxiv.org/abs/2605.26857)

**Authors**: Yiming Xu, Zihan Chen, Zhen Peng, Song Wang, Bin Shi, Bo Dong, Chao Shen  
**Category**: cs.LG  
**Published**: 2026-05-27  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.26857v1  

#### Abstract
Driven by the pressing demand for graph anomaly detection (GAD) in high-stakes domains, the generalist GAD paradigm, which trains a single detector transferable across new graphs, has recently gained growing attention. However, existing methods often rely on scarce and costly annotations for trainin...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Generalist Graph Anomaly Detection via Prototype-Based Distillation

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
现有的 **Graph Anomaly Detection (GAD)** 方法在跨图（cross-graph）场景中存在严重局限性：
- 多数方法需为每个新图重新训练（retraining），计算成本高；
- 现有的“通用型”（generalist）GAD 方法依赖昂贵且稀缺的**异常标签**进行监督训练；
- 部分方法甚至在推理阶段需要少量标注样本（few-shot support），限制了其在真实开放世界中的部署。

本文旨在解决：**如何构建一个无需任何标签、可零样本迁移至未见图的通用图异常检测框架？**

---

### 提出了什么新方法或新思路
作者提出了 **ProMoS**（Prototype-guided Mixture-of-Students），是首个**完全无监督的通用图异常检测框架**，其核心创新如下：

#### （1）基于知识蒸馏（Knowledge Distillation, KD）的范式
- 利用一个**冻结的自监督预训练 GNN 教师模型**（self-supervised GNN teacher）作为正常性先验来源；
- 学生模型通过蒸馏学习教师编码的“正常模式”，避免从零开始学习。

#### （2）混合学生架构（Mixture-of-Students, MoS）
- 包含一个**共享分支**（shared branch）捕捉全局规律；
- 和多个**个性化轻量子模型**（personalized students），通过稀疏路由（Top-K routing）动态激活，建模多样化的局部正常模式；
- 在表达力与效率之间取得平衡。

#### （3）原型引导的软标签蒸馏（Prototype-guided Soft-Label Distillation）
- 引入可学习的语义原型（prototypes）作为空间锚点；
- 教师与学生的输出被映射到共享原型空间，并对齐其分布（使用 KL 散度）；
- 提升跨图泛化能力，避免过拟合于实例级细节。

#### （4）差异感知的承诺与精炼机制（Discrepancy-aware Commitment & Refinement）
- 动态加权机制根据节点可靠性调整梯度，抑制异常节点对原型更新的干扰；
- 承诺损失（commitment loss）稳定教师特征空间；
- 精炼损失（refinement loss）持续优化原型以捕获高质量语义。

#### （5）零样本推理机制
- 推理时无需微调或重训练；
- 异常分数由两项构成：
  - **蒸馏偏差**（distillation bias）：教师软标签 vs 学生预测之间的 KL 差异；
  - **几何偏差**（geometric deviation）：嵌入与其量化原型的距离。

---

### 相比现有方法的优势
| 维度 | ProMoS | 现有方法 |
|------|--------|---------|
| 是否需要标签 | ❌ 完全无监督 | ✅ 多数需监督或半监督 |
| 是否支持零样本迁移 | ✅ 是 | ❌ 多数需 retrain 或 few-shot 支持 |
| 跨图泛化能力 | ✅ 强（通过原型空间对齐） | ⚠️ 弱（易过拟合特定图结构） |
| 推理效率 | ✅ 高（子线性扩展） | ⚠️ 低（如 CoLA 需大量随机游走） |

---

## 2. 核心实验方法和设置

### 使用了哪些数据集
共使用 **15 个真实世界图数据集**，涵盖多种领域与规模，分为训练集与测试集：

#### 📚 训练图（4个）
- `PubMed`, `Flickr`, `Questions`, `YelpChi`

#### 🔍 测试图（11个）
- **同域图**：`Cora`, `CiteSeer`, `ACM`, `BlogCatalog`, `Facebook`, `Weibo`, `Reddit`
- **跨域图**：`CoAuthor CS`, `Amazon Photo`, `Tolokers`, `T-Finance`

> 数据集类型包括：引用网络、社交网络、共购网、金融交易图等，覆盖注入异常与真实异常。

---

### 实验设置和评估指标

#### 评估协议：Zero-shot Generalist GAD
- 在训练图上训练一次 → 直接迁移到所有未见测试图；
- **不允许**在目标图上微调、适配或使用任何标注数据；
- 符合实际应用场景下的“冷启动”需求。

#### 评估指标
- **AUROC**（Area Under ROC Curve）
- **AUPRC**（Area Under Precision-Recall Curve）
- 报告五次独立运行的均值 ± 标准差（mean±std）

#### 实现细节
- 教师模型：采用 GCA（Graph Contrastive Augmentation）等主流 SSL 模型；
- 特征维度统一映射为 64；
- 所有超参数在训练集上确定后固定，不在测试集上调参。

---

### 基线方法对比

#### ✅ 监督类方法（Supervised）
- GCN, GAT（仅预训练）
- BGNN, BWGNN, GHRN（专用 GAD 模型）
- ARC, UNPrompt, AnomalyGFM（最新 generalist GAD 方法）

#### ✅ 无监督类方法（Unsupervised）
- DOMINANT（重构）
- CoLA（对比学习）
- HCM-A（跳数预测）
- TAM（亲和最大化）

> 注意：ARC 和 AnomalyGFM 虽然也是 generalist 方法，但它们依赖监督训练 + 推理时 few-shot 样本；而 ProMoS 完全无监督。

---

## 3. 主要实验结果和性能指标

### 关键性能数据（来自 Table 2 & 3）

#### 📊 AUROC 结果（平均提升 14.12%）
| 指标 | 最佳表现 | 第二名 | 平均排名 |
|------|--------|--------|----------|
| ProMoS | **9/11 数据集第一** | 1/11 第二 | **1.18** |
| DOMINANT（最强无监督基线） | — | — | 3.09 |
| TAM | — | — | 3.27 |

> 在 `Cora` 上达到 **84.56% AUROC**，远超第二名（TAM: 62.02%）

#### 📈 AUPRC 结果（更关注类别不平衡）
| 指标 | 表现 |
|------|------|
| ProMoS | **9/11 数据集第一**，其余两个第二 |
| 在 `Cora` 上 AUPRC 达 **46.48%**，比最佳基线（DOMINANT: 12.75%）高出 **33.73%**

---

### 与基线方法的对比结果

| 对比维度 | 发现 |
|--------|------|
| **vs. 监督方法** | 即使不使用任何标签，ProMoS 性能仍全面超越所有监督方法（包括 ARC 和 AnomalyGFM） |
| **vs. 无监督方法** | 显著优于 DOMINANT、CoLA、TAM 等经典无监督方法，尤其在跨域图上优势明显 |
| **vs. Few-shot 方法**（见 Table 9） | 在 10-shot 设置下，ARC 和 AnomalyGFM 仍落后于 ProMoS 的零样本性能（平均 AUROC 77.16% vs 75.03%） |

> **结论**：ProMoS 不仅性能更强，而且摆脱了对标签的依赖，更具实用价值。

---

### 消融实验结果（Ablation Study）

#### 🔍 移除关键组件的影响（Table 4）

| 变体 | 描述 | 平均 AUROC 下降 |
|------|------|----------------|
| `w/o PSD` | 移除原型引导蒸馏 | ↓19.14%（灾难性下降） |
| `w/o DCR` | 移除差异感知机制 | ↓5.26% |
| `w/o SSL` | 替换教师为随机初始化 GCN | ↓5.53%（OOM on T-Finance） |

> 表明：**原型蒸馏是核心驱动因素**，教师知识与 DCR 机制同样不可或缺。

#### 更多消融分析（Appendix E.3）
- `w/o PB`（移除个性化分支）→ 性能下降，说明局部模式建模重要；
- `w/o SB`（移除共享分支）→ 同样下降，说明全局建模不可替代；
- `w/o DIS`（移除质量加权）→ 性能下降，验证了可靠性权重的有效性；
- 联合移除（如 `w/o PB & DIS`）导致更大退化，表明各模块协同作用。

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **无监督也能实现强泛化的通用 GAD**  
   ProMoS 首次证明：无需任何标签，仅通过建模“正常性”即可实现卓越的跨图异常检测能力。

2. ✅ **原型空间是跨图迁移的关键桥梁**  
   将教师与学生对齐在共享原型空间，有效缓解了图间异质性（heterogeneity gap）带来的挑战。

3. ✅ **混合学生架构兼具表达力与效率**  
   MoS 架构通过稀疏激活，在保持高效的同时增强了模型容量，理论证明其误差不会高于任一单学生。

4. ✅ **零样本推理可行且高效**  
   ProMoS 推理时间随边数呈**亚线性增长**（$T \propto |E|^{0.3}$），适合大规模图应用。

5. ✅ **框架具有鲁棒性和可插拔性**  
   在不同教师骨干（GCA, GraphCL, BGRL, DGI, GraphMAE）下均表现稳定（Table 5），显示其对未来 SSL 模型的兼容潜力。

---

### 方法的局限性
1. **依赖高质量的预训练教师模型**  
   若教师未能充分捕捉正常性先验（如训练不足或领域偏移），性能会受限。

2. **原型初始化敏感性**  
   当前使用 k-means 初始化原型，可能受初始聚类质量影响。

3. **极端稀疏异常下的边界情况**  
   在异常比例极低（<1%）或结构极为隐蔽的情况下，检测难度仍大。

4. **无法解释具体异常原因**  
   与多数深度 GAD 方法一样，缺乏细粒度归因能力。

---

### 未来工作方向
1. **探索更强大的教师模型集成策略**  
   如结合多个 SSL 教师进行多视角蒸馏。

2. **引入因果或解耦表示以增强可解释性**  
   分离出导致异常的具体属性或子结构。

3. **扩展至动态图与时序异常检测**  
   将 ProMoS 框架推广到 streaming graph 场景。

4. **设计在线增量更新机制**  
   在不破坏零样本假设的前提下，允许轻量级适应新图统计特性。

5. **探索更高效的路由机制**  
   如基于图拓扑的结构化路由，而非纯特征驱动。

---

> 💡 **一句话总结**：  
> **ProMoS 开辟了一条全新的路径——利用无监督知识蒸馏 + 原型空间对齐 + 混合学生架构，实现了高性能、高效率、真正意义上的零样本通用图异常检测。**

</details>

---

### 12. [BrickAnything: Geometry-Conditioned Buildable Brick Generation with Structure-Aware Tokenization](https://arxiv.org/abs/2605.26182)

**Authors**: Zhengyang Ni, Feng Yan, Yu Guo, Fei Wang  
**Category**: cs.AI  
**Published**: 2026-05-27  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.26182v1  

#### Abstract
Generating physically buildable brick structures from 3D shapes requires more than geometric reconstruction: the output must also satisfy discrete part constraints and structural stability. Existing brick generation methods either rely on heuristic optimization, which can break down when the target ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：BrickAnything: Geometry-Conditioned Buildable Brick Generation with Structure-Aware Tokenization**

---

## **1. 论文的主要贡献和创新点**

### **解决的问题**
现有砖块结构生成方法存在两大局限：
- **基于启发式搜索的方法**（如 Legolization）虽然能保证物理可行性，但在目标几何形状无法在离散砖块空间中实现时会失败，且计算成本高、扩展性差。
- **生成式模型**（如 BrickGPT、LEGO-Maker）通常依赖文本或图像等高层输入，缺乏对显式 3D 几何约束的建模，难以精确重建复杂形状。

因此，如何设计一个既能利用显式 3D 几何信息、又能灵活适应多种输入形式，并生成**几何保真度高且物理可构建**的砖块结构的统一框架，是一个开放挑战。

### **提出的新方法与创新思路**
本文提出了 **BrickAnything** —— 一种基于几何条件的自回归砖块生成框架，其核心创新包括：

#### ✅ **1. 统一的几何接口：Point Cloud 作为中间表示**
- 使用 **point cloud** 作为模态无关（modality-agnostic）的中间表示，将多样化的 3D 输入（mesh、RGB-D、GS 等）统一映射为显式的空间几何信号。
- 利用预训练的 **Michelangelo encoder** 编码点云及其法向量，提供强几何引导。

#### ✅ **2. 结构感知的树状 tokenization（Structure-Aware Tree Tokenization）**
- 不同于传统按坐标排序的扁平序列（如 BrickGPT-style），该方法根据砖块间的**局部连接关系**组织 token 序列。
- 构建垂直附着图并进行 BFS 遍历，每个非根砖块以相对父砖块的 `(f, h, w, m)` 四元组编码，其中：
  - `f`：父砖上的连接位置
  - `h, w`：子砖尺寸
  - `m`：子砖侧锚点
- 引入 `EOP` 标记结束每个父节点的子组，形成树形结构化序列。

> 🌟 这种表示更贴近真实搭建过程，显式建模了砖块之间的装配依赖，提升了生成一致性，减少了无效中间状态。

#### ✅ **3. 可构建性感知的 DPO 后训练（Buildability-Aware DPO）**
- 设计了一个联合衡量**几何保真度**（IoU + Chamfer Distance）和**结构稳定性**（最小单砖稳定分）的奖励函数 $ R(B,P) = R_{\text{geo}} + R_{\text{stable}} \in [0,3] $。
- 基于此奖励构造 preference pairs，采用 **Direct Preference Optimization (DPO)** 对模型微调，使模型优化超越似然目标，直接提升 buildability。

#### ✅ **4. 轻量级父感知回滚策略（Parent-Aware Rollback）**
- 在推理阶段引入 **validity-constrained decoding** 和 **stability-guided rollback**：
  - 解码时逐 token 检查合法性（连接有效性、碰撞检测）
  - 若最终结构不稳定，则定位首个不稳定的砖块，回溯至其**父砖对应的 token 位置**，重新生成后续子结构。
- 利用树结构中的 parent-child 关系实现精准修正，避免全局重采样。

---

### **相比现有方法的优势**
| 方面 | BrickAnything | 现有方法 |
|------|---------------|----------|
| **几何控制能力** | 显式使用 point cloud 条件，重建精度高 | 多数依赖文本/图像，几何模糊 |
| **结构合理性** | 树状 tokenization 显式建模装配依赖 | 扁平序列易产生非法连接 |
| **物理可构建性** | DPO + 回滚机制联合保障稳定性 | 或无建模，或依赖复杂搜索 |
| **推理效率** | 平均回滚次数显著降低（<0.5次 vs >6次） | 搜索类方法耗时长，生成类需频繁重试 |

---

## **2. 核心实验方法和设置**

### **数据集**
- **训练数据**：从 ShapeNet、Objaverse、Objaverse-XL 中精选约 230K 高质量 mesh。
- 使用 **Legolization [25]** 将其转换为砖块结构，得到约 168K 稳定的 mesh-brick 对。
- **验证集**：随机选取 4K 样本。
- **测试集** 分为两类：
  - **Stable subset (500)**：Legolization 成功转换的样本 → 衡量上限性能
  - **Challenging subset (500)**：Legolization 失败的样本 → 测试鲁棒性和泛化能力

### **实验设置**
- **模型架构**：基于 OPT-350M transformer 解码器
- **训练流程**：
  1. **Pre-training**：标准 next-token 预测目标
  2. **Post-training**：使用 buildability-aware reward 构造 preference pairs，执行 DPO 微调
- **推理策略**：
  - Validity-constrained decoding（拒绝非法 token）
  - Stability-guided rollback（最多允许若干次回滚）

### **评估指标**
| 指标 | 描述 |
|------|------|
| **Chamfer Distance (CD)** ↓ | 表面点云距离，越小越好 |
| **Voxel IoU** ↑ | 体素重叠率，越高越好 |
| **%Valid** ↑ | 输出满足砖型、边界、无碰撞的比例 |
| **%Stable** ↑ | 物理上稳定的比例（每砖稳定分 > 0） |
| **Rollback ↓** | 平均回滚次数，反映纠错开销 |

### **基线方法对比**
1. **Legolization [25]**：启发式搜索方法，代表传统优化路线
2. **BrickGPT-style tokenization**：相同模型架构 + 坐标排序扁平序列，用于隔离 tokenization 影响

---

## **3. 主要实验结果和性能指标**

### **定量结果（Table 1）**

#### **(a) Challenging Subset 结果**
| Method | CD↓ | IoU↑ | Rollback↓ | %Stable↑ | %Valid↑ |
|--------|-----|------|-----------|----------|---------|
| Legolization | – | – | – | 0.0% | 100% |
| BrickGPT-style (w/o DPO) | 0.1307 | 0.544 | 6.991 | 74.0% | 100% |
| BrickGPT-style | 0.1309 | 0.553 | 6.750 | 76.0% | 100% |
| **Ours (Full)** | **0.1299** | **0.586** | **0.422** | **83.4%** | **100%** |

> 🔍 在 Legolization 完全失效的情况下，BrickAnything 仍能达到 **83.4% 稳定率**，且平均仅需 **0.422 次回滚**，远优于基线的 ~6.8 次。

#### **(b) Stable Subset 结果**
| Method | CD↓ | IoU↑ | Rollback↓ | %Stable↑ | %Valid↑ |
|--------|-----|------|-----------|----------|---------|
| Legolization | 0.1120 | 1.000 | – | 100% | 100% |
| BrickGPT-style | 0.1292 | 0.742 | 3.620 | 100% | 100% |
| **Ours (Full)** | **0.1283** | **0.788** | **0.184** | **100%** | **100%** |

> 💡 尽管 Legolization 在自身成功案例上有最佳 IoU，但 BrickAnything 在学习方法中表现最优，**IoU 提升 46 个百分点（0.742→0.788）**，**回滚减少 95%（3.62→0.184）**。

---

### **消融实验结果（Ablation Study）**

| 变体 | Challenging-IoU | Challenging-%Stable | Rollback |
|------|------------------|----------------------|----------|
| w/o Validity/Rollback/DPO | 0.602 | 60.6% | – |
| w/o Rollback/DPO | 0.597 | 72.0% | – |
| w/o DPO | 0.573 | 82.4% | 0.444 |
| **Full Model** | **0.586** | **83.4%** | **0.422** |

#### **关键发现：**
- **Validity-constrained decoding** 是确保 `%Valid=100%` 的关键；
- **Rollback** 显著提升 `%Stable`，说明局部合法 ≠ 全局稳定；
- **DPO** 改善生成分布本身，不仅提高 IoU，还**减少回滚需求**，体现“学得更好，修得更少”；
- **Tree tokenization** 是性能跃迁的基础，相比坐标排序显著提升稳定性与效率。

---

## **4. 关键结论和发现**

### **主要结论**
1. ✅ **结构感知的树状 tokenization 显著优于传统坐标排序**：
   - 更符合物理搭建逻辑
   - 显式建模 parent-child 依赖
   - 降低无效生成与回滚频率

2. ✅ **几何条件化生成是实现高保真重建的关键**：
   - 使用 point cloud 作为统一接口，支持多模态输入
   - 显式几何监督显著提升形状对齐能力

3. ✅ **DPO + 回滚构成高效的 buildability 优化闭环**：
   - DPO 让模型“学会”什么是好结构
   - 回滚机制提供容错能力
   - 二者结合大幅减少推理修正开销

4. ✅ **BrickAnything 在 challenging 场景下表现出色**：
   - 即使 heuristic 方法完全失败，仍能生成稳定结构
   - 展现出更强的鲁棒性与泛化能力

---

### **局限性**
- **受限的工作空间**：当前限定在 20×20×20 voxel grid，限制了分辨率和复杂度。
- **有限的砖块类型**：仅使用 8 种标准矩形砖，难以表达曲面、细长部件。
- **依赖合成数据**：训练数据由 Legolization 自动生成，缺乏人类设计的真实构造先验。
- **手工设计奖励函数**：buildability-aware reward 为人工定义，可能未覆盖所有实际建造考量。

---

### **未来工作方向**
1. **扩展到更大空间与更多砖型**：支持更大尺寸、斜角砖、柔性连接等。
2. **引入真实人类设计数据集**：提升构造多样性与创造性。
3. **学习动态 reward model**：通过真实组装反馈或用户偏好进一步优化 buildability。
4. **端到端支持 image/text-to-brick**：结合更强的 3D 生成模型（如 Hunyuan3D）作为前端。
5. **探索非自回归生成范式**：提升长序列生成效率。

---

> 📌 **一句话总结**：  
> **BrickAnything 通过 structure-aware tree tokenization + geometry-conditioned generation + DPO + rollback 的协同设计，在保持物理可构建性的前提下，实现了更高保真度、更低纠错成本的砖块结构生成，尤其在传统方法失败的复杂场景中展现出显著优势。**

</details>

---

### 13. [The MiniMax-M2 Series: Mini Activations Unleashing Max Real-World Intelligence](https://arxiv.org/abs/2605.26494)

**Authors**: MiniMax,  :, Aili Chen, Aonian Li, Baichuan Zhou, Bangwei Gong, Binyang Jiang, Boji Dan, Changqing Yu, Chao Wang, Cheng Ma, Cheng Zhong, Cheng Zhu, Chengjun Xiao, Chengyi Yang, Chengyu Du, Chenyang Zhang, Chi Zhang, Chuangyi Huang, Chunhao Zhang, Chunhui Du, Chunyu Zhao, Congchao Guo, Da Chen, Deming Ding, Dianjun Sun, Dongyu Zhang, Enhui Yang, Fei Yu, Guang Zheng, Guodong Zheng, Guohong Li, Haichao Zhu, Haigang Zhou, Haimo Zhang, Han Ding, Hao Zhang, Haohai Sun, Haolin Lyu, Haonan Lu, Haoyu Wang, Huajie Shi, Huiyang Li, Jiacheng Chen, Jian Zhang, Jiaqi Zhuang, Jiaren Cai, Jiaxin Pan, Jiayao Li, Jiayuan Song, Jichuan Zhang, Jie Wang, Jihao Gu, Jin Zhu, Jingwei Dong, Jingyang Li, Jingyu Zhang, Jingze Zhuang, Jinhao Tian, Jinli Liu, Jinyi Hu, Jun Tao, Jun Zhang, Junbin Ruan, Junhao Xu, Junjie Yan, Junteng Liu, Junxian He, Kang Xu, Ke Ji, Ke Yang, Kecheng Xiao, Keyu Duan, Keyu Li, Le Han, Letian Ruan, Li Yuan, Lianfei Yu, Liheng Feng, Lijie Mo, Lin Li, Lingye Bao, Lingyu Yang, Lingyuan Zhou,  Loki, Lu Chen, Lunbin Ceng, Ming Li, Ming Zhong, Mingliang Tao, Mingyuan Chi, Mujie Lin, Nan Hu, Ningxin Chen, Peiyin Zhu, Peng Gao, Pengcheng Gao, Pengfei Li, Penglin Li, Pengyu Zhao, Qibin Ren, Qidi Xu, Qihan Ren, Qile Li, Qin Wang, Quanliang Chen, Qunhong Ceng, Rong Tian, Rui Dong, Ruitao Leng, Ruize Zhang, Shanqi Liu, Shaoyu Chen, Sheng Jia, Shun Yao, Shuoran Zhao, Shuqi Yu, Sichen Li, Sicheng Pan, Songquan Zhu, Tengfei Li, Tian Xie, Tiancheng Qin, Tianrun Liang, Wei Liu, Weiqi Xu, Weitao Li, Weixiang Chen, Weiyu Cheng, Weiyu Zhang, Wenhu Chen, Wenqian Zhao, Xiancai Chen, Xiangjun Song, Xiangyuan Wang, Xiao Luo, Xiao Su, Xiaobo Li, Xiaodong Han, Xiaojie Wu, Xihao Song, Xingyi Han, Xinyu Guan, Xuan Lu, Xun Zou, Xunhao Lai, Xutong Li, Yan Gong, Yang Wang, Yang Xu, Yangsen Wang, Ye Tang, Yicheng Chen, Yinran Qiu, Yiqi Shi, Yiting Guo, Yiwen Huang, Yixuan Wang, Yongyi Hu, Yu Gao, Yu Zhang, Yuanxiang Ying, Yuanzhen Zhang, Yubo Wang, Yuchen Song, Yufeng Yang, Yuhang Meng, Yuhang Miao, Yuhao Li, Yujie Liu, Yulin Hu, Yunan Huang, Yunji Li, Yunyi Huang, Yusen Zhang, Yusu Hong, Yutao Xie, Yutong Zhang, Yuwen Liao, Yuxuan Shi, Yuze Wenren, Zebin Li, Zehan Li, Zejian Luo, Zeyu Jin, Zeyuan Sun, Zhanpeng Zhou, Zhaochen Su, Zhendong Li, Zhengmao Zhu, Zhengyuan Peng, Zhenhua Fan, Zhi Zhang, Zhichao Xu, Zhiheng Lv, Zhikang Xu, Zhitao He, Zhiwei He, Zhongyuan Li, Zibo Gao, Zijia Wu, Zijian Song, Zijian Zhou, Zijun Sun, Zishan Huang, Ziying Chen, Ziyue Ge  
**Category**: cs.AI  
**Published**: 2026-05-27  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.26494v1  

#### Abstract
We introduce the MiniMax-M2 series, a family of Mixture-of-Experts language models built around the principle that mini activations can unleash maximum real-world intelligence. The flagship M2 contains 229.9B total parameters with only 9.8B activated per token. Designed end-to-end for agentic deploy...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：The MiniMax-M2 Series: Mini Activations Unleashing Max Real-World Intelligence

---

## 1. 论文的主要贡献和创新点

### 解决的问题
当前大语言模型（LLMs）正从短对话向**长周期、多步骤的 agentic workflows**（如软件开发、网页操作、工具调用等）迁移。这一转变带来了两大挑战：
- **效率瓶颈**：agentic 任务通常需要超长上下文（up to 192K tokens），导致训练和推理成本极高。
- **复杂性要求**：真实场景中的任务（如生产级代码工程、办公自动化）具有高难度和高风险，对模型的推理、执行和纠错能力提出更高要求。

### 提出的新方法与核心思想
MiniMax-M2 系列基于一个核心设计原则：**mini activations can unleash maximum real-world intelligence**——即通过极低的激活参数量实现前沿级别的智能表现。

#### 主要创新点包括：

| 创新模块 | 核心技术 |
|--------|--------|
| **Agent-Driven Data Pipelines** | 构建了面向 agentic coding 和 cowork 的大规模、可验证轨迹数据集，每个任务都绑定可执行环境（executable workspace）和 artifact-aligned reward（如测试通过率、UI 渲染质量）。 |
| **Forge：Agent-Native RL 系统** | 专为 agentic 强化学习设计的系统，支持 white-box 和 black-box agents，具备 windowed-FIFO 调度、prefix-tree merging、推理优化等机制，显著提升训练稳定性和吞吐量。 |
| **Self-Evolution 自我演化能力（M2.7）** | M2.7 可以自主诊断失败的训练运行、修改自身 agent scaffold，并在 ML 工程任务上进行多轮自我改进，初步实现了闭环迭代开发。 |

### 相比现有方法的优势
- **高效性**：仅激活 ~9.8B 参数，远低于多数闭源前沿模型（如 GPT-5.4、Claude Opus 4.6），却能达到相近甚至超越的性能。
- **真实性**：所有训练数据均来自真实或高度仿真的工作流，强调**可执行性**与**可验证性**，避免幻觉。
- **通用性**：支持任意 agent 架构（white-box/black-box），无需修改训练框架即可接入新 agent。
- **可持续进化**：首次展示 LLM 在真实基础设施中实现“自我调试”和“自我升级”的能力，降低人类干预成本。

---

## 2. 核心实验方法和设置

### 使用的数据集
论文构建了多个领域专用的高质量数据集，涵盖以下五大类任务：

| 类别 | 数据集/任务 |
|------|-----------|
| **Agentic Coding** | SWE-bench Pro, SWE-bench Multilingual, Multi-SWE-bench, Terminal-Bench 2.0, MLE-Bench Lite, NL2Repo |
| **Application Development** | VIBE-Pro, HyperTask |
| **Agentic Cowork** | BrowseComp, Wide Search, RISE, GDPval-AA, Toolathlon, MM Claw, MEWC v2, Finance Modeling Pro |
| **Reasoning & Knowledge** | AIME 2026, GPQA-Diamond, SciCode, IFBench, AA-LCR, HLE, MMLU-Pro |
| **General Purpose** | 包括 long CoT 写作、角色扮演、多轮对话等 |

> 所有数据均经过严格清洗、增强与验证，确保 reward 信号可信且与最终输出 artifact 对齐。

### 实验设置和评估指标
- **模型配置**：
  - M2: 229.9B 总参数，9.8B 激活参数，62 层 MoE Transformer，256 个专家，每 token 激活 8 个。
  - 上下文长度：192K tokens。
  - MTP（Multi-Token Prediction）模块用于 speculative decoding 加速推理。
- **训练流程**：
  - 预训练：29.2T tokens。
  - SFT：引入 interleaved thinking（交错思考）模式。
  - RL：使用 CISPO 算法，在 Forge 系统中进行混合域强化学习（mixed-domain RL）。
- **评估协议**：
  - 所有模型在相同 scaffold 和 tool environment 下测试。
  - 多数任务运行 3–4 次取平均。
  - 使用 **pass@1** 或 **medal rate**（金/银/铜牌比例）作为主要指标。

### 基线方法对比
对比对象均为当前最强的闭源模型：
- **Claude Opus 4.6**
- **Claude Sonnet 4.6**
- **GPT-5.4**
- **Gemini 3.1 Pro**

此外还包括前代版本 **MiniMax-M2.5** 用于内部演进分析。

---

## 3. 主要实验结果和性能指标

### 关键性能数据（MiniMax-M2.7）

| 任务类别 | 基准 | M2.7 成绩 | 最佳基线成绩 |
|--------|-------|------------|--------------|
| **Agentic Coding** | SWE-bench Pro | **56.2** | 57.7 (GPT-5.4) |
| | SWE-bench Multilingual | **76.5** | 77.8 (Opus) |
| | Multi-SWE-bench | **52.7** | 51.0 (Sonnet) ✅ |
| | Terminal-Bench 2.0 | 57.0 | 75.1 (GPT-5.4) ❌ |
| | MLE-Bench Lite | **66.6%** medal rate | 66.6% (Gemini 3.1 Pro) ✅ |
| **AppDev** | VIBE-Pro | 55.6 | 56.1 (Sonnet) |
| | HyperTask | **67.6** | 75.7 (Opus) ❌ |
| **Cowork - Search** | BrowseComp | **77.8** | 84.0 (Opus) ❌ |
| | RISE | **64.3** | 68.5 (Opus) ❌ |
| **Cowork - Office** | GDPval-AA | **50.0** | 58.0 (GPT-5.4) ❌ |
| | MM Claw | **62.7** | 75.4 (Opus) ❌ |
| **Reasoning & Knowledge** | AIME 2026 | **94.2** | 97.0 (GPT-5.4) ❌ |
| | GPQA-Diamond | **89.8** | 94.1 (Gemini) ❌ |
| | MMLU-Pro | 81.8 | 91.2 (Gemini) ❌ |

> ✅ 表示优于所有基线；❌ 表示落后于最佳基线但仍具竞争力。

### 与基线方法的对比结果
- M2.7 在 **Multi-SWE-bench** 上取得 SOTA，表明其跨仓库修复能力强。
- 在 **MLE-Bench Lite** 中与 Gemini 3.1 Pro 并列第一，证明其具备自主 ML 工程能力。
- 尽管在部分任务（如 Terminal-Bench、AIME）上略逊于 GPT-5.4 或 Gemini，但考虑到其仅激活 ~10B 参数，性价比极高。
- 在 **within-series progression** 中，M2 → M2.5 → M2.7 全面提升，尤其在 deep search 和 office automation 上增益显著（+15~30 pts）。

### 消融实验结果
#### （1）MoE 设计消融（Table 1）
| 配置 | MATH | MMLU | HumanEval |
|------|------|------|----------|
| 基线（32 experts） | 19.6 | 39.8 | 29.7 |
| + MTP | 21.3 | 39.7 | 30.1 |
| + Fine-Grained Experts (128 exp.) | **24.1** | **40.2** | **32.5** |

👉 结论：细粒度专家 + MTP 显著提升推理与编码能力。

#### （2）Attention 架构比较（Tables 2 & 3）
- Full attention 在长上下文任务（>32K）上明显优于 Hybrid SWA。
- SWA 在短任务上有轻微优势，但在 retrieval、multi-hop reasoning 上全面落后。
- 支持 M2 采用全注意力的设计选择。

#### （3）Interleaved Thinking 消融
- 移除 reasoning state persistence 导致 deep search 和 SWE 任务性能大幅下降。
- 说明保留完整推理历史对长期规划至关重要。

---

## 4. 关键结论和发现

### 主要发现
1. **Mini Activations ≠ Low Intelligence**  
   通过高质量数据、精准 reward 设计和高效的 RL 系统，即使只激活 ~10B 参数也能达到与更大模型相当的 agentic 能力。

2. **Executable Workspace + Artifact-Aligned Reward 是关键**  
   所有训练任务都必须能被执行并验证，reward 必须与最终产出物（如代码、网页、Excel 表格）直接挂钩，才能有效驱动真实世界能力。

3. **Interleaved Thinking 提升样本效率与鲁棒性**  
   允许模型在每一步中持续积累和更新 reasoning state，形成 Plan-Act-Reflect 循环，显著优于 front-loaded 或 stateless 推理。

4. **Self-Evolution 初步可行**  
   M2.7 能够自动诊断训练异常、修改 scaffold 并完成多轮迭代优化，在 MLE-Bench Lite 上实现持续 medal rate 提升，标志着迈向“自我改进 AI 系统”的第一步。

5. **Mixed-Domain RL 防止 Catastrophic Forgetting**  
   同时训练 reasoning、coding、cowork、general 四类任务，避免单一领域过拟合，保持模型通用性。

### 方法的局限性
- **部分任务仍落后于最大模型**：如 Terminal-Bench、AIME、HLE 等，显示在极端复杂任务上仍有差距。
- **依赖高质量仿真环境构建**：如 Docker 环境生成、Playwright 浏览器交互等，构建成本较高。
- **Self-Evolution 尚处早期阶段**：目前仅限于特定 ML 工程任务，尚未扩展到全栈模型训练。

### 未来工作方向
- 继续扩展 **self-evolution** 能力，覆盖更多类型的 scaffold 修改与训练策略调整。
- 推进 sub-quadratic attention 技术，应对未来更长上下文需求。
- 进一步提升 **security-aware agent** 能力，发展 CVE-Factory 等自主漏洞分析系统。
- 探索 **multi-agent collaboration** 在复杂任务中的应用。
- 持续扩大 **reasoning diversity** 与 **solution path scaling**，提升泛化能力。

---

> **总结一句话**：  
> MiniMax-M2 系列证明了“小激活、大智能”的可行性——通过 agent-native 数据、RL 系统与初步 self-evolution 机制，以极低计算开销实现了接近甚至超越最大模型的真实世界任务表现，为下一代 agentic AI 提供了一条高效、可持续的发展路径。

</details>

---

### 14. [Helicase: Uncertainty-Guided Supply Chain Knowledge Graph Construction with Autonomous Multi-Agent LLMs](https://arxiv.org/abs/2605.26835)

**Authors**: Yunbo Long, Haolang Zhao, Ge Zheng, Alexandra Brintrup  
**Category**: cs.AI  
**Published**: 2026-05-27  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.26835v1  

#### Abstract
LLM-based multi-agent systems have been widely adopted for knowledge retrieval and report generation, synthesizing known information through web search and textual reasoning. However, many critical information tasks in supply chains are not simple one-shot queries: they are structural inference prob...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Helicase: Uncertainty-Guided Supply Chain Knowledge Graph Construction with Autonomous Multi-Agent LLMs*

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
现代供应链研究面临四大挑战：
- **缺乏自主搜索能力**：现有系统依赖预处理数据或固定流程，无法动态响应复杂、模糊的查询。
- **无量化不确定性**：主流多智能体系统（如ChatGPT、Gemini）生成的答案缺乏可信度评估，易产生幻觉（hallucination），难以支持高风险决策。
- **不可解释性与不可审计性**：推理过程为“黑箱”，无法追溯证据链和逻辑路径。
- **缺乏结构性知识构建能力**：仅能进行文本合成，无法构建用于分析的知识图谱（Knowledge Graph, KG）。

这些问题导致在面对**多跳（multi-hop）、低可见性（low-visibility）** 的供应链问题时（例如：“哪些特斯拉组件使用来自澳大利亚矿山的锂？”），传统方法完全失效。

---

### 🚀 提出的新方法：Helicase
作者提出 **Helicase** —— 一个基于 **Autonomous Multi-Agent LLMs** 的不确定性引导型供应链知识图谱构建系统。其核心创新如下：

#### （1）**三层次不确定性量化框架（Three-Layer Uncertainty Quantification）**
- **Action Layer**：衡量每个智能体执行动作的可靠性（如并行搜索结果的一致性）。
- **Trajectory Layer**：检测迭代过程中是否存在重复探索，避免冗余。
- **Memory Layer**：整合所有事实的不确定性，形成全局置信度 $U_{\text{memory}}$，指导后续行动。

该框架使系统不仅能输出答案，还能提供**可校准的置信度估计（calibrated confidence）**，实现“知道自己知道多少”。

#### （2）**闭环螺旋式知识图谱构建机制（Helical Process）**
- 通过 Planner Agent 将高层查询分解为可执行计划。
- 多个专用 Agent 并行协作：
  - **Web Search Agent**：从异构源（HTML、PDF、CSV、社交媒体）提取证据。
  - **Reasoning Agent**：跨源推理，识别需更新的结构。
  - **Coding Agent**：将推理结果转化为确定性的 JSON 变更操作，写入 KG。
- 系统以“执行 → 更新图谱 → 评估不确定性 → 规划下一步”循环推进，直至收敛。

#### （3）**动态自适应执行策略**
- 根据目标概念的不确定性动态调整并行搜索数量（$n \in [1,10]$）。
- 基于不确定性梯度优先探索高不确定区域，提升效率。

---

### 🔍 相比现有方法的优势
| 维度 | 现有方法（如 ReAct、ToT） | Helicase |
|------|--------------------------|--------|
| 是否支持结构化输出 | ❌ 文本摘要 | ✅ 结构化 KG |
| 是否具备不确定性感知 | ❌ 无 | ✅ 三层量化框架 |
| 是否支持多模态输入 | ⚠️ 有限 | ✅ 支持 PDF、CSV、JS 渲染页面等 |
| 是否自主规划 | ❌ 固定流程 | ✅ 动态生成调查路径 |
| 是否可审计 | ❌ 黑箱 | ✅ 图谱+溯源+置信度 |

> Helicase 是首个实现 **端到端自动化、不确定性感知、结构化知识发现** 的 agentic LLM 系统。

---

## 2. 核心实验方法和设置

### 📚 数据集：SCQA（Supply Chain Query Assessment）
- **首次公开发布的供应链深度研究基准**，包含 **80 个真实世界查询**，按两个维度划分四象限（每象限 20 条）：
  - **推理复杂度**：单跳 vs 多跳
  - **信息可见性**：高可见 vs 低可见

| 象限 | 类型 | 示例 |
|------|------|------|
| Q1 | 单跳 + 高可见 | “潘婷洗发水是否含月桂醇硫酸钠？” |
| Q2 | 多跳 + 高可见 | “强生哪些婴儿产品在美国制造且含芦荟？” |
| Q3 | 单跳 + 低可见 | “麦当劳美国薯条的主要土豆供应商是谁？” |
| Q4 | 多跳 + 低可见 | “宝洁哪些护发产品共用泛醇和生物素原料？其共享供应商是谁？” |

> 所有答案均经人工标注+领域专家审核，附带证据来源。

---

### 🧪 实验设置

#### 模型配置（见 Table 1）
| Agent Role | Model |
|-----------|-------|
| Planner / Web Search / Reasoning | Qwen3-Next-80B-A3B-Thinking |
| Coding | Qwen3-Next-80B-A3B-Instruct |
| Consensus Scorer | 同上（用于计算 U_action） |

> 使用 SiliconFlow 提供服务，统一访问 Serper API 和 Jina Reader 工具。

#### 对比基线
| 类别 | 方法 |
|------|------|
| **前沿 LLMs（零样本）** | Claude Opus 4.6, Qwen3-235B, DeepSeek-V3.2, GLM-5 |
| **Agentic 框架** | ReAct (Qwen3-235B), Tree-of-Thoughts (ToT, Qwen3-235B) |

> 所有系统在相同条件下运行（工具、速率限制、无预加载源）。

---

### 📊 评估指标（分象限设计）

| 象限 | 主要指标 | 说明 |
|------|--------|------|
| Q1 | **Answer Accuracy (Acc.)** | 语义等价匹配（LLM Judge 判断） |
| Q2 | **Set F1 (Precision, Recall, F1)** | 多项列表任务的集合相似度 |
| Q3 | **Accuracy + Source Discovery Rate (SDR)** | 不仅答对，还需引用可靠来源 |
| Q4 | **Graph F1 (G-F1) + Uncertainty Calibration Error (UCE)** | 图级实体/关系匹配 + 置信度校准误差 |

其中：
- $ \text{G-F1} = 0.6 \times \text{E-F1} + 0.4 \times \text{R-F1} $
- $ \text{UCE} = \left| \frac{1}{|F|}\sum (c_f - a_f) \right| $，越低越好（理想值为0）

> 使用 **ChatGPT 5.5** 作为 LLM Judge 进行语义判断，并手动抽样验证一致性（>90%）。

---

## 3. 主要实验结果和性能指标

### 📈 性能汇总（Table 2）

| System | Q1 Acc. | Q2 F1 | Q3 Acc. | Q3 SDR | Q4 G-F1 | Q4 UCE |
|--------|---------|--------|---------|--------|---------|--------|
| **Claude Opus 4.6** | 0.80 | 0.55 | 0.55 | 0.00 | 0.63 | – |
| **ReAct** | 0.60 | 0.39 | 0.45 | 0.45 | 0.32 | – |
| **ToT** | 0.55 | 0.30 | 0.35 | 0.35 | 0.39 | – |
| **Helicase (Ours)** | **0.95** | **0.85** | **1.00** | **0.65** | **0.85** | **0.25** |

> ✅ Helicase 在所有象限全面领先，尤其在最难的 **Q4（多跳+低可见）** 上表现碾压式优势（0.85 vs 最佳基线 0.63）。

---

### 🔍 消融实验（Ablation Study on Q4 Queries）

| Variant | G-F1 | UCE |
|--------|------|-----|
| **Full Helicase** | **0.85** | **0.25** |
| w/o UQ (uniform planning) | 0.73 | – |
| w/o multiplicative accumulation (min-based) | 0.65 | 0.41 |
| w/o dynamic parallel search (n=1) | 0.68 | 0.34 |
| w/o MAS (single-agent loop) | 0.45 | – |

> 关键发现：
- **不确定性引导规划（UQ）** 是性能最大驱动力（↓0.12 G-F1）。
- **乘法式证据积累** 显著改善置信度校准（UCE 从 0.25↑至 0.41）。
- **多智能体专业化（MAS）** 是根本性优势，单一Agent无法复现效果。

> 表明 Helicase 的价值不在于“后处理提取KG”，而在于**整个闭环中各模块的协同作用**。

---

### 💰 计算成本（Table 4）
| System | Cost ($/query) |
|--------|----------------|
| Claude Opus 4.6 | 0.45 |
| ReAct | 0.15 |
| ToT | 0.20 |
| **Helicase** | **0.20–0.45** |

> 成本随查询复杂度自适应变化，虽略高于部分基线，但产出为**结构化、可审计、带置信度的知识图谱**，性价比极高。

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **现有 LLM 和 agentic 框架无法胜任结构性供应链推理**：
   - 前沿模型（如 Claude Opus）在 Q4 上仅得 0.63 G-F1，远低于人类水平。
   - ReAct/ToT 缺乏图结构建模能力，无法完成多跳推理。

2. **Helicase 实现了真正的“主动发现”而非“被动检索”**：
   - 能自动构建跨层级供应链图谱（如从矿场 → 精炼厂 → 电池厂 → 特斯拉产品）。
   - 支持跨行业依赖分析（如某原料同时用于化妆品与药品）。

3. **不确定性是可信决策的关键**：
   - Helicase 是唯一能输出 **calibrated uncertainty** 的系统（UCE=0.25）。
   - 管理者可根据置信度决定是否需要人工介入验证。

4. **多智能体架构 + 不确定性反馈环 = 可扩展的 agentic SCM 系统**：
   - 系统能根据问题难度自适应分配资源，无需人为设定迭代次数。
   - 适用于采购、可持续性、风险管理等多个场景。

---

### ⚠️ 局限性
1. **仅限公开可查信息**：无法获取真正私有的合同、商业秘密或非公开协议。
2. **依赖 LLM 共识机制**：若多个网页传播同一错误信息，系统可能误判为“真实”。
3. **易受对抗攻击**：SEO 操控、虚假内容投放可能导致知识图谱中毒。
4. **未涵盖时间维度**：当前不支持追踪供应商关系随时间演变。
5. **未集成企业内部数据**：仅基于公网信息，无法打通 ERP、SRM 等系统。

---

### 🔮 未来工作方向
1. **下游网络分析**：在生成的 KG 上进行 ripple-effect 分析、中断传播模拟。
2. **人机协同验证**：将高不确定性事实（U > T_high）自动路由给人类专家审查。
3. **跨组织协调**：不同企业的 discovery agent 协同绘制完整供应链地图。
4. **时序发现（Temporal Discovery）**：跟踪配方、所有权、合作关系的时间演化。
5. **融合企业数据源**：连接 ERP、PLM、MES 等系统，突破公网边界。
6. **增强抗攻击能力**：引入 provenance-aware 验证机制，识别信息源依赖关系。

---

## 总结

> **Helicase 标志着供应链智能从“被动报告”向“主动发现”的范式转变**。

它不仅是技术上的突破——实现了 **autonomous、structural、uncertainty-aware** 的知识发现；更是方法论上的革新——提出了 **agentic SCM** 的可行架构。结合新发布的 **SCQA benchmark**，本研究为未来供应链 AI 研究提供了标准化测试平台和明确发展方向。

> 🔗 开源地址：[https://github.com/Yunbo-max/Helicase](https://github.com/Yunbo-max/Helicase)  
> 📦 数据集将随论文发表公开发布。

</details>

---

### 15. [LELA: An End-to-end LLM-based Entity Linking Framework with Zero-shot Domain Adaptation](https://arxiv.org/abs/2605.26956)

**Authors**: Samy Haffoudhi (IP Paris, LTCI, DIG), Nikola Dobri\v{c}i\'c (IP Paris), Fabian Suchanek (IP Paris, LTCI), Nils Holzenberger  
**Category**: cs.AI  
**Published**: 2026-05-27  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.26956v1  

#### Abstract
Entity linking is a key component of many downstream NLP systems, yet existing approaches are often tied to the specific target knowledge bases and domains, limiting their real world application. In this paper, we extend LELA, a modular and domain-agnostic LLM-based entity disambiguation method, int...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：LELA: An End-to-end LLM-based Entity Linking Framework with Zero-shot Domain Adaptation

## 1. 论文的主要贡献和创新点

### 解决的问题
现有的 **Entity Linking (EL)** 方法通常依赖于特定的知识库（KB）和领域训练数据，难以适应真实世界中广泛存在的**专有或领域特定知识库**（如法律、生物医学或企业内部KB）。此外，大多数系统仅关注 **Entity Disambiguation (ED)**，而假设实体提及（mention）已预先标注，忽略了实际应用中必须进行的 **Named Entity Recognition (NER)** 步骤。

### 提出的新方法与思路
本文将先前提出的 **LELA** 系统从一个仅支持零样本实体消歧（zero-shot ED）的方法，扩展为一个**端到端的、模块化的、基于 LLM 的实体链接框架**，完整覆盖：
- **Zero-shot NER**：无需训练即可识别文本中的实体提及
- **Candidate Generation & Reranking**
- **LLM-based Disambiguation**

该框架以 spaCy 架构为基础，设计为高度可插拔的 pipeline，允许用户自由组合不同组件（如 NER 模型、检索器、重排序模型、LLM 推理后端等），实现真正的“即插即用”。

### 相比现有方法的优势
- ✅ **真正零样本（True zero-shot）**：无需任何训练数据或 fine-tuning，适用于任意领域和自定义 KB。
- ✅ **端到端流程**：集成 NER 和 ED，输入原始文本即可输出链接结果。
- ✅ **高度模块化与可扩展性**：支持多种 NER 工具（GLiNER、spaCy、regex）、候选生成方式（BM25、dense retrieval、fuzzy matching）、LLM 后端（vLLM、Transformers、OpenAI API、llama.cpp）。
- ✅ **灵活接口**：提供 Python API、CLI 和 Web 应用三种使用方式，便于研究与部署。
- ✅ **支持自定义 KB**：用户可以轻松上传自己的 JSONL 格式知识库进行测试。

---

## 2. 核心实验方法和设置

### 使用的数据集
- **Elgold** [Islamaj et al., 2021]：跨七个领域的 Wikipedia 实体链接基准，涵盖新闻、招聘、电影、汽车、电商、科学论文摘要、历史文献。
- **MHERCL** [Graciotti et al., 2025]：聚焦 Wikidata 中的长尾实体（long-tail entities），特别针对音乐文化遗产领域，更具挑战性。

### 实验设置
- **LELA 配置**：
  - **NER**: NuNER_Zero-span（zero-shot NER model）
  - **Candidate Generator**: Qwen3-Embedding-4B（dense retrieval via FAISS）
  - **Reranker**: Qwen3-Reranker-4B，top-k=10
  - **Disambiguator**: Qwen3-30B-A3B（via vLLM），采样 3 次进行 self-consistency 投票
  - **KB 输入格式**：JSONL，每条包含 id、label、description

- **评估指标**
  - 在 **Elgold** 上使用 **InKB EL F1**（只评估存在于 KB 中的 mention）
  - 在 **MHERCL** 上使用标准 **EL F1**
  - 使用 **ELEVANT** [Bast et al., 2022] 进行细粒度评估分析

### 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| **BLINK + NER** | Zero-shot ED | 经典的基于 dense retrieval 的 zero-shot 方法 |
| **ReFinED** | End-to-end | 当前最先进的 end-to-end EL 方法之一（ACL 2022） |
| **Relik** | End-to-end | 高效且准确的学术级 EL 系统（ACL 2024） |
| **GLiNKER** | Modular | 基于 GLiNER 的生产导向框架 |

---

## 3. 主要实验结果和性能指标

### 关键性能数据（来自 Tables 1 & 2）

#### 在 Elgold 数据集上的 F1 表现（InKB, %）

| Domain | BLINK+NER | Relik | ReFinED | **LELA (Ours)** |
|--------|-----------|-------|---------|-----------------|
| News | 68.2 | 76.5 | 78.4 | **74.7** |
| Jobs | 43.3 | 67.0 | 72.0 | **60.2** |
| Movie | 69.2 | 72.5 | 74.3 | **75.3** |
| Auto | 63.7 | 65.8 | 74.9 | **66.5** |
| Amazon | 63.4 | 67.8 | 66.9 | **71.5** |
| **Science** | **29.3** | 31.5 | 23.8 | **41.6** ⬆️ |
| Historic | 65.7 | 68.2 | 72.2 | **69.9** |
| **Macro Avg** | 57.6 | 64.2 | 66.1 | **65.7** |

> 💡 **亮点**：在 **Science** 领域（科学论文摘要），LELA 显著优于所有基线（比 ReFinED 高近 18 个百分点），显示出其在复杂、专业文本中的强大鲁棒性。

#### 在 MHERCL 数据集上的 EL F1（%, 95% CI）

| Method | ELF1 |
|--------|------|
| GLiNKER | 16 ± 1.5 |
| BLINK+NER | 47 ± 2.0 |
| Relik | 44 ± 2.0 |
| ReFinED | 49 ± 2.0 |
| **LELA (Ours)** | **56 ± 2.0** ✅ |

> 🏆 **State-of-the-art result**：LELA 在极具挑战性的长尾音乐实体链接任务上建立新的 SOTA，显著超越监督方法（如 ReFinED）和其他 zero-shot 方法。

### 对比结论
- 尽管 ReFinED 和 Relik 是全监督模型，在通用领域表现强劲，但在**未见过的专业领域**（如 Science 或 Music Heritage）表现下降明显。
- LELA 凭借 **LLM 的推理能力**，在 zero-shot 条件下仍能保持高准确性，尤其擅长处理模糊性和上下文复杂的 mention。
- 当与相同 NER 组件配合时，LELA 明显优于 BLINK，证明了 **LLM-based disambiguation 的有效性**。

> ❌ **无消融实验报告**：文中未提供对各模块（如 NER、reranker、self-consistency）的 ablation study。

---

## 4. 关键结论和发现

### 主要发现
- ✅ **LLMs 能有效支撑端到端的 zero-shot EL**：通过结合 LLM 的语义理解与推理能力，LELA 成功实现了无需训练即可在多样化领域中执行高质量实体链接。
- ✅ **模块化设计提升实用性**：用户可根据资源限制（GPU/CPU）、速度需求或精度目标灵活选择组件组合。
- ✅ **在专业与长尾领域具有显著优势**：尤其在科学、历史、音乐遗产等监督方法难以覆盖的领域，LELA 展现出更强的泛化能力和鲁棒性。
- ✅ **支持用户自定义 KB**：这是区别于多数封闭系统的重大优势，极大增强了在工业界的应用潜力。

### 方法的局限性
- ⚠️ **计算开销较大**：使用大尺寸 LLM（如 Qwen3-30B）进行推理需要较强的 GPU 支持；尽管支持轻量模型和 CPU 推理（via llama.cpp），但性能会有所下降。
- ⚠️ **依赖描述质量**：KB 中 entity 的 description 质量直接影响检索与消歧效果；若描述缺失或不准确，性能可能下降。
- ⚠️ **未支持结构化 KB 格式**：目前仅接受 JSONL，尚不支持 RDF/Turtle 等主流知识图谱序列化格式（作者已在 future work 中提出改进计划）。

### 未来工作方向
- 🔧 **增加更多 pipeline 组件**：例如引入更先进的 zero-shot NER 或 retrieval 模型。
- 📦 **支持 Turtle/RDF 格式的 KB 输入**
- 🤖 **自动化生成 entity description 和 NER labels**
- 🌐 **优化 Web UI 功能**，增强交互体验与调试能力

---

📌 **总结一句话**：  
**LELA 是首个真正实现 zero-shot、端到端、模块化且开放可用的 LLM-based Entity Linking 框架，在多样领域尤其是专业与长尾场景中表现出卓越性能，为现实世界中的定制化 EL 应用提供了强大工具。**

🔗 开源地址：[https://github.com/NDobricic/LELA](https://github.com/NDobricic/LELA)  
🎥 演示视频：[https://www.youtube.com/watch?v=WdupiRjLbR4](https://www.youtube.com/watch?v=WdupiRjLbR4)

</details>

---

### 16. [Verilog-Evolve: Feedback-Driven and Skill-Evolving Verilog Generation](https://arxiv.org/abs/2605.26498)

**Authors**: Zehua Pei, Hui-Ling Zhen, Yu Zhang, Sinno Jialin Pan, Mingxuan Yuan, Bei Yu  
**Category**: cs.CL  
**Published**: 2026-05-27  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.26498v1  

#### Abstract
Large language models (LLMs) have improved Verilog generation from natural-language specifications, but most pipelines still treat generation as isolated sampling followed by functional checking. This is insufficient for practical RTL design, where useful Verilog must be correct, synthesizable, timi...

---

### 17. [LLMs Are Already Good Tutors: Training-Free Prompt Optimization for Pedagogical Math Tutoring](https://arxiv.org/abs/2605.27088)

**Authors**: Unggi Lee, Minchul Shin, Yeil Jeong, Sookbun Lee, Jeongsu Moon, Kyungtae Joo, Eunjoo Lee, Hoilym Kwon  
**Category**: cs.CL  
**Published**: 2026-05-27  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.27088v1  

#### Abstract
Aligning LLMs for math tutoring typically requires RL-based training with multi-GPU infrastructure. We investigate whether training-free prompt optimization-evolving only the system prompt via API calls-can serve as a practical alternative. We adapt 7 published methods and propose 5 education-specia...

---

### 18. [Not All Tokens Matter Equally: Dynamic In-context Vector Distillation with Decisive-Token Supervision for Long-form Medical Report Generation](https://arxiv.org/abs/2605.27194)

**Authors**: Ning Wu, Rui Liu, Xinkun Lin, Weixing Chen, Jinxi Xiang, Tao Wei, Lina Yao, Mingjie Li  
**Category**: cs.CL  
**Published**: 2026-05-27  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.27194v1  

#### Abstract
Distilling demonstration effects into hidden-space interventions offers a lightweight alternative to full finetuning. However, existing multimodal variants are mostly evaluated on short-form tasks, where outputs end after a few tokens. Extending these methods to long-form generation exposes a fundam...

---

### 19. [MTL-FNO: A Lightweight Multi-Task Fourier Neural Operator for Sparse Field Reconstruction](https://arxiv.org/abs/2605.26718)

**Authors**: Siyu Ye, Shihang Li, Zhiqiang Gong, Benrong Zhang, Weien Zhou, Yiyong Huang, Wen Yao  
**Category**: cs.LG  
**Published**: 2026-05-27  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.26718v1  

#### Abstract
Efficient onboard multi-field sparse reconstruction is essential for the autonomous operation of aerospace vehicles. While existing deep learning models exhibit promise for single-field reconstruction, deploying multiple independent models leads to prohibitive model size growth and fails to exploit ...

---

### 20. [Tail-Aware HiFloat4: W4A4 Post-Training Quantization for Wan2.2](https://arxiv.org/abs/2605.26628)

**Authors**: Zhanfeng Feng, Shuai Guo, Xin Di, Long Peng, Yang Cao, Zhengjun Zha  
**Category**: cs.AI  
**Published**: 2026-05-27  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.26628v1  

#### Abstract
This report describes Tail-Aware HiFloat4, our submission to the low-bit text-to-video generation quantization challenge. Our method adapts the public ViDiT-Q post-training quantization pipeline to Wan2.2 under the HiFloat4 numerical format. We quantize the main linear layers in both Wan2.2 transfor...

---

### 21. [Uncertainty-Aware Budget Allocation for Adaptive Test-Time Reasoning](https://arxiv.org/abs/2605.26849)

**Authors**: Manh Nguyen, Sunil Gupta, Hung Le  
**Category**: cs.CL  
**Published**: 2026-05-27  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.26849v1  

#### Abstract
Sampling multiple responses improves language model reasoning, but uniform compute allocation is inefficient: easy questions are over-sampled while hard questions remain under-explored. We propose Uncertainty-Aware Budget Allocation (UAB), a concave integer optimization framework that reallocates a ...

---

### 22. [Telenor Nordics Customer Service self-help corpus](https://arxiv.org/abs/2605.26891)

**Authors**: Mike Riess  
**Category**: cs.CL  
**Published**: 2026-05-27  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.26891v1  

#### Abstract
This paper presents a multilingual customer service self-help corpus comprising 1,122 manually validated documents in Finnish, Danish, Norwegian, and Swedish, totaling over one million tokens. The documents have been sourced from the public self-help pages of four Nordic telecommunications operators...

---

### 23. [Share More, Search Less: Collaborative Parallel Thinking for Efficient Test-Time Scaling](https://arxiv.org/abs/2605.27030)

**Authors**: Xinglin Wang, Hao Lin, Shaoxiong Feng, Peiwen Yuan, Yiwei Li, Jiayi Shi, Yueqi Zhang, Chuyi Tan, Ji Zhang, Boyuan Pan, Yao Hu, Kan Li  
**Category**: cs.CL  
**Published**: 2026-05-27  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.27030v1  

#### Abstract
Test-Time Scaling (TTS) enhances the reasoning capabilities of large language models by allocating additional inference compute to explore the solution space. However, existing parallel TTS methods typically keep branches isolated during search: intermediate discoveries remain branch-private and can...

---

### 24. [Neural Bayesian Sequential Routing](https://arxiv.org/abs/2605.26147)

**Authors**: Yongchao Huang  
**Category**: cs.LG  
**Published**: 2026-05-27  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.26147v1  

#### Abstract
Human decision-making is sequential and uncertainty-aware, yet standard neural networks often rely on static, dense forward computation with limited visibility into evidence acquisition, uncertainty evolution, or when computation should stop. We introduce \textbf{Neural Bayesian Sequential Routing (...

---

### 25. [Scaling World-Model Reinforcement Learning Through Diffusion Policy Optimization](https://arxiv.org/abs/2605.26282)

**Authors**: Xiaoyuan Cheng, Wenxuan Yuan, Zhancun Mu, Yuanzhao Zhang, Yiming Yang, Hai Wang, Zhuo Sun, Che Liu  
**Category**: cs.LG  
**Published**: 2026-05-27  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.26282v1  

#### Abstract
Model-based reinforcement learning (RL) can be effectively supported at scale through the use of world models. However, in practice, scaling such approaches remains fundamentally limited. A commonly recognized challenge is model bias and error compounding, which degrade long-horizon predictions. Bey...

---

### 26. [RT-Lynx: Putting the GEMM Sparsity In a Right Way for Diffusion Models](https://arxiv.org/abs/2605.26632)

**Authors**: Xing Cong, Hanlin Tang, Kan Liu, Lan Tao, Lin Qu, Chenhao Xie  
**Category**: cs.LG  
**Published**: 2026-05-27  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.26632v1  

#### Abstract
Diffusion Transformers (DiT) achieve strong performance in image generation but incur substantial inference costs. While prior work has reduced this cost via quantization and distillation, semi-structured sparsity, which can nearly halve FLOPs, remains underexplored. A key reason is that most existi...

---

### 27. [WINDQuant: Weight-Informed Neural Decision-Making for Global Mixed-Precision LLM Quantization](https://arxiv.org/abs/2605.26660)

**Authors**: Phong Nam Huu Nguyen, Khoi M. Le, Cong-Duy T Nguyen, Anh Tuan Luu, Thong Thanh Nguyen, Tho Quan  
**Category**: cs.LG  
**Published**: 2026-05-27  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.26660v1  

#### Abstract
Quantization is an effective approach to reduce the memory footprint and inference cost of large language models (LLMs), yet maintaining performance in the ultra-low-bit regime remains challenging. Existing post-training methods often suffer from severe accuracy degradation, while quantization-aware...

---

### 28. [Pretrained Approximators for Low-Thrust Trajectory Cost and Reachability](https://arxiv.org/abs/2605.26790)

**Authors**: Zhong Zhang, Giacomo Acciarini, Dario Izzo, Hexi Baoyin, Francesco Topputo  
**Category**: cs.LG  
**Published**: 2026-05-27  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.26790v1  

#### Abstract
Low-thrust trajectory design relies heavily on repeated evaluations of fuel consumption and transfer feasibility, which require expensive optimal control solutions. In this work, we show these quantities can be accurately approximated by machine learning surrogates, enabling fast and scalable evalua...

---

### 29. [Neuro-Symbolic Verification of LLM Outputs for Data-Sensitive Domains (extended preprint)](https://arxiv.org/abs/2605.26942)

**Authors**: Paul Sigloch, Christoph Benzm\"uller  
**Category**: cs.AI  
**Published**: 2026-05-27  
**Score**: 6.5  
**Type**: new  
**ArXiv ID**: 2605.26942v1  

#### Abstract
LLMs deployed in high-stakes domains face fundamental reliability challenges: hallucinations, inconsistencies, and privacy vulnerabilities introduce unacceptable risks where errors carry legal, financial, or safety consequences. This paper presents a hybrid verification architecture combining formal...

---

### 30. [Why Prompt Optimization Works, and Why It Sometimes Doesn't: A Causal-Inspired Edit-Level Analysis](https://arxiv.org/abs/2605.26655)

**Authors**: Shuzhi Gong, Hechuan Wen  
**Category**: cs.CL  
**Published**: 2026-05-27  
**Score**: 6.5  
**Type**: new  
**ArXiv ID**: 2605.26655v1  

#### Abstract
Automated prompt optimization methods (e.g., DSpy, TextGrad) can substantially improve the performance of large language model (LLM), however, their generalization ability across different tasks remains underperformed. In practice, the superiority of the optimized prompt on one benchmark often fails...

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
