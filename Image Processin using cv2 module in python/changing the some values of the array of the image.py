import cv2
img=cv2.imread("copy.png")
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img)
img=img*2
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img)
#there is change in the image after changing the array values of the image.
