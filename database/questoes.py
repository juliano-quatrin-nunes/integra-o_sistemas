import sqlite3

conn = sqlite3.connect('aula.db')
c = conn.cursor()

def ex_1(): 
    # Quem trancou o curso?

    c.execute("SELECT Nome FROM Alunos WHERE Situacao = 'Trancamento'")
    data = c.fetchall()
    print('Alunos que trancaram o curso: ')
    for row in data:
        print(row[0])

def ex_2():
    # Quem entrou após 2012?

    c.execute("SELECT Nome FROM Alunos WHERE Ingresso > 2012")
    data = c.fetchall()
    print('\nAlunos que ingressaram após 2012: ')
    for row in data:
        print(row[0])

def ex_3():
    # Qual a idade de Patrick?

    c.execute("SELECT Idade FROM Alunos WHERE Nome = 'Patrick'")

    data = c.fetchall()
    print('\nA idade de Patrick é:', data[0][0])

def ex_4():
    # Alterar o nome de Pedro para Carlos (UPDATE)

    c.execute("UPDATE Alunos SET Nome = 'Carlos' WHERE Nome = 'Pedro'")
    conn.commit()

    if (c.rowcount == 1):
        print('\nNome Pedro alterado para Carlos com sucesso!')
    else:
        print('\nNão existia nenhum Pedro no banco de dados.')


ex_1()
ex_2()
ex_3()
ex_4()
c.close()
conn.close()