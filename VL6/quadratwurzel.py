import math
def quadratwurzel(x: float):
    return -math.sqrt(x), math.sqrt(x)

print(f"Die Wurzel aus 9 ist: ", quadratwurzel(9))
pos, neg = quadratwurzel(16)
print(neg)