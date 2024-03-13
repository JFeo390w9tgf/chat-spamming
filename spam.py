# coded by -> ig : @hackie.techie

import pyautogui as spam
import time

limit = input("Jumlah pesan : ")
msg = input("isi pesan : ")

i = 0

time.sleep(5)

while i<int(limit):
	spam.typewrite(msg)
	spam.press('Enter')

i+=1
