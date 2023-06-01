# Importar o móduo pyodbc para conexão com banco de dados
import pyodbc

# Importa o móduo tkinter para construção de interfaces gráficas
from tkinter import *

# Importa a classe ttk do módulo tkinter
from tkinter import ttk

# Função que verifica usuario e senha


def verifica_credenciais():
    print("Testando a função do botão")
    conexao = pyodbc.connect(
        "DRIVER={SQLite3 ODBC Driver};SERVER=localhost;DATABASE=./database/projeto_compras.db;Trusted_connection=yes")

    print("Se chegou até aqui é porque está conectado!")
    # cursor - Executar os comandos SQL
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND senha = ?",
                   (ent_nome_usuario.get(), ent_senha.get()))


# Criando a janela principal para tela de login

login_window = Tk()
login_window.title("Tela de Login")

login_window.configure(bg="#F5F5F5")


def fechar_janela():
    login_window.destroy()
    print("Fechando a janela")


"""fg - foreground (cor da letra)
row - linha
column - coluna
columnspan - quantas colunas vai ocupar no grid
pady - espaço"""

titulo_lbl = Label(login_window, text="Tela de Login",
                   font="Arial 20", fg="blue", bg="#F5F5F5")
titulo_lbl.grid(row=0, column=0, columnspan=2, pady=20)

# Label e campo nome de usuário
lbl_nome_usuario = Label(login_window, text="Nome de Usuário",
                         font="FiraCode 14 bold", bg="#F5F5F5")
lbl_nome_usuario.grid(row=1, column=0)

ent_nome_usuario = Entry(login_window, font="Arial 14")
ent_nome_usuario.grid(row=2, column=0, padx=30, sticky="NSEW")


# Label e Campo senha
lbl_senha = Label(login_window, text="Senha",
                  font="Arial 14 bold", bg="#F5F5F5")
lbl_senha.grid(row=3, column=0)

ent_senha = Entry(login_window, font="Arial 14")
ent_senha.grid(row=4, column=0, padx=30)

# Botões Entrar e Sair
btn_entrar = Button(login_window, text="Entrar",
                    font="Arial 14", command=verifica_credenciais)
btn_entrar.grid(row=5, columnspan=2, pady=20, padx=30)

btn_sair = Button(login_window, text="Sair",
                  font="Arial 14", command=fechar_janela)
btn_sair.grid(row=6, columnspan=1, pady=20)

# Inicia a janela Tkinter
login_window.mainloop()
