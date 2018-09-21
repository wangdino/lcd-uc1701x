# Prerequisites

Project is based on Python3 (3.5 tested)
```
sudo apt-get install python3 python3-dev python3-spidev python3-pip python3-rpi.gpio
pip3 install pillow
```

BCM2835 library is required
```
# download the latest version of the library, say bcm2835-1.xx.tar.gz, then:
tar zxvf bcm2835-1.xx.tar.gz
cd bcm2835-1.xx
./configure
make
sudo make check
sudo make install
```

Enable SPI interface (Advanced Options)
```
sudo raspi-config
```

# Wiring

Pins can be adapted to every user's need but the following pins can be all connected by a 5x2 Dupont connector.
Colors are totally optional.

| Pin 1701 | Description | RPi BCM Pin | RPi Board Pin | Color |
| :---: | :---: | :---: | :---: | :---: |
| 01 | ROM_IN | N/C | N/C | N/C |
| 02 | ROM_OUT | N/C | N/C | N/C |
| 03 | ROM_SCK | N/C | N/C | N/C |
| 04 | ROM_CS | N/C | N/C | N/C |
| 05 | LEDA* | 22 | 15 | GY |
| 06 | VSS/GND | GND | 20 | BK |
| 07 | VDD/PWR | 3.3V | 17 | RD |
| 08 | SCLK | 11 | 23 | VT |
| 09 | SDA | 10 | 19 | BU |
| 10 | RS | 23 | 16 | GN |
| 11 | RESET | 24 | 18 | YE |
| 12 | CS | 25 | 22 | OG |

* The backlight (LEDA) can share connection with VDD/PWR - same voltage either 3.3V or 5.0V.
