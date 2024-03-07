import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.6


pyautogui.press("WIN")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)

pyautogui.click(x=480, y=112)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(1)

pyautogui.click(x=438, y=742)
pyautogui.write("rhaonyferraz@hotmail.com")
pyautogui.press('tab')
pyautogui.write("123456")
pyautogui.press("enter")

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# para cada linha da tabela
# clicar no primeiro campo
for linha in tabela.index:
 # clicar no primeiro campo.
    pyautogui.click(x=458, y=536)

    # codigo do produto
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')

    # marca
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')

    # tipo
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')

    # categoria
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    # preço
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    # custo
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    # obs
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press('tab')
    # enviar
    pyautogui.press('enter')
    pyautogui.scroll(3000)
