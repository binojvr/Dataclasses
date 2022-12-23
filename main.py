from dataclasses import dataclass, field


@dataclass(order=True)
class Investor:
    sort_index: float = field(init=False, repr=False, hash=False)
    name: str
    age: int = field(repr=False)
    cash: float = field(repr=False)

    def __post_init__(self):
        self.sort_index = self.cash


i1 = Investor("Binoj", 45, 20000.45)
i2 = Investor("Cinoj", 46, 10000.45)
i3 = Investor("Dinoj", 41, 50000.45)
i4 = Investor("Oinoj", 44, 70000.45)
i5 = Investor("Binoj", 45, 20000.45)
print(i1)
print(i4 == i3)
print(i4 > i1)

i_list = [i1, i2, i3, i4]
i_list.sort()
print(i_list)

