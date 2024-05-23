# Online Grocery Ordering

# Sobre o projeto

Atividade realizada com base no exercício 'Online Grocery Ordering' proposto no site: https://community.automationanywhere.com/developer-challenges-85011/challenge-pages-85136.

Online Grocery Ordering é uma aplicação web para treinamento de RPA, onde deve ser feito download de um arquivo CSV e realizar a leitura e o preenchimento de dados no formulário do site.

Ao final do preenchimento surge um modal que mostra o tempo que o robô levou para preencher e a acurácia, o mesmo faz um screenshot da tela e salva na pasta do projeto.

## Layout da web
![Web 1](https://github.com/Samaelpicoli/Online_Grocery_Ordering/blob/main/assets/web1.PNG)

![Web 2](https://github.com/Samaelpicoli/Online_Grocery_Ordering/blob/main/assets/acuracia.png)


# Tecnologias Utilizadas

Python

## Bibliotecas Utilizadas

Pandas

Selenium

Requests

Webdriver-Manager

Os

## Sobre o código

O projeto foi desenvolvido utilizando o paradigma Orientado a Objetos, onde o arquivo grocery_ordering.py contém todas as funcionalidades do projeto como a requisição do arquivo csv via requests e
a interação com o site da atividade, a classe é instanciada dentro do arquivo main que os executa.

No main, o projeto foi desenvolvido como uma máquina de estados (INITIALIZATION, GET TRANSACTION, PROCESS, END), emulando o ReFramework do UiPath,
auxiliando a criar automações mais confiáveis, flexíveis e fáceis de manter ao longo do tempo.

# Como executar o projeto
Pré-requisitos: Python 3.11+

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
