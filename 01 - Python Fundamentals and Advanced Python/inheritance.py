# 🇹🇷 Kalıtım (Inheritance): Bir sınıfın başka bir sınıfın özellik ve metotlarını devralmasıdır.
# 🇬🇧 Inheritance: a class taking over the attributes and methods of another class.

class Musician():  # 🇹🇷 Ana (base/parent) sınıf / 🇬🇧 Base (parent) class

    def __init__(self,name):
        self.name = name
        print("musician created")


class MusicianPlus(Musician):  # 🇹🇷 Parantez içindeki sınıftan miras alınır / 🇬🇧 Inherits from the class written in parentheses
    def __init__(self,name):  # 🇹🇷 Alt sınıf kendi __init__'ini yazarsa üst sınıfınkini ezer (override) / 🇬🇧 If the subclass defines its own __init__, it overrides the parent's
        Musician.__init__(self,name)  # 🇹🇷 Üst sınıfın yapıcısını çağırır, böylece self.name de kurulur (super().__init__(name) ile aynı iş) / 🇬🇧 Calls the parent constructor so self.name is also set (same as super().__init__(name))
        print("musician plus created")

musician = MusicianPlus("Efe")

print(musician.name)  # 🇹🇷 name özniteliği üst sınıftan miras alındı / 🇬🇧 The name attribute was inherited from the parent class
