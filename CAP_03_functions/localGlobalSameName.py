def spam():
    eggs = 'spam local'
    print(eggs)  # pronts 'spam local'


def bacon():
    eggs = 'bacon local'
    print(eggs)  # pronts 'bacon local'
    spam()
    print(eggs)  # prints 'bacon local'


eggs = 'global'
bacon()
print(eggs)  # prints 'global'

