# -*- coding: UTF-8 -*-
from PIL import Image, ImageDraw, ImageGrab
import os

# 获取屏幕的宽度和高度
screen_width, screen_height = ImageGrab.grab().size

# 计算正方形色块的尺寸（5 cm x 5 cm，但不超过屏幕面积的25%）
target_size = min(screen_width * 0.25, screen_height * 0.25, 5 * 37.7952756)  # 1 cm = 37.7952756 pixels
square_size = int(target_size)

# 计算正方形色块的位置（屏幕中心）
x = (screen_width - square_size) // 2
y = (screen_height - square_size) // 2

# 指定保存路径
save_folder = "gamma_patch"

# 如果文件夹不存在，则创建文件夹
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# 生成全红、全绿、全蓝色块，驱动值从0到255，步长为8
for value in range(0, 256, 8):
    # 创建全红、全绿、全蓝色块
    red_image = Image.new('RGB', (square_size, square_size), color=(value, 0, 0))
    green_image = Image.new('RGB', (square_size, square_size), color=(0, value, 0))
    blue_image = Image.new('RGB', (square_size, square_size), color=(0, 0, value))

    # 创建一个黑色背景图像
    black_background = Image.new('RGB', (screen_width, screen_height), color='black')

    # 将正方形色块粘贴到黑色背景图像上，居中显示
    black_background.paste(red_image, (x, y))
    black_background.save(os.path.join(save_folder, f"red_{value}.png"))

    black_background.paste(green_image, (x, y))
    black_background.save(os.path.join(save_folder, f"green_{value}.png"))

    black_background.paste(blue_image, (x, y))
    black_background.save(os.path.join(save_folder, f"blue_{value}.png"))

# 保存全红、全绿、全蓝色块，驱动值为255
red_image = Image.new('RGB', (square_size, square_size), color=(255, 0, 0))
green_image = Image.new('RGB', (square_size, square_size), color=(0, 255, 0))
blue_image = Image.new('RGB', (square_size, square_size), color=(0, 0, 255))

black_background.paste(red_image, (x, y))
black_background.save(os.path.join(save_folder, "red_255.png"))

black_background.paste(green_image, (x, y))
black_background.save(os.path.join(save_folder, "green_255.png"))

black_background.paste(blue_image, (x, y))
black_background.save(os.path.join(save_folder, "blue_255.png"))

# 显示保存成功的消息
print(f"Images saved successfully in the folder '{save_folder}'.")


