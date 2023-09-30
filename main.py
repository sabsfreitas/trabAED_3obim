from graphics import *

def criar_arquivo_csv():
    header = ["Login", "Senha", "Tipo"]
    try:
        file = open("usuarios.csv", "r")
        file.close()  
    except FileNotFoundError:
        file = open("usuarios.csv", "w", newline="")
        file.write(",".join(header) + "\n")
    finally:
        file.close()

    # header = ["Login", "Senha", "Tipo"]
    # try:
    #     file = open("usuarios.csv", "r")
    # except FileNotFoundError:
    #     try:
    #         file = open("usuarios.csv", "w", newline="")
    #         file.write(",".join(header) + "\n")
    #     finally:
    #         file.close()
    # else:
    #     file.close()

# função para pegar as coordenadas de um botão automaticamente
def inside(point, rectangle):
    # is point inside rectangle?

    ll = rectangle.getP1()
    ur = rectangle.getP2()

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

def verificar_login(login, senha, tipo):
    file = open("usuarios.csv", "r")
    next(file) 
    for line in file:
        row = line.strip().split(",")
        if len(row) == 3 and row[0] == login and row[1] == senha and row[2] == tipo:
            return True
    file.close()
    return False

def adicionar_usuario(login, senha, tipo):
    file = open("usuarios.csv", "a", newline="")
    file.write(f"{login},{senha},{tipo}\n")
    file.close()

    # abaixo cria a ficha de treino do aluno
    if tipo == "aluno":
        file = open(f"treinos/{login}.csv", "w")
        file.write("treino,exercicio,series,carga,grupo muscular")
        file.close()
        file = open("treinos/lista.csv", "a", newline="")
        file.write(f"{login}\n")

def criar_janela_mensagem(mensagem, nome, cor):
    win = GraphWin(nome, 300, 100)
    win.setBackground("white")

    mensagem_texto = Text(Point(150, 50), mensagem)
    mensagem_texto.setSize(14)
    mensagem_texto.setStyle("bold")
    mensagem_texto.setTextColor(cor)
    mensagem_texto.draw(win)

    while not win.isClosed():
        click = win.checkMouse()
        if click:
            break 

    win.close()

def criar_janela_treino(login):
    win = GraphWin("Gerenciador de treinos", 800, 600)
    win.setBackground("#F0FFFF")

    logo = Image(Point(400, 300), "FitVibes.png")
    logo.draw(win)

    welcome_text = Text(Point(400, 90), f"Bem-vindo, {login}")
    welcome_text.setSize(30)
    welcome_text.setStyle("bold italic")
    welcome_text.setTextColor("black")
    welcome_text.draw(win)

    # caixa de pesquisa de alunos
    view_text = Text(Point(175, 180), "Visualize os treinos")
    view_text.setSize(15)
    view_text.setStyle("bold")
    view_text.draw(win)

    training_list_box = Rectangle(Point(50, 210), Point(300, 540))
    training_list_box.setFill("#95AE95")
    training_list_box.draw(win)

    # barra de pesquisa
    search_by_user = Rectangle(Point(50, 210), Point(300, 270))
    search_by_user.setFill("#C1E1C1")
    search_by_user.draw(win)
    search_bar = Entry(Point(157, 255), 22)
    search_bar.setFill("#F0FFFF")
    search_bar.draw(win)
    search_button = Rectangle(Point(258, 244), Point(294, 265))
    search_button.setFill("black")
    search_button.draw(win)
    search_icon = Text(Point(276, 254), "✅")
    search_icon.setSize(15)
    search_icon.setTextColor("white")
    search_icon.draw(win)
    search_text = Text(Point(175, 225), "Pesquise por aluno:")
    search_text.setSize(15)
    search_text.draw(win)
    search_list = Text(Point(175, 375), "")
    search_list.setSize(15)
    search_list.draw(win)
    update_list_button = Rectangle(Point(50, 480), Point(300, 540))
    update_list_button.setFill("#C1E1C1")
    update_list_button.draw(win)
    update_list_text = Text(Point(175, 510), "Lista completa de alunos:")
    update_list_text.setSize(15)
    update_list_text.draw(win)

    # caixa de opções
    options_text = Text(Point(625, 180), "Opções")
    options_text.setSize(15)
    options_text.setStyle("bold")
    options_text.draw(win)

    trainer_options_box = Rectangle(Point(500, 210), Point(750, 540))
    trainer_options_box.setFill("#95AE95")
    trainer_options_box.draw(win)

    # variável que determina se um usuário foi selecionado...
    is_user_selected = False
    clickonce = False

    # opções para criar ou visualizar treinos no dispositivo
    trainer_createnew_button = Rectangle(Point(500, 210), Point(750, 320))
    trainer_createnew_button.setFill("#C1E1C1")
    trainer_createnew_button.draw(win)
    trainer_createnew_text = Text(Point(625, 265), "Criar um novo treino base")
    trainer_createnew_text.setSize(12)
    trainer_createnew_text.draw(win)
    trainer_view_button = Rectangle(Point(500, 320), Point(750, 430))
    trainer_view_button.setFill("#C1E1C1")
    trainer_view_button.draw(win)
    trainer_view_text = Text(Point(625, 375), "Visualizar seus treinos base")
    trainer_view_text.setSize(12)
    trainer_view_text.draw(win)
    trainer_lorem = Text(Point(625, 485), "Um treino base é salvo\nno seu dispositivo para que\npossa ser reutilizado!")
    trainer_lorem.setSize(12)
    trainer_lorem.draw(win)


    while True:
        if win.isClosed():
            break

        clickPoint = win.getMouse()

        # ao clicar na barra de pesquisa...
        if inside(clickPoint, search_button):
            pesquisa = search_bar.getText()
            is_user_selected = pesquisar(pesquisa, search_list)

        # ao clicar no botão "lista completa de alunos: "...
        if inside(clickPoint, update_list_button):
            criar_html_l_alunos()

        if inside(clickPoint, trainer_createnew_button):
            criador_treino("create_base")

        # se um usuário estiver selecionado as opções mudarão!
        if is_user_selected:
            trainer_lorem.undraw()
            trainer_createnew_text.setText("Associar um treino base ao aluno")
            trainer_mod_button = Rectangle(Point(500, 430), Point(750, 540))
            trainer_mod_button.setFill("#C1E1C1")
            trainer_mod_button.draw(win)
            trainer_view_text.setText("Visualizar treino atual do aluno")
            trainer_mod_text = Text(Point(625, 485), "Modificar treino atual do aluno")
            trainer_mod_text.setSize(12)
            trainer_mod_text.draw(win)
            clickonce = True

        # as opções retornarão ao normal ao deselecionar o usuário.
        if not is_user_selected and clickonce:
            trainer_createnew_text.setText("Criar um novo treino base")
            trainer_view_text.setText("Visualizar seus treinos base")
            trainer_mod_text.undraw()
            trainer_mod_button.undraw()
            trainer_lorem.draw(win)
            clickonce = False

    win.close()

# pesquisa e retorna aluno
def pesquisar(pesquisa, search_list):
    file = open("treinos/lista.csv", "r")
    pesquisa += "\n"
    for line in file:
        if pesquisa == line:
            search_list.setText(f"{line}Aluno encontrado!")
            return True
    search_list.setText("Aluno não encontrado.")
    return False

# gera um html com a lista de alunos
def criar_html_l_alunos():
    alunos = ""
    file = open("treinos/lista.csv", "r")
    for line in file:
        alunos += f"""    <p>
        {line}    </p>\n"""
    file.close()
    file = open("paginas/lista_de_alunos.html", "w")
    file.write(f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Alunos</title>
</head>
<body>
               
    <h1>Lista de alunos:</h1>
    <br>
{alunos}
</body>
</html>""")
    file.close()
    criar_janela_mensagem("Lista de alunos atualizada!\nCheque a pasta para acessar o\nhtml contendo a lista completa.", "Atualização completa", "green")

def criador_treino(option):
    if option == "create_base":
        win = GraphWin("Criador de Treinos", 640, 480)
        win.setBackground("#F0FFFF")

        logo = Image(Point(320, 240), "FitVibes.png")
        logo.draw(win)

        titulo = Text(Point(320, 72), "Criador de treino base")
        titulo.setSize(15)
        titulo.setStyle("bold italic")
        titulo.draw(win)

        treino_base = "treino,exercicio,series,carga,grupo muscular\n"

def criar_janela():
    win = GraphWin("FitVibe", 440, 400)
    win.setBackground("#F0FFFF")

    logo = Image(Point(50, 50), "FitVibes.png")
    logo.draw(win)

    titulo = Text(Point(250, 50), "FitVibe - Wellness & Lifestyle")
    titulo.setSize(17)
    titulo.setStyle("bold italic")
    titulo.setTextColor("black")
    titulo.draw(win)

    # Login
    label_login = Text(Point(120, 130), "Login:")
    label_login.setTextColor("black")
    label_login.setStyle("bold")
    label_login.draw(win)

    login_entry = Entry(Point(250, 130), 20)
    login_entry.draw(win)
    login_entry.setFill("white")

    # Senha
    label_senha = Text(Point(120, 180), "Senha:")
    label_senha.setTextColor("black")
    label_senha.setStyle("bold")
    label_senha.draw(win)

    senha_entry = Entry(Point(250, 182), 20)
    senha_entry.draw(win)
    senha_entry.setFill("white")

    # Tipo
    label_tipo = Text(Point(190, 230), "Tipo (aluno ou treinador):")
    label_tipo.setTextColor("black")
    label_tipo.setStyle("bold")
    label_tipo.draw(win)

    tipo_entry = Entry(Point(250, 260), 20)
    tipo_entry.draw(win)
    tipo_entry.setFill("white")

    cadastrar_button = Rectangle(Point(80, 280), Point(180, 310))
    cadastrar_button.setFill("#C1E1C1")
    cadastrar_button.draw(win)

    label_cadastrar = Text(Point(130, 295), "Cadastrar")
    label_cadastrar.setTextColor("black")
    label_cadastrar.setSize(10)
    label_cadastrar.setStyle("bold")
    label_cadastrar.draw(win)

    logar_button = Rectangle(Point(295, 280), Point(395, 310))
    logar_button.setFill("#C1E1C1")
    logar_button.draw(win)

    label_logar = Text(Point(345, 295), "Logar")
    label_logar.setTextColor("black")
    label_logar.setSize(10)
    label_logar.setStyle("bold")
    label_logar.draw(win)

    return win, login_entry, senha_entry, tipo_entry

def main():
    criar_arquivo_csv()
    win, login_entry, senha_entry, tipo_entry = criar_janela()

    while True:
        click = win.checkMouse()
        if click is not None:
            login = login_entry.getText()
            senha = senha_entry.getText()
            tipo = tipo_entry.getText().strip()

            if click.getX() >= 80 and click.getX() <= 180 and click.getY() >= 280 and click.getY() <= 310:
                if login and senha and tipo:
                    if tipo.lower() == "treinador" or tipo.lower() == "aluno":
                        if not verificar_login(login, senha, tipo):
                            adicionar_usuario(login, senha, tipo)
                            criar_janela_mensagem("Cadastro realizado com sucesso!", "Sucesso", "green")
                        else:
                            criar_janela_mensagem("Esse usuário já existe.", "Erro", "red")
                    else:
                        criar_janela_mensagem("Apenas treinadores ou alunos.", "Erro", "red")
            elif click.getX() >= 295 and click.getX() <= 395 and click.getY() >= 280 and click.getY() <= 310:
                if login and senha and tipo:
                    if verificar_login(login, senha, tipo):
                        criar_janela_mensagem(f"Login realizado com sucesso!\nBem-vindo, {login}", "Sucesso", "green")
                        if tipo.lower().strip() == "treinador":
                            win.close()
                            criar_janela_treino(login) # se é treinador, abre janela de treino e fecha a anterior. se for aluno, tem que criar janela p visualização dos seus treinos
                    else:
                        criar_janela_mensagem("Faça um cadastro primeiro.", "Erro", "red")
        if win.isClosed():
            break


if __name__ == "__main__":
    main()