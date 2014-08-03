#!/usr/bin/python
#
# A quick and dirty test program for the Screen class.

from ScreenController import ScreenController

def main():
    screen = ScreenController()

    screen.println1("Hello sexy")
    screen.println2("check yo' tty")

    choice = raw_input("\nWould you like to write to line (1) or (2), or clear the LCD (3)? ")
    
    while choice.strip() != "0":
        if choice == "1":
            screen.println1(raw_input("\nWhat would you like to write? "))
        elif choice == "2":
            screen.println2(raw_input("\nWhat would you like to write? "))
        elif choice == "3":
            screen.clear()
            
        choice = raw_input("\nWould you like to write to line (1) or (2), or clear the LCD (3)? ")

    screen.clear()

if __name__ == '__main__': main()
