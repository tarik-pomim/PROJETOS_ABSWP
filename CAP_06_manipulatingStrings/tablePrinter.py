"""

Table Printer

Write a function named printTable() that takes a list of lists of strings
and displays it in a well-organized table with each column right-justified.

Assume that all the inner lists will contain the same number of strings.

For example, the value could look like this:


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


Your printTable() function would print the following:


   apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose


Hint: your code will first have to find the longest string in each of the inner lists
so that the whole column can be wide enough to fit all the strings.

You can store the maximum width of each column as a list of integers.

The printTable() function can begin with colWidths = [0] * len(tableData),
which will create a list containing the same number of 0 values as the
number of inner lists in tableData.

That way, colWidths[0] can store the width of the longest string in tableData[0],
colWidths[1] can store the width of the longest string in tableData[1], and so on.
You can then find the largest value in the colWidths list to find out what integer
width to pass to the rjust() string method.

"""

tableData = [['apples', 'oranges', 'cherries', 'banana', 'abacateAvocado', 'abacate'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose'],
             ['car', 'boat', 'plane', 'spaceship', 'submarine', 'missle'],
             ['sofa', 'television', 'table', 'computer'],
             ['towel', 'shirt', 'hoodie', 'sweatpants']]


def printTable(table):
    #  Encontrando a str mais longa
    columWidths = [0] * len(table)
    lenghtiestItem = 0

    for i in range(len(table)):  # para cada lista presente na table
        maisLongaStr = 0
        print('Lista numero: ' + str(i))  # i = indice de cada lista dentro de table
        for y in table[i]:  # para cada item da lista
            print(y + ' - ' + str(len(y)))  # y = str dos itens dentro da lista

            if len(y) > maisLongaStr:  # se a maisLongaStr for maior que a variavel
                maisLongaStr = len(y)  # maisLongaStr = comprimento da variavel

            print('maisLongaStr é: ' + str(maisLongaStr))
            columWidths[i] = maisLongaStr
    print(columWidths)
    print('-' * 40)

    #  Formatando tabela:
    for i in range(len(table)):
        for y in table[i]:
            print(y.rjust(columWidths[i]))

    for row in table:
        print("{: >20} {: >20} {: >20}".format(*row))


printTable(tableData)
