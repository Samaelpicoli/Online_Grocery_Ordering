import os

# Credenciais de login. Em um projeto real, EMAIL e SENHA devem
# estar em um cofre de senhas.
EMAIL = 'samaelpicoli8@gmail.com'
SENHA = 'Samael27'

# URL do site que será acessado durante a automação.
URL = 'https://pathfinder.automationanywhere.com/challenges/AutomationAnywhereLabs-ShoppingList.html?_gl=1*7jy6ue*_gcl_au*OTQ2NjYzODcwLjE3MzM0NDI5MTI.*_ga*Mjc3ODU2MjcxLjE3MzM0NDI5MTI.*_ga_DG1BTLENXK*MTczMzQ0MjkxMi4xLjEuMTczMzQ0MzY2OC4xNy4wLjEyOTQwNjk3NDA.'

# Constantes de diretórios, definindo caminhos para armazenamento de arquivos.
DIRECTORY_ORIGIN = os.getcwd()  # Diretório atual do projeto
DIRECTORY_SAVED_FILE = os.path.join(DIRECTORY_ORIGIN, 'BASE DE DADOS A SER PROCESSADA')  # Diretório para dados a serem processados
DIRECTORY_DESTINATION_FILE = os.path.join(DIRECTORY_ORIGIN, 'PROCESSADOS')  # Diretório para arquivos processados
DIRECTORY_SCREENSHOTS_ERROR = os.path.join(DIRECTORY_ORIGIN, 'SCREENSHOTS_ERROR')  # Diretório para screenshots de erros
DIRECTORY_SCREENSHOTS_SUCCESS = os.path.join(DIRECTORY_ORIGIN, 'SCREENSHOTS_SUCCESS')  # Diretório para screenshots de sucesso


# Variáveis de controle do fluxo do programa
loop = 'ON'  # Controle para manter o loop ativo
state = 'INITIALIZATION'  # Estado inicial do sistema
transaction_id = -1  # ID da transação, inicializado como -1 e será incrementado.
first_execution = True  # Flag para indicar a primeira execução