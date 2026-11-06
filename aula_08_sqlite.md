# Aula 8 — Análise de dados com SQL no SQLiteOnline

**Tema:** filtros combinados, agrupamentos e consultas analíticas  
**Curso:** Linguagens de Programação e Banco de Dados — Tecnologia em Automação Industrial  
**Instituição:** Instituto Federal do Paraná — Campus Assis Chateaubriand  
**Duração sugerida:** 2 a 3 horas  
**Ferramenta:** [SQLiteOnline](https://sqliteonline.com/)  
**Base de dados:** `historico_leituras.csv` (19 leituras válidas)

## 1. Contexto e conexão com a Aula 7

Na Aula 7, a turma criou uma tabela, inseriu leituras e praticou comandos `SELECT`, filtros simples com `WHERE`, ordenação com `ORDER BY` e algumas funções como `COUNT`, `AVG`, `MIN` e `MAX`. Nesta aula, vamos combinar condições e resumir os dados para responder perguntas operacionais sobre o equipamento **M-01**.

O arquivo CSV usa ponto e vírgula como separador. Ele contém **19 registros válidos**; o ciclo 5 não aparece porque a coleta foi ignorada por falha de comunicação. A atividade mantém os números de ciclo originais.

## 2. Objetivos de aprendizagem

Ao final da atividade, você deverá ser capaz de:

- combinar condições usando `AND` e `OR`;
- filtrar valores em listas e intervalos com `IN` e `BETWEEN`;
- agrupar registros com `GROUP BY`;
- filtrar grupos com `HAVING`;
- limitar resultados com `LIMIT`;
- produzir resumos por estado e por turno;
- interpretar resultados SQL no contexto da automação industrial.

## 3. Preparação no SQLiteOnline

Abra o [SQLiteOnline](https://sqliteonline.com/) e selecione o mecanismo SQLite. Se ainda tiver a tabela da Aula 7 com os registros, continue nela e **não execute novamente a carga**, para evitar duplicatas.

Se precisar começar uma base de exercício do zero, execute o bloco abaixo uma única vez. **Atenção:** `DROP TABLE` apaga a tabela `leituras` existente e seus dados; use-o apenas quando puder reiniciar a atividade.

```sql
-- Use em uma base vazia de exercícios.
-- Se já tiver dados que deseja preservar, não execute DROP TABLE.
DROP TABLE IF EXISTS leituras;

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
    situacao_critica INTEGER NOT NULL CHECK (situacao_critica IN (0, 1)),
    data TEXT,
    horario TEXT,
    operador TEXT,
    turno TEXT,
    observacao TEXT
);

INSERT INTO leituras (ciclo, equipamento, dispositivo, temperatura, pressao, corrente, status_temperatura, status_pressao, status_corrente, estado_geral, situacao_critica, data, horario, operador, turno, observacao)
VALUES
(1, 'M-01', 'CLP-SIM-01', 85.25, 6.24, 11.2, 'ALARME', 'NORMAL', 'NORMAL', 'ALARME', 0, '2026-10-02', '19:48:33', 'Operador 01', 'A', 'Coleta automática'),
(2, 'M-01', 'CLP-SIM-01', 93.72, 5.04, 17.63, 'ALARME', 'NORMAL', 'ALARME', 'EMERGÊNCIA', 1, '2026-10-02', '19:50:22', 'Operador 01', 'A', 'Coleta automática'),
(3, 'M-01', 'CLP-SIM-01', 62.68, 7.58, 11.38, 'NORMAL', 'ATENÇÃO', 'NORMAL', 'ATENÇÃO', 0, '2026-10-02', '19:50:25', 'Operador 01', 'A', 'Coleta automática'),
(4, 'M-01', 'CLP-SIM-01', 64.65, 7.09, 15.97, 'NORMAL', 'ATENÇÃO', 'ALARME', 'ALARME', 0, '2026-10-02', '19:50:28', 'Operador 01', 'A', 'Coleta automática'),
(6, 'M-01', 'CLP-SIM-01', 81.7, 7.58, 13.35, 'ALARME', 'ATENÇÃO', 'ATENÇÃO', 'ALARME', 0, '2026-10-02', '19:50:50', 'Operador 01', 'A', 'Coleta automática'),
(7, 'M-01', 'CLP-SIM-01', 64.6, 9.0, 16.99, 'NORMAL', 'ALARME', 'ALARME', 'ALARME', 0, '2026-10-02', '19:51:03', 'Operador 01', 'A', 'Coleta automática'),
(8, 'M-01', 'CLP-SIM-01', 83.84, 7.73, 19.0, 'ALARME', 'ATENÇÃO', 'ALARME', 'EMERGÊNCIA', 1, '2026-10-02', '19:51:03', 'Operador 01', 'A', 'Coleta automática'),
(9, 'M-01', 'CLP-SIM-01', 83.24, 6.41, 19.51, 'ALARME', 'NORMAL', 'ALARME', 'EMERGÊNCIA', 1, '2026-10-02', '19:51:03', 'Operador 01', 'A', 'Coleta automática'),
(10, 'M-01', 'CLP-SIM-01', 81.08, 9.29, 16.77, 'ALARME', 'ALARME', 'ALARME', 'ALARME', 0, '2026-10-02', '19:51:03', 'Operador 01', 'A', 'Coleta automática'),
(11, 'M-01', 'CLP-SIM-01', 62.96, 5.18, 19.36, 'NORMAL', 'NORMAL', 'ALARME', 'EMERGÊNCIA', 1, '2026-10-02', '19:51:03', 'Operador 01', 'A', 'Coleta automática'),
(12, 'M-01', 'CLP-SIM-01', 81.95, 9.96, 11.72, 'ALARME', 'ALARME', 'NORMAL', 'ALARME', 0, '2026-10-02', '19:51:03', 'Operador 01', 'A', 'Coleta automática'),
(13, 'M-01', 'CLP-SIM-01', 69.52, 5.95, 19.89, 'NORMAL', 'NORMAL', 'ALARME', 'EMERGÊNCIA', 1, '2026-10-02', '19:51:03', 'Operador 01', 'A', 'Coleta automática'),
(14, 'M-01', 'CLP-SIM-01', 91.48, 8.64, 16.32, 'ALARME', 'ALARME', 'ALARME', 'EMERGÊNCIA', 1, '2026-10-02', '19:51:03', 'Operador 01', 'A', 'Coleta automática'),
(15, 'M-01', 'CLP-SIM-01', 65.94, 7.27, 11.03, 'NORMAL', 'ATENÇÃO', 'NORMAL', 'ATENÇÃO', 0, '2026-10-02', '19:51:03', 'Operador 01', 'A', 'Coleta automática'),
(16, 'M-01', 'CLP-SIM-01', 66.01, 7.6, 18.19, 'NORMAL', 'ATENÇÃO', 'ALARME', 'EMERGÊNCIA', 1, '2026-10-02', '19:51:03', 'Operador 01', 'A', 'Coleta automática'),
(17, 'M-01', 'CLP-SIM-01', 89.7, 5.74, 12.93, 'ALARME', 'NORMAL', 'NORMAL', 'ALARME', 0, '2026-10-02', '19:51:03', 'Operador 01', 'A', 'Coleta automática'),
(18, 'M-01', 'CLP-SIM-01', 67.18, 9.15, 19.6, 'NORMAL', 'ALARME', 'ALARME', 'EMERGÊNCIA', 1, '2026-10-02', '19:51:03', 'Operador 01', 'A', 'Coleta automática'),
(19, 'M-01', 'CLP-SIM-01', 67.19, 7.23, 14.33, 'NORMAL', 'ATENÇÃO', 'ATENÇÃO', 'ATENÇÃO', 0, '2026-10-02', '19:51:03', 'Operador 01', 'A', 'Coleta automática'),
(20, 'M-01', 'CLP-SIM-01', 65.95, 9.15, 12.95, 'NORMAL', 'ALARME', 'NORMAL', 'ALARME', 0, '2026-10-02', '19:51:03', 'Operador 01', 'A', 'Coleta automática');
```


Confirme a carga:

```sql
SELECT COUNT(*) AS total_registros
FROM leituras;
```

O resultado esperado, usando todos os dados do CSV, é **19**. A coluna `situacao_critica` representa falso como `0` e verdadeiro como `1`.

## 4. Revisão rápida

```sql
-- Escolher colunas
SELECT ciclo, temperatura, estado_geral
FROM leituras;

-- Filtrar e ordenar
SELECT ciclo, temperatura
FROM leituras
WHERE temperatura > 80
ORDER BY temperatura DESC;
```

Lembrete: `WHERE` filtra linhas antes de qualquer agrupamento; `ORDER BY` organiza as linhas do resultado.

## 5. Novos recursos SQL

### 5.1 Combinar condições com AND

`AND` exige que **todas** as condições sejam verdadeiras.

```sql
SELECT ciclo, temperatura, corrente, estado_geral
FROM leituras
WHERE temperatura > 80
  AND corrente > 15
ORDER BY temperatura DESC;
```

A consulta encontra leituras acima dos dois limites ao mesmo tempo.

### 5.2 Combinar alternativas com OR

`OR` aceita registros que atendam a **pelo menos uma** condição. Use parênteses para deixar clara a lógica quando misturar `AND` e `OR`.

```sql
SELECT ciclo, estado_geral, situacao_critica
FROM leituras
WHERE estado_geral = 'ALARME'
   OR estado_geral = 'EMERGÊNCIA'
ORDER BY ciclo;
```

Forma equivalente e mais compacta para os estados:

```sql
SELECT ciclo, estado_geral
FROM leituras
WHERE estado_geral IN ('ALARME', 'EMERGÊNCIA')
ORDER BY ciclo;
```

### 5.3 Filtrar intervalos com BETWEEN

`BETWEEN` inclui os dois extremos do intervalo.

```sql
SELECT ciclo, pressao
FROM leituras
WHERE pressao BETWEEN 7 AND 8
ORDER BY pressao;
```

Esse exemplo inclui valores iguais a `7` e a `8`, caso existam.

### 5.4 Agrupar com GROUP BY

`GROUP BY` reúne registros que têm o mesmo valor em uma coluna. É comum usá-lo com `COUNT`, `AVG`, `MIN` e `MAX`.

```sql
SELECT estado_geral, COUNT(*) AS quantidade
FROM leituras
GROUP BY estado_geral
ORDER BY quantidade DESC;
```

O resultado terá uma linha por estado geral. `COUNT(*)` conta quantas leituras estão em cada grupo.

### 5.5 Filtrar grupos com HAVING

`WHERE` filtra registros individuais; `HAVING` filtra os grupos produzidos por `GROUP BY`.

```sql
SELECT estado_geral, COUNT(*) AS quantidade
FROM leituras
GROUP BY estado_geral
HAVING COUNT(*) >= 5
ORDER BY quantidade DESC;
```

A consulta exibe somente os estados com cinco ou mais registros.

### 5.6 Mostrar somente os primeiros resultados com LIMIT

```sql
SELECT ciclo, corrente
FROM leituras
ORDER BY corrente DESC
LIMIT 3;
```

`LIMIT 3` restringe a saída às três primeiras linhas após a ordenação.

## 6. Atividade guiada

Execute cada consulta e registre brevemente o que o resultado informa.

### Parte A — Filtros combinados

1. Liste ciclo, temperatura e corrente quando a temperatura for maior que `80` **e** a corrente maior que `15`.
2. Liste as leituras cujo estado geral seja `ALARME` ou `EMERGÊNCIA`, em ordem de ciclo.
3. Consulte leituras em que a pressão esteja entre `7` e `8` bar, incluindo os extremos.
4. Liste registros com `situacao_critica = 1` e mostre ciclo, estado e valores dos três sensores.
5. Escreva uma consulta para leituras com temperatura abaixo de `70` **ou** pressão acima de `9` bar. Ordene pelo ciclo.

### Parte B — Resumos e agrupamentos

6. Conte quantas leituras existem em cada estado geral. Ordene da maior quantidade para a menor.
7. Calcule temperatura média, mínima e máxima para cada estado geral.
8. Conte quantas leituras críticas existem (`situacao_critica = 1`) para cada estado geral.
9. Exiba somente os estados que aparecem em pelo menos cinco registros, usando `HAVING`.
10. Calcule média, mínimo e máximo de corrente por estado geral.

### Parte C — Ranking de leituras

11. Mostre as três maiores temperaturas, com os respectivos ciclos.
12. Mostre os dois ciclos com maior pressão.
13. Mostre as cinco maiores correntes, da maior para a menor.
14. Em cada consulta, selecione apenas as colunas necessárias e atribua nomes legíveis às estatísticas com `AS`.

## 7. Desafio de análise operacional

A equipe de manutenção quer priorizar a investigação do equipamento. Escreva consultas SQL para responder:

1. Quantas leituras em `EMERGÊNCIA` ocorreram?
2. Qual ciclo teve a maior temperatura? Qual foi o valor?
3. Qual ciclo teve a maior pressão?
4. Qual ciclo teve a maior corrente?
5. Qual é a temperatura média das leituras classificadas como `NORMAL`?
6. Quantas leituras tiveram pressão acima de `8` bar **ou** corrente acima de `18` A?
7. Há leituras críticas que não estejam classificadas como `EMERGÊNCIA`? Escreva a consulta e interprete o resultado.

**Dica para agrupar por estado:** selecione o campo do agrupamento e as funções de agregação; os campos selecionados que não forem agregados devem aparecer no `GROUP BY`.

## 8. Perguntas de análise

1. Qual é a diferença entre `WHERE` e `HAVING`?
2. O que muda entre combinar condições com `AND` e com `OR`?
3. Por que parênteses podem ser importantes ao misturar `AND` e `OR`?
4. `BETWEEN 7 AND 8` inclui os valores 7 e 8?
5. Qual é a função de `GROUP BY`?
6. O que significa ordenar por uma quantidade usando `ORDER BY quantidade DESC`?
7. Para que serve `LIMIT`? Por que a ordenação é importante antes de limitar um ranking?
8. O ciclo 5 deve ser criado artificialmente para completar a sequência? Justifique com base no contexto da falha de comunicação.
9. Como esses resumos poderiam ajudar uma equipe de manutenção industrial?

## 9. Conferência dos resultados — dados completos

Os valores abaixo servem para conferência quando a tabela contém os **19 registros do CSV**. Diferenças podem ocorrer se a turma inseriu apenas parte dos registros.

| Verificação | Resultado esperado |
|---|---:|
| Total de registros | 19 |
| Leituras por estado: `ALARME` | 8 |
| Leituras por estado: `EMERGÊNCIA` | 8 |
| Leituras por estado: `ATENÇÃO` | 3 |
| Leituras por estado: `NORMAL` | 0 |
| Leituras críticas (`situacao_critica = 1`) | 8 |
| Maior temperatura | 93,72 °C — ciclo 2 |
| Maior pressão | 9,96 bar — ciclo 12 |
| Maior corrente | 19,89 A — ciclo 13 |

A conferência serve para identificar erros de digitação e compreender o resultado; o foco é escrever e interpretar as consultas, não apenas chegar ao número.

## 10. Entrega

Cada estudante ou dupla deverá apresentar:

- as consultas SQL das partes A, B e C;
- os resultados das sete perguntas do desafio operacional;
- respostas às perguntas de análise;
- uma breve interpretação de pelo menos dois resultados relevantes para a manutenção;
- evidência das consultas executadas no SQLiteOnline, conforme orientação do professor.

## 11. Critérios de avaliação

| Critério | Pontuação |
|---|---:|
| Uso correto de `AND`, `OR`, `IN` e `BETWEEN` | 2,0 |
| Consultas com `GROUP BY` e funções de agregação | 2,0 |
| Uso correto de `HAVING` e diferença em relação a `WHERE` | 1,5 |
| Ordenação e rankings com `ORDER BY` e `LIMIT` | 1,5 |
| Respostas e interpretação dos resultados | 2,0 |
| Organização e clareza da entrega | 1,0 |
| **Total** | **10,0** |

## 12. Fechamento

Na Aula 7, foram praticadas a criação de tabela, a inserção e as consultas iniciais. Nesta Aula 8, as consultas passam a combinar condições e produzir resumos por grupos, aproximando o SQL de perguntas reais de monitoramento e manutenção industrial.
