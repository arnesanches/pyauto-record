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

# Iterando por cada linha da tabela para realizar o cadastro dos produtos
for linha in tabela.index:
    pyautogui.press("tab")  # Navega até o campo do código do produto
    codigo = str(tabela.loc[linha, "codigo"])  # Obtém o valor da coluna "codigo"
    pyautogui.write(codigo)  # Digita o código do produto

    pyautogui.press("tab")  # Navega até o campo da marca
    marca = str(tabela.loc[linha, "marca"])  # Obtém o valor da coluna "marca"
    pyautogui.write(marca)  # Digita a marca do produto

    pyautogui.press("tab")  # Navega até o campo do tipo
    tipo = str(tabela.loc[linha, "tipo"])  # Obtém o valor da coluna "tipo"
    pyautogui.write(tipo)  # Digita o tipo do produto

    pyautogui.press("tab")  # Navega até o campo da categoria
    categoria = str(tabela.loc[linha, "categoria"])  # Obtém o valor da coluna "categoria"
    pyautogui.write(categoria)  # Digita a categoria do produto

    pyautogui.press("tab")  # Navega até o campo do preço unitário
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])  # Obtém o valor da coluna "preco_unitario"
    pyautogui.write(preco_unitario)  # Digita o preço unitário

    pyautogui.press("tab")  # Navega até o campo do custo
    custo = str(tabela.loc[linha, "custo"])  # Obtém o valor da coluna "custo"
    pyautogui.write(custo)  # Digita o custo do produto

    pyautogui.press("tab")  # Navega até o campo de observações
    obs = str(tabela.loc[linha, "obs"])  # Obtém o valor da coluna "obs"
    if obs != "nan":  # Se houver observação (valor não for NaN), digita o texto
        pyautogui.write(obs)

    pyautogui.press("tab")  # Navega até o botão de enviar
    pyautogui.press("enter")  # Envia o cadastro

    pyautogui.hotkey("ctrl", "r")  # Reinicia a página
    pyautogui.press("tab")  # Navega para o início do formulário
    time.sleep(2.5)  # Aguarda o carregamento
