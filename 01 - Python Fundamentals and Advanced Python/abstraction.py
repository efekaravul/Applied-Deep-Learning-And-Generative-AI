# 🇹🇷 Soyutlama (Abstraction): Ortak arayüzü tanımlayıp uygulama detayını alt sınıflara bırakmaktır.
#     Soyut sınıftan nesne üretilemez, alt sınıflar soyut metotları yazmak zorundadır.
# 🇬🇧 Abstraction: defining a common interface and leaving the implementation details to
#     subclasses. An abstract class cannot be instantiated and subclasses must implement its abstract methods.

from abc import ABC, abstractmethod  # 🇹🇷 ABC = Abstract Base Class; soyut sınıf altyapısı / 🇬🇧 ABC = Abstract Base Class; the abstract class infrastructure

class Car(ABC):  # 🇹🇷 ABC'den türeyen sınıf soyut olur, Car() denemez / 🇬🇧 A class deriving from ABC becomes abstract, Car() is not allowed

    @abstractmethod  # 🇹🇷 Bu metodu yazmayan alt sınıftan nesne üretilemez / 🇬🇧 A subclass that does not implement this method cannot be instantiated
    def maxSpeed(self):
        pass  # 🇹🇷 Gövde boş: sadece kural, uygulama alt sınıfta / 🇬🇧 Empty body: only the contract, the implementation lives in the subclass

class Tesla(Car):  # 🇹🇷 Soyut sınıfı somutlaştıran alt sınıf / 🇬🇧 Subclass that makes the abstract class concrete

    def maxSpeed(self):  # 🇹🇷 Soyut metodun zorunlu uygulaması / 🇬🇧 The required implementation of the abstract method
        print("Max speed of tesla 200 km/h")


tesla = Tesla()
tesla.maxSpeed()

class Mercedes(Car):

    def maxSpeed(self):  # 🇹🇷 Her alt sınıf aynı arayüzü kendi içeriğiyle doldurur / 🇬🇧 Each subclass fills the same interface with its own content
        print("Max speed of mercedes 250 km/h")

mercedes = Mercedes()
print(mercedes.maxSpeed())  # 🇹🇷 Metot nesne üzerinden çağrılmalı; sınıf üzerinden (Mercedes.maxSpeed()) çağrılırsa self eksik kalır / 🇬🇧 The method must be called on the object; calling it on the class (Mercedes.maxSpeed()) leaves self missing
