
# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.python.framework import ops
# from tensorflow.python.framework import dtypes
# import os

from keras_preprocessing.image import ImageDataGenerator
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Flatten
import numpy as np
# # Dataset Parameters - CHANGE HERE
# MODE = 'file' # or 'file', if you choose a plain text file (see above).
# DATASET_PATH = 'data_catalog.txt' # the dataset file or root folder path.

# # Image Parameters
# N_CLASSES = 3 # CHANGE HERE, total number of classes
# IMG_HEIGHT = 64 # CHANGE HERE, the image height to be resized to
# IMG_WIDTH = 64 # CHANGE HERE, the image width to be resized to
# CHANNELS = 1 # The 3 color channels, change to 1 if grayscale

# batch_size = 5


# train = tf.keras.preprocessing.image_dataset_from_directory(
#     'dataset',
#     labels = 'inferred',
#     label_mode = "int",
#     color_mode = "grayscale",
#     batch_size = batch_size,
#     image_size = (IMG_HEIGHT,IMG_WIDTH),
#     shuffle = True,    
# )

# print(train.shape)

print("train_dir")
training_dir = 'training'
image_size = (200, 200)

train_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=.2,
        zoom_range=.2,
        rotation_range = 40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        )
validation_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=.2,
        rotation_range = 40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        )

train_generator = train_datagen.flow_from_directory(
        training_dir,
        target_size = image_size,
        subset="training",
        batch_size=32,
        class_mode='categorical',
        seed=42,shuffle=True)

validation_generator = validation_datagen.flow_from_directory(
        training_dir,
        target_size=image_size,
        batch_size=32,
        class_mode='categorical',
        subset="validation",
        seed=42)
print("test_dir")
test_dir = 'testing'

test_datagen = ImageDataGenerator(rescale=1./255,zoom_range=.2,
        rotation_range = 40,
        width_shift_range=0.2,
        height_shift_range=0.2)
test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(200, 200),
        classes=['test'],
        class_mode='categorical',
        shuffle=False)