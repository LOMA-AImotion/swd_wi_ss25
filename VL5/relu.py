# ReLU = Rectified Linear Unit -> relu(x) = max(x, 0)
# Soll von -10 bis 10 ausgegeben werden
def relu(x : int) -> int:
    """ berechnet die ReLU = Rectified Linear Unit -> relu(x) = max(x, 0)

    Args:
        x (int): der Input

    Returns:
        int: ReLU(x)
    """
    if x < 0:
        ergebnis = 0 # return 0
    else:
        ergebnis = x # return x
    return ergebnis

for x in range(-10, 11):
    print(f"x = {x}, relu(x) = {relu(x)}")