import time as tm

import getpass

import datetime

import calendar

import os

import sys

print("real os (R) Core Open Source System 1.1")

print("更新检查系统:似乎有新的更新! 访问 github.com/LittleWhite 来下载更新!")

count = 0

stpasswd = "114514"

while count < 3:

    user = input("输入您的用户,它默认是root: ")

    if user == "root":

        while count < 3:

            passwd = getpass.getpass("输入您的密码，它默认是114514，但是您可以改变它，登录后输入help来获取帮助: ")

            if passwd == stpasswd:

                tm.sleep(1.5)

                while count < 3:

                    cmd = input("~ $ ")

                    if cmd == "ls":

                        print("下载  文档  音乐  图片")

                    elif cmd == "version":

                        print("Real OS (R) Core Open Source System 1.1 ")

                    elif cmd == "coverter":

                        print("File Covert\nCovert .lpap/.lpcu/.bbc to .umm")

                        input("Input file's path:\n")

                        for i in range(1, 101):

                            print("\r", end="")

                            print("Progress: {}%: ".format(i), "=" * (i // 2), end="")

                            sys.stdout.flush()

                            tm.sleep(0.05)

                        print("\nCovert Complete.")

                    elif cmd == "time":

                        now = datetime.datetime.now()

                        other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")

                        print(other_StyleTime)

                    elif cmd == "passwd":

                        stpasswd = input("您的新密码是什么呢: ")

                    elif cmd == "calendar":

                        yy = int(input("今天的年份: "))

                        mm = int(input("今天的月份: "))

                        print(calendar.month(yy, mm))

                    elif cmd == "help":

                        print("ls          View the path")

                        print("version     Show the system's version")

                        print("coverter    A tool to covert .lpap/.lpcu/.bbc to .umm")

                        print("time        Show the time and date")

                        print("calendar    Show a calendar")

                        print("calc        A simple calculator")

                        print("clear       Clean the screen")

                        print("passwd      Change your password")

                        print("exit        Log out")
                        
                        print("这些是英语，后期会出现中文版")
                    elif cmd == "calc":

                        try:

                            formula = input("Enter the formula to be calculated:\n")

                            print(formula + "=", eval(formula))

                        except Exception as e:

                            print("Input error.")

                    elif cmd == "":

                        space = "0"

                    elif cmd == "clear":

                        i = os.system("cls")

                    elif cmd == "exit":

                        break

                    else:

                        print("很抱歉，此命令并不存在于此计算机上")

            else:

                print("对不起，密码不正确，重新试一次？")

    else:

        print("对不起，此计算机上并不存在这个用户")
