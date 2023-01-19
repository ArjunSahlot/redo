import pyautogui
import time

pyautogui.PAUSE = 0

def play(file, skip_time, ignore_keyboard, ignore_mouse):
    with open(file, "r") as log:
        commands = log.read().strip().split("\n")

    start = time.time()

    for command in commands:
        c, t, *args = command.split(" ")

        if not skip_time:
            t = float(t[:-1])
            curr_time = time.time()-start
            while curr_time < t:
                curr_time = time.time()-start

        if not ignore_mouse:
            if c == "m":
                pyautogui.moveTo(int(args[0]), int(args[1]))
            elif c == "cp":
                pyautogui.mouseDown(int(args[0]), int(args[1]), button=args[2])
            elif c == "cr":
                pyautogui.mouseUp(int(args[0]), int(args[1]), button=args[2])
            elif c == "sh":
                pyautogui.scroll(int(args[2]), int(args[0]), int(args[1]))
            elif c == "sv":
                pyautogui.hscroll(int(args[2]), int(args[0]), int(args[1]))

        if not ignore_keyboard:
            if c == "kp":
                pyautogui.keyDown(args[0])
            elif c == "kr":
                pyautogui.keyUp(args[0])
