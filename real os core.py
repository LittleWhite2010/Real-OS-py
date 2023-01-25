import time as tm

import getpass

import datetime

import calendar

import os

import sys

print("real os (R) Core Open Source System 1.0")

print("Avaliable update! Visit github.com/LittleWhite to update")

count = 0

stpasswd = "114514"

while count < 3:

    user = input("Login（输入您的用户,它是root）: ")

    if user == "root":

        while count < 3:

            passwd = getpass.getpass("Password（输入您的密码，它默认是114514，但是您可以改变它，登录后输入help来获取帮助）: ")

            if passwd == stpasswd:

                tm.sleep(1.5)

                while count < 3:

                    cmd = input("~ $ ")

                    if cmd == "ls":

                        print("Downloads  Documents  Music  Pictures")

                    elif cmd == "version":

                        print("real os (R) Core Open Source System 1.0 ")

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

                        stpasswd = input("Input new password: ")

                    elif cmd == "calendar":

                        yy = int(input("Year: "))

                        mm = int(input("Month: "))

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
                        
                        print("这些是英语，后期会变成汉字")
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

                        print("很抱歉，此命令并不存在于计算只因上")

            else:

                print("对不起，密码不正确，重新试一次？")

    else:

        print("对不起，计算只因上并不存在这个用户")
