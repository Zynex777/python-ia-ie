# Importando a biblioteca e nomeando de tk
from functions import teste_botao
import tkinter as tk
import random as rdm
import string
ALTURA = "450"
LARGURA = "400"
back = "#3D0A50"
fundo = "#FFFFFF"
#- funcoes:

def gerar_senha():
    erro = "#ff0000"
    try:
        tamanho = int(entry_tamanho_senha.get())
        #verificando se a quantidade de caracteres é menor doque 4
        if tamanho < 4:
            lbl_resultado.config(
                text="Minimo de 4 caracteres",
                fg=erro
            )
            return
        caracteres = ""
        if var_maiuscula.get():
            caracteres += string.ascii_uppercase
        if var_minuscula.get():
            caracteres += string.ascii_lowercase
        if var_numeros.get():
            caracteres += string.digits
        if var_simbolos.get():
            caracteres += string.punctuation

        if not caracteres:
            lbl_resultado.config(
                text="Erro: Selecione ao menos uma opção!",
                fg=erro
            )
            return
        senha = "".join(rdm.choice(caracteres) for i in range(tamanho))
        lbl_resultado.config(
            text=f"Senha: {senha}",
            fg="#00FF00"
        )
        print("conjunto de caracteres disponiveis para criação da senha")
        print(caracteres)
        return
    except ValueError:
        lbl_resultado.config(
            text="Erro: digite um numero valido!",
            fg=erro
        )


#==================================================#
# 1. Configuração da janela principal
#==================================================#
janela = tk.Tk()
janela.title("Gerador De Senhas em python")
janela.config(bg=back)
janela.geometry(f"{LARGURA}x{ALTURA}")


#==================================================#
#2.Titulo da Janela principal
#==================================================#
titulo = tk.Label(
    text="Gerador De Senhas",
    font=("vivaldi",22,"bold"),
    bg=back,
    fg=fundo
)
titulo.pack(pady=25)

#==================================================#
#3. Label tamanho senha
#==================================================#
lbl_tamanho_senha = tk.Label(
    text="Tamanho Da senha",
    font=("felix titling",12),
    bg=back,
    fg=fundo
)
lbl_tamanho_senha.pack(pady=12)

#==================================================#
# 4. Entrada do tamanho da senha
#==================================================#

entry_tamanho_senha = tk.Entry(
    janela,
    font=("Comic Sans MS", 12),
    width=10,
    justify="center",
    bg=back,
    fg=fundo
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
    bg=back,
    fg=fundo,
    selectcolor=back,
    activebackground=back,
    activeforeground=fundo
)
chk_maiuscula.pack(anchor="w",padx=60, pady=2)

chk_minuscula = tk.Checkbutton(
    janela,
    text="Minuscula (a-z)",
    variable=var_minuscula,
    bg=back,
    fg=fundo,
    selectcolor=back,
    activebackground=back,
    activeforeground=fundo
)
chk_minuscula.pack(anchor="w",padx=60, pady=2)

chk_numero = tk.Checkbutton(
    janela,
    text="Numeros (0-9)",
    variable=var_numeros,
    bg=back,
    fg=fundo,
    selectcolor=back,
    activebackground=back,
    activeforeground=fundo
)
chk_numero.pack(anchor="w",padx=60, pady=2)

chk_simbolos = tk.Checkbutton(
    janela,
    text="Simbolos (@-#-$-%-&-*)",
    variable=var_simbolos,
    bg=back,
    fg=fundo,
    selectcolor=back,
    activebackground=back,
    activeforeground=fundo
)
chk_simbolos.pack(anchor="w",padx=60, pady=2)

#==================================================#
# 7. Criar botao gerador de senha
#==================================================#

btn_gerar = tk.Button(
    janela,
    text="Gerar Senha Segura",
    command=gerar_senha,
    bg=back,
    fg=fundo,
    padx=10,
    pady=5
)
btn_gerar.pack()


#==================================================#
# 8. label que apresenta o resultado no programa
#==================================================#

lbl_resultado = tk.Label(
    janela,
    text="Senha Gerada",
    font=("Arial",11,"bold"),
    bg=back,
    fg=fundo
)
lbl_resultado.pack()
#==================================================#
# 9. Execução da janela
#==================================================#
# Mantém a janela aberta e escutando eventos
janela.mainloop()

