# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-09-07 10:49:37 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [ConsensusBench: Benchmark of Consensus Nodes for LLM Reasoning via Outcome Reward Densifying](https://arxiv.org/abs/2609.04648v1)

**Authors**: Shi-Qi Yan, Chao-Hong Tan, Qian Chen, Wen Wang, Xiangang Li, Zhen-Hua Ling  
**Category**: cs.CL  
**Published**: 2026-09-07  
**Score**: 64.5  
**Type**: new  
**ArXiv ID**: 2609.04648v1  

#### Abstract
Reinforcement learning (RL) has become one of the primary paradigms for reasoning enhancement of large language models (LLMs). In particular, Group Relative Policy Optimization (GRPO) and related algorithms have demonstrated strong performance with outcome-level rewards. However, these methods depen...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：ConsensusBench: Benchmark of Consensus Nodes for LLM Reasoning via Outcome Reward Densifying
1. 论文的主要贡献和创新点
✅ 解决的问题
RL（如GRPO）用于LLM推理增强时，仅依赖最终答案的稀疏结果奖励，缺少对中间推理步骤的反馈；随着任务复杂度提升、推理轨迹长度增加，这类稀疏结果奖励的局限性愈发凸显。现有方法（GRPO）仅采用结果级奖励，无过程级反馈，应对长复杂推理时奖励不足。

🚀 提出的新方法与思路
**ConsensusBench**：新基准数据集，用于提供基于规则的过程级信号；通过过滤N次rollout的正确轨迹，聚类语义等价的中间语句得到可验证的子结果（Consensus Nodes）。
**ConsensusPR**：将基于Consensus Nodes的规则式过程奖励整合到GRPO类算法中的新强化学习信号，以减少长推理轨迹中结果奖励的稀疏性。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
奖励机制 | 补充结果级奖励的不足，引入过程级信号以减少长推理轨迹的奖励稀疏性
推理表现 | 在多个推理数据集上优于GRPO类算法

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
AIME 2024 | LLM推理性能评估
AIME 2025 | LLM推理性能评估
GSM8K | LLM推理性能评估
MATH-500 | LLM推理性能评估
ConsensusBench | 基准测试，提供过程级信号评估

🎯 实验设置与评估指标
任务为LLM数学推理任务，评估指标如下：
指标 | 含义
--- | ---
Final Answer Accuracy (Acc) | 最终答案正确率，越高越好
Node Coverage Rate (NCR) | Consensus节点覆盖率，越高越好
Tokens per Node (TPN) | 每个Consensus节点的平均token数，越低越好

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
GRPO | 强化学习算法 | 仅使用结果级奖励，无过程级反馈

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告具体的表号、数值及对应表现细节，仅说明在上述数据集上所提方法优于GRPO类方法。
2. 效率对比：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现
1. 从多rollout的正确推理轨迹中可聚类得到语义等价的Consensus Nodes，作为有效的过程级信号；
2. 整合Consensus Nodes的过程奖励（ConsensusPR）可减少长推理轨迹的结果奖励稀疏性，进而提升LLM推理性能。
- 方法局限性：论文未报告
- 未来工作：论文未报告

✅ **总结一句话**：本文提出ConsensusBench数据集和ConsensusPR算法，通过引入Consensus节点的过程奖励缓解长推理轨迹的奖励稀疏问题，在多个LLM推理任务中表现优于GRPO类算法。

</details>

---

### 2. [CoSkill: Joint Reinforcement Learning of Reasoning and Meta-Skill Agents for Hierarchical Skill Evolution](https://arxiv.org/abs/2609.04865v1)

**Authors**: Jinyuan Feng, Dongmin Li, Yiqun Chen, Yang Gao, Xing Chen, Huimu Wang, Zhiqiang Pu  
**Category**: cs.AI  
**Published**: 2026-09-07  
**Score**: 62.0  
**Type**: new  
**ArXiv ID**: 2609.04865v1  

#### Abstract
Skill libraries improve the sample efficiency of agentic reinforcement learning (RL) by enabling large language model (LLM) agents to reuse procedural knowledge. Yet existing paradigms exhibit structural shortcomings: they either decouple skill evolution from policy optimization or instantiate meta-...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

CoSkill: Joint Reinforcement Learning of Reasoning and Meta-Skill Agents for Hierarchical Skill Evolution
1. 论文的主要贡献和创新点
✅ 解决的问题
现有基于技能库的智能体强化学习范式存在结构缺陷：要么将技能演化与策略优化解耦，要么将元技能实例化为固定工作流，两类范式均把技能视为被动管理对象，限制了技能的灵活演化及其与推理智能体的协同适应能力。

🚀 提出的新方法与思路
**CoSkill统一多智能体强化学习框架**：将静态元技能工作流重塑为可学习的Meta-Skill Agent，与Reasoning Agent在分层技能库上开展联合训练；该框架将Reasoning Agent和Meta-Skill Agent建模为共享单一骨干网络的协作团队，实现端到端协同适应：Reasoning Agent基于检索到的任务技能及其子步骤技能选择动作，任务表现结果用于指导Meta-Skill Agent优化步骤技能。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 任务成功速率（ALFWorld） | 较基线方法提升3.5个百分点（达98.4%） |
| 任务成功速率（WebShop） | 较基线方法提升6.2个百分点（达90.6%） |
| 早期样本效率 | 优于现有基线方法 |
| 渐近性能 | 优于现有基线方法 |
| 时钟效率 | 优于现有基线方法 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| ALFWorld | 测试智能体任务完成性能与效率 |
| WebShop | 测试智能体任务完成性能与效率 |

🎯 实验设置与评估指标
任务：在ALFWorld和WebShop场景下，评估智能体完成对应任务的性能与效率表现。
| 指标 | 含义（箭头标方向） |
| --- | --- |
| 任务成功速率（%） | 越高越好（↑） |
| 早期样本效率 | 越高越好（↑） |
| 渐近性能 | 越高越好（↑） |
| 时钟效率 | 越高越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 现有基于技能的基线方法 | 基准方法 | 性能与效率均低于CoSkill |
| 现有强化学习基线方法 | 基准方法 | 性能与效率均低于CoSkill |

3. 主要实验结果和性能指标
📊 定量结果汇总
**论文未明确提供表号，相关结果见正文及图1**
论文仅在正文给出实验结果：CoSkill在ALFWorld任务上的成功速率为98.4%，在WebShop任务上的成功速率为90.6%，较现有基线方法分别提升3.5、6.2个百分点；如图1所示，CoSkill在早期样本效率、渐近性能、时钟效率上均优于所有对比基线方法。
💡 结论：CoSkill在ALFWorld和WebShop两个任务场景下的任务完成性能及运行效率均显著优于现有基于技能和强化学习的基线方法。
其余需覆盖的实验项：跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验均为论文未报告。

4. 关键结论和发现
- 主要发现：1. CoSkill通过将静态元技能转化为可学习的Meta-Skill Agent，与Reasoning Agent在分层技能库上联合训练，实现了技能的灵活演化及与推理智能体的端到端协同适应；2. 在ALFWorld和WebShop任务场景中，CoSkill的任务成功速率及效率表现均大幅超越现有基线方法。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：CoSkill提出的将可学习Meta-Skill Agent与Reasoning Agent在分层技能库上联合训练的统一多智能体强化学习框架，解决了现有技能库范式限制技能演化与协同适应的缺陷，在ALFWorld和WebShop场景下实现了任务性能与效率的显著提升。

</details>

---

### 3. [Budgeting Bytes: A Windowed Storage Roofline and Dual-Budget Architecture Ablations for Storage-Bound LLM Decoding](https://arxiv.org/abs/2609.04238v1)

**Authors**: Hanhaodi Zhang  
**Category**: cs.AR  
**Published**: 2026-09-07  
**Score**: 56.5  
**Type**: new  
**ArXiv ID**: 2609.04238v1  

#### Abstract
Autoregressive decoding on cheap hardware is bound not by FLOPs but by the bytes each generated token must move across the slowest populated tier of a memory hierarchy. We treat bytes-per-token as a first-class design axis, organized by an address-determinism taxonomy that classifies parameters by w...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Budgeting Bytes: A Windowed Storage Roofline and Dual-Budget Architecture Ablations for Storage-Bound LLM Decoding
1. 论文的主要贡献和创新点
✅ 解决的问题：自回归解码在廉价硬件上的性能瓶颈并非FLOPs，而是每个生成token需在存储层次最慢层间移动的字节数；现有预取方法（如基于时间局部性的预取、带完美预测的trace驱动预取）因总线饱和无法减少跨层字节量，导致预取无效，无法突破存储绑定的性能天花板。
🚀 提出的新方法与思路：
**地址确定性分类法（address-determinism taxonomy）**：将参数按token前向传播过程中获取其地址的时间分为A0（token采样时）、A1（注意力前）、A2（层间数据依赖）、A3（总需读取）四类，将预取调度问题转化为带释放时间的单机器可行性问题；
**窗口存储屋顶线（Windowed Storage Roofline）**：基于上述分类推导得到闭式性能边界表达式，为存储绑定的LLM解码提供量化分析工具；
**双预算架构消融（Dual-Budget Architecture Ablations）**：在三个sub-100M参数尺度模型上，开展基于“token级字节数×存储容量”双预算的架构消融分析。
🔍 相比现有方法的优势：
| 维度 | 优势 |
| ---- | ---- |
| 瓶颈定义方式 | 以bytes-per-token为第一级设计轴，替代传统仅关注FLOPs的屋顶线模型，更贴合廉价硬件的LLM解码场景 |
| 预取调度可行性 | 地址确定性分类法将预取调度转化为带释放时间的单机器问题，实现单机器下的预取可行性分析，而非仅理论规划 |
| 性能边界可解释性 | 窗口存储屋顶线可准确预测廉价硬件上LLM解码的性能天花板，如边缘板Qwen3-30B的预取无效问题，为优化提供明确指引 |
2. 核心实验方法和设置
📚 使用的数据集：论文未报告具体数据集。
🎯 实验设置与评估指标：任务为存储绑定的LLM解码性能评估；评估指标及含义：
| 指标 | 含义 |
| ---- | ---- |
| 每秒token数（tok/s） | LLM解码吞吐量，↑越高越好 |
| 专家路由预测准确率 | 专家路由决策的预测正确率，↑越高越好 |
⚔️ 基线方法对比：
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 基于时间局部性的预取 | 预取优化方法 | 利用数据时间局部性预取，论文指出其净负收益 |
| Trace驱动的oracle预取 | 预取优化方法 | 基于完美预测的预取，论文指出其无法突破总线饱和限制 |
| 量化适配方法 | 模型优化方法 | 通过量化压缩模型，使其适配快速存储层 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**无表N：边缘板Qwen3-30B模型性能实验（场景：8GB边缘板运行Qwen3-30B-A3B，4-bit量化，存储需求约18GB）**
| 实验场景 | 指标 | 数值 |
| ---- | ---- | ---- |
| 边缘板（原模型未适配） | 解码吞吐量 | 被eMMC带宽上限限制（论文未报告具体数值） |
| 16GB统一内存设备（量化适配） | 解码吞吐量 | 11.5 tok/s ✅ |
| 专家路由预测实验（A100 PCIe-offload路径） | 专家路由预测准确率 | 91.2% |
💡 结论：对于存储绑定的LLM解码，降低bytes-per-token（如量化）直至模型适配快速存储层，可大幅提升性能；专家路由高预测准确率（91.2%）仅在快速层缓存大部分模型时可转化为吞吐量，带宽受限的边缘存储无法实现该转化。

**消融实验（场景：三个sub-100M模型尺度的双预算架构消融）**
论文未报告具体实验结果数值，仅提及开展了该消融分析。

主benchmark性能、效率对比、跨域迁移、鲁棒性扰动测试：论文未报告。
4. 关键结论和发现
- 主要发现：1）廉价硬件上存储绑定的LLM解码的瓶颈是跨饱和总线的字节量，预取无法减少该字节量，因此无法提升性能；2）通过量化降低bytes-per-token使模型适配快速存储层，可实现大幅性能提升（本例中为22倍）；3）专家路由预测的高准确率（91.2%）是规模不变的属性，但仅在快速层缓存大部分模型时才能转化为实际吞吐量，带宽受限的边缘存储会阻断该转化。
- 方法局限性：边缘板这类资源有限设备上，即使采用预取技术，也无法突破总线饱和带来的带宽限制，仅能依赖量化适配快速存储层的方法优化性能。
- 未来工作：论文未报告。
✅ **总结一句话**：该论文提出以bytes-per-token为核心设计轴的窗口存储屋顶线模型，明确了廉价硬件上存储绑定的LLM解码的瓶颈为跨层字节量，验证了量化适配快速存储层可突破性能天花板，同时指出预取技术在带宽饱和场景下的无效性及专家路由预测转化为吞吐量的条件。

</details>

---

### 4. [MM-IFEval-Pro: A Multilingual and Attack-Resistant Benchmark for Instruction-Following in Vision-Language Models](https://arxiv.org/abs/2609.04859v1)

**Authors**: Changming Xiao, Zhenliang Ni, Jinhui He, Han Shu, Jie Hu  
**Category**: cs.AI  
**Published**: 2026-09-07  
**Score**: 55.5  
**Type**: new  
**ArXiv ID**: 2609.04859v1  

#### Abstract
As vision-language models (VLMs) rapidly advance in image understanding, cross-modal reasoning, and complex instruction execution, instruction-following capability has become a key indicator of their reliability and practicality. However, existing multimodal instruction-following benchmarks still su...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：MM-IFEval-Pro: A Multilingual and Attack-Resistant Benchmark for Instruction-Following in Vision-Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题：现有多模态指令跟随基准存在语言覆盖有限、对抗安全场景不足的缺陷，无法满足现实中多语言及安全敏感场景的评估需求。
🚀 提出的新方法与思路
**MM-IFEval-Pro基准**：该基准涵盖中文与英文任务、多样指令劫持案例，包含4大类任务及24个任务子类别，8类指令及52个指令子类别，每个样本平均包含3.0个约束，用于模拟复杂指令场景。
**含中文与对抗指令的强化学习训练集**：构建该训练集，用于优化视觉语言模型性能。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 语言覆盖 | 支持中文、英文双语任务覆盖 |
| 场景覆盖 | 包含多样指令劫持案例，具备对抗安全场景评估能力 |
| 指令复杂度 | 每个样本含平均3.0个约束，贴近现实复杂指令场景 |
| 泛化能力 | 相关训练集可实现跨任务、跨语言的性能迁移 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| MM-IFEval-Pro | 评估视觉语言模型的多模态指令跟随能力，覆盖中英任务、指令劫持场景及多约束样本 |
| 含中文与对抗指令的强化学习训练集 | 训练优化视觉语言模型，提升其在多模态指令跟随任务上的性能 |
🎯 实验设置与评估指标：论文未报告
⚔️ 基线方法对比：论文未报告
3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能（L2/碰撞率等）：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告
4. 关键结论和发现
- 主要发现：1）提出的MM-IFEval-Pro基准弥补了现有多模态指令跟随基准在语言覆盖和对抗安全场景上的不足；2）构建的含中文与对抗指令的强化学习训练集可提升模型性能，且能有效迁移至其他主流多模态基准，具备跨任务、跨语言泛化性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：论文提出支持中英双语、包含指令劫持案例的多模态指令跟随基准MM-IFEval-Pro，并构建含中文与对抗指令的强化学习训练集，缓解现有基准语言覆盖有限、对抗安全场景不足的问题，且训练集具备跨任务、跨语言泛化性。

</details>

---

### 5. [FlexPosit: Tunable Fractional Precision for LLM Inference Accelerators](https://arxiv.org/abs/2609.04724v1)

**Authors**: Yimin Gao, Liangtao Dai, Jun Yin, Xinfei Guo, Mircea Stan  
**Category**: cs.AR  
**Published**: 2026-09-07  
**Score**: 49.5  
**Type**: new  
**ArXiv ID**: 2609.04724v1  

#### Abstract
Large language models (LLMs) offer remarkable capabilities but impose prohibitive compute and energy costs. Quantization governs the trade-offs between accuracy and hardware efficiency across granularity and bit-width. Finer granularity (e.g., group-wise) provides high accuracy but incurs scaling an...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

FlexPosit: Tunable Fractional Precision for LLM Inference Accelerators
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾为LLM推理的计算与能耗成本过高，量化在精度与硬件效率间的权衡存在粒度缺陷：细粒度量化（如组量化）精度高但有缩放与控制开销，粗粒度量化（如通道量化）开销低但低精度下精度损失；混合精度量化算法上有丰富权衡，但现有LLM加速器仅支持离散精度模式，未探索中间的分数精度设计空间。
🚀 提出的新方法与思路
**FlexPosit**：通过Posit-based量化与精度可调的位串行架构协同设计解决上述问题。算法层面，采用感知分布的量化，结合硬件对齐、敏感度引导的混合精度分配，利用Posit格式的锥形精度，实现类组量化的精度与类通道量化的规则性；架构层面，构建统一的位串行脉动阵列，包含轻量的每列解码器、统一处理单元（PE）与全局精度控制器，在保持完全规则的脉动数据流的同时实现可调分数精度。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 精度 | 采用亚5位分数权重达到接近FP16的精度 |
| 吞吐量 | 优于现有组量化方法BitMoD与通道量化方法OliVe |
| 能耗 | 优于现有组量化方法BitMoD与通道量化方法OliVe |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |
🎯 实验设置与评估指标
任务为LLM推理加速。
| 指标 | 含义 |
| ---- | ---- |
| 吞吐量 | 越高越好（↑） |
| 能耗 | 越低越好（↓） |
| 精度 | 越高越好（接近FP16） |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| BitMoD | 组量化方法 | 细粒度量化，精度高但有缩放与控制开销 |
| OliVe | 通道量化方法 | 粗粒度量化，开销低但低精度下精度损失 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告

4. 关键结论和发现
- 主要发现：
  1. 现有LLM加速器在量化精度设计上局限于离散模式，未探索分数精度空间，存在精度与效率权衡的优化空间；
  2. 结合Posit格式的锥形精度与硬件协同设计，可同时实现类细粒度量化的精度与类粗粒度量化的硬件规则性；
  3. FlexPosit在LLM推理中达到接近FP16的精度，同时在吞吐量和能耗上优于现有组量化与通道量化方法，建立了新的Pareto前沿。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：FlexPosit通过Posit量化与精度可调位串行架构的协同设计，在LLM推理中实现了接近FP16的精度，同时在吞吐量和能耗上优于现有量化方法，为LLM加速器提供了新的精度-效率权衡方案。

</details>

---

### 6. [From Vision to Language: Investigating Causal Information Flow in Multimodal Decision-Making](https://arxiv.org/abs/2609.05149v1)

**Authors**: Davide Testa, Hugh Mee Wong, Alessandro Lenci, Bernardo Magnini, Albert Gatt  
**Category**: cs.CL  
**Published**: 2026-09-07  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2609.05149v1  

#### Abstract
Vision-Language Models are commonly evaluated through their final predictions, but understanding whether these decisions are grounded in visual evidence requires tracing how visual information contributes to language-based decisions. With this purpose in mind, we investigate cross-modal information ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

From Vision to Language: Investigating Causal Information Flow in Multimodal Decision-Making
1. 论文的主要贡献和创新点
✅ 解决的问题
现有Vision-Language Models（VLMs）的评估多聚焦于最终预测，缺少对其决策是否基于视觉证据的机制性理解，针对视频类多模态任务的跨模态信息流底层逻辑研究不足，未明确视觉信息如何影响语言决策过程。

🚀 提出的新方法与思路
**Layer-wise Causal Intervention**：在视频文本注意力路径上实施分层因果干预，针对空间、因果、时间三类视觉推理任务，追踪视觉信息对基于语言的多模态决策的因果影响。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 跨模态决策可解释性 | 通过分层因果干预明确视觉信息在VLMs中的整合阶段与作用机制 |
| 语义角色功能分析 | 区分名词作为语义锚、动词关联时间关系处理的不同语义角色功能 |
| 时间推理缺陷分析 | 揭示VLMs时间推理的序列信息重建缺陷及关联的语言表达偏差 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 视频-based生成式多选类似任务的多模态推理实验 |

🎯 实验设置与评估指标
任务：视频-based生成式多选类似的多模态决策任务，针对空间、因果、时间三类视觉推理开展分析。
| 指标 | 含义（箭头标方向） |
| --- | --- |
| 论文未报告 | 论文未报告 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能
论文未报告
2. 效率对比（FPS / 参数量）
论文未报告
3. 跨域 / zero-shot 迁移
论文未报告
4. 鲁棒性 / 扰动测试
论文未报告
5. 消融实验
论文未报告

4. 关键结论和发现
- 主要发现：
  1. 视觉信息主要在模型处理候选答案选项时整合，候选答案为最终决策的主要文本接地位点。
  2. 名词在多模态增强过程中扮演语义锚的角色，动词更与时间关系处理相关。
  3. VLMs在时间推理中难以重建视频帧间的序列信息，该脆弱性也可能源于场景事件时间关系表达的语言偏差。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文通过分层因果干预方法，在视频类多模态推理任务中揭示了VLMs跨模态决策的视觉信息流整合阶段、语义角色功能及时间推理缺陷，为VLMs的可解释性研究提供了新的分析路径。

</details>

---

### 7. [GNN-Guided Graph Coarsening and Adaptive QUBO Penalties for the Capacitated Vehicle Routing Problem with Time Windows on a Quantum Annealer](https://arxiv.org/abs/2609.04593v1)

**Authors**: Youssef Kamel Rezk, Pawe{\l} Gora  
**Category**: cs.LG  
**Published**: 2026-09-07  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2609.04593v1  

#### Abstract
Graph coarsening reduces the large Quadratic Unconstrained Binary Optimization (QUBO) formulations arising when vehicle-routing problems are solved by quantum annealing. Nearby customers with compatible time windows are merged into super-nodes, the reduced problem is solved, and the solution is expa...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

GNN-Guided Graph Coarsening and Adaptive QUBO Penalties for the Capacitated Vehicle Routing Problem with Time Windows on a Quantum Annealer
1. 论文的主要贡献和创新点
✅ 解决的问题
核心痛点：现有将带时间窗的容量车辆路径问题（CVRPTW）转化为二次无约束二元优化（QUBO）在量子退火上求解时，图粗化启发式存在家族特定调优需求、随机实例下不可靠的缺陷，且均匀罚项缩放效果差，手动调优的合并分数在部分实例可行性低。
现有方法缺陷：1）手动调优的图粗化合并分数依赖家族特定调优，在随机实例上表现不可靠；2）均匀罚项缩放对减少约束违反效果差；3）手动方法在R型实例、中大规模实例上的可行性低于预期。

🚀 提出的新方法与思路
**自适应罚项校准**：替代均匀罚项缩放，移除非绑定约束、归一化绑定约束、缩放剩余罚项，同时控制罚项内部系数范围，以改善原始样本的约束满足效果，而非仅调整整体罚项尺度。
**GNN引导的合并分数替代手动调优合并分数**：用图神经网络（GNN）代替手动调优的合并分数，采用单套配置覆盖所有家族，实现粗化过程的通用性。
**硬件验证罚项条件效应**：在D-Wave Advantage2处理器上开展硬件实验，验证固定逻辑变量数时的罚项条件效应，辅助确认优化效果的来源。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 约束违反量 | 自适应罚项校准可将平均原始约束违反从33.0降至0.06，减少99.8%以上 |
| 粗化通用性 | GNN替代手动合并分数，单套配置适用于所有Solomon实例家族 |
| 小实例可行性 | N=10时所有Solomon家族可行性达100%，R型实例可行性较手动方法提升20% |
| 中大规模实例性能 | N=10~100时整体可行性达83%，手动方法为69%；N=80、100时可行性差异显著，QUBO规模缩小5~6倍 |
| 硬件端表现 | 固定逻辑变量数时可行样本率从0.02%提升至39% |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| Solomon基准 | 测试CVRPTW的求解性能 |

🎯 实验设置与评估指标
任务：用模拟退火和D-Wave Advantage2处理器在Solomon基准上求解CVRPTW
| 指标 | 含义（箭头方向） |
|------|------------------|
| 平均原始约束违反 | 越低越好 |
| 可行性 | 越高越好 |
| QUBO规模 | 越小越好 |
| 可行样本率 | 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 手动调优的图粗化启发式 | 粗化方法 | 需家族特定调优，在部分实例可行性低 |
| 均匀罚项缩放 | 罚项调整方法 | 对约束违反改善有限 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**自适应罚项校准实验（Solomon基准）**
| 指标 | 数值 |
|------|------|
| 原平均原始约束违反 | 33.0 |
| 优化后平均原始约束违反 | 0.06 ✅ |
| 统计显著性p值 | 3.7e-11 |
| 样本量n | 56 |
💡 结论：自适应罚项校准可大幅降低原始样本的约束违反，增益来自罚项条件而非问题规模。

**GNN引导粗化实验（Solomon基准）**
| 实例规模N | GNN方法可行性 | 手动方法可行性 | QUBO规模倍数（GNN/手动） |
|-----------|---------------|----------------|--------------------------|
| 10 | 100% ✅ | 80% | - |
| 10~100 | 83% ✅ | 69% | 5~6倍 |
| 80、100 | - | - | - |
💡 结论：GNN引导的粗化方法跨家族通用性强，在小、中实例上的可行性优于手动方法，且QUBO规模更小。

**硬件实验（D-Wave Advantage2）**
| 场景 | 可行样本率 |
|------|------------|
| 原罚项设置 | 0.02% |
| 自适应罚项设置 | 39% ✅ |
💡 结论：固定逻辑变量数时，自适应罚项可大幅提升硬件上的可行样本率，验证了罚项条件效应。

4. 关键结论和发现
- 主要发现：1）自适应罚项校准能有效减少量子退火求解CVRPTW时的约束违反，优化增益来自罚项条件而非问题规模；2）GNN引导的图粗化替代手动调优方法，实现了跨所有Solomon家族的粗化通用性，在中大规模实例上可行性和QUBO规模均更优；3）硬件端验证了自适应罚项可显著提升可行样本率，符合罚项条件效应。
- 方法局限性：论文未报告除经典局部搜索修复（作为参考边界）外的其他局限性。
- 未来工作：论文未报告。

> ✅ **总结一句话**：该论文提出自适应QUBO罚项校准和GNN引导的图粗化方法，在量子退火上针对CVRPTW求解，实现了更低的约束违反、更高的可行性与更小的QUBO规模，优于现有手动调优方法。

</details>

---

### 8. [DCFA: Dual-view Causal-inspired Attribution for Failure Reasoning in LLM-based Multi-agent Systems](https://arxiv.org/abs/2609.04749v1)

**Authors**: Zehao Wang, Lanjun Wang, Shilong Jin, Junjie Chen, Yanghua Xiao  
**Category**: cs.AI  
**Published**: 2026-09-07  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2609.04749v1  

#### Abstract
Large language model (LLM)-based multi-agent systems have experienced rapid growth in recent years. Despite their promise, such systems remain fragile, frequently exhibiting reasoning and coordination errors that can lead to system-level failures. Failure attribution in such systems relies on tracin...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

DCFA: Dual-view Causal-inspired Attribution for Failure Reasoning in LLM-based Multi-agent Systems
1. 论文的主要贡献和创新点
✅ 解决的问题
LLM驱动的多智能体系统存在推理与协调错误导致的系统级故障问题，故障归因面临两大核心挑战：一是浅层归因，现有方法仅捕获不完整检索、格式错误等 minor deviations，未定位系统故障的决定性原因；二是上下文退化，系统轨迹长度增加时，模型推理能力快速下降。

🚀 提出的新方法与思路
**DCFA**：训练-free的故障归因框架，由两个核心模块构成：
1. **全局模块**：从系统轨迹构建结构化因果启发的依赖图，用于识别系统故障的初始决定性错误；
2. **局部模块**：应用局部反事实启发的推理，优化上述因果启发的归因结果。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 浅层归因问题 | 解决现有方法仅识别 minor deviations的局限，定位系统故障的决定性原因 |
| 上下文退化问题 | 缓解系统轨迹长度增加引发的模型推理能力快速下降问题 |
| 模型属性 | 训练-free，无需额外训练 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| Who&When benchmark | 验证DCFA在LLM多智能体系统故障归因任务上的性能 |

🎯 实验设置与评估指标
任务：在Who&When基准上对LLM多智能体系统执行步骤级故障归因；指标：步骤级准确率（↑越高越好）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| DCFA | 提出方法 | 训练-free，含全局因果启发依赖图模块、局部反事实启发推理模块 |
| SOTA基线方法 | 基线方法 | 存在浅层归因（仅识别 minor deviations）与上下文退化问题，论文未详述基线训练属性 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能**：论文未报告（仅提及涉及六个LLMs的Who&When基准上DCFA提升步骤级准确率，未披露具体数值与对应表号/章节信息）；
**效率对比**：论文未报告；
**跨域/zero-shot迁移**：论文未报告；
**鲁棒性/扰动测试**：论文未报告；
**消融实验**：论文未报告；

💡 结论：论文证实DCFA在Who&When基准针对六个LLMs的实验中，较SOTA基线的步骤级准确率具备提升效果，但未披露具体量化结果与详细对比维度。

4. 关键结论和发现
- 主要发现：1. DCFA作为训练-free框架，可有效解决LLM多智能体系统故障归因中的浅层归因与上下文退化两大核心挑战；2. DCFA通过全局模块与局部模块的协同，能更精准定位系统故障的初始决定性错误；3. DCFA在Who&When基准的多LLMs实验中，相较SOTA基线的故障归因性能有提升潜力。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：DCFA是一种训练-free的双视图因果启发式故障归因框架，用于应对LLM多智能体系统故障归因中的浅层归因与上下文退化问题，可有效提升故障归因的准确性。

</details>

---

### 9. [GUT: Quantifying and Optimizing the Reasoning Uncertainty of LLMs via Graph Complexity](https://arxiv.org/abs/2609.05284v1)

**Authors**: Shuang Liang, Xin-Yu Hu, Xiang-Jun Ou, Shao-Qun Zhang  
**Category**: cs.AI  
**Published**: 2026-09-07  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2609.05284v1  

#### Abstract
Recent years have witnessed great advances in the reasoning ability of Large Language Models (LLMs). However, the reasoning processes of LLMs often exhibit uncertainty, where LLMs often produce a proliferation of divergent branches at each reasoning step even when fed the same prompting inputs, and ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

GUT: Quantifying and Optimizing the Reasoning Uncertainty of LLMs via Graph Complexity
1. 论文的主要贡献和创新点
✅ 解决的问题
LLM的推理过程存在不确定性，每一步会产生大量分歧分支，其中部分分支的推理链与结果明显不合理；现有未明确提及的方法缺乏对LLM推理不确定性的有效量化与优化手段。

🚀 提出的新方法与思路
**GUT方法**：以有向无环图表征LLM推理的潜在分支，实现所有潜在分支的全面覆盖，包含两个核心模块：
- **GUT-Q模块**：通过图复杂度近似推理空间复杂度，完成LLM推理不确定性的量化；
- **GUT-O模块**：将负不确定性作为强化学习的奖励函数，实现推理不确定性的优化。

🔍 相比现有方法的优势
论文未报告与现有方法的优势对比相关内容

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ------ | ---- |
| 5个未明确说明名称的数据集 | 验证GUT方法的有效性 |

🎯 实验设置与评估指标
论文未报告具体的实验任务、评估指标及对应含义

⚔️ 基线方法对比
论文未报告基线方法相关信息

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体的表号、图号及定量数值，所有实验项目均为：论文未报告

4. 关键结论和发现
- 主要发现：论文通过四个LLM和五个数据集的实验，验证了GUT方法能够有效量化并优化LLM的推理不确定性
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：提出基于图复杂度的GUT方法，通过构建有向无环图覆盖LLM推理的潜在分支，实现了对推理不确定性的量化与优化，相关实验验证了该方法的有效性。

</details>

---

### 10. [Do LLMs Exhibit Coherent Knowledge Structures in Mathematical Reasoning? A Perspective from Knowledge Space Theory](https://arxiv.org/abs/2609.05245v1)

**Authors**: Peng Cui, Heejin Do, Mrinmaya Sachan  
**Category**: cs.AI  
**Published**: 2026-09-07  
**Score**: 41.5  
**Type**: new  
**ArXiv ID**: 2609.05245v1  

#### Abstract
Human knowledge is inherently structured and interdependent: mastery of a concept requires prior mastery of its prerequisites, a principle formalized by Knowledge Space Theory (KST). While LLMs achieve strong performance on complex reasoning tasks, it remains unclear whether they exhibit coherent, h...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Do LLMs Exhibit Coherent Knowledge Structures in Mathematical Reasoning? A Perspective from Knowledge Space Theory
1. 论文的主要贡献和创新点
✅ 解决的问题：现有LLMs在复杂推理任务上表现优异，但未被验证是否具备类人连贯的知识结构；人类知识具有由Knowledge Space Theory（KST）形式化的结构化依赖特性，而传统的准确率评估、LLM-as-judge评估无法察觉LLMs的知识结构层面缺陷。
🚀 提出的新方法与思路：**KST-Grounded评估框架**：基于Knowledge Space Theory构建规范性评估框架，用于评估LLMs在数学推理中的知识结构，分析LLMs行为是否遵循人类的知识依赖性原则。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 知识结构评估 | 以KST为评估规范，可发现传统评估无法察觉的LLMs知识结构缺陷 |
| 跨主体知识对比 | 可实现LLMs与人类学习者的知识结构对比，以及不同LLMs间的知识结构一致性对比 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未明确报告具体数据集，仅提及评估时对比真实人类学习者的知识结构 |
🎯 实验设置与评估指标：任务为评估8个开源和闭源LLMs在数学推理中的知识结构，并与真实人类学习者的知识结构进行对比；
| 指标 | 含义 |
| --- | --- |
| 知识依赖违规情况 | 反映LLMs是否遵循人类的知识结构依赖性原则 |
| 不同LLMs的知识分布重叠度 | 反映LLMs之间知识结构的一致性 |
| 准确率（accuracy） | 传统推理性能评估指标，用于对比其对结构缺陷的察觉能力 |
| LLM-as-judge评估 | 传统LLMs输出合理性评估方式，用于对比其对结构缺陷的察觉能力 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 真实人类学习者 | 对比基准 | 作为类人知识结构的参照对象 |
| 准确率（accuracy） | 传统评估方法 | 用于评估LLMs的数学推理任务性能 |
| LLM-as-judge评估 | 传统评估方法 | 用于评估LLMs输出的合理性 |
3. 主要实验结果和性能指标
📊 定量结果汇总
由于论文未明确报告具体表号及对应定量数值，相关定量结果的表格为论文未报告。
💡 结论：
1. LLMs不遵循人类知识结构，存在频繁的知识依赖违规，且无法利用上下文提供的相关知识提升依赖问题的性能；
2. 不同LLMs之间的知识结构不一致，知识分布重叠度低；
3. LLMs的知识结构缺陷无法被传统的准确率评估和LLM-as-judge评估察觉。
4. 关键结论和发现
- 主要发现：① 当前LLMs在数学推理中不具备类人连贯的知识结构，存在知识依赖违规，且无法利用相关上下文知识优化依赖问题性能；② 不同LLMs之间的知识结构缺乏一致性，知识分布重叠度低；③ 传统的准确率评估与LLM-as-judge评估无法察觉LLMs的知识结构层面缺陷。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：该研究基于Knowledge Space Theory构建的评估框架，发现当前8个开源和闭源LLMs在数学推理中不具备类人连贯的知识结构，且这一结构缺陷无法被传统的准确率评估与LLM-as-judge评估感知。

</details>

---

### 11. [Extremely Sparse Supervision Incentivizes Reasoning Ability](https://arxiv.org/abs/2609.04565v1)

**Authors**: Zhishuai Liu, Xingzi Xu, Mehmet Saygin Seyfioglu, Pan Xu, Karim Bouyarmane  
**Category**: cs.AI  
**Published**: 2026-09-07  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2609.04565v1  

#### Abstract
Large language models demonstrate increasingly strong reasoning capabilities through effective post-training. Yet, prevailing post-training methods optimize over massive numbers of tokens, implicitly assuming that effective learning must be token-intensive. We revisit this assumption in the on-polic...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Extremely Sparse Supervision Incentivizes Reasoning Ability
1. 论文的主要贡献和创新点
✅ 解决的问题
现有大语言模型的后训练方法普遍假设，有效学习必须依赖巨量token（即token密集性），需优化海量token以提升模型性能，这一假设导致训练成本高、效率低下，存在显著的效率痛点。

🚀 提出的新方法与思路
**基于OPD的极稀疏推理监督机制**：在on-policy distillation (OPD)的训练框架下，针对大语言模型的推理任务，采用每个推理轨迹仅1-2个token（仅占该轨迹总token数的0.05%）的极少量监督信号，替代传统全token的逐步监督，以此激励模型的推理能力。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 监督资源消耗 | 仅需全token训练的0.05%的监督信号，大幅降低训练所需的标注/计算资源 |
| 推理性能表现 | 多数情况下匹配或超越全token训练对推理能力的提升效果 |
| 场景泛用性 | 跨不同模型规模（9种配置）、推理任务（数学/编码）、模型系列（Qwen3/Llama）、后训练算法（基于RLVR的PPO）均有效 |
| 学习逻辑契合度 | 更接近人类自然学习中“反思关键步骤而非逐词修正”的过程，学习逻辑更合理 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告具体数据集名称，仅提及用于数学推理任务、编码推理任务的相关训练数据

🎯 实验设置与评估指标
任务：面向数学推理、编码推理的大语言模型推理能力评估任务
| 指标 | 含义 |
| ---- | ---- |
| 推理正确率 | 衡量模型推理能力的核心指标，↑越高表示推理能力越强 |

⚔️ 基线方法对比
论文未报告具体基线方法的详细类型与特点，仅提及对比传统全token训练的方法，涉及Qwen3系列、Llama系列不同规模的teacher-student模型配置，以及基于RLVR的PPO后训练算法

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未提供具体指标数值及对应表号/图号，仅陈述在9种不同模型规模的teacher-student配置（基于Qwen3的数学推理任务）中，极稀疏监督匹配或超过全token训练的推理效果
2. 效率对比：论文未报告FPS、参数量等具体效率指标数据
3. 跨域 / zero-shot 迁移：论文未报告具体跨域/zero-shot迁移的指标数值，仅提及在编码推理任务、Llama模型、基于RLVR的PPO算法中验证了极稀疏监督的有效性
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

💡 结论：极稀疏监督信号在多种推理场景下，可实现与全token训练相当或更优的推理能力提升，且具备广泛的泛用性。

4. 关键结论和发现
- 主要发现：
  1. 大语言模型的推理能力可通过仅占总token 0.05%的极稀疏监督（每个推理轨迹仅1-2个token）有效激励，无需对每一步推理进行全token的修正监督
  2. 该极稀疏监督的效果在多数情况下优于或匹配传统全token训练，且跨不同模型规模、推理任务、模型系列、后训练算法的场景均稳定存在
  3. 极稀疏监督的学习逻辑更贴合人类的自然反思学习模式，而非逐步微调整的机械学习
- 方法局限性：论文未报告明确的方法局限性
- 未来工作：探索基于极稀疏监督的更高效后训练算法，推动大语言模型训练效率的提升

> ✅ **总结一句话**：该论文打破了“大语言模型后训练必须依赖海量token（token密集）”的传统假设，提出基于on-policy distillation的极稀疏监督机制，可高效激励模型推理能力，为设计低成本、高效率的后训练算法提供了新方向。

</details>

---

### 12. [PerfReasoning: How Well Do LLMs Reason on Hardware Performance?](https://arxiv.org/abs/2609.04476v1)

**Authors**: Dan Zhao, Karthikeyan Sankaralingam, Christos Kozyrakis, Qijing Huang  
**Category**: cs.AI  
**Published**: 2026-09-07  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2609.04476v1  

#### Abstract
Performance modeling is central to hardware design and software optimization, yet constructing these models requires structured reasoning about computation, data reuse, storage, and movement. We introduce PerfReasoning, a benchmark that evaluates LLMs both as direct performance reasoners and as gene...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

PerfReasoning: How Well Do LLMs Reason on Hardware Performance?
1. 论文的主要贡献和创新点
✅ 解决的问题
性能建模是硬件设计和软件优化的核心，构建这些模型需要对计算、数据复用、存储和移动进行结构化推理；目前缺乏专门评估LLMs在硬件性能推理及分析性能模型代码生成能力的基准，且LLMs在可靠性能模型构建上存在明显瓶颈。

🚀 提出的新方法与思路
**PerfReasoning 基准**，用于评估LLMs作为直接性能推理器和分析性能模型代码生成器的能力；给定 workload、架构和映射规范，模型可完成映射比较、片外流量及缓冲区需求预测的任务。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 评估维度 | 首次针对LLMs，同时覆盖硬件性能推理与分析性能模型代码生成两类核心任务 |
| 任务场景 | 贴合硬件设计与软件优化中性能建模的实际需求 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| PerfReasoning 基准 | 评估LLMs在硬件性能推理及性能模型代码生成任务上的表现 |

🎯 实验设置与评估指标
任务：给定 workload、架构和映射规范，完成映射比较、片外流量与缓冲区需求预测，同时评估推理-based问答准确率、性能模型代码生成通过率。
| 指标 | 含义 |
| --- | --- |
| 推理-based问答准确率 | 衡量LLMs进行硬件性能推理的正确率 |
| 代码生成通过率 | 衡量LLMs生成有效分析性能模型代码的比例 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| GPT-5.6 Sol | 闭-source LLM | 推理-based问答准确率超90%，代码生成通过率超80% |
| 最优开放-weight模型 | 开放-weight LLM | 推理-based问答准确率达82.4% |
| 其他模型配置（平均） | 各类LLM配置 | 代码生成通过率低于15%，运行结果差异显著 |
| 4B模型（经任务-specific RL） | 经任务-specific RL优化的LLM | 映射推理准确率提升15.7个点 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体表号、图号、章节或页码来源
**对应表/图未在论文中明确指定来源**
| 模型类型 | 推理-based问答准确率 | 代码生成通过率 | 映射推理准确率（变化） |
| --- | --- | --- | --- |
| 最强闭-source模型 | ≥90% ✅ | - | - |
| 最优开放-weight模型 | 82.4% | - | - |
| GPT-5.6 Sol | - | ≥80% ✅ | - |
| 其他模型配置（平均） | - | <15% | - |
| 4B模型（经任务-specific RL） | - | - | 提升15.7个点 ✅ |
💡 结论：闭-source模型在硬件性能推理任务上表现最优，开放-weight模型也达到较高性能；但多数LLMs生成可靠性能模型代码的能力不足，仅GPT-5.6 Sol表现突出；任务-specific RL可显著提升小模型的映射推理准确率。

主 benchmark 性能（L2/碰撞率等）
论文未报告

效率对比（FPS / 参数量）
论文未报告

跨域 / zero-shot 迁移
论文未报告

鲁棒性 / 扰动测试
论文未报告

消融实验
论文未报告

4. 关键结论和发现
- 主要发现：PerfReasoning基准揭示了LLMs在合理的硬件架构推理与可靠的性能模型构建之间存在显著差距；闭-source模型在硬件性能推理任务上表现优异，最优开放-weight模型准确率达82.4%；多数LLMs生成性能模型代码的能力不足，仅GPT-5.6 Sol表现突出；任务-specific RL可使4B模型的映射推理准确率提升15.7个点，反馈-free多轮自修正提示对提升性能无可靠效果。
- 方法局限性：多数模型配置的性能模型代码生成通过率极低（平均低于15%），运行结果不稳定；反馈-free多轮自修正提示不可靠，无法有效提升模型性能。
- 未来工作：公开PerfReasoning基准，以支持硬件性能领域LLM的可复现评估及未来进展追踪。

> ✅ **总结一句话**：PerfReasoning是首个针对LLMs在硬件性能领域推理能力与分析性能模型代码生成能力的评估基准，揭示了LLMs在性能建模中推理能力与代码构建能力的显著差距。

</details>

---

### 13. [Beneath the Surface of Chains-of-Thought: A Mechanistic Interpretation of Reasoning Operations in LLMs](https://arxiv.org/abs/2609.04753v1)

**Authors**: Seogyeong Jeong, Jaehui Hwang, Dongyoon Han, Geonmo Gu, Alice Oh, Taekyung Kim  
**Category**: cs.CL  
**Published**: 2026-09-07  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2609.04753v1  

#### Abstract
Reasoning in large language models unfolds through diverse functional operations, such as problem formulation, goal decomposition, and deduction. Although these operations are explicitly distinguished in text, little is known about how they are geometrically organized in representation spaces. To th...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Beneath the Surface of Chains-of-Thought: A Mechanistic Interpretation of Reasoning Operations in LLMs
1. 论文的主要贡献和创新点
✅ 解决的问题
现有研究虽在文本层面区分了LLM的推理功能操作（如问题 formulation、目标分解、演绎），但对这些操作在表示空间中的几何组织方式知之甚少，缺乏对LLM推理操作内部结构的机制性理解。

🚀 提出的新方法与思路
**推理操作几何结构分析**：研究不同推理操作是否在LLM的隐藏表示中呈现对应几何结构，通过held-out表示分析操作的可分性，验证该结构不受词汇或位置混淆的影响；进一步分析不同层的token级操作对齐的分布变化，以及相同表面token在不同操作chunk中的表示差异；通过注意力掩码干预实验，探究chunk onset处的操作对齐表示与前序推理上下文的依赖关系。

🔍 相比现有方法的优势
论文未报告相关对比表格

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
任务：研究LLM推理操作在隐藏表示中的几何结构及对应关系
论文未报告具体指标

⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告
💡 结论：LLM的不同推理操作在held-out表示中具有可分的几何结构，可分性峰值出现在中间层，且该结构不受词汇或位置混淆的影响；token级操作对齐随层增加更分散，相同表面token的表示会因周围chunk的操作不同而变化；chunk onset处的操作对齐表示依赖于前序推理上下文。

4. 关键结论和发现
- 主要发现：1. LLM的不同推理操作在隐藏表示中存在可分的几何结构，中间层可分性最高，且该结构不受词汇或位置混淆的干扰；2. token级操作对齐的分布随层变化，越深层越分散，相同表面token的表示会因周围chunk的操作不同而产生差异；3. chunk onset处的操作对齐表示依赖于前序推理上下文，注意力掩码干预可验证该关系。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该研究通过分析LLM隐藏表示的几何结构，揭示了语言推理表达式与其内部机制的对应关系，为理解LLM的推理过程提供了机制性视角。

</details>

---

### 14. [Compression Beyond the Uncompressed: A Two-Stage Training Recipe for Soft Context Compression in RAG](https://arxiv.org/abs/2609.05152v1)

**Authors**: Shuyu Guo, Shuo Zhang, Zhaochun Ren  
**Category**: cs.CL  
**Published**: 2026-09-07  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2609.05152v1  

#### Abstract
Retrieval-Augmented Generation (RAG) enhances language models with external knowledge, but the lengthy retrieved context inflates the input and degrades inference efficiency. Soft context compression encodes each document into a substantially shorter embedding sequence. However, most existing approa...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Compression Beyond the Uncompressed: A Two-Stage Training Recipe for Soft Context Compression in RAG
1. 论文的主要贡献和创新点
✅ 解决的问题
RAG通过外部知识增强语言模型，但过长的检索上下文会增加模型输入长度，导致推理效率下降；现有软上下文压缩方法大多基于未压缩RAG系统的输出进行蒸馏训练，其性能天生受限于原始模型的能力上限。

🚀 提出的新方法与思路
**Two-stage training recipe**，提出DEX-Comp的两阶段训练框架：① Pure Distillation阶段：用未压缩RAG的正确响应预热压缩模型，让压缩模型初步学习匹配原始模型的输出逻辑；② Hard Exploration阶段：仅在未压缩RAG出错的查询上运行强化学习，迫使压缩模型探索更适配压缩表示的计算模式，突破原始模型的性能限制。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 性能上限 | 突破现有蒸馏类软上下文压缩方法受限于原始未压缩RAG性能的固有局限 |
| 上下文压缩 | 实现检索上下文的有效压缩 |
| 推理效率 | 可提升RAG系统的推理效率 |
| 泛化性 | 对多样数据集与模型backbones具有良好适应性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 五个开放域QA基准 | 主benchmark性能评估、不同检索深度（top-5至top-30）评估、泛化性评估 |

🎯 实验设置与评估指标
任务：针对检索增强生成（RAG）系统，评估软上下文压缩模型在开放域QA任务中的有效性，包括压缩效果、推理效率与QA性能。
| 指标 | 含义（箭头方向） |
| --- | --- |
| 压缩比例 | 越高越好 |
| 推理加速倍数 | 越高越好 |
| QA任务性能 | 越优于未压缩RAG基线越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 现有软上下文压缩方法 | 输出蒸馏型软上下文压缩方法 | 性能受限于未压缩RAG系统的输出，无法突破原始模型的性能上限 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能（无对应表号）**
论文未报告对应表号的具体主benchmark性能表格，摘要明确指出：DEX-Comp在五个开放域QA基准、检索深度top-5至top-30下，性能与未压缩RAG基线相当或超越。
💡 结论：DEX-Comp在压缩RAG检索上下文的同时，保持了不逊于未压缩RAG的QA性能。

**效率对比（无对应表号）**
论文未报告对应表号的效率对比表格，摘要明确指出：DEX-Comp可实现检索上下文压缩与推理加速。
💡 结论：DEX-Comp兼具上下文压缩与推理加速的效果。

**跨域 / zero-shot迁移**
论文未报告对应表号的跨域/zero-shot迁移评估表格，摘要提及方法具有泛化性但未附具体结果表格。

**鲁棒性 / 扰动测试**
论文未报告对应表号的鲁棒性/扰动测试表格。

**消融实验**
论文未报告对应表号的消融实验表格，摘要提及Ablation验证了各阶段的贡献但未附具体结果表格。

4. 关键结论和发现
- 核心发现1：DEX-Comp的两阶段训练框架（Pure Distillation + Hard Exploration）能有效提升软上下文压缩模型的性能，突破现有蒸馏方法的固有性能上限。
- 核心发现2：DEX-Comp在适配压缩表示的计算模式后，可在保持QA性能的同时实现检索上下文压缩与推理效率提升。
- 核心发现3：两阶段训练的各模块贡献可被Ablation验证，且方法对多样数据集与模型backbones具有泛化性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：提出DEX-Comp两阶段训练的软上下文压缩方法，突破现有蒸馏类方法受限于原始RAG性能的局限，在压缩RAG检索上下文、提升推理效率的同时保持与未压缩基线相当或更优的QA性能。

</details>

---

### 15. [MonoMoE: An Efficient Fused Mega-kernel for Quantized MoE Decoding](https://arxiv.org/abs/2609.04244v1)

**Authors**: Yu Gong, Kailash Budhathoki, Taeho Kim, Haipeng Li, Ashish Khetan  
**Category**: cs.AR  
**Published**: 2026-09-07  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2609.04244v1  

#### Abstract
Mixture-of-Experts (MoE) layers increase model capacity without proportionally increasing arithmetic, but their sparse expert computation is difficult to execute efficiently during autoregressive decode. Existing grouped and batched GEMMs are token-major: they construct expert-local token tiles and ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

### 论文标题：MonoMoE: An Efficient Fused Mega-kernel for Quantized MoE Decoding
---
1. 论文的主要贡献和创新点
✅ 解决的问题
现有MoE解码采用token-major的分组、批处理GEMM架构，在每个专家分配token数量较少时，存在tile填充与预处理开销、内存带宽利用不足、运算阶段拆分导致效率低的痛点。

🚀 提出的新方法与思路
**Weight-major Persistent Mega-kernel**：针对块级量化MoE解码，将完整解码步的token tile放置于细粒度张量核心N维度，通过CTA按专家权重tile划分，消除专家本地token物化，减少填充运算；采用持久网格将路由、top-$k$选择、量化、双专家投影、激活、归约等操作合并为一次启动，同时通过warp specialization与就绪标志重叠辅助工作和主导专家权重流，提升资源利用率。
**vLLM集成与通用支持**：将MonoMoE与vLLM集成，通过生成内核特化和离线调度调优，支持多种模型形状。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 专家算子加速（对比vLLM Triton Grouped GEMM） | 最高达1.54× |
| 专家算子加速（对比FlashMoE-FP8 adaptation） | 2.20–3.84× |
| 端到端解码效率 | 减少单输出token时间最高18.7% |
| 任务精度 | 保留任务原始准确率 |
| 兼容性 | 集成vLLM，支持多种模型形状 |
| 可访问性 | 实现开源，提供于FlashInfer仓库 |
---
2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标
任务为量化MoE解码任务；评估指标如下：
| 指标 | 含义 |
| --- | --- |
| 专家算子加速比 | ↑越高表示算子速度越快 |
| 端到端单输出token时间 | ↓越低表示解码延迟越小 |
| 任务准确率 | ↑越高表示任务性能越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| vLLM Triton Grouped GEMM | MoE解码算子 | 现有基于token-major分组、批处理GEMM的方案 |
| FlashMoE-FP8 adaptation | MoE解码算子 | 现有FlashMoE的FP8适应方案 |
---
3. 主要实验结果和性能指标
📊 定量结果汇总
（论文未提供对应表号、图号，按原文描述整理）
在NVIDIA H200 GPU上，MonoMoE加速完整routed-MoE算子最高达1.54×（对比vLLM Triton Grouped GEMM），对比FlashMoE-FP8 adaptation快2.20–3.84×；端到端每输出token时间最多降低18.7%，同时保留任务原始准确率。
💡 结论：本文提出的MonoMoE在NVIDIA H200 GPU上显著提升了块级量化MoE解码的效率，且保持了任务的精度性能。
---
4. 关键结论和发现
- 主要发现：1）MonoMoE通过权重主导的持久mega-kernel架构，融合MoE解码的多阶段运算，消除专家本地token物化，减少填充运算，提升资源利用率；2）在NVIDIA H200 GPU上，MonoMoE实现了对现有两种MoE解码方案的显著加速，且未损失任务精度；3）MonoMoE与vLLM兼容，通过内核特化支持多种模型形状，实现开源可访问；
- 方法局限性：论文未报告
- 未来工作：论文未报告
---
> ✅ **总结一句话**：本文提出了用于块级量化MoE解码的权重主导持久mega-kernel方案MonoMoE，融合多阶段运算以提升解码效率，在NVIDIA H200 GPU上对现有MoE解码方法实现了显著加速，且保留任务精度，集成vLLM并开源实现。

</details>

---

### 16. [Corporate Language Model (CLM): Transforming Tacit and Fragmented Enterprise Knowledge into a Sovereign, Auditable, and Executable Corporate Intelligence Layer](https://arxiv.org/abs/2609.04377v1)

**Authors**: Fabricio C. Avini, Guilherme Trez  
**Category**: cs.AI  
**Published**: 2026-09-07  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2609.04377v1  

#### Abstract
Enterprise AI deployments fail not from model inadequacy, but because organizations lack a structured substrate encoding how they decide, negotiate, and execute. Generic LLMs carry no firm-specific ontological priors; RAG remains brittle, with no path to executable action; static playbooks encode lo...

---

### 17. [Unifying ICL, SFT, KL-Regularized RL Through a Bayesian Lens](https://arxiv.org/abs/2609.05111v1)

**Authors**: Junxin Fan  
**Category**: cs.AI  
**Published**: 2026-09-07  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2609.05111v1  

#### Abstract
Large language models are now trained and evaluated under a diverse set of paradigms: supervised fine-tuning (SFT), few-shot in-context learning (ICL), KL-regularized RLHF/RLVR, on-policy distillation (OPD), and test-time reasoning with search and chain-of-thought. These methods are often discussed ...

---

### 18. [Leveraging Imperfect Restoration for Data Availability Attack](https://arxiv.org/abs/2609.04627v1)

**Authors**: Yi Huang, Jeremy Styborski, Mingzhi Lyu, Fan Wang, Adams Kong  
**Category**: cs.AI  
**Published**: 2026-09-07  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2609.04627v1  

#### Abstract
The abundance of online data is at risk of unauthorized usage in training deep learning models. To counter this, various Data Availability Attacks (DAAs) have been devised to make data unlearnable for such models by subtly perturbing the training data. However, existing attacks often excel against e...

---

### 19. [Predicting Spatiotemporal Mobile Sensing-Based PM2.5 Concentrations Using Low-Rank Adapted Spatially Attentive Graph Neural Network](https://arxiv.org/abs/2609.04693v1)

**Authors**: Om Chiddarwar, Priyanka Mandal, Praveen Kumar Chandaliya, Shriniwas Arkatkar  
**Category**: cs.AI  
**Published**: 2026-09-07  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2609.04693v1  

#### Abstract
Urban air quality can vary significantly along transit corridors, necessitating high-resolution monitoring. This work introduces a novel mobile-sensing dataset from Surat, Gujarat, India, comprising PM$*{2.5}$ concentrations, meteorological variables (temperature, humidity, wind speed, wind directio...

---

### 20. [DODR: Deterministic Operator-Driven Reasoning in Latent Space](https://arxiv.org/abs/2609.04782v1)

**Authors**: Weicai Huang (Beijing MQPat Technologies, Co., Ltd.)  
**Category**: cs.AI  
**Published**: 2026-09-07  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2609.04782v1  

#### Abstract
Autoregressive (AR) large language models formulate reasoning as token-level probabilistic sampling, which induces three fundamental defects in complex logical reasoning: error accumulation, probability substituting necessity, and the linear-chain information bottleneck. This paper proposes the Dete...

---

### 21. [A Robust Watermark-based Fingerprint Framework for GNNs Ownership Verification](https://arxiv.org/abs/2609.04772v1)

**Authors**: Han Zhang, Yan Wang, Guanfeng Liu, Pengfei Ding, Huaxiong Wang, Kwok-Yan Lam  
**Category**: cs.LG  
**Published**: 2026-09-07  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2609.04772v1  

#### Abstract
The high training cost of Graph Neural Networks (GNNs) has raised growing concerns regarding model ownership infringement, such as model stealing and unauthorized misuse. To verify model ownership and prevent significant economic losses, two groups of GNN Ownership Verification (OV) methods have bee...

---

### 22. [A Comparative Study of Counterfactual Explainers for Graph Neural Networks Enabling Multiple Types of Graph Edit](https://arxiv.org/abs/2609.05113v1)

**Authors**: Maria Myrto Villia, Filippos Gouidis, Theodore Patkos, Panos Trahanias  
**Category**: cs.LG  
**Published**: 2026-09-07  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2609.05113v1  

#### Abstract
Counterfactual explanations for graph-structured data seek to determine minimal and realistic modifications required in an input graph to alter a model's prediction to a predefined output. Although counterfactual explainers that support modifying the graph by both adding and removing edges have rece...

---

### 23. [Distill Globally, Adapt Locally: Reasoning Distillation and Product-Type Test-Time Training for Scalable Trade-Up Recommendation](https://arxiv.org/abs/2609.05363v1)

**Authors**: Siliang Liu, Mohammad Ghasemi, Sapan Patel, Amin Banitalebi-Dehkordi  
**Category**: cs.LG  
**Published**: 2026-09-07  
**Score**: 26.0  
**Type**: new  
**ArXiv ID**: 2609.05363v1  

#### Abstract
Trade-up recommendation identifies higher-quality alternatives that preserve a customer's purchase intent while offering upgraded benefits. Large language models (LLMs) can reason about such distinctions, but applying them directly to hundreds of millions of product pairs is operationally impractica...

---

### 24. [A Removal Based Approach to Improve LLM Faithfulness at Test-Time](https://arxiv.org/abs/2609.04343v1)

**Authors**: Qinglan Luo, S M A Nahian, John Guttag, S. Mazdak Abulnaga, Katie Matton  
**Category**: cs.AI  
**Published**: 2026-09-07  
**Score**: 23.5  
**Type**: new  
**ArXiv ID**: 2609.04343v1  

#### Abstract
Large language models (LLMs) are increasingly used for consequential decisions, making their explanations an important tool for auditing model behavior. Unfortunately, these explanations can be unfaithful, failing to reflect the actual reasoning underlying the model's decisions. We consider a settin...

---

### 25. [IPGeoAI: Transformer-Based Geolocation with LLM Semantic Fusion](https://arxiv.org/abs/2609.04559v1)

**Authors**: Avinash Kadimisetty, Andy Jinqing Yu, Philip Favaloro, Wenlong Liu, Xiaolu Xiong  
**Category**: cs.AI  
**Published**: 2026-09-07  
**Score**: 23.5  
**Type**: new  
**ArXiv ID**: 2609.04559v1  

#### Abstract
Accurate city-level IP Geolocation is an important enabler for the modern digital ecosystem, underpinning services ranging from local content delivery and targeting to digital rights enforcement. However, traditional heuristic and database-driven methods often struggle to resolve the complex, non-li...

---

### 26. [HarvestBench: Measuring Whether LLM Agents Will Pay to Avoid Killing Animals](https://arxiv.org/abs/2609.04444v1)

**Authors**: Jasmine Brazilek, Miles Tidmarsh, Matthias Endres, Anshuman Singh, Jeremiah Miller  
**Category**: cs.AI  
**Published**: 2026-09-07  
**Score**: 22.5  
**Type**: new  
**ArXiv ID**: 2609.04444v1  

#### Abstract
Benchmarks for the side effects an agent causes on the way to a goal already exist, but HarvestBench is the first to put a price on avoiding the side effect and to name that side effect as a living creature. It is a farm simulation: LLM sub-agents drive a crew of two tractors through a cooperative c...

---

### 27. [Physics-Aware Random Walk Fingerprints for Scalable Power Grid Graph Classification](https://arxiv.org/abs/2609.04943v1)

**Authors**: Adnan Anwar  
**Category**: cs.LG  
**Published**: 2026-09-07  
**Score**: 22.5  
**Type**: new  
**ArXiv ID**: 2609.04943v1  

#### Abstract
Recent benchmarks such as PowerGraph provide large collections of power-grid graphs for cascading-failure classification. Graph neural networks (GNNs) achieve strong predictive performance on this task, but typically require end-to-end training and model-specific tuning, while their latent represent...

---

### 28. [ElderBench: Benchmarking Autonomous Mobile Agents for Older Adults](https://arxiv.org/abs/2609.04850v1)

**Authors**: Weide Zhan, Qumu Shaqu, Yuanqing Liu, Peng Zhang, Jiahao Liu, Kam Him Lam, Ning Gu, Zhan Hu, Tun Lu  
**Category**: cs.AI  
**Published**: 2026-09-07  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2609.04850v1  

#### Abstract
While autonomous mobile agents hold great potential for assisting older adults with smartphone usage, existing GUI benchmarks mainly rely on explicit, goal-oriented instructions and rarely capture the naturally occurring language patterns of older users, such as indirect speech, referential ambiguit...

---

### 29. [Reinforcement Learning for Sequential Solar PV Policy Design under Uncertainty: An Agent-Based Approach](https://arxiv.org/abs/2609.04880v1)

**Authors**: Iias Faiud, Jonaid Shianifar, Michael Schukat, Karl Mason  
**Category**: cs.AI  
**Published**: 2026-09-07  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2609.04880v1  

#### Abstract
Designing effective and fiscally sustainable policies for solar photovoltaic (PV) adoption requires balancing adoption gains against public expenditure under uncertainty and heterogeneous decision-making. This study formulates PV policy design as a sequential decision problem and integrates reinforc...

---

### 30. [Measuring AI Accountability Through Argumentation Analysis: Can Model Reasoning Withstand Scrutiny?](https://arxiv.org/abs/2609.05088v1)

**Authors**: Daan R. Henselmans, Derck W. E. Prinzhorn, Arno Libert  
**Category**: cs.AI  
**Published**: 2026-09-07  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2609.05088v1  

#### Abstract
AI oversight methods rely on ground truth for validation, but what constitutes appropriate AI behavior is contested. This leaves evaluation of moral reasoning in LLMs and debate-based oversight implicitly avoiding realistic ambiguity. We investigate an alternative standard designed to function despi...

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
