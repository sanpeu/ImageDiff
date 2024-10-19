import os, time
import pyautogui
from PIL import ImageChops

# https://malang.xelf.io/land/spotdifference

# 이미지 시작 (204, 137)
# 비교 (968, 137)

# 이미지 크기
# width 751
# height 625

width, height = 751, 624
x_pos = 204
y_pos = 137

src = pyautogui.screenshot(region=(204, y_pos, width, height))
dest = pyautogui.screenshot(region=(968, y_pos, width, height))

src.save('./image/src.jpg')
dest.save('./image/dest.jpg')

diff = ImageChops.difference(src, dest)
diff.save('./image/diff.jpg')

while not os.path.exists('./image/diff.jpg'):
    time.sleep(1)

# 이미지 전처리, 윤곽선 추출
import cv2
src_img = cv2.imread('./image/src.jpg')
dest_img = cv2.imread('./image/dest.jpg')
diff_img = cv2.imread('./image/diff.jpg')

gray = cv2.cvtColor(diff_img, cv2.COLOR_BGR2GRAY) # gray로 바꾸기
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# edges = cv2.Canny(blurred, 50, 150)
# cv2.imshow('edges', edges)
contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

COLOR = (0, 200, 0)

for cnt in contours:
    if cv2.contourArea(cnt) > 70:
        x, y, width, height = cv2.boundingRect(cnt)
        cv2.rectangle(src_img, (x, y), (x + width, y + height), COLOR, 2)
        cv2.rectangle(dest_img, (x, y), (x + width, y + height), COLOR, 2)
        cv2.rectangle(diff_img, (x, y), (x + width, y + height), COLOR, 2)

        to_x = x + width // 2 + x_pos # 이미지 시작 위치와 컴퓨터에서 보이는 위치 조절
        to_y = y + height // 2 + y_pos
        pyautogui.moveTo(to_x, to_y, duration=0.5)
        # pyautogui.click()

cv2.imshow('src', src_img)
cv2.imshow('dest', dest_img)
cv2.imshow('diff', diff_img)
cv2.waitKey(0)
cv2.destroyAllWindows()