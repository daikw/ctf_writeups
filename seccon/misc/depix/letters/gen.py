import cv2
import numpy as np

def depix(letter):
    img = np.full((100, 85, 3), (255,255,255), dtype=np.uint8)
    cv2.putText(img, letter, (0, 80), cv2.FONT_HERSHEY_PLAIN, 8, (0, 0, 0), 5, cv2.LINE_AA)

    cv2.putText(img, "P", (0, 90), cv2.FONT_HERSHEY_PLAIN, 7, (0, 0, 0), 5, cv2.LINE_AA)
    cv2.putText(img, "I", (0, 90), cv2.FONT_HERSHEY_PLAIN, 8, (0, 0, 0), 5, cv2.LINE_AA)
    cv2.putText(img, "X", (0, 90), cv2.FONT_HERSHEY_PLAIN, 9, (0, 0, 0), 5, cv2.LINE_AA)
    simg = cv2.resize(img, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_NEAREST) # WTF :-o
    img = cv2.resize(simg, img.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

    cv2.imwrite(f"{letter}.png", img)

alphabets = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
symbols = '.{}-_'
letters = alphabets + alphabets.upper() + numbers + symbols

for letter in letters:
    depix(letter)

