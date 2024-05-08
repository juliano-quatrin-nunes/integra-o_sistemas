from socket import *

serverHost = '127.0.0.1'
serverPort = 50009

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

print('Chat iniciado, digite q e pressione enter para finalizar.')

while True:
    msg = input('\nDigite uma mensagem: ')

    sockobj.send(msg.encode())

    if msg == 'q':
        sockobj.close()
        break

    data = sockobj.recv(1024)

    print('\nServer enviou: ', data.decode())