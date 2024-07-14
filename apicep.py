import requests
import pandas as pd

while True:
    try:
        cod_cep = input("Força o código CEP: ")
        if len(cod_cep) !=8:
            print("Atenção, seu código CEP precisa ter 08 caracteries. Forneça outro código: ")
        else:
            api = f'https://viacep.com.br/ws/{cod_cep}/json/'
            consulta = requests.get(api)
            consulta = consulta.json()
            consulta = pd.DataFrame(consulta)
            print(consulta)

    except ValueError:
        print("Isso não é um código de CEP válido. Tente novamente.")