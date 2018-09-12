#!/bin/bash
######################################################################
# .____                  _____    _________ __                       # 
# |    |    ____ _____ _/ ____\  /   _____//  |_  ___________ ___.__.# 
# |    |  _/ __ \\__  \\   __\   \_____  \\   __\/  _ \_  __ <   |  |# 
# |    |__\  ___/ / __ \|  |     /        \|  | (  <_> )  | \/\___  |# 
# |_______ \___  >____  /__|    /_______  /|__|  \____/|__|   / ____|# 
#        \/   \/     \/                \/                    \/      #  
######################################################################
#    A simple game that I've constructed to showcase my skills       #
#      as a programmer. The artwork used is opensource, the          #
#      music is self composed and it used python and pygame, as      #   
#      well as PyTMX for tilemap loading.                            # 
#                                                                    # 
#                                                                    #
#                                                                    #
#                                                                    #
#                                                                    #  
#                                                                    # 
#                                                                    # 
#                                                                    # 
#                                                                    #
#                                                                    # 
#                                                                    #
#                                                                    # 
#                                                                    #
#                                                                    # 
#                                                                    # 
######################################################################
from Globals import *
from GameStateManager import *
from Background import *
from TiledMap import *
from Foreground import *
from Player import *
from Camera import *
from MainMenu import *
from NPC import *
from Shopkeeper import *
from DialogueManager import *


def main():
    screen = pygame.display.set_mode((640, 480),pygame.HWSURFACE)
    gsm = GameStateManager()
    isRunning = True
    clock = pygame.time.Clock()
    menu = MainMenu(gsm)
    gsm.set_state("s_main_menu")
    player = Player(0, 0, 32, 32, 0)    
    player.walls = collision_sprite
    font_renderer = pygame.font.SysFont('Comic Sans MS', 29)
    player.entrance = entrance_sprite
    camera = Camera(player)
    player.set_camera_object(camera)
    background = Background('./assets/background.png')
    tiledMap = TiledMap("./assets/beginning.tmx", player, "", font_renderer)
    foreground = Foreground("./assets/beginning.tmx", "Foreground", foreground_layer)
    while isRunning:
        clock.tick(FPS)
        if(gsm.currentState == "s_main_menu"):
            #main menu state
            #gsm.set_state("s_main_game")
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    isRunning = False
                menu.update(event)
            menu.draw(screen)
        elif(gsm.currentState == "s_credits"):
            print("Made by John Padilla")
            gsm.set_state("s_main_menu")
        elif(gsm.currentState == "s_paused"):
            pass
        #hhave a class that controls everything
        elif(gsm.currentState == "s_main_game"):
            screen.fill((255, 255, 255))
            #####################################
            for event in pygame.event.get():
                for ent in shopkeeper_sprite:
                    ent.set_event(event)
                if event.type == pygame.QUIT:
                    isRunning = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        isRunning = False
                    
                    player.update_keypressed(event, "test")
                if event.type == pygame.KEYUP:
                    player.update_keyup(event)
            #####################################
            camera.update(background, tiledMap, foreground)
            for ent in player_sprite:
                ent.update(background, tiledMap, foreground)
            for ent in bullet_sprite:
                ent.update()
            for ent in shopkeeper_sprite:
                ent.update(player, font_renderer)
            for ent in skeleton_sprite:
                ent.update(player)
            for ent in lava_sprite:
                ent.update(player)
            for ent in money_sprite:
                ent.update(player)
            for ent in fireball_sprite:
                ent.update(player)
            #####################################
            background_layer.draw(screen)
            #player_sprite.draw(screen)
            tiled_layer.draw(screen)
            player_sprite.draw(screen)
            foreground_layer.draw(screen)
            player.draw_gui(screen, font_renderer)
            bullet_sprite.draw(screen)
            shopkeeper_sprite.draw(screen)
            money_sprite.draw(screen)
            for sprite in shopkeeper_sprite:
                sprite.render_text(screen, font_renderer, camera)
            skeleton_sprite.draw(screen)
            for sprite in shopkeeper_sprite:
                if sprite.shopMenu.show:
                    shopmenu_sprite.draw(screen)
            fireball_sprite.draw(screen)
            pygame.display.flip()
    pygame.quit()

if __name__ == "__main__": main()















