from xgboost import XGBClassifier
from sklearn.metrics import classification_report

def train_xgboost_model(X_train, y_train):
    xgb_model = XGBClassifier()
    xgb_model.fit(X_train, y_train)
    return xgb_model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    recall_churn_class = classification_report(y_test, y_pred, target_names=["Not Churn", "Churn"]).split('\n')[3].split()[2]
    return y_pred, recall_churn_class