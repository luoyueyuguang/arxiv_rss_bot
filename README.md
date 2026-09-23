# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-09-23 10:17:22 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [Disaggregated Quantization: Specializing LLM Prefill and Decode](https://arxiv.org/abs/2609.26333v1)

**Authors**: Andrei Panferov, Maximilian Kleinegger, Sweta Priyadarshi, Tijmen Blankevoort, Dan Alistarh  
**Category**: cs.LG  
**Published**: 2026-09-23  
**Score**: 112.5  
**Type**: new  
**ArXiv ID**: 2609.26333v1  

#### Abstract
Prefill and decode reward different approaches to quantization: low-precision arithmetic accelerates prompt processing, while compact weights reduce memory traffic during generation. We propose "disaggregated quantization" (DQ), which specializes computation formats, weights and storage placement to...

---

### 2. [Diffusion Drafts, AR Verifies: Accelerating Document OCR with Self-Speculative Decoding](https://arxiv.org/abs/2609.26638v1)

**Authors**: Dohyun Kim, Sungjun Han, Hyungguk Kim, Yusik Kim, Jamin Shin, Paul Hongsuck Seo, Hongjoon Ahn  
**Category**: cs.CL  
**Published**: 2026-09-23  
**Score**: 86.5  
**Type**: new  
**ArXiv ID**: 2609.26638v1  

#### Abstract
Autoregressive OCR vision-language models accurately convert document images into text and structured markup, but require one sequential decoding step per output token, limiting inference speed. Unlike open-ended text generation, OCR outputs are strongly grounded in the input image, making diffusion...

---

### 3. [VLM-in-Sandbox: Visual Workspaces for Agentic Visual Reasoning](https://arxiv.org/abs/2609.24362v1)

**Authors**: Hexiong Yang, Mingrui Chen, Jie Cao, Ran He  
**Category**: cs.AI  
**Published**: 2026-09-23  
**Score**: 77.5  
**Type**: new  
**ArXiv ID**: 2609.24362v1  

#### Abstract
Sandboxed computer environments support multi-step reasoning with tools, executable programs, and persistent files, yet their extension from language models to vision-language models (VLMs) introduces a distinct state-management problem. Visual reasoning produces intermediate image-valued evidence--...

---

### 4. [Hot-Cold Tiering of HBM and High Bandwidth Flash for Agentic LLM Serving](https://arxiv.org/abs/2609.25782v1)

**Authors**: Jongjin Baek, Won Ji, Seungjae Yoo, Joo-Young Kim  
**Category**: cs.AR  
**Published**: 2026-09-23  
**Score**: 74.0  
**Type**: new  
**ArXiv ID**: 2609.25782v1  

#### Abstract
Large language model (LLM) serving is increasingly agentic, with multi-turn sessions that idle between actions yet must retain their full context. Limited GPU memory capacity forces inactive KV states to be evicted, so resuming a session incurs either costly recomputation or slow interconnect transf...

---

### 5. [HySparse2: Hybrid Sparse Attention with Two-Level KV Sharing](https://arxiv.org/abs/2609.26368v1)

**Authors**: Jianyu Wei, Yizhao Gao, Qihao Zhang, Shimao Chen, Zhengju Tang, Yu Cheng, Shengjie Zhou, Zihan Jiang, Yifan Song, Hailin Zhang, Liang Zhao, Bo Yang, Gang Wang, Shijie Cao, Fuli Luo  
**Category**: cs.CL  
**Published**: 2026-09-23  
**Score**: 68.0  
**Type**: new  
**ArXiv ID**: 2609.26368v1  

#### Abstract
Long-horizon and multi-turn agents typically generate short actions and process long observations from tools and environments. This growing context demands efficient prefill, compact KV-cache storage, and accurate long-context retrieval. To meet these demands, we introduce HySparse2, a hybrid sparse...

---

### 6. [Fast Recovery for LLM Serving via Decoupled Device Memory Lifetime in Dynamo](https://arxiv.org/abs/2609.25451v1)

**Authors**: Schwinn Saereesitthipitak (NVIDIA), Mohammed Abdulwahhab (NVIDIA), Hannah Zhang (NVIDIA), Dan Feigin (NVIDIA), Neelay Shah (NVIDIA), Maksim Khadkevich (NVIDIA), Itay Neeman (NVIDIA), Vikram Sharma Mailthody (NVIDIA), Wen-mei W. Hwu (NVIDIA Research)  
**Category**: cs.DC  
**Published**: 2026-09-23  
**Score**: 66.5  
**Type**: new  
**ArXiv ID**: 2609.25451v1  

#### Abstract
Large language model (LLM) inference replicas run across tightly coupled GPUs and serve traffic continuously for weeks. Hardware and software failures are therefore inevitable, and one worker failure can disrupt an entire replica. Recovery requires reinitializing the engine, taking minutes even when...

---

### 7. [Taming CoT Obfuscation in VLMs: From Mechanistic Evidence to Activation Enforcement](https://arxiv.org/abs/2609.24243v1)

**Authors**: Xutao Mao, Jianing Zhu, Jinman Zhao, Tongliang Liu, Xiaowen Chu, Cong Wang, Bo Han  
**Category**: cs.AI  
**Published**: 2026-09-23  
**Score**: 55.5  
**Type**: new  
**ArXiv ID**: 2609.24243v1  

#### Abstract
Reinforcement learning (RL) improves reasoning in vision-language models (VLMs) but can induce chain-of-thought (CoT) obfuscation: an operational, non-intentional outcome where task reward or accuracy rises while traces become less grounded and monitorable. Prior work largely documents this decay be...

---

### 8. [Informed Masking: Structure-Aware Perturbation for Reinforcement Learning in Diffusion Large Language Models](https://arxiv.org/abs/2609.25927v1)

**Authors**: Xiaoyi Yu, Enver Sangineto, Pei Fu, Fiorenzo Parascandolo, Wenhui Tan, Ruikang Zhang, Rita Cucchiara, Ruihua Song, Jian Luan  
**Category**: cs.CL  
**Published**: 2026-09-23  
**Score**: 55.0  
**Type**: new  
**ArXiv ID**: 2609.25927v1  

#### Abstract
Diffusion Large Language Models (dLLMs) have emerged as an efficient alternative to autoregressive models, yet aligning them via Reinforcement Learning (RL) requires likelihood surrogates estimated from masked reconstruction subproblems under a small Monte Carlo budget per rollout. Existing methods ...

---

### 9. [You Only Need 2/3 of the Chosen Experts: An Empirical Study of Dynamic Expert Pruning in Fine-Grained MoE LLMs](https://arxiv.org/abs/2609.25809v1)

**Authors**: Yuanteng Chen, Qiwei Lai, Chen Tianqi, Peisong Wang, Yuantian Shao, Nanxin Zeng, Zhilei Liu, Chuangyi Li, Jing Liu, Jian Cheng  
**Category**: cs.LG  
**Published**: 2026-09-23  
**Score**: 55.0  
**Type**: new  
**ArXiv ID**: 2609.25809v1  

#### Abstract
Fine-grained mixture-of-experts (MoE) architectures have become a mainstream design for open-weight LLMs, with hundreds of experts and increasingly many selected per token. This shift makes dynamic expert pruning an attractive route to cheaper inference. Yet existing evidence comes largely from coar...

---

### 10. [Deep Reinforcement Learning on Item-Compatibility Graphs for One-Dimensional Bin Packing](https://arxiv.org/abs/2609.25397v1)

**Authors**: M. Asl{\i} Ayd{\i}n  
**Category**: cs.LG  
**Published**: 2026-09-23  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2609.25397v1  

#### Abstract
The one-dimensional bin packing problem (1D-BPP) is a classical NP-hard combinatorial optimization problem with applications ranging from logistics and manufacturing to cloud resource management. Although deep reinforcement learning (DRL) has become a competitive paradigm for data-driven optimizatio...

---

### 11. [DefaultGNN: A Dual-Perspective GNN Framework for Predicting Corporate Default from Buyer-Seller Transaction Networks](https://arxiv.org/abs/2609.25542v1)

**Authors**: Junghoon Kim, Hyunsung Kim, Seungyoon Choi, KyoungYong Park, Jihun Lee, YongGu Ji, Chanyoung Park  
**Category**: cs.LG  
**Published**: 2026-09-23  
**Score**: 51.0  
**Type**: new  
**ArXiv ID**: 2609.25542v1  

#### Abstract
Corporate default prediction is a core problem in financial risk management, yet traditional credit models rely heavily on financial statements that are often sparse or unavailable for many firms. Corporate transaction networks offer a complementary view of real economic activity, but how risk propa...

---

### 12. [PatchKV: Efficient KV Cache Recovery for Dynamically Edited LLM Contexts](https://arxiv.org/abs/2609.26219v1)

**Authors**: Guotao Yang, Rui Guo, Siwei He, Sheng Chen, Yitao Hu, Keqiu Li  
**Category**: cs.DC  
**Published**: 2026-09-23  
**Score**: 48.5  
**Type**: new  
**ArXiv ID**: 2609.26219v1  

#### Abstract
Long-running LLM agent workflows often revise interior context spans while retaining long suffixes. Although suffix tokens remain unchanged, altered causal histories and rotary positions prevent exact reuse of their offloaded key-value (KV) states. Full suffix recomputation wastes prefill work, whil...

---

### 13. [Decoupling Logical Masks from GPU Execution for Dynamic Block-Sparse Attention](https://arxiv.org/abs/2609.25869v1)

**Authors**: Shanghao Liu, Xiaoyun Yu, Wanting Li, Wenqi Jiang  
**Category**: cs.AR  
**Published**: 2026-09-23  
**Score**: 46.0  
**Type**: new  
**ArXiv ID**: 2609.25869v1  

#### Abstract
Attention computation makes inference expensive in video diffusion transformers (vDiTs), which generate videos through iterative denoising. Block-sparse attention (BSA) reduces
  this cost by computing only blocks selected by a logical mask, which specifies attention interactions to compute. However...

---

### 14. [Toki: Profiling HBM Performance on FPGA Systems with RISC-V Soft Cores and PCIe Host DMA Traffic](https://arxiv.org/abs/2609.26551v1)

**Authors**: Andrea Galimberti, Andrea Motta, Gianni Antichi, Davide Zoni  
**Category**: cs.AR  
**Published**: 2026-09-23  
**Score**: 46.0  
**Type**: new  
**ArXiv ID**: 2609.26551v1  

#### Abstract
Programmable RISC-V soft cores are becoming more widespread in data-center scenarios, making it crucial to design efficient systems that deploy them on FPGA chips with HBM memory. Toki, released as open source, is the first hardware-software framework that enables profiling the performance of HBM on...

---

### 15. [TSS: Target-Side Sparsification for Speculative Decoding in Domain-Specific Large Language Models](https://arxiv.org/abs/2609.26100v1)

**Authors**: Haibo Hu, Lianming Huang, Qiao Li, Nan Guan, Chun Jason Xue  
**Category**: cs.CL  
**Published**: 2026-09-23  
**Score**: 45.5  
**Type**: new  
**ArXiv ID**: 2609.26100v1  

#### Abstract
Speculative decoding accelerates large language model inference through collaboration between a lightweight draft model and a target verifier. Existing methods mainly improve the draft side, while the target model is typically kept dense and unchanged. We show that, under domain-specific inference, ...

---

### 16. [An Affordable AI-Integrated Smart Cane for Multimodal Mobility Assistance of Visually Impaired Users](https://arxiv.org/abs/2609.22277v1)

**Authors**: Ali Akarma, Adeel Ahmad, Toqeer Ali Syed  
**Category**: cs.AI  
**Published**: 2026-09-23  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2609.22277v1  

#### Abstract
Visual impairment affects over 2.2 billion people worldwide, yet conventional white canes cannot detect elevated hazards or provide semantic environmental context. Existing AI-assisted navigation systems typically rely on expensive hardware or cloud connectivity, limiting accessibility in resource-c...

---

### 17. [ICDAR2026 Competition on Multimodal Reasoning over Documents in Multiple Domains](https://arxiv.org/abs/2609.25055v1)

**Authors**: Artemis Llabr\'es, Marc Serra Ortega, Tom\`as Ockier, Samuel Ortega Cuadra, Amritpal Singh, Christos Georgakilas, Andrey Barsky, Ernest Valveny, Dimosthenis Karatzas  
**Category**: cs.CL  
**Published**: 2026-09-23  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2609.25055v1  

#### Abstract
In this report we present results of the ICDAR2026 Competition on Multimodal Reasoning over Documents in Multiple Domains. This competition aimed to advance research in document understanding through the task of Visual Question Answering (VQA). Building upon previous DocVQA benchmarks, this competit...

---

### 18. [Spatial-Interactor: Learning Spatial Reasoning through Interaction with the Observable Physical World](https://arxiv.org/abs/2609.23038v1)

**Authors**: Kaixiang Yao, Xu Wang, Miao Pan, Hu Xiyue, Weishi Wang, Daniel Dahlmeier, Jintao Chen, Yongliang Shen, Xuhong Zhang, Wenqi Zhang  
**Category**: cs.AI  
**Published**: 2026-09-23  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2609.23038v1  

#### Abstract
Spatial reasoning is essential for vision-language models (VLMs) to understand and act in the physical world. Reasoning in dynamic environments requires VLMs to perceive local state transitions caused by object motion and viewpoint changes and integrate them over long trajectories to maintain an upd...

---

### 19. [Fully Byzantine-Resilient Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2609.25701v1)

**Authors**: Haejoon Lee, Dimitra Panagou  
**Category**: cs.LG  
**Published**: 2026-09-23  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2609.25701v1  

#### Abstract
We study distributed Byzantine-resilient actor-critic multi-agent reinforcement learning (AC-MARL), where agents collectively learn policies through local interactions. Existing methods guarantee convergence of the agents' parameters only to a neighborhood of the attack-free limit points, resulting ...

---

### 20. [Beyond Linear Context: Graph-Guided Evidence Navigation for Long-Novel Reasoning with a Local 9B Language Model](https://arxiv.org/abs/2609.22939v1)

**Authors**: Wenji Fu  
**Category**: cs.AI  
**Published**: 2026-09-23  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2609.22939v1  

#### Abstract
Long-context models read a novel the way a person reads a printout: one token after another, in narrative order, with the whole history competing for a fixed budget of attention. A detective does not work that way. They sort what happened when, and they keep a map of who relates to whom, so a clue f...

---

### 21. [Semantic Abstraction for Natural Language Inference: a Methodological Framework for Discovering and Compensating Semantic Knowledge and Reasoning Gaps in Large Language Models](https://arxiv.org/abs/2609.26610v1)

**Authors**: David Torres-Moreno, Jorge Hermosillo-Valadez  
**Category**: cs.CL  
**Published**: 2026-09-23  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2609.26610v1  

#### Abstract
Despite their outstanding performance on many NLP tasks, LLMs face serious challenges related to semantic abstraction. In this study, we are interested in understanding how LLMs leverage abstract semantic knowledge in natural language inference (NLI), which requires sophisticated linguistic capabili...

---

### 22. [Terminal Shrinkage Averaging Reveals a Schedule-Estimator Interaction in LLM Pretraining](https://arxiv.org/abs/2609.25482v1)

**Authors**: Adam Ousherovitch, Yixin Wang  
**Category**: cs.LG  
**Published**: 2026-09-23  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2609.25482v1  

#### Abstract
Large language model (LLM) pretraining conventionally returns the raw final iterate. This couples two design choices: the learning-rate schedule that generates the parameter trajectory and the estimator that constructs the deployed model (e.g. the raw final iterate or a checkpoint average). A schedu...

---

### 23. [Cloud, Edge, or Split? Profiling Onboard and Split Vision-Language Model Deployment for Drone AI](https://arxiv.org/abs/2609.25415v1)

**Authors**: Zoha Azimi, Reza Farahani, Schahram Dustdar, Christian Timmerer  
**Category**: cs.DC  
**Published**: 2026-09-23  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2609.25415v1  

#### Abstract
Vision-Language Models (VLMs) enable edge devices like unmanned aerial vehicles (UAVs) to interpret visual observations and reason about complex environments using natural-language instructions. However, their practical deployment remains challenging as onboard inference is constrained by limited co...

---

### 24. [LADDER: Graph-Guided Diffusion Language Models for Efficient Multi-Hop Reasoning](https://arxiv.org/abs/2609.24346v1)

**Authors**: Senlei Zhang, Linhao Luo, Qian-Wen Zhang, Siyu An, Junnan Dong, Shuhao Zhang, Xing Sun  
**Category**: cs.AI  
**Published**: 2026-09-23  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2609.24346v1  

#### Abstract
Graph Retrieval-Augmented Generation (GraphRAG) has remarkably enhanced large language models on complex reasoning by leveraging structured entity topologies. However, existing frameworks heavily rely on standard autoregressive language models where the nature of inherent sequential generation sever...

---

### 25. [Differentiable Fuzzy Inference Layer: A Monotone, Compositional Ordinal Reasoning Head for Large Language Models](https://arxiv.org/abs/2609.26113v1)

**Authors**: Zhen Zhang, Amr Alanwar  
**Category**: cs.CL  
**Published**: 2026-09-23  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2609.26113v1  

#### Abstract
A state-of-the-art language model asked to interpret "most of most students passed" typically answers "most," though composing two instances of "most" yields a proportion closer to "some." We trace this failure to an architectural choice rather than a data deficit: standard classifier heads treat or...

---

### 26. [WeightBridge: An Efficient Weight Transfer Library for Reinforcement Learning](https://arxiv.org/abs/2609.25442v1)

**Authors**: Xuanlin Jiang, Samuel Hsia, Michael Kuchnik, Zachary DeVito, Minlan Yu, Carole-Jean Wu  
**Category**: cs.DC  
**Published**: 2026-09-23  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2609.25442v1  

#### Abstract
Weight transfer - the propagation of updated parameters from trainers to rollout generators - is becoming an important performance bottleneck in reinforcement learning (RL) systems for LLMs. The central challenge is supporting the diverse trainer and rollout layouts and synchronization requirements ...

---

### 27. [Construting Reverse Thinking: Developing Large Language Models' Reverse Thingking Ability](https://arxiv.org/abs/2609.24760v1)

**Authors**: Xin Liu, Yunhai Li, Chunfu Jia, Ziliang Chen, Jisen Song  
**Category**: cs.AI  
**Published**: 2026-09-23  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2609.24760v1  

#### Abstract
When facing complex problems, humans tend to try various ideas for different issues. Human thinking patterns exhibit remarkable flexibility in adapting to diverse scenarios. GPT-o1, GPT-o3, and DeepSeek-R1 adopt long chain-of-thought models to address complex problems by increasing reasoning depth, ...

---

### 28. [Text, Pixels, or Both? Evaluating Input Representations for Multimodal Document QA](https://arxiv.org/abs/2609.22628v1)

**Authors**: Nikhil Reddy Pottanigari, Sepideh Kharaghani, Saverio Vadacchino, Alejandro Posada, Ying Zhang  
**Category**: cs.AI  
**Published**: 2026-09-23  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2609.22628v1  

#### Abstract
Every document QA system begins with a choice that is rarely studied on its own: whether to feed the model page images, extracted text, or both. We isolate this choice, holding the prompt, judge, and scoring pipeline fixed, across four commercial model endpoints, two corpora, and two context regimes...

---

### 29. [When Should a VLM Look? Paying Only for Visual Calls That Were Needed and Used](https://arxiv.org/abs/2609.22910v1)

**Authors**: Kunyu Peng, Junming Liu, Ruiqi He, Qingzhuo Wang, Jianzhong Qi, Xianhui Liu  
**Category**: cs.AI  
**Published**: 2026-09-23  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2609.22910v1  

#### Abstract
Vision-language agents that crop and zoom are trained with rewards that credit a successful tool call, yet a successful call does not show that the model needed to look or used the pixels it received. On our cold-start checkpoint only 10% to 12% of visual calls were both needed and used, and release...

---

### 30. [LatentPort: Beyond KV Cache - Cross-Model Transfer of Recurrent Memory in Hybrid Language Models: A 4B-to-9B Hybrid-State Handoff Without Target Prefix Replay](https://arxiv.org/abs/2609.25053v1)

**Authors**: Simon P. Villani  
**Category**: cs.CL  
**Published**: 2026-09-23  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2609.25053v1  

#### Abstract
Can one language model hand its live memory to another without the receiver rereading the context? We demonstrate useful persistent hybrid-state transfer across one architecture-matched Qwen3.5 4B-to-9B sibling pair. To our knowledge, this is the first demonstrated cross-model handoff of persistent ...

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
