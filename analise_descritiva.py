from recolha import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df, ano, municipio, curso, ano_escolar, valor_alunos, valor_rsi, valor_gmm = recolha()

'''Mapa de calor das correlações'''
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Matriz de Correlação entre Variáveis Numéricas")
plt.tight_layout()
plt.show()
