# 🇹🇷 Dekoratörler (Decorators): Bir fonksiyonu parametre alıp, onu saran yeni bir fonksiyon
#     döndüren yapılardır. Fonksiyonun kodunu değiştirmeden davranışını genişletmeye yarar.
# 🇬🇧 Decorators: constructs that take a function and return a new function wrapping it.
#     They extend a function's behaviour without changing its own code.

def my_decorator(func):  # 🇹🇷 Dekore edilecek fonksiyon parametre olarak gelir / 🇬🇧 The function to be decorated arrives as a parameter
    def wrapper():  # 🇹🇷 İç fonksiyon (wrapper): ek davranışın eklendiği yer / 🇬🇧 Inner function (wrapper): where the extra behaviour is added
        print("wrapper called")
        func()  # 🇹🇷 Orijinal fonksiyon burada çağrılır / 🇬🇧 The original function is called here
        print("function called")

    return wrapper  # 🇹🇷 Fonksiyonun kendisi döndürülür, çağrılmaz (wrapper() değil wrapper) / 🇬🇧 The function itself is returned, not called (wrapper, not wrapper())


@my_decorator  # 🇹🇷 hello_world = my_decorator(hello_world) ile aynı anlama gelir / 🇬🇧 Equivalent to hello_world = my_decorator(hello_world)
def hello_world():
    print("hello world")

hello_world()  # 🇹🇷 Artık aslında wrapper çalışır / 🇬🇧 What actually runs now is the wrapper
