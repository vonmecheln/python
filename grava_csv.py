import csv

historico = [
    {
        "ciclo": 1,
        "equipamento": "M-01",
        "temperatura": 72.5,
        "pressao": 6.8,
        "corrente": 12.4,
        "estado_geral": "ATENÇÃO"
    },
    {
        "ciclo": 2,
        "equipamento": "M-01",
        "temperatura": 81.3,
        "pressao": 8.2,
        "corrente": 15.7,
        "estado_geral": "ALARME"
    }
]

campos = [
    "ciclo",
    "equipamento",
    "temperatura",
    "pressao",
    "corrente",
    "estado_geral"
]

with open("historico.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=campos,
        delimiter=";"
    )

    escritor.writeheader()
    escritor.writerows(historico)