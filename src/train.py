import numpy as np
from cnn_model import create_model

spectrogram = np.load("results/spectrogram.npy")
X = spectrogram[..., None]
y = np.mean(spectrogram, axis=0)

model = create_model(X.shape[1:])
model.fit(X, y, epochs=10)

model.save("results/model.h5")
print("Training complete.")
