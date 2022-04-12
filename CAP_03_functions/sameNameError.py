def spam():
    print(eggs)  # ERROR! pois a variavel local ta vindo depois
    eggs = 'spam local'


eggs = 'global'
spam()
