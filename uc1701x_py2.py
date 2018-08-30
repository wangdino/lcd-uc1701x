#| 1701 | RPi.BCM   | BOARD |
#|======|===========|=======|
#| cs   | 2         | 3     |
#| rst  | 3         | 5     |
#| rs   | 4         | 7     |
#| sda  | 17        | 11    |
#| sck  | 27        | 13    |
#| vdd  | 3.3v      | 1     |
#| vss  | GND       | 9     |
#| LEDA | 22        | 15    |
#|======|===========|=======|

from RPi import GPIO
from PIL import Image
import time

# Display resolution
LCD_WIDTH       = 128
LCD_HEIGHT      = 64

# GPIO level
LOW, HIGH = [0, 1]


GPIO.setmode(GPIO.BCM) #GPIO.BCM or GOIO.BOARD

# Pin definition
cs      = 2
rst     = 3
rs      = 4
sda     = 17
sck     = 27
LEDA    = 22


class LCD:

    def __init__(self):
        self.cs = cs
        self.rst = rst
        self.rs = rs
        self.sda = sda
        self.sck = sck
        self.LEDA = LEDA
        self.width = LCD_WIDTH
        self.height = LCD_HEIGHT
    
    def GPIOInit(self):

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM) # GPIO.BCM or GPIO.BOARD
        GPIO.setup([cs, rst, rs,sda, sck, LEDA], GPIO.OUT)

    def delay(self, delaytime):

        time.sleep(delaytime / 1000.0)

    def setBackLight(self, brightness):
        
        pwm = GPIO.PWM(self.LEDA, 1000)
        pwm.start(brightness)

        
    def fullBackLight(self):
        
        GPIO.output(self.LEDA, HIGH)


    def offBackLight(self):
        
        GPIO.output(self.LEDA, LOW)
        
        
    def transferCommand(self, command):
        
        GPIO.output(self.cs, LOW)
        GPIO.output(self.rs, LOW)
        for i in xrange(8):
            GPIO.output(self.sck, LOW)
            if (command & 0x80): 
                GPIO.output(self.sda, HIGH)
            else: 
                GPIO.output(self.sda, LOW)
            GPIO.output(self.sck, HIGH)
            command = command << 1

            
            
    def transferData(self, data):
        
        GPIO.output(self.cs, LOW)
        GPIO.output(self.rs, HIGH)
        for i in xrange(8):
            GPIO.output(self.sck, LOW)
            if (data & 0x80): 
                GPIO.output(self.sda, HIGH)
            else: 
                GPIO.output(self.sda, LOW)
            GPIO.output(self.sck, HIGH)
            data = data << 1
            

    def transferDataBlocks(self, data_blocks):
        
        GPIO.output(self.cs, LOW)
        GPIO.output(self.rs, HIGH)
        for data in data_blocks:
            for i in xrange(8):
                GPIO.output(self.sck, LOW)
                if (data & 0x80): 
                    GPIO.output(self.sda, HIGH)
                else: 
                    GPIO.output(self.sda, LOW)
                GPIO.output(self.sck, HIGH)
                data = data << 1
            
            
    def initialLCD(self):

        self.GPIOInit()
        GPIO.output(self.cs, LOW)
        GPIO.output(self.rst, LOW)
        self.delay(100)
        GPIO.output(self.rst, HIGH)
        self.delay(20)
        self.transferCommand(0xe2)
        self.transferCommand(0x40)
        self.transferCommand(0xa0)
        self.transferCommand(0xc8)
        self.transferCommand(0xa2)
        self.transferCommand(0x2c)
        self.transferCommand(0x2e)
        self.transferCommand(0x2f)
        self.transferCommand(0xf8)
        self.transferCommand(0x00)
        self.transferCommand(0x23)
        self.transferCommand(0x81)
        self.transferCommand(0x28)
        self.transferCommand(0xac)
        self.transferCommand(0x00)
        self.transferCommand(0xa6)
        self.transferCommand(0xaf)
        self.delay(100)
        self.transferCommand(0xa5)
        self.delay(200)
        self.transferCommand(0xa4)
        GPIO.output(self.cs, HIGH)

        
    def setLCDAddress(self, col, line):

        GPIO.output(self.cs, LOW)
        self.transferCommand(0xb0 + line)
        self.transferCommand(((col & 0x0f) >>4) + 0x10)
        self.transferCommand(col & 0x0f)

            
    def clearLCD(self):
        
        for i in xrange(9):
            self.setLCDAddress(0, i)
            for j in xrange(132):
                self.transferData(0x00)
        self.setLCDAddress(0, 0)
        

    def fillDisplay(self):

        for i in xrange(8):
            self.setLCDAddress(0, i)
            for j in xrange(128):
                self.transferData(0xff)
        self.setLCDAddress(0, 0)
    
    def setFrameBuffer(self, image):

        buf = [0x00] * (self.width * self.height / 8)
        image_monocolor = image.convert('1')
        imwidth, imheight = image_monocolor.size
        if imwidth != self.width or imheight != self.height:
            raise ValueError('Image must be same dimensions as display \
                ({0} x {1}).' .format(self.width, self.height))

        pixels = image_monocolor.load()
        for i in xrange(0, self.height / 8):
            for j in xrange(self.width):
                for k in xrange(8):
                    if pixels[j, i * 8 + k] != 0:
                        buf[i * self.width + j] |= 0x80 >> (7 - k)
        return buf

    def displayImage(self, image):

        data = self.setFrameBuffer(image)
        for i in xrange(8):
            self.setLCDAddress(0, i)
            for j in xrange(128):
                self.transferData(data[i * 128 + j])
        self.setLCDAddress(0, 0)

### EOF ###
