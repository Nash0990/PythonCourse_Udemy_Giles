import numpy as np
import cv2

def av_pix(img,circles,size):
    av_value = []
    for coords in circles[0,:]:
        col = np.mean(img[coords[1]-size:coords[1]+size,coords[0]-size:coords[0]+size])
        #print(col)
        av_value.append(col)
    return av_value


def get_raidus(circles):
    # Get radius from the HoughCircles function output of circle coordinated detected.
    radius = []
    for coords in circles[0,:]:
        radius.append(coords[2])
    return radius


img = cv2.imread('capstone_coins.png',cv2.IMREAD_GRAYSCALE)
original_image = cv2.imread('capstone_coins.png',1)
img = cv2.GaussianBlur(img, (5,5), 0)


circles  = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT, 0.9, 120, param1=50, param2=27, minRadius=60, maxRadius=120)


print(circles)

circles = np.uint16(np.around(circles))
count = 1

for i in circles[0,:]:
    
    #draw the outer circle
    cv2.circle(original_image,(i[0],i[1]),i[2],(0,255,0),2)
    #draw the centre of the circle
    cv2.circle(original_image,(i[0],i[1]),2,(0,0,255),3)
    #cv2.putText(original_image,str(count),(i[0],i[1]),cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,0),2)
    count += 1    

radii = get_raidus(circles)
print(radii)
bright_values=av_pix(img,circles,20)
print(bright_values)


values = []

for a,b in zip(bright_values,radii):
    if a > 150 and b > 110:
        values.append(10)
    elif a > 150 and b < 110:
        values.append(5)
    elif a < 150 and b > 110:
        values.append(2)
    elif a < 150 and b < 110:
        values.append(1)
print(values)


count_2 = 0
for i in circles[0,:]:
    cv2.putText(original_image, str(values[count_2]) + 'p',(i[0],i[1]),cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0),2)
    count_2 += 1
cv2.putText(original_image, 'ESTIMATED TOTAL VALUE: ' + str(sum(values)) + 'p', (200,100), cv2.FONT_HERSHEY_SIMPLEX, 1.3, 255)

#imgGrey = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY), thrash = cv2.threshold(imgGray, 240, 255, cv2.THRESH_BINARY), contours = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

imgGrey = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
_, thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour,True),True)
    cv2.drawContours(original_image, [approx], 0, (0,0,0),5)
    x = approx.ravel()[0] 
    y = approx.ravel()[1]
    if len(approx) == 7:
        cv2.putText(original_image, 'Heptagon', cv2.FONT_HERSHEY_SIMPLEX, 1.3, 255)

cv2.imshow('Detected Coins',original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()