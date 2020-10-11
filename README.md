# Halloween project using Arduino, DFPlayer, and PIR

## Components

- [Arduino Trinket M0](https://www.adafruit.com/product/3500)
- [DFPlayer](https://www.amazon.com/gp/product/B07Y2YKYRS)
- [PIR sensor](https://www.amazon.com/gp/product/B012ZZ4LPM)
- [Speaker](https://www.amazon.com/gp/product/B0738NLFTG)
- 2 x 2 x 1.5V AA Batteries
- LEDs


## Circuit Schematic

<img src="https://github.com/ins429/halloween-arduino-pir-dfplayer/blob/master/circuit.png" width="480" height="320" />


## Photos & Videos

<img src="https://github.com/ins429/halloween-arduino-pir-dfplayer/blob/master/photo_1.jpeg" width="480" height="320" />

![video 1](https://github.com/ins429/halloween-arduino-pir-dfplayer/blob/master/video_1.mp4)

![video 2](https://github.com/ins429/halloween-arduino-pir-dfplayer/blob/master/video_2.mp4)

![video 3](https://github.com/ins429/halloween-arduino-pir-dfplayer/blob/master/video_3.mp4)


## Tips

Monitor Arduino serial port via cli.

```
$ ls /dev/tty.*

# should see a port starts with 'tty.usbmodem' e.g) /dev/tty.usbmodem142401

$ screen /dev/tty.usbmodem142401 115200
```
