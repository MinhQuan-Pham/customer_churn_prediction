import os

import pandas as pd
from data_loader import drop_columns, get_database_data
from data_preprocessing import (
    handle_dates,
    handle_outliers,
    impute_referral_role,
    log_transform_numerical,
    one_hot_encode,
)
from email_notifier import send_email
from model import evaluate_model, train_xgboost_model
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

# Import the data
df = get_database_data("get_data_churn")

# Data Preprocessing
df = drop_columns(df)
df = impute_referral_role(df)
df = handle_outliers(df)
df = handle_dates(df)
df_encoded = one_hot_encode(df)
df = log_transform_numerical(df)

# Concatenate numerical and encoded categorical features
X = pd.concat([df.select_dtypes(exclude=["object"]), df_encoded], axis=1)
y = df["is_churn"]

# Split the dataset into training and testing sets with stratification
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train XGBoost model
xgb_model = train_xgboost_model(X_train, y_train)

# Evaluate the model
y_pred, recall_churn_class = evaluate_model(xgb_model, X_test, y_test)

# Print the results
print("XGBoost Model:")
print(f"Recall for Churn: {recall_churn_class}")
print()  # print a blank line
print("Classification Report")
print(classification_report(y_test, y_pred, target_names=["Not Churn", "Churn"]))

# Trigger an email alert if recall for Churn falls below a certain value
if float(recall_churn_class) < 0.8:
    send_email(
        "Alert: Churn Recall Below Threshold",
        "Churn recall is below the acceptable threshold. Please investigate.",
        "mike@gmail.com",
        "smtp.your_email_provider.com",
        465,  # SMTP port (use SSL)
        "mike@gmail.com",
        "mike_email_password",
    )
