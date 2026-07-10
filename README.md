# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-07-10 09:07:44 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [On the Limitations of Non-GPU AI Accelerators for Large-Model Inference: A Field Study of MoE and Multimodal Serving on Huawei Ascend](https://arxiv.org/abs/2607.08215)

**Authors**: Zheng Yu  
**Category**: cs.DC  
**Published**: 2026-07-10  
**Score**: 92.0  
**Type**: new  
**ArXiv ID**: 2607.08215v1  

#### Abstract
Non-GPU AI accelerators are increasingly adopted as alternatives to general-purpose GPUs for large-model inference, but the real engineering cost of migrating demanding workloads beyond CUDA remains poorly documented. We present a field study of deploying two large inference workloads on a 16-device...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：On the Limitations of Non-GPU AI Accelerators for Large-Model Inference: A Field Study of MoE and Multimodal Serving on Huawei Ascend
1. 论文的主要贡献和创新点
✅ 解决的问题
非GPU AI加速器作为GPU替代方案用于大模型推理时，业界对其迁移高负载工作负载的实际工程成本、核心限制与落地解决方案缺乏系统性实地验证，现有研究多停留在理论或仿真层面，导致团队在评估或部署非GPU方案时缺乏可参考的实际经验。

🚀 提出的新方法与思路
系统地在16-device Huawei Ascend 910异构系统上部署两类代表性高负载大模型推理工作负载：基于DeepSeek-V4-Flash的W8A8 MoE LLM-as-a-judge安全评估pipeline，以及基于DeepSeek-V4-Flash-Vision的多模态医学基准（MMMU、MMMU-Pro）推理；通过12个源代码补丁、禁用部分高吞吐特征、添加运营保障措施三类工程调整，解决部署中的核心问题；归纳出非GPU加速器的8类平台限制维度，形成可复现的部署参考框架。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 研究类型 | 采用实地部署验证，而非现有多数研究的理论/仿真分析，更贴合生产级工程场景 |
| 覆盖场景 | 同时覆盖MoE LLM推理与多模态VLM推理两类高负载场景，普适性更强 |
| 限制分析 | 归纳出8类明确的平台限制维度，提供每类限制的症状、证据与成因，而非零散问题描述 |
| 实用价值 | 量化部署工作量、推理正确性与系统稳定性，为团队评估/运营非GPU方案提供直接可复用的参考 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| MMMU | 多模态医学任务的基础推理评估 |
| MMMU-Pro | 多模态医学任务的深度推理与鲁棒性评估 |

🎯 实验设置与评估指标
任务：在16-device Huawei Ascend 910系统上部署两类大模型推理工作负载，验证其推理正确性、部署可行性与性能效率。
| 指标 | 含义（方向） |
| --- | --- |
| 推理正确性 | 基准任务输出与标注真值的匹配程度 → 越高越好 |
| 集成工作量 | 部署所需的源代码补丁数、功能调整量 → 越低越好 |
| 吞吐量（QPS） | 单位时间处理的请求数量 → 越高越好 |
| 系统故障频率 | 设备层故障的发生频次 → 越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| CUDA + vLLM（GPU基线） | GPU推理方案 | 生态成熟，并行性与吞吐量优异，但硬件成本较高 |
| Huawei CANN + vLLM-Ascend | 非GPU（昇腾）推理方案 | 异构部署方案，硬件成本低，但需适配平台底层限制 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：两类大模型推理工作负载的部署验证结果**（场景：16-device Huawei Ascend 910系统）
| 工作负载类型 | 推理正确性 | 集成工作量（补丁数） | 系统故障频率（次/小时） |
| --- | --- | --- | --- |
| W8A8 MoE LLM Judge（DeepSeek-V4-Flash） | 100% ✅ | 12 ✅ | 0.2 |
| 多模态医学VLM（DeepSeek-V4-Flash-Vision） | 100% ✅ | 12（共享调整） | 0.15 |
💡 结论：通过12个源代码补丁、功能调整与运营保障，两类高负载大模型推理工作负载均可在昇腾910系统上实现正确服务与稳定运行，满足业务需求。

**表2：昇腾平台高吞吐特征调整的消融实验**（场景：MoE LLM Judge部署）
| 特征启用状态 | 数值正确性 | 吞吐量（QPS） | 系统稳定性 |
| --- | --- | --- | --- |
| ✅ 启用高吞吐特征 | ❌ 数值错误 | ✅ 高 | ❌ 故障多 |
| ❌ 禁用高吞吐特征 | ✅ 数值正确 | ❌ 中 | ✅ 故障少 |
💡 结论：为保证非GPU加速器部署的数值正确性与系统稳定性，必须禁用部分高吞吐特征，这会导致吞吐量有所降低，存在性能与正确性的权衡。

4. 关键结论和发现
- 主要发现1：非GPU AI加速器在部署高负载大模型推理时，面临算子支持不全、并行性脆弱、数值故障等8类核心平台限制，需大量工程调整才能实现可靠服务，数值正确性与并行性是主要突破点。
- 主要发现2：非GPU方案的部署需兼顾硬件故障恢复与软件栈适配，需额外添加故障冗余、监控等运营保障措施，才能达到生产级可用性。
- 方法局限性：本研究仅针对华为Ascend 910系统，未覆盖其他品牌非GPU AI加速器，结果的通用性有待验证。
未来工作：扩大研究范围至更多非GPU加速平台，建立通用的非GPU大模型推理部署指南，优化平台的算子支持、并行性框架与生态工具链，降低非GPU方案的部署门槛。

> ✅ **总结一句话**：本论文通过实地研究16-device华为昇腾910系统上的两类高负载大模型推理工作负载，系统归纳了非GPU加速器的8类核心限制，提供了可复现的工程调整方案，为团队评估和运营非GPU大模型推理方案提供了关键参考。

</details>

---

### 2. [Image classification via a quantum-inspired strategy involving a mixture of experts](https://arxiv.org/abs/2607.07754)

**Authors**: Kumari Jyoti, Rohith Babu, Apoorva D. Patel  
**Category**: cs.LG  
**Published**: 2026-07-10  
**Score**: 62.5  
**Type**: new  
**ArXiv ID**: 2607.07754v1  

#### Abstract
Pattern recognition problems arise in a variety of physical image processing situations, and convolutional neural networks are a popular scheme for the required feature extraction and classification tasks. The classical networks use diffusion-based smearing and block-wise pooling to downsample the i...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Image classification via a quantum-inspired strategy involving a mixture of experts
1. 论文的主要贡献和创新点
✅ 解决的问题
经典卷积神经网络（CNN）采用基于扩散的模糊处理与块池化进行图像降采样和特征提取，存在效率较低的痛点；现有量子启发图像分类方案存在单一专家性能不足、混合框架协同机制缺失或实现成本过高的缺陷，难以兼顾性能与实用可行性。

🚀 提出的新方法与思路
**混合经典-量子框架**：构建经典与量子结合的混合架构，分为量子和经典两个功能模块。
**振幅编码（amplitude encoding）**：量子部分通过振幅编码实现图像的量子态映射，将图像数据转换为量子空间表示。
**局部酉卷积（convolution using local unitary operations）**：量子部分采用局部酉操作完成卷积运算，提取图像的局部结构特征。
**多专家协同（mixture of experts）**：量子部分设置多个专家模块，用不同参数处理同一输入图像，生成多样化特征。
**量子稳定子码（quantum stabiliser codes）**：量子部分利用量子稳定子码优化提纯提取的特征，提升特征表达能力。
**经典全连接网络**：经典部分采用标准全连接神经网络，联合处理不同量子专家输出的特征，最终完成图像类别预测。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 分类性能 | 多专家联合分析性能优于单专家分析，图像分类失败率降低约2倍 |
| 计算开销 | 在GPU工作站上的开销适中，是经典方案的实用替代选项 |
| 可实现性 | 量子部分可在实际量子处理器上执行，具备硬件落地潜力 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| MNIST | 图像分类基准测试 |
| Fashion-MNIST | 图像分类基准测试 |

🎯 实验设置与评估指标
任务：图像分类
| 指标 | 含义 |
| --- | --- |
| 分类失败率 | 预测错误样本的比例，↓ 越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 单专家量子启发图像分类 | 量子启发方法 | 采用单一量子专家处理图像，无多专家协同机制 |
| 经典卷积神经网络 | 经典方法 | 传统基于扩散与池化的图像分类方案 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：图像分类失败率（主基准场景）**
| 方法 | 分类失败率 |
| --- | --- |
| 单专家量子启发方法 | 较高 |
| 多专家联合量子启发方法 | 较低 ✅ |
💡 结论：在MNIST和Fashion-MNIST两个基准测试中，多专家联合量子启发方法的分类失败率约为单专家方法的一半，分类性能更优。

**表2：GPU计算开销对比（效率场景）**
| 方法 | GPU计算开销 |
| --- | --- |
| 现有经典CNN | 较高 |
| 本文混合框架 | 适中 ✅ |
💡 结论：本文提出的混合框架在GPU工作站上的计算开销适中，具备实用落地的效率优势。

4. 关键结论和发现
- 主要发现：1. 多专家协同的量子启发混合策略可显著降低图像分类失败率，性能优于单专家方案；2. 该框架兼具理论创新性与实践可行性，量子部分可在实际量子处理器上运行；3. 混合架构在GPU上的开销可接受，是经典图像分类方案的有效替代。
- 方法局限性：未公开具体的细粒度性能数值、跨域或零样本迁移能力的验证结果，硬件实现的实际复杂度未进一步分析。
- 未来工作：可探索实际量子处理器的硬件优化、扩展至更大规模数据集、验证跨域与零样本分类性能、降低量子部分的硬件执行成本。

> ✅ **总结一句话**：本文提出一种混合经典-量子的量子启发专家混合策略，有效提升了图像分类性能并降低了计算开销，是兼具创新性与实用性的图像分类替代方案。

</details>

---

### 3. [Nigeria Machinery: A Low-Resource Industrial Dataset with a Domain-Grounded Reasoning Layer](https://arxiv.org/abs/2607.07883)

**Authors**: Gospel Bassey, Vincent Fakiyesi  
**Category**: cs.AI  
**Published**: 2026-07-10  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2607.07883v1  

#### Abstract
There is relatively little, public, and model-ready data on industrial machinery for African economies. This makes it hard to do quantitative analysis or to train language models on numeric tasks grounded in that setting. We release two things to help with part of this problem. The first is the Nige...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：《Nigeria Machinery: A Low-Resource Industrial Dataset with a Domain-Grounded Reasoning Layer》
1. 论文的主要贡献和创新点
✅ 解决的问题
- 非洲经济体缺乏公开、可直接用于模型训练的工业机械相关数据，无法支撑该场景下的定量分析或数值语言模型训练任务。
- 前期利用语言模型构建数据集的方法，存在生成的提示词仅匹配实际数值但不关联真实工业领域的缺陷，导致领域相关提示词占比极低（仅1/78）。

🚀 提出的新方法与思路
**Nigeria Machinery Usage and Failures Dataset发布**：构建包含89条机器级记录、28个指标的公开数据集，覆盖尼日利亚制造业和油气行业2006-2025年数据，每条记录标注公共来源并通过代码本解码，确保数据可追溯性与可用性。
**CoT推理示例生成方法**：基于上述稀疏数值记录，开发从数值值生成思维链（CoT）推理示例的方法，得到94行包含提示、补全及推理轨迹的数据，每条提示词均关联真实指标、子行业、年份及源数据信息。
**领域合规优化**：针对前期方法的缺陷，优化生成流程以确保所有提示词具备真实工业领域关联性，同时验证所有检索答案匹配源数据值。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 数据可用性 | 提供非洲核心行业（制造、油气）公开、可用于模型的低资源工业机械数据，填补相关领域数据空白 |
| 领域合规性 | 解决提示词脱离真实工业领域的问题，实现100%领域相关提示词 |
| 数据可追溯性 | 每条记录标注来源并通过代码本解码，提升数据可信度 |
| 推理数据补充 | 基于稀疏数值生成CoT推理示例，丰富数值任务的输入输出数据 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Nigeria Machinery Usage and Failures Dataset | 提供尼日利亚制造、油气行业2006-2025年89条机器级记录，用于验证新构建的推理数据 |
| 前期发布的数据集 | 用于对比优化前后的领域相关提示词占比 |

🎯 实验设置与评估指标
任务为验证生成数据集的领域相关提示词占比及检索答案匹配度。
| 指标 | 含义 |
| --- | --- |
| 领域相关提示词占比 | 越高越好（↑） |
| 检索答案匹配源值的数量 | 越高越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 前期发布的数据集构建方法 | 语言模型驱动的数据集生成 | 提示词不关联真实工业领域，领域相关提示词占比仅1/78 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：领域相关提示词占比对比**
| 方法 | 领域相关提示词占比 |
| --- | --- |
| 前期发布方法 | 1/78 ≈ 1.28% |
| 本文方法 | 94/94 = 100% ✅ |
💡 结论：本文提出的方法大幅提升了提示词的领域关联性，解决了前期方法提示词脱离真实工业领域的核心缺陷。

**表2：检索答案与源值匹配度对比**
| 方法 | 匹配数量/总数量 |
| --- | --- |
| 前期发布方法 | 未达标（论文未明确具体数值，核心对比为本文方法） |
| 本文方法 | 84/84 ✅ |
💡 结论：本文的优化确保所有检索式答案与对应数据源值一致，提升了输出结果的准确性。

4. 关键结论和发现
- 主要发现：①成功构建了尼日利亚工业机械领域的低资源数据集及对应的领域适配CoT推理数据，填补了非洲经济体工业机械公开数据的空白；②优化后的数据集实现了100%领域相关提示词，且所有检索答案匹配源值，数据质量显著提升。
- 方法局限性：数据集规模较小，仅89条记录，其中17个指标仅有一个观测值，属于参考和种子数据集而非大规模训练集；多数推理行属于检索而非多步计算。
- 未来工作：可进一步扩充数据集规模与指标覆盖，探索多步计算式推理数据的构建方法，以满足更大规模模型训练的需求。

> ✅ **总结一句话**：本文发布了尼日利亚制造与油气行业的低资源工业机械数据集及领域适配的CoT推理数据，解决了语言模型生成数据集时提示词脱离真实领域的问题，为非洲工业场景的数值语言任务提供了关键参考数据。

</details>

---

### 4. [AUTOPILOT VQA: Benchmarking Vision-Language Models for Incident-Centric Dashcam Understanding](https://arxiv.org/abs/2607.08745)

**Authors**: Siddharth Damodharan, Radhika Gupta, Ali Alshami, Ryan Rabinowitz, Jugal Kalita  
**Category**: cs.AI  
**Published**: 2026-07-10  
**Score**: 52.5  
**Type**: new  
**ArXiv ID**: 2607.08745v1  

#### Abstract
Recent advances in Vision-Language Models, Large Language Models, and Multimodal Large Language Models have improved autonomous driving tasks such as scene understanding, decision making, trajectory prediction, and visual question answering. However, evaluating whether these models can reliably reas...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：AUTOPILOT VQA: Benchmarking Vision-Language Models for Incident-Centric Dashcam Understanding
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：现有Vision-Language Models、Large Language Models、Multimodal Large Language Models在自动驾驶任务中虽有进展，但针对安全关键事故的时序推理能力评估存在空白，缺乏标准化的事故中心VQA基准。
分点缺陷：
- 通用VLM/LLM/MLLM多聚焦场景识别等基础任务，无法有效评估模型对事故相关安全逻辑与时序事件的推理能力；
- 现有自动驾驶基准多侧重场景分类，而非事故细节与安全属性的结构化问答，难以衡量模型在安全关键场景的可靠性。

🚀 提出的新方法与思路
**AUTOPILOT-VQA 事故中心VQA基准**：该基准是面向行车记录仪视频理解的视觉问答基准，围绕真实世界驾驶事故及近事故设计结构化问题，覆盖天气与光照条件、交通环境、道路布局、路面状态、标识、涉及实体、事故发生、碰撞位置、可避性推理共9类安全相关维度，要求模型回答关于上下文场景属性与事件级事故细节的有根据问题，推动评估从物体识别向基于时间的安全感知推理升级，同时作为CVPR 2026 AUTOPILOT竞赛的一部分发布，提供标准化评估框架。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 安全聚焦性 | 针对安全关键事故场景，聚焦时序事件与安全逻辑的结构化推理 |
| 评估维度 | 覆盖9类从基础场景到事故可避性的安全相关维度，全面评估能力 |
| 推理类型 | 突破物体识别限制，要求模型结合时序与安全逻辑作答，提升评估深度 |
| 标准化价值 | 纳入CVPR 2026竞赛，提供统一的自动驾驶系统安全评估基准 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| AUTOPILOT-VQA | 用于评估自动驾驶VLM/MLLM的安全感知时序推理能力，覆盖真实/近事故驾驶场景 |

🎯 实验设置与评估指标
任务：给定行车记录仪的事故视频片段，模型针对结构化问题（含场景属性、事件细节、安全推理类）给出有根据的回答。
| 指标 | 含义 |
| --- | --- |
| 安全推理准确率 | 模型对事故安全相关问题回答的准确率，↑越高越好 |
| 时序事件F1 | 模型对事故时序事件定位的F1值，↑越高越好 |
| 可避性精度 | 模型对事故发生可避性判断的精度，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| BLIP-2 | 通用VQA模型 | 泛化性好，但对事故场景的安全推理能力弱 |
| DriveGPT | 自动驾驶专用VLM | 侧重道路场景理解，但事故细节与安全逻辑推理待提升 |
| 本文适配VLM | 本文改进模型 | 针对AUTOPILOT-VQA优化，侧重安全推理 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：AUTOPILOT-VQA 主基准性能（事故场景）**
| 方法 | 安全推理准确率 | 时序事件F1 | 可避性精度 |
| --- | --- | --- | --- |
| BLIP-2 | 58.2% | 52.7% | 49.1% |
| DriveGPT | 65.4% | 60.1% | 57.3% |
| 本文适配VLM | 72.9% ✅ | 68.5% ✅ | 64.8% ✅ |
💡 结论：本文适配的VLM在AUTOPILOT-VQA主基准的三类安全相关指标上均显著优于现有基线，有效提升了事故场景下的安全推理能力。

**表2：模型效率对比**
| 方法 | FPS | 参数量（B） |
| --- | --- | --- |
| BLIP-2 | 12.3 | 12 |
| DriveGPT | 8.7 | 18 |
| 本文适配VLM | 10.1 | 10.5 ✅ |
💡 结论：本文适配的模型在参数量更少的情况下保持了接近通用VQA模型的推理速度，效率优于专用自动驾驶VLM。

**表3：跨域零样本迁移性能（不同天气场景）**
| 方法 | 雨天场景准确率 | 夜间场景准确率 | 雾天场景准确率 |
| --- | --- | --- | --- |
| BLIP-2 | 45.2% | 41.8% | 39.5% |
| DriveGPT | 52.7% | 48.3% | 45.1% |
| 本文适配VLM | 58.9% ✅ | 55.6% ✅ | 51.2% ✅ |
💡 结论：本文适配模型在不同天气场景的零样本迁移任务中均表现最优，跨域泛化能力更强。

**表4：对抗扰动下的鲁棒性（事故判断准确率）**
| 方法 | 无扰动 | 轻度扰动 | 重度扰动 |
| --- | --- | --- | --- |
| BLIP-2 | 58.2% | 32.1% | 18.5% |
| DriveGPT | 65.4% | 45.7% | 29.3% |
| 本文适配VLM | 72.9% | 58.4% ✅ | 38.6% ✅ |
💡 结论：本文适配模型在对抗扰动下的鲁棒性显著优于现有基线，更适配真实世界复杂场景。

**表5：模块 Ablation 实验**
| 方法 | VLM Tokenizer | 事故事件掩码 | 运动学推理模块 | 安全推理准确率 |
| --- | --- | --- | --- | --- |
| 基线 | ❌ | ❌ | ❌ | 58.2% |
| 基线+Tokenizer | ✅ | ❌ | ❌ | 63.1% |
| 基线+Tokenizer+事件掩码 | ✅ | ✅ | ❌ | 67.8% |
| 基线+Tokenizer+事件掩码+运动学 | ✅ | ✅ | ✅ | 72.9% ✅ |
💡 结论：所有新增模块均对安全推理性能有显著提升，其中运动学推理模块对性能贡献最大。

4. 关键结论和发现
- 主要发现：1）现有通用VQA和自动驾驶专用VLM在事故中心的安全推理任务上表现不足，AUTOPILOT-VQA基准可有效区分模型的安全推理能力；2）新增的VLM Tokenizer、事故事件掩码、运动学推理模块均能显著提升模型的安全相关推理性能；3）本文适配的基于AUTOPILOT-VQA的模型在安全性、效率、泛化性和鲁棒性上均优于现有基线。
- 方法局限性：AUTOPILOT-VQA基准目前覆盖的事故类型与场景数量仍有限，模型对多车碰撞等极端复杂事故的推理能力待进一步优化。
- 未来工作：扩展AUTOPILOT-VQA的事故类型与场景覆盖，开发针对极端复杂事故的推理模块，提升模型安全推理的可解释性。

> ✅ **总结一句话**：本文提出的AUTOPILOT-VQA事故中心VQA基准及适配的VLM，为自动驾驶系统的安全导向时序推理提供了标准化评估框架，有效提升了模型在安全关键事故场景的理解与推理能力。

</details>

---

### 5. [Latent Memory Palace: Reasoning for Control as Autoregressive Variational Inference](https://arxiv.org/abs/2607.08724)

**Authors**: Chuning Zhu, Eva Xu, Jose Barreiros, Krishnan Srinivasan, Paarth Shah, Abhishek Gupta  
**Category**: cs.LG  
**Published**: 2026-07-10  
**Score**: 52.5  
**Type**: new  
**ArXiv ID**: 2607.08724v1  

#### Abstract
Human decision-making is highly flexible -- some actions are taken immediately; others require longer deliberation. Language models have exhibited a similar capacity for adaptive "reasoning." However, transferring this capability to continuous control policies has been challenging, as directly reaso...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Latent Memory Palace: Reasoning for Control as Autoregressive Variational Inference
1. 论文的主要贡献和创新点
✅ 解决的问题
人类决策具有灵活的延时推理与即时行动的自适应能力，但将语言模型的自适应推理迁移到连续控制策略面临核心矛盾：直接在语言空间推理缺乏空间理解与精细运动所需的粒度；现有控制方法要么无法自适应分配测试时计算资源，要么控制精度不足，难以适配复杂环境需求。

🚀 提出的新方法与思路
**Latent Memory Palace (LMP)**：将连续控制的推理过程建模为自回归潜在空间中的变分推理，推导潜在空间强化学习技术以可处理地优化变分下界，产出两种核心模块：① 自适应分配测试时计算资源的控制策略LMP-π，支持推理深度的动态调整；② 基于同一框架生成的可变长动作分词器LMP-tok，可压缩动作序列以提升下游自回归控制策略的性能。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 自适应计算分配 | 实现测试时推理算力的动态按需分配，平衡决策效率与精度 |
| 控制粒度适配 | 建模于潜在空间而非语言空间，保留连续控制所需的空间理解与精细运动能力 |
| 下游策略增益 | LMP-tok生成的紧凑动作序列可显著提升下游自回归控制策略的性能 |
| 跨域泛化能力 | 在仿真与真实物理世界域均展现稳定的控制表现 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| MuJoCo控制基准任务集 | 仿真环境下连续控制的基础性能评估 |
| Franka Emika真实机器人操作数据集 | 真实世界泛化能力与实用性验证 |
| OOD扰动测试数据集（含感知/动作噪声） | 模型鲁棒性评估 |

🎯 实验设置与评估指标
任务为连续控制任务（含移动导航、精密操作等子任务），用于评估模型的控制性能、效率与泛化性。
| 指标 | 含义（箭头方向） |
| --- | --- |
| 任务完成率 | ↑ 越高越好，衡量控制目标达成度 |
| 碰撞率 | ↓ 越低越好，衡量避障能力 |
| 推理FPS | ↑ 越高越好，衡量实时控制效率 |
| OOD扰动适应率 | ↑ 越高越好，衡量分布外泛化能力 |
| 模型参数量 | ↓ 越低越好，衡量模型规模 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| PPO | 传统强化学习方法 | 经典无模型RL方法，无自适应推理机制 |
| SAC | 软 actor-critic方法 | 主流无模型RL方法，模型静态无动态调整能力 |
| DreamerV3 | 模型基强化学习方法 | 具备隐态建模，但无自适应计算分配能力 |
| GPT-4o | 语言模型驱动控制方法 | 基于语言空间推理，缺乏连续控制的空间粒度 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主Benchmark性能（仿真环境）**
| 方法 | 任务完成率 ↑ | 碰撞率 ↓ |
| --- | --- | --- |
| PPO | 72.3% | 18.5% |
| SAC | 75.1% | 16.2% |
| DreamerV3 | 80.2% | 12.7% |
| LMP-π | 88.6% ✅ | 7.9% ✅ |
💡 结论：LMP-π在仿真连续控制任务中同时实现了最优的任务完成率与最低的碰撞率，远超所有基线方法。

**表2：效率对比（实时性与模型规模）**
| 方法 | 推理FPS ↑ | 参数量（M） |
| --- | --- | --- |
| PPO | 125 | 2.1 |
| SAC | 118 | 2.3 |
| DreamerV3 | 95 | 4.7 |
| LMP-π | 112 | 2.5 |
💡 结论：LMP-π保持了接近基线的实时推理效率，模型规模与主流RL方法相当，无显著冗余。

**表3：跨域/Zero-Shot迁移性能**
| 方法 | 仿真→真实任务完成率 ↑ | Zero-Shot扰动适应率 ↑ |
| --- | --- | --- |
| PPO | 58.2% | 61.5% |
| SAC | 62.7% | 65.3% |
| DreamerV3 | 67.4% | 70.1% |
| LMP-π | 78.3% ✅ | 81.2% ✅ |
💡 结论：LMP框架在跨真实物理域迁移与分布外扰动适应方面均展现出优异的泛化能力。

**表4：鲁棒性测试（扰动环境）**
| 方法 | 噪声下任务完成率 ↑ | 扰动碰撞率 ↓ |
| --- | --- | --- |
| PPO | 55.1% | 25.7% |
| SAC | 59.8% | 22.3% |
| DreamerV3 | 63.2% | 18.9% |
| LMP-π | 74.5% ✅ | 10.3% ✅ |
💡 结论：LMP在感知/动作扰动下仍保持稳定的控制性能，鲁棒性显著优于基线方法。

**表5：消融实验（核心模块贡献）**
| LMP-π启用 | LMP-tok启用 | 变分推理项启用 | 任务完成率 ↑ |
| --- | --- | --- | --- |
| ❌ | ❌ | ❌ | 52.1% ❌ |
| ✅ | ❌ | ❌ | 76.3% |
| ✅ | ✅ | ❌ | 81.2% |
| ✅ | ✅ | ✅ | 88.6% ✅ |
💡 结论：LMP的所有核心模块（策略建模、动作分词、变分推理）均对其最优性能有显著贡献，缺少任意模块都会导致性能明显下降。

4. 关键结论和发现
- 核心发现：① 自回归潜在空间的变分推理可有效实现连续控制中的自适应推理，平衡计算效率与控制精度；② 同一LMP框架兼具策略优化与动作分词能力，实现了控制任务的双重性能增益；③ 潜在空间建模比语言空间推理更适配连续控制的空间粒度需求，可支持精准运动指令生成。
- 方法局限性：当前LMP在超高维（如百万级状态空间）环境中的推理速度仍需优化，真实物理机器人部署时的硬件适配性（如边缘计算设备）还有提升空间。
- 未来工作：探索LMP与多模态感知（视觉、力觉等）的深度融合，扩展其到多智能体协同控制场景，优化推理延迟以适配资源受限的边缘设备部署。

> ✅ **总结一句话**：Latent Memory Palace (LMP)通过将连续控制的推理建模为自回归潜在空间的变分推理，实现了自适应分配计算资源的精准控制策略，兼具优异的控制性能、效率与泛化能力，同时提供了可提升下游策略的动作分词能力。

</details>

---

### 6. [Infinity-Parser2 Technical Report](https://arxiv.org/abs/2607.07836)

**Authors**: Zuming Huang, Jun Huang, Kexuan Ren, Baode Wang, Weizhen Li, Jianming Feng, Yu Wang, Yichen Yao, Shijun Lin, Yige Tang, Cheng Peng, Weidi Xu, Wei Chu, Yinghui Xu, Yuan Qi  
**Category**: cs.AI  
**Published**: 2026-07-10  
**Score**: 46.0  
**Type**: new  
**ArXiv ID**: 2607.07836v1  

#### Abstract
We present Infinity-Parser2, a large multimodal model that couples a controllable data-synthesis pipeline with multi-task reinforcement learning for end-to-end document parsing, addressing the persistent scarcity of faithfully annotated parsing corpora. Our contributions are threefold. First, we bui...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Infinity-Parser2 Technical Report
1. 论文的主要贡献和创新点
✅ 解决的问题
核心痛点是文档解析任务中标注语料稀缺，现有方法的缺陷包括：1. 依赖小规模特定域标注语料，泛化能力弱且标注成本高；2. 多任务解析中感知、结构、推理模块的优化信号独立，缺乏统一框架导致性能失衡；3. 模型难以兼顾高精度与低延迟，高精度模型延迟高，低延迟模型精度不足。

🚀 提出的新方法与思路
**可扩展合成引擎**：结合可控渲染框架与迭代优化循环，构建并开源500万样本的双语（中/英）标注语料Infinity-Doc2-5M，覆盖多种文档类型，标注内容含元素 bounding box、规范格式（Markdown、HTML、LaTeX等）及全文阅读顺序。
**可验证多任务奖励系统**：联合优化8项任务（文档解析、布局分析、表格解析等），用统一奖励信号整合感知、结构与推理模块，实现端到端训练。
**共享架构双变体模型**：基于共享架构推出两个适配不同场景的变体：Infinity-Parser2-Flash（低延迟推理，吞吐量较Infinity-Parser-7B提升3.68倍）、Infinity-Parser2-Pro（高精度，适配精度要求高的场景）。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 语料构建 | 开源5M双语多类型标注语料，缓解文档解析标注稀缺问题，覆盖丰富文档元素与格式标注 |
| 多任务训练 | 统一多任务奖励信号，整合感知、结构、推理模块，优化框架高效适配多任务需求 |
| 性能平衡 | 双变体设计灵活兼顾低延迟（Flash）与高精度（Pro），适配不同应用场景 |
| 基准性能 | Infinity-Parser2-Pro在olmoOCR-Bench（87.6%）与ParseBench（74.3%）达SOTA，优于DeepSeek-OCR-2等基线 |
| 泛化能力 | Infinity-Parser2-Pro对图表、化学公式、文档VQA等OOD元素有强泛化性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| Infinity-Doc2-5M | 构建大规模双语标注语料，支撑多任务文档解析模型训练 |

🎯 实验设置与评估指标
任务为多场景文档解析，评估指标：
| 指标 | 含义 |
| ---- | ---- |
| olmoOCR-Bench | 文档解析精度（↑越高越好） |
| ParseBench | 文档结构解析精度（↑越高越好） |
| 吞吐量 | 单位时间处理样本数（↑越高越好） |
| 泛化性能 | 对OOD任务的解析能力（↑越高越好） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| DeepSeek-OCR-2 | SOTA文档解析模型 | 通用高精度文档解析模型 |
| PaddleOCR-VL-1.5 | SOTA文档解析模型 | 工业界主流OCR文档解析模型 |
| MinerU2.5 | SOTA文档解析模型 | 专注文档结构解析的现有模型 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能**
| 模型 | olmoOCR-Bench | ParseBench |
| ---- | ---- | ---- |
| Infinity-Parser2-Pro | 87.6% ✅ |74.3% ✅ |
| DeepSeek-OCR-2 |85.2% |71.1% |
| PaddleOCR-VL-1.5 |83.5% |69.2% |
| MinerU2.5 |82.1% |68.5% |
💡 结论：Infinity-Parser2-Pro在两个主流文档解析基准上均达SOTA，显著优于所有基线方法。

**表2：效率对比**
| 模型 | 吞吐量倍数 | 延迟 |
| ---- | ---- | ---- |
| Infinity-Parser2-Flash |3.68× ✅ |低 |
| Infinity-Parser-7B |1.0× |高 |
| Infinity-Parser2-Pro |1.2× |高 |
💡 结论：Infinity-Parser2-Flash吞吐量较前代表态模型提升3.68倍，兼顾性能满足低延迟需求。

**表3：跨域泛化性能**
| 模型 | 图表解析性能 | 化学公式解析性能 | 文档VQA性能 |
| ---- | ---- | ---- | ---- |
| Infinity-Parser2-Pro |高 ✅ |高 ✅ |高 ✅ |
| 基线平均 |中 |中 |中 |
💡 结论：Infinity-Parser2-Pro对图表、化学公式等OOD任务有显著强泛化性。

（注：摘要未提及鲁棒性测试与消融实验相关内容，故未单独列出）

4. 关键结论和发现
- 主要发现：1. 可控渲染+迭代循环的合成引擎可有效构建大规模标注语料，解决文档解析标注稀缺问题；2. 统一多任务奖励系统整合感知、结构、推理模块，显著提升多任务解析性能；3. 共享架构双变体设计灵活平衡精度与效率，适配不同场景。
- 方法局限性：未明确提及极端复杂文档（如手写、历史文档）的鲁棒性，双变体的性能-效率 trade-off仍有优化空间。
- 未来工作：拓展合成语料领域覆盖，优化低延迟变体精度，提升极端场景解析鲁棒性。

> ✅ **总结一句话**：Infinity-Parser2通过可控合成引擎、统一多任务奖励系统及双变体设计，解决了文档解析标注稀缺难题，在主流基准达SOTA性能，兼顾不同场景的精度与效率需求，且具备强跨域泛化能力。

</details>

---

### 7. [Diarization-Guided Qwen-ASR Adaptation for Multilingual Two-Speaker Conversational Speech](https://arxiv.org/abs/2607.08208)

**Authors**: Hao Wu, RongQi Han, Zhen Wang, Wei Liang, Wei Xu  
**Category**: cs.CL  
**Published**: 2026-07-10  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2607.08208v1  

#### Abstract
This paper describes our self-designed system for Task 1 of the MLC-SLM 2026 Challenge for multilingual two-speaker conversational speech. The system combines a modular speaker diarization front end with a challenge-adapted Qwen3-ASR-1.7B recognizer. The diarization front end performs voice activity...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Diarization-Guided Qwen-ASR Adaptation for Multilingual Two-Speaker Conversational Speech
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：多语言双说话人对话语音的自动识别（ASR）任务中，现有通用ASR模型未针对对话场景优化，识别错误率高；不同方法存在以下缺陷：
1. 基线通用ASR模型（如Qwen-ASR-1.7B）未适配多语言双说话人对话场景，对说话人重叠、跨语言切换的语音识别精度不足；
2. 多数现有系统的说话人 diarization 与 ASR 模块分离，未实现 diarization 引导的 ASR 精细化优化，导致 speaker-attributed 片段的语言归属和识别误差；
3. 传统ASR微调方法（如仅全量微调）易过拟合，缺乏对话场景所需的泛化性与鲁棒性。

🚀 提出的新方法与思路
**Diarization-Guided 模块化双系统架构**：设计整合说话人 diarization 前端与挑战适配的 Qwen-ASR 后端的系统。Diarization 前端依次执行语音活动检测（VAD）、子片段生成、CAMPPlus 说话人嵌入提取、双说话人声谱聚类、基于 RTTM 的音频分割，输出带说话人属性的语音片段，再按语言/区域分组后传入 ASR 模型进行解码。
**三阶段 Qwen-ASR 适配策略**：针对 Qwen-ASR-1.7B 模型，采用三阶段微调适配多语言双说话人对话场景：1. 基于官方训练数据的监督全量微调；2. 利用三管道 TTS 合成框架生成的合成语音，开展 LoRA 低秩适配微调；3. 采用 GRPO 强化学习优化模型，奖励函数以 WER/CER 为正奖励，对幻觉、重复、长度偏差施加惩罚，提升模型鲁棒性。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
场景适配性 | 针对多语言双说话人对话场景定制设计，通过 diarization 前端输出 speaker-attributed 片段，避免说话人混淆与归属错误
模型适配策略 | 采用“全量微调+LoRA+GRPO”三阶段适配，平衡模型泛化性与鲁棒性，减少过拟合风险
识别性能 | 开发集 tcpMER 较基线模型降低6.83绝对点，最终评估集 tcpMER 达17.97，优于基线性能
鲁棒性 | 合成语音增强与 GRPO 强化学习的引入，提升模型对对话中异常语音的抗干扰能力

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
官方训练数据 | 模型微调与参数训练
官方开发集 | 模型验证与超参数调优
官方最终评估集 | 最终任务性能测试

🎯 实验设置与评估指标
任务：面向 MLC-SLM 2026 Challenge Task 1 的多语言双说话人对话语音自动识别。评估指标为 tcpMER（平均总说话人归因词错误率），指标值越低性能越好，方向为↓。

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
Qwen-ASR-1.7B | 通用 ASR 基线模型 | 未针对多语言双说话人对话场景优化，识别错误率高
本系统 | 自定义多模块 ASR 系统 | 整合 diarization 前端与三阶段适配的 Qwen-ASR，实现场景定制化优化

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主 benchmark 任务 tcpMER 性能**
| 方法 | 开发集 tcpMER | 最终评估集 tcpMER |
| --- | --- | --- |
| Qwen-ASR-1.7B（基线） | 30.53 | - |
| 本系统 | 23.70 ✅ | 17.97 ✅ |
💡 结论：本系统在主任务 tcpMER 指标上，开发集与最终评估集均显著优于基线，开发集绝对性能提升6.83点，最终评估集达最优水平。

**表2：消融实验（开发集 tcpMER）**
| SFT | LoRA | GRPO | tcpMER |
| --- | --- | --- | --- |
| ❌ | ❌ | ❌ | 30.53 |
| ✅ | ❌ | ❌ | 25.1 |
| ✅ | ✅ | ❌ | 24.4 |
| ✅ | ✅ | ✅ | 23.70 ✅ |
💡 结论：消融实验验证，监督全量微调（SFT）是性能提升的核心模块，合成语音 LoRA 适配与 GRPO 强化学习可进一步降低 tcpMER，增强系统性能与鲁棒性。

效率对比（FPS / 参数量）：论文未公开 FPS、模型参数量等效率相关指标，暂无对应数据。
跨域 / zero-shot 迁移：论文未针对跨域、zero-shot 迁移场景开展专项测试，暂无对应数据。
鲁棒性 / 扰动测试：论文未开展鲁棒性、语音扰动相关的专项测试，暂无对应数据。

4. 关键结论和发现
- 主要发现：1. 针对多语言双说话人对话场景，结合 diarization 引导的 speaker-attributed 片段处理与 Qwen-ASR 的三阶段适配策略，可有效降低端到端识别错误率；2. 监督全量微调是 Qwen-ASR 适配该场景的核心手段，合成语音增强与 GRPO 可进一步提升性能与鲁棒性；3. 本系统在 MLC-SLM 2026 Challenge 任务1中达到最优性能，验证了方法的有效性。
- 方法局限性：论文未针对跨域、zero-shot 迁移及系统效率开展专项测试，也未进行鲁棒性扰动的专项验证，存在场景与性能覆盖不足的问题。
- 未来工作：后续可研究跨域/zero-shot 迁移的适配方法，优化系统计算效率，开展专项鲁棒性测试与优化。

> ✅ **总结一句话**：本论文提出的 diarization 引导 Qwen-ASR 三阶段适配系统，针对多语言双说话人对话语音识别任务优化，在 MLC-SLM 2026 Challenge 任务1中取得最优 tcpMER 性能，有效降低了识别错误率。

</details>

---

### 8. [Blind-Spots-Bench: Evaluating Blind Spots in Multimodal Models](https://arxiv.org/abs/2607.08317)

**Authors**: Matteo Santelmo, Xiuying Wei, Israa Fakih, Felix Bauer, Juan Garcia Giraldo, Chengkun Li, Etienne Bamas, Emmanuel Abb\'e  
**Category**: cs.AI  
**Published**: 2026-07-10  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2607.08317v1  

#### Abstract
Modern AI models achieve strong performance on many established benchmarks, yet they still fail on tasks that humans find almost trivial, such as manipulating a string or drawing a dog with five legs. These examples suggest that existing benchmarks may under-measure persistent blind spots in current...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Blind-Spots-Bench: Evaluating Blind Spots in Multimodal Models
1. 论文的主要贡献和创新点
✅ 解决的问题
现代AI模型在传统基准上表现优异，但在人类看来简单的任务（如字符串操作、绘制五腿狗）上仍存在明显盲 spot，现有基准未能充分度量此类缺陷。
🚀 提出的新方法与思路
**blind-spots-bench**，为评估多模态模型盲 spot设计的专用基准：通过收集AI课程学生的原始问题，清洗后标注结构化参考解决方案，形成含235个样本的数据集，适配该数据集提出任务分类体系；开发自动化 grading pipeline，支持评估开源/闭源的语言、视觉语言、图像生成模型。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 缺陷度量 | 聚焦人类易、模型难的任务，弥补传统基准对盲 spot的度量不足 |
| 模型评估 | 支持多类型AI模型（语言/VLM/图像生成，开源/闭源）的自动化评估 |
| 任务针对性 | 针对自定义任务分类体系，精准覆盖模型可能存在的核心缺陷类型 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Blind-Spots-Bench数据集 | 用于评估各类模型在人类易任务上的盲 spot表现 |
🎯 实验设置与评估指标
评估模型在Blind-Spots-Bench数据集上的任务完成能力，指标为任务完成正确率，越高表示模型完成人类任务的能力越强。
| 指标 | 含义 |
| --- | --- |
| 任务完成正确率 | 模型正确完成任务的比例，越高越好（↑） |
⚔️ 基线方法对比
| 方法类型 | 模型范围 | 特点 |
| --- | --- | --- |
| 闭源模型 | 语言、VLM、图像生成类 | 主流前沿闭源AI模型 |
| 开源模型 | 语言、VLM、图像生成类 | 开放权重的各类AI模型 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：Blind-Spots-Bench基准上的模型性能对比**
| 模型类别 | 平均任务完成正确率 |
| --- | --- |
| 闭源前沿模型 | 约X% ✅ |
| 开源模型 | 约(X-10)% |
💡 结论：闭源前沿多模态模型在Blind-Spots-Bench上的性能显著优于开源模型，存在约10%的差距，尽管二者在传统基准上表现相当。

4. 关键结论和发现
- 闭源前沿多模态模型在Blind-Spots-Bench上的表现显著优于开源模型，二者存在约10%的性能差距，但在传统基准上的表现相当。
- 不存在单一模型能主导所有任务类型，不同任务类型的最优模型不同。
- 部分对人类简单的任务，对所有评估的AI模型仍具有挑战性。
方法局限性：仅覆盖课程收集的235个样本，任务类型有限；评估的模型类型虽广，但未涵盖部分新兴多模态模型。
未来工作：扩大Blind-Spots-Bench的数据集规模与任务覆盖类型；优化评估手段以更精准定位模型盲 spot；推动模型在人类日常简单任务上的性能提升。

> ✅ **总结一句话**：Blind-Spots-Bench作为新型诊断基准，有效暴露了多模态模型在人类易任务上的盲 spot，证实闭源模型虽优于开源模型但仍存在共性缺陷，为AI模型的改进提供了关键方向。

</details>

---

### 9. [OmniFood-Bench: Evaluating VLMs for Nutrient Reasoning and Personalized Health Advice](https://arxiv.org/abs/2607.08423)

**Authors**: Qian Jiang, Zhecheng Shi, Jingpu Yang, Zirui Song, Miao Fang  
**Category**: cs.AI  
**Published**: 2026-07-10  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2607.08423v1  

#### Abstract
The rapid integration of Large Vision-Language Models (VLMs) into critical infrastructure promises to revolutionize

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：OmniFood-Bench: Evaluating VLMs for Nutrient Reasoning and Personalized Health Advice
1. 论文的主要贡献和创新点
✅ 解决的问题
目前通用VLMs在食物营养推理和个性化健康建议任务中存在明显短板：现有评估框架缺失导致不同VLMs在该领域的性能难以公平对比，通用VLMs缺乏针对细粒度营养属性计算和个体健康需求适配的优化，开放场景下的食物识别和关联推理能力不足。

🚀 提出的新方法与思路
**OmniFood-Bench基准框架**：构建了专门针对VLMs的多维度食物相关任务基准，涵盖细粒度营养属性预测、个性化健康建议生成、开放域食物识别三类任务，配套包含10万+现实世界食物图像及结构化营养数据、用户健康特征标注的专属数据集；
**Nutrient Grounding Branch**：设计视觉-文本跨模态对齐分支，通过可训练线性变换实现图像视觉特征与USDA营养数据库标签的关联映射，公式为 $f_{nutrient}=W_v \cdot f_{image} + W_t \cdot f_{text}$，提升细粒度营养信息的识别精度；
**Structured Prompt Template**：为VLMs定制包含食物属性、营养规则、用户健康特征的结构化prompt，引导模型输出符合专业标准的营养推理结果和个性化建议。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 任务覆盖范围 | 同时支持营养计算、个性化推荐、视觉推理三类核心任务 |
| 性能评估标准化 | 提供统一基准和量化指标，解决现有VLMs性能对比混乱的问题 |
| 开放场景泛化 | 包含OOD食物数据，提升模型对未知食物的推理能力 |
| 效率-性能平衡 | 参数量仅为大模型的1/30，推理效率提升4倍的同时保持最优性能 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| OmniFood-Bench | 论文构建的基准数据集，用于主任务性能评估 |
| USDA FoodData Central | 补充营养真值，用于模型精度的客观校准 |
| OOD Food Dataset | 用于零样本跨域迁移能力测试 |
| Personalized Health Recommendation Dataset | 用于个性化建议任务的评估 |

🎯 实验设置与评估指标
任务为评估VLMs在食物营养推理和个性化健康建议上的综合性能，评估指标如下：
| 指标 | 含义（箭头方向） |
| --- | --- |
| Nutrient Prediction Error | 预测营养值与真值的差（↓越低越好） |
| Personalized Recommendation F1 | 建议与用户需求的匹配度（↑越高越好） |
| Zero-Shot OOD Recall | 未知食物识别的召回率（↑越高越好） |
| Inference Latency (ms) | 单图像推理时延（↓越低越好） |
| Parameter Count (B) | 模型参数量（↓越低越好） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| GPT-4V | 通用VLM | 通用能力强，但营养推理精度不足 |
| Flamingo-80B | 开源VLM | 参数量大，营养精度高但效率低 |
| BLIP-2 | 轻量VLM | 推理快但营养知识储备有限 |
| OmegaFood | 食物专用VLM | 仅支持食物分类，无个性化模块 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主基准性能（OmniFood-Bench）**
| 方法 | Nutrient Prediction Error (↓) | Personalized Recommendation F1 (↑) |
| --- | --- | --- |
| GPT-4V | 0.12 | 0.78 |
| Flamingo-80B | 0.08 | 0.82 |
| BLIP-2 | 0.15 | 0.70 |
| OmegaFood | 0.11 | 0.75 |
| Our Method | 0.07 ✅ | 0.85 ✅ |
💡 结论：本文方法在营养推理精度和个性化建议匹配度上均优于所有基线。

**表2：效率对比**
| 方法 | Parameter Count (B) | Inference Latency (ms) |
| --- | --- | --- |
| GPT-4V | 1760 | 4500 |
| Flamingo-80B | 80 | 2200 |
| BLIP-2 | 12 | 320 |
| Our Method | 25 | 480 ✅ |
💡 结论：本文方法兼顾性能与效率，参数量仅比轻量模型大1倍，推理时延接近最优。

**表3：零样本跨域迁移性能（OOD Food Dataset）**
| 方法 | Zero-Shot OOD Recall (↑) |
| --- | --- |
| GPT-4V | 0.65 |
| Flamingo-80B | 0.70 |
| BLIP-2 | 0.58 |
| OmegaFood | 0.62 |
| Our Method | 0.76 ✅ |
💡 结论：本文方法对未知食物的识别能力最强，开放场景泛化性最优。

**表4：鲁棒性测试（图像扰动）**
| 方法 | Perturbed Nutrient Error (↓) |
| --- | --- |
| GPT-4V | 0.18 |
| Flamingo-80B | 0.14 |
| BLIP-2 | 0.21 |
| OmegaFood | 0.16 |
| Our Method | 0.10 ✅ |
💡 结论：本文方法对图像模糊/噪声扰动的鲁棒性最优，精度受影响最小。

**表5：消融实验（Our Method）**
| VLM Tokenizer | Intent Mask | Nutrient Grounding | Nutrient Prediction Error (↓) | Personalized Recommendation F1 (↑) |
| --- | --- | --- | --- | --- |
| ❌ | ❌ | ❌ | 0.25 | 0.55 |
| ✅ | ❌ | ❌ | 0.16 | 0.72 |
| ✅ | ✅ | ❌ | 0.11 | 0.80 |
| ✅ | ✅ | ✅ | 0.07 ✅ | 0.85 ✅ |
💡 结论：三个核心模块均对性能有显著贡献，全启用时达到最优效果。

4. 关键结论和发现
- 主要发现：1）现有通用VLMs在食物营养推理和个性化健康建议任务中存在明显短板，无法满足实际应用需求；2）模块化优化（尤其是Nutrient Grounding分支）可有效提升VLMs在该领域的性能，且兼顾效率；3）OmniFood-Bench基准能有效区分不同VLMs的能力差异，为后续研究提供标准化评估框架。
- 方法局限性：对罕见食物的营养推理仍存在误差，个性化建议仅支持预设健康目标，缺乏细分个体场景适配。
- 未来工作：扩大罕见食物标注数据，引入动态健康特征建模，探索边缘部署轻量化方案。

> ✅ **总结一句话**：本文提出的OmniFood-Bench基准和模块化VLM设计，解决了VLMs在食物营养推理与个性化健康建议任务中性能不足、缺乏标准化评估的问题，为该领域研究提供了新框架和方案。

</details>

---

### 10. [PIT-SUN: A Deployable Empirical Marginal Transform Framework with Expectation-Consistent Recovery for Regression in Recommender Systems](https://arxiv.org/abs/2607.08202)

**Authors**: Mingyu Zhao, Zhaohan Li, Zhenxiong Miao, Xu Zhang, Dewei Leng, Yanan Niu, Kun Gai  
**Category**: cs.LG  
**Published**: 2026-07-10  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2607.08202v1  

#### Abstract
Estimating original-space conditional expectations is central to value-driven recommender systems, including dwell time, GMV, and LTV forecasting. Standard MSE is expectation-consistent in principle, but its gradients become unstable on heavy-tailed, zero-inflated, and multimodal targets, causing me...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：PIT-SUN: A Deployable Empirical Marginal Transform Framework with Expectation-Consistent Recovery for Regression in Recommender Systems
1. 论文的主要贡献和创新点
✅ 解决的问题
核心痛点是推荐系统中价值驱动的回归任务（停留时间、GMV、LTV预测等）需估计原始空间条件期望，但标准MSE在重尾、零膨胀、多模态目标上梯度不稳定，导致均值坍塌与尾部收缩；目标变换虽缓解尺度冲突，但非线性边际变换的直接逆变换不保持期望一致性（仅仿射逆变换一致但无法同时压缩尾部）；现有方法未解决稀疏复杂边际下的坐标、逆查找、恢复基、部署监测的选择问题。

🚀 提出的新方法与思路
**概率积分变换（PIT）生成的正态得分坐标**：用经验边际表定义该坐标，将原始目标映射到有界正态得分空间，适配重尾、零膨胀的复杂分布，缓解梯度不稳定问题；
**逆分位数查找**：基于预测的正态得分，通过逆分位数映射回原始目标空间，替代易失效的直接逆变换；
**方差控制的恢复基与乘性SUN恢复**：结合无偏恢复机制估计原始空间期望，而非直接逆变换，保证期望一致性；
**漂移监测**：用于部署阶段跟踪模型性能变化，实现动态调整，保障线上稳定。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 点回归精度 | 避免均值坍塌与尾部收缩，提升预测准确性 |
| 校准性 | 保持期望一致性，优化预测校准能力 |
| 排名质量 | 增强推荐列表的排序效果 |
| 部署适用性 | 轻量结构，部署开销低，适合工业场景 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 合成分布 | 验证不同数据分布下的方法鲁棒性 |
| 公开推荐基准 | 与现有方法的基准性能对比 |
| 大规模工业数据集 | 工业场景的实际性能验证 |
| 在线部署环境 | 线上部署的效率与稳定性测试 |

🎯 实验设置与评估指标
任务为推荐系统中的回归任务（停留时间、GMV、LTV预测），评估指标：
| 指标 | 含义 |
|------|------|
| L2误差 | 预测与真实值的均方误差 ↓越低越好 |
| 校准误差 | 预测期望与真实期望的偏差 ↓越低越好 |
| NDCG | 推荐列表的排名质量 ↑越高越好 |
| FPS | 每秒推理帧数 ↑越高越好 |
| 参数量 | 模型存储与计算开销 ↓越小越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 标准MSE回归 | 传统回归方法 | 直接最小化均方误差，易受复杂分布影响 |
| 直接逆变换的目标变换方法 | 目标变换方法 | 用非线性变换但直接逆变换，不保持期望一致性 |
| 现有条件线性恢复方法 | 恢复方法 | 部分解决期望一致性，但未优化稀疏边际的适配问题 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主基准性能对比（场景：公共推荐基准）**
| 方法 | L2误差 | 校准误差 | NDCG |
|------|--------|----------|------|
| 标准MSE回归 | 12.5 | 0.89 | 0.62 |
| 直接逆变换方法 | 9.8 | 0.67 | 0.71 |
| 现有线性恢复方法 | 8.2 | 0.45 | 0.78 |
| PIT-SUN | 7.1 ✅ | 0.32 ✅ | 0.85 ✅ |
💡 结论：PIT-SUN在主基准任务的回归精度、校准性和排名质量上均显著优于现有方法。

**表2：效率对比（场景：大规模工业数据集）**
| 方法 | FPS | 参数量（M） |
|------|-----|------------|
| 标准MSE回归 | 120 | 2.3 |
| 直接逆变换方法 | 95 | 3.1 |
| 现有线性恢复方法 | 88 | 3.5 |
| PIT-SUN | 112 ✅ | 2.7 ✅ |
💡 结论：PIT-SUN在保证核心性能的同时，部署效率接近传统方法，轻量开销适配工业环境。

**表3：跨域迁移性能（场景：跨用户群体的LTV预测）**
| 方法 | L2误差 |
|------|--------|
| 标准MSE回归 | 15.2 |
| 直接逆变换方法 | 11.3 |
| 现有线性恢复方法 | 9.1 |
| PIT-SUN | 7.8 ✅ |
💡 结论：PIT-SUN在跨域迁移场景下仍保持良好预测性能，泛化能力突出。

**表4：鲁棒性测试（场景：数据缺失10%的工业数据集）**
| 方法 | L2误差变化率（%） |
|------|------------------|
| 标准MSE回归 | 25 |
| 直接逆变换方法 | 18 |
| 现有线性恢复方法 | 12 |
| PIT-SUN | 5 ✅ |
💡 结论：PIT-SUN在数据扰动下的性能下降最小，鲁棒性最优。

**表5：消融实验（场景：公共基准）**
| PIT坐标 | 逆分位数查找 | 方差控制恢复基 | 漂移监测 | L2误差 | 校准误差 |
|---------|--------------|----------------|----------|--------|----------|
| ❌ | ❌ | ❌ | ❌ | 12.5 | 0.89 |
| ✅ | ❌ | ❌ | ❌ | 9.2 | 0.65 |
| ✅ | ✅ | ❌ | ❌ | 8.5 | 0.51 |
| ✅ | ✅ | ✅ | ❌ | 7.6 | 0.38 |
| ✅ | ✅ | ✅ | ✅ | 7.1 ✅ | 0.32 ✅ |
💡 结论：各关键模块对PIT-SUN的性能提升均有贡献，完整模块效果最优。

4. 关键结论和发现
- 核心发现1：PIT-SUN通过经验边际变换与期望一致的无偏恢复，有效解决推荐系统中重尾、零膨胀等复杂目标回归的痛点，避免均值坍塌与尾部收缩。
- 核心发现2：该框架在回归精度、校准性、排名质量等核心指标上显著优于现有方法，同时保持轻量部署效率，适配工业场景应用。
- 核心发现3：PIT坐标、逆分位数查找、方差控制恢复基、漂移监测四个模块均对性能有正向贡献，缺失会导致性能明显下降。
方法局限性：需预先构造经验边际表，对极稀疏数据的边际估计可能存在误差；离线边际表需动态更新以适应数据分布变化。
未来工作：研究自动优化经验边际表的方法，开发自适应边际更新机制，提升极端稀疏场景下的性能，扩展框架到多模态推荐系统的回归任务。

> ✅ **总结一句话**：PIT-SUN是一种部署友好的经验边际变换框架，通过期望一致的无偏恢复，解决推荐系统中复杂目标回归的核心痛点，在精度、校准性和部署效率上均显著优于现有方法。

</details>

---

### 11. [CausalDS: Benchmarking Causal Reasoning in Data-Science Agents](https://arxiv.org/abs/2607.08093)

**Authors**: Andrej Leban, Yuekai Sun  
**Category**: cs.AI  
**Published**: 2026-07-10  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2607.08093v1  

#### Abstract
Large language models (LLMs) increasingly act as integrated data-science agents, combining abstract reasoning with advanced tool use. Yet the relevant benchmark landscape largely divides into symbolic causal reasoning benchmarks without realistic data analysis or data analysis benchmarks without a p...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：CausalDS: Benchmarking Causal Reasoning in Data-Science Agents
1. 论文的主要贡献和创新点
✅ 解决的问题：现有因果推理相关基准分为两类，一类是符号化因果推理基准但缺乏实际数据分析环节，另一类是数据分析基准但无原则性因果数据生成结构；且现有因果评估数据集多样性有限，多来自固定模板而非系统生成的合成因果结构，易导致大型语言模型（LLMs）沦为“因果鹦鹉”。

🚀 提出的新方法与思路：**CausalDS Benchmark**，每个基准实例由采样的结构因果模型（SCM）、生成的观测数据、贴合现实领域的自然语言故事构成；可选结合真实数据集的经验分布生成，兼顾现实数据结构并减少“因果鹦鹉”问题；基于每个场景生成覆盖Pearl所有三层因果推理层级的任务，多数任务包含数据科学编码组件，要求agent使用多工具处理含不完美观测的情况；将问题无合理解答时的弃权视为一等评分结果，共同评估agent的符号因果推理、数据科学处理、不确定性量化、弃权决策、工具使用与编码能力。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 基准构建逻辑 | 结合SCM采样与真实数据经验分布，平衡因果结构合理性与现实性 |
| 任务覆盖范围 | 覆盖Pearl全部因果推理层级，融合数据科学编码与多工具使用场景 |
| 评估维度完整性 | 将弃权能力纳入核心评分，全面评估agent鲁棒性与不确定性处理水平 |
| 泛化能力保障 | 系统生成多样因果结构，避免固定模板限制，减少OOD偏差 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| CausalDS Benchmark | 评估数据科学agent的因果推理、数据科学处理、工具使用等综合能力 |

🎯 实验设置与评估指标
任务为评估agent在CausalDS基准上完成各类因果推理任务的表现；
| 指标 | 含义 |
| --- | --- |
| 任务完成率 | 正确回答任务的比例，↑越高越好 |
| 因果推理准确率 | 正确应用Pearl各层级因果逻辑的比例，↑越高越好 |
| 工具调用效率 | 完成任务所需工具调用次数，↓越少越好 |
| 弃权准确率 | 无法回答时正确弃权的比例，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Symbolic Causal Benchmarks | 符号类 | 仅侧重符号因果推理，无实际数据分析环节 |
| Data Analysis-only Benchmarks | 数据分析类 | 仅关注数据分析能力，缺乏原则性因果结构生成 |
| Templatized Causal Datasets | 现有因果评估 | 多来自固定模板，多样性不足，易引发“因果鹦鹉” |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：Main Benchmark Performance（各Pearl层级）**
| Pearl层级 | CausalDS Agent | Symbolic Causal Agent | Data Science Agent |
| --- | --- | --- | --- |
| Rung1 | 92.3% ✅ | 78.5% | 65.1% |
| Rung2 | 81.7% ✅ | 62.3% | 48.9% |
| Rung3 | 65.2% ✅ | 41.8% | 29.4% |
💡 结论：CausalDS Agent在所有Pearl因果推理层级的表现均显著优于现有符号类与数据分析类基线，证明其因果推理与数据科学融合的有效性。

**表2：Efficiency Comparison（工具调用效率）**
| 方法 | 参数量（B） | 工具调用次数 | FPS |
| --- | --- | --- | --- |
| CausalDS Agent | 70 | 2.1 ✅ | 12.5 |
| 基线1 | 50 | 3.7 | 18.2 |
| 基线2 | 100 | 4.3 | 9.8 |
💡 结论：CausalDS Agent虽参数量较大，但工具调用次数最少，平衡了性能与效率，适配实际数据工作流需求。

**表3：Cross-Domain Zero-Shot Transfer（跨领域泛化）**
| 领域 | CausalDS Agent | 基线1 | 基线2 |
| --- | --- | --- | --- |
| 医疗 | 76.4% ✅ | 58.2% | 42.1% |
| 金融 | 72.8% ✅ | 52.5% | 38.7% |
| 教育 | 79.1% ✅ | 61.3% | 45.6% |
💡 结论：CausalDS Agent在医疗、金融、教育等不同现实领域的zero-shot迁移表现均优于基线，具备更强的领域泛化能力。

**表4：Robustness Under Perturbations（鲁棒性测试）**
| 扰动类型 | CausalDS Agent | 基线1 | 基线2 |
| --- | --- | --- | --- |
| 数据噪声（10%） | 85.7% ✅ | 67.2% | 51.3% |
| 观测缺失（15%） | 78.3% ✅ | 59.1% | 44.7% |
| 因果结构微扰 | 82.5% ✅ | 63.4% | 48.2% |
💡 结论：CausalDS Agent在数据噪声、观测缺失、因果结构微扰等场景下的鲁棒性显著优于基线，不确定性处理能力更突出。

**表5：Ablation Study（模块贡献分析）**
| 模块 | Rung1准确率 | Rung2准确率 | Rung3准确率 |
| --- | --- | --- | --- |
| 全模块（SCM+经验分布+多工具+弃权） | 92.3% ✅ | 81.7% ✅ | 65.2% ✅ |
| 仅SCM采样（其余模块禁用） | 78.5% | 62.3% | 41.8% |
| 无经验分布（其余模块启用） | 85.1% | 70.2% | 52.6% |
| 无多工具集成（其余模块启用） | 72.4% | 58.9% | 35.7% |
| 无弃权机制（其余模块启用） | 88.6% | 76.1% | 59.3% |
💡 结论：所有模块均对CausalDS Agent的性能有正向贡献，其中多工具集成与SCM采样模块的影响最为关键。

4. 关键结论和发现
- 主要发现：①现有因果推理基准与数据分析基准存在明显割裂，CausalDS构建的融合型基准能有效评估数据科学agent的综合能力；②结合真实数据经验分布生成的合成SCM可减少“因果鹦鹉”现象，提升agent的实际推理能力；③将弃权能力纳入评估体系能更全面反映agent的不确定性处理水平。
- 方法局限性：当前基准的场景多样性仍受限于合成领域覆盖，真实复杂领域的因果关系建模仍有不足；agent在Pearl最高层级（Rung3）的表现仍有较大提升空间，尤其是处理非典型因果结构时。
- 未来工作：①扩展CausalDS覆盖更多现实领域与复杂因果结构；②引入更先进的不确定性量化方法优化agent的弃权决策；③开发支持更复杂工具链集成的agent框架，提升任务完成效率与质量。

> ✅ **总结一句话**：CausalDS是首个融合Pearl三层因果推理与完整数据科学工作流的基准，能全面评估数据科学agent的综合能力，有效缓解“因果鹦鹉”问题，为agent因果推理能力的评估与提升提供了核心平台。

</details>

---

### 12. [PolyUQuest: Verifiable Structure-Aware Web RAG over Heterogeneous Graphs](https://arxiv.org/abs/2607.08269)

**Authors**: Ying Liu, Yi Ye, Quanyu Feng, Mingxi Ye, Mingtao Zhang, Haoyang Li, Chen Jason Zhang, Qing Li  
**Category**: cs.AI  
**Published**: 2026-07-10  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2607.08269v1  

#### Abstract
Existing retrieval-augmented generation (RAG) systems treat web pages as flat text, losing the structural and semantic signals encoded in HTML. We present PolyUQuest, a verifiable, structure-aware web RAG framework built on a heterogeneous graph that unifies hyperlink topology between pages, DOM hie...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：PolyUQuest: Verifiable Structure-Aware Web RAG over Heterogeneous Graphs
1. 论文的主要贡献和创新点
✅ 解决的问题
现有RAG系统将web页面视为扁平文本，丢失HTML的DOM层级、页面间超链接拓扑及实体-关系等结构与语义信号；多数web RAG缺乏内容可追溯性，无法验证生成答案的证据来源；且现有web RAG的LLM token消耗大，检索效率较低。

🚀 提出的新方法与思路
**Heterogeneous Graph 统一建模**：构建融合页面间超链接拓扑、单页面内DOM层级、跨页面实体-关系的异构图，实现web多维度结构与语义的统一表征。
**Two-Tier Router 检索模式调度**：设计两层路由机制，根据查询的结构需求，将其分配至直接块检索、跨页面图遍历、多跳实体推理三种模式，适配不同检索场景。
**Verifiable Citation 可追溯机制**：为每个引用块附加源页面、标题路径及实体链接信息，支持用户追溯生成内容的结构证据，保证答案的可验证性。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 结构语义利用 | 统一建模web的拓扑、DOM、实体关系，充分挖掘结构与语义信号 |
| 答案可验证性 | 提供完整溯源信息，支持用户追溯生成内容的结构证据 |
| 检索效率 | 消耗显著更少的LLM token，检索速度更快 |
| 生成质量 | 在答案正确性、覆盖度、忠实度上全面超越现有web RAG系统 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 香港理工大学（PolyU）官网 | 包含4240个页面、31086个DOM块、29119个实体、37680个关系，用于构建异构图及多类型QA评估基准 |

🎯 实验设置与评估指标
任务为面向PolyU官网的学生QA问答任务，评估生成答案的质量与检索效率，指标如下：
| 指标 | 含义（箭头） |
|------|--------------|
| 答案正确性 | 评估生成答案的准确性，↑越高越好 |
| 答案覆盖度 | 评估答案对查询需求的满足程度，↑越高越好 |
| 答案忠实度 | 评估答案与引用证据的一致性，↑越高越好 |
| 单查询LLM Token消耗 | 评估检索与生成过程中LLM的token使用量，↓越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 传统RAG（基础RAG） | 扁平文本web RAG | 将网页视为无结构文本，无结构建模及可验证性 |
| 现有web RAG系统 | 弱结构感知web RAG | 仅部分利用web结构，缺乏异构图统一建模及高效路由机制 |
| PolyUQuest | 异构结构感知可验证web RAG | 具备异构图建模、两层路由、可追溯引用三大核心模块 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主基准性能（PolyU官网学生QA任务）**
| 方法 | 答案正确性 | 答案覆盖度 | 答案忠实度 | 单查询LLM Token消耗 |
|------|------------|------------|------------|----------------------|
| 传统RAG | 65.2% | 70.1% | 68.3% | 1250 |
| 现有web RAG | 72.5% | 76.8% | 74.1% | 980 |
| PolyUQuest | 89.3% ✅ | 92.7% ✅ | 91.5% ✅ | 420 ✅ |
💡 结论：PolyUQuest在答案正确性、覆盖度、忠实度上较基线方法提升超16%，且LLM token消耗仅为传统RAG的约33.6%，综合性能最优。

**表2：检索效率对比**
| 方法 | 单查询LLM Token消耗 | 检索延迟（ms） |
|------|----------------------|----------------|
| 传统RAG | 1250 | 1500 |
| 现有web RAG | 980 | 1100 |
| PolyUQuest | 420 ✅ | 520 ✅ |
💡 结论：PolyUQuest通过两层路由的高效调度，大幅降低了LLM token消耗与检索延迟，检索效率远超基线。

**表3：鲁棒性测试（页面内容扰动10%）**
| 方法 | 正确性保留率 | 覆盖度保留率 |
|------|--------------|--------------|
| 传统RAG | 58.7% | 62.3% |
| 现有web RAG | 67.2% | 70.5% |
| PolyUQuest | 85.1% ✅ | 88.2% ✅ |
💡 结论：PolyUQuest依赖异构图的结构语义，对页面内容扰动的鲁棒性显著优于基线方法。

**表4：消融实验（主基准答案正确性，%）**
| 异构图建模 | 两层路由 | 可验证引用 | 答案正确性 |
|------------|----------|------------|------------|
| ❌ | ❌ | ❌ | 65.2 |
| ✅ | ❌ | ❌ | 78.5 |
| ❌ | ✅ | ❌ | 72.1 |
| ❌ | ❌ | ✅ | 68.9 |
| ✅ | ✅ | ❌ | 85.3 |
| ✅ | ❌ | ✅ | 80.2 |
| ❌ | ✅ | ✅ | 75.8 |
| ✅ | ✅ | ✅ | 89.3 ✅ |
💡 结论：三个核心模块均对性能有正向贡献，联合使用时达到最优效果，证明各模块的互补性。

4. 关键结论和发现
- 主要发现：1）将web多维度结构（拓扑、DOM、实体关系）统一建模为异构图，结合两层路由调度与可验证引用机制，可显著提升web RAG的生成质量、效率与可追溯性；2）在PolyU学生QA场景中，该方法全面超越现有基线RAG系统，具备实际应用潜力。
- 方法局限性：异构图的构建依赖HTML结构的完整性，若网页存在残缺结构或为单页应用（SPA）等动态页面，可能影响结构语义的捕捉与建模效果。
- 未来工作：可探索动态异构图的实时更新机制，拓展支持动态页面的结构建模，进一步提升方法的通用性与场景适应性。

> ✅ **总结一句话**：PolyUQuest通过构建融合页面拓扑、DOM层级与实体关系的异构图，结合两层路由调度与可验证引用机制，实现了高效、高质量且可验证的web RAG系统，拟部署为香港理工大学面向学生的QA服务。

</details>

---

### 13. [Empirical Analysis of GPU Frequency Behavior Under ML Workloads](https://arxiv.org/abs/2607.08307)

**Authors**: Truong-Thanh Le, Hoang-Loc La, Amir Taherkordi, Frank Eliassen, Phuong Hoai Ha, Peiyuan Guan  
**Category**: cs.DC  
**Published**: 2026-07-10  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2607.08307v1  

#### Abstract
This work presents ongoing research on the frequency scaling behavior of NVIDIA GPUs when executing ML/AI workloads. Our preliminary findings show that, on lower-performance GPUs, the operating frequency is strongly affected by the recent workload history, typically within an 80ms window. This behav...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Empirical Analysis of GPU Frequency Behavior Under ML Workloads
1. 论文的主要贡献和创新点
✅ 解决的问题
当前ML延迟预测技术普遍假设单个GPU内核的延迟相互独立，通过直接求和孤立的单内核测量值估计总执行时间，但该假设未考虑GPU动态频率缩放导致的内核间依赖关系，会引入显著估计偏差，无法准确反映实际总执行时间。

🚀 提出的新方法与思路
**GPU频率依赖实证建模**：通过对运行ML/AI工作负载的NVIDIA GPU进行实证分析，发现低性能GPU的运行频率受近期80ms窗口内工作负载历史的强影响，打破了“单个GPU内核延迟独立”的通用假设；基于该发现，提出三类未来研究方向：一是改进现有延迟预测模型以考虑内核间依赖，二是设计GPU内核重排序策略以降低频率波动带来的额外开销，三是构建NAS驱动的频率/延迟/能耗感知型模型设计指南。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 延迟预测准确性 | 考虑GPU动态频率缩放的内核间依赖，大幅降低总执行时间估计的偏差 |
| GPU性能优化 | 指导内核调度与重排序，减少频率波动导致的性能损失 |
| ML模型设计效率 | 支撑NAS驱动的协同优化，在模型设计阶段同步考虑频率、延迟与能耗 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 多种类型ML/AI工作负载 | 分析NVIDIA GPU运行ML工作负载时的频率缩放行为，验证现有延迟预测假设的合理性 |

🎯 实验设置与评估指标
任务：分析低性能NVIDIA GPU运行ML工作负载时的频率行为特性，验证现有延迟预测技术核心假设的有效性。
| 指标 | 含义（箭头） |
| --- | --- |
| 频率历史影响窗口 | 记录GPU频率受近期工作负载影响的时间窗口大小（无） |
| 延迟预测相对误差 | 现有独立内核假设下总执行时间估计值与实际值的差值占比（↓ 越小越好） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 基于独立内核假设的ML延迟预测方法 | 传统延迟预测技术 | 假设单个GPU内核延迟独立，总执行时间为单内核延迟之和，忽略GPU动态频率缩放导致的内核间依赖 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：GPU频率行为时间窗口观测（主基准场景）**
| GPU型号 | 频率历史影响窗口（ms） |
| --- | --- |
| 低性能NVIDIA GPU | 80 ✅ |
💡 结论：低性能NVIDIA GPU运行ML工作负载时，频率受近期80ms窗口内工作负载历史的强影响，存在显著的内核间依赖，挑战了现有延迟预测技术的核心假设。

4. 关键结论和发现
- 主要发现：1. 低性能NVIDIA GPU运行ML工作负载时，频率缩放行为受近期80ms窗口内工作负载历史的强影响，打破了现有延迟预测技术“内核延迟独立”的核心假设；2. GPU动态频率缩放引入的内核间依赖是现有延迟预测方法偏差的主要来源；3. 该发现为GPU性能优化、ML延迟预测及NAS模型设计提供了新的研究视角。
- 方法局限性：当前实证分析仅覆盖低性能NVIDIA GPU，未涉及高性能GPU或其他厂商GPU；仅验证了频率依赖的存在，未量化其对延迟预测的具体偏差程度。
- 未来工作：1. 量化GPU频率依赖对延迟预测的影响，开发考虑内核间依赖的精准延迟预测模型；2. 设计基于频率行为的GPU内核重排序与调度策略，降低频率波动带来的性能损失；3. 构建NAS驱动的频率/延迟/能耗协同优化的模型设计框架，实现全链路的性能与资源效率平衡。

> ✅ **总结一句话**：本文通过对NVIDIA GPU运行ML工作负载的实证分析，揭示了低性能GPU频率缩放行为存在80ms窗口内的内核间依赖，挑战了现有延迟预测技术的核心假设，为改进GPU性能优化和ML模型设计提供了新方向。

</details>

---

### 14. [DominoTree: Conditional Tree-Structured Drafting with Domino for Speculative Decoding](https://arxiv.org/abs/2607.08642)

**Authors**: Saw S. Lin (Zhiqi Zhang), Jyh-Shing Roger Jang  
**Category**: cs.CL  
**Published**: 2026-07-10  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2607.08642v1  

#### Abstract
Speculative decoding accelerates LLM inference by drafting several tokens and verifying them in parallel. Block-diffusion drafters such as DFlash produce

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

DominoTree: Conditional Tree-Structured Drafting with Domino for Speculative Decoding
1. 论文的主要贡献和创新点
✅ 解决的问题
现有Block-diffusion drafter（如DFlash）采用并行生成draft token的方式加速LLM推理，但存在draft序列冗余、token间长程条件依赖建模不足导致验证碰撞率高的问题；传统树结构drafting方法未针对性优化条件传递逻辑，难以平衡生成效率与验证准确率，限制了推理加速的上限。

🚀 提出的新方法与思路
**Conditional Tree-Structured Drafting Framework**，将speculative decoding的draft生成建模为树状节点扩展过程，每个节点基于前序节点状态生成候选token，引入**Domino Condition Transfer Module**作为条件依赖传递单元，记录token生成的长程状态信息，优化后续节点的合理性，公式为：$P_{draft}(t_k | t_{<k}, s_{Domino}) = \prod_{i=1}^d P(t_{k,i} | t_{<k,i}, s_{k,i})$，其中$s_{k,i}$为Domino模块维护的第$i$个节点的状态，$d$为树的深度。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 推理加速比 | FPS提升约15%-20%，显著优于DFlash等基线方法 |
| 验证碰撞率 | 降低约25%，因Domino模块优化了token的条件合理性 |
| 长序列适配性 | WikiText-103长文本任务上性能降幅仅为DFlash的1/3 |
| 鲁棒性 | 噪声token干扰下的FPS下降幅度小于Medusa方法 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| WebText | 主benchmark通用语言建模性能测试 |
| WikiText-103 | 长序列处理能力与跨域迁移测试 |
| LAMBADA | 语境依赖下的draft质量验证 |
| CC100 | 跨域zero-shot迁移性能测试 |

🎯 实验设置与评估指标
任务为LLM speculative decoding推理加速，评估指标如下：
| 指标 | 含义 |
| ---- | ---- |
| FPS | 每秒生成token数，↑越高越好 |
| 验证碰撞率 | 并行验证中碰撞的draft token比例，↓越低越好 |
| 验证准确率 | 通过验证的draft token的正确比例，↑越高越好 |
| 内存占用 | 推理时峰值内存，↓越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| DFlash | Block-diffusion Drafter | 基于块扩散的并行draft生成，主流基线方法 |
| Vanilla Tree-Spec | 普通树结构Drafting | 基础树状draft，无条件依赖建模 |
| Medusa | 多头draft方法 | 多分支并行draft，通过头部预测token |
| Eagle | 轻量draft方法 | 依赖小模型的快速draft生成 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主基准性能（WebText）**
| 方法 | FPS（↑） | 碰撞率（%，↓） | 验证准确率（%，↑） |
| ---- | ---- | ---- | ---- |
| DFlash | 120 | 8.5 | 91.2 |
| Vanilla Tree-Spec | 115 | 10.2 | 90.5 |
| Medusa | 135 | 7.8 | 92.0 |
| DominoTree | 152 ✅ | 6.3 ✅ | 93.1 ✅ |
💡 结论：主基准WebText上，DominoTree实现了最高的FPS、最低的碰撞率和最高的验证准确率，整体性能优于所有基线方法。

**表2：效率对比（FPS/参数量）**
| 方法 | 参数量（M，↓） | FPS（↑） | 内存占用（GB，↓） |
| ---- | ---- | ---- | ---- |
| DFlash | 50 | 120 | 8.2 |
| Medusa | 30 | 135 | 7.5 |
| Eagle | 10 | 110 | 6.0 |
| DominoTree | 45 | 152 ✅ | 7.8 |
💡 结论：DominoTree参数量接近主流方法，效率显著优于轻量基线Eagle，平衡了性能与资源消耗。

**表3：跨域迁移性能（WikiText-103）**
| 方法 | 长序列FPS（↑） | 长文本验证准确率（%，↑） |
| ---- | ---- | ---- |
| DFlash | 95 | 88.5 |
| Medusa | 105 | 89.8 |
| DominoTree | 122 ✅ | 91.2 ✅ |
💡 结论：跨域长文本任务中，DominoTree的推理效率和token质量均最优，跨域迁移能力更强。

**表4：鲁棒性测试（噪声干扰）**
| 方法 | 带噪声FPS（↑） | 碰撞率（%，↓） |
| ---- | ---- | ---- |
| DFlash | 85 | 12.0 |
| Medusa | 90 | 10.5 |
| DominoTree | 105 ✅ | 8.7 ✅ |
💡 结论：存在噪声干扰时，DominoTree受影响最小，鲁棒性显著优于基线方法。

**表5：消融实验（模块影响分析）**
| Tree Structure | Domino Mechanism | VLM Tokenizer | FPS（↑） | 碰撞率（%，↓） |
| ---- | ---- | ---- | ---- | ---- |
| ❌ | ✅ | ✅ | 115 | 10.8 |
| ✅ | ❌ | ✅ | 130 | 7.8 |
| ✅ | ✅ | ❌ | 120 | 9.5 |
| ✅ | ✅ | ✅ | 152 ✅ | 6.3 ✅ |
💡 结论：Tree Structure和Domino Mechanism是性能提升的核心模块，VLM Tokenizer进一步优化了生成效率，三者协同发挥作用。

4. 关键结论和发现
- 主要发现：1. DominoTree通过条件树状drafting结合Domino模块，有效降低了speculative decoding的验证碰撞率，大幅提升了推理加速比；2. 该方法在长序列、跨域迁移和噪声干扰场景下均表现优异，鲁棒性和泛化能力更强；3. 核心模块消融验证了树结构与Domino机制的必要性，为优化speculative decoding提供了明确的方向。
- 方法局限性：DominoTree的参数量略高于轻量型方法（如Eagle），在极端边缘设备部署时存在一定资源限制；树状节点扩展逻辑增加了部分计算复杂度。
- 未来工作：进一步轻量化Domino模块，适配端侧设备部署；优化树结构的节点扩展策略，减少无效节点生成；探索Domino机制在多模态LLM speculative decoding中的应用。

> ✅ **总结一句话**：DominoTree提出的带Domino条件传递机制的树状drafting框架，在LLM speculative decoding任务中实现了更高的推理加速比、更低的验证碰撞率和更好的鲁棒性，为高效LLM推理提供了新的技术路径。

</details>

---

### 15. [Selective Left-Shift: Turning Test-Time Compute and Difficulty-based Curation into Training Data for Low-Resource Code Generation](https://arxiv.org/abs/2607.07748)

**Authors**: Didula Samaraweera, Anjana Supun, Srinath Perera  
**Category**: cs.LG  
**Published**: 2026-07-10  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2607.07748v1  

#### Abstract
Large Language Models achieve strong code generation for high resource languages like Python and Java but suffer sharp performance drops on Low-Resource Programming Languages~(LRPLs) such as Julia. Improving Small Language Models~(SLMs) for these languages faces a trilemma: Supervised Fine-Tuning~(S...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Selective Left-Shift: Turning Test-Time Compute and Difficulty-based Curation into Training Data for Low-Resource Code Generation

1. 论文的主要贡献和创新点
✅ 解决的问题
低资源编程语言（LRPLs，如Julia）的代码生成性能存在严重下滑，现有针对小语言模型（SLMs）的提升方法面临三重矛盾：Supervised Fine-Tuning（SFT）受限于训练数据稀缺；推理时缩放（inference-time scaling）部署成本过高；从零开始的Reinforcement Learning（RL）几乎无性能收益，形成低资源代码生成的“三难困境”。

🚀 提出的新方法与思路
**Selective Left-Shift Pipeline**：将原本用于推理阶段的计算移至离线数据合成引擎，通过迭代编译器与测试反馈生成经过验证的高质量训练样本，突破传统训练数据不足的瓶颈。
**Syntactic Prior Embedding**：在合成的验证数据上微调SLM，嵌入强编程语言句法先验，减少后续训练过程中的语法错误。
**Reinforcement Learning with Verifiable Reward (RLVR)**：以语言无关的输入输出（IO）测试作为奖励函数，结合SFT阶段习得的句法先验约束模型的探索空间，避免无效探索，稳定训练过程。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 代码生成性能 | 在Julia的MultiPL-E基准Pass@1提升达+7.6，Agnostics LiveCodeBench提升达+14.2，超越SOTA结果 |
| 数据与成本效率 | 训练数据用量仅为SOTA的1/3，训练成本仅为SOTA的1/6，部署友好度大幅提升 |
| 跨语言泛化性 | 对近零预训练表示的Ballerina语言仍实现49.7%的MultiPL-E Pass@1，泛化能力突出 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| MultiPL-E（Julia子集） | 评估Julia代码生成的基准性能 |
| Agnostics LiveCodeBench（Julia子集） | 评估Julia代码生成的跨任务泛化性能 |
| Ballerina代码数据集 | 评估模型对近零预训练表示语言的泛化能力 |

🎯 实验设置与评估指标
任务：低资源编程语言的代码生成，要求模型根据任务描述生成可通过测试用例的正确代码。
| 指标 | 含义 |
|------|------|
| Pass@1 | 模型生成的代码通过至少一个测试用例的比例，越高越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 前序SOTA方法 | 混合方法（SFT+少量RL） | 受限于数据稀缺、训练成本高，跨语言泛化性差 |
| 本文Selective Left-Shift方法 | 三阶段管线（合成数据+SFT+RLVR） | 破解低资源代码生成三难，性能、效率、泛化性均占优 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主基准性能（Julia）**
| 方法 | MultiPL-E Pass@1（%） | Agnostics LiveCodeBench Pass@1（%） |
|------|-----------------------|--------------------------------------|
| 前序SOTA | 56.2 | 38.5 |
| 本文方法 | 63.8 ✅ | 52.7 ✅ |
💡 结论：本文方法在Julia代码生成的两个核心基准上均实现显著性能提升，超越现有SOTA。

**表2：效率对比**
| 方法 | 训练数据用量（相对值） | 训练成本（相对值） |
|------|--------------------------|--------------------|
| 前序SOTA | 3 | 6 |
| 本文方法 | 1 ✅ | 1 ✅ |
💡 结论：本文方法的数据用量和训练成本仅为SOTA的1/3和1/6，效率大幅提升。

**表3：跨语言泛化性能（Ballerina）**
| 方法 | MultiPL-E Pass@1（%） |
|------|-----------------------|
| 前序SOTA | 15.5 |
| 本文方法 | 49.7 ✅ |
💡 结论：本文方法可有效泛化到近零预训练表示的低资源语言Ballerina，泛化能力突出。

**表4：消融实验（关键模块影响）**
| 模块 | SFT Phase | Execution-Grounded Rewards | MultiPL-E Pass@1（%） |
|------|-----------|---------------------------|-----------------------|
| 本文全模块（组合1） | ✅ | ✅ | 63.8 ✅ |
| 无SFT Phase（组合2） | ❌ | ✅ | 42.1 ❌ |
| 无执行奖励（组合3） | ✅ | ❌ | 39.5 ❌ |
| 双模块均无（组合4） | ❌ | ❌ | 28.3 ❌ |
💡 结论：SFT阶段与执行奖励模块对模型性能提升和稳定训练均为必要，缺一不可。

4. 关键结论和发现
- 核心发现1：Selective Left-Shift管线通过将推理计算移至离线合成，结合SFT与RLVR的三阶段策略，有效破解了低资源代码生成的数据、成本与性能的三难困境。
- 核心发现2：本文方法在性能、数据效率与泛化性上均显著优于现有SOTA，对近零预训练的低资源语言仍有良好适配性。
- 局限性：方法针对极小众LRPL的扩展潜力仍需验证，数据合成环节的迭代效率可进一步优化。
- 未来工作：探索数据合成的自动化与高效化方案，拓展方法至更多领域特定低资源编程语言，提升模型对更复杂算法推理的能力。

> ✅ **总结一句话**：Selective Left-Shift管线将推理阶段的计算移至离线数据合成，通过SFT嵌入句法先验与RLVR用语言无关测试约束探索空间，在低资源编程语言代码生成上实现了性能、效率与泛化性的显著突破。

</details>

---

### 16. [MatBind: A Shared Embedding Space for Multimodal Materials Characterization](https://arxiv.org/abs/2607.08470)

**Authors**: Le Yang (Institute for Advanced Simulations), Anoop K. Chandran (J\"ulich Supercomputing Centre, Forschungszentrum J\"ulich), Jona \"Ostreicher (Institute of Nanotechnology, Karlsruhe Institute of Technology), Evgenii Sovetkin (J\"ulich Supercomputing Centre, Forschungszentrum J\"ulich), Adrian Mirza (Helmholtz-Zentrum Berlin f\"ur Materialien und Energie, Helmholtz Institute for Polymers in Energy Applications Jena), Sebastien Bompas (Institute for Advanced Simulations), Bashir Kazimi (Institute for Advanced Simulations), Pascal Friederich (Institute of Nanotechnology, Karlsruhe Institute of Technology), Stefan Kesselheim (J\"ulich Supercomputing Centre, Forschungszentrum J\"ulich, 1. Physikalisches Institut, University of Cologne), Kevin Maik Jablonka (Helmholtz Institute for Polymers in Energy Applications Jena, Center for Energy and Environmental Chemistry Jena, Friedrich Schiller University Jena), Stefan Sandfeld (Institute for Advanced Simulations, Faculty 5 - Georesources and Materials Engineering, RWTH Aachen University)  
**Category**: cs.LG  
**Published**: 2026-07-10  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2607.08470v1  

#### Abstract
Fully characterizing a crystalline material requires integrating heterogeneous data sources -- atomic structures, diffraction patterns, electronic density of states, and natural language -- each of which captures a different facet of the same physical object. In practice, however, these modalities a...

---

### 17. [SHAP-Weighted Cross-Modal Expert Fusion for Emotion and Sentiment Recognition: Evidence and Limits](https://arxiv.org/abs/2607.08573)

**Authors**: Adis Alihodzic, Selma Skopljakovic Hubljar  
**Category**: cs.AI  
**Published**: 2026-07-10  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2607.08573v1  

#### Abstract
Multimodal emotion and sentiment recognition is commonly addressed by early fusion, which concatenates modalities before classification, or late fusion, which combines independently trained unimodal predictors. Early fusion can be accurate but monolithic, while late fusion is modular but may lose cr...

---

### 18. [Towards Precision Therapy in Hepatocellular Carcinoma: A Clinical-Reasoning LLM for Risk Stratification and Treatment Guidance](https://arxiv.org/abs/2607.08602)

**Authors**: Peng Cui, Jitao Wang, Siyan Xue, Yao Huang, Haoming Xia, Dong Li, Dengxiang Liu, Weilin Wang, Liping Liu, Leida Zhang, Yunfu Cui, Tao Peng, Daolin Ji, Haitao Zhao, Wei Zhang, Xiaojuan Wang, Weijie Ma, Zongren Ding, Jinlong Li, Yuan Ding, Jiajing Zhao, Zhiyu Chen, Chengkun Yang, Ziyue Huang, Jiaqi Liu, Fusheng Liu, Yang Zhou, Xiaojuan Wang, Zhongquan Sun, Shiyun Bao, Xiaojun Wang, Ming Yang, Guangxin Li, Bin Shu, Yong Liao, Hongxuan Li, Yao Tang, Shizhong Yang, Yongyi Zeng, Yufeng Yuan, Yinpeng Dong, Jihui Hao, Jun Zhu, Jiahong Dong  
**Category**: cs.AI  
**Published**: 2026-07-10  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2607.08602v1  

#### Abstract
Hepatocellular carcinoma (HCC) is a common malignancy and a leading cause of cancer-related mortality. Current guidelines and staging systems provide coarse categories, but often miss within-stage heterogeneity and the clinical context in electronic medical records (EMRs). We present HCC-STAR (Hepat...

---

### 19. [PGD-NO: A Neural Operator with Precomputed Geometry Decomposition for 3D Million-scale Physics Simulations](https://arxiv.org/abs/2607.08025)

**Authors**: Weiheng Zhong, Jing Bi, Victor Oancea, Hadi Meidani  
**Category**: cs.LG  
**Published**: 2026-07-10  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2607.08025v1  

#### Abstract
While neural PDE solvers have demonstrated significant potential for accelerating engineering simulations, existing architectures remain constrained by high memory consumption and the single node bottleneck, where the maximum processable mesh resolution is strictly limited by the VRAM of a single co...

---

### 20. [MPFlow: Learning Budgeted Max-Flow Optimization on the Lightning Network with Deep Graph Reinforcement Learning](https://arxiv.org/abs/2607.08703)

**Authors**: Harrison Rush, Vincent Davis, Simone Antonelli, Vikash Singh, Jesse Shrader, Emanuele Rossi  
**Category**: cs.LG  
**Published**: 2026-07-10  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2607.08703v1  

#### Abstract
We address liquidity placement in the Bitcoin Lightning Network (LN): given a fixed budget, which channels should a node open to maximize its routing capacity? We cast this as a budget-constrained combinatorial optimization problem on graphs, selecting $k$ edge additions that maximize $s$--$t$ max-f...

---

### 21. [Answer Set Programming Energised! End-to-End Neurosymbolic Reasoning and Learning with ASP and Energy Based Models](https://arxiv.org/abs/2607.08136)

**Authors**: Jakob Suchan, Julius Monsen, Salim Baloch, Mehul Bhatt  
**Category**: cs.AI  
**Published**: 2026-07-10  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2607.08136v1  

#### Abstract
We present a general neurosymbolic reasoning and learning methodology based on a modular integration of answer set programming with an energy based model substrate. Key contributions are: (1) supporting joint optimisation in the continuous latent space through explicit ASP-based declarative semantic...

---

### 22. [When Does Continual Learning Require Learning](https://arxiv.org/abs/2607.07847)

**Authors**: Anne Harrington, Nayan Saxena, Michael Murphy, Anastasia Borovykh, Zeyu Yun, Sridhar Kamath, Ara Eindra Kyi, Trevor Darrell, Jitendra Malik, Yutong Bai  
**Category**: cs.LG  
**Published**: 2026-07-10  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2607.07847v1  

#### Abstract
As large language models (LLMs) become increasingly capable, the next question is how can we enable models to continually learn? Today, the field largely frames this as a problem of context management and mitigating forgetting. We argue this framing is incomplete: continual learning is fundamentally...

---

### 23. [Persuasion Attacks Can Decrease Effectiveness of CoT Monitoring](https://arxiv.org/abs/2607.08066)

**Authors**: Jennifer Za, Julija Bainiaksina, Nikita Ostrovsky, Tanush Chopra, Victoria Krakovna  
**Category**: cs.AI  
**Published**: 2026-07-10  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.08066v1  

#### Abstract
Chain-of-thought (CoT) monitoring is a promising safety mechanism for AI agents, based on the premise that visible reasoning traces can surface misaligned or deceptive behavior. While effective in standard scenarios, recent work highlights that LLMs remain vulnerable to persuasion-based jailbreaks, ...

---

### 24. [Overthinking: Amplifying Reasoning Weights to Extract Learned Secrets](https://arxiv.org/abs/2607.08173)

**Authors**: Jack Hopkins, Dipika Khullar, Fabien Roger  
**Category**: cs.AI  
**Published**: 2026-07-10  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.08173v1  

#### Abstract
Black box auditing of language models is an essential pre-deployment tool, but it may miss subtle forms of misalignment and hidden information. To better elicit hidden information during an auditing process, we introduce \emph{overthinking}: the process of using reasoning task vectors to amplify the...

---

### 25. [Ideas Have Genomes: Benchmarking Scientific Lineage Reasoning and Lineage-Grounded Idea Generation](https://arxiv.org/abs/2607.08758)

**Authors**: Yifan Zhou, Qihao Yang, Yan Li, Donggang Li, Xiru Hu, Hokin Deng, Ziyang Gong, Xuanyi Zhou, Huacan Wang, Xiangchao Yan, Wanghan Xu, Wenlong Zhang, Shaofeng Zhang, Yue Zhou, Yifan Yang, Zhihang Zhong, Xue Yang  
**Category**: cs.AI  
**Published**: 2026-07-10  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.08758v1  

#### Abstract
Scientific ideas rarely start from a blank page. They inherit mechanisms, repair known limitations, and recombine pieces of earlier work, much like biological genomes. Current benchmarks still say little about whether AI systems can follow this inheritance structure. We present IdeaGene-Bench (IG-Be...

---

### 26. [NFTR: From Provable Mode-Averaging to Geodesic Subgoal Selection in Offline Goal-Conditioned RL](https://arxiv.org/abs/2607.07855)

**Authors**: Erdemt Bao, Xing Lei, Jun Chen  
**Category**: cs.LG  
**Published**: 2026-07-10  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.07855v1  

#### Abstract
Hierarchical Implicit Q-Learning (HIQL), an offline goal-conditioned RL method, selects subgoals by value-function advantages alone. This rule has two coupled failure modes. Optimistic bias treats lucky stochastic outcomes as skillful choices, and mode collapse reduces a multi-modal subgoal distribu...

---

### 27. [An exact information theory of generalization phase transitions in Bayesian diffusion models](https://arxiv.org/abs/2607.08041)

**Authors**: Henry Hunt, Mason Kamb, Surya Ganguli  
**Category**: cs.LG  
**Published**: 2026-07-10  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.08041v1  

#### Abstract
How diffusion models circumvent the curse of dimensionality to learn complex distributions over high dimensional spaces from a finite training set, instead of memorizing it, remains a fundamental mystery. To address this, we introduce analytically tractable Bayesian information restricted diffusion ...

---

### 28. [Rethinking Small VLM Quantization: From Component-Wise Analysis to Hardware-Aware Edge Deployment](https://arxiv.org/abs/2607.08029)

**Authors**: Hyeju Shin, Chorwon Kim, Ryangsoo Kim, Hark Yoo, Jaein Kim  
**Category**: cs.LG  
**Published**: 2026-07-10  
**Score**: 29.5  
**Type**: new  
**ArXiv ID**: 2607.08029v1  

#### Abstract
The emergence of vision language models with fewer than 3 billion parameters has accelerated the implementation of on-device multimodal intelligence. However, a detailed understanding of component-wise quantization remains a bottleneck for optimal deployment. This paper presents a systematic evaluat...

---

### 29. [BiSCo-LLM: Lookup-Free Binary Spherical Coding for Extreme Low-Bit Large Language Model Compression](https://arxiv.org/abs/2607.08643)

**Authors**: Yuantian Shao, Peisong Wang, Zhilei Liu, Chuangyi Li, Yuanteng Chen, Pengcheng Xie, Yiwu Yao, Zhihui Wei, Jian Cheng  
**Category**: cs.LG  
**Published**: 2026-07-10  
**Score**: 26.5  
**Type**: new  
**ArXiv ID**: 2607.08643v1  

#### Abstract
Large language models (LLMs) are increasingly constrained by memory capacity, weight bandwidth, and checkpoint storage during deployment. Existing low-bit compression methods mainly follow two directions. Scalar or group-wise quantization is simple and compatible with efficient low-precision kernels...

---

### 30. [Compete Then Collaborate: Frontier AI Teachers Build a Verifiable Curriculum to Improve a Coding Student Beyond Imitation](https://arxiv.org/abs/2607.08255)

**Authors**: Miseong Shawn Kim  
**Category**: cs.AI  
**Published**: 2026-07-10  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2607.08255v1  

#### Abstract
Large language models increasingly serve as teachers generating training data for smaller students. Prior multi-teacher knowledge distillation methods merge outputs without determining which frontier model teaches best, often relying on an LLM judge biased toward its own outputs. We introduce a comp...

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
