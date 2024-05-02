import psycopg2

class PostgresDBConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, host, port, database, user, password):
        if not hasattr(self, 'connection'):
            self.host = host
            self.port = port
            self.database = database
            self.user = user
            self.password = password
            self.connect()

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connected to PostgreSQL database successfully")
        except psycopg2.Error as e:
            print(f"Error connecting to PostgreSQL database: {e}")

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")
            self.connection.rollback()

    def close_connection(self):
        if hasattr(self, 'connection'):
            self.connection.close()
            print("Connection to PostgreSQL database closed")

# Example usage:
if __name__ == "__main__":
    db_connection = PostgresDBConnection(
        host='localhost',
        port='5432',
        database='your_database',
        user='your_user',
        password='your_password'
    )

    # Execute a query
    db_connection.execute_query("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, data VARCHAR);")

    # Close the connection
    db_connection.close_connection()


#This singleton class PostgresDBConnection ensures that only one instance of the database connection is created throughout the application. It uses the psycopg2 library to connect to a PostgreSQL database. You can initialize the connection parameters 
#like host, port, database name, username, and password when creating an instance of the class. The execute_query method can be used to execute SQL queries, and the close_connection method is used to close the database connection.



