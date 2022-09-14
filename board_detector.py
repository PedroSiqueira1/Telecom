import cv2

# path
path = r'C:\Users\T-Gamer\Documents\Faculdade\Telecom\Images\test_board3.png'

# Using cv2.imread() method
img = cv2.imread(path)

# Converting image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# Applying GaussianBlur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Applying Canny Edge detection
canny = cv2.Canny(blur, 50, 150)

# Finding contours

contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Finding the biggest contour
biggest = None
max_area = 0
for i in contours:
        area = cv2.contourArea(i)
        if area > 100:
                peri = cv2.arcLength(i,True)
                approx = cv2.approxPolyDP(i,0.02*peri,True)
                if area > max_area and len(approx)==4:
                        biggest = approx
                        max_area = area

#cv2.imshow('Pre Contorno', img)
#cv2.waitKey()
# Draw the biggest contour
cv2.drawContours(img, [biggest], -1, (0,255,0), 3)

# Displaying the image
#cv2.imshow('image', img)
#cv2.imshow('gray', gray)
#cv2.imshow('blur', blur)
cv2.imwrite('te.png', img)
cv2.imshow('\Images\test4.png', img)
cv2.waitKey()