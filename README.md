#### English 

# PyAuto Record

PyAuto Record is an automation tool developed in Python to register products on a fictional website in an automated way. The website used is for educational and demonstration purposes only, allowing you to view all the products registered during the execution of the script.

## Features

- **Automated Product Registration**: Automatically registers products on a fictional website.
- **Simulated Keyboard and Mouse Actions**: Uses the PyAutoGUI library to fill out forms.
- **Data Reading with Pandas**: Product data is extracted from a CSV file and automatically entered into the website.
- **Data Visibility**: At the end of the execution, all the registered products can be viewed on the fictional website.

## Technologies Used

- **Python**: The programming language used for the development of the tool.
- **PyAutoGUI**: Library for simulating keyboard and mouse actions on the computer.
- **Pandas**: Library for manipulating and reading data in CSV format.
- **CSV**: The file format used to store product data.

## Execution Requirements

1. **Python 3.8 or higher**: Ensure you are using the appropriate version of Python.
2. **Libraries**: Install the required libraries with the following command:
   
   `pip install pyautogui pandas`

3. **Operating System**: The code has been tested on Windows. If you're using another operating system or browser, adjustments may be necessary.

4. **CSV File**: The produtos.csv file contains the necessary information about the products to be registered. Ensure it is located in the same directory as the Python script.

## How to Run

1. **Setup**: 
   - Make sure the produtos.csv file is in the script's folder.
   
2. **Run the Script**: 
   - Execute the Python script (`pyauto_record.py`) in your local environment.
   
3. **Monitor**:
   - The script logs into the fictional website and automatically fills in the form fields with the data from the CSV.

4. **Results**:
   - At the end of the execution, all the registered products can be viewed on the fictional website.

## Important Notes

- **Educational Purpose**: This project was created to demonstrate how to automate tasks with Python. It is not recommended for use on real websites without permission.
- **Responsibility in Usage**: Make sure that the website or application you're automating allows such interaction.
- **Adaptation**: You can adapt the code and customize parameters such as wait times and field coordinates if necessary.

## Contribute or Share Feedback

Feel free to explore, modify, and contribute to the code. If you find any bugs or have suggestions, share your feedback to improve the project.

---

#### Português

# PyAuto Record

PyAuto Record é uma ferramenta de automação desenvolvida em Python para realizar o cadastro de produtos em um site fictício de forma automatizada. O site utilizado é apenas para fins educacionais e demonstração, permitindo visualizar ao final todos os produtos cadastrados durante a execução do script.

## Funcionalidades

- **Automação de Cadastro de Produtos**: Registra produtos automaticamente em um site fictício.
- **Simulação de Ações de Teclado e Mouse**: Utiliza a biblioteca PyAutoGUI para preencher formulários.
- **Leitura de Dados com Pandas**: Os dados dos produtos são extraídos de um arquivo CSV e inseridos automaticamente no site.
- **Visibilidade dos Dados**: Ao final da execução, todos os produtos cadastrados podem ser visualizados no site fictício.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento da ferramenta.
- **PyAutoGUI**: Biblioteca para simular ações de teclado e mouse no computador.
- **Pandas**: Biblioteca para manipulação e leitura de dados em formato CSV.
- **CSV**: Formato de arquivo utilizado para armazenar os dados dos produtos.

## Requisitos para Execução

1. **Python 3.8 ou superior**: Certifique-se de que está utilizando a versão adequada do Python.
2. **Bibliotecas**: Instale as bibliotecas necessárias utilizando o seguinte comando:
   
   `pip install pyautogui pandas`

3. **Sistema Operacional**: O código foi testado no Windows. Caso utilize outro sistema operacional ou navegador, ajustes podem ser necessários.

4. **Arquivo CSV**: O arquivo `produtos.csv` contém as informações dos produtos a serem cadastrados. Certifique-se de que ele esteja localizado no mesmo diretório que o script Python.

## Como Executar

1. **Configuração**: 
   - Verifique se o arquivo `produtos.csv` está na pasta do script.
   
2. **Execução do Script**: 
   - Execute o script Python (`pyauto_record.py`) em seu ambiente local.
   
3. **Acompanhamento**:
   - O script realiza login no site fictício e preenche automaticamente os campos do formulário com as informações do CSV.

4. **Resultados**:
   - Ao final da execução, todos os produtos cadastrados podem ser visualizados no site fictício.

## Observações Importantes

- **Objetivo Educacional**: Este projeto foi criado para demonstrar como automatizar tarefas com Python. Não é recomendado para uso em sites reais sem permissão.
- **Responsabilidade no Uso**: Garanta que o site ou aplicação que você está automatizando permita esse tipo de interação.
- **Adaptação**: Você pode adaptar o código e personalizar parâmetros como os tempos de espera e as coordenadas dos campos, caso necessário.
  
## Contribua ou Compartilhe Feedback

Sinta-se à vontade para explorar, modificar e contribuir para o código. Se encontrar algum erro ou tiver sugestões, compartilhe seu feedback para melhorar o projeto.
