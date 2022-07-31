from machine import Pin
import utime
import _thread


led1 = Pin(25,Pin.OUT)
led2 = Pin(15,Pin.OUT)

sLock = _thread.allocate_lock()

def core_task():
    while 1:
        # Acquire the semaphore lock
        sLock.acquire()
        print("Entered into the second thread")
        utime.sleep(1)
        led2.high()
        print("Led2 turned on")
        utime.sleep(2)
        led2.low()
        print("Led 2 turned off")
        utime.sleep(1)
        print("Exitting the second thread")
        utime.sleep(1)
        sLock.release()
_thread.start_new_thread(core_task,())
while True:
    # Acquire the semaphore lock
    sLock.acquire()
    print("Entered into the main thread")
    led1.toggle()
    utime.sleep(0.15)
    print("Led 1 started to toggle")
    utime.sleep(1)
    print("Exiting from the main thread")
    utime.sleep(1)
    # Release the semaphore lock
    sLock.release()
