import cv2

img = cv2.imread('./auto.jpg', cv2.IMREAD_GRAYSCALE)

if img is None:
    raise FileNotFoundError("Image not found.")

equalized_img = cv2.equalizeHist(img)

resized_img = cv2.resize(equalized_img, (800, 600))
cv2.imshow("Histogram Equalized Image", resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
