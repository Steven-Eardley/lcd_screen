from ScreenController import ScreenController
import sys

def main():
    screen = ScreenController()

    for line in sys.stdin:
        uptime = line.split()
    
    screen.println1(uptime[0][:-3] + " " + uptime[1] + " " + uptime[2][:-1])
    print(uptime[0][:-3] + " " + uptime[1] + " " + uptime[2][:-1])

if __name__ == '__main__':
    main()
