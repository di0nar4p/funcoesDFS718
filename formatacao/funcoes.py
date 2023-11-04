import random as ran
def titulo(texto:str):
    print(texto.capitalize())


def olutit(texto:str):
    nome=str()
    for letra in texto[::-1]:
        nome= nome+letra
    print(nome.capitalize())

def cesarCypher(texto:str):
    cifra= str()
    base= {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I',10:'J',11:'K',12:'L',
    13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'W',23:'X',24:'Y',25:'Z'
           
           
           
           
           }
    for letra in texto:
        cifra += letra+ base[ran.randint(1,25)]
    frase = cifra.split()
    cifra = ''.join(frase)   
    print(cifra.lower())




if __name__ == '__main__':
    print('Por favor, não execute as funções neste módulo, IMPORTE!!!')