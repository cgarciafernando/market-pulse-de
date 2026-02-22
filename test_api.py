import requests

url = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd'

respuesta = requests.get(url)

datos = respuesta.json()

precio = datos['ethereum']['usd']

print(f'El precio de ethereum es: {precio}')
