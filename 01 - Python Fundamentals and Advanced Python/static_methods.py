# 🇹🇷 Statik metotlar (Static Methods): Ne self ne cls alır. Sınıfın verisine ihtiyaç duymayan,
#     ama konu olarak sınıfa ait olan yardımcı fonksiyonlardır.
# 🇬🇧 Static methods: take neither self nor cls. Helper functions that need no class or instance
#     data but belong to the class topically.

class MathOperations:

    @staticmethod  # 🇹🇷 Metodu statik yapar; nesne oluşturmadan çağrılabilir / 🇬🇧 Makes the method static; it can be called without creating an instance
    def add(x,y):
        return x+ y  # 🇹🇷 Sadece parametrelerle çalışır, self kullanılmaz / 🇬🇧 Works only with its parameters, self is not used

    @staticmethod
    def divide(x,y):
        return x/y


print(MathOperations.add(2,3))  # 🇹🇷 Nesne üretmeden sınıf üzerinden çağrı / 🇬🇧 Called on the class without creating an instance
print(MathOperations.divide(2,3))
