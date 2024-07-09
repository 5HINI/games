import pygame
import random 

pygame.init()

window = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Snake Game")
pyicon = pygame.image.load("icon.png")
pygame.display.set_icon(pyicon)
clock = pygame.time.Clock()
with open("hs.txt", "r") as file:
    highscore = int(file.read())
game_running = True
backms = pygame.mixer.music.load("back.mp3")
pygame.mixer.music.play(-1)
overms = pygame.mixer.Sound("over.wav")
scorems = pygame.mixer.Sound("score.wav")
background = pygame.image.load("back.png")
background = pygame.transform.scale(background, (720, 720))
snake_head = pygame.image.load("snake_head.png")
snake_head = pygame.transform.scale(snake_head, (40, 40))
snake_tail = pygame.image.load("snake_tail.png")
snake_tail = pygame.transform.scale(snake_tail, (20, 20))
snake_body = pygame.image.load("snake_body.png")
snake_body = pygame.transform.scale(snake_body, (40, 40))
apple = pygame.image.load("apple.png")
apple = pygame.transform.scale(apple, (40, 40))

def gameloop():
    global highscore, game_running, backms, overms, scorems, background, snake_body, snake_head, snake_tail, apple
    score = 0
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    char_x = 360
    char_y = 360
    char_size_x = 40
    char_size_y = 40
    fps = 30
    velocity = [0, 0]
    uelocity = 5
    food_x = random.randint(100, 620)
    food_y = random.randint(100, 620)
    food_size_x = 40
    food_size_y = 40
    font = pygame.font.SysFont(None, 40)
    lenght = 1
    char_list = []
    game_over = False

    while game_running:
        if game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                    with open("hs.txt", "w") as file:
                        file.write(f"{highscore}")
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                if event.type == pygame.KEYDOWN:       
                    if event.key == pygame.K_RIGHT:
                        velocity = [uelocity, 0]
                    if event.key == pygame.K_UP:
                        velocity = [0, -uelocity]
                    if event.key == pygame.K_LEFT:
                        velocity = [-uelocity, 0]
                    if event.key == pygame.K_DOWN:
                        velocity = [0, uelocity]

            char_x += velocity[0]
            char_y += velocity[1]
            if abs(char_x - food_x) < 10 + lenght and abs(char_y - food_y) < 10 + lenght:
                score += 1
                scorems.play()
                if score > highscore:
                    highscore = score
                lenght += 1
                uelocity += 1
                food_x = random.randint(100, 620)
                food_y = random.randint(100, 620)

            window.fill(black)
            window.blit(background, [0, 0])
            scoreboard = font.render(f"Score: {score}        Highscore: {highscore}", True, white)
            window.blit(scoreboard, [0, 0])
            head = [char_x, char_y, 40, 40]
            char_list.append(head)
            if len(char_list) > lenght:
                del char_list[0]
            for i, pos in enumerate(char_list):
                if i == len(char_list) - 1:
                    window.blit(snake_head, pos)
                elif i == 0:
                    window.blit(snake_tail,[pos[0]+10, pos[1]+10])
                else:
                    window.blit(snake_body, pos)
            window.blit(apple, [food_x, food_y, food_size_x, food_size_y])
            if char_x > 720 or char_x < 0 or char_y > 720 or char_y < 0 or head in char_list[:-1]:
                game_over = True
                overms.play()
                window.fill(black)
                window.blit(background, [0, 0])
                over = font.render(f"Game Over!!    Your score: {score}     press space to restart", True, white)
                window.blit(over, [0, 360])
            pygame.display.update()
            clock.tick(fps)

gameloop()
pygame.quit()
quit()