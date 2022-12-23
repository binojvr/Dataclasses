from dataclasses import dataclass, field


@dataclass(order=True)
class Investor:
    name: str = field(compare=False)
    age: int = field(repr=False, compare=False)
    cash: float = field(repr=False)


i1 = Investor("Binoj", 45, 70000.45)
i2 = Investor("Cinoj", 46, 20000.45)
i3 = Investor("Dinoj", 41, 70000.45)
i4 = Investor("Binoj", 44, 70000.45)

print(i4 == i3)
print(i4 > i1)



