#  Chess Dictionary Validator


#  In this chapter, we used the dictionary value
#  {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
#  to represent a chess board.

#  Write a function named isValidChessBoard() that takes a dictionary argument and
#  returns True or False depending on if the board is valid.

#  A valid board will have exactly one black king and exactly one white king.
#  Each player can only have at most 16 pieces
#   at most 8 pawns,
#  and all pieces must be on a valid space from '1a' to '8h' that is, a piece can’t be on space '9z'.
#  The piece names begin with either a 'w' or 'b' to represent white or black,
#  followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.
#  This function should detect when a bug has resulted in an improper chess board.
import pprint

#  tabuleiro = {'1a': 'bking', '1b': 'bqueen', '1c': 'bbishop', '1d': 'bbishop', '1e': 'bknight',
#             '1f': 'bknight', '1g': 'brook', '1h': 'brook', '2a': 'bpawn', '2b': 'bpawn',
#             '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn',
#             '2h': 'bpawn', '5a': 'wking', '5b': 'wqueen', '5c': 'wbishop', '5d': 'wbishop', '5e': 'wknight',
#             '5f': 'wknight', '5g': 'wrook', '5h': 'wrook', '6a': 'wpawn', '6b': 'wpawn',
#             '6c': 'wpawn', '6d': 'wpawn', '6e': 'wpawn', '6f': 'wpawn', '6g': 'wpawn',
#             '6h': 'wpawn'}


tabuleiro = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}


def isValidChessBoard(tabuleiro):
    for k in tabuleiro.keys():  # checa se as casas estão corretas
        for i in k:
            if i not in '12345678abcdefgh' or len(k) != 2:
                return 'O nome de uma ou mais casas está errado.'

    for v in tabuleiro.values():  # checa o nome das peças
        pecas = ('pawn', 'knight', 'bishop', 'rook', 'queen', 'king')
        if v[0] not in 'bw':  # se nao começam com b ou w
            return 'Uma ou mais peças nao está começando com "b" ou "w"'
        elif v[1:] not in pecas:  # se o nome das pecas esta errado
            return 'Uma ou mais peças está com o nome errado'

    if 'wking' not in tabuleiro.values() or 'bking' not in tabuleiro.values():  # checa se os reis estão no tabuleiro
        return 'Um ou ambos os reis não estão presentes no tabuleiro.'

    pecasCount = {}  # conta o numero de peças e coloca em um dicionario
    for k, v in tabuleiro.items():
        if v not in pecasCount.keys():
            pecasCount.setdefault(v, 1)
        else:
            pecasCount[v] += 1
    print(pecasCount)
    try:  # verifica se existem peças excedentes
        if pecasCount['wking'] != 1 or \
                pecasCount['bking'] != 1 or \
                pecasCount['wqueen'] != 1 or \
                pecasCount['bqueen'] != 1 or \
                pecasCount['bknight'] > 2 or \
                pecasCount['wknight'] > 2 or \
                pecasCount['bbishop'] > 2 or \
                pecasCount['wbishop'] > 2 or \
                pecasCount['wrook'] > 2 or \
                pecasCount['brook'] > 2 or \
                pecasCount['wpawn'] > 8 or \
                pecasCount['bpawn'] > 8:
            return 'Peças a mais presentes no tabuleiro'
    except KeyError:
        pass
    return True


print(isValidChessBoard(tabuleiro))
