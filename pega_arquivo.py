import os
import time

def verifica_planilha_baixada(pasta_download):
    try:
        os.chdir(pasta_download)
        time.sleep(1)
        arquivos = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
        novo_arquivo = arquivos[-1]
        print(novo_arquivo)
        return novo_arquivo
    except:
        raise Exception("Falha ao encontrar último arquivo baixado.")

def deleta_arquivos_xl_downloads(pasta_download):
    try:
        arqs = os.listdir(pasta_download)
        
        for arq in arqs:
            if arq.endswith(".csv") or arq.endswith(".xlsx"):
                os.remove(os.path.join(pasta_download, arq))
    except:
        raise Exception("Falha ao limpar pasta de Download.")

def espera_finalizar_download_planilha(pasta_download):
    try:
        arquivo_ext = "crdownload"
        #limpa pasta de download de arquivos xls/xlsx
        deleta_arquivos_xl_downloads(pasta_download)
        cont = 0
        while "crdownload" == arquivo_ext:
            novo = verifica_planilha_baixada(pasta_download)
            if (("csv" in novo) or ("xlsx" in novo)) and not (("crdownload" in novo) or ("tmp" in novo)) :
                arquivo_ext = "c"
                return novo
            else:
                arquivo_ext = "crdownload"
            cont = cont+1
            if cont == 10:
                raise Exception('Erro durante o download do arquivo')
    except:
        raise Exception("Falha ao encontrar último arquivo baixado.")