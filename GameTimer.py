import cv2
import numpy as np

display = 200 * np.ones([400, 400, 3], dtype=np.uint8)

cv2.imshow("", display)
cv2.waitKey(0)