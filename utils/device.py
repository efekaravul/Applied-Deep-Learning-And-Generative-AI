"""Cihaz secimi ve tekrarlanabilirlik (reproducibility) yardimcilari."""

import random

import numpy as np
import torch


def get_device() -> torch.device:
    """CUDA varsa GPU, yoksa CPU dondurur."""
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def set_seed(seed: int = 42) -> None:
    """Python, NumPy ve PyTorch icin ayni tohumu ayarlar.

    Ayni sonuclari tekrar uretebilmek icin her notebook'un basinda cagrilir.
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
