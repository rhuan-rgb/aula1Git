import time

beatles = []

beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('Geroge Harrison')

print(beatles)
print()

for i in range(2):
    if i == 1:
        print()
        digitado = str(input('Escreva "Stu Sutcliffe" para adicioná-lo à banda: '))
        beatles.append(digitado)
    else:
        digitado = str(input('Escreva "Pete Best" para adicioná-lo à banda:'))
        beatles.append(digitado)

print(beatles)
print()


del(beatles[-1])
del(beatles[-1])


print(beatles)
print()

beatles.insert(0, "Ringo Starr")

print(beatles)
print()

time.sleep(3)