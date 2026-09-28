# Aula 1 — Da lógica em C para Python

## Componente curricular

**Linguagens de Programação e Banco de Dados**

## Curso

**Curso Superior de Tecnologia em Automação Industrial**

## Instituição

**Instituto Federal do Paraná — Campus Assis Chateaubriand**

## Unidade curricular

**Unidade 1 — Da lógica em C para Python**

## Duração

**4 horas-aula**

---

## 1. Contextualização

O componente curricular **Linguagens de Programação e Banco de Dados** possui carga horária de 80 horas-aula, distribuídas em 20 unidades de 4 horas-aula.

A ementa prevê:

- Desenvolvimento de algoritmos;
- Programação orientada a objetos;
- Bancos de dados relacionais;
- Modelagem e manipulação de dados utilizando SQL;
- Bancos de dados de séries temporais;
- Aplicações em sistemas industriais de controle e automação.

Os estudantes já tiveram contato com lógica de programação e linguagem C no componente **Algoritmos de Programação**. Portanto, esta primeira aula propõe uma revisão prática desses conceitos utilizando Python, destacando semelhanças e diferenças entre as linguagens.

---

## 2. Situação-problema

Uma indústria deseja iniciar o monitoramento de um motor elétrico identificado como **M-01**.

Durante a operação, um dispositivo de coleta recebe informações de três sensores:

- Temperatura do motor;
- Pressão do sistema de lubrificação;
- Corrente elétrica consumida.

Neste primeiro momento, o sistema ainda não terá banco de dados nem interface gráfica. As informações serão digitadas pelo operador e processadas pelo programa.

O objetivo é criar, em Python, um programa que apresente um **relatório inicial da condição de operação do motor**.

---

## 3. Objetivos da atividade

Ao final da atividade, o estudante deverá ser capaz de:

- Reconhecer a correspondência entre estruturas básicas de C e Python;
- Criar um programa simples em Python;
- Utilizar variáveis;
- Identificar tipos de dados;
- Receber dados com `input()`;
- Exibir resultados com `print()`;
- Converter dados de texto para números;
- Utilizar operadores aritméticos;
- Realizar cálculos relacionados a uma situação industrial;
- Organizar um relatório textual de uma leitura de processo.

---

## 4. Organização da aula

| Etapa | Atividade | Tempo sugerido |
|---|---|---:|
| 1 | Apresentação do problema e diagnóstico da turma | 20 min |
| 2 | Comparação entre C e Python | 30 min |
| 3 | Desenvolvimento orientado | 60 min |
| 4 | Implementação individual ou em duplas | 80 min |
| 5 | Desafios progressivos | 40 min |
| 6 | Testes, demonstrações e fechamento | 30 min |
| **Total** |  | **260 min** |

O tempo corresponde a aproximadamente **4 horas-aula de 50 minutos**.

---

# 5. Etapa 1 — Identificação do problema

Antes de programar, analise a situação apresentada.

O programa deverá receber informações do operador, realizar cálculos e produzir um relatório.

## 5.1 Entradas, processamentos e saídas

Preencha a tabela:

| Tipo | Informação |
|---|---|
| Entrada | |
| Entrada | |
| Entrada | |
| Entrada | |
| Entrada | |
| Entrada | |
| Processamento | |
| Processamento | |
| Processamento | |
| Saída | |
| Saída | |
| Saída | |

## 5.2 Questões para discussão

1. Quais dados deverão ser armazenados como texto?
2. Quais dados deverão ser armazenados como números?
3. O código do equipamento poderia ser armazenado como número? Justifique.
4. Qual é a diferença entre `220` e `"220"` em Python?
5. Quais informações são digitadas pelo operador?
6. Quais informações são calculadas pelo programa?
7. Que dados poderiam ser armazenados futuramente em um banco de dados?

---

# 6. Etapa 2 — Comparação entre C e Python

Considere o seguinte trecho em C:

```c
float temperatura;

printf("Digite a temperatura: ");
scanf("%f", &temperatura);

printf("Temperatura registrada: %.2f", temperatura);
```

Uma versão equivalente em Python é:

```python
temperatura = float(input("Digite a temperatura: "))

print(f"Temperatura registrada: {temperatura:.2f} °C")
```

## 6.1 Comparação

| Aspecto | Linguagem C | Python |
|---|---|---|
| Declaração de variável | `float temperatura;` | `temperatura = 0.0` |
| Entrada de dados | `scanf()` | `input()` |
| Saída de dados | `printf()` | `print()` |
| Conversão de entrada | Definida no formato do `scanf()` | Realizada com `int()` ou `float()` |
| Final da instrução | Geralmente utiliza `;` | Não utiliza `;` obrigatoriamente |
| Blocos de código | Delimitados por chaves | Definidos por indentação |
| Tipagem | Declaração explícita | Tipagem dinâmica |

## 6.2 Questões

Responda:

1. Por que foi utilizada a função `float()`?
2. O que aconteceria se o valor digitado não fosse convertido?
3. Qual é a finalidade de `:.2f`?
4. Qual é a principal diferença entre a estrutura de blocos de C e Python?
5. Qual linguagem apresentou menor quantidade de código nesse exemplo?

---

# 7. Etapa 3 — Desenvolvimento do programa

Crie um arquivo chamado:

```text
monitoramento_motor.py
```

Inicie o programa com:

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
```

---

## 7.1 Conversão de temperatura

Converta a temperatura de graus Celsius para Fahrenheit:

$$
F = (C \times 1,8) + 32
$$

Em Python:

```python
temperatura_fahrenheit = (temperatura * 1.8) + 32
```

---

## 7.2 Cálculo da potência estimada

Considere a tensão fixa de 220 V.

$$
P = V \times I
$$

Em Python:

```python
tensao = 220
potencia_estimada = tensao * corrente
```

> Este é um cálculo simplificado utilizado apenas para fins didáticos. Em aplicações reais, outros fatores devem ser considerados, como fator de potência, rendimento e sistema monofásico ou trifásico.

---

## 7.3 Cálculo da energia estimada

Utilize a fórmula:

$$
E = P \times t
$$

Em Python:

```python
energia_estimada = potencia_estimada * tempo_operacao
```

---

## 7.4 Cálculo da média numérica

Para praticar operações aritméticas, calcule a média simples dos valores informados:

```python
media_medicoes = (temperatura + pressao + corrente) / 3
```

> A média possui finalidade didática, pois temperatura, pressão e corrente são grandezas diferentes e não devem ser comparadas diretamente em uma análise física real.

---

# 8. Etapa 4 — Geração do relatório

Ao final do programa, apresente um relatório organizado:

```python
print()
print("==========================================")
print(" RELATÓRIO DE MONITORAMENTO")
print("==========================================")
print(f"Equipamento: {codigo_equipamento}")
print(f"Operador: {nome_operador}")
print("------------------------------------------")
print(f"Temperatura: {temperatura:.2f} °C")
print(f"Temperatura: {temperatura_fahrenheit:.2f} °F")
print(f"Pressão: {pressao:.2f} bar")
print(f"Corrente: {corrente:.2f} A")
print(f"Potência estimada: {potencia_estimada:.2f} W")
print(f"Tempo de operação: {tempo_operacao:.2f} h")
print(f"Energia estimada: {energia_estimada:.2f} Wh")
print(f"Média numérica das medições: {media_medicoes:.2f}")
print("==========================================")
```

---

# 9. Programa completo de referência

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

temperatura_fahrenheit = (temperatura * 1.8) + 32

tensao = 220
potencia_estimada = tensao * corrente

energia_estimada = potencia_estimada * tempo_operacao

media_medicoes = (temperatura + pressao + corrente) / 3

print()
print("==========================================")
print(" RELATÓRIO DE MONITORAMENTO")
print("==========================================")
print(f"Equipamento: {codigo_equipamento}")
print(f"Operador: {nome_operador}")
print("------------------------------------------")
print(f"Temperatura: {temperatura:.2f} °C")
print(f"Temperatura: {temperatura_fahrenheit:.2f} °F")
print(f"Pressão: {pressao:.2f} bar")
print(f"Corrente: {corrente:.2f} A")
print(f"Potência estimada: {potencia_estimada:.2f} W")
print(f"Tempo de operação: {tempo_operacao:.2f} h")
print(f"Energia estimada: {energia_estimada:.2f} Wh")
print(f"Média numérica das medições: {media_medicoes:.2f}")
print("==========================================")
```

---

# 10. Exemplo de execução

## Dados de entrada

```text
Código do equipamento: M-01
Nome do operador: Ana
Temperatura do motor (°C): 75
Pressão do sistema (bar): 6.5
Corrente elétrica (A): 12
Tempo de operação (horas): 4
```

## Resultado esperado

```text
==========================================
 RELATÓRIO DE MONITORAMENTO
==========================================
Equipamento: M-01
Operador: Ana
------------------------------------------
Temperatura: 75.00 °C
Temperatura: 167.00 °F
Pressão: 6.50 bar
Corrente: 12.00 A
Potência estimada: 2640.00 W
Tempo de operação: 4.00 h
Energia estimada: 10560.00 Wh
Média numérica das medições: 31.17
==========================================
```

---

# 11. Desafios progressivos

## Desafio 1 — Data e horário da coleta

Solicite ao operador a data e o horário da leitura:

```python
data_coleta = input("Data da coleta: ")
hora_coleta = input("Hora da coleta: ")
```

Inclua os dados no relatório:

```python
print(f"Data da coleta: {data_coleta}")
print(f"Hora da coleta: {hora_coleta}")
```

---

## Desafio 2 — Custo estimado da energia

Considere o custo de **R$ 0,85 por kWh**.

Converta a energia de Wh para kWh:

```python
energia_kwh = energia_estimada / 1000
```

Calcule o custo:

```python
custo_energia = energia_kwh * 0.85
```

Exiba os resultados:

```python
print(f"Energia estimada: {energia_kwh:.2f} kWh")
print(f"Custo estimado: R$ {custo_energia:.2f}")
```

---

## Desafio 3 — Distância para os limites

Considere os limites operacionais:

```python
limite_temperatura = 80
limite_pressao = 8
limite_corrente = 15
```

Calcule a diferença entre cada limite e o valor medido:

```python
diferenca_temperatura = limite_temperatura - temperatura
diferenca_pressao = limite_pressao - pressao
diferenca_corrente = limite_corrente - corrente
```

Inclua os resultados no relatório.

---

## Desafio 4 — Segunda leitura do motor

Adapte o programa para receber duas leituras:

- Leitura inicial;
- Leitura final.

Calcule a variação da temperatura:

```python
temperatura_inicial = float(
    input("Temperatura inicial (°C): ")
)

temperatura_final = float(
    input("Temperatura final (°C): ")
)

variacao_temperatura = temperatura_final - temperatura_inicial

print(f"Variação de temperatura: {variacao_temperatura:.2f} °C")
```

Faça o mesmo para:

- Pressão;
- Corrente;
- Potência, se possível.

---

## Desafio 5 — Comparação com C

Escolha uma parte do programa e crie uma versão equivalente em C.

Compare:

- Declaração das variáveis;
- Entrada de dados;
- Conversão de tipos;
- Cálculos;
- Saída formatada;
- Uso de ponto e vírgula;
- Organização dos blocos;
- Quantidade de código.

Complete:

| Aspecto | C | Python |
|---|---|---|
| Entrada da temperatura | | |
| Declaração da variável | | |
| Cálculo da potência | | |
| Exibição do resultado | | |
| Formatação decimal | | |
| Organização do bloco | | |

---

# 12. Testes obrigatórios

Execute o programa com pelo menos três conjuntos de dados:

## Teste 1 — Operação normal

- Temperatura: 60 °C;
- Pressão: 5 bar;
- Corrente: 8 A;
- Tempo: 2 horas.

## Teste 2 — Valores elevados

- Temperatura: 85 °C;
- Pressão: 9 bar;
- Corrente: 16 A;
- Tempo: 6 horas.

## Teste 3 — Valores decimais

- Temperatura: 72,5 °C;
- Pressão: 6,8 bar;
- Corrente: 11,3 A;
- Tempo: 3,5 horas.

Para cada teste, registre:

- Dados informados;
- Resultado obtido;
- Possíveis erros;
- Observações sobre o comportamento do programa.

---

# 13. Entrega

Cada estudante ou dupla deverá entregar:

- Arquivo `monitoramento_motor.py`;
- Tabela de entradas, processamentos e saídas;
- Três exemplos de execução;
- Respostas às questões de comparação entre C e Python;
- Desafios implementados;
- Registro dos testes realizados.

---

# 14. Critérios de avaliação

| Critério | Pontuação |
|---|---:|
| Leitura correta dos dados | 2,0 |
| Uso adequado dos tipos e conversões | 2,0 |
| Implementação dos cálculos | 2,0 |
| Organização e clareza do código | 1,5 |
| Geração correta do relatório | 1,5 |
| Testes e explicação da solução | 1,0 |
| **Total** | **10,0** |

Os desafios progressivos poderão ser utilizados como aprofundamento ou como evidência de aprendizagem ampliada.

---

# 15. Fechamento da aula

Discuta com a turma:

1. O que permaneceu igual em relação à linguagem C?
2. O que ficou mais simples em Python?
3. Qual foi a principal dificuldade?
4. Por que foi necessário converter o resultado de `input()`?
5. O que aconteceria se o operador digitasse texto no lugar de um número?
6. Quais informações deveriam ser armazenadas em um banco de dados?
7. Como realizar essa coleta automaticamente, sem digitação do operador?
8. Como representar um sensor por meio de um objeto Python?
9. Como registrar várias leituras ao longo do tempo?

As perguntas finais preparam as próximas unidades da disciplina:

- Estruturas condicionais;
- Simulação automática de sensores;
- Histórico de leituras;
- Classes de sensores e equipamentos;
- Persistência em PostgreSQL.

