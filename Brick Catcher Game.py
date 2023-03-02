import pygame
import random


def get_highscore():
    with open("BrickCatcherHighscores.txt", "r+") as f:
        return f.read()

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catcher game")

clock = pygame.time.Clock()

boardX = 370
boardY = 530
board_length = 100
board = pygame.Rect(boardX, boardY, board_length, 10)
board_speed = 10

squareX = random.randrange(0, 750, 10)
squareY = 0
square = pygame.Rect(squareX, squareY, 20, 20)
square_speed = 5


score = 0

def Game():
    global board, square, score

    FPS_num = clock.get_fps()

    pygame.draw.rect(screen, (255, 255, 255), board)
    pygame.draw.rect(screen, (255, 255, 255), square)

    font = pygame.font.Font("freesansbold.ttf", 32)
    highScoreText = font.render("High Score: " + get_highscore(), True, (255, 255, 255))
    scoreText = font.render("Score: " + str(score), True, (255, 255, 255))
    FPS = font.render("FPS: " + str(round(FPS_num)), True, (255, 255, 255))
    screen.blit(scoreText, (0, 30))
    screen.blit(highScoreText, (0, 64))
    screen.blit(FPS, (0, 100))

    if isCollision(board, square):
        square.x = random.randrange(0, 750, 10)
        square.y = 0

    if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
        board.x += -board_speed
    if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
        board.x += board_speed
    square.y += square_speed

    if board.x >= 730:
        board.x = 730
    if board.x <= 0:
        board.x = 0
    if square.y >= screen_height:
        Change_Highscore(score)
        gameOver()

def Change_Highscore(score):
    if score > int(get_highscore()):
        highscore = open("BrickCatcherHighscores.txt", "w")
        highscore.write(str(score))
        highscore.close()

def isCollision(player, box):
    global score, square_speed, board_speed
    if player.colliderect(box):
        score += 1
        square_speed += 1
        board_speed += 1
        return True

def gameOver():
    global running, score
    font = pygame.font.Font("freesansbold.ttf", 32)
    gameOverText = font.render("GAME OVER!", True, (255, 255, 255))
    playAgainText = font.render("Play again(Y/N)?", True, (255, 255, 255))

    screen.blit(playAgainText, ((screen_width // 2) - 135, (screen_height // 2) + 50))
    screen.blit(gameOverText, ((screen_width//2) - 120 , (screen_height//2 - 100)))

    if pygame.key.get_pressed()[pygame.K_y]:
        Reset()
    elif pygame.key.get_pressed()[pygame.K_n]:
        running = False

def Reset():
    global board, square, board_speed, boardX, boardY, squareX, score, squareY, square_speed
    boardX = 370
    boardY = 530
    board = pygame.Rect(boardX, boardY, board_length, 10)
    board_speed = 10

    squareX = random.randrange(0, 750, 10)
    squareY = 0
    square = pygame.Rect(squareX, squareY, 20, 20)
    square_speed = 5

    score = 0

running = True

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Game()
    pygame.display.update()
    clock.tick(60)