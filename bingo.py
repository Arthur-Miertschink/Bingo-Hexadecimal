import numpy
import pandas

"""
FUNÇÃO: Criar Cartela (4 x 4), com a seguintes características:
1: Números Aleatórios: Intervalo entre [16, 159];
2: Criar em Decimal (Base 10: 0, 1, 2, 3, 4, 5, 6, 7, 8 e 9)
3: NÃO pode ter NÚMEROS REPETIDOS na cartela. Caso seja sorteado um número repetido,
o sorteio deve ser refeito até sair um número que ainda não foi sorteado na partida.
3: PARÂMETRO NOMINAL: Inserir (de forma OPCIONAL) o Nome do Jogador na Cartela.
"""
numeroDePedrasNaCartela = 16
pedrasSorteadas = []

def criarCartela (nominal= False):
  criandoCartela = numpy.random.randint(16, 160, 16)
  criandoCartela = criandoCartela.reshape(4,4)
  return criandoCartela

def exibirPontuacao(args):
    pedrasSorteadasCartela1 = 0
    pedrasSorteadasCartela2 = 0
    pedrasSorteadasCartela3 = 0
    while True:
        for value in pedrasSorteadas:
            if value in cartela1:
                pedrasSorteadasCartela1 += 1
            if value in cartela2:
                pedrasSorteadasCartela2 += 1
            if value in cartela3:
                pedrasSorteadasCartela3 += 1

        if args == 1:
            return pedrasSorteadasCartela1
        if args == 2:
            return pedrasSorteadasCartela2
        else:
            return pedrasSorteadasCartela3


def sortearPedra():
    sorteandoPedras = numpy.random.randint(16, 160, 1, dtype=int)
    while sorteandoPedras in pedrasSorteadas:
        sorteandoPedras = numpy.random.randint(16, 160, 1, dtype=int)


    return sorteandoPedras


def conferirPedra():
    pedrasQueForamSorteadas = [(pedrasSorteadas)]

    return pedrasQueForamSorteadas

def converterTabela (args):
    cartela1Convertida = cartela1.copy()
    reorganizarCartela1 = cartela1Convertida.reshape(-1)
    converterCartela1 = numpy.array([f'{campo:X}' for campo in reorganizarCartela1]).reshape(4,4)

    cartela2Convertida = cartela2.copy()
    reorganizarCartela2 = cartela2Convertida.reshape(-1)
    converterCartela2 = numpy.array([f'{campo:X}' for campo in reorganizarCartela2]).reshape(4,4)

    cartela3Convertida = cartela3.copy()
    reorganizarCartela3 = cartela3Convertida.reshape(-1)
    converterCartela3 = numpy.array([f'{campo:X}' for campo in reorganizarCartela3]).reshape(4,4)



    if args == 1:
        return converterCartela1
    elif args == 2:
        return converterCartela2
    else:
        return converterCartela3



def sortearSemRepeticao(numeroDePedrasNaCartela):
    sorteandoCartela = numpy.zeros(numeroDePedrasNaCartela, dtype=int)
    i = 1
    sorteandoCartela[0] = numpy.random.randint(16, 160 , 1)
    while i != numeroDePedrasNaCartela:
        flag = True
        j = i - 1
        termo = numpy.random.randint(16, 160, 1)
        while j != -1:
            if termo == sorteandoCartela[j]:
                flag = False
                break
            j -= 1
        if flag:
            sorteandoCartela[i] = termo
            i += 1
    sorteandoCartela = sorteandoCartela.reshape(4,4)
    return sorteandoCartela




def exibirCartelaHex (args):
    cartela1HexPd = pandas.DataFrame(cartela1Hex, index=['L1', 'L2', 'L3', 'L4'], columns= ['C1', 'C2', 'C3', 'C4'])
    cartela2HexPd = pandas.DataFrame(cartela2Hex, index=['L1', 'L2', 'L3', 'L4'], columns= ['C1', 'C2', 'C3', 'C4'])
    cartela3HexPd = pandas.DataFrame(cartela3Hex, index=['L1', 'L2', 'L3', 'L4'], columns= ['C1', 'C2', 'C3', 'C4'])

    if args == 1:
        return cartela1HexPd
    elif args == 2:
        return cartela2HexPd
    else:
        return cartela3HexPd

def exibirGanhadorEPremiacao():
        premioVencedor = None
        if exibirPontuacao(1) == numeroDePedrasNaCartela:
            premioVencedor = 100 - len(pedrasSorteadas) + max([valor for linha in cartela1 for valor in linha])


        elif (exibirPontuacao(2) == numeroDePedrasNaCartela):
            premioVencedor = 100 - len(pedrasSorteadas) + max([valor for linha in cartela2 for valor in linha])


        elif (exibirPontuacao(3) == numeroDePedrasNaCartela):
            premioVencedor = 100 - len(pedrasSorteadas) + max([valor for linha in cartela3 for valor in linha])


        return premioVencedor



opcao = 0
TAMANHO = 4
cartela1 = sortearSemRepeticao(numeroDePedrasNaCartela)
cartela2 = sortearSemRepeticao(numeroDePedrasNaCartela)
cartela3 = sortearSemRepeticao(numeroDePedrasNaCartela)

cartela1Hex = converterTabela(1)
cartela2Hex = converterTabela(2)
cartela3Hex = converterTabela(3)






while True:
    if exibirGanhadorEPremiacao() is not None:
        if exibirPontuacao(1) == numeroDePedrasNaCartela:
            print(f'O vencedor do bingo é aquele que possui a cartela 1 e seu prêmio é de R$: {exibirGanhadorEPremiacao()}')
        elif exibirPontuacao(2) == numeroDePedrasNaCartela:
            print(f'O vencedor do bingo é aquele que possui a cartela 2 e seu prêmio é de R$: {exibirGanhadorEPremiacao()}')
        elif exibirPontuacao(3) == numeroDePedrasNaCartela:
            print(f'O vencedor do bingo é aquele que possui a cartela 2 e seu prêmio é de R$: {exibirGanhadorEPremiacao()} ')
        break
    else:
        print('\n BINGO HEXADECIMAL - MENU:')
        print('Opção 1: Criar/Exibir Cartela: ')
        print('Opção 2: Sortear/Exibir Pedra')
        print('Opção 3: Exibir pontuação')
        print('Opção 4: Conferir Pedra')
        print('Opção 0: Sair do Programa')
        opcao = int(input('Qual a sua Opção: '))
        if opcao == 0:
            print('TCHAU!!! - BOA SORTE')
            break
        elif (opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4):
            print('Opcao Incorreta. Escolha de novo.')
        elif(opcao == 2):
            pedrasSorteadas.append(sortearPedra())
            print(f'A pedra sorteada foi: {pedrasSorteadas[-1]}')
        elif(opcao == 3):
            print(f'A quantidade de pedras batidas das cartelas 1: {exibirPontuacao(1)}')
            print(f'A quantidade de pedras batidas das cartelas 2: {exibirPontuacao(2)}')
            print(f'A quantidade de pedras batidas das cartelas 3: {exibirPontuacao(3)}')
            print(exibirGanhadorEPremiacao())
        elif(opcao == 4):
            print(conferirPedra())
        elif exibirGanhadorEPremiacao() is not None:
            print(exibirGanhadorEPremiacao())
            break
        else:
            opcao = 1
            print(f'\nCartela 1:', end='\n')
            print(f'{cartela1Hex}')

            print(f'\nCartela 2:', end='\n')
            print(f'{cartela3Hex}')

            print(f'\nCartela 3:', end='\n')
            print(f'{cartela3Hex}')

