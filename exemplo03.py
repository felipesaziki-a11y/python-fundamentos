import requests

url_base = "https://api.franciscosensaulas.com"

url = f"{url_base}/api/v1/biblioteca/categorias"

resposta = requests.get(url)

print("Status code: ", resposta.status_code)
print("Response: ", resposta.text)

def apagar_categoria():
    id = 191
    url = f"{url_base}/api/v1/biblioteca/categorias/{id}"

    resposta = requests.delete(url)
    print("")