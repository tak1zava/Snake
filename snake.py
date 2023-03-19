import random
import time

import pygame

pygame.init()
dis_width = 400
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake game')

black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 125, 50)
white = (255, 255, 255)
green = (0, 255, 0)

snake_block = 10
snake_speed = 10

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 15)
score_font = pygame.font.SysFont("comicsansms", 35)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [10, dis_height / 3])

def your_score(score):
    value = score_font.render("Your score: {}".format(score), True, orange)
    dis.blit(value, [0, 0])

def snake_tail(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def game_loop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
    foody = round(random.randrange(0, dis_height - snake_block) / 10) * 10

    while not game_over:

        while game_close:
            dis.fill(white)

            message("You lost! Press Q to quit or R to play again!", red)
            your_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= dis_width or x1 < 0 or y1 >= dis_width or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(white)

        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake_tail(snake_block, snake_list)
        your_score(snake_length - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            snake_length += 1

            foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
            foody = round(random.randrange(0, dis_height - snake_block) / 10) * 10

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
