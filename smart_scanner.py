import urllib.request as req
import numpy as np
import cv2
from PIL import Image
import time

url = 'http://192.168.29.65:8080/shot.jpg';
while True:
    img = req.urlopen(url)
    img_bytes = bytearray(img.read())
    img_nparr = np.array(img_bytes, dtype=np.uint8)
    frame = cv2.imdecode(img_nparr, -1) # 0 for grayscale, -1 for unchanged
    frame_cvt = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_blur = cv2.GaussianBlur(frame_cvt, (5,5), 0)
    frame_edge = cv2.Canny(frame_blur, 30, 50)
    cv2.imshow('Smart Scanner', frame_edge)
    contours, h = cv2.findContours(frame_edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    if cv2.waitKey(1) == ord('s'):
        img_pil = Image.fromarray(frame)
        time_str = time.strftime('%Y-%m-%d-%H-%M-%S')
        img_pil.save(f'{time_str}.pdf') 
        print(time_str)