import pandas as pd
import mysql.connector
import sql_statements

def get_database_data(sql_statement):
    # Enter database connection details here
    # Set ssl_disabled = "True" if facing any issue with SSL
    sh_db = mysql.connector.connect(
        host="",
        user="",
        passwd="",
        database="",
        auth_plugin='',
        port=3306
        # ssl_disabled="True",
        # ssl_ca='',
        # ssl_cert='',
        # ssl_key='',
    )

    db_cursor = sh_db.cursor()

    # Run Query, put return output into a dataframe
    if sql_statement == "get_data_churn":
        # Execute SQL Statement
        db_cursor.execute(sql_statements.get_data_churn)
        
        # Fetch all rows from query result
        result = db_cursor.fetchall()

        # Define Column Names
        columns = [
            # list of columns
        ]

        # Create a DataFrame using the query result and column names
        df = pd.DataFrame(result, columns=columns)
        
        # Return the DataFrame
        return df

def load_data(file_path):
    return pd.read_csv(file_path, header=0)

def drop_columns(df):
    columns_to_drop = ['customer_id', 'company_name', 'zip_code', 'country']
    df.drop(columns_to_drop, axis=1, inplace=True)
    return df