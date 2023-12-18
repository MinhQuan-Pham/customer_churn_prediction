import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path, header=0)

def drop_columns(df):
    columns_to_drop = ['customer_id', 'company_name', 'zip_code', 'country']
    df.drop(columns_to_drop, axis=1, inplace=True)
    return df