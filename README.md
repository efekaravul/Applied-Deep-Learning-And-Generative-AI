# 🔥 Applied Deep Learning & Generative AI

A deep learning study repository, built in the same working style as its sibling repo
[Applied Data Engineering & Machine Learning](https://github.com/efekaravul/Applied-Data-Engineering-And-Machine-Learning):
one numbered learning path, one folder per topic, one commit per study day.

The path starts at advanced Python and PyTorch tensors and ends at a Vision Transformer and a
GPT trained from scratch. Every notebook is documented **bilingually (🇹🇷 Türkçe / 🇬🇧 English)**
and explains the *reasoning*, not just the code. Where a run produces a wrong number, the notebook
says so, shows the corrected value, and explains what made the bug invisible — those write-ups are
deliberately kept rather than quietly fixed, because knowing *how* a silent bug hides is the
transferable skill.

> **Status:** in progress. The structure below is the full curriculum; each section fills in as the
> work is committed. Completed milestones are promoted into **Featured Work** with their actual
> measured numbers — nothing is listed there before it has been run.

---

## 🚀 Featured Work

*Populated as milestones land. Each entry will state the dataset, the architecture, the measured
result, and the trade-off or bug that made the result worth writing down.*

Planned milestones, in the order the curriculum reaches them:

1. **Multi-Class Classification From Scratch** *(Days 20–32)* — a full PyTorch training loop written by hand: forward pass, loss, `backward()`, optimizer step, non-linearity's effect on separability, and model checkpointing with `state_dict`.
2. **CNN on CIFAR-10 & Desert101** *(Days 33–49)* — convolution, pooling and a VGG-style architecture built block by block, with experiments compared in TensorBoard rather than trusted one at a time.
3. **Transfer Learning: Dog Breed Classifier** *(Days 50–57)* — a pretrained backbone with a replaced classifier head, feature extraction vs. fine-tuning compared on the same split.
4. **Vision Transformer, Implemented Paper-Faithfully** *(Days 60–80)* — patch embedding, the learnable class token and position embeddings, multi-head self-attention and the MLP block, assembled into a working ViT.
5. **GPT Trained From Scratch** *(Days 81–86)* — tokenization and data batching, token + position embeddings, masked self-attention, and sampling from logits via `torch.multinomial`.

---

## 📂 Repository Structure

A numbered learning path, from Python fundamentals to generative models:

*   **`00 - Bonus - Introduction to Programming with Python/`** — the bonus introductory Python track (61 lessons), kept separate from the main 100-day path.
*   **`01 - Python Fundamentals and Advanced Python/`** *(Days 1–9)*: Core language foundations plus the advanced constructs the rest of the course assumes — comprehensions, functional built-ins, OOP and error handling — closing with the advanced-Python quiz assignment.
*   **`02 - PyTorch Fundamentals/`** *(Days 10–12)*: Tensor creation, `dtype`/`shape`/`device`, and the NumPy ↔ tensor bridge; indexing, slicing, `reshape`/`view`/`squeeze`/`permute` and the copy-vs-view distinction; element-wise arithmetic, matrix multiplication and the shape rules behind it, aggregation and broadcasting.
*   **`03 - Machine Learning/`** *(Days 13–14)*: An accelerated pass over the machine-learning vocabulary deep learning builds on, followed by the underlying mathematics — derivatives, the chain rule, and gradients as the actual mechanism behind backpropagation.
*   **`04 - Introduction to Deep Learning/`** *(Days 15–19)*: The neuron, the layer and forward propagation; activation functions (ReLU, Sigmoid, Tanh, Softmax) and where each one fails (vanishing gradients, dead ReLUs); loss and cost functions matched to the output layer — MSE/MAE for regression, BCE and Cross-Entropy for classification, and why logits vs. probabilities decides which loss is correct; optimizers from SGD and Momentum through RMSProp to Adam, with the learning rate treated as the single most consequential hyperparameter.
*   **`05 - Model Training and Prediction/`** *(Days 20–32)*: The training loop written by hand — `zero_grad()` → forward → loss → `backward()` → `step()` — with `eval()`/`inference_mode()` discipline on the test side. Then non-linearity, shown on non-linearly-separable data where a stack of linear layers is still just one linear layer; multi-class output via `CrossEntropyLoss` and logits → `softmax` → `argmax`; `state_dict`-based saving and loading; and the pretrained-model assignment.
*   **`06 - Image Processing and CNN/`** *(Days 33–49)*: Images as tensors — channels, normalization and `torchvision.transforms`; `Dataset`/`DataLoader` batching on CIFAR-10; `kernel_size`, `stride`, `padding` and pooling with the output-shape arithmetic that ties them together; a VGG-style architecture built block by block; the larger applied Desert101 study; TensorBoard experiment tracking; and working with pretrained `torchvision` models.
*   **`07 - Transfer Learning/`** *(Days 50–57)*: Freezing a pretrained backbone, replacing the classifier head, and matching the model's own preprocessing transforms — applied to a dog-breed classifier and then to the transfer-learning assignment.
*   **`08 - NLP and Transformer Theory/`** *(Days 58–59)*: Tokenization, embeddings and the sequence-modelling problem; then attention, multi-head self-attention, positional encoding, and the encoder/decoder split.
*   **`09 - Vision Transformer/`** *(Days 60–80)*: Reading the ViT paper as an architecture spec and the transform choices it dictates; patching — turning an image into a sequence, the step that lets a language architecture read pixels; the learnable class token and position embeddings; the MLP block with layer normalization and residual connections; the assembled model; and the course's capstone assignment.
*   **`10 - GPT and LLM/`** *(Days 81–86)*: The decoder-only architecture and preparing text into training batches; next-token prediction as the training objective; token and position embeddings with masked self-attention; logits → text via temperature and `torch.multinomial` sampling; and training the model end to end.
*   **`11 - Closing Project/`** *(Days 87–100)*: The closing project and wrap-up.

Shared infrastructure:

*   **`utils/`** — the code every notebook would otherwise repeat: `get_device()` and `set_seed()` for reproducibility, `train_step`/`test_step`/`train` as the standard training loop, and `plot_loss_curves`/`plot_predictions`/`plot_decision_boundary` for evaluation plots.
*   **`check_env.py`** — verifies the install: PyTorch/TorchVision versions, CUDA availability, and a sample tensor on the selected device.

> Datasets (`data/`), model weights (`models/`) and TensorBoard logs (`runs/`) are kept locally and
> intentionally excluded from version control (see `.gitignore`) to keep the repository lightweight.

---

## 🛠️ Technical Skills & Stack

**Languages & Core Libraries:** Python 3.12 · `PyTorch` · `TorchVision` · `torchinfo` · `torchmetrics` · `NumPy` · `Pandas` · `Scikit-Learn` · `Matplotlib` · `Seaborn` · `OpenCV` · `Transformers` · `TensorBoard` · Jupyter · PyCharm · Git

* **PyTorch Fundamentals:** Tensor creation and `dtype`/`device` management, shape manipulation (`reshape`, `view`, `permute`, `squeeze`), broadcasting and matrix multiplication, autograd and the computation graph, and device-agnostic CPU/GPU code
* **Neural Network Building Blocks:** `nn.Module` subclassing, `nn.Sequential`, linear layers, activation functions (ReLU, Sigmoid, Tanh, Softmax), loss functions matched to the output layer (`MSELoss`, `BCEWithLogitsLoss`, `CrossEntropyLoss`), and optimizers (SGD, Momentum, RMSProp, Adam)
* **Training Discipline:** The hand-written training loop, `train()`/`eval()` mode switching, `inference_mode()`, learning-rate selection, over/underfitting diagnosis read off loss curves, and `state_dict`-based checkpointing
* **Computer Vision:** Images as tensors, `torchvision.transforms` and data augmentation, custom `Dataset`/`DataLoader` pipelines, convolution/pooling and output-shape arithmetic, VGG-style CNN architectures, and pretrained-model fine-tuning
* **Transfer Learning:** Backbone freezing vs. full fine-tuning, classifier-head replacement, and reusing a pretrained model's own preprocessing transforms rather than improvising new ones
* **Transformers:** Attention and multi-head self-attention, positional encoding, layer normalization and residual connections; Vision Transformer patch embedding, class token and position embeddings; decoder-only GPT with causal masking, next-token prediction, and temperature-controlled `multinomial` sampling
* **Experiment Tracking:** TensorBoard-logged runs compared against each other, with `set_seed()` reproducibility so a difference between two runs is attributable to the change and not to the shuffle
* **Software Engineering:** Modular repository architecture with a shared `utils/` package, Git version control with Conventional Commits, one commit per study day, and bilingual (🇹🇷/🇬🇧) technical documentation on every notebook

---

📫 **Contact:** [efekaravul@gmail.com](mailto:efekaravul@gmail.com) · [Kaggle](https://www.kaggle.com/efekaravul) · [GitHub](https://github.com/efekaravul)
