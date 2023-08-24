import json
import requests

arquivo_cep= requests.get("https://viacep.com.br/ws/RS/Porto%20Alegre/Domingos/json/")

print(arquivo_cep.json())

data_cep = arquivo_cep.json()

f_cep = json.dumps(data_cep, indent=4, ensure_ascii=False)

print(f_cep)

for rel_cep in data_cep:
    cep = rel_cep["cep"]
    logradouro = rel_cep["logradouro"]
    bairro = rel_cep["bairro"]
    localidade = rel_cep["localidade"]


    print(
        "cep: ", cep,
        "\nlogradouro: ", logradouro,
        "\nbairo: ", bairro,
        "\nlocalidade: ", localidade,
        "\n-----------------------------"          
        )