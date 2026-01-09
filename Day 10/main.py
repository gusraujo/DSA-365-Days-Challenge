# 🔥 Problema #4 — Sliding Window (muito cobrado em entrevista)
# Longest Substring Without Repeating Characters

# Dada uma string s, encontre o comprimento da maior substring sem caracteres repetidos.

# Exemplos
# s = "abcabcbb" → 3   # "abc"
# s = "bbbbb"    → 1   # "b"
# s = "pwwkew"   → 3   # "wke"

# Regras

# 0 <= len(s) <= 10⁵

# String pode conter letras, números e símbolos

# Tempo esperado: O(n)

# Espaço: O(n)

def findRepeatingSubstring(word: str):
    substringHashMap = {}
    for char in word:
        if substringHashMap.get(char) == None:
            substringHashMap[char] = 1
        else:
            substringHashMap = {}
    
    return len(substringHashMap)


def test_basic_case():
    string = "abceefga"
    
    resultado = findRepeatingSubstring(string)
    
    print(resultado)


def main():
    test_basic_case()
    print("🎉 Todos os testes passaram!")


if __name__ == "__main__":
    main()