import sqlite3
import customtkinter as ctk
from PIL import Image

# ========================
# Criação do banco de dados
# ========================
def criar_banco():
    conexao = sqlite3.connect("tereza/customtkinter/usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    """)
    # Usuário padrão
    cursor.execute("SELECT * FROM usuarios WHERE nome = ?", ("Tereza C",))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", ("Tereza C", "admin"))
    conexao.commit()
    conexao.close()

# ========================
# Função de login
# ========================
def login1():
    usuario = cmb1.get()
    senha = etr1_var1.get()

    conexao = sqlite3.connect("tereza/customtkinter/usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND senha = ?", (usuario, senha))
    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        print("Login bem-sucedido!")
        loginwin.destroy()

        # ================
        # Função Cadastro
        # ================
        def cadastro1():
            win2 = ctk.CTk()
            win2.resizable(False, False)
            win2.geometry("1024x576")
            win2.title("Cadastro de Pacientes")
            win2.mainloop()

        # ======================
        # Janela Principal
        # ======================
        win1 = ctk.CTk()
        win1.configure(fg_color="#fdfdfd")
        win1.geometry("1200x720")
        win1.resizable(False, False)
        win1.title("Programa Para Consultório Psicológico v1.1")

        # Barra de menu personalizada
        menu_frame = ctk.CTkFrame(win1, height=40, fg_color="#eceff6")
        menu_frame.pack(fill="x")

        btn_font = ctk.CTkFont(weight="bold", size=16)

        btn_cadastro = ctk.CTkButton(
            menu_frame, text="CADASTROS", font=btn_font,
            hover_color="#f2f2f2", height=35, width=140,
            fg_color="#eceff6", text_color="#5c5e6a",
            corner_radius=0, command=cadastro1
        )
        btn_cadastro.pack(side="left")

        btn_relatorios = ctk.CTkButton(
            menu_frame, text="RELATÓRIOS", font=btn_font,
            hover_color="#f2f2f2", height=35, width=140,
            fg_color="#eceff6", text_color="#5c5e6a",
            corner_radius=0, command=lambda: print("Abrir relatórios")
        )
        btn_relatorios.pack(side="left")

        btn_config = ctk.CTkButton(
            menu_frame, text="CONFIGURAÇÕES", font=btn_font,
            hover_color="#f2f2f2", height=35, width=160,
            fg_color="#eceff6", text_color="#5c5e6a",
            corner_radius=0, command=lambda: print("Abrir configurações")
        )
        btn_config.pack(side="left")

        win1.mainloop()

    else:
        print("Usuário ou senha incorretos.")
        lbl4 = ctk.CTkLabel(
            loginwin, text="usuário ou senha inválidas",
            text_color="red", font=ctk.CTkFont(family="Segoe UI", size=13)
        )
        lbl4.place(x=165, y=138)

# ========================
# Inicialização do sistema
# ========================
criar_banco()
ctk.set_appearance_mode("light")

# ========================
# Janela de Login
# ========================
loginwin = ctk.CTk()
loginwin.title("Login do sistema")
loginwin.geometry("480x180")
loginwin.configure(fg_color="#f2f2f2")
loginwin.resizable(False, False)

frm1 = ctk.CTkFrame(loginwin, width=460, height=160, corner_radius=0,
                    border_color="#8b8b8b", fg_color="#f2f2f2", border_width=1)
frm1.place(x=10, y=10)

# Logo
image1 = ctk.CTkImage(Image.open("tereza/assets/Captura de Tela 2025-06-17 às 16.45.22.png"), size=(115, 110))
lbl1 = ctk.CTkLabel(loginwin, image=image1, text="")
lbl1.place(x=30, y=35)

# Usuário
lbl2 = ctk.CTkLabel(loginwin, text="Informe o Usuário", font=ctk.CTkFont(family="Segoe UI", size=13))
lbl2.place(x=180, y=30)

cmb1_variable1 = ctk.StringVar(value="Tereza C")
cmb1 = ctk.CTkComboBox(loginwin, values=["Tereza C"], variable=cmb1_variable1,
                       height=14, width=130, fg_color="#fdfdfd",
                       border_width=1, border_color="#bdbdbd",
                       corner_radius=2, hover=False)
cmb1.place(x=180, y=56)

# Senha
lbl3 = ctk.CTkLabel(loginwin, text="Informe a Senha", font=ctk.CTkFont(family="Segoe UI", size=13))
lbl3.place(x=180, y=85)

etr1_var1 = ctk.StringVar()
etr1 = ctk.CTkEntry(loginwin, show="*", textvariable=etr1_var1,
                    height=14, width=130, fg_color="#fdfdfd",
                    border_width=1, corner_radius=2, border_color="#bdbdbd")
etr1.place(x=180, y=111)

# Frame lateral
frm2 = ctk.CTkFrame(loginwin, width=134, height=110, corner_radius=0,
                    border_color="#8b8b8b", fg_color="#f2f2f2", border_width=1)
frm2.place(x=325, y=34)

# Botão Acessar
image2 = ctk.CTkImage(Image.open("tereza/assets/certo.png"), size=(30, 30))
btn1 = ctk.CTkButton(loginwin, image=image2, text="Acessar",
                     fg_color="#fafffe", border_color="#a0a0a0",
                     border_width=1, width=100, height=31,
                     text_color="black", cursor="hand1",
                     hover=False, corner_radius=2, compound="left",
                     command=login1)
btn1.place(x=340, y=45)

# Botão Sair
image3 = ctk.CTkImage(Image.open("tereza/assets/pngtree-glossy-blue-forward-arrow-icon-with-round-metallic-edge-ideal-for-png-image_14463628.png"), size=(30, 30))
btn2 = ctk.CTkButton(loginwin, text="Sair",
                     fg_color="#fafffe", border_color="#a0a0a0",
                     border_width=1, width=100, height=31,
                     text_color="black", cursor="hand1",
                     hover=False, corner_radius=2, compound="left",
                     command=lambda: exit())
btn2.place(x=340, y=100)

loginwin.mainloop()
