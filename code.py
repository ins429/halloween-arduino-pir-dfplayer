import board
import digitalio
import time
import microcontroller
from DFPlayer import DFPlayer

dfplayer = DFPlayer()

builtin_led = digitalio.DigitalInOut(board.D13)
builtin_led.direction = digitalio.Direction.OUTPUT

led = digitalio.DigitalInOut(board.D2)
led.direction = digitalio.Direction.OUTPUT

pir = digitalio.DigitalInOut(board.D0)
pir.direction = digitalio.Direction.INPUT

dfplayer.stop()

dfplayer.set_volume(20)

reset_counter = 0

print('\n******\nStart!\n******\n')

while True:
    builtin_led.value = True
    time.sleep(0.5)
    builtin_led.value = False
    time.sleep(0.5)

    reset_counter = reset_counter + 1
    if reset_counter > 100:
      print('reset: count due')
      microcontroller.reset()

    pir_value = pir.value

    # 513 - busy, 512 - idle
    if dfplayer.get_status() == 512:
        led.value = False

    if dfplayer.get_status() == None:
        print('reset: dfplayer no response')
        microcontroller.reset()

    if pir_value:
        if dfplayer.get_status() == 512:
            dfplayer.random()
            dfplayer.stop()
            dfplayer.play()
            led.value = True
            reset_counter = 0
