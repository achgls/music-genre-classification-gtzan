import numpy as np

def PCA(data: np.ndarray):
    # Mean-standardize data

    # Perform SVD
    U, s, VT = np.linalg.svd(...)

    return 

def audio_to_spectrogram(audio_file):
    ...
    spectrogram = ...
    return spectrogram