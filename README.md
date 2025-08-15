# SalesSight
SalesSight is a powerful yet user-friendly grocery sales forecasting tool. At its core, it uses a LightGBM machine learning model to predict sales with high accuracy. The project includes two versions of the model: a solid baseline (Alpha) and an improved, hyperparameter-tuned version (Beta).

SalesSight: A Grocery Sales Forecasting Tool 
This project provides a tool for forecasting grocery sales using machine learning. It includes a baseline model (Alpha) and an optimized model (Beta) built with LightGBM. The project also features an interactive web application built with Streamlit for live forecasting.

Features
Two Forecasting Models:

Alpha Model: A baseline LightGBM model that serves as the starting point for predictions.

Beta Model: An optimized LightGBM model with hyperparameter tuning for improved accuracy.

Interactive UI: A user-friendly web interface built with Streamlit (live_app.py) that allows for:

Model selection (Alpha or Beta).

Selection of store and item numbers.

Date range selection for forecasting.

Visualization of the sales forecast.

Efficient Data Handling: Utilizes Polars for fast and memory-efficient data manipulation.

Getting Started
Prerequisites
Python 3.7+

Pip

Installation
Clone the repository:

git clone https://github.com/your-username/SalesSight.git

Navigate to the project directory:

cd SalesSight

Install the required packages:

pip install -r requirements.txt

How to Launch the UI
To run the Streamlit application, execute the following command in your terminal:

streamlit run live_app.py

This will launch the web application in your default browser.

Future Development
This project is currently in development, with a focus on improving forecasting accuracy. Future plans include:

Model Expansion: We are actively exploring and adapting new models like ARIMA, SARIMA, and Auto-Regressors to enhance the forecasting capabilities.

Feature Engineering: We will be incorporating more advanced features, such as holiday and promotional data, to create more robust models.

Performance Metrics: Additional metrics will be added to provide a more comprehensive evaluation of model performance.
