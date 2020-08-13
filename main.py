import cv2, numpy as np

img = cv2.imread("Resources/lena.png", 0)
"""
for x in range(512):
    for y in range(512):
        img[x][y][1]= 256 - x%256
        img[x][y][0]=  y%256
     # 1 chan, grayscale!
"""

imf = np.float32(img)/255.0  # float conversion/scale
dst = cv2.dft(imf,flags = cv2.DFT_COMPLEX_OUTPUT)         # the dct
img2 = np.uint8(dst)*255.0    # convert back

inv = cv2.idft(dst) 
img3 = np.uint8(inv)*255.0

cv2.imshow("Image",img)
cv2.imshow("Fourrier",img2)
cv2.imshow("Iversa Fourrier",img3)

cv2.waitKey(0)
