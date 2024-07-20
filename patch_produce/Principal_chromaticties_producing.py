# -*- coding: UTF-8 -*-
from PIL import Image, ImageDraw, ImageGrab
import os

# 获取屏幕的宽度和高度
screen_width, screen_height = ImageGrab.grab().size

# 创建一个全红色块
red_image = Image.new('RGB', (screen_width, screen_height), color='red')

# 创建一个全绿色块
green_image = Image.new('RGB', (screen_width, screen_height), color='green')

# 创建一个全蓝色块
blue_image = Image.new('RGB', (screen_width, screen_height), color='blue')

# 指定保存路径
save_path = "principal_chromaticities_patch"

# 如果保存路径不存在，则创建文件夹
if not os.path.exists(save_path):
    os.makedirs(save_path)

# 保存全红色块
red_image.save(os.path.join(save_path, 'red_patch.png'))

# 保存全绿色块
green_image.save(os.path.join(save_path, 'green_patch.png'))

# 保存全蓝色块
blue_image.save(os.path.join(save_path, 'blue_patch.png'))

# 显示保存成功的消息
print("Images saved successfully in the folder 'principal_chromaticities_patch'.")
