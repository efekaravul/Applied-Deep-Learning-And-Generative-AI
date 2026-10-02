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

1. **Multi-Class Classification From Scratch**  — a full PyTorch training loop written by hand: forward pass, loss, `backward()`, optimizer step, non-linearity's effect on separability, and model checkpointing with `state_dict`.
2. **CNN on CIFAR-10 & Desert101**  — convolution, pooling and a VGG-style architecture built block by block, with experiments compared in TensorBoard rather than trusted one at a time.
3. **Transfer Learning: Dog Breed Classifier**  — a pretrained backbone with a replaced classifier head, feature extraction vs. fine-tuning compared on the same split.
4. **Vision Transformer, Implemented Paper-Faithfully**  — patch embedding, the learnable class token and position embeddings, multi-head self-attention and the MLP block, assembled into a working ViT.
5. **GPT Trained From Scratch**  — tokenization and data batching, token + position embeddings, masked self-attention, and sampling from logits via `torch.multinomial`.

---

## 📂 Repository Structure

A numbered learning path, from Python fundamentals to generative models:


*   **`01 - Python Fundamentals and Advanced Python/`** : Core language foundations plus the advanced constructs the rest of the course assumes — comprehensions, functional built-ins, OOP and error handling — closing with the advanced-Python quiz assignment.
*   **`02 - PyTorch Fundamentals/`** : Tensor creation, `dtype`/`shape`/`device`, and the NumPy ↔ tensor bridge; indexing, slicing, `reshape`/`view`/`squeeze`/`permute` and the copy-vs-view distinction; element-wise arithmetic, matrix multiplication and the shape rules behind it, aggregation and broadcasting.
*   **`03 - Model Training and Prediction/`** : Four bilingual notebooks covering linear regression and binary classification. Regression progresses from manually defined weight/bias to `nn.Linear`; classification progresses from stacked linear layers to a ReLU network on a separate dataset. Covers 80/20 splits, tensor shapes, MSE and `BCEWithLogitsLoss`, SGD and Adam, forward → loss → `zero_grad()` → `backward()` → `step()`, evaluation with `eval()`/`inference_mode()`, accuracy, loss curves, prediction plots, and decision-boundary/probability visualizations. Planned extensions include multi-class classification and checkpoint saving/loading.
*   **`04 - Image Processing and CNN/`** *(planned)* : Images as tensors, normalization and `torchvision.transforms`; `Dataset`/`DataLoader` batching on CIFAR-10; convolution, pooling and output-shape arithmetic; a VGG-style architecture; Desert101 experiments; TensorBoard tracking; and pretrained `torchvision` models.
*   **`05 - Transfer Learning/`** *(planned)* : Freezing a pretrained backbone, replacing the classifier head, and matching the model's preprocessing transforms, applied to a dog-breed classifier and the transfer-learning assignment.
*   **`06 - NLP and Transformer Theory/`** *(planned)* : Tokenization, embeddings and sequence modelling; attention, multi-head self-attention, positional encoding, and the encoder/decoder split.
*   **`07 - Vision Transformer/`** *(planned)* : Patch embedding, a learnable class token and position embeddings, attention and MLP blocks with layer normalization and residual connections, and the assembled ViT model.
*   **`08 - GPT and LLM/`** *(planned)* : Preparing text batches, decoder-only architecture, next-token prediction, token and position embeddings, masked self-attention, temperature-controlled sampling with `torch.multinomial`, and end-to-end training.

Supporting directories and files:

* **`utils/`** : Shared device, training, and plotting helpers.
* **`data/`** : Local datasets, excluded from Git.
* **`models/`** : Local model weights, excluded from Git.
* **`runs/`** : Local TensorBoard logs, excluded from Git.
* **`requirements.txt`** and **`check_env.py`** : Dependency list and environment checks.

### Training Notebooks / Eğitim Notebook'ları

| Notebook | English | Türkçe |
| --- | --- | --- |
| [pytorch_training_steps.ipynb](03%20-%20Model%20Training%20and%20Prediction/pytorch_training_steps.ipynb) | Manually registered weight and bias; 250 training epochs; training/test loss curves and learned parameters. | Elle kaydedilen ağırlık ve bias; 250 epoch eğitim; eğitim/test kayıp eğrileri ve öğrenilen parametreler. |
| [pytorch_training_structural.ipynb](03%20-%20Model%20Training%20and%20Prediction/pytorch_training_structural.ipynb) | `nn.Linear(1, 1)` with `(N, 1)` float32 tensors; 120 training epochs; test predictions compared visually with true grades. | `(N, 1)` şeklinde float32 tensörlerle `nn.Linear(1, 1)`; 120 epoch eğitim; test tahminlerinin gerçek notlarla görsel karşılaştırması. |
| [linear_data_practice.ipynb](03%20-%20Model%20Training%20and%20Prediction/linear_data_practice.ipynb) | Binary email classification with `2 → 5 → 1` linear layers, no hidden activation, `BCEWithLogitsLoss`, and SGD; 100 epochs; analytical straight decision boundary. | `2 → 5 → 1` doğrusal katmanlarla, gizli aktivasyon olmadan ikili e-posta sınıflandırması; `BCEWithLogitsLoss` ve SGD; 100 epoch; analitik doğru karar sınırı. |
| [nonlinear_data_practice.ipynb](03%20-%20Model%20Training%20and%20Prediction/nonlinear_data_practice.ipynb) | Binary seismic-event classification with `2 → 10 → ReLU → 10 → ReLU → 1`, Adam, and 500 epochs; probability maps on a 300 × 300 grid. | `2 → 10 → ReLU → 10 → ReLU → 1`, Adam ve 500 epoch ile ikili deprem olayı sınıflandırması; 300 × 300 ızgarada olasılık haritaları. |

**English:** Each non-empty code cell is preceded by English and Turkish Markdown explanations. Run the cells in order with the notebook folder as the working directory so `../data/` resolves correctly. Supply the CSV files locally; datasets are excluded from Git:

**Türkçe:** Her dolu kod hücresinin önünde İngilizce ve Türkçe Markdown açıklamaları bulunur. `../data/` yolunun doğru çözülmesi için notebook klasörünü çalışma dizini olarak kullanıp hücreleri sırayla çalıştır. CSV dosyalarını yerel olarak sağla; veri setleri Git'e dahil değildir:

| Notebook(s) | Required local file / Gerekli yerel dosya |
| --- | --- |
| `pytorch_training_steps`, `pytorch_training_structural` | `data/06-study_hours_grades.csv` |
| `linear_data_practice` | `data/08-email_classification_svm.csv` |
| `nonlinear_data_practice` | `data/08-seismic_activity_svm.csv` |

**English:** The classification notebooks explain why stacked linear layers still give a linear boundary, why the loss receives logits while accuracy uses labels, and how ReLU enables nonlinear boundaries. They also document existing code details: the PyTorch seed is set after model creation; the nonlinear loop does not restore `train()` each epoch; its plot colors probabilities without explicitly drawing the 0.5 contour. The two exercises use different datasets, so their accuracy scores are not a controlled comparison of architectures.

**Türkçe:** Sınıflandırma notebook'ları, ardışık doğrusal katmanların neden doğrusal sınır verdiğini, kaybın neden logits ve doğruluğun neden etiket kullandığını, ReLU'nun doğrusal olmayan sınırları nasıl mümkün kıldığını anlatır. Mevcut kod ayrıntıları da açıklanır: PyTorch tohumu model oluşturulduktan sonra ayarlanır; doğrusal olmayan döngü her epoch'ta `train()` moduna dönmez; grafik 0.5 konturunu açıkça çizmeden olasılıkları renklendirir. İki alıştırma farklı veri setleri kullandığından doğrulukları mimarilerin kontrollü karşılaştırması değildir.

The classification notebooks use colored step headers, section labels, language headings, and learning-path tables for easier navigation. / Sınıflandırma notebook'ları kolay takip için renkli adım başlıkları, bölüm etiketleri, dil başlıkları ve öğrenme rotası tabloları kullanır.


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
