# Descrição:

# Dado um array (lista) de números inteiros, você deve retornar um dicionário que mostre quantas vezes cada número aparece na lista.

# Exemplo:
# Entrada: [1, 2, 2, 3, 1, 4, 2]
# Saída: {1: 2, 2: 3, 3: 1, 4: 1}

# Requisitos:

# A função deve se chamar count_frequency(nums: list[int]) -> dict[int, int]

# Não use collections.Counter (faça na mão!)

# Retorne o dicionário com as frequências.



        
def count_frequency(array):
    result = {}
    for i in array:
        result[i] = getCountDict(array, i)
    return result

def getCountDict(array, n):
    count = 0
    for element in array:
        if element == n:
            count= count + 1
    
    return count

def main():
    array = [1, 2, 2, 3, 1, 4, 2]
    print(count_frequency(array))

if __name__ == "__main__":
    main()
    
    
    
# Better solution 

# def count_frequency(array):
#     result = {}
#     for element in array:
#         result[element] = result.get(element, 0) + 1
#     return result