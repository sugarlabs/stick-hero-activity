#!/usr/bin/env python
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
from rules import *


class welcomescreen:

    def make(self, gameDisplay, back, mainGame):

        sound = True

        black = (0, 0, 0)
        white = (255, 255, 255)
        clock = pygame.time.Clock()
        timer = pygame.time.Clock()

        disp_width = 600
        disp_height = 600

        press = 0

        info = pygame.display.Info()
        gameDisplay = pygame.display.get_surface()

        if not(gameDisplay):

            gameDisplay = pygame.display.set_mode(
                (info.current_w, info.current_h))

            pygame.display.set_caption(_("Stick Hero"))
            # gameicon=pygame.image.load('data/images/icon.png')
            # pygame.display.set_icon(gameicon)

        fruit = pygame.image.load("images/welcomescreen/fruit.png")
        fruit = pygame.transform.scale(fruit, (40, 40))

        scoreplate = pygame.image.load("images/scoreplate.png").convert()
        scoreplate = pygame.transform.scale(scoreplate, (40, 50))

        scoreplate.set_alpha(100)

        play = pygame.image.load

        help = pygame.image.load("images/help.png")
        help = pygame.transform.scale(help, (40, 40))

        hero = pygame.image.load("images/hero.png")
        hero = pygame.transform.scale(hero, (38, 38))

        play = pygame.image.load("images/play.png")
        play = pygame.transform.scale(play, (170, 170))

        beta = pygame.image.load("images/alpha.png")

        # herotr=hero

        # herotr=pygame.transform.scale(hero,(30,26))

        # hero1=pygame.image.load("images/hero1.png")

        font_path = "fonts/Arimo.ttf"
        font_size = 70
        font1 = pygame.font.Font(font_path, font_size)
        font2 = pygame.font.Font("fonts/Arimo.ttf", 15)
        font3 = pygame.font.Font("fonts/Arimo.ttf", 40)
        font4 = pygame.font.Font("fonts/Arimo.ttf", 20)

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

        while not mainGame.crashed:
            # Gtk events

            while Gtk.events_pending():
                Gtk.main_iteration()
            
            event = pygame.event.poll()
            # totaltime+=timer.tick()
            if event.type == pygame.QUIT:
                return

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
            gameDisplay.blit(back, (350, 0))

            # scoreplate.set_alpha(20)
            # gameDisplay.blit(scoreplate,(540,40))

            gameDisplay.blit(help, (380, 20))
            # score blitting
            gameDisplay.blit(play, (510, 200 + bounce))

            gameDisplay.blit(beta, (540, 470))

            gameDisplay.blit(hero, (568, 432))

            # score check

            if fruit.get_rect(center=(790 + 20, 20 + 20)).collidepoint(mos_x, mos_y):
                if(pygame.mouse.get_pressed())[0] == 1 and press == 0:

                    gameDisplay.blit(scoreplate, (780, 40))
                    # gameDisplay.blit(scoreplate,(780,60))

                    head1 = font2.render(_(str(fruitmaxscore)), 1, (white))
                    gameDisplay.blit(head1, (785, 60))

                if event.type == pygame.MOUSEBUTTONUP:
                    press = 0

            # GAME START

            if play.get_rect(center=(510 + 85, 200 + bounce + 85)).collidepoint(mos_x, mos_y):
                if(pygame.mouse.get_pressed())[0] == 1 and press == 0:

                    return 2

                '''
                if event.type==pygame.MOUSEBUTTONUP:
                    press=0

                '''

            # Help menu

            if help.get_rect(center=(380 + 20, 20 + 20)).collidepoint(mos_x, mos_y):
                if(pygame.mouse.get_pressed())[0] == 1 and press == 0:

                    a = rulescreen()
                    catch = a.make(gameDisplay, mainGame)

                    if(catch == 0):
                        return 2

                '''

                if event.type==pygame.MOUSEBUTTONUP:
                    press=0
                '''

            gameDisplay.blit(fruit, (780, 20))

            head1 = font1.render(_("STICK"), 1, (black))
            gameDisplay.blit(head1, (500, 20))

            head2 = font1.render(_("HERO"), 1, (black))
            gameDisplay.blit(head2, (510, 80))

            # fruitscores=font2.render(str(fruitscore),1,(0,0,0))
            # gameDisplay.blit(fruitscores,(770+fruitscoreshift,13))

            # left and right black background patches

            pygame.draw.rect(gameDisplay, black, (0, 0, 350, 768))

            pygame.draw.rect(gameDisplay, black, (840, 0, 693, 768))

            pygame.display.update()
            clock.tick(60)
