import requests
import json
import hashlib

mapAlphabetic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
url = "https://api.codenation.dev/v1/challenge/dev-ps";
token = ""

# Requisição e parse do json recebido no body
response = requests.get(url=url+"/generate-data?token="+token)
response = json.loads(response.text)

def code(text, numbers):
    text = text.lower()
    crypt = ""
    for c in text:
        if(c.isalpha()):
            crypt += getNewCharacter(c, numbers)
        else:
            crypt += c

    return crypt

def getNewCharacter(character, number):
    number = (mapAlphabetic.index(character) - int(number)) % len(mapAlphabetic)

    return mapAlphabetic[number]

cryptoStr = code(response['cifrado'], response['numero_casas'])
response['decifrado'] = cryptoStr
response['resumo_criptografico'] = hashlib.sha1(str(cryptoStr).encode('utf-8')).hexdigest()


url = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=1ddf62549c132e9ee8f576221da693c7bfbe8d1b"

payload = {}
files = [
  ('answer', open('/home/jonathan/PycharmProjects/Cryptography-of-Julius-Caesar/answer.json','rb'))
]

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))


#requests.post(url=url+"/submit-solution?token="+token, files=response)
