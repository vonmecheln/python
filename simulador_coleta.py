import csv
import random
from datetime import datetime

NOME_ARQUIVO = "historico_leituras.csv"

CODIGO_EQUIPAMENTO = "M-01"
DISPOSITIVO_COLETA = "CLP-SIM-01"
TOTAL_CICLOS = 20

LIMITE_TEMPERATURA = 80
LIMITE_PRESSAO = 8
LIMITE_CORRENTE = 15

CAMPOS = [
    "ciclo",
    "equipamento",
    "dispositivo",
    "temperatura",
    "pressao",
    "corrente",
    "status_temperatura",
    "status_pressao",
    "status_corrente",
    "estado_geral",
    "situacao_critica",
    "data",
    "horario",
    "operador",
    "turno",
    "observacao"
]


def classificar_temperatura(temperatura):
    if temperatura < 70:
        return "NORMAL"
    elif temperatura <= LIMITE_TEMPERATURA:
        return "ATENÇÃO"
    else:
        return "ALARME"


def classificar_pressao(pressao):
    if pressao < 7:
        return "NORMAL"
    elif pressao <= LIMITE_PRESSAO:
        return "ATENÇÃO"
    else:
        return "ALARME"


def classificar_corrente(corrente):
    if corrente < 13:
        return "NORMAL"
    elif corrente <= LIMITE_CORRENTE:
        return "ATENÇÃO"
    else:
        return "ALARME"


def determinar_estado_geral(
    situacao_critica,
    status_temperatura,
    status_pressao,
    status_corrente
):
    status_sensor = [
        status_temperatura,
        status_pressao,
        status_corrente
    ]

    if situacao_critica:
        return "EMERGÊNCIA"
    elif "ALARME" in status_sensor:
        return "ALARME"
    elif "ATENÇÃO" in status_sensor:
        return "ATENÇÃO"
    else:
        return "NORMAL"


def criar_leitura(numero_ciclo):
    temperatura = round(random.uniform(60, 95), 2)
    pressao = round(random.uniform(5.0, 10.0), 2)
    corrente = round(random.uniform(10.0, 20.0), 2)

    status_temperatura = classificar_temperatura(temperatura)
    status_pressao = classificar_pressao(pressao)
    status_corrente = classificar_corrente(corrente)

    situacao_critica = (
        temperatura > 90
        or pressao > 10
        or corrente > 18
    )

    estado_geral = determinar_estado_geral(
        situacao_critica,
        status_temperatura,
        status_pressao,
        status_corrente
    )

    agora = datetime.now()

    leitura = {
        "ciclo": numero_ciclo,
        "equipamento": CODIGO_EQUIPAMENTO,
        "dispositivo": DISPOSITIVO_COLETA,
        "temperatura": temperatura,
        "pressao": pressao,
        "corrente": corrente,
        "status_temperatura": status_temperatura,
        "status_pressao": status_pressao,
        "status_corrente": status_corrente,
        "estado_geral": estado_geral,
        "situacao_critica": situacao_critica,
        "data": agora.strftime("%Y-%m-%d"),
        "horario": agora.strftime("%H:%M:%S"),
        "operador": "Operador 01",
        "turno": "A",
        "observacao": "Coleta automática"
    }

    return leitura


def salvar_csv(historico, nome_arquivo):
    with open(
        nome_arquivo,
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:
        escritor = csv.DictWriter(
            arquivo,
            fieldnames=CAMPOS,
            delimiter=";"
        )
        escritor.writeheader()
        escritor.writerows(historico)


def converter_registro(registro):
    registro["ciclo"] = int(registro["ciclo"])
    registro["temperatura"] = float(registro["temperatura"])
    registro["pressao"] = float(registro["pressao"])
    registro["corrente"] = float(registro["corrente"])
    registro["situacao_critica"] = (
        registro["situacao_critica"].lower() == "true"
    )
    return registro


def ler_csv(nome_arquivo):
    historico = []

    with open(
        nome_arquivo,
        "r",
        newline="",
        encoding="utf-8"
    ) as arquivo:
        leitor = csv.DictReader(
            arquivo,
            delimiter=";"
        )

        for registro in leitor:
            try:
                historico.append(converter_registro(registro))
            except (TypeError, ValueError, KeyError) as erro:
                print(f"Registro inválido ignorado: {erro}")

    return historico


def exibir_leitura(leitura):
    print()
    print(f"Ciclo: {leitura['ciclo']}")
    print(f"Equipamento: {leitura['equipamento']}")
    print(f"Dispositivo: {leitura['dispositivo']}")
    print(f"Temperatura: {leitura['temperatura']:.2f} °C")
    print(f"Pressão: {leitura['pressao']:.2f} bar")
    print(f"Corrente: {leitura['corrente']:.2f} A")
    print(f"Estado geral: {leitura['estado_geral']}")
    print(f"Situação crítica: {leitura['situacao_critica']}")
    print(f"Data: {leitura['data']}")
    print(f"Horário: {leitura['horario']}")


def calcular_media(historico, campo):
    if not historico:
        return 0

    return sum(
        leitura[campo]
        for leitura in historico
    ) / len(historico)


def obter_menor_valor(historico, campo):
    if not historico:
        return None

    return min(
        leitura[campo]
        for leitura in historico
    )


def obter_maior_valor(historico, campo):
    if not historico:
        return None

    return max(
        leitura[campo]
        for leitura in historico
    )


def obter_maior_leitura(historico, campo):
    if not historico:
        return None

    return max(
        historico,
        key=lambda leitura: leitura[campo]
    )


def filtrar_por_estado(historico, estado):
    return [
        leitura
        for leitura in historico
        if leitura["estado_geral"] == estado
    ]


def exibir_estatisticas(historico):
    if not historico:
        print("Não há registros para analisar.")
        return

    print("\n===== ESTATÍSTICAS =====")
    print(f"Registros recuperados: {len(historico)}")

    for campo, unidade in [
        ("temperatura", "°C"),
        ("pressao", "bar"),
        ("corrente", "A")
    ]:
        menor = obter_menor_valor(historico, campo)
        maior = obter_maior_valor(historico, campo)
        media = calcular_media(historico, campo)

        print(f"\n{campo.capitalize()}:")
        print(f"  Menor: {menor:.2f} {unidade}")
        print(f"  Maior: {maior:.2f} {unidade}")
        print(f"  Média: {media:.2f} {unidade}")

    for estado in [
        "NORMAL",
        "ATENÇÃO",
        "ALARME",
        "EMERGÊNCIA"
    ]:
        quantidade = len(filtrar_por_estado(historico, estado))
        print(f"Quantidade em {estado}: {quantidade}")

    maior_temperatura = obter_maior_leitura(
        historico,
        "temperatura"
    )
    maior_pressao = obter_maior_leitura(
        historico,
        "pressao"
    )
    maior_corrente = obter_maior_leitura(
        historico,
        "corrente"
    )

    print("\n===== MAIORES REGISTROS =====")
    print(
        f"Maior temperatura: ciclo "
        f"{maior_temperatura['ciclo']}"
    )
    print(
        f"Maior pressão: ciclo "
        f"{maior_pressao['ciclo']}"
    )
    print(
        f"Maior corrente: ciclo "
        f"{maior_corrente['ciclo']}"
    )


def executar_simulacao():
    historico = []
    leituras_ignoradas = 0

    print("===== INÍCIO DA SIMULAÇÃO =====")

    for numero_ciclo in range(1, TOTAL_CICLOS + 1):
        print(f"\nColetando ciclo {numero_ciclo}...")

        if numero_ciclo == 5:
            print("Falha de comunicação com o sensor.")
            leituras_ignoradas += 1
            continue

        leitura = criar_leitura(numero_ciclo)
        historico.append(leitura)
        print(f"Ciclo armazenado: {leitura['estado_geral']}")

    salvar_csv(historico, NOME_ARQUIVO)

    print("\nHistórico gravado com sucesso.")
    print(f"Leituras válidas: {len(historico)}")
    print(f"Leituras ignoradas: {leituras_ignoradas}")

    historico_recuperado = ler_csv(NOME_ARQUIVO)

    print("\n===== HISTÓRICO RECUPERADO DO CSV =====")
    for leitura in historico_recuperado:
        exibir_leitura(leitura)

    exibir_estatisticas(historico_recuperado)


if __name__ == "__main__":
    executar_simulacao()