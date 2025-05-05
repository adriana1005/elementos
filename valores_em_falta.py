from recolha import *

df, ano, municipio, curso, ano_escolar, valor_alunos, valor_rsi, valor_gmm = recolha()

def valores_em_falta(faltar):
    '''funçao geral para todos os valores'''
    return faltar.isnull().sum()


def faltar_valores_alunos(valor_alunos):
    '''valores em falta da desistência escolar em percentagem'''
    print(faltar_valores_alunos(valor_alunos))
    return valores_em_falta(valor_alunos)


def faltar_valor_rsi(valor_rsi):
    '''valores em falta rendimento social de inserção'''
    print(faltar_valor_rsi(valor_rsi))
    return valores_em_falta(valor_rsi)


def faltar_valor_gmm(valor_gmm):
    '''valores em falta do ganho médio mensal'''
    print(faltar_valor_gmm(valor_gmm))
    return valores_em_falta(valor_gmm)




