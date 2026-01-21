# Este problema foi levantado pela Apple.

# Suponha que você tenha uma tabela de multiplicação de tamanho N por N. Ou seja, uma matriz 2D onde o valor na i -ésima linha e j -ésima coluna é (i + 1) * (j + 1) (se indexado a partir de 0) ou i * j (se indexado a partir de 1).

# Dados dois números inteiros N e X, escreva uma função que retorne o número de vezes que X aparece como um valor em uma tabela de multiplicação N por N.

# Por exemplo, dados N = 6 e X = 12, você deve retornar 4, já que a tabuada é assim:

# | 1 | 2 | 3 | 4 | 5 | 6 |

# | 2 | 4 | 6 | 8 | 10 | 12 |

# | 3 | 6 | 9 | 12 | 15 | 18 |

# | 4 | 8 | 12 | 16 | 20 | 24 |

# | 5 | 10 | 15 | 20 | 25 | 30 |

# | 6 | 12 | 18 | 24 | 30 | 36 |

# E há quatro números 12 na tabela.


    


# Solução N² acima. Abaixo uma solução N mais eficiente.

# def executeCountMultiplicationTable(n: int, x: int) -> int:
#     matrix = createMatrix(n)
#     count = 0
#     for i in range(n):
#         for j in range(n):
#             if matrix[i][j] == x:
#                 count += 1
#     return count
    

# def createMatrix(n: int) -> list[list[int]]:
#     matrix = []
#     for i in range(1, n + 1):
#         row = []
#         for j in range(1, n + 1):
#             row.append(i * j)
#         matrix.append(row)
#     return matrix

# Solução N mais eficiente
def executeCountMultiplicationTable(n: int, x: int) -> int:
    count = 0
    for i in range(1, n + 1):
        if x % i == 0 and x // i <= n:
            count += 1
    return count


def test_basic_case():
    n = 6
    x = 12

    resultado = executeCountMultiplicationTable(n, x)
    
    print(resultado)
    
def main():
    test_basic_case()
    print("🎉 Todos os testes passaram!")
    
if __name__ == "__main__":
    main()