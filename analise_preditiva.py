from recolha import *
import seaborn as sns
import matplotlib.pyplot as plt





df, ano, municipio, alunos1, alunos2, alunos3, alunos4, alunos5, alunos6, valor_rsi, valor_gmm = recolha()

df_ri, ano_ri, municipio_ri, alunos1ri, alunos2ri, alunos3ri, alunos4ri, alunos5ri, alunos6ri, valor_rsi_ri, valor_gmm_ri, valor_RSI_ri = recolha_rsi_inf()

df_rs, ano_rs, municipio_rs, alunos1rs, alunos2rs, alunos3rs, alunos4rs, alunos5rs, alunos6rs, valor_rsi_rs, valor_gmm_rs, valor_RSI_rs = recolha_rsi_sup()

df_gs, ano_gs, municipio_gs, alunos1gs, alunos2gs, alunos3gs, alunos4gs, alunos5gs, alunos6gs, valor_rsi_gs, valor_gmm_gs, valor_GMM_gs = recolha_gmm_sup()

df_gi, ano_gi, municipio_gi, alunos1gi, alunos2gi, alunos3gi, alunos4gi, alunos5gi, alunos6gi, valor_rsi_gi, valor_gmm_gi, valor_GMM_gi= recolha_gmm_inf()

#df_z, ano_z, municipio_z, anoescolar, valor_alunos_z, valor_rsi_z, valor_gmm_z, zscore_alunos, zscore_alunosb, zscore_rsi, zscore_gmm,  zscore_rsib, zscore_gmmb, alunos_normalizado, rsi_normalizado, gmm_normalizado = recolha_zscore()


def principal():
    dados = pd.DataFrame({
        "10º ano CG": alunos1,
        "10º ano CP:": alunos2,
        "11º ano CG:": alunos3,
        "11º ano CP:": alunos4,
        "12º ano CG:": alunos5,
        "12º ano CP:": alunos6,
        "Rendimento Social de Inserção():": valor_rsi,
        "Ganho médio mensal:": valor_gmm
    })

    corr_df = dados.corr(numeric_only=True)

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_df, annot=True, fmt=".2f", cmap="mako", square=True)
    plt.title("Matriz de Correlação")
    plt.tight_layout()
    plt.show()

def c_rsi_inf():
    dados = pd.DataFrame({
        "10º ano CG": alunos1ri,
        "10º ano CP:": alunos2ri,
        "11º ano CG:": alunos3ri,
        "11º ano CP:": alunos4ri,
        "12º ano CG:": alunos5ri,
        "12º ano CP:": alunos6ri,
        "Rendimento Social de Inserção:": valor_rsi_ri,
        "Ganho médio mensal:": valor_gmm_ri
    })

    corr_df = dados.corr(numeric_only=True)

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_df, annot=True, fmt=".2f", cmap="mako", square=True)
    plt.title("Matriz de Correlação rsi inf")
    plt.tight_layout()
    plt.show()


def c_rsi_sup():
    dados = pd.DataFrame({
        "10º ano CG": alunos1rs,
        "10º ano CP:": alunos2rs,
        "11º ano CG:": alunos3rs,
        "11º ano CP:": alunos4rs,
        "12º ano CG:": alunos5rs,
        "12º ano CP:": alunos6rs,
        "Rendimento Social de Inserção:": valor_rsi_rs,
        "Ganho médio mensal:": valor_gmm_rs
    })

    corr_df = dados.corr(numeric_only=True)

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_df, annot=True, fmt=".2f", cmap="mako", square=True)
    plt.title("Matriz de Correlação rsi sup")
    plt.tight_layout()
    plt.show()

def c_gmm_sup():
    dados = pd.DataFrame({
        "10º ano CG": alunos1gs,
        "10º ano CP:": alunos2gs,
        "11º ano CG:": alunos3gs,
        "11º ano CP:": alunos4gs,
        "12º ano CG:": alunos5gs,
        "12º ano CP:": alunos6gs,
        "Rendimento Social de Inserção:": valor_rsi_gs,
        "Ganho médio mensal:": valor_gmm_gs
    })

    corr_df = dados.corr(numeric_only=True)

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_df, annot=True, fmt=".2f", cmap="mako", square=True)
    plt.title("Matriz de Correlação gmm sup")
    plt.tight_layout()
    plt.show()

def c_gmm_inf():
    dados = pd.DataFrame({
        "10º ano CG": alunos1gi,
        "10º ano CP:": alunos2gi,
        "11º ano CG:": alunos3gi,
        "11º ano CP:": alunos4gi,
        "12º ano CG:": alunos5gi,
        "12º ano CP:": alunos6gi,
        "Rendimento Social de Inserção:": valor_rsi_gi,
        "Ganho médio mensal:": valor_gmm_gi
    })

    corr_df = dados.corr(numeric_only=True)

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_df, annot=True, fmt=".2f", cmap="mako", square=True)
    plt.title("Matriz de Correlação gmm inf")
    plt.tight_layout()
    plt.show()


def grafico_media_alunos():
    df = pd.read_csv("dados_com_zscore1.csv", sep=";", encoding="latin1")
    df_grouped = df.groupby('Ano')['Valor Alunos'].mean().reset_index()

    # Plotar gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(df_grouped['Ano'], df_grouped['Valor Alunos'], color='#CD7BEB', edgecolor='black')
    plt.title('Média da Taxa Retenção e Desistência no Ensino Secundário Por Ano')
    plt.xlabel('Ano')
    plt.ylabel('Taxa Retenção e Desistência no Ensino Secundário')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def grafico_media_gmm():
    df = pd.read_csv("dados_com_zscore1.csv", sep=";", encoding="latin1")
    df_grouped = df.groupby('Ano')['Valor GMM'].mean().reset_index()

    # Plotar gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(df_grouped['Ano'], df_grouped['Valor GMM'], color='#CD7BEB', edgecolor='black')
    plt.title('Média dos Ganhos Médios Mensais por Ano')
    plt.xlabel('Ano')
    plt.ylabel('Ganhos Médios Mensais')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def grafico_media_rsi():
    df = pd.read_csv("dados_com_zscore1.csv", sep=";" , encoding="latin1")
    df_grouped = df.groupby('Ano')['Valor RSI'].mean().reset_index()

    # Plotar gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(df_grouped['Ano'], df_grouped['Valor RSI'], color='#CD7BEB', edgecolor='black')
    plt.title('Média dos Rendimentos Sociais de Inserção por Ano')
    plt.xlabel('Ano')
    plt.ylabel('Rendimentos Sociais de Inserção')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def grafico_media_gmminf():
    df_grouped = df_gi.groupby('Ano')['Valor GMM'].mean().reset_index()

    # Plotar gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(df_grouped['Ano'], df_grouped['Valor GMM'], color='#CD7BEB', edgecolor='black')
    plt.title('Média dos Ganho Médio Mensal por Ano')
    plt.xlabel('Ano')
    plt.ylabel('Ganho Médio Mensal')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def grafico_media_gmmsup():
    df_grouped = df_gs.groupby('Ano')['Valor GMM'].mean().reset_index()

    # Plotar gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(df_grouped['Ano'], df_grouped['Valor GMM'], color='#CD7BEB', edgecolor='black')
    plt.title('Média dos Ganho Médio Mensal entre 1015.1 a 1346.7 por Ano')
    plt.xlabel('Ano')
    plt.ylabel('Ganho Médio Mensal')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def grafico_media_gmminf():
    df_grouped = df_gi.groupby('Ano')['Valor GMM'].mean().reset_index()

    # Plotar gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(df_grouped['Ano'], df_grouped['Valor GMM'], color='#CD7BEB', edgecolor='black')
    plt.title('Média dos Ganho Médio Mensal entre 683.5 e 1014.6 por Ano')
    plt.xlabel('Ano')
    plt.ylabel('Ganho Médio Mensal')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def grafico_media_rsiinf():
    df_grouped = df_ri.groupby('Ano')['Valor RSI'].mean().reset_index()

    # Plotar gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(df_grouped['Ano'], df_grouped['Valor RSI'], color='#CD7BEB', edgecolor='black')
    plt.title('Média dos Rendimento de Inserção Social entre entre 10 a 404 por Ano')
    plt.xlabel('Ano')
    plt.ylabel('Ganho Médio Mensal')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def grafico_media_rsisup():
    df_grouped = df_rs.groupby('Ano')['Valor RSI'].mean().reset_index()

    # Plotar gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(df_grouped['Ano'], df_grouped['Valor RSI'], color='#CD7BEB', edgecolor='black')
    plt.title('Média dos Rendimento de Inserção Social entre 405 a 799 por Ano')
    plt.xlabel('Ano')
    plt.ylabel('Ganho Médio Mensal')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
