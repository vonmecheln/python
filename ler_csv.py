import csv

historico = []

with open("historico.csv", "r", newline="", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(
        arquivo,
        delimiter=";"
    )

    for registro in leitor:
        historico.append(registro)

for leitura in historico:
    print(leitura)