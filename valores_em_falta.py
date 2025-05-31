from recolha import *


dff, anof, municipiof, cursof, anoescolarf, alunosf, rsi_f, gmm_f = recolhaantesfalta()
print(dff.describe())

def valores_em_falta(faltar):
    '''função geral para todos os valores'''
    return faltar.isnull().sum()


def faltar_valores_alunos(valor_alunos):
    '''valores em falta da desistência escolar em percentagem'''
    media_valores = dff['Valor Alunos'].mean()
    dff['Valor Alunos'] = dff['Valor Alunos'].fillna(media_valores)

    # 4. Salvar o DataFrame com os vlores imputados num novo CSV
    dff.to_csv('dados_imputados_media.csv', index=False)


    return valores_em_falta(valor_alunos)


def faltar_valor_rsi(valor_rsi):
    '''valores em falta rendimento social de inserção'''
    print(faltar_valor_rsi(valor_rsi))
    return valores_em_falta(valor_rsi)


def faltar_valor_gmm(valor_gmm):
    '''valores em falta do ganho médio mensal'''
    print(faltar_valor_gmm(valor_gmm))
    return valores_em_falta(valor_gmm)
'''
print(df.describe()) # para saber média, quartis, desvio padrão

df.fillna(df.median(numeric_only=True), inplace=True)

# Guardar o novo ficheiro CSV
df.to_csv("dados_imputados.csv", index=False)'''

#Iterative Imputation with Scikit-learn
#https://towardsdatascience.com/iterative-imputation-with-scikit-learn-8f3eb22b1a38/
# por causa do z-score
#https://www.investopedia.com/terms/z/zscore.asp#:~:text=In%20investing%20and%20trading%2C%20Z-scores%20are%20measures%20of,to%20the%20mean%20in%20a%20group%20of%20scores.
'''
original_columns = df.columns.tolist()  # Salva a ordem original

# --- SEPARAR COLUNAS NUMÉRICAS E CATEGÓRICAS ---
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_cols = [col for col in original_columns if col not in numeric_cols]

# --- IMPUTAÇÃO E ARREDONDAMENTO DAS COLUNAS NUMÉRICAS ---
if numeric_cols:  # Só executa se houver colunas numéricas
    imputer = IterativeImputer(max_iter=10, random_state=42)
    df_numeric_imputed = pd.DataFrame(
        imputer.fit_transform(df[numeric_cols]),
        columns=numeric_cols
    )
    df_numeric_imputed = df_numeric_imputed.round(1)  # 1 casa decimal
else:
    df_numeric_imputed = pd.DataFrame()

# --- TRATAR COLUNAS CATEGÓRICAS (PREENCHER COM MODA) ---
df_categorical_imputed = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])

# --- RECRIAR O DATAFRAME COM A ORDEM ORIGINAL ---
df_final = pd.concat([df_numeric_imputed, df_categorical_imputed], axis=1)
df_final = df_final[original_columns]  # Reordena as colunas

# --- SALVAR O CSV ---
df_final.to_csv("dados_preenchidos1.csv", index=False, sep=';')
'''
