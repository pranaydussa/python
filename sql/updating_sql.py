
import mysql.connector

try:
    
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='learning'
    )

    cursor = connection.cursor()

    # Define the SQL update query
    update_query = """
    UPDATE employees
    SET salary = %s
    WHERE name = %s
    """
   
    data_to_update = (80000.00, 'pranay')

    cursor.execute(update_query, data_to_update)
    connection.commit()

    print(f"Number of rows affected: {cursor.rowcount}")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection closed.")

    
        
