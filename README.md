
## Elementos de Inteligência Artificial e Ciência de Dados - Trabalho Prático 
## Descrição do trabalho
Este projeto é um package Python desenvolvido para leitura, tratamento e análise de dados relativamente aos municípios de Portugal. Utiliza ficheiros CSV extraídos do **PORDATA** e implementa diversas funcionalidades, incluindo ,  e .


O objetivo principal é permitir que os dados sejam analisados de forma eficiente, gerando insights sobre os municípios com base nos dados fornecidos.

---

## Estrutura do package
Para a realização deste package foi necessário seguir estes passos:
1. **Recolha de Dados:** através do PORDATA, realizou-se a recolha dos dados em ficheiro CSV para a elaboração do package. Os dados tidos em conta foram:
    - **Taxa de retenção e desistência no ensino secundário por modalidade de ensino e ano de escolaridade**
    - **Ganho médio mensal**
    - **Beneficiários do Rendimento Social de Inserção (RSI) por grupo etário**


2. **Integração de Dados:** após a recolha, criámos um Excel com todos os dados entre os anos de 2012 e 2022


3. **Análise Exploratória de Dados:**
    - **Listar Companhias**: Cria uma lista com os nomes das companhias mencionadas.
    - **Contagem de Tweets por Companhia**: Mostra o número total de tweets por companhia.
    - **Filtrar tweets por Companhia**: Filtra e exibe os detalhes de tweets de uma companhia especifica(texto, sentimento, número de tweets e data).


4. **Limpeza e Processamento de Dados:**:
    - **Dia com mais Tweets**: Identifica o dia do mês com o maior número de tweets.
    - **Dia com mais Tweets**: Identifica o dia do mês com o maior número de tweets.
    - **Mês com mais ou menos Tweets**: Determina os meses com maior e menor quantidade de tweet.
    - **Distribuição Temporal**: Cria contadores de tweets por dia e mês para análise temporal detalhada.
 
    
5. **Análise Descritiva:**
    - **Gráfico de Sentimento**: Gera um gráfico de barras com a disribuição de sentimentos(positivo, negativo e neutro) por companhia aérea.
    - **Gráfico de Confiança**: Exibe a distribuição dos valores de confiança em intervalos definidos.
    - **Mapa de Localizações**: Gera um mapa interativo com as localizações associadas aos tweets, utilizando coordenadas geográficas.
    - **Ordenação de Sentimentos**: Ordena as companhias aéreas pela percentagem de sentimentos específicos.


6. **Exportação de Resultados**
    - **CSV**: Exporta os resultados das percentagens de sentimentos por companhia para um ficheiro CSV.

---

## Estrutura do Projeto
```
projeto/
|- funcoes
   |- recolha.py
   |- valores_em_falta.py
   |- outliers.py
|- projeto
|- ven
|- main.py
|- README.md
|- requirements.txt
|- setup.py
```

---

## Requesitos

Para executar este projeto, é necessário ter instaladas as seguintes dependências:

```bash
pip install matplotlib

```

---

## Como Executar
### 1. **Descarregar a pasta zip**
- Para descarregar a pasta zip: [Twitter US Airline Sentiment](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment)
- Colocar o caminho do ficheiro 'Tweet.csv' em ler_documento.py dentro do projeto em path

### 2. **Executar o Script Principal**
Corra o 'main.py':
```bash
python main.py
```

### 3. **Exmplo de Uso**
#### Contar Sentimentos: 
``` python
count_sentiment()
```
**Saída**:
```
0  erro
9178  negative
2363  positive
3099 neutral
```

#### Filtar Tweets de uma Companha Específica
```python
filtrar_tweets_por_companhia("Delta")
```
**Saída**:
```
Texto: @JetBlue I hope so because I fly very often and would hate to change airlines.
Sentimento: neutral
Retweets: 0
Data: 2015-02-24 11:48:29 -0800
--------------------------------------------------------------------------------------------------
```





## Exportação de Resultados
Os resultados das análises são exportados automaticamente para os seguintes ficheiros:
   - **CSV**: 'sentimentos_companhias.csv'
   - **JSON**: 'sentimentos_companhias.json'
   - **Mapa**: 'mapa_tweets.html'


## Autores
   - **Nome**: Leonor Rebola, 53663 (Github: leonorrebola9)
   - **Nome**: Adriana Abreu, 53672 (Github: adriana1005 )
