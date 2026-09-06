# 🇹🇷 Dekoratörleri birleştirme (Combining Decorators): Bir fonksiyona birden fazla dekoratör
#     uygulanabilir. Sarma işlemi alttan yukarı, çalışma ise dıştan içe doğru gerçekleşir.
# 🇬🇧 Combining decorators: several decorators can be applied to one function. Wrapping happens
#     bottom-up, while execution flows from the outermost wrapper inwards.

def multiply_decorator(func):

    def wrapper(x: int):
        return func(x) * 2  # 🇹🇷 Sardığı fonksiyonun sonucunu 2 ile çarpar / 🇬🇧 Multiplies the wrapped function's result by 2
    return wrapper

def other_decorator(func):
    def wrapper(x: int):
        return func(x) * 4  # 🇹🇷 Sardığı fonksiyonun sonucunu 4 ile çarpar / 🇬🇧 Multiplies the wrapped function's result by 4
    return wrapper


@multiply_decorator  # 🇹🇷 En dıştaki dekoratör: en son sarar, ilk çalışır / 🇬🇧 The outermost decorator: wraps last, runs first
@other_decorator  # 🇹🇷 Fonksiyona en yakın dekoratör: ilk sarar / 🇬🇧 The decorator closest to the function: wraps first
def calculate(x: int):
    return x * 2

print(calculate(5))  # 🇹🇷 Sıra: calculate(5)=10 -> other *4 = 40 -> multiply *2 = 80 / 🇬🇧 Order: calculate(5)=10 -> other *4 = 40 -> multiply *2 = 80
