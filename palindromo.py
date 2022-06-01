#Comprobar si una palabra o frase es palindromo

def its_palindromo(phrase):
    phrase = phrase.lower()
    phrase = phrase.replace(' ', '')
    length = len(phrase)
    if length % 2 == 0: #para palabras/frases par
        left = phrase[:length // 2] 
        right = phrase[length // 2:] #2: es indicar que vaya hasta el final de la frase
    else:
        left = phrase[:length // 2] #primera parte de la frase
        right = phrase[length // 2 + 1:] #segunda parte de la frase y que vaya hasta el final
    
    print(left)
    print(right)

    return left == right[::-1] #invertir cadena string con slice


print(its_palindromo('1001'))
print(its_palindromo('anita lava la tina'))
print(its_palindromo('2022 22 20'))
