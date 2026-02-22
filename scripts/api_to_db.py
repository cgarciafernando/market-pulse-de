import os
import time
import requests
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def run_ingestion():
    # Variables de entorno
    db_host = os.getenv("DB_HOST", "127.0.0.1")
    db_name = os.getenv("DB_NAME", "market_pulse")
    db_user = os.getenv("DB_USER", "engineer")
    db_pass = os.getenv("DB_PASSWORD", "password123")
    db_port = os.getenv("DB_PORT", "5432")

    try:
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_pass,
            port=db_port
        )
        cur = conn.cursor()
        print(f"Connected to database at {db_host}")
    except Exception as e:
        print(f"Database connection failed: {e}")
        return

    monedas = ["bitcoin", "ethereum", "solana"]

    for moneda in monedas:
        try:
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={moneda}&vs_currencies=usd"
            response = requests.get(url)
            data = response.json()

            if moneda in data:
                precio = data[moneda]['usd']
                
                cur.execute(
                    "INSERT INTO precios_crypto (moneda, precio) VALUES (%s, %s)",
                    (moneda, precio)
                )
                print(f"Inserted {moneda}: {precio}")
            else:
                print(f"No data found for {moneda}")
            
            time.sleep(2)

        except Exception as e:
            print(f"Error processing {moneda}: {e}")

    conn.commit()
    cur.close()
    conn.close()
    print("Ingestion process completed")

if __name__ == "__main__":
    run_ingestion()
