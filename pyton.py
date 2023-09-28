import csv
import request

#função para verificar se as informações existem
def verificar_cnpj_na_api(cnpj_basico, cnpj_ordem, cnpj_div):
    #URL da Api
    url =f""

    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False

#Função para atualizar a api
def atualizar_apii(cnpj_basico, cnpj_ordem, cnpj_div):
    #URL Api Atualização
    url = ""
    data = {
        'cnpj_basico': cnpj_basico,
        'cnpj_ordem': cnpj_ordem,
        'cnpj_div': cnpj_div,
    }

    response = requests.put(url, json=data)
    if response.status_code == 200:
        print(f"Atualização bem-sucedida para CNPJ: {cnpj_basico}-{cnpj_ordem}-{cnpj_div}")
        else:
            print(f"Falha na atualização para CNPJ: {cnpj_basico}-{cnpj_ordem}-{cnpj_div}")

#Função para post Api
def fazer_post_na_api(cnpj_basico, cnpj_ordem, cnpj_div):
    #Url Api Criação
    url = ""
    data = {
        'cnpj_basico': cnpj_basico,
        'cnpj_ordem': cnpj_ordem,
        'cnpj_div': cnpj_div,
    }

    response = requests.post(url, json=data)
    if response.status_code = 201:
        print(f"Criação bem-sucedida para CNPJ: {cnpj_basico}-{cnpj_ordem}-{cnpj_div}")
        else:
            print(f"Falha na criação para CNPJ:" {cnpj_basico}-{cnpj_ordem}-{cnpj_div})

#abrir o arquivo CSV para leitura
with open('aquivo.csv' mode='r') as file:
    reader + csv.reader(file)
    next(reader) #Pula o cabeçalho se ouver

    for row in reader:
        cnpj_basico, cnpj_ordem, cnpj_div = row[0], row[1], row[2]

        if verificar_cnpj_na_api(cnpj_basico, cnpj_ordem, cnpj_div):
            atualizar_api(cnpj_basico, cnpj_ordem, cnpj_div)
            else:
                fazer_post_na_api(cnpj_basico, cnpj_ordem, cnpj_div)
                