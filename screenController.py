# A class to control the LCD Keypad Shield's screen.
#
# Authors: Steven Eardley and Duncan Blair
# Copyright 2014
#
# __init__ section based on HD44780 Test Script by Matt Hawkins.

import RPi.GPIO as GPIO
import time

class screenController:
    def __init__(self):
        # Define GPIO to LCD mapping (configured for arduino bridge ports)
        self.LCD_RS = 21
        self.LCD_E  = 22
        self.LCD_D4 = 24
        self.LCD_D5 = 25
        self.LCD_D6 = 4
        self.LCD_D7 = 17
         
        # Define some device constants (16x2 display)
        self.LCD_WIDTH  = 16   # Maximum characters per line
        self.LCD_CHR    = True
        self.LCD_CMD    = False
        self.LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
        self.LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line 
         
        # Timing constants
        self.E_PULSE = 0.00005
        self.E_DELAY = 0.00005

        # Suppress terminal warnings that pins are in use.
        # This allows rewriting messages without being nagged.
        GPIO.setwarnings(False)

        # Some GPIO set-up 
        GPIO.setmode(GPIO.BCM)            # Use BCM GPIO numbers
        GPIO.setup(self.LCD_E, GPIO.OUT)  # E
        GPIO.setup(self.LCD_RS, GPIO.OUT) # RS
        GPIO.setup(self.LCD_D4, GPIO.OUT) # DB4
        GPIO.setup(self.LCD_D5, GPIO.OUT) # DB5
        GPIO.setup(self.LCD_D6, GPIO.OUT) # DB6
        GPIO.setup(self.LCD_D7, GPIO.OUT) # DB7
     
        # Initialise display
        self.lcd_init()

    def lcd_byte(self, bits, mode):
        # Send byte to data pins
        # bits = data
        # mode = True  for character
        #        False for command

        GPIO.output(self.LCD_RS, mode) # RS

        # High bits
        GPIO.output(self.LCD_D4, False)
        GPIO.output(self.LCD_D5, False)
        GPIO.output(self.LCD_D6, False)
        GPIO.output(self.LCD_D7, False)
        if bits & 0x10 == 0x10:
            GPIO.output(self.LCD_D4, True)
        if bits & 0x20 == 0x20:
            GPIO.output(self.LCD_D5, True)
        if bits & 0x40 == 0x40:
            GPIO.output(self.LCD_D6, True)
        if bits & 0x80 == 0x80:
            GPIO.output(self.LCD_D7, True)

        # Toggle 'Enable' pin
        time.sleep(self.E_DELAY)
        GPIO.output(self.LCD_E, True)
        time.sleep(self.E_PULSE)
        GPIO.output(self.LCD_E, False)
        time.sleep(self.E_DELAY)      

        # Low bits
        GPIO.output(self.LCD_D4, False)
        GPIO.output(self.LCD_D5, False)
        GPIO.output(self.LCD_D6, False)
        GPIO.output(self.LCD_D7, False)
        if bits & 0x01 == 0x01:
            GPIO.output(self.LCD_D4, True)
        if bits & 0x02 == 0x02:
            GPIO.output(self.LCD_D5, True)
        if bits & 0x04 == 0x04:
            GPIO.output(self.LCD_D6, True)
        if bits & 0x08 == 0x08:
            GPIO.output(self.LCD_D7, True)

        # Toggle 'Enable' pin
        time.sleep(self.E_DELAY)
        GPIO.output(self.LCD_E, True)
        time.sleep(self.E_PULSE)
        GPIO.output(self.LCD_E, False)
        time.sleep(self.E_DELAY)   

    def lcd_init(self):
        # Initialise display
        self.lcd_byte(0x33, self.LCD_CMD)
        self.lcd_byte(0x32, self.LCD_CMD)
        self.lcd_byte(0x28, self.LCD_CMD)
        self.lcd_byte(0x0C, self.LCD_CMD)
        self.lcd_byte(0x06, self.LCD_CMD)
        self.lcd_byte(0x01, self.LCD_CMD)

    def lcd_string(self, message):
        # Send string to display

        message = message.ljust(self.LCD_WIDTH, " ")

        for i in range(self.LCD_WIDTH):
            self.lcd_byte(ord(message[i]), self.LCD_CHR)

    def println1(self, input):
    # Prints input to the top line of the LCD
        self.lcd_byte(self.LCD_LINE_1, self.LCD_CMD)
        self.lcd_string(input)
        
    def println2(self, input):
    # Prints input to the bottom line of the LCD
        self.lcd_byte(self.LCD_LINE_2, self.LCD_CMD)
        self.lcd_string(input)

