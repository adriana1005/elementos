import pandas as pd
from recolha import recolha

df = recolha()

def valores_em_falta(df, nome_coluna):
    faltar = df[nome_coluna].isnull().sum()
    return faltar

def faltar_ano(df):
    return valores_em_falta(df, "Ano")

def faltar_regiao(df):
    return valores_em_falta(df, "Regiao")

def faltar_curso(df):
    return valores_em_falta(df, "Curso")

def faltar_ano_escolar(df):
    return valores_em_falta(df, "Ano Escolar")

def faltar_valores_alunos(df):
    return valores_em_falta(df, "Valor Alunos")

def faltar_valor_rsi(df):
    return valores_em_falta(df, "Valor RSI ")

def faltar_valor_gmm(df):
    return valores_em_falta(df, "Valor GMM")

faltar_ano(df)
faltar_regiao(df)
faltar_curso(df)
faltar_ano_escolar(df)
faltar_valores_alunos(df)
faltar_valor_rsi(df)
faltar_valor_gmm(df)