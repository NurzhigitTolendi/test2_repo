import psycopg2 

conn = psycopg2.connect(
    host='localhost', 
    dbname='students', 
    user='postgres', 
    password='admin'
)

cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    score INTEGER
)
""")
conn.commit()

print("Table created successfully!")

# Closing connection
cur.close()
conn.close()
