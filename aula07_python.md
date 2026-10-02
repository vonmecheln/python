# Aula 7 — Persistência de dados com SQLite

**Curso:** Linguagens de Programação e Banco de Dados  
**Curso Superior:** Tecnologia em Automação Industrial  
**Instituição:** Instituto Federal do Paraná — Campus Assis Chateaubriand  
**Duração sugerida:** 2 a 3 horas  
**Pré-requisitos:** listas e dicionários em Python, funções, arquivos CSV e noções básicas de SQL.

---

## 1. Tema da aula

Na Aula 6, o simulador gravava e recuperava leituras em arquivos CSV. Nesta aula, os dados serão armazenados em um **banco de dados SQLite**, consultados com SQL e manipulados pelo módulo `sqlite3` do Python.

O objetivo é evoluir o histórico da lista de dicionários para uma tabela persistente. O arquivo do banco permanece disponível depois que o programa termina, permitindo inserir novas leituras e consultar o histórico em execuções futuras.

> **Ideia central:** CSV organiza dados em linhas e colunas em um arquivo de texto; SQLite permite armazenar registros em tabelas e consultá-los com SQL.

## 2. Objetivos de aprendizagem

Ao final da aula, o estudante deverá ser capaz de:

- explicar o que é um banco de dados relacional e o que é SQLite;
- criar uma conexão com o banco usando `sqlite3`;
- criar tabelas com `CREATE TABLE`;
- inserir registros com `INSERT` e parâmetros;
- consultar dados com `SELECT`, `WHERE`, `ORDER BY` e funções de agregação;
- atualizar e remover registros com `UPDATE` e `DELETE`;
- relacionar as operações CRUD aos comandos SQL;
- converter leituras do simulador em registros persistentes;
- usar transações e fechar conexões corretamente;
- evitar a montagem de comandos SQL por concatenação de texto.

## 3. Situação-problema

O simulador industrial gera temperatura, pressão, corrente e estado geral do equipamento M-01. Na Aula 5, cada leitura era um dicionário; na Aula 6, a lista de dicionários podia ser salva em CSV. Agora, a equipe precisa:

1. armazenar cada leitura em uma tabela;
2. preservar o número original do ciclo, mesmo quando uma coleta é ignorada;
3. consultar alarmes, emergências e valores máximos;
4. acrescentar leituras em novas execuções sem apagar o histórico;
5. atualizar ou excluir registros quando necessário.

O ciclo 5 continuará simulando falha de comunicação: ele não produzirá registro no banco, mas os ciclos seguintes continuarão com a numeração original.

## 4. Conceitos essenciais

### 4.1 Banco de dados, tabela, registro e campo

- **Banco de dados:** conjunto organizado de dados. Neste exercício, será um arquivo SQLite.
- **Tabela:** estrutura que agrupa registros de um mesmo tipo, semelhante a uma planilha.
- **Registro ou linha:** conjunto de valores referentes a uma leitura de um ciclo.
- **Campo ou coluna:** informação definida para cada registro, como temperatura ou estado geral.
- **Chave primária:** campo que identifica cada linha de forma única.

### 4.2 O que é SQLite?

SQLite é um sistema de banco de dados relacional que armazena o banco em um arquivo local. O Python inclui o módulo `sqlite3`, portanto não é necessário instalar um servidor de banco para esta aula.

A conexão pode criar o arquivo do banco automaticamente:

```python
import sqlite3

conexao = sqlite3.connect("historico_industrial.db")
```

Se o arquivo não existir, o SQLite o cria. O banco não é um CSV: trata-se de um arquivo próprio, que deve ser acessado pelo SQLite.

### 4.3 Tipos de dados usados

| Tipo SQLite | Uso no simulador               | Exemplo                                |
| ----------- | ------------------------------ | -------------------------------------- |
| `INTEGER`   | números inteiros e indicadores | ciclo `1`, situação crítica `0` ou `1` |
| `REAL`      | números decimais               | temperatura `72.5`                     |
| `TEXT`      | textos                         | equipamento `M-01`, estado `ATENÇÃO`   |

SQLite também aceita `NULL` para representar ausência de valor. Nesta atividade, os campos principais serão preenchidos.

## 5. SQL básico

SQL é a linguagem usada para definir e consultar dados relacionais.

### Criar uma tabela

```sql
CREATE TABLE IF NOT EXISTS leituras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ciclo INTEGER NOT NULL,
    equipamento TEXT NOT NULL,
    dispositivo TEXT NOT NULL,
    temperatura REAL NOT NULL,
    pressao REAL NOT NULL,
    corrente REAL NOT NULL,
    status_temperatura TEXT NOT NULL,
    status_pressao TEXT NOT NULL,
    status_corrente TEXT NOT NULL,
    estado_geral TEXT NOT NULL,
    situacao_critica INTEGER NOT NULL
);
```

`id` é um identificador gerado pelo banco. Ele é diferente de `ciclo`: o ciclo representa a posição da coleta na simulação; o `id` distingue cada registro armazenado. Isso permite que a tabela aceite históricos de várias execuções sem exigir que o ciclo seja único.

`NOT NULL` indica que o campo deve receber um valor. `AUTOINCREMENT` solicita que o SQLite gere o identificador automaticamente.

### Inserir um registro

```sql
INSERT INTO leituras (
    ciclo, equipamento, dispositivo,
    temperatura, pressao, corrente,
    status_temperatura, status_pressao, status_corrente,
    estado_geral, situacao_critica
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
```

Os pontos de interrogação são parâmetros. Os valores são fornecidos separadamente pelo Python.

### Consultar registros

```sql
SELECT ciclo, temperatura, pressao, corrente, estado_geral
FROM leituras
WHERE equipamento = 'M-01'
ORDER BY ciclo;
```

- `SELECT` escolhe os campos;
- `FROM` indica a tabela;
- `WHERE` filtra linhas;
- `ORDER BY` define a ordenação.

### Atualizar e remover

```sql
UPDATE leituras
SET estado_geral = 'ATENÇÃO'
WHERE id = 1;

DELETE FROM leituras
WHERE id = 1;
```

**Atenção:** sempre confira o `WHERE` em `UPDATE` e `DELETE`. Sem ele, todas as linhas da tabela podem ser afetadas.

## 6. Mapeamento das operações CRUD

CRUD representa as quatro operações básicas sobre dados persistentes.

| Operação | Significado   | SQL      |
| -------- | ------------- | -------- |
| Create   | criar/inserir | `INSERT` |
| Read     | consultar/ler | `SELECT` |
| Update   | atualizar     | `UPDATE` |
| Delete   | excluir       | `DELETE` |

## 7. Exercício guiado: criar o banco e a tabela

Crie o arquivo `aula_07_sqlite.py` e comece com:

```python
import sqlite3

NOME_BANCO = "historico_industrial.db"

conexao = sqlite3.connect(NOME_BANCO)
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS leituras (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ciclo INTEGER NOT NULL,
        equipamento TEXT NOT NULL,
        dispositivo TEXT NOT NULL,
        temperatura REAL NOT NULL,
        pressao REAL NOT NULL,
        corrente REAL NOT NULL,
        status_temperatura TEXT NOT NULL,
        status_pressao TEXT NOT NULL,
        status_corrente TEXT NOT NULL,
        estado_geral TEXT NOT NULL,
        situacao_critica INTEGER NOT NULL
    )
""")

conexao.commit()
```

`cursor` executa comandos SQL. `commit()` confirma as alterações pendentes. A tabela só é criada se ainda não existir, então o programa pode ser executado novamente sem tentar recriá-la.

## 8. Inserção de dicionários com parâmetros

Cada leitura gerada pelo simulador pode continuar sendo representada como dicionário em Python:

```python
leitura = {
    "ciclo": 1,
    "equipamento": "M-01",
    "dispositivo": "CLP-SIM-01",
    "temperatura": 72.5,
    "pressao": 6.8,
    "corrente": 12.4,
    "status_temperatura": "ATENÇÃO",
    "status_pressao": "NORMAL",
    "status_corrente": "NORMAL",
    "estado_geral": "ATENÇÃO",
    "situacao_critica": False
}
```

Uma função separada pode inserir o registro:

```python
def inserir_leitura(cursor, conexao, leitura):
    cursor.execute("""
        INSERT INTO leituras (
            ciclo, equipamento, dispositivo,
            temperatura, pressao, corrente,
            status_temperatura, status_pressao, status_corrente,
            estado_geral, situacao_critica
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        leitura["ciclo"],
        leitura["equipamento"],
        leitura["dispositivo"],
        leitura["temperatura"],
        leitura["pressao"],
        leitura["corrente"],
        leitura["status_temperatura"],
        leitura["status_pressao"],
        leitura["status_corrente"],
        leitura["estado_geral"],
        int(leitura["situacao_critica"])
    ))
    conexao.commit()
```

O Python converte `True` e `False` para inteiros; aqui fazemos essa conversão explicitamente para gravar `1` ou `0`.

> **Segurança e correção:** use parâmetros `?` em vez de construir SQL com `+` ou f-strings. A parametrização trata os valores corretamente e ajuda a evitar erros e injeção de SQL.

## 9. Simulador integrado — versão de referência

O programa abaixo cria a tabela, simula 20 ciclos, ignora a falha de comunicação no ciclo 5, grava as leituras válidas e executa consultas básicas. Execute-o na mesma pasta de trabalho: o arquivo `historico_industrial.db` será criado ali.

```python
import random
import sqlite3

NOME_BANCO = "historico_industrial.db"
EQUIPAMENTO = "M-01"
DISPOSITIVO = "CLP-SIM-01"
CICLOS_PLANEJADOS = 20

LIMITE_TEMPERATURA = 80
LIMITE_PRESSAO = 8
LIMITE_CORRENTE = 15


def criar_tabela(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leituras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ciclo INTEGER NOT NULL,
            equipamento TEXT NOT NULL,
            dispositivo TEXT NOT NULL,
            temperatura REAL NOT NULL,
            pressao REAL NOT NULL,
            corrente REAL NOT NULL,
            status_temperatura TEXT NOT NULL,
            status_pressao TEXT NOT NULL,
            status_corrente TEXT NOT NULL,
            estado_geral TEXT NOT NULL,
            situacao_critica INTEGER NOT NULL
        )
    """)


def classificar_temperatura(temperatura):
    if temperatura < 70:
        return "NORMAL"
    if temperatura <= LIMITE_TEMPERATURA:
        return "ATENÇÃO"
    return "ALARME"


def classificar_pressao(pressao):
    if pressao < 7:
        return "NORMAL"
    if pressao <= LIMITE_PRESSAO:
        return "ATENÇÃO"
    return "ALARME"


def classificar_corrente(corrente):
    if corrente < 13:
        return "NORMAL"
    if corrente <= LIMITE_CORRENTE:
        return "ATENÇÃO"
    return "ALARME"


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

    existe_alarme = (
        status_temperatura == "ALARME"
        or status_pressao == "ALARME"
        or status_corrente == "ALARME"
    )
    existe_atencao = (
        status_temperatura == "ATENÇÃO"
        or status_pressao == "ATENÇÃO"
        or status_corrente == "ATENÇÃO"
    )

    if situacao_critica:
        estado_geral = "EMERGÊNCIA"
    elif existe_alarme:
        estado_geral = "ALARME"
    elif existe_atencao:
        estado_geral = "ATENÇÃO"
    else:
        estado_geral = "NORMAL"

    return {
        "ciclo": numero_ciclo,
        "equipamento": EQUIPAMENTO,
        "dispositivo": DISPOSITIVO,
        "temperatura": temperatura,
        "pressao": pressao,
        "corrente": corrente,
        "status_temperatura": status_temperatura,
        "status_pressao": status_pressao,
        "status_corrente": status_corrente,
        "estado_geral": estado_geral,
        "situacao_critica": situacao_critica
    }


def inserir_leitura(cursor, leitura):
    cursor.execute("""
        INSERT INTO leituras (
            ciclo, equipamento, dispositivo,
            temperatura, pressao, corrente,
            status_temperatura, status_pressao, status_corrente,
            estado_geral, situacao_critica
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        leitura["ciclo"],
        leitura["equipamento"],
        leitura["dispositivo"],
        leitura["temperatura"],
        leitura["pressao"],
        leitura["corrente"],
        leitura["status_temperatura"],
        leitura["status_pressao"],
        leitura["status_corrente"],
        leitura["estado_geral"],
        int(leitura["situacao_critica"])
    ))


def exibir_historico(cursor):
    cursor.execute("""
        SELECT ciclo, temperatura, pressao, corrente, estado_geral
        FROM leituras
        WHERE equipamento = ?
        ORDER BY id
    """, (EQUIPAMENTO,))

    registros = cursor.fetchall()
    print("\\n=== HISTÓRICO DO EQUIPAMENTO ===")

    if not registros:
        print("Não há leituras armazenadas.")
        return

    for ciclo, temperatura, pressao, corrente, estado in registros:
        print(
            f"Ciclo {ciclo:02d} | "
            f"T={temperatura:.2f} °C | "
            f"P={pressao:.2f} bar | "
            f"I={corrente:.2f} A | "
            f"Estado={estado}"
        )


def exibir_estatisticas(cursor):
    cursor.execute("""
        SELECT
            COUNT(*),
            MIN(temperatura), MAX(temperatura), AVG(temperatura),
            MIN(pressao), MAX(pressao), AVG(pressao),
            MIN(corrente), MAX(corrente), AVG(corrente)
        FROM leituras
        WHERE equipamento = ?
    """, (EQUIPAMENTO,))

    resultado = cursor.fetchone()
    quantidade = resultado[0]

    print("\\n=== ESTATÍSTICAS ===")
    if quantidade == 0:
        print("Não há dados para calcular estatísticas.")
        return

    (_, t_min, t_max, t_media,
     p_min, p_max, p_media,
     i_min, i_max, i_media) = resultado

    print(f"Quantidade de leituras: {quantidade}")
    print(f"Temperatura: mín. {t_min:.2f}, máx. {t_max:.2f}, média {t_media:.2f} °C")
    print(f"Pressão: mín. {p_min:.2f}, máx. {p_max:.2f}, média {p_media:.2f} bar")
    print(f"Corrente: mín. {i_min:.2f}, máx. {i_max:.2f}, média {i_media:.2f} A")


def exibir_leituras_criticas(cursor):
    cursor.execute("""
        SELECT ciclo, temperatura, pressao, corrente, estado_geral
        FROM leituras
        WHERE equipamento = ?
          AND estado_geral IN ('ALARME', 'EMERGÊNCIA')
        ORDER BY id
    """, (EQUIPAMENTO,))

    registros = cursor.fetchall()
    print("\\n=== ALARMES E EMERGÊNCIAS ===")
    if not registros:
        print("Nenhum alarme ou emergência encontrado.")
        return

    for ciclo, temperatura, pressao, corrente, estado in registros:
        print(
            f"Ciclo {ciclo}: {estado} — "
            f"{temperatura:.2f} °C, {pressao:.2f} bar, {corrente:.2f} A"
        )


def main():
    conexao = sqlite3.connect(NOME_BANCO)

    try:
        cursor = conexao.cursor()
        criar_tabela(cursor)
        conexao.commit()

        leituras_ignoradas = 0

        for numero_ciclo in range(1, CICLOS_PLANEJADOS + 1):
            print(f"\\nColetando ciclo {numero_ciclo}...")

            if numero_ciclo == 5:
                print("Falha de comunicação com o sensor. Leitura ignorada.")
                leituras_ignoradas += 1
                continue

            leitura = criar_leitura(numero_ciclo)
            inserir_leitura(cursor, leitura)
            print(f"Registro do ciclo {numero_ciclo} inserido: {leitura['estado_geral']}")

        # Confirma as inserções da execução atual.
        conexao.commit()

        print(f"\\nCiclos planejados: {CICLOS_PLANEJADOS}")
        print(f"Leituras ignoradas: {leituras_ignoradas}")
        exibir_historico(cursor)
        exibir_leituras_criticas(cursor)
        exibir_estatisticas(cursor)

    except sqlite3.Error as erro:
        # Se houver erro antes do commit, desfaz as alterações pendentes.
        conexao.rollback()
        print(f"Erro no banco de dados: {erro}")

    finally:
        conexao.close()
        print("\\nConexão com o banco encerrada.")


if __name__ == "__main__":
    main()
```

### Observação importante sobre execuções repetidas

O banco persiste os dados. Por isso, executar o simulador várias vezes **acrescenta** novas leituras, em vez de apagar as anteriores. Como esta versão grava uma nova simulação a cada execução, os ciclos de 1 a 20 podem aparecer repetidos em diferentes execuções; o campo `id` continua identificando cada linha.

Para uma atividade inicial, isso ajuda a demonstrar persistência. Em um sistema real, é recomendável adicionar um campo `data_hora` ou um identificador da execução para distinguir simulações. Evite apagar o banco automaticamente: isso eliminaria o histórico salvo.

> **Limite da simulação:** com pressão gerada entre 5,0 e 10,0 bar, a condição `pressao > 10` nunca será verdadeira. A corrente acima de 18 A e a temperatura acima de 90 °C ainda podem produzir situação crítica. Essa observação é útil para discutir se os limites e as faixas de geração são coerentes.

## 10. Consultas SQL de análise

As consultas a seguir podem ser executadas pelo cursor do Python usando `cursor.execute(...)`.

### Consultar leituras de um equipamento

```sql
SELECT ciclo, temperatura, pressao, corrente, estado_geral
FROM leituras
WHERE equipamento = ?
ORDER BY ciclo;
```

### Consultar apenas alarmes e emergências

```sql
SELECT ciclo, estado_geral, temperatura, pressao, corrente
FROM leituras
WHERE estado_geral IN ('ALARME', 'EMERGÊNCIA')
ORDER BY ciclo;
```

### Encontrar a maior temperatura

```sql
SELECT ciclo, temperatura
FROM leituras
WHERE temperatura = (SELECT MAX(temperatura) FROM leituras);
```

Essa consulta pode retornar mais de uma linha em caso de empate.

### Contar estados gerais

```sql
SELECT estado_geral, COUNT(*) AS quantidade
FROM leituras
GROUP BY estado_geral
ORDER BY quantidade DESC;
```

`GROUP BY` agrupa linhas com o mesmo valor; `COUNT(*)` conta as linhas de cada grupo.

### Calcular estatísticas

```sql
SELECT
    MIN(temperatura), MAX(temperatura), AVG(temperatura),
    MIN(pressao), MAX(pressao), AVG(pressao),
    MIN(corrente), MAX(corrente), AVG(corrente)
FROM leituras;
```

O SQLite oferece `MIN`, `MAX`, `AVG`, `SUM` e `COUNT` para cálculos agregados.

### Contar leituras acima de um limite

```sql
SELECT COUNT(*)
FROM leituras
WHERE temperatura > ?;
```

No Python:

```python
cursor.execute(
    "SELECT COUNT(*) FROM leituras WHERE temperatura > ?",
    (LIMITE_TEMPERATURA,)
)
quantidade = cursor.fetchone()[0]
print(f"Leituras acima do limite: {quantidade}")
```

## 11. Atualização e exclusão controladas

Para praticar `UPDATE`, use o identificador (`id`) de uma linha conhecida:

```python
cursor.execute("""
    UPDATE leituras
    SET estado_geral = ?
    WHERE id = ?
""", ("ATENÇÃO", 1))
conexao.commit()
```

Para praticar `DELETE`, exclua apenas uma linha identificada:

```python
cursor.execute(
    "DELETE FROM leituras WHERE id = ?",
    (1,)
)
conexao.commit()
```

Esses comandos alteram dados reais no banco. Realize os testes em um banco de exercício ou com registros de teste, não no histórico que se deseja preservar.

## 12. Transações e conexão

Uma transação agrupa alterações que devem ser confirmadas ou desfeitas. No exemplo, `commit()` confirma mudanças e `rollback()` desfaz alterações ainda não confirmadas após um erro.

Práticas importantes:

- abrir a conexão com `sqlite3.connect(...)`;
- confirmar alterações com `commit()`;
- usar `rollback()` quando necessário;
- fechar a conexão ao terminar;
- executar SQL parametrizado;
- tratar o caso de consulta sem resultados;
- não assumir que o banco começa vazio.

O `try/except/finally` da versão de referência garante que a conexão seja fechada mesmo se ocorrer erro.

## 13. Comparação: CSV e SQLite

| Aspecto                    | CSV                                    | SQLite                                |
| -------------------------- | -------------------------------------- | ------------------------------------- |
| Formato                    | Texto organizado por delimitadores     | Banco relacional em arquivo próprio   |
| Consultas e filtros        | Geralmente feitos pelo programa        | Feitos diretamente com SQL            |
| Tipos                      | Valores lidos como texto e convertidos | Tipos declarados nas colunas          |
| Atualização de um registro | Normalmente reescreve o arquivo        | Usa `UPDATE` para linhas selecionadas |
| Relações e integridade     | Limitadas                              | Tabelas, chaves e restrições          |
| Melhor uso didático        | Troca simples de dados                 | Persistência estruturada e consultas  |

CSV continua sendo útil para intercâmbio e planilhas. SQLite é mais apropriado quando se deseja consultar e modificar registros com frequência e manter dados estruturados.

## 14. Testes controlados

### Teste 1 — Banco e tabela

- Executar o programa;
- verificar se o arquivo `historico_industrial.db` foi criado;
- executar novamente e confirmar que a tabela não causa erro de criação duplicada.

### Teste 2 — Persistência

- Executar o simulador;
- encerrar o programa;
- executar novamente;
- observar que a quantidade total de registros aumenta.

### Teste 3 — Ciclo com falha

- conferir se o ciclo 5 não foi inserido;
- verificar se os ciclos 4 e 6 permanecem com seus números originais;
- confirmar que a falha não interrompe as demais coletas.

### Teste 4 — Filtro de críticos

- consultar alarmes e emergências;
- comparar as linhas retornadas com a coluna `estado_geral`;
- lembrar que uma execução aleatória pode não gerar todos os estados.

### Teste 5 — Estatísticas

- comparar `MIN`, `MAX` e `AVG` com os valores apresentados no histórico;
- confirmar que os cálculos usam apenas as linhas consultadas, caso exista um `WHERE`.

### Teste 6 — Banco sem leituras

Criar uma tabela vazia ou usar outro nome de banco e verificar se as funções apresentam mensagem informativa, sem tentar formatar valores inexistentes.

### Teste 7 — Atualização e exclusão

- inserir um registro de teste;
- atualizar somente o registro com o `id` escolhido;
- consultar o resultado;
- excluir o registro de teste e conferir novamente.

## 15. Exercícios

### Exercício 1 — Explorar a tabela

Escreva uma consulta que mostre `id`, ciclo, equipamento e estado geral em ordem decrescente de temperatura.

### Exercício 2 — Filtrar por faixa

Liste as leituras com temperatura superior a 80 °C e corrente superior a 15 A.

### Exercício 3 — Contar emergências

Use SQL para contar quantas leituras possuem estado geral `EMERGÊNCIA`.

### Exercício 4 — Maior valor por variável

Faça consultas para encontrar os valores máximos de temperatura, pressão e corrente, indicando o ciclo correspondente.

### Exercício 5 — Inserir um registro controlado

Insira manualmente uma leitura de teste com estado `ALARME`, usando parâmetros no Python. Consulte-a depois com `SELECT`.

### Exercício 6 — Completar os campos

Evolua a tabela para armazenar `data_hora`, `operador`, `turno` e `observacao`. Atualize também o comando `INSERT` para preencher as novas colunas.

### Exercício 7 — Importar CSV

Como extensão, leia um CSV gerado na Aula 6 com `csv.DictReader` e insira suas linhas no SQLite. Converta os campos numéricos para os tipos adequados e converta `situacao_critica` para `0` ou `1`.

## 16. Desafio final

Evolua o simulador para:

1. registrar data e horário da coleta;
2. identificar uma execução de simulação;
3. armazenar operador e turno;
4. inserir as leituras válidas em uma transação;
5. permitir consulta pelo equipamento e por intervalo de data;
6. exibir o ciclo de maior temperatura, pressão e corrente;
7. contar quantidades por estado geral;
8. exportar uma consulta selecionada para CSV;
9. incluir uma opção de menu para consultar, atualizar ou excluir uma leitura de teste.

## 17. Perguntas de análise

1. Qual é a diferença entre um arquivo CSV e um banco SQLite?
2. O que representam tabela, linha e coluna?
3. Qual é a finalidade da chave primária `id`?
4. Por que o número do ciclo não substitui necessariamente o `id`?
5. O que fazem `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE` e `DELETE`?
6. Para que serve o `WHERE`? O que pode acontecer se ele for omitido em um `UPDATE` ou `DELETE`?
7. Por que os valores devem ser enviados como parâmetros em vez de concatenados ao SQL?
8. Qual é a diferença entre `commit()` e `rollback()`?
9. Por que a falha do ciclo 5 não deve alterar a numeração dos ciclos seguintes?
10. O que acontece com o histórico se o simulador for executado várias vezes?
11. Como `GROUP BY` e `COUNT(*)` podem ajudar na análise de estados?
12. Quais vantagens e limitações o SQLite apresenta para um simulador local?
13. Quais campos adicionais seriam úteis para a rastreabilidade industrial?
14. Como o SQLite pode apoiar uma futura integração com sistemas maiores?

## 18. Entrega da atividade

Cada estudante ou dupla deverá entregar:

- arquivo `aula_07_sqlite.py`;
- arquivo do banco SQLite criado pelo programa;
- tabela `leituras` com registros completos;
- implementação da falha de comunicação no ciclo 5;
- consultas para histórico, críticos e estatísticas;
- demonstração de pelo menos uma operação de atualização e uma de exclusão em registro de teste;
- testes controlados e evidências dos resultados;
- respostas às perguntas de análise;
- uma melhoria no simulador, como data/hora, filtros, menu ou importação de CSV.

**Cuidados com a entrega:** o banco deve conter os dados necessários para demonstrar o trabalho. Não apagar o arquivo do banco antes de enviá-lo. Se o histórico tiver dados de várias execuções, explicar isso no relatório.

## 19. Critérios de avaliação

| Critério                                            | Pontuação |
| --------------------------------------------------- | --------: |
| Criação da conexão e da tabela                      |       1,0 |
| Inserção parametrizada dos registros                |       1,5 |
| Integração correta com o simulador e ciclo ignorado |       1,5 |
| Consultas, filtros e ordenação                      |       1,5 |
| Estatísticas e agrupamentos SQL                     |       1,0 |
| Uso correto de commit, rollback e fechamento        |       1,0 |
| Testes, organização e clareza do código             |       1,0 |
| Operações CRUD demonstradas com segurança           |       1,0 |
| Implementação de melhoria                           |       0,5 |
| **Total**                                           |  **10,0** |

## 20. Fechamento conceitual

A sequência de aulas evoluiu o modo de representar e persistir as leituras:

1. **Aula 4:** listas paralelas para guardar o histórico em memória;
2. **Aula 5:** lista de dicionários, com cada leitura organizada como um registro;
3. **Aula 6:** gravação e recuperação dos registros em CSV;
4. **Aula 7:** armazenamento persistente em tabela SQLite e consultas com SQL.

O caminho de uma leitura é: **sensores simulados → dicionário Python → comando parametrizado `INSERT` → tabela SQLite → consultas SQL**. Essa base prepara o estudante para aprofundar modelagem relacional, chaves, relações entre tabelas e integração com sistemas de automação.
