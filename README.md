# An open-source application for predicting NDVI from RGB calibrated images
The shallow neural network (SNN) model to predict NDVI from sRGB is loaded in the GitHub repository in the format “.h5” and will be accompanied by a Python demonstration function of its use which take the input from user (3 integer values from 0 to 255, corresponding to R-red, G-green and B-blue). These input data are converted to H (hue), S (saturation) and V (value) and all the six values (R, G, B, H, S, V) are collected in a data frame to be the input of the SNN model.


# RGBtoNDVI.py contains:

- Import of required libraries;
- Function (RGBtoNDVI) for ANN_saved_model.h5 application;
- Example of input take from user (R, G, B) and result prediction (NDVI).


# Model descriptors:

- Number of samples:	4100
- Number of hidden layers:	1
- Number of neurons:	200
- % Training set:	75
- % Test set:	25
- r Training:	0.93
- r Test:	0.91


# Required libraries:

- TensorFlow
- Numpy
- Pandas
- colorsys

# Authors

Lavinia Moscovini, Luciano Ortenzi, Federico Pallottino, Simone Figorilli, Simona Violino, Catello Pane, Valerio Capparella, Simone Vasta, Corrado Costa
