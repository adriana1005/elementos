import numpy as np
import pandas as pd
from scipy.stats import zscore


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