# 🧠 Day 16 — DSA Challenge
# Problem: Daily Temperatures

# Você recebe um array temperatures onde temperatures[i] representa a temperatura do dia i.

# Para cada dia, retorne quantos dias você teria que esperar até um dia mais quente.
# Se não existir um dia futuro mais quente, retorne 0 para aquele dia.

# Exemplos
# temperatures = [73,74,75,71,69,72,76,73]
# → [1,1,4,2,1,1,0,0]
  
# temperatures = [30,40,50,60]
# → [1,1,1,0]

# temperatures = [30,60,90]
# → [1,1,0]

# Regras

# 1 <= len(temperatures) <= 10⁵

# 30 <= temperatures[i] <= 100

# Tempo esperado: O(n)

# Espaço: O(n)

# 🧠 O que o entrevistador quer ver

# Uso de Monotonic Stack

# Processamento em uma passagem

# Boa explicação do porquê funciona

# Dicas (sem entregar 😉)

# Use uma pilha para guardar índices

# A pilha deve ser decrescente

# Quando encontrar temperatura maior, resolva dias anteriores

def daily_temperatures(temperatures: list[int]) -> list[int]:
    stack = [] # Pilha para guardar índices dos dias
    result = [0] * len(temperatures) # Inicializa o resultado com zeros

    for day, temp in enumerate(temperatures): # Percorre cada dia e sua temperatura
         # Enquanto a pilha não estiver vazia e a temperatura atual for maior que a do dia no topo da pilha
        while stack and temperatures[stack[-1]] < temp:
            prev_day = stack.pop()
            result[prev_day] = day - prev_day
            # Adiciona o índice do dia atual na pilha
        stack.append(day)

    return result