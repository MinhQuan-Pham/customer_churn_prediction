import pandas as pd
from datetime import datetime


def log_metrics_to_excel(classification_report, file_path):
    # Parse the classification report and create a DataFrame
    report_data = []
    lines = classification_report.split("\n")

    # Extract the date
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for line in lines[2:-4]:  # Exclude headers and support information
        row_data = line.split()
        metric_name = row_data[0]
        values = [float(x) for x in row_data[1:]]
        report_data.append([current_date, metric_name] + values)

    # Create a DataFrame
    columns = ["Date", "Metric", "Precision", "Recall", "F1-Score", "Support"]
    metrics_df = pd.DataFrame(report_data, columns=columns)

    # Save the DataFrame to an Excel file
    metrics_df.to_excel(file_path, index=False)
