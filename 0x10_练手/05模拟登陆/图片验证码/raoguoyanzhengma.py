import pytesseract
from PIL import Image

def convert(img,threshold):
    #用于对图片进行灰度处理和二值化
    img = img.convert('L')#对图片进行灰度处理
    pixels = img.load()
    for x in range(img.width):#对图片进行二值化
        for y in range(img.height):
            if pixels[x,y] > threshold:
                pixels[x,y] = 255
            else:
                pixels[x,y] = 0
    return img

def deaden(img):
    #用于对图片进行降噪处理
    data = img.getdata()#返回sequence对象，每一个元素对应一个像素点的RGB值
    weight, height = img.size#返回图片的宽度和高度
    count = 0
    for x in range(1, height - 1):
        for y in range(1, height - 1):
            mid_pixel = data[weight * y + x]#找到中心元素对应的RGB
            if mid_pixel == 0:
                #获取中心元素各个方向像素的RGB
                top_pixel = data[weight * (y - 1) + x]
                left_pixel = data[weight * y + (x - 1)]
                right_pixel = data[weight * y + (x + 1)]
                bottom_pixel = data[weight * (y + 1) + x]

                if top_pixel == 0:
                    count += 1
                if left_pixel == 0:
                    count += 1
                if right_pixel == 0:
                    count += 1
                if bottom_pixel == 0:
                    count += 1
                if count > 4:
                    img.putpixel((x, y), 0)#如果中心元素周围像素都是黑色，则将中心元素也设置为黑色
    return img

image = Image.open('验证码/5.jpg')
image = convert(image,150)
image = deaden(image)
result = pytesseract.image_to_string(image)#用tesseract把图片转变成文字
print(result)

