<h1 align="center"> RPI Pico Playground </h1>

Messing around with the pico

## <b> Installing Micropython on the Pi Pico </b>
### Drag and Drop Micropython
1. Download the Micropython UF2 file for the board [here](https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2)
2. Push and hold the BOOTSEL button and plug your Pico into the USB port of your Raspberry Pi or other computer. Release the BOOTSEL button after your Pico is connected.
3. It will mount as a Mass Storage Device called RPI-RP2.
4. Drag and drop the MicroPython UF2 file onto the RPI-RP2 volume. Your Pico will reboot. You are now running MicroPython
5. You can access the REPL via USB Serial

## <b>Connecting via USB </b>
The MicroPython firmware is equipped with a virtual USB serial port which is accessed through the micro USB
connector on Raspberry Pi Pico. Your computer should notice this serial port and list it as a character device, most likely
`/dev/ttyACM0`.

### Install a serial terminal emulator
I use `picocom`:
```bash
$ sudo apt install picocom
```
Open the serial port as:
```bash
$ picocom /dev/ttyACM0
```



## Resources
1. [Documentation](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
2. [Raspberry Pi Pico Python SDK](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf)
