from recolha import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
import matplotlib.pyplot as plt

df, ano, municipio, alunos1, alunos2, alunos3, alunos4, alunos5, alunos6, valor_rsi, valor_gmm = recolha()


def reg_aluno1(alunos1, valor_rsi, valor_gmm):
    sns.set(style="whitegrid")

    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(alunos1, valor_rsi, c = valor_gmm, cmap="plasma", s=40, alpha=0.6)
    plt.colorbar(scatter, label="Ganho médio mensal")
    
    # Linha de regressão sem os pontos (scatter=False)
    sns.regplot(x=alunos1, y=valor_gmm, scatter=False, color="black")

    plt.xlabel("Taxa de desistência escolar do 10º ano em Ensino Geral")
    plt.ylabel("Valor do Rendimento Social de Inserção")
    plt.title("Relação entre desistência escolar, rendimento social e ganho médio mensal para os alunos do 10ºano em Ensino Geral")
    plt.tight_layout()
    plt.show()
#reg_aluno1(alunos1, valor_rsi, valor_gmm)


def reg_aluno2(alunos2, valor_rsi, valor_gmm):
    sns.set(style="whitegrid")

    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(alunos2, valor_rsi, c=valor_gmm, cmap="plasma", s=40, alpha=0.6)
    plt.colorbar(scatter, label="Ganho médio mensal")

    # Linha de regressão sem os pontos (scatter=False)
    sns.regplot(x=alunos2, y=valor_gmm, scatter=False, color="black")

    plt.xlabel("Taxa de desistência escolar do 10º ano em Ensino Profissional")
    plt.ylabel("Valor do Rendimento Social de Inserção")
    plt.title(
        "Relação entre desistência escolar, rendimento social e ganho médio mensal para os alunos do 10º ano em Ensino Profissional")
    plt.tight_layout()
    plt.show()
#reg_aluno2(alunos2, valor_rsi, valor_gmm)


def reg_aluno3(alunos3, valor_rsi, valor_gmm):
    sns.set(style="whitegrid")

    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(alunos2, valor_rsi, c=valor_gmm, cmap="plasma", s=40, alpha=0.6)
    plt.colorbar(scatter, label="Ganho médio mensal")

    # Linha de regressão sem os pontos (scatter=False)
    sns.regplot(x=alunos3, y=valor_gmm, scatter=False, color="black")

    plt.xlabel("Taxa de desistência escolar do 11º ano em Ensino Geral")
    plt.ylabel("Valor do Rendimento Social de Inserção")
    plt.title(
        "Relação entre desistência escolar, rendimento social e ganho médio mensal para os alunos do 11º ano em Ensino Geral")
    plt.tight_layout()
    plt.show()
#reg_aluno3(alunos3, valor_rsi, valor_gmm)


def reg_aluno4(alunos4, valor_rsi, valor_gmm):
    sns.set(style="whitegrid")

    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(alunos4, valor_rsi, c=valor_gmm, cmap="plasma", s=40, alpha=0.6)
    plt.colorbar(scatter, label="Ganho médio mensal")

    # Linha de regressão sem os pontos (scatter=False)
    sns.regplot(x=alunos4, y=valor_gmm, scatter=False, color="black")

    plt.xlabel("Taxa de desistência escolar do 11º ano em Ensino Profissional")
    plt.ylabel("Valor do Rendimento Social de Inserção")
    plt.title(
        "Relação entre desistência escolar, rendimento social e ganho médio mensal para os alunos do 11º ano em Ensino Profissional")
    plt.tight_layout()
    plt.show()
#reg_aluno4(alunos4, valor_rsi, valor_gmm)


def reg_aluno5(alunos5, valor_rsi, valor_gmm):
    sns.set(style="whitegrid")

    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(alunos5, valor_rsi, c=valor_gmm, cmap="plasma", s=40, alpha=0.6)
    plt.colorbar(scatter, label="Ganho médio mensal")

    # Linha de regressão sem os pontos (scatter=False)
    sns.regplot(x=alunos5, y=valor_gmm, scatter=False, color="black")

    plt.xlabel("Taxa de desistência escolar do 12º ano em Ensino Geral")
    plt.ylabel("Valor do Rendimento Social de Inserção")
    plt.title(
        "Relação entre desistência escolar, rendimento social e ganho médio mensal para os alunos do 12º ano em Ensino Geral")
    plt.tight_layout()
    plt.show()
#reg_aluno5(alunos5, valor_rsi, valor_gmm)


def reg_aluno6(alunos6, valor_rsi, valor_gmm):
    sns.set(style="whitegrid")

    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(alunos6, valor_rsi, c=valor_gmm, cmap="plasma", s=40, alpha=0.6)
    plt.colorbar(scatter, label="Ganho médio mensal")

    # Linha de regressão sem os pontos (scatter=False)
    sns.regplot(x=alunos6, y=valor_gmm, scatter=False, color="black")

    plt.xlabel("Taxa de desistência escolar do 12º ano em Ensino Profissional")
    plt.ylabel("Valor do Rendimento Social de Inserção")
    plt.title(
        "Relação entre desistência escolar, rendimento social e ganho médio mensal para os alunos do 12º ano em Ensino Profissional")
    plt.tight_layout()
    plt.show()
reg_aluno6(alunos6, valor_rsi, valor_gmm)