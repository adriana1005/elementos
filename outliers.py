from recolha import *
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np



dfp, ano, municipio, curso, anoescolar, alunos, rsi_p, gmm_p = recolhaantesoutlies()

#print(df["Valor Alunos"].describe())


def iqralunos():
    sns.boxplot(y=dfp["Valor Alunos"])
    plt.show()

    coluna = "Valor Alunos"

    # 3. Calcula Q1, Q3 e IQR
    Q1 = dfp[coluna].quantile(0.25)
    Q3 = dfp[coluna].quantile(0.75)
    IQR = Q3 - Q1

    # 4. Define limites
    LI = Q1 - 1.5 * IQR
    LS = Q3 + 1.5 * IQR

    # 5. Identifica outliers
    outliers_sup = dfp[dfp[coluna] > LS][coluna]
    outliers_inf = dfp[dfp[coluna] < LI][coluna]

    # 6. Resultados
    min_sup = outliers_sup.min() if not outliers_sup.empty else None
    max_inf = outliers_inf.max() if not outliers_inf.empty else None

    #print(f"Limite inferior (LI): {LI:.2f}")
    #print(f"Limite superior (LS): {LS:.2f}")
    #print(f"Maior outlier inferior: {max_inf}")
    #print(f"Menor outlier superior: {min_sup}")
    '''Name: Valor Alunos, dtype: float64
    Limite inferior (LI): -15.35
    Limite superior (LS): 38.65
    Maior outlier inferior: None
    Menor outlier superior: 38.7
    '''
    max_inf = max_inf if max_inf is not None else 0
    return min_sup,max_inf

def iqrrsi():
    plt.figure(figsize=(3, 8))
    sns.boxplot(y=dfp["Valor RSI "])
    plt.show()

    coluna = "Valor RSI "

    # 3. Calcula Q1, Q3 e IQR
    Q1 = dfp[coluna].quantile(0.25)
    Q3 = dfp[coluna].quantile(0.75)
    IQR = Q3 - Q1

    # 4. Define limites
    LI = Q1 - 1.5 * IQR
    LS = Q3 + 1.5 * IQR

    # 5. Identifica outliers
    outliers_sup = dfp[dfp[coluna] > LS][coluna]
    outliers_inf = dfp[dfp[coluna] < LI][coluna]

    # 6. Resultados
    min_sup = outliers_sup.min() if not outliers_sup.empty else None
    max_inf = outliers_inf.max() if not outliers_inf.empty else None

    #print(f"Limite inferior (LI): {LI:.2f}")
    #print(f"Limite superior (LS): {LS:.2f}")
    #print(f"Maior outlier inferior: {max_inf}")
    #print(f"Menor outlier superior: {min_sup}")
    max_inf = max_inf if max_inf is not None else 0
    return min_sup,max_inf



def iqrgmm():
    sns.boxplot(y=dfp["Valor GMM"])
    plt.show()

    coluna = "Valor GMM"

    # 3. Calcula Q1, Q3 e IQR
    Q1 = dfp[coluna].quantile(0.25)
    Q3 = dfp[coluna].quantile(0.75)
    IQR = Q3 - Q1

    # 4. Define limites
    LI = Q1 - 1.5 * IQR
    LS = Q3 + 1.5 * IQR

    # 5. Identifica outliers
    outliers_sup = dfp[dfp[coluna] > LS][coluna]
    outliers_inf = dfp[dfp[coluna] < LI][coluna]

    # 6. Resultados
    min_sup = outliers_sup.min() if not outliers_sup.empty else None
    max_inf = outliers_inf.max() if not outliers_inf.empty else None

    #print(f"Limite inferior (LI): {LI:.2f}")
    #print(f"Limite superior (LS): {LS:.2f}")
    #print(f"Maior outlier inferior: {max_inf}")
    #print(f"Menor outlier superior: {min_sup}")
    max_inf = max_inf if max_inf is not None else 0
    return min_sup, max_inf



def winsorizealunos(max_infa, min_supa):
    def winsorize_by_value(data, lower_bound, upper_bound):
        data = np.array(data)
        data[data < lower_bound] = lower_bound
        data[data > upper_bound] = upper_bound
        return data

    
    # Aplica a winsorização à coluna desejada (substitui a original)
    dfp['Valor Alunos'] = winsorize_by_value(dfp['Valor Alunos'], lower_bound=10, upper_bound=90)
    winsorize_by_value(dfp["Valor Alunos"], max_infa, min_supa)
    # Salva no mesmo arquivo (sobrescreve)
    dfp.to_csv('dados_com_zscore20.csv', index=False)


def winsorizersi(max_infr, min_supr):
    def winsorize_by_value(data, lower_bound, upper_bound):
        data = np.array(data)
        data[data < lower_bound] = lower_bound
        data[data > upper_bound] = upper_bound
        return data

    
    # Aplica a winsorização à coluna desejada (substitui a original)
    dfp['Valor RSI'] = winsorize_by_value(dfp['Valor RSI'], lower_bound=10, upper_bound=1000)
    winsorize_by_value(dfp["Valor RSI"], max_infr, min_supr)
    # Salva no mesmo arquivo (sobrescreve)
    dfp.to_csv('dados_com_zscore21.csv', index=False)


def winsorizegmm(max_infg, min_supg):
    def winsorize_by_value(data, lower_bound, upper_bound):
        data = np.array(data)
        data[data < lower_bound] = lower_bound
        data[data > upper_bound] = upper_bound
        return data

    
    # Aplica a winsorização à coluna desejada (substitui a original)
    dfp['Valor GMM'] = winsorize_by_value(dfp['Valor GMM'], lower_bound=650, upper_bound=min_supg)
    winsorize_by_value(dfp["Valor GMM"], max_infg, min_supg)
    # Salva no mesmo arquivo (sobrescreve)
    dfp.to_csv('dados_com_zscore221.csv', index=False)

