# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

# Show inline image
from matplotlib.pyplot import imshow

# Test fonts - https://fonts.google.com/
# ../fonts/UbuntuMono-Regular.ttf    Bold|BoldItalic|Italic
# ../fonts/Rokkitt-Regular.ttf    Black|Bold|ExtraBold|ExtraLight|Light|Medium|SemiBold|Thin
# ../fonts/PoiretOne-Regular.ttf
# ../fonts/Comfortaa-Regular.ttf    Bold|Light

Comfortaa = '../fonts/Comfortaa-Regular.ttf'
PoiretOne = '../fonts/PoiretOne-Regular.ttf'
Rokkitt = '../fonts/Rokkitt-Regular.ttf'
UbuntuMono = '../fonts/UbuntuMono-Regular.ttf'
RobotoMono = '../fonts/RobotoMono-Regular.ttf'

ft_face = RobotoMono
ft_size = 14
ft_gen = ImageFont.truetype(ft_face, ft_size)

test_text = '''The quick brown fox jumps over the lazy dog
See if a new line is possible.
Another new line.
Yet another new line.'''
text_size = ft_gen.getsize(test_text)
text_length = len(test_text)
print(text_size, text_length, text_size[0]/text_length)

test_image = Image.new('1', (128, 64), 0)
draw = ImageDraw.Draw(test_image)
draw.multiline_text((0, 0), test_text, font = ft_gen, spacing = 0, fill = 255)

imshow(test_image)