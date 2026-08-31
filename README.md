# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-08-31 12:16:09 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [A Probabilistic Interpretation of KV Cache Eviction](https://arxiv.org/abs/2608.28293v1)

**Authors**: Renato Geh, Alex Chen, Daniel Israel, Aditya Grover, Guy Van den Broeck  
**Category**: cs.CL  
**Published**: 2026-08-31  
**Score**: 73.5  
**Type**: new  
**ArXiv ID**: 2608.28293v1  

#### Abstract
The premise and promise of KV (cache) eviction is simple: higher throughput can be achieved by evicting some entries from the KV cache, at a negligible cost to quality. This holds empirically for many existing methods, though most rely on creative heuristics for selecting which entries to drop. Desp...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：A Probabilistic Interpretation of KV Cache Eviction
1. 论文的主要贡献和创新点
✅ 解决的问题
现有KV缓存驱逐方法多依赖启发式策略选择需丢弃的条目，该问题在现有文献中一直是非正式的；同时驱逐过程中“解码时修正被驱逐条目”的问题长期被忽略，导致现有方法泛化性与性能存在局限。

🚀 提出的新方法与思路
**KV驱逐问题形式化**：正式定义KV驱逐问题，并证明该问题在计算上是困难的。
**概率视角转换**：从概率角度将KV驱逐问题转化为可通过采样近似的期望估计问题。
**解码时修正方案**：基于概率解释，让解码时修正被驱逐条目（此前被忽略的问题）变得可行。
**偏差分析与调整**：指出现有方法是零方差偏差估计器，可调整其结构以支持解码时修正。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 问题形式化 | 正式定义KV驱逐问题并明确其计算复杂度属性，解决问题的非正式性缺陷 |
| 驱逐策略科学性 | 替代启发式策略，采用可采样近似的概率方法，提升驱逐逻辑的合理性 |
| 解码兼容性 | 支持解码时修正被驱逐条目，解决此前被忽略的修正问题 |
| 跨任务鲁棒性 | 相比现有方法，对不同任务的鲁棒性更强 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：论文未报告
⚔️ 基线方法对比：论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总：论文未报告

4. 关键结论和发现
- 主要发现：1. KV驱逐问题经形式化后被证明是计算复杂的；2. 从概率视角可将KV驱逐问题转化为可通过采样近似的期望估计问题；3. 该概率解释使此前被忽略的“解码时修正被驱逐条目”问题成为可行；4. 现有KV驱逐方法属于零方差偏差估计器，可调整以支持解码时修正。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文通过概率视角对KV缓存驱逐问题进行正式定义与分析，提出将KV驱逐转化为可采样近似的期望估计问题的思路及解码时修正被驱逐条目的方案，使方法对不同任务更鲁棒，且在相同压缩预算下具备竞争力。

</details>

---

### 2. [Trajectory-Level Speculative Decoding for Diffusion Language Models](https://arxiv.org/abs/2608.27514v1)

**Authors**: Tianxiang Pan, Baitao Gong, Mo Guang, Hongwei Yong, Tianpeng Jiang, Yaqian Li, Zheng Cao, Kaiwen Long  
**Category**: cs.CL  
**Published**: 2026-08-31  
**Score**: 54.5  
**Type**: new  
**ArXiv ID**: 2608.27514v1  

#### Abstract
Diffusion-based language models (dLLMs) enable parallel token generation through iterative denoising, but existing decoding strategies collapse to single-token generation under low confidence, severely limiting throughput. Unlike autoregressive models where speculative decoding operates on token seq...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Trajectory-Level Speculative Decoding for Diffusion Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题
现有扩散语言模型（dLLMs）在低置信度下的解码策略会退化为单令牌生成，严重限制吞吐量；且自回归模型的投机解码基于固定左右顺序的令牌序列，与dLLMs需推测带明确位置和未掩盖顺序的多令牌更新序列（即去噪轨迹）的特性不匹配。

🚀 提出的新方法与思路
**Trajectory-Level Speculative Framework**：通过置信度分层树探索构建草稿去噪轨迹，并采用带双向注意力掩码的分块并行评估对轨迹进行验证。
**Inter-Block Speculation**：利用扩散模型的双向结构执行跨块前瞻，进一步优化解码效率。
该方法基于Fast-dLLM的双缓存基础设施，减少去噪迭代次数。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 去噪迭代数 | 减少30-40% |
| 吞吐量（令牌/步） | 从2.6提升至4.3 |
| 推理速度 | 比普通dLLMs提升7-14x，比Fast-dLLM提升1.3x |
| 准确率变化 | 小于1% |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 推理与代码基准（具体名称未明确） | 评估模型在推理、代码任务上的解码性能 |

🎯 实验设置与评估指标
任务：优化扩散语言模型的解码效率，同时保持生成准确率
| 指标 | 含义 |
| ---- | ---- |
| 去噪迭代数 | ↓ 越低越好 |
| 吞吐量（令牌/步） | ↑ 越高越好 |
| 推理速度 | ↑ 越高越好 |
| 准确率变化 | ± 越小越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| vanilla dLLMs | 扩散语言模型 | 原始未优化的解码策略 |
| Fast-dLLM | 扩散语言模型 | 采用双缓存基础设施的改进模型 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告各实验对应的表号、图号等来源，以下为摘要明确提及的结果：
1. 主benchmark性能：论文仅提及在推理和代码基准上的准确率变化小于1%，未报告其他相关指标。
2. 效率对比：提及减少去噪迭代30-40%，令牌/步从2.6提升至4.3，推理速度比vanilla dLLMs提升7-14x，比Fast-dLLM提升1.3x。
3. 跨域/zero-shot迁移：论文未报告。
4. 鲁棒性/扰动测试：论文未报告。
5. 消融实验：论文未报告。

4. 关键结论和发现
- 主要发现：① 针对扩散语言模型低置信度下吞吐量受限的核心问题，提出的轨迹级投机解码框架有效适配了dLLMs的去噪轨迹特性，提升了解码效率；② 结合置信度分层树探索、块间投机及双向注意力掩码的分块评估策略，在保持极低准确率损失（<1%）的前提下实现显著加速；③ 基于Fast-dLLM的双缓存基础设施增强了方法的实用性。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：该论文提出的Trajectory-Level Speculative Decoding框架，通过适配扩散语言模型特性的轨迹级投机机制，在仅保持小于1%准确率变化的情况下，大幅降低去噪迭代数并提升解码吞吐量与速度。

</details>

---

### 3. [Great Expectations: Benchmarking the Real-World Performance of RVV 1.0 in HPC](https://arxiv.org/abs/2608.28097v1)

**Authors**: Stepan Nassyr, Prateek Chawla, Daniel Seibel, Jayesh Badwaik, Kaveh Haghighi Mood, Andreas Herten  
**Category**: cs.DC  
**Published**: 2026-08-31  
**Score**: 54.5  
**Type**: new  
**ArXiv ID**: 2608.28097v1  

#### Abstract
Following the ratification of the RISC-V Vector Extension (RVV 1.0), new commercially available silicon has been adopting the extension. This paper revisits the question of RISC-V viability for High-Performance-Computing (HPC) by benchmarking the latest RVV 1.0-capable hardware (SiFive X280 (Tenstor...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Great Expectations: Benchmarking the Real-World Performance of RVV 1.0 in HPC
1. 论文的主要贡献和创新点
✅ 解决的问题
① 此前RISC-V在高性能计算（HPC）领域的可行性尚未得到充分验证；② RVV 1.0标准获批后，商用RISC-V芯片已开始采用该扩展，但硬件存在特定实现挑战，且缺乏最新RVV 1.0硬件在HPC场景下的实测对比数据。
🚀 提出的新方法与思路
**RVV 1.0 HPC多维度基准评估方案**：选取多款最新商用RVV 1.0-capable硬件，采用标准HPC基准（BLAS、FFTW、HPL、HPCG）与合成负载（STREAM、FMA throughput）作为测试集，与状态-of-the-art HPC ARM64芯片（NVIDIA Grace）进行性能对比，分析RVV 1.0在HPC场景下的实际表现。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 评估覆盖范围 | 针对最新商用RVV 1.0硬件开展测试，填补了该领域实测数据空白 |
| 基准设计 | 采用真实HPC基准与合成负载结合的方式，实现对RVV硬件性能的多维度评估 |
| 参照对比 | 与顶级HPC ARM64芯片对比，提供RISC-V用于HPC的性能参照 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 标准HPC基准（BLAS、FFTW、HPL、HPCG） | 评估HPC场景下的真实性能 |
| 合成负载（STREAM、FMA throughput） | 评估向量单元的基础性能 |
🎯 实验设置与评估指标
本实验的核心任务是评估多款RVV 1.0-capable硬件在HPC场景下的性能表现，并与状态-of-the-art HPC ARM64芯片（NVIDIA Grace）进行对比分析。论文未报告具体评估指标及相关定义。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| NVIDIA Grace | 基线方法 | 状态-of-the-art HPC ARM64芯片 |
| SiFive X280 (Tenstorrent Blackhole) | 受试RVV硬件 | 支持RVV 1.0 |
| SpacemiT X60 (K1) | 受试RVV硬件 | 支持RVV 1.0 |
| SpacemiT X100/A100 (K3) | 受试RVV硬件 | 支持RVV 1.0 |
| T-Head C920v2 (Sophon SG2044) | 受试RVV硬件 | 支持RVV 1.0 |

3. 主要实验结果和性能指标
📊 定量结果汇总
本部分所有实验内容，论文未报告：
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：① RVV 1.0相比标量执行可带来显著的性能提升；② 各类RVV 1.0硬件存在特定的实现挑战；③ 目前仍有多项障碍阻碍RISC-V（含RVV）成为HPC领域的主流架构。
- 方法局限性：仅评估了指定的几款RVV 1.0-capable硬件，未覆盖所有商用RVV 1.0设备。
- 未来工作：解决RVV相关的剩余障碍，推动RISC-V成为HPC领域的主流架构。

> ✅ **总结一句话**：该论文通过对多款最新商用RVV 1.0硬件开展HPC场景的多维度基准测试，为评估RISC-V在高性能计算领域的可行性提供了实测分析依据。

</details>

---

### 4. [Marginal Coverage Credit Reduces Redundant Exploration in Parallel State-Entropy Optimization](https://arxiv.org/abs/2608.27507v1)

**Authors**: Junhao Cao, Hongyi Xia, Jianian Wu, Xiaopeng Yi, Lixia Huang, Ping Guo  
**Category**: cs.LG  
**Published**: 2026-08-31  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2608.27507v1  

#### Abstract
Policy Gradient for Parallel State Entropy maximization (PGPSE) expands state-space coverage by training independently parameterized policies in replicated copies of the same environment. However, its pooled team-entropy score measures only collective exploration and cannot identify policies that co...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Marginal Coverage Credit Reduces Redundant Exploration in Parallel State-Entropy Optimization
1. 论文的主要贡献和创新点
✅ 解决的问题
原PGPSE（Policy Gradient for Parallel State Entropy maximization）通过复制相同环境的独立参数策略扩展状态空间覆盖，但它的池化团队熵分数仅衡量集体探索，无法识别贡献非冗余覆盖的策略。

🚀 提出的新方法与思路
**Marginal Coverage Credit (MCC-PGPSE)**
结合leave-one-policy-out coverage与state-owner specialization来估计策略专属信用；保留PGPSE的池化目标，基于该信用分配非负的辅助内在奖励，总奖励质量不变，以此抑制冗余访问，促进策略间的互补覆盖。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 策略贡献识别 | PGPSE仅衡量集体探索，无法识别策略的非冗余覆盖贡献；MCC-PGPSE可估计策略专属信用，明确识别非冗余覆盖贡献 |
| 奖励分配效果 | PGPSE无针对冗余探索的奖励设计；MCC-PGPSE的奖励分配基于策略贡献，总奖励质量不变，能减少冗余访问，推动互补覆盖 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 受控环境 | 验证MCC-PGPSE的核心设计 |
| 7个公开离散状态基准 | 公共标准性能测试 |
| 原始PGPSE协议的Room和Maze设置 | 与原PGPSE方法的对比实验 |

🎯 实验设置与评估指标
任务为离散状态空间下的并行策略探索，以最大化状态覆盖的团队性能。
| 指标 | 含义（箭头） |
| --- | --- |
| 归一化团队状态熵 | 衡量团队整体的状态覆盖程度，↑越高越好 |
| 状态支持 | 衡量已覆盖的有效状态数量，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Entropy baseline | 基准方法 | 熵基线，用于性能对比 |
| PGPSE | 原方法 | 并行状态熵最大化的原方法，用于对比 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体实验对应的表号、图号及精确数值，仅报告相关结论：
- 主benchmark性能：在受控环境、7个公开离散基准、原始PGPSE协议的Room和Maze（5种子）实验中，MCC-PGPSE产生正的归一化团队状态熵和状态支持最终窗口增益；受控任务与固定公共基准的对比结果显著，5种子原协议对比结果方向一致。
- 效率对比：论文未报告
- 跨域/zero-shot迁移：论文未报告
- 鲁棒性/扰动测试：论文未报告
- 消融实验：大部分增益源于leave-one-policy-out coverage，而非非均匀加权、不匹配的信用分配或神经新奇性单独作用。

消融实验：
| 模块名称 | Leave-one策略外覆盖 | 非均匀加权 | 不匹配信用 | 神经新奇性 |
| --- | --- | --- | --- | --- |
| 是否启用 | ✅ | ❌ | ❌ | ❌ |
| 指标最优性 | ✅ | ❌ | ❌ | ❌ |
💡 结论：MCC-PGPSE的增益主要来自基于leave-one策略外覆盖的贡献信用分配，其他因素贡献较小。

4. 关键结论和发现
- 主要发现：1. MCC-PGPSE在离散状态空间并行策略探索中，相比熵基线可取得正的团队状态覆盖性能增益；2. 固定公共基准的MCC-PGPSE与基线对比结果显著，原始PGPSE协议的5种子对比结果方向一致；3. MCC-PGPSE的核心增益来自leave-one策略外覆盖的贡献信用分配。
- 方法局限性：论文未报告
- 未来工作：论文未报告

✅ **总结一句话**：提出MCC-PGPSE，结合leave-one策略外覆盖与状态所有者专业化估计策略专属信用，基于该信用分配辅助奖励，在离散空间并行策略探索中减少冗余、提升互补覆盖。

</details>

---

### 5. [SciReC: Diagnostic Evaluation of Multimodal, Multi-Turn Relational Reasoning with Adaptive Interaction](https://arxiv.org/abs/2608.27461v1)

**Authors**: Nilay Yilmaz, Naga Sai Abhiram Kusumba, Stella Wenxing Liu, Yezhou Yang  
**Category**: cs.CL  
**Published**: 2026-08-31  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2608.27461v1  

#### Abstract
Relational reasoning requires the process of perceptual understanding, comparing, and integrating the underlying relationships between concepts. This ability consists of multiple categories, such as analogical, structural, and cause-effect, each capturing a different aspect of higher-order understan...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：SciReC: Diagnostic Evaluation of Multimodal, Multi-Turn Relational Reasoning with Adaptive Interaction

1. 论文的主要贡献和创新点
✅ 解决的问题
- 缺乏适配多模态、多轮交互场景的关系推理评估基准，难以有效评估多模态大语言模型（MLLM）在高阶关系推理任务上的性能；
- 缺少可量化的诊断框架，无法明确区分视觉理解、领域知识、记忆回忆等不同因素对MLLM关系推理任务的贡献，难以定位推理失败的核心原因。

🚀 提出的新方法与思路
**SciReC**：开发模型自适应的多模态学术对话基准，用于评估MLLM在各类关系推理任务（类比、结构、因果等）上的表现。
**DMRA**：提出基于缺陷的诊断框架，通过量化视觉理解、领域知识、记忆回忆等组件的贡献，定位关系推理失败案例的主要原因。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 评估基准 | 适配多模态、多轮的学术对话场景，针对性评估MLLM的关系推理能力 |
| 错误诊断 | 可量化各组件对关系推理任务的贡献，明确推理失败的核心原因 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| SciReC | 用于评估MLLM在多模态、多轮关系推理任务（学术对话场景）上的性能 |

🎯 实验设置与评估指标
任务：评估MLLM在不同类型关系推理、不同学术领域的性能，及定位关系推理失败的核心原因。
| 指标 | 含义 |
| ---- | ---- |
| 关系推理性能 | 衡量模型在关系推理任务上的表现，值越高越好 |
| DMRA诊断结果 | 区分不同类型错误的占比，用于定位推理失败原因 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Claude 4.6 | 闭源模型 | 整体关系推理性能最优 |
| GPT 5.4 | 闭源模型 | 整体关系推理性能次于Claude 4.6 |
| 开源模型 | 开源模型 | 在空间关系推理任务上表现最差 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能**：论文报告不同模型的整体关系推理性能，Claude 4.6表现最优，GPT 5.4次之；开源模型在空间关系任务上得分最低，闭源模型在层次和序列关系任务上得分更低；跨领域性能上，模型在天文领域得分最低，心理领域得分最高。
**效率对比**：论文未报告
**跨域 / zero-shot 迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告

💡 结论：不同模型、关系类型及学术领域的关系推理性能存在明显差异，关系推理错误是MLLM关系推理失败的主要原因。

4. 关键结论和发现
- 闭源模型在整体关系推理任务上的表现优于开源模型，但各模型的弱点不同：开源模型在空间关系上表现差，闭源模型在层次和序列关系上表现更差；
- 关系推理性能存在跨领域差异，天文领域的关系推理任务难度最高，心理领域难度最低；
- 所有模型关系推理失败的核心原因中，关系推理错误占比最高，其次是记忆限制错误。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出适配学术对话场景的多模态关系推理评估基准SciReC及缺陷诊断框架DMRA，通过实验明确了不同MLLM、任务类型及学术领域的关系推理性能差异与错误分布特征。

</details>

---

### 6. [There and Back Again: Bidirectional Diffusion Bridges for Multimodality Translation](https://arxiv.org/abs/2608.27885v1)

**Authors**: Gabe Guo, Elon Litman, Thanawat Sornwanee, Jose Blanchet, Stefano Ermon  
**Category**: cs.LG  
**Published**: 2026-08-31  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2608.27885v1  

#### Abstract
Multimodality translation (e.g., text-to-image) is a core generative AI task. However, existing approaches (1) follow generative paths that do not directly represent the source modality, limiting the flexibility of some sampling algorithms; and (2) are unidirectional, preventing inversion (e.g., ima...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

There and Back Again: Bidirectional Diffusion Bridges for Multimodality Translation
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多模态翻译（如文本到图像）方法存在两大缺陷：①生成路径不直接表征源模态，限制了部分采样算法的灵活性；②为单向结构，无法实现逆生成过程（如图像转文本）。

🚀 提出的新方法与思路
**BIT: Bidirectional Image-Text Diffusion Bridges**，该方法与以往方法不同，直接从源模态（文本）出发插值至目标模态（图像），提供源感知的生成路径，支持多样化灵活采样算法；同时为端点条件化过程，可实现从图像到文本的遍历，构成统一的双向生成框架；该方法通过随机微积分推导得到适合模拟的SDE形式，以及可处理高维数据的易处理损失函数。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 源模态表征 | 生成路径直接表征源模态，支持多样化灵活采样算法 |
| 生成方向性 | 端点条件化设计，可实现双向生成过程（如文本→图像、图像→文本） |
| 模型扩展性 | 推导得到适合模拟的SDE形式及可处理高维数据的损失函数，可扩展至高维度数据 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告具体采用的数据集 |

🎯 实验设置与评估指标
任务为多模态翻译（如文本到图像）的生成性能评估，论文未报告具体的评估指标及其含义。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 去噪扩散（denoising-diffusion）基线 | 多模态生成基线 | 采用传统去噪扩散模型 |
| 确定性流（deterministic-flow）基线 | 多模态生成基线 | 采用传统确定性流模型 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告
2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：提出的BIT方法与去噪扩散、确定性流基线方法相比具有竞争力，在多个视觉-语言及自然科学评估任务上表现更优。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本论文提出了双向图像文本扩散桥（BIT），构建了统一的双向多模态生成框架，具备源感知的生成路径与灵活采样能力，在多模态翻译任务中相比基线方法展现出更优的性能。

</details>

---

### 7. [VICT: Verifier-Instrumented Credit Tracing for Long-Horizon LLM Agent Reinforcement Learning](https://arxiv.org/abs/2608.28128v1)

**Authors**: Pengcheng Li, Zhengyang Zhang, Dongxu Zhang, Sui Huang, Shaohua Ma  
**Category**: cs.LG  
**Published**: 2026-08-31  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2608.28128v1  

#### Abstract
Fine-grained credit assignment is a central challenge in reinforcement learning for long horizon LLM agents. Standard objectives often train from programmatically verifiable terminal rewards by broadcasting each sparse outcome to every action in a trajectory. Existing methods typically seek finer cr...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

VICT: Verifier-Instrumented Credit Tracing for Long-Horizon LLM Agent Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
长horizon LLM agent的强化学习中，细粒度信用分配是核心挑战：现有细粒度信用方法从rollout侧估计动作重要性，仍将判断任务成功的验证器视为仅返回标量奖励的模块，丢弃了验证器内部编码的任务结构；仅基于终端奖励的训练则将稀疏结果均匀分配给轨迹所有动作，信用分配粗糙。
🚀 提出的新方法与思路
**VICT (Verifier-Instrumented Credit Tracing)**：一种训练时的接口，可暴露验证器中可执行或有证据支持的原子，再通过验证依赖关系的证明边将这些原子追溯到轨迹对应动作；仅沿证明边重新分配组相对优势，将信用分配核心从rollout侧推断转移到验证器侧追溯；该方法保留任务原始终端奖励，证据不完整或模糊时不随意分配信用，仅修改训练时的优势张量，无需学习评论者、过程标签、分支rollouts，也无需推理时访问验证器。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 信用分配逻辑 | 现有方法聚焦rollout侧动作重要性推断，VICT利用验证器内部结构转向验证器侧依赖追溯 |
| 额外模块需求 | 现有细粒度方法需学习评论者、过程标签等，VICT无需上述额外模块 |
| 奖励保留 | VICT保留任务原始终端奖励，避免破坏原有监督信号 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| ALFWorld | 主基准性能验证 |
| WebShop | 主基准性能验证 |
🎯 实验设置与评估指标
实验任务为长horizon LLM agent强化学习任务，论文未报告具体评估指标定义。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Outcome-only training | 基线方法 | 仅基于终端奖励训练 |
| Recent fine-grained credit methods | 现有对比方法 | 从rollout侧估计动作重要性的细粒度信用方法 |
| VICT | 本文方法 | 从验证器侧追溯信用的细粒度分配方法 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能**
论文未报告具体数值；💡 结论：VICT在ALFWorld和WebShop上的表现显著优于Outcome-only training，且与近期细粒度信用方法性能相当。
**效率对比**
论文未报告。
**跨域/zero-shot迁移**
论文未报告。
**鲁棒性/扰动测试**
论文未报告。
**消融实验**
论文未提供定量数值，仅说明排除了Dense atom rewards、Final-commit credit、Temporal proximity、Sparsity是VICT性能提升的充分原因。
4. 关键结论和发现
- 主要发现：1. 现有聚焦rollout侧的细粒度信用方法未充分利用验证器内部任务结构；2. VICT通过验证器侧信用追溯接口，无需额外模块即可提升长horizon LLM agent RL性能；3. Dense atom rewards、Final-commit credit、Temporal proximity、Sparsity均不是VICT性能提升的充分解释。
- 方法局限性：论文未报告效率、跨域迁移、鲁棒性等实验结果，未提及其他基准的泛化能力。
- 未来工作：论文未提及。
> ✅ **总结一句话**：VICT通过训练时的验证器侧信用追溯接口，在长horizon LLM agent强化学习任务上大幅优于仅终端奖励训练，且性能与近期细粒度信用方法相当。

</details>

---

### 8. [When Can Conditional Flow Matching Replace Pointwise Negative Log-Likelihood?](https://arxiv.org/abs/2608.28010v1)

**Authors**: Yansen Han, Hongxin Sun, Tao Lin  
**Category**: cs.LG  
**Published**: 2026-08-31  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2608.28010v1  

#### Abstract
Flow matching enables likelihood-free training, yet alignment methods increasingly reuse conditional flow matching (CFM) losses as endpoint negative log-likelihoods (NLLs) and their old/new differences as log-likelihood ratios. We characterize when these substitutions are valid. For linear Gaussian ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

When Can Conditional Flow Matching Replace Pointwise Negative Log-Likelihood?
1. 论文的主要贡献和创新点
✅ 解决的问题
Flow matching支持似然-free训练，但现有对齐方法常将Conditional Flow Matching（CFM）损失重用为端点负对数似然（NLL）、将新/旧差异作为对数似然比，却未明确这种替代的有效性边界；同时普通CFM作为点wise NLL估计器的适用性存疑，on-policy时对数似然比仍有偏差。
🚀 提出的新方法与思路
**精确分解框架**：对线性高斯路径，将端点NLL精确分解为熵、加权CFM目标、内部速度-得分残差、边界残差，明确普通CFM仅当对应残差抵消时可作为端点NLL的近似估计；
**权重修正方案**：推导权重 $w_{\mathrm{sc}}(t)=(1-t)/t$ 可消除内部残差，使普通CFM在off-policy总体最优时成为点wise NLL估计器，但该结论无法推广到训练阶段或on-policy对齐场景。
🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 理论适配 | 提供似然型LLM方法适配到流匹配的理论依据 |
| 边界界定 | 明确CFM替代点wise NLL的适用与不适用场景，区分精确替代与受控代理 |
2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：论文未报告
⚔️ 基线方法对比：论文未报告
3. 主要实验结果和性能指标
所有实验相关内容：论文未报告
4. 关键结论和发现
- 主要发现
1. 线性高斯路径中，普通CFM作为端点NLL估计器的有效性依赖于对应残差的抵消，仅在残差抵消时近似成立；
2. 权重 $w_{\mathrm{sc}}(t)=(1-t)/t$ 仅能消除off-policy总体最优场景下的内部残差，无法推广到训练阶段或on-policy对齐；
3. on-policy场景下，即使端点分布相同或经代理优化，对数似然比仍存在偏差。
- 方法局限性
普通CFM的残差抵消及权重修正方案仅适用于特定场景，无法普遍解决CFM作为NLL估计器的偏差问题，on-policy时对数似然比仍有偏差。
- 未来工作：论文未报告
> ✅ **总结一句话**：这篇论文通过端点NLL的精确分解，明确了Conditional Flow Matching（CFM）替代点wise负对数似然（NLL）的有效性边界与适用场景，推导了相关修正方案，为似然型LLM方法适配流匹配提供了理论支撑。

</details>

---

### 9. [Conditional Diffusion Models for Energy-Efficient Driving](https://arxiv.org/abs/2608.28142v1)

**Authors**: Hemanth Neelgund Ramesh, Andr\'e Snoeck, Chyi-Fu Hong, Shijing Sun  
**Category**: cs.LG  
**Published**: 2026-08-31  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2608.28142v1  

#### Abstract
Electrification of commercial delivery fleets is shifting fleet routing from distance- and time-based optimization toward energy-aware decision-making. Existing sequence models primarily provide deterministic point estimates or limited uncertainty summaries, which do not capture the range of plausib...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Conditional Diffusion Models for Energy-Efficient Driving
1. 论文的主要贡献和创新点
✅ 解决的问题
现有序列模型主要提供确定性点估计或有限不确定性摘要，无法捕捉运营决策所需的合理能耗轨迹范围；而商用车队电气化后，车队路由需从基于距离和时间的优化转向能量感知的决策。

🚀 提出的新方法与思路
**Conditional Diffusion Framework**：结合latent conditioning encoder与temporal 1D U-Net denoising backbone，将行程相关的路线特征（如车辆速度、环境温度等）映射到共享表示，基于该共享表示引导反向扩散过程，生成对应路线特征条件的EV电池电流轨迹。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 分布匹配度 | 生成电流分布的Wasserstein距离（0.0029）低于真实vs真实样本间Wasserstein距离的参考值（0.0085），生成样本落在测试集的经验变异性内 |
| 轨迹预测性能 | 潜在条件注入方式相比直接条件注入方式，Wasserstein距离降低89.1%，MAE降低52.8%，性能提升显著 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| open-access commercial EV telemetry dataset | 评估提出的框架（包含12k trips，9 vehicles） |

🎯 实验设置与评估指标
任务：基于路线特征（如车辆速度、环境温度等）生成EV电池电流轨迹；
指标：Wasserstein距离（↓，衡量生成与实测电流分布的接近度）、MAE（↓，衡量生成与实测电流轨迹的均值绝对误差）；参考指标：真实vs真实样本间的Wasserstein距离（0.0085）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Direct Condition Injection | 对比方法 | 直接将条件注入模型，未采用潜在条件编码器 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告主基准性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验，仅给出以下定量结果：
- 生成电流分布的Wasserstein距离为0.0029，低于真实vs真实样本间的Wasserstein参考距离（0.0085）；
- 与Direct Condition Injection相比，潜在条件注入模型的Wasserstein距离降低89.1%，MAE降低52.8%。
💡 结论：论文提出的潜在条件扩散模型可生成符合EV真实电流轨迹特征的样本，分布匹配度优于测试集真实样本间的差异，且潜在条件注入设计显著提升了模型性能。

4. 关键结论和发现
- 主要发现：1. 提出的条件扩散框架能生成捕捉EV电流轨迹时间包络和瞬态事件的现实样本，生成样本的分布接近测试集真实分布；2. 潜在条件注入的设计相比直接条件注入，性能提升显著；3. 该模型为不确定性感知的大规模车队运营规划提供了重要基础。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：《Conditional Diffusion Models for Energy-Efficient Driving》提出的结合潜在条件编码器与时序1D U-Net主干的条件扩散框架，可生成符合EV真实能耗特征的电流轨迹，为能量感知的商用车队运营决策提供了不确定性建模支撑。

</details>

---

### 10. [Load-Bearing Context: The Question Damage Score for Evaluating Context Reliance in Linguistic Reasoning](https://arxiv.org/abs/2608.27756v1)

**Authors**: Neh Majmudar, Elena Filatova  
**Category**: cs.CL  
**Published**: 2026-08-31  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2608.27756v1  

#### Abstract
Determining whether large language models derive answers from context or prior knowledge remains a fundamental challenge. Self-contained linguistic olympiad puzzles provide a controlled setting where all answers derive solely from expert-designed context examples without external knowledge. Removing...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Load-Bearing Context: The Question Damage Score for Evaluating Context Reliance in Linguistic Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题：确定大语言模型（LLMs）的答案源自上下文还是先验知识是语言学推理领域的基础挑战，现有方法缺乏可控手段单独分析每个上下文示例对答案推导的作用。
🚀 提出的新方法与思路
**Question Damage Score**：采用两种删除单个上下文示例的干预操作（uniform random deletion和受错误纠正码启发的targeted deletion），基于移除上下文后对模型答案推导的影响，将语言学奥赛谜题分类为脆弱或鲁棒，结合53个UK Linguistics Olympiad自包含谜题（所有答案仅来自专家设计的上下文，无外部知识）实现对LLMs上下文依赖的细粒度分析。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 上下文依赖分析 | 提供细粒度分析能力，支持因果干预、停止集分析、目标污染研究及机械可解释性等多方向探索 |
| 研究设置 | 采用无外部知识干扰的受控设置，精准聚焦上下文的作用 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 53个UK Linguistics Olympiad puzzles | 作为受控研究设置，所有答案仅来自专家设计的上下文，排除外部知识干扰，用于分析模型的上下文依赖 |
🎯 实验设置与评估指标
任务：评估三个前沿LLMs在被要求“信息不足时拒绝回答”的指令下的上下文依赖情况。
| 指标 | 含义（箭头方向） |
| --- | --- |
| Question Damage Score | 论文未明确报告该指标的具体评估方向 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| - | - | 论文未报告 |
3. 主要实验结果和性能指标
1. 主benchmark性能：论文未报告
2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告
4. 关键结论和发现
- 主要发现：
  1. 被要求“信息不足时拒绝回答”的指令下，三个前沿LLMs很少执行拒绝回答的操作。
  2. 移除负载承重的上下文示例后，三个前沿LLMs仍常常生成正确答案，说明模型推导答案可能依赖先验知识而非输入上下文。
  3. 提出的Question Damage Score框架结合上下文删除干预，为分析LLMs的上下文依赖提供了可控且可扩展的研究工具。
- 方法局限性：论文未报告
- 未来工作：进一步调查LLMs的上下文推理能力、先验知识依赖、记忆特性及语言推理逻辑等，拓展框架应用于因果干预、停止集分析、目标污染研究及机械可解释性等方向。

> ✅ **总结一句话**：这篇论文提出Question Damage Score框架，通过删除UK语言学奥赛谜题中单个上下文示例的干预方法，结合受控的语言学奥赛数据集分析前沿LLMs的上下文依赖，发现模型在被要求信息不足时很少拒绝回答且常在移除关键上下文后仍生成正确答案，为语言学推理领域的上下文依赖研究提供了新的可控工具。

</details>

---

### 11. [Self-Explainable Multi-Label Graph Neural Network for Correlated Evidence Attribution](https://arxiv.org/abs/2608.27574v1)

**Authors**: Yingqi Feng, Yufei Tang, Min Shi, Xingquan Zhu  
**Category**: cs.LG  
**Published**: 2026-08-31  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2608.27574v1  

#### Abstract
Multi-label graph learning intends to capture the intrinsic complexity of real-world applications, where one sample is often related to multiple groups or consists of multiple objects. To date, a handful of multi-label graph learning methods exist, but none of them integrate training-time interpreta...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Self-Explainable Multi-Label Graph Neural Network for Correlated Evidence Attribution
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多标签图学习方法存在两类缺陷：一是缺乏训练时的解释能力；二是已有的后验图解释器未显式建模多标签图学习器中依赖的标签相关证据共享，尤其针对弱关联或负关联的标签对，会导致后验方法遗漏证据在不同标签间的共享或分离方式。

🚀 提出的新方法与思路
**SEMGNN**，一款端到端的自解释多标签图神经网络，在统一框架与训练目标中联合学习预测器和稀疏边缘掩码解释器；利用标签-标签相关性提升多标签节点分类性能，并强化每个标签对应的解释，使节点的不同标签能由既区分又关联的结构证据及/或相关证据支撑。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 多标签解释能力集成 | 具备训练时的解释能力，区别于仅采用后验解释的方法 |
| 标签相关证据建模 | 显式处理标签-标签间的证据共享与分离（针对弱/负关联标签对），避免后验方法遗漏证据关联逻辑 |
| 模型功能统一性 | 端到端实现多标签节点分类与标签条件下的证据贡献识别 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| synthetic multi-label networks, real-world multi-label networks (social networking, entertainment, life sciences domains) | 开展多标签节点分类及标签条件解释相关的对比实验 |

🎯 实验设置与评估指标
任务为多标签节点分类与标签条件下的证据归因。论文未报告具体评估指标。

⚔️ 基线方法对比
论文未报告具体基线方法列表。

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告

4. 关键结论和发现
- 主要发现：端到端自解释多标签图神经网络SEMGNN可同步实现多标签节点分类与对应标签的证据归因；利用标签相关性可兼顾多标签分类性能与解释的区分性、关联性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：SEMGNN是一款端到端的自解释多标签图神经网络，可在多标签节点分类任务中同步生成更贴合标签关联特性的保真、紧凑解释，弥补了现有多标签图学习方法在训练时解释能力与标签相关证据建模上的不足。

</details>

---

### 12. [Knowing Before Answering: Decoding Language Models for Reliable RAG](https://arxiv.org/abs/2608.27661v1)

**Authors**: Syed Mahbubul Huq, Christopher Child, Tillman Weyde, Pranava Madhyastha  
**Category**: cs.CL  
**Published**: 2026-08-31  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2608.27661v1  

#### Abstract
In Retrieval-Augmented Generation (RAG), retrieval may provide insufficient or conflicting information needed to answer a question. The system should not only know when to answer but also be able to identify cases in which the documents provided in RAG are insufficient or contain conflicting informa...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Knowing Before Answering: Decoding Language Models for Reliable RAG
1. 论文的主要贡献和创新点
✅ 解决的问题
在Retrieval-Augmented Generation（RAG）场景中，检索获取的信息可能存在不充足或冲突的情况，现有系统无法有效识别该类情形，导致生成内容不可靠。
🚀 提出的新方法与思路
**Three-way Classification RAG Triage**：将RAG检索信息的可信度判定转化为三类的分类任务，分别为信息充足、信息不足、信息冲突；
**LM Internal Signal-based Lightweight Linear Router**：利用语言模型的隐藏激活、注意力衍生特征作为输入，训练轻量线性模型，实现对上述三类的区分；
**Controlled Benchmark Construction**：构建复制RAG设置的受控基准数据集，使用人造信息并对每个实例标注为可回答、信息不足或信息冲突。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 多模型泛化 | 在16种涵盖不同架构和规模的语言模型上，效果始终优于基于提示的基线及专用RAG模型 |
| 信号有效性 | 分类最有用的信号位于中间层，隐藏激活状态相比注意力值、MLP特征输出更有效（大多数测试模型中） |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 受控基准数据集 | 模拟RAG场景，提供标注数据用于训练和测试分类模型 |
🎯 实验设置与评估指标
任务说明：针对RAG提供的信息，判断其是否充足、不足或冲突，属于三分类任务。
论文未报告具体评估指标及含义。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| prompting-based baselines | 基线方法 | 基于提示的RAG评估方式 |
| specialised RAG-models | 专用模型 | 针对RAG场景设计的专用语言模型 |

3. 主要实验结果和性能指标
📊 定量结果汇总
无对应表号，论文提到：在16种涵盖不同架构和范围规模的语言模型上，基于特征的路由器始终优于基于提示的基线和专用RAG模型的性能。
💡 结论：该论文构建的基于语言模型内部信号的轻量线性路由器，在多种语言模型中均实现了更优的RAG信息可信度分类效果。
其他实验结果：论文未报告
效率对比：论文未报告
跨域/zero-shot迁移：论文未报告
鲁棒性/扰动测试：论文未报告
消融实验：论文未报告

4. 关键结论和发现
- 主要发现：① 语言模型内部编码了检索证据是否足够支持回答的信号，该信号可被可靠解码用于RAG分流；② 用于三分类的最有效信号来自语言模型的中间层，且隐藏激活状态比注意力值或MLP特征输出更有效；③ 基于特征的轻量线性路由器在多种不同架构和规模的语言模型上，表现优于基于提示的基线方法和专用RAG模型。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出将RAG检索信息的可信度判定转化为三分类任务，利用语言模型内部的隐藏激活等信号训练轻量线性路由器，可提升RAG场景下生成回答的可靠性，且在多类语言模型上效果优于基线与专用模型。

</details>

---

### 13. [DAMP: Decay-Aware Mixed-Precision Recurrent-State Quantization](https://arxiv.org/abs/2608.27513v1)

**Authors**: Tao Zhang, Jianchao Tan, Pingwei Sun, Yanqi Yu, Zixu Jiang, Yuchen Xie, Xunliang Cai, Ziqian Zeng  
**Category**: cs.LG  
**Published**: 2026-08-31  
**Score**: 27.5  
**Type**: new  
**ArXiv ID**: 2608.27513v1  

#### Abstract
Softmax attention stores key and value vectors for every preceding token, causing inference memory to grow with sequence length. Recent language models incorporating Gated DeltaNet (GDN) or Kimi Delta Attention (KDA) reduce this cost by replacing the KV cache in most layers with fixed-size recurrent...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

DAMP: Decay-Aware Mixed-Precision Recurrent-State Quantization
1. 论文的主要贡献和创新点
✅ 解决的问题
1. 现有基于Gated DeltaNet (GDN)或Kimi Delta Attention (KDA)的语言模型，虽用固定大小的循环状态替代KV缓存减少推理内存，但循环状态通常以FP32存储，消耗大量GPU内存；且其更新是内存带宽绑定的，会显著增加解码延迟。
2. 现有的均匀量化策略对循环状态的后训练量化效果差：INT8和FP8会降低复杂推理任务的精度，INT4和NVFP4会使精度降至接近零，无法获得良好的精度-存储权衡。

🚀 提出的新方法与思路
**DAMP（Decay-Aware Mixed-Precision Recurrent-State Quantization）**：论文发现两个关键规律：一是循环状态的量化误差能量集中在少量通道，二是状态通道的相对衰减强度在不同提示和任务间保持稳定。基于此，DAMP在离线校准阶段，利用量化误差能量和基于衰减的持久性识别高风险通道；对高风险通道采用更高精度存储，其余通道采用INT8存储，实现混合精度的循环状态量化。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 循环状态存储 | 显著减少循环状态的存储量 |
| 循环状态更新效率 | 提升循环状态更新核的运行速度 |
| 全模型推理速度 | 降低全模型的TPOT |
| 任务精度保持 | 保持接近FP32基线的平均任务精度 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告具体数据集名称 | 评估模型在数学推理、通用推理、代码生成任务上的性能 |

🎯 实验设置与评估指标
任务：评估不同量化策略在基于GDN/KDA的语言模型上的精度与效率表现
| 指标 | 含义（箭头方向） |
| --- | --- |
| 平均任务准确率 | 衡量模型各项任务的表现，越高越好（↑） |
| 循环状态存储占比 | 相对于基线方法的存储减少比例，越低越好（↓） |
| 循环状态更新核加速倍数 | 相对于基线方法的速度提升，越高越好（↑） |
| 全模型TPOT | 衡量全模型推理速度，越低越好（↓） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 基于GDN/KDA的基线语言模型 | 现有模型 | 循环状态以FP32存储，无量化策略 |
| 均匀量化方法（INT8/FP8/INT4/NVFP4） | 量化策略 | 对所有循环状态通道采用统一精度量化，精度-存储权衡差 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告具体数值
2. 效率对比：论文未报告具体FPS/参数量数值
3. 跨域/zero-shot迁移：论文未报告相关实验
4. 鲁棒性/扰动测试：论文未报告相关实验
5. 消融实验：论文未报告相关实验

4. 关键结论和发现
- 主要发现：①均匀量化对循环状态的精度-存储权衡差，INT8/FP8降低复杂推理精度，INT4/NVFP4使精度接近零；状态通道相对衰减强度在提示和任务间稳定，量化误差集中在少量通道。②DAMP通过识别高风险通道混合精度量化，可在保持平均精度接近FP32基线的同时，优化循环状态存储与效率。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：论文提出DAMP方法，即结合量化误差能量与衰减稳定性的混合精度循环状态量化策略，在保持语言模型推理精度接近FP32基线的前提下，实现循环状态存储减少、推理速度提升和全模型TPOT降低。

</details>

---

### 14. [Memory-efficient GPU pipelines for real-time non-line-of-sight reconstruction](https://arxiv.org/abs/2608.28183v1)

**Authors**: Alfonso L\'opez-Ruiz, Diego Royo  
**Category**: cs.DC  
**Published**: 2026-08-31  
**Score**: 26.0  
**Type**: new  
**ArXiv ID**: 2608.28183v1  

#### Abstract
Non-line-of-sight (NLOS) imaging reconstructs scenes hidden around a corner from indirect light recorded by a single-photon avalanche diode (SPAD). A single reconstruction is a large inverse problem: billions of photon timestamps must be binned, moved through memory, transformed and inverted. As SPA...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Memory-efficient GPU pipelines for real-time non-line-of-sight reconstruction
1. 论文的主要贡献和创新点
✅ 解决的问题
非视距（NLOS）成像需从单光子雪崩二极管（SPAD）记录的间接光重建拐角后隐藏场景，其重建是包含数十亿光子时间戳的大型逆问题，需处理分箱、内存移动、变换与逆变换；随着SPAD阵列采集吞吐量提升，重建成为流程瓶颈，现有相关GPU实现存在内存占用高、速度不足的问题。
🚀 提出的新方法与思路
**波基算法的GPU执行优化**：针对f-k migration和phasor-fields两种已有的波基算法，构建适用于流式与离线处理的定制化GPU执行方案。
**phasor-fields传播核优化**：对phasor-fields的ring-and-radius核，采用环的解析傅里叶变换组装离线版本，使传播核在运行时无需以稠密形式存在，降低内存与带宽消耗。
**流水线与算子协同优化**：重组两种算法的执行流水线，融合多种算子（融合核、warp级光子分箱、批量变换、CUDA图重放），仅在减少实际瓶颈的场景中使用FP16存储。
🔍 相比现有方法的优势
维度 | 优势
--- | ---
重建速度 | 相对于参考流式管道与最快已发表GPU基线，取得显著速度提升
内存占用 | 内存占用大幅降低，可在相同硬件上实现更大更精细的重建，或在更低内存预算下实现相当规模的重建

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
论文未报告 | 论文未明确提及所使用的数据集名称及来源
🎯 实验设置与评估指标
任务为实时非视距成像（NLOS）重建，评估指标包括重建速度、内存占用。
指标 | 含义
--- | ---
重建速度 | 衡量算法的实时处理能力，越高越好
内存占用 | 衡量算法的硬件资源需求，越低越好
⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
参考流式管道 | 基准方法 | 原未优化的GPU执行NLOS重建的流式管道
最快已发表GPU基线 | 现有GPU实现 | 已发表的性能最优的GPU端NLOS重建方案
本论文所提方法 | 优化方案 | 融合解析傅里叶变换、算子优化的定制化GPU流水线

3. 主要实验结果和性能指标
论文未明确提供对应表号/图号等来源标识的具体定量数值，仅报告所提方法相对于参考流式管道和最快已发表GPU基线存在显著速度提升，且内存占用大幅降低；同时论文报告了各实现选择的消融分析以验证优化的有效性。

4. 关键结论和发现
- 主要发现：1. 针对NLOS重建的GPU流水线瓶颈，通过定制化优化两种波基算法的GPU执行，可实现重建速度的显著提升和内存占用的大幅降低；2. 利用环的解析傅里叶变换优化phasor-fields的ring-and-radius核是降低内存消耗的关键；3. 低内存占用特性使本方法可适配不同硬件资源，还支持针对下一代NLOS视频处理的三种去噪策略。
- 方法局限性：论文未报告
- 未来工作：基于当前方法获得的帧预算，提出三种去噪策略用于下一代NLOS视频处理。

> ✅ **总结一句话**：该论文聚焦实时NLOS成像的GPU重建瓶颈，通过优化f-k migration和phasor-fields两种波基算法的GPU执行方案，实现了速度与内存占用性能的大幅提升，为高吞吐量下的实时NLOS重建提供了高效的GPU解决方案。

</details>

---

### 15. [SOMTab: Set-Order Mamba for Efficient Tabular In-Context Learning](https://arxiv.org/abs/2608.27882v1)

**Authors**: Hao Wang, Siyu Zhang, Wei Ma  
**Category**: cs.LG  
**Published**: 2026-08-31  
**Score**: 23.5  
**Type**: new  
**ArXiv ID**: 2608.27882v1  

#### Abstract
Tabular foundation models based on in-context learning have recently emerged as strong alternatives to task-specific model fitting. However, the current performance frontier remains dominated by attention-heavy architectures, where attention is used throughout the modeling pipeline. This raises a na...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

SOMTab: Set-Order Mamba for Efficient Tabular In-Context Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
当前基于上下文学习的表格基础模型的性能前沿被全程使用注意力的架构主导，这引出了表格上下文学习的每个阶段是否都需要注意力的核心疑问，现有全程注意力架构可能存在推理效率、GPU内存消耗的潜在瓶颈。

🚀 提出的新方法与思路
**SOMTab**（Set-Order Mamba架构）：将表征构造与查询条件检索分离，行和列表征阶段把无序表格token映射为稳定隐槽，通过基于Mamba的状态空间混合构造紧凑表征；最终预测阶段保留基于注意力的上下文学习，以保留带标签上下文示例的查询条件检索。
**DCH-TailMix**：一种合成先验，结合度校正图异质性与混合重尾机制，用于多样化合成依赖结构。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 性能 | 接近强Transformer-based表格基础模型的性能 |
| 推理效率 | 相比注意力-heavy架构，推理速度更快 |
| GPU内存占用 | 相比注意力-heavy架构，GPU内存占用更低 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 表格基准数据集 | 用于评估模型的表格上下文学习性能 |

🎯 实验设置与评估指标
任务为表格上下文学习，论文未明确报告具体评估指标。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Transformer-based表格基础模型 | 基线方法 | 当前表格上下文学习的性能前沿方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能（L2/碰撞率等）：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：SOMTab通过分离表征构造（基于Mamba）与查询条件检索（基于注意力）的架构设计，可在表格上下文学习任务中实现与强Transformer-based模型相近的性能，同时提升效率、降低GPU内存消耗；DCH-TailMix合成先验能多样化表格的合成依赖结构。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：SOMTab通过Set-Order Mamba架构分离表征构造与查询条件检索，结合DCH-TailMix合成先验，实现了接近强Transformer-based表格基础模型的性能，同时提升了表格上下文学习的推理效率并降低了GPU内存占用，为高效表格上下文学习提供了新方案。

</details>

---

### 16. [INSPIRE: An Internalize-Then-Improve Approach for Example-Driven Mathematical Reasoning](https://arxiv.org/abs/2608.27501v1)

**Authors**: Shuai Wang, Jiayi Kuang, Yinghui Li, Haojing Huang, Xinnian Liang, Ying Shen, Liang Lin  
**Category**: cs.CL  
**Published**: 2026-08-31  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2608.27501v1  

#### Abstract
Mathematical reasoning has seen rapid progress in large language models (LLMs), yet existing methods optimize predominantly for final-answer correctness, raising the question whether models truly internalize mathematical concepts or merely memorize solution patterns. In human mathematics education, ...

---

### 17. [Beyond Flat Netlist: Hierarchical Graph Representation Learning for Scalable Analysis of Sequential Circuits](https://arxiv.org/abs/2608.28188v1)

**Authors**: Jingyi Zhou, Zhengyuan Shi, Jiaying Zhu, Ziyang Zheng, Qiang Xu  
**Category**: cs.LG  
**Published**: 2026-08-31  
**Score**: 22.5  
**Type**: new  
**ArXiv ID**: 2608.28188v1  

#### Abstract
Circuit Representation Learning (CRL) offers a powerful paradigm to guide and optimize core Electronic Design Automation (EDA) tasks, but its practical adoption is hindered by the immense scale of industrial netlists and a failure to explicitly model register-level temporal dynamics. To overcome the...

---

### 18. [SegBench-GC: Testing Segmentation Invariance in Multi-Step Offline Goal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2608.27678v1)

**Authors**: Musa Shams  
**Category**: cs.LG  
**Published**: 2026-08-31  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2608.27678v1  

#### Abstract
Offline goal-conditioned reinforcement learning (GCRL) often uses trajectory structure for future-goal sampling and multi-step targets, yet logged trajectories may be partitioned for administrative reasons that do not correspond to termination. We introduce SegBench-GC, a controlled stress test of s...

---

### 19. [Euclidean Fourier Neural Operators](https://arxiv.org/abs/2608.28425v1)

**Authors**: Nathanael Bosch, Niklas Frederik Schmitz, Michael F. Herbst  
**Category**: cs.LG  
**Published**: 2026-08-31  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2608.28425v1  

#### Abstract
Fourier neural operators (FNOs) provide an efficient framework for learning mappings between function spaces as they are, by construction, independent of the grid resolution at which they are trained and evaluated. However, FNOs are not independent of the periodic domain they are applied to: their d...

---

### 20. [QUORUM: QUality-Optimized Routing Using Multiple annotators](https://arxiv.org/abs/2608.27974v1)

**Authors**: Antonio Purificato, Maria Sofia Bucarelli, Andrea Bacciu, Amin Mantrach, Fabrizio Silvestri  
**Category**: cs.CL  
**Published**: 2026-08-31  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2608.27974v1  

#### Abstract
Data annotation remains a central bottleneck in natural language processing, requiring human effort to obtain high-quality labels at scale. While Large Language Models (LLMs) offer a fast and cost-effective alternative, their reliability is highly instance-dependent: they perform well on simple inpu...

---

### 21. [Twin Worlds: Equivariance-Based Abstention for Evidence-Grounded Reasoning](https://arxiv.org/abs/2608.28018v1)

**Authors**: Vy Nguyen, Ziqi Xu, Jeffrey Chan, Estrid He, Feng Xia, Renqiang Luo, Erik Cambria, Xiuzhen Zhang  
**Category**: cs.CL  
**Published**: 2026-08-31  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2608.28018v1  

#### Abstract
Knowledge-intensive reasoning requires Large Language Models (LLMs) to ground answers in provided evidence. When evidence is insufficient, it is desirable that models abstain rather than confidently generating unsupported answers. Existing abstention methods rely on uncertainty estimation or evidenc...

---

### 22. [A Formal Limitation on Learning Human Language From Textual Corpora](https://arxiv.org/abs/2608.28560v1)

**Authors**: Emily Cheng, Ryan Cotterell  
**Category**: cs.CL  
**Published**: 2026-08-31  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2608.28560v1  

#### Abstract
Can a listener recover what a speaker means from the form of an utterance alone? We answer this question information-theoretically, and for a listener given by any featurizer of text, including the hidden states of contemporary large language models. Modeling language use as a joint distribution ove...

---

### 23. [QGPINNs: A Physics-Informed Neural Network Framework for Nonlocal Differential Equations on Quantum Graphs](https://arxiv.org/abs/2608.28589v1)

**Authors**: Vaibhav Mehandiratta, Saket Ramchandra  
**Category**: cs.LG  
**Published**: 2026-08-31  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2608.28589v1  

#### Abstract
We propose QGPINNs, a physics-informed neural network framework developed in PyTorch for the numerical solution of nonlocal differential equations on quantum graphs. The framework is designed as a general computational implementation in which the solution on each edge of the graph is approximated by...

---

### 24. [Neuromorphic architectures as numerical solvers for computational neuroscience](https://arxiv.org/abs/2608.28387v1)

**Authors**: Jakob Jordan, Ole Richter, Congyang Li, Mihai A. Petrovici, Rajit Manohar  
**Category**: cs.AR  
**Published**: 2026-08-31  
**Score**: 17.0  
**Type**: new  
**ArXiv ID**: 2608.28387v1  

#### Abstract
Neuromorphic computing is closely associated with spiking neuronal networks. However, an alternative class of so-called "rate-based" models arising from computational neuroscience and machine learning forgoes spiking interactions and instead relies on continuous coupling between neurons. Existing ne...

---

### 25. [TerraceMoE: A Cost Model for Hierarchical MoE All-to-All Communication](https://arxiv.org/abs/2608.27874v1)

**Authors**: Weicheng Xue, Bingqiang Wang, Li Yuan, Huihui Zhou, Yonghong Tian  
**Category**: cs.DC  
**Published**: 2026-08-31  
**Score**: 16.0  
**Type**: new  
**ArXiv ID**: 2608.27874v1  

#### Abstract
Hierarchical two-hop dispatch can reduce slow-fabric traffic in expert-parallel Mixture-of-Experts training, but it adds a second collective and an arrival-side operator chain. We present a cost model for screening that trade at the communication-call level, bounded by validation gates that withdraw...

---

### 26. [An Enclosed Mode Is a Gauge Choice: Topology Relative to Reach in Certified Code World Models](https://arxiv.org/abs/2608.28541v1)

**Authors**: Javier Aguilar Mart\'in  
**Category**: cs.LG  
**Published**: 2026-08-31  
**Score**: 14.0  
**Type**: new  
**ArXiv ID**: 2608.28541v1  

#### Abstract
A code world model accepted by a sampling gate can be exactly right on everything the gate can see and arbitrarily wrong beyond it. We characterize what a certified model can know, and what its errors can cost, when the omission is an annular freeze mode enclosing an unreachable interior. The gate q...

---

### 27. [EvoHarmBench: Breaking Content Moderation with Iterative Human-Like Evasion](https://arxiv.org/abs/2608.27844v1)

**Authors**: Ruijie Jian, Benlei Cui, Ting Ma, Haidong Ding, Kangwei Liu, Ziwen Xu, Longtao Huang, Hui Xue, Ziqiang Zhu, Junjie Li, Haiwen Hong  
**Category**: cs.CL  
**Published**: 2026-08-31  
**Score**: 13.0  
**Type**: new  
**ArXiv ID**: 2608.27844v1  

#### Abstract
Existing evaluations of harmful content detection rely predominantly on static benchmarks, which struggle to reflect the interactive adversarial ecosystem of real-world content platforms where users continuously revise their expressions in response to moderation feedback. This mismatch creates a sig...

---

### 28. [Beyond Pairwise Graphs in Science: Hypergraph Adaptive Wavelet Operators for Parametric PDEs](https://arxiv.org/abs/2608.27883v1)

**Authors**: Rajat Sarkar, Venkataramana Runkana, Souvik Chakraborty  
**Category**: cs.LG  
**Published**: 2026-08-31  
**Score**: 13.0  
**Type**: new  
**ArXiv ID**: 2608.27883v1  

#### Abstract
Physical systems are often modeled by solution operators that map input fields, parameters, geometries, or past states to steady or future physical states. Learning these maps is difficult, especially for time-dependent systems that must assimilate history and remain stable under autoregressive roll...

---

### 29. [A Shaky Voice Is Not Always a Dodge: Benchmarking Textual and Vocal Evasion Detection in Earnings Calls](https://arxiv.org/abs/2608.28040v1)

**Authors**: Mirae Kim, Seonghun Jeong, Youngjun Kwak  
**Category**: cs.CL  
**Published**: 2026-08-31  
**Score**: 12.0  
**Type**: new  
**ArXiv ID**: 2608.28040v1  

#### Abstract
Existing approaches to evasion detection in earnings calls focus on textual transcripts, treating evasion as a single-dimensional phenomenon. We argue that evasion in spoken communication is inherently multidimensional: beyond what executives say, how they say it carries independent and complementar...

---

### 30. [Temporal Memory-Aware Online Test-Time Adaptation on Dynamic Graphs](https://arxiv.org/abs/2608.27948v1)

**Authors**: Bo Li, Xin Zheng, Ming Jin, Can Wang, Shirui Pan  
**Category**: cs.LG  
**Published**: 2026-08-31  
**Score**: 12.0  
**Type**: new  
**ArXiv ID**: 2608.27948v1  

#### Abstract
Test-time adaptation (TTA) on graphs aims to adapt a graph neural network (GNN) that is well-trained on the training graph to the test graph, which involves potential distribution shifts that may harm model generalization and test-time inference. While recent efforts have investigated TTA on static ...

---

## 🔧 Configuration

This bot is configured to look for papers containing the following keywords:
- LLM, Inference, Training, kv cache, Speculative decoding, Prefill, Decode, FlashAttention, PagedAttention, continuous batching, MOE, mixture of experts, Quantization, FP8, FP4, Parallel, Distributed, Pipeline, Sparse, Sparse Attention, State Space, SSM, Throughput, Scalable, Efficient, vLLM, SGLang, DeepSpeed, FSDP, AI compiler, TVM, Triton, MLIR, torch.compile, kernel fusion, polyhedral, RISC-V, RVV, XiangShan, custom instruction, eBPF, RDMA, disaggregated, chiplet, NoC, CXL, HBM, systolic array, Kernel, Cluster, Communication, Offload, Hardware, Accelerator, Compiler, Optimization, Embodied, Embodied AI, Embodied Intelligence, Robotics, Robot, Manipulation, Navigation, Sim-to-real, Simulation, World Model, World Models, Video Generation, Video Prediction, Multimodal, Multi-modal, Vision-Language, Vision Language, VLM, Image-Text, Cross-modal, Cross modal, Text-to-Image, Text-to-Video, Vision Transformer, Visual Understanding

## 📅 Schedule

The bot runs on weekdays at 05:40 UTC via GitHub Actions to fetch the latest papers.

## 🚀 How to Use

1. **Fork this repository** to your GitHub account
2. **Customize the configuration** by editing `config.json`:
   - Add/remove arXiv categories (e.g., `cs.AI`, `cs.LG`, `cs.CL`)
   - Modify keywords to match your research interests
   - Adjust `max_papers` and `days_back` settings
3. **Enable GitHub Actions** in your repository settings
4. **The bot will automatically run on weekdays** and update the README.md

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
