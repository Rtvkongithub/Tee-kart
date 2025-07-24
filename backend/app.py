from prometheus_flask_exporter import PrometheusMetrics
from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)
metrics =  PrometheusMetrics(app)

# Database connection config from environment
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "teekart")
DB_USER = os.getenv("DB_USER", "ritvik")
DB_PASSWORD = os.getenv("DB_PASSWORD", "pass123")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

@app.route("/products")
def get_products():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, price FROM products")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    products = [{"id": row[0], "name": row[1], "price": row[2]} for row in rows]
    return jsonify(products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

