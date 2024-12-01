# Importando as bibliotecas necessárias
import pyautogui  # Automação de ações no teclado e mouse
import time  # Controle de tempo/pausas entre as ações

# Configuração de uma pausa padrão entre os comandos do PyAutoGUI
pyautogui.PAUSE = 0.5  # 0.5 segundos de intervalo entre os comandos

# Abrindo o navegador Chrome
pyautogui.press("win")  # Pressiona a tecla Windows para abrir o menu iniciar
pyautogui.write("chrome")  # Digita "chrome" no menu iniciar
pyautogui.press("enter")  # Pressiona "Enter" para abrir o navegador

# Aguardando o navegador abrir completamente
time.sleep(3)  # Pausa de 3 segundos para garantir que o navegador esteja pronto

# Acessando a URL de login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")  # Digita o link de login
pyautogui.press("enter")  # Pressiona "Enter" para acessar a URL
