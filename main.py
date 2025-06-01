from recolha import *
from outliers import *
from analise_preditiva import *


'''
def main():

    dados = recolha()
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
    '''
class EncerrarPrograma(Exception):
    pass


def main():

    print('\033[1;36mApartir de vários datasets do Pordata foi analisada se a Taxa de retenção e desistência no ensino secundário '
        'relacionava-se com uma proporcionalidade direta ou inderta com o Rendimento de Inserção Social e com os Ganhos Médios Mensais.'
        ' \n Aqui apresentamos um menu de todos as tarefas que foram executadas \033[m')
    print(' ')

    try:
        while True:
            print('\033[1;97;46mMENU\033[m')
            print('1 - Quais as variaveis em análise? \n'
                '2 - Acerca dos valores em falta \n'
                '3 - Acerca dos outliers \n'
                '4 - Acerca de análise\n'
                '5 - Conlusão\n'
                '0 - Sair')

            try:
                opcao = int(input('Escolha uma das opções: '))

                if opcao == 0:
                    raise EncerrarPrograma

                elif opcao == 1:
                    print(f'\033[1;36mAs variáveis  são: \033[m4')
                    print('Taxa de retenção e desistência no ensino secundário por modalidade de ensino e ano de escolaridade (em percentagem) ')
                    print('Beneciários do Rendimento Social de Inserção (por faixa etária) ')
                    print('Ganho médio mensal (em euros)')
                    print(' ')

                elif opcao == 2:
                    while True:
                        print('1 - Quantos valores em falta haviam na Taxa de desistência escolar?\n'
                            '2 - Quantos valores em falta haviam na Rendimento de Inserção Social?\n'
                            '3 - Quantos valores em falta haviam nos Ganhos Médios Mensais\n'
                            '4 - Como é que tratamos os valores em falta? \n'
                            '0 - Sair ')
                        opcao1 = int(input('Escolha uma das opções: '))
                        try:
                            if opcao1 == 0:
                                break
                            elif opcao1 == 1:
                                print(f'\033[1;36mA quantidade de valores em falta são: 2949 \033[m')
                                
                                print(' ')
                            elif opcao1 == 2:
                                print(f'\033[1;36mA quantidade de valores em falta são: 168 \033[m')

                                print(' ')
                            elif opcao1 == 3:
                                print(f'\033[1;36mA quantidade de valores em falta são: 342 \033[m')
                            elif opcao1 == 4:
                                print(f'\033[1;36mApartir da função describe descobrimos a mediana das várias variáveis e substituímos\033[m')
                            else:
                                print('Essa opção não existe, tente novamente.')

                        except ValueError:
                            print('Inseriu um valor não inteiro, tente novamente.')

                elif opcao == 3:
                    while True:
                        print('1 - Gráfico dos outputs da taxa de desistência \n'
                            '2 - Gráfico dos outputs do rendimento social de inserção\n'
                            '3 - Gráfico dos outputs dos ganhos médios mensais\n'
                            '4 - Como é que tratamos dos outliers?\n'
                            '0 - Sair')
                        try:
                            opcao2 = int(input('Escolha uma das opções: '))

                            if opcao2 == 0:
                                break
                            elif opcao2 == 1:
                                iqralunos()
                                
                            elif opcao2 == 2:
                                iqrrsi()
                            elif opcao2 == 3:
                                iqrgmm()
                            elif opcao2 == 4:
                                print(f'\033[1;36m Para identificá-los utilizámos o método iqr e para tratá-los o winsorize. \033[m')
                            else:
                                print('Essa opção não existe, tente novamente.')
                        except ValueError:
                            print('Inseriu um valor não inteiro, tente novamente.')

                elif opcao == 4:
                    while True:
                        print('1 - Gráfico das correlações \n'
                            '2 - Gráfico das correlações com rendimentos entre 10 e 404 \n'
                            '3 - Gráfico das correlações com rendimentos entre 405 e 799 \n'
                            '4 - Gráfico das correlações com ganhos medios entre 683.5 e 1014.6 \n'
                            '5 - Gráfico das correlações com ganhos medios entre 1015.1 e 1346.7 \n'
                            '6 - Gráfico das barras da taxa de desistencia por anos \n'
                            '7 - Gráfico das barras dos rendimentos de inserção por anos \n'
                            '8 - Gráfico das barras dos ganhos médios por anos \n'
                            '9 - Gráfico das barras dos rendimento de inserção 10 e 404 por anos \n'
                            '10 - Gráfico das barras dos rendimento de inserção 405 e 799 por anos \n'
                            '11 - Gráfico das barras dos ganho médio mensal 683.5 e 1014.6 por anos \n'
                            '12 - Gráfico das barras dos ganho médio mensal 1015.1 e 1346.7 por anos \n'
                            '0 - Sair')
                        try:
                            opcao3 = int(input('Escolha uma das opções: '))

                            if opcao3 == 0:
                                break
                            elif opcao3 == 1:
                                principal()
                            elif opcao3 == 2:
                                c_rsi_inf()
                            elif opcao3 == 3:
                                c_rsi_sup()
                            elif opcao3 == 4:
                                c_gmm_sup()
                            elif opcao3 == 5:
                                c_gmm_inf()
                            elif opcao3 == 6:
                                grafico_media_alunos()
                            elif opcao3 == 7:
                                grafico_media_gmm()
                            elif opcao3 == 8:
                                grafico_media_rsi()
                            elif opcao3 == 9:
                                grafico_media_rsiinf()
                            elif opcao3 == 10:
                                grafico_media_rsisup()
                            elif opcao3 == 11:
                                grafico_media_gmminf()
                            elif opcao3 == 12:
                                grafico_media_gmmsup()
                        except ValueError:
                            print('Inseriu um valor não inteiro, tente novamente.')
                elif opcao == 5:
                    print(f'\033[1;36m No futuro, é possível que a taxa de desistência diminua, que o ganho médio mensal aumente e que aqueles que beneficiam do RSI tendem a ser cada vez menos.\033[m')
            except ValueError:
                print('Inseriu um valor não inteiro, tente novamente.')

    except EncerrarPrograma:
        print('Encerrando o programa...')


if __name__ == "__main__":
    main()