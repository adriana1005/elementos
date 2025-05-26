from recolha import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

df, ano, municipio, alunos1, alunos2, alunos3, alunos4, alunos5, alunos6, valor_rsi, valor_gmm = recolha()

np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.rand(100, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

X_line = np.linspace(0, 2, 100).reshape(-1, 1)
y_pred = model.predict(X_line)

plt.scatter(X_train, y_train, color='pink', label='Treino')
plt.plot(X_line, y_pred, color='purple', linewidth=2, label='Regressão')
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

#nova_experiencia = np.array([1.5])
#salario_previsto = model.predict(nova_experiencia)
