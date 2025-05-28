from recolha import *
import seaborn as sns
import matplotlib.pyplot as plt


df, ano, municipio, alunos1, alunos2, alunos3, alunos4, alunos5, alunos6, valor_rsi, valor_gmm = recolha()

df_ri, ano_ri, municipio_ri, alunos1ri, alunos2ri, alunos3ri, alunos4ri, alunos5ri, alunos6ri, valor_rsi_ri, valor_gmm_ri = recolha_rsi_inf()

df_rs, ano_rs, municipio_rs, alunos1rs, alunos2rs, alunos3rs, alunos4rs, alunos5rs, alunos6rs, valor_rsi_rs, valor_gmm_rs = recolha_rsi_sup()

df_gs, ano_gs, municipio_gs, alunos1gs, alunos2gs, alunos3gs, alunos4gs, alunos5gs, alunos6gs, valor_rsi_gs, valor_gmm_gs = recolha_gmm_sup()

df_gi, ano_gi, municipio_gi, alunos1gi, alunos2gi, alunos3gi, alunos4gi, alunos5gi, alunos6gi, valor_rsi_gi, valor_gmm_gi = recolha_gmm_inf()


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

c_gmm_sup()

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

c_gmm_inf()