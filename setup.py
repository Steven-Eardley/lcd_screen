from setuptools import setup, find_packages

setup(
    name = 'lcd_screen',
    version = '0.0.1',
    packages = find_packages(),
    install_requires = [
        "rpi.gpio==0.5.5",
    ],
    url = 'https://github.com/Steven-Eardley/lcd_screen',
    author = 'Steve Eardley',
    author_email = 'me@steveneardley.co.uk',
    description = 'Control the LCD screen attached to Charon via pi-arduino bridge',
)
