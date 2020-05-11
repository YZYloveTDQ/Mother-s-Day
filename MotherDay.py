"""母亲节的祝福"""
import os
import time
import random
import pygame
import colorama

bgm_path = 'bgm.mp3'
colorama.init(convert=True)
stars = [2, 4, 8, 10, 14, 20, 26, 28, 38, 42, 50, 58, 62, 74]
flowers = [7, 15, 21, 31, 39, 46]
hearts = [13, 27, 39, 53, 67, 75]

RED = colorama.Fore.RED + colorama.Style.BRIGHT
CYAN = colorama.Fore.CYAN + colorama.Style.BRIGHT # 蓝绿色
GREEN = colorama.Fore.GREEN + colorama.Style.BRIGHT
YELLOW = colorama.Fore.YELLOW + colorama.Style.BRIGHT
MAGENTA = colorama.Fore.MAGENTA + colorama.Style.BRIGHT # 玫瑰红
BLUE = colorama.Fore.BLUE + colorama.Style.BRIGHT

def playBGM(bgm):
    pygame.mixer.init()
    pygame.mixer.music.load(bgm)
    pygame.mixer.music.play()

def nextLine():
    time.sleep(0.5)
    print()

def drawHeart(spaces):
    num_spaces = spaces + 27 # 起始位置
    print(' '*num_spaces, end='')
    for i in range(78):
        if i in hearts: # 到这几个数字换行
            nextLine()
            print(' ' *num_spaces, end='')
        elif i in stars:
            print(RED + '*', end='')
        elif i in [32, 35]:
            print(GREEN + '妈', end='')
        else:
            print(' ', end='')

def showText(spaces):
    print(' '*spaces, end='')
    print(CYAN + "-------------------Happy  Mother's  Day ! 母亲节快乐！-------------------")

def showText_zh(spaces):
    num_spaces = spaces + 24
    index = random.randint(1, 10)
    if index==1:
        print(' '*num_spaces, end='')
        print(CYAN + "妈妈！您辛苦了，爱您~")
    elif index==2:
        print(' '*num_spaces, end='')
        print(CYAN + "妈妈，节日快乐哦~")
    elif index==3:
        print(' '*num_spaces, end='')
        print(BLUE + "妈妈，感谢您为我付出的一切！")
    elif index==4:
        print(' '*num_spaces, end='')
        print(BLUE + "妈妈，等我长大了，我来保护您")
    elif index==5:
        print(' '*num_spaces, end='')
        print(BLUE + "妈妈，我永远爱您")
    elif index==6:
        print(' '*num_spaces, end='')
        print(YELLOW + "妈妈，我会永远听您的话的！")
    elif index==6:
        print(' '*num_spaces, end='')
        print(YELLOW + "妈妈，祝福您永远健康美丽")
    elif index==7:
        print(' '*num_spaces, end='')
        print(MAGENTA + "妈妈，以后会给你买好多好看的衣服")
    elif index==8:
        print(' '*num_spaces, end='')
        print(MAGENTA + "妈妈，感谢您对我一直以来的严厉")
    elif index==9:
        print(' '*num_spaces, end='')
        print(RED + "妈妈，我真的长大了！ 谢谢您")
    elif index==10:
        print(' '*num_spaces, end='')
        print(RED + "妈妈，每一天都要开开心心的哦")

def drawFlower(spaces):
    num_spaces = spaces + 30
    print(' '*num_spaces, end='')
    for i in range(47):
        if i in flowers:
            nextLine()
            print(' '*num_spaces, end='')
        elif i in [2, 8, 12, 18]:
            print(MAGENTA + '{', end='')
        elif i in [3, 9, 13, 19]:
            print(MAGENTA + '~', end='')
        elif i in [4, 10, 14, 20]:
            print(MAGENTA + '}', end='')
        elif i in [25, 35, 43]:
            print(GREEN + '|', end='')
        elif i in [34, 44]:
            print(GREEN + '~', end='')
        else:
            print(' ', end='')
    time.sleep(0.6)

def clearScreen():
    try:
        os.system('cls') # windows
    except:
        os.system('clear') # linux

def main():
    playBGM(bgm_path)
    clearScreen()
    while True:
        num_spaces = random.randint(5, 50)
        showText(num_spaces)
        nextLine()
        drawHeart(num_spaces)
        nextLine()
        showText_zh(num_spaces)
        nextLine()
        drawFlower(num_spaces)
        nextLine()

if __name__ == "__main__":
    main()
