"""Kurulumun dogru yapildigini kontrol eder: torch surumu, CUDA, ornek tensor."""

import torch
import torchvision

print(f"PyTorch      : {torch.__version__}")
print(f"TorchVision  : {torchvision.__version__}")
print(f"CUDA var mi  : {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"GPU          : {torch.cuda.get_device_name(0)}")
    print(f"CUDA surumu  : {torch.version.cuda}")
else:
    print("GPU          : yok, CPU kullanilacak")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = torch.randn(3, 3, device=device)
print(f"\nOrnek tensor ({device}):\n{x}")
print("\nOrtam hazir.")
