def soma(num1:int,num2:int) -> None:
    total = num1+num2
    print(f'A soma de {num1}+{num2} é {total}')

def subtracao(num1:int,num2:int) -> None:
    total = num1-num2
    print(f'A subtração de {num1}-{num2} é {total}')

def multiplicacao(num1:int,num2:int) -> None:
    total = num1*num2
    print(f'A multiplicação de {num1}*{num2} é {total}')

def divisao(num1:int,num2:int) -> None:
    if num1 ==0 or num2 == 0:
        print('Impossível dividir por 0!')
    else:
        total = num1/num2
        print(f'A divisão de {num1}/{num2} é {total}')

def decimalBin(dividendo:int):
  numero_digitado = dividendo
  quociente = 1
  lista = []

  while quociente >= 1:
    resto = dividendo%2
    lista.insert(0,resto)
    quociente = dividendo // 2
    dividendo = quociente

  binario = ''.join([str(item) for item in lista])
  print("O número",numero_digitado,", quando convertido em binário, vale:",binario)

def binDecimal(binario:int):
  n = len(str(binario))
  valor_digitado = binario
  decimal = 0
  i = 0

  while n >= 0:
    resto = binario % 10
    decimal = decimal + (resto * (2**i))
    n = n - 1
    i = i + 1
    binario = binario // 10

  print("O número (binario) digitado",valor_digitado,", na base decimal, vale:",decimal)

def imc(peso:float,altura:float):
    altura = altura*altura
    imc = peso/altura
    print(f'Seu IMC é de: {imc:.2f}')

def medidas(medida:float):
    
    '''
    1 metro tem 100cm
    1 centímetro tem 10mm
    1 km tem 1000m

    '''

if __name__ == '__main__':
    print('Por favor, não execute as funções neste módulo, IMPORTE!!!')