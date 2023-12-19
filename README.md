## Overview
- This repository contains a machine learning model designed to predict customer churn.
- Customer churn refers to the phenomenon where customers stop using a service or product.
- The objective of this model is to identify potential churners based on various features.

## Contents
- Notebooks: The notebooks directory includes Jupyter notebooks used for data exploration, preprocessing, and model training. Follow the notebooks in sequential order to understand the development thought process.

- Requirements: The requirements.txt file enumerates the Python packages and their versions required for running the code successfully. Use the following command to install them: pip install -r requirements.txt

- Modules: The modules folder contains organized Python code that is utilized in the notebooks for specific tasks, such as data loading or data preprocessing.

## Model Monitoring
- Loggers module has been implemented to log the model's performance into a flat file for future monitoring and reference
- Email notifier module has been implemented to send an alert email whenever the performance drops below 80% (Recall Class 1 < 0.8)

## License
This project is licensed under the MIT License.
