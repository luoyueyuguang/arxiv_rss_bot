# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-11-23 17:04:34 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [Reinforcement Learning Unlearns Corrupted SFT Reasoning](https://arxiv.org/abs/2611.26756v1)

**Authors**: Anika Misra, Shreyas Vinod, Huteng Dai  
**Category**: cs.CL  
**Published**: 2026-11-23  
**Score**: 72.0  
**Type**: new  
**ArXiv ID**: 2611.26756v1  

#### Abstract
We show that reinforcement learning (RL) in reasoning tasks can succeed even when the supervised fine-tuning (SFT) data is severely corrupted. In a mathematical reasoning dataset (GSM8K), we systematically corrupt training trajectories across 361 configurations by injecting realistic error types, va...

---

### 2. [LongCat Recall Sparse Attention: Co-Designing Key Organization and Retrieval for Long-Context Inference](https://arxiv.org/abs/2611.27233v1)

**Authors**: Hao Zhang, Bin Xiao, Kefeng Zhang  
**Category**: cs.CL  
**Published**: 2026-11-23  
**Score**: 68.5  
**Type**: new  
**ArXiv ID**: 2611.27233v1  

#### Abstract
Retrieval-based sparse attention, exemplified by DeepSeek Sparse Attention (DSA), reduces attention computation by selecting a small subset of key-value entries. However, selecting these entries can still require searching the entire visible history. For long sequences, retrieval becomes a major bot...

---

### 3. [Graph-XGB: A Hybrid GNN Framework for Outdoor-to-Indoor 5G Signal Reconstruction via Aerial-Only UAV RF Sensing](https://arxiv.org/abs/2611.26828v1)

**Authors**: David Hason Rudd, Eunkwang Shin, Nithiwat Pattrapong, Huan Huo, Xiangmeng Wang  
**Category**: cs.LG  
**Published**: 2026-11-23  
**Score**: 65.0  
**Type**: new  
**ArXiv ID**: 2611.26828v1  

#### Abstract
Delivering robust In-Building Coverage (IBC) is critically impeded by severe Outdoor-to-Indoor (O2I) attenuation, a constraint that intensifies as deployments move from 5G mid-band towards mmWave and prospective 6G sub-THz carriers, where losses of 60-80 dB have been reported across modern building ...

---

### 4. [Reasoning in Two Dimensions: Quantifying Chain-of-Thought Faithfulness and Efficiency](https://arxiv.org/abs/2611.27100v1)

**Authors**: Chenruo Liu, Quan Zhang, Qi Lei  
**Category**: cs.AI  
**Published**: 2026-11-23  
**Score**: 63.0  
**Type**: new  
**ArXiv ID**: 2611.27100v1  

#### Abstract
Chain-of-thought (CoT) reasoning exposes intermediate steps, but a correct answer does not establish that an LLM relies on the dependence expressed by those steps or reasons efficiently. We operationalize CoT faithfulness and efficiency within a common framework. Specifically, we represent a CoT as ...

---

### 5. [FOREST: Coordinating Tree-based HBF, RRAM, and HBM for Efficient Speculative LLM Inference](https://arxiv.org/abs/2611.27701v1)

**Authors**: Hao Ding, Zheng Shi, Dongxue Zhao, Huiying Bian, Meng Li, Xu Zheng, Kun Wang, Nanjian Wu, Jie Chen, Yimao Cai  
**Category**: cs.AR  
**Published**: 2026-11-23  
**Score**: 61.0  
**Type**: new  
**ArXiv ID**: 2611.27701v1  

#### Abstract
Speculative decoding (SD) accelerates large language model (LLM) inference by combining lightweight drafting with parallel target-model verification. However, its stages impose distinct resource demands: target verification requires high-throughput access to large weight sets, sequential drafting ex...

---

### 6. [BitPrefill: W1.58A4 Tensor-Core Acceleration for Compute-Bound LLM Prefill](https://arxiv.org/abs/2611.26657v1)

**Authors**: Fang Chen, Xuming Chen, Sanmukh Kuppannagari, Gourav Datta  
**Category**: cs.AR  
**Published**: 2026-11-23  
**Score**: 58.0  
**Type**: new  
**ArXiv ID**: 2611.26657v1  

#### Abstract
Low-bit quantization reduces large language model (LLM) inference cost, yet implementations optimized for memory-bound decode can leave compute-bound prefill on BF16 tensor cores. This gap matters for input-heavy workloads, including long-context and multimodal applications, where prefill can accoun...

---

### 7. [CTRL: Concurrent Training and Rollout for LLM Reinforcement Learning via GPU Co-Residency](https://arxiv.org/abs/2611.27119v1)

**Authors**: Ruijia Yang, Ruikai Li, Zeyi Wen  
**Category**: cs.DC  
**Published**: 2026-11-23  
**Score**: 55.0  
**Type**: new  
**ArXiv ID**: 2611.27119v1  

#### Abstract
Reinforcement learning (RL) post-training of large language models runs two GPU workloads with different hardware demands: rollout decoding, which is dominated by memory access and whose batch shrinks as responses finish, and a dense learner. Current systems either time-share every GPU between them,...

---

### 8. [MemOnce: A Scalable Memory Architecture for Large Language Models](https://arxiv.org/abs/2611.27973v1)

**Authors**: Chang Nie, Chaoyou Fu, Songlin Liu, Yiqing Hu, Caifeng Shan  
**Category**: cs.CL  
**Published**: 2026-11-23  
**Score**: 51.5  
**Type**: new  
**ArXiv ID**: 2611.27973v1  

#### Abstract
Deploying large language models (LLMs) in long-horizon and continual interactions requires maintaining reusable memory states for future inference, posing challenges for existing architectures. Standard Transformers accumulate layer-wise, token-level KV caches, incurring linear GPU memory growth and...

---

### 9. [Stratum: A Hardware-Software Co-Design Framework for SNN Inference on RISC-V](https://arxiv.org/abs/2611.27277v1)

**Authors**: Wajahat Riaz, Muhammad Adeel Pasha, Shahid Masud, Muhammad Ali Siddiqi  
**Category**: cs.AR  
**Published**: 2026-11-23  
**Score**: 50.5  
**Type**: new  
**ArXiv ID**: 2611.27277v1  

#### Abstract
Efficient spiking neural network (SNN) inference on RISC-V processors requires tracing implementation costs back to the compiler and hardware decisions that produce them. Training environments, compilers, and cycle-level simulators, however, typically operate as distinct tools, making this attributi...

---

### 10. [CarrierKV: An Edge LLM Accelerator with Positional Carrier Decomposition for Low-Bit KV Cache](https://arxiv.org/abs/2611.26857v1)

**Authors**: Junyi Luo, Xinting Jiang, Ruichen Qi, Gregory Kielian, Quan Cheng, Mehdi Saligane  
**Category**: cs.AR  
**Published**: 2026-11-23  
**Score**: 49.5  
**Type**: new  
**ArXiv ID**: 2611.26857v1  

#### Abstract
Long-context decoding on edge devices is limited by DRAM, because every generated token reads the whole, growing KV cache. 4-bit block-scaled formats such as NVFP4 reduce this traffic but degrade accuracy: on Qwen3-4B, NVFP4 lowers 32K RULER (seven tasks) from 92.6 to 79.4, and a Hadamard rotation l...

---

### 11. [Dynamic Token Merging for Efficient Vision-Language Models](https://arxiv.org/abs/2611.27064v1)

**Authors**: Chris Gu, Marco Andono Sie, Nathan Zhou, Christopher Potts, Julie Kallini  
**Category**: cs.AI  
**Published**: 2026-11-23  
**Score**: 49.0  
**Type**: new  
**ArXiv ID**: 2611.27064v1  

#### Abstract
Vision-language models (VLMs) represent each image with hundreds of visual tokens, which can make inference costly even when a prompt depends on only part of the image. Dynamic Token Merging (DTM), introduced in MrT5 for byte-level text encoders, learns which tokens to remove: a lightweight delete g...

---

### 12. [Efficient VLA Reinforcement Learning via Subchunk Rollouts in Latent World Models](https://arxiv.org/abs/2611.27645v1)

**Authors**: Nan Tang, Han-Tao Zhang, Jing-Cheng Pang, Hao-Nan Wang, Hao-Xiang Ren, Yi-Fei Sheng, Jun-Yin Ye, Tian Xu, Fan-Ming Luo, Hao-Xin Lin, Yang Yu  
**Category**: cs.LG  
**Published**: 2026-11-23  
**Score**: 48.5  
**Type**: new  
**ArXiv ID**: 2611.27645v1  

#### Abstract
Model-based reinforcement learning (MBRL) can improve pretrained vision-language-action (VLA) policies through imagined experiences. However, existing VLA-MBRL methods primarily rely on large-scale image or video generation world models, incurring large computational overhead. Latent world models of...

---

### 13. [Weave: Routing-Adaptive Runtime Warp Scheduling for MoE Megakernels](https://arxiv.org/abs/2611.27765v1)

**Authors**: Ziyu Huang, Yangjie Zhou, Chenhao Zhu, Hongzhe Yan, Tianwei Qiao, Sicheng He, Zihan Liu, Peng Yu, Shulai Zhang, Xingxun Tang, Xinhao Luo, Minyi Guo, Xiu Lin, Yinghao Yu, Guodong Yang, Liping Zhang, Shixuan Sun, Qingyun Chen, Jingwen Leng  
**Category**: cs.DC  
**Published**: 2026-11-23  
**Score**: 47.0  
**Type**: new  
**ArXiv ID**: 2611.27765v1  

#### Abstract
The Mixture-of-Experts (MoE) architecture is widely used in mainstream large language models. Under expert parallelism (EP), state-of-the-art systems fuse each MoE layer into a persistent megakernel for high performance. By the nature of EP, each GPU's communication and computation volumes vary with...

---

### 14. [Can Vision-Language Models Synthesize Executable Game-Playing Programs?](https://arxiv.org/abs/2611.27741v1)

**Authors**: Yao Tong, Jiaxin Qi, Dingyu Zhang, Jianqiang Huang  
**Category**: cs.AI  
**Published**: 2026-11-23  
**Score**: 46.5  
**Type**: new  
**ArXiv ID**: 2611.27741v1  

#### Abstract
Recent advances in vision-language models (VLMs) have endowed multimodal agents with increasingly strong visual perception and long-horizon reasoning capabilities, making VLM-based autonomous game playing feasible. Existing game benchmarks primarily evaluate whether an agent can select appropriate a...

---

### 15. [Topology Hub Optimal Transport: Eliminating Long Context Dilution at Flash Speed](https://arxiv.org/abs/2611.27951v1)

**Authors**: Dylan Forde  
**Category**: cs.LG  
**Published**: 2026-11-23  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2611.27951v1  

#### Abstract
Long-context models use sparse or structured attention to avoid quadratic cost, yet retrieving a small set of relevant facts embedded among hundreds of thousands of distractors degrades as normalization mass disperses with length. Hub-and-spoke optimal transport (OT) replaces the dense $L \times L$ ...

---

### 16. [Abstract What Varies, Reuse Longer Patterns: Efficient Offline Chain-of-Thought Compression](https://arxiv.org/abs/2611.27710v1)

**Authors**: Shibo Wang, Yuzhe He, Yifeng Zhao, Yunjiao Zhou, Zepeng Ning, Hanzhang Zhou, Kezhi Mao, Junlang Qian  
**Category**: cs.AI  
**Published**: 2026-11-23  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2611.27710v1  

#### Abstract
Offline chain-of-thought (CoT) compression creates shorter supervision for efficient reasoning, but per-example compressors repeatedly process similar expressions across traces, wasting compressor budget. Methods that reuse identical text across examples miss longer shared expressions when names, nu...

---

### 17. [When Are Images Needed in Multimodal Machine Translation? Text-Only Routing for On-Demand Visual Context](https://arxiv.org/abs/2611.27712v1)

**Authors**: Xinyu Wang, Yingfeng Luo, Yuxin Gao, Anxiang Ma, Jingbo Zhu, Tong Xiao  
**Category**: cs.AI  
**Published**: 2026-11-23  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2611.27712v1  

#### Abstract
Image-guided multimodal machine translation (MMT) leverages visual context to resolve translation-relevant uncertainty. However, prevailing systems either process images unconditionally or apply gating only after visual encoding, leaving redundant visual computation unavoidable. To mitigate this com...

---

### 18. [Improved Accuracy Scaling with Problem Complexity in LLM Arithmetic Reasoning Using Executable Symbolic Representations](https://arxiv.org/abs/2611.27203v1)

**Authors**: Yu-Bin Liu, Shi-Ju Ran  
**Category**: cs.LG  
**Published**: 2026-11-23  
**Score**: 41.5  
**Type**: new  
**ArXiv ID**: 2611.27203v1  

#### Abstract
High accuracy on mathematical benchmarks does not establish whether reasoning remains reliable as problem complexity increases. We examine how executable symbolic representations change accuracy scaling in large language models compared with natural-language reasoning. To address this limitation, we...

---

### 19. [Late-Time Dynamics of Flow Matching: Distance Geometry and Learning](https://arxiv.org/abs/2611.27653v1)

**Authors**: Umberto Biccari, Junqing Huang, Kang Liu, Enrique Zuazua  
**Category**: cs.LG  
**Published**: 2026-11-23  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2611.27653v1  

#### Abstract
Generative models transform simple random inputs into samples that resemble observed data. For a finite training set, a central question is how its geometry shapes the terminal dynamics and the probabilities assigned to individual samples. We address this question for flow matching with linear inter...

---

### 20. [Cruella: A Unified Microscaling and Floating-Point Dot-Product Unit for LLM Inference on FPGAs](https://arxiv.org/abs/2611.27323v1)

**Authors**: Jinho Yang, Taehyeong Kim, Mincheol Cha, Hyeoncheol Kim, Donggeun Kim, Nahye Kim, Yujin Lee, Ryeowook Ko, Woong Gyu Park, Jiwoong Park, Junsoo Kim, Tae-Hyoung Kim, Yongjun Park, Seongmin Hong, Joo-Young Kim  
**Category**: cs.AR  
**Published**: 2026-11-23  
**Score**: 39.0  
**Type**: new  
**ArXiv ID**: 2611.27323v1  

#### Abstract
The number formats that accelerators execute natively are fixed at fabrication, yet large language model (LLM) checkpoints are released with MXFP4 weights in the Microscaling (MX) formats standardized in 2023. FPGAs adopt new formats through bitstreams. However, to the best of our knowledge, no depl...

---

### 21. [Analysis of Multi-Client Inference Techniques for Vision-Language-Action Models](https://arxiv.org/abs/2611.26944v1)

**Authors**: Stefan de Lasa, Mohammadreza Mofayezi, Gennady Pekhimenko, Nandita Vijaykumar  
**Category**: cs.DC  
**Published**: 2026-11-23  
**Score**: 36.0  
**Type**: new  
**ArXiv ID**: 2611.26944v1  

#### Abstract
Vision-Language-Action models (VLAs) are a new class of machine learning model for generalizable robot control. While they enable robots to perform complex tasks in unseen environments, serving VLAs leaves hardware idle between inference passes and under-utilized during inference. Serving multiple c...

---

### 22. [Speculative Decoding Is Less Speculative Than You Think](https://arxiv.org/abs/2611.27891v1)

**Authors**: Guanning Zeng, Andrea Zanette  
**Category**: cs.AI  
**Published**: 2026-11-23  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2611.27891v1  

#### Abstract
Speculative decoding accelerates language-model inference by preparing candidate continuations before the target model generates them. Its efficiency depends on how well limited drafting computation anticipates the path the target will actually follow. Anticipating this path involves two sources of ...

---

### 23. [ORBIT: Offset-based Activation Steering for Cross-lingual Multimodal Fact Verification](https://arxiv.org/abs/2611.27421v1)

**Authors**: Huy Trieu, Duy-Minh Nguyen-Tran, Thanh-Dat Nguyen, Huy Tien Nguyen, Tung Le  
**Category**: cs.CL  
**Published**: 2026-11-23  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2611.27421v1  

#### Abstract
Multimodal fact verification faces a fundamental accessibility bottleneck: while large proprietary models exhibit cross-lingual robustness, small vision-language models suffer a severe, disproportionate accuracy collapse on low-resource languages. Closing this gap traditionally requires prohibitive ...

---

### 24. [Learning Inside Types: Epistemic Typestates for Safe Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2611.27631v1)

**Authors**: Lorenzo Bacchiani, Mario Bravetti, Giovanni Pau, Roberto Girau  
**Category**: cs.AI  
**Published**: 2026-11-23  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2611.27631v1  

#### Abstract
Type disciplines make programs safe by construction: components checked against each other's types compose into programs that cannot go wrong in the ways the types exclude. Types suit reinforcement learning: a type constrains what an agent may choose, not how it chooses, so the guarantee holds for e...

---

### 25. [Average-Depth Variable Execution via Request-Local Token Routing](https://arxiv.org/abs/2611.27738v1)

**Authors**: Pengjie Zheng, Mengwei Xie, Huan Yang, Si Wu, Pengfei Hu, Feng Li  
**Category**: cs.AI  
**Published**: 2026-11-23  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2611.27738v1  

#### Abstract
Layer skipping can reduce large language model inference costs, but a request budget does not specify how to allocate layer execution across generated tokens. We introduce \method{}, which allows tokens to execute different numbers of layers while matching each request's mean executed depth to a con...

---

### 26. [Writing Weights or Training Them? Spatial Reasoning through Weight-Space Programming and Low-Rank Adaptation](https://arxiv.org/abs/2611.27089v1)

**Authors**: Yalin Yang, Xiao Huang, Yanan Wu, Hao Yang, Ryan Zhenqi Zhou  
**Category**: cs.AI  
**Published**: 2026-11-23  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2611.27089v1  

#### Abstract
Weight-space programming lets a language model inspect and edit another model's weights, offering an alternative to gradient-based adaptation. We evaluated both approaches using Qwen3.5-0.8B on a fixed reference-frame task (128 items), StepGame (200 items), and two untrained distance-comparison task...

---

### 27. [Spatiotemporal Graph Neural Networks for Fault Detection and Structural Learning in Chemical Processes: Use Case on the Tennessee Eastman Process](https://arxiv.org/abs/2611.27698v1)

**Authors**: Rayane Ammar Khodja, Alexandre Voisin, Victor Costa, Fanny Casteran, Benoit Celse, Beno\^it Iung  
**Category**: cs.AI  
**Published**: 2026-11-23  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2611.27698v1  

#### Abstract
Classical Fault Detection and Diagnosis (FDD) methods, including many data-driven approaches, assume a static normal operating space and interpret deviations from a fixed reference as fault indicators. When Operating Conditions (OCs) vary over time, this assumption breaks down: legitimate transition...

---

### 28. [Contention-Aware Flexible Execution for Machine Learning Workloads](https://arxiv.org/abs/2611.26840v1)

**Authors**: Marco Kurzynski, Shaizeen Aga, Di Wu  
**Category**: cs.DC  
**Published**: 2026-11-23  
**Score**: 27.0  
**Type**: new  
**ArXiv ID**: 2611.26840v1  

#### Abstract
Concurrent kernel execution is a ubiquitous paradigm in artificial intelligence (AI) and machine learning (ML) across both training and inference. That said, concurrency causes potential slowdown as concurrent kernels contend for limited GPU resources (cores, caches, memory bandwidth), which are sha...

---

### 29. [Cannot Wait to Verify: Parallel Drafting to Eliminate Verifier Idle Time in Speculative Decoding](https://arxiv.org/abs/2611.27477v1)

**Authors**: Divya Jyoti Bajpai, Arun Verma, Manjesh Kumar Hanawal  
**Category**: cs.LG  
**Published**: 2026-11-23  
**Score**: 27.0  
**Type**: new  
**ArXiv ID**: 2611.27477v1  

#### Abstract
Autoregressive inference in large transformer models is limited by token-level sequential execution, resulting in high latency and low GPU utilization. Speculative decoding (SD) mitigates this bottleneck by introducing a draft-and-verifier model. However, the drafting stage remains sequential, leavi...

---

### 30. [WePM: Hierarchical Conflict Reconciliation for Unified MLLMs](https://arxiv.org/abs/2611.27365v1)

**Authors**: Zhiqiang Yuan, Qiwei Yan, Liwei Yang, Jinzhe Liu, Yang Liu, Zhongyan Hou, Liyan Xu, Peixiang Luo, Jiapei Zhang, Ying Deng, Jie Zhou, Jinchao Zhang  
**Category**: cs.AI  
**Published**: 2026-11-23  
**Score**: 26.5  
**Type**: new  
**ArXiv ID**: 2611.27365v1  

#### Abstract
Bringing multimodal intelligence from the cloud to users' devices keeps sensitive data local and reduces inference cost, but deploying a specialized model per capability duplicates vision-language capacity under tight memory and compute budgets. We formalize heterogeneous capability density (HCD), m...

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
