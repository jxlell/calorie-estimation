import cv2
import numpy as np
import os
import json

folder_path = "MyFood Dataset/val_ann"


all_objects = []

for filename in os.listdir(folder_path):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        mask = cv2.imread(os.path.join(folder_path, filename), cv2.IMREAD_GRAYSCALE)

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) > 0:
            largest_contour = max(contours, key=cv2.contourArea)

            epsilon = 0.01 * cv2.arcLength(largest_contour, True)
            approx = cv2.approxPolyDP(largest_contour, epsilon, True)

            vertices = approx.squeeze().tolist()


            image_object = {
                "filename": filename,
                "vertices": vertices,
                "class": filename.split("_")[0]
            }

            all_objects.append(image_object)
            print("processed " + filename)

with open("myfood_region_validation.json", "w") as f:
    json.dump(all_objects, f)


food_classes = ["rice", "beans", "boiled egg", "fried egg", "pasta", "salad", "roasted meat", "apple", "chicken breast"]
