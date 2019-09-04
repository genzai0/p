import fcntl
import termios
import sys
import os

def getkey():
    fno = sys.stdin.fileno()

    attr_old = termios.tcgetattr(fno)

    attr = termios.tcgetattr(fno)
    attr[3] = attr[3] &~termios.ECHO & ~termios.ICANON
    termios.tcsetattr(fno, termios.TCSADRAIN, attr)

    fcntl_old = fcntl.fcntl(fno, fcntl.F_GETFL)
    fcntl.fcntl(fno, fcntl.F_SETFL, fcntl_old | os.O_NONBLOCK)

    chr = 0

    try:
        c = sys.stdin.read(1)
        if len(c):
            while len(c):
                chr = (chr << 8) + ord(c)
                c = sys.stdin.read(1)
    finally:
        fcntl.fcntl(fno, fcntl.F_SETFL, fcntl_old)
        termios.tcsetattr(fno, termios.TCSANOW, attr_old)

    return chr

if __name__=="__main__":
    while 1:
        key = getkey()

        if key == 10:
            break
        elif key:
            print(key)
