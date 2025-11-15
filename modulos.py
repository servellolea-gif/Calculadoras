#Crie um programa em Python com interface gráfica que receba dois números e realize a soma de ambos.

import tkinter as tk
from tkinter import messagebox

def somar_numeros():
    num1 = float(entry_num1.get()) #janela de digitação de dados
    num2 = float(entry_num2.get())
    resultado = num1 + num2
    messagebox.showinfo("Resultado", f"A soma dos números é: {resultado}")

#Criando a janela principal
janela = tk.Tk() #Janela de interface gráfica
janela.title("Calculadora de Soma")

#Criando os widgets
label_num1 = tk.Label(janela, text="Número 1:") #Rótulo para o primeiro número
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e") #Posicionamento do rótulo na janela gráfico. Linha 0, coluna 0, com espaçamento de 10 pixels na horizontal e 5 pixels na vertical, alinhado à direita.

entry_num1 = tk.Entry(janela) #Campo de entrada para o primeiro número. Ficará em frente do rótulo do número 1.
entry_num1.grid(row=0, column=1, padx=10, pady=5) #Posicionamento do campo de entrada na janela gráfica. Linha 0, coluna 1, com espaçamento de 10 pixels na horizontal e 5 pixels na vertical.

label_num2 = tk.Label(janela, text="Número 2:") #Rótulo para o segundo número
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e") #Posicionamento do rótulo na janela gráfico. Linha 1, coluna 0, com espaçamento de 10 pixels na horizontal e 5 pixels na vertical, alinhado à direita.

entry_num2 = tk.Entry(janela) #Campo de entrada para o segundo número. Ficará em frente do rótulo do número 2.
entry_num2.grid(row=1, column=1, padx=10, pady=5) #Posicionamento do campo de entrada na janela gráfica. Linha 1, coluna 1, com espaçamento de 10 pixels na horizontal e 5 pixels na vertical.

botao_somar = tk.Button(janela, text="Somar", command=somar_numeros) #Botão para realizar a soma dos números
botao_somar.grid(row=2, columnspan=2, padx=10, pady=5)  #Posicionamento do botão na janela gráfica. Linha 2, ocupando duas colunas, com espaçamento de 10 pixels na horizontal e 5 pixels na vertical.

# Rodando o loop principal
janela.mainloop()