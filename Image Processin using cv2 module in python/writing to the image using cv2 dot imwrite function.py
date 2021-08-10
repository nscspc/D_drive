import cv2
#from os import system
img=cv2.imread("D:\Image Processin using cv2 module in python\wood.jpeg")
cv2.imshow("myimg",img)
cv2.waitKey(0)
cv2.imwrite("copy.png",img)
cv2.imwrite("copy2.jpg",img)
cv2.destroyAllWindows()
print(img)
#system("cls")
