import time

def hi_everbody(lista):
    for name in lista:
        print("Oi", name)
hi_everbody(["Tina", "Gabi", "Jão"])

def criar_list(n):
    lista = []
    for i in range(n):
        lista.append(i)
    return lista
 
print(criar_list(10))

global a 
a = 1
 
 
def fun():
    a = 2
    print(a)
 
 
fun()
print(a)

time.sleep(3)