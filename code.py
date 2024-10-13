import pyautogui #imports the pyautogui library
import time #imports the time library

pyautogui.PAUSE = 0.5 #sets a 0.5 delay between each command line

pyautogui.press("win") #presses the win key
pyautogui.write("chrome") #writes 'chrome' with keyboard imputs
pyautogui.press("enter")

time.sleep(1.5) #waits for 1.5 seconds, only in this command line
pyautogui.hotkey("ctrl", "t") #presses a combination of keys, forming a hotkey

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" #creates the variable 'link' and assigns a string to it
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(1.5) 

email = "email@email.com"
senha = "PyTh0N"

pyautogui.click(x=1024, y=406) #Presses the left mouse button at the desired position (this position is obtained through the auxiliary.py file) 
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.click(x=1275, y=558)

time.sleep(1.5)

import pandas

tabela = pandas.read_csv("produtos.csv") #creates the variable 'tabela' and assigns the csv file to it

print(tabela) #prints the csv table in the terminal 

for linha in tabela.index: #Starts a for loop that repeats the commands for each row in the CSV table
    pyautogui.click(x=1177, y=286)

    pyautogui.write(tabela.loc[linha, "codigo"]) #Finds the cell in the current row of the loop within the 'codigo' column and writes its content in the selected field
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"])) #str transforms a numeric variable into a string
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    if not pandas.isna(tabela.loc[linha, "obs"]): #If the selected cell is not null, it writes the value in the selected field. If it is null, it presses the Tab key.
        pyautogui.write(tabela.loc[linha, "obs"])
    pyautogui.press("tab")

    pyautogui.click(x=1203, y=943)
    pyautogui.scroll(+10000) #scrolls to the top of the webpage
