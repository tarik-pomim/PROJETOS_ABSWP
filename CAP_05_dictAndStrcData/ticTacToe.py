tabuleiro = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}


def printTabu(tabuleiro):
    print(tabuleiro['7'] + '|' + tabuleiro['8'] + '|' + tabuleiro['9'])
    print('-+-+-')
    print(tabuleiro['4'] + '|' + tabuleiro['5'] + '|' + tabuleiro['6'])
    print('-+-+-')
    print(tabuleiro['1'] + '|' + tabuleiro['2'] + '|' + tabuleiro['3'])


vez = 'X'
for i in range(9):
    printTabu(tabuleiro)
    print('Vez do ' + vez + '. Marcar aonde? (Use o teclado numérico)')
    movimento = input()
    tabuleiro[movimento] = vez
    if vez == 'X':
        vez = 'O'
    else:
        vez = 'X'
printTabu(tabuleiro)
