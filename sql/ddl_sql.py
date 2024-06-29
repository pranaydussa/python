import mysql.connector

try:
    # Establish the connection
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='learning'
    )

    cursor = connection.cursor()

    
    create_table_query = """
    CREATE TABLE workers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        position VARCHAR(100),
        salary DECIMAL(10, 2)
    );
    """
    cursor.execute(create_table_query)
    print("Table 'workers' created successfully.")

    # Example DDL: Alter a table to add a column
    alter_table_query = """
    ALTER TABLE workers
    ADD birthdate DATE;
    """
    cursor.execute(alter_table_query)
    print("Column 'birthdate' added to 'workers' table.")

    # Example DDL: Drop a table
    drop_table_query = """
    DROP TABLE workers;
    """
    cursor.execute(drop_table_query)
    print("Table 'workers' dropped successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection closed.")
