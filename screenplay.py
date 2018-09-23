# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont


dimension = (128, 64)
#mode = 'mono'

# fontface value tuple (font path, default font size, char per line for mono)
# Test fonts - https://fonts.google.com/
fontfaces = {
'Comfortaa': ('fonts/Comfortaa-Regular.ttf', 12, 0),
'PoiretOne': ('fonts/PoiretOne-Regular.ttf', 16, 0),
'Rokkitt': ('fonts/Rokkitt-Regular.ttf', 14, 0),
'UbuntuMono': ('fonts/UbuntuMono-Regular.ttf', 15, 16),
'RobotoMono': ('fonts/RobotoMono-Regular.ttf', 16, 16),
'Wenq': ('fonts/wqy-zenhei.ttc', 16, 0),
'NotoSansSC': ('fonts/NotoSansSC-Regular.otf', 16, 0),
'NotoSerifSC': ('fonts/NotoSerifSC-Regular.otf', 16, 0),
'unifont': ('fonts/unifont-11.0.02.pil', 0, 16), # bitmap font
'Zfull': ('fonts/Zfull-GB.ttf', 16, 16),
}

fontsizes = {
'reg' :  12,
'l'   :  16,
'xl'  :  20,
'xxl' :  24,
'xxxl':  28,
'max' :  32,
}

class DISP:
    
    def __init__(self):
        self.dim_x = dimension[0]
        self.dim_y = dimension[1]
    
    def txtDisp(self, lines, fontface = None, fontsize = None, align = 0, output = 0):
        # font path handle; fontface can be text or none
        try:
            path = fontfaces[fontface][0]
        except:
            fontface = 'Wenq'
            path = fontfaces[fontface][0]
        # font size handle; fontsize input can be integer or text or none
        if fontsize == None:
            size = fontfaces[fontface][1]
        try:
            size = int(fontsize)
        except (ValueError, TypeError) as e:
            try:
                size = fontsizes[fontsize]
            except KeyError:
                size = fontsizes['reg']
        # generate font handle
        if fontfaces[fontface][1] != 0:
            fonthandle = ImageFont.truetype(path, size)
        else:
            fonthandle = ImageFont.load(path)
        
        # get text overall size
        lines_x, lines_y = fonthandle.getsize(lines)
        
        # alignment handle
        x, y, validity = self.objAlign(lines_x, lines_y, align)

        canvas = Image.new('1', (self.dim_x, self.dim_y), 0)
        disp = ImageDraw.Draw(canvas)

        if validity == 0:
            print('Aborted...')
            return canvas
        
        disp.text((x, y), lines, font = fonthandle, fill = 255, spacing = 0)
        # output: 0 - return image, 1 - LCD screen
        if output == 1:
            self.output(canvas)
        else:
            return canvas
    
    def output(self, canvas):
        import uc1701x
        lcd = uc1701x.LCD()
        lcd.initialLCD()
        lcd.fullBackLight()
        lcd.clearLCD()
        lcd.setFrameBuffer(canvas)
        lcd.displayImage(canvas)
        lcd.delay(5000)
        lcd.clearLCD()
        lcd.offBackLight
        
    def objAlign(self, obj_x, obj_y, align):
        # align method
        # 0   1   2
        # 3   4   5
        # 6   7   8
        dx = self.dim_x - obj_x
        dy = self.dim_y - obj_y
        if dx < 0 or dy < 0:
            print('Object oversize: %d x %d \nScreen size: %d x %d' %(obj_x, obj_y, self.dim_x, self.dim_y))
            return 0, 0, 0
        try:
            if int(align) in range(9):
                align = int(align)
        except:
            align = 0
        alignmap = {
        0 : (0, 0),
        1 : (dx / 2, 0),
        2 : (dx, 0),
        3 : (0, dy / 2),
        4 : (dx / 2, dy / 2),
        5 : (dx, dy / 2),
        6 : (0, dy),
        7 : (dx / 2, dy),
        8 : (dx, dy),
        }
        x, y = alignmap[align]
        return x, y, 1
            
### EOF ###