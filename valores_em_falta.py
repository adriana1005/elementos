from recolha import recolha

ano, municipio, curso, ano_escolar, valor_alunos, valor_rsi, valor_gmm = recolha()

def valores_em_falta(faltar):
    return faltar.isnull().sum()


def faltar_ano(ano):
    return valores_em_falta(ano)


def faltar_regiao(municipio):
    return valores_em_falta(municipio)


def faltar_curso(curso):
    return valores_em_falta(curso)


def faltar_ano_escolar(ano_escolar):
    return valores_em_falta(ano_escolar)


def faltar_valores_alunos(valor_alunos):
    return valores_em_falta(valor_alunos)


def faltar_valor_rsi(valor_rsi):
    return valores_em_falta(valor_rsi)


def faltar_valor_gmm(valor_gmm):
    return valores_em_falta(valor_gmm)



print(faltar_valores_alunos(valor_alunos))
print(faltar_valor_rsi(valor_rsi))
print(faltar_valor_gmm(valor_gmm))