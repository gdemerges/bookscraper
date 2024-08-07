import psycopg2
import json

# Lire les informations de connexion depuis le fichier config.json
with open('config.json', 'r') as f:
    config = json.load(f)

hostname = config['hostname']
database = config['database']
username = config['username']
password = config['password']
port = config['port']

conn = psycopg2.connect(
    host=hostname,
    database=database,
    user=username,
    password=password,
    port=port
)

cur = conn.cursor()
cur.execute("SELECT version();")
record = cur.fetchone()
print(f"Vous êtes connecté à - {record}\n")
cur.close()
conn.close()
