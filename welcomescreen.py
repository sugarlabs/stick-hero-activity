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
from rules import rulescreen, sx, sy, display_init


class welcomescreen:

    def make(self, gameDisplay, back):

        gameDisplay = display_init()
        sound = True

        try:
            pygame.mixer.init()
        except Exception as err:
            sound = False
            print(_('error with sound'), err)

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
            # gameicon=pygame.image.load('data/images/icon.png')
            # pygame.display.set_icon(gameicon)

        fruit = pygame.image.load("images/welcomescreen/fruit.png")
        fruit = pygame.transform.scale(fruit, (int(sx(40)), int(sy(40))))

        scoreplate = pygame.image.load("images/scoreplate.png").convert()
        scoreplate = pygame.transform.scale(scoreplate, (int(sx(40)), int(sy(50))))

        scoreplate.set_alpha(100)

        help = pygame.image.load("images/help.png")
        help = pygame.transform.scale(help, (int(sx(40)), int(sy(40))))

        hero = pygame.image.load("images/hero.png")
        hero = pygame.transform.scale(hero, (int(sx(38)), int(sy(38))))

        play = pygame.image.load("images/play.png")
        play = pygame.transform.scale(play, (int(sx(170)), int(sy(170))))

        beta = pygame.image.load("images/alpha.png")
        beta = pygame.transform.scale(beta, (int(sx(105)), int(sy(248))))

        # herotr=hero

        # herotr=pygame.transform.scale(hero,(30,26))

        # hero1=pygame.image.load("images/hero1.png")

        font_path = "fonts/Arimo.ttf"
        font_size = int(sx(70))
        font1 = pygame.font.Font(font_path, font_size)
        font2 = pygame.font.Font("fonts/Arimo.ttf", int(sx(15)))
        font3 = pygame.font.Font("fonts/Arimo.ttf", int(sx(40)))
        font4 = pygame.font.Font("fonts/Arimo.ttf", int(sx(20)))

        down = 1
        bounce = 0
        i = 0

        maxscore = 0
        fruitmaxscore = 0
        score_path = os.path.join(get_activity_root(), 'data', 'score.pkl')

        if os.path.getsize(score_path) == 0:

            with open(score_path, 'wb') as output:
                pickle.dump(maxscore, output, pickle.HIGHEST_PROTOCOL)
                pickle.dump(fruitmaxscore, output, pickle.HIGHEST_PROTOCOL)

        with open(score_path, 'rb') as input:  # REading
            maxscore = pickle.load(input)
            fruitmaxscore = pickle.load(input)

        # GAME LOOP BEGINS !!!

        while not crashed:
            # Gtk events
            mouse_button_up = False

            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                # totaltime+=timer.tick()
                if event.type == pygame.QUIT:
                    crashed = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_button_up = True

            mos_x, mos_y = pygame.mouse.get_pos()

            # print event

            i += 1

            if(i > 20):
                i = 0

            if(i % 3 == 0):
                if(down == 1):
                    bounce += 1
                    if(bounce > 8):
                        down = 0
                if(down == 0):
                    bounce -= 1
                    if(bounce < 0):
                        down = 1

            gameDisplay.fill(white)
            gameDisplay.blit(back, (sx(350, 1), 0))

            # scoreplate.set_alpha(20)
            # gameDisplay.blit(scoreplate,(540,40))

            gameDisplay.blit(help, (sx(380, 1), sy(20)))
            # score blitting
            gameDisplay.blit(play, (sx(510, 1), sy(200 + bounce)))

            gameDisplay.blit(beta, (sx(540, 1), sy(470)))

            gameDisplay.blit(hero, (sx(568, 1), sy(432)))

            # score check

            if fruit.get_rect(center=(sx(790 + 20, 1), sy(20 + 20))).collidepoint(mos_x, mos_y):
                if(pygame.mouse.get_pressed())[0] == 1 and press == 0:

                    gameDisplay.blit(scoreplate, (sx(780, 1), sy(40)))
                    # gameDisplay.blit(scoreplate,(780,60))

                    head1 = font2.render(_(str(fruitmaxscore)), 1, (white))
                    gameDisplay.blit(head1, (sx(785, 1), sy(60)))

                if mouse_button_up:
                    press = 0

            # GAME START

            if play.get_rect(center=(sx(510 + 85, 1), sy(200 + bounce + 85))).collidepoint(mos_x, mos_y):
                if(pygame.mouse.get_pressed())[0] == 1 and press == 0:

                    return 2

                '''
                if event.type==pygame.MOUSEBUTTONUP:
                    press=0

                '''

            # Help menu

            if help.get_rect(center=(sx(380 + 20, 1), sy(20 + 20))).collidepoint(mos_x, mos_y):
                if(pygame.mouse.get_pressed())[0] == 1 and press == 0:

                    a = rulescreen()
                    catch = a.make(gameDisplay)

                    if(catch == 0):
                        return 2

                '''

                if event.type==pygame.MOUSEBUTTONUP:
                    press=0
                '''

            gameDisplay.blit(fruit, (sx(780, 1), sy(20)))

            head1 = font1.render(_("STICK"), 1, (black))
            gameDisplay.blit(head1, (sx(500, 1), sy(20)))

            head2 = font1.render(_("HERO"), 1, (black))
            gameDisplay.blit(head2, (sx(510, 1), sy(80)))

            # fruitscores=font2.render(str(fruitscore),1,(0,0,0))
            # gameDisplay.blit(fruitscores,(770+fruitscoreshift,13))

            # left and right black background patches

            pygame.draw.rect(gameDisplay, black, (0, 0, sx(350, 1), sy(768)))

            pygame.draw.rect(gameDisplay, black, (sx(840, 1), 0, sx(693, 1), sy(768)))

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
