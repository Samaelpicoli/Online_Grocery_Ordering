# Online Grocery Ordering

# Sobre o projeto

Atividade realizada com base no exercício 'Online Grocery Ordering' proposto no site: https://community.automationanywhere.com/developer-challenges-85011/challenge-pages-85136.

Online Grocery Ordering é uma aplicação web para treinamento de RPA, onde deve ser feito download de um arquivo CSV e realizar a leitura e o preenchimento de dados no formulário do site.

Ao final do preenchimento surge um modal que mostra o tempo que o robô levou para preencher e a acurácia, o mesmo faz um screenshot da tela e salva na pasta do projeto.


# Tecnologias Utilizadas

Python

## Bibliotecas Utilizadas

Pandas

Selenium

Requests

Demais bibliotecas estão listadas no arquivo 'requirements.txt'

## Sobre o código

O projeto foi desenvolvido utilizando o paradigma Orientado a Objetos, destacando a implementação de padrões de projeto como Singleton e Page Object Model (POM). O arquivo main.py contém todas as funcionalidades do projeto, incluindo a requisição do arquivo CSV via Requests e a interação com o site da atividade, utilizando Selenium para automação de navegação.

### Estrutura do Projeto
No main, o projeto é estruturado como uma máquina de estados (INITIALIZATION, GET TRANSACTION, PROCESS, END), emulando o ReFramework do UiPath. Essa abordagem auxilia na criação de automações mais confiáveis, flexíveis e fáceis de manter ao longo do tempo.

### Padrões de Projeto
Singleton: O uso do padrão Singleton garante que apenas uma instância do WebDriver seja criada, centralizando o controle e a manipulação das interações com o navegador. Isso evita a sobrecarga de múltiplas instâncias e melhora a eficiência do sistema.
Page Object Model (POM): A implementação do POM facilita a separação das lógicas de interação com a interface do usuário, tornando o código mais modular e legível. Isso permite que as classes de página sejam reutilizadas e mantidas de forma independente da lógica de negócios.


### Facilidade de Manutenção e Preparo para Paralelismo
O design modular do projeto, aliado ao uso de padrões de projeto como POM e Singleton, proporciona uma facilidade significativa para manutenção e evolução do código. O sistema é preparado para suportar paralelismo, permitindo que múltiplas transações sejam processadas simultaneamente, aumentando a eficiência e a escalabilidade.

### Manipulação de Dados
O projeto realiza a leitura, escrita e manipulação de dados de forma eficiente. Utiliza-se o requests para realizar requisições HTTP e o pandas para manipulação de arquivos CSV. A lógica de captura e atualização de dados é clara e organizada, permitindo fácil acesso e modificação.


### Princípios SOLID
Os princípios SOLID estão presentes neste projeto, garantindo que o código seja bem estruturado e fácil de entender. Cada classe e método é responsável por uma única tarefa, promovendo a coesão e reduzindo o acoplamento entre os componentes do sistema. Isso não apenas melhora a legibilidade do código, mas também facilita a realização de testes e a implementação de novas funcionalidades.

# Como executar o projeto
Pré-requisitos: Python 3.10+

```bash
#insalar dependências, dentro do seu projeto e com ambiente virtual ativo:
pip install -r requirements.txt
```

# Executar o projeto
python main.py

## Observações:

Por ser uma automação web baseada no código fonte do site e utilizando Xpaths, Ids e Class, pode ser que em 
algum momento a automação pare de funcionar caso o site mude.

# Autor
Samael Muniz Picoli
