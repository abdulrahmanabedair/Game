import pygame
import players
import display
pygame.init()

run = True

while run:
    display.screen.fill((0,0,0))
    #this fill The screen in a color
    pygame.draw.rect(display.screen, (255, 0, 0), players.player)
    pygame.draw.rect(display.screen, (0, 0, 255), players.player2)
    #Make player on display
    key = pygame.key.get_pressed()
    #adds keys like arows or normal
    if key[pygame.K_a] == True:
        players.player.move_ip(-1,0)
    #makes player move
    elif key[pygame.K_d] == True:
        players.player.move_ip(1,0)
    elif key[pygame.K_w] == True:
        players.player.move_ip(0,-1)
    elif key[pygame.K_s] == True:
        players.player.move_ip(0,1)
    if key[pygame.K_LEFT] == True:
        players.player2.move_ip(-1,0)
    elif key[pygame.K_RIGHT] == True:
        players.player2.move_ip(1,0)
    elif key[pygame.K_UP] == True:
        players.player2.move_ip(0,-1)
    elif key[pygame.K_DOWN] == True:
        players.player2.move_ip(0,1)
    # --- Add this line to keep the player inside the screen boundaries ---
    players.player.clamp_ip(display.screen.get_rect())
    players.player2.clamp_ip(display.screen.get_rect())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    #update Display
pygame.quit()