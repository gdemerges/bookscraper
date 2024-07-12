import psycopg2

hostname = 'dem-gui-postgre1.postgres.database.azure.com'
database = 'bookscraper'
username = 'gdemerges'
password = 'c_}nsG6xr~Zhu"P'
port = 5432

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
