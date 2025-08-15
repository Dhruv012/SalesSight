# SalesSight: A Grocery Sales Forecasting Tool

SalesSight is a powerful yet user-friendly grocery sales forecasting tool that leverages machine learning to predict sales with high accuracy. At its core, it uses LightGBM models optimized for grocery retail data, providing businesses with actionable insights for inventory management and sales planning.

## 🌟 Features

- **Dual Model Architecture**: 
  - **Alpha Model**: Solid baseline LightGBM model for reliable predictions
  - **Beta Model**: Hyperparameter-tuned version for enhanced accuracy
- **Interactive Web Interface**: User-friendly Streamlit application for real-time forecasting
- **Store & Item Selection**: Flexible filtering by store and item numbers
- **Date Range Forecasting**: Customizable prediction periods
- **Visual Analytics**: Interactive charts and graphs for forecast visualization
- **High Performance**: Utilizes Polars for lightning-fast data processing

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Dhruv012/SalesSight.git
   cd SalesSight
   ```

2. **Download the model files**:
   - Go to the [Releases page](https://github.com/Dhruv012/SalesSight/releases)
   - Download `models.zip` from the latest release
   - Extract the zip file in your project root directory
   - Ensure the `models/` folder contains both model files

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the application**:
   ```bash
   streamlit run live_app.py
   ```

The application will open in your default web browser at `http://localhost:8501`

## 📁 Project Structure

```
SalesSight/
├── models/                          # Machine learning models (download required)
│   ├── model_alpha.txt             # Baseline LightGBM model
│   └── model_beta.txt              # Optimized LightGBM model
├── Sales_Forecast_alphaModel.ipynb # Alpha model development notebook
├── Sales_Forecast-betaModel.ipynb  # Beta model development notebook  
├── live_app.py                     # Streamlit web application
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
└── LICENSE                         # MIT License
```

## 🎯 How to Use

1. **Launch the App**: Run `streamlit run live_app.py`
2. **Select Model**: Choose between Alpha (baseline) or Beta (optimized) model
3. **Configure Parameters**: 
   - Select store number
   - Choose item number  
   - Set forecasting date range
4. **Generate Forecast**: Click to generate predictions
5. **Analyze Results**: View interactive charts and numerical forecasts

## 🔧 Model Details

### Alpha Model (Baseline)
- **Algorithm**: LightGBM Gradient Boosting
- **Purpose**: Reliable baseline predictions
- **Use Case**: Standard forecasting scenarios

### Beta Model (Optimized)  
- **Algorithm**: Hyperparameter-tuned LightGBM
- **Purpose**: Enhanced accuracy through optimization
- **Use Case**: High-precision forecasting requirements

**Note**: Model files are large (7GB combined) and distributed via GitHub Releases to maintain repository performance.

## 📊 Technical Stack

- **Machine Learning**: LightGBM, scikit-learn
- **Data Processing**: Polars, Pandas, NumPy
- **Web Framework**: Streamlit
- **Visualization**: Plotly, Matplotlib
- **Development**: Jupyter Notebooks

## 🛠️ Development Notebooks

- `Sales_Forecast_alphaModel.ipynb`: Alpha model development and training
- `Sales_Forecast-betaModel.ipynb`: Beta model optimization and validation

## 🚧 Future Roadmap

- **Advanced Models**: Integration of ARIMA, SARIMA, and Auto-Regressors
- **Feature Enhancement**: Holiday and promotional data integration
- **Performance Metrics**: Comprehensive model evaluation dashboard
- **API Development**: REST API for programmatic access
- **Cloud Deployment**: Scalable cloud-based forecasting service

## 📈 Performance

Both models are optimized for grocery retail data and provide:
- High accuracy predictions for short to medium-term forecasts
- Efficient processing of large datasets
- Real-time inference capabilities

## 🤝 Contributing

Contributions are welcome! Please feel free to:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Important Notes

- **Model Download Required**: The machine learning models must be downloaded separately from the Releases page
- **Data Requirements**: Ensure your data follows the expected format for optimal predictions
- **Performance**: Initial model loading may take a few moments due to file size


---

**Made with ❤️ for better grocery sales forecasting**
