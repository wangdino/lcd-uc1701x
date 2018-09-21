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
    
    font_size = 14
    Comfortaa = ImageFont.truetype('fonts/Comfortaa-Regular.ttf', font_size)
    PoiretOne = ImageFont.truetype('fonts/PoiretOne-Regular.ttf', font_size)
    Rokkitt = ImageFont.truetype('fonts/Rokkitt-Regular.ttf', font_size)
    UbuntuMono = ImageFont.truetype('fonts/UbuntuMono-Regular.ttf', font_size)
    RobotoMono = ImageFont.truetype('fonts/RobotoMono-Regular.ttf', font_size)
    
    line1 = 'The quick brown fox jumps over the lazy dog.'
    line2 = '1234567890123456789'
    line3 = 'PoiretOne'
    line4 = 'Comfortaa'

    lcd = uc1701x.LCD()
    lcd.initialLCD()

    # fill and clear LCD test
    lcd.fillDisplay()
    lcd.clearLCD()
    lcd.fullBackLight()

    image = Image.new('1', (uc1701x.LCD_WIDTH, uc1701x.LCD_HEIGHT), 0)
    lcd.displayImage(image)
    lcd.delay(1000)
    draw = ImageDraw.Draw(image)
    draw.text((0,0), line1, font = Rokkitt, spacing = 0, fill = 255)
    draw.text((0,17), line2, font = RobotoMono, spacing = 0, fill = 255)
    draw.text((0,33), line3, font = PoiretOne, spacing = 0, fill = 255)
    draw.text((0,49), line4, font = Comfortaa, spacing = 0, fill = 255)
    lcd.setFrameBuffer(image)
    lcd.displayImage(image)
    lcd.delay(60000)
    lcd.clearLCD()
    #lcd.offBackLight()

    # keep refreshing
    try:
        while True:
            time = strftime("%H:%M:%S", gmtime())
            draw.rectangle((0, 0, image.size[0], image.size[1]), fill = 0)
            draw.rectangle((0, 0, 128, 20), fill = 255)
            draw.text((0, 0), "Zulu Time:", font = UbuntuMono, fill = 0)
            draw.text((0, 20), time, font = UbuntuMono, fill = 255)
            lcd.setFrameBuffer(image)
            lcd.displayImage(image)
    except KeyboardInterrupt:
        print('Demo stopped...')
        lcd.clearLCD()
        lcd.offBackLight()


if __name__ == '__main__':
    main()
