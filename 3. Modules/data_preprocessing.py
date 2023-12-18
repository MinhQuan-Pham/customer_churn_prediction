import numpy as np
import pandas as pd

def impute_referral_role(df):
    df['referral_role'].fillna("not participated", inplace=True)
    return df

def handle_outliers(df, threshold_multiplier=1.5):
    numerical_features = df.loc[:, ((df != 0) & (df != 1)).any()].select_dtypes(exclude=['object']).columns.tolist()
    Q1 = df[numerical_features].quantile(0.25)
    Q3 = df[numerical_features].quantile(0.75)
    IQR = Q3 - Q1
    outliers = ((df[numerical_features] < (Q1 - threshold_multiplier * IQR)) |
                (df[numerical_features] > (Q3 + threshold_multiplier * IQR)))
    df = df[~outliers.any(axis=1)]
    return df

def handle_dates(df, date_format='%m/%d/%y'):
    invalid_dates = df.loc[~pd.to_datetime(df['start_date'], format=date_format, errors='coerce').notnull(), 'start_date']
    df = df[~df['start_date'].isin(invalid_dates)]
    return df

def one_hot_encode(df):
    categorical_features = df.select_dtypes(include='object').columns.tolist()
    df_encoded = pd.get_dummies(df[categorical_features], drop_first=True)
    return df_encoded

def log_transform_numerical(df):
    numerical_features = df.select_dtypes(exclude=['object']).columns.tolist()
    for feature in numerical_features:
        df[feature] = np.log1p(df[feature])
    return df