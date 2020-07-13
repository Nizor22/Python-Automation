import pyautogui as pg
import time


for i in range(50):
	pg.moveTo(599, 383)
	pg.click()
	time.sleep(.4)
	pg.moveTo(608, 486)
	pg.click()
	time.sleep(.4)
	pg.moveTo(714, 352)
	pg.click()
	time.sleep(.4)
	print(pg.position())
	time.sleep(.4)