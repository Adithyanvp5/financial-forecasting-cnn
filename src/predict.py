import numpy as np
from tensorflow.keras.models import load_model

model = load_model("results/model.h5")
spectrogram = np.load("results/spectrogram.npy")
X = spectrogram[..., None]

prediction = model.predict(X)
print("Future price prediction:")
print(prediction)
