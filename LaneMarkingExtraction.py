import cv2
import numpy as np
import os
# Load image
image = cv2.imread("highway.png")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define color ranges (HSV values)
yellow_lower = np.array([15, 80, 80])   # Lower bound for yellow color on the hsv color wheel
yellow_upper = np.array([32, 255, 255]) # Upper bound for yellow color on the hsv color wheel

white_lower = np.array([0, 0, 200])     # Lower bound for white color on the hsv color wheel
white_upper = np.array([255, 30, 255])  # Upper bound for white color on the hsv color wheel

# Create masks
yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
white_mask = cv2.inRange(hsv, white_lower, white_upper)

# Apply masks on original image
yellow_lane = cv2.bitwise_and(image, image, mask=yellow_mask)
white_lane = cv2.bitwise_and(image, image, mask=white_mask)

# Show results
cv2.imwrite("YellowLane.png",yellow_lane)
cv2.imwrite("WhiteLane.png",white_lane)



cv2.waitKey(0)
cv2.destroyAllWindows()
