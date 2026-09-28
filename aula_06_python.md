# Aula 6 — Persistência de leituras em arquivos CSV

**Curso:** Linguagens de Programação e Banco de Dados  
**Curso superior:** Tecnologia em Automação Industrial  
**Instituição:** Instituto Federal do Paraná — Campus Assis Chateaubriand  
**Tema:** Arquivos CSV e persistência de dados do simulador industrial

---

## 1. Contextualização

Na Aula 5, cada leitura do simulador passou a ser representada por um dicionário e o conjunto das leituras foi armazenado em uma lista de dicionários:

```python
historico = [
    {
        "ciclo": 1,
        "equipamento": "M-01",
        "dispositivo": "CLP-SIM-01",
        "temperatura": 72.5,
        "pressao": 6.8,
        "corrente": 12.4,
        "estado_geral": "ATENÇÃO",
        "situacao_critica": False
    }
]
```

Essa estrutura organiza os dados durante a execução do programa. Porém, quando o programa é encerrado, o conteúdo da lista é perdido. Para manter o histórico disponível em outra execução, é necessário gravá-lo em um arquivo.

Nesta aula, o histórico será persistido em um arquivo **CSV**. Depois, o arquivo será lido novamente pelo programa para recuperar os registros e realizar consultas e análises.

> O arquivo CSV funciona como uma etapa intermediária entre a lista de dicionários em memória e um banco de dados.

---

## 2. Objetivos da aula

Ao final desta aula, o estudante deverá ser capaz de:

- explicar o que é um arquivo CSV;
- diferenciar memória principal e armazenamento permanente;
- criar arquivos usando Python;
- utilizar o módulo `csv`;
- gravar uma lista de dicionários com `csv.DictWriter`;
- ler registros com `csv.DictReader`;
- compreender cabeçalho, campos, linhas e delimitadores;
- converter os valores lidos como texto para os tipos adequados;
- validar a existência de campos obrigatórios;
- integrar gravação e leitura ao simulador industrial;
- filtrar registros recuperados de um arquivo;
- calcular estatísticas a partir dos dados persistidos;
- evitar perda de dados ao utilizar modos de abertura de arquivos;
- preparar os dados para a futura utilização do SQLite.

---

## 3. Revisão da Aula 5

Na aula anterior, os dados eram organizados em uma lista de dicionários:

```python
leitura = {
    "ciclo": 1,
    "temperatura": 72.5,
    "pressao": 6.8,
    "corrente": 12.4,
    "estado_geral": "ATENÇÃO"
}

historico.append(leitura)
```

O dicionário representa um registro completo. A lista reúne vários registros.

Enquanto o programa está em execução, os dados podem ser consultados assim:

```python
for leitura in historico:
    print(leitura["temperatura"])
```

Entretanto, ao fechar o programa, a variável `historico` deixa de existir. A persistência em CSV resolve esse problema armazenando os dados em um arquivo externo.

---

## 4. O que é um arquivo CSV?

CSV significa **Comma-Separated Values**, ou **valores separados por vírgula**. É um formato textual utilizado para representar dados organizados em linhas e colunas.

Exemplo de um arquivo CSV:

```text
ciclo,equipamento,temperatura,pressao,corrente,estado_geral
1,M-01,72.5,6.8,12.4,ATENÇÃO
2,M-01,81.3,8.2,15.7,ALARME
```

Nesse exemplo:

- a primeira linha é o cabeçalho;
- cada coluna representa um campo;
- cada linha seguinte representa um registro;
- os valores são separados por um delimitador;
- os dados ficam armazenados como texto no arquivo.

No Brasil, é comum utilizar ponto e vírgula como delimitador, pois a vírgula pode ser utilizada na representação decimal. Nesta aula, será utilizado `;`.

Exemplo:

```text
ciclo;equipamento;temperatura;pressao;corrente;estado_geral
1;M-01;72.5;6.8;12.4;ATENÇÃO
```

### 4.1 Vantagens do CSV

- formato simples e legível;
- fácil abertura em editores de texto e planilhas;
- baixo custo de armazenamento;
- fácil exportação e importação;
- adequado para pequenos históricos;
- útil para trocar dados entre sistemas diferentes.

### 4.2 Limitações do CSV

- não possui consultas SQL;
- não controla relacionamentos entre tabelas;
- não possui validação automática de tipos;
- pode apresentar problemas com delimitadores dentro de textos;
- não é adequado para muitos usuários gravando ao mesmo tempo;
- exige cuidados para evitar duplicações e perda de dados.

---

## 5. O módulo `csv` do Python

O Python possui o módulo padrão `csv`, que oferece recursos para ler e gravar arquivos nesse formato.

```python
import csv
```

As classes mais utilizadas nesta aula são:

| Recurso | Finalidade |
|---|---|
| `csv.writer` | Gravar listas de valores |
| `csv.reader` | Ler linhas como listas |
| `csv.DictWriter` | Gravar dicionários |
| `csv.DictReader` | Ler linhas como dicionários |

Como os registros da Aula 5 já são dicionários, `DictWriter` e `DictReader` são as opções mais adequadas.

---

## 6. Gravando um dicionário em CSV

```python
import csv

leitura = {
    "ciclo": 1,
    "equipamento": "M-01",
    "temperatura": 72.5,
    "pressao": 6.8,
    "corrente": 12.4,
    "estado_geral": "ATENÇÃO"
}

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
    escritor.writerow(leitura)
```

### 6.1 Elementos importantes

- `"w"`: abre o arquivo para escrita, substituindo o conteúdo existente;
- `newline=""`: evita linhas em branco extras em alguns sistemas;
- `encoding="utf-8"`: permite armazenar acentos corretamente;
- `fieldnames`: define os nomes e a ordem das colunas;
- `delimiter=";"`: define o separador das colunas;
- `writeheader()`: grava o cabeçalho;
- `writerow()`: grava um dicionário como uma linha.

> Atenção: utilizar o modo `"w"` novamente apaga o conteúdo anterior. Para adicionar registros ao final, utilize o modo `"a"`.

---

## 7. Gravando uma lista de dicionários

```python
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
```

O método `writerows()` grava vários dicionários de uma só vez.

---

## 8. Lendo um arquivo CSV com `DictReader`

```python
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
```

Cada linha lida é transformada em um dicionário. Porém, todos os valores são inicialmente textos.

Por exemplo:

```python
print(leitura["temperatura"])
print(type(leitura["temperatura"]))
```

O resultado será semelhante a:

```text
72.5
<class 'str'>
```

Para calcular médias, mínimos e máximos, é necessário converter os valores numéricos.

---

## 9. Convertendo os tipos dos dados

```python
def converter_registro(registro):
    registro["ciclo"] = int(registro["ciclo"])
    registro["temperatura"] = float(registro["temperatura"])
    registro["pressao"] = float(registro["pressao"])
    registro["corrente"] = float(registro["corrente"])
    registro["situacao_critica"] = (
        registro["situacao_critica"].lower() == "true"
    )

    return registro
```

Aplicação durante a leitura:

```python
historico = []

with open("historico.csv", "r", newline="", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")

    for registro in leitor:
        registro = converter_registro(registro)
        historico.append(registro)
```

Agora os campos numéricos poderão ser utilizados em cálculos:

```python
media = sum(
    leitura["temperatura"]
    for leitura in historico
) / len(historico)
```

---

## 10. Validando os campos do arquivo

Um arquivo pode estar incompleto ou ter sido alterado incorretamente. Por isso, é importante verificar se os campos esperados estão presentes.

```python
CAMPOS_OBRIGATORIOS = [
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
    "situacao_critica"
]


def validar_campos(registro):
    for campo in CAMPOS_OBRIGATORIOS:
        if campo not in registro:
            return False

    return True
```

A validação pode ser utilizada assim:

```python
if validar_campos(registro):
    historico.append(converter_registro(registro))
else:
    print("Registro ignorado: campos obrigatórios ausentes.")
```

Também é possível tratar erros de conversão:

```python
try:
    registro = converter_registro(registro)
except (TypeError, ValueError, KeyError) as erro:
    print(f"Registro inválido: {erro}")
```

---

## 11. Funções para persistência

Organizar as operações em funções facilita a manutenção do programa.

### 11.1 Gravar histórico

```python
import csv

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
```

### 11.2 Ler histórico

```python
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
                registro = converter_registro(registro)
                historico.append(registro)
            except (TypeError, ValueError, KeyError) as erro:
                print(f"Registro ignorado: {erro}")

    return historico
```

### 11.3 Converter um registro

```python
def converter_registro(registro):
    registro["ciclo"] = int(registro["ciclo"])
    registro["temperatura"] = float(registro["temperatura"])
    registro["pressao"] = float(registro["pressao"])
    registro["corrente"] = float(registro["corrente"])
    registro["situacao_critica"] = (
        registro["situacao_critica"].lower() == "true"
    )

    return registro
```

---

## 12. Integração com o simulador industrial

O simulador deverá:

- utilizar o equipamento `M-01`;
- utilizar o dispositivo `CLP-SIM-01`;
- executar 20 ciclos planejados;
- gerar temperatura entre 60 e 95 °C;
- gerar pressão entre 5.0 e 10.0 bar;
- gerar corrente entre 10.0 e 20.0 A;
- manter a falha de comunicação no ciclo 5;
- não armazenar o ciclo 5;
- gravar o histórico válido no arquivo CSV;
- ler o arquivo após a gravação;
- apresentar estatísticas do histórico recuperado.

### 12.1 Código completo da Aula 6

```python
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
```

---

## 13. Cuidados importantes com arquivos

### 13.1 Modo de abertura

| Modo | Comportamento |
|---|---|
| `"r"` | leitura; o arquivo precisa existir |
| `"w"` | escrita; substitui o conteúdo anterior |
| `"a"` | adiciona conteúdo ao final |
| `"x"` | cria um novo arquivo; falha se ele já existir |

### 13.2 Adicionando registros sem apagar o histórico

Para acrescentar registros a um CSV existente, seria possível utilizar `"a"`. Porém, o cabeçalho não deve ser repetido a cada execução.

```python
import csv
import os


def adicionar_registros(historico, nome_arquivo):
    arquivo_existe = os.path.exists(nome_arquivo)
    arquivo_vazio = (
        not arquivo_existe
        or os.path.getsize(nome_arquivo) == 0
    )

    with open(
        nome_arquivo,
        "a",
        newline="",
        encoding="utf-8"
    ) as arquivo:
        escritor = csv.DictWriter(
            arquivo,
            fieldnames=CAMPOS,
            delimiter=";"
        )

        if arquivo_vazio:
            escritor.writeheader()

        escritor.writerows(historico)
```

### 13.3 Evitando duplicação

Se o simulador for executado várias vezes no modo de acréscimo, os ciclos poderão ser repetidos. Uma melhoria possível é verificar se o ciclo já existe antes de gravar, ou utilizar um identificador único para cada leitura.

---

## 14. Consultas no histórico recuperado

Depois da leitura do CSV, os registros voltam a ser uma lista de dicionários. Portanto, as consultas da Aula 5 continuam funcionando.

### 14.1 Último registro

```python
if historico:
    print(historico[-1])
```

### 14.2 Leituras críticas

```python
leituras_criticas = []

for leitura in historico:
    if leitura["estado_geral"] in [
        "ALARME",
        "EMERGÊNCIA"
    ]:
        leituras_criticas.append(leitura)
```

### 14.3 Temperaturas acima do limite

```python
for leitura in historico:
    if leitura["temperatura"] > LIMITE_TEMPERATURA:
        print(
            f"Ciclo {leitura['ciclo']}: "
            f"{leitura['temperatura']:.2f} °C"
        )
```

### 14.4 Verificação do ciclo ignorado

```python
ciclos = [
    leitura["ciclo"]
    for leitura in historico
]

if 5 not in ciclos:
    print("O ciclo 5 não foi armazenado.")
```

---

## 15. Testes controlados

### Teste 1 — Gravar um registro

Criar um único dicionário, gravá-lo no CSV e verificar:

- se o arquivo foi criado;
- se o cabeçalho foi gravado;
- se o registro aparece na segunda linha;
- se os acentos foram preservados.

### Teste 2 — Gravar vários registros

Criar três dicionários e utilizar `writerows()`.

Verificar:

- quantidade de linhas;
- ordem dos campos;
- correspondência entre cada registro e sua linha.

### Teste 3 — Ler o arquivo

Ler o CSV com `DictReader` e verificar:

```python
print(type(historico))
print(type(historico[0]))
print(historico[0]["equipamento"])
```

### Teste 4 — Conversão de tipos

Verificar que:

```python
print(type(historico[0]["ciclo"]))
print(type(historico[0]["temperatura"]))
print(type(historico[0]["situacao_critica"]))
```

Os tipos esperados são `int`, `float` e `bool`.

### Teste 5 — Falha de comunicação

Executar o simulador e verificar:

- se existem 19 leituras válidas;
- se existe uma leitura ignorada;
- se o ciclo 5 não aparece no CSV;
- se os ciclos 1 a 4 e 6 a 20 foram preservados.

### Teste 6 — Lista vazia

```python
historico_vazio = []

print(calcular_media(historico_vazio, "temperatura"))
print(obter_menor_valor(historico_vazio, "temperatura"))
print(obter_maior_valor(historico_vazio, "temperatura"))
print(obter_maior_leitura(historico_vazio, "temperatura"))
```

As funções não devem gerar erro.

### Teste 7 — Arquivo inexistente

```python
try:
    historico = ler_csv("arquivo_que_nao_existe.csv")
except FileNotFoundError:
    print("Arquivo não encontrado.")
```

Uma melhoria é tratar essa situação dentro da própria função de leitura.

---

## 16. Exercícios propostos

### Exercício 1 — Criar um CSV manualmente

Criar um arquivo com três leituras do equipamento `M-01`. Utilizar as colunas:

- ciclo;
- equipamento;
- temperatura;
- pressão;
- corrente;
- estado geral.

Ler o arquivo no Python e exibir os registros.

### Exercício 2 — Gravar a lista de dicionários

Criar uma lista com pelo menos cinco dicionários e gravá-la utilizando `DictWriter`.

### Exercício 3 — Recuperar e converter

Ler o arquivo e converter:

- `ciclo` para inteiro;
- `temperatura` para número decimal;
- `pressao` para número decimal;
- `corrente` para número decimal.

### Exercício 4 — Filtrar o arquivo

Criar uma lista contendo apenas leituras com estado `ALARME` ou `EMERGÊNCIA`.

### Exercício 5 — Estatísticas persistidas

Calcular, a partir do CSV:

- menor temperatura;
- maior temperatura;
- média da temperatura;
- menor pressão;
- maior pressão;
- média da pressão;
- menor corrente;
- maior corrente;
- média da corrente.

### Exercício 6 — Encontrar os maiores registros

Identificar:

- o ciclo de maior temperatura;
- o ciclo de maior pressão;
- o ciclo de maior corrente.

Utilizar `max()` com `key=lambda`.

### Exercício 7 — Exportar somente leituras críticas

Ler o arquivo principal e criar um segundo arquivo contendo apenas as leituras em alarme ou emergência.

### Exercício 8 — Corrigir registros inválidos

Inserir manualmente uma linha com temperatura inválida no CSV e modificar a função de leitura para ignorar apenas essa linha, mantendo as demais.

---

## 17. Desafio final

Evoluir o simulador para que ele:

1. execute a coleta de 20 ciclos;
2. ignore o ciclo 5 por falha de comunicação;
3. armazene cada leitura como dicionário;
4. grave os registros em `historico_leituras.csv`;
5. leia o arquivo em uma nova etapa do programa;
6. converta os tipos corretamente;
7. exiba o histórico recuperado;
8. filtre alarmes e emergências;
9. calcule estatísticas;
10. identifique os ciclos de maior temperatura, pressão e corrente;
11. informe a quantidade de leituras válidas e ignoradas;
12. valide a existência dos campos obrigatórios.

### Melhoria obrigatória

Implementar pelo menos uma melhoria:

- tratamento de arquivo inexistente;
- prevenção de duplicação de ciclos;
- exportação de leituras críticas para outro CSV;
- inclusão de data, horário, operador e turno;
- criação de um menu de opções;
- gravação em modo de acréscimo;
- validação de valores fora das faixas esperadas;
- geração de um relatório textual.

---

## 18. Perguntas de análise

1. O que significa a sigla CSV?
2. Qual é a função do cabeçalho de um arquivo CSV?
3. Qual é a diferença entre uma linha e uma coluna?
4. Por que o delimitador `;` pode ser mais adequado em arquivos utilizados no Brasil?
5. Qual é a diferença entre os modos `"r"`, `"w"` e `"a"`?
6. Por que `newline=""` é utilizado ao abrir um CSV?
7. Por que o parâmetro `encoding="utf-8"` é importante?
8. Qual é a diferença entre `DictWriter` e `DictReader`?
9. Por que os valores lidos de um CSV são inicialmente textos?
10. Por que é necessário converter temperatura, pressão e corrente antes de calcular estatísticas?
11. O que pode acontecer quando um programa utiliza o modo `"w"` sem verificar o conteúdo anterior?
12. Como evitar a repetição do cabeçalho ao adicionar novos registros?
13. Por que é importante validar os campos obrigatórios?
14. Qual é a vantagem de manter cada leitura como um dicionário?
15. Qual é a vantagem de armazenar o histórico em um arquivo?
16. Quais são as limitações do CSV em comparação com um banco de dados?
17. Por que o ciclo 5 não deve aparecer no histórico?
18. Como verificar se uma leitura apresenta situação crítica?
19. Como encontrar o registro com maior temperatura depois de ler o CSV?
20. Que informações adicionais poderiam ser armazenadas no arquivo?
21. O que aconteceria se dois operadores gravassem no mesmo arquivo ao mesmo tempo?
22. Como um CSV poderia ser importado para uma planilha?
23. Em que situação seria melhor utilizar SQLite em vez de CSV?
24. Como identificar registros duplicados?
25. Que campo poderia funcionar como identificador único de uma leitura?

---

## 19. Entrega da atividade

Cada estudante ou dupla deverá entregar:

- arquivo `aula_06_arquivos_csv.py`;
- arquivo CSV com o histórico das leituras;
- código de gravação utilizando `DictWriter`;
- código de leitura utilizando `DictReader`;
- conversão dos tipos dos dados;
- tratamento da falha de comunicação do ciclo 5;
- exibição formatada do histórico;
- filtro de leituras críticas;
- cálculo das estatísticas;
- identificação dos maiores registros;
- testes controlados;
- respostas às perguntas de análise;
- implementação de pelo menos uma melhoria.

---

## 20. Critérios de avaliação

| Critério | Pontuação |
|---|---:|
| Compreensão do formato CSV | 1,0 |
| Gravação correta com `DictWriter` | 1,5 |
| Leitura correta com `DictReader` | 1,5 |
| Conversão e validação dos tipos | 1,0 |
| Integração com o simulador | 2,0 |
| Consultas, filtros e estatísticas | 1,5 |
| Testes, organização e clareza do código | 1,0 |
| Implementação de melhoria | 0,5 |
| **Total** | **10,0** |

---

## 21. Relação entre memória, CSV e banco de dados

A evolução do sistema pode ser compreendida em três etapas:

### Etapa 1 — Dados em memória

```python
historico = []
```

Os dados existem somente enquanto o programa está executando.

### Etapa 2 — Dados em arquivo CSV

```python
salvar_csv(historico, "historico_leituras.csv")
```

Os dados passam a sobreviver ao encerramento do programa.

### Etapa 3 — Dados em banco de dados

Na próxima etapa, o histórico poderá ser armazenado em uma tabela SQLite:

```sql
CREATE TABLE leituras (
    ciclo INTEGER,
    equipamento TEXT,
    temperatura REAL,
    pressao REAL,
    corrente REAL,
    estado_geral TEXT
);
```

O banco de dados permitirá realizar consultas estruturadas, criar índices, evitar duplicidades e trabalhar com maior volume de dados.

---

## 22. Fechamento conceitual

Na Aula 5, cada leitura foi organizada como um registro completo em um dicionário. Na Aula 6, a lista de dicionários passou a ser gravada em um arquivo CSV e recuperada posteriormente.

O fluxo desenvolvido foi:

```text
Sensores simulados
        ↓
Dicionário de leitura
        ↓
Lista de dicionários
        ↓
Arquivo CSV
        ↓
Leitura do arquivo
        ↓
Conversão dos tipos
        ↓
Filtros e estatísticas
```

O CSV é uma solução simples para persistir dados e trocar informações entre aplicações. Entretanto, quando o volume de dados cresce ou quando são necessárias consultas mais complexas, o banco de dados passa a ser mais adequado.

Na próxima aula, o histórico poderá ser migrado para o **SQLite**, permitindo trabalhar com tabelas, comandos SQL, inserções, consultas, atualizações e exclusões.
