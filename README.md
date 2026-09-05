# 🔥 Applied Deep Learning & Generative AI

100 günlük derin öğrenme eğitimi boyunca yazılan notebook'lar, script'ler ve ödevler.
Python ileri seviyeden başlayıp PyTorch temelleri, CNN, Transfer Learning, Vision Transformer
ve GPT/LLM eğitimine kadar tek bir öğrenme hattını takip eder.

Her gün ayrı bir klasör, her gün ayrı bir commit.

---

## 📁 Klasör Yapısı

| Klasör | Günler | İçerik |
|---|---|---|
| `00 - Bonus - Python ile Programlamaya Giris` | Bonus | Python'a giriş (61 ders) |
| `01 - Python Temelleri ve Ileri Seviye` | 1 – 9 | Python temelleri, ileri seviye konular, quiz ödevi |
| `02 - PyTorch Temelleri` | 10 – 12 | Tensor'lar, tensor işlemleri ve operasyonlar |
| `03 - Makine Ogrenmesi` | 13 – 14 | Hızlandırılmış ML ve matematiksel detaylar |
| `04 - Derin Ogrenmeye Giris` | 15 – 19 | Aktivasyon fonksiyonları, loss/cost, optimizer'lar |
| `05 - Model Egitimi ve Tahminleme` | 20 – 32 | Eğitim döngüsü, non-linearity, multi-class, model kaydetme |
| `06 - Goruntu Isleme ve CNN` | 33 – 49 | Görüntü işleme, CIFAR-10, CNN, VGG, TensorBoard |
| `07 - Transfer Learning` | 50 – 57 | Transfer learning ve köpek türü sınıflandırıcı |
| `08 - NLP ve Transformer Teori` | 58 – 59 | NLP ve Transformer teorisi |
| `09 - Vision Transformer` | 60 – 80 | Patching, learnable class/position, MLP block, ViT |
| `10 - GPT ve LLM` | 81 – 86 | GPT mimarisi, embedding & attention, LLM eğitimi |
| `11 - Kapanis Projesi` | 87 – 100 | Kapanış projesi ve kapanış |

Ortak klasörler:

- `utils/` — her notebook'ta tekrar kullanılan yardımcı modüller
  (`get_device`, `set_seed`, `train`/`test_step`, loss eğrisi ve karar sınırı çizimleri)
- `data/` — veri setleri (lokal, `.gitignore`'da)
- `models/` — kaydedilen model ağırlıkları (lokal, `.gitignore`'da)
- `runs/` — TensorBoard logları (lokal, `.gitignore`'da)

---

## ⚙️ Kurulum

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

GPU (CUDA 12.1) kullanacaksan PyTorch'u ayrı kur:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

Kurulumu doğrula:

```bash
python check_env.py
```

---

## 🧰 utils Kullanımı

Notebook'lar alt klasörlerde olduğu için proje kökünü `sys.path`'e eklemek gerekir:

```python
import sys, pathlib
sys.path.append(str(pathlib.Path.cwd().parents[1]))  # proje kökü

from utils import get_device, set_seed, train, plot_loss_curves

set_seed(42)
device = get_device()
```

---

## 📅 Günlük Akış

1. O günün klasörüne notebook / script yaz.
2. `git add .`
3. `git commit -m "feat(gun-XX): <konu>"`
4. `git push`
