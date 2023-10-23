from graphics import * 
from functions import *
import webbrowser
import os

# apenas funções principais

def criar_janela_aluno(login):
    win = GraphWin("Seus treinos", 800, 600)
    win.setBackground("#F0FFFF")

    welcome_text = Text(Point(400, 90), f"Treino do aluno {login}")
    welcome_text.setSize(24)
    welcome_text.setStyle("bold italic")
    welcome_text.setTextColor("black")
    welcome_text.draw(win)
    
    file = open(f"public/treinos/{login}.csv", "r")
    cache = "".join(file)
    file.close()
    
    # split = cache.strip().split(",")
    
    script_dir = os.path.dirname(__file__)

    rel_path = f'public/paginas/{login}.html'
    abs_file_path = os.path.join(script_dir, rel_path)
            # Verifica se o arquivo existe
    if os.path.exists(abs_file_path):
        webbrowser.open('file://' + abs_file_path)
        treino = Text(Point(400, 300), cache)
        treino.setSize(20)
        treino.setStyle("bold")
        treino.setTextColor("black")
        treino.draw(win)
    else:
        treino = Text(Point(400, 300), "Ainda sem treinos disponíveis!")
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

        # substitui o treino de um aluno por um treino base da escolha do treinador
        if inside(clickPoint, trainer_createnew_button) and is_user_selected:
            edit = GraphWin("")
            edit.setBackground("#F0FFFF")

            text = Text(Point(100, 60), f"Treino base do aluno {search_bar.getText()}") # aqui acho que precisa mostrar direto os treinos que tem

            file = open("public/treinos base/lista.csv", "r")
            cache = "".join(file)
            file.close()
            treinos =  Text(Point(70, 180), cache)  
            treinos.draw(edit)

            text.setSize(12)
            text.draw(edit)
            which = Entry(Point(100, 100), 20)
            which.draw(edit)
            button = Rectangle(Point(90, 120), Point(110, 140))
            button.setFill("green")
            button.draw(edit)


            while not edit.isClosed():

                click = edit.getMouse()

                if inside(click, button):
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
    exercise_list_text = Text(Point(460, 262), ''.join(treino_base))
    exercise_list_text.setSize(10)
    exercise_list_text.draw(win)
    save_base_training = Rectangle(Point(284, 408), Point(636, 438))
    save_base_training.setFill("green")
    save_base_training.draw(win)
    save_base_ttext = Text(Point(460, 423), "Salvar")
    save_base_ttext.draw(win)

    while not win.isClosed():

        clickPoint = win.getMouse()

        if inside(clickPoint, create_exercise_box):
            treino_base += [criador_exercicio()]
            exercise_list_text.setText(''.join(treino_base))

        if inside(clickPoint, edit_exercise_box):
            edit = GraphWin("", 200, 100)
            edit.setBackground("#F0FFFF")

            text = Text(Point(100, 20), "Editar qual linha?")
            text.draw(edit)
            which = Entry(Point(100, 50), 3)
            which.setFill("#C1E1C1")
            which.draw(edit)
            confirm = Rectangle(Point(90, 70), Point(110, 90))
            confirm.setFill("green")
            confirm.draw(edit)

            while not edit.isClosed():

                clickPoint = edit.getMouse()

                if inside(clickPoint, confirm):
                        
                    print(len(treino_base)-1)
                    line_edit = int(str(which.getText()))
                    if line_edit >= 1 and line_edit <= len(treino_base)-1:
                        edit.close()
                        treino_base[line_edit] = criador_exercicio()
                    else:
                        edit.close()
                        criar_janela_mensagem("Número de linha inválido.", "Erro", "red")

            exercise_list_text.setText(''.join(treino_base))
            
        if inside(clickPoint, delete_exercise_box):
            edit = GraphWin("", 200, 100)
            edit.setBackground("#F0FFFF")

            text = Text(Point(100, 20), "Apagar qual linha?\nDigite 0 para cancelar.")
            text.draw(edit)
            which = Entry(Point(100, 50), 3)
            which.setFill("#C1E1C1")
            which.draw(edit)
            confirm = Rectangle(Point(90, 70), Point(110, 90))
            confirm.setFill("green")
            confirm.draw(edit)

            while not edit.isClosed():

                clickPoint = edit.getMouse()

                if inside(clickPoint, confirm):
                        
                    print(len(treino_base)-1)
                    line_edit = int(str(which.getText()))
                    if line_edit >= 1 and line_edit <= len(treino_base)-1:
                        edit.close()
                        del treino_base[line_edit]
                    else:
                        edit.close()
                        criar_janela_mensagem("Número de linha inválido.", "Erro", "red")
                
            exercise_list_text.setText(''.join(treino_base))
            
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
def criador_exercicio():
    win = GraphWin("", 300, 600)
    win.setBackground("#F0FFFF")

    new_training_text = Text(Point(150, 20), "Treino")
    new_training_text.draw(win)
    new_training_entry = Entry(Point(150, 50), 30)
    new_training_entry.setFill("#C1E1C1")
    new_training_entry.draw(win)
    new_exercise_text = Text(Point(150, 140), "Exercicio")
    new_exercise_text.draw(win)
    new_exercise_entry = Entry(Point(150, 170), 30)
    new_exercise_entry.setFill("#C1E1C1")
    new_exercise_entry.draw(win)
    new_series_text = Text(Point(150, 260), "Series")
    new_series_text.draw(win)
    new_series_entry = Entry(Point(150, 290), 30)
    new_series_entry.setFill("#C1E1C1")
    new_series_entry.draw(win)
    new_load_text = Text(Point(150, 380), "Carga")
    new_load_text.draw(win)
    new_load_entry = Entry(Point(150, 410), 30)
    new_load_entry.setFill("#C1E1C1")
    new_load_entry.draw(win)
    new_group_text = Text(Point(150, 500), "Grupo Muscular")
    new_group_text.draw(win)
    new_group_entry = Entry(Point(150, 530), 30)
    new_group_entry.setFill("#C1E1C1")
    new_group_entry.draw(win)
    confirm_new_entry = Rectangle(Point(135, 560), Point(165, 590))
    confirm_new_entry.setFill("green")
    confirm_new_entry.draw(win)

    while not win.isClosed():

        clickPoint = win.getMouse()

        if inside(clickPoint, confirm_new_entry):
            win.close()
            return str(new_training_entry.getText() + "," + new_exercise_entry.getText() + "," + new_series_entry.getText() + "," + new_load_entry.getText() + "," + new_group_entry.getText() + "\n")

def main():
    criar_arquivo_csv()
    win, login_entry, senha_entry, tipo_entry = criar_janela()

    while True:
        click = win.checkMouse()
        if click is not None:
            login = login_entry.getText()
            senha = senha_entry.getText()
            tipo = tipo_entry

            if click.getX() >= 80 and click.getX() <= 180 and click.getY() >= 280 and click.getY() <= 310:
                if login and senha and tipo:
                    if tipo == "treinador" or tipo == "aluno":
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
                        if tipo == "treinador":
                            win.close()
                            criar_janela_treino(login) # se é treinador, abre janela de treino e fecha a anterior. se for aluno, tem que criar janela p visualização dos seus treinos
                        elif tipo == "aluno":
                            
                            criar_janela_aluno(login)
                    else:
                        criar_janela_mensagem("Faça um cadastro primeiro.", "Erro", "red")
        if win.isClosed():
            break


if __name__ == "__main__":
    main()