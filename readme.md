## lcd_screen

Files relating to the operation of the LCD screen connected over GPIO via the arduino bridge.
The goal is to make a sensible set of tools to present text on the display in useful and interesting ways for use in other projects, or the system.

See Issues on github for todos etc.

## Installation:

For development on a different machine, it may be useful to create a virtualenv - it allows you to keep project packages (e.g. rpi.gpio) separate from host system Python installation.

Set up a virtualenv for this project:

	virtualenv -p python2.7 lcd_screen --no-site-packages

This will create a new virtual environment, including places for local libraries. The virtualenv is activated by sourcing the file 'activate' in bin:

	. bin/activate

Deactivate thusly:

	deactivate

Create a folder for the code, e.g. src, then clone (shown below).

	git clone git@github.com:Steven-Eardley/lcd_screen.git src

From the source folder created above, use the virtualenv's pip installer to download the dependencies specified in setup.py

	pip install -e .

**Note, lcd_screen may only be executed on a the raspberry pi, due to the GPIO requirements.** These instructions are useful for developing in an IDE, however.

## On the pi:

### (TODO: Instructions for setting up GPIO and SPI)

May as well use the main python environment - use the above pip command without a virtualenv to install the dependencies if they're not already there.

Currently the useful code is in screenController.py. You can have a play with the working functionality in by running

	sudo python test_screen.py

Running scripts with GPIO access requires sudo access.

## Class references

### ScreenController.py

This controls the screen. Current callable methods are:

	lcd_init()
This clears the LCD screen.

	println1()
This prints up to 16 characters to the top line of the LCD.

	println2()
This prints up to 16 characters to the bottom line of the LCD.

### Buffer.py

This contains different kinds of buffers; currently the scrollBuffer and the marqueeBuffer. 


## Find connected i2c devices

The following command shows at which addresses the i2c devices are on your system. 

    sudo i2cdetect -y 0

It can be installed by running `sudo apt-get install i2c-tools`.
