#Importação De Bibliotecas Necessárias
import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage
#Fim De Importações


# Criando a Janela
janela = tk.Tk() 
janela.title("My Aplicativo De Tarefas")
janela.configure(bg = "black")
janela.geometry("500x600")

#Função adicionar tarefas
frame_em_edicao = None
def adicionar_tarefas():
    global frame_em_edicao

    tarefa = entrada_tarefa.get().strip()
    if tarefa and tarefa != "Escreva sua Tarefa aqui":
        if frame_em_edicao is not None:
            atualizar_tarefa(tarefa)
            frame_em_edicao = None
        else:
            adicionar_item_tarefa(tarefa)
            entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada Invalida!", "Por favor Insira uma tarefa")

def adicionar_item_tarefa(tarefa):
    frame_tarefa = tk.Frame(canvas_interior, bg = "white", bd = 1, relief = tk.SOLID)

    label_tarefa = tk.Label(frame_tarefa, text = tarefa, font = ("Garamond", 16), bg = "white", width = 25, height = 2)
    label_tarefa.pack(side = tk.LEFT, fill = tk.X, padx = 10, pady = 5)

    botao_editar = tk.Button(frame_tarefa, image = icon_editar, command = lambda f= frame_tarefa, l = label_tarefa: preparar_edicao(f, l), bg = "white", relief = tk.FLAT)
    botao_editar.pack(side = tk.RIGHT, padx = 5)
    
    botao_deleta = tk.Button(frame_tarefa, image = icon_deleta, command = lambda f= frame_tarefa: deleta_tarefa(f), bg = "white", relief = tk.FLAT)
    botao_deleta.pack(side = tk.RIGHT, padx = 5)

    frame_tarefa.pack(fill = tk.X, padx = 5, pady = 5)

    checkbutton = ttk.Checkbutton(frame_tarefa, command = lambda Label = label_tarefa: alterar_sublinhado(Label))
    checkbutton.pack(side = tk.RIGHT, padx = 5)

    canvas_interior.update_idletasks()
    canvas.config(scrollregion = canvas.bbox("all"))

icon_editar = PhotoImage(file = "adiciona.png").subsample(3, 3)
icon_deleta = PhotoImage(file = "delete.png").subsample(3, 3)

def preparar_edicao(frame_tarefa, label_tarefa):
    global frame_em_edicao
    frame_em_edicao = frame_tarefa
    entrada_tarefa.delete(0, tk.END)
    entrada_tarefa.insert(0, label_tarefa.cget("text"))

def atualizar_tarefa(nova_tarefa):
    global frame_em_edicao
    for widget in frame_em_edicao.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(text = nova_tarefa)

def deleta_tarefa(frame_tarefa):
    frame_tarefa.destroy()
    canvas_interior.update_idletasks()
    canvas.config(scrollregion = canvas.bbox("all"))

def alterar_sublinhado(label):
    fonte_atual = label.cget("font")
    if "overstrike" in fonte_atual:
        nova_fonte = fonte_atual.replace("overstrike", "")
#Fonte
fonte_topo = font.Font(family = "Garamond", size = 24, weight = "bold")
rotulo_topo = tk.Label(janela, text = "Gestão De Tarefas", font = fonte_topo, bg = "white", fg = "black").pack(pady = 20)

#Campo para entrada
frame = tk.Frame(janela, bg = "#F0F0F0")
frame.pack(pady=10)
entrada_tarefa = tk.Entry(frame, font = ("Garamond", 14), relief = tk.FLAT, bg = "white", fg = "grey", width = 30)
entrada_tarefa.pack(side = tk.LEFT, padx = 10)
botao_adicionar = tk.Button(frame, command = adicionar_tarefas, text = "Adicionar Tarefa", bg = "#4CAF50", fg = "white", height = 1, width = 15, font = ("Roboto", 11))
botao_adicionar.pack(side = tk.LEFT, padx = 10)

#Criar Freme com lista e rolagem
frame_lista_tarefas = tk.Frame(janela, bg = "white")
frame_lista_tarefas.pack(fill = tk.BOTH, expand= "true", padx = 10, pady = 10)

canvas = tk.Canvas(frame_lista_tarefas, bg = "white")
canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand = "true")

rolagem = ttk.Scrollbar(frame_lista_tarefas, orient = "vertical", command = canvas.yview)
rolagem.pack(side = tk.RIGHT, fill = tk.Y)

canvas.configure(yscrollcommand = rolagem.set)
canvas_interior = tk.Frame(canvas, bg = "white")
canvas.create_window((0, 0), window = canvas_interior, anchor = "nw")
def ajustar_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas_interior.bind("<Configure>", ajustar_scrollregion)
# Aqui em cima você pode adicionar o restante da sua interface gráfica, como widgets, etc.
janela.mainloop()
