from screenController import screenController
import sys

def main():
    screen = screenController()

    for line in sys.stdin:
        screen.println1(line)
