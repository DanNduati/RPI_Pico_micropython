import time, _thread, machine

def task(n,delay):
    led = machine.Pin(25,machine.Pin.OUT)
    for i in range(n):
        led.high()
        time.sleep(delay)
        led.low()
        time.sleep(delay)
    print("done")

"""Only one thread can be started/running at any one time, because there is no RTOS just a second core. The GIL is not
enabled so both core0 and core1 can run Python code concurrently, with care to use locks for shared data."""

_thread.start_new_thread(task,(10,0.5))
