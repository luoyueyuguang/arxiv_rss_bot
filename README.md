# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-11-11 13:22:37 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [SHADOWPREFILL: Keeping Your Next Model Warm for Per-Step Model Routing in Agentic LLM Serving](https://arxiv.org/abs/2611.13176v1)

**Authors**: Haoran Qiu, Rohan Mahapatra, Rodrigo Fonseca, Mark Russinovich  
**Category**: cs.DC  
**Published**: 2026-11-11  
**Score**: 74.0  
**Type**: new  
**ArXiv ID**: 2611.13176v1  

#### Abstract
Per-step model routers send each LLM call of an agent to the cost-optimal model dynamically within each session. However, every model switch discards prefix-cache reuse: KV caches are per model, so the new model must prefill the relevant context before it emits a token. Across representative agentic...

---

### 2. [Integrating Action Prefix Prediction and Alignment Across Modalities for Multimodal Reinforcement Learning](https://arxiv.org/abs/2611.13782v1)

**Authors**: Sijie Xu, Francisco Cruz  
**Category**: cs.AI  
**Published**: 2026-11-11  
**Score**: 73.0  
**Type**: new  
**ArXiv ID**: 2611.13782v1  

#### Abstract
Learning representations from multimodal observations is difficult in reinforcement learning with limited interaction data. Multimodal Joint Predictive Representation combines multimodal latent prediction with contrastive learning across modalities, but its recursive rollout depends on earlier predi...

---

### 3. [Looping Deeper Without Growing the KV Cache: Recurrent Depth for Causal Encoder-Decoders](https://arxiv.org/abs/2611.13378v1)

**Authors**: Jiaqi Leng, Minshen Zhang, Zhaofeng Sun, Yu-Yang Qian, Peng Zhao, Hao Zhang  
**Category**: cs.LG  
**Published**: 2026-11-11  
**Score**: 66.0  
**Type**: new  
**ArXiv ID**: 2611.13378v1  

#### Abstract
Looped language models deepen computation without adding parameters, yet caching full-context key-value (KV) states across layers and rounds severely bounds serving batch size. We design a looped causal encoder-decoder (CED) that achieves recurrent depth with zero round-wise KV growth, addressing wh...

---

### 4. [Disentangling Multimodal Rotary Positional Embedding in Vision-Language Models](https://arxiv.org/abs/2611.13334v1)

**Authors**: Zhaoyi Liu, Haichuan Zhang, Xiaochuan Gong, Yancheng Zhu, Bowei Tian, Wanghao Ye, Yufan Zhang, Ang Li  
**Category**: cs.AI  
**Published**: 2026-11-11  
**Score**: 64.0  
**Type**: new  
**ArXiv ID**: 2611.13334v1  

#### Abstract
Vision-language models widely adopt Multimodal Rotary Position Embedding (MRoPE), an extension of Rotary Position Embedding (RoPE) that incorporates temporal, height, and width axes to encode the spatial structure of visual tokens. However, MRoPE also assigns height and width coordinates to text tok...

---

### 5. [When Reasoning looks like Hidden Understanding: How Chain-of-Thought Fosters Anthropomorphism, Perceptions of Epistemic Superiority, and Cognitive Deference](https://arxiv.org/abs/2611.13456v1)

**Authors**: Oliver Lack, Lana Tikhomirov, Humphrey Thompson, Carolyn Semmler, Melissa McCradden  
**Category**: cs.AI  
**Published**: 2026-11-11  
**Score**: 61.0  
**Type**: new  
**ArXiv ID**: 2611.13456v1  

#### Abstract
As AI-based products permeate society, specifically systems using generative models, a belief system is emerging about what these products are and what they can and cannot do. One common belief concerns the perception of the form of language as evidence of 'understanding' language. As these generati...

---

### 6. [Parallel Broyden Methods for Efficiently Evaluating Nonlinear State Space Models](https://arxiv.org/abs/2611.13523v1)

**Authors**: Ian Christopher Tanoh, Scott W. Linderman  
**Category**: cs.LG  
**Published**: 2026-11-11  
**Score**: 56.5  
**Type**: new  
**ArXiv ID**: 2611.13523v1  

#### Abstract
Nonlinear state space models are typically evaluated sequentially, limiting their ability to exploit modern parallel hardware. Recent work has shown that state space models can be evaluated in parallel by reformulating evaluation as a root-finding problem, which can be solved with a parallel form of...

---

### 7. [Train on prefill, monitor at decode: Using sparse autoencoders for topic monitoring](https://arxiv.org/abs/2611.12935v1)

**Authors**: Rishikesh Mallagundla, Pranav Patel  
**Category**: cs.AI  
**Published**: 2026-11-11  
**Score**: 55.5  
**Type**: new  
**ArXiv ID**: 2611.12935v1  

#### Abstract
Topic monitoring is the task of labelling the topic of each token in a model's response during generation. Activation-based monitors that run at generation time have so far been trained to detect harmful content and are limited to two or three classes. We introduce TopicScope, a framework for traini...

---

### 8. [SinkState: On-the-Fly SVD of Recurrent States for Efficient Hybrid LLM Serving](https://arxiv.org/abs/2611.14246v1)

**Authors**: Haolin Jiang, Weihang Li, Zhongzhu Zhou, Jinwen Pan, Santosh Pandey, Hang Liu  
**Category**: cs.LG  
**Published**: 2026-11-11  
**Score**: 55.0  
**Type**: new  
**ArXiv ID**: 2611.14246v1  

#### Abstract
Hybrid models combine softmax attention with linear attention, which compresses history into fixed-size recurrent states to balance model quality and inference efficiency. However, linear attention has not pushed this compression to its limit: we find that the queries, keys, and values of linear lay...

---

### 9. [TimeOmni-o1: Bidirectionally Coupling Time Series Foundation Models and LLMs for Multimodal Reasoning and Forecasting](https://arxiv.org/abs/2611.12902v1)

**Authors**: Ziyang Zhang, Shenyi Li, Wen Wu, Chao Zhang  
**Category**: cs.CL  
**Published**: 2026-11-11  
**Score**: 54.0  
**Type**: new  
**ArXiv ID**: 2611.12902v1  

#### Abstract
Time series from real-world systems are often accompanied by text, such as a report on an event that affects them. Two common tasks on these series are understanding, e.g., answering questions about a series, and forecasting its future values. Both tasks require reasoning over the series and the tex...

---

### 10. [Darmok: Championship Cryptic Crossword Solving via Constraint Tightening and Resilient Orchestration](https://arxiv.org/abs/2611.13557v1)

**Authors**: Siddhartha Chatterjee (The University of Texas at Austin)  
**Category**: cs.AI  
**Published**: 2026-11-11  
**Score**: 51.0  
**Type**: new  
**ArXiv ID**: 2611.13557v1  

#### Abstract
We present Darmok, the first automated system to reach superhuman performance on British cryptic crosswords. Unlike American-style crosswords, cryptic clues disguise an unmarked definition and compositional wordplay beneath a misleading surface reading, sparse grids leave nearly half of each word's ...

---

### 11. [F3-AGI v4.0: Bioenergetically-Gated Active Inference, Metaplastic Preconditioning, and Residual Program Synthesis for Sample-Efficient Abstract Reasoning](https://arxiv.org/abs/2611.13325v1)

**Authors**: Henrique Oliveira  
**Category**: cs.AI  
**Published**: 2026-11-11  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2611.13325v1  

#### Abstract
Few-shot abstract reasoning on ARC-AGI requires inducing algorithmic transformations from 2 to 5 demonstration pairs without task-specific pretraining. Because few-shot demonstrations under-constrain the hypothesis space, program synthesis suffers from the Rashomon effect (predictive multiplicity): ...

---

### 12. [Sckwoky at SHROOM-Visions: Character-Level Hallucination-Span Detection in Image-Conditioned VLMs via Dual-Prompted LoRA Decoders](https://arxiv.org/abs/2611.14100v1)

**Authors**: Mikhail Kulakov (Novosibirsk State University), Ruslan Solikhov (Novosibirsk State University), Ivan Bondarenko (Novosibirsk State University)  
**Category**: cs.CL  
**Published**: 2026-11-11  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2611.14100v1  

#### Abstract
We present our system for the SHROOM-visions 2026 shared task on character-level hallucination span detection in image-conditioned vision-language model (VLM) responses, evaluated across English, French, Italian, and Chinese. The detector is built on a frozen Gemma-4-12B-it backbone with trainable L...

---

### 13. [Unified Optimization of Traffic Signal and Lane Channelization for an Isolated Intersection Using Reinforcement Learning](https://arxiv.org/abs/2611.13599v1)

**Authors**: Jiwon Kang, Jiyoung Kim, Hyunseok Jun, Keemin Sohn  
**Category**: cs.LG  
**Published**: 2026-11-11  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2611.13599v1  

#### Abstract
Optimizing traffic signal control has been a long-lasting critical issue in traffic engineering, and a number of robust methodologies have emerged to solve the problem so far. On the other hand, the road design for lane channelization is a static problem that is difficult to solve jointly with the r...

---

### 14. [Recurrent Modular Structure in Spiking Neural Network Reinforcement Learning](https://arxiv.org/abs/2611.14262v1)

**Authors**: Vikram Ramavarapu, Himanshu Udupi, Ashish Gautam  
**Category**: cs.AI  
**Published**: 2026-11-11  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2611.14262v1  

#### Abstract
Biological neural circuits are both modular and recurrent, with dense communities sparsely linked to one another. Spiking neural networks (SNNs) for reinforcement learning are usually feed-forward, and it is unclear how to obtain functional modules in a recurrent SNN or what they buy. In this work, ...

---

### 15. [One Trajectory, Two Requirements: Accuracy and Local Stability in Euler Sampling for Flow Matching Policies](https://arxiv.org/abs/2611.13311v1)

**Authors**: Mahindra Rautela  
**Category**: cs.LG  
**Published**: 2026-11-11  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2611.13311v1  

#### Abstract
Flow matching robot policies commonly use a fixed Euler step count selected from offline accuracy sweeps. At inference time, however, each policy input (visual observation, robot state, and language instruction) together with a source-noise draw defines a different ODE trajectory and sequence of loc...

---

### 16. [Uncertainty-Aware Hybrid Offline Reinforcement Learning with Online Action Selection Enabled by Sparse Gaussian-Process Critics](https://arxiv.org/abs/2611.14374v1)

**Authors**: Marco Chan (Sargent Centre for Process Systems Engineering, Department of Chemical Engineering, Imperial College London), Christos Evripidou (Sargent Centre for Process Systems Engineering, Department of Chemical Engineering, Imperial College London), Liqiu Dong (Sargent Centre for Process Systems Engineering, Department of Chemical Engineering, Imperial College London), Benoit Chachuat (Sargent Centre for Process Systems Engineering, Department of Chemical Engineering, Imperial College London), Mehmet Mercang\"oz (Sargent Centre for Process Systems Engineering, Department of Chemical Engineering, Imperial College London)  
**Category**: cs.LG  
**Published**: 2026-11-11  
**Score**: 41.5  
**Type**: new  
**ArXiv ID**: 2611.14374v1  

#### Abstract
Start-ups and grade changes remain largely operator-driven, while developing and maintaining dynamic models for model-based control requires substantial engineering effort. Hybrid Offline Learning and Online Optimisation (HOFLON) uses one-step offline reinforcement learning to select actions from hi...

---

### 17. [APS-VLA: Action-Guided and Future-Aware Token Pruning for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2611.13030v1)

**Authors**: Xiaoyang Xing, Chun-Mei Feng, Anthony Cohn, Xiaoliang Gong, Asoke Nandi  
**Category**: cs.AI  
**Published**: 2026-11-11  
**Score**: 37.0  
**Type**: new  
**ArXiv ID**: 2611.13030v1  

#### Abstract
Vision-language-action (VLA) policies have demonstrated strong generalization in robotic manipulation, yet processing dense visual tokens often incurs high inference latency. Visual token pruning offers a practical way to reduce this cost, but identifying a compact set of tokens that preserves relia...

---

### 18. [Cognitive Multi-Agent Search and Rescue: Language-Grounded Hierarchical Reinforcement Learning for Collaborative Robotics](https://arxiv.org/abs/2611.13161v1)

**Authors**: Sepideh Ravanbakhsh, Hamidreza Moradi  
**Category**: cs.AI  
**Published**: 2026-11-11  
**Score**: 36.0  
**Type**: new  
**ArXiv ID**: 2611.13161v1  

#### Abstract
Effective search and rescue (SAR) operations require autonomous systems capable of coordinating multiple heterogeneous agents, adapting to dynamic hazards, and aligning with human mission intent. Existing language-guided reinforcement learning (RL) methods primarily focus on single-agent instruction...

---

### 19. [Graph Visualizations in Prompts for Knowledge Graph Question Answering](https://arxiv.org/abs/2611.12938v1)

**Authors**: Luiz do Valle Miranda, Andreas L. Opdahl, Grzegorz J. Nalepa  
**Category**: cs.AI  
**Published**: 2026-11-11  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2611.12938v1  

#### Abstract
We study when and how multimodal input improves knowledge graph question answering (KGQA) in large vision--language models. Using a controlled evaluation over 1,500 WebQSP and CWQ questions and six VLMs within a fixed KGQA pipeline, we compare text-only prompting against text-plus-graph visualizatio...

---

### 20. [Understanding Mixture-of-Experts Language Models Beyond Expert Boundaries](https://arxiv.org/abs/2611.13975v1)

**Authors**: Zhenhong Zhou, Mao Zheng, Mingyang Song, Qiankun Li, Kun Wang, Junfeng Fang  
**Category**: cs.AI  
**Published**: 2026-11-11  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2611.13975v1  

#### Abstract
In Mixture-of-Experts (MoE) models, the nature of expert specialization remains controversial. Reports of domain-associated expert preferences contrast with analyses attributing routing primarily to token identity or syntactic patterns. To clarify these differing accounts, we look beyond expert-leve...

---

### 21. [A Theory of Policy Optimization in Post-Training: Coverage Collapse and Reference Resets](https://arxiv.org/abs/2611.14467v1)

**Authors**: Audrey Huang, Nan Jiang, Sham M. Kakade, Sadhika Malladi, Akshay Krishnamurthy, Dylan J. Foster  
**Category**: cs.LG  
**Published**: 2026-11-11  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2611.14467v1  

#### Abstract
Policy optimization is central to language model post-training, yet principled guidance remains limited. We revisit its theoretical foundations to identify algorithms that learn near-optimal policies using total samples and gradient steps governed by the base model's response coverage, a measure of ...

---

### 22. [Multimodal Abstention That Preserves Acquired Correct Answers](https://arxiv.org/abs/2611.14311v1)

**Authors**: Jinyuan Zhang  
**Category**: cs.AI  
**Published**: 2026-11-11  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2611.14311v1  

#### Abstract
Adding abstention to a task-adapted multimodal model can discard correct answers, including capabilities acquired during adaptation. We formulate abstention repair as maximizing correct abstention on unanswerable questions under a budget on newly lost correct answers. We propose ReFrain (Regression-...

---

### 23. [Bits or permutations? Spending a fixed inference budget on weight precision or on option-order averaging in small local language models](https://arxiv.org/abs/2611.14413v1)

**Authors**: Mohammed Nayeem Khan, Logesh L, Aliyas Ahmad Misri  
**Category**: cs.AI  
**Published**: 2026-11-11  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2611.14413v1  

#### Abstract
Local language models can save memory by storing weights in fewer bits, and they can reduce sensitivity to the order of answer options by averaging a few reorderings. We ask whether the first makes the second worse, and which is the cheaper way to spend a fixed budget. On Qwen3-0.6B and Qwen3-1.7B w...

---

### 24. [Catch It Where It Happens: Real Time Error Correction During LLM Reasoning](https://arxiv.org/abs/2611.13107v1)

**Authors**: Rotem Elimelech, Michael Shalyt, Ido Kaminer  
**Category**: cs.CL  
**Published**: 2026-11-11  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2611.13107v1  

#### Abstract
Large language models (LLMs) are increasingly trusted with mathematical, scientific and engineering work, yet their mistakes are often confidently written and hard to spot. A single wrong step tends to propagate, making the model waste inference tokens following a false premise. Existing safeguards ...

---

### 25. [Audited Gradients, Anchored Policies: Model-Based Reinforcement Learning for Efficient Flow Control](https://arxiv.org/abs/2611.13203v1)

**Authors**: Ruige Kong, Stefania Fresca  
**Category**: cs.LG  
**Published**: 2026-11-11  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2611.13203v1  

#### Abstract
Feedback controllers for flows are expensive to design, since each candidate must be evaluated with a high-fidelity solver. Differentiable surrogates reduce that cost, but they also introduce a failure mode that prediction error cannot detect. Policy optimization uses the derivative of the objective...

---

### 26. [Breakdown of Autoregressive Multi-Step Reasoning Under Concentrated vs. Diffuse Attention Head Dropout](https://arxiv.org/abs/2611.14209v1)

**Authors**: Karol Struniawski  
**Category**: cs.AI  
**Published**: 2026-11-11  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2611.14209v1  

#### Abstract
During extended wakefulness, mammalian neocortical networks experience localized periods of transient neuronal silence termed off-states. Here, we examine how analogous spatiotemporally concentrated disruptions affect sequential reasoning in autoregressive Large Language Models (LLMs). Evaluating 25...

---

### 27. [EarthRecord: From Pixels to Land Change with Multimodal Agents over Four Decades of Satellite Imagery](https://arxiv.org/abs/2611.12934v1)

**Authors**: Haoran Zhang, Huizhen Sun, Hanbin Wen, Jie Leng, Jiaxin Zhu, Zhaohua Sun  
**Category**: cs.AI  
**Published**: 2026-11-11  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2611.12934v1  

#### Abstract
While multimodal agents now carry out complex data analysis with tools, their ability to turn decades of satellite imagery into reliable land-change analysis, crucial for Earth observation science, remains unmeasured. Existing benchmarks fall short: they pose questions on curated images or give agen...

---

### 28. [Multi-Future Drafting: Mixture Block Drafters for Tree-Verified Speculative Decoding](https://arxiv.org/abs/2611.13017v1)

**Authors**: Haoyu Huang, Jialiang Kang, Linlin Yang, Xiao Yang, Baochang Zhang  
**Category**: cs.AI  
**Published**: 2026-11-11  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2611.13017v1  

#### Abstract
Block drafters such as DFlash draft a block of future tokens in one forward pass, and draft trees such as DDTree verify the prefixes ranked highest by the product of the drafter's per-position distributions. Under tree verification, the expected number of accepted tokens is the probability mass the ...

---

### 29. [Agreeing on the Answer but Not the Reason: Measurement Limits of LLM Reasoning Failure Taxonomies](https://arxiv.org/abs/2611.13140v1)

**Authors**: Madhu Sudhan Rao Beesetty  
**Category**: cs.AI  
**Published**: 2026-11-11  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2611.13140v1  

#### Abstract
Failure taxonomies for LLM reasoning are increasingly reported as measurements: papers state what fraction of a model's errors fall into named categories, then compare those fractions across models. We show that for one such category the reported fraction is largely a property of the measurement pro...

---

### 30. [Dependable Long-Horizon LLM Agents: A Trajectory-Centered Empirical Study of Where Errors Enter and Which Controls Reach Them](https://arxiv.org/abs/2611.13254v1)

**Authors**: Shaohuang Wang, Jinghao Wen, Xulei Zhang, Xun Jiao  
**Category**: cs.AI  
**Published**: 2026-11-11  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2611.13254v1  

#### Abstract
When an LLM agent fails part-way through a long task, the usual analysis records a symptom: a failure-mode label, or the agent and step judged responsible. It does not say where the error entered, which state carried it to the symptom, whether anything in the trajectory contradicted it, or which con...

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
