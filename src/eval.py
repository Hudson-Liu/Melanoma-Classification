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
model = tf.keras.models.load_model("converted_savedmodel/model.savedmodel", compile=False)
class_names = open("converted_savedmodel/labels.txt", "r").readlines()

# Create the array of the right shape
NUM_IMGS = 200
data = np.ndarray(shape=(NUM_IMGS, 224, 224, 3), dtype=np.float32)

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
    return class_name[2:]

c = 0
y_true = []
y_pred = []
root = os.getcwd()

# Benign
os.chdir(root + "ISIC_2020_Training_JPEG/ben_t")
for f in os.listdir():
    # Generate Prediction
    data = prep_img(f)
    p = make_pred(data)
    y_pred.append() 
    y_true.append("Benign")

# Malignant
os.chdir(root + "ISIC_2020_Training_JPEG/mal_t")
for f in os.listdir():
    # Generate Prediction
    data = prep_img(f)
    p = make_pred(data)
    y_pred.append() 
    y_true.append("Malignant")

conf_mat = confusion_matrix(y_true, y_pred)
d = ConfusionMatrixDisplay(conf_mat)
d.plot()
plt.show()
