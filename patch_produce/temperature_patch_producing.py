# -*- coding: UTF-8 -*-
from PIL import Image, ImageDraw
import os

# 获取屏幕的宽度和高度
screen_width = 1920  # 举例：屏幕宽度为1920像素
screen_height = 1080  # 举例：屏幕高度为1080像素

# 计算每个色块的尺寸
block_size = screen_width // 32

# 指定保存路径
save_folder = "temperature_patch"

# 如果文件夹不存在，则创建文件夹
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# 生成32张图片，每张图片是一个完整屏幕大小的R=G=B色块
for value in range(0, 256, 8):
    # 创建R=G=B色块
    rgb_image = Image.new('RGB', (screen_width, screen_height), color=(value, value, value))

    # 保存图片
    image_path = os.path.join(save_folder, f"rgb_{value}.png")
    rgb_image.save(image_path)

    # 显示保存成功的消息
    print(f"Image saved successfully: {image_path}")

# 最后一个色块的值为255
rgb_image = Image.new('RGB', (screen_width, screen_height), color=(255, 255, 255))
image_path = os.path.join(save_folder, "rgb_255.png")
rgb_image.save(image_path)
print(f"Image saved successfully: {image_path}")
