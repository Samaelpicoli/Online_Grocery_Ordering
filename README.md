# Online Grocery Ordering

# Sobre o projeto

Atividade realizada com base no exercício 'Online Grocery Ordering' proposto no site: https://community.automationanywhere.com/developer-challenges-85011/challenge-pages-85136.

Online Grocery Ordering é uma aplicação web para treinamento de RPA, onde deve ser feito download de um arquivo CSV e realizar a leitura e o preenchimento de dados no formulário do site.

Ao final do preenchimento surge um modal que mostra o tempo que o robô levou para preencher e a acurácia, o mesmo tira um print e salva na pasta do projeto.

## Layout da web
Rede 1


# Tecnologias Utilizadas

Python

## Bibliotecas Utilizadas

Pandas

Selenium

Requests

## Sobre o código

O projeto foi dividido em módulos, onde um arquivo faz as interações com o site, e outro arquivo faz a requisição e faz download do CSV, 
os 2 arquivos são chamados dentro do arquivo main que os executa.

No main, o projeto foi desenvolvido como uma máquina de estados (INITIALIZATION, GET TRANSACTION, PROCESS, END), emulando o ReFramework do UiPath,
auxiliando a criar automações mais confiáveis, flexíveis e fáceis de manter ao longo do tempo.

# Como executar o projeto
Pré-requisitos: Python 3.10

```bash
#insalar dependências, dentro do seu projeto e com ambiente virtual ativo:
pip install -r requirements.txt
```

# Executar o projeto
python main.py

# Autor
Samael Muniz Picoli
