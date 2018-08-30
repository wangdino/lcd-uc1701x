#!/usr/bin/python
import uc1701x
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from time import gmtime, strftime

def main():
    
    lcd = uc1701x.LCD()
    lcd.initialLCD()

    # fill and clear LCD test
    lcd.fillDisplay()
    lcd.clearLCD()

    # display UTC time
    image = Image.new('1', (uc1701x.LCD_WIDTH, uc1701x.LCD_HEIGHT), 0)
    lcd.displayImage(image)
    lcd.delay(1000)
    draw = ImageDraw.Draw(image)
    font_time = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 18)

    # keep refreshing
    while True:
        time = strftime("%H:%M:%S", gmtime())
        draw.rectangle((0, 0, image.size[0], image.size[1]), fill = 0)
        draw.rectangle((0, 0, 128, 20), fill = 255)
        draw.text((5, 3), "UTC", font = font_time, fill = 0)
        draw.text((5, 25), time, font = font_time, fill = 255)
        datas = lcd.setFrameBuffer(image)
        lcd.displayImage(image)


if __name__ == '__main__':
    main()
