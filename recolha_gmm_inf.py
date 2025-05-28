import pandas as pd


def recolha_gmm_inf():
    '''
    separar os dados pelas várias variaveis
    '''
    df = pd.read_csv('.csv', sep=';', encoding='latin1')
    ano = df['Ano']  # 2012 a 2022
    municipio = df['Regiao']
    alunos1 = df['Alunos10CGeral']
    alunos2 = df['Alunos10CProfissional']
    alunos3 = df['Alunos11CGeral']
    alunos4 = df['Alunos11CProfissional']
    alunos5 = df['Alunos12CGeral']
    alunos6 = df['Alunos12CProfissional']
    valor_rsi = df['valor_RSI']  # valor de pessoas que recebem o rendimento social de inserção
    valor_gmm = df['valor_GMM']  # valor em euros do ganho medio mensal

    return df, ano, municipio, alunos1, alunos2, alunos3, alunos4, alunos5, alunos6, valor_rsi, valor_gmm


'''
df, ano, municipio, curso, ano_escolar, valor_alunos, valor_rsi, valor_gmm = recolha()
missing_values = df.isnull().sum()
print(missing_values)
print(df.columns)
'''

