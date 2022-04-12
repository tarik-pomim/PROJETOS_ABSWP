#  Comma Code
#  Say you have a list value like this:

#  spam = ['apples', 'bananas', 'tofu', 'cats']

#  Write a function that takes a list value as an argument
#  and returns a string with all the items separated by a comma and a space,
#  with and inserted before the last item.
#
#  For example, passing the previous spam list to the function
#  would return 'apples, bananas, tofu, and cats'.

#  But your function should be able to work with any list value passed to it.
#  Be sure to test the case where an empty list [] is passed to your function.


def muitosItens(lista):
    palavras = ''
    for i in range(len(lista)):
        if i == len(lista) - 1:
            palavras += 'and ' + str(lista[-1]) + '.'
        else:
            palavras += str(lista[i]) + ', '
    return palavras if palavras != '' else print('Lista vazia')


variasPalavras = [43, 1.33, -15.67, 'bananas', 'tofu', 'cats', 'armario', 'vaso', 'copo']
#variasPalavras = []
print(muitosItens(variasPalavras))




