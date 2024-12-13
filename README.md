### English 

# PyAutoRecord

PyAutoRecord is an automation tool developed in Python to register products on a fictional website automatically. The website used is for educational and demonstration purposes, allowing you to view all the products registered during the execution of the script.

The tool uses the PyAutoGUI library to simulate keyboard and mouse actions, filling in the form fields with data extracted from a CSV file. Additionally, the Pandas library is used for data manipulation and reading the contents of the file.

To run PyAutoRecord, you need to have Python 3.8 or higher installed, along with the PyAutoGUI and Pandas libraries. The code has been tested on the Windows operating system, using the Google Chrome browser. If you're using another operating system or browser, you may need to adjust wait times or command simulations to ensure proper functionality.

The produtos.csv file should contain the product information to be registered on the website, following the appropriate format with columns like code, brand, type, category, unit price, cost, and notes. Make sure the file is saved in the same directory as the script.

During execution, the script logs into the fictional website, accesses the registration page, reads the data from the CSV, and automatically fills in the corresponding fields. At the end, you can view all the products theoretically registered on the site.

It is important to note that this project was created for educational purposes. It demonstrates the use of task automation in Python but should be used responsibly, ensuring that the website or application you're automating allows this type of interaction.

If you wish to adapt the code or customize its settings, feel free to explore and modify the parameters. You are welcome to contribute or share your feedback!

---

### Português

# PyAuto Record

PyAuto Record é uma ferramenta de automação desenvolvida em Python para realizar o cadastro de produtos em um site fictício de forma automatizada. O site utilizado é apenas para fins educacionais e demonstração, permitindo visualizar ao final todos os produtos cadastrados durante a execução do script.

A ferramenta utiliza a biblioteca PyAutoGUI para simular ações de teclado e mouse, preenchendo os campos do formulário com os dados extraídos de um arquivo CSV. Além disso, a biblioteca Pandas é empregada para manipulação e leitura dos dados contidos no arquivo.

Para executar o PyAuto Record, é necessário ter instalado o Python 3.8 ou superior e as bibliotecas PyAutoGUI e Pandas. O código foi testado no sistema operacional Windows, utilizando o navegador Google Chrome. Caso você utilize outro sistema operacional ou navegador, podem ser necessários ajustes nos tempos de espera ou na simulação de comandos para garantir o funcionamento correto.

O arquivo produtos.csv deve conter as informações dos produtos a serem cadastrados no site, seguindo o formato adequado, com colunas como código, marca, tipo, categoria, preço unitário, custo e observações. Certifique-se de que o arquivo está salvo no mesmo diretório do script.

Durante a execução, o script realiza login no site fictício, acessa a página de cadastro, lê os dados do CSV e os insere automaticamente nos campos correspondentes. Ao final, é possível visualizar no site todos os produtos teoricamente cadastrados.

Vale ressaltar que este projeto foi criado com propósitos educacionais. Ele demonstra o uso de automação de tarefas em Python, mas deve ser utilizado com responsabilidade, garantindo que o site ou aplicação que você automatizar permita esse tipo de interação.

Se você deseja adaptar o código ou personalizar suas configurações, fique à vontade para explorar e modificar os parâmetros. Sinta-se convidado a contribuir ou compartilhar seu feedback!
