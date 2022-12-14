import urllib.request as req
import numpy as np
import cv2

url = 'http://192.168.29.65:8080/shot.jpg';
while True:
    img = req.urlopen(url)
    img_bytes = bytearray(img.read())
    img_nparr = np.array(img_bytes, dtype=np.uint8)
    frame = cv2.imdecode(img_nparr, -1) # 0 for grayscale, -1 for unchanged
    cv2.imshow('Smart Scanner', frame)
    cv2.waitKey(1)