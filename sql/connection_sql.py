import mysql.connector

try:
    
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='learning'
    )

    cursor = connection.cursor()
    # Execute the query
    cursor.execute("SELECT VERSION();")
    version = cursor.fetchone()

    print(version)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection closed.")
