import yfinance as yf
import pandas as pd

# Define the stock ticker (TATASTEEL for National Stock Exchange)
ticker = "TATASTEEL.NS"

def download_data():
    print(f"Fetching data for {ticker}...")
    # Get 2 years of daily historical data
    data = yf.download(ticker, period="2y", interval="1d")
    
    if data.empty:
        print("Error: No data found. Check your internet or ticker symbol.")
        return
    
    # Clean data: Remove any missing values
    data_cleaned = data.dropna()
    
    # Save to CSV
    filename = "raw_stock_data.csv"
    data_cleaned.to_csv(filename)
    print(f"Success! Data saved to {filename}")

if __name__ == "__main__":
    download_data()

