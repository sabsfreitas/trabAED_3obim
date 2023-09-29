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
    win.setBackground("white")

    while True:
        click = win.checkMouse()
        if click is not None:
            # logica
            pass # retira isso quando for codar, eh so p nao dar erro de identação no if abaixo
        if win.isClosed():
            break

    win.close()


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
                    if tipo.lower().strip() == "treinador" or tipo.lower().strip() == "aluno":
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