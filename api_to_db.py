import requests
import psycopg2
url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'

dato = requests.get(url).json()

precio_btc = dato['bitcoin']['usd']

conn = psycopg2.connect(
	host = 'localhost',
	database = 'market_pulse',
	user = 'engineer',
	password = 'password123',
	port = '5432'
	)

cur = conn.cursor()

sql = 'INSERT INTO precios_crypto (moneda, precio) VALUES (%s, %s)'
valores = ('bitcoin', precio_btc)

cur.execute(sql, valores)
conn.commit()

cur.close()
conn.close()

print(f'Exito. Guardado bitcoin a: {precio_btc}')
