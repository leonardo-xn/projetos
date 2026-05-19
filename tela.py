from tkinter import *
from tkinter import messagebox
import banco

# JANELA
#
janela = Tk()
janela.title("Sistema de Login")
janela.geometry("350x300")
janela.resizable(False, False)
janela.configure(bg="#1e1e1e")

# FUNÇÕES

def cadastrar():

    usuario = entry_usuario.get().strip()
    senha = entry_senha.get().strip()

    if usuario == "" or senha == "":
        messagebox.showwarning("Erro", "Preencha todos os campos")
        return

    if banco.cadastrar(usuario, senha):

        messagebox.showinfo("Sucesso", "Usuário cadastrado!")

        entry_usuario.delete(0, END)
        entry_senha.delete(0, END)

    else:
        messagebox.showerror("Erro", "Usuário já existe")


def entrar():

    usuario = entry_usuario.get().strip()
    senha = entry_senha.get().strip()

    if banco.login(usuario, senha):

        messagebox.showinfo("Login", f"Bem-vindo {usuario}!")

        abrir_painel(usuario)

    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos")


def abrir_painel(usuario):

    painel = Toplevel()

    painel.title("Painel do Usuário")
    painel.geometry("400x250")
    painel.configure(bg="#2b2b2b")

    Label(
        painel,
        text=f"Olá, {usuario}",
        font=("Arial", 18, "bold"),
        bg="#2b2b2b",
        fg="white"
    ).pack(pady=20)

    Label(
        painel,
        text="Login realizado com sucesso!",
        font=("Arial", 12),
        bg="#2b2b2b",
        fg="white"
    ).pack(pady=10)

    Button(
        painel,
        text="Sair",
        width=15,
        bg="red",
        fg="white",
        command=painel.destroy
    ).pack(pady=20)


# TÍTULO
Label(
    janela,
    text="SISTEMA LOGIN",
    font=("Arial", 20, "bold"),
    bg="#1e1e1e",
    fg="white"
).pack(pady=20)


# USUÁRIO
Label(
    janela,
    text="Usuário",
    bg="#1e1e1e",
    fg="white"
).pack()

entry_usuario = Entry(
    janela,
    width=30
)

entry_usuario.pack(pady=5)

# SENHA
Label(
    janela,
    text="Senha",
    bg="#1e1e1e",
    fg="white"
).pack()

entry_senha = Entry(
    janela,
    width=30,
    show="*"
)

entry_senha.pack(pady=5)

# BOTÕES
Button(
    janela,
    text="Entrar",
    width=20,
    bg="#4CAF50",
    fg="white",
    command=entrar
).pack(pady=10)

Button(
    janela,
    text="Cadastrar",
    width=20,
    bg="#2196F3",
    fg="white",
    command=cadastrar
).pack()

# LOOP
janela.mainloop()