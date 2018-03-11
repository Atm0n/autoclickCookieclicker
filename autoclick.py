from pynput.mouse import Button, Controller
from time import sleep
posicions = "(444, 228)", "(520, 308)"
mouse =Controller()
x = input("Entra el número de clics per segon: ")
print(mouse.position)
pos = "(114, 368)"
mouse.position = (114, 368)
def click1():
    mouse.position = (444, 228)
    mouse.click(Button.left, 1)
    mouse.position = (114, 368)
def click2():
    mouse.position = (520, 308)
    mouse.click(Button.left, 1)
    mouse.position = (114, 368)
while True:
    mouse.click(Button.left, int(x))
    sleep(0.5)
    click2()
    click1()
    if str(mouse.position)!="(114, 368)":
        break