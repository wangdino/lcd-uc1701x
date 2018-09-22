# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

# Show inline image
from matplotlib.pyplot import imshow

# Test fonts - https://fonts.google.com/
# ../fonts/UbuntuMono-Regular.ttf    Bold|BoldItalic|Italic
# ../fonts/Rokkitt-Regular.ttf    Black|Bold|ExtraBold|ExtraLight|Light|Medium|SemiBold|Thin
# ../fonts/PoiretOne-Regular.ttf
# ../fonts/Comfortaa-Regular.ttf    Bold|Light

font_size_reg = 16 # Height about 19-21px
font_size_xl = 32 # Height about 40px

Wenq = ImageFont.truetype('../fonts/wqy-zenhei.ttc', font_size_reg)
NotoSansSC = ImageFont.truetype('../fonts/NotoSansSC-Regular.otf', font_size_reg)
NotoSerifSC = ImageFont.truetype('../fonts/NotoSerifSC-Regular.otf', font_size_xl)
unifont = ImageFont.load('../fonts/unifont-11.0.02.pil')
Wenq9 = ImageFont.load('../fonts/wenquanyi_9pt.pil')

line_SC = '这是坠吼的！'
line_SC_XL = '吼哇！'
line_num = '123456789012345678901234567890'
line_EN = 'The quick brown fox jumps over the lazy dog.'

#print('Wenq: ', Wenq.getsize(line_SC))
#print('NotoSansSC: ', NotoSansSC.getsize(line_SC))
#print('NotoSerifSC: ', NotoSerifSC.getsize(line_SC_XL))
print(Wenq9.getsize(line_num))
print(unifont.getsize(line_num))

test_image = Image.new('1', (128, 64), 0)
draw = ImageDraw.Draw(test_image)
#draw.text((0, 0), line_SC, font = Wenq, spacing = 0, fill = 255)
#draw.text((0, 20), line_SC, font = NotoSansSC, spacing = 0, fill = 255)
#draw.text((0, 41), line_SC, font = NotoSerifSC, spacing = 0, fill = 255)
#draw.text((16, 12), line_SC_XL, font = NotoSerifSC, spacing = 0, fill = 255)

#draw.text((0,0), line_num, font = unifont, fill = 255)
#draw.text((0,17), line_num, font = unifont, fill = 255)
#draw.text((0,33), line_num, font = unifont, fill = 255)
#draw.text((0,49), line_num, font = unifont, fill = 255)

draw.text((0,0), line_EN, font = unifont, fill = 255)
draw.text((0,17), line_EN, font = unifont, fill = 255)
draw.text((0,33), line_EN, font = unifont, fill = 255)
draw.text((0,49), line_EN, font = unifont, fill = 255)

#draw.text((0,0), line_num, font = Wenq9, fill = 255)
#draw.text((0,17), line_num, font = Wenq9, fill = 255)
#draw.text((0,33), line_num, font = Wenq9, fill = 255)
#draw.text((0,49), line_num, font = Wenq9, fill = 255)

#draw.text((0,0), line_EN, font = Wenq9, fill = 255)
#draw.text((0,17), line_EN, font = Wenq9, fill = 255)
#draw.text((0,33), line_EN, font = Wenq9, fill = 255)
#draw.text((0,49), line_EN, font = Wenq9, fill = 255)


imshow(test_image)