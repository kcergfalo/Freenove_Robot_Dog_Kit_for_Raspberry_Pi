import time
from Led import *
from Buzzer import *
led=Led()
buzzer=Buzzer()

def startup_func():
        try:
            print ("\nIch versuche")
            led.theaterChase(led.strip,[0,120,0],350)

#            buzzer.run('1')
            print ("\nBeep On")

            time.sleep(1)
#            buzzer.run('0')
            print ("\nBeep Off")
            led.theaterChase(led.strip, [0,0,0])   #turn off the light

            led.colorWipe(led.strip,[0,120,0])
            
        except KeyboardInterrupt:
            led.theaterChase(led.strip, [0,0,0])   #turn off the light
            buzzer.run('0') #turn off buzzer

            print ("\nEnd of program")

# Main program logic follows:
if __name__ == '__main__':

    print ('Program is starting ... ')
    import sys
    startup_func()
