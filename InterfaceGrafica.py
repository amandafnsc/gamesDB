import JogoDOA
from Jogo_UsuarioDOA import JogoUsuarioDOA
from UsuarioDOA import UsuarioDAO
from JogoDOA import JogoDOA
from Jogo import Jogo
class InterfaceGrafica:
    def menu_principal(self):
        while True:
            print("""
⢋⣴⠒⡝⣿⣿⣿⣿⣿⡿⢋⣥⣶⣿⣿⣿⣿⣿⣿⣶⣦⣍⠻⣿⣿⣿⣿⣿⣷⣿
⢾⣿⣀⣿⡘⢿⣿⡿⠋⠄⠻⠛⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣷⣌⠻⣿⣿⣿⣿⣿
⠄⠄⠈⠙⢿⣦⣉⡁⠄⠄⣴⣶⣿⣿⢷⡶⣾⣿⣿⣿⣿⡛⠛⠻⠃⠙⢿⣿⣿⣿
⠄⠄⠄⠄⠄⠈⠉⣀⣀⣴⡟⢩⠁⠩⣝⢂⢨⣿⣿⣿⣿⢟⡛⣳⣶⣤⡘⠿⢋⣡
⠄⠄⠄⠄⠄⠄⠘⣿⣿⣿⣿⣾⣿⣶⣿⣿⣿⣿⣿⣿⣿⣆⣈⣱⣮⣿⣷⡾⠟⠋
⠄⠄⠄⠄⠄⠄⠄⠈⠿⠛⠛⣻⣿⠉⠛⠋⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠸⣿
⠄⠄⠄⠄⢀⡠⠄⢒⣤⣟⠿⣿⣿⣿⣷⣤⣤⣀⣀⣉⣉⣠⣽⣿⣟⠻⣿⣿⡆⢻
⠄⣀⠄⠄⠄⠄⠈⠋⠉⣿⣿⣶⣿⣟⣛⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣼⣿⡇⣸
⣿⠃⠄⠄⠄⠄⠄⠄⠠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⣿⣿⠁⢿
⡋⠄⠄⠄⠄⠄⠄⢰⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄
            """)
            print("========================")
            print("JOGOS DB - Menu Principal")
            print("========================")
            print("1 - Cadastrar Jogo")
            print("2 - Cadastrar Usuário")
            print("3 - Registrar Aquisição")
            print("4 - Listar Jogos")
            print("5 - Listar Usuários")
            print("6 - Buscar Jogo por Nome")
            print("7 - Buscar Jogo por Categoria")
            print("8 - Buscar Jogo por Editora")
            print("9 - Atualizar Jogo")
            print("10 - Atualizar Usuário")
            print("11 - Deletar Jogo")
            print("12 - Deletar Usuário")
            print("0 - Sair")
            print("========================")

            try:
                opcao = int(input("Digite uma opção [0-12]: "))
            except ValueError:
                print("Opção inválida! Digite um número.")
                continue

            if opcao == 1:
                self.menuInserirJogo()
            elif opcao == 2:
                self.menuInserirUser()
            elif opcao == 3:
                self.menuRegistrarAquisicao()
            elif opcao == 4:
                self.menuListarTodosJogos()
            elif opcao == 5:
                self.menuListarTodosUsuarios()
            elif opcao == 6:
                self.menuBuscarJogoPorNome()
            elif opcao == 7:
                self.menuBuscarJogoPorCategoria()
            elif opcao == 8:
                self.menuBuscarJogoPorEditora()
            elif opcao == 9:
                self.menuAtualizarJogo()
            elif opcao == 10:
                self.menuAtualizarUsuario()
            elif opcao == 11:
                self.menuDeletarJogo()
            elif opcao == 12:
                self.menuDeletarUsuario()
            elif opcao == 0:
                print("Saindo do sistema. Até a próxima, jogador!")
                break
            else:
                print("Opção inválida! Tente novamente.")
    
    def menuListarTodosUsuarios(self):
        dao = UsuarioDAO()
        print ('Listando Usuários...')
        pessoas = dao.listarUsuarios()
        encontrou = False
        for p in pessoas:
            encontrou = True
            print("Id = {} - Nome = {} - Email = {}".format(p.id, p.nome,p.email))
        if not encontrou:
            print ('Nenhum Registro Encontrado')
        self.menu_principal

    def menuBuscarJogoPorCategoria(self):
        dao = JogoDOA()
        categoria = input ("Categoria do Jogo:")
        jogos = dao.buscarJogoPorCategoria(categoria)
        encontrou = False
        for j in jogos:
            encontrou = True
            print("Id = {} - Nome = {} - Categoria = {} - Idioma = {} - Editora = {} - Descrição = {} - Duração = {} - Tipo = {} - Min Jogadores = {} - Max Jogadores = {}".format(
                j.id, j.nome, j.categoria, j.idioma, j.editora, j.descricao, j.duracao, j.tipo, j.min_jogadores, j.max_jogadores))
        if not encontrou:
            print ('Nenhum Registro Encontrado')
        self.menu_principal()
    
    def menuBuscarJogoPorEditora(self):
        dao = JogoDOA()
        editora = input ("Editora do Jogo:")
        jogos = dao.buscarJogoPorEditora(editora) 
        encontrou = False
        for j in jogos:
            encontrou = True
            print("Id = {} - Nome = {} - Categoria = {} - Idioma = {} - Editora = {} - Descrição = {} - Duração = {} - Tipo = {} - Min Jogadores = {} - Max Jogadores = {}".format(
                j.id, j.nome, j.categoria, j.idioma, j.editora, j.descricao, j.duracao, j.tipo, j.min_jogadores, j.max_jogadores))
        if not encontrou:
            print ('Nenhum Registro Encontrado')
        self.menu_principal()
    
    def menuInserirUser(self):
        dao = UsuarioDAO()
        nome = input ("Nome do Usuário:")
        email = input ("Email do Usuário:")
        senha = input ("Senha do Usuário:")
        sucess = dao.inserirUsuario(nome, email, senha)
        if sucess:
            print ("Usuario Inserido Com Sucesso!")
        else:
            print ("Erro ao Inserir o Usuário")
        self.menu_principal()

    def menuListarTodosJogos (self):
        doa = JogoDOA()
        print ('Listando Jogos...')
        pessoas = doa.listarJogos()
        encontou = False
        for p in pessoas:
            encontou = True
            print("Id = {} - Nome = {}".format(
                p.id, p.nome))
        if not encontou:
            print ('Nenhum Registro Encontrado')
        self.menu_principal()
    
    def menuBuscarJogoPorNome(self):
        dao = JogoDOA()
        nome = input ("Nome do Jogo:")
        jogos = dao.buscarJogoPorNome(nome)
        encontrou = False
        for j in jogos:
            encontrou = True
            print("Id = {} - Nome = {} - Categoria = {} - Idioma = {} - Editora = {} - Descrição = {} - Duração = {} - Tipo = {} - Min Jogadores = {} - Max Jogadores = {}".format(
                j.id, j.nome, j.categoria, j.idioma, j.editora, j.descricao, j.duracao, j.tipo, j.min_jogadores, j.max_jogadores))
        if not encontrou:
            print ('Nenhum Registro Encontrado')
        self.menu_principal()
    
    def menuInserirJogo(self):
        dao = JogoDOA()
        nome = input ("Nome do Jogo: ")
        descricao = input ("Descrição do Jogo: ")   
        duracao = input ("Duração do Jogo: ")
        tipo = input ("Mecânica do Jogo: ")
        idioma = input ("Idioma do Jogo: ")
        min_jogadores = input ("Número Mínimo de Jogadores: ")
        max_jogadores = input ("Número Máximo de Jogadores: ")
        nome_categoria = input ("Categoria do Jogo: ")
        nome_editora = input ("Nome da Editora: ")
        sucess = dao.inserirJogo(nome, descricao,idioma, duracao, tipo, min_jogadores, max_jogadores, nome_categoria, nome_editora)
        if sucess:
            print ("Jogo Inserido Com Sucesso!")
        else:
            print ("Erro ao Inserir o Jogo")
        self.menu_principal()
    
    def menuDeletarJogo(self):
        dao = JogoDOA()
        id = input ("Id do Jogo:")
        sucess = dao.deletarJogo(id)
        if sucess:
            print ("Jogo Deletado Com Sucesso!")
        else:
            print ("Erro ao Deletar o Jogo")
        self.menu_principal()
    
    def menuDeletarUsuario(self):
        dao = UsuarioDAO()
        id = input ("Id do Usuário:")
        sucess = dao.deletarUsuario(id)
        if sucess:
            print ("Usuário Deletado Com Sucesso!")
        else:
            print ("Erro ao Deletar o Usuário")
        self.menu_principal()
    
    def menuAtualizarUsuario(self):
        dao = UsuarioDAO()
        id = input ("Id do Usuário:")
        nome = input ("Nome do Usuário:")
        email = input ("Email do Usuário:")
        senha = input ("Senha do Usuário:")
        sucess = dao.atualizarUsuario(id, nome, email, senha)
        if sucess:
            print ("Usuário Atualizado Com Sucesso!")
        else:
            print ("Erro ao Atualizar o Usuário")
        self.menu_principal()
    
    def menuAtualizarJogo (self):
        dao = JogoDOA()
        id = input ("Id do Jogo:")
        nome = input ("Nome do Jogo:")
        descricao = input ("Descrição do Jogo:")
        idioma = input ("Idioma do Jogo:")
        duracao = input ("Duração do Jogo:")
        tipo = input ("Tipo do Jogo:")
        min_jogadores = input ("Número Mínimo de Jogadores:")
        max_jogadores = input ("Número Máximo de Jogadores:")
        nome_categoria = input ("Nome da Categoria:")
        nome_editora = input ("Nome da Editora:")
        sucess = dao.atualizarJogo(id, nome, descricao,idioma, duracao, tipo, min_jogadores, max_jogadores, nome_categoria, nome_editora)
        if sucess:
            print ("Jogo Atualizado Com Sucesso!")
        else:
            print ("Erro ao Atualizar o Jogo")
        self.menu_principal()
    
    def menuRegistrarAquisicao(self):
        dao = JogoUsuarioDOA()
        jogo_id = input("Digite o Nome do jogo: ")
        usuario_id = input("Digite o ID do usuário: ")
        local = input("Digite o local de aquisição: ")
        data_aquisicao = input("Digite a data de aquisição (DD-MM-YYYY): ")
        status = input("Digite o status da aquisição (ativo/inativo): ")

        sucesso = dao.registrarAquisicao(usuario_id, jogo_id, local, data_aquisicao, status)
        if sucesso:
            print("Aquisição registrada com sucesso!")
        else:
            print("Erro ao registrar a aquisição.")
        
        self.menu_principal()


if __name__ == '__main__':
    gui = InterfaceGrafica()
    gui.menu_principal()


