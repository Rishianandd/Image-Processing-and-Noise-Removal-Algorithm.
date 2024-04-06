import cv2
import numpy as np
image = cv2.imread('image.jpg')
x, y = 100, 100  
DN_values = image[y, x]  
subset_image = image[y:y+8, x:x+8]
subset_image_resized = cv2.resize(subset_image, (300, 300)) 
noise_image = np.copy(subset_image)
salt_pepper = 0.01  
salt_pepper_mask = np.random.rand(8, 8)
noise_image[salt_pepper_mask < salt_pepper / 2] = 0  
noise_image[salt_pepper_mask > 1 - salt_pepper / 2] = 255  
noise_image_resized = cv2.resize(noise_image, (300, 300))  
filtered_image = cv2.medianBlur(noise_image, 3)  
filtered_image_resized = cv2.resize(filtered_image, (300, 300)) 
cv2.imshow('Subset Image with Noise', noise_image_resized)
cv2.imshow('Filtered Image', filtered_image_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
