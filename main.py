from graphics import * 
from functions import *
import webbrowser
import os

# apenas funções principais

def criar_janela_aluno(login):
    win = GraphWin("Seus treinos", 800, 600)
    win.setBackground("#F0FFFF")

    welcome_text = Text(Point(400, 100), f"Seus treinos")
    welcome_text.setSize(24)
    welcome_text.setStyle("bold")
    welcome_text.setTextColor("black")
    welcome_text.draw(win)

    aluno_text = Text(Point(650, 50), f"Aluno: {login}")
    aluno_text.setSize(18)
    aluno_text.setStyle("normal")
    aluno_text.setTextColor("black")
    aluno_text.draw(win)

    file = open(f"public/treinos/{login}.csv", "r")
    for _ in range(1):
        next(file)
    cache = "".join(file)
    file.close()
    
    script_dir = os.path.dirname(__file__)

    rel_path = f'public/paginas/{login}.html'
    abs_file_path = os.path.join(script_dir, rel_path)

    split = cache.strip().split(",")

    count = 0
    header_ficha = []
    for i in split:
        count += 1
        if count < 5:
            header_ficha.append(i)

    for i in range(len(header_ficha)):
        if header_ficha[i] == 'treino':
            header_ficha[i] = 'Treino'
        if header_ficha[i] == 'exercicio':
            header_ficha[i] = 'Exercício'
        if header_ficha[i] == 'series':
            header_ficha[i] = 'Séries'
        if header_ficha[i] == 'carga':
            header_ficha[i] = 'Carga'

    array_texto = "  |  ".join(split)
    array_textoheader = " | ".join(header_ficha)
    
    if os.path.exists(abs_file_path):
        webbrowser.open('file://' + abs_file_path)
        rect = Rectangle(Point(100, 150), Point(700, 500))
        rect.setFill("#C6E6CC")
        rect.setWidth(0) 
        rect.draw(win)
        # header = Text(Point(400, 220), array_textoheader)
        # header.setSize(20)
        # header.setTextColor("black")
        # header.draw(win)
        treino = Text(Point(400, 220), array_texto)
        treino.setSize(20)
        treino.setTextColor("black")
        treino.draw(win)
        
    else:
        treino = Text(Point(400, 200), "Ainda sem treinos disponíveis!")
        treino.setSize(20)
        treino.setStyle("bold")
        treino.setTextColor("black")
        treino.draw(win)
    


def criar_janela_treino(login):
    win = GraphWin("Gerenciador de treinos", 800, 600)
    win.setBackground("#F0FFFF")

    logo = Image(Point(400, 300), "public/FitVibes.png")
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

    trainer_view_text = Text(Point(625, 375), "Visualizar os títulos dos\nseus treinos base")
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

        # criador de treinos base
        if inside(clickPoint, trainer_createnew_button) and not is_user_selected:
            criador_treino("create_base")

        # visualizador de treinos base (sem html!)
        if inside(clickPoint, trainer_view_button) and not is_user_selected:
            file = open("public/treinos base/lista.csv", "r")
            cache = "".join(file)
            file.close()
            criar_janela_lista(f"{cache}", "nomes dos treinos", "black")

        # visualizador de treinos dos alunos (gera um html!)
        if inside(clickPoint, trainer_view_button) and is_user_selected:
            file = open(f"public/paginas/{search_bar.getText()}.html", "w")
            origin = open(f"public/treinos/{search_bar.getText()}.csv", "r")
            origin_cache = []
            origin_cache.append("<table border='1'>")
            for line in origin:
                origin_cache.append("<tr>")
                cells = line.strip().split(',')
                for cell in cells:
                    origin_cache.append(f"<th>{cell}</th>")
                origin_cache.append("</tr>")

            origin_cache.append("</table>")

            file.write(f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Treinos</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Treino do aluno {search_bar.getText()}</h1>
{''.join(origin_cache)}
</body>
</html>""")
            file.close()
            origin.close()

            # VISUALIZA TREINO ALUNO
                # diretório atual do script
            script_dir = os.path.dirname(__file__)

            rel_path = f'public/paginas/{search_bar.getText()}.html'
            abs_file_path = os.path.join(script_dir, rel_path)

            # Verifica se o arquivo existe
            if os.path.exists(abs_file_path):
                webbrowser.open('file://' + abs_file_path)
            else:
                print("Arquivo não encontrado.")

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

        if inside(clickPoint, trainer_createnew_button) and is_user_selected:
            edit = GraphWin("Associar treino base", 500, 400)
            edit.setBackground("#F0FFFF")

            text = Text(Point(100, 60), f"Treino base do aluno {search_bar.getText()}") 
            text.setSize(12)
            text.draw(edit)

            file = open("public/treinos base/lista.csv", "r")
            cache = []
            for line in file:
                cache.append(line.strip())
            file.close()

            buttons = []
            for i, treino in enumerate(cache):
                button2 = Rectangle(Point(300, 120 + i * 40), Point(400, 150 + i * 40))
                button2.setFill("#C1E1C1")
                button2.draw(edit)  
                text = Text(Point(350, 135 + i * 40), treino)
                text.draw(edit)  
                buttons.append((button2, treino))

            which = Entry(Point(100, 100), 20)
            which.draw(edit)
            button1 = Rectangle(Point(90, 120), Point(110, 140))
            button1.setFill("green")
            button1.draw(edit)

            while not edit.isClosed():

                click = edit.getMouse()

                for button2, treino_text in buttons:
                    if inside(click, button2):
                        which.setText(treino_text)
                    
                print(which.getText())
                if inside(click, button1):
                    file = open("public/treinos base/lista.csv", "r")
                    check = which.getText()+"\n"
                    for line in file:
                        if check == line:
                            file.close()
                            file = open(f"public/treinos/{search_bar.getText()}.csv", "w")
                            fileswitch = open(f"public/treinos base/{which.getText()}.csv", "r")
                            file.write("".join(fileswitch))
                            file.close()
                            fileswitch.close()
                            edit.close()
                            criar_janela_mensagem("Sucesso!", "Sucesso", "green")
                            break
                    file.close()
                    edit.close()

        # modifica o treino de um aluno!
        if is_user_selected:
            if inside(clickPoint, trainer_mod_button) and is_user_selected:
                criador_treino(f"{search_bar.getText()}")

        # as opções retornarão ao normal ao deselecionar o usuário.
        if not is_user_selected and clickonce:
            trainer_createnew_text.setText("Criar um novo treino base")
            trainer_view_text.setText("Visualizar os títulos dos\nseus treinos base")
            trainer_mod_text.undraw()
            trainer_mod_button.undraw()
            trainer_lorem.draw(win)
            clickonce = False

    win.close()

#função responsável por listar o treino!
def listador_treino(treino=["treino,exercicio,series,carga,grupo muscular\n"], win=False):
    treinos = []
    for i in range(len(treino)):
        buttony = Rectangle(Point(288, 100 + i * 20), Point(298, 110 + i * 20))
        buttony.setFill("#F0FFFF")
        buttony.draw(win)
        selecter = i

        text = Text(Point(460, 105 + i * 20), treino[i].replace("\n",""))
        text.draw(win)

        treinos.append((buttony, selecter, text))
    return treinos

# função responsável por criar treinos!
def criador_treino(option):
    win = GraphWin("Criador de Treinos", 640, 480)
    win.setBackground("#F0FFFF")

    logo = Image(Point(320, 240), "public/FitVibes.png")
    logo.draw(win)

    if option == "create_base":
        titulo = Text(Point(320, 48), "Criador de treino base")
    else:
        titulo = Text(Point(320, 48), "Modificador de treino")
    titulo.setSize(15)
    titulo.setStyle("bold italic")
    titulo.draw(win)

    create_exercise_box = Rectangle(Point(40, 96), Point(240, 184))
    create_exercise_box.setFill("#C1E1C1")
    create_exercise_box.draw(win)
    create_exercise_text = Text(Point(140, 140), "Criar exercício")
    create_exercise_text.draw(win)

    edit_exercise_box = Rectangle(Point(40, 208), Point(240, 296))
    edit_exercise_box.setFill("#C1E1C1")
    edit_exercise_box.draw(win)
    edit_exercise_text = Text(Point(140, 252), "Editar exercício")
    edit_exercise_text.draw(win)

    delete_exercise_box = Rectangle(Point(40, 320), Point(240, 408))
    delete_exercise_box.setFill("#C1E1C1")
    delete_exercise_box.draw(win)
    delete_exercise_text = Text(Point(140, 364), "Deletar exercício")
    delete_exercise_text.draw(win)

    exercise_list_box = Rectangle(Point(284, 96), Point(636, 408))
    exercise_list_box.setFill("#C1E1C1")
    exercise_list_box.draw(win)

    if option == "create_base":
        treino_base = ["treino,exercicio,series,carga,grupo muscular\n"]
    else:
        file = open(f"public/treinos/{option}.csv")
        treino_base = []
        for line in file:
            treino_base += [line]
        file.close()

    treinos = []
    for i in range(len(treino_base)):
        buttony = Rectangle(Point(288, 100 + i * 20), Point(298, 110 + i * 20))
        buttony.setFill("#F0FFFF")
        buttony.draw(win)

        selecter = i

        text = Text(Point(460, 105 + i * 20), treino_base[i].replace("\n",""))
        text.draw(win)

        treinos.append((buttony, selecter, text))

    save_base_training = Rectangle(Point(284, 408), Point(636, 438))
    save_base_training.setFill("green")
    save_base_training.draw(win)

    save_base_ttext = Text(Point(460, 423), "Salvar")
    save_base_ttext.draw(win)
    line_select = 0

    while not win.isClosed():

        clickPoint = win.getMouse()

        if inside(clickPoint, create_exercise_box):
            treino_base += [criador_exercicio()]
            line_select = 0
            for buttony, selecter, text in treinos:
                buttony.undraw()
                text.undraw()
            treinos = listador_treino(treino_base, win)

        if inside(clickPoint, edit_exercise_box):
            line_edit = line_select
            if line_edit >= 1 and line_edit <= len(treino_base)-1:
                lineit = treino_base[line_edit].replace("\n",",")
                lineit = lineit.split(",")
                lineit = list(filter(None, lineit))
                treino_base[line_edit] = criador_exercicio(lineit[0],lineit[1],lineit[2],lineit[3],lineit[4])
            else:
                criar_janela_mensagem("Número de linha inválido.", "Erro", "red")

            line_select = 0
            for buttony, selecter, text in treinos:
                buttony.undraw()
                text.undraw()
            treinos = listador_treino(treino_base, win)
            
        if inside(clickPoint, delete_exercise_box):
            line_edit = line_select
            if line_edit >= 1 and line_edit <= len(treino_base)-1:
                del treino_base[line_edit]
            else:
                criar_janela_mensagem("Número de linha inválido.", "Erro", "red")
                
            line_select = 0
            for buttony, selecter, text in treinos:
                buttony.undraw()
                text.undraw()
            treinos = listador_treino(treino_base, win)

        for buttony, selecter, text in treinos:
            if inside(clickPoint, buttony):
                if selecter == 0:
                    criar_janela_mensagem("Você não pode\n selecionar a\n primeira linha!", "Erro", "red")
                else:
                    if line_select == selecter:
                        buttony.setFill("#F0FFFF")
                        line_select = 0
                        print(line_select)
                    elif line_select == 0:
                        buttony.setFill("black")
                        line_select = selecter
                        print(line_select)
                    elif line_select != 0 and line_select != selecter:
                        criar_janela_mensagem("Você só pode\n selecionar uma\n linha por vez!", "Erro", "red")
                        print(line_select)

            
        if inside(clickPoint, save_base_training) and option == "create_base":
            edit = GraphWin("", 250, 125)
            edit.setBackground("#F0FFFF")

            text = Text(Point(100, 20), "Qual o nome do treino?")
            text.draw(edit)
            which = Entry(Point(100, 50), 20)
            which.setFill("#C1E1C1")
            which.draw(edit)
            confirm = Rectangle(Point(90, 70), Point(110, 90))
            confirm.setFill("green")
            confirm.draw(edit)

            while not edit.isClosed():

                clickPoint = edit.getMouse()

                if inside(clickPoint, confirm):
                    name_training = which.getText()
                    file = open(f"public/treinos base/{name_training}.csv", "w")
                    file.write(''.join(treino_base))
                    file.close()
                    file = open("public/treinos base/lista.csv", "a", newline="")
                    file.write(f"{name_training}\n")
                    file.close()
                    edit.close()
                    win.close()

        if inside(clickPoint, save_base_training) and option != "create_base":
            file = open(f"public/treinos/{option}.csv", "w")
            file.write(''.join(treino_base))
            file.close()
            win.close()

# função responsável por criar e editar exercícios!
def criador_exercicio(treino="",exercicio="",series="",carga="",gm=""):
    win = GraphWin("", 600, 800)
    win.setBackground("#F0FFFF")

    exercise_list = ["Supino", "Agachamento", "Legpress", "Abdominal", "Bíceps rosca"] # adicionar mais

    exercises = {
    "Supino": "Peito",
    "Agachamento": "Perna",
    "Agachamento sumô": "Perna",
    "Abdominal": "Abdomen",
    "Bíceps rosca": "Braço"
    } # dicionário associando os grupos musculares respectivos

    buttons = []

    for i, exercise in enumerate(exercise_list):
        button = Rectangle(Point(300, 120 + i * 40), Point(400, 150 + i * 40))
        button.setFill("#C1E1C1")
        button.draw(win)

        text = Text(Point(350, 135 + i * 40), exercise)
        text.draw(win)

        buttons.append((button, exercise))

    new_training_text = Text(Point(150, 20), "Treino")
    new_training_text.draw(win)
    new_training_entry = Entry(Point(150, 50), 30)
    new_training_entry.setFill("#C1E1C1")
    new_training_entry.draw(win)
    new_training_entry.setText(treino)

    new_exercise_text = Text(Point(150, 140), "Exercicio")
    new_exercise_text.draw(win)
    new_exercise_entry = Entry(Point(150, 170), 30)
    new_exercise_entry.setFill("#C1E1C1")
    new_exercise_entry.draw(win)
    new_exercise_entry.setText(exercicio)

    new_series_text = Text(Point(150, 260), "Séries")
    new_series_text.draw(win)
    new_series_entry = Entry(Point(150, 290), 30)
    new_series_entry.setFill("#C1E1C1")
    new_series_entry.draw(win)
    new_series_entry.setText(series)

    new_load_text = Text(Point(150, 380), "Carga")
    new_load_text.draw(win)
    new_load_entry = Entry(Point(150, 410), 30)
    new_load_entry.setFill("#C1E1C1")
    new_load_entry.draw(win)
    new_load_entry.setText(carga)

    new_group_text = Text(Point(150, 500), "Grupo muscular")
    new_group_text.draw(win)
    new_group_entry = Entry(Point(150, 530), 30)
    new_group_entry.setFill("#C1E1C1")
    new_group_entry.draw(win)
    new_group_entry.setText(gm)

    confirm_new_entry = Rectangle(Point(135, 560), Point(165, 590))
    confirm_new_entry.setFill("green")
    confirm_new_entry.draw(win)

    while not win.isClosed():

        clickPoint = win.getMouse()

        if inside(clickPoint, confirm_new_entry):
            win.close()
            return str(new_training_entry.getText() + "," + new_exercise_entry.getText() + "," + new_series_entry.getText() + "," + new_load_entry.getText() + "," + new_group_entry.getText() + "\n")
        
        for button, exercise in buttons:
            if inside(clickPoint, button):
                new_exercise_entry.setText(exercise)
                if exercise in exercises:
                    new_group_entry.setText(exercises[exercise])

def main():
    criar_arquivo_csv()
    win, login_entry, senha_entry, checkbox_aluno, checkbox_treinador, cadastrar_button, logar_button = criar_janela()
    aluno_check = False
    treinador_check = False
    linhas_selecionadas = []

    while True:
        click = win.checkMouse()
        if click is not None:
            login = login_entry.getText()
            senha = senha_entry.getText()

            if inside(click, checkbox_aluno):
                if aluno_check:
                    apagar_x(linhas_selecionadas)
                    aluno_check = False
                else:
                    if treinador_check:
                        criar_janela_mensagem("Você só pode escolher uma opção.", "Erro", "red")
                    else:
                        aluno_check = True
                        treinador_check = False
                        linhas_selecionadas = desenhar_x(checkbox_aluno.getCenter(), win)
                        if treinador_check:
                            apagar_x(linhas_selecionadas)
                            treinador_check = False
            elif inside(click, checkbox_treinador):
                if treinador_check:
                    apagar_x(linhas_selecionadas)
                    treinador_check = False
                else:
                    if aluno_check:
                        criar_janela_mensagem("Você só pode escolher uma opção.", "Erro", "red")
                    else:
                        treinador_check = True
                        aluno_check = False
                        linhas_selecionadas = desenhar_x(checkbox_treinador.getCenter(), win)
                        if aluno_check:
                            apagar_x(linhas_selecionadas)
                            aluno_check = False

            if inside(click, cadastrar_button):
                if login and senha and (aluno_check or treinador_check):
                    tipo = "aluno" if aluno_check else "treinador"
                    if tipo == "treinador" or tipo == "aluno":
                        if not verificar_login(login, senha, tipo):
                            adicionar_usuario(login, senha, tipo)
                            criar_janela_mensagem("Cadastro realizado com sucesso!", "Sucesso", "green")
                        else:
                            criar_janela_mensagem("Esse usuário já existe.", "Erro", "red")
            elif inside(click, logar_button):
                if login and senha and (aluno_check or treinador_check):
                    tipo = "aluno" if aluno_check else "treinador"
                    if verificar_login(login, senha, tipo):
                        criar_janela_mensagem(f"Login realizado com sucesso!\nBem-vindo, {login}", "Sucesso", "green")
                        if tipo == "treinador":
                            win.close()
                            criar_janela_treino(login)
                        elif tipo == "aluno":
                            criar_janela_aluno(login)
                    else:
                        criar_janela_mensagem("Faça um cadastro primeiro.", "Erro", "red")

        if win.isClosed():
            break


if __name__ == "__main__":
    main()