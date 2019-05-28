#!/usr/bin/env python
# encoding: utf-8

"""
@description: image & doc

@author: baoqiang
@time: 2019-05-25 22:36
"""

from sty import fg
from PIL import Image, ImageFilter

"""
excel: openpyxl
word: python-docx
pdf: pypdf2
"""

colors = {
    'White': (255, 255, 255),
    'Red': (255, 0, 0),
    'Green': (0, 255, 0),
    'Blue': (0, 0, 255),
    'Gray': (128, 128, 128),
    'Yellow': (255, 255, 0),
    'Black': (0, 0, 0),
    'Purple': (128, 0, 128),
}


def print_color():
    for color, rgb in colors.items():
        r, g, b = rgb
        src = '{}{}{}'.format(fg(r, g, b), color, fg.rs)

        print(src)


img_file = 'guido.jpg'
img_file2 = 'new_guido.jpg'


def c1_open_image():
    image = Image.open(img_file)

    print(image.format, image.size, image.mode)

    image.show()


def c2_cut_image():
    image = Image.open(img_file)

    rect = 80, 20, 310, 360

    image.crop(rect).show()


def c3_thumb_image():
    image = Image.open(img_file)

    size = 128, 128

    image.thumbnail(size)

    image.show()


def c4_paste_image():
    image1 = Image.open(img_file)
    image2 = Image.open(img_file2)

    rect = 80, 20, 310, 360
    head = image2.crop(rect)
    width, height = head.size

    # past it
    image1.paste(head.resize((int(width * 1.5), int(height * 1.5))), (172, 40))

    image1.show()


def c5_rotate_image():
    image = Image.open(img_file)

    image.show()

    # image.rotate(180).show()

    # 左右反转
    image.transpose(Image.FLIP_LEFT_RIGHT).show()

    # 上下反转
    # image.transpose(Image.FLIP_TOP_BOTTOM).show()


def c6_pixel_image():
    image = Image.open(img_file)

    for x in range(88, 310):
        for y in range(20, 360):
            image.putpixel((x, y), (128, 128, 128))

    image.show()


# 滤镜
def c7_filter_image():
    image = Image.open(img_file)

    image.filter(ImageFilter.CONTOUR).show()


if __name__ == '__main__':
    # print_color()
    # c1_open_image()
    # c2_cut_image()
    # c3_thumb_image()
    # c4_paste_image()
    # c5_rotate_image()
    # c6_pixel_image()
    c7_filter_image()
