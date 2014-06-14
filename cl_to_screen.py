__author__ = 'steve'

"""
Quick and dirty script to write from an interactive console to the LCD screen.
Based on HD44780 LCD Test Script for Raspberry Pi, by Matt Hawkins.
"""
import RPi.GPIO as GPIO
import time
from itertools import cycle

# Define GPIO to LCD mapping (configured for arduino bridge ports)
LCD_RS = 21
LCD_E  = 22
LCD_D4 = 24
LCD_D5 = 25
LCD_D6 = 4
LCD_D7 = 17

# Define some device constants (16x2 display)
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

# Timing constants
E_PULSE = 0.00005
E_DELAY = 0.00005

def main():

    # Suppress warnings that pins are in use (allows rewriting messages without being nagged)
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
    GPIO.setup(LCD_E, GPIO.OUT)
    GPIO.setup(LCD_RS, GPIO.OUT)
    GPIO.setup(LCD_D4, GPIO.OUT)
    GPIO.setup(LCD_D5, GPIO.OUT)
    GPIO.setup(LCD_D6, GPIO.OUT)
    GPIO.setup(LCD_D7, GPIO.OUT)

    # Initialise display
    lcd_init()

    # Repeatedly ask user to write messages to the display
    print "Type a message and press Enter to send to the screen. Ctrl+c to exit"

    # Cycle through 0, 1 to write to first, second lines
    l = [0, 1]
    ticktock = cycle(l)

    while True:
        new_message = raw_input("\nwrite to screen: ")

        if ticktock.next():
            lcd_write(0, new_message)
        else:
            lcd_write(1, new_message)

def lcd_init():
    # Initialise display
    lcd_byte(0x33, LCD_CMD)
    lcd_byte(0x32, LCD_CMD)
    lcd_byte(0x28, LCD_CMD)
    lcd_byte(0x0C, LCD_CMD)
    lcd_byte(0x06, LCD_CMD)
    lcd_byte(0x01, LCD_CMD)

def lcd_write(line_pos, message):
    if line_pos:
        lcd_byte(LCD_LINE_1, LCD_CMD)
    else:
        lcd_byte(LCD_LINE_2, LCD_CMD)

    # Send string to display
    message = message.ljust(LCD_WIDTH, " ")

    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)

def lcd_byte(bits, mode):
    # Send byte to data pins
    # bits = data
    # mode = True  for character
    #        False for command

    GPIO.output(LCD_RS, mode) # RS

    # High bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits & 0x10 == 0x10:
        GPIO.output(LCD_D4, True)
    if bits & 0x20 == 0x20:
        GPIO.output(LCD_D5, True)
    if bits & 0x40 == 0x40:
        GPIO.output(LCD_D6, True)
    if bits & 0x80 == 0x80:
        GPIO.output(LCD_D7, True)

    # Toggle 'Enable' pin
    time.sleep(E_DELAY)
    GPIO.output(LCD_E, True)
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, False)
    time.sleep(E_DELAY)

    # Low bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits & 0x01 == 0x01:
        GPIO.output(LCD_D4, True)
    if bits & 0x02 == 0x02:
        GPIO.output(LCD_D5, True)
    if bits & 0x04 == 0x04:
        GPIO.output(LCD_D6, True)
    if bits & 0x08 == 0x08:
        GPIO.output(LCD_D7, True)

    # Toggle 'Enable' pin
    time.sleep(E_DELAY)
    GPIO.output(LCD_E, True)
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, False)
    time.sleep(E_DELAY)

if __name__ == '__main__':
    main()