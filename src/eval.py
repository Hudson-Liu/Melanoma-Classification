#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""eval.py: Evaluates the exported model on the reserved test split."""

__author__ = "Hudson Liu"
__email__ = "hudsonliu0@gmail.com"

import os

import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Load model & labels
model = tf.keras.models.load_model("converted_keras/keras_model.h5", compile=False)
class_names = open("converted_keras/labels.txt", "r").readlines()

# Create the array of the right shape
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def prep_img(filename: str):
    """Prepare a given image"""
    SIZE = (224, 224)
    image = Image.open(filename).convert("RGB")
    image = ImageOps.fit(image, SIZE, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array
    return data

def make_pred(data):
    """Make prediction from data"""
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Prints for debugging purposes (can be removed)
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", confidence_score)
    return class_name[2:-1]

c = 0
y_true = []
y_pred = []
root = os.getcwd()

# Benign
os.chdir(root + "/ISIC_2020_Training_JPEG/ben_t")
for f in os.listdir():
    # Generate Prediction
    data = prep_img(f)
    p = make_pred(data)
    y_pred.append(p) 
    y_true.append("Benign")

# Malignant
os.chdir(root + "/ISIC_2020_Training_JPEG/mal_t")
for f in os.listdir():
    # Generate Prediction
    data = prep_img(f)
    p = make_pred(data)
    y_pred.append(p) 
    y_true.append("Malignant")

d = ConfusionMatrixDisplay.from_predictions(y_true, y_pred, labels=["Benign", "Malignant"], cmap="Blues")
d.plot()
plt.show()

