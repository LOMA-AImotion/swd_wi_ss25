def addition(x: int, y: int) -> int:
    return x + y

from functools import partial
addiere_5 = partial(addition, 5)
konst_7 = partial(addiere_5, 2)

print(addition(2,5))
print(addiere_5(10))
print(konst_7())
