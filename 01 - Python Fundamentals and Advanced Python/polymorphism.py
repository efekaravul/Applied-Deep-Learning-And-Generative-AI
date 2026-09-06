# 🇹🇷 Çok biçimlilik (Polymorphism): Farklı sınıfların aynı isimli metodu kendine göre
#     uygulaması; böylece nesneler tek bir arayüz üzerinden kullanılabilir.
# 🇬🇧 Polymorphism: different classes implementing a method with the same name in their
#     own way, so objects can be used through a single common interface.

class Banana():
    def __init__(self, name):
        self.name = name

    def info(self):  # 🇹🇷 Aynı isimli metot, Banana'ya özgü davranış / 🇬🇧 Same method name, behaviour specific to Banana
        return f"100 calories {self.name}"

class Apple():  # 🇹🇷 Banana ile akraba değil; ortak olan tek şey metot isimleri (duck typing) / 🇬🇧 Not related to Banana; only the method names are shared (duck typing)
    def __init__(self, name):
        self.name = name

    def info(self):  # 🇹🇷 Aynı isim, farklı gövde -> çok biçimlilik / 🇬🇧 Same name, different body -> polymorphism
        return f"150 calories {self.name}"

banana = Banana("Banana")
print(banana.info())

apple = Apple("Apple")
print(apple.info())

fruit_list = [banana, apple]  # 🇹🇷 Farklı tipteki nesneler aynı listede toplanabilir / 🇬🇧 Objects of different types can be collected in the same list

for fruit in fruit_list:
    print(fruit.info())  # 🇹🇷 Hangi metodun çalışacağı nesnenin tipine göre çalışma anında belirlenir / 🇬🇧 Which method runs is decided at runtime according to the object's type
