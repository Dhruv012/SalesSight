import streamlit as st
import polars as pl
import pandas as pd
import lightgbm as lgb
import altair as alt
from datetime import date, timedelta
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="Live Sales Forecaster",
    page_icon="📊",
    layout="wide"
)

# --- App State ---
if 'model_rmse' not in st.session_state:
    st.session_state.model_rmse = 19.0

# --- Title and Description ---
st.title("📉 Live Grocery Sales Forecaster")
st.markdown("Select a model, store, item, and date range to generate a live forecast.")

# --- Functions ---
def find_model_files(path="models"):
    if not os.path.exists(path):
        return []
    return [f for f in os.listdir(path) if f.endswith((".txt", ".bin"))]

# MODIFIED: Load model function now takes a full path
@st.cache_resource(show_spinner="Loading model...")
def load_model(model_path):
    model = lgb.Booster(model_file=model_path)
    st.session_state.model_rmse = 19.0 # You could make this dynamic later
    return model

# MODIFIED: Load data function now takes a filename argument
@st.cache_data(show_spinner="Loading prediction data...")
def load_initial_data(prediction_filename):
    df = pl.read_csv(prediction_filename)
    unique_stores = sorted(df["store_nbr"].unique().to_list())
    unique_items = sorted(df["item_nbr"].unique().to_list())
    return unique_stores, unique_items

def feature_engineer_pandas(df):
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day_of_week'] = df['date'].dt.weekday
    df['week_of_year'] = df['date'].dt.isocalendar().week.astype(int)
    return df

# --- Sidebar User Inputs & DYNAMIC DATA LOADING ---
st.sidebar.header("Forecasting Inputs")

model_files = find_model_files()
if not model_files:
    st.error("No model files found in the 'models' folder.")
    st.stop()

# 1. User selects a model
selected_model_file = st.sidebar.selectbox("Select Model", model_files)
model_path = os.path.join("models", selected_model_file)

# 2. NEW: Derive the associated CSV name from the model name
associated_csv_file = selected_model_file.replace("model_", "detailed_predictions_").replace(".txt", ".csv")

# 3. NEW: Check if the associated CSV exists and load the data
if not os.path.exists(associated_csv_file):
    st.error(f"Error: The associated data file '{associated_csv_file}' was not found for the selected model.")
    st.stop()
else:
    # Load the model and the correct data file
    model = load_model(model_path)
    unique_stores, unique_items = load_initial_data(associated_csv_file)

    # Continue with the rest of the UI
    selected_store = st.sidebar.selectbox("Select Store Number", unique_stores)
    selected_item = st.sidebar.selectbox("Select Item Number", unique_items)

    today = date.today()
    start_date = st.sidebar.date_input("Start Date", today)
    end_date = st.sidebar.date_input("End Date", today + timedelta(days=14))

    # --- Prediction Logic ---
    if st.sidebar.button("🚀 Generate Forecast"):
        if start_date > end_date:
            st.error("Error: End date must be after start date.")
        else:
            # (The rest of the prediction logic is the same as before)
            date_range = pd.date_range(start_date, end_date, freq='D')
            future_df = pd.DataFrame({
                'date': date_range,
                'store_nbr': selected_store,
                'item_nbr': selected_item,
                'onpromotion': False
            })

            future_df_featured = feature_engineer_pandas(future_df.copy())
            features = ['store_nbr', 'item_nbr', 'onpromotion', 'year', 'month', 'day_of_week', 'week_of_year']
            X_future = future_df_featured[features]

            predictions = model.predict(X_future, num_iteration=model.best_iteration)
            predictions[predictions < 0] = 0
            future_df['predicted_sales'] = predictions

            st.header(f"Forecast for Item `{selected_item}` in Store `{selected_store}`")

            total_sales = predictions.sum()
            avg_daily_sales = predictions.mean()
            total_uncertainty = st.session_state.model_rmse * (len(predictions) ** 0.5)

            st.markdown(f"""
            Using model **{selected_model_file}**, the forecast is a total of **{total_sales:.0f}** units.
            The average daily forecast is **{avg_daily_sales:.1f}** units.
            """)

            col1, col2 = st.columns(2)
            col1.metric("Total Forecasted Sales", f"{total_sales:.0f} units")
            col2.metric("Estimated Uncertainty", f"± {total_uncertainty:.0f} units")

            chart = alt.Chart(future_df).mark_line(
                point=True, tooltip=True
            ).encode(
                x=alt.X('date:T', title='Date'),
                y=alt.Y('predicted_sales:Q', title='Predicted Unit Sales')
            ).properties(
                height=400
            ).interactive()

            st.altair_chart(chart, use_container_width=True)