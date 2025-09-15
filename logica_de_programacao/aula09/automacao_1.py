import pyautogui
import time


print(pyautogui.position())
# print(pyautogui.size())
time.sleep(3)
pyautogui.moveTo(x=243, y=156)
pyautogui.click(button="left", clicks=2)
time.sleep(3)
pyautogui.moveTo(x=605, y=223)
pyautogui.click(x=605, y=223)
time.sleep(3)
pyautogui.write("chatbot", interval=0.2)
time.sleep(1)
pyautogui.click(x=556, y=356)

pyautogui.hotkey("ctrl","c")
pyautogui.press("enter")


# time.sleep(5)
# # # pyautogui.click(x=105, y=242, button= "middle", clicks=1)
# # pyautogui.moveTo(x=105, y=242, duration=1)
# pyautogui.scroll(-3000)
