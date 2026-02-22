import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def transform():
    db_host = os.getenv("DB_HOST", "postgres")
    db_name = os.getenv("DB_NAME", "market_pulse")
    db_user = os.getenv("DB_USER", "engineer")
    db_pass = os.getenv("DB_PASSWORD", "password123")
    db_port = os.getenv("DB_PORT", "5432")

    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_pass,
        port=db_port
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS daily_avg_prices (
            moneda VARCHAR(50),
            precio_promedio NUMERIC,
            fecha DATE,
            PRIMARY KEY (moneda, fecha)
        );
    """)

    cur.execute("""
        INSERT INTO daily_avg_prices (moneda, precio_promedio, fecha)
        SELECT moneda, AVG(precio), CURRENT_DATE
        FROM precios_crypto
        WHERE fecha_captura >= CURRENT_DATE
        GROUP BY moneda
        ON CONFLICT (moneda, fecha) DO UPDATE 
        SET precio_promedio = EXCLUDED.precio_promedio;
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Transformation completed")

if __name__ == "__main__":
    transform()
