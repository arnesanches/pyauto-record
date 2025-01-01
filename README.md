### Project Demonstration / Demonstração do Projeto

![Project Demonstration / Demonstração do Projeto](https://github.com/arnesanches/pyauto-record/blob/main/Anima%C3%A7%C3%A3o.gif?raw=true)

#### English 

# PyAuto Record

PyAuto Record is a Python automation tool that showcases the power of the PyAutoGUI library for automating repetitive tasks, such as product registration. Using a fictional website for educational and demonstrative purposes, the script performs automatic product registration, allowing users to see the final result and understand how automation can save time and effort.

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

1. **Python 3.8 or higher**: You can download the latest version at [https://www.python.org/downloads/](https://www.python.org/downloads/).
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

To interrupt the automation, move the mouse cursor to the top left corner of the screen and wait for about five seconds.

## Important Notes

- **Educational Purpose**: This project was created to demonstrate how to automate tasks with Python. It is not recommended for use on real websites without permission.
- **Adaptation**: You can adapt the code and customize parameters such as wait times and field coordinates if necessary.

## Contributions

Contributions are welcome! Feel free to open issues or pull requests in this repository.

## License

This project is licensed under the MIT License.

---

#### Português

# PyAuto Record

O PyAuto Record é uma ferramenta de automação em Python que demonstra o poder da biblioteca PyAutoGUI para automatizar tarefas repetitivas, como o cadastro de produtos. Utilizando um site fictício para fins educacionais e demonstrativos, o script realiza o cadastro automático de produtos, permitindo visualizar o resultado final e entender como a automação pode economizar tempo e esforço.

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

1. **Python 3.8 ou superior**: Você pode baixar a versão mais recente em [https://www.python.org/downloads/](https://www.python.org/downloads/).
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

Para interromper a automação, posicione o cursor do mouse no canto superior esquerdo da tela e aguarde cerca de cinco segundos.

## Observações Importantes

- **Objetivo Educacional**: Este projeto foi criado para demonstrar como automatizar tarefas com Python. Não é recomendado para uso em sites reais sem permissão.
- **Adaptação**: Você pode adaptar o código e personalizar parâmetros como os tempos de espera e as coordenadas dos campos, caso necessário.
  
## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests neste repositório.

## Licença

Este projeto está licenciado sob a MIT License.
