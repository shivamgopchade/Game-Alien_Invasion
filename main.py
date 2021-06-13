import sys
import pygame
from pygame.sprite import Group
from alien_invasion.settings import Settings
from alien_invasion.ship import Ship
import alien_invasion.game_funcns as gf
from alien_invasion.game_stats import GameStats
#from alien_invasion.alien import Alien

def rungame():

    ai_settings=Settings()
    pygame.init()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion!!")

    stats=GameStats(ai_settings)
    #make a ship,grp. of bullets n grp.of alien

    ship=Ship(ai_settings,screen)
    bullets=Group()
    aliens=Group()

    gf.create_fleet(ai_settings,screen,ship,aliens)

    #alien=Alien(ai_settings,screen)


    while True:
        gf.check_events(ai_settings,screen,ship,bullets)

        if stats.game_active:
            ship.update()

            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
        #gf.update_screen(ai_settings,screen,ship,alien,bullets)
        #gf.update_aliens(ai_settings,ship,aliens)

        #gf.update_screen(ai_settings,screen,ship,aliens,bullets)
rungame()