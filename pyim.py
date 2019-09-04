import sys
from ggg import set_raw_mode,scankey,getkey
#import scankey
#import getkey

#def save():
#    f = open("./" + )

def load(path):
    #f = open("./" + args[1])
    #print(f)
    with open("./" + path) as f:
        l = [s.strip() for s in f.readlines()]
        return l

def move(s):
    if s=="j":
        sys.stdout.write("\033[B")
    if s=="k":
        sys.stdout.write("\033[A")
    if s=="h":
        sys.stdout.write("\033[D")
    if s=="l":
        sys.stdout.write("\033[C")

if __name__ == '__main__':
    args = sys.argv
    path = args[1]
    while(True):
        #f = load(path)
        #sout.write("\033[")
        #s = input()
        with set_raw_mode():
            while 1:
                key = scankey()
                #if key == '\n': s = key
                #elif key: s = key
                #sys.stdout.write()
                sys.stdout.write("\033[2K")
        #sys.stdout.write()
                move(key)

        # \n is "0x10" . after i need this area rewrite to handle character
