import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

import tensorflow as tf
from keras.models import load_model

def load_dataset(filepath : str):
    test = pd.read_csv(filepath)
    y_test = test["label"].astype('int32')
    x_test = test.drop(columns='label')
    x_test = x_test.values.reshape(-1,27,48,3)
    x_test = x_test / 255.0
    y_test = y_test-1
    y_test = tf.keras.utils.to_categorical(y_test, 3)
    return x_test, y_test

def eval_model(test_dataset_path: str):
    x_test, y_test = load_dataset(test_dataset_path)
    model = load_model("model\model-gen-1.h5")
    print(model.predict(x_test))
    results = model.evaluate(x_test, y_test, batch_size=256)
    return results