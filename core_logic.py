import pandas as pd
import matplotlib.pyplot as plt

#  Basic Moving Average Crossover Strategy
def generate_signals(df):
    df['ma50'] = df['close'].rolling(50).mean()
    df['ma200'] = df['close'].rolling(200).mean()
    df['signal'] = 0
    df['signal'][df['ma50'] > df['ma200']] = 1
    df['signal'][df['ma50'] < df['ma200']] = -1
    return df

# (Optional) Visualization
def plot_signals(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['close'], label='Close Price', alpha=0.5)
    plt.plot(df['ma50'], label='MA50', linestyle='--')
    plt.plot(df['ma200'], label='MA200', linestyle='--')
    plt.title("MA50/MA200 Crossover Strategy")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("data/ohlc_sample.csv", parse_dates=['date'])
    df.set_index('date', inplace=True)
    df = generate_signals(df)
    plot_signals(df)
