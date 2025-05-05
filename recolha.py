import pandas as pd


def recolha():
    '''
    separar os dados pelas várias variaveis
    '''
    df = pd.read_csv('elementoscsv.csv', sep=';', encoding='latin1')
    ano = df['Ano'] #2012 a 2022
    municipio = df['Regiao']
    curso = df['Curso'] #Profissional ou Ensino Normal
    ano_escolar = df['Ano Escolar'] #10 ao 12
    valor_alunos = df['Valor Alunos'] #valor de desistência escolar em percentagem
    valor_rsi = df['Valor RSI '] #valor de pessoas que recebem o rendimento social de inserção
    valor_gmm = df['Valor GMM'] #valor em euros do ganho medio mensal
    missing_values = df.isnull().sum()
    print(missing_values)

    return df, ano, municipio, curso, ano_escolar, valor_alunos, valor_rsi, valor_gmm

'''
df, ano, municipio, curso, ano_escolar, valor_alunos, valor_rsi, valor_gmm = recolha()
missing_values = df.isnull().sum()
print(missing_values)
print(df.columns)
'''

