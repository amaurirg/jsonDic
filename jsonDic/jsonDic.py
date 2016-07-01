import json
import requests

nome = input("Digite o nome do usuário: ")
resposta = requests.get(nome)

dicJson = json.loads(resposta.text)
print(dicJson)

for k,v in dicJson.items():
    print(k + ' : ' + str(v))
