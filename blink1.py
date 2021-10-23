from machine import Pin
import time

LED = Pin(25, Pin.OUT)
BUTTON = Pin(9, Pin.IN, Pin.PULL_UP)

def main():
    
    while(True):
        if BUTTON.value() == False:
            LED.on()
        else:
            LED.off()
            
        time.sleep_ms(100)


if __name__ == "__main__":
    main()