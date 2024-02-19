import requests

def solicitar_csv():
    #faz uma requisição ao site e traz o arquivo para minha máquina
    url = 'https://aai-devportal-media.s3.us-west-2.amazonaws.com/challenges/shopping-list.csv'
    r = requests.get(url, allow_redirects=True)
    nome = 'shopping-list.csv'
    with open(nome, 'wb') as arquivo:
        arquivo.write(r.content)
    return nome
