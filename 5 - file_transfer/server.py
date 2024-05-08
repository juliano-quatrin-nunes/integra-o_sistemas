import socket

port = 6001
s = socket.socket()

host = 'localhost'
s.bind((host, port))
s.listen(1)

while True:
    conn, addr = s.accept()
    print('Conectado por:', addr)

    filename = 'FT_teste.xlsx'
    f = open(filename, 'r+b')
    f.fileno
    l = f.read(1024*16)

    while(l):
        conn.send(l)
        l = f.read(1024*16)

    while True:
        print('Recebendo novos dados...')
        data = conn.recv(1024*16)

        if not data:
            break
        
        f.write(data)           ## Adiciona dados editados no cliente
    
    f.close()

    print('Novo arquivo recebido e FT_teste alterado')
    conn.close()
    print('Conexão fechada')