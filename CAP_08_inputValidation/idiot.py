import pyinputplus as pyip

while True:
    prompt = 'Quer saber como manter um idiota ocupado por horas?\n'
    response = pyip.inputYesNo(prompt, yesVal='sim', noVal='nao')
    if response == 'nao':
        break
print('Thank you. Have a nice day.')
