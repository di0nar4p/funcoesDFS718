def contVogal(texto:str):
    vogais = 'aeiou'
    cont=0
    for arg in texto:
        if arg in vogais:
            cont= cont+1
    print(f'O texto contém {cont} vogais')

def contConsoante(texto:str):
    vogais = ' aeiou'
    cont=0
    for arg in texto:
        if arg not in vogais:
            cont= cont+1
    print(f'O texto contém {cont} consoantes')

def palindromo(texto:str):
    inverso= str()
    for letra in texto[::-1]:
        if letra == ' ':
            continue
        else:
            texto = inverso+letra
            inverso = inverso+letra
    if inverso == texto:
        print('É PALINDROMO!')
    else:
        print(inverso)
        print(texto)
        print('NÃO É PALINDROMO!')





if __name__ == '__main__':
    print('Por favor, não execute as funções neste módulo, IMPORTE!!!')