import customtkinter as ctk

def tela_add_usuario():   
    ctk.set_appearance_mode("dark")      # ou "light", "system"
    ctk.set_default_color_theme("blue")  # ou "green", "dark-blue", etc.

    tela_adicionar = ctk.CTk()  # Cria a janela
    tela_adicionar.geometry("1000x500")
    tela_adicionar.title("Consultoria Online - Adicionar Novo Usuário")

    tela_adicionar.mainloop()