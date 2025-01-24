# Land-Cover-Classification
Remote Sensing & Image Processing - Machine Learning
Gabriela Malec & Patrycja Majdak
---
This project demonstrates an image classification using machine learning techniques applied to a raster image. The image data is processed and classified into different categories using a Random Forest classifier.

## Description

This repository contains Python code that performs raster image classification. The classification is done using the `RandomForestClassifier` from `scikit-learn`. The project uses the `rasterio` library to read the image data, and `matplotlib` for visualization.

### Key Features:
- Read raster images with `rasterio`.
- Create training data by manually labeling different regions of the image.
  ![pobrane](https://github.com/user-attachments/assets/ad769544-ecef-42de-9e3e-7d3e25bb78e7)
- Train a Random Forest model to classify the raster image.
- Visualize the classification results.

## Requirements

To run this project, you need to have the following Python libraries installed:

- `rasterio`
- `numpy`
- `matplotlib`
- `scikit-learn`

You can install the required dependencies by running:

```bash
pip install rasterio numpy matplotlib scikit-learn
