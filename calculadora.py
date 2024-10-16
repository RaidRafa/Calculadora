# Importando TKINTER
from idlelib.colorizer import color_config
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Label
from unittest.mock import right

# Criando frames

# Cores
cor1 = "#2d332f" # Cor display
cor2 = "#3f4742" # Cor background
cor3 = "#de9a35" # Cor botões dos operadores
cor4 = "#6e6963" # Cor teclado
cor5 = "#feffff" # Cor branca

# Criando janela

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x347")
janela.config(background="#2d332f")

# Dividindo a janela

frame_tela = Frame(janela, width=235, height=50, bg="#3f4742")
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=300, bg=cor2)
frame_corpo.grid(row=1, column=0)

# Variavel todos os valores

todos_valores= ""

# Criando função

def entrar_valores(event):

    global todos_valores
    todos_valores= todos_valores + str(event)


    # Passando o valor para label
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado= eval(todos_valores)

    valor_texto.set(str(resultado))

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

def creator():
    criador = "RaidRafa.github"
    valor_texto.set(criador)





# Criando label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, padding=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 19'), background=cor1)
app_label.place(x=0, y=0)

# Botões

b_1 = Button(frame_corpo, command=limpar_tela,text="C", width=11, height=2, relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, command= lambda: entrar_valores("%"), text="%", width=10, height=2,  relief=RAISED, overrelief=RIDGE)
b_2.place(x=88, y=0)

# Botões operadores

b_3 = Button(frame_corpo,command= lambda: entrar_valores("/"), text="/", width=8, height=2, bg="#de9a35", relief=RAISED, overrelief=RIDGE)
b_3.place(x=170, y=0)

b_4 = Button(frame_corpo, command= lambda: entrar_valores("*"), text="*", width=8, height=3, bg="#de9a35", relief=RAISED, overrelief=RIDGE)
b_4.place(x=170, y=42)

b_5 = Button(frame_corpo, command= lambda: entrar_valores("-"), text="-", width=8, height=3, bg="#de9a35", relief=RAISED, overrelief=RIDGE)
b_5.place(x=170, y=99)

b_6 = Button(frame_corpo, command= lambda: entrar_valores("+"), text="+", width=8, height=3, bg="#de9a35", relief=RAISED, overrelief=RIDGE)
b_6.place(x=170, y=156)

b_7 = Button(frame_corpo, command=calcular,text="=", width=8, height=3, bg="#de9a35", relief=RAISED, overrelief=RIDGE)
b_7.place(x=170, y=213)

# Botões do teclado

b_8 = Button(frame_corpo, command= lambda: entrar_valores("7"), text="7", width=7, height=4, bg="#6e6963", relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=42)

b_9 = Button(frame_corpo, command= lambda: entrar_valores("8"), text="8", width=7, height=4, bg="#6e6963", relief=RAISED, overrelief=RIDGE)
b_9.place(x=55, y=42)

b_10 = Button(frame_corpo, command= lambda: entrar_valores("9"), text="9", width=7, height=4, bg="#6e6963", relief=RAISED, overrelief=RIDGE)
b_10.place(x=110, y=42)

b_11 = Button(frame_corpo, command= lambda: entrar_valores("4"), text="4", width=7, height=4, bg="#6e6963", relief=RAISED, overrelief=RIDGE)
b_11.place(x=0, y=113)

b_12 = Button(frame_corpo, command= lambda: entrar_valores("5"), text="5", width=7, height=4, bg="#6e6963", relief=RAISED, overrelief=RIDGE)
b_12.place(x=55, y=113)

b_13 = Button(frame_corpo, command= lambda: entrar_valores("6"), text="6", width=7, height=4, bg="#6e6963", relief=RAISED, overrelief=RIDGE)
b_13.place(x=110, y=113)

b_14 = Button(frame_corpo, command= lambda: entrar_valores("1"), text="1", width=7, height=4, bg="#6e6963", relief=RAISED, overrelief=RIDGE)
b_14.place(x=0, y=184)

b_15 = Button(frame_corpo, command= lambda: entrar_valores("2"), text="2", width=7, height=4, bg="#6e6963", relief=RAISED, overrelief=RIDGE)
b_15.place(x=55, y=184)

b_16 = Button(frame_corpo, command= lambda: entrar_valores("3"), text="3", width=7, height=4, bg="#6e6963", relief=RAISED, overrelief=RIDGE)
b_16.place(x=110, y=184)

b_17 = Button(frame_corpo, command= lambda: entrar_valores("."), text=".", width=7, height=2, bg="#6e6963", relief=RAISED, overrelief=RIDGE)
b_17.place(x=0, y=255)

b_18 = Button(frame_corpo, command= lambda: entrar_valores("0"), text="0", width=7, height=2, bg="#6e6963", relief=RAISED, overrelief=RIDGE)
b_18.place(x=55, y=255)

b_19 = Button(frame_corpo, command= lambda: entrar_valores(","), text=",", width=7, height=2, bg="#6e6963", relief=RAISED, overrelief=RIDGE)
b_19.place(x=110, y=255)

b_20 = Button(frame_corpo, command=creator,text="CREATOR", width=8, height=1, bg="#072ef2", relief=RAISED, overrelief=RIDGE)
b_20.place(x=170, y=270)






janela.mainloop()