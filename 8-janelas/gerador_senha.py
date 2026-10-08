# Importando a biblioteca e nomeando de tk
import tkinter as tk
ALTURA = "450"
LARGURA = "400"

def acao_clique():
    print("o botao foi clicado")
#==================================================#
# 1. Configuração da janela principal
#==================================================#
janela = tk.Tk()
janela.title("Gerador De Senhas em python")
janela.config(bg="#3D0A50")
janela.geometry(f"{LARGURA}x{ALTURA}")


#==================================================#
#2.Titulo da Janela principal
#==================================================#
titulo = tk.Label(
    text="Gerador De Senhas",
    font=("vivaldi",22,"bold"),
    bg="#3D0A50",
    fg="#FFFFFF"
)
titulo.pack(pady=25)

#==================================================#
#3. Label tamanho senha
#==================================================#
lbl_tamanho_senha = tk.Label(
    text="Tamanho Da senha",
    font=("felix titling",12),
    bg="#3D0A50",
    fg="#FFFFFF"
)
lbl_tamanho_senha.pack(pady=12)

#==================================================#
# 4. Entrada do tamanho da senha
#==================================================#

entry_tamanho_senha = tk.Entry(
    janela,
    font=("Comic Sans MS", 12),
    width=10,
    justify="center"
)
entry_tamanho_senha.pack(pady=5)

#==================================================#
# 5. criando as variaveis de controle true or false
#==================================================#
var_maiuscula = tk.BooleanVar(value=False)
var_minuscula = tk.BooleanVar(value=False)
var_numeros = tk.BooleanVar(value=False)
var_simbolos = tk.BooleanVar(value=False)

#==================================================#
# 6. criando as caixinhas de seleção
#==================================================#

chk_maiuscula = tk.Checkbutton(
    janela,
    text="Maiuscula (A-Z)",
    variable=var_maiuscula,
    bg="#3D0A50",
    fg="#ffffff",
    selectcolor="#3D0A50",
    activebackground="#3D0A50",
    activeforeground="#ffffff"
)
chk_maiuscula.pack(anchor="w",padx=60, pady=2)

chk_minuscula = tk.Checkbutton(
    janela,
    text="Minuscula (a-z)",
    variable=var_minuscula,
    bg="#3D0A50",
    fg="#ffffff",
    selectcolor="#3D0A50",
    activebackground="#3D0A50",
    activeforeground="#ffffff"
)
chk_minuscula.pack(anchor="w",padx=60, pady=2)

chk_numero = tk.Checkbutton(
    janela,
    text="Numeros (0-9)",
    variable=var_numeros,
    bg="#3D0A50",
    fg="#ffffff",
    selectcolor="#3D0A50",
    activebackground="#3D0A50",
    activeforeground="#ffffff"
)
chk_numero.pack(anchor="w",padx=60, pady=2)

chk_simbolos = tk.Checkbutton(
    janela,
    text="Simbolos (@-#-$-%-&-*)",
    variable=var_simbolos,
    bg="#3D0A50",
    fg="#ffffff",
    selectcolor="#3D0A50",
    activebackground="#3D0A50",
    activeforeground="#ffffff"
)
chk_simbolos.pack(anchor="w",padx=60, pady=2)

#==================================================#
# 7. Execução da janela
#==================================================#
# Mantém a janela aberta e escutando eventos
janela.mainloop()