import sys
import os
import glob
import numpy as np
from math import sqrt,sin,cos,radians,pi
from scipy.ndimage import geometric_transform
import glymur


def equirectangularToOrthographic(output_coords):
    radius = 1600;
    imageWidth = 4096
    imageWidthHalved = imageWidth >> 1

    longitude = pi * (output_coords[1] - imageWidthHalved) / imageWidth ;
    latitude = pi * (output_coords[0] - imageWidthHalved) / imageWidth;

    resultX = imageWidthHalved + radius * cos(latitude) * sin(longitude);
    resultY = imageWidthHalved + radius * sin(latitude);
  
    return (resultY, resultX);


outdir ="./out/"
if not os.path.exists(outdir):
    os.makedirs(outdir)

for file in glob.glob("*.jp2"):
    sourceImage = glymur.Jp2k(file)[:]
    transformedImage = geometric_transform(sourceImage, equirectangularToOrthographic)
    savedJP2 = glymur.Jp2k(outdir + file, data=transformedImage, colorspace='gray')

