import os
import cv2

base_dir = 'data'
target_size = (64, 64)

for label in os.listdir(base_dir):
    class_dir = os.path.join(base_dir, label)
    if not os.path.isdir(class_dir):
        continue
    for img_name in os.listdir(class_dir):
        img_path = os.path.join(class_dir, img_name)
        img = cv2.imread(img_path)
        if img is None:
            continue
        resized = cv2.resize(img, target_size)
        cv2.imwrite(img_path, resized)
