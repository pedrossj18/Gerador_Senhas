import customtkinter as s
import tkinter as tk
import random
import string

# Função para gerar a senha
def gerar_senha():
    tamanho = int(entry_tamanho.get())
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    caixa_visualizacao.delete("1.0", tk.END)  # Limpa o conteúdo atual da caixa de visualização
    caixa_visualizacao.insert(tk.END, senha)  # Insere a senha gerada na caixa de visualização

# Configuração da janela principal
app = s.CTk()
app.title("Gerador de Senhas")
app.geometry("400x250")
app.resizable(width=False, height=False)
app.iconbitmap("C:/Users/pedri/OneDrive/Documentos/One Drive/OneDrive/Área de Trabalho/Pedro_IndFlow/Senhas/imagem_2024-07-23_150047053.ico")

# Label e Entry para o tamanho da senha
label_tamanho = s.CTkLabel(app, text="Tamanho da senha:")
label_tamanho.pack(pady=10)

entry_tamanho = s.CTkEntry(app)
entry_tamanho.pack(pady=10)
entry_tamanho.insert(0, "12")  # Valor padrão

# Botão para gerar a se
button_gerar = s.CTkButton(app, text="Gerar Senha", command=gerar_senha)
button_gerar.pack()

label_senha = s.CTkLabel(app, text="Senha Gerada: ")
label_senha.pack(pady=10)

# Label para exibir a senha gerada
caixa_visualizacao = tk.Text(app, width=40, height=2)
caixa_visualizacao.place(x=90, y=210)

# Inicia o loop principal da interface gráfica
app.mainloop()
