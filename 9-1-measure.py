import RPi.GPIO as GPIO
import time
import datetime
import numpy as np


leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comparator = 4 
troykaVoltage = 17

bits = len(dac)
levels = 2 ** bits
dV = 3.3 / levels

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds + dac, GPIO.OUT)
GPIO.setup(troykaVoltage, GPIO.OUT)
GPIO.setup(comparator, GPIO.IN)

def num2pins(pins, value):
    GPIO.output(pins, [int(i) for i in bin(value)[2:].zfill(bits)])

def adc2():

    timeout = 0.001
    value = 128
    delta = 128

    for i in range(8):
        num2pins(dac, value)
        time.sleep(timeout)

        direction = -1 if (GPIO.input(comparator) == 0) else 1
        num = delta * direction / 2
        value = int(value + num)
        delta = delta / 2

    return value

try:
    
    now = datetime.datetime.now()
    DATE = now.strftime("%d.%m.%Y-%H:%M:%S")
  
    t = 20
    measure = []
    value = 0
    
    start = time.time()

    GPIO.output(troykaVoltage, 1)

    while time.time() - start <= t:
        value = adc2()
        measure.append(value)

    delta = round(t / int(len(measure)), 3)
    
    np.savetxt('/home/pi/Desktop/marina/9-blood/{}_{}.txt'.format(DATE, delta), measure, fmt='%d')
    print('Done! Files already saved!')

finally:
    
    GPIO.cleanup()
    print('GPIO cleanup completed.')