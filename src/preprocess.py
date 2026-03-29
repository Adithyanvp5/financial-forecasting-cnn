import pandas as pd
import glob

files = glob.glob("data/*.csv")

dfs = []
for f in files:
    df = pd.read_csv(f, index_col="Date", parse_dates=True)
    df = df[["Close"]]
    df.rename(columns={"Close": f.split("/")[-1].replace(".csv", "")}, inplace=True)
    dfs.append(df)

final = pd.concat(dfs, axis=1).dropna()
final = (final - final.min()) / (final.max() - final.min())

final.to_csv("data/merged.csv")
print("Preprocessing complete.")
