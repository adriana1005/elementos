import pandas as pd

def recolha():
    '''
    separar os dados pelas várias variaveis
    '''
    df = pd.read_csv('dadostratados.csv', sep=';', encoding='latin1')
    ano = df['Ano'] #2012 a 2022
    municipio = df['Regiao']
    alunos1 = df['Alunos10CGeral']
    alunos2 = df['Alunos10CProfissional']
    alunos3 = df['Alunos11CGeral']
    alunos4 = df['Alunos11CProfissional']
    alunos5 = df['Alunos12CGeral']
    alunos6 = df['Alunos12CProfissional']
    valor_rsi = df['valor_RSI'] #valor de pessoas que recebem o rendimento social de inserção
    valor_gmm = df['valor_GMM'] #valor em euros do ganho medio mensal
    
    

    return df, ano, municipio, alunos1, alunos2, alunos3, alunos4, alunos5, alunos6, valor_rsi, valor_gmm

def recolha_rsi_inf():
    '''
    separar os dados pelas várias variaveis
    '''
    df_ri = pd.read_csv('rsi_inf.csv', sep=';', encoding='latin1')
    ano_ri = df_ri['Ano']  # 2012 a 2022
    municipio_ri = df_ri['Regiao']
    alunos1ri = df_ri['Alunos10CGeral']
    alunos2ri = df_ri['Alunos10CProfissional']
    alunos3ri = df_ri['Alunos11CGeral']
    alunos4ri = df_ri['Alunos11CProfissional']
    alunos5ri = df_ri['Alunos12CGeral']
    alunos6ri = df_ri['Alunos12CProfissional']
    valor_rsi_ri = df_ri['valor_RSI']  # valor de pessoas que recebem o rendimento social de inserção
    valor_gmm_ri = df_ri['valor_GMM']  # valor em euros do ganho medio mensal

    return df_ri, ano_ri, municipio_ri, alunos1ri, alunos2ri, alunos3ri, alunos4ri, alunos5ri, alunos6ri, valor_rsi_ri, valor_gmm_ri

def recolha_gmm_inf():
    '''
    separar os dados pelas várias variaveis
    '''
    df_gi = pd.read_csv('gmm_inf.csv', sep=';', encoding='latin1')
    ano_gi = df_gi['Ano']  # 2012 a 2022
    municipio_gi = df_gi['Regiao']
    alunos1gi = df_gi['Alunos10CGeral']
    alunos2gi = df_gi['Alunos10CProfissional']
    alunos3gi = df_gi['Alunos11CGeral']
    alunos4gi = df_gi['Alunos11CProfissional']
    alunos5gi = df_gi['Alunos12CGeral']
    alunos6gi = df_gi['Alunos12CProfissional']
    valor_rsi_gi = df_gi['valor_RSI']  # valor de pessoas que recebem o rendimento social de inserção
    valor_gmm_gi = df_gi['valor_GMM']  # valor em euros do ganho medio mensal

    return df_gi, ano_gi, municipio_gi, alunos1gi, alunos2gi, alunos3gi, alunos4gi, alunos5gi, alunos6gi, valor_rsi_gi, valor_gmm_gi


def recolha_gmm_sup():
    '''
    separar os dados pelas várias variaveis
    '''
    df_gs = pd.read_csv('gmm_sup.csv', sep=';', encoding='latin1')
    ano_gs = df_gs['Ano']  # 2012 a 2022
    municipio_gs = df_gs['Regiao']
    alunos1gs = df_gs['Alunos10CGeral']
    alunos2gs = df_gs['Alunos10CProfissional']
    alunos3gs = df_gs['Alunos11CGeral']
    alunos4gs = df_gs['Alunos11CProfissional']
    alunos5gs = df_gs['Alunos12CGeral']
    alunos6gs = df_gs['Alunos12CProfissional']
    valor_rsi_gs = df_gs['valor_RSI']  # valor de pessoas que recebem o rendimento social de inserção
    valor_gmm_gs = df_gs['valor_GMM']  # valor em euros do ganho medio mensal

    return df_gs, ano_gs, municipio_gs, alunos1gs, alunos2gs, alunos3gs, alunos4gs, alunos5gs, alunos6gs, valor_rsi_gs, valor_gmm_gs


def recolha_rsi_sup():
    '''
    separar os dados pelas várias variaveis
    '''
    df_rs = pd.read_csv('rsi_sup.csv', sep=';', encoding='latin1')
    ano_rs = df_rs['Ano']  # 2012 a 2022
    municipio_rs = df_rs['Regiao']
    alunos1rs = df_rs['Alunos10CGeral']
    alunos2rs = df_rs['Alunos10CProfissional']
    alunos3rs = df_rs['Alunos11CGeral']
    alunos4rs = df_rs['Alunos11CProfissional']
    alunos5rs = df_rs['Alunos12CGeral']
    alunos6rs = df_rs['Alunos12CProfissional']
    valor_rsi_rs = df_rs['valor_RSI']  # valor de pessoas que recebem o rendimento social de inserção
    valor_gmm_rs = df_rs['valor_GMM']  # valor em euros do ganho medio mensal

    return df_rs, ano_rs, municipio_rs, alunos1rs, alunos2rs, alunos3rs, alunos4rs, alunos5rs, alunos6rs, valor_rsi_rs, valor_gmm_rs
'''
df, ano, municipio, curso, ano_escolar, valor_alunos, valor_rsi, valor_gmm = recolha()
missing_values = df.isnull().sum()
print(missing_values)
print(df.columns)
'''

def recolha_zscore():
    '''
    separar os dados pelas várias variaveis
    '''
    df_z = pd.read_csv('dados_com_zscore1.csv', sep=';', encoding='latin1')
    ano_z = df_z['Ano']  # 2012 a 2022
    municipio_z = df_z['Regiao']
    anoescolar = df_z['Ano Escolar']
    valor_alunos_z = df_z['Valor Alunos']
    valor_rsi_z = df_z['Valor RSI']
    valor_gmm_z = df_z['Valor GMM']
    zscore_alunos = df_z['zscore_valor_alunos']
    zscore_alunosb = df_z['zscore_bool_valor_alunos']
    zscore_rsi = df_z['zscore_valor_rsi']
    zscore_rsib = df_z['zscore_bool_valor_rsi']
    zscore_gmm = df_z['zscore_valor_gmm']  
    zscore_gmmb = df_z['zscore_bool_valor_gmm'] 
    alunos_normalizado = df_z['valor_alunos_minmax']
    rsi_normalizado = df_z['valor_RSI_minmax']
    gmm_normalizado = df_z['valor_GMM_minmax']

    return df_z, ano_z, municipio_z, anoescolar, valor_alunos_z, valor_rsi_z, valor_gmm_z, zscore_alunos, zscore_alunosb, zscore_rsi, zscore_gmm,  zscore_rsib, zscore_gmmb, alunos_normalizado, rsi_normalizado, gmm_normalizado   