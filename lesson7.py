from PIL import Image

# 打开图像文件
image_path = "image.jpg"
image = Image.open(image_path)

# 获取图像信息
image_info = {
    "Size": image.size,
    "Format": image.format,
    "Mode": image.mode
}

# 打印图像信息
for key, value in image_info.items():
    print(f"{key}: {value}")

# 显示图像
image.show()
# 缩小尺寸
small_image = image.resize((int(image.width / 3), int(image.height / 3)))

# 水平和垂直镜像
horizontal_mirror = image.transpose(Image.FLIP_LEFT_RIGHT)
vertical_mirror = image.transpose(Image.FLIP_TOP_BOTTOM)

# 保存新图像
small_image.save("small_image.jpg")
horizontal_mirror.save("horizontal_mirror.jpg")
vertical_mirror.save("vertical_mirror.jpg")
from PIL import ImageFilter
import os

# 创建一个新文件夹来保存处理后的图像
if not os.path.exists("filtered_images"):
    os.mkdir("filtered_images")

# 图像文件列表
image_files = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

# 应用过滤器
for filename in image_files:
    img = Image.open(filename)

    # 例如，应用边缘增强过滤器
    filtered_img = img.filter(ImageFilter.EDGE_ENHANCE)

    # 保存处理后的图像到新文件夹
    filtered_img.save(f"filtered_images/{filename}")
from PIL import ImageDraw, ImageFont

# 打开图像
img = Image.open("image.jpg")

# 创建一个可绘制的对象
draw = ImageDraw.Draw(img)

# 设置水印文本和字体
text = "Watermark"
font = ImageFont.truetype("arial.ttf", 50)

# 添加水印到图像
draw.text((img.width - 300, img.height - 100), text, fill="white", font=font)

# 保存带有水印的图像
img.save("watermarked_image.jpg")