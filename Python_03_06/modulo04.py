import time

#função que possui muitas atribuições
#parece mais um método  
# def somar():
#     n1 = int(input("Digite o primeiro número da adição: "))
#     n2 = int(input("Digite o segundo número da adição: "))
#     print(n1 + n2)

# somar()

#função exclusiva de soma
# def somar2(n1, n2):
#     soma = n1 + n2
#     return soma

# print("Soma2:", somar2(22,20))

#terceiro exemplo função
# def somar3(n1, n2):
#     return n1 + n2
# numero1 = float(input("Digite um número: "))
# numero2 = float(input("Digite outro número: "))

#chamada de função
# print(somar3(numero1, numero2))

#chamada da função por argumentos
# print(somar3(n2 = 12, n1 = 5))

# função com parâmetros default (padrão)
# def somar4(n1 = 0,n2 = 0):
#     return n1 + n2

# print(somar4(50 + 25))
# print(somar4())

# função com apenas alguns valores default
def somar5(n1, n2=0):
    return n1 + n2

print(somar5(50 + 25)) #75
# print(somar5()) #erro
print(somar5(10)) #10
print(somar5(n1 = 51, n2 = 12))

def somar6(n1, n2):
    if n1 == 1:
        return 1

print(somar6 (1,3)) # True
print(somar6 (13,3)) # None

print(somar6(1, 2) + 10) #mostra 11
print(somar6(2, 2) + 10) #mostra type não suportado



time.sleep(1)