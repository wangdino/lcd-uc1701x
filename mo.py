# -*- coding: utf-8 -*-

import screenplay
import uc1701x
#from PIL import Image

def main():
    
    MAX_FRAME = 360
    
    disp = screenplay.DISP()
    lcd = uc1701x.LCD()
    lcd.initialLCD()
    lcd.clearLCD()
    lcd.fullBackLight()
    
    try:
        while True:
            for i in range(MAX_FRAME):
                filename = 'pic/{0:03}.png'.format(i+1)
                canvas = disp.imgDisp(filename, align=0, resize=0, output=0)
                lcd.setFrameBuffer(canvas)
                lcd.displayImage(canvas)
                lcd.delay()
    except KeyboardInterrupt:
        lcd.clearLCD()
        lcd.offBackLight()
        print('+1s...')

if __name__ == '__main__':
    main()

## Prep converting TXT files to PNG files
#for i in range(MAX_FRAME):
#    filename = 'pic/{0:03}.txt'.format(i+1)
#    with open(filename, 'r') as fh:
#        text = fh.read()
#        canvas = disp.txtDisp(text, 'UbuntuMono', 15, align=0, resize=1, output=0)
#        canvas.save('pic/{0:03}.png'.format(i+1), 'PNG')

## Handle prepared PNG files and send to LCD
