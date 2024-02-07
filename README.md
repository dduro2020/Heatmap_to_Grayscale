# Heatmap to Grayscale Converter

This program converts a heatmap image into grayscale with customized transformations. It includes features like resizing the image to focus on relevant information and applying thresholds for color transformation.

## Requirements

- Python 3.x
- OpenCV (cv2)
- NumPy
- OS
- Tempfile
- Subprocess

## Usage

1. Make sure you have Python and the required libraries installed.
2. Place your heatmap image in the same directory as the script or provide the correct path.
3. Adjust the threshold values and transformation parameters according to your requirements.
4. Run the script.
5. The resulting grayscale image will be saved as 'imagen_resultante.png' in the current directory and automatically opened using the default image viewer.

## Customization

- `GREEN_THRESHOLD`: Threshold value for green color.
- `RED_THRESHOLD`: Threshold value for red color.
- `DECREASE2GREY`: Transformation factor for decreasing intensity.
- `INCREASE2GREY`: Transformation factor for increasing intensity.
- `ZOOM_SIZE`: Size for zooming the image.
- `WIDE_TRANS`: Width for centering the relevant information.
- `HEIGH_TRANS`: Height for centering the relevant information.

