# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:31:21 2020

@author: hcbarnet
"""
##https://www.youtube.com/watch?v=sHwWSFQqGBM
import pygame
from random import randint

pygame.mixer.init()
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1)

all_fonts = pygame.font.get_fonts()
s_width = 600
s_height = 600

image_height = 30
image_width = 40

top_left_x = s_width // 2
top_left_y = s_height

sky_blue = (204,255,255)
white = (255,255,255)
red = (255, 102, 102)
pygame.init()
##set screen to 1000,600
surface = pygame.display.set_mode((s_width, s_height))
##name the game
pygame.display.set_caption('When Pigs Can Fly')
##Set the time clock
clock = pygame.time.Clock()

#load in the pig I made! woo
img = pygame.image.load('flyingpigsmall.png')
#variables for start point



def playDing():
	pygame.mixer.init()
	ding = pygame.mixer.Sound('ding.wav')
	ding.play()
	

def score(count):
    font = pygame.font.SysFont(all_fonts[0], 20)
    text = font.render("Score: " + str(count), True, (0,0,0))
    surface.blit(text, [0,0])

    

def blocks(x_block, y_block, block_width, block_height, gap):
    pygame.draw.rect(surface, red, [x_block, y_block, block_width, block_height])
    pygame.draw.rect(surface, red, [x_block, y_block+block_height+gap, block_width, s_height])

def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main()
        else:
            return None

def make_text_object(text, font):
    text_surface = font.render(text, True, (0,0,0))
    return text_surface, text_surface.get_rect()
    
def msg_surface(text, count=0):
    last_score = max_score()
    small_text = pygame.font.SysFont(all_fonts[0], 20)
    large_text =  pygame.font.SysFont(all_fonts[0], 90)
    
    title_text_surface, title_text_rect = make_text_object(text, large_text)
    title_text_rect.center = s_width/2, s_height/2
    surface.blit(title_text_surface, title_text_rect)
    
    typical_text_surface, typical_text_rect = make_text_object('PRESS THE UP KEY TO PLAY AGAIN', small_text)
    typical_text_rect.center = s_width/2, ((s_height/2) + 100)
    surface.blit(typical_text_surface, typical_text_rect)
    
    score_text_surface, score_text_rect = make_text_object('FINAL SCORE: ' + str(count) + ' POINTS        ', small_text)
    score_text_rect.center = s_width/2, ((s_height/2) + 150)
    surface.blit(score_text_surface, score_text_rect)
    
    score_text_surface, score_text_rect = make_text_object('HIGH SCORE: ' + str(last_score) + ' POINTS        ', small_text)
    score_text_rect.center = s_width/2, ((s_height/2) + 200)
    surface.blit(score_text_surface, score_text_rect)
    
    pygame.display.update()
    pygame.time.wait(3000)
    
    ##if user does nothing
    while replay_or_quit() == None:
        clock.tick()

 
    main()
 
def update_score(nscore):
    score = max_score()
    with open('scores.txt', 'w') as f:
        if int(score) > nscore:
            f.write(str(score))
        else:
            f.write(str(nscore))


def max_score():
    with open('scores.txt', 'r') as f:
        lines = f.readlines()
        score = lines[0].strip()

    return score


    
def game_over(count):
    pygame.mixer.init()
    game_over = pygame.mixer.Sound('game-over.ogg')
    game_over.play()
    msg_surface('GAME OVER', count)

    
	
    
    
	
    

def flying_pig(x,y,image):
    surface.blit(img, (x,y))


def main():
    
    x = 150
    y = 200
    y_move = 0
    
    x_block = s_width
    y_block = 0
    
    block_width = 75
    block_height = randint(50, (s_height/2))
    gap = image_height * 3.5
    block_move = 3
    run = False
    current_score = 0
    
    while not run:
        
        for event in pygame.event.get():
            ##user hits the x, stop loop
            if event.type == pygame.QUIT:
                run = True
            ##user events press the key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    #negative is up
                    y_move = -5
            ##user event not pressing a key
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    #negative is up
                    y_move = 5
        y += y_move
        
        
        ##fill a background color
        surface.fill(sky_blue)
        ##add the pig!
        flying_pig(x, y, img)
        
        blocks(x_block, y_block, block_width, block_height, gap)
        x_block -= block_move
        
        ##set bounbaries dont want to go too high, or too low
        if y > (s_height - 43):
            y = s_height - 43
        
        if y < 6:
            y = 6
            
        if x_block < (-1*block_width):
            x_block = s_width
            block_height = randint(0, (s_height/2))
            current_score = current_score + 1
            pygame.display.update()

        if x_block <= ((-1*block_width)+(image_width*2)):
        	playDing()
            
            
            
        ##Upper bar            
        if x + image_width > x_block:
            if x < x_block + block_width:
                if y < block_height:
                    if x- image_width < block_width + x_block:
                        game_over(current_score)
                        
			
                        
                        
        
        if x + image_width > x_block:
            if y + 35 > block_height+gap:
                if x < block_width + x_block:
                    game_over(current_score)
                    
                    
               
                    
        
             
        score(current_score)
        ##sets the frames per loop
        pygame.display.update()
        clock.tick(60)
        update_score(current_score)

main()
pygame.quit()
quit()
