# -*- coding: utf-8 -*-

import uc1701x
from PIL import Image, ImageDraw, ImageFont
from time import gmtime, strftime

def main():
    
    # Test fonts - https://fonts.google.com/
    # ../fonts/UbuntuMono-Regular.ttf    Bold|BoldItalic|Italic
    # ../fonts/Rokkitt-Regular.ttf    Black|Bold|ExtraBold|ExtraLight|Light|Medium|SemiBold|Thin
    # ../fonts/PoiretOne-Regular.ttf
    # ../fonts/Comfortaa-Regular.ttf    Bold|Light
    font_size_reg = 16 # Height about 19-21px
    font_size_xl = 32 # Height about 40px
    
    Comfortaa = ImageFont.truetype('fonts/Comfortaa-Regular.ttf', 12)
    PoiretOne = ImageFont.truetype('fonts/PoiretOne-Regular.ttf', 16)
    Rokkitt = ImageFont.truetype('fonts/Rokkitt-Regular.ttf', 14)
    UbuntuMono = ImageFont.truetype('fonts/UbuntuMono-Regular.ttf', 15) # 16 char per line
    RobotoMono = ImageFont.truetype('fonts/RobotoMono-Regular.ttf', 14) # 16 char per line

    Wenq = ImageFont.truetype('fonts/wqy-zenhei.ttc', font_size_reg)
    NotoSansSC = ImageFont.truetype('fonts/NotoSansSC-Regular.otf', font_size_reg)
    NotoSerifSC = ImageFont.truetype('fonts/NotoSerifSC-Regular.otf', font_size_xl)
    
    line1 = 'The quick brown fox jumps over the lazy dog.'
    line2 = '1234567890123456789'
    line3 = 'PoiretOne'
    line4 = 'Comfortaa'
    line_SC = '这是坠吼的！'
    line_SC_XL = '吼哇！'

    lcd = uc1701x.LCD()
    lcd.initialLCD()

    # fill and clear LCD test
    lcd.fillDisplay()
    lcd.clearLCD()
    lcd.fullBackLight()

    image = Image.new('1', (uc1701x.LCD_WIDTH, uc1701x.LCD_HEIGHT), 0)
    lcd.displayImage(image)
    lcd.delay(100)
    draw = ImageDraw.Draw(image)
    draw.text((0,0), line1, font = Rokkitt, spacing = 0, fill = 255)
    draw.text((0,17), line2, font = RobotoMono, spacing = 0, fill = 255)
    draw.text((0,33), line3, font = PoiretOne, spacing = 0, fill = 255)
    draw.text((0,49), line4, font = Comfortaa, spacing = 0, fill = 255)
    lcd.setFrameBuffer(image)
    lcd.displayImage(image)
    lcd.delay(5000)
    lcd.clearLCD()
    image = Image.new('1', (uc1701x.LCD_WIDTH, uc1701x.LCD_HEIGHT), 0)
    lcd.displayImage(image)
    draw = ImageDraw.Draw(image)
    draw.text((16, 12), line_SC_XL, font = NotoSerifSC, spacing = 0, fill = 255)
    lcd.setFrameBuffer(image)
    lcd.displayImage(image)
    lcd.delay(10000)
    lcd.clearLCD()

    # keep refreshing
    try:
        while True:
            time = strftime("%H:%M:%S", gmtime())
            draw.rectangle((0, 0, image.size[0], image.size[1]), fill = 0)
            draw.rectangle((0, 0, 128, 16), fill = 255)
            draw.text((0, 0), "Zulu Time:", font = UbuntuMono, fill = 0)
            draw.text((0, 17), time, font = UbuntuMono, fill = 255)
            draw.rectangle((0, 33, 128, 48), fill = 255)
            draw.text((0, 33), 'RobotoMono12345678901234567890', font = RobotoMono, spacing = 0, fill = 0)
            draw.text((0, 49), 'UbuntuMono12345678901234567890', font = UbuntuMono, spacing = 0, fill = 255)
            lcd.setFrameBuffer(image)
            lcd.displayImage(image)
    except KeyboardInterrupt:
        print('Demo stopped...')
        image = Image.new('1', (uc1701x.LCD_WIDTH, uc1701x.LCD_HEIGHT), 0)
        lcd.displayImage(image)
        lcd.offBackLight()


if __name__ == '__main__':
    main()
