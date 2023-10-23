from graphics import *
import webbrowser
import os

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

def criar_janela_lista(mensagem, nome, cor):
    win = GraphWin(nome, 300, 600)
    win.setBackground("#F0FFFF")

    mensagem_texto = Text(Point(150, 300), mensagem)
    mensagem_texto.setSize(10)
    mensagem_texto.setTextColor(cor)
    mensagem_texto.draw(win)

    while not win.isClosed():
        click = win.checkMouse()
        if click:
            break 

    win.close()

def desenhar_x(posicao, win):
    x1 = posicao.getX() - 8
    y1 = posicao.getY() - 8
    x2 = posicao.getX() + 8
    y2 = posicao.getY() + 8
    linha_1 = Line(Point(x1, y1), Point(x2, y2))
    linha_1.draw(win)
    linha_2 = Line(Point(x1, y2), Point(x2, y1))
    linha_2.draw(win)
    return [linha_1, linha_2]

def apagar_x(linhas):
    for linha in linhas:
        linha.undraw()

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
        file = open(f"public/treinos/{login}.csv", "w")
        file.write("treino,exercicio,series,carga,grupo muscular")
        file.close()
        file = open("public/treinos/lista.csv", "a", newline="")
        file.write(f"{login}\n")

def criar_janela_mensagem(mensagem, nome, cor):
    win = GraphWin(nome, 300, 100)
    win.setBackground("#F0FFFF")

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
    
# pesquisa e retorna aluno
def pesquisar(pesquisa, search_list):
    file = open("public/treinos/lista.csv", "r")
    pesquisa += "\n"
    for line in file:
        if pesquisa == line:
            search_list.setText(f"{line}Aluno encontrado!")
            return True
    search_list.setText("Aluno não encontrado.")
    return False

def verificar_cliques(win, checkbox_aluno, checkbox_treinador, linhas_aluno, linhas_treinador):
    aluno_check = False
    treinador_check = False
    tipo_entry = ""

    while True:
        click = win.getMouse()
        if not aluno_check and inside(click, checkbox_aluno):
            linhas_aluno = desenhar_x(checkbox_aluno.getCenter(), win)
            tipo_entry = "aluno"
            aluno_check = True
            treinador_check = False
            if linhas_treinador:
                apagar_x(linhas_treinador)

        elif not treinador_check and inside(click, checkbox_treinador):
            linhas_treinador = desenhar_x(checkbox_treinador.getCenter(), win)
            tipo_entry = "treinador"
            treinador_check = True
            aluno_check = False
            if linhas_aluno:
                apagar_x(linhas_aluno)

        print(tipo_entry)
        return tipo_entry

# gera um html com a lista de alunos - table
def criar_html_l_alunos():
    alunos = ""
    file = open("public/treinos/lista.csv", "r")
    alunos += "<table border='1'>\n"
    alunos += "    <tr>\n"
    alunos += "        <th>Lista de Alunos</th>\n"
    alunos += "    </tr>\n"
    for line in file:
        alunos += "    <tr>\n"
        cells = line.strip().split(",") 
        for cell in cells:
            alunos += f"        <td>{cell}</td>\n"
        alunos += "    </tr>\n"
    alunos += "</table>\n"
    file.close()

    file = open("public/paginas/lista_de_alunos.html", "w")
    file.write(f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Alunos</title>
</head>
<body>
    {alunos}
</body>
</html>""")
    file.close()
    criar_janela_mensagem("Lista de alunos atualizada!", "Atualização completa", "green")

    # diretório atual do script
    script_dir = os.path.dirname(__file__)

    rel_path = 'public/paginas/lista_de_alunos.html'
    abs_file_path = os.path.join(script_dir, rel_path)

    # Verifica se o arquivo existe
    if os.path.exists(abs_file_path):
        webbrowser.open('file://' + abs_file_path)
    else:
        print("Arquivo não encontrado.")

def criar_janela():
    win = GraphWin("FitVibe", 440, 400)
    win.setBackground("#F0FFFF")

    logo = Image(Point(50, 50), "public/FitVibes.png")
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

        # Checkbox do aluno
    checkbox_aluno = Rectangle(Point(250, 200), Point(270, 220))
    checkbox_aluno.draw(win)

    texto_checkbox_aluno = Text(Point(190, 210), "Aluno:")
    texto_checkbox_aluno.setTextColor("black")
    texto_checkbox_aluno.setStyle("bold")
    texto_checkbox_aluno.draw(win)

    # Checkbox do treinador
    checkbox_treinador = Rectangle(Point(250, 240), Point(270, 260))
    checkbox_treinador.draw(win)

    texto_checkbox_treinador = Text(Point(190, 250), "Treinador:")
    texto_checkbox_treinador.setTextColor("black")
    texto_checkbox_treinador.setStyle("bold")
    texto_checkbox_treinador.draw(win)

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

    aluno_check = False
    treinador_check = False
    linhas_aluno = []
    linhas_treinador = []

    tipo_entry = verificar_cliques(win, checkbox_aluno, checkbox_treinador, linhas_aluno, linhas_treinador)

    return win, login_entry, senha_entry, tipo_entry