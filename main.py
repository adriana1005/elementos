from outliers import *
from analise_preditiva import *


class EncerrarPrograma(Exception):
    pass


def main():
    print('\033[1;36mA partir de vários datasets do Pordata foi analisado se a Taxa de retenção e desistência no ensino secundário '
          'se relacionava com uma proporcionalidade direta ou indireta com o Rendimento de Inserção Social e com os Ganhos Médios Mensais.'
          '\nAqui apresentamos um menu de todas as tarefas que foram executadas:\033[m\n')

    try:
        while True:
            print('\033[1;97;46mMENU\033[m')
            print('1 - Quais as variáveis em análise? \n'
                  '2 - Acerca dos valores em falta \n'
                  '3 - Acerca dos outliers \n'
                  '4 - Acerca de análise\n'
                  '5 - Conclusão\n'
                  '0 - Sair')

            try:
                opcao = int(input('Escolha uma das opções: '))

                if opcao == 0:
                    raise EncerrarPrograma

                elif opcao == 1:
                    print(f'\033[1;36mAs variáveis são: \033[m')
                    print('- Taxa de retenção e desistência no ensino secundário por modalidade de ensino e ano de escolaridade (em percentagem)')
                    print('- Beneficiários do Rendimento Social de Inserção (por faixa etária)')
                    print('- Ganho médio mensal (em euros)\n')

                elif opcao == 2:
                    while True:
                        print('1 - Quantos valores em falta haviam na Taxa de desistência escolar?\n'
                              '2 - Quantos valores em falta haviam no Rendimento de Inserção Social?\n'
                              '3 - Quantos valores em falta haviam nos Ganhos Médios Mensais\n'
                              '4 - Como é que tratamos os valores em falta?\n'
                              '0 - Voltar ao menu principal')
                        try:
                            opcao1 = int(input('Escolha uma das opções: '))
                            if opcao1 == 0:
                                break
                            elif opcao1 == 1:
                                print(f'\033[1;36mA quantidade de valores em falta é: 2949 \033[m\n')
                            elif opcao1 == 2:
                                print(f'\033[1;36mA quantidade de valores em falta é: 168 \033[m\n')
                            elif opcao1 == 3:
                                print(f'\033[1;36mA quantidade de valores em falta é: 342 \033[m\n')
                            elif opcao1 == 4:
                                print(f'\033[1;36mA partir da função `describe` descobrimos a mediana das várias variáveis e substituímos os valores em falta por ela.\033[m\n')
                            else:
                                print('Essa opção não existe, tente novamente.\n')
                        except ValueError:
                            print('Inseriu um valor não inteiro, tente novamente.\n')

                elif opcao == 3:
                    while True:
                        print('1 - Gráfico dos outputs da taxa de desistência \n'
                              '2 - Gráfico dos outputs do rendimento social de inserção\n'
                              '3 - Gráfico dos outputs dos ganhos médios mensais\n'
                              '4 - Como é que tratamos dos outliers?\n'
                              '0 - Voltar ao menu principal')
                        try:
                            opcao2 = int(input('Escolha uma das opções: '))
                            if opcao2 == 0:
                                break
                            elif opcao2 == 1:
                                winsorizealunos()
                            elif opcao2 == 2:
                                winsorizersi()
                            elif opcao2 == 3:
                                winsorizegmm()
                            elif opcao2 == 4:
                                print(f'\033[1;36mPara identificá-los utilizámos o método IQR e para tratá-los o `winsorize`.\033[m\n')
                            else:
                                print('Essa opção não existe, tente novamente.\n')
                        except ValueError:
                            print('Inseriu um valor não inteiro, tente novamente.\n')

                elif opcao == 4:
                    while True:
                        print('1 - Gráfico das correlações \n'
                              '2 - Gráfico das correlações com rendimentos entre 10 e 404\n'
                              '3 - Gráfico das correlações com rendimentos entre 405 e 799\n'
                              '4 - Gráfico das correlações com ganhos médios entre 683.5 e 1014.6\n'
                              '5 - Gráfico das correlações com ganhos médios entre 1015.1 e 1346.7\n'
                              '6 - Gráfico das barras da taxa de desistência por anos\n'
                              '7 - Gráfico das barras dos rendimentos de inserção por anos\n'
                              '8 - Gráfico das barras dos ganhos médios por anos\n'
                              '0 - Voltar ao menu principal')
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
                            else:
                                print('Essa opção não existe, tente novamente.\n')
                        except ValueError:
                            print('Inseriu um valor não inteiro, tente novamente.\n')

                elif opcao == 5:
                    print(f'\033[1;36mCom base na análise, observámos que existem padrões que indicam uma correlação entre a taxa de desistência escolar e as variáveis socioeconómicas analisadas.\033[m\n')

                else:
                    print('Essa opção não existe, tente novamente.\n')

            except ValueError:
                print('Inseriu um valor não inteiro, tente novamente.\n')

    except EncerrarPrograma:
        print('\nA encerrar o programa...')


if __name__ == "__main__":
    main()