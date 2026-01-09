import pyautogui as p


def ticket():
    x, y = p.position()
    p.click(1450, 230)
    p.sleep(1)
    p.click(1100, 750)
    p.moveTo(x, y)
    # p.click(x,y)
    p.sleep(1)


def coin():
    x, y = p.position()
    p.click(1450, 600)
    p.sleep(0.6)
    p.moveTo(x, y)
    p.sleep(1)


hours = 12
for i in range(60 * 60 * hours):
    ticket()
    # coin()
