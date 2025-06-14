import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from hmmlearn.hmm import GaussianHMM
from sklearn.preprocessing import StandardScaler
from datetime import datetime

# 🔹 Load your OHLC data (CSV format with date, open, high, low, close)
def load_data(filepath):
    df = pd.read_csv(filepath, parse_dates=['date'])
    df.set_index('date', inplace=True)
    return df

# 🔹 Feature Engineering
def prepare_features(data):
    data['log_returns'] = np.log(data['close'] / data['close'].shift(1))
    data['atr'] = data['high'] - data['low']
    data.dropna(inplace=True)
    return data

# 🔹 HMM Model Training
def train_hmm(data):
    features = data[['log_returns', 'atr']]
    scaler = StandardScaler()
    X = scaler.fit_transform(features)
    
    model = GaussianHMM(n_components=3, covariance_type="full", n_iter=200)
    model.fit(X)
    hidden_states = model.predict(X)
    return model, hidden_states, X

# 🔹 Plotting Regimes
def plot_hidden_states(data, hidden_states):
    data = data.copy()
    data['state'] = hidden_states
    plt.figure(figsize=(12, 6))
    for state in sorted(data['state'].unique()):
        subset = data[data['state'] == state]
        plt.plot(subset.index, subset['close'], label=f"Regime {state}")
    plt.title("Market Regimes Identified by HMM")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    filepath = "data/ohlc_sample.csv"  # Provide your own CSV file here
    df = load_data(filepath)
    df = prepare_features(df)
    model, hidden_states, X = train_hmm(df)
    plot_hidden_states(df, hidden_states)
