from data_loader import load_data, drop_columns
from data_preprocessing import impute_referral_role, handle_outliers, handle_dates, one_hot_encode, log_transform_numerical
from model import train_xgboost_model, evaluate_model
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import os
import pandas as pd

# Import the data
wd = os.getcwd()
input_data = os.path.join(wd, 'churn_prediction', 'Dataset', 'data_churn_model.csv')
df = load_data(input_data)

# Data Preprocessing
df = drop_columns(df)
df = impute_referral_role(df)
df = handle_outliers(df)
df = handle_dates(df)
df_encoded = one_hot_encode(df)
df = log_transform_numerical(df)

# Concatenate numerical and encoded categorical features
X = pd.concat([df.select_dtypes(exclude=['object']), df_encoded], axis=1)
y = df["is_churn"]

# Split the dataset into training and testing sets with stratification
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

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
