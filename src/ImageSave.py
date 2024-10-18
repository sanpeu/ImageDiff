import pyautogui
from PIL import ImageChops

# https://malang.xelf.io/land/spotdifference

# 이미지 시작 (204, 137)
# 비교 (968, 137)

# 이미지 크기
# width 751
# height 625

width, height = 751, 624
y_pos = 137

src = pyautogui.screenshot(region=(204, y_pos, width, height))
src.save('./image/src.jpg')

dest = pyautogui.screenshot(region=(968, y_pos, width, height))
dest.save('./image/dest.jpg')