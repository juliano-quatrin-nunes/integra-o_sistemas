import time
import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8005')

operacoes = {
    1: ('Soma', s.add),
    2: ('Subtração', s.sub),
    3: ('Multiplicação', s.mult),
    4: ('Divisão', s.div),
    5: ('Potenciação', s.pwr)
}

def main():
    print('\nQual operação você deseja fazer?')
    for key in operacoes:
        print(f"{key} para {operacoes[key][0]}")

    operacao = int(input('\n'))

    if not (operacao > 0 and operacao <= 5):
        print('Digite uma operação válida!\n')
        return

    print('Operação escolhida: ', operacoes[operacao][0])

    numero1 = input("\nDigite o 1º número:")
    numero2 = input("Digite o 2º número:")

    print('Resultado: ', operacoes[operacao][1](int(numero1), int(numero2)))

while True:
    main()
    time.sleep(2)