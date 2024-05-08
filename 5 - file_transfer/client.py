import socket
import time

s = socket.socket()
host = 'localhost'
port = 6001

s.connect((host, port))

with open('FT_teste_recebido.xlsx', 'wb') as f:
    print('Arquivo Aberto')

    print('Recebendo dados...')
    data = s.recv(1024*16)

    f.write(data)

    f.close()

with open('FT_teste_recebido.xlsx', 'rb') as f:
    print('Aguardando alteração...')
    time.sleep(10)                      ## Espera usuário alterar por 10 segundos

    l = f.read(1024*16)

    print('Enviando alterações...')
    s.send(l)

    f.close()

    print('Transferência realizada com sucesso')
    s.close()
    print('Conexão fechada')