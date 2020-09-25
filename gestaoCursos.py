import sqlite3



conn = sqlite3.connect('estudo.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS estudo(
        idd int NOT NULL,
        plataformas TEXT NOT NULL,
        nomes TEXT NOT NULL,
        horasTotais int NOT NULL,
        horasFeitas int NOT NULL,
        porcentagemHorasFeitas int NOT NULL);''')
#======================================== funçoes ========================================
def incluirDados(idd, plataforma, nome, horasTotais, horasFeitas, porcentagemHorasFeitas):
    """ incluir dados no Banco """
    cursor.execute(f'''
        INSERT INTO estudo (idd, plataformas, nomes, horasTotais, horasFeitas, porcentagemHorasFeitas)
        VALUES ('{idd}', '{plataforma}', '{nome}', '{horasTotais}', '{horasFeitas}', '{porcentagemHorasFeitas}');''')
    conn.commit()

def mostrarDados(opcao, platafomaEscolhida=''):
    """ Mostrar os dados do banco """
    
    if opcao == '1':
        print('#'*80,'\n')
        print('                          TODOS OS CURSOS  \n')
        print('id / Plataforma  / curso / horas Total / horas estudadas / Porcentagem Feita')
        cursor.execute('''SELECT * FROM estudo ORDER BY plataformas; ''')
        for plataforma in cursor.fetchall():
            print(plataforma)
        print('\n')
        print('#'*80)

    elif opcao == '2':   
        print('#'*80,'\n')
        print('                        CURSOS ACIMA DE 50% \n')
        print(' id / Plataforma  / curso / horas Total / horas estudadas / Porcentagem Feita')
        cursor.execute('''SELECT * FROM estudo WHERE porcentagemHorasFeitas >= 50 AND porcentagemHorasFeitas <=99.9; ''')
        for plataforma in cursor.fetchall():
            print(plataforma)
        print('\n')
        print('#'*80)
        
    elif opcao == '3':
        print('#'*80,'\n')
        print('                        CURSOS ABAIXO DE 50% \n')
        print('id / Plataforma  / curso / horas Total / horas estudadas / Porcentagem Feita')
        cursor.execute('''SELECT * FROM estudo WHERE porcentagemHorasFeitas >0 AND porcentagemHorasFeitas <= 49.9; ''')
        for plataforma in cursor.fetchall():
            print(plataforma)
        print('\n')
        print('#'*80)
            
    elif opcao == '4':
        print('#'*80,'\n')
        print('                        CURSOS CONCLUIDOS \n')
        print('id / Plataforma  / curso / horas Total / horas estudadas / Porcentagem Feita')
        cursor.execute('''SELECT * FROM estudo WHERE horasTotais = horasFeitas; ''')
        for plataforma in cursor.fetchall():
            print(plataforma)
        print('\n')
        print('#'*80)
            
    elif opcao == '5':
        print('#'*80,'\n')
        print('                        CURSOS NÃO INICIADOS \n')
        print('id / Plataforma  / curso / horas Total / horas estudadas / Porcentagem Feita')
        cursor.execute('''SELECT * FROM estudo WHERE porcentagemHorasFeitas = 0; ''')
        for plataforma in cursor.fetchall():
            print(plataforma)
        print('\n')
        print('#'*80)
    elif opcao == '6':
        print('\n','#'*80)
        print(f'                        CURSOS {plataformaEscolhida} ')
        print('id / Plataforma  / curso / horas Total / horas estudadas / Porcentagem Feita \n')
        cursor.execute(f'''SELECT * FROM estudo WHERE plataformas = '{plataformaEscolhida}' ORDER BY idd; ''')
        for plataforma in cursor.fetchall():
            print(plataforma)
        print('\n')
        print('#'*80)

def update(nomeCurso):
    """ """
    cursor.execute(f'''SELECT * FROM estudo WHERE plataformas = '{nomeCurso}'; ''')
    for plataforma in cursor.fetchall():
        print(plataforma)
    atualizar = input('\n'
                      'Nome plataforma esta errado: 1\n'
                      'Nome do curso esta errado: 2\n'
                      'Atualizar horas Totais: 3\n'
                      'Atualizar horas Feitas: 4\n'
                      'Atulizar porcentagem feita: 5\n'
                      'Deseja atualizar o que: ')
    if atualizar == '1':
        novoValor = input('Digite o nome correto da plataforma: ')
        antigoValor = input ('Digite o nome errado para atualizar: ')
        idValor = input('Digite o numero do curso: ')
        cursor.execute(f'''UPDATE estudo SET plataformas = REPLACE(plataformas, '{antigoValor}', '{novoValor}') WHERE idd = {idValor} ''')
        conn.commit()
    elif atualizar == '2':
        novoValor = input('Digite o nome correto do curso: ')
        antigoValor = input ('Digite o nome errado para atualizar: ')
        idValor = input('Digite o numero do curso: ')
        cursor.execute(f'''UPDATE estudo SET nomes = REPLACE(nomes, '{antigoValor}', '{novoValor}') WHERE idd = {idValor} ''')
        conn.commit()
    elif atualizar == '3':
        novoValor = input('Digite a nova hora total do curso: ')
        antigoValor = input ('Digite a antiga hora para atualizar: ')
        idValor = int(input('Digite o numero do curso: '))
        cursor.execute(f'''UPDATE estudo SET horasTotais = REPLACE(horasTotais, '{antigoValor}', '{novoValor}') WHERE idd = {idValor} ''')
        cursor.execute(f'''UPDATE estudo SET porcentagemHorasFeitas = horasFeitas * 100 / horasTotais WHERE idd = {idValor}''')
        cursor.execute(f''' SELECT * FROM estudo WHERE idd = {idValor} ''')
        for plataforma in cursor.fetchall():
            print(plataforma, '\n')
        conn.commit()
    elif atualizar == '4':
        novoValor = input('Nova horas estudadas: ')
        antigoValor = input ('Digite a antiga hora para atualizar: ')
        idValor = int(input('Digite o numero do curso: '))
        cursor.execute(f'''UPDATE estudo SET horasFeitas = REPLACE(horasFeitas, '{antigoValor}', '{novoValor}') WHERE idd = {idValor} ''')
        cursor.execute(f'''UPDATE estudo SET porcentagemHorasFeitas = horasFeitas * 100 / horasTotais WHERE idd = {idValor}''')
        cursor.execute(f''' SELECT * FROM estudo WHERE idd = {idValor} ''')
        for plataforma in cursor.fetchall():
            print(plataforma, '\n')
        conn.commit()
    elif atualizar == '5':
        novoValor = input('Nova porcentagem  estudadas: ')
        antigoValor = input ('Digite a antiga porcentagem para atualizar: ')
        idValor = int(input('Digite o numero do curso: '))
        cursor.execute(f'''UPDATE estudo SET porcentagemHorasFeitas = REPLACE(porcentagemHorasFeitas, '{antigoValor}', '{novoValor}') WHERE idd = {idValor} ''')
        cursor.execute(f'''UPDATE estudo SET horasFeitas = horasTotais * porcentagemHorasFeitas / 100  WHERE idd = {idValor}''')
        cursor.execute(f''' SELECT * FROM estudo WHERE idd = {idValor} ''')
        for plataforma in cursor.fetchall():
            print(plataforma, '\n')
        conn.commit()
    else:
        print('Favor digitar uma opção correta')
           
def mostrarPlataformas():
    print('#'*20)
    print(f'           Plataformas              \n')
    cursor.execute(f'''SELECT DISTINCT Plataformas FROM estudo; ''')
    for plataforma in cursor.fetchall():
        print(plataforma)
    print('#'*20, '\n')

def delete():
    """ Deletar um dado """
    mostrarDados('1')
    escolherId = input('Digite o id para excluir: ')
    ctz = input('Deseja realmente deletar os dados: (s/n)')
    if ctz == 's':
        sql = (f''' DELETE FROM estudo WHERE idd = '{escolherId}' ''')
        cursor.execute(sql)
        print('Dados deletados!')
    conn.commit()

def menu():
    print('\n')
    print('#'*31)
    print('#          Menu               #')
    print('#  0 : Sair                   #')
    print('#  1 : Listar cursos salvos   #')
    print('#  2 : Inserir novo curso     #')
    print('#  3 : Atualizar curso salvo  #')
    print('#  4 : Apagar curso           #')
    print('#                             #')
    print('#                             #')
    print('#'*31,'\n')

def menuMostrarDados():
    print('\n')
    print('#'*53)
    print('#      Menu    Listar Cursos                      \n')
    print('#  0 : Sair                                         ')
    print('#  1 : Listar todos cursos salvos                   ')
    print('#  2 : Listar cursos acima de 50%                   ')
    print('#  3 : Listar cursos abaixo de 50%                  ')
    print('#  4 : Listar cursos concluidos                     ')
    print('#  5 : Listar cursos não inciados                   ')
    print('#  6 : Listar por plataformas \n                    ')
    print('#'*53,'\n')
    
#======================================== Programa =====================================

while True:

    menu()

    start = input('Digite uma opção do menu: ')

    if start == '0':
        print('Saindo....')
        break
    if start == '1':
        menuMostrarDados()
        opcao = input('Digite uma opção do menu: ')
        if opcao == '6':
            mostrarPlataformas()
            plataformaEscolhida = input('Digite o nome da plataforma: ')
            mostrarDados(opcao, plataformaEscolhida)
        else:
            mostrarDados(opcao)
    if start == '2':
        identificadorCurso = int(input('Digite o id do curso: '))
        plat = input('Coloque o nome da plataforma: ')
        name = input('Nome do curso: ')
        horasTotais = float(input('Quantidade de horas: '))
        horasFeitas = float(input('Quantidade de horas estudadas: '))
        porcentagemHorasFeitas = float(input('Digite a porcentagem de horas feitas: '))

        if horasFeitas == 0:
            horasFeitas = (porcentagemHorasFeitas * horasTotais) / 100
        if porcentagemHorasFeitas == 0:
            porcentagemHorasFeitas = (horasFeitas * 100) / horasTotais
        incluirDados(identificadorCurso, plat, name, horasTotais, horasFeitas, porcentagemHorasFeitas)
    if start == '3':
        mostrarPlataformas()
        nomeCurso = input('Em qual plataforma esta o curso: ')
        update(nomeCurso)
    if start == '4':
        deletar = input('deseja deletar algum dado: (s/n)')
        if deletar == 's':
            delete()



