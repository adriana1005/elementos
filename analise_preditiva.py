from recolha import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
import matplotlib.pyplot as plt

df, ano, municipio, alunos1, alunos2, alunos3, alunos4, alunos5, alunos6, valor_rsi, valor_gmm = recolha()


def reg_aluno1_gmm(alunos1, valor_rsi, valor_gmm):
    sns.set(style="whitegrid")

    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(alunos1, valor_rsi, c = valor_gmm, cmap="plasma", s=40, alpha=0.6)
    plt.colorbar(scatter, label="Ganho médio mensal")
    
    # Linha de regressão sem os pontos (scatter=False)
    sns.regplot(x=alunos1, y=valor_gmm, scatter=False, color="black")

    plt.xlabel("Taxa de desistência escolar do 10º ano em Ensino Geral")
    plt.ylabel("Valor do Rendimento Social de Inserção")
    plt.title("Relação entre desistência escolar e rendimento social e ganho médio mensal para os alunos do 10ºano em Ensino Geral")
    plt.tight_layout()
    plt.show()
reg_aluno1_gmm(alunos1, valor_rsi, valor_gmm)

def reg_aluno1_gmm():
    sns.set(style="whitegrid")

    plt.figure(figsize=(8, 6))
    sns.regplot(x=alunos1, y=valor_gmm, color="mediumpurple", scatter_kws={"s": 40, "alpha": 0.6})
    plt.xlabel("Taxa de desisistência escolar do 10º ano em Ensino Geral")
    plt.ylabel("Valor do Rendimento Social de Inserção")
    plt.show()



'''
def reg_aluno1_rsi():
    X = alunos1.values.reshape(-1, 1)
    y = valor_rsi.values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    X_line = np.linspace(0, 150, 100).reshape(-1, 1)
    y_pred = model.predict(X_line)

    plt.scatter(X_train, y_train, color='pink', label='Treino')
    plt.plot(X_line, y_pred, color='purple', linewidth=2, label='Regressão')
    plt.xlabel("Número de alunos no 1º ciclo")
    plt.ylabel("Valor do RSI")
    plt.legend()
    plt.title("Regressão Linear: alunos1 vs RSI")
    plt.show()
#nova_experiencia = np.array([1.5])
'''

