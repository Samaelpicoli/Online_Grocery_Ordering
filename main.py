from grocery_ordering import OnlineGroceryOrdering

import grocery_ordering

state = 'INITIALIZATION'
status_loop = 'ON'

while status_loop == 'ON':
    
    match state:
    
        case 'INITIALIZATION':
            
            bot = OnlineGroceryOrdering('base_de_dados')
            state = 'GET TRANSACTION'
            continue
            
        case 'GET TRANSACTION':
            
            dados = bot.extrair_dados()
            if dados is None:
                state = 'END'
                continue
            bot.exibir_dados(dados)
            state = 'PROCESS'
            continue
            
        case 'PROCESS':
                 
            bot.inserir_dados()
            bot.capturar_tempo()
            state = 'END'
            continue 

        case 'END':
            bot.encerrar_driver()
            status_loop = 'OFF'
            continue

