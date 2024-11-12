
from tkinter import filedialog as f
from tkinter import *
import os

def selecionar_pasta():
    global pasta_caminho
    pasta_caminho = f.askdirectory()
    if pasta_caminho:
        texto_selecao.config(text='Pasta selecionada!', fg='green')

def organizador():
    lista_arquivos = os.listdir(pasta_caminho)

    for arquivo in lista_arquivos:
        if '.docx' in arquivo:
            pasta = os.path.join(pasta_caminho, 'word')
            if not os.path.exists(pasta):
                os.makedirs(pasta)
            os.rename(os.path.join(pasta_caminho, arquivo), os.path.join(pasta, arquivo))
        if '.xlsx' in arquivo:
            pasta = os.path.join(pasta_caminho, 'excel')
            if not os.path.exists(pasta):
                os.makedirs(pasta)
            os.rename(os.path.join(pasta_caminho, arquivo), os.path.join(pasta, arquivo))
        if '.jpg' in arquivo or '.png' in arquivo or '.jpeg' in arquivo:
            pasta = os.path.join(pasta_caminho, 'fotos')
            if not os.path.exists(pasta):
                os.makedirs(pasta)
            os.rename(os.path.join(pasta_caminho, arquivo), os.path.join(pasta, arquivo))
        if '.pdf' in arquivo:
            pasta = os.path.join(pasta_caminho, 'pdf')
            if not os.path.exists(pasta):
                os.makedirs(pasta)
            os.rename(os.path.join(pasta_caminho, arquivo), os.path.join(pasta, arquivo))
        if '.zip' in arquivo:
            pasta = os.path.join(pasta_caminho, 'zip')
            if not os.path.exists(pasta):
                os.makedirs(pasta)
            os.rename(os.path.join(pasta_caminho, arquivo, os.path.join(pasta, arquivo)))

janela = Tk()
janela.title('Organizador de arquivos')
texto_principal = Label(janela, text='=-=-=-Organizador de arquivos-=-=-=', font=('Arial', 16))
texto_principal.grid(column=0, row=0, pady=10)
botao_caminho = Button(janela, text='Selecionar pasta', font=('Arial', 10), command=selecionar_pasta)
botao_caminho.grid(column=0, row=1, pady=10)

texto_selecao = Label(janela, text='Clique para selecionar a pasta a ser organizada', font=('Arial', 10))
texto_selecao.grid(column=0, row=2, pady=10)

botao_organizar = Button(janela, text='Organizar arquivos', font=('Arial', 10), command=organizador)
botao_organizar.grid(column=0, row=3, pady=10)


janela.mainloop()

