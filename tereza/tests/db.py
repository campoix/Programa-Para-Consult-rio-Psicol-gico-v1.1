import customtkinter as ctk
import sqlite3
from tkinter import messagebox

# Configurações iniciais do customtkinter
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Conectar ou criar banco de dados
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Criar tabela se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
)
''')
conn.commit()


# Função de login
def fazer_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND senha=?", (usuario, senha))
    resultado = cursor.fetchone()

    if resultado:
        messagebox.showinfo("Login", f"Bem-vindo, {usuario}!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos.")


# Função de registro
def registrar_usuario():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if not usuario or not senha:
        messagebox.showwarning("Atenção", "Preencha todos os campos.")
        return

    try:
        cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha))
        conn.commit()
        messagebox.showinfo("Registro", "Usuário registrado com sucesso!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Usuário já existe.")


# Criar janela principal
janela = ctk.CTk()
janela.geometry("400x300")
janela.title("Login")

# Widgets
label_titulo = ctk.CTkLabel(janela, text="Login", font=ctk.CTkFont(size=20, weight="bold"))
label_titulo.pack(pady=10)

entry_usuario = ctk.CTkEntry(janela, placeholder_text="Usuário")
entry_usuario.pack(pady=10)

entry_senha = ctk.CTkEntry(janela, placeholder_text="Senha", show="*")
entry_senha.pack(pady=10)

btn_login = ctk.CTkButton(janela, text="Entrar", command=fazer_login)
btn_login.pack(pady=10)

btn_registrar = ctk.CTkButton(janela, text="Registrar", fg_color="gray", command=registrar_usuario)
btn_registrar.pack(pady=5)

janela.mainloop()
