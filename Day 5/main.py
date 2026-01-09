# 🧩 DSA – Dia 5
# 🧠 Problema: “Verificar se duas strings são anagramas”
# 📜 Descrição:

# Dadas duas strings s1 e s2, determine se uma é anagrama da outra.
# Duas strings são anagramas se contêm exatamente as mesmas letras, com a mesma quantidade, apenas em ordens diferentes.

# 🧩 Exemplo 1:
# s1 = "listen"
# s2 = "silent"


# ✅ Saída esperada: True
# Explicação: Ambas têm as mesmas letras — apenas em ordem diferente.

# 🧩 Exemplo 2:
# s1 = "hello"
# s2 = "bello"


# ❌ Saída esperada: False

# ⚙️ Requisitos:

# Ignorar maiúsculas/minúsculas ("Listen" == "Silent").

# Ignorar espaços (ex: "a gentleman" == "elegant man" → True).

# Não usar collections.Counter (faz na lógica pura primeiro 😉).

# 💡 Dica:

# Você pode resolver de duas formas:

# Ordenando ambas as strings e comparando.

# Contando caracteres manualmente (como um pequeno hash map/dicionário).

def isAnagram(s1: str, s2: str) -> bool:
    if(len(s1) != len(s2)):
        return False
    
    sortedS1 = sorted(list(s1))
    sortedS2 = sorted(list(s2))
    
    return sortedS1 == sortedS2

    
def main():
    print(isAnagram("racecar", "racecar"))   # True
    print(isAnagram("madam", "racecar"))     # True
    print(isAnagram("python", "racecar"))    # False

if __name__ == "__main__":
    main()
    
    
# Better solution

# def isAnagram(s1: str, s2: str) -> bool:
#     # Normalize both strings
#     s1 = s1.replace(" ", "").lower()
#     s2 = s2.replace(" ", "").lower()

#     if len(s1) != len(s2):
#         return False

#     # Compare sorted characters
#     return sorted(s1) == sorted(s2)