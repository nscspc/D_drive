import cv2
img=cv2.imread("copy.png")
cv2.imshow("colourful(original) image",img)
cv2.waitKey(0)
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#cvt=convert
cv2.imshow("gray-scale(black and white) image",gray_img)
cv2.waitKey(0)

#another way to convert the image in grayscale:-
img2=cv2.imread("copy.png",0)
cv2.imshow("gray-scale(black and white) image 2",img2)
cv2.waitKey(0)


