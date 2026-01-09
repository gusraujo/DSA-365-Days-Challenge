# 🧩 Problema #7 — HashMap + Prefix Sum (muito forte em entrevista)
# Subarray Sum Equals K

# Dado um array de inteiros nums e um inteiro k, retorne o número total de subarrays contínuos cuja soma seja exatamente k.

# Exemplos
# nums = [1,1,1]
# k = 2
# → 2

# nums = [1,2,3]
# k = 3
# → 2   # [1,2], [3]

# Regras

# 1 <= len(nums) <= 2 * 10⁴

# -1000 <= nums[i] <= 1000

# Tempo esperado: O(n)

# Espaço: O(n)

# 🧠 O que o entrevistador quer ver

# Uso de prefix sum

# HashMap para contagem

# Entendimento de subarrays contínuos

# Dicas (sem entregar 😉)

# Pense na soma acumulada

# Se prefix_sum - k já apareceu antes, há subarrays válidos

# Inicialize o mapa corretamente


def subarraySum(nums: list[int], k: int) -> int:
    prefix_sum_count = {0: 1}
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        if (current_sum - k) in prefix_sum_count:
            count += prefix_sum_count[current_sum - k]
        prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

    return count