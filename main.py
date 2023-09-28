from graphics import *

def criar_arquivo_csv():
    header = ["Login", "Senha", "Tipo"]
    try:
        file = open("usuarios.csv", "r")
    except FileNotFoundError:
        try:
            file = open("usuarios.csv", "w", newline="")
            file.write(",".join(header) + "\n")
        finally:
            file.close()
    else:
        file.close()

def verificar_login(login, senha, tipo):
    try:
        file = open("usuarios.csv", "r")
        next(file) 
        for line in file:
            row = line.strip().split(",")
            if len(row) == 3 and row[0] == login and row[1] == senha and row[2] == tipo:
                return True
    finally:
        file.close()
    return False

def adicionar_usuario(login, senha, tipo):
    try:
        file = open("usuarios.csv", "a", newline="")
        file.write(f"{login},{senha},{tipo}\n")
    finally:
        file.close()

def criar_janela_sucesso():
    win = GraphWin("Sucesso", 300, 100)
    win.setBackground("white")

    mensagem_sucesso = Text(Point(150, 50), "Cadastro realizado com sucesso!")
    mensagem_sucesso.setSize(14)
    mensagem_sucesso.setStyle("bold")
    mensagem_sucesso.setTextColor("green")
    mensagem_sucesso.draw(win)

    win.getMouse() 
    win.close()

def criar_janela():
    win = GraphWin("FitVibe", 700, 600)
    win.setBackground("#F0FFFF")

    logo = Image(Point(180, 50), "FitVibes.png")
    logo.draw(win)

    titulo = Text(Point(350, 100), "FitVibe - Wellness & Lifestyle")
    titulo.setSize(17)
    titulo.setStyle("bold italic")
    titulo.setTextColor("black")
    titulo.draw(win)

    # Login
    label_login = Text(Point(160, 130), "Login:")
    label_login.setTextColor("black")
    label_login.setStyle("bold")
    label_login.draw(win)

    login_entry = Entry(Point(420, 130), 20)
    login_entry.draw(win)
    login_entry.setFill("white")

    # Senha
    label_senha = Text(Point(160, 180), "Senha:")
    label_senha.setTextColor("black")
    label_senha.setStyle("bold")
    label_senha.draw(win)

    senha_entry = Entry(Point(420, 180), 20)
    senha_entry.draw(win)
    senha_entry.setFill("white")

    # Tipo
    label_tipo = Text(Point(160, 230), "Tipo (aluno ou treinador):")
    label_tipo.setTextColor("black")
    label_tipo.setStyle("bold")
    label_tipo.draw(win)

    tipo_entry = Entry(Point(420, 230), 20)
    tipo_entry.draw(win)
    tipo_entry.setFill("white")

    cadastrar_button = Rectangle(Point(150, 260), Point(250, 290))
    cadastrar_button.setFill("#C1E1C1")
    cadastrar_button.draw(win)

    label_cadastrar = Text(Point(200, 275), "Cadastrar")
    label_cadastrar.setTextColor("black")
    label_cadastrar.setSize(10)
    label_cadastrar.setStyle("bold")
    label_cadastrar.draw(win)

    return win, login_entry, senha_entry, tipo_entry

def main():
    criar_arquivo_csv()
    win, login_entry, senha_entry, tipo_entry = criar_janela()

    while True:
        click = win.getMouse()

        if click.getX() >= 150 and click.getX() <= 250 and click.getY() >= 280 and click.getY() <= 310:
            login = login_entry.getText()
            senha = senha_entry.getText()
            if login and senha:
                tipo = tipo_entry.getText().strip()
                if tipo:
                    if not verificar_login(login, senha, tipo):
                        adicionar_usuario(login, senha, tipo)
                        print(f"Cadastro de {tipo} realizado com sucesso!")
                        criar_janela_sucesso()
                    else:
                        print("Usuário já existe...")


if __name__ == "__main__":
    main()