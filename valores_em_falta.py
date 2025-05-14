from recolha import *

from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from scipy.stats import zscore

df, ano, municipio, curso, ano_escolar, valor_alunos, valor_rsi, valor_gmm = recolha()

def valores_em_falta(faltar):
    '''funçao geral para todos os valores'''
    return faltar.isnull().sum()


def faltar_valores_alunos(valor_alunos):
    '''valores em falta da desistência escolar em percentagem'''
    print(faltar_valores_alunos(valor_alunos))

    df = pd.read_csv('elementos.csv')

    # Remover linhas com NaN na coluna 'email'
    df.dropna(subset=['Valor Alunos'], inplace=True)

    # Salvar o DataFrame modificado em um novo CSV
    df.to_csv('dados_sem_nulos.csv', index=False)
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



'''
# Nome da coluna numérica
coluna = 'Valor Alunos'

# Calcula o z-score de todos os dados
df['zscore_valor_alunos'] = zscore(df[coluna])

# Marca se o valor está dentro do intervalo [-3, 3]
df['zscore_bool_valor_alunos'] = df['zscore_valor_alunos'].between(-3, 3)

# Salva o DataFrame com todas as informações
df.to_csv("dados_com_zscore1.csv", index=False)

print("Arquivo salvo como 'dados_com_zscore.csv'")
'''

'''
coluna = 'Valor RSI '

# Calcula o z-score de todos os dados
df['zscore_valor_rsi'] = zscore(df[coluna])

# Marca se o valor está dentro do intervalo [-3, 3]
df['zscore_bool_valor_rsi'] = df['zscore_valor_rsi'].between(-3, 3)

# Salva o DataFrame com todas as informações
df.to_csv("dados_com_zscore2.csv", index=False)

print("Arquivo salvo como 'dados_com_zscore.csv'")

'''

coluna = 'Valor GMM'

# Calcula o z-score de todos os dados
df['zscore_valor_gmm'] = zscore(df[coluna])

# Marca se o valor está dentro do intervalo [-3, 3]
df['zscore_bool_valor_gmm'] = df['zscore_valor_gmm'].between(-3, 3)

# Salva o DataFrame com todas as informações
df.to_csv("dados_com_zscore3.csv", index=False)

print("Arquivo salvo como 'dados_com_zscore.csv'")