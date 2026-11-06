# Aula 7 — Atividade prática: SQL com SQLiteOnline

**Tema:** criação de tabela, inserção e consulta de dados de um simulador industrial  
**Ferramenta:** [SQLiteOnline](https://sqliteonline.com/)  
**Base da atividade:** arquivo `historico_leituras.csv`

## Objetivos

Ao concluir a atividade, você deverá ser capaz de:

- criar uma tabela usando `CREATE TABLE`;
- reconhecer tipos de dados usados pelo SQLite;
- inserir registros com `INSERT INTO`;
- consultar dados com `SELECT` e filtrar com `WHERE`;
- ordenar resultados com `ORDER BY`;
- calcular contagens e estatísticas básicas;
- relacionar os registros da tabela aos dados do CSV.

## Contexto dos dados

O CSV registra leituras do equipamento **M-01**, coletadas pelo dispositivo **CLP-SIM-01**. Cada linha representa um ciclo de coleta, com valores de temperatura, pressão e corrente, classificações dos sensores e informações operacionais.

O arquivo possui **16 colunas** e usa ponto e vírgula (`;`) como separador. O ciclo 5 não aparece porque a leitura foi ignorada por uma falha de comunicação; os números de ciclo originais devem ser preservados.

## 1. Campos e tipos sugeridos

| Campo | Tipo SQLite | Para que serve / exemplo |
|---|---|---|
| `id` | `INTEGER` | Identificador único criado pela tabela |
| `ciclo` | `INTEGER` | Número original do ciclo, por exemplo `1` |
| `equipamento` | `TEXT` | Código do equipamento, por exemplo `M-01` |
| `dispositivo` | `TEXT` | Identificação do dispositivo, por exemplo `CLP-SIM-01` |
| `temperatura` | `REAL` | Temperatura em °C, por exemplo `85.25` |
| `pressao` | `REAL` | Pressão em bar, por exemplo `6.24` |
| `corrente` | `REAL` | Corrente em A, por exemplo `11.2` |
| `status_temperatura` | `TEXT` | Classificação da temperatura: `NORMAL`, `ATENÇÃO` ou `ALARME` |
| `status_pressao` | `TEXT` | Classificação da pressão |
| `status_corrente` | `TEXT` | Classificação da corrente |
| `estado_geral` | `TEXT` | Estado consolidado, como `NORMAL`, `ATENÇÃO`, `ALARME` ou `EMERGÊNCIA` |
| `situacao_critica` | `INTEGER` | Indicador lógico: `0` para falso e `1` para verdadeiro |
| `data` | `TEXT` | Data no formato `AAAA-MM-DD` |
| `horario` | `TEXT` | Horário no formato `HH:MM:SS` |
| `operador` | `TEXT` | Nome ou identificação do operador |
| `turno` | `TEXT` | Turno de trabalho, por exemplo `A` |
| `observacao` | `TEXT` | Observação da coleta |

> **Observação sobre os tipos:** SQLite usa tipagem dinâmica. Nesta atividade, `INTEGER` será usado para números inteiros e valores lógicos `0`/`1`, `REAL` para números com casas decimais e `TEXT` para textos. Data e horário serão armazenados como texto em formatos padronizados.

## 2. Criar a tabela

Abra o [SQLiteOnline](https://sqliteonline.com/), selecione SQLite e execute:

```sql
CREATE TABLE leituras (
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
        CHECK (situacao_critica IN (0, 1)),
    data TEXT,
    horario TEXT,
    operador TEXT,
    turno TEXT,
    observacao TEXT
);
```

O campo `id` é gerado automaticamente pelo SQLite. O campo `ciclo` guarda o número original da coleta, por isso não deve ser renumerado para preencher o ciclo ausente.

## 3. Inserir registros

Insira os registros abaixo. Eles correspondem a linhas reais do CSV. Para cada inserção, não é necessário informar o campo `id`.

```sql
INSERT INTO leituras (
    ciclo, equipamento, dispositivo,
    temperatura, pressao, corrente,
    status_temperatura, status_pressao,
    status_corrente, estado_geral,
    situacao_critica, data, horario,
    operador, turno, observacao
)
VALUES (
    1, 'M-01', 'CLP-SIM-01',
    85.25, 6.24, 11.2,
    'ALARME', 'NORMAL', 'NORMAL', 'ALARME',
    0, '2026-10-02', '19:48:33',
    'Operador 01', 'A', 'Coleta automática'
);

INSERT INTO leituras (
    ciclo, equipamento, dispositivo,
    temperatura, pressao, corrente,
    status_temperatura, status_pressao,
    status_corrente, estado_geral,
    situacao_critica, data, horario,
    operador, turno, observacao
)
VALUES (
    2, 'M-01', 'CLP-SIM-01',
    93.72, 5.04, 17.63,
    'ALARME', 'NORMAL', 'ALARME', 'EMERGÊNCIA',
    1, '2026-10-02', '19:50:22',
    'Operador 01', 'A', 'Coleta automática'
);

INSERT INTO leituras (
    ciclo, equipamento, dispositivo,
    temperatura, pressao, corrente,
    status_temperatura, status_pressao,
    status_corrente, estado_geral,
    situacao_critica, data, horario,
    operador, turno, observacao
)
VALUES (
    3, 'M-01', 'CLP-SIM-01',
    62.68, 7.58, 11.38,
    'NORMAL', 'ATENÇÃO', 'NORMAL', 'ATENÇÃO',
    0, '2026-10-02', '19:50:25',
    'Operador 01', 'A', 'Coleta automática'
);

INSERT INTO leituras (
    ciclo, equipamento, dispositivo,
    temperatura, pressao, corrente,
    status_temperatura, status_pressao,
    status_corrente, estado_geral,
    situacao_critica, data, horario,
    operador, turno, observacao
)
VALUES (
    4, 'M-01', 'CLP-SIM-01',
    64.65, 7.09, 15.97,
    'NORMAL', 'ATENÇÃO', 'ALARME', 'ALARME',
    0, '2026-10-02', '19:50:28',
    'Operador 01', 'A', 'Coleta automática'
);

INSERT INTO leituras (
    ciclo, equipamento, dispositivo,
    temperatura, pressao, corrente,
    status_temperatura, status_pressao,
    status_corrente, estado_geral,
    situacao_critica, data, horario,
    operador, turno, observacao
)
VALUES (
    6, 'M-01', 'CLP-SIM-01',
    81.7, 7.58, 13.35,
    'ALARME', 'ATENÇÃO', 'ATENÇÃO', 'ALARME',
    0, '2026-10-02', '19:50:50',
    'Operador 01', 'A', 'Coleta automática'
);
```

Na coluna `situacao_critica`, o CSV apresenta `True` e `False`. Ao inserir no SQLite, use `1` para `True` e `0` para `False`, sem aspas.

**Tarefa:** após executar os cinco comandos, confirme que há cinco registros. Se houver tempo, escolha e insira mais linhas do CSV, mantendo os valores e números de ciclo originais.

## 4. Consultas guiadas

Execute cada consulta e observe o resultado.

### 4.1 Exibir todos os registros

```sql
SELECT * FROM leituras;
```

### 4.2 Selecionar apenas algumas colunas

```sql
SELECT ciclo, temperatura, estado_geral
FROM leituras;
```

### 4.3 Consultar leituras em emergência

```sql
SELECT ciclo, temperatura, pressao, corrente, estado_geral
FROM leituras
WHERE estado_geral = 'EMERGÊNCIA';
```

### 4.4 Consultar temperaturas acima de 80 °C

```sql
SELECT ciclo, temperatura
FROM leituras
WHERE temperatura > 80;
```

### 4.5 Ordenar da maior para a menor temperatura

```sql
SELECT ciclo, temperatura
FROM leituras
ORDER BY temperatura DESC;
```

### 4.6 Contar quantos registros foram inseridos

```sql
SELECT COUNT(*) AS total_leituras
FROM leituras;
```

### 4.7 Calcular média, mínimo e máximo da temperatura

```sql
SELECT
    AVG(temperatura) AS temperatura_media,
    MIN(temperatura) AS temperatura_minima,
    MAX(temperatura) AS temperatura_maxima
FROM leituras;
```

## 5. Desafios

Escreva e execute uma consulta SQL para cada desafio:

1. Exibir somente as leituras cujo estado geral seja `ALARME`.
2. Exibir ciclo e pressão para leituras com pressão maior que `8` bar.
3. Exibir ciclo e corrente para leituras com corrente maior que `15` A.
4. Exibir registros em que `situacao_critica` seja igual a `1`.
5. Contar quantas leituras estão em cada estado geral.
6. Exibir as três leituras com maior corrente. **Dica:** use `ORDER BY` e `LIMIT`.
7. Consultar leituras do equipamento `M-01` que estejam em `EMERGÊNCIA`.
8. Verificar qual número de ciclo não está presente entre os registros fornecidos no CSV e explicar por quê.

## 6. Perguntas para responder

1. Para que serve o campo `id`? Qual é a diferença entre ele e o campo `ciclo`?
2. Por que `temperatura`, `pressao` e `corrente` foram definidos como `REAL`?
3. Por que os campos `data` e `horario` foram definidos como `TEXT` nesta atividade?
4. O que a cláusula `WHERE` faz?
5. O que significa `ORDER BY temperatura DESC`?
6. Como a consulta identifica somente as leituras em emergência?
7. Como representar `True` e `False` na coluna `situacao_critica`?
8. Por que o ciclo 5 não deve ser inventado ou usado para renumerar os demais registros?
9. Qual é a diferença entre selecionar todas as colunas com `SELECT *` e indicar colunas específicas?

## 7. Entrega

Cada estudante ou dupla deverá apresentar:

- a tabela `leituras` criada no SQLiteOnline;
- pelo menos cinco registros inseridos com os dados correspondentes ao CSV;
- resultado das consultas guiadas;
- respostas aos desafios e às perguntas de análise;
- uma breve explicação sobre a utilidade dos campos `id` e `ciclo`.

## 8. Critérios de avaliação

| Critério | Pontuação |
|---|---:|
| Criação correta da tabela e definição dos campos | 2,0 |
| Inserção dos dados sem alterar os valores do CSV | 2,0 |
| Execução e compreensão das consultas guiadas | 2,0 |
| Resolução dos desafios com SQL | 2,0 |
| Respostas às perguntas e organização da entrega | 2,0 |
| **Total** | **10,0** |

## Fechamento

Nesta atividade, os dados que antes estavam organizados em um arquivo CSV foram representados em uma tabela SQLite. Os comandos `CREATE TABLE`, `INSERT INTO` e `SELECT` são uma introdução à persistência estruturada e às consultas em banco de dados relacionais.
