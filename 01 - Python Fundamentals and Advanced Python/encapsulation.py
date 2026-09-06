# 🇹🇷 Kapsülleme (Encapsulation): Verinin doğrudan dışarıdan değiştirilmesini engelleyip
#     erişimi sınıfın kendi metotları üzerinden sağlamaktır.
# 🇬🇧 Encapsulation: hiding data from direct outside access and exposing it only
#     through the class's own methods.

def Phone():  # 🇹🇷 DİKKAT: burada "class" yerine "def" yazılmış, bu yüzden Phone bir sınıf değil fonksiyon olur / 🇬🇧 NOTE: "def" was written instead of "class", so Phone is a function, not a class
    def __init__(self,name,price):
        self.name = name  # 🇹🇷 Public (herkese açık) öznitelik: dışarıdan okunup değiştirilebilir / 🇬🇧 Public attribute: readable and writable from outside
        self.__price = price  # 🇹🇷 Çift alt çizgi -> private öznitelik, isim karıştırma (name mangling) ile dışarıdan gizlenir / 🇬🇧 Double underscore -> private attribute, hidden from outside via name mangling

    def info(self):  # 🇹🇷 Getter benzeri metot: private veriyi kontrollü biçimde okur / 🇬🇧 Getter-like method: reads the private data in a controlled way
        print(f"{self.name} has a price of {self.__price}")

    def change_price(self, price):  # 🇹🇷 Setter benzeri metot: private veriyi kontrollü biçimde değiştirir / 🇬🇧 Setter-like method: changes the private data in a controlled way
        self.__price = price
