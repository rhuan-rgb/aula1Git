import time

# Encontrar o maior valor na lista - Exemplo 1

lista = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maior_numero = lista[0] #recebeu o numero 17

for i in range(1, len(lista)):
    if lista[i] > maior_numero:
        maior_numero = lista[i]       
print("O maior número é:", maior_numero)
    
# exemplo 2
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maior = my_list[0]
for i in my_list:
    if i > maior:
        maior = i
print("Maior valor 2:", maior)

#exemplo3:
ultima_lista = my_list[:]
mel = ultima_lista[0]
for i in ultima_lista[1:]:
    if i > mel:
        mel = i 
print("Maior valor 3:", mel)

#encontrar a localização de um determinado elemento dentro de uma lista
frutas = ["abacaxi", "maçã", "pêra", "mamão", "uva", "melancia"]
elemento = "melancia"
achado = False

for i in range(len(frutas)):
    achado = frutas[i] == elemento
    if achado:
        break

if achado:
    print("elemento encontrado no índice:", i)
else:
    print("NÃO ENCONTRADO!!!")

#conferidor de aposta em loteria
sorteados = [5, 11, 9, 42, 3, 49]
apostados = [3, 7, 11, 42, 34, 49]
acertos = 0

for numero in sorteados:
    if numero in apostados:
        acertos += 1

print(acertos)

#remoção de numeros repetidos em uma lista
lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print("Lista original:", lista)

#Lista de apoio
vistos = []

#iterar pela lista original de trás pra frente
for i in range(len(lista) - 1, -1, -1):
    #se o número já está na lista "vistos", remove-lo da lista original
    if lista[i] in vistos:
        del lista[i]
    else:
        #caso contrário, adicionar à lista "vistos"
        vistos.append(lista[i])
#Exibir a lista original modificada
print("lista modificada:", lista)

#listas avançadas
#2d - listas aninhadas bidimensionais
tabela = [[":(", ":)", ":|", ";-;"], [";-;", ":|", ":)", ":("], [":|", ":)", ";-;", ":("]] 
print(tabela[0][3])

print(tabela)

#3d - Matriz Tridimensional
cubo = [[[":("], ["y"], ["z"], [":)"], ["y"], ["z"], [":|"], ["y"], ["z"]],
        [["amor"], ["ódio"], ["caridade"], ["paz"], ["esperança"], ["férias"], ["tina"], ["prior"], ["pp"]], 
        [["restinga"], ["patrocínio"], ["rifaina"], ["amazonense"], ["fluminense"], ["santos"], ["pizza"], ["lasanha"], ["pastel"]]]

print(cubo)
print(cubo[1])
print(cubo[1][0])
print(cubo[1][0][2])

time.sleep(1)