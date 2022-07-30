<h1 align="center"> RPI Pico Playground </h1>

Messing around with the RPI pico.
[![asciicast](https://asciinema.org/a/leMMPhqLBcWTbaajszcaMxutw.svg)](https://asciinema.org/a/leMMPhqLBcWTbaajszcaMxutw)
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
Quit the program with `C-a-q`(Ctrl+a+q) assuming that `C-a` is the escape character.

## <b>Ampy</b>
Utility to interact with a CircuitPython or MicroPython board over a serial connection.

### Installation
```bash
$ pip install adafruit-ampy
```
### Usage
1. List the files on the board
```bash
$ ampy --port /dev/ttyACM0 ls
```
2. Put a file on the board
```bash
$ ampy --port /dev/ttyACM0 put main.py
```
3. Remove a file from the board.
```bash
$ ampy --port /dev/ttyACM0 rm main.py
```
4. Run a script on the board
```bash
$ ampy --port /dev/ttyACM0 run main.py
```
### Configuration
For convenience you can set `AMPY_PORT` and `AMPY_BAUD` environment variables which will be used f the port parameter is not specified.
To set these variables automatically each time you run `ampy`, copy them into a file named `.ampy`:
```.ampy
AMPY_PORT=/dev/ttyACM0
AMPY_BAUD=115200
```
Put this `.ampy` file to your project's directory and you can now run `ampy` within this directory without having to specify this parameters

```bash
$ ampy run main.py
```

### Example usage
1. Create the `hello_world.py` file and add whatever:
```python
while 1:
    print("Hello world!")
```
2. Put the file on the RPI Pico
We put our `hello_world.py` file to the board as `main.py` so that it autoruns. Think of `main.py` as the `entrypoint module` run by the Pico on reset/reboot:
```bash
$ ampy put hello_world.py main.py
```
3. List the files on the pico
```bash
$ ampy ls
/main.py
```
4. Open up the boards serial port and do a soft reset/reboot with `C-d`(Ctrl+d) and the code will autorun!:
```
$ picocom /dev/ttyACM0
picocom v2.2

port is        : /dev/ttyACM0
flowcontrol    : none
baudrate is    : 9600
parity is      : none
databits are   : 8
stopbits are   : 1
escape is      : C-a
local echo is  : no
noinit is      : no
noreset is     : no
nolock is      : no
send_cmd is    : sz -vv
receive_cmd is : rz -vv -E
imap is        : 
omap is        : 
emap is        : crcrlf,delbs,

Type [C-a] [C-h] to see available commands

Terminal ready

>>> 
Hello Micropython!
Hello Micropython!
Hello Micropython!
Hello Micropython!
Hello Micropython!
Hello Micropython!
Hello Micropython!
Hello Micropython!
Hello Micropython!
Traceback (most recent call last):
  File "main.py", line 2, in <module>
KeyboardInterrupt: 
MicroPython v1.19.1 on 2022-06-18; Raspberry Pi Pico with RP2040
Type "help()" for more information.
>>> 
```
Quit picocom with `C-a-q`(Ctrl+a+q)

## Resources
1. [Documentation](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
2. [Raspberry Pi Pico Python SDK](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf)
3. [Ampy](https://pypi.org/project/adafruit-ampy/)

## License
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=for-the-badge)](LICENSE)

Copyright 2022 Daniel Chege Nduati
