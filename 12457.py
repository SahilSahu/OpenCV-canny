import cv2
print(cv2.__version__)
#from matplotlib import pyplot as plt
 
def nothing(x):
    pass
 
 
img_noblur = cv2.imread('test2.jpg', 0)
img = cv2.blur(img_noblur, (2,2))
 
canny_edge = cv2.Canny(img, 100, 100)
 
cv2.imshow('image', img)
cv2.imshow('canny_edge', canny_edge)
 
cv2.createTrackbar('min_value','canny_edge',500,500,nothing)
cv2.createTrackbar('max_value','canny_edge',240,500,nothing)
 
while(1):
    cv2.imshow('image', img)
    cv2.imshow('canny_edge', canny_edge)
     
    min_value = cv2.getTrackbarPos('min_value', 'canny_edge')
    max_value = cv2.getTrackbarPos('max_value', 'canny_edge')
 
    canny_edge = cv2.Canny(img, min_value, max_value)
     
    k = cv2.waitKey(37)
    if k == 27:
        break
