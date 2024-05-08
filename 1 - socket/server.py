from socket import *

meuHost = '127.0.0.1'
minhaPort = 50009

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((meuHost, minhaPort))
sockobj.listen(1)

while True:
    conexao, endereco = sockobj.accept()
    print('Server conectado por', endereco)

    while True:
        data = conexao.recv(1024).decode()

        if(data == 'q'):
            print('Cliente desconectou')
            break

        print('\nCliente enviou: ', data)

        msg = input('\nDigite uma mensagem: ')

        conexao.send(msg.encode())

        