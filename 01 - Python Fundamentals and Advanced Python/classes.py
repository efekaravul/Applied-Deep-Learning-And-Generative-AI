# 🇹🇷 Sınıflar (Classes): Nesnelerin ortak veri ve davranışlarını tanımlayan şablonlardır.
# 🇬🇧 Classes: templates that define the shared data and behaviour of objects.

class Person():
    def __init__(self, name, age, gender, job):  # 🇹🇷 Yapıcı metot: nesne oluşturulurken otomatik çalışır / 🇬🇧 Constructor: runs automatically when an object is created
        self.name = name  # 🇹🇷 self.<isim> = örnek (instance) değişkeni, her nesneye özeldir / 🇬🇧 self.<name> = instance attribute, unique to each object
        self.age = age
        self.gender = gender
        self.job = job

    def printName(self):  # 🇹🇷 Metot: sınıfa ait fonksiyon, ilk parametresi her zaman self'tir / 🇬🇧 Method: a function of the class, its first parameter is always self
        print(self.name)

efe = Person("Efe",22,"Male","Developer")  # 🇹🇷 Sınıftan bir nesne (instance) üretiyoruz / 🇬🇧 Creating an object (instance) from the class

print(efe.name)
print(efe.printName())  # 🇹🇷 Metot zaten print ediyor ve None döndürüyor, bu yüzden ekranda ayrıca None görünür / 🇬🇧 The method already prints and returns None, so None is also displayed
print(efe.job)

class Dog():
    year = 7  # 🇹🇷 Sınıf değişkeni: tüm nesneler tarafından paylaşılır / 🇬🇧 Class attribute: shared by all instances
    def __init__(self,age=5):  # 🇹🇷 age için varsayılan değer verildi / 🇬🇧 age has a default value
        self.age = age
        self.dogHumanAge = age * self.year  # 🇹🇷 Sınıf değişkenine self üzerinden erişilebilir / 🇬🇧 The class attribute can be accessed through self
        print("dog instance created")

    def humanAge(self):
        return self.age * self.year  # 🇹🇷 Metot değer döndürür, ekrana yazdırmaz / 🇬🇧 The method returns a value instead of printing it


myDog = Dog(3)

print(myDog.age)
print(myDog.humanAge())  # 🇹🇷 Metot çağrısı: parantez gerekli / 🇬🇧 Method call: parentheses required
print(myDog.dogHumanAge())  # 🇹🇷 Bu bir metot değil, öznitelik; parantezsiz yazılmalı (dogHumanAge) / 🇬🇧 This is an attribute, not a method; it must be written without parentheses

barley = Dog()  # 🇹🇷 Argüman verilmezse varsayılan age=5 kullanılır / 🇬🇧 Without an argument the default age=5 is used
