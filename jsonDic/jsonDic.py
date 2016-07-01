import json
import requests

resposta = requests.get('https://api.github.com/users/amaurirg')
print(resposta.text)

dicJson = json.loads(resposta.text)
print(dicJson)

for k,v in dicJson.items():
    print(k + ' : ' + str(v))

print(dicJson['login'])