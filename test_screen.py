#!/usr/bin/python
#
# A quick and dirty test program for the Screen class.

from screenController import screenController

def main():
    screen = screenController()

    screen.println1("Hello sexy")

if __name__ == '__main__': main()
