import yfinance as yf
import os

companies = ["AAPL", "GOOGL", "META"]
os.makedirs("data", exist_ok=True)

for c in companies:
    df = yf.download(c, start="2015-01-01", end="2024-01-01")
    df.to_csv(f"data/{c}.csv")

print("Data downloaded successfully.")
