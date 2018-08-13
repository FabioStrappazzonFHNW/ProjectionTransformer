# Projection Transformer
This program was created as part of the bachelor's thesis by Sandro Schwager and Fabio Strappazzon.

## Usage
This script transforms orthographic projections of spheres into equirectangular projections. It is meant to be used with images from api.helioviewer.org.

Copy this script to a directory containing JPEG 2000 images and start it with  
`python3 ProjectionTransformer.py`  
The transformed images will be placed in the out subdirectory.



## Dependencies
* python3
* numpy
* scipy
* Glymur
  * OpenJpeg (needs to be accessible accessible from PATH)
  
## Notes
numpy, scipy and Glymur can be installed via PIP.  
On Windows Glymur seems to require the 32 bit version of OpenJpeg.  
This script assumes 4096x4096 images. The radius uf the sphere is assumed to be 1600 Pixel. Note that there may be small variations in radius in the images from helioviewer.org.