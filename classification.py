import rasterio
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

image_path = "IMG_PNEO4_202206190946390_MS-FS_ORT_8dd7caa4828d4a86ca26f8ce88f2fb4f_NED_R1C1.TIF"
with rasterio.open(image_path) as src:
    img = src.read()
    profile = src.profile

img_rgb = np.transpose(img, (1, 2, 0))

labels = np.zeros((img_rgb.shape[0], img_rgb.shape[1]), dtype=int)

labels[1100:1200, 1100:1200] = 1
labels[700:800, 900:1000] = 2
labels[600:700, 50:150] = 3

plt.imshow(labels, cmap='tab10')
plt.title("Training fields")
plt.colorbar()
plt.show()

X = img_rgb.reshape(-1, 3)
y = labels.flatten()

mask = y > 0
X_train, X_test, y_train, y_test = train_test_split(X[mask], y[mask], test_size=0.3, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

predicted_labels = clf.predict(X).reshape(img_rgb.shape[:2])

plt.imshow(predicted_labels, cmap='tab10')
plt.title("Result of classification")
plt.colorbar()
plt.show()
