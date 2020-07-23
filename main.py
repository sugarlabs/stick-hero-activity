# -*- coding: utf-8 -*-
#
# Stick Hero
# Copyright (C) 2015  Utkarsh Tiwari
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Contact information:
# Utkarsh Tiwari    iamutkarshtiwari@gmail.com

import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import pickle
import pygame
import sys
from gettext import gettext as _

from sugar3.activity.activity import get_activity_root

from math import *
from random import *

from scorescreen import scorescreen
from welcomescreen import welcomescreen

from rules import rulescreen, sx, sy, display_init, scale_img


class game:

    def make(self):

        gameDisplay = display_init()
        sound = True

        try:
            pygame.mixer.init()
        except Exception as err:
            sound = False
            print('error with sound', err)

        black = (0, 0, 0)
        white = (255, 255, 255)
        clock = pygame.time.Clock()
        timer = pygame.time.Clock()

        crashed = False
        disp_width = 600
        disp_height = 600

        press = 0

        info = pygame.display.Info()

        if not(gameDisplay):

            gameDisplay = pygame.display.set_mode(
                (info.current_w, info.current_h))

            pygame.display.set_caption(_("Stick Hero"))
            gameicon = pygame.image.load('images/icon.png')
            pygame.display.set_icon(gameicon)

        hero = scale_img("images/hero.png")
        herotr = hero

        hero1 = scale_img("images/hero1.png")
        hero2 = scale_img("images/hero2.png")
        hero3 = scale_img("images/hero3.png")

        herodown = pygame.transform.flip(hero, False, True)
        hero1down = pygame.transform.flip(hero1, False, True)
        hero2down = pygame.transform.flip(hero2, False, True)
        hero3down = pygame.transform.flip(hero3, False, True)

        scoreplate = scale_img("images/scoreplate.png").convert()
        scoreplate.set_alpha(50)

        stick = scale_img("images/stick.png").convert()
        # background=pygame.image.load("images/background.png").convert()
        alpha = scale_img("images/alpha.png").convert()
        beta = scale_img("images/beta.png").convert()
        gamma = scale_img("images/gamma.png").convert()
        delta = scale_img("images/delta.png").convert()
        back1 = pygame.image.load("background/back1.png").convert()
        back1 = pygame.transform.scale(back1, (int(sx(1280)), int(sy(720))))
        back2 = pygame.image.load("background/back2.png").convert()
        back2 = pygame.transform.scale(back2, (int(sx(1280)), int(sy(720))))

        back3 = pygame.image.load("background/back3.jpg").convert()
        back3 = pygame.transform.scale(back3, (int(sx(1280)), int(sy(720))))

        back4 = pygame.image.load("background/back4.png").convert()
        back4 = pygame.transform.scale(back4, (int(sx(1280)), int(sy(720))))

        back5 = pygame.image.load("background/back5.jpg").convert()
        back5 = pygame.transform.scale(back5, (int(sx(1280)), int(sy(720))))

        back6 = pygame.image.load("background/back6.jpg").convert()
        back6 = pygame.transform.scale(back6, (int(sx(1280)), int(sy(720))))

        back7 = pygame.image.load("background/back7.png").convert()
        back7 = pygame.transform.scale(back7, (int(sx(1280)), int(sy(720))))

        fruit = scale_img("images/fruit.png").convert()
        # BIRD FRAMES

        frame1 = pygame.image.load("birds/1.png")
        # frame1=pygame.transform.flip(frame1,True,False)

        frame2 = pygame.image.load("birds/2.png")
        # frame2=pygame.transform.flip(frame2,True,False)

        frame3 = pygame.image.load("birds/3.png")
        # frame3=pygame.transform.flip(frame3,True,False)

        frame4 = pygame.image.load("birds/4.png")
        # frame4=pygame.transform.flip(frame4,True,False)

        frame5 = pygame.image.load("birds/5.png")
        # frame5=pygame.transform.flip(frame5,True,False)

        frame6 = pygame.image.load("birds/6.png")
        # frame6=pygame.transform.flip(frame6,True,False)

        frame7 = pygame.image.load("birds/7.png")
        # frame7=pygame.transform.flip(frame7,True,False)

        frame8 = pygame.image.load("birds/8.png")
        # frame8=pygame.transform.flip(frame8,True,False)

        birds = [frame1, frame2, frame3, frame4,
                 frame5, frame6, frame7, frame8]

        backgroundlist = [back1, back2, back3, back4, back5, back6, back7]

        back = backgroundlist[randint(0, 6)]
        # back=back5

        # stickx1=455
        # sticky1=50

        herokicklist = [hero, herotr]

        herolist = [hero, hero1, hero2, hero3]

        herodownlist = [herodown, hero1down, hero2down, hero3down]

        pillarlist = [alpha, beta, gamma, delta]

        # Sound loads

        pop1 = pygame.mixer.Sound("sound/pop_1.ogg")
        pop2 = pygame.mixer.Sound("sound/pop_2.ogg")

        stickgrow = pygame.mixer.Sound("sound/stick_grow_loop.ogg")

        kick = pygame.mixer.Sound("sound/kick.ogg")

        landing = pygame.mixer.Sound("sound/fall.ogg")

        scoresound = pygame.mixer.Sound("sound/score.ogg")

        dead = pygame.mixer.Sound("sound/dead.ogg")
        kick = pygame.mixer.Sound("sound/kick.ogg")
        rollupdown = pygame.mixer.Sound("sound/roll_up_down.ogg")
        eating_fruit = pygame.mixer.Sound("sound/eating_fruit.ogg")
        perfectsound = pygame.mixer.Sound("sound/perfect.ogg")

        flappy = pygame.mixer.Sound("sound/bird/bonus_loop_bird.ogg")
        chichi = pygame.mixer.Sound("sound/bird/bonus_trigger_bird.ogg")

        font_path = "fonts/Arimo.ttf"
        font_size = int(sx(40))
        font1 = pygame.font.Font(font_path, font_size)
        font2 = pygame.font.Font("fonts/Arimo.ttf", int(sx(25)))
        font3 = pygame.font.Font("fonts/Arimo.ttf", int(sx(40)))
        font4 = pygame.font.Font("fonts/Arimo.ttf", int(sx(20)))

        # VARIABLE INITIALIZATION

        stickx1 = stickx = sx(455, 1)
        sticky1 = sticky = sy(472)

        anglenum = 90
        angle = (pi / 180) * anglenum

        sticklength = 0

        time = 0
        flag = 0  # stick fall flag
        keypressflag = 0

        moveit = 0  # hero move flag

        herox = sx(429, 1)
        heroy = sy(442)

        heropointer = 0

        i = 0
        j = 0
        k = 0

        pillar1x = sx(355, 1)
        msgx = pillar2x = sx(650, 1)

        pillar3x = randint(int(sx(845, 1)), int(sx(900, 1)))

        pillar1 = alpha
        pillar2 = beta
        pillar3 = pillarlist[randint(0, 2)]

        herofall = 0
        herofallflag = 0

        pillarmoveflag = 0

        stickmove = 0

        backx = 0

        pillarfound = 0

        score = 0

        keyinit = 0

        speed = sx(8)

        acc1 = acc2 = acc3 = 0

        pillarfast = 0

        pillardist = randint(int(sx(60, 1)), int(sx(260, 1)))
        lastpillardist = pillardist

        stickgrowsound = 0

        ext = 0

        backx1 = sx(350, 1)
        backx2 = sx(1630, 1)

        upsidedown = False

        keypress = 0

        if(pillar1x > (sx(429, 1)) and pillar1x < (sx(840, 1))):
            # acc1=2
            pillar2nd = pillar1x

        if(pillar2x > (sx(429, 1)) and pillar2x < (sx(840, 1))):
            # acc2=2
            pillar2nd = pillar2x

        if(pillar3x > (sx(429, 1)) and pillar3x < (sx(840, 1))):
            # acc3=2
            pillar2nd = pillar3x

        bouncedown = True
        bounce = 0

        fruitx = 0

        fruitgot = False
        fruitflag = 0

        herod = sy(33)

        fruitscore = 0
        score = 0
        
        score_path = os.path.join(get_activity_root(), 'data', 'score.pkl')
        if not os.path.exists(score_path):
            open(score_path,'w+')

        if os.path.getsize(score_path) == 0:

            with open(score_path, 'wb') as output:
                pickle.dump(0, output, pickle.HIGHEST_PROTOCOL)
                pickle.dump(0, output, pickle.HIGHEST_PROTOCOL)

        with open(score_path, 'rb') as input:  # REading
            fruitscore = pickle.load(input)
            fruitscore = pickle.load(input)

        scoreshift = 0
        fruitscoreshift = 0
        shift1 = 1
        shift2 = 1

        perfectflag = 0
        vanish = 0
        perfect = 0
        b1 = 0
        b2 = 2
        b3 = 4
        b4 = 6

        birdx = sx(900, 1)
        birdxslow = sx(950, 1)
        birdxfast = sx(860, 1)

        birdgroupshow = 0
        birdsingleshow = 0
        birdmainshow = 0
        birdpickup = 0
        birdsound = 0

        flagchk1 = flagchk2 = flagchk3 = 0

        flagchk = 0

        catch = 0

        # lastpillardist=pillar2x-457

        # GAME LOOP BEGINS !!!

        while not crashed:
            # Gtk events
            keydown_pressed = False
            keyup_pressed = False
            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                # totaltime+=timer.tick()
                if event.type == pygame.QUIT:
                    crashed = True
                elif event.type == pygame.KEYDOWN and event.key == 273:
                    keydown_pressed = True
                elif event.type == pygame.KEYUP and event.key == 273:
                    keyup_pressed = True

            mos_x, mos_y = pygame.mouse.get_pos()

            # print "hello"

            if(catch == 0):
                b = welcomescreen()
                catch = b.make(gameDisplay, back)

            gameDisplay.fill(white)
            gameDisplay.blit(back, (backx1, 0))
            gameDisplay.blit(back, (backx2, 0))
            gameDisplay.blit(fruit, (sx(800, 1), sy(20)))

            # scoreplate.set_alpha(20)
            gameDisplay.blit(scoreplate, (sx(540, 1), sy(40)))

            # score blitting

            # Bird frames processing

            if(i % 7 == 0):
                b1 += 1
                if(b1 == 8):
                    b1 = 0

                b2 += 1
                if(b2 == 8):
                    b2 = 0

                b3 += 1
                if(b3 == 8):
                    b3 = 0

                b4 += 1
                if(b4 == 8):
                    b4 = 0

            if(birdgroupshow == 1):

                gameDisplay.blit(pygame.transform.scale(
                    birds[b1], (int(sx(57)), int(sy(39)))), (birdx + sx(10), sy(100)))
                gameDisplay.blit(pygame.transform.scale(
                    birds[b2], (int(sx(57 - 10)), int(sy(39 - 10)))), (birdx - sx(50), sy(115)))

                gameDisplay.blit(pygame.transform.scale(
                    birds[b3], (int(sx(57 - 20)), int(sy(39 - 20)))), (birdx, sy(110 + 30)))

            if(birdsingleshow == 1):

                gameDisplay.blit(pygame.transform.scale(
                    birds[b3], (int(sx(57 + 10)), int(sy(39 + 10)))), (birdxslow, sy(110)))

            # Birds movement

            if(birdx >= (sx(300, 1)) and birdgroupshow == 1):
                birdx -= sx(3)

            if(birdxslow >= (sx(300, 1)) and birdsingleshow == 1):
                birdxslow -= sx(2)

            if(birdmainshow == 1):

                birdxfast -= birdspeed

            # Birds coordinates updates

            if(birdx < (sx(300, 1))):
                birdx = sx(900, 1)
                birdgroupshow = 0

            if(birdxslow < (sx(300, 1))):
                birdxslow = sx(950, 1)
                birdsingleshow = 0

            if((birdxfast + sx(30)) <= (sx(300, 1))):
                birdxfast = sx(860, 1)
                birdmainshow = 0

            if(birdsingleshow == 0 and i % 18 == 0):
                r = randint(0, 99)
                if(r % 18 == 0):
                    birdgroupshow = 1
                    birdsingleshow = 1

            # BIRD PICK'S YOU UP

            if(pygame.transform.scale(birds[b4], (int(sx(57 + 30)), int(sy(39 + 20)))).get_rect(center=(birdxfast + sx(40), sy(400 + 20))).colliderect(herolist[j].get_rect(center=(herox + sx(18), heroy + herod + sy(15))))):

                herox = birdxfast + sx(30)
                birdpickup = 1

                if(birdsound == 0):
                    birdsound = 1

                moveit = 0

                if(herox < (sx(320, 1))):

                    ext = 1

            #pygame.draw.circle(gameDisplay,white, (birdxfast,400) ,3, 2)

            #pygame.draw.circle(gameDisplay,white, (herox+18,heroy+herod) ,3, 2)

            if(birdsound == 1):
                birdsound = 2
                flappy.play(0)

            scores = font1.render(str(score), 1, (255, 255, 255))
            gameDisplay.blit(scores, (sx(580 + scoreshift, 1), sy(40)))
            fruitscores = font2.render(str(fruitscore), 1, (0, 0, 0))
            gameDisplay.blit(fruitscores, (sx(770 + fruitscoreshift, 1), sy(13)))

            if(perfect == 1):

                vanish -= 1

                msg1 = font3.render(_("Perfect!!!"), 1, (0, 0, 0))
                gameDisplay.blit(msg1, (sx(510, 1), sy(120)))

                msg2 = font4.render(_("+1"), 1, (0, 0, 0))
                gameDisplay.blit(msg2, (msgx, sy(460 + vanish)))

                if(vanish < -50):
                    perfect = 0
                    vanish = 0

            # fruits bounce up-down

            if((pillar2nd - sx(429)) > (sx(80, 1)) and fruitx >= (sx(429, 1)) and fruitx != 0 and not(fruitgot)):
                gameDisplay.blit(fruit, (fruitx, sy(480 + bounce)))

            if(bouncedown == True):
                if(i % 6 == 0):
                    bounce += 1
                    if(bounce > 5):
                        bouncedown = not(bouncedown)
            else:
                if(i % 6 == 0):
                    bounce -= 1
                    if(bounce < 0):
                        bouncedown = not(bouncedown)

            # Fruit vanish condition

            if(fruitflag == 0 and herodownlist[j].get_rect(center=(herox + sx(18), heroy + herod + sy(10))).colliderect(fruit.get_rect(center=(fruitx + sx(14), sy(480 + bounce + 10))))):
                fruitgot = not fruitgot
                fruitflag = 1
                if(herofallflag != 1):
                    fruitscore += 1
                    # rollupdown.stop()
                    # eating_fruit.stop()
                    eating_fruit.play()

            # if(upsidedown==1 and herox+15>=fruitx):
            #    fruitgot=not fruitgot

            #pygame.draw.circle(gameDisplay,black, (herox+15,heroy+60) ,3, 2)

            #pygame.draw.circle(gameDisplay,black, (herox+18,heroy+10+33) ,3, 2)

            #pygame.draw.circle(gameDisplay,black, (fruitx+13,480+bounce+10) ,3, 2)

            # backgound frames roll-over

            if(backx1 < -(sx(1280))):
                # if not(back==back2):
                backx1 = sx(1270)
                # else:
                #    backx1=1260
            if(backx2 < -(sx(1280))):
                # if not(back==back2):
                backx2 = sx(1270)
                # else:
                #    backx2=1260

            if(i > 20):
                i = 0

            i += 1
            if(i % 4 == 0):
                j += 1

            if(j == 4):
                j = 0

            if(moveit == 1):

                if(upsidedown == False):
                    herod = 0
                    gameDisplay.blit(
                        herolist[j], (herox, heroy + (herod - sy(birdpickup * 5))))
                else:
                    herod = 33
                    gameDisplay.blit(herodownlist[j], (herox, heroy + sy(herod)))

            # Main bird display

            if(birdmainshow == 1):

                gameDisplay.blit(pygame.transform.scale(
                    birds[b4], (int(sx(57 + 30)), int(sy(39 + 20)))), (birdxfast, sy(400)))

            # Inverted hero collsion with pillar test

            if(upsidedown == True and (herox + sx(30)) >= pillar2nd):

                herofall = 1
                moveit = 0
                flag = 1

            # print upsidedown

            if(moveit == 0):

                if(k <= 6):
                    gameDisplay.blit(herokicklist[0], (herox, heroy))
                if(k <= 12):
                    gameDisplay.blit(herokicklist[1], (herox - sx(1), heroy + sy(2)))

                if(keypressflag == 1):
                    k += 1
                if(k == 12):
                    k = 0

            if(moveit == 1):  # hero moving right
                herox += sx(4)
                heropointer += sx(4)
                backx1 -= sx(1)
                backx2 -= sx(1)

            if(herox >= (sx(845, 1))):
                herofallflag = 1
                herofall = 1
                moveit = 0
                flag = 1

            gameDisplay.blit(pillar1, (pillar1x, sy(470)))

            gameDisplay.blit(pillar2, (pillar2x, sy(470)))

            gameDisplay.blit(pillar3, (pillar3x, sy(470)))

            #pygame.draw.circle(gameDisplay,white, (birdxfast+40,400+40) ,3, 2)

            #pygame.draw.circle(gameDisplay,white, (herox+18,heroy+herod+15) ,3, 2)

            # sticklength calculation

            if(flag == 0):

                if(stickx == stickx1):
                    sticklength = abs(sticky - sticky1)
                if(sticky == sticky1):
                    sticklength = abs(stickx1 - stickx)

            # stick fall from Vertical to Horizontal

            if(anglenum > 0 and flag == 1):

                anglenum -= 0.03 * (time) * (time)
                if(anglenum <= 0):
                    kick.stop()
                    landing.play(0)
                    anglenum = 0
                    sticky1 = sy(472)
                    stickx1 = stickx + sticklength
                    # sticklength=stickx1-stickx
                    flag = 0
                    moveit = 1
                    time = 0

                    # 2nd PILLAR DETECTION

                    '''
                    
                    if(pillar1x>429 and pillar1x<840):
                        #acc1=2
                        pillar2nd=pillar1x
                 
                    if(pillar2x>429 and pillar2x<840):
                        #acc2=2
                        pillar2nd=pillar2x
                       
                    if(pillar3x>429 and pillar3x<840):
                        #acc3=2
                        pillar2nd=pillar3x
                    
                    '''

                    # Birds Speed calculation

                    if(sticklength > sx(190, 1) and randint(0, 2) == 0):
                        birdspeed = int(sx(1680) / sticklength)
                        birdspeed += sx(3)
                        birdmainshow = 1
                        chichi.play(0)

                    colortest = gameDisplay.get_at(
                        (int(sx(457, 1) + sticklength + sx(2)), int(heroy + sy(40))))

                    if not((colortest[0] == 0 and colortest[1] == 0 and colortest[2] == 0) or (colortest[0] == 1 and colortest[1] == 1 and colortest[2] == 1)):
                        herofallflag = 1
                    colortest = gameDisplay.get_at(
                        (int(sx(457, 1) + sticklength), int(heroy + sy(30))))

                    if(colortest[0] == 255):
                        perfectflag = 1
                        perfectsound.play()
                        perfect = 1
                        msgx = pillar2nd

                time += 1

            # stick fall from horizontal to bottom

            if(herofall == 1):

                if(anglenum > -90):
                    anglenum -= 0.03 * (time) * (time)

                    # print "hey"

                    if(anglenum <= -90):

                        # print "hey"
                        anglenum = -90
                        sticky1 = sticky + sticklength
                        stickx1 = sx(455, 1)
                        # sticklength=stickx1-stickx
                        # flag=0
                        moveit = 1
                        time = 0

                    time += 1

            # angle calculation

            angle = (pi / 180) * anglenum

            # keypress check

            if(keyinit == 0):

                if keydown_pressed:
                    # jump.play(0)

                    keypressflag = 1
                    keyinit = 1
                    stickgrowsound = 1

            if(keypressflag == 1):

                if keyup_pressed:
                    flag = 1

                    stickgrow.stop()
                    kick.stop()
                    kick.play()

                    kick.play(0)
                    keypressflag = 0

            if(stickgrowsound == 1):

                stickgrow.play(-1)

            '''            
            if(pillar1x>429 and pillar1x<840):
                #acc1=2
                pillar2nd=pillar1x
                    
            if(pillar2x>429 and pillar2x<840):
                #acc2=2
                pillar2nd=pillar2x
                        
            if(pillar3x>429 and pillar3x<840):
                #acc3=2
                pillar2nd=pillar3x
            
            '''

            if(moveit == 1 and heropointer <= (pillar2nd - sx(457, 1))):

                if keydown_pressed and keypress == 0:
                    # jump.play(0)

                    rollupdown.play()
                    upsidedown = not upsidedown

                    keypress = 1

            if keyup_pressed and keypress == 1:

                keypress = 0

            if keypressflag == 1:

                stickgrowsound = 0
                if(sticky1 >= 0):
                    sticky1 -= sy(5)

            # print pillar2nd

            # coordinates calculation while stick free fall

            if(flag == 1):
                sticky1 = sy(472) - sticklength * sin(angle)
                stickx1 = sx(455, 1) + sticklength * cos(angle)

            # zeroing the length of the stick as it surpassed left boundary

            if(stickx <= (sx(349, 1))):

                stickmove = 0
                stickx1 = stickx = sx(455, 1)
                sticky1 = sticky = sy(472)

            if((stickx1 - stickx) != 0 or sticky1 - sticky != 0):
                pygame.draw.line(gameDisplay, black,
                                 (stickx1, sticky1), (stickx, sticky), int(sx(6)))

            # test circles

            #pygame.draw.circle(gameDisplay,white, (herox+30,heroy+30) ,2, 2)
            #pygame.draw.circle(gameDisplay,white, (457+sticklength+2,heroy+30) ,2, 2)

            # if hero has to fall

            if((herox + sx(30)) >= sx(457, 1) + sticklength and herofallflag == 1):
                herofall = 1
                moveit = 0
                flag = 1

            # if hero has to stop
            if((herox + sx(30)) >= sx(457, 1) + sticklength and herofallflag == 0 and moveit == 1 and heroy < sy(768)):

                color = gameDisplay.get_at((int(herox + sx(30 + 4)), int(heroy + sy(40))))

                if not((color[0] == 0 and color[1] == 0 and color[2] == 0) or (color[0] == 1 and color[1] == 1 and color[2] == 1)):
                    moveit = 0
                    pillarmoveflag = 1
                    stickmove = 1

                    if(pillar1x > sx(840, 1)):
                        acc1 = 1
                        acc2 = 0
                        acc3 = 0
                        pillarfast = pillar1x

                    if(pillar2x > sx(840, 1)):
                        acc1 = 0
                        acc2 = 1
                        acc3 = 0
                        pillarfast = pillar2x

                    if(pillar3x > sx(840, 1)):
                        acc1 = 0
                        acc2 = 0
                        acc3 = 1
                        pillarfast = pillar3x

                    '''
                    
                        
                    if(pillar1x>429 and pillar1x<840):
                        #acc1=2
                        pillar2nd=pillar1x
                    
                    if(pillar2x>429 and pillar2x<840):
                        #acc2=2
                        pillar2nd=pillar2x
                        
                    if(pillar3x>429 and pillar3x<840):
                        #acc3=2
                        pillar2nd=pillar3x 
                        
                    
                    '''

                    time = abs((heropointer) / speed)
                    # print heropointer

                    acc = abs(((pillarfast) - (sx(429, 1) + pillardist)) / time)

                    # print
                    # str(((pillarfast)-(429+pillardist)))+str(heropointer)

                    # print pillardist
                    # print heropointer

            if(moveit == 0 and pillarmoveflag == 1):

                if(stickmove == 1):
                    stickx1 -= speed
                    stickx -= speed

                if(heropointer > 0):

                    if(acc1 == 0):
                        pillar1x -= (speed)
                    if(acc2 == 0):
                        pillar2x -= (speed)
                    if(acc3 == 0):
                        pillar3x -= (speed)

                    herox -= speed
                    heropointer -= speed
                    fruitx -= speed
                    # print "help"

                # if(abs(pillarfast-450)>=pillardist):
                    if(acc1 == 1):
                        pillar1x -= (acc)
                        pillarfast = pillar1x

                    if(acc2 == 1):
                        pillar2x -= (acc)
                        pillarfast = pillar2x

                    if(acc3 == 1):
                        pillar3x -= (acc)
                        pillarfast = pillar3x

                else:
                    # if ((heropointer<=0) and
                    # (abs(pillarfast-450)<=pillardist)):

                    landing.stop()
                    scoresound.stop()
                    scoresound.play(0)

                    # print "hello"

                    vanish = 0

                    pillarmoveflag = 0

                    if(lastpillardist < sx(160, 1)):
                        pillardist = randint(int(sx(160, 1)), int(sx(260, 1)))
                        lastpillardist = pillardist
                    else:
                        pillardist = randint(int(sx(100, 1)), int(sx(160, 1)))
                        lastpillardist = pillardist

                    if(score < (10**shift1) - 1):
                        if not(perfectflag == 1):
                            score += 1
                        else:
                            score += 2
                    else:
                        if not(perfectflag == 1):
                            score += 1
                        else:
                            score += 2
                        shift1 += 1
                        scoreshift -= 10

                    if not(fruitscore < (10**shift2) - 1):

                        # fruitscore+=1
                        shift2 += 1
                        fruitscoreshift -= 4

                    perfectflag = 0

                    pillar1x += speed
                    pillar2x += speed
                    pillar3x += (speed)

                    # re-initialization of the variables

                    stickx1 = stickx = sx(455, 1)
                    sticky1 = sticky = sy(472)

                    anglenum = 90
                    angle = (pi / 180) * anglenum

                    sticklength = 0

                    time = 0
                    flag = 0  # stick fall flag
                    keypressflag = 0

                    moveit = 0  # hero move flag

                    herox = sx(429, 1)
                    heroy = sy(442)
                    heropointer = 0

                    i = 0
                    j = 0
                    k = 0

                    fruitgot = False
                    fruitflag = 0

                    herofall = 0
                    herofallflag = 0

                    pillarmoveflag = 0

                    stickmove = 0

                    keyinit = 0
                    flagchk = 0

                    # print fruitx

            if(pillarmoveflag == 0):
                pillarmoveflag = 2

                # print "help"

                if(pillar1 == delta and pillar1x < (sx(415, 1))):
                    pillarfast = pillar1x = randint(int(sx(845, 1)), int(sx(900, 1)))
                    pillar1 = pillarlist[randint(0, 2)]
                    flagchk1 = 1

                if(pillar2 == delta and pillar2x < (sx(415, 1))):
                    pillarfast = pillar2x = randint(int(sx(845, 1)), int(sx(900, 1)))
                    pillar2 = pillarlist[randint(0, 2)]
                    flagchk2 = 1

                if(pillar3 == delta and pillar3x < (sx(415, 1))):
                    pillarfast = pillar3x = randint(int(sx(845, 1)), int(sx(900, 1)))
                    pillar3 = pillarlist[randint(0, 2)]
                    flagchk3 = 1

                if(pillar1x <= (sx(348, 1)) and flagchk1 != 1):
                    pillarfast = pillar1x = randint(int(sx(845, 1)), int(sx(900, 1)))
                    pillar1 = pillarlist[randint(0, 2)]

                if(pillar2x <= (sx(348, 1)) and flagchk2 != 1):
                    pillarfast = pillar2x = randint(int(sx(845, 1)), int(sx(900, 1)))
                    pillar2 = pillarlist[randint(0, 2)]

                if(pillar3x <= (sx(348, 1)) and flagchk3 != 1):
                    pillarfast = pillar3x = randint(int(sx(845, 1)), int(sx(900, 1)))
                    pillar3 = pillarlist[randint(0, 2)]

                # 2nd PILLAR DETECTION

                if(pillar1x > (sx(457, 1)) and pillar1x < (sx(840, 1))):
                    # acc1=2
                    pillar2nd = pillar1x

                if(pillar2x > (sx(457, 1)) and pillar2x < (sx(840, 1))):
                    # acc2=2
                    pillar2nd = pillar2x

                if(pillar3x > (sx(457, 1)) and pillar3x < (sx(840, 1))):
                    # acc3=2
                    pillar2nd = pillar3x

                flagchk1 = flagchk2 = flagchk3 = 0

                # fruit placement

                if((pillar2nd - sx(459, 1)) > (sx(80, 1))):
                    fruitx = randint(int(sx(470, 1)), int(pillar2nd - sx(20 - 8)))

            # print pillar1.rect.topleft

            # left and right black background patches

            pygame.draw.rect(gameDisplay, black, (0, 0, sx(350, 1), sy(768)))

            pygame.draw.rect(gameDisplay, black, (sx(840, 1), 0, sx(693, 1), sy(768)))

            if(herofall == 1 or ext == 1):

                if(ext != 1):
                    heroy += sy(15)

                if(heroy > (sy(770)) or ext == 1):

                    landing.stop()
                    dead.stop()
                    dead.play()
                    #rect = pygame.Rect(350, 0, 490, 768)
                    #sub = gameDisplay.subsurface(rect)
                    #pygame.image.save(sub, "screenshot/screenshot.png")

                    a = scorescreen()
                    catch = a.make(gameDisplay, back, score, fruitscore)

                    if(catch == 1 or catch ==0):

                        # VARIABLE INITIALIZATION

                        stickx1 = stickx = sx(455, 1)
                        sticky1 = sticky = sy(472)

                        anglenum = 90
                        angle = (pi / 180) * anglenum

                        sticklength = 0

                        time = 0
                        flag = 0  # stick fall flag
                        keypressflag = 0

                        moveit = 0  # hero move flag

                        herox = sx(429, 1)
                        heroy = sy(442)

                        heropointer = 0

                        i = 0
                        j = 0
                        k = 0

                        pillar1x = sx(355, 1)
                        msgx = pillar2x = sx(650, 1)
                        pillar3x = randint(int(sx(845, 1)), int(sx(900, 1)))

                        pillar1 = alpha
                        pillar2 = beta
                        pillar3 = pillarlist[randint(0, 2)]

                        herofall = 0
                        herofallflag = 0

                        pillarmoveflag = 0

                        stickmove = 0

                        ackx = 0

                        pillarfound = 0

                        score = 0

                        keyinit = 0

                        ext = 0

                        speed = sx(8)

                        acc1 = acc2 = acc3 = 0

                        pillarfast = 0

                        pillardist = randint(int(sx(60, 1)), int(sx(260, 1)))
                        lastpillardist = pillardist

                        stickgrowsound = 0

                        back = backgroundlist[randint(0, 6)]

                        keypress = 0

                        backx1 = sx(350, 1)
                        backx2 = sx(1630, 1)

                        upsidedown = False

                        '''
        
                        if(pillar1x>429 and pillar1x<840):
                            #acc1=2
                            pillar2nd=pillar1x
                    
                        if(pillar2x>429 and pillar2x<840):
                            #acc2=2
                            pillar2nd=pillar2x
                        
                        if(pillar3x>429 and pillar3x<840):
                            #acc3=2
                            pillar2nd=pillar3x 
                            
                        '''

                        bouncedown = True
                        bounce = 0

                        fruitx = 0

                        fruitgot = False
                        fruitflag = 0

                        herod = sy(33)

                        fruitscore = 0
                        score = 0

                        scoreshift = 0
                        fruitscoreshift = 0
                        shift1 = 1
                        shift2 = 1

                        perfectflag = 0
                        vanish = 0
                        perfect = 0
                        b1 = 0
                        b2 = 2
                        b3 = 4
                        b4 = 6

                        birdx = sx(900, 1)
                        birdxslow = sx(950, 1)
                        birdxfast = sx(860, 1)

                        birdgroupshow = 0
                        birdsingleshow = 0
                        birdmainshow = 0
                        birdpickup = 0
                        birdsound = 0

                        flagchk1 = flagchk2 = flagchk3 = 0

                        flagchk = 0

            #pygame.draw.circle(gameDisplay,white,(pillar2nd,700) ,3, 2)

            pygame.display.update()
            clock.tick(60)

            if crashed == True:                                   # Game crash or Close check
                pygame.quit()
                sys.exit()

        # Just a window exception check condition

        event1 = pygame.event.get()
        if event1.type == pygame.QUIT:
            crashed = True

        if crashed == True:
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    g = game()
    g.make()
