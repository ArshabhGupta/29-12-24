def Swap1(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("After swapping: a =",a , "b =", b )

def Swap2(a, b):
    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a = a + (~b) + 1
    print("After swapping: a =",a , "b =", b )

Swap1(1, 2)
Swap2(1, 2)