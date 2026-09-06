# 🇹🇷 Aşırı yükleme (Overloading) ve @overload: Python'da gerçek anlamda aynı isimli birden fazla
#     metot yaşayamaz; son tanım öncekileri ezer. typing.overload sadece tip ipucu üretir,
#     çalışma anında iş yapan tek gövde en sondaki gerçek tanımdır.
# 🇬🇧 Overloading and @overload: Python cannot really keep several methods with the same name;
#     the last definition overwrites the earlier ones. typing.overload only declares type hints,
#     the single body that actually runs is the final real definition.

from typing import overload, Union  # 🇹🇷 Union[int,str] = "int veya str" anlamına gelir / 🇬🇧 Union[int,str] means "int or str"


class Calculator:

    @overload  # 🇹🇷 Sadece imza bildirimi: iki argümanlı kullanım / 🇬🇧 Signature declaration only: the two-argument usage
    def add(self, a: int, b: int) -> int:
        pass  # 🇹🇷 Gövde boş kalır, bu tanım hiç çalışmaz / 🇬🇧 The body stays empty, this definition never runs

    @overload
    def add(self,a : int, b : int, c : int) -> int:  # 🇹🇷 Üç argümanlı kullanımın imzası / 🇬🇧 Signature of the three-argument usage
        pass

    def add(self,a: int, b: int, c: int | None = None) -> int:  # 🇹🇷 Gerçek uygulama: tüm imzaları karşılayacak tek gövde / 🇬🇧 The real implementation: one body covering all declared signatures
        if c is None:  # 🇹🇷 Varsayılan None ile argüman sayısı ayırt edilir / 🇬🇧 The default None distinguishes the number of arguments
            return a + b
        return a + b + c

    @overload
    def process(self, x : int) -> int:  # 🇹🇷 int girerse int döner bilgisi / 🇬🇧 Declares that an int input returns an int
        pass

    @overload
    def process(self, x : str) -> str:  # 🇹🇷 str girerse str döner bilgisi / 🇬🇧 Declares that a str input returns a str
        pass

    def process(self, x : Union[int,str]) -> Union[int,str]:
        if isinstance(x, int):  # 🇹🇷 Tip kontrolü çalışma anında elle yapılır / 🇬🇧 The type check is done manually at runtime
            return x * 2
        elif isinstance(x, str):
            return x.upper()
        else:
            raise ValueError("Value must be an integer or a string")



calculator = Calculator()
print(calculator.add(2,3,4))  # 🇹🇷 Üç argümanlı çağrı / 🇬🇧 Three-argument call

calculator2 = Calculator()
print(calculator2.add(2,3))  # 🇹🇷 Aynı metot, c varsayılan None olduğu için iki argümanla da çalışır / 🇬🇧 Same method; it also works with two arguments because c defaults to None

result = calculator.process(2)
print(result)

result2 = calculator.process("efe")
print(result2)
