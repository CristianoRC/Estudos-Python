def exibirLista(lista):
    for item in lista:
        print(item)
        
numeros = [1, 56, 5, 7, 29]
exibirLista(numeros)

print("Ordenados")
numeros.sort()
exibirLista(numeros)

