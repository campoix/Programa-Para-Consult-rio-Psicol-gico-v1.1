import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("900x100")
app.title("Barra de Menus")

# ========================
# Barra de MENUS (texto)
# ========================
menu_bar = ctk.CTkFrame(app, height=30, fg_color="#d9d9d9", corner_radius=0)
menu_bar.pack(fill="x", side="top")

menus = ["CADASTROS", "TABELA DE CONSULTAS", "BOLETIM DE ATENDIMENTO",
        "RELATÓRIOS", "FERRAMENTAS", "AJUDA"]

def on_click(name):
    print(f"Clicou em: {name}")

for nome in menus:
    btn = ctk.CTkButton(
        menu_bar,
        text=nome,
        width=160,
        height=28,
        fg_color="transparent",   # fundo transparente
        hover_color="#c0c0c0",    # cinza mais escuro no hover
        corner_radius=0,
        font=("Arial", 12, "bold"),
        command=lambda n=nome: on_click(n)
    )
    btn.pack(side="left", padx=1, pady=1)

app.mainloop()
