import random

print("==========================================")
print(" SIMULADOR DE COLETA INDUSTRIAL")
print("==========================================")

codigo_equipamento = "M-01"
dispositivo_coleta = "CLP-SIM-01"
quantidade_ciclos = 20

limite_temperatura = 90
limite_pressao = 12
limite_corrente = 20

ciclos_normais = 0
ciclos_atencao = 0
ciclos_alarme = 0
ciclos_emergencia = 0
ciclos_realizados = 0
leituras_ignoradas = 0

# historico_ciclos = []
# historico_temperatura = []
# historico_pressao = []
# historico_corrente = []
# historico_estados = []

historico = []

print(f"Equipamento: {codigo_equipamento}")
print(f"Dispositivo: {dispositivo_coleta}")
print(f"Ciclos planejados: {quantidade_ciclos}")

for ciclo in range(quantidade_ciclos):
    numero_ciclo = ciclo + 1

    print()
    print(f"========== CICLO {numero_ciclo} ==========")

    # Simulação de uma falha de comunicação
    if numero_ciclo == 5:
        print("Falha de comunicação com o sensor.")
        leituras_ignoradas += 1
        continue

    # Simulação das leituras
    temperatura = random.randint(60, 95)
    pressao = random.uniform(5.0, 10.0)
    corrente = random.uniform(10.0, 20.0)

    ciclos_realizados += 1

    # Classificação da temperatura
    if temperatura < 70:
        status_temperatura = "NORMAL"
    elif temperatura <= limite_temperatura:
        status_temperatura = "ATENÇÃO"
    else:
        status_temperatura = "ALARME"

    # Classificação da pressão
    if pressao < 7:
        status_pressao = "NORMAL"
    elif pressao <= limite_pressao:
        status_pressao = "ATENÇÃO"
    else:
        status_pressao = "ALARME"

    # Classificação da corrente
    if corrente < 13:
        status_corrente = "NORMAL"
    elif corrente <= limite_corrente:
        status_corrente = "ATENÇÃO"
    else:
        status_corrente = "ALARME"

    # Identificação de situação crítica
    situacao_critica = (
        temperatura > 90
        or pressao > 10
        or corrente > 18
    )

    # Identificação de alarme
    existe_alarme = (
        status_temperatura == "ALARME"
        or status_pressao == "ALARME"
        or status_corrente == "ALARME"
    )

    # Identificação de atenção
    existe_atencao = (
        status_temperatura == "ATENÇÃO"
        or status_pressao == "ATENÇÃO"
        or status_corrente == "ATENÇÃO"
    )

    # Classificação do estado geral
    if situacao_critica:
        estado_geral = "EMERGÊNCIA"
    elif existe_alarme:
        estado_geral = "ALARME"
    elif existe_atencao:
        estado_geral = "ATENÇÃO"
    else:
        estado_geral = "NORMAL"

    # Contagem dos estados
    if estado_geral == "NORMAL":
        ciclos_normais += 1
    elif estado_geral == "ATENÇÃO":
        ciclos_atencao += 1
    elif estado_geral == "ALARME":
        ciclos_alarme += 1
    elif estado_geral == "EMERGÊNCIA":
        ciclos_emergencia += 1

    leitura = {
        "ciclo": numero_ciclo,
        "equipamento": codigo_equipamento,
        "dispositivo": dispositivo_coleta,
        "temperatura": temperatura,
        "pressao": pressao,
        "corrente": corrente,
        "status_temperatura": status_temperatura,
        "status_pressao": status_pressao,
        "status_corrente": status_corrente,
        "estado_geral": estado_geral,
        "situacao_critica": situacao_critica
    }

    historico.append(leitura)

    # Exibição da leitura
    print(f"Temperatura: {temperatura:.2f} °C - {status_temperatura}")
    print(f"Pressão: {pressao:.2f} bar - {status_pressao}")
    print(f"Corrente: {corrente:.2f} A - {status_corrente}")
    print(f"Estado geral: {estado_geral}")

    # Interrupção em caso de emergência
    if estado_geral == "EMERGÊNCIA":
        print("PARADA DE EMERGÊNCIA ATIVADA.")
        break



menor_temperatura = min(leitura["temperatura"] for leitura in historico)
maior_temperatura = max(leitura["temperatura"] for leitura in historico)
media_temperatura = sum(leitura["temperatura"] for leitura in historico) / numero_ciclo

menor_pressao = min(leitura["pressao"] for leitura in historico)
maior_pressao = max(leitura["pressao"] for leitura in historico)
media_pressao = sum(leitura["pressao"] for leitura in historico) / numero_ciclo

menor_corrente = min(leitura["corrente"] for leitura in historico)
maior_corrente = max(leitura["corrente"] for leitura in historico)
media_corrente = sum(leitura["corrente"] for leitura in historico) / numero_ciclo

print()
print("==========================================")
print(" RESUMO DA COLETA")
print("==========================================")
print(f"Equipamento: {codigo_equipamento}")
print(f"Dispositivo: {dispositivo_coleta}")
print(f"Ciclos planejados: {quantidade_ciclos}")
print(f"Ciclos realizados: {ciclos_realizados}")
print(f"Leituras ignoradas: {leituras_ignoradas}")
print(f"Ciclos normais: {ciclos_normais}")
print(f"Ciclos em atenção: {ciclos_atencao}")
print(f"Ciclos em alarme: {ciclos_alarme}")
print(f"Ciclos em emergência: {ciclos_emergencia}")
print("==========================================")

print()
print("==========================================")
print(" ESTATÍSTICAS DO HISTÓRICO")
print("==========================================")
print(
 f"Leituras armazenadas: "
 f"{len(historico)}"
)

print()
print("TEMPERATURA")
print(f"Mínima: {menor_temperatura:.2f} °C")
print(f"Máxima: {maior_temperatura:.2f} °C")
print(f"Média: {media_temperatura:.2f} °C")

print()
print("PRESSÃO")
print(f"Mínima: {menor_pressao:.2f} bar")
print(f"Máxima: {maior_pressao:.2f} bar")
print(f"Média: {media_pressao:.2f} bar")

print()
print("CORRENTE")
print(f"Mínima: {menor_corrente:.2f} A")
print(f"Máxima: {maior_corrente:.2f} A")
print(f"Média: {media_corrente:.2f} A")