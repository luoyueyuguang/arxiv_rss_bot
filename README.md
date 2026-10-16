# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-10-16 10:15:55 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [When the KV Cache Is Slower Than the GPU: Scaling Remote KV Tiers for Context-Parallel Prefill](https://arxiv.org/abs/2610.21500v1)

**Authors**: Muhammad Ibrahim  
**Category**: cs.DC  
**Published**: 2026-10-16  
**Score**: 99.5  
**Type**: new  
**ArXiv ID**: 2610.21500v1  

#### Abstract
Reusing the attention KV cache across requests is a standard way to cut prefill cost in long-context LLM serving, and production systems increasingly back the per-engine cache with a remote tier shared by every engine. We study such a tier in a disaggregated deployment of GLM-5.3, an FP8 mixture-of-...

---

### 2. [RoLaQ: Joint Rotation and Range Calibration for 2-Bit KV Caches in Multi-Head Latent Attention](https://arxiv.org/abs/2610.20686v1)

**Authors**: Shiyu Ji, Peng Ling, Chen Lin, Shupeng Li, Yixuan Wang, Qingfu Zhu, Wanxiang Che  
**Category**: cs.LG  
**Published**: 2026-10-16  
**Score**: 76.5  
**Type**: new  
**ArXiv ID**: 2610.20686v1  

#### Abstract
Multi-head latent attention (MLA) compresses the content of a key-value cache into a shared latent per token, making low-bit storage attractive for long-context inference. At two bits, errors in this representation perturb both attention matching and value readout, with effects that depend on error ...

---

### 3. [When Reasoning Is Not Enough: Proactive Inquiry for Cross-Modal Safety in Multimodal Large Language Models](https://arxiv.org/abs/2610.22068v1)

**Authors**: Wei Cai, Jian Zhao, Yuchen Yuan, Xuelong Li  
**Category**: cs.AI  
**Published**: 2026-10-16  
**Score**: 75.0  
**Type**: new  
**ArXiv ID**: 2610.22068v1  

#### Abstract
Multimodal large language models (MLLMs) can act unsafely when individually benign images and texts are interpreted jointly. Beyond implicit reasoning risk, where reasoning drifts toward harm, we identify intent-level risk, where cross-modal ambiguity silently commits the model to a hazardous premis...

---

### 4. [AbridgeKV: Compressing Long Reasoning into the KV Cache of Learned Pause Tokens](https://arxiv.org/abs/2610.20641v1)

**Authors**: Jack Cai, Lijie Yang, Vasilis Kontonis, Dimitris Papailiopoulos, Shivam Garg  
**Category**: cs.CL  
**Published**: 2026-10-16  
**Score**: 73.5  
**Type**: new  
**ArXiv ID**: 2610.20641v1  

#### Abstract
Long chain-of-thought decoding is memory-bound: the KV cache of the generated tokens grows linearly with the test-time compute being spent. Evicting cache entries does not fix this, because a model never trained on a cache with entries removed generates longer, often up to the length limit. We inste...

---

### 5. [CoWorld Reasoner: Agentic Multimodal Reasoning with the Evolving Video World Model-Driven Harness](https://arxiv.org/abs/2610.21910v1)

**Authors**: Dongjie Cheng, Ruifeng Yuan, Ran Wei, Ning Song, Yongqi Li, Wenjie Li  
**Category**: cs.AI  
**Published**: 2026-10-16  
**Score**: 67.0  
**Type**: new  
**ArXiv ID**: 2610.21910v1  

#### Abstract
As Vision-Language Models (VLMs) advance, they are increasingly expected to perform spatiotemporal reasoning over motion, actions, and view changes beyond what the input images show. Video World Models (VWMs) provide a natural unified engine for visual imagination by generating task-relevant visual ...

---

### 6. [Enhancing Multimodal RLVR with Pairwise Token Contrast and Adaptive Trajectory Confidence](https://arxiv.org/abs/2610.21671v1)

**Authors**: Yiran Zhang, Hanbo Huang, Jielan Li, Zhen Zhao, Shiyu Liang, Hongxia Hao  
**Category**: cs.CL  
**Published**: 2026-10-16  
**Score**: 62.5  
**Type**: new  
**ArXiv ID**: 2610.21671v1  

#### Abstract
Reinforcement learning with verifiable rewards (RLVR) improves multimodal reasoning, but group-relative policy optimization broadcasts a single sequence-level advantage to every token of a response, although errors usually localize to a few decisive steps. Recent self-distilled variants refine credi...

---

### 7. [Does Latent Chain-of-Thought Actually Reason? A Single, Unifying Taxonomy for Latent Reasoning](https://arxiv.org/abs/2610.21182v1)

**Authors**: Jingjie Qiu, Sheldon Yu, Xunyi Jiang, Jiajin Liu, Zihan Huang, Zhendong Chu, Tong Yu, Julian McAuley, Junda Wu  
**Category**: cs.AI  
**Published**: 2026-10-16  
**Score**: 61.0  
**Type**: new  
**ArXiv ID**: 2610.21182v1  

#### Abstract
Latent chain-of-thought replaces written reasoning steps with continuous hidden states, giving models additional steps to compute before answering. It remains unclear what computation these steps actually perform. High task accuracy and decodable intermediate answers do not establish that a model us...

---

### 8. [Efficient KV Cache Migration for Geo-Distributed LLM Inference in Collaborative Edge Computing](https://arxiv.org/abs/2610.22172v1)

**Authors**: Mingjin Zhang, Jiannong Cao, Tao Wu, Xiangchun Chen, Ne Wang  
**Category**: cs.DC  
**Published**: 2026-10-16  
**Score**: 51.5  
**Type**: new  
**ArXiv ID**: 2610.22172v1  

#### Abstract
Large Language Models (LLMs) have shown exceptional capabilities but rely heavily on centralized cloud GPU clusters, leading to high bandwidth costs, latency, and privacy issues. Edge computing offers a solution by deploying LLMs closer to users on edge servers, yet single edge servers often cannot ...

---

### 9. [QREF: Improving DeepSearch Agents by Aligning Search with Reasoning via Query Refinement and Evidence Filtering](https://arxiv.org/abs/2610.21512v1)

**Authors**: Yujia Chen, Yuhui Wang, Junzhe Wang, Shihan Dou, Di Liang, Yujiong Shen, Yuhao Zhou, Zhiheng Xi, Ming Zhang, Senjie Jin, Jiayi Chen, Dingwei Zhu, Yajie Yang, Yuan Hua, Chenyao Lu, Tao Gui, Qi Zhang, Xuanjing Huang  
**Category**: cs.AI  
**Published**: 2026-10-16  
**Score**: 51.0  
**Type**: new  
**ArXiv ID**: 2610.21512v1  

#### Abstract
DeepSearch agents achieve strong performance on complex information-seeking tasks through iterative search and reasoning. However, they often issue intent-misaligned, under-constrained, or redundant search queries, resulting in poor evidence coverage and accumulating retrieval noise. To mitigate the...

---

### 10. [BitSparse: Compact Activation Storage for ReLU Feed-Forward Networks](https://arxiv.org/abs/2610.22256v1)

**Authors**: Max Zhu, Bohang Sun, Pietro Lio, Jialin Yu  
**Category**: cs.LG  
**Published**: 2026-10-16  
**Score**: 46.5  
**Type**: new  
**ArXiv ID**: 2610.22256v1  

#### Abstract
Reducing memory use in large language model (LLM) training is an ongoing challenge. Activation checkpointing saves memory by recomputation, while lossy compression changes the stored activations. The reemergence of sparse $\relu$ and $\relu^2$ activations creates a third opportunity: losslessly comp...

---

### 11. [Coordination-Free Workload Regularization for Variable-Cost Distributed Training](https://arxiv.org/abs/2610.21162v1)

**Authors**: Tao Huang, Chen Zhu, Antonio Alonso, Daming Li, Adarsh Goura, Jaideep Ray, Yitong Zhou  
**Category**: cs.DC  
**Published**: 2026-10-16  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2610.21162v1  

#### Abstract
Synchronous data-parallel training usually assigns every rank the same number of records, even when record costs vary by orders of magnitude. For variable-length models, this converts input variation into idle time because each step waits for its most expensive rank-local batch. We present Batch Cos...

---

### 12. [Minimum RISC-V: Maximum FPGA Efficiency](https://arxiv.org/abs/2610.21552v1)

**Authors**: Martin Langhammer, Bogdan Pasca, Gregg Baeckler  
**Category**: cs.AR  
**Published**: 2026-10-16  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2610.21552v1  

#### Abstract
RISC-V processors are now widely available for FPGAs, with most FPGA vendors replacing their proprietary soft-CPU architectures with this instruction-set architecture (ISA). Although contemporary FPGAs are increasingly resource- and feature-rich, a soft processor system---including memory---often oc...

---

### 13. [X-RIC: An Agentic RAN-Intelligent Controller Benchmark for Enhancing Reinforcement Learning](https://arxiv.org/abs/2610.22269v1)

**Authors**: Adhwaa Al-Chaab, Ayman Younis, Dario Pompili  
**Category**: cs.AI  
**Published**: 2026-10-16  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2610.22269v1  

#### Abstract
The O-RAN ALLIANCE introduces architectural flexibility through disaggregation and AI-driven control. While the RAN Intelligent Controller (RIC) enables centralized optimization, current AI approaches lack reasoning capabilities and explainability. We propose eXplainable RIC (X-RIC), a novel framewo...

---

### 14. [CLUE: Uncovering Social Context for Pragmatic Understanding](https://arxiv.org/abs/2610.22167v1)

**Authors**: Chengfei Wu, Zhaoqing Wu, Dan Goldwasser  
**Category**: cs.CL  
**Published**: 2026-10-16  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2610.22167v1  

#### Abstract
Understanding a conversation requires connecting what is said to the speakers' relationships, expectations, and earlier exchanges. Prior work shows that supplying relevant context can improve models' social judgments, but much of this information may already be present in the conversation. This moti...

---

### 15. [GNN-Guided Local Refinement for Efficient Layout Decomposition with DSA-MP](https://arxiv.org/abs/2610.22214v1)

**Authors**: Yu Feng, Liyi Zhou, Haoyu Wang, Yiming Xu, Hao Geng, Shaozhi Deng, Ningsheng Xu, Shisheng Xiong  
**Category**: cs.AI  
**Published**: 2026-10-16  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2610.22214v1  

#### Abstract
Multiple patterning lithography (MPL) has been widely used to improve lithography resolution in advanced nodes, but it faces cost limits as feature sizes shrink. Directed self-assembly (DSA) offers a cost-effective complement, extending the resolution of optical lithography to sub-10 nm and beyond. ...

---

### 16. [Constrained Multi-Agent Reinforcement Learning in Imagination](https://arxiv.org/abs/2610.21319v1)

**Authors**: Raz Shmueli, Shahaf S. Shperberg  
**Category**: cs.AI  
**Published**: 2026-10-16  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2610.21319v1  

#### Abstract
Predicting cost in a multi-agent world model moves most constrained policy updates into imagination: the stronger model-free baseline needs $10$ to $20$ times CA-MAMBA's interactions on the median SMAC configuration, and CA-MAMBA earns $2.8$ to $12$ times the baselines' MAMuJoCo reward at equal budg...

---

### 17. [Hy-Memory-30B-A3B: Attributed Reinforcement Learning for Long-Term Memory Writing](https://arxiv.org/abs/2610.22196v1)

**Authors**: Tianxiang Fei, Jiazheng Kang, Mao Zheng, Xingyan He, Xiang Yu  
**Category**: cs.CL  
**Published**: 2026-10-16  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2610.22196v1  

#### Abstract
External-memory systems extend language-model applications beyond a context window, but their quality depends critically on the model executing the write path: deciding what to retain, how precisely to represent it, and how new evidence should update persistent state. Existing frameworks typically p...

---

### 18. [DocPilot: Interactive Agent Orchestration and Training for Long Visual Document Understanding](https://arxiv.org/abs/2610.21327v1)

**Authors**: Zhuowen Liang, Xiaotian Lin, Yuyu Luo, Haixun Wang, Nan Tang  
**Category**: cs.AI  
**Published**: 2026-10-16  
**Score**: 37.5  
**Type**: new  
**ArXiv ID**: 2610.21327v1  

#### Abstract
Multimodal long-document question answering requires models to seek sparse evidence across pages and modalities, understand heterogeneous document content, and reason over the collected evidence. Even advanced vision-language models (VLMs) can overlook sparse evidence and struggle with cross-modal r...

---

### 19. [MSP: Modality Self-Play for Training Multimodal LLMs Without Paired Cross-Modal Data](https://arxiv.org/abs/2610.20965v1)

**Authors**: Robert Moseley, Md Kaykobad Reza, Ameya Patil, Edward Ayrapetian, Salman Asif  
**Category**: cs.AI  
**Published**: 2026-10-16  
**Score**: 37.0  
**Type**: new  
**ArXiv ID**: 2610.20965v1  

#### Abstract
Large multimodal models have achieved remarkable progress by scaling model capacity and training on massive paired multimodal data. However, this paradigm introduces a fundamental bottleneck: aligned multimodal datasets are expensive to curate, difficult to scale across diverse modality combinations...

---

### 20. [DropKV: Decoupling Residual-Output Perturbation for Near-Optimal KV-Cache Eviction](https://arxiv.org/abs/2610.22130v1)

**Authors**: Aozhong Zhang, Selcuk Gurses, Yanxia Deng, Naigang Wang, Chi-Chun Liu, Davis Wertheimer, Derrick Liu, Xin Li, Zi Yang, Felix X. -F. Ye, Penghang Yin  
**Category**: cs.AI  
**Published**: 2026-10-16  
**Score**: 36.0  
**Type**: new  
**ArXiv ID**: 2610.22130v1  

#### Abstract
Key-value (KV) cache management has become a critical bottleneck for scaling Large Language Models (LLMs) to long-context scenarios due to linear memory growth. While recent eviction methods have moved beyond simple attention-score heuristics to incorporate value representations, they typically face...

---

### 21. [Compression Does Not End at Selection: Post-Selection Positional Geometry for Sparse KV Caches](https://arxiv.org/abs/2610.21126v1)

**Authors**: Wanyang Hong, Zhaoning Zhang  
**Category**: cs.CL  
**Published**: 2026-10-16  
**Score**: 36.0  
**Type**: new  
**ArXiv ID**: 2610.21126v1  

#### Abstract
Sparse KV compression reduces long-context inference costs by retaining selected historical states, yet these states typically keep their coordinates from the full history. Under Rotary Position Embedding (RoPE), gaps left by evicted tokens continue to affect query-key matching, potentially limiting...

---

### 22. [OmniVerifier-C1: Decomposed Graded Verifier for Rule-Governed Generative World Modeling](https://arxiv.org/abs/2610.22355v1)

**Authors**: Bowei Liu, Xinchen Zhang, Xuhuan Li, Tianlin Zhang, Kaian Jiang, Jingwei Liu, Congyang Zhao, Yifei Qian, Junhong Liu, Zhiheng Li, Yujiu Yang, Yang Cai, Ling Yang  
**Category**: cs.CL  
**Published**: 2026-10-16  
**Score**: 35.5  
**Type**: new  
**ArXiv ID**: 2610.22355v1  

#### Abstract
Generative visual verifiers play a crucial role in advancing multimodal intelligence. To enhance the robustness of visual verifiers in complex multimodal scenarios involving compositional requirements, we move beyond conventional binary verifiers that produce only True/False discrete judgments and i...

---

### 23. [Progress Reward Model for Reinforcement Learning via Large Language Models](https://arxiv.org/abs/2610.22056v1)

**Authors**: Xiuhui Zhang, Ning Gao, Xingyu Jiang, Yihui Chen, Yuheng Pan, Mohan Zhang, Yue Deng  
**Category**: cs.AI  
**Published**: 2026-10-16  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2610.22056v1  

#### Abstract
Traditional reinforcement learning (RL) algorithms face significant limitations in handling long-term tasks with sparse rewards. Recent advancements have leveraged large language models (LLMs) to enhance RL by utilizing their world knowledge for task planning and reward generation. However, planning...

---

### 24. [FlowBudget: Training-Free Sampling-Budget Estimation for Flow Matching Models](https://arxiv.org/abs/2610.20636v1)

**Authors**: Zahra Dehghani, Pablo Piantanida, Mohammadhadi Shateri  
**Category**: cs.LG  
**Published**: 2026-10-16  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2610.20636v1  

#### Abstract
Sampling from continuous flow-based generators such as flow matching models requires numerical ODE or SDE integration, making inference cost depend on the number of function evaluations (NFEs). In practice, the sampling budget is inherited from prior work or selected through expensive FID-versus-NFE...

---

### 25. [Do As I Do, Not As I Say: On-Policy Distillation Inherits the Teacher in Vision-Language Models](https://arxiv.org/abs/2610.20989v1)

**Authors**: Frank F. Yang, Kefei Yan, Yiren Wang, Yiyang Wang  
**Category**: cs.LG  
**Published**: 2026-10-16  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2610.20989v1  

#### Abstract
Improving the reasoning capabilities of vision-language models (VLMs) often relies on post-training with supervision from stronger models. Two common strategies are supervised fine-tuning (SFT), which trains on teacher-generated demonstrations, and on-policy distillation (OPD), which provides teache...

---

### 26. [Learning Lean Feedback for Efficient Proof-Candidate Evaluation on GPUs](https://arxiv.org/abs/2610.21881v1)

**Authors**: Lazar Milikic, Etienne Bamas, Emmanuel Abbe, Viktor Kun\v{c}ak  
**Category**: cs.LG  
**Published**: 2026-10-16  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2610.21881v1  

#### Abstract
Training language models for formal theorem proving requires large numbers of verifier calls. Slow checks and timeouts often leave GPUs waiting and withhold rewards from potentially correct proofs. We train neural evaluators to predict Lean 4 verdicts and compiler feedback on GPUs using 4.84M labell...

---

### 27. [HyCo: Hybrid Drafting for Cost-Efficient Mobile-Cloud Speculative Decoding](https://arxiv.org/abs/2610.21436v1)

**Authors**: Hanbin Bae, Heejin Choi, Joohyung Lee, Byoung Jin Choi, Sangjun Park, Hoon-Young Cho  
**Category**: cs.CL  
**Published**: 2026-10-16  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2610.21436v1  

#### Abstract
Device-cloud speculative decoding reduces server computation, but growing a deep draft tree with a small language model (SLM) requires repeated passes on a mobile neural processing unit (NPU). We present HyCo, which assigns depth to the server model's native multi-token prediction (MTP) head, execut...

---

### 28. [MemComposer: Learning to Assemble Memories for LLM Agents via Reinforcement Learning](https://arxiv.org/abs/2610.21091v1)

**Authors**: Yixuan Xie, Xueqiang Xu, Xinyi Fan, Xinxi Lyu, Tao Feng, Xing Fan, Chenlei Guo, Jie Hao, Shaowen Wang, Jiashuo Sun, Jiawei Han  
**Category**: cs.AI  
**Published**: 2026-10-16  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2610.21091v1  

#### Abstract
Agent memory enables large language model (LLM) agents to reuse past experiences without updating their parameters. However, semantic similarity alone does not guarantee memory usefulness: downstream performance depends on how memories are selected and presented to the agent. We propose MemComposer,...

---

### 29. [Emotion Is Not External Knowledge: Internal Attention Signals for Affective State Reasoning](https://arxiv.org/abs/2610.21347v1)

**Authors**: Wenqiu Tang, Zhen Wan, Yihui Wang, Takahiro Komamizu, Ichiro Ide  
**Category**: cs.CL  
**Published**: 2026-10-16  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2610.21347v1  

#### Abstract
Large Language Models (LLMs) increasingly operate in multi-turn interactions that require maintaining latent conversational states, not only explicit facts. We study affective state as an implicit state inferred from sparse contextual cues that remain relevant after topic shifts, and ask whether LLM...

---

### 30. [Lethe: Link Inference Attacks For Evaluation of Edge Unlearning Methods](https://arxiv.org/abs/2610.21869v1)

**Authors**: Andrea D'Angelo, Francesco Gullo, Davide Mottin, Sayan Ranu, Giovanni Stilo  
**Category**: cs.LG  
**Published**: 2026-10-16  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2610.21869v1  

#### Abstract
Graph Unlearning (GU) aims to remove the influence of specific training data from a Graph Neural Network without retraining anew. While most methods address removal of nodes and features, Edge Unlearning (EU), aiming at forgetting edges, has recently attracted dedicated attention as a standalone pro...

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
