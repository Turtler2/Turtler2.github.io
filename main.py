from pygame import *
from random import *
import asyncio

async def main():
    init()
    key.start_text_input()
    screen_width = 1200
    screen_height = 600
    screen = display.set_mode([screen_width,screen_height])
    font.init()
    fah = font.Font(font.get_default_font(), 36)
    # to make harder use round(uniform(min,max), decimal points )
    n1=randint(1,12)
    n2=randint(1,12)
    look = n1*n2
    gyf = ""
    kind = False
    hiii = f"{n1}*{n2}"
    bouncer = fah.render(hiii, False, (35,56,67))
    mememe = 0
    streak = fah.render(str(mememe), False, (35,56,67))
    youyouyou = 50
    darn = fah.render(str(youyouyou), False, (35,56,67))
    why = fah.render(gyf, False, (35,56,67))
    while youyouyou > 0:
        await asyncio.sleep(0)

        screen.fill([255,255,255])
        screen.blit(bouncer,(screen_width/2-20,screen_height/2-20))
        screen.blit(streak,(screen_width-150,screen_height/4))
        screen.blit(darn,(screen_width/5,screen_height/4))
        screen.blit(why,(screen_width/4-25,screen_height-125))
        display.flip()
        why = fah.render(gyf, False, (35,56,67))
        for evt in event.get():
            if evt.type==QUIT:
                youyouyou=0
            if evt.type == KEYDOWN:
                if evt.key == K_RETURN:
                    kind = True
                elif evt.key == K_BACKSPACE:
                    gyf = gyf[0:-1]
                else:
                    gyf +=  evt.unicode
        if not kind: continue


        if gyf == "prank":
            youyouyou = 9999999998
        if gyf == str(look) : 
            mememe +=1
            youyouyou -=1
        else:
            print (f"{look}")
            nooo = fah.render(str(look), False, (35,56,67))
            screen.blit(nooo,(screen_width/2-20,screen_height/2-100))
            display.flip()
            time.delay(150)
            mememe = 0
            youyouyou +=2
        if gyf == "RaifE":
            youyouyou = 1
            mememe = 9999999
        #if youyouyou <= 0:
        #   youyouyou = 50
        n1=randint(1,12)
        n2=randint(1,12)
        look = n1*n2
        hiii = f"{n1}*{n2}"
        bouncer = fah.render(hiii, False, (35,56,67))
        streak = fah.render(str(mememe), False, (35,56,67))
        darn = fah.render(str(youyouyou), False, (35,56,67))
        gyf = ""
        kind = False    
    key.stop_text_input()
asyncio.run(main())
