def fibo(n):  #Iterative Form
    a = 0
    b = 1

    for i in range(n):
        c = a + b
        a = b
        b = c

    return b

for x in range(10):
    print(fibo(x))