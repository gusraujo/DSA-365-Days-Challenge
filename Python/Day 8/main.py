# Problema #1 – Nível Fácil / Entrevista Clássica

# 👉 Two Sum

# Dado um array de inteiros nums e um inteiro target, retorne os índices dos dois números que somam target.

# Regras:

# Cada input tem exatamente uma solução

# Você não pode usar o mesmo elemento duas vezes

# Pode retornar os índices em qualquer ordem

# Exemplo:

# nums = [2, 7, 11, 15]
# target = 9
# Resultado: [0, 1]


def two_sum(nums: list[int], target: int):
    print(f"\n🔹 Iniciando two_sum")
    print(f"nums = {nums}")
    print(f"target = {target}\n")

    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        print(f"➡️ Índice atual: {i}")
        print(f"   Número atual: {num}")
        print(f"   Complemento necessário: {complement}")
        print(f"   HashMap (seen) antes: {seen}")

        if complement in seen:
            print(f"✅ Encontrado! {num} + {complement} = {target}")
            print(f"   Índices retornados: {seen[complement]} e {i}\n")
            return [seen[complement], i]

        seen[num] = i
        print(f"   HashMap (seen) depois: {seen}\n")

    print("❌ Nenhuma combinação encontrada\n")
    return []


def test_basic_case():
    print("🧪 Teste: caso básico")
    nums = [2, 7, 11, 15]
    target = 9
    assert set(two_sum(nums, target)) == {0, 1}
    print("✔️ Teste passou\n")


def test_with_negative_numbers():
    print("🧪 Teste: números negativos")
    nums = [-3, 4, 3, 90]
    target = 0
    assert set(two_sum(nums, target)) == {0, 2}
    print("✔️ Teste passou\n")


def test_small_array():
    print("🧪 Teste: array pequeno")
    nums = [3, 2]
    target = 5
    assert set(two_sum(nums, target)) == {0, 1}
    print("✔️ Teste passou\n")


def main():
    test_basic_case()
    test_with_negative_numbers()
    test_small_array()
    print("🎉 Todos os testes passaram!")


if __name__ == "__main__":
    main()

