import cv2
import numpy as np

#read image
img = cv2.imread('xxx.jpg', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('origin',img)

#SIFT
sift= cv2.xfeatures2d.SIFT_create()
keypoints = sift.detect(gray, None)

#kp, des = sift.detectAndCompute(gray,None)  #des是描述子，for match， should use des, bf = cv2.BFMatcher();smatches = bf.knnMatch(des1,des2, k=2
cv2.drawKeypoints(gray, keypoints, img)
cv2.imshow('testSift', img)

cv2.imwrite('sift_keypoints.jpg',img)

#使用SURF
img = cv2.imread("xxx.jpg")
img = cv2.resize(img,(136 * 3,76 * 3))

surf = cv2.xfeatures2d.SURF_create()
keypoints, descriptor = surf.detectAndCompute(gray,None)

cv2.drawKeypoints(image = img,
                  outImage = img,
                  keypoints = keypoints,
                  flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
                  color = (51,163,236))
cv2.imshow("SURF",img)

cv2.waitKey(0)
cv2.destroyAllWindows()