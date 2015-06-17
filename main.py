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
import gtk
import pickle
import pygame
import sys

from math import *



class game:

    def make(self):
        
        pygame.init()
        sound=True
        
        try:
            pygame.mixer.init()
        except Exception, err:
            sound=False
            print 'error with sound', err
            
        black=(0,0,0)
        white=(255,255,255)
        clock=pygame.time.Clock()
        timer=pygame.time.Clock()
            
        crashed=False   
        disp_width = 600
        disp_height = 600
            
        press=0    
        
        info=pygame.display.Info()
        gameDisplay=pygame.display.get_surface()
        
        
        if not(gameDisplay):
            
            gameDisplay = pygame.display.set_mode((info.current_w,info.current_h))
            
            #pygame.display.set_caption("Stick Hero")
            #gameicon=pygame.image.load('data/images/icon.png')
            #pygame.display.set_icon(gameicon)
            
            
        hero=pygame.image.load("images/hero.png")
        stick=pygame.image.load("images/stick.png")
        background=pygame.image.load("images/background.png")
        alpha=pygame.image.load("images/alpha.png")
        
        #stickx1=455
        #sticky1=50
        
        stickx1=stickx=455
        sticky1=sticky=470
        
        anglenum=90
        angle=(pi/180)*anglenum
        
        sticklength=0
        
        time=0
        flag=0
        keypressflag=0
        
        while not crashed:
        #Gtk events
            
            while gtk.events_pending():
                gtk.main_iteration()
            event=pygame.event.poll()
            #totaltime+=timer.tick()
            if event.type == pygame.QUIT:
                crashed=True
                
            
            mos_x,mos_y=pygame.mouse.get_pos() 
            
            #print event
            
                
            gameDisplay.fill(white)
            gameDisplay.blit(background,(350,0))
            
            gameDisplay.blit(hero,(420,443))
            
            
            #gameDisplay.blit(stick,(455,sticky1))
            
            gameDisplay.blit(alpha,(355,470))
            
            
            
            
            
            
            
            
            
            if(flag==0):
                sticklength=sticky-sticky1
            
            if(anglenum>=0 and flag==1 ):
                
                anglenum-=0.03*(time)*(time)
                if(anglenum<0):
                    
                    anglenum=0
                    sticky1=470
                    stickx1=stickx+sticklength
                    flag=0
                #if(anglenum<0):
                #    break
                
                #if(anglenum>85):
                time+=1
            
            angle=(pi/180)*anglenum
            
            if event.type==pygame.KEYDOWN and event.key==273:
                #jump.play(0)
                
                keypressflag=1
              
              
            if keypressflag==1:  
                
                sticky1-=5
                #print sticky1
                #print "hello"
                
                
                
            if event.type==pygame.KEYUP  and event.key==273:
                flag=1
                keypressflag=0
                #print "fuck"
                
            
            #print event
            #print sticklength
            #print stickx1
            
            
            
            if(flag==1):
                sticky1=470-sticklength*sin(angle)
                stickx1=455+sticklength*cos(angle)
            
            pygame.draw.line(gameDisplay,black,(stickx1,sticky1), (stickx,sticky), 6)
            
            print str(stickx1)+" "+str(sticky1)
            
            #print event
            
            '''
            if event.type==pygame.KEYDOWN and event.key==273 and f1==0:
                jump.play(0)
                f1=1
                m1=1
            '''
            
            
            
            pygame.display.update()
            clock.tick(60)
     
            if crashed==True:                                   # Game crash or Close check
                pygame.quit()
                sys.exit()
     
     
     
     
        # Just a window exception check condition

        event1=pygame.event.get()                                 
        if event1.type == pygame.QUIT:
            crashed=True
   
        if crashed==True:
            pygame.quit()
            sys.exit()
            

if __name__ == "__main__":
    g = game()
    g.make()         

            