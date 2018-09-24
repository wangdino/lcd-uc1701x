# -*- coding: utf-8 -*-

import screenplay
import uc1701x
#from PIL import Image, ImageDraw, ImageFont
#from time import gmtime, strftime

def main():
    
#'Comfortaa': ('fonts/Comfortaa-Regular.ttf', 12, 0),
#'PoiretOne': ('fonts/PoiretOne-Regular.ttf', 16, 0),
#'Rokkitt': ('fonts/Rokkitt-Regular.ttf', 14, 0),
#'UbuntuMono': ('fonts/UbuntuMono-Regular.ttf', 15, 16),
#'RobotoMono': ('fonts/RobotoMono-Regular.ttf', 16, 16),
#'Wenq': ('fonts/wqy-zenhei.ttc', 16, 0),
#'NotoSansSC': ('fonts/NotoSansSC-Regular.otf', 16, 0),
#'NotoSerifSC': ('fonts/NotoSerifSC-Regular.otf', 16, 0),
#'unifont': ('fonts/unifont-11.0.02.pil', 0, 16), # bitmap font
#'Zfull': ('fonts/Zfull-GB.ttf', 16, 16),
    
    
    en_multi = u'The quick brown\nfox jumps over\nthe lazy dog.\n1234567890'
    zh_multi = u'明月几时有\n把酒问青天\n不知天上宫阙\n今夕是何年'
    excited = '吼哇！'
    
    demo1 = u'DEMO 1/5\nLetters Numbers'
    demo2 = u'DEMO 2/5\n中文字符'
    demo3 = u'DEMO 3/5\nMonospace Text'
    demo4 = u'DEMO 4/5\nAuto Resize'
    demo5 = u'DEMO 5/5\nPicture'

    disp = screenplay.DISP()

    lcd = uc1701x.LCD()
    lcd.initialLCD()
    # fill and clear LCD test
    lcd.fillDisplay()
    lcd.clearLCD()
    # full back light ready
    lcd.fullBackLight()
    
    try:
        while True:
            lcd.displayImage(disp.txtDisp(demo1, 'Rokkitt', 30, resize=1, align=1))
            lcd.delay(1000)
            lcd.clearLCD()
            lcd.displayImage(disp.txtDisp('Comfortaa:\n'+en_multi, 'Comfortaa', resize=1))
            lcd.delay(2000)
            lcd.clearLCD()
            lcd.displayImage(disp.txtDisp('PoiretOne:\n'+en_multi, 'PoiretOne', resize=1))
            lcd.delay(2000)
            lcd.clearLCD()
            lcd.displayImage(disp.txtDisp('Rokkitt:\n'+en_multi, 'Rokkitt',  resize=1))
            lcd.delay(2000)
            lcd.clearLCD()
            lcd.displayImage(disp.txtDisp('Wenq:\n'+en_multi, 'Wenq', resize=1))
            lcd.delay(2000)
            lcd.clearLCD()
            lcd.displayImage(disp.txtDisp('NotoSansSC:\n'+en_multi, 'NotoSansSC', resize=1))
            lcd.delay(2000)
            lcd.clearLCD()
            lcd.displayImage(disp.txtDisp('NotoSerifSC:\n'+en_multi, 'NotoSerifSC', resize=1))
            lcd.delay(2000)
            lcd.clearLCD()
            lcd.displayImage(disp.txtDisp('Zfull:\n'+en_multi, 'Zfull', resize=1))
            lcd.delay(2000)
            lcd.clearLCD()
            lcd.displayImage(disp.txtDisp(demo2, 'Wenq', 30, resize=1, align=1))
            lcd.delay(1000)
            lcd.clearLCD()
            lcd.displayImage(disp.txtDisp(zh_multi, 'Wenq', resize=1))
            lcd.delay(2000)
            lcd.clearLCD()
            lcd.displayImage(disp.txtDisp(zh_multi, 'NotoSansSC', resize=1))
            lcd.delay(2000)
            lcd.clearLCD()
            lcd.displayImage(disp.txtDisp(zh_multi, 'NotoSerifSC', resize=1))
            lcd.delay(2000)
            lcd.clearLCD()
            lcd.displayImage(disp.txtDisp(zh_multi, 'Zfull', resize=1))
            lcd.delay(2000)
            lcd.clearLCD()
            lcd.displayImage(disp.txtDisp(demo3, 'Rokkitt', 30, resize=1, align=1))
            lcd.delay(1000)
            lcd.clearLCD()
            lcd.displayImage(disp.txtDisp(en_multi, 'unifont'))
            lcd.delay(2000)
            lcd.clearLCD()
            lcd.displayImage(disp.txtDisp(en_multi, 'UbuntuMono', resize=1))
            lcd.delay(2000)
            lcd.clearLCD()
            lcd.displayImage(disp.txtDisp(en_multi, 'RobotoMono', resize=1))
            lcd.delay(2000)
            lcd.clearLCD()
            lcd.displayImage(disp.txtDisp(en_multi, 'Zfull', resize=1))
            lcd.delay(2000)
            lcd.clearLCD()
            lcd.displayImage(disp.txtDisp(demo4, 'Rokkitt', 30, resize=1, align=1))
            lcd.delay(1000)
            lcd.clearLCD()
            lcd.displayImage(disp.txtDisp(excited, 'NotoSerifSC', 99, resize=1))
            lcd.delay(2000)
            lcd.clearLCD()
            lcd.displayImage(disp.txtDisp(demo5, 'Rokkitt', 30, resize=1, align=1))
            lcd.delay(1000)
            lcd.clearLCD()
            lcd.displayImage(disp.imgDisp('cat.png', align=0, resize=1, output=0))
            lcd.delay(2000)
            lcd.clearLCD()
    except KeyboardInterrupt:
        lcd.clearLCD()
        lcd.offBackLight()
        print('Demo stopped...')



if __name__ == '__main__':
    main()
