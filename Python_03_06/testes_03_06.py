import time
# Biblioteca para retornar um número inteiro aleatório
from random import randint as rd

# sorteia um número de -100 a 100
# sorteado = rd(-100, 100)
# print(sorteado)

# criando uma lista de numeros inteiros aleatorios
# lista = [rd(1, 6) for i in range(1,11)]
# lista2 = [x for x in range (1, 11)]
# lista3 = ["Rolo compressor!!!" for f in range (1, 4)]


# print(lista)
# print(lista2)
# print(lista3)

# criando lista par
# par = [i for i in range(10) if i % 2 == 0]
# print(par)

# Povoando uma lista com 'input'
# listaUsuario = [input("Digite um número: ")for p in range(5)]
# print(listaUsuario)

# Utilizando o método split (cada palavra se torna um elemento da lista)
# nome = "Mickey Mouse"
# print(nome)
# print(nome.split())
# print(nome)

# aplicando o "split" com o input
# notas = [n for n in input("Notas: ").split() ]
# print(notas)

# exemplo com float
# notas2 = [float(n) for n in input("Notas: ").split(",")]
# print(notas2)

#lista com tipos diferentes de dados 
listaMista = [17, 70.5, "Sem mundial", True]
# print(listaMista)

#Manipulação / fatiamento de listas
veiculos1 = ["carro", "bicicleta", "moto"]
# print("Veiculos1:", veiculos1)

# Copiando todo o conteúdo de uma lista para outra 
veiculos2 = veiculos1[:]
del veiculos1[2]
# print("Veiculos1:", veiculos1)
# print("Veiculos2:", veiculos2)

# Copiado parte do conteúdo de uma lista
veiculos3 = veiculos2[0:1]
# print("Veiculos3:", veiculos3)

# Copiando parte do conteúdo, incluindo o último elemento
veiculos4 = veiculos2[1:-1] #ele tira o primeiro(posiçao 0) e o ultimo elemento
# print(veiculos4)

veiculos5 = veiculos2[-1:1]
# print(veiculos5)

# outras maneiras de fatiamento(omissão do start ou do end)

my_list = ["A", "B", "C", "D", "E", "F"]
print(my_list)

new_list = my_list[:3]
print(new_list)

new_list_fim = my_list[5:]
print(new_list_fim)

# Apagando contrudo de listas
del my_list[1:3] #apaga a posição 1 e 2
print(my_list)
del my_list[:]#apaga todo o conteudo
print(my_list)

# testando para ver se alguns itens existem em uma lista ou não
# Para isso, usamos palavras chaves in ou not in
naosei = ["A", "B", 18, 15]
print("A" in naosei)
print("C" not in naosei)
print(15 not in naosei)

time.sleep(3)
