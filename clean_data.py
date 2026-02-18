import pandas as pd


def clean_stock_data():
    file_path = 'raw_stock_data.csv'

    try:
        # 1. Load data - skipping the first row if yfinance added a 'Ticker' header
        # If your CSV looks weird, try adding: header=[0, 1]
        df = pd.read_csv(file_path, index_col=0)

        print("Raw data loaded successfully.")

        # 2. FORCE columns to be numbers (This fixes the 'str' and 'str' error)
        # errors='coerce' turns text like "Price" into NaN, which we then drop
        df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
        df['Open'] = pd.to_numeric(df['Open'], errors='coerce')

        # 3. Remove any rows that failed to convert or have empty values
        df = df.dropna(subset=['Close', 'Open'])

        print("Data types converted. Cleaning missing values...")

        # 4. Perform the calculation (Now safe from TypeError)
        df['Pct_Change'] = ((df['Close'] - df['Open']) / df['Open']) * 100

        # 5. Save the cleaned version
        df.to_csv('cleaned_stock_data.csv')
        print("Success! Cleaned data saved to cleaned_stock_data.csv")
        print(df.head())  # Preview the first 5 rows

    except FileNotFoundError:
        print(f"Error: {file_path} not found. Run fetch_data.py first!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    clean_stock_data()
