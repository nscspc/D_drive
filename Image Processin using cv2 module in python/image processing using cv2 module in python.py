import cv2
img=cv2.imread("wood.jpeg")#imread( ) function is used to read the image file.
cv2.imshow("myimg",img)#imshow( ) function is used to show the image file.
cv2.waitKey(1000)
#waitKey( ):-
'''
this is a function used to wait for particular no. of microseconds to execute the next line of code.
if 0 is passed as argument then it will no close until we close it manually.
if 1000 is passed as argument then it will close(using destroyAllWindows( ) function) after 1000ms or uder that time we can close it manually.
'''
cv2.destroyAllWindows()#destroyAllWindows function is used to destroy the window created by the program.
'''
destroyAllWindows() simply destroys all the windows we created.
To destroy any specific window, use the function cv2. destroyWindow() where you pass the exact window name.
'''
print(img)
