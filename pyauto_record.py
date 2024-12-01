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

# Espera o site carregar
time.sleep(3)

# Preenchendo o formulário de login
pyautogui.press("tab")  # Navega para o campo de e-mail
pyautogui.write("arnejr@uol.com")  # Digita o e-mail

pyautogui.press("tab")  # Navega para o campo de senha
pyautogui.write("123456789")  # Digita a senha

pyautogui.press("tab")  # Navega para o botão de login
pyautogui.press("enter")  # Confirma o login

# Aguarda o site processar o login
time.sleep(3)

# Importando a biblioteca para manipular dados em tabelas
import pandas  # Utilizado para leitura de arquivos CSV e manipulação de tabelas

# Lendo o arquivo CSV com os dados dos produtos
tabela = pandas.read_csv("produtos.csv")  # Substitua pelo caminho correto do seu arquivo CSV

# Exibindo os dados da tabela no console (apenas para verificação)
print(tabela)
