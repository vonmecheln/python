import random

historico = []

for ciclo in range(5):

    numero_ciclo = ciclo + 1
    temperatura = random.randint(60, 95)
    pressao = random.uniform(5.0, 10.0)
    corrente = random.uniform(10.0, 20.0)
    leitura = {
        "ciclo": numero_ciclo,
        "temperatura": temperatura,
        "pressao": pressao,
        "corrente": corrente,
        "estado_geral": "EM ANÁLISE"
    }

    historico.append(leitura)

for leitura in historico:
    print(leitura)