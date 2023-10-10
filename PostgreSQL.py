# Required Libraries
import psycopg2
import pandas as pd


class Database:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connected to PostgreSQL")
        except psycopg2.Error as e:
            print("Error connecting to PostgreSQL:", e)

    def get_table_as_dataframe(self, table_name):
        query = f"SELECT * FROM {table_name};"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            columns = [desc[0] for desc in cursor.description]
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=columns)
            return df
        except psycopg2.Error as e:
            print("Error retrieving table as DataFrame:", e)
            return None

    def execute_query(self, query):
        # SQL commands are made in other methods. They use this method to run the SQL commands
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except psycopg2.Error as e:
            print("Error executing query:", e)

    def create_table(self, table_name, columns):
        # SQL format : CREATE TABLE properties (col1 DATATYPE, col2 DATATYPE, ...)
        query = f"CREATE TABLE {table_name} ({columns})"
        self.execute_query(query)

    def insert_data(self, table_name, values):
        # SQL format : INSERT INTO properties VALUES (col1, col2, ...)
        query = f"INSERT INTO {table_name} VALUES {values}"
        self.execute_query(query)

    def create_table_from_dataframe(self, table_name, dataframe):
        # Generate the SQL column definitions
        columns = ', '.join([f"{column} {dataframe[column].dtype}" for column in dataframe.columns])

        # Create the table
        self.create_table(table_name, columns)

    def save_dataframe_to_table(self, table_name, dataframe):
        # Convert dataframe to a list of tuples
        records = list(dataframe.itertuples(index=False, name=None))

        # Generate placeholders for SQL query
        placeholders = ','.join(['%s'] * len(records[0]))

        # Generate SQL INSERT statement
        query = f"INSERT INTO {table_name} VALUES ({placeholders});"

        try:
            cursor = self.connection.cursor()
            cursor.executemany(query, records)
            self.connection.commit()
            print("Data saved to table successfully")
        except psycopg2.Error as e:
            print("Error saving data to table:", e)

    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection closed")

