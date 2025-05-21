from recolha import *
from valores_em_falta import *
from outliers import *

def main():

    dados =
    if dados:
        print("Ficheiro lido com sucesso!")
    else:
        print("Não foi possível carregar os dados.")
        return

    assert recolha() is not None and dados != ""

    assert valores_em_falta() is not None and dados != ""
    assert faltar_valores_alunos() is not None and dados != ""
    assert faltar_valor_rsi() is not None and dados != ""
    assert faltar_valor_gmm() is not None and dados != ""

    assert iqralunos() is not None and dados != ""
    assert iqrrsi() is not None and dados != ""
    assert iqrgmm() is not None and dados != ""
    assert winsorizealunos() is not None and dados != ""
    assert winsorizersi() is not None and dados != ""
    assert winsorizegmm() is not None and dados != ""

if __name__ == "__main__":
    main()