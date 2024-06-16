import requests
import pandas as pd

while True:
    try:
        uf = input("Força o código o estado: ")
        cidade = input("Força  a cidade: ")
        endereco = input("Informe a rua: ")

        if len(uf) !=2:
            print("Atenção, forneça o estado apenas com a sigla (UF): ")
        else:
            api = f'https://www.viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/'
            consulta = requests.get(api)
            print(consulta)
            consulta = consulta.json()
            consulta = pd.DataFrame(consulta)
            print(consulta)

    except ValueError:
        print("Isso não é um código de CEP válido. Tente novamente.")