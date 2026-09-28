**Aula 5 --- Organização de leituras com dicionários**

**Componente curricular**

**Linguagens de Programação e Banco de Dados**

**Curso**

**Curso Superior de Tecnologia em Automação Industrial**

**Unidade curricular**

**Estruturas de dados aplicadas ao histórico de sensores**

**Duração**

**4 horas-aula**

**1. Tema da aula**

Nesta aula, o histórico de leituras será reorganizado utilizando
**dicionários** e **listas de dicionários**.

Na Aula 4, as informações foram armazenadas em listas separadas:

> historico_ciclos = \[\]
>
> historico_temperatura = \[\]
>
> historico_pressao = \[\]
>
> historico_corrente = \[\]
>
> historico_estados = \[\]

Esse modelo funciona, mas exige que todas as listas permaneçam
alinhadas. Se uma informação for inserida em uma posição incorreta, os
dados poderão ficar associados ao ciclo errado.

Na Aula 5, cada leitura será representada como um registro completo:

> leitura = {
>
> \"ciclo\": 1,
>
> \"temperatura\": 72.5,
>
> \"pressao\": 6.8,
>
> \"corrente\": 12.4,
>
> \"estado\": \"ATENÇÃO\"
>
> }

As leituras serão armazenadas em uma única lista:

> historico = \[\]
>
> historico.append(leitura)

**2. Situação-problema**

O sistema de monitoramento precisa armazenar as leituras de um motor
industrial.

Cada leitura deve conter:

• Número do ciclo;

• Código do equipamento;

• Dispositivo de coleta;

• Temperatura;

• Pressão;

• Corrente;

• Estado da temperatura;

• Estado da pressão;

• Estado da corrente;

• Estado geral;

• Indicação de situação crítica.

O supervisor deseja consultar uma leitura completa sem precisar acessar
várias listas diferentes.

No modelo anterior, para exibir uma leitura, era necessário utilizar
vários índices:

> print(historico_ciclos\[indice\])
>
> print(historico_temperatura\[indice\])
>
> print(historico_pressao\[indice\])
>
> print(historico_corrente\[indice\])
>
> print(historico_estados\[indice\])

Com dicionários, todas as informações da leitura ficam agrupadas:

> leitura = {
>
> \"ciclo\": 1,
>
> \"temperatura\": 72.5,
>
> \"pressao\": 6.8,
>
> \"corrente\": 12.4,
>
> \"estado_geral\": \"ATENÇÃO\"
>
> }

**3. Objetivos da aula**

Ao final da aula, o estudante deverá ser capaz de:

• Criar dicionários em Python;

• Diferenciar chaves e valores;

• Acessar valores por meio de chaves;

• Inserir e alterar informações em um dicionário;

• Criar uma lista de dicionários;

• Armazenar registros completos de leituras;

• Percorrer uma lista de dicionários com for;

• Filtrar registros por estado;

• Identificar leituras críticas;

• Calcular estatísticas a partir de uma lista de registros;

• Organizar dados para futura gravação em arquivo ou banco de dados.

**4. Produto final da aula**

Ao final da aula, cada estudante ou dupla deverá possuir um programa
que:

1\. Simule vários ciclos de coleta;

2\. Crie um dicionário para cada leitura;

3\. Armazene os dicionários em uma lista;

4\. Exiba os registros completos;

5\. Filtre leituras em situação de alarme;

6\. Identifique ciclos críticos;

7\. Calcule estatísticas;

8\. Mostre um resumo organizado;

9\. Preserve os dados em uma estrutura adequada para as próximas aulas.

**5. Conhecimentos utilizados**

Esta aula utilizará:

• Variáveis;

• Tipos de dados;

• Listas;

• Dicionários;

• Estruturas condicionais;

• Estruturas de repetição;

• Funções;

• Operadores relacionais;

• Operadores lógicos;

• Simulação com random;

• Formatação de textos com f-strings.

**6. Organização da aula**

  ----------------------- ----------------------- -----------------------
  Etapa                   Atividade               Tempo sugerido

  1                       Retomada da Aula 4      20 min

  2                       Introdução aos          30 min
                          dicionários             

  3                       Criação e consulta de   30 min
                          registros               

  4                       Lista de dicionários    35 min

  5                       Integração com o        50 min
                          simulador               

  6                       Exibição e filtragem do 35 min
                          histórico               

  7                       Estatísticas com        35 min
                          registros               

  8                       Desafio de melhoria     35 min

  9                       Testes e fechamento     30 min

  Total                                           300 min
  ----------------------- ----------------------- -----------------------

**7. Retomada da Aula 4**

Na Aula 4, o programa utilizava listas paralelas para armazenar o
histórico:

> historico_ciclos = \[\]
>
> historico_temperatura = \[\]
>
> historico_pressao = \[\]
>
> historico_corrente = \[\]
>
> historico_estados = \[\]

Durante cada ciclo, os valores eram adicionados:

> historico_ciclos.append(numero_ciclo)
>
> historico_temperatura.append(temperatura)
>
> historico_pressao.append(pressao)
>
> historico_corrente.append(corrente)
>
> historico_estados.append(estado_geral)

Para exibir uma leitura completa, era necessário utilizar o mesmo índice
em várias listas:

> for indice in range(len(historico_ciclos)):
>
> print(f\"Ciclo: {historico_ciclos\[indice\]}\")
>
> print(
>
> f\"Temperatura: \"
>
> f\"{historico_temperatura\[indice\]:.2f} °C\"
>
> )
>
> print(
>
> f\"Pressão: \"
>
> f\"{historico_pressao\[indice\]:.2f} bar\"
>
> )
>
> print(
>
> f\"Corrente: \"
>
> f\"{historico_corrente\[indice\]:.2f} A\"
>
> )
>
> print(
>
> f\"Estado: \"
>
> f\"{historico_estados\[indice\]}\"
>
> )

Esse modelo pode gerar problemas se:

• Uma lista receber um valor e outra não;

• Um valor for inserido em posição incorreta;

• Uma leitura inválida for armazenada parcialmente;

• O índice utilizado não for o mesmo em todas as listas;

• Novos campos precisarem ser adicionados ao registro.

Na Aula 5, todos os dados de uma leitura serão armazenados juntos.

**8. O que é um dicionário?**

Um dicionário é uma estrutura de dados formada por pares de:

• Chave;

• Valor.

Exemplo:

> equipamento = {
>
> \"codigo\": \"M-01\",
>
> \"tipo\": \"Motor\",
>
> \"setor\": \"Produção\"
>
> }

Nesse exemplo:

• \"codigo\" é uma chave;

• \"M-01\" é o valor associado à chave;

• \"tipo\" é uma chave;

• \"Motor\" é o valor associado à chave;

• \"setor\" é uma chave;

• \"Produção\" é o valor associado à chave.

A estrutura geral é:

> dicionario = {
>
> \"chave\": valor,
>
> \"outra_chave\": outro_valor
>
> }

**9. Criando um dicionário de leitura**

Crie um dicionário para representar uma leitura:

> leitura = {
>
> \"ciclo\": 1,
>
> \"temperatura\": 72.5,
>
> \"pressao\": 6.8,
>
> \"corrente\": 12.4,
>
> \"estado_geral\": \"ATENÇÃO\"
>
> }

Exiba o dicionário completo:

> print(leitura)

Resultado possível:

> {
>
> \'ciclo\': 1,
>
> \'temperatura\': 72.5,
>
> \'pressao\': 6.8,
>
> \'corrente\': 12.4,
>
> \'estado_geral\': \'ATENÇÃO\'
>
> }

O dicionário pode conter valores de diferentes tipos:

> leitura = {
>
> \"ciclo\": 1,
>
> \"temperatura\": 72.5,
>
> \"pressao\": 6.8,
>
> \"corrente\": 12.4,
>
> \"estado_geral\": \"ATENÇÃO\",
>
> \"emergencia\": False
>
> }

**10. Acessando valores por meio de chaves**

Para acessar um valor, utilize a chave entre colchetes:

> print(leitura\[\"ciclo\"\])
>
> print(leitura\[\"temperatura\"\])
>
> print(leitura\[\"estado_geral\"\])

Para exibir uma leitura formatada:

> print(f\"Ciclo: {leitura\[\'ciclo\'\]}\")
>
> print(
>
> f\"Temperatura: \"
>
> f\"{leitura\[\'temperatura\'\]:.2f} °C\"
>
> )
>
> print(
>
> f\"Pressão: \"
>
> f\"{leitura\[\'pressao\'\]:.2f} bar\"
>
> )
>
> print(
>
> f\"Corrente: \"
>
> f\"{leitura\[\'corrente\'\]:.2f} A\"
>
> )
>
> print(f\"Estado: {leitura\[\'estado_geral\'\]}\")

**Atenção**

A chave precisa existir no dicionário.

O código abaixo gera erro:

> print(leitura\[\"umidade\"\])

Para verificar se uma chave existe:

> if \"umidade\" in leitura:
>
> print(leitura\[\"umidade\"\])
>
> else:
>
> print(\"A chave umidade não existe.\")

**11. Inserindo novos campos**

Um novo campo pode ser criado atribuindo um valor a uma nova chave:

> leitura\[\"equipamento\"\] = \"M-01\"
>
> leitura\[\"dispositivo\"\] = \"CLP-SIM-01\"

O dicionário passará a conter:

> {
>
> \"ciclo\": 1,
>
> \"temperatura\": 72.5,
>
> \"pressao\": 6.8,
>
> \"corrente\": 12.4,
>
> \"estado_geral\": \"ATENÇÃO\",
>
> \"equipamento\": \"M-01\",
>
> \"dispositivo\": \"CLP-SIM-01\"
>
> }

Também é possível adicionar o resultado de uma avaliação:

> leitura\[\"temperatura_acima_limite\"\] = True

Ou armazenar uma observação:

> leitura\[\"observacao\"\] = \"Verificar sistema de refrigeração\"

**12. Alterando valores**

Para alterar um valor existente:

> leitura\[\"estado_geral\"\] = \"ALARME\"

A temperatura também pode ser atualizada:

> leitura\[\"temperatura\"\] = 84.0

Exemplo:

> leitura = {
>
> \"ciclo\": 1,
>
> \"temperatura\": 72.5,
>
> \"estado_geral\": \"ATENÇÃO\"
>
> }
>
> leitura\[\"temperatura\"\] = 84.0
>
> leitura\[\"estado_geral\"\] = \"ALARME\"
>
> print(leitura)

**13. Removendo campos**

Para remover uma chave e seu valor:

> del leitura\[\"observacao\"\]

Outra forma é utilizar pop():

> observacao = leitura.pop(\"observacao\")

O valor removido poderá ser armazenado na variável:

> print(observacao)

Antes de remover uma chave, verifique se ela existe:

> if \"observacao\" in leitura:
>
> del leitura\[\"observacao\"\]

**14. Desafio 1 --- Criando um registro simples**

Crie um dicionário que represente uma leitura:

> leitura = {
>
> \"ciclo\": 1,
>
> \"temperatura\": 75.0,
>
> \"pressao\": 7.2,
>
> \"corrente\": 13.5,
>
> \"estado_geral\": \"ATENÇÃO\"
>
> }

Exiba cada informação:

> print(f\"Ciclo: {leitura\[\'ciclo\'\]}\")
>
> print(
>
> f\"Temperatura: \"
>
> f\"{leitura\[\'temperatura\'\]:.2f} °C\"
>
> )
>
> print(
>
> f\"Pressão: \"
>
> f\"{leitura\[\'pressao\'\]:.2f} bar\"
>
> )
>
> print(
>
> f\"Corrente: \"
>
> f\"{leitura\[\'corrente\'\]:.2f} A\"
>
> )
>
> print(f\"Estado: {leitura\[\'estado_geral\'\]}\")

**Atividade**

Adicione ao dicionário:

• Código do equipamento;

• Dispositivo de coleta;

• Estado da temperatura;

• Estado da pressão;

• Estado da corrente;

• Indicação de emergência.\
leitura\[\"equipamento\"\] = \"M-01\"\
leitura\[\"dispositivo\"\] = \"CLP-SIM-01\"leitura\[\"status*\
temperatura\"\] = \"ATENÇÃO\"leitura\[\"status*\
pressao\"\] = \"ATENÇÃO\"\
leitura\[\"status_corrente\"\] = \"ATENÇÃO\"leitura\[\"emergencia\"\] =
False

**15. Lista de dicionários**

Uma lista pode armazenar vários dicionários.

> historico = \[\]

Crie o primeiro registro:

> leitura_1 = {
>
> \"ciclo\": 1,
>
> \"temperatura\": 72.5,
>
> \"pressao\": 6.8,
>
> \"corrente\": 12.4,
>
> \"estado_geral\": \"NORMAL\"
>
> }

Adicione o registro à lista:

> historico.append(leitura_1)

Crie o segundo registro:

> leitura_2 = {
>
> \"ciclo\": 2,
>
> \"temperatura\": 81.0,
>
> \"pressao\": 8.2,
>
> \"corrente\": 15.5,
>
> \"estado_geral\": \"ALARME\"
>
> }

Adicione o segundo registro:

> historico.append(leitura_2)

Exiba o histórico:

> print(historico)

**16. Acessando registros específicos**

Para acessar o primeiro registro:

> print(historico\[0\])

Para acessar o segundo registro:

> print(historico\[1\])

Para acessar a temperatura do primeiro registro:

> print(historico\[0\]\[\"temperatura\"\])

Para acessar o estado do segundo registro:

> print(historico\[1\]\[\"estado_geral\"\])

Para acessar a última leitura:

> print(historico\[-1\])

Para acessar a temperatura da última leitura:

> print(historico\[-1\]\[\"temperatura\"\])

A estrutura possui dois níveis de acesso:

> historico\[indice\]\[\"chave\"\]

Exemplo:

> historico\[0\]\[\"pressao\"\]

**17. Percorrendo uma lista de dicionários**

Utilize for para percorrer os registros:

> for leitura in historico:
>
> print(leitura)

Para exibir os campos individualmente:

> for leitura in historico:
>
> print()
>
> print(f\"Ciclo: {leitura\[\'ciclo\'\]}\")
>
> print(
>
> f\"Temperatura: \"
>
> f\"{leitura\[\'temperatura\'\]:.2f} °C\"
>
> )
>
> print(
>
> f\"Pressão: \"
>
> f\"{leitura\[\'pressao\'\]:.2f} bar\"
>
> )
>
> print(
>
> f\"Corrente: \"
>
> f\"{leitura\[\'corrente\'\]:.2f} A\"
>
> )
>
> print(
>
> f\"Estado: \"
>
> f\"{leitura\[\'estado_geral\'\]}\"
>
> )

**18. Desafio 2 --- Criando vários registros**

Crie uma lista chamada historico:

> historico = \[\]

Depois, crie três registros:

> leitura_1 = {
>
> \"ciclo\": 1,
>
> \"temperatura\": 65.0,
>
> \"pressao\": 6.0,
>
> \"corrente\": 11.5,
>
> \"estado_geral\": \"NORMAL\"
>
> }
>
> leitura_2 = {
>
> \"ciclo\": 2,
>
> \"temperatura\": 76.0,
>
> \"pressao\": 7.5,
>
> \"corrente\": 13.2,
>
> \"estado_geral\": \"ATENÇÃO\"
>
> }
>
> leitura_3 = {
>
> \"ciclo\": 3,
>
> \"temperatura\": 85.0,
>
> \"pressao\": 8.5,
>
> \"corrente\": 16.0,
>
> \"estado_geral\": \"ALARME\"
>
> }

Adicione os registros:

> historico.append(leitura_1)
>
> historico.append(leitura_2)
>
> historico.append(leitura_3)

Exiba todos os registros:

> for leitura in historico:
>
> print(
>
> f\"Ciclo {leitura\[\'ciclo\'\]}: \"
>
> f\"{leitura\[\'estado_geral\'\]}\"
>
> )

**19. Criando registros diretamente com append()**

Também é possível criar o dicionário diretamente dentro do append():

> historico = \[\]
>
> historico.append({
>
> \"ciclo\": 1,
>
> \"temperatura\": 65.0,
>
> \"pressao\": 6.0,
>
> \"corrente\": 11.5,
>
> \"estado_geral\": \"NORMAL\"
>
> })
>
> historico.append({
>
> \"ciclo\": 2,
>
> \"temperatura\": 76.0,
>
> \"pressao\": 7.5,
>
> \"corrente\": 13.2,
>
> \"estado_geral\": \"ATENÇÃO\"
>
> })
>
> historico.append({
>
> \"ciclo\": 3,
>
> \"temperatura\": 85.0,
>
> \"pressao\": 8.5,
>
> \"corrente\": 16.0,
>
> \"estado_geral\": \"ALARME\"
>
> })

Essa forma é útil quando os dados já estão disponíveis.

**20. Criando registros dentro de um laço**

O dicionário pode ser criado dentro do laço de simulação:

> import random
>
> historico = \[\]
>
> for ciclo in range(5):
>
> numero_ciclo = ciclo + 1
>
> temperatura = random.randint(60, 95)
>
> pressao = random.uniform(5.0, 10.0)
>
> corrente = random.uniform(10.0, 20.0)
>
> leitura = {
>
> \"ciclo\": numero_ciclo,
>
> \"temperatura\": temperatura,
>
> \"pressao\": pressao,
>
> \"corrente\": corrente,
>
> \"estado_geral\": \"EM ANÁLISE\"
>
> }
>
> historico.append(leitura)
>
> for leitura in historico:
>
> print(leitura)

**21. Incluindo os estados dos sensores**

O registro pode armazenar o estado de cada sensor:

> leitura = {
>
> \"ciclo\": numero_ciclo,
>
> \"temperatura\": temperatura,
>
> \"pressao\": pressao,
>
> \"corrente\": corrente,
>
> \"status_temperatura\": status_temperatura,
>
> \"status_pressao\": status_pressao,
>
> \"status_corrente\": status_corrente,
>
> \"estado_geral\": estado_geral
>
> }

Também pode armazenar informações booleanas:

> leitura\[\"temperatura_acima_limite\"\] = (
>
> temperatura \> limite_temperatura
>
> )
>
> leitura\[\"pressao_acima_limite\"\] = (
>
> pressao \> limite_pressao
>
> )
>
> leitura\[\"corrente_acima_limite\"\] = (
>
> corrente \> limite_corrente
>
> )
>
> leitura\[\"situacao_critica\"\] = situacao_critica

**22. Modelo completo de um registro**

Um registro completo poderá possuir a seguinte estrutura:

> leitura = {
>
> \"ciclo\": numero_ciclo,
>
> \"equipamento\": codigo_equipamento,
>
> \"dispositivo\": dispositivo_coleta,
>
> \"temperatura\": temperatura,
>
> \"pressao\": pressao,
>
> \"corrente\": corrente,
>
> \"status_temperatura\": status_temperatura,
>
> \"status_pressao\": status_pressao,
>
> \"status_corrente\": status_corrente,
>
> \"estado_geral\": estado_geral,
>
> \"temperatura_acima_limite\": (
>
> temperatura \> limite_temperatura
>
> ),
>
> \"pressao_acima_limite\": (
>
> pressao \> limite_pressao
>
> ),
>
> \"corrente_acima_limite\": (
>
> corrente \> limite_corrente
>
> ),
>
> \"situacao_critica\": situacao_critica
>
> }

**23. Desafio 3 --- Integrando com o simulador**

Utilize o programa da Aula 4.

Substitua as listas paralelas:

> historico_ciclos = \[\]
>
> historico_temperatura = \[\]
>
> historico_pressao = \[\]
>
> historico_corrente = \[\]
>
> historico_estados = \[\]

Por uma única lista:

> historico = \[\]

Depois da classificação do estado geral, crie o registro:

> leitura = {
>
> \"ciclo\": numero_ciclo,
>
> \"equipamento\": codigo_equipamento,
>
> \"dispositivo\": dispositivo_coleta,
>
> \"temperatura\": temperatura,
>
> \"pressao\": pressao,
>
> \"corrente\": corrente,
>
> \"status_temperatura\": status_temperatura,
>
> \"status_pressao\": status_pressao,
>
> \"status_corrente\": status_corrente,
>
> \"estado_geral\": estado_geral,
>
> \"situacao_critica\": situacao_critica
>
> }

Adicione o registro ao histórico:

> historico.append(leitura)

A partir desse ponto, as informações deverão ser consultadas no
dicionário.

**24. Exibindo o histórico integrado**

Depois do laço principal:

> print()
>
> print(\"==========================================\")
>
> print(\" HISTÓRICO DE LEITURAS\")
>
> print(\"==========================================\")
>
> for leitura in historico:
>
> print()
>
> print(f\"Ciclo: {leitura\[\'ciclo\'\]}\")
>
> print(
>
> f\"Equipamento: \"
>
> f\"{leitura\[\'equipamento\'\]}\"
>
> )
>
> print(
>
> f\"Dispositivo: \"
>
> f\"{leitura\[\'dispositivo\'\]}\"
>
> )
>
> print(
>
> f\"Temperatura: \"
>
> f\"{leitura\[\'temperatura\'\]:.2f} °C\"
>
> )
>
> print(
>
> f\"Status da temperatura: \"
>
> f\"{leitura\[\'status_temperatura\'\]}\"
>
> )
>
> print(
>
> f\"Pressão: \"
>
> f\"{leitura\[\'pressao\'\]:.2f} bar\"
>
> )
>
> print(
>
> f\"Status da pressão: \"
>
> f\"{leitura\[\'status_pressao\'\]}\"
>
> )
>
> print(
>
> f\"Corrente: \"
>
> f\"{leitura\[\'corrente\'\]:.2f} A\"
>
> )
>
> print(
>
> f\"Status da corrente: \"
>
> f\"{leitura\[\'status_corrente\'\]}\"
>
> )
>
> print(
>
> f\"Estado geral: \"
>
> f\"{leitura\[\'estado_geral\'\]}\"
>
> )

**25. Filtrando registros**

Para exibir somente leituras em alarme:

> for leitura in historico:
>
> if leitura\[\"estado_geral\"\] == \"ALARME\":
>
> print(
>
> f\"Ciclo em alarme: \"
>
> f\"{leitura\[\'ciclo\'\]}\"
>
> )

Para exibir situações de alarme ou emergência:

> for leitura in historico:
>
> if (
>
> leitura\[\"estado_geral\"\] == \"ALARME\"
>
> or leitura\[\"estado_geral\"\] == \"EMERGÊNCIA\"
>
> ):
>
> print(
>
> f\"Ciclo crítico: \"
>
> f\"{leitura\[\'ciclo\'\]}\"
>
> )

Para exibir registros com temperatura acima do limite:

> for leitura in historico:
>
> if leitura\[\"temperatura\"\] \> limite_temperatura:
>
> print(
>
> f\"Ciclo {leitura\[\'ciclo\'\]}: \"
>
> f\"{leitura\[\'temperatura\'\]:.2f} °C\"
>
> )

Para exibir somente situações críticas:

> for leitura in historico:
>
> if leitura\[\"situacao_critica\"\]:
>
> print(
>
> f\"Situação crítica no ciclo \"
>
> f\"{leitura\[\'ciclo\'\]}\"
>
> )

**26. Calculando estatísticas com uma lista de dicionários**

Para calcular a menor temperatura:

> if len(historico) \> 0:
>
> menor_temperatura = min(
>
> leitura\[\"temperatura\"\]
>
> for leitura in historico
>
> )
>
> print(
>
> f\"Menor temperatura: \"
>
> f\"{menor_temperatura:.2f} °C\"
>
> )

Para calcular a maior temperatura:

> maior_temperatura = max(
>
> leitura\[\"temperatura\"\]
>
> for leitura in historico
>
> )

Para calcular a média:

> soma_temperaturas = sum(
>
> leitura\[\"temperatura\"\]
>
> for leitura in historico
>
> )
>
> media_temperatura = (
>
> soma_temperaturas
>
> / len(historico)
>
> )
>
> print(
>
> f\"Média da temperatura: \"
>
> f\"{media_temperatura:.2f} °C\"
>
> )

A mesma lógica pode ser utilizada para pressão e corrente:

> menor_pressao = min(
>
> leitura\[\"pressao\"\]
>
> for leitura in historico
>
> )
>
> maior_pressao = max(
>
> leitura\[\"pressao\"\]
>
> for leitura in historico
>
> )
>
> media_pressao = sum(
>
> leitura\[\"pressao\"\]
>
> for leitura in historico
>
> ) / len(historico)
>
> menor_corrente = min(
>
> leitura\[\"corrente\"\]
>
> for leitura in historico
>
> )
>
> maior_corrente = max(
>
> leitura\[\"corrente\"\]
>
> for leitura in historico
>
> )
>
> media_corrente = sum(
>
> leitura\[\"corrente\"\]
>
> for leitura in historico
>
> ) / len(historico)

**27. Contando ocorrências com dicionários**

Para contar leituras acima do limite:

> leituras_temperatura_alta = 0
>
> for leitura in historico:
>
> if leitura\[\"temperatura\"\] \> limite_temperatura:
>
> leituras_temperatura_alta += 1

Para contar estados gerais:

> quantidade_normal = 0
>
> quantidade_atencao = 0
>
> quantidade_alarme = 0
>
> quantidade_emergencia = 0
>
> for leitura in historico:
>
> estado = leitura\[\"estado_geral\"\]
>
> if estado == \"NORMAL\":
>
> quantidade_normal += 1
>
> elif estado == \"ATENÇÃO\":
>
> quantidade_atencao += 1
>
> elif estado == \"ALARME\":
>
> quantidade_alarme += 1
>
> elif estado == \"EMERGÊNCIA\":
>
> quantidade_emergencia += 1

Exibição:

> print(f\"Normais: {quantidade_normal}\")
>
> print(f\"Atenção: {quantidade_atencao}\")
>
> print(f\"Alarmes: {quantidade_alarme}\")
>
> print(f\"Emergências: {quantidade_emergencia}\")

**28. Encontrando a leitura de maior temperatura**

A função max() pode ser utilizada com uma chave:

> if len(historico) \> 0:
>
> leitura_maior_temperatura = max(
>
> historico,
>
> key=lambda leitura: leitura\[\"temperatura\"\]
>
> )
>
> print(
>
> f\"Maior temperatura: \"
>
> f\"{leitura_maior_temperatura\[\'temperatura\'\]:.2f} °C\"
>
> )
>
> print(
>
> f\"Ciclo: \"
>
> f\"{leitura_maior_temperatura\[\'ciclo\'\]}\"
>
> )

O parâmetro key informa qual valor deve ser utilizado na comparação.

A mesma lógica pode ser aplicada à pressão:

> leitura_maior_pressao = max(
>
> historico,
>
> key=lambda leitura: leitura\[\"pressao\"\]
>
> )

E à corrente:

> leitura_maior_corrente = max(
>
> historico,
>
> key=lambda leitura: leitura\[\"corrente\"\]
>
> )

**29. Ordenando registros**

Para ordenar as leituras por temperatura:

> historico_ordenado = sorted(
>
> historico,
>
> key=lambda leitura: leitura\[\"temperatura\"\]
>
> )

Para ordenar da maior para a menor temperatura:

> historico_ordenado = sorted(
>
> historico,
>
> key=lambda leitura: leitura\[\"temperatura\"\],
>
> reverse=True
>
> )

Exibição:

> for leitura in historico_ordenado:
>
> print(
>
> f\"Ciclo {leitura\[\'ciclo\'\]}: \"
>
> f\"{leitura\[\'temperatura\'\]:.2f} °C\"
>
> )

**30. Desafio 4 --- Filtrando e ordenando leituras críticas**

Crie uma lista somente com as leituras críticas:

> leituras_criticas = \[\]
>
> for leitura in historico:
>
> if (
>
> leitura\[\"estado_geral\"\] == \"ALARME\"
>
> or leitura\[\"estado_geral\"\] == \"EMERGÊNCIA\"
>
> ):
>
> leituras_criticas.append(leitura)

Ordene as leituras críticas pela temperatura:

> leituras_criticas_ordenadas = sorted(
>
> leituras_criticas,
>
> key=lambda leitura: leitura\[\"temperatura\"\],
>
> reverse=True
>
> )

Exiba:

> for leitura in leituras_criticas_ordenadas:
>
> print(
>
> f\"Ciclo: {leitura\[\'ciclo\'\]}\"
>
> )
>
> print(
>
> f\"Temperatura: \"
>
> f\"{leitura\[\'temperatura\'\]:.2f} °C\"
>
> )
>
> print(
>
> f\"Estado: \"
>
> f\"{leitura\[\'estado_geral\'\]}\"
>
> )
>
> print()

**31. Desafio 5 --- Criando uma função para exibir leituras**

Crie uma função para exibir um registro:

> def exibir_leitura(leitura):
>
> print()
>
> print(f\"Ciclo: {leitura\[\'ciclo\'\]}\")
>
> print(
>
> f\"Temperatura: \"
>
> f\"{leitura\[\'temperatura\'\]:.2f} °C\"
>
> )
>
> print(
>
> f\"Pressão: \"
>
> f\"{leitura\[\'pressao\'\]:.2f} bar\"
>
> )
>
> print(
>
> f\"Corrente: \"
>
> f\"{leitura\[\'corrente\'\]:.2f} A\"
>
> )
>
> print(
>
> f\"Status geral: \"
>
> f\"{leitura\[\'estado_geral\'\]}\"
>
> )

Utilize a função:

> for leitura in historico:
>
> exibir_leitura(leitura)

**32. Desafio 6 --- Criando funções de análise**

Crie uma função para obter a média da temperatura:

> def calcular_media_temperatura(historico):
>
> if len(historico) == 0:
>
> return 0
>
> soma = sum(
>
> leitura\[\"temperatura\"\]
>
> for leitura in historico
>
> )
>
> return soma / len(historico)

Utilize a função:

> media = calcular_media_temperatura(historico)
>
> print(
>
> f\"Média da temperatura: \"
>
> f\"{media:.2f} °C\"
>
> )

Crie uma função para contar leituras acima do limite:

> def contar_temperaturas_altas(
>
> historico,
>
> limite
>
> ):
>
> contador = 0
>
> for leitura in historico:
>
> if leitura\[\"temperatura\"\] \> limite:
>
> contador += 1
>
> return contador

Utilize a função:

> quantidade = contar_temperaturas_altas(
>
> historico,
>
> limite_temperatura
>
> )
>
> print(
>
> f\"Temperaturas acima do limite: \"
>
> f\"{quantidade}\"
>
> )

**33. Programa completo de referência**

Crie um arquivo chamado:

> aula_05_dicionarios.py

Utilize o programa abaixo como referência.

> import random
>
> print(\"==========================================\")
>
> print(\" SIMULADOR COM LISTA DE DICIONÁRIOS\")
>
> print(\"==========================================\")
>
> codigo_equipamento = \"M-01\"
>
> dispositivo_coleta = \"CLP-SIM-01\"
>
> quantidade_ciclos = 20
>
> limite_temperatura = 80
>
> limite_pressao = 8
>
> limite_corrente = 15
>
> historico = \[\]
>
> ciclos_normais = 0
>
> ciclos_atencao = 0
>
> ciclos_alarme = 0
>
> ciclos_emergencia = 0
>
> ciclos_realizados = 0
>
> leituras_ignoradas = 0
>
> print(f\"Equipamento: {codigo_equipamento}\")
>
> print(f\"Dispositivo: {dispositivo_coleta}\")
>
> print(f\"Ciclos planejados: {quantidade_ciclos}\")
>
> for ciclo in range(quantidade_ciclos):
>
> numero_ciclo = ciclo + 1
>
> print()
>
> print(
>
> f\"========== CICLO \"
>
> f\"{numero_ciclo} ==========\"
>
> )
>
> if numero_ciclo == 5:
>
> print(
>
> \"Falha de comunicação \"
>
> \"com o sensor.\"
>
> )
>
> leituras_ignoradas += 1
>
> continue
>
> temperatura = random.randint(60, 95)
>
> pressao = random.uniform(5.0, 10.0)
>
> corrente = random.uniform(10.0, 20.0)
>
> ciclos_realizados += 1
>
> if temperatura \< 70:
>
> status_temperatura = \"NORMAL\"
>
> elif temperatura \<= limite_temperatura:
>
> status_temperatura = \"ATENÇÃO\"
>
> else:
>
> status_temperatura = \"ALARME\"
>
> if pressao \< 7:
>
> status_pressao = \"NORMAL\"
>
> elif pressao \<= limite_pressao:
>
> status_pressao = \"ATENÇÃO\"
>
> else:
>
> status_pressao = \"ALARME\"
>
> if corrente \< 13:
>
> status_corrente = \"NORMAL\"
>
> elif corrente \<= limite_corrente:
>
> status_corrente = \"ATENÇÃO\"
>
> else:
>
> status_corrente = \"ALARME\"
>
> situacao_critica = (
>
> temperatura \> 90
>
> or pressao \> 10
>
> or corrente \> 18
>
> )
>
> existe_alarme = (
>
> status_temperatura == \"ALARME\"
>
> or status_pressao == \"ALARME\"
>
> or status_corrente == \"ALARME\"
>
> )
>
> existe_atencao = (
>
> status_temperatura == \"ATENÇÃO\"
>
> or status_pressao == \"ATENÇÃO\"
>
> or status_corrente == \"ATENÇÃO\"
>
> )
>
> if situacao_critica:
>
> estado_geral = \"EMERGÊNCIA\"
>
> elif existe_alarme:
>
> estado_geral = \"ALARME\"
>
> elif existe_atencao:
>
> estado_geral = \"ATENÇÃO\"
>
> else:
>
> estado_geral = \"NORMAL\"
>
> leitura = {
>
> \"ciclo\": numero_ciclo,
>
> \"equipamento\": codigo_equipamento,
>
> \"dispositivo\": dispositivo_coleta,
>
> \"temperatura\": temperatura,
>
> \"pressao\": pressao,
>
> \"corrente\": corrente,
>
> \"status_temperatura\": status_temperatura,
>
> \"status_pressao\": status_pressao,
>
> \"status_corrente\": status_corrente,
>
> \"estado_geral\": estado_geral,
>
> \"situacao_critica\": situacao_critica
>
> }
>
> historico.append(leitura)
>
> if estado_geral == \"NORMAL\":
>
> ciclos_normais += 1
>
> elif estado_geral == \"ATENÇÃO\":
>
> ciclos_atencao += 1
>
> elif estado_geral == \"ALARME\":
>
> ciclos_alarme += 1
>
> elif estado_geral == \"EMERGÊNCIA\":
>
> ciclos_emergencia += 1
>
> print(
>
> f\"Temperatura: \"
>
> f\"{temperatura:.2f} °C - \"
>
> f\"{status_temperatura}\"
>
> )
>
> print(
>
> f\"Pressão: \"
>
> f\"{pressao:.2f} bar - \"
>
> f\"{status_pressao}\"
>
> )
>
> print(
>
> f\"Corrente: \"
>
> f\"{corrente:.2f} A - \"
>
> f\"{status_corrente}\"
>
> )
>
> print(f\"Estado geral: {estado_geral}\")
>
> if estado_geral == \"EMERGÊNCIA\":
>
> print(
>
> \"PARADA DE EMERGÊNCIA \"
>
> \"ATIVADA.\"
>
> )
>
> break
>
> print()
>
> print(\"==========================================\")
>
> print(\" RESUMO DA COLETA\")
>
> print(\"==========================================\")
>
> print(f\"Equipamento: {codigo_equipamento}\")
>
> print(f\"Dispositivo: {dispositivo_coleta}\")
>
> print(f\"Ciclos planejados: {quantidade_ciclos}\")
>
> print(f\"Ciclos realizados: {ciclos_realizados}\")
>
> print(f\"Leituras ignoradas: {leituras_ignoradas}\")
>
> print(f\"Leituras armazenadas: {len(historico)}\")
>
> print(f\"Ciclos normais: {ciclos_normais}\")
>
> print(f\"Ciclos em atenção: {ciclos_atencao}\")
>
> print(f\"Ciclos em alarme: {ciclos_alarme}\")
>
> print(
>
> f\"Ciclos em emergência: \"
>
> f\"{ciclos_emergencia}\"
>
> )
>
> if len(historico) \> 0:
>
> temperaturas = \[
>
> leitura\[\"temperatura\"\]
>
> for leitura in historico
>
> \]
>
> pressoes = \[
>
> leitura\[\"pressao\"\]
>
> for leitura in historico
>
> \]
>
> correntes = \[
>
> leitura\[\"corrente\"\]
>
> for leitura in historico
>
> \]
>
> menor_temperatura = min(temperaturas)
>
> maior_temperatura = max(temperaturas)
>
> media_temperatura = (
>
> sum(temperaturas)
>
> / len(temperaturas)
>
> )
>
> menor_pressao = min(pressoes)
>
> maior_pressao = max(pressoes)
>
> media_pressao = (
>
> sum(pressoes)
>
> / len(pressoes)
>
> )
>
> menor_corrente = min(correntes)
>
> maior_corrente = max(correntes)
>
> media_corrente = (
>
> sum(correntes)
>
> / len(correntes)
>
> )
>
> print()
>
> print(\"==========================================\")
>
> print(\" ESTATÍSTICAS DO HISTÓRICO\")
>
> print(\"==========================================\")
>
> print(
>
> f\"Leituras armazenadas: \"
>
> f\"{len(historico)}\"
>
> )
>
> print()
>
> print(\"TEMPERATURA\")
>
> print(
>
> f\"Mínima: \"
>
> f\"{menor_temperatura:.2f} °C\"
>
> )
>
> print(
>
> f\"Máxima: \"
>
> f\"{maior_temperatura:.2f} °C\"
>
> )
>
> print(
>
> f\"Média: \"
>
> f\"{media_temperatura:.2f} °C\"
>
> )
>
> print()
>
> print(\"PRESSÃO\")
>
> print(
>
> f\"Mínima: \"
>
> f\"{menor_pressao:.2f} bar\"
>
> )
>
> print(
>
> f\"Máxima: \"
>
> f\"{maior_pressao:.2f} bar\"
>
> )
>
> print(
>
> f\"Média: \"
>
> f\"{media_pressao:.2f} bar\"
>
> )
>
> print()
>
> print(\"CORRENTE\")
>
> print(
>
> f\"Mínima: \"
>
> f\"{menor_corrente:.2f} A\"
>
> )
>
> print(
>
> f\"Máxima: \"
>
> f\"{maior_corrente:.2f} A\"
>
> )
>
> print(
>
> f\"Média: \"
>
> f\"{media_corrente:.2f} A\"
>
> )
>
> leituras_criticas = \[\]
>
> for leitura in historico:
>
> if (
>
> leitura\[\"estado_geral\"\] == \"ALARME\"
>
> or leitura\[\"estado_geral\"\] == \"EMERGÊNCIA\"
>
> ):
>
> leituras_criticas.append(leitura)
>
> print()
>
> print(\"LEITURAS CRÍTICAS\")
>
> print(\"\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\")
>
> for leitura in leituras_criticas:
>
> print(
>
> f\"Ciclo: \"
>
> f\"{leitura\[\'ciclo\'\]}\"
>
> )
>
> print(
>
> f\"Temperatura: \"
>
> f\"{leitura\[\'temperatura\'\]:.2f} °C\"
>
> )
>
> print(
>
> f\"Pressão: \"
>
> f\"{leitura\[\'pressao\'\]:.2f} bar\"
>
> )
>
> print(
>
> f\"Corrente: \"
>
> f\"{leitura\[\'corrente\'\]:.2f} A\"
>
> )
>
> print(
>
> f\"Estado: \"
>
> f\"{leitura\[\'estado_geral\'\]}\"
>
> )
>
> print()
>
> leitura_maior_temperatura = max(
>
> historico,
>
> key=lambda leitura: leitura\[\"temperatura\"\]
>
> )
>
> print()
>
> print(
>
> f\"Maior temperatura: \"
>
> f\"{leitura_maior_temperatura\[\'temperatura\'\]:.2f} °C\"
>
> )
>
> print(
>
> f\"Ciclo: \"
>
> f\"{leitura_maior_temperatura\[\'ciclo\'\]}\"
>
> )
>
> if len(historico) \>= 2:
>
> primeira_temperatura = (
>
> historico\[0\]\[\"temperatura\"\]
>
> )
>
> ultima_temperatura = (
>
> historico\[-1\]\[\"temperatura\"\]
>
> )
>
> variacao = (
>
> ultima_temperatura
>
> \- primeira_temperatura
>
> )
>
> if variacao \> 0:
>
> tendencia = \"AUMENTO\"
>
> elif variacao \< 0:
>
> tendencia = \"REDUÇÃO\"
>
> else:
>
> tendencia = \"ESTÁVEL\"
>
> print()
>
> print(\"TENDÊNCIA DA TEMPERATURA\")
>
> print(\"\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\")
>
> print(
>
> f\"Primeira leitura: \"
>
> f\"{primeira_temperatura:.2f} °C\"
>
> )
>
> print(
>
> f\"Última leitura: \"
>
> f\"{ultima_temperatura:.2f} °C\"
>
> )
>
> print(
>
> f\"Variação: \"
>
> f\"{variacao:.2f} °C\"
>
> )
>
> print(f\"Tendência: {tendencia}\")
>
> else:
>
> print()
>
> print(\"Nenhuma leitura foi armazenada.\")
>
> print()
>
> print(\"==========================================\")
>
> print(\" FIM DA ANÁLISE\")
>
> print(\"==========================================\")

**34. Testes controlados**

**Teste 1 --- Registro simples**

Utilize:

> leitura = {
>
> \"ciclo\": 1,
>
> \"temperatura\": 72.0,
>
> \"pressao\": 6.5,
>
> \"corrente\": 12.0,
>
> \"estado_geral\": \"NORMAL\"
>
> }

Verifique:

• Se todas as chaves foram criadas;

• Se os valores podem ser acessados;

• Se os valores podem ser alterados;

• Se uma nova chave pode ser adicionada.

**Teste 2 --- Lista de registros**

Utilize:

> historico = \[
>
> {
>
> \"ciclo\": 1,
>
> \"temperatura\": 65.0,
>
> \"pressao\": 6.0,
>
> \"corrente\": 11.0,
>
> \"estado_geral\": \"NORMAL\"
>
> },
>
> {
>
> \"ciclo\": 2,
>
> \"temperatura\": 82.0,
>
> \"pressao\": 8.5,
>
> \"corrente\": 16.0,
>
> \"estado_geral\": \"ALARME\"
>
> }
>
> \]

Verifique:

• O tamanho da lista;

• O primeiro registro;

• O segundo registro;

• A temperatura do segundo registro;

• O estado geral do segundo registro.

**Teste 3 --- Filtragem**

Crie uma lista somente com registros em alarme:

> leituras_alarme = \[\]
>
> for leitura in historico:
>
> if leitura\[\"estado_geral\"\] == \"ALARME\":
>
> leituras_alarme.append(leitura)

Exiba o resultado.

**Teste 4 --- Maior temperatura**

Utilize:

> leitura_maior = max(
>
> historico,
>
> key=lambda leitura: leitura\[\"temperatura\"\]
>
> )

Exiba o ciclo e a temperatura da leitura encontrada.

**Teste 5 --- Falha de comunicação**

Ignore um dos ciclos e verifique:

• Se o ciclo não foi armazenado;

• Se a lista de registros permaneceu consistente;

• Se os demais registros continuaram completos;

• Se o número original do ciclo foi preservado.

**35. Atividade de análise**

Responda:

1\. Qual é a diferença entre uma lista e um dicionário?

2\. O que é uma chave?

3\. O que é um valor?

4\. Como acessar uma informação específica de um dicionário?

5\. Como criar uma lista de dicionários?

6\. Qual é a vantagem de armazenar uma leitura completa em um único
dicionário?

7\. Qual problema pode ocorrer com listas paralelas?

8\. Como filtrar somente registros em alarme?

9\. Como encontrar o registro com a maior temperatura?

10\. Como calcular a média de uma variável armazenada em uma lista de
dicionários?

11\. Por que o número original do ciclo deve ser armazenado no registro?

12\. Quais campos seriam necessários para gravar esse registro em um
banco de dados?

13\. Como um dicionário poderia ser convertido em uma linha de arquivo
CSV?

14\. Quais informações adicionais poderiam ser armazenadas em cada
leitura?

**36. Desafio final**

Modifique o programa para incluir os seguintes campos em cada registro:

• Data da leitura;

• Horário da leitura;

• Nome do operador;

• Turno de trabalho;

• Observação operacional.

Exemplo:

> leitura = {
>
> \"ciclo\": numero_ciclo,
>
> \"equipamento\": codigo_equipamento,
>
> \"dispositivo\": dispositivo_coleta,
>
> \"temperatura\": temperatura,
>
> \"pressao\": pressao,
>
> \"corrente\": corrente,
>
> \"estado_geral\": estado_geral,
>
> \"data\": \"2026-09-04\",
>
> \"horario\": \"14:30:00\",
>
> \"operador\": \"Operador 01\",
>
> \"turno\": \"Tarde\",
>
> \"observacao\": \"Coleta automática\"
>
> }

Depois:

1\. Exiba os novos campos;

2\. Filtre registros de um determinado turno;

3\. Exiba somente registros com observação;

4\. Calcule estatísticas por turno;

5\. Identifique o registro mais crítico.

**37. Entrega da atividade**

Cada estudante ou dupla deverá entregar:

• Arquivo aula_05_dicionarios.py;

• Lista de dicionários contendo o histórico;

• Registros com dados completos;

• Exibição formatada do histórico;

• Filtro de leituras críticas;

• Identificação da maior temperatura;

• Cálculo de estatísticas;

• Testes controlados;

• Respostas às questões de análise;

• Implementação de pelo menos uma melhoria.

**38. Critérios de avaliação**

  ----------------------------------- -----------------------------------
  Critério                            Pontuação

  Criação correta de dicionários      1,5

  Uso adequado de chaves e valores    1,0

  Criação da lista de dicionários     1,5

  Integração com o simulador          2,0

  Exibição e filtragem dos registros  1,5

  Cálculo das estatísticas            1,0

  Testes, organização e clareza do    1,0
  código                              

  Implementação de melhoria           0,5

  Total                               10,0
  ----------------------------------- -----------------------------------

**39. Fechamento da aula**

**Síntese dos conceitos**

Nesta aula, o programa passou a:

• Representar uma leitura como um dicionário;

• Armazenar vários registros em uma lista;

• Consultar valores por meio de chaves;

• Percorrer

**Aula 5 --- Organização de leituras com dicionários**

**Componente curricular**

**Linguagens de Programação e Banco de Dados**

**Curso**

**Curso Superior de Tecnologia em Automação Industrial**

**Unidade curricular**

**Estruturas de dados aplicadas ao histórico de sensores**

**Duração**

**4 horas-aula**

**1. Tema da aula**

Nesta aula, o histórico de leituras será reorganizado utilizando
**dicionários** e **listas de dicionários**.

Na Aula 4, as informações foram armazenadas em listas separadas:

> historico_ciclos = \[\]
>
> historico_temperatura = \[\]
>
> historico_pressao = \[\]
>
> historico_corrente = \[\]
>
> historico_estados = \[\]

Esse modelo funciona, mas exige que todas as listas permaneçam
alinhadas. Se uma informação for inserida em uma posição incorreta, os
dados poderão ficar associados ao ciclo errado.

Na Aula 5, cada leitura será representada como um registro completo:

> leitura = {
>
> \"ciclo\": 1,
>
> \"temperatura\": 72.5,
>
> \"pressao\": 6.8,
>
> \"corrente\": 12.4,
>
> \"estado\": \"ATENÇÃO\"
>
> }

As leituras serão armazenadas em uma única lista:

> historico = \[\]
>
> historico.append(leitura)

**2. Situação-problema**

O sistema de monitoramento precisa armazenar as leituras de um motor
industrial.

Cada leitura deverá conter:

• Número do ciclo;

• Código do equipamento;

• Dispositivo de coleta;

• Temperatura;

• Pressão;

• Corrente;

• Estado da temperatura;

• Estado da pressão;

• Estado da corrente;

• Estado geral;

• Indicação de situação crítica.

O supervisor deseja consultar uma leitura completa sem precisar acessar
várias listas diferentes.

No modelo anterior, para exibir uma leitura, era necessário utilizar
vários índices:

> print(historico_ciclos\[indice\])
>
> print(historico_temperatura\[indice\])
>
> print(historico_pressao\[indice\])
>
> print(historico_corrente\[indice\])
>
> print(historico_estados\[indice\])

Com dicionários, todas as informações da leitura ficam agrupadas:

> leitura = {
>
> \"ciclo\": 1,
>
> \"temperatura\": 72.5,
>
> \"pressao\": 6.8,
>
> \"corrente\": 12.4,
>
> \"estado_geral\": \"ATENÇÃO\"
>
> }

**3. Objetivos da aula**

Ao final da aula, o estudante deverá ser capaz de:

• Criar dicionários em Python;

• Diferenciar chaves e valores;

• Acessar valores por meio de chaves;

• Inserir e alterar informações em um dicionário;

• Criar uma lista de dicionários;

• Armazenar registros completos de leituras;

• Percorrer uma lista de dicionários com for;

• Filtrar registros por estado;

• Identificar leituras críticas;

• Calcular estatísticas a partir de uma lista de registros;

• Organizar dados para futura gravação em arquivo ou banco de dados.

**4. Produto final da aula**

Ao final da aula, cada estudante ou dupla deverá possuir um programa
que:

1\. Simule vários ciclos de coleta;

2\. Crie um dicionário para cada leitura;

3\. Armazene os dicionários em uma lista;

4\. Exiba os registros completos;

5\. Filtre leituras em situação de alarme;

6\. Identifique ciclos críticos;

7\. Calcule estatísticas;

8\. Mostre um resumo organizado;

9\. Preserve os dados em uma estrutura adequada para as próximas aulas.

**5. Conhecimentos utilizados**

Esta aula utilizará:

• Variáveis;

• Tipos de dados;

• Listas;

• Dicionários;

• Estruturas condicionais;

• Estruturas de repetição;

• Funções;

• Operadores relacionais;

• Operadores lógicos;

• Simulação com random;

• Formatação de textos com f-strings.

**6. Retomada da Aula 4**

Na Aula 4, o programa utilizava listas paralelas para armazenar o
histórico:

> historico_ciclos = \[\]
>
> historico_temperatura = \[\]
>
> historico_pressao = \[\]
>
> historico_corrente = \[\]
>
> historico_estados = \[\]

Durante cada ciclo, os valores eram adicionados:

> historico_ciclos.append(numero_ciclo)
>
> historico_temperatura.append(temperatura)
>
> historico_pressao.append(pressao)
>
> historico_corrente.append(corrente)
>
> historico_estados.append(estado_geral)

Para exibir uma leitura completa, era necessário utilizar o mesmo índice
em várias listas:

> for indice in range(len(historico_ciclos)):
>
> print(f\"Ciclo: {historico_ciclos\[indice\]}\")
>
> print(
>
> f\"Temperatura: \"
>
> f\"{historico_temperatura\[indice\]:.2f} °C\"
>
> )
>
> print(
>
> f\"Pressão: \"
>
> f\"{historico_pressao\[indice\]:.2f} bar\"
>
> )
>
> print(
>
> f\"Corrente: \"
>
> f\"{historico_corrente\[indice\]:.2f} A\"
>
> )
>
> print(
>
> f\"Estado: \"
>
> f\"{historico_estados\[indice\]}\"
>
> )

Esse modelo pode gerar problemas se:

• Uma lista receber um valor e outra não;

• Um valor for inserido em posição incorreta;

• Uma leitura inválida for armazenada parcialmente;

• O índice utilizado não for o mesmo em todas as listas;

• Novos campos precisarem ser adicionados ao registro.

Na Aula 5, todos os dados de uma leitura serão armazenados juntos.

**7. O que é um dicionário?**

Um dicionário é uma estrutura de dados formada por pares de:

• Chave;

• Valor.

Exemplo:

> equipamento = {
>
> \"codigo\": \"M-01\",
>
> \"tipo\": \"Motor\",
>
> \"setor\": \"Produção\"
>
> }

Nesse exemplo:

• \"codigo\" é uma chave;

• \"M-01\" é o valor associado à chave;

• \"tipo\" é uma chave;

• \"Motor\" é o valor associado à chave;

• \"setor\" é uma chave;

• \"Produção\" é o valor associado à chave.

A estrutura geral é:

> dicionario = {
>
> \"chave\": valor,
>
> \"outra_chave\": outro_valor
>
> }

**8. Criando um dicionário de leitura**

Crie um dicionário para representar uma leitura:

> leitura = {
>
> \"ciclo\": 1,
>
> \"temperatura\": 72.5,
>
> \"pressao\": 6.8,
>
> \"corrente\": 12.4,
>
> \"estado_geral\": \"ATENÇÃO\"
>
> }

Exiba o dicionário completo:

> print(leitura)

Resultado possível:

> {
>
> \'ciclo\': 1,
>
> \'temperatura\': 72.5,
>
> \'pressao\': 6.8,
>
> \'corrente\': 12.4,
>
> \'estado_geral\': \'ATENÇÃO\'
>
> }

O dicionário pode conter valores de diferentes tipos:

> leitura = {
>
> \"ciclo\": 1,
>
> \"temperatura\": 72.5,
>
> \"pressao\": 6.8,
>
> \"corrente\": 12.4,
>
> \"estado_geral\": \"ATENÇÃO\",
>
> \"emergencia\": False
>
> }

**9. Acessando valores por meio de chaves**

Para acessar um valor, utilize a chave entre colchetes:

> print(leitura\[\"ciclo\"\])
>
> print(leitura\[\"temperatura\"\])
>
> print(leitura\[\"estado_geral\"\])

Para exibir uma leitura formatada:

> print(f\"Ciclo: {leitura\[\'ciclo\'\]}\")
>
> print(
>
> f\"Temperatura: \"
>
> f\"{leitura\[\'temperatura\'\]:.2f} °C\"
>
> )
>
> print(
>
> f\"Pressão: \"
>
> f\"{leitura\[\'pressao\'\]:.2f} bar\"
>
> )
>
> print(
>
> f\"Corrente: \"
>
> f\"{leitura\[\'corrente\'\]:.2f} A\"
>
> )
>
> print(f\"Estado: {leitura\[\'estado_geral\'\]}\")

**Verificando se uma chave existe**

A chave precisa existir no dicionário.

O código abaixo gera erro:

> print(leitura\[\"umidade\"\])

Para verificar se uma chave existe:

> if \"umidade\" in leitura:
>
> print(leitura\[\"umidade\"\])
>
> else:
>
> print(\"A chave umidade não existe.\")

Também é possível utilizar get():

> umidade = leitura.get(\"umidade\")
>
> if umidade is None:
>
> print(\"Umidade não cadastrada.\")
>
> else:
>
> print(f\"Umidade: {umidade}\")

**10. Inserindo novos campos**

Um novo campo pode ser criado atribuindo um valor a uma nova chave:

> leitura\[\"equipamento\"\] = \"M-01\"
>
> leitura\[\"dispositivo\"\] = \"CLP-SIM-01\"

O dicionário passará a conter os novos campos.

Também é possível adicionar o resultado de uma avaliação:

> leitura\[\"temperatura_acima_limite\"\] = True

Ou armazenar uma observação:

> leitura\[\"observacao\"\] = (
>
> \"Verificar sistema de refrigeração\"
>
> )

**11. Alterando valores**

Para alterar um valor existente:

> leitura\[\"estado_geral\"\] = \"ALARME\"

A temperatura também pode ser atualizada:

> leitura\[\"temperatura\"\] = 84.0

Exemplo completo:

> leitura = {
>
> \"ciclo\": 1,
>
> \"temperatura\": 72.5,
>
> \"estado_geral\": \"ATENÇÃO\"
>
> }
>
> leitura\[\"temperatura\"\] = 84.0
>
> leitura\[\"estado_geral\"\] = \"ALARME\"
>
> print(leitura)

**12. Removendo campos**

Para remover uma chave e seu valor:

> del leitura\[\"observacao\"\]

Outra forma é utilizar pop():

> observacao = leitura.pop(\"observacao\")
>
> print(observacao)

Antes de remover uma chave, verifique se ela existe:

> if \"observacao\" in leitura:
>
> del leitura\[\"observacao\"\]

**13. Desafio 1 --- Criando um registro simples**

Crie um dicionário que represente uma leitura:

> leitura = {
>
> \"ciclo\": 1,
>
> \"temperatura\": 75.0,
>
> \"pressao\": 7.2,
>
> \"corrente\": 13.5,
>
> \"estado_geral\": \"ATENÇÃO\"
>
> }

Exiba cada informação:

> print(f\"Ciclo: {leitura\[\'ciclo\'\]}\")
>
> print(
>
> f\"Temperatura: \"
>
> f\"{leitura\[\'temperatura\'\]:.2f} °C\"
>
> )
>
> print(
>
> f\"Pressão: \"
>
> f\"{leitura\[\'pressao\'\]:.2f} bar\"
>
> )
>
> print(
>
> f\"Corrente: \"
>
> f\"{leitura\[\'corrente\'\]:.2f} A\"
>
> )
>
> print(f\"Estado: {leitura\[\'estado_geral\'\]}\")

Adicione ao dicionário:

• Código do equipamento;

• Dispositivo de coleta;

• Estado da temperatura;

• Estado da pressão;

• Estado da corrente;

• Indicação de emergência.

> leitura\[\"equipamento\"\] = \"M-01\"
>
> leitura\[\"dispositivo\"\] = \"CLP-SIM-01\"
>
> leitura\[\"status_temperatura\"\] = \"ATENÇÃO\"
>
> leitura\[\"status_pressao\"\] = \"ATENÇÃO\"
>
> leitura\[\"status_corrente\"\] = \"ATENÇÃO\"
>
> leitura\[\"emergencia\"\] = False

**14. Lista de dicionários**

Uma lista pode armazenar vários dicionários:

> historico = \[\]

Crie o primeiro registro:

> leitura_1 = {
>
> \"ciclo\": 1,
>
> \"temperatura\": 72.5,
>
> \"pressao\": 6.8,
>
> \"corrente\": 12.4,
>
> \"estado_geral\": \"NORMAL\"
>
> }

Ad o registro à lista:

> historico.append(leitura_1)

Crie o segundo registro:

> leitura_2 = {
>
> \"ciclo\": 2,
>
> \"temperatura\": 81.0,
>
> \"pressao\": 8.2,
>
> \"corrente\": 15.5,
>
> \"estado_geral\": \"ALARME\"
>
> }

Adicione o segundo registro:

> historico.append(leitura_2)

Exiba o histórico:

> print(historico)

**15. Acessando registros específicos**

Para acessar o primeiro registro:

> print(historico\[0\])

Para acessar o segundo registro:

> print(historico\[1\])

Para acessar a temperatura do primeiro registro:

> print(historico\[0\]\[\"temperatura\"\])

Para acessar o estado do segundo registro:

> print(historico\[1\]\[\"estado_geral\"\])

Para acessar a última leitura:

> print(historico\[-1\])

Para acessar a temperatura da última leitura:

> print(historico\[-1\]\[\"temperatura\"\])

A estrutura possui dois níveis de acesso:

> historico\[indice\]\[\"chave\"\]

Exemplo:

> historico\[\]\[\"pressao\"\]

**16. Percorrendo uma lista de dicionários**

Utilize for para percorrer os registros:

> for leitura in historico:
>
> print(leitura)

Para exibir os campos individualmente:

> for leitura in historico:
>
> print()
>
> print(f\"Ciclo: {leitura\[\'ciclo\'\]}\")
>
> print(
>
> f\"Temperatura: \"
>
> f\"{leitura\[\'temperatura\'\]:.2f} °C\"
>
> )
>
> print(
>
> f\"Pressão: \"
>
> f\"{leitura\[\'pressao\'\]:.2f} bar\"
>
> )
>
> print(
>
> f\"Corrente: \"
>
> f\"{leitura\[\'corrente\'\]:.2f} A\"
>
> )
>
> print(
>
> f\"Estado: \"
>
> f\"{leitura\[\'estado_geral\'\]}\"
>
> )

**17. Desafio 2 --- Criando vários registros**

Crie uma lista chamada historico:

> historico = \[\]

Depois, crie três registros:

> leitura_1 = {
>
> \"ciclo\": 1,
>
> \"temperatura\": 65.0,
>
> \"pressao\": 6.0,
>
> \"corrente\": 11.5,
>
> \"estado_geral\": \"NORMAL\"
>
> }
>
> leitura_2 = {
>
> \"ciclo\": 2,
>
> \"temperatura\": 76.0,
>
> \"pressao\": 7.5,
>
> \"corrente\": 13.2,
>
> \"estadogeral\": \"ATENÇÃO\"
>
> }
>
> leitura_3 = {
>
> \"ciclo\": 3,
>
> \"temperatura\": 85.0,
>
> \"pressao\": 8.5,
>
> \"corrente\": 16.0,
>
> \"estado_geral\": \"ALARME\"
>
> }

Adicione os registros:

> historico.append(leitura_1)
>
> historico.append(leitura_2)
>
> historico.append(leitura_3)

Exiba todos os registros:

> for leitura in historico:
>
> print(
>
> f\"Ciclo {leitura\[\'ciclo\'\]}: \"
>
> f\"{leitura\[\'estado_geral\'\]}\"
>
> )

**18. Criando registros diretamente com append()**

Também é possível criar o dicionário diretamente dentro do append():

> historico = \[\]
>
> historico.append({
>
> \"ciclo\": 1,
>
> \"temperatura\": 65.0,
>
> \"pressao\": 6.0,
>
> \"corrente\": 11.5,
>
> \"estado_geral\": \"NORMAL\"
>
> })
>
> historico.append({
>
> \"ciclo\": 2,
>
> \"temperatura\": 76.0,
>
> \"pressao\": 7.5,
>
> \"corrente\": 13.2,
>
> \"estado_geral\": \"ATENÇÃO\"
>
> })
>
> historico.append({
>
> \"ciclo\": 3,
>
> \"temperatura\": 85.0,
>
> \"pressao\": 8.5,
>
> \"corrente\": 16.0,
>
> estado_geral\": \"ALARME\"
>
> })

Essa forma é útil quando os dados já estão disponíveis.

**19. Criando registros dentro de um laço**

O dicionário pode ser criado dentro do laço de simulação:

> import random
>
> historico = \[\]
>
> for ciclo in range(5):
>
> numero_ciclo = ciclo + 1
>
> temperatura = random.randint(60, 95)
>
> pressao = random.uniform(5.0, 10.0)
>
> corrente = random.uniform(10.0, 20.0)
>
> leitura = {
>
> \"ciclo\": numero_ciclo,
>
> \"temperatura\": temperatura,
>
> \"pressao\": pressao,
>
> \"corrente\": corrente,
>
> \"estado_geral\": \"EM ANÁLISE\"
>
> }
>
> historico.append(leitura)
>
> for leitura in historico:
>
> print(leitura)

**20. Incluindo os estados dos sensores**

O registro pode armazenar o estado de cada sensor:

> leitura = {
>
> \"ciclo\": numero_ciclo,
>
> \"temperatura\": temperatura,
>
> \"pressao\": pressao,
>
> \"corrente\": corrente,
>
> \"status_temperatura\": status_temperatura,
>
> \"status_pressao\": status_pressao,
>
> \"status_corrente\": status_corrente,
>
> \"estado_geral\": estado_geral
>
> }

Também pode armazenar informações booleanas:

> leitura\[\"temperatura_acima_limite\"\] = (
>
> temperatura \> limite_temperatura
>
> )
>
> leitura\[\"pressao_acima_limite\"\] = (
>
> pressao \> limite_pressao
>
> )
>
> leitura\[\"corrente_acima_limite\"\] = (
>
> corrente \> limite_corrente
>
> )
>
> leitura\[\"situacao_critica\"\] = situacao_critica

**21. Modelo completo de um registro**

Um registro completo poderá possuir a seguinte estrutura:

> leitura = {
>
> \"ciclo\": numero_ciclo,
>
> \"equipamento\": codigo_equipamento,
>
> \"dispositivo\": dispositivo_coleta,
>
> \"temperatura\": temperatura,
>
> \"pressao\": pressao,
>
> \"corrente\": corrente,
>
> \"status_temperatura\": status_temperatura,
>
> \"status_pressao\": status_pressao,
>
> \"status_corrente\": status_corrente,
>
> \"estado_geral\": estado_geral,
>
> \"temperatura_acima_limite\": (
>
> temperatura \> limite_temperatura
>
> ),
>
> \"pressao_acima_limite\": (
>
> pressao \> limite_pressao
>
> ),
>
> \"corrente_acima_limite\": (
>
> corrente \> limite_corrente
>
> ),
>
> \"situacao_critica\": situacao_critica
>
> }

**22. Desafio 3 --- Integrando com o simulador**

Utilize o programa da Aula 4.

Substitua as listas paralelas:

> historico_ciclos = \[\]
>
> historico_temperatura = \[\]
>
> historico_pressao = \[\]
>
> historico_corrente = \[\]
>
> historico_estados = \[\]

Por uma única lista:

> historico = \[\]

Depois da classificação do estado geral, crie o registro:

> leitura = {
>
> \"ciclo\": numero_ciclo,
>
> \"equipamento\": codigo_equipamento,
>
> \"dispositivo\": dispositivo_coleta,
>
> \"temperatura\": temperatura,
>
> \"pressao\": pressao,
>
> \"corrente\": corrente,
>
> \"status_temperatura\": status_temperatura,
>
> \"status_pressao\": status_pressao,
>
> \"status_corrente\": status_corrente,
>
> \"estado_geral\": estado_geral,
>
> \"situacao_critica\": situacao_critica
>
> }

Adicione o registro ao histórico:

> historico.append(leitura)

A partir desse ponto, as informações deverão ser consultadas no
dicionário.

**23. Exibindo o histórico integrado**

Depois do laço principal:

> print()
>
> print(\"==========================================\")
>
> print(\" HISTÓRICO DE LEITURAS\")
>
> print(\"==========================================\")
>
> for leitura in historico:
>
> print()
>
> print(f\"Ciclo: {leitura\[\'ciclo\'\]}\")
>
> print(
>
> f\"Equipamento: \"
>
> f\"{leitura\[\'equipamento\'\]}\"
>
> )
>
> print(
>
> f\"Dispositivo: \"
>
> f\"{leitura\[\'dispositivo\'\]}\"
>
> )
>
> print(
>
> f\"Temperatura: \"
>
> f\"{leitura\[\'temperatura\'\]:.2f} °C\"
>
> )
>
> print(
>
> f\"Status da temperatura: \"
>
> f\"{leitura\[\'status_temperatura\'\]}\"
>
> )
>
> print(
>
> f\"Pressão: \"
>
> f\"{leitura\[\'pressao\'\]:.2f} bar\"
>
> )
>
> print(
>
> f\"Status
