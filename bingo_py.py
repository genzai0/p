# 5x5想定でしか作ってないので最初のint(input())で5を入れないとバグるかも
# そのあとは表示された数字or表示されていない数字を入れると該当すればXが付く
# ターミナルが汚れるので使い終わったらEnter連打するといいかも
import random
import sys

n = int(input())
f = 0
l,e = [],[]

def check_bingo(list_obj):
    for i in range(n):
        for j in range(n):
            if list_obj[i][j] != "X": break
        else:
            return True
    
    for i in range(n):
        for j in range(n):
            if list_obj[j][i] != "X": break
        else:
            return True
        
    for i in range(n):
        if list_obj[i][i] != "X": break
    else:
        return True
    
    for i in range(n):
        for j in reversed(range(n)):
            if list_obj[i][j] != "X": break
    else:
        return True
        


def screen(l):
    for i in range(n+2):
        # https://qiita.com/exy81/items/99e99ab8c184343948cc
        # CSIシーケンスっていうらしい
        sys.stdout.write("\033[A\033[2K\033[G")
    
    sys.stdout.write(str(number) + "\n")
    for i in range(n):
        for j in range(n):
            sys.stdout.write(str(l[i][j]) + "\t")
        else:
            sys.stdout.write("\n")

def make_bingo(list_obj,n):
    global e
    for i in range(n):
        tmp_list = []
        for j in range(n):
            tmp = random.randint(j*15+1,(j+1)*15)
            while tmp in e:
                tmp = random.randint(j*15+1,(j+1)*15)
            
            l[i][j] = tmp
            e.append(tmp)

if __name__ == '__main__':
    for i in range(n):
        l.append([0]*n)

    make_bingo(l,n)

    for i in range(n):
        for j in range(n):
            sys.stdout.write(str(l[i][j]) + "\t")
        else:
            sys.stdout.write("\n")


    while(True):
        number = int(input())
        if number == 88888:
            sys.stdout.write("\033[6B")
            break
        if number in e:
            l[e.index(number)//n][e.index(number)%n] = "X"
        screen(l)

        if check_bingo(l):
            print("BINGO!!!")

