def meine_funktion(x: int) -> int:
    def meine_operation(y: int) -> int:
        return 2*y
    return meine_operation(x)

x = 10
print(f"x, meine_funktion(x)", x, meine_funktion(x))