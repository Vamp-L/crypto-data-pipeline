import snowflake.connector

#configure the connnections
conn = snowflake.connector.connect(
    user="vamp",
    password="Vampplays12345",
    account="pp08321.ap-southeast-3.aws",
    warehouse="COMPUTE_WH",
    database="DEMO_DB",
    schema="PUBLIC"
)

#opean a cursor
cursor = conn.cursor()

#execute a query
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER,
    amount FLOAT,
    country STRING
    )
    """
)
#insert a record
try:
    cursor.execute(
        """
        INSERT INTO orders(order_id, amount, country)
        VALUES(%s, %s, %s)
        """,
        (2, 200, "INA"),
        (3, 300, "JP")
    )
    print("insert successfull")
except Exception as e:
    print(f"insert failed : {e}")

#select data from table
cursor.execute(
    "SELECT order_id, amount, country FROM orders"
)

rows = cursor.fetchall()

for row in rows:
    print(row)



#close cursor
cursor.close()
conn.close()


