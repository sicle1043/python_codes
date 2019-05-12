import tesserocr
from PIL import Image
image = Image.open('E:/1sicle/python程序源码/project2_qiangke/image.png')
image = image.convert('L')
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')

pixdata = image.load()  # 8 邻域降噪
w, h = image.size
for y in range(1, h - 1):
    for x in range(1, w - 1):
        count = 0
        if pixdata[x, y - 1] > 0:
            count = count + 1
        if pixdata[x, y + 1] > 0:
            count = count + 1
        if pixdata[x - 1, y] > 0:
            count = count + 1
        if pixdata[x + 1, y] > 0:
            count = count + 1
        if pixdata[x - 1, y - 1] > 0:
            count = count + 1
        if pixdata[x - 1, y + 1] > 0:
            count = count + 1
        if pixdata[x + 1, y - 1] > 0:
            count = count + 1
        if pixdata[x + 1, y + 1] > 0:
            count = count + 1
        if count > 4:
            pixdata[x, y] = 255
image.show()
secretcode = tesserocr.image_to_text(image)
print(secretcode)
