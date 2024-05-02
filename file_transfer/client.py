import socket

s = socket.socket()
host = 'localhost'
port = 6001

s.connect((host, port))

with open('FT_teste.xlsx', 'wb') as f:
    print('Arquivo Aberto')

    while True:
        print('Recebendo dados...')
        data = s.recv(1024*16)

        if not data:
            break
        f.write(data)

    f.close()

    print('Transferência realizada com sucesso')
    s.close()
    print('Conexão fechada')