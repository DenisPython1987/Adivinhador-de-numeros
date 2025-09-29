"""Jogo de advinhar números. O Python gera um número aleatório entre 1 e 100, e 
você tem que advinhar.
Autor: Denisander Vivan. Data: 29/09/2025"""
#Código com pequenas correções do cht GPT
import tkinter as tk
from tkinter import ttk
from random import randint

#Aqui eu crio a janela raiz
root = tk.Tk()

#Aqui eu determino o tamanho da janela
root.geometry('400x400+300+300')

#Aqui eu proíbo o redimensionamento
root.resizable(False, False)

#Aqui eu crio uma função para validação numérica
def validar(num):

    #Aqui eu crio um bloco try/except para checar se a entrada é um número inteiro
    try:
        int(num)

    except ValueError:

        #Aqui coloco no mostrador a mensagem de erro
        most_var.set('Digite um número válido')
        return False
    return True

#Aqui eu crio uma variável de controle para armazenar o número aleatório
numero = tk.IntVar(value=randint(1, 100))

#Aqui eu crio uma função para gerar um novo número
def gerar_novo():

    #Aqui eu atribuo à variavel de controle um novo número
    numero.set(randint(1, 100))

    #Aqui eu coloco no mostrador a mensagem de status do novo número
    most_var.set("Novo número gerado! Tente advinhar!")

#Aqui eu crio uma função para calcular a vitória no jogo
def calcular(num):

    #Aqui eu pego o número da variável de controle
    alvo = numero.get()

    #Aqui eu chamo a função validar para tratar as entradas
    if validar(num):

        #Aqui eu crio uma declaração if para validar a vitória
        if int(num) == alvo:

            #Aqui eu coloco no mostrador a mensagem de vitória
            most_var.set(f"Acertou, o número é {alvo}")

        #Aqui eu crio uma declaração if para ver se o número é menor que o número aleatório
        elif int(num) < alvo:

            #Aqui eu coloco no mostrador a mensagem correspondente
            most_var.set('É maior que isso!')

        #Aqui eu crio uma declaração if para ver se o número é maior que o número aleatório
        elif int(num) > alvo:

            #Aqui eu coloco no mostrador a mensagem correspondente
            most_var.set('É menor que isso!')

#Aqui eu crio um painel para armazenar o mostrador
painel = ttk.LabelFrame(root, text="Resultado")

#Aqui eu coloco o painel na janela raiz
painel.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

#Aqui eu crio a variável de controle para o mostrador
most_var = tk.StringVar()

#Aqui eu crio o rótulo para o mostrador
mostrador = ttk.Label(painel, textvariable=most_var, foreground='lime', 
                      background='black')

#Aqui eu coloco o mostrador dentro do painel
mostrador.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

#Aqui eu crio a variável de controle para a entrada
num_var = tk.StringVar()

#Aqui eu crio a entrada para o programa
entrada = ttk.Entry(root, textvariable=num_var)

#Aqui eu coloco a entrada na janela raiz
entrada.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)

#Aqui eu crio o botão de tentativa de acertar chamando a função calcular
botão = ttk.Button(root, text='Tentar', command=lambda: calcular(num_var.get()))

#Aqui eu coloco o botão na janela raiz
botão.grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)

#Aqui eu crio o botão para gerar um novo número aleatório
bot_gerar_novo = ttk.Button(root, text='Gerar novo número', command=lambda: 
                            gerar_novo())

#Aqui eu coloco o botão na janela raiz
bot_gerar_novo.grid(row=3, column=0, sticky=tk.E, padx=5, pady=5)

#Aqui eu coloco o programa para rodar
root.mainloop()