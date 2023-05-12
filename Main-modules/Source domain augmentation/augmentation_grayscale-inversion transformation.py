import os
import cv2

# Define input and output directories
input_dir = r"G:\data\cbis-ddsm\chen_dong_selectdata\ddsm\cbis_train_test\train\image_512_sum"
output_dir = r"G:\data\cbis-ddsm\chen_dong_selectdata\ddsm\cbis_train_test\train\image_512_trans_sum"

# Loop through all files in input directory
for filename in os.listdir(input_dir):
    # Check if file is an image
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Read image
        img = cv2.imread(os.path.join(input_dir, filename))
        # Convert image to grayscale
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Invert grayscale image
        inverted_img = 255 - gray_img
        # Write inverted image to output directory
        cv2.imwrite(os.path.join(output_dir, filename), inverted_img)