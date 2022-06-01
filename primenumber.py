def prime(num):
    contador = 0
    for i in range(1, num+1):
        if num % i == 0:
            contador += 1
            print('sus divisores son:',i)
    if contador == 2:
        return True
    else:
        return False

print(prime(141))