# import cv2 # computer vision library
# from .helpers import load_dataset # helper functions

# import random
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg # for loading in images


# # Image data directories
# IMAGE_DIR_TRAINING = "traffic_light_images/training/"
# IMAGE_DIR_TEST = "traffic_light_images/test/"


# # Using the load_dataset function in helpers.py
# # Load training data
# IMAGE_LIST = load_dataset(IMAGE_DIR_TRAINING)



# # This function should take in an RGB image and return a new, standardized version
# def standardize_input(image):

#     ## TODO: Resize image and pre-process so that all "standard" images are the same size
#     standard_im = np.copy(image)
#     standard_im = cv2.resize(standard_im, (32,32))

#     return standard_im



# ## TODO: One hot encode an image label
# ## Given a label - "red", "green", or "yellow" - return a one-hot encoded label

# # Examples:
# # one_hot_encode("red") should return: [1, 0, 0]
# # one_hot_encode("yellow") should return: [0, 1, 0]
# # one_hot_encode("green") should return: [0, 0, 1]

# def one_hot_encode(label):

#     ## TODO: Create a one-hot encoded label that works for all classes of traffic lights
#     one_hot_encoded = [0, 0, 0]

#     if label == 'red':
#         one_hot_encoded[0] = 1
#     if label == 'yellow':
#         one_hot_encoded[1] = 1
#     if label == 'green':
#         one_hot_encoded[2] = 1

#     return one_hot_encoded


# def standardize(image_list):

#     # Empty image data array
#     standard_list = []

#     # Iterate through all the image-label pairs
#     for item in image_list:
#         image = item[0]
#         label = item[1]

#         # Standardize the image
#         standardized_im = standardize_input(image)

#         # One-hot encode the label
#         one_hot_label = one_hot_encode(label)

#         # Append the image, and it's one hot encoded label to the full, processed list of image data
#         standard_list.append((standardized_im, one_hot_label))

#     return standard_list

# # Standardize all training images
# STANDARDIZED_LIST = standardize(IMAGE_LIST)


# def avg_brightness(rgb_image):
#     # Convert image to HSV
#     hsv = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)

#     # Add up all the pixel values in the V channel
#     sum_brightness = np.sum(hsv[:,:,2])
#     area = 32*32.0  # pixels

#     # find the avg
#     avg = sum_brightness/area

#     return avg


# ## TODO: Create a brightness feature that takes in an RGB image and outputs a feature vector and/or value
# ## This feature should use HSV colorspace values
# def create_feature(rgb_image):

#     ## TODO: Convert image to HSV color space
#     hsv = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)

#     #Red light mask
#     cropped_img = np.copy(hsv)[:,5:26,:]
#     low_red = np.array([150, 40, 40])
#     upp_red = np.array([180, 255, 255])
#     mask_red = cv2.inRange(cropped_img, low_red, upp_red)
#     cropped_img[mask_red==0] = 0
#     red_brightness = np.sum(cropped_img[:, :, 2])

#     #green light mask
#     cropped_img = np.copy(hsv)[:,5:26,:]
#     low_green = np.array([70, 40, 40])
#     upp_green = np.array([100, 255, 255])
#     mask_green = cv2.inRange(cropped_img, low_green, upp_green)
#     cropped_img[mask_green==0] = 0
#     green_brightness = np.sum(cropped_img[:, :, 2])

#     #yellow light mask
#     cropped_img = np.copy(hsv)[:,5:26,:]
#     low_yellow = np.array([10, 10, 150])
#     upp_yellow = np.array([35, 255, 255])
#     mask_yellow = cv2.inRange(cropped_img, low_yellow, upp_yellow)
#     cropped_img[mask_yellow==0] = 0
#     yellow_brightness = np.sum(cropped_img[:, :, 2])

#     ## TODO: Create and return a feature value and/or vector
#     feature = [red_brightness, yellow_brightness, green_brightness]


#     return feature


# # This function should take in RGB image input
# # Analyze that image using your feature creation code and output a one-hot encoded label
# def estimate_label(rgb_image):
#     pred_color = ''
#     predicted_label = [0, 0, 0]
#     ## TODO: Extract feature(s) from the RGB image and use those features to
#     ## classify the image and output a one-hot encoded label
#     features = create_feature(rgb_image)
#     index = np.argmax(features)
#     predicted_label[index] = 1

#     if index==0:
# 	       pred_color = 'red'
#     elif index==1:
# 	       pred_color = 'yellow'
#     else:
# 	       pred_color = 'green'

#     return predicted_label, pred_color
