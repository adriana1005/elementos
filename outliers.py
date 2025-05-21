from recolha import *
from sklearn.experimental import enable_iterative_imputer
from scipy.stats import zscore
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df, ano, municipio, curso, ano_escolar, valor_alunos, valor_rsi, valor_gmm = recolha()

print(df["Valor Alunos"].describe())

def zscore_alunos():
    pass


def zscore_rsi():
    coluna = 'Valor RSI '

    # Calcula o z-score de todos os dados
    df['zscore_valor_rsi'] = zscore(df[coluna])

    # Marca se o valor está dentro do intervalo [-3, 3]
    df['zscore_bool_valor_rsi'] = df['zscore_valor_rsi'].between(-3, 3)

    # Salva o DataFrame com todas as informações
    df.to_csv("dados_com_zscore_rsi.csv", index=False)

    print("Arquivo salvo como 'dados_com_zscore.csv'")


def zscore_gmm():
    coluna = 'Valor GMM'

    # Calcula o z-score de todos os dados
    df['zscore_valor_gmm'] = zscore(df[coluna])

    # Marca se o valor está dentro do intervalo [-3, 3]
    df['zscore_bool_valor_gmm'] = df['zscore_valor_gmm'].between(-3, 3)

    # Salva o DataFrame com todas as informações
    df.to_csv("dados_com_zscore_gmm.csv", index=False)

    print("Arquivo salvo como 'dados_com_zscore.csv'")



def graph():

    x1points = np.array(df['zscore_valor_alunos'])
    x2points = np.array(df['zscore_valor_rsi'])
    x3points = np.array(df['zscore_valor_gmm'])
    y1points = np.array(df['Valor Alunos'])
    y2points = np.array(df['Valor RSI '])
    y3points = np.array(df['Valor GMM'])


    plt.plot(x1points, y1points, label = 'Valor Alunos')
    plt.plot(x2points, y1points, label = 'Valor RSI')
    plt.plot(x3points, y1points, label = 'Valor GMM')
    plt.legend()
    plt.show()

    
def winsorizacaoalunos():

    # Coluna alvo
    col = df["Valor Alunos"]

    # Calcular Z-score
    z_scores = zscore(col)

    # Limite de Z-score (3 desvios padrão)
    limite = 3

    # Filtrar valores dentro do limite
    col_dentro = col[(z_scores >= -limite) & (z_scores <= limite)]

    # Definir mínimo e máximo aceitáveis
    valor_min = col_dentro.min()
    valor_max = col_dentro.max()

    # Fazer o capping (winsorizing manual)
    df["Valor Alunos Tratado"] = col.clip(lower=valor_min, upper=valor_max)

    # Verificar resultado
    print(df[["Valor Alunos", "Valor Alunos Tratado"]].describe())

    df.to_csv("dados_outliers_alunos.csv", index=False)
winsorizacaoalunos()

def winsorizacaorsi():

    # Coluna alvo
    col = df["Valor RSI"]

    # Calcular Z-score
    z_scores = zscore(col)

    # Limite de Z-score (3 desvios padrão)
    limite = 3

    # Filtrar valores dentro do limite
    col_dentro = col[(z_scores >= -limite) & (z_scores <= limite)]

    # Definir mínimo e máximo aceitáveis
    valor_min = col_dentro.min()
    valor_max = col_dentro.max()

    # Fazer o capping (winsorizing manual)
    df["Valor RSI TRATADO"] = col.clip(lower=valor_min, upper=valor_max)

    # Verificar resultado
    print(df[["Valor RSI", "Valor RSI TRATADO"]].describe())


    df.to_csv("dados_outliers_rsi.csv", index=False)



def winsorizacaogmm():

    # Coluna alvo
    col = df["Valor GMM"]

    # Calcular Z-score
    z_scores = zscore(col)

    # Limite de Z-score (3 desvios padrão)
    limite = 3

    # Filtrar valores dentro do limite
    col_dentro = col[(z_scores >= -limite) & (z_scores <= limite)]

    # Definir mínimo e máximo aceitáveis
    valor_min = col_dentro.min()
    valor_max = col_dentro.max()

    # Fazer o capping (winsorizing manual)
    df["Valor GMM TRATADO"] = col.clip(lower=valor_min, upper=valor_max)

    # Verificar resultado
    print(df[["Valor GMM", "Valor GMM TRATADO"]].describe())


    df.to_csv("dados_outliers_gmm.csv", index=False)


def iqralunos():
    sns.boxplot(y=df["Valor Alunos"])
    plt.show()

    coluna = "Valor Alunos"

    # 3. Calcula Q1, Q3 e IQR
    Q1 = df[coluna].quantile(0.25)
    Q3 = df[coluna].quantile(0.75)
    IQR = Q3 - Q1

    # 4. Define limites
    LI = Q1 - 1.5 * IQR
    LS = Q3 + 1.5 * IQR

    # 5. Identifica outliers
    outliers_sup = df[df[coluna] > LS][coluna]
    outliers_inf = df[df[coluna] < LI][coluna]

    # 6. Resultados
    min_sup = outliers_sup.min() if not outliers_sup.empty else None
    max_inf = outliers_inf.max() if not outliers_inf.empty else None

    print(f"Limite inferior (LI): {LI:.2f}")
    print(f"Limite superior (LS): {LS:.2f}")
    print(f"Maior outlier inferior: {max_inf}")
    print(f"Menor outlier superior: {min_sup}")
    '''Name: Valor Alunos, dtype: float64
    Limite inferior (LI): -15.35
    Limite superior (LS): 38.65
    Maior outlier inferior: None
    Menor outlier superior: 38.7
    '''

def iqrrsi():
    plt.figure(figsize=(3, 8))
    sns.boxplot(y=df["Valor RSI"])
    plt.show()

    coluna = "Valor RSI"

    # 3. Calcula Q1, Q3 e IQR
    Q1 = df[coluna].quantile(0.25)
    Q3 = df[coluna].quantile(0.75)
    IQR = Q3 - Q1

    # 4. Define limites
    LI = Q1 - 1.5 * IQR
    LS = Q3 + 1.5 * IQR

    # 5. Identifica outliers
    outliers_sup = df[df[coluna] > LS][coluna]
    outliers_inf = df[df[coluna] < LI][coluna]

    # 6. Resultados
    min_sup = outliers_sup.min() if not outliers_sup.empty else None
    max_inf = outliers_inf.max() if not outliers_inf.empty else None

    print(f"Limite inferior (LI): {LI:.2f}")
    print(f"Limite superior (LS): {LS:.2f}")
    print(f"Maior outlier inferior: {max_inf}")
    print(f"Menor outlier superior: {min_sup}")
iqrrsi()


def iqrgmm():
    sns.boxplot(y=df["Valor GMM"])
    plt.show()

    coluna = "Valor GMM"

    # 3. Calcula Q1, Q3 e IQR
    Q1 = df[coluna].quantile(0.25)
    Q3 = df[coluna].quantile(0.75)
    IQR = Q3 - Q1

    # 4. Define limites
    LI = Q1 - 1.5 * IQR
    LS = Q3 + 1.5 * IQR

    # 5. Identifica outliers
    outliers_sup = df[df[coluna] > LS][coluna]
    outliers_inf = df[df[coluna] < LI][coluna]

    # 6. Resultados
    min_sup = outliers_sup.min() if not outliers_sup.empty else None
    max_inf = outliers_inf.max() if not outliers_inf.empty else None

    print(f"Limite inferior (LI): {LI:.2f}")
    print(f"Limite superior (LS): {LS:.2f}")
    print(f"Maior outlier inferior: {max_inf}")
    print(f"Menor outlier superior: {min_sup}")

