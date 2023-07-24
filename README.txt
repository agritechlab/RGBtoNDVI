The RGBtoNDVI function allows you to predict the NDVI (Normalized Difference Vegetation Index) from the RGB values. The input data are 3 integer values (0 to 255) corresponding to R (red), G (green) and B (blue). The input is scaled from 0 to 1 and converted to the values H (hue), S (saturation) and V (value). The six values (R, G, B, H, S, V) form the input data frame of the ANN model.


RGBtoNDVI.py contains:

import of required libraries;
function (RGBtoNDVI) for ANN_saved_model.h5 application;
example of input take from user (R, G, B) and result prediction (NDVI).


Model descriptors:

Number of samples:	4100
Number of hidden layers:	1
Number of neurons:	200
% Training set:	75
% Test set:	25
r Training:	0.93
r Test:	0.91


Required libraries:

TensorFlow
Numpy
Pandas
colorsys
