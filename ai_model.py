import tensorflow as tf
import numpy as np
import os
from config import MODEL_PATH

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"❌ Không tìm thấy model: {MODEL_PATH}")

model = tf.keras.models.load_model(MODEL_PATH)

def predict(feature):
    feature = np.expand_dims(feature, axis=0)

    pred = model.predict(feature, verbose=0)[0]

    print("DEBUG PRED:", pred)  # 👈 debug

    prob = float(pred[0])

    if prob > 0.5:
        gender = "Male"
        confidence = prob
    else:
        gender = "Female"
        confidence = 1 - prob

    return gender, confidence