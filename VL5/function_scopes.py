def my_function(x: int, y: int) -> int:
    x = x + y 
    # global left <- wenn Sie eine globale Variable schreiben möchten
    print(f"Left is {left}, right is {right}")
    # left = x * 2 <- so würden Sie eine neue lokale Variable definieren
    return 2*x

left, right = 5, 10
print(my_function(left, right))
print(left)
print(right)