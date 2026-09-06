# 🇹🇷 Sınıf metotları (Class Methods): İlk parametresi cls olan, nesneye değil sınıfın kendisine
#     bağlı metotlardır. Sınıf değişkenlerine erişmek ve alternatif kurucular (factory) yazmak için kullanılır.
# 🇬🇧 Class methods: methods whose first parameter is cls, bound to the class itself rather than to an
#     instance. Used to access class attributes and to write alternative constructors (factories).

class Pizza:

    total_pizzas = 0  # 🇹🇷 Sınıf değişkeni: tüm nesnelerde ortak sayaç / 🇬🇧 Class attribute: a counter shared by all instances

    def __init__(self, ingredients):

        self.ingredients = ingredients
        Pizza.total_pizzas += 1  # 🇹🇷 self değil sınıf üzerinden artırılır, yoksa nesneye özel yeni bir değişken oluşur / 🇬🇧 Incremented on the class, not on self; otherwise a new instance-level attribute would be created

    @classmethod  # 🇹🇷 Metodu sınıf metoduna çevirir; self yerine cls alır / 🇬🇧 Turns the method into a class method; it takes cls instead of self
    def margherita(cls):
        return cls(["peynir","domates","fesleğen"])  # 🇹🇷 cls(...) sınıfın kendisini çağırır -> hazır ayarlı nesne üreten "factory" / 🇬🇧 cls(...) calls the class itself -> a factory producing a preconfigured object

    @classmethod
    def pepperoni(cls):
        return cls(["peynir", "sucuk", "fesleğen"])  # 🇹🇷 Aynı desen, farklı varsayılan malzemelerle / 🇬🇧 Same pattern with different default ingredients

    @classmethod
    def get_total_pizzas(cls):
        return cls.total_pizzas  # 🇹🇷 cls üzerinden sınıf değişkenine erişim; nesneye ihtiyaç yok / 🇬🇧 Accessing the class attribute through cls; no instance needed



pizza1 = Pizza.margherita()  # 🇹🇷 __init__ yerine sınıf metodu ile nesne üretimi / 🇬🇧 Creating an object via the class method instead of __init__
print(Pizza.get_total_pizzas())  # 🇹🇷 Sınıf metodu doğrudan sınıf üzerinden çağrılabilir / 🇬🇧 A class method can be called directly on the class
pizza2 = Pizza.pepperoni()
print(pizza2.ingredients)
print(Pizza.get_total_pizzas())  # 🇹🇷 Sayaç paylaşıldığı için ikinci nesneden sonra 2 döner / 🇬🇧 As the counter is shared, it returns 2 after the second object
