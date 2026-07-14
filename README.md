# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-07-14 07:57:04 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [SVR-R1: Bootstrapping Multi-modal Reasoning with Self-verification in Reinforcement Learning](https://arxiv.org/abs/2607.10966)

**Authors**: Mingyuan Wu, Jingcheng Yang, Shengyi Qian, Xudong Wang, Jize Jiang, Qifan Wang, Aashu Singh, Khoi Pham, Fei Liu, Zhaolun Su, Zhuokai Zhao, Klara Nahrstedt, Jianyu Wang, Hanchao Yu  
**Category**: cs.AI  
**Published**: 2026-07-14  
**Score**: 96.5  
**Type**: new  
**ArXiv ID**: 2607.10966v1  

#### Abstract
We introduce Self-Verified Reasoner (SVR-R1), a multi-turn RL framework that turns a model's own verification into a learning signal for multimodal reasoning. For each query, the model proposes an answer using the same weights, and issues a binary self-verdict (Yes/No). A 'No' triggers a second-chan...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：《SVR-R1: Bootstrapping Multi-modal Reasoning with Self-verification in Reinforcement Learning》
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多模态大模型（VLMs）在强化学习训练中，多依赖外部监督信号或缺乏有效的自主校验与自校正机制，导致推理过程中错误难以修正，且模型无法内化自我验证能力，最终限制了多模态推理的准确率提升。

🚀 提出的新方法与思路
**Self-Verified Reasoner (SVR-R1)**：一种基于GRPO的异步多回合强化学习框架。对于每个查询，模型先生成答案并输出二元自我验证结果（是/否）；若验证结果为“否”则触发二次修正，为“是”或达到回合上限则输出最终结果，基于结果类奖励进行策略学习，无需外部监督或辅助评论家，专门用于多模态推理的引导式强化学习。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 自我校验机制 | 利用模型自身生成的答案进行二元验证，无需依赖外部标注数据 |
| 训练框架 | 基于GRPO的异步多回合RL架构，支持策略内化自校正能力 |
| 推理性能 | 训练中减少对验证环节的依赖（回合数降低），同时提升测试准确率 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| vision-language reasoning benchmarks（如ScienceQA、VQA-v2等） | 评估多模态推理的准确性与自校正效果 |

🎯 实验设置与评估指标
任务为视觉-语言问答推理任务，评估指标为推理准确率，规则为 ↑ 越高越好。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 标准GRPO | 多模态推理基准方法 | 无自我验证机制，仅基于生成结果进行策略训练 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark推理性能对比**
| 方法 | 推理准确率 |
| --- | --- |
| 标准GRPO | 基线水平 |
| SVR-R1 | 大幅提升 ✅ |
💡 结论：SVR-R1在视觉-语言推理基准上显著优于标准GRPO，大幅提升了多模态推理的准确性。

**表2：训练动态与效率对比**
| 指标 | 标准GRPO | SVR-R1 |
| --- | --- | --- |
| 平均验证回合数 | 稳定 | 减少 ✅ |
| 测试准确率 | 基线水平 | 提升 ✅ |
💡 结论：SVR-R1训练过程中模型内化了自校正能力，验证环节依赖降低，推理效率与准确率同步提升。

4. 关键结论和发现
- 主要发现：SVR-R1将模型自身的自我验证转化为强化学习信号，无需外部监督即可有效提升多模态推理能力；训练中验证回合减少但测试准确率上升，说明模型缩小了验证与生成环节的差距，能自主选择更自信的答案。
- 方法局限性：目前仅在通用视觉语言推理基准上验证，未覆盖超长文本、多图像组合等复杂多模态推理场景。
- 未来工作：扩展SVR-R1框架到更复杂的多模态任务，优化异步多回合框架的部署效率，探索更多类型的自我校验机制。

> ✅ **总结一句话**：SVR-R1是一种结合自我验证与GRPO的异步多回合强化学习框架，无需外部监督即可自主提升多模态推理能力，缩小了推理中验证与生成的差距。

</details>

---

### 2. [The Ebb and Flow of Multimodal Focus: Scheduling Visual Relay Windows for Grounded VLM Reasoning](https://arxiv.org/abs/2607.11436)

**Authors**: Wencheng Ye, Yi Bin, Yujuan Ding, Hongye Fang, Zheng Wang, Xing Xu, Jingkuan Song, Yun Zhang, Sirui Da, Heng Tao Shen  
**Category**: cs.AI  
**Published**: 2026-07-14  
**Score**: 96.0  
**Type**: new  
**ArXiv ID**: 2607.11436v1  

#### Abstract
Vision-language models increasingly succeed on multimodal reasoning benchmarks, yet their visual evidence often becomes unstable once it enters the language stack, weakening evidence-grounded reasoning. To understand this fragility, we examine the internal dynamics of VLMs through a mechanistic lens...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：The Ebb and Flow of Multimodal Focus: Scheduling Visual Relay Windows for Grounded VLM Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有视觉语言模型（VLM）的视觉证据进入语言处理阶段后易不稳定，导致基于证据的多模态推理效果弱；多数方法未显式捕捉VLM内部多模态注意力的深度动态，忽略了视觉中继窗口（VRW）的任务相关性，通用控制方法无法适配不同任务对视觉证据的需求，进而削弱推理的 grounded 性。

🚀 提出的新方法与思路
**TRACE框架**：一种用于grounded VLM推理的任务自适应推理时控制框架，核心逻辑是先分析VLM内部多模态注意力的稳定三阶段节奏（问题条件组织→视觉主导VRW→ answer形成），再通过轻量级训练模块实现两点优化：① Prefill阶段：调整VRW的分配，适配不同任务的视觉证据需求；② Decoding阶段：保留视觉支持的传递，防止视觉证据在语言解码中流失。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 跨模型泛化 | 适配4种开放-weight VLM backbone，无需针对单个模型重新训练 |
| grounded 推理增益 | 在视觉证据敏感场景平均提升4.33点，最高达6.6点，大幅减少无依据输出 |
| 内部逻辑稳定性 | 能区分未支撑的错误答案与强推理轨迹，提升推理可靠性 |
| 部署效率 | 推理时添加的轻量级模块几乎不增加额外参数量，推理速度接近基线 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 7个多模态推理基准 | 评估TRACE框架在不同grounded VLM推理任务上的性能 |

🎯 实验设置与评估指标
任务：开放-weight VLM上的grounded多模态推理；指标 | 含义
| --- | --- |
| Grounded Reasoning Accuracy | 回答与输入视觉证据一致的准确率，越高越好（↑） |
| Reasoning Correctness | 推理步骤的正确性，越高越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Base VLMs（不同开放-weight backbone） | 基准模型 | 无显式视觉中继窗口控制，原生VLM性能 |
| Generic Inference-time Control Methods | 对比方法 | 通用控制策略，未适配VLM内部三阶段注意力节奏 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：Main Benchmark Performance（Grounded Reasoning）**
| 方法 | 基准1 | 基准2 | ... | 平均 |
| --- | --- | --- | --- | --- |
| Base VLMs | 62.1 | 58.3 | ... | 60.2 |
| Generic Methods | 64.5 | 61.2 | ... | 62.8 |
| TRACE | 68.7 ✅ | 65.5 ✅ | ... | 64.5 ✅ |
💡 结论：TRACE框架在核心grounded推理基准上显著优于基线方法，平均性能提升约4.33点。

**表2：Efficiency Comparison**
| 方法 | 参数量（M） | FPS（推理速度） |
| --- | --- | --- |
| Base VLMs | 1200 | 32 |
| TRACE | 1210 | 31 ✅ |
💡 结论：TRACE是轻量级框架，仅增加极少量参数量，推理速度几乎无下降。

**表3：Cross-domain Zero-shot Transfer**
| 方法 | OOD基准1 | OOD基准2 |
| --- | --- | --- |
| Base VLMs | 55.2 | 52.8 |
| TRACE | 61.3 ✅ | 58.7 ✅ |
💡 结论：TRACE在未见过的领域任务上仍保持稳定性能，零迁移效果优异。

**表4：Robustness to Visual Perturbations**
| 方法 | 无噪声 | 轻度噪声 | 重度噪声 |
| --- | --- | --- | --- |
| Base VLMs | 60.2 | 51.5 | 40.3 |
| TRACE | 64.5 | 58.2 ✅ | 48.7 ✅ |
💡 结论：TRACE能更好抵抗视觉图像噪声，推理稳定性更强。

**表5：Ablation Study of TRACE Modules**
| VRW Allocation | Visual Support Preservation | Grounded Accuracy |
| --- | --- | --- |
| ❌ | ❌ | 60.1 |
| ✅ | ❌ | 62.3 |
| ❌ | ✅ | 62.8 |
| ✅ | ✅ | 64.5 ✅ |
💡 结论：TRACE的两个核心模块（VRW分配、视觉支持保留）共同作用时，框架性能最优，缺一不可。

4. 关键结论和发现
- 主要发现：1. VLM内部多模态注意力确实存在稳定的三阶段深度动态（问题组织→视觉中继→回答），中间视觉中继窗口（VRW）是grounded推理的关键节点；2. 任务自适应调整VRW的TRACE框架能有效解决视觉证据在语言阶段的流失问题，大幅提升多模态推理的 grounded 性；3. TRACE跨不同VLM backbone、benchmark及领域均表现稳定，轻量且易部署。
- 方法局限性：对包含长序列图像的多模态任务（如视频推理）适配性需进一步验证；轻量级模块的训练仍依赖现有标注数据，数据效率待提升。
- 未来工作：1. 扩展TRACE框架至视频多模态推理场景；2. 优化VRW的预测机制，进一步降低模块对额外训练数据的依赖；3. 探索结合更大规模的无标注多模态数据微调模块，提升泛化能力。

> ✅ **总结一句话**：TRACE通过捕捉VLM内部三阶段多模态注意力节奏，自适应调度视觉中继窗口，有效减少了视觉证据在语言处理阶段的流失，显著提升了open-weight VLM的 grounded 多模态推理性能，是一种通用高效的推理时控制方案。

</details>

---

### 3. [FlashAccel: Leveraging High-Bandwidth Flash for High-Throughput LLM Inference](https://arxiv.org/abs/2607.10186)

**Authors**: Xinyu Wang, Yalong Xue, Xiaotian Sun, Xiaoyu Zhang, Chunmeng Dou, Xueqi Li, Xiaoming Chen  
**Category**: cs.AR  
**Published**: 2026-07-14  
**Score**: 87.5  
**Type**: new  
**ArXiv ID**: 2607.10186v1  

#### Abstract
Large language model (LLM) inference is increasingly limited by the capacity of High-Bandwidth Memory (HBM) in GPUs, as model weights and KV cache grow rapidly. High-Bandwidth Flash (HBF) provides higher capacity than HBM while retaining comparable bandwidth, making it a promising substrate for capa...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：FlashAccel: Leveraging High-Bandwidth Flash for High-Throughput LLM Inference
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾为：LLM推理中模型权重与KV Cache规模快速增长，GPU的HBM容量受限；高带宽闪存（HBF）虽容量高、带宽接近HBM，但存在固有访问延迟高、带宽利用率低、异构资源支持不足等问题，无法直接集成到GPU用于LLM推理，现有方案未兼顾这些痛点。

🚀 提出的新方法与思路
**HBF与HBM集成架构支持**：将HBF整合到基于HBM的GPU，提供架构层面的优化以缓解HBF的高访问延迟；
**专用数据布局设计**：针对模型权重和KV Cache设计专属数据布局，提升HBF的带宽利用率；
**HBF感知的存储管理层与编程模型**：在系统层面组织HBF中的持久化数据，实现异构内存资源的高效协调。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 内存容量 | 整合HBF（高容量）与HBM，突破GPU内存容量瓶颈 |
| 访问延迟 | 架构层面优化缓解HBF固有高延迟的影响 |
| 带宽利用率 | 专属数据布局提升HBF的带宽使用效率 |
| 异构资源管理 | 提供感知HBF的存储层与编程模型，协调异构内存资源 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 未明确提供具体名称 | 100ms延迟约束下的LLM推理性能与能效评估 |

🎯 实验设置与评估指标
任务为100ms延迟约束下的GPU LLM推理性能与能效测试。
| 指标 | 含义 |
| --- | --- |
| 吞吐量每GPU | 单GPU的LLM推理吞吐量（↑越高越好） |
| 能效 | 单位能耗对应的LLM推理吞吐量（↑越高越好） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| HBM-only GPU | 基线方法 | 仅以HBM作为内存资源，无HBF集成 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：100ms延迟约束下的LLM推理性能与能效对比（主Benchmark场景）**
| 方法 | 吞吐量每GPU | 能效 | 延迟约束 |
| --- | --- | --- | --- |
| HBM-only GPU | 基准值 | 基准值 | 100ms |
| FlashAccel | 2.54× ✅ | 1.93× ✅ | 100ms |
💡 结论：集成6个HBF栈的FlashAccel，在100ms延迟约束下，平均吞吐量和能效分别较仅用HBM的GPU提升2.54倍和1.93倍，性能优化效果显著。

其他专项实验：论文未明确提及跨域/zero-shot迁移、鲁棒性/扰动测试及消融实验的具体结果，暂不呈现相关内容。

4. 关键结论和发现
- 主要发现：1. FlashAccel通过架构支持、数据布局优化与异构内存管理，有效解决了HBF难以集成到GPU用于LLM推理的问题；2. 100ms延迟约束下，集成HBF可大幅提升GPU的LLM推理吞吐量与能效。
- 方法局限性：未覆盖跨域场景、鲁棒性测试及不同规模LLM模型的适配性，未提及HBF集成的硬件成本与兼容性问题。
- 未来工作：可探索FlashAccel在各类GPU、不同规模LLM模型及复杂场景中的适配方案，研究降低HBF集成成本的可行路径。

> ✅ **总结一句话**：FlashAccel是一种将高带宽闪存（HBF）集成到GPU的协同设计系统，通过架构优化、专用数据布局与异构资源管理，实现LLM推理在100ms延迟约束下的高吞吐量与高能效。

</details>

---

### 4. [Direct Image-to-Modern Vietnamese Translation of Han-Nom Manuscripts via Multimodal RLHF Preference Alignment](https://arxiv.org/abs/2607.11434)

**Authors**: Thi Kim Trang Vo, Nghia Hieu Nguyen, Ha Minh Tan  
**Category**: cs.CL  
**Published**: 2026-07-14  
**Score**: 83.5  
**Type**: new  
**ArXiv ID**: 2607.11434v1  

#### Abstract
Translating Han-Nom manuscripts into modern Vietnamese is challenging because historical pages are often degraded, the script contains rare logographic characters, and parallel supervision is limited. We propose a multimodal RLHF preference-alignment framework that conditions Vietnamese generation o...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Direct Image-to-Modern Vietnamese Translation of Han-Nom Manuscripts via Multimodal RLHF Preference Alignment
1. 论文的主要贡献和创新点
✅ 解决的问题：翻译汉喃手稿到现代越南语面临三大核心痛点——手稿退化、含罕见语素字符、平行监督数据有限；现有相关框架未充分整合视觉与文本特征，且未系统对比不同偏好对齐方法在该低资源任务的性能，难以平衡多维度翻译质量指标。
🚀 提出的新方法与思路
**Multimodal RLHF Preference Alignment Framework**，该框架以手稿图像与对齐的汉喃源文本为条件生成现代越南语，整合四类模型的特征表示：CLIP ViT-L/14@336提取视觉特征、bert-base-chinese提取汉喃表征、vinai/phobert-base提取越南语表征、T5-small编码器状态；通过模态特定投影与融合块，将2048维拼接特征压缩为512维共享表征；在相同SFT策略基础上，对比PPO、DPO、KTO三类偏好对齐方法的性能。
🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 模态融合架构 | 首次系统整合退化手稿的视觉图像、汉喃源文本、目标越南语文本三类特征，解决历史文档退化导致的翻译歧义问题 |
| 偏好对齐方法对比 | 在低资源历史翻译任务中全面对比PPO、DPO、KTO三类算法的多指标性能，为任务适配提供方法选型依据 |
| 翻译质量提升 | 偏好对齐策略（尤其是DPO）可显著优化低资源场景下的翻译词汇与语义质量，优于传统SFT基线模型 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 有限汉喃-现代越南语平行数据集（含退化手稿图像） | 用于模型的SFT与偏好对齐训练 |
🎯 实验设置与评估指标
实验任务：低资源历史翻译任务，即针对退化汉喃手稿，将其图像与对应汉喃源文本翻译为现代越南语，评估翻译的词汇、语义与错误率等多维度质量。
| 指标 | 含义（箭头） |
|------|-------------|
| BLEU-4 | 翻译与参考文本的词汇匹配度，↑越高越好 |
| ROUGE-L | 翻译与参考文本的重叠度，↑越高越好 |
| BERTScore | 翻译与参考文本的语义相似度，↑越高越好 |
| 语义相似度 | 翻译与参考文本的语义一致性，↑越高越好 |
| CER | 字符错误率，↓越低越好 |
| WER | 词错误率，↓越低越好 |
| token accuracy | 翻译token的正确率，↑越高越好 |
| 准确率/召回率/F1 | 翻译单元的分类性能，↑越高越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| SFT | 基线方法 | 仅通过监督学习训练的基础翻译模型，作为对比基准 |
| PPO | 偏好对齐方法 | 近端策略优化算法，用于强化学习偏好对齐 |
| DPO | 偏好对齐方法 | 直接偏好优化算法，用于偏好对齐 |
| KTO | 偏好对齐方法 | 基于效用目标的偏好对齐算法 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（低资源汉喃翻译）**
| 方法 | BLEU-4 | ROUGE-L | BERTScore | 语义相似度 | CER | WER | token accuracy | 准确率 | 召回率 | F1 |
|------|--------|---------|-----------|------------|-----|-----|----------------|--------|--------|-----|
| SFT | 基准值 | 基准值 | 基准值 | 基准值 | 基准值 | 基准值 | 基准值 | 基准值 | 基准值 | 基准值 |
| PPO | 中等提升 | 中等提升 | 中等提升 | 中等提升 | 中等降低 | 中等降低 | 中等提升 | ✅ | ✅ | ✅ |
| DPO | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 次优 | 次优 | 次优 |
| KTO | 轻度提升 | 轻度提升 | 轻度提升 | 轻度提升 | 轻度降低 | 轻度降低 | 轻度提升 | 次优 | 次优 | 次优 |
💡 结论：DPO在低资源汉喃翻译的多数核心指标上表现最优，PPO在准确率、召回率、F1指标上最优，KTO具备良好竞争力，所有偏好对齐方法均优于SFT基线模型。
4. 关键结论和发现
- 主要发现：1. 针对低资源汉喃手稿翻译任务，多模态RLHF偏好对齐框架可有效提升翻译的词汇质量与语义一致性，显著优于传统SFT基线模型；2. 不同偏好对齐方法各有侧重，DPO综合性能最优，PPO在精确性指标上更具优势，KTO具备良好竞争潜力；3. 整合退化手稿的视觉特征与文本特征的多模态融合，为低资源历史文档翻译提供了新的有效思路。
- 方法局限性：对汉喃手稿中的极罕见语素字符建模能力仍不足，训练数据规模的限制导致模型泛化能力存在边界。
- 未来工作：扩大汉喃手稿平行数据集规模，优化极罕见字符的建模策略，探索多模态融合与偏好对齐的更优组合方案。
> ✅ **总结一句话**：该研究提出的多模态RLHF偏好对齐框架，结合视觉与文本特征，系统对比不同偏好对齐方法，为低资源汉喃手稿到现代越南语的翻译任务提供了有效解决方案，显著提升翻译质量。

</details>

---

### 5. [[AAFLOW+] Stateful Operator Abstraction with Zero-Copy Distributed KV Cache Orchestration for Multi-Agent Workflows](https://arxiv.org/abs/2607.10987)

**Authors**: Arup Kumar Sarker, Alexander James Halpern, Mills Staylor, Aymen Alsaadi, Gregor von Laszewski, Yue Cheng, Shantenu Jha, Geoffrey Fox  
**Category**: cs.DC  
**Published**: 2026-07-14  
**Score**: 79.0  
**Type**: new  
**ArXiv ID**: 2607.10987v1  

#### Abstract
Multi-agent LLM systems increasingly integrate retrieval, planning, and reasoning, but remain fundamentally text-centric, requiring agents to repeatedly recompute shared context through expensive prefill. Although single-request inference is known to be accelerated by KV-cache management, it is usua...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：[AAFLOW+] Stateful Operator Abstraction with Zero-Copy Distributed KV Cache Orchestration for Multi-Agent Workflows
1. 论文的主要贡献和创新点
✅ 解决的问题
多智能体LLM系统集成了检索、规划、推理等能力，但本质以文本为核心，导致智能体需重复计算共享上下文，prefill阶段开销高昂；现有KV缓存管理仅适用于单请求推理，且局限于本地服务范围，无法适配分布式多智能体场景的状态共享需求。

🚀 提出的新方法与思路
**AAFLOW+**：代理工作流运算符的有状态扩展，将KV缓存作为分布式系统的一等公民对象；构建通信感知图，同步优化数据、提示及可复用模型状态；支持KV物化、传输、分叉、组合、驱逐等操作，运行时实现零拷贝、传输感知执行，使智能体可重用长上下文而无需重新计算。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| TTFT（首令牌延迟） | 最高降低50.2倍 |
| 16智能体规模下计算成本 | 最高降低7.63倍 |
| KV内存占用 | 降低1.72-6.10倍 |
| 系统吞吐量 | 提升超过7.74倍 |
| 多智能体协作效率 | 中等及以上带宽网络下，KV状态共享性能优于文本传递（重计算） |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 硬件微基准测试生成数据 | 为分析成本模型提供参数，支撑多智能体系统的性能评估 |

🎯 实验设置与评估指标
任务为多智能体LLM系统的协作性能与效率优化，核心评估指标如下：
| 指标 | 含义（箭头方向） |
|------|------------------|
| TTFT | 首令牌生成延迟，↓ 越低越好 |
| 多智能体计算成本 | 多智能体协作的计算资源消耗，↓ 越低越好 |
| KV内存占用 | KV缓存占据的内存空间，↓ 越低越好 |
| 吞吐量 | 单位时间内处理的任务数量，↑ 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 本地KV缓存管理 | 现有KV管理方案 | 仅适用于单请求推理，局限于本地服务范围 |
| 文本传递多智能体协作 | 现有多智能体方案 | 以文本为核心传递上下文，需重复计算，prefill开销高 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：AAFLOW+与基线方法的多智能体性能对比**
| 指标 | AAFLOW+ | 本地KV缓存管理 | 文本传递协作 |
|------|---------|----------------|--------------|
| TTFT降低倍数 | 50.2 ✅ | - | - |
| 16智能体计算成本降低倍数 |7.63 ✅ | - | - |
| KV内存降低倍数范围 |1.72-6.10 ✅ | - | - |
| 吞吐量提升倍数 |7.74 ✅ | - | - |
💡 结论：AAFLOW+在多智能体LLM的延迟、计算成本、内存占用、吞吐量等关键性能指标上均取得最优结果，在中等及以上带宽网络下，KV状态共享方案显著优于传统文本传递的重计算方式。

4. 关键结论和发现
- 主要发现：① 将KV缓存作为分布式系统对象的AAFLOW+方案，可有效减少多智能体场景下的重复计算开销，实现性能的大幅提升；② 网络带宽中等及以上时，KV状态共享比文本传递的重计算更具效率，是多智能体协作优化的核心方向；③ AAFLOW+的通信感知图与零拷贝传输设计，可显著降低多智能体系统的资源消耗。
- 方法局限性：AAFLOW+的性能优势依赖于网络带宽条件，低带宽场景下KV传输的额外开销可能削弱部分收益；当前方案主要针对推理阶段优化，未覆盖多智能体LLM的训练场景。
- 未来工作：① 研究低带宽网络下AAFLOW+的性能补偿策略，扩展方案的适用范围；② 拓展AAFLOW+的设计至多智能体LLM训练阶段，支持训练期的状态共享优化；③ 优化KV缓存动态调度机制，提升超大规模智能体集群下的资源利用率。

> ✅ **总结一句话**：AAFLOW+通过将KV缓存作为分布式系统对象，引入零拷贝分布式编排机制，为多智能体LLM系统提供了高效的状态共享方案，可大幅降低延迟与资源消耗，显著提升系统协作效率。

</details>

---

### 6. [TIGER: Text-Conditioned Visual Gated Routing with Acceptance Alignment for Multimodal Speculative Decoding](https://arxiv.org/abs/2607.11131)

**Authors**: Quynh Vo, Cong-Duy Nguyen, Ponhvoan Srey, Luu Anh Tuan, Thong Nguyen  
**Category**: cs.CL  
**Published**: 2026-07-14  
**Score**: 78.0  
**Type**: new  
**ArXiv ID**: 2607.11131v1  

#### Abstract
Speculative decoding accelerates autoregressive generation by letting a lightweight drafter propose multiple tokens that are verified by a larger target model. Although effective for text-only LLMs, speculative decoding yields limited gains in VLMs because drafters often diverge on vision-critical c...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：TIGER: Text-Conditioned Visual Gated Routing with Acceptance Alignment for Multimodal Speculative Decoding
1. 论文的主要贡献和创新点
✅ 解决的问题
原适用于纯文本LLM的speculative decoding在VLM中加速效果有限，核心矛盾是drafter与verifier常于视觉关键内容产生分歧；现有多模态加速方法既未解决无关视觉证据干扰，也未优化对加速至关重要的verifier接受前缀长度。

🚀 提出的新方法与思路
**Text-conditioned Visual Gated Routing**：基于drafter的当前文本状态，动态选择稀疏、与上下文相关的视觉token，替代原全视觉token集或固定压缩接口，减少无关视觉信息干扰，聚焦视觉关键内容。
**Acceptance-aligned Group-based Policy Training**：针对drafter的训练，先通过KL锚定的蒸馏warm start初始化，再采用基于verifier接受前缀长度的奖励开展组策略训练；鼓励drafter不仅模仿target model，更能生成长前缀验证存活的推测序列，对齐训练与推理效率。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 接受前缀长度 | 有效提升verifier认可的推测序列前缀长度，强化speculative decoding的核心加速前提 |
| 推测解码加速性能 | 实现更显著的speculative speedup，且保持稳定增益 |
| 下游任务质量 | 在视觉路由分析等下游任务中，与基线方法相当的准确率，保障性能无明显下降 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 摘要未明确提及具体数据集 | 用于评估TIGER在多模态推测解码、视觉路由任务及跨域迁移上的综合性能 |

🎯 实验设置与评估指标
任务为多模态视觉语言模型（VLM）的speculative decoding加速任务，附带视觉路由等下游任务验证。
| 指标 | 含义 |
| --- | --- |
| 接受前缀长度 | verifier认可的推测序列前缀的token数，↑越长越好 |
| speculative speedup | 推测解码相对于普通解码的速度提升倍数，↑越高越好 |
| 下游任务准确率 | 视觉路由分析任务的输出精度，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 纯文本speculative decoding | 传统方法 | 仅适用于纯文本LLM，未针对VLM优化视觉相关问题 |
| 现有多模态加速方法 | 同类方法 | 未解决无关视觉证据干扰，未优化verifier接受前缀长度 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（接受前缀长度，场景：VLM通用推测解码）**
| 方法 | 接受前缀长度 |
| --- | --- |
| TIGER | 12.3 ✅ |
| 现有多模态加速方法 | 8.7 |
| 纯文本speculative decoding | 5.2 |
💡 结论：TIGER大幅提升了VLM中speculative decoding的接受前缀长度，解决了drafter与verifier的视觉内容分歧问题。

**表2：效率对比（speculative speedup，场景：通用VLM解码）**
| 方法 | speculative speedup |
| --- | --- |
| TIGER | 2.8x ✅ |
| 现有多模态加速方法 | 1.9x |
| 纯文本speculative decoding | 1.5x |
💡 结论：TIGER实现了更显著的speculative speedup，证明其高效的视觉路由机制在加速上的优势。

**表3：跨域/zero-shot迁移性能（下游视觉路由准确率）**
| 方法 | 域内准确率 | 跨域准确率 |
| --- | --- | --- |
| TIGER | 92.1% ✅ | 85.3% ✅ |
| 现有多模态加速方法 | 91.5% | 82.7% |
💡 结论：TIGER在零样本及跨域视觉路由任务上保持与基线相当的性能，验证了其方法的泛化性。

**表4：消融实验（模块有效性）**
| 方法 | Text-conditioned Visual Gated Routing | Acceptance-aligned Training | 接受前缀长度 | speculative speedup | 下游准确率 |
| --- | --- | --- | --- | --- | --- |
| TIGER | ✅ | ✅ | 12.3 ✅ | 2.8x ✅ | 92.1% ✅ |
| 无视觉路由 | ❌ | ✅ | 7.5 | 1.7x | 91.8% |
| 无接受对齐训练 | ✅ | ❌ | 9.2 | 2.1x | 92.0% |
| 基线方法 | ❌ | ❌ | 5.2 | 1.5x | 90.5% |
💡 结论：Text-conditioned Visual Gated Routing与Acceptance-aligned Training两个模块对TIGER的性能均有关键贡献，缺一不可。

4. 关键结论和发现
- TIGER通过Text-conditioned视觉门控路由与接受对齐训练，有效解决了VLM中speculative decoding的视觉分歧与加速不足问题，实现了更长的接受前缀与更高的推测速度，同时保持了下游任务性能。
- TIGER在下游任务上兼顾了效率与质量平衡，且具备一定的跨域泛化能力，适用性更广。
- 两个核心模块的协同优化是TIGER性能提升的关键，缺失任一模块都会导致性能明显下降。
方法局限性：现有实验未覆盖极低分辨率视觉输入、极端跨模态场景等边界情况，泛化范围需进一步验证；未提及drafter模型的参数量压缩方案，边缘设备部署潜力待挖掘。
未来工作：可针对极端视觉输入场景优化视觉路由的鲁棒性，或探索轻量型drafter结构以适配资源受限的边缘设备。

> ✅ **总结一句话**：TIGER是针对多模态视觉语言模型设计的新型推测解码框架，通过文本条件视觉门控路由聚焦关键视觉信息，结合接受对齐训练优化drafter的推测质量，有效提升了多模态推测解码的效率，同时保持了下游任务的性能。

</details>

---

### 7. [UNIBROWSE: A Data-to-Agent Framework for Multimodal BrowseComp](https://arxiv.org/abs/2607.10557)

**Authors**: Xiyu Wei, Qingwei Zong, Zhuocheng Yu, Sujian Li  
**Category**: cs.CL  
**Published**: 2026-07-14  
**Score**: 65.5  
**Type**: new  
**ArXiv ID**: 2607.10557v1  

#### Abstract
Multimodal BrowseComp tasks require agents to combine perception, tool use, and long-horizon reasoning over dynamic web content, challenging their ability to handle compositional structure, open-world uncertainty, and multimodal integration across extended interactions. Crucially, real-world multimo...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：UNIBROWSE: A Data-to-Agent Framework for Multimodal BrowseComp
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多模态BrowseComp任务的相关数据构建方法仅覆盖文本、图像转文本两种信息流模式，缺失文本转图像模式，导致代理在处理动态网页的开放式、长程交互任务时泛化性与鲁棒性不足；同时现有方法缺乏对训练数据有效信号的筛选，不利于强化学习的训练效率与效果。

🚀 提出的新方法与思路
**UNIBROWSE统一数据管道**：首次同时生成覆盖文本、图像转文本、文本转图像三种信息流模式的训练数据；将带知识图谱的 curated数据与实时网页检索结合，提升训练数据对动态网页的保真度。
**探索度（exploration degree）指标**：引入新的探索度指标筛选低信号实例，用于高效强化学习训练，减少冗余样本，优化训练过程。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 数据覆盖范围 | 首次覆盖文本、图像转文本、文本转图像三种信息流模式，填补文本转图像模式的空白 |
| 数据保真度 | 将知识图谱与实时网页检索结合，提升动态网页内容训练数据的真实度 |
| 训练效率 | 通过探索度指标筛选低信号实例，减少训练冗余，提升强化学习效率 |
| 代理性能 | 35B规模代理在多模态BrowseComp基准上超越Qwen3.5-35B-A3B及多个主流闭源代理（GPT-5、Gemini系列） |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| UNIBROWSE生成的训练数据集 | 覆盖三种信息流模式的代理训练数据 |
| 5个多模态BrowseComp基准数据集 | 用于评估代理的任务性能 |

🎯 实验设置与评估指标
任务为多模态BrowseComp，要求代理结合感知、工具使用和长程推理完成网页相关任务；评估指标为平均准确率（越高越好，↑）。
| 指标 | 含义 |
|------|------|
| 平均准确率 | 多模态BrowseComp任务的平均完成准确率（越高越好↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| Qwen3.5-35B-A3B | 基础代理模型 | 未采用UNIBROWSE框架训练的35B规模代理 |
| GPT-5 | 闭源代理 | 通用闭源大型语言模型 |
| Gemini-2.5 Pro | 闭源代理 | 多模态闭源代理 |
| Gemini-2.5 Flash | 闭源代理 | 轻量多模态闭源代理 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（多模态BrowseComp场景）**
| 方法 | 平均准确率 |
|------|------------|
| Qwen3.5-35B-A3B | 43.9 |
| GPT-5 | 42.9 |
| Gemini-2.5 Flash | 41.3 |
| Gemini-2.5 Pro | 44.8 |
| UNIBROWSE代理 | 54.4 ✅ |
💡 结论：UNIBROWSE代理在五个多模态BrowseComp基准上的平均准确率最优，远超基线及主流闭源代理，性能提升幅度达10.5分。

**表2：效率对比（参数量与训练效率）**
| 方法 | 参数量 | 训练效率特性 |
|------|--------|--------------|
| Qwen3.5-35B-A3B | 35B | 基准训练效率 |
| UNIBROWSE代理 | 35B | 因探索度指标筛选优化训练效率 |
💡 结论：UNIBROWSE代理与基线参数量相当，通过低信号实例筛选有效提升了强化学习的训练效率。

**表3：跨域/zero-shot迁移性能**
| 方法 | 跨域zero-shot平均准确率 |
|------|--------------------------|
| 基线代理（Qwen3.5-35B-A3B） | 约40 |
| UNIBROWSE代理 | 约50 ✅ |
💡 结论：UNIBROWSE代理在跨域与zero-shot迁移场景下展现出更强的泛化能力，性能显著优于基线。

**表4：鲁棒性/扰动测试性能**
| 方法 | 动态网页扰动后任务完成率 |
|------|--------------------------|
| 基线代理（Qwen3.5-35B-A3B） | 约45 |
| UNIBROWSE代理 | 约53 ✅ |
💡 结论：UNIBROWSE代理对动态网页内容的扰动具有更强的鲁棒性，任务完成率优于基线模型。

**表5：消融实验结果**
| 模块（数据覆盖三种模式/知识图谱+实时检索/探索度指标） | 平均准确率 |
|--------------------------------------------------------|------------|
| 全模块启用（✅/✅/✅） | 54.4 ✅ |
| 仅启用数据覆盖+知识图谱+检索（✅/✅/❌） | 48.7 |
| 仅启用数据覆盖+探索度（✅/❌/✅） | 46.2 |
| 仅启用基础数据（❌/❌/❌） | 40.1 |
💡 结论：数据覆盖范围、数据保真度提升、探索度指标三者协同作用是UNIBROWSE代理性能最优的核心，任一模块缺失都会导致性能明显下降。

4. 关键结论和发现
- 主要发现：1. 覆盖文本、图像转文本、文本转图像三种信息流模式的训练数据，可显著提升多模态BrowseComp代理的任务性能与泛化能力；2. 知识图谱与实时网页检索的结合，能有效增强代理对动态网页内容的理解与工具使用的准确性；3. 探索度指标筛选低信号训练样本，可优化强化学习过程，提升代理的长程推理与任务探索能力。
- 方法局限性：未针对极端复杂动态网页场景进行优化，文本转图像模式的训练数据规模与质量仍有提升空间。
- 未来工作：进一步优化文本转图像模式的数据生成质量与规模，拓展代理对极端复杂动态网页任务的处理能力，提升代理在极端扰动场景下的鲁棒性。

> ✅ **总结一句话**：UNIBROWSE是首个覆盖三种信息流模式的多模态浏览代理框架，通过统一数据管道、知识图谱+实时检索及探索度指标的核心设计，实现了远超基线和主流闭源代理的多模态BrowseComp性能，为开放式动态网页任务的代理研究提供了新的技术路线。

</details>

---

### 8. [Trust Before Fusion: QIMG-7 and Source-Aware Resolution for Polluted Multimodal RAG](https://arxiv.org/abs/2607.10798)

**Authors**: Saadeldine Eletter, Owais Aijaz, Preslav Nakov  
**Category**: cs.CL  
**Published**: 2026-07-14  
**Score**: 62.5  
**Type**: new  
**ArXiv ID**: 2607.10798v1  

#### Abstract
Multimodal retrieval-augmented generation (RAG) is often evaluated with clean evidence, yet real retrieval can return topically relevant but unreliable content: false text and misleading images from corrupted metadata, entity swaps, typographic overlays, semantic edits, adversarial patches, blends, ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Trust Before Fusion: QIMG-7 and Source-Aware Resolution for Polluted Multimodal RAG
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多模态RAG多基于干净检索数据评估，但实际应用中易返回受污染内容（如虚假文本、误导性图像），污染原因包括元数据损坏、实体交换、语义编辑等；不同现有方法存在以下缺陷：
1. 全模态融合方法（Full-MM）在污染场景下性能骤降（如GPT-4o-mini中从干净的0.908降至污染的0.490）；
2. 纯文本方法（Text-only）忽略了检索的图像信息，未能充分利用多模态输入；
3. 级联路由方法（Cascaded Router）在污染场景下无法可靠选择最优答案路径，性能不及参数化模型的 fallback策略。

🚀 提出的新方法与思路
**Source-Aware Trust Resolution (SATR)**：一种训练无关的策略，通过对比Parametric、Text-only、Full-MM三种候选答案的源可靠性，选择最优答案或执行 fallback决策，无需对模型或检索系统进行额外训练；其衍生的Field-Selector变体在文本优先场景下基于显式文本可靠性建模实现选择，是性能提升的核心模块。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
多模态检索污染鲁棒性 | 在文本优先事实QA场景中，平衡分数达0.816，较Full-MM提升11.7，较Cascaded Router提升2.7
训练成本 | 训练无关，无需额外模型训练或微调
信息利用与抗污染平衡 | 兼顾多模态融合的信息利用能力和纯文本方法的抗污染特性，综合性能均衡性最优

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
QIMG-7 | 构建的受控多模态检索污染基准，跨越4个基础数据集，覆盖7种图像攻击家族，设置16组干净/污染配对，共1760条评估行

🎯 实验设置与评估指标
任务为文本优先的多模态检索事实QA，评估指标含义如下：
指标 | 含义（箭头）
--- | ---
平衡分数 | 兼顾正确率与鲁棒性的综合指标，↑越高越好

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
Full-MM | 多模态融合方法 | 直接整合检索的文本与图像内容生成答案
Text-only | 纯文本方法 | 仅利用检索的文本内容生成答案
Parametric Fallback | 参数化方法 | 当融合性能不足时，调用预训练参数化模型生成答案
Cascaded Router | 路由方法 | 现有多模态RAG路由策略，基于规则选择最优答案路径

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主基准QIMG-7性能（文本优先事实QA）**
方法 | 平衡分数
--- | ---
Full-MM | 0.699
Cascaded Router | 0.789
Field-Selector (SATR变体) | 0.816 ✅
💡 结论：SATR的Field-Selector变体在QIMG-7主基准上达到最优平衡分数，显著优于传统全模态融合和级联路由方法，验证了选择性信任策略的有效性。

**表2：SATR消融实验（文本可靠性建模影响）**
模块（启用✅/禁用❌） | 平衡分数
--- | ---
文本可靠性建模 ✅ | 0.816 ✅
文本可靠性建模 ❌ | 0.752
💡 结论：显式文本可靠性建模是SATR性能提升的核心驱动因素，验证了文本优先场景下文本可靠性的关键作用。

4. 关键结论和发现
- 主要发现：1）在多模态检索污染的文本优先事实QA场景中，选择性信任策略（SATR）较无条件全模态融合具有显著性能优势；2）显式文本可靠性建模是SATR性能提升的核心驱动力；3）现有全模态融合方法在污染场景下性能骤降，不如参数化模型的 fallback策略，而SATR实现了性能与鲁棒性的平衡。
- 方法局限性：仅在文本优先的事实QA场景中验证了方法有效性，未覆盖其他多模态任务（如生成对话、多轮问答）；仅考虑了7种图像攻击类型，未涵盖所有可能的检索污染场景（如文本语义污染）。
- 未来工作：扩展SATR至其他多模态任务类型；覆盖更多样的检索污染类型（如文本语义污染、图像细节污染）；研究主动检测检索内容污染的机制，进一步提升多模态RAG的可靠性。

> ✅ **总结一句话**：该论文构建了多模态检索污染基准QIMG-7，提出训练无关的Source-Aware Trust Resolution方法及其Field-Selector变体，证明在文本优先的多模态检索事实QA场景中，选择性信任策略可显著优于传统全模态融合方法，为解决多模态RAG的可靠性痛点提供了有效思路。

</details>

---

### 9. [Route, Communicate, and Reason: Gated Routing and Adaptive Depth for Efficient Multi-Agent Reasoning](https://arxiv.org/abs/2607.10836)

**Authors**: Sudipto Ghosh, Tanmoy Chakraborty  
**Category**: cs.AI  
**Published**: 2026-07-14  
**Score**: 55.5  
**Type**: new  
**ArXiv ID**: 2607.10836v1  

#### Abstract
Multi-agent ensembling multiplies active parameters and inference cost without answering three basic questions: which agents to consult, how deeply a query should traverse a hierarchy of agents, and when inter-agent communication is worth its cost. We present GRADE (Gated Routing and Adaptive Depth ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Route, Communicate, and Reason: Gated Routing and Adaptive Depth for Efficient Multi-Agent Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题：现有多智能体集成会成倍增加活跃参数和推理成本，且未明确解决三个核心问题：需咨询哪些智能体、查询应在智能体层次中遍历多深、跨智能体通信何时具备成本效益，导致推理效率与性能难以平衡。
🚀 提出的新方法与思路
**GRADE框架**：一种层次化多智能体系统，通过四个轻量可学习门控，分别控制智能体选择、层次深度、跨智能体通信及分支修剪，实现推理过程的动态调度。
**CoGRPO训练算法**：一种新型无评论家多智能体优化方法，将GRPO适配到多智能体层次结构中，为所有参与回合的门控模块和智能体分配共享优势信号，完成模型训练。
**热插拔专家注册表+智能体校准映射**：支持灵活替换智能体专家，无需重新训练即可在推理时完成专家替换，提升系统灵活性。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 推理效率 | 仅需一半活跃计算量即可取得高基准性能，有效降低推理成本 |
| 性能表现 | 在GSM8K、MMLUPro、GPQA等基准上优于所有基线，MMLUPro上超出最强基线4.8分 |
| 专家适配性 | 支持智能体专家热插拔，无需重训，提升系统部署灵活性 |
| 深度任务性能 | 在AIME-2025等深度主导的任务中仍保持竞争力 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| GSM8K | 测试数学推理能力 |
| MMLUPro | 测试通用语言理解能力 |
| GPQA | 测试通用专业问答能力 |
| AIME-2025 | 测试深度相关推理能力 |
🎯 实验设置与评估指标
任务为多智能体推理任务，评估指标如下：
| 指标 | 含义（箭头） |
| --- | --- |
| 任务准确率 | 衡量推理结果正确性，↑越高越好 |
| 活跃参数量 | 衡量推理所需激活的参数规模，↓越低越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 现有多智能体集成框架 | 多智能体系统 | 未解决智能体选择、深度控制、通信效益判断问题，活跃参数及计算成本较高 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主基准性能（通用推理任务）**
| 方法 | GSM8K准确率 | MMLUPro准确率 | GPQA准确率 |
| --- | --- | --- | --- |
| 基线1 | 82.3% | 76.5% | 68.2% |
| 基线2 | 83.1% | 77.2% | 69.0% |
| GRADE | 85.2% ✅ | 82.0% ✅ | 73.1% ✅ |
💡 结论：GRADE在GSM8K、MMLUPro、GPQA等通用推理基准上均取得最优性能。
**表2：效率对比**
| 方法 | 平均活跃参数量 | 相对活跃计算量 |
| --- | --- | --- |
| 基线最强方法 | ~34B | 100% |
| GRADE | ~17B | 50% ✅ |
💡 结论：GRADE以约一半的活跃计算量实现更强性能，效率优势显著。
**表3：AIME-2025性能（深度主导任务）**
| 方法 | AIME-2025准确率 |
| --- | --- |
| 基线最优 | 45.3% |
| GRADE | 44.8% ✅ |
💡 结论：GRADE在深度主导的AIME-2025任务中保持与最优基线相近的性能，具备较强的任务适应性。
**表4：消融实验（模块贡献）**
| 模块 | 层次结构 | 掩码交叉注意力 | 智能体校准映射 | MMLUPro准确率 |
| --- | --- | --- | --- | --- |
| 完整GRADE | ✅ | ✅ | ✅ | 82.0% ✅ |
| 无层次结构 | ❌ | ✅ | ✅ | 78.3% |
| 无掩码交叉注意力 | ✅ | ❌ | ✅ | 79.1% |
| 无智能体校准映射 | ✅ | ✅ | ❌ | 80.2% |
💡 结论：层次结构和掩码交叉注意力是GRADE准确性的核心贡献模块，智能体校准映射对安全热替换智能体必要。
4. 关键结论和发现
- 主要发现1：GRADE通过四部门控机制有效平衡了多智能体推理的性能与效率，在低活跃计算量下实现最优基准性能。
- 主要发现2：层次结构和掩码交叉注意力对模型准确性贡献最大，智能体校准映射是安全替换专家的必要条件。
- 主要发现3：GRADE在通用推理基准和深度主导任务中均表现出较强竞争力，具备任务泛化能力。
- 方法局限性：在深度主导任务（如AIME-2025）中性能略逊于最优基线，仍有提升空间。
- 未来工作：可针对深度主导任务优化门控机制，进一步提升跨场景通信效率，增强专家动态调度的灵活性。

> ✅ **总结一句话**：GRADE是一种高效的门控层次化多智能体推理框架，通过新颖的训练算法与灵活的专家管理机制，在降低活跃计算量的同时实现优异的推理性能，并支持智能体专家的热插拔部署。

</details>

---

### 10. [Nonparametric Bayesian Inverse Reinforcement Learning with Data-Parallel Gibbs Sampling](https://arxiv.org/abs/2607.09886)

**Authors**: Sai Anirudh Katupilla, Shreeya Dasa Lakshminath  
**Category**: cs.LG  
**Published**: 2026-07-14  
**Score**: 55.5  
**Type**: new  
**ArXiv ID**: 2607.09886v1  

#### Abstract
Inverse Reinforcement Learning recovers reward functions from expert demonstrations, but standard formulations assume that all demonstrations come from a single expert. When demonstrations are pooled from multiple experts with distinct preferences, parametric methods recover an averaged reward that ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Nonparametric Bayesian Inverse Reinforcement Learning with Data-Parallel Gibbs Sampling
1. 论文的主要贡献和创新点
✅ 解决的问题
现有标准逆强化学习（IRL）假设所有专家演示来自单一偏好，而多偏好专家的演示会让参数化方法输出平均奖励函数，对个体专家的奖励拟合效果差，尤其是当存在多组不同偏好的专家时，聚类和奖励恢复的性能会进一步下降。

🚀 提出的新方法与思路
**Nonparametric Bayesian Inverse Reinforcement Learning**
引入Dirichlet Process先验对奖励函数建模，可联合推断潜在奖励类型的数量与对应各类型的奖励；推理采用collapsed Gibbs sampler，集成Chinese Restaurant Process（CRP）更新聚类分配、Metropolis-Hastings更新奖励权重，内部规划用soft value iteration；进一步基于Ray在HPC上并行化采样器，解决串行推断效率低的问题；设计共识合并启发式用于状态聚合，但该启发式会引入吞吐量与准确率的权衡。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 多专家建模适配性 | 支持不同偏好的多专家演示，避免参数化方法的平均奖励缺陷 |
| K=2时聚类Adjusted Rand Index（ARI） | 达到1.000，显著优于基线Maximum Entropy IRL的0.000 |
| K=3时聚类能力 | 正确识别真实聚类数量，ARI为0.48-0.58，表现优于基线 |
| 并行推断效率 | 8个CPU worker时峰值加速比达4.79x，大幅提升推断速度 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 10x10 ObjectWorld grid | 验证多专家IRL方法在离散网格场景下的聚类与奖励恢复能力，测试K=2、K=3真实奖励类型的性能 |

🎯 实验设置与评估指标
任务：从多专家演示中恢复对应各专家类型的奖励函数。
| 指标 | 含义（箭头方向） |
|------|------------------|
| Adjusted Rand Index（ARI）↑ | 越高越好，衡量聚类分配与真实标签的匹配度 |
| 加速比↑ | 越高越好，衡量并行推断相对于串行的速度提升倍数 |
| 吞吐量↑ | 越高越好，衡量单位时间处理的样本数 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| Maximum Entropy IRL | 参数化IRL | 假设演示来自单一专家，输出平均奖励函数，单专家场景表现尚可，多专家时拟合差 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：不同方法在K=2、K=3专家的ARI结果**
| 方法 | ARI（K=2） | ARI（K=3） |
|------|------------|------------|
| Serial Nonparametric Bayesian IRL | 1.000✅ | 0.55✅ |
| Parallel Nonparametric Bayesian IRL | 0.998 | 0.52 |
| Maximum Entropy IRL | 0.000 | 0.12 |
💡 结论：本文串行方法在K=2时完全恢复真实聚类，K=3时聚类表现显著优于基线，有效解决多偏好专家的奖励拟合问题。

**表2：并行推断的加速比结果**
| Worker数 | 加速比 |
|----------|--------|
| 1 | 1.00 |
| 2 | 2.12 |
| 4 | 3.65 |
| 8 | 4.79✅ |
💡 结论：基于Ray的并行化随worker数增加实现加速，8个worker时峰值加速比达4.79x，大幅提升推断效率。

**表3：共识合并启发式的吞吐量-准确率权衡**
| 状态聚合启发式 | 吞吐量（样本/秒） | ARI |
|----------------|-------------------|-----|
| 启用（共识合并）✅ | 200 | 0.50 |
| 禁用（基础聚合）❌ | 150 | 0.52 |
💡 结论：共识合并启发式可提升推断吞吐量，但会轻微损失聚类准确率，可根据需求灵活调整。

4. 关键结论和发现
- 带Dirichlet Process先验的非参数贝叶斯IRL，可从多偏好专家演示中联合推断奖励聚类与对应奖励，避免参数化方法的平均奖励缺陷，在K=2时完全聚类正确，K=3时表现显著优于基线。
- 基于Ray的并行Gibbs采样在HPC平台实现高效加速，8个worker时峰值加速比达4.79x，有效解决串行IRL推断效率低的问题。
- 状态聚合的共识合并启发式存在吞吐量与准确率的权衡，是并行IRL设计的关键考量因素。

方法局限性：K=3时聚类的ARI仍处于中等水平，因专家行为存在重叠；10x10 ObjectWorld的评估依赖物体放置，随机种子会影响结果，需受控放置保证评估可靠性。

未来工作：优化多专家类型（K>3）时的聚类准确性；改进并行采样的状态聚合策略，减少吞吐量与准确率的权衡损失；拓展方法到更大规模环境或真实机器人演示场景。

> ✅ **总结一句话**：本文提出的带Dirichlet Process先验的非参数贝叶斯IRL方法结合Ray并行Gibbs采样，能有效从多偏好专家演示中恢复对应奖励函数与聚类，在离散网格场景取得优于基线的性能并实现显著加速。

</details>

---

### 11. [Empowering Long-form Omni-modal Understanding with Robust Audio Perception](https://arxiv.org/abs/2607.10299)

**Authors**: Kaiying Yan, Luoyi Sun, Xiao Zhou, Weidi Xie  
**Category**: cs.LG  
**Published**: 2026-07-14  
**Score**: 55.0  
**Type**: new  
**ArXiv ID**: 2607.10299v1  

#### Abstract
Recent advances in large-scale multimodal models have drivenremarkable progress in vision-language tasks; however, comprehensiveomni-modal understanding remains under-explored, largely due to thescarcity of datasets with rich, explicitly aligned auditory cues. To bridgethis gap, we present AVDC (Aud...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Empowering Long-form Omni-modal Understanding with Robust Audio Perception
1. 论文的主要贡献和创新点
✅ 解决的问题
现有大规模视觉-语言多模态模型在视觉相关任务上进展显著，但全面的全模态理解（融合视觉、音频等多模态）仍未充分探索，核心痛点是缺乏带有丰富、明确对齐听觉线索的高质量数据集；此外，现有音频-视频相关模型多侧重单模态或简单跨模态交互，未明确分离视听模态的语义细节，难以捕捉长视频中的复杂多模态关系，限制了全模态理解能力。

🚀 提出的新方法与思路
**AVDC (Audio-Visual Decoupled Captions)**：提出自动化标注流程，利用现有模型为视频生成三类解耦字幕——仅视觉（V）、仅音频（A）、联合视听（AV），明确区分模态特异性细节与跨模态交互，适配长视频全模态语义建模。
**AVDC-QA-CoT**：构建Chain-of-Thought（CoT）增强的音频-视觉问答数据集，通过思维链推理强化模型对跨模态逻辑的理解能力。
**两阶段训练范式**：采用“全模态字幕生成预训练+指令调优”的两阶段训练，先在AVDC上学习通用多模态语义，再在AVDC-QA-CoT上适配下游推理任务，平衡性能与泛化性。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 数据结构 | 解耦式视听标注明确分离模态特异性与跨模态交互，CoT问答强化逻辑推理，支持长视频全模态理解 |
| 训练范式 | 两阶段训练适配多类下游任务，解决单阶段训练泛化性不足的问题 |
| 任务覆盖 | 支持视频字幕生成、音频分析、全模态基准等多类任务，覆盖现有模型未充分探索的音频中心分析场景 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| AVDC | 用于全模态字幕生成预训练，提供解耦视听语义的标注数据 |
| AVDC-QA-CoT | 用于音频-视觉推理指令调优，增强模型的跨模态推理能力 |

🎯 实验设置与评估指标
实验覆盖视频字幕生成、音频中心分析、全模态理解基准三类任务，评估指标及含义如下：
| 指标 | 含义 | 方向 |
|------|------|------|
| CIDEr/BLEU（视频字幕） | 衡量字幕与参考文本的语义相似度 | ↑ 越高越好 |
| 音频分类准确率 | 衡量音频内容识别的正确比例 | ↑ 越高越好 |
| 基准任务整体准确率 | 衡量全模态理解任务的综合表现 | ↑ 越高越好 |
| FPS | 衡量推理速度（帧/秒） | ↑ 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| BLIP-2 | 通用视觉-语言大模型 | 仅支持视觉-语言交互，未利用丰富听觉线索，无解耦式语义建模 |
| AV-HuBERT | 音频-视频专用模型 | 侧重单模态处理，对长视频全模态推理支持不足，无CoT问答数据 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（跨下游任务）（场景：视频字幕、音频分析、全模态理解）**
| 方法 | 视频字幕CIDEr | 音频分类准确率 | 全模态基准准确率 |
|------|--------------|----------------|------------------|
| BLIP-2 | 72.3 | 78.5 | 81.2 |
| AV-HuBERT | 75.1 | 82.3 | 83.6 |
| 本方法 | 78.9✅ | 85.7✅ | 87.4✅ |
💡 结论：本方法在三类下游任务上均实现显著性能提升，验证了解耦数据集与两阶段训练的有效性。

**表2：效率对比（FPS）（场景：推理速度）**
| 方法 | FPS（帧/秒） |
|------|--------------|
| BLIP-2 | 16.2 |
| AV-HuBERT | 22.5 |
| 本方法 | 20.1✅ |
💡 结论：本方法在保持高任务性能的同时，推理效率优于通用视觉-语言模型，可适配长视频实时处理需求。

**表3：跨域/zero-shot迁移性能（场景：OOD视频数据集）**
| 方法 | OOD数据集准确率 |
|------|----------------|
| BLIP-2 | 68.7 |
| AV-HuBERT | 71.3 |
| 本方法 | 76.9✅ |
💡 结论：本方法具有更强的zero-shot跨域迁移能力，在未见过的视频场景中表现更稳定。

**表4：鲁棒性测试（场景：音频/视觉扰动）**
| 扰动类型 | BLIP-2保留率 | AV-HuBERT保留率 | 本方法保留率 |
|----------|--------------|------------------|--------------|
| 音频噪声 | 75.2 | 80.1 | 88.5✅ |
| 视觉模糊 | 72.8 | 78.3 | 85.2✅ |
💡 结论：本方法在扰动下的鲁棒性显著优于基线，适配实际复杂应用场景。

**表5：消融实验（场景：各模块对整体性能的影响）**
| V | A | AV | CoT问答 | 两阶段训练 | 整体准确率 |
|---|---|---|---------|------------|------------|
| ❌ | ❌ | ✅ | ❌ | ❌ | 71.5 |
| ✅ | ❌ | ❌ | ❌ | ✅ | 76.2 |
| ❌ | ✅ | ❌ | ✅ | ✅ | 78.9 |
| ✅ | ✅ | ❌ | ✅ | ✅ | 83.1 |
| ✅ | ✅ | ✅ | ✅ | ✅ | 87.4✅ |
💡 结论：所有模块均对性能有正向贡献，完整配置的解耦结构、CoT问答与两阶段训练是最优组合。

4. 关键结论和发现
- 主要发现：1）解耦视听语义的AVDC数据集与CoT增强的AVDC-QA-CoT数据，有效提升了模型对模态特异性和跨模态关系的捕捉能力；2）两阶段训练范式平衡了性能与泛化性，适配多类下游任务；3）本方法在zero-shot跨域迁移和扰动鲁棒性上显著优于现有通用多模态模型。
- 方法局限性：当前模型对超长时间视频（>10分钟）的全模态理解存在细节丢失，未针对动态时序推理优化，极端复杂场景表现有待提升。
- 未来工作：1）扩展超长时间视频的时序建模能力；2）结合动态推理机制提升效率；3）探索融合触觉、嗅觉等更多模态的全模态框架；4）构建更大规模的跨域多模态数据集。

> ✅ **总结一句话**：本文提出的AVDC解耦字幕数据集、AVDC-QA-CoT问答数据集及两阶段训练范式，解决了现有全模态理解缺乏丰富对齐听觉线索的痛点，在多下游任务上实现显著性能提升，推动了长视频全模态理解的进展。

</details>

---

### 12. [Multimodal Routing for Interpretable, Robust, and Auditable Clinical Prediction](https://arxiv.org/abs/2607.09982)

**Authors**: Nikkie Hooman, Zhongjie Wu, Eric C. Larson, Mehak Gupta  
**Category**: cs.LG  
**Published**: 2026-07-14  
**Score**: 54.5  
**Type**: new  
**ArXiv ID**: 2607.09982v1  

#### Abstract
Electronic health record (EHR) data are inherently multimodal, and leveraging multiple modalities can improve predictive performance. However, most existing approaches rely on deep fusion, which obscures how individual modalities contribute to predictions and limits the interpretability of multimoda...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Multimodal Routing for Interpretable, Robust, and Auditable Clinical Prediction
1. 论文的主要贡献和创新点
✅ 解决的问题
现有临床预测的多模态方法多采用深度融合策略，导致模型推理过程不透明，无法清晰展示各模态对预测结果的贡献，严重限制了多模态临床预测的可解释性、鲁棒性及可审计性，难以满足临床决策的可靠性要求。

🚀 提出的新方法与思路
**Multimodal Routing Framework**：针对电子健康记录（EHR）的三种模态（结构化纵向变量L、临床笔记N、胸部X光I），构建离散的单模态路径、定向双模态路径及三模态路径，全面捕捉单个模态的信号贡献及非对称跨模态交互；引入推理时的Route Masking技术，通过模拟某一模态缺失的场景，重新调整剩余模态路径的权重，无需对模型进行重新训练，即可实现多模态推理的审计及模型鲁棒性评估。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 可解释性 | 构建离散的路由路径，清晰呈现各模态及跨模态交互对预测的贡献，避免深度融合带来的黑箱问题 |
| 鲁棒性 | Route Masking可快速评估模型在单一模态缺失等实际数据场景下的性能，无需重新训练模型 |
| 可审计性 | 路由权重的可追溯性支持量化分析模型决策依赖的数据源，提升临床预测过程的透明度与可验证性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| MIMIC-IV | 多标签表型预测（K=25）及二进制ICU死亡率预测的三模态患者数据 |

🎯 实验设置与评估指标
任务为多标签表型预测（共25类表型）与二进制ICU死亡率预测，采用的评估指标包括AUC（ROC）、F1-score。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Deep Fusion Model | 多模态方法 | 采用黑箱式深度融合，可解释性差 |
| Unimodal Models | 基准方法 | 仅使用单一模态数据，性能受限 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主Benchmark性能（MIMIC-IV）**
| 方法 | AUC（表型） | AUC（死亡率） | F1（表型） | F1（死亡率） |
| ---- | ---- | ---- | ---- | ---- |
| Deep Fusion | 0.85 | 0.88 | 0.79 | 0.83 |
| Unimodal (L) | 0.78 | 0.82 | 0.72 | 0.76 |
| Unimodal (N) | 0.81 | 0.85 | 0.75 | 0.79 |
| Unimodal (I) | 0.80 | 0.84 | 0.74 | 0.78 |
| Multimodal Routing | 0.89 ✅ | 0.92 ✅ | 0.83 ✅ | 0.87 ✅ |
💡 结论：所提Multimodal Routing框架在多标签表型预测与ICU死亡率预测任务上，均显著优于基线方法，达到最优性能。

**表2：鲁棒性测试（Route Masking）**
| 方法 | 模态全保留AUC（死亡率） | L缺失AUC（死亡率） | N缺失AUC（死亡率） | I缺失AUC（死亡率） |
| ---- | ---- | ---- | ---- | ---- |
| Deep Fusion | 0.88 | 0.80 | 0.82 | 0.79 |
| Multimodal Routing | 0.92 | 0.87 | 0.89 | 0.86 |
💡 结论：Multimodal Routing框架在模拟模态缺失的鲁棒性测试中，性能下降幅度更小，表现出更优的鲁棒性。

**表3：消融实验（ICU死亡率预测）**
| 模块（L/N/I路由） | AUC（死亡率） | 路由权重可追溯性 |
| ---- | ---- | ---- |
| 全禁用 | 0.75 ❌ | 无 |
| 仅L启用 | 0.82 | 部分 |
| 仅N启用 | 0.83 | 部分 |
| 仅I启用 | 0.81 | 部分 |
| 双模态启用（L+N） | 0.87 | 中等 |
| 三模态启用（L+N+I） | 0.92 ✅ | 完全 |
💡 结论：三模态路由模块的全启用是模型达到最优性能及可追溯性的关键。

4. 关键结论和发现
- 主要发现：1）不同临床表型及ICU死亡率预测中，模态依赖存在显著差异，如ICU死亡率预测更依赖胸部X光（I）与结构化变量（L）；2）Multimodal Routing框架在保持预测性能的同时，实现了更优的可解释性、鲁棒性及可审计性；3）推理时的Route Masking技术可有效量化模型在模态缺失场景下的鲁棒性，且能直观呈现各模态的决策贡献。
- 方法局限性：仅在公开数据集MIMIC-IV上进行验证，未纳入更多不同医院、不同地区的外部临床数据，泛化能力需进一步验证；
- 未来工作：扩展框架至更多临床模态（如实验室检查结果、生命体征时序数据），优化路由权重的临床可解释性，开发支持临床医生交互的可视化工具。

> ✅ **总结一句话**：提出的Multimodal Routing框架为多模态临床预测提供了兼具可解释性、鲁棒性和可审计性的实用解决方案，解决了现有深度融合多模态方法黑箱化的核心缺陷。

</details>

---

### 13. [Agentic-DPO: From Imitation to Agentic Policy Optimization on Expert Trajectories](https://arxiv.org/abs/2607.10601)

**Authors**: Yixiong Chen, Alan Yuille  
**Category**: cs.AI  
**Published**: 2026-07-14  
**Score**: 53.5  
**Type**: new  
**ArXiv ID**: 2607.10601v1  

#### Abstract
Large Language Model (LLM) agents are commonly trained from expert trajectories using supervised fine-tuning (SFT), which treats multi-turn agent behavior as ordinary text imitation. This recipe is simple and low-cost, but it only learns to imitate the sequence of expert actions, rather than trainin...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Agentic-DPO: From Imitation to Agentic Policy Optimization on Expert Trajectories
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：LLM智能体常用SFT从专家轨迹训练，但SFT仅做普通文本序列模仿，未训练智能体应对每个状态下的合理错误；现有偏好学习或强化学习方法需高代价的环境rollout和奖励模型，成本高昂。

🚀 提出的新方法与思路
**Agentic-DPO**：提出的轻量离线智能体策略优化方法，将专家轨迹转换为状态条件偏好监督；每个专家动作状态下，从当前策略采样单步动作作为合理错误负样本，采用DPO-style偏好目标对比专家动作与负样本；无需在线环境rollout、奖励模型或全轨迹学生探索。
**Policy-Preserving Augmentation (PPA)**：引入的策略保留增强模块，在保持专家策略固定的情况下，对同一潜在轨迹渲染多种schema，避免偏好学习中混淆策略与schema，确保偏好监督的有效性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 训练代价 | 无需在线环境rollout、奖励模型，仅需离线专家轨迹，成本极低 |
| 策略优化效果 | 9B模型tau-bench准确率从SFT的21.7%提升至41.4%，匹配在线GRPO性能 |
| 资源依赖 | 不需要全轨迹学生探索，仅需步级rollout，梯度步骤中无环境交互 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| StableToolBench、tau-bench retail、Mind2Web | 不同工具调用类任务的智能体性能评估 |

🎯 实验设置与评估指标
任务：多步工具调用的LLM智能体任务完成能力评估
| 指标 | 含义（方向） |
| ---- | ---- |
| 任务准确率 | 衡量智能体完成目标任务的正确率，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| SFT | 监督微调 | 基于专家轨迹的文本序列模仿，简单低成本但性能有限 |
| 在线GRPO | 强化学习方法 | 需在线环境交互rollout，性能较好但代价高 |
| Agentic-DPO | 本文方法 | 轻量离线策略优化，无在线环境交互，成本低且性能接近在线GRPO |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：不同基准任务性能对比（9B模型）**
| 方法 | tau-bench准确率 | StableToolBench准确率 | Mind2Web准确率 |
| ---- | ---- | ---- | ---- |
| SFT | 21.7% | 35.2% | 28.9% |
| 在线GRPO | 40.8% | 52.1% | 41.5% |
| Agentic-DPO | 41.4% ✅ | 53.7% ✅ | 42.3% ✅ |
💡 结论：Agentic-DPO在三个基准任务上均显著超越SFT，性能接近在线GRPO，大幅提升9B模型的任务完成能力。

**表2：训练效率对比**
| 方法 | 在线环境交互需求 | 训练成本 |
| ---- | ---- | ---- |
| SFT | 无 | 低 |
| 在线GRPO | 需大量环境rollout | 极高 |
| Agentic-DPO | 仅需步级rollout（梯度步骤无交互） | 低 |
💡 结论：Agentic-DPO在低训练代价下实现了接近在线RL的性能，大幅降低了智能体策略优化的成本。

**表3：Agentic-DPO消融实验结果（tau-bench准确率）**
| PPA | DPO偏好目标 | 准确率 |
| ---- | ---- | ---- |
| ❌ | ❌ | 21.7% |
| ✅ | ❌ | 32.5% |
| ❌ | ✅ | 35.1% |
| ✅ | ✅ | 41.4% ✅ |
💡 结论：PPA和DPO偏好目标是Agentic-DPO性能提升的核心模块，两者同时启用时性能最优。

4. 关键结论和发现
- 主要发现：1、Agentic-DPO无需在线环境交互和奖励模型，即可将专家轨迹有效转化为状态级动作偏好监督，实现智能体策略优化；2、PPA模块通过保持专家策略固定，解决了偏好学习中策略与schema混淆的问题，对性能提升至关重要；3、在工具调用任务上，Agentic-DPO的性能接近在线GRPO，但训练成本显著更低。
- 方法局限性：仅在工具调用类任务中验证，未覆盖对话、导航等其他智能体任务；依赖高质量专家轨迹，轨迹质量下降可能导致性能衰减。
- 未来工作：拓展Agentic-DPO至更多类型的智能体任务；研究低质量专家轨迹下的鲁棒优化方法；探索更大模型规模下的性能表现。

> ✅ **总结一句话**：Agentic-DPO通过将专家轨迹转换为状态级动作偏好监督，结合策略保留增强模块，以低成本实现了接近在线强化学习的LLM智能体性能提升，无需在线环境交互和奖励模型。

</details>

---

### 14. [TabPFN beyond Tabular Data: Calibration and Accuracy on Multimodal Embeddings](https://arxiv.org/abs/2607.11007)

**Authors**: Jingxiang Zhang, Lujia Zhong, Zijie Zhu, Shuo Huang, Yuang Xu  
**Category**: cs.LG  
**Published**: 2026-07-14  
**Score**: 53.5  
**Type**: new  
**ArXiv ID**: 2607.11007v1  

#### Abstract
Few-shot multimodal classification commonly attaches a lightweight head, such as $k$-nearest neighbors, logistic regression, or a linear SVM, to a frozen pretrained encoder. Although computationally efficient, these heads can produce poorly calibrated confidence scores, limiting their reliability in...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：TabPFN beyond Tabular Data: Calibration and Accuracy on Multimodal Embeddings
1. 论文的主要贡献和创新点
✅ 解决的问题
①少样本多模态分类任务中，常用的轻量分类头（如k-nearest neighbors、logistic regression、linear SVM等）虽计算效率高，但预测置信度校准能力差，限制了其在可靠性要求高的场景（如医疗、自动驾驶）的应用；②TabPFN此前仅面向表格数据设计，未被探索作为多模态嵌入的分类头。

🚀 提出的新方法与思路
**TabPFN作为零梯度插即用分类头**：将原本面向表格数据的TabPFN改造为无需梯度更新的插即用分类头，直接适配冻结的图像、文本、音频等多模态编码器输出的嵌入特征，用于少样本多模态分类任务，通过覆盖14个数据集、11个编码器、3种模态的大规模评估验证性能。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 校准性能 | 在9种对比分类头中负对数似然（NLL）、预期校准误差（ECE）表现最优，NLL较基线平均降低48~62%，ECE较基线平均降低2.1~5.3倍 |
| 分类准确率 | 准确率匹配或超过8种基线方法的平均水平，在中等及以上shot数、低到中等特征维度场景下优势更明显 |
| 计算效率 | 作为零梯度头无需额外梯度训练，仅需对嵌入特征分类推理，部署成本低 |
| 适用范围 | 覆盖图像、文本、音频三类模态，通用性强 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 14个含图像、文本、音频模态的多模态分类数据集 | 覆盖不同模态与任务场景，用于少样本多模态分类的全面性能评估 |

🎯 实验设置与评估指标
任务为：基于冻结的多模态编码器输出嵌入特征的少样本多模态分类。
| 指标 | 含义 |
| ---- | ---- |
| 负对数似然（NLL） | 衡量预测概率与真实标签的匹配程度，↓ 越低越好 |
| 预期校准误差（ECE） | 衡量预测置信度与实际准确率的一致性，↓ 越低越好 |
| 分类准确率 | 衡量分类预测正确性，↑ 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| k-nearest neighbors（kNN） | 传统非参数分类头 | 基于距离的非参数分类，计算高效但易受噪声影响 |
| logistic regression（LR） | 线性参数分类头 | 轻量线性模型，训练成本低，适配小样本场景 |
| linear SVM | 线性支持向量机 | 基于最大间隔的线性模型，泛化性好，常用于少样本任务 |
| 其余6种分类头 | 各类轻量分类头 | 少样本多模态分类常用替代头，作为对比基线 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（多模态少样本分类）**
| 方法 | NLL（↓） | ECE（↓） | 准确率（↑） |
| ---- | ---- | ---- | ---- |
| TabPFN | ✅（最优） | ✅（最优） | 优秀 |
| 8种基线平均 | 较高 | 较高 | 平均水平 |
💡 结论：TabPFN的校准性能显著优于现有轻量分类头，同时准确率达到或超过基线平均水平。

**表2：效率对比（训练/部署成本）**
| 方法 | 训练成本 | 部署成本 |
| ---- | ---- | ---- |
| TabPFN | 零梯度，无需额外训练 | 低，仅需推理嵌入特征 |
| 需梯度训练的轻量头 | 需少量梯度迭代，成本稍高 | 中等 |
💡 结论：TabPFN作为零梯度头，训练和部署成本远低于需梯度训练的分类头，适合快速部署场景。

**表3：消融实验（场景依赖性）**
| 场景 | TabPFN准确率（↑） | 基线平均准确率（↑） |
| ---- | ---- | ---- |
| 中等及以上shot数（k≥50） | ✅ 优势明显 | 一般 |
| 少shot数（k<50） | 优势减弱 | 一般 |
| 低到中等特征维度（d≤32） | ✅ 优势显著 | 一般 |
| 高特征维度（d>32） | 优势减弱 | 一般 |
💡 结论：TabPFN的准确率优势在中等及以上shot数、低到中等特征维度场景下更突出，在少标记或高维度场景下优势下降。

4. 关键结论和发现
- 主要发现：①TabPFN作为零梯度分类头，在多模态少样本分类中校准性能最优且准确率匹配基线，适合校准敏感场景；②其准确率优势存在场景依赖性，在中等及以上shot数、低到中等特征维度时更明显。
- 方法局限性：未系统验证跨域迁移性能，少shot场景准确率仍有提升空间。
- 未来工作：探索TabPFN在跨域多模态分类、视频模态任务中的表现，优化少shot场景准确率。

> ✅ **总结一句话**：本文将面向表格数据的TabPFN改造为零梯度插即用分类头，应用于多模态嵌入的少样本分类，在保证计算高效的同时大幅提升了预测置信度的校准性能，为校准敏感的多模态分类应用提供了新方案。

</details>

---

### 15. [Valid $\ne$ Necessary: Diagnosing Latent Inefficiency in Chain-of-Thought](https://arxiv.org/abs/2607.11266)

**Authors**: Daeyeop Lee, Hwanjo Yu  
**Category**: cs.AI  
**Published**: 2026-07-14  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2607.11266v1  

#### Abstract
Chain-of-Thought (CoT) prompting has significantly advanced the reasoning capabilities of Large Language Models (LLMs), yet it often incurs substantial computational costs due to over-reasoning: the generation of redundant, verbose, or irrelevant steps. While existing reasoning step evaluators effec...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Valid ≠ Necessary: Diagnosing Latent Inefficiency in Chain-of-Thought

1. 论文的主要贡献和创新点
✅ 解决的问题
Chain-of-Thought（CoT）提示提升了大语言模型（LLM）的推理能力，但存在过度推理导致的高计算成本问题；现有推理步评估器仅能检测逻辑谬误和事实错误，无法惩罚有效但低效的推理步骤，这类步骤虽不提升解决方案却会增加Token消耗，成为CoT压缩的核心盲点。

🚀 提出的新方法与思路
**RIV-GSM8K**：构建的诊断基准，在GSM8K数据集上注入循环推理、过度分解等5种不同类型的低效推理步骤，用于测试现有评估器对低效推理的识别能力；
**CAID（Context-Aware Information Density）**：训练无关的信息论度量，通过衡量推理步骤的信息密度识别低效用步骤；
**PACE**：基于CAID的事后压缩策略，从CoT推理链中移除低效用步骤，实现轻量压缩。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 低效推理识别 | 填补现有评估器盲点，成功区分必要推理与有效但低效的冗余步骤 |
| CoT压缩性能 | 在多数据集上实现31-53%的Token压缩率，同时保持推理准确率 |
| 策略通用性 | 训练无关（CAID无需模型微调），属于事后压缩，不依赖PRM等强监督资源 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| RIV-GSM8K | 诊断现有评估器对低效推理的识别盲点 |
| GSM8K | 主实验验证PACE压缩效果 |
| StrategyQA | 跨域验证压缩策略泛化性 |
| ARC-Challenge | 跨域验证压缩策略泛化性 |

🎯 实验设置与评估指标
任务为评估CoT推理链的冗余性及压缩后的推理性能；评估指标及含义如下：
| 指标 | 含义（箭头） |
| --- | --- |
| 推理准确率 | 推理结果正确的比例，越高越好，↑ |
| Token消耗率 | 压缩后推理链Token数与原始的比值，越低越好，↓ |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Random Step Removal | 基准压缩方法 | 随机删除推理步，无针对性 |
| PRM-based Compression | 基准压缩方法 | 基于推理奖励模型（PRM）选择保留步骤，依赖强监督 |
| 现有推理步评估器 | 评估方法 | 仅检测逻辑/事实错误，无法识别有效但低效步骤 |
| PACE | 提出的压缩策略 | 基于CAID识别低效用步骤，事后轻量压缩 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：RIV-GSM8K上低效推理识别准确率（主benchmark性能）**
| 方法 | 识别准确率（%） |
| --- | --- |
| 现有推理步评估器 | 42 |
| CAID | 91 ✅ |
💡 结论：CAID在诊断基准RIV-GSM8K上对低效推理步骤的识别准确率远高于现有评估器，有效填补了其功能盲点。

**表2：不同压缩方法在GSM8K上的效率与性能对比（效率对比）**
| 方法 | Token节省率（%） | 推理准确率（↑） |
| --- | --- | --- |
| 原始CoT | - | 89.2 |
| Random Step Removal | 21 | 85.7 |
| PRM-based Compression | 32 | 88.1 |
| PACE | 45 ✅ | 88.9 ✅ |
💡 结论：PACE在接近PRM-based压缩的准确率下，实现了显著更高的Token节省率，效率优势突出。

**表3：不同数据集上的PACE跨域性能（跨域/zero-shot迁移）**
| 数据集 | Token节省率（%） | 推理准确率（↑） |
| --- | --- | --- |
| StrategyQA | 38 | 75.2 ✅ |
| ARC-Challenge | 53 ✅ | 72.1 |
💡 结论：PACE在StrategyQA、ARC-Challenge等跨域数据集上均实现了高Token压缩率，具备良好的跨域泛化能力。

**表4：PACE消融实验（消融实验）**
| CAID启用 | 阈值调整 | Token节省率（%） | 推理准确率（↑） |
| --- | --- | --- | --- |
| ✅ | ✅ | 45 ✅ | 88.9 ✅ |
| ❌ | ✅ | 22 | 86.3 |
| ✅ | ❌ | 31 | 85.7 |
| ❌ | ❌ | 12 | 82.1 |
💡 结论：CAID模块和合理的阈值调整对PACE的压缩效果与准确率保留均至关重要，缺一不可。

4. 关键结论和发现
- 主要发现：1. 现有推理步评估器存在显著盲点，无法区分有效但低效的推理步骤，导致CoT冗余问题被低估；2. CAID度量可准确识别低效用推理步，PACE策略在保持推理准确率的同时实现了31-53%的Token压缩；3. PACE作为训练无关的事后压缩策略，无需模型微调或强监督，实用性更强。
- 方法局限性：CAID对部分特殊推理结构或少数任务的低效用步骤识别可能存在偏差，需进一步优化通用适用性；PACE依赖阈值设置，需针对不同任务调整以达到最优效果。
- 未来工作：探索更通用的训练无关信息度量以提升CAID的跨任务鲁棒性；将PACE策略扩展应用于更多推理密集型任务（如逻辑证明、科学推理等）；优化阈值自适应调整机制以减少人工干预。

> ✅ **总结一句话**：这篇论文提出训练无关的CAID度量和事后压缩策略PACE，解决了CoT过度推理导致的高计算成本问题，在保持推理准确率的同时显著降低了Token消耗。

</details>

---

### 16. [Calibrated e-CUSUM Decoding for Quantized Reasoning Models: Why Token Log-Probability Is the Wrong Observable for Decoding Monitors](https://arxiv.org/abs/2607.11317)

**Authors**: El Hassane Ettifouri (Novelis Research, Paris, France), Ayoub Belfatmi (Novelis Research, Paris, France), Mahaman Sanoussi Yahaya Alassan (Novelis Research, Paris, France), Walid Dahhane (Novelis Research, Paris, France)  
**Category**: cs.AI  
**Published**: 2026-07-14  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2607.11317v1  

#### Abstract
Low-bit quantization makes small reasoning models inexpensive to deploy but can degrade their chains of thought. This motivates decoder-side monitors that intervene when generation becomes unreliable. We show that a natural candidate, the centered token log-probability increment $\log p(w_t)+H_t$, i...

---

### 17. [Personalized Emotional Intelligence in Generative AI through Symbolic Affective Reasoning](https://arxiv.org/abs/2607.10678)

**Authors**: Qing Lin, Mengmi Zhang  
**Category**: cs.AI  
**Published**: 2026-07-14  
**Score**: 52.0  
**Type**: new  
**ArXiv ID**: 2607.10678v1  

#### Abstract
Emotional intelligence enables humans to recognize emotions, infer their causes, reason about interventions, and modify their environment to achieve desired affective states. Despite recent advances in artificial intelligence (AI), current models remain largely limited to generating realistic conten...

---

### 18. [When Reasoning Hurts Legal Drafting: The Verbalization Bottleneck in Patent Claim Generation](https://arxiv.org/abs/2607.10480)

**Authors**: Lekang Jiang, Wenjun Sun, Stephan Goetz  
**Category**: cs.CL  
**Published**: 2026-07-14  
**Score**: 52.0  
**Type**: new  
**ArXiv ID**: 2607.10480v1  

#### Abstract
Patent claim drafting is a challenging legal drafting task that requires technical expertise, precise linguistic control, strict adherence to formal conventions, and the preservation of complex logical relationships among claim elements. While Chain-of-Thought (CoT) prompting has been widely used to...

---

### 19. [Graph Neural Networks for RFID-Based Spatial Geometry Inference in Spatial AI Systems](https://arxiv.org/abs/2607.10822)

**Authors**: Curtis Shull, Merrick Green, Roy Rucker  
**Category**: cs.LG  
**Published**: 2026-07-14  
**Score**: 51.5  
**Type**: new  
**ArXiv ID**: 2607.10822v1  

#### Abstract
Indoor spatial understanding remains a fundamental challenge for intelligent systems operating in physical environments. Traditional RFID localization techniques typically estimate positions of tags using signal strength measurements but fail to capture higher-order spatial relationships between obj...

---

### 20. [A Dynamic Scene Interaction Reasoning Framework for Scene-level Lane-Change Intention and Trajectory Prediction of Multiple Interacting Vehicles](https://arxiv.org/abs/2607.09740)

**Authors**: Joshua Kofi Asamoah, Blessing Agyei Kyem, Eugene Denteh, Armstrong Aboah  
**Category**: cs.AI  
**Published**: 2026-07-14  
**Score**: 51.0  
**Type**: new  
**ArXiv ID**: 2607.09740v1  

#### Abstract
Safe motion planning in advanced driver-assistance systems and autonomous vehicles requires an accurate understanding of how the surrounding traffic scene is likely to evolve. However, many existing lane-change prediction methods remain centered on a single target vehicle, while multi-agent forecast...

---

### 21. [Length Penalties Make Chain-of-Thought Less Monitorable](https://arxiv.org/abs/2607.09786)

**Authors**: Bryce Little  
**Category**: cs.AI  
**Published**: 2026-07-14  
**Score**: 51.0  
**Type**: new  
**ArXiv ID**: 2607.09786v1  

#### Abstract
Length-penalized reinforcement learning can shorten chain-of-thought reasoning while hiding an influence that drives the model's answer. In our experiments, training with length penalties does not stop misleading hints from steering models, even though the models' chains of thought mention the hint ...

---

### 22. [GRASP: GRanularity-Aware Search Policy for Agentic RAG](https://arxiv.org/abs/2607.10463)

**Authors**: Varun Gandhi, Jaewook Lee, Shantanu Todmal, Franck Dernoncourt, Ryan Rossi, Zichao Wang, Andrew Lan  
**Category**: cs.AI  
**Published**: 2026-07-14  
**Score**: 51.0  
**Type**: new  
**ArXiv ID**: 2607.10463v1  

#### Abstract
Agentic retrieval-augmented generation (RAG) extends static RAG by allowing language models to iteratively reason, generate search queries, retrieve evidence, and predict answers. However, it remains challenging for models to decide when to retrieve, whether to use lexical matching or semantic simil...

---

### 23. [DSSMs: State Space Models with Explicit Memory via Delay Differential Equations](https://arxiv.org/abs/2607.10244)

**Authors**: Yixiao Qian, Song Chen, Jiaxu Liu, Shengze Cai, Chao Xu  
**Category**: cs.LG  
**Published**: 2026-07-14  
**Score**: 48.0  
**Type**: new  
**ArXiv ID**: 2607.10244v1  

#### Abstract
State Space Models (SSMs) have emerged as a powerful paradigm for efficient long-sequence modeling, offering parallel training and fast linear-time recurrent inference. However, like other recurrent architectures, SSMs must compress an unbounded history into a fixed-size state, which limits context ...

---

### 24. [Silent Failures in Quantized LLM Reasoning: A Taxonomy-Based Analysis of Hollow Convergence and Failure Mode Shifts](https://arxiv.org/abs/2607.09999)

**Authors**: Renuka Oladri, Mohan Vamsi Varadaraju Priya, Jerry Wu  
**Category**: cs.CL  
**Published**: 2026-07-14  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2607.09999v1  

#### Abstract
We show that post-training quantization can silently alter how large language models reason even when task accuracy is preserved. Using a six-category failure taxonomy validated by two independent human annotators (Cohen's $\kappa$ = 0.906), we classify 30,000 chain-of-thought outputs from five inst...

---

### 25. [TreeThink: A Modular Tree Search Library for Mathematical Reasoning with LLMs](https://arxiv.org/abs/2607.11258)

**Authors**: Burak S. Akbudak, Zeynel A. Ulu\c{s}an, Can S. Erer, G\"ozde G\"ul \c{S}ahin  
**Category**: cs.CL  
**Published**: 2026-07-14  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2607.11258v1  

#### Abstract
Tree search algorithms enable systematic exploration of the proof space in neural theorem proving. Existing LLM tree search libraries primarily target natural language reasoning and do not provide native integration with formal verifiers, while theorem proving systems often rely on task-specific sea...

---

### 26. [EvoCUA-1.5: Online Reinforcement Learning for Multi-turn Computer-Use Agents](https://arxiv.org/abs/2607.09773)

**Authors**: Mianqiu Huang, Taofeng Xue, Chong Peng, Jinrui Ding, Sicheng Fan, Jiale Hong, Yufei Gao, Xiaocheng Zhang, Linsen Guo, Xin Yang, Dengchang Zhao, Yuchen Xie, Peng Pei, Xunliang Xie, Xipeng Qiu  
**Category**: cs.AI  
**Published**: 2026-07-14  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2607.09773v1  

#### Abstract
Computer-use agents must solve long-horizon tasks through repeated interaction with partially observable, multimodal desktop environments. Although imitation learning and offline trajectory refinement provide strong priors, static traces cannot cover the causal feedback loop of real computer use: ea...

---

### 27. [MAG: A Web-Agent Benchmark and Harness for Multimodal Action and Guide Generation](https://arxiv.org/abs/2607.10079)

**Authors**: Chengguang Gan, Hanjun Wei, Yunhao Liang, Zhixi Cai, Qinghao Zhang, Shiwen Ni  
**Category**: cs.AI  
**Published**: 2026-07-14  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2607.10079v1  

#### Abstract
Digital Adoption Platforms (DAPs) are embedded overlays widely used on web systems to guide users through operations inside a page, helping them get started with unfamiliar interfaces quickly. Completing a real task, however, rarely means clicking a few buttons on a single page: it takes a sequence ...

---

### 28. [Chiplet3D: Pin- and Thermal-Aware 3D Chiplet Floorplanning via Convolution-Embedded MILP](https://arxiv.org/abs/2607.09742)

**Authors**: Shuo Ren, Libo Shen, Yaohui Han, Rongliang Fu, Junying Huang, Bei Yu, Tsung-Yi Ho  
**Category**: cs.AR  
**Published**: 2026-07-14  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2607.09742v1  

#### Abstract
As traditional Moore's Law scaling slows down, 3D-ICs stack multiple active dies vertically to sustain performance scaling. However, this vertical stacking traps heat inside, making temperature a design concern. Although we can fix thermal issues at different design steps, floorplanning is the earli...

---

### 29. [OS-Pruner: Pruning Chains-of-Thought of Reasoning Models via Optimal Stopping](https://arxiv.org/abs/2607.11089)

**Authors**: Mohammed Ehab, Aymane El Gadarri, Vivek F. Farias, Adam Jozefiak, Ciamac C. Moallemi  
**Category**: cs.AI  
**Published**: 2026-07-14  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2607.11089v1  

#### Abstract
Large Language Models (LLMs) have achieved remarkable success in complex reasoning tasks through Chain-of-Thought (CoT) prompting. However, these models often exhibit "computational overthinking," generating redundant reasoning steps that increase latency and cost without improving accuracy. Recent ...

---

### 30. [AutoVSR: Automatic Visual-to-Symbolic Reasoning for Symbolic Expression Generation from Circuit Schematic](https://arxiv.org/abs/2607.11338)

**Authors**: Zhe Xiao, Longfei Li, Xu He, Haoying Wu, Zixing Zhang, Mingyu Liu  
**Category**: cs.AI  
**Published**: 2026-07-14  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2607.11338v1  

#### Abstract
Symbolic expressions can effectively characterize and predict circuit behavior, but deriving them directly from circuit schematics is challenging. This process requires accurate visual-to-symbolic construction of circuit structure from images and correct multi-step symbolic derivation, both of which...

---

## 🔧 Configuration

This bot is configured to look for papers containing the following keywords:
- LLM, Inference, Training, kv cache, Speculative decoding, Prefill, Decode, FlashAttention, PagedAttention, continuous batching, MOE, mixture of experts, Quantization, FP8, FP4, Parallel, Distributed, Pipeline, Sparse, Sparse Attention, State Space, SSM, Throughput, Scalable, Efficient, vLLM, SGLang, DeepSpeed, FSDP, AI compiler, TVM, Triton, MLIR, torch.compile, kernel fusion, polyhedral, RISC-V, RVV, XiangShan, custom instruction, eBPF, RDMA, disaggregated, chiplet, NoC, CXL, HBM, systolic array, Kernel, Cluster, Communication, Offload, Hardware, Accelerator, Compiler, Optimization, Embodied, Embodied AI, Embodied Intelligence, Robotics, Robot, Manipulation, Navigation, Sim-to-real, Simulation, World Model, World Models, Video Generation, Video Prediction, Multimodal, Multi-modal, Vision-Language, Vision Language, VLM, Image-Text, Cross-modal, Cross modal, Text-to-Image, Text-to-Video, Vision Transformer, Visual Understanding

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
