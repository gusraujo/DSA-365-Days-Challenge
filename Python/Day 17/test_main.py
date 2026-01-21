# 🧠 Problema — Rate Limiter por Serviço (Sliding Window + Hash Map + Queue)
# 📌 Contexto (microserviços real)

# Em um sistema de microserviços, cada serviço pode fazer chamadas a um serviço compartilhado (ex: auth, payments).

# Para evitar sobrecarga, você precisa implementar um rate limiter:

# Cada service_id pode fazer no máximo N requisições dentro de uma janela de T segundos.

# 📥 Entrada

# Uma lista de requisições ordenadas por tempo

# Cada requisição é uma tupla:

# (service_id, timestamp)


# Dois inteiros:

# N → limite de requisições

# T → janela de tempo (segundos)

# 📤 Saída

# Retorne uma lista de booleans, onde:

# True → requisição permitida

# False → requisição bloqueada

# 🧪 Exemplo
# Entrada
# requests = [
#     ("auth", 1),
#     ("auth", 2),
#     ("auth", 3),
#     ("auth", 4),
#     ("payment", 5),
#     ("auth", 6),
#     ("auth", 7),
# ]

# N = 3
# T = 5

# Saída
# [True, True, True, False, True, False, False]

# 🔍 Explicação

# Para auth:

# Janela [1–5]: timestamps 1,2,3 → ok

# Timestamp 4 → 4 requisições → ❌

# Para payment:

# Só 1 requisição → ok

# Timestamp 6 → janela [2–6], ainda 4 → ❌

# Timestamp 7 → janela [3–7], ainda 4 → ❌

# 🎯 O que esse problema avalia

# Sliding window real

# HashMap de filas (dict[str, deque])

# Pensamento de sistema distribuído

# Código eficiente (O(n))

# 🚫 Regras

# Não pode recalcular tudo

# Cada serviço tem sua própria janela

# Eventos vêm ordenados

# 🧩 Dicas (se travar)

# Um dict de deque

# Antes de aceitar, remova timestamps < current_time - T

# Se tamanho da fila ≥ N → bloqueia

# 🔥 Desafio extra (opcional)

# Tornar thread-safe

# Resolver com token bucket

# Implementar em Go

# Adaptar para redis (distributed rate limit)

def rate_limiter(events: list[tuple[str, int]], N, T) -> list[bool]:
    if not events:
        return {}

    result = []
    current_time = events[-1][1]
    window_start = current_time - T
    rateCounter = 0
    for service_id, timestamp in events:
        if timestamp >= window_start and rateCounter < N:
            result.append(True)
            rateCounter += 1
        else:
            result.append(False)
    return result

def test_basic_case():
    requests = [
        ("auth", 1),
        ("auth", 2),
        ("auth", 3),
        ("auth", 4),
        ("payment", 5),
        ("auth", 6),
        ("auth", 7),
    ]

    N = 3
    T = 5

    result = rate_limiter(requests, N, T)

    assert result == [True, True, True, False, True, False, False]