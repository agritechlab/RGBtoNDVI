import tensorflow as tf
import numpy as np
import pandas as pd
import colorsys

def RGBtoNDVI(rgb):

  (h, s, v) = colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2])

  X = rgb + [h, s, v]
  X = pd.DataFrame(X).T
  model = tf.keras.saving.load_model('ANN_saved_model.h5')

  ndvi = model.predict(X)
  
  print('RGB=', np.array(rgb)*255)
  print('NDVI=', ndvi)

  return ndvi

R=int(input('R='))/255
G=int(input('G='))/255
B=int(input('B='))/255

RGB=[R,G,B]

NDVI = RGBtoNDVI(RGB)
