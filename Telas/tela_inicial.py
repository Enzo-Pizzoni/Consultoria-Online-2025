import customtkinter as ctk
import tela_add_usuario as adi

def adicionar_usuario():
    tela_inicial.destroy()
    adi.tela_add_usuario()

def visualizar_casos():
    pass

ctk.set_appearance_mode("dark")      # ou "light", "system"
ctk.set_default_color_theme("blue")  # ou "green", "dark-blue", etc.

tela_inicial = ctk.CTk()  # Cria a janela principal
tela_inicial.geometry("1000x500")
tela_inicial.title("Consultoria Online")
label_de_bem_vindo = ctk.CTkLabel(tela_inicial, text= "Bem Vindo Astélio!", font=("Arial", 24))
label_de_bem_vindo.pack()
botao_adicionar_novo_usuario = ctk.CTkButton(tela_inicial, text= "Adicionar novo caso",
                                             height=60, width=200, font=("Arial", 24),
                                             command= adicionar_usuario)
botao_adicionar_novo_usuario.pack(pady= 100)
botao_visualizar_casos = ctk.CTkButton(tela_inicial, text= "Visualizar casos",
                                             height=60, width=200, font=("Arial", 24),
                                             command= visualizar_casos)
botao_visualizar_casos.pack(pady= 10)
tela_inicial.mainloop()