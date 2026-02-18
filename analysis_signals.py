import pandas as pd

def generate_signals():
    try:
        df = pd.read_csv("cleaned_stock_data.csv")
        
        # Calculate Moving Averages
        df['MA5'] = df['Close'].rolling(window=5).mean()
        df['MA20'] = df['Close'].rolling(window=20).mean()
        
        # Simple Buy/Sell Logic
        # If 5-day average crosses above 20-day average, it's a 'Golden Cross' (Buy)
        df['Signal'] = "HOLD"
        df.loc[df['MA5'] > df['MA20'], 'Signal'] = "BUY"
        df.loc[df['MA5'] < df['MA20'], 'Signal'] = "SELL"
        
        df.to_csv("stock_signals.csv", index=False)
        print("Signals generated! Check 'stock_signals.csv' for BUY/SELL indicators.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    generate_signals()
