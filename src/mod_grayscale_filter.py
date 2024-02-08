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
def optimize_grayscale_transform(heatmap):
    # separate color channels
    b = heatmap[:,:,0]
    g = heatmap[:,:,1]
    r = heatmap[:,:,2]
    
    # masks for pixels with b > g
    mask = b > g
    
    # blue lighter than green scale
    gray1 = np.where(mask, b * INCREASEBLUE - g * DECREASECIAN, 0) # smoothe texture
    
    # normal grayscale
    gray2 = DECREASERED * r + DECREASEGREEN * g + DECREASEBLUE * b
    
    # Combine both gray values based on the mask
    grayscale_transformed = gray1 + np.where(mask, 0, gray2)
    
    # uint8 range
    grayscale_transformed = np.clip(grayscale_transformed, 0, 255).astype(np.uint8)
    
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
result = optimize_grayscale_transform(resized_zoom)

cv2.imwrite('imagen_resultante.png', result)
subprocess.run(['xdg-open', 'imagen_resultante.png'])

