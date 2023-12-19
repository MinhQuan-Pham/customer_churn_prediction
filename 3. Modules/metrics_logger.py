from datetime import datetime

def log_metrics_to_txt(classification_report, file_path):
    # Parse the classification report
    lines = classification_report.split('\n')
    
    # Extract the date
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Prepare log data
    log_data = [f"Date: {current_date}"]
    log_data.extend(lines[2:-4])  # Exclude headers and support information

    # Write the log data to a text file
    with open(file_path, 'a') as file:
        for line in log_data:
            file.write(line + '\n')
        file.write('\n')  # Add a blank line for better readability
