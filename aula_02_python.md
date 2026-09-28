# Aula 2 — Sistema de alarmes industriais

## Componente curricular

**Linguagens de Programação e Banco de Dados**

## Curso

**Curso Superior de Tecnologia em Automação Industrial**

## Instituição

**Instituto Federal do Paraná — Campus Assis Chateaubriand**

## Unidade curricular

**Unidade 2 — Estruturas condicionais aplicadas ao monitoramento industrial**

## Duração

**4 horas-aula**

---

## 1. Situação-problema

O programa desenvolvido na Aula 1 recebe as leituras de um motor e gera um relatório, mas ainda não é capaz de tomar decisões.

A equipe de operação precisa que o sistema:

- Identifique se o motor está em condição normal;
- Avise quando uma variável estiver próxima do limite;
- Gere um alarme quando o limite for ultrapassado;
- Indique uma situação de emergência;
- Informe ao operador qual ação deve ser tomada.

O desafio da aula é transformar um **relatório passivo** em um **sistema que analisa as condições do processo e toma decisões**.

---

## 2. Objetivos da aula

Ao final da aula, o estudante deverá ser capaz de:

- Utilizar estruturas `if`, `elif` e `else`;
- Aplicar operadores relacionais;
- Utilizar operadores lógicos `and`, `or` e `not`;
- Criar regras de classificação;
- Desenvolver mensagens diferentes para cada estado;
- Analisar mais de uma variável de processo;
- Testar um programa com diferentes cenários;
- Evoluir o programa da Aula 1 sem reescrevê-lo completamente.

---

## 3. Produto final da aula

Ao final do encontro, cada estudante ou dupla deverá possuir um programa que:

1. Receba os dados de um motor;
2. Analise temperatura, pressão e corrente;
3. Classifique cada variável;
4. Determine o estado geral do equipamento;
5. Gere uma mensagem de orientação ao operador;
6. Informe se o motor pode continuar operando.

---

## 4. Organização da aula

| Etapa | Atividade | Tempo |
|---|---|---:|
| 1 | Retomada da Aula 1 e apresentação do problema | 20 min |
| 2 | Desafio 1 — classificar a temperatura | 30 min |
| 3 | Estrutura `if`, `elif` e `else` com mensagens | 25 min |
| 4 | Desafio 2 — classificar três variáveis | 35 min |
| 5 | Operadores lógicos e regras combinadas | 25 min |
| 6 | Desafio 3 — determinar o estado geral | 35 min |
| 7 | Intervalo ou pausa técnica | 10 min |
| 8 | Desafio 4 — ação recomendada ao operador | 35 min |
| 9 | Desafio 5 — situações inválidas e testes por cenários | 25 min |
| 10 | Desafio final curto — melhoria livre e demonstrações | 20 min |
| 11 | Fechamento e registro da aprendizagem | 20 min |
| **Total** |  | **260 min** |

---

# 5. Etapa 1 — Retomada da Aula 1

Solicite que os estudantes abram o programa `monitoramento_motor.py` desenvolvido na aula anterior e respondam:

- O que o programa calcula?
- Quais dados ele recebe?
- O programa identifica algum problema?
- O que falta para ele auxiliar o operador?
- Como o programa poderia saber que uma temperatura está perigosa?

## Problema para projetar no quadro

```text
O motor M-01 apresentou 86 °C.
O limite máximo é 80 °C.
O programa apenas exibiu o valor.

O que deveria acontecer?
```

Conduza a turma até a ideia:

```text
SE a temperatura ultrapassar o limite
ENTÃO exibir um alerta
SENÃO informar que a temperatura está dentro do limite
```

Apresente a estrutura geral:

```python
if condição:
    comando
else:
    outro_comando
```

Reforce a importância da **indentação**.

---

# 6. Desafio 1 — Classificação da temperatura

## Problema

O setor de manutenção definiu três faixas para a temperatura do motor:

| Faixa | Condição |
|---|---|
| Normal | Menor que 70 °C |
| Atenção | De 70 °C até 80 °C |
| Alarme | Acima de 80 °C |

## Código inicial

```python
if temperatura < 70:
    status_temperatura = "NORMAL"
elif temperatura <= 80:
    status_temperatura = "ATENÇÃO"
else:
    status_temperatura = "ALARME"

print(f"Status da temperatura: {status_temperatura}")
```

## Testes rápidos

Execute com: `65 °C`, `70 °C`, `80 °C`, `81 °C`.

## Perguntas rápidas

- O que acontece exatamente em `70 °C`?
- O que acontece exatamente em `80 °C`?
- Qual é a diferença entre `<` e `<=`?
- Por que a condição mais grave aparece no `else`?

> Faça uma rápida correção coletiva antes de avançar.

---

# 7. Estrutura de decisão com mensagens

```python
if temperatura < 70:
    status_temperatura = "NORMAL"
    acao_temperatura = "Manter o monitoramento."
elif temperatura <= 80:
    status_temperatura = "ATENÇÃO"
    acao_temperatura = "Verificar tendência de aumento."
else:
    status_temperatura = "ALARME"
    acao_temperatura = "Inspecionar o motor imediatamente."

print(f"Status da temperatura: {status_temperatura}")
print(f"Ação recomendada: {acao_temperatura}")
```

### Discussão

Mostre que uma condição pode determinar mais de uma informação: o estado, a mensagem e a ação recomendada.

---

# 8. Desafio 2 — Classificar temperatura, pressão e corrente

## Limites

```python
limite_temperatura = 80
limite_pressao = 8
limite_corrente = 15
```

## Temperatura

```python
if temperatura < 70:
    status_temperatura = "NORMAL"
elif temperatura <= limite_temperatura:
    status_temperatura = "ATENÇÃO"
else:
    status_temperatura = "ALARME"
```

## Pressão

Normal: menor que 7 bar | Atenção: 7 a 8 bar | Alarme: acima de 8 bar.

```python
if pressao < 7:
    status_pressao = "NORMAL"
elif pressao <= limite_pressao:
    status_pressao = "ATENÇÃO"
else:
    status_pressao = "ALARME"
```

## Corrente

Normal: menor que 13 A | Atenção: 13 a 15 A | Alarme: acima de 15 A.

```python
if corrente < 13:
    status_corrente = "NORMAL"
elif corrente <= limite_corrente:
    status_corrente = "ATENÇÃO"
else:
    status_corrente = "ALARME"
```

## Relatório parcial

```python
print()
print("STATUS DAS VARIÁVEIS")
print("------------------------------------------")
print(f"Temperatura: {status_temperatura}")
print(f"Pressão: {status_pressao}")
print(f"Corrente: {status_corrente}")
```

## Teste rápido

| Cenário | Temperatura | Pressão | Corrente |
|---|---:|---:|---:|
| 1 — Normal | 60 | 5 | 10 |
| 2 — Atenção | 75 | 7,5 | 14 |
| 3 — Alarme térmico | 85 | 5 | 10 |
| 4 — Múltiplos alarmes | 90 | 9 | 17 |

> Valores decimais devem ser digitados com ponto, por exemplo, `7.5`.

---

# 9. Operadores lógicos

```text
Quando o motor deve ser desligado imediatamente?
```

```python
if temperatura > 90:
    print("PARADA DE EMERGÊNCIA")
```

### Temperatura muito alta e corrente elevada

```python
if temperatura > 90 and corrente > 16:
    print("PARADA DE EMERGÊNCIA: sobrecarga e sobretemperatura")
```

### Pressão baixa ou temperatura muito alta

```python
if pressao < 3 or temperatura > 90:
    print("INSPEÇÃO IMEDIATA NECESSÁRIA")
```

### Equipamento ativo

```python
equipamento_ativo = True

if equipamento_ativo and temperatura > 80:
    print("Alarme com equipamento em operação")
```

## Quadro de apoio

| Operador | Significado | Exemplo |
|---|---|---|
| `and` | Todas as condições devem ser verdadeiras | `temperatura > 90 and corrente > 16` |
| `or` | Pelo menos uma condição deve ser verdadeira | `pressao < 3 or temperatura > 90` |
| `not` | Inverte o resultado lógico | `not equipamento_ativo` |

---

# 10. Desafio 3 — Determinar o estado geral do motor

## Regras

1. Situação crítica → **EMERGÊNCIA**;
2. Alguma variável em alarme → **ALARME**;
3. Alguma variável em atenção → **ATENÇÃO**;
4. Caso contrário → **NORMAL**.

## Situação crítica

```python
situacao_critica = (
    temperatura > 90
    or pressao > 10
    or corrente > 18
)
```

## Existência de alarme

```python
existe_alarme = (
    status_temperatura == "ALARME"
    or status_pressao == "ALARME"
    or status_corrente == "ALARME"
)
```

## Existência de atenção

```python
existe_atencao = (
    status_temperatura == "ATENÇÃO"
    or status_pressao == "ATENÇÃO"
    or status_corrente == "ATENÇÃO"
)
```

## Classificação do estado geral

```python
if situacao_critica:
    estado_geral = "EMERGÊNCIA"
elif existe_alarme:
    estado_geral = "ALARME"
elif existe_atencao:
    estado_geral = "ATENÇÃO"
else:
    estado_geral = "NORMAL"

print()
print(f"ESTADO GERAL DO MOTOR: {estado_geral}")
```

## Perguntas para a turma

- Por que a condição de emergência deve ser analisada primeiro?
- O que aconteceria se `ATENÇÃO` fosse verificada antes de `ALARME`?
- É possível haver temperatura normal e pressão em alarme?
- Uma variável em atenção deve necessariamente parar o motor?

---

# 11. Desafio 4 — Ação recomendada ao operador

```python
if estado_geral == "NORMAL":
    acao_recomendada = "Continuar a operação normal."
elif estado_geral == "ATENÇÃO":
    acao_recomendada = "Acompanhar as variáveis e programar inspeção."
elif estado_geral == "ALARME":
    acao_recomendada = "Verificar o equipamento e reduzir a carga."
else:
    acao_recomendada = "Parar o equipamento imediatamente."

print(f"Ação recomendada: {acao_recomendada}")
```

## Desafio adicional

```python
if estado_geral == "NORMAL" or estado_geral == "ATENÇÃO":
    pode_operar = True
else:
    pode_operar = False

if pode_operar:
    print("Operação permitida.")
else:
    print("Operação não permitida.")
```

---

# 12. Desafio 5 — Situações inválidas

```python
if temperatura < -50 or temperatura > 200:
    print("Leitura de temperatura inválida.")

if pressao < 0:
    print("Leitura de pressão inválida.")

if corrente < 0:
    print("Leitura de corrente inválida.")
```

## Questão para reflexão

O que o programa deveria fazer quando uma leitura for inválida?

- Encerrar;
- Solicitar novamente;
- Ignorar a leitura;
- Registrar uma falha.

> A repetição da entrada será tratada em uma aula posterior, com laços e validação contínua.

---

# 13. Programa-base da aula

```python
print("==========================================")
print(" SISTEMA DE MONITORAMENTO INDUSTRIAL")
print("==========================================")

codigo_equipamento = input("Código do equipamento: ")
nome_operador = input("Nome do operador: ")

temperatura = float(input("Temperatura do motor (°C): "))
pressao = float(input("Pressão do sistema (bar): "))
corrente = float(input("Corrente elétrica (A): "))
tempo_operacao = float(input("Tempo de operação (horas): "))

limite_temperatura = 80
limite_pressao = 8
limite_corrente = 15

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

# Situações críticas
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

# Estado geral
if situacao_critica:
    estado_geral = "EMERGÊNCIA"
    acao_recomendada = "Parar o equipamento imediatamente."
elif existe_alarme:
    estado_geral = "ALARME"
    acao_recomendada = "Verificar o equipamento e reduzir a carga."
elif existe_atencao:
    estado_geral = "ATENÇÃO"
    acao_recomendada = "Acompanhar as variáveis e programar inspeção."
else:
    estado_geral = "NORMAL"
    acao_recomendada = "Continuar a operação normal."

# Relatório
print()
print("==========================================")
print(" RELATÓRIO DE MONITORAMENTO")
print("==========================================")
print(f"Equipamento: {codigo_equipamento}")
print(f"Operador: {nome_operador}")
print("------------------------------------------")
print(f"Temperatura: {temperatura:.2f} °C")
print(f"Status da temperatura: {status_temperatura}")
print(f"Pressão: {pressao:.2f} bar")
print(f"Status da pressão: {status_pressao}")
print(f"Corrente: {corrente:.2f} A")
print(f"Status da corrente: {status_corrente}")
print("------------------------------------------")
print(f"Estado geral: {estado_geral}")
print(f"Ação recomendada: {acao_recomendada}")

# Variáveis em alarme
print()
print("VARIÁVEIS EM ALARME")
print("------------------------------------------")

houve_alarme_individual = False

if status_temperatura == "ALARME":
    print("- Temperatura")
    houve_alarme_individual = True

if status_pressao == "ALARME":
    print("- Pressão")
    houve_alarme_individual = True

if status_corrente == "ALARME":
    print("- Corrente")
    houve_alarme_individual = True

if not houve_alarme_individual:
    print("Nenhuma variável em alarme.")

print("==========================================")
```

---

# 14. Testes por cenários

## Cenário 1 — Operação normal

```text
Temperatura: 60
Pressão: 5
Corrente: 10
```

Resultado esperado: `Estado geral: NORMAL`

## Cenário 2 — Situação de atenção

```text
Temperatura: 75
Pressão: 7.5
Corrente: 14
```

Resultado esperado: `Estado geral: ATENÇÃO`

## Cenário 3 — Alarme de temperatura

```text
Temperatura: 85
Pressão: 5
Corrente: 10
```

Resultado esperado: `Estado geral: ALARME`

## Cenário 4 — Emergência

```text
Temperatura: 95
Pressão: 6
Corrente: 12
```

Resultado esperado: `Estado geral: EMERGÊNCIA`

## Cenário 5 — Múltiplos alarmes

```text
Temperatura: 92
Pressão: 11
Corrente: 19
```

Resultado esperado: `Estado geral: EMERGÊNCIA`

---

# 15. Entrega da atividade

Cada estudante ou dupla deverá entregar:

- Arquivo `monitoramento_motor.py` atualizado;
- Resultados de pelo menos os cinco cenários testados;
- Breve explicação das regras de classificação;
- Lista de melhorias implementadas durante a aula.

---

# 16. Critérios de avaliação

| Critério | Pontuação |
|---|---:|
| Classificação correta das três variáveis | 2,5 |
| Uso adequado de `if`, `elif`, `else` | 2,0 |
| Uso adequado de operadores lógicos | 2,0 |
| Determinação correta do estado geral | 1,5 |
| Testes e explicação da solução | 1,0 |
| Organização e clareza do código | 1,0 |
| **Total** | **10,0** |

---

# 17. Fechamento da aula

Discuta com a turma:

1. Qual foi a diferença entre `if`, `elif` e `else`?
2. Qual é a finalidade dos operadores `and` e `or`?
3. Por que as emergências devem ser verificadas antes das situações normais?
4. Qual foi o cenário mais difícil de testar?
5. Que tipo de informação seria importante registrar em um banco de dados?
6. Como um sensor real poderia enviar esses valores automaticamente ao programa?

## Registro de saída

Cada estudante deverá entregar ou salvar:

- A versão atualizada do programa;
- Os resultados de pelo menos quatro cenários;
- Uma breve explicação das regras de classificação;
- A lista de melhorias implementadas durante a aula.

As perguntas finais preparam a próxima unidade da disciplina: **estruturas de repetição e simulação de ciclos de coleta de dados**.