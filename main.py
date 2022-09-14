from microbit import *
import utime


ok = False
while True:
    msg = str(temperature()) + "\n"
    msg2 = str(display.read_light_level()) + "\n"
    msg3 = str(microphone.sound_level()) + "\n"
    uart.write(msg)
    uart.write(msg2)
    uart.write(msg3)
    #print(msg)
    #print(msg2)
    #print(msg3)
    utime.sleep(2)
    
    if int(msg3) > 40:
        while ok == False:
            audio.play(Sound.GIGGLE)
            if button_a.is_pressed():
                ok = True
        ok = False
        