# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-07-22 17:49:17 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [What Governs Decode Throughput in Absolute-Offset GPU LZ77? A Work-Granularity Mechanism and an Encode-Time Min-Match-Length Lever](https://arxiv.org/abs/2607.18541v1)

**Authors**: Yakiv Shavidze  
**Category**: cs.DC  
**Published**: 2026-07-22  
**Score**: 76.0  
**Type**: new  
**ArXiv ID**: 2607.18541v1  

#### Abstract
The ACEAPEX line of work established a lossless LZ77 format whose back-references are absolute output positions, giving parallel, compressed-resident GPU decode with sub-millisecond region seek. What it did not establish is what governs the decode throughput of such a format, or how to improve it. T...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：What Governs Decode Throughput in Absolute-Offset GPU LZ77? A Work-Granularity Mechanism and an Encode-Time Min-Match-Length Lever
1. 论文的主要贡献和创新点
✅ 解决的问题
ACEAPEX系列提出的绝对偏移GPU LZ77格式虽实现了并行压缩驻留解码与亚毫秒级区域查找，但未明确该格式解码吞吐量的影响因素，也未提出对应的性能提升方法；真实数据下该格式解码吞吐量较低，压缩效率与吞吐量可能存在潜在权衡。

🚀 提出的新方法与思路
**Work-Granularity解码吞吐量机制**：通过NVIDIA H100上的受控ablation实验，排除occupancy、compute、地址散射、启动并行性等干扰因素，明确绝对偏移GPU LZ77的解码吞吐量由工作粒度（平均匹配长度）决定——较短匹配会导致协作warp的多数lane闲置，进而限制吞吐量。
**Encode-Time Min-Match-Length调节机制**：提出按距离类调整最小匹配长度的encode端杠杆，将最小匹配长度配置从6/8/10/12调整为12/16/24/32，无需修改解码内核，可同时提升压缩比与解码吞吐量。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 解码吞吐量核心影响因素 | 仅由工作粒度（平均匹配长度）决定，无需考虑资源利用率、计算负载等其他因素，优化针对性强 |
| 压缩比与吞吐量的关系 | 无性能权衡，通过移除成本高于熵节省的短距离短匹配，同时实现压缩效率与解码吞吐量的双提升 |
| 落地兼容性 | 属于encode端参数调整，无需改动解码内核，适配性高 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| synthetic copy kernel生成的测试数据 | 验证平均匹配长度对解码吞吐量的影响 |
| enwik9、FASTQ | 真实数据验证最小匹配长度调节机制的效果 |
| 8个测试数据集 | 验证最小匹配长度调节机制的通用性 |

🎯 实验设置与评估指标
任务为测试绝对偏移GPU LZ77的解码吞吐量及压缩比优化效果，实验在NVIDIA H100上开展，评估指标如下：
| 指标 | 含义（箭头） |
| --- | --- |
| 解码吞吐量 | GPU LZ77解码的吞吐能力，单位GB/s，↑越高越好 |
| 平均匹配长度 | LZ77匹配操作的平均匹配长度，单位字节，↑与吞吐量正相关 |
| 压缩比 | 压缩后数据的压缩效率，提升代表压缩效果更好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 原min-match-length配置（6/8/10/12） | Encode端基础参数设置 | 原有基线配置，作为性能对比基准 |
| 新min-match-length配置（12/16/24/32） | 提出的Encode端调节机制 | 按距离类提升最小匹配长度，无需修改解码内核 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**受控消融实验（synthetic copy kernel，NVIDIA H100）**
平均匹配长度从32字节增长至1024字节时，解码吞吐量范围为212 GB/s到744 GB/s，跨度达3.5倍。
💡 结论：解码吞吐量与平均匹配长度正相关，工作粒度是决定解码吞吐量的核心因素，而非occupancy、compute、地址散射或启动并行性；真实数据的平均匹配长度较低（enwik9为6.5字节，FASTQ为10.1字节），因此原解码吞吐量处于较低水平。

**真实数据集实验（enwik9、FASTQ及8个测试数据集）**
| 数据集 | 原解码吞吐量（GB/s） | 新解码吞吐量（GB/s） | 压缩比提升 | 吞吐量提升 |
| --- | --- | --- | --- | --- |
| FASTQ | 142.6 | 178.6 ✅ | 1.8% ✅ | - |
| enwik9 | - | - | - | 78% ✅ |
| 8个测试数据集 | - | 所有数据集均提升 ✅ | 所有数据集均提升 ✅ | 所有数据集均提升 ✅ |
💡 结论：按距离类提升最小匹配长度的机制，在所有测试数据集上均实现了解码吞吐量与压缩比的双提升，且无需修改解码内核，无性能权衡。

其余要求评估的实验：主benchmark性能（L2/碰撞率等）、效率对比（FPS/参数量）、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验其他模块结果均论文未报告。

4. 关键结论和发现
- 主要发现：1. 绝对偏移GPU LZ77的解码吞吐量由工作粒度（平均匹配长度）决定，与occupancy、compute等因素无关；2. Encode端按距离类调整最小匹配长度的机制，可同时提升解码吞吐量与压缩比，无性能权衡；3. 该机制在所有8个测试数据集上均有效，具备通用性。
- 方法局限性：实验scope明确，仅覆盖匹配阶段、设备驻留场景，熵计算与主机传输未纳入计时，查找为读/块级而非坐标级，未声称超过硬件带宽上限；未评估熵和主机传输的性能影响。
- 未来工作：论文未报告
> ✅ **总结一句话**：该论文通过受控消融实验明确了绝对偏移GPU LZ77解码吞吐量的核心决定因素，提出的Encode端最小匹配长度调节机制可在不修改解码内核的前提下，同步提升压缩比与解码吞吐量，且在所有测试数据集上均表现出良好效果。

</details>

---

### 2. [MeetingToM: Evaluating Multimodal LLMs on Theory-of-Mind Reasoning in Multi-Party Meetings](https://arxiv.org/abs/2607.19235v1)

**Authors**: Ziyi Wang, Yuhang Wu, Dongxu Piao, Xingyu Liu, Tianhui Zhou, Miao Liu  
**Category**: cs.CL  
**Published**: 2026-07-22  
**Score**: 74.0  
**Type**: new  
**ArXiv ID**: 2607.19235v1  

#### Abstract
Theory of Mind (ToM), the ability to infer other's beliefs, intentions, and states of knowledge, is central to social interaction, yet remains challenging for current Multimodal Large Language Models (MLLMs), especially in multi-party meetings where cues are distributed across speech and behavior. E...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：MeetingToM: Evaluating Multimodal LLMs on Theory-of-Mind Reasoning in Multi-Party Meetings
1. 论文的主要贡献和创新点
✅ 解决的问题
现存多模态ToM基准主要聚焦于视频上基于显性、可外部验证信号的问答，对潜在社会状态和群体动态的覆盖有限；多party会议场景下的ToM推理对多模态大语言模型（MLLMs）具有挑战性，现有模型在处理跨言语与行为线索方面存在不足，尤其难以区分会议中表面同意掩盖私下异议的伪共识现象。

🚀 提出的新方法与思路
**MeetingToM基准**：构建面向自然多party会议的复杂社会行为推理基准，按社会粒度层级化设计ToM评估框架，包含三个层级的任务：①个体层面心理状态预测；②二元层面听话人理解；③群体层面共识推理；同时提出统一的评估协议。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 覆盖场景类型 | 聚焦自然多party会议场景 |
| 评估粒度 | 支持个体、二元、群体三级社会粒度的ToM评估 |
| 核心现象覆盖 | 包含会议特有的伪共识现象，兼顾潜在社会状态与群体动态 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| MeetingToM | 评估多模态LLM在多party会议场景下的ToM推理能力 |

🎯 实验设置与评估指标
任务为多party会议场景下的ToM推理，涵盖个体心理状态预测、二元听话人理解、群体共识推理三类子任务；论文未报告具体评估指标及对应含义。

⚔️ 基线方法对比
论文未报告基线方法的具体内容。

3. 主要实验结果和性能指标
📊 定量结果汇总
以下实验相关内容论文均未报告：
1. 主 benchmark 性能（L2/碰撞率等）
2. 效率对比（FPS / 参数量）
3. 跨域 / zero-shot 迁移
4. 鲁棒性 / 扰动测试
5. 消融实验

4. 关键结论和发现
- 主要发现：①现有代表性多模态大语言模型（MLLMs）存在整合非言语线索不足、难以推断隐藏态度、无法区分真实共识与伪共识的持续局限性；②MeetingToM可作为推进会议相关多模态模型ToM能力的测试平台。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出面向多party会议场景的ToM推理基准MeetingToM，评估多模态大语言模型在复杂社会行为推理中的能力，揭示现有模型在整合非言语线索等方面的长期局限，为相关研究提供测试平台。

</details>

---

### 3. [Fishing Out Free Riders: Shapley-Based Reward Attribution for Parallel Reasoning via Reinforcement Learning](https://arxiv.org/abs/2607.18979v1)

**Authors**: Wentao Zhang, Haoyu Zhang, Xinke Jiang, Yuxuan Cheng, Yuhan Pan, Miao Li, Zhipeng Qiao, Tao Feng, Zhen Tao, Dengji Zhao  
**Category**: cs.AI  
**Published**: 2026-07-22  
**Score**: 64.5  
**Type**: new  
**ArXiv ID**: 2607.18979v1  

#### Abstract
Large Language Models (LLMs) excel at multi-step reasoning, yet current parallel reasoning approaches often fail to distinguish the contributions of individual reasoning paths. Many paths may be redundant, misleading, or even detrimental, but outcome-level rewards assign uniform reward, leading to a...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Fishing Out Free Riders: Shapley-Based Reward Attribution for Parallel Reasoning via Reinforcement Learning

1. 论文的主要贡献和创新点
✅ 解决的问题
现有大语言模型的并行推理方法存在以下核心痛点：
1. 无法区分多路径推理中各推理路径的贡献；
2. 难以识别多路径推理中冗余、误导或有害的路径；
3. 采用输出级统一奖励分配方式，导致学习信号模糊，训练不稳定。

🚀 提出的新方法与思路
**Parallel Shapley**：该方法是基于强化学习的框架，将每条推理路径视为合作博弈中的独立玩家，通过Shapley值量化各路径的边际贡献；引入生成奖励模型评估每条路径的效用，结合蒙特卡洛采样实现Shapley值的高效近似，从而实现细粒度的路径级贡献归因。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 奖励分配精度 | 实现细粒度的路径级贡献归因，可有效识别并行推理中的自由骑手，按比例分配奖励 |
| 训练稳定性 | 提供清晰的路径学习信号，改善现有并行推理方法训练不稳定的问题 |
| 推理性能 | 在数学推理基准上优于现有并行推理基线方法 |
| 可解释性 | 可量化各推理路径的贡献，提升推理过程的可解释性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 数学推理基准 | 评估Parallel Shapley框架的并行推理性能 |

🎯 实验设置与评估指标
实验任务为大语言模型的多路径数学推理任务；论文未报告具体使用的评估指标名称。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 现有并行推理基线方法 | 并行推理方法 | 采用统一输出级奖励分配，未区分各推理路径的贡献 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体实验结果对应的表号、图号及数值，仅提及Parallel Shapley在数学推理基准上的表现优于现有基线方法。
以下实验论文未报告：
1. 主 benchmark 性能
2. 效率对比（FPS / 参数量）
3. 跨域 / zero-shot 迁移
4. 鲁棒性 / 扰动测试
5. 消融实验

4. 关键结论和发现
- 主要发现：
  1. Parallel Shapley框架通过Shapley值实现了并行推理中细粒度的路径级贡献归因，能够有效识别并处理并行推理中的自由骑手，实现按比例分配奖励；
  2. 该框架在数学推理基准上相比现有并行推理基线方法，推理性能更优且训练过程更稳定；
  3. 结合生成奖励模型与蒙特卡洛采样的Shapley值近似方案，可高效完成多路径推理中的贡献量化。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出的Parallel Shapley框架，将Shapley值与强化学习结合，解决了大语言模型并行推理中路径贡献分配模糊、训练不稳定的问题，实现了按比例奖励分配，提升了多路径数学推理的性能与可解释性。

</details>

---

### 4. [MAGE: Human-Like Macro Placement via Agentic Multimodal Reasoning](https://arxiv.org/abs/2607.18536v1)

**Authors**: Andrew B. Kahng, Sayak Kundu, Bodhisatta Pramanik  
**Category**: cs.AI  
**Published**: 2026-07-22  
**Score**: 62.5  
**Type**: new  
**ArXiv ID**: 2607.18536v1  

#### Abstract
Macro placement still requires substantial manual refinement in industrial physical design flows. We present MAGE (Macro Placement Agentic Engine), a multimodal multi-agent framework for macro placement refinement. MAGE decomposes the macro placement task into a six-phase workflow that combines stru...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

MAGE: Human-Like Macro Placement via Agentic Multimodal Reasoning
1. 论文的主要贡献和创新点
解决的问题
宏布局在工业物理设计流程中仍需大量人工优化；现有方法多从标注数据中学习专家知识，难以结合结构规则、视觉特性优化布局，且无法保障布局符合人类专家的结构习惯，同时现有商用及基线方法在时序性能、人类似性及跨场景泛化上存在不足。

🚀 提出的新方法与思路
**Six-Phase Agentic Workflow**：构建包含六个阶段的宏布局工作流，结合结构化布局规则、视觉检查与迭代优化，通过自然语言指令和验证标准编码专家知识，无需依赖标注布局数据。
**Tournament-style Refinement Mode**：采用锦标赛式优化模式，同步评估多个候选布局方案，将高质量方案的反馈传播给后续优化过程，提升布局全局质量。
**Human-Like Layout Metrics**：设计四个专属指标（notch score、whitespace score、pocket score、alignment score），用于捕捉专家布局关注的结构特性，弥补传统PPA指标的不足。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 专家知识编码 | 通过自然语言指令和验证标准编码专家知识，无需依赖标注布局数据 |
| 人类似性评估 | 提出四个结构专属指标，可有效衡量布局符合人类专家习惯的程度 |
| 时序性能 | 在WNS、TNS上优于商用宏布局器、人类专家及Hier-RTLMP基线 |
| 泛化能力 | 无需设计特定重训即可应用于新布局场景（如未见设计、匿名网表等） |
| 布局特性 | 线长和功耗与基线相当，兼顾性能与功耗指标 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| NanGate45 | 评估该工艺节点下的宏布局性能及基线对比 |
| GlobalFoundries 12nm | 评估该工艺节点下的宏布局性能 |
| 匿名网表、未见设计等 | 评估跨场景泛化能力 |

🎯 实验设置与评估指标
任务：宏布局优化，提升时序性能及人类似性。
| 指标 | 含义（箭头方向） |
|------|------------------|
| WNS | 负 slack 均值，↓越低越好，衡量时序性能 |
| TNS | 负 slack 总和，↓越低越好，衡量时序性能 |
| notch score | 衡量布局缺口特性，捕捉专家关注的结构，↑越高越好 |
| whitespace score | 衡量布局留白特性，捕捉专家关注的结构，↑越高越好 |
| pocket score | 衡量布局口袋状空间特性，捕捉专家关注的结构，↑越高越好 |
| alignment score | 衡量布局对齐特性，捕捉专家关注的结构，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 商用宏布局器 | 工业基线 | 工业领域常用自动化宏布局方案 |
| 人类专家 | 专业基线 | 人工优化的专业宏布局方案 |
| Hier-RTLMP | 学术基线 | 层级式RTL驱动的宏布局基线方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
- **主 benchmark 性能（场景：NanGate45、GlobalFoundries 12nm的九个设计；NanGate45的三个设计）**
论文摘要提及MAGE在对应设计上实现优于基线的时序性能，但论文未报告具体数值及对应表号，无法定位来源。
💡 结论：MAGE在时序性能上优于商用宏布局器、人类专家及Hier-RTLMP基线。

- **跨域 / zero-shot 迁移**
论文提及MAGE在匿名网表、未见设计等额外案例中表现良好，无需设计特定重训即可应用，论文未报告具体表号。
💡 结论：MAGE具有良好的跨场景泛化能力。

其他实验项说明：效率对比（FPS / 参数量）、鲁棒性 / 扰动测试、消融实验，论文未报告。

4. 关键结论和发现
- 主要发现
1. MAGE通过编码自然语言专家知识并结合多模态推理，时序性能优于商用宏布局器及学术基线方法，且线长和功耗与基线相当。
2. MAGE提出的四个人类似性指标可有效捕捉专家布局的结构特性，整体人类似性得分优于所有对比基线。
3. MAGE无需针对设计进行特定重训，即可在未见设计、匿名网表等新布局场景中有效应用。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：MAGE是一种代理式多模态宏布局框架，通过结合自然语言专家知识、多模态推理与迭代优化，在时序性能、人类似性及跨场景泛化上均优于现有基线方法，且无需设计特定重训。

</details>

---

### 5. [Stochastic Meta-Unlearning: Bridging Language Backbone and Multimodal Unlearning](https://arxiv.org/abs/2607.18615v1)

**Authors**: Zijie Liu, Jinhao Duan, Gaowen Liu, Sijia Liu, Tianlong Chen  
**Category**: cs.CL  
**Published**: 2026-07-22  
**Score**: 53.5  
**Type**: new  
**ArXiv ID**: 2607.18615v1  

#### Abstract
Machine unlearning for vision-language models (VLMs) remains underexplored. Unlike language models, VLMs combine a language backbone with visual components, which makes unlearning more complex. There is a surprising phenomenon when moving from single-modality unlearning to VLM unlearning: a target f...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Stochastic Meta-Unlearning: Bridging Language Backbone and Multimodal Unlearning
1. 论文的主要贡献和创新点
✅ 解决的问题
- 机器unlearning在视觉语言模型（VLMs）中探索不足，VLMs因结合语言骨干与视觉组件，unlearning复杂度远高于单模态模型。
- 单模态unlearning与VLM unlearning存在关键差异：仅对独立语言骨干完成遗忘后，给完整VLM补充图像信息，目标内容仍可被恢复，说明纯文本反馈无法实现可靠的VLM unlearning。
- 现有方法缺陷：未适配VLM的多模态特性，未结合VLM层面的反馈，导致遗忘不可靠、迁移性差。

🚀 提出的新方法与思路
**Stochastic Meta-Unlearning (SMU)**：双层bilevel框架，内层循环使用文本数据对语言骨干执行少量unlearning步骤；外层循环将更新后的语言骨干与冻结的VLM重组，在VLM层面评估遗忘效果与效用，使unlearning更新关注最终多模态行为，同时将更新范围局限于语言骨干。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 遗忘-保留权衡 | 达到最佳整体遗忘-保留性能 |
| 遗忘效果 | 降低平均Forget accuracy |
| 保留效果 | 提升平均Retain accuracy |
| 整体性能 | 提升平均Test accuracy |
| 迁移性 | 可迁移至新遗忘目标与不同元测试unlearning方法 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 两种多模态meme数据集 | 用于SMU方法的实验评估 |

🎯 实验设置与评估指标
任务为VLM层面的unlearning任务，核心评估指标如下：
| 指标 | 含义及方向 |
| --- | --- |
| Forget accuracy | 衡量遗忘效果，值越低越好（↓） |
| Retain accuracy | 衡量保留未遗忘内容的效果，值越高越好（↑） |
| Test accuracy | 衡量模型整体性能，值越高越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 3个基线方法 | 未明确具体类型 | 与SMU进行性能对比的参考方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表N：主benchmark性能（VLM unlearning任务）**
论文未报告具体表号，无法提供对应定量数值。

以下实验论文未报告：
1. 效率对比（FPS / 参数量）
2. 跨域 / zero-shot 迁移（仅摘要提及迁移性，无具体实验结果）
3. 鲁棒性 / 扰动测试
4. 消融实验

4. 关键结论和发现
- 核心发现1：VLM的unlearning存在单模态模型未有的特殊问题，纯文本层面的遗忘可通过补充图像信息恢复，需依赖VLM层面的多模态反馈。
- 核心发现2：提出的SMU双层框架兼顾语言骨干的局部更新与VLM层面的全局评估，实现了更优的遗忘-保留权衡。
- 核心发现3：SMU具备良好的跨场景迁移能力，可适配新的遗忘目标与不同的元测试unlearning方法。

- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：SMU框架通过结合VLM层面的多模态反馈优化语言骨干的unlearning过程，实现了VLMs更可靠、可迁移的遗忘性能。

</details>

---

### 6. [S3: Stable Subgoal Selection by Constraining Uncertainty of Coarse Dynamics in Hierarchical Reinforcement Learning](https://arxiv.org/abs/2607.19232v1)

**Authors**: Kshitij Kumar Srivastava, Kshitij Jerath  
**Category**: cs.LG  
**Published**: 2026-07-22  
**Score**: 53.5  
**Type**: new  
**ArXiv ID**: 2607.19232v1  

#### Abstract
Hierarchical Reinforcement Learning (HRL) intends to separate strategic planning from primitive execution. It has been widely successful in solving long-horizon and complex tasks, where flat-RL algorithms have difficulty in learning. However, while the low-level agent in HRL benefits from dense feed...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：S3: Stable Subgoal Selection by Constraining Uncertainty of Coarse Dynamics in Hierarchical Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
分层强化学习（HRL）中，高层智能体接收稀疏、延迟的环境反馈，性能依赖低层执行能力；现有基于原始转移动力学的高层动机方法需覆盖宽状态-动作空间，导致高层子目标选择策略稳定性不足。

🚀 提出的新方法与思路
**S3方法**：通过最小化与粗粒度动力学（高层时间尺度下聚合多步环境转移）相关的预测不确定性稳定高层策略，采用混合密度网络（MDN）建模该预测不确定性，设计基于粗粒度动力学的密集内在奖励，实现风险厌恶的子目标选择。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 高层策略稳定性 | 通过最小化粗粒度动力学预测不确定性实现稳定子目标选择 |
| 非平稳长horizon环境适应性 | 在非平稳长horizon环境中表现优于现有SOTA HRL方法 |
| 反馈效率 | 提供密集的动力学感知内在奖励，缓解高层反馈稀疏问题 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务：论文未报告具体任务
| 指标 | 含义 |
| --- | --- |
| 论文未报告 | 论文未报告 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 现有SOTA HRL方法 | 基准对比方法 | 论文未报告具体名称 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未明确包含带表号、图号等定位来源的定量数据，仅提及定性结论：在非平稳长horizon环境中优于现有SOTA HRL方法。
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1）基于粗粒度动力学预测不确定性的内在奖励可实现风险厌恶的子目标选择，稳定HRL高层策略；2）S3方法在非平稳长horizon环境中性能优于现有SOTA HRL方法。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：S3方法通过混合密度网络建模粗粒度动力学的预测不确定性，设计密集动力学感知内在奖励实现稳定的风险厌恶子目标选择，在非平稳长horizon环境中表现优于现有SOTA分层强化学习方法。

</details>

---

### 7. [CASE: Causal Alignment and Structural Enforcement for Improving Chain-of-Thought Faithfulness](https://arxiv.org/abs/2607.18820v1)

**Authors**: Ziming Wang, Yinghua Yao, Changwu Huang, Ke Tang, Xin Yao  
**Category**: cs.CL  
**Published**: 2026-07-22  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2607.18820v1  

#### Abstract
Chain-of-thought (CoT) reasoning is widely used to improve both the performance and interpretability of large language models (LLMs), yet the generated reasoning may not faithfully support the final answer. We study this problem from a causal perspective, where a faithful CoT process should follow t...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

CASE: Causal Alignment and Structural Enforcement for Improving Chain-of-Thought Faithfulness
1. 论文的主要贡献和创新点
✅ 解决的问题
Chain-of-thought (CoT)推理虽广泛用于提升大型语言模型（LLMs）的性能和可解释性，但生成的推理链可能无法忠实地支撑最终答案；从因果视角，忠实CoT应遵循指令→推理链→最终答案（$Z\rightarrow X\rightarrow Y$）的路径，但常规自回归LLM生成答案时同时依赖指令和CoT，存在指令到答案的直接捷径问题。

🚀 提出的新方法与思路
**训练时因果对齐**：构建反事实-CoT、偏差-指令、空-指令三类数据集，通过选择性损失微调强化CoT到答案的依赖关系，同时抑制指令到答案的直接捷径。
**推理时结构强制**：屏蔽指令令牌到答案令牌的直接注意力，防止模型绕过生成的CoT推理链。
此外，提供信息论分析说明上述组件如何促进忠实CoT链的生成。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| CoT忠诚信度 | 相比最强基线，平均达到37%的相对提升 |
| 跨数据集忠诚信度迁移能力 | 表现更强 |
| 平均准确率 | 保持有竞争力的水平 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 四个基准数据集 | 用于评估CASE框架的CoT忠诚信度及相关性能指标 |

🎯 实验设置与评估指标
任务：评估LLM生成的CoT推理链对最终答案的忠实性，以及模型的平均准确率。
| 指标 | 含义 |
| --- | --- |
| CoT忠诚信度 | 衡量生成推理链对最终答案的忠实性，数值越高越好（↑） |
| 平均准确率 | 模型整体预测的准确性，数值越高越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 最强基线 | 对比方法 | 常规CoT推理框架，未抑制指令到答案的直接捷径 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告具体表号，仅说明CASE相比最强基线，在CoT忠诚信度上达到平均37%的相对提升；💡 结论：CASE可显著提升基准数据集上的CoT忠诚信度。
2. 效率对比：论文未报告。
3. 跨域/zero-shot迁移：论文未报告具体表号，仅说明CASE具备更强的跨数据集忠诚信度迁移能力；💡 结论：CASE的CoT忠诚信度可更好地跨数据集迁移。
4. 鲁棒性/扰动测试：论文未报告。
5. 消融实验：论文未报告具体模块的消融分析及对应表号。

4. 关键结论和发现
- 主要发现：1. CASE通过训练时因果对齐与推理时结构强制，有效提升了LLM的CoT忠诚信度；2. CASE在提升CoT忠实性的同时，保持了模型的平均准确率；3. CASE具备比现有常规CoT框架更强的跨数据集忠诚信度迁移能力。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：CASE是结合训练时因果对齐与推理时结构强制的框架，在提升CoT忠诚信度、抑制指令到答案直接捷径的同时，保持模型平均准确率，且具备更强的跨数据集迁移能力。

</details>

---

### 8. [Reasoning Error from Known Fact: Step-Level Self-Consistency Group Relative Policy Optimization for LLM](https://arxiv.org/abs/2607.18915v1)

**Authors**: Xiaomeng Hu, Jiaqi Hu, Hao Chen, Qi Zhang, Zhanming Shen, Wentao Ye, Junbo Zhao  
**Category**: cs.CL  
**Published**: 2026-07-22  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2607.18915v1  

#### Abstract
With the rapid advancement of large language models (LLMs), modern systems not only possess strong foundational capabilities and extensive knowledge, but can also solve complex problems via long, multi-step reasoning. However, as reasoning traces become longer, LLMs may produce a substantial amount ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Reasoning Error from Known Fact: Step-Level Self-Consistency Group Relative Policy Optimization for LLM
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾为LLM在多步推理过程中易产生大量难以检测的幻觉，其中上下文敏感事实幻觉尤为突出：模型本身具备相关知识，但因推理过程中的上下文干扰导致事实错误；现有方法未针对性解决该类幻觉问题。

🚀 提出的新方法与思路
**Step-level Self-Consistency Group Relative Policy Optimization（SSC-GRPO）**，该方法通过计算多个rollout中单个步骤的自一致性分数，为推理轨迹分配步骤级奖励，以此缓解推理过程中的上下文敏感事实幻觉。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 数学推理任务性能 | 在数学推理基准上达到SOTA性能 |
| 幻觉抑制性能 | 在幻觉排行榜上达到SOTA性能 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 数学推理基准数据集 | 用于数学推理任务的性能验证 |
| 幻觉排行榜数据集 | 用于幻觉抑制任务的性能验证 |

🎯 实验设置与评估指标
论文未报告

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 现有方法（Prior Methods） | 对比基准 | 用于与SSC-GRPO的性能对比 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体定量结果及对应表格

4. 关键结论和发现
- 主要发现
  1. LLM多步推理中的上下文敏感事实幻觉的成因是模型自身具备相关知识，却受推理上下文干扰出现事实错误，而非完全缺失对应知识；
  2. SSC-GRPO通过步骤级自一致性奖励机制可有效缓解上述上下文敏感事实幻觉；
  3. SSC-GRPO在数学推理基准和幻觉排行榜上的性能优于现有方法，达到SOTA。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文针对LLM多步推理中因上下文干扰导致的、模型本身具备知识却仍出现事实错误的上下文敏感事实幻觉问题，提出SSC-GRPO方法，通过步骤级自一致性奖励实现幻觉缓解，在数学推理和幻觉抑制任务上达到SOTA性能。

</details>

---

### 9. [S2T-RLHF: Hierarchical Credit Assignment for Stable Preference-Based RLHF](https://arxiv.org/abs/2607.18258v1)

**Authors**: Wei Chen, Guanghui Zhu, Yafei Li, Limin Wang, Yihua Huang  
**Category**: cs.AI  
**Published**: 2026-07-22  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2607.18258v1  

#### Abstract
Reinforcement learning from human feedback (RLHF) with preference-based reward models often exhibits unstable training dynamics. A key contributing factor is that standard RLHF relies on a single sequence-level scalar reward, which is propagated to token-level policy updates and leaves credit assign...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

S2T-RLHF: Hierarchical Credit Assignment for Stable Preference-Based RLHF
1. 论文的主要贡献和创新点
✅ 解决的问题
1. 标准Preference-Based RLHF依赖单序列级标量奖励，Token层面的信用分配模糊。
2. 近期将奖励细化至Token级的方法，因偏好信号仅定义在响应级且含噪声，过细的奖励细化会放大奖励不确定性，导致训练不稳定。

🚀 提出的新方法与思路
**S2T-RLHF**：提出granularity-aware的分层信用分配原则，以句子作为中间粒度平衡语义一致性与对Token级噪声的鲁棒性；该sentence-to-token奖励分解框架，先将序列级偏好奖励分配到句子层面，再在每个句子内应用受限的Token级细化，无需重新训练奖励模型或Token级监督。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
训练稳定性 | 相比标准RLHF和Token级细化方法，提升了训练稳定性
鲁棒性 | 对Token级奖励噪声的鲁棒性更强
偏好对齐性能 | 保持了与现有方法有竞争力的偏好对齐表现

2. 核心实验方法和设置
📚 使用的数据集
论文未报告具体数据集名称，仅提及在多个数据集上开展实验

🎯 实验设置与评估指标
任务为偏好-based的强化学习人类反馈（RLHF）相关任务；论文未报告具体评估指标名称，仅提及评估训练稳定性、鲁棒性和偏好对齐

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
标准RLHF | 基准方法 | 采用单序列级标量奖励，信用分配模糊
近期Token级细化RLHF方法 | 对比方法 | 依赖Token级奖励细化，易受偏好信号噪声影响

3. 主要实验结果和性能指标
论文未报告具体定量数值、表号、图号或章节信息，仅提及实验整体效果满足预期。

4. 关键结论和发现
- 主要发现：
  1. 当偏好信号仅定义在响应级且存在噪声时，过度细化至Token级的奖励分配会放大奖励不确定性，加剧训练不稳定。
  2. 以句子作为中间粒度的信用分配，可平衡语义一致性与对Token级噪声的鲁棒性。
  3. S2T-RLHF无需奖励模型重训或Token级监督，即可提升训练稳定性与鲁棒性，同时保持竞争的偏好对齐性能。
- 方法局限性：论文未明确提及方法局限性。
- 未来工作：论文未报告未来工作相关内容。

> ✅ **总结一句话**：S2T-RLHF通过提出granularity-aware的分层信用分配原则，以句子作为中间粒度实现sentence-to-token奖励分解，有效解决了偏好-based RLHF中因奖励细化过度导致的训练不稳定问题，提升了训练稳定性、鲁棒性且保持了竞争力的偏好对齐表现。

</details>

---

### 10. [Comparative Study of Multi-Agent Actor-Critic Algorithms in Parameterized Action Reinforcement Learning](https://arxiv.org/abs/2607.19117v1)

**Authors**: Ubayd Ali Bapoo, Clement N Nyirenda  
**Category**: cs.AI  
**Published**: 2026-07-22  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2607.19117v1  

#### Abstract
Parameterized action reinforcement learning has shown strong performance in environments requiring both discrete action selection and continuous parameterization. Prior work established the effectiveness of single-agent actor-critic algorithms - Greedy Actor-Critic (GAC), Soft Actor-Critic (SAC), an...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

### 论文标题：Comparative Study of Multi-Agent Actor-Critic Algorithms in Parameterized Action Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
参数化动作强化学习中，单智能体Actor-Critic算法（GAC、SAC、TQC）的有效性已被验证，但其多智能体扩展研究极为匮乏；现有多智能体Actor-Critic方法多遵循集中式训练分布式执行（CTDE）范式，相关多智能体算法设计思路的多样性不足。

🚀 提出的新方法与思路
**共享经验多智能体Actor-Critic框架**：该框架摒弃CTDE范式，采用多个独立的Actor-Critic智能体构建，智能体间共享重播缓冲区（replay buffer），同时各自维护独立的策略和价值网络；基于该框架，将单智能体的GAC、SAC、TQC分别扩展为多智能体算法MAGAC、MASAC、MATQC。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 多智能体扩展思路 | 提供非CTDE范式下的共享经验多智能体Actor-Critic设计路径，填补了参数化动作强化学习的多智能体方法研究空白 |
| 性能表现 | 可持续提升GAC的多智能体性能，对MASAC、MATQC也实现了适度的性能增益 |
| 可扩展性分析 | 量化了智能体数量对算法性能与计算成本的权衡关系，明确了智能体数量过多时的效率问题 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Platform-v0 | 评估多智能体Actor-Critic算法在参数化动作强化学习中的性能与效率 |
| Goal-v0 | 评估多智能体Actor-Critic算法在参数化动作强化学习中的性能与效率 |

🎯 实验设置与评估指标
实验任务为参数化动作强化学习，设置3、5、10智能体的多智能体配置，每个配置下运行10次独立实验；评估指标如下：
| 指标 | 含义 |
| --- | --- |
| 平均评估回报 | 衡量算法性能，越高越好 |
| 训练时间 | 衡量计算效率，越低越好 |
| one-way ANOVA、Tukey HSD post-hoc tests | 用于评估实验结果的统计显著性 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| MAGAC | 多智能体算法 | 由单智能体GAC扩展而来，采用共享重播缓冲区的独立智能体设计 |
| MASAC | 多智能体算法 | 由单智能体SAC扩展而来，采用共享重播缓冲区的独立智能体设计 |
| MATQC | 多智能体算法 | 由单智能体TQC扩展而来，采用共享重播缓冲区的独立智能体设计 |
| GAC | 单智能体基线算法 | 用于参数化动作强化学习的单智能体Actor-Critic算法 |
| SAC | 单智能体基线算法 | 用于参数化动作强化学习的单智能体Actor-Critic算法 |
| TQC | 单智能体基线算法 | 用于参数化动作强化学习的单智能体Actor-Critic算法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告具体的主基准任务（Platform-v0、Goal-v0）的性能数值及对应表号
2. 效率对比（FPS / 参数量）：论文未报告具体的效率指标数值
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. 提出的共享经验多智能体框架可持续提升GAC的多智能体性能，对MASAC、MATQC的性能提升相对有限；2. 当智能体数量超过5时，算法额外性能增益有限，但计算成本大幅上升，尤其MAGAC的计算成本受智能体数量影响最显著；3. 该多智能体框架在参数化动作强化学习中存在性能与计算效率的权衡关系，智能体数量需平衡两者需求。
- 方法局限性：论文仅在Platform-v0、Goal-v0两个基准任务上评估算法，未验证其他参数化动作强化学习环境的适用性；未开展效率对比、跨域迁移、鲁棒性测试及消融实验；未对比该框架与CTDE范式多智能体算法的性能差异。
- 未来工作：探索该共享经验多智能体框架在更多参数化动作强化学习环境中的表现；对比该框架与CTDE范式多智能体算法的性能与效率；研究其他多智能体Actor-Critic算法在参数化动作强化学习场景中的适配性。

> ✅ **总结一句话**：该论文针对参数化动作强化学习的多智能体扩展问题，提出非CTDE范式下共享经验的独立智能体Actor-Critic算法，通过实验明确了算法性能与计算效率的权衡关系，为该领域多智能体方法研究提供了参考方向。

</details>

---

### 11. [Graph Neural Network-based Algorithm Selection for the Traveling Salesman Problem: A Systematic Study of Cost and Rank Losses under Distinct Budget Regimes](https://arxiv.org/abs/2607.18632v1)

**Authors**: Zhaoxuan Li, Jiale Yang, Yifei Lu, Mustafa Misir  
**Category**: cs.LG  
**Published**: 2026-07-22  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2607.18632v1  

#### Abstract
Automated Algorithm Selection (AS) aims to improve problem-solving performance by selecting, for each problem instance, the most suitable algorithm from a predefined portfolio. This is particularly relevant to the Traveling Salesman Problem (TSP), where solver performance is strongly instance-depend...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Graph Neural Network-based Algorithm Selection for the Traveling Salesman Problem: A Systematic Study of Cost and Rank Losses under Distinct Budget Regimes
1. 论文的主要贡献和创新点
✅ 解决的问题
针对旅行商问题（TSP）这类求解器性能随实例具有强依赖性的场景，现有自动算法选择（AS）方法多依赖手动特征工程，存在额外开销或表示质量受限的痛点，缺乏直接从原始图数据学习实例表示的图神经网络（GNN）驱动的AS框架。

🚀 提出的新方法与思路
**GNNAS-TSP**：该框架是基于GNN的TSP专用自动算法选择框架，核心创新为：将TSP的AS任务转化为联合成本预测与排序任务；无需手动特征工程，直接从TSP原始图数据学习实例的结构化表示；针对包含Chained Lin-Kernighan、Edge Assembly Crossover、Lin-Kernighan-Helsgaun、Multiagent Optimization System、Concorde的求解器 portfolio，系统评估了三类学习目标的性能，包括基于损失的均方误差（MSE）、平均绝对误差（MAE）、Huber损失，基于排序的RankNet、ListNet、LambdaRank损失，以及混合学习目标；实验设置固定计算预算为10秒与60秒。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 特征工程依赖 | 无需手动特征工程，直接从TSP原始图数据学习实例表示，降低特征工程成本与人工依赖 |
| 任务适配性 | 将TSP的AS任务建模为联合成本预测与排序任务，可适配不同类型的学习目标（基于损失、排序损失、混合损失） |
| 性能表现 | 在held-out测试集的固定计算预算下，所选算法配置的归一化解成本优于Single Best Solver，10秒预算下的成本提升具统计显著性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务：针对TSP问题，基于GNNAS-TSP框架，在10秒、60秒两种固定计算预算下，从给定求解器 portfolio中为每个实例选择最优算法，评估所选算法配置的归一化求解成本；
指标：
| 指标 | 含义（箭头标方向） |
| --- | --- |
| 归一化解成本 | ↓，值越低代表求解性能越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Single Best Solver（SBS） | 基线求解策略 | 为每个TSP实例选择预定义性能最优的单一求解器作为对比基线 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能（L2/碰撞率等）：论文未报告；
2. 效率对比（FPS / 参数量）：论文未报告；
3. 跨域 / zero-shot 迁移：论文未报告；
4. 鲁棒性 / 扰动测试：论文未报告；
5. 消融实验：论文未报告；
💡 结论：论文在held-out测试集的10秒、60秒固定计算预算下，GNNAS-TSP框架所选算法配置的归一化解成本均优于Single Best Solver；10秒预算下，该成本提升具统计学显著性。

4. 关键结论和发现
- 主要发现：
  1. GNNAS-TSP是针对TSP的有效GNN-based自动算法选择框架，无需手动特征工程，直接从原始图数据学习实例表示；
  2. 在10秒、60秒两种固定计算预算下，GNNAS-TSP所选算法配置的归一化解成本均优于Single Best Solver；
  3. 10秒预算下，GNNAS-TSP相比Single Best Solver的成本提升具有统计显著性，适用于求解器性能存在可利用差异的元求解场景。
- 方法局限性：论文未报告；
- 未来工作：论文未报告；
✅ **总结一句话**：该研究提出了GNNAS-TSP框架，将TSP的自动算法选择建模为联合成本预测与排序任务，直接从原始图数据学习实例表示，在10秒和60秒固定计算预算下均实现了优于Single Best Solver的求解性能，10秒预算下的提升具统计显著性，是适用于TSP的有效元求解策略。

</details>

---

### 12. [Real-time optimal control with shallow recurrent decoder networks](https://arxiv.org/abs/2607.19302v1)

**Authors**: Matteo Tomasetto, Francesco Braghin, J. Nathan Kutz, Andrea Manzoni  
**Category**: cs.LG  
**Published**: 2026-07-22  
**Score**: 35.5  
**Type**: new  
**ArXiv ID**: 2607.19302v1  

#### Abstract
Controlling dynamical systems in real-time across multiple scenarios is critical to enabling adaptive control strategies, ensuring stability and efficiency. However, to tailor control actions in response to varying scenarios, traditional optimal control problems typically require several system simu...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Real-time optimal control with shallow recurrent decoder networks
1. 论文的主要贡献和创新点
✅ 解决的问题
实时控制高维动态系统以适配多场景是自适应控制策略的关键，但传统最优控制需多次系统仿真，因高维时空动态导致计算量巨大，存在维度灾难问题，难以满足实时控制需求。
现有方法的缺陷：传统最优控制的计算成本过高，无法适配高维动态的多场景实时控制。

🚀 提出的新方法与思路
**SHRED-ROM**：基于Shallow Recurrent Decoder networks的降阶建模方法，仅用少量专家提供的最优示例训练，合成针对高维参数化动态的实时闭环控制器，缓解维度灾难问题，可在新场景下生成有效的分布控制动作。
**传感器预测器**：用于在隐层层面实现闭环，有效缓解传感器故障或延迟问题。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 计算效率 | 缓解高维动态的维度灾难，实现实时控制 |
| 场景适配 | 支持高维参数化动态的多场景自适应控制，仅依赖有限状态传感器读数 |
| 鲁棒性 | 通过传感器预测器实现隐层闭环，缓解传感器故障或延迟问题 |

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
论文未报告 | 论文未报告

🎯 实验设置与评估指标
任务为针对参数密度控制或流体流动控制的三个高维案例进行最优控制性能评估，具体指标及含义论文未报告

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
论文未报告 | 论文未报告 | 论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：基于SHRED-ROM的方法可模仿专家最优控制行为，在新场景下生成有效分布控制动作；结合传感器预测器可实现隐层闭环，缓解传感器故障或延迟问题。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出基于SHRED-ROM和传感器预测器的实时最优控制方法，可应对高维参数化动态的多场景控制需求，缓解维度灾难与传感器相关问题，实现高效的实时控制。

</details>

---

### 13. [Search-on-Graph-R1: Training Large Language Models to Search Knowledge Graphs with Reinforcement Learning](https://arxiv.org/abs/2607.18481v1)

**Authors**: Jia Ao Sun, Hao Yu, Fengran Mo, Zhan Su, Yuchen Hui, Bang Liu, Jian-Yun Nie  
**Category**: cs.CL  
**Published**: 2026-07-22  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2607.18481v1  

#### Abstract
Knowledge graph question answering (KGQA) requires navigating from topic entities to an answer several relations away. Recent methods prompt a frontier LLM to explore the graph through a retrieval tool, but their reliance on frontier-scale inference makes them costly to deploy. We present Search-on-...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Search-on-Graph-R1: Training Large Language Models to Search Knowledge Graphs with Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题：现有知识图谱问答（KGQA）方法依赖前沿规模的大语言模型（LLM）进行推理，部署成本高昂，需探索图谱路径以找到答案，存在大模型推理成本高与路径导航效率不足的核心痛点。
（现有方法的缺陷：① 依赖前沿规模LLM，部署成本高；② 需自行探索知识图谱路径，路径发现难度大）
🚀 提出的新方法与思路
**Search-on-Graph-R1（SogR1）**：采用8B紧凑规模的LLM，依次通过监督微调（SFT）、强化学习（RL）完成训练，将知识图谱导航能力内化为模型本身。核心思路是为每个问题的黄金SPARQL查询搭建脚手架，让前沿教师模型使用实时的Search工具遍历已知的答案所在图谱路径，无需自行发现路径；所有Search调用均指向实时Freebase服务器，生成的轨迹天然基于知识图谱结构。
🔍 相比现有方法的优势
维度 | 优势
--- | ---
模型规模 | 采用8B紧凑模型，部署成本远低于前沿规模LLM
性能表现 | 8B版本在WebQSP、CWQ、GrailQA基准上，超越所有对比的冻结前沿LLM系统，CWQ任务为对比系统中表现最强
训练与推理方式 | 推理阶段无需辅助模块，训练阶段无需LLM裁判
训练增益 | SFT与RL对性能提升呈互补作用
迁移性 | 方法可跨模型家族迁移
导航效率 | 经RL训练后的模型，相比SFT初始版本，到达答案所需的Search调用更少

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
WebQSP | KGQA主benchmark性能评估
CWQ | KGQA主benchmark性能评估
GrailQA | KGQA主benchmark性能评估
🎯 实验设置与评估指标
任务为知识图谱问答（KGQA），需从主题实体出发，通过多跳关系导航找到答案。评估指标：论文未报告具体指标名称，仅说明性能的相对比较结果。
⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
冻结前沿LLM的KGQA系统 | KGQA方法 | 依赖前沿规模LLM推理，部署成本高

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告具体数值及对应图表号，仅说明SogR1 8B版本在WebQSP、CWQ、GrailQA上超越所有对比的冻结前沿LLM系统，CWQ任务为对比系统中表现最强的系统。
💡 结论：SogR1的8B紧凑KGQA模型在多个主流KGQA基准上的性能优于所有对比的冻结前沿LLM系统，CWQ任务表现最优。
2. 效率对比：论文未报告FPS、参数量等具体效率数值，仅提及SogR1为8B模型，部署成本低于前沿规模LLM，且RL训练后模型的Search调用数更少。
3. 跨域/zero-shot迁移：论文未报告具体测试结果，仅说明方法可跨模型家族迁移。
4. 鲁棒性/扰动测试：论文未报告相关内容。
5. 消融实验：论文未报告具体消融实验表格，仅表明SFT与RL对性能提升呈互补作用。

4. 关键结论和发现
- 主要发现：① Search-on-Graph-R1（SogR1）仅用8B紧凑模型实现了优于前沿冻结LLM系统的KGQA性能，部署成本大幅降低；② 训练阶段的监督微调（SFT）与强化学习（RL）对性能的提升呈互补作用；③ SogR1方法可跨模型家族迁移，且经RL训练后模型的导航效率更高（所需Search调用更少）。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：Search-on-Graph-R1（SogR1）是一种结合监督微调与强化学习训练的8B紧凑KGQA模型，部署成本低，在WebQSP、CWQ、GrailQA基准上超越所有对比的冻结前沿LLM系统，训练与推理流程无需辅助模块或LLM裁判，且可跨模型家族迁移，导航效率更高。

</details>

---

### 14. [Attacking Graph Foundation Models Through Their Shared Representation](https://arxiv.org/abs/2607.18567v1)

**Authors**: Pankaj Kumar, Subhankar Mishra  
**Category**: cs.AI  
**Published**: 2026-07-22  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2607.18567v1  

#### Abstract
A graph foundation model generalizes across graph domains by mapping every input into one shared representation before any task reasoning. We call this map the alignment layer, the component that separates a graph foundation model from a graph neural network, and we show it is a distinct attack surf...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# Attacking Graph Foundation Models Through Their Shared Representation
1. 论文的主要贡献和创新点
✅ 解决的问题：图基础模型通过映射输入至共享表示的对齐层，成为其区别于普通图神经网络的核心，但现有攻击研究未将该对齐层作为攻击面，存在未被覆盖的攻击盲区。
🚀 提出的新方法与思路
**推理阶段对齐层定向表示空间扰动攻击**：在无训练访问权限的推理阶段，针对对齐层实施定向表示空间扰动，该攻击在可接受预算下可破坏多数图基础模型；
**输入空间编辑攻击**：通过修改输入的边、特征或文本实施输入空间攻击，可降低图基础模型的预测准确率。
🔍 相比现有方法的优势
维度 | 优势
聚焦攻击面 | 首次关注图基础模型的对齐层这一未被研究的攻击面
攻击条件 | 推理阶段攻击无需训练访问
攻击覆盖 | 覆盖表示空间扰动和输入空间编辑两种攻击类型

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：任务为图基础模型的攻击鲁棒性测试，评估指标包括攻击预算、正确预测移除率，指标方向未明确报告。
⚔️ 基线方法对比：论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验的对应表号内容。仅根据摘要明确内容：论文在6个公开图基础模型（涵盖谱标记器、文本嵌入空间、离散码本）上开展实验，发现定向表示空间扰动可破坏多数模型；OpenGraph的谱标记器存在对齐层特有的脆弱性，该脆弱性源于谱标记器而非解码器；可实现输入空间攻击在峰值时可对部分模型的正确预测率产生显著影响；攻击的可实现性与解码器读取共享表示的直接度相关，与任务干净准确率无关，基于干净准确率的模型内排序启发式在可实现攻击下不成立。

4. 关键结论和发现
- 主要发现：①图基础模型的共享表示对齐层是未被现有研究关注的关键攻击面；②定向表示空间扰动和输入空间编辑攻击可有效破坏图基础模型；③OpenGraph的谱标记器存在对齐层特有的脆弱性，且该脆弱性源于标记器而非解码器；④攻击效果与解码器读取共享表示的直接度相关，而非模型的干净准确率。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文针对图基础模型未被研究的共享表示对齐层攻击面，提出两种推理阶段无训练访问的攻击方式，揭示了图基础模型的攻击脆弱性与解码器结构特性的关联。

</details>

---

### 15. [Quality Action Assurance: Multimodal Verification of Examiner Claims in VR OSCEs](https://arxiv.org/abs/2607.19063v1)

**Authors**: Harry Rogers, Sally Shiels, Ashley Tomlinson, James Thomas, James Aylward, Nathan Gauge, Helen Higham, Alison Noble  
**Category**: cs.AI  
**Published**: 2026-07-22  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2607.19063v1  

#### Abstract
Objective Structured Clinical Examinations (OSCEs) are the gold standard for assessing clinical competence, yet scoring remains vulnerable to examiner subjectivity, fatigue, and cognitive bias. Standard examiner validation via inter-rater statistics lacks explanatory power regarding the source of er...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Quality Action Assurance: Multimodal Verification of Examiner Claims in VR OSCEs
1. 论文的主要贡献和创新点
✅ 解决的问题
OSCE是临床能力评估的金标准，但其评分易受考官主观性、疲劳、认知偏差影响；传统考官验证采用的组间评分统计缺乏解释力，既不分析考官推理也无法验证考官主张是否符合真实事件序列。

🚀 提出的新方法与思路
**Quality Action Assurance (QAA)**，一种多模态验证框架，用于VR儿科OSCE中核查考官主张。框架包含两大核心模块：
**constrained temporal action alignment model**：执行动作定位与行为者来源归因；
结合**large language model (LLM)**：提取考官主张，并将其与由视频、VR日志、行为者数据构建的真实事件记录进行比对核查。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 考官主张核查 | 对比多模态数据构建的真实事件序列进行验证，而非仅依赖组间评分统计 |
| 错误检测能力 | 具备较高的考官错误检测精度与召回率，大幅提升OSCE评估的事实正确性 |
| 评估公平性 | 支持更公平的临床能力评估 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| VR pediatric OSCEs | 验证QAA框架在VR儿科OSCE考官主张核查中的有效性 |

🎯 实验设置与评估指标
任务：在VR儿科OSCE中，将考官主张与多模态真实事件记录比对，实现考官主张验证与错误检测。
| 指标 | 含义 | 方向 |
| --- | --- | --- |
| Actor F1 | 动作行为者的F1值 | ↑ |
| W@16 | 时间对齐指标W@16 | ↑ |
| 考官错误检测精度 | 检测考官错误的准确率 | ↑ |
| 考官错误检测召回 | 检测考官错误的覆盖率 | ↑ |
| 事实正确率 | OSCE评估的事实准确性 | ↑ |

⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
实验在5折交叉验证下完成，结果如下：
- Actor F1：99.2% ± 0.7%
- W@16：93.4% ± 1.9%
- 考官错误检测精度：70.0%
- 考官错误检测召回：76.7%
- 事实正确率：从39.2%提升至79.2%
💡 结论：QAA在VR OSCE的动作定位与时间对齐任务中表现优异，可有效检测考官错误，显著提升OSCE评估的事实正确性。

4. 关键结论和发现
- 2-3 条主要发现
  1. 传统组间评分统计无法解释考官错误来源，QAA通过多模态比对填补了该空白；
  2. QAA在5折交叉验证中取得高Actor F1与时间对齐指标表现，具备较高的考官错误检测精度和召回；
  3. QAA可实现更公平的OSCE临床能力评估。
- 方法局限性
论文未报告
- 未来工作
论文未报告

> ✅ **总结一句话**：QAA是一种用于VR OSCE考官主张核查的多模态框架，可提升考官错误检测能力、改善评估事实正确性并增强OSCE的公平性。

</details>

---

### 16. [MUX: Continuous Reasoning via Multiplexed Tokens](https://arxiv.org/abs/2607.18264v1)

**Authors**: Ayhan Suleymanzade, Halil Alperen Gozeten, Michael Bronstein, \.Ismail \.Ilkan Ceylan, Jinwoo Kim  
**Category**: cs.AI  
**Published**: 2026-07-22  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2607.18264v1  

#### Abstract
Language models solve complex problems by articulating intermediate reasoning steps in natural language. While effective, this process is computationally bottlenecked: each reasoning step conveys only a single subword, and many are spent expressing a thought instead of carrying out computation. We p...

---

### 17. [Deep Reinforcement Learning to Master the Asymmetric Strategy of Baghchal](https://arxiv.org/abs/2607.18296v1)

**Authors**: Ranjit Raut, Aarav Subedi, Sagun Rai, Aaryan Shakya, Manoj Shakya  
**Category**: cs.AI  
**Published**: 2026-07-22  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2607.18296v1  

#### Abstract
Baghchal is a two-player asymmetric board game with Nepali origins where four tigers are to capture goats and twenty goats desire to keep tigers in immobility. Although Baghchal has a complex structure which is strategic, has perfect information structure, and has cultural meaning, it has not been a...

---

### 18. [Black-Mamba: Biologically-Inspired Leaky Accumulation for Conceptual Knowledge under Distribution Drift](https://arxiv.org/abs/2607.18899v1)

**Authors**: Giuseppe Soriano, Nicola Tonellotto, Alberto Gotta  
**Category**: cs.AI  
**Published**: 2026-07-22  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2607.18899v1  

#### Abstract
Forecasting under real-world conditions is inherently non-stationary, as the conditional distribution of future observations evolves over time. Recent test-time adaptive sequence models address this challenge by updating internal states during inference, but tie adaptation to instantaneous predictio...

---

### 19. [AHEAD: Advancing Multi-Class Label Aggregation with Interpretable Cross-Annotator Modeling](https://arxiv.org/abs/2607.18465v1)

**Authors**: Ju Chen, Sijia Xu, Jun Feng, Zhiqiang Gao, Zhengyi Yang  
**Category**: cs.LG  
**Published**: 2026-07-22  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2607.18465v1  

#### Abstract
Crowdsourced labeling provides valuable labeled data for domains across natural language processing, computer vision, and video. Label aggregation aims to infer latent true labels from noisy and biased annotations, with the key lying in annotator reliability estimation. Despite promising progress, e...

---

### 20. [GEqTrain: A Configuration-Driven Framework for Retargeting Equivariant Graph Neural Networks Across 3D Scientific Tasks](https://arxiv.org/abs/2607.19083v1)

**Authors**: Daniele Angioletti, Marco Nobile, Vittorio Limongelli  
**Category**: cs.LG  
**Published**: 2026-07-22  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.19083v1  

#### Abstract
Equivariant graph neural networks provide a powerful modeling language for three-dimensional scientific data, but their reuse is often limited by implementations tied to specific tasks, outputs, and training regimes. We present GEqTrain, a configuration-driven framework that separates dataset semant...

---

### 21. [PIP-NTT: Towards a Scalable Memory-Parallelized Accelerator for Iterative NTT in PQC](https://arxiv.org/abs/2607.18533v1)

**Authors**: Malik Imran, Ayesha Khalid, Ciara Rafferty, Safiullah Khan, Muhammad Rashid, Maire O'Neill  
**Category**: cs.AR  
**Published**: 2026-07-22  
**Score**: 27.5  
**Type**: new  
**ArXiv ID**: 2607.18533v1  

#### Abstract
The iterative forward and inverse number theoretic transform (NTT) is a key component in lattice-based post-quantum cryptography (PQC), typically implemented using Cooley-Tukey and Gentleman-Sande butterfly units. Existing iterative NTT accelerators often rely on ping-pong memory schemes and large m...

---

### 22. [ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D](https://arxiv.org/abs/2607.19321v1)

**Authors**: Lena Libon, Ben Rank, Jehyeok Yeon, David Schmotz, Jeremy Qin, Daniel Donnelly, Derck Prinzhorn, Maksym Andriushchenko  
**Category**: cs.AI  
**Published**: 2026-07-22  
**Score**: 24.0  
**Type**: new  
**ArXiv ID**: 2607.19321v1  

#### Abstract
As AI agents begin to automate AI R&amp;D, we need ways to assess whether their outputs are safe to deploy, even when the agents themselves may be untrusted. AI control offers one such approach: rather than trusting the agent, it treats it as a potential adversary and uses a monitor to detect covert...

---

### 23. [One Model, Many Graphs: Learning over Attributed Graphs across Heterogeneous Modalities with Vision-Language Models](https://arxiv.org/abs/2607.19128v1)

**Authors**: Jiayi Yang, Yifang Chen, Yuanfu Sun, Jiajin Liu, Qiaoyu Tan  
**Category**: cs.LG  
**Published**: 2026-07-22  
**Score**: 23.5  
**Type**: new  
**ArXiv ID**: 2607.19128v1  

#### Abstract
Vision-language models (VLMs) provide a unified representation space for textual and visual information, yet their potential as general-purpose backbones for graph-structured data remains largely unexplored. In practice, attributed graphs exhibit substantial modality heterogeneity: some graphs conta...

---

### 24. [An Efficient Fault-Tolerance Scheme for CKKS Computation on CPUs](https://arxiv.org/abs/2607.18720v1)

**Authors**: Jianan Mu, Ge Yu, Tenghui Hua, Liang Kong, Jing Ye, Xing Hu, Meng Li, Xiaowei Li, Huawei Li  
**Category**: cs.AR  
**Published**: 2026-07-22  
**Score**: 23.5  
**Type**: new  
**ArXiv ID**: 2607.18720v1  

#### Abstract
Fully homomorphic encryption (FHE) enables computation on encrypted data, but its long ciphertext dataflow and high-dimensional modular arithmetic make it vulnerable to silent data corruption caused by transient hardware faults. Existing protection methods either target dedicated accelerators or imp...

---

### 25. [Conservative Query and Adaptive Regularization for Offline RL Under Uncertainty Estimation](https://arxiv.org/abs/2607.19199v1)

**Authors**: Li-Rong Zhou, Qin-Wen Luo, Sheng-Jun Huang  
**Category**: cs.LG  
**Published**: 2026-07-22  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2607.19199v1  

#### Abstract
Offline reinforcement learning (RL) aims to learn an effective policy from a static dataset, but its performance is fundamentally limited by dataset coverage. Action preference queries leverage expert feedback without additional environment interaction, enabling policy improvement during offline tra...

---

### 26. [Operational Hallucination and Safety Drift in AI Agents](https://arxiv.org/abs/2607.18366v1)

**Authors**: Shasha Yu, Fiona Carroll, Barry L. Bentley  
**Category**: cs.AI  
**Published**: 2026-07-22  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2607.18366v1  

#### Abstract
Large language models (LLMs) serving as planners in tool-using autonomous agents introduce dynamic reliability risks in multi-turn execution. While single-turn safety mechanisms are relatively mature, extended interactions reveal structural vulnerabilities where initial alignment degrades over time....

---

### 27. [On the Limits of Support-Preserving Alignment and Bounded Filtering](https://arxiv.org/abs/2607.18295v1)

**Authors**: Aryan Dutt, Rui Mao, Anupam Chattopadhyay  
**Category**: cs.LG  
**Published**: 2026-07-22  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2607.18295v1  

#### Abstract
We study whether alignment schemes that reshape a base model's output distribution, combined with bounded safety filters, can drive the probability of harmful behavior to zero in modern large language models. Recent research suggests that harmful behaviors can persist under preference-based alignmen...

---

### 28. [A Better Start for Language Models: Domain-Conditional Position Offsets](https://arxiv.org/abs/2607.18302v1)

**Authors**: Ye Qiao  
**Category**: cs.LG  
**Published**: 2026-07-22  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2607.18302v1  

#### Abstract
Autoregressive language models are least accurate at the beginning of a sequence, where little context forces reliance on a generic pretraining prior. We show that this cold-start penalty is domain dependent and reduce it with a domain-conditional position offset: a single learned vector added to th...

---

### 29. [Reasoning Fine-Tuning Induces Persistent Latent Policy States](https://arxiv.org/abs/2607.18532v1)

**Authors**: Abir Harrasse, Michael Lan, Hunar Batra, Fateme Hashemi Chaleshtori, Chaithanya Bandi  
**Category**: cs.CL  
**Published**: 2026-07-22  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2607.18532v1  

#### Abstract
Reasoning-specialized language models show large performance gains over base models, yet the internal changes responsible for improved multi-step reasoning remain poorly understood. It is unclear whether reasoning fine-tuning improves local token-level competence or globally reorganizes how models s...

---

### 30. [Spatio-Temporal Prediction of Unsteady Airfoil Aerodynamics Using Augmented Graph Neural Ordinary Differential Equations with Exogenous Controls](https://arxiv.org/abs/2607.18309v1)

**Authors**: Henrik Lange, Reik Thormann, Philipp Bekemeyer  
**Category**: cs.LG  
**Published**: 2026-07-22  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2607.18309v1  

#### Abstract
Unsteady aerodynamic phenomena, such as gusts, turbulence, and fluid-structure interactions affect an aircraft during flight. For design, optimisation and certification, it is indispensable to quantify such unsteady aerodynamic effects. Industry-standard computational fluid dynamics methods, such as...

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
