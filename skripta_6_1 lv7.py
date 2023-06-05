from tensorflow.keras.preprocessing import image_dataset_from_directory
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix

from tensorflow.keras.preprocessing import image_dataset_from_directory
# ucitavanje podataka iz odredenog direktorija
train_ds = image_dataset_from_directory(
 directory='C:\\Users\\student\\Desktop\\PSU\\PSU LV7\\Test',
 labels='inferred',
 label_mode='categorical',
 batch_size=32,
 image_size=(48, 48, 3))


train_ds = image_dataset_from_directory (directory='PSU_LV7/Train/',labels='inferred',label_mode='categorical',batch_size= 32, image_size=(48, 48))
test_ds = image_dataset_from_directory (directory='PSU_LV7/Test/',labels='inferred',label_mode='categorical',batch_size= 32, image_size=(48, 48))
# Model / data parameters

# train i test podaci
train_ds = keras.datasets.mnist.load_data()



# TODO: kreiraj model pomocu keras.Sequential(); prikazi njegovu strukturu pomocu .summary()
model = keras.Sequential()
model.add(layers.Input(shape=(48, 48, 3 )))
model.add(layers.Dense(32, activation="relu"))
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(43, activation="softmax"))

model.summary()


# TODO: definiraj karakteristike procesa ucenja pomocu .compile()
model.compile(loss="categorical_crossentropy",
optimizer = "adam",
metrics = ["accuracy",] )


# TODO: provedi ucenje mreze
batch_size = 32
epochs = 5
history = model.fit(train_ds, batch_size = batch_size, epochs = epochs, validation_split=0.1)


# TODO: Prikazi test accuracy i matricu zabune
score = model.evaluate(test_ds, verbose=0)
print("Test loss", score[0])
print("Test accuracy:", score[1])

predicted_classes = np.argmax(model.predict(test_ds), axis = -1)
conf_matrix = confusion_matrix(test_ds, predicted_classes)
print(conf_matrix)


# TODO: spremi model
model.save("FCN/")

