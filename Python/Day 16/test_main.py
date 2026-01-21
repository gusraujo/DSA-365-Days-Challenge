# 🧠 Problema — Event Aggregator (Sliding Window + Hash Map)
# 📌 Contexto (bem real de microserviços)

# Em um sistema de microserviços, vários serviços emitem eventos com:

# service_id

# timestamp (em segundos)

# type (string)

# Você precisa monitorar o sistema e responder consultas do tipo:

# Quantos eventos de cada serviço aconteceram nos últimos T segundos?

# 📥 Entrada

# Uma lista de eventos ordenados por timestamp

# Um inteiro T (janela de tempo, em segundos)

# events = [
#   ("auth", 1),
#   ("order", 2),
#   ("auth", 5),
#   ("payment", 7),
#   ("auth", 10),
#   ("order", 12)
# ]

# T = 5

# 📤 Saída esperada

# Retorne um mapa {service_id: count} contendo apenas eventos com timestamp ≥ (current_time - T)
# Considere current_time como o timestamp do último evento.

# {
#   "auth": 2,
#   "order": 1,
#   "payment": 1
# }

# 🎯 O que esse problema avalia

# Sliding Window

# Hash Map

# Pensamento de stream / observabilidade

# Código limpo e eficiente (O(n))

# 🚫 Regras

# Não pode recalcular tudo a cada evento

# Use dois ponteiros ou fila

# Espaço O(n) no pior caso

# 🧩 Dicas (se travar)

# Use um ponteiro left

# Quando timestamp < current_time - T, remova

# Atualize o contador por serviço

# 🔥 Desafio extra (opcional)

# Suportar consulta dinâmica (janela muda)

# Resolver como stream infinito

# 💡 Pergunta estilo entrevista

# Como isso mudaria se os eventos chegassem fora de ordem?
import pytest
from collections import Counter


def aggregate_events(events: list[tuple[str, int]], T: int) -> dict[str, int]:
    if not events:
        return {}

    result = {}
    current_time = events[-1][1]
    window_start = current_time - T

    for service_id, timestamp in events:
        if timestamp >= window_start:
            result[service_id] = result.get(service_id, 0) + 1

    return result


def test_basic_case():
    events = [
        ("auth", 1),
        ("order", 2),
        ("auth", 5),
        ("payment", 7),
        ("auth", 10),
        ("order", 12)
    ]
    T = 5

    result = aggregate_events(events, T)

    assert result == {
        "auth": 1,
        "order": 1,
        "payment": 1
    }
