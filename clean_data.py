import pandas as pd

def clean_stock_data():
    try:
        # 1. Load the raw data
        df = pd.read_csv("raw_stock_data.csv")
        print("Raw data loaded successfully.")

        # 2. Check for missing values (Nulls)
        if df.isnull().values.any():
            print("Missing values detected. Cleaning...")
            df = df.dropna() # Remove rows with empty values
        
        # 3. Calculate 'Daily Return' (A key feature for AI)
        # Formula: ((Close Price - Open Price) / Open Price) * 100
        df['Daily_Return_Pct'] = ((df['Close'] - df['Open']) / df['Open']) * 100
        
        # 4. Save the cleaned version
        df.to_csv("cleaned_stock_data.csv", index=False)
        print("Success! Cleaned data saved as 'cleaned_stock_data.csv'")
        
    except FileNotFoundError:
        print("Error: 'raw_stock_data.csv' not found. Run fetch_data.py first!")

if __name__ == "__main__":
    clean_stock_data()
