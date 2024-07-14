import requests
from PySimpleGUI import PySimpleGUI as sg

# Função para consultar o CEP
def consulta_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    dados = response.json()
    if 'erro' not in dados:
        return dados
    else:
        return None

# Layout da interface
sg.theme('Dark Blue 3')
layout = [
    [sg.Text('CEP:'), sg.Input(key='cep', size=(20, 1))],
    [sg.Button('Entrar')],
    [sg.Text('', size=(40, 10), key='output')],
]

# Janela
janela = sg.Window('Consulta CEP', layout)

# Loop de eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        cep = valores['cep']
        if cep:
            dados_cep = consulta_cep(cep)
            if dados_cep:
                output_text = (
                    f"CEP: {dados_cep['cep']}\n"
                    f"Logradouro: {dados_cep['logradouro']}\n"
                    f"Bairro: {dados_cep['bairro']}\n"
                    f"Cidade: {dados_cep['localidade']}\n"
                    f"Estado: {dados_cep['uf']}"
                )
            else:
                output_text = "CEP não encontrado."
        else:
            output_text = "Por favor, insira um CEP."
        
        janela['output'].update(output_text)

janela.close()
