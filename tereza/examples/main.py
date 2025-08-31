import customtkinter as ctk

# Inicialização do CustomTkinter
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Janela principal
root = ctk.CTk()
root.geometry("500x300")
root.title("Menu simulado (CTk)")

# Frame superior que simula a barra de menu
menu_frame = ctk.CTkFrame(root, height=30)
menu_frame.pack(fill="x", side="top")

# Botões de menu simulados
def novo():
    print("Novo clicado")

def sobre():
    print("Sobre clicado")

btn_arquivo = ctk.CTkButton(menu_frame, text="Arquivo", width=80, height=24, command=novo)
btn_arquivo.pack(side="left", padx=5, pady=3)

btn_ajuda = ctk.CTkButton(menu_frame, text="Ajuda", width=80, height=24, command=sobre)
btn_ajuda.pack(side="left", padx=5, pady=3)

# Resto da interface
main_label = ctk.CTkLabel(root, text="Conteúdo principal aqui", font=("Arial", 16))
main_label.pack(pady=50)

root.mainloop()
