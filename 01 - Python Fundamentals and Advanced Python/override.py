# 🇹🇷 Ezme (Override): Alt sınıfın, üst sınıftan miras aldığı metodu aynı isimle yeniden yazmasıdır.
#     @override dekoratörü niyeti belirtir; üst sınıfta öyle bir metot yoksa tip denetleyici uyarır.
# 🇬🇧 Override: a subclass rewriting an inherited method under the same name. The @override
#     decorator states the intent; a type checker warns if no such method exists in the parent.

from typing import override  # 🇹🇷 Python 3.12+ ile gelir / 🇬🇧 Available from Python 3.12 onwards

class Shape:

    def area(self) -> float:  # 🇹🇷 Üst sınıftaki varsayılan davranış, alt sınıflarca ezilmesi beklenir / 🇬🇧 Default behaviour in the parent, expected to be overridden by subclasses
        return 0.0

    def perimeter(self) -> float:
        return 0.0


class Rectangle(Shape):

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @override  # 🇹🇷 Bu metot üst sınıftaki area'yı bilerek eziyor / 🇬🇧 This method deliberately overrides area from the parent
    def area(self) -> float:
        return self.width * self.height  # 🇹🇷 Dikdörtgene özgü gerçek hesap / 🇬🇧 The real calculation specific to a rectangle

    @override
    def perimeter(self) -> float:
        return 2 * self.width + self.height  # 🇹🇷 DİKKAT: doğru çevre formülü 2 * (width + height) olmalı / 🇬🇧 NOTE: the correct perimeter formula should be 2 * (width + height)

rectangle = Rectangle(2, 3)
print(rectangle.area())  # 🇹🇷 Shape'in değil Rectangle'ın metodu çalışır / 🇬🇧 Rectangle's method runs, not Shape's
print(rectangle.perimeter())
