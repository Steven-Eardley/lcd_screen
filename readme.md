# lcd_screen

Files relating to the operation of the LCD screen connected over GPIO via the arduino bridge.
The goal is to make a sensible set of tools to present text on the display in useful and interesting ways.

See Issues on github for todos etc.

# Installation:

Use a virtualenv if you like - it allows you to keep project packages (e.g. rpi.gpio) separate from host system Python installation.

Set up a virtualenv for this project:
	virtualenv -p python2.7 lcd_screen --no-site-packages

This will create a new virtual environment, including places for local libraries. The virtualenv is activated by sourcing the file 'activate' in bin:

	. bin/activate

Deactivate thusly:

	deactivate

Create a folder for the code, e.g. src, or clone straight into the virtualenv main folder.

	git clone git@github.com:Steven-Eardley/lcd_screen.git src

The use the virtualenv's pip installer to download the dependencies specified in setup.py

	pip install -e .

Currently the useful code is in screentest.py
