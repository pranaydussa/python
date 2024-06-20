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

    # Create a 
    
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        position VARCHAR(100),
        salary DECIMAL(10, 2)
    )
    """
    cursor.execute(create_table_query)
    print("Table 'employees' created successfully.")

    # Insert data into the table
    insert_data_query = """
    INSERT INTO employees (name, position, salary)
    VALUES (%s, %s, %s)
    """
    employee_data = [
        ('pranay', 'Software Engineer', 75000.00),
        ('pavan', 'Data Scientist', 85000.00),
        ('samara', 'Product Manager', 95000.00)
    ]

    cursor.executemany(insert_data_query, employee_data)
    connection.commit()  # Commit the transaction
    print(f"{cursor.rowcount} rows were inserted successfully.")

    # Check the created tables
    show_tables_query = "SHOW TABLES"
    cursor.execute(show_tables_query)
    tables = cursor.fetchall()
    print("Tables in the database:")
    for table in tables:
        print(table[0])

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection closed.")
