import cv2
import numpy as np
import os
import tempfile
import subprocess



DECREASERED = 0.05
DECREASEGREEN = 0.2
DECREASEBLUE = 0.75

INCREASEBLUE = 1.05
DECREASECIAN = 0.1 

ZOOM_SIZE = 750
WIDE_TRANS = 650
HEIGH_TRANS = 350

PIXELS = 50

# Grayscale on heatmap
def heatmap_to_grayscale(heatmap):
    grayscale_transformed = np.zeros_like(heatmap, dtype=np.uint8)
    for i in range(heatmap.shape[0]):
        for j in range(heatmap.shape[1]):
            b, g, r = heatmap[i, j]
            if b > g:
                gray = b * INCREASEBLUE - g * DECREASECIAN # smoothe texture
            else:
                gray = DECREASERED * r + DECREASEGREEN * g + DECREASEBLUE * b
            grayscale_transformed[i,j] = gray
    
    return grayscale_transformed

# Center image to process relevant info
def resize_img(img):
    img = img[HEIGH_TRANS:HEIGH_TRANS+ZOOM_SIZE, WIDE_TRANS:WIDE_TRANS+ZOOM_SIZE]
    
    return img

# Open image in 'current_directory'
def init():
    print("OpenCV version:", cv2.__version__)

    current_dir = os.getcwd()
    path = (str(current_dir) + '/data/flux_2024-01-22T140613-00Z.png')

    print("Image to process:", path)
    return path



img = cv2.imread(init())

zoom_img = resize_img(img)
resized_zoom = cv2.resize(zoom_img, (PIXELS,PIXELS))
result = heatmap_to_grayscale(resized_zoom)

cv2.imwrite('imagen_resultante.png', result)
subprocess.run(['xdg-open', 'imagen_resultante.png'])

