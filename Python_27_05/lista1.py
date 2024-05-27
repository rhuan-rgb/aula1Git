import time

numeros = [111, 7, 2, 1]

print(len(numeros))

numeros.append(52)
print(len(numeros))
print(numeros)

numeros.insert(0, 222)
print(len(numeros))
print(numeros)

numeros.insert(1, 18)

numeros.insert(-2, 20)
print(numeros)
print(len(numeros))


print(numeros)


time.sleep(3)