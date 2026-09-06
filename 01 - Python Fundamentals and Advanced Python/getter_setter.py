# 🇹🇷 Getter / Setter ve @property: Private özniteliklere kontrollü erişim sağlar. Dışarıdan
#     normal bir değişken gibi kullanılır, ama arka planda doğrulama yapan metotlar çalışır.
# 🇬🇧 Getter / setter and @property: provide controlled access to private attributes. From the
#     outside they look like plain variables, but validating methods run behind the scenes.

class Person:

    def __init__(self,name,age):
        self.__name = name  # 🇹🇷 Çift alt çizgi -> private, dışarıdan doğrudan erişilmesi istenmez / 🇬🇧 Double underscore -> private, not meant to be accessed directly from outside
        self.__age = age

    @property  # 🇹🇷 Metodu okunabilir bir özniteliğe çevirir: efe.name() değil efe.name / 🇬🇧 Turns the method into a readable attribute: efe.name instead of efe.name()
    def name(self):
        return self.__name  # 🇹🇷 Getter: private değeri okur / 🇬🇧 Getter: reads the private value

    @name.setter  # 🇹🇷 efe.name = ... atamasında çalışacak metot / 🇬🇧 The method that runs on the assignment efe.name = ...
    def name(self,value):
        if not isinstance(value,str):  # 🇹🇷 Setter'ın asıl faydası: atamadan önce doğrulama / 🇬🇧 The real benefit of a setter: validation before assignment
            raise ValueError("name must be a string")
        if len(value) < 2:
            raise ValueError("name must be at least 2 characters")
        self.__name = value

    @name.deleter  # 🇹🇷 del efe.name çağrıldığında çalışır / 🇬🇧 Runs when del efe.name is called
    def name(self):
        self.__name = None

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if not isinstance(value,int):
            raise ValueError("age must be an integer")
        if value <= 0:
            raise ValueError("age must be greater than 0")
        self.__age = value




efe = Person("Efe",22)
print(efe.name)  # 🇹🇷 Parantezsiz kullanım: getter otomatik çalışır / 🇬🇧 Used without parentheses: the getter runs automatically

efe.name = "Efe Karavul"  # 🇹🇷 Atama setter'ı tetikler, doğrulamadan geçer / 🇬🇧 The assignment triggers the setter and passes validation
print(efe.name)

efe.name = 70  # 🇹🇷 Geçersiz tip: setter ValueError fırlatır ve program burada durur / 🇬🇧 Invalid type: the setter raises ValueError and the program stops here
print(efe.name)

del efe.name  # 🇹🇷 deleter'ı çalıştırır, __name None olur / 🇬🇧 Runs the deleter, __name becomes None
print(efe.name)

print(efe.age)

efe.age = -20  # 🇹🇷 age setter'ındaki pozitiflik kuralına takılır / 🇬🇧 Blocked by the positivity rule in the age setter
print(efe.age)
