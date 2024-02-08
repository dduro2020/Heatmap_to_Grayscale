# Heatmap to Grayscale Converter

This program provides a custom solution to convert a heatmap image into grayscale with the specific requirement of representing warm colors with darker shades and cool colors with lighter shades. OpenCV does not inherently provide a function to achieve this color mapping directly. Therefore, this script implements a customized transformation to achieve the desired effect, allowing the user to modify various constants to fine-tune the transformation process.
## Requirements

- Python 3.x
- OpenCV (cv2)
- NumPy
- OS
- Tempfile
- Subprocess


## Background

In standard grayscale conversion, each pixel's intensity is typically derived from a linear combination of its RGB color components. However, this approach does not always produce visually meaningful representations, especially when dealing with heatmap images where different colors represent different data ranges.

To address this limitation, this script customizes the grayscale conversion process. Warm colors (such as red) are mapped to darker shades in the grayscale output, while cool colors (such as blue) are mapped to lighter shades. This transformation enhances the visual contrast in the resulting grayscale image, making it easier to interpret and analyze the heatmap data.

## Usage

1. Make sure you have Python and the required libraries installed.
2. Place your heatmap image in the same directory as the script or provide the correct path.
3. Adjust the threshold values and transformation parameters according to your requirements.
4. Run the script.
5. The resulting grayscale image will be saved as 'imagen_resultante.png' in the current directory and automatically opened using the default image viewer.

## Customization

- `DECREASERED`: Transformation factor for decreasing white intensity in red.
- `DECREASEGREEN`: Transformation factor for decreasing white intensity in green.
- `DECREASEBLUE`: Transformation factor for decreasing white intensity in blue.

- `INCREASEBLUE`: Transformation factor for increasing white intensity in blue.
- `DECREASECIAN`: Transformation factor for increasing white intensity in cian (blue+green).
  
- `ZOOM_SIZE`: Size for zooming the image.
- `WIDE_TRANS`: Width for centering the relevant information.
- `HEIGH_TRANS`: Height for centering the relevant information.
- `PIXELS`: Size for resize image to easier processing.

## Note
  
- While OpenCV provides powerful image processing capabilities, custom solutions like this one may be necessary to achieve specific visual effects or data representations.
- Experiment with different parameter values to find the optimal transformation for your heatmap images.

By offering a customized approach to grayscale conversion, this script enhances the interpretability and visualization of heatmap data, facilitating data analysis and insights extraction.

## Example

![Imagen 1](/imgs/work_img.png) | ![Imagen 2](/imgs/result.png)
:-------------------------:|:-------------------------:
*Preprocessed* | *Processed*


