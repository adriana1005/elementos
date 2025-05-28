from recolha import *
import seaborn as sns
import matplotlib.pyplot as plt

df, ano, municipio, alunos1, alunos2, alunos3, alunos4, alunos5, alunos6, valor_rsi, valor_gmm = recolha()


dados = pd.DataFrame({
    "10º ano CG": alunos1,
    "10º ano CP:": alunos2,
    "11º ano CG:": alunos3,
    "11º ano CP:": alunos4,
    "12º ano CG:": alunos5,
    "12º ano CP:": alunos6,
    "Rendimento Social de Inserção:": valor_rsi,
    "Ganho médio mensal:": valor_gmm
})

corr_df = dados.corr(numeric_only=True)

plt.figure(figsize=(10, 8))
sns.heatmap(corr_df, annot=True, fmt=".2f", cmap="mako", square=True)
plt.title("Matriz de Correlação")
plt.tight_layout()
plt.show()