# -*- coding: utf-8 -*-

import screenplay
from PIL import Image
try:
    import matplotlib.pyplot as plt
except:
    pass

disp = screenplay.DISP()

# Available test fonts:
#'Comfortaa': ('fonts/Comfortaa-Regular.ttf', 12, 0),
#'PoiretOne': ('fonts/PoiretOne-Regular.ttf', 16, 0),
#'Rokkitt': ('fonts/Rokkitt-Regular.ttf', 14, 0),
#'UbuntuMono': ('fonts/UbuntuMono-Regular.ttf', 15, 16),
#'RobotoMono': ('fonts/RobotoMono-Regular.ttf', 16, 16),
#'Wenq': ('fonts/wqy-zenhei.ttc', 16, 0),
#'NotoSansSC': ('fonts/NotoSansSC-Regular.otf', 16, 0),
#'NotoSerifSC': ('fonts/NotoSerifSC-Regular.otf', 16, 0),
#'unifont': ('fonts/unifont-11.0.02.pil', 0, 16), # bitmap font
#'Zfull': ('fonts/Zfull-GB.ttf', 16, 0),

line1 = u'这是坠吼的！'
line2 = u'吼哇！'
num = '123456789012345678901234567890'
en = 'The quick brown fox jumps over the lazy dog.'
multi = num + '\n' + en
img_path = 'test.png'

canvas = disp.txtDisp(line2, 'Wenq', 'xxxl', 8, 0)
#canvas = disp.imgDisp(img_path, 0, 0)

try:
    plt.imshow(canvas)
except:
    pass

#canvas.save('test_output.png', 'PNG')