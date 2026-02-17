import pandas as pd
import matplotlib.pyplot as plt

def plot_stock_trend():
    try:
        # 1. Load the cleaned data
        df = pd.read_csv("cleaned_stock_data.csv")
        
        # 2. Plotting the Closing Price
        plt.figure(figsize=(10, 5))
        plt.plot(df['Close'], label='Close Price', color='blue')
        plt.title('TATASTEEL Stock Price Trend')
        plt.xlabel('Days')
        plt.ylabel('Price (INR)')
        plt.legend()
        
        # 3. Save the plot as an image
        plt.savefig("stock_trend.png")
        print("Chart saved as 'stock_trend.png'. View it to see the trend!")
        
    except FileNotFoundError:
        print("Error: Run clean_data.py first!")

if __name__ == "__main__":
    plot_stock_trend()
