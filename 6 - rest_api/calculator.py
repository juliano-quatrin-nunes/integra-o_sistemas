import requests
import os
import json

BASE_URL = "https://mrl0vy3w26.execute-api.sa-east-1.amazonaws.com/api/"

operacoes = {
    1: ('soma', 'soma'),
    2: ('subtração', 'sub'),
    3: ('multiplicação', 'mult'),
    4: ('divisão', 'div'),
}

def main():
    print('\nQual operação você deseja fazer?')
    for key in operacoes:
        print(f"{key} para {operacoes[key][0]}")

    operacao = int(input('\n'))

    if not (operacao > 0 and operacao <= 4):
        print('Operação inválida!\n')
        return

    print('Operação escolhida: ', operacoes[operacao][0])

    numero1: str = input("\nDigite o 1º número:")
    numero2: str = input("Digite o 2º número:")

    request_url = BASE_URL + '/'+ operacoes[operacao][1]+ '/'+ numero1+ '/'+ numero2

    response = requests.get(request_url).json()

    print(response)

main()