# Land-Cover-Classification

Remote Sensing & Image Processing - Machine Learning Project <br>
Gabriela Malec & Patrycja Majdak

---

This project demonstrates an image classification using machine learning techniques applied to a raster image. The image data is processed and classified into different categories using a Random Forest classifier.

## Description

This repository contains Python code that performs raster image classification. The classification is done using the `RandomForestClassifier` from `scikit-learn`. The project uses the `rasterio` library to read the image data, and `matplotlib` for visualization.

### Key Features:
- Read raster images with `rasterio`.
- Create training data by manually labeling different regions of the image. <br>
  ![pobrane](https://github.com/user-attachments/assets/ad769544-ecef-42de-9e3e-7d3e25bb78e7) <br>
  In this project, we manually defined the training fields by labeling specific regions of the image. We labeled three regions as follows: <br>

    Class 1 (Buildings): Region (1100:1200, 1100:1200) <br>
    Class 2 (Crops): Region (700:800, 900:1000) <br>
    Class 3 (Forest): Region (600:700, 50:150) <br>
    
  ![trainig_fields_display](https://github.com/user-attachments/assets/92f23d6b-6f89-43cb-b425-0bb05e4b9e50)  
- Train a Random Forest model to classify the raster image. <br>
  ![8df39724-977b-409d-8598-7950b8264008](https://github.com/user-attachments/assets/08b6bf02-19c7-4361-a10d-80c863c1750f)
  ![409e529e-0a96-4e58-845f-81aa1f588c94](https://github.com/user-attachments/assets/f1022590-b464-43bc-be5a-9b1c6c5deedd) <br>
  We checked the accuracy and improved it by providing more precise square areas for labeling. Initially, the accuracy was 0.756, but after refining the labeled areas, the accuracy increased to 0.839.
- Visualize the classification results. <br>
  ![pobrane (1)](https://github.com/user-attachments/assets/3800da35-ee8c-46ac-823d-d07f307d7fc9)

