import cv2
import numpy as np

alphabets = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
symbols = '.{}-_'
letters = alphabets + alphabets.upper() + numbers + symbols

letter_imgs = {letter: cv2.imread(f"letters/{letter}.png") for letter in letters}

output = cv2.imread("output.png")
w = 85

flag = ''
for i in range(31):
    flgi_img = output[:, i*w:(i+1)*w]
    print(i*w, (i+1)*w)
    for letter, letter_img in letter_imgs.items():
        diff = np.sum(np.abs(flgi_img - letter_img))
        if diff < 0.1:
            flag = flag + letter

print(flag)

