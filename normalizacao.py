from recolha import *
from sklearn.preprocessing import MinMaxScaler


df, ano, municipio, curso, ano_escolar, valor_alunos, valor_rsi, valor_gmm = recolha()

def normalisealunos():
    scaler = MinMaxScaler()

    # Aplicar a normalização
    df['valor_alunos_minmax'] = scaler.fit_transform(df[['Valor Alunos']])
    df["valor_alunos_minmax"] = df["valor_alunos_minmax"].round(3)

        # 3. Salvar o novo CSV com a nova coluna
    df.to_csv("dados_com_zscore1.csv", sep=";", index=False)

normalisealunos()

def normaliseRSI():
    scaler = MinMaxScaler()

    # Aplicar a normalização
    df['valor_RSI_minmax'] = scaler.fit_transform(df[['Valor RSI']])
    df["valor_RSI_minmax"] = df["valor_RSI_minmax"].round(3)

        # 3. Salvar o novo CSV com a nova coluna
    df.to_csv("dados_com_zscore1.csv", sep=";", index=False)

normaliseRSI()

def normaliseGMM():
    scaler = MinMaxScaler()

    # Aplicar a normalização
    df['valor_GMM_minmax'] = scaler.fit_transform(df[['Valor GMM']])
    df["valor_GMM_minmax"] = df["valor_GMM_minmax"].round(3)

        # 3. Salvar o novo CSV com a nova coluna
    df.to_csv("dados_com_zscore1.csv", sep=";", index=False)

normaliseGMM()