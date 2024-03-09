import pyautogui as p

hours = 12
for i in range(60*60 * hours):
    x,y = p.position()
    p.click(1450,600)
    p.moveTo(x,y)
    #p.click(x,y)
    p.sleep(1)
