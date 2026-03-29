import numpy as np
import pandas as pd
from scipy.signal import stft
import os

os.makedirs("results", exist_ok=True)

data = pd.read_csv("data/merged.csv")
signal = data.values[:, 0]

f, t, Zxx = stft(signal, nperseg=128)
spectrogram = np.abs(Zxx)

np.save("results/spectrogram.npy", spectrogram)
print("STFT spectrogram saved.")
