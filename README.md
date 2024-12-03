PyAuto Record

PyAuto Record é uma ferramenta de automação desenvolvida em Python para realizar o cadastro de produtos em um site fictício de forma automatizada. O site utilizado é apenas para fins educacionais e demonstração, permitindo visualizar ao final todos os produtos cadastrados durante a execução do script.

A ferramenta utiliza a biblioteca PyAutoGUI para simular ações de teclado e mouse, preenchendo os campos do formulário com os dados extraídos de um arquivo CSV. Além disso, a biblioteca Pandas é empregada para manipulação e leitura dos dados contidos no arquivo.

Para executar o PyAuto Record, é necessário ter instalado o Python 3.8 ou superior e as bibliotecas PyAutoGUI e Pandas. O código foi testado no sistema operacional Windows, utilizando o navegador Google Chrome. Caso você utilize outro sistema operacional ou navegador, podem ser necessários ajustes nos tempos de espera ou na simulação de comandos para garantir o funcionamento correto.

O arquivo produtos.csv deve conter as informações dos produtos a serem cadastrados no site, seguindo o formato adequado, com colunas como código, marca, tipo, categoria, preço unitário, custo e observações. Certifique-se de que o arquivo está salvo no mesmo diretório do script.

Durante a execução, o script realiza login no site fictício, acessa a página de cadastro, lê os dados do CSV e os insere automaticamente nos campos correspondentes. Ao final, é possível visualizar no site todos os produtos teoricamente cadastrados.

Vale ressaltar que este projeto foi criado com propósitos educacionais. Ele demonstra o uso de automação de tarefas em Python, mas deve ser utilizado com responsabilidade, garantindo que o site ou aplicação que você automatizar permita esse tipo de interação.

Se você deseja adaptar o código ou personalizar suas configurações, fique à vontade para explorar e modificar os parâmetros. Sinta-se convidado a contribuir ou compartilhar seu feedback!
