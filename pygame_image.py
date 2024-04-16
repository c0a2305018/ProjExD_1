import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")  #練習２
    kk_img = pg.transform.flip(kk_img, True, False)  #練習２
    kk_rct = kk_img.get_rect() #８－１　工科とんrectを抽出
    kk_rct.center = 300, 200
    
    bg_img2 = pg.transform.flip(bg_img, True, False)  #練習７ー１
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:        #練習8
            #print("上押された")
            kk_rct.move_ip((0, -1))
        elif key_lst[pg.K_DOWN]:
            kk_rct.move_ip((0, 1))
        elif key_lst[pg.K_RIGHT]:
            kk_rct.move_ip((1, 0))
        elif key_lst[pg.K_LEFT]:
            kk_rct.move_ip((-1, 0))
        else:
            kk_rct.move_ip((-1, 0))   #演習課題１

        x = tmr%3200  
        # print(tmr, x)
        screen.blit(bg_img, [-x , 0]) #練習６
        screen.blit(bg_img2, [-x+1600, 0]) #練習７－1
        
        screen.blit(bg_img, [-x+3600, 0]) #練習７－２
        screen.blit(bg_img2, [-x+4800, 0]) #練習７ー２
        screen.blit(kk_img , kk_rct)  #練習４ 8
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習５


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()