# DSA – Dia 6
# 🧠 Problema: “Mover todos os zeros para o fim”
# 📜 Descrição:

# Dado um array de inteiros, mova todos os zeros para o final, mantendo a ordem relativa dos demais elementos.

# ⚠️ Importante:
# Deves fazer isso in-place (sem criar uma nova lista, se possível).

# 🧩 Exemplo 1:
# nums = [0, 1, 0, 3, 12]


# ✅ Saída esperada:

# [1, 3, 12, 0, 0]

# 🧩 Exemplo 2:
# nums = [0, 0, 1]


# ✅ Saída esperada:

# [1, 0, 0]

# ⚙️ Requisitos:

# Fazer sem criar um novo array, ou seja, modificando o array original.

# Complexidade O(n).

# Não usar funções prontas como .sort().

# 💡 Dica:

# Usa dois ponteiros:

# Um para percorrer o array,

# Outro para rastrear a posição onde o próximo número diferente de zero deve ir.

def move_zeroes(nums: list[int]) -> None:
    # pointer to track position of next non-zero element
    insert_pos = 0

    # First pass: move non-zero elements forward
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1

    # Second pass: fill remaining positions with zero
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1
    print(nums)
            
def main():
    print(move_zeroes([0, 1, 0, 3, 12]))   # [1, 3, 12, 0, 0]
    print(move_zeroes([0, 0, 1]))          # [1, 0, 0]
    print(move_zeroes([1, 2, 3]))          # [1, 2, 3]   (no zeros)
    print(move_zeroes([0, 0, 0]))          # [0, 0, 0]   (all zeros)

if __name__ == "__main__":
    main()