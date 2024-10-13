import pyautogui #imports the pyautogui library
import time #imports the time library

pyautogui.PAUSE = 0.5 #sets a 0.5 delay between each command line

pyautogui.press("win") #presses the win key
pyautogui.write("chrome") #writes 'chrome' with keyboard imputs
pyautogui.press("enter")

time.sleep(1.5) #waits for 1.5 seconds, only in this command line
pyautogui.hotkey("ctrl", "t") #presses a combination of keys, forming a hotkey

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" #define um texto a variavel link
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(1.5) 

# Passo 2: Fazer login
email = "email@email.com"
senha = "PyTh0N"

pyautogui.click(x=1024, y=406) #pressiona o botão esquerdo do mouse na posição configurada
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.click(x=1275, y=558)

time.sleep(1.5)

# Passo 3: Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv") #atribui a variavel tabela o arquivo externo em csv

print(tabela) #printa no terminal a variavel tabela

# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o processo até acabar
for linha in tabela.index: #declara uma repetição para todas as linhas da tabela
    pyautogui.click(x=1177, y=286)

    pyautogui.write(tabela.loc[linha, "codigo"]) #localiza a linha atual do loop e a coluna "codigo" e escreve no campo selecionado
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"])) #transforma uma informação numerica em string
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    if not pandas.isna(tabela.loc[linha, "obs"]): #caso a coluna for nao for vazia, escreve ela no campo. Se for vazia apenas aperta tab
        pyautogui.write(tabela.loc[linha, "obs"])
    pyautogui.press("tab")

    pyautogui.click(x=1203, y=943)
    pyautogui.scroll(+10000) #volta para o inicio da pagina
