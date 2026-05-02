import librosa
import numpy as np

SR = 16000

def extract_spectrogram(path):
    audio, sr = librosa.load(path, sr=SR, duration=3)

    if len(audio) < SR * 3:
        audio = np.pad(audio, (0, SR * 3 - len(audio)))

    mel = librosa.feature.melspectrogram(
        y=audio,
        sr=sr,
        n_mels=128,
        fmax=8000
    )

    mel = librosa.power_to_db(mel, ref=np.max)
    mel = mel[:, :128]

    if mel.shape[1] < 128:
        pad = 128 - mel.shape[1]
        mel = np.pad(mel, ((0, 0), (0, pad)))

    # 🔥 QUAN TRỌNG
    mel = (mel - np.mean(mel)) / (np.std(mel) + 1e-6)

    return mel.reshape(128, 128, 1)