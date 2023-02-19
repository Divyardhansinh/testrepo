import pygame
pygame.init()

#set color with rgb
white,black,red = (255,255,255),(0,0,0),(255,0,0)

#set display
gameDisplay = pygame.display.set_mode((800,600))

#caption
pygame.display.set_caption("ChessBoard")

#beginning of logic
gameExit = False

lead_x = 20
lead_y = 20

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

#For loop for chessboard

#draw a rectangle
gameDisplay.fill(white)
pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,20,20])
pygame.display.update()


#quit from pygame & python
pygame.quit()
quit()