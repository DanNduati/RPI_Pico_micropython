from machine import Pin,Timer

led = Pin(25,Pin.OUT)
tim = Timer()

def tick(timer):
    global led
    led.toggle()

tim.init(period=1000,mode=Timer.PERIODIC,callback=tick)
