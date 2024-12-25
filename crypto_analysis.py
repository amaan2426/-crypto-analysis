from pycoingecko import CoinGeckoAPI
import pandas as pd
import schedule
import time
import os

# Fetch cryptocurrency data
def fetch_crypto_data():
    cg = CoinGeckoAPI()
    data = cg.get_coins_markets(vs_currency='usd', order='market_cap_desc', per_page=50, page=1)
    crypto_data = [
        {
            "Name": coin['name'],
            "Symbol": coin['symbol'],
            "Price (USD)": coin['current_price'],
            "Market Cap": coin['market_cap'],
            "24h Volume": coin['total_volume'],
            "24h Change (%)": coin['price_change_percentage_24h']
        } for coin in data
    ]
    return pd.DataFrame(crypto_data)

# Export data to Excel
def update_excel(df, filename="crypto_data.xlsx"):
    df.to_excel(filename, index=False)
    print(f"Data has been written to {filename}")
    os.startfile(filename)  # Open Excel file automatically

# Perform scheduled updates
def job():
    print("\nUpdating data...")
    df = fetch_crypto_data()  # Fetch the latest data
    update_excel(df)         # Write to Excel
    print("Data updated successfully!")

# Main execution
if __name__ == "__main__":
    print("Fetching initial data...")
    df = fetch_crypto_data()
    update_excel(df)

    print("Starting live updates every 5 minutes. Press Ctrl+C to stop.")
    schedule.every(5).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
