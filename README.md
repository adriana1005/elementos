
## Elementos de Inteligência Artificial e Ciência de Dados - Trabalho Prático 
## Descrição do Trabalho
Este projeto é um package Python desenvolvido para análise de dados extraídos do PORDATA, focando na relação entre:
- **Taxa de retenção e desistência no ensino secundário por modalidade de ensino e ano de escolaridade**
- **Ganho médio mensal (GMM)**
- **Beneficiários do Rendimento Social de Inserção (RSI) por grupo etário** 

O objetivo principal é permitir que os dados sejam analisados de forma eficiente, gerando insights sobre as variáveis em estudo e a relação entre elas.

---


## Estrutura do package
Para a realização deste package foi necessário seguir estes passos:
1. **Integração de Dados:** após a recolha, criámos um Excel com todos os dados entre os anos de 2012 e 2022


2. **Análise Exploratória e Limpeza e Preprocessamento de Dados:**
- Uso de estatísticas descritivas (média, moda, mediana, ...) através do describe()
- **Tratamento de Outliers**:
  - Deteção por IQR 
  - Winsorização
- **Normalização** (MinMaxScaler)


3. **Visualização de Dados:**
- Diagramas de Caixa
- Mapas de Correlação
- Gráficos de Barras 

---

## Estrutura do Trabalho
```
projeto/
|- funcoes
   |- recolha.py
   |- valores_em_falta.py
   |- outliers.py
   |- normalizacao.py
   |- analise_preditiva.py
|- projeto
|- main.py
|- README.md
|- requirements.txt
|- setup.py
```

---

## Requesitos

Para executar este projeto, é necessário ter instaladas as seguintes dependências:

```bash
pip install pandas
pip install matplotlib
pip install numpy
pip install scikit-learn
pip install seaborn
```
---

## Como Executar

### 1. **Executar o Script Principal**
Corra o 'main.py':
```bash
python main.py
```

--------------------------------------------------------------------------------------------------

## Exportação de Resultados
Os resultados das análises são exportados automaticamente para os seguintes ficheiros CSV:
   - dadostratados.csv
   - dados_preenchidos1.csv
   - gmm_inf.csv
   - gmm_sup.csv
   - rsi_inf.csv
   - rsi_sup.csv


--------------------------------------------------------------------------------------------------

## Autores
   - **Nome**: Adriana Abreu, 53672 (Github: adriana1005 )
   - **Nome**: Leonor Rebola, 53663 (Github: leonorrebola9)