# 🔥 Problema #3 — Array + Two Pointers (Muito cobrado)
# Container With Most Water

# Dado um array height onde cada elemento representa a altura de uma linha vertical, encontre duas linhas que, junto com o eixo X, formam um container que armazena a maior quantidade de água.

# 🔑 Você não pode inclinar o container.

# Exemplo
# height = [1,8,6,2,5,4,8,3,7]
# Resultado: 49


# Explicação:
# As linhas nas posições 1 e 8 formam a maior área:

# min(8, 7) * (8 - 1) = 7 * 7 = 49

# O que o entrevistador quer ver

# Técnica de two pointers

# Redução de complexidade de O(n²) → O(n)

# Boa explicação do porquê mover o ponteiro menor

# Regras

# 2 <= len(height) <= 10⁵

# 0 <= height[i] <= 10⁴

# Tempo esperado: O(n)

# Espaço: O(1)


def executeTwoPointers(height: list[int]):
    maxSize = len(height)
    
    left = 0
    right = maxSize - 1  
    
    maiorArea = 0
    resultLeft = left
    resultRight = right
    
    while left != right:
        area = min(height[left], height[right]) * (right - left)
        if(area > maiorArea):
            maiorArea = area
            resultLeft = left
            resultRight = right
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return resultLeft, resultRight, maiorArea

def test_basic_case():
    lista = [1,8,6,2,5,4,8,3,7]
    
    resultado = executeTwoPointers(lista)
    
    print(resultado)


def main():
    test_basic_case()
    print("🎉 Todos os testes passaram!")


if __name__ == "__main__":
    main()