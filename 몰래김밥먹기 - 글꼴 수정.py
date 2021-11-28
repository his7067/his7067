import pygame, sys, time, random
from time import sleep

clock = pygame.time.Clock()
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height)) #화면 크기

sound = pygame.mixer.Sound("사운드/music.mp3")
sound.play(-1)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
YELLOWGREEN = (128, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PUPPLE = (128, 0, 255)

student_posX = 50#학생 위치
student_posY = 100
professor_posX = 200#교수 위치
professor_posY = 200

#점수 관련 변수
score = 0
high_Score = 0

start_time = int(time.time())   #시작 시간

hungryPoint = 50
thirstPoint = 50
comeAcross = False

eating = False
drinking = False

isNeedToRestart = False

studentCount = 0
drinkingCount = 0

remain_second = -2   #교수님 뒤 도는 타이머 변수

professor = [pygame.image.load("이미지/교수_수업.png"), pygame.image.load("이미지/교수_돌아보기.png"), pygame.image.load("이미지/game_over.png")]
student_eating = [pygame.image.load("이미지/student_gimbab1.png"), pygame.image.load("이미지/student_gimbab2.png"), pygame.image.load("이미지/student_gimbab3.png")]#리스트에 학생들 이미지 넣음 바탕화면 st파일에 st1..이미지
student_drink = [pygame.image.load("이미지/student_water1.png"), pygame.image.load("이미지/student_water2.png"), pygame.image.load("이미지/student_water3.png")]
idle = pygame.image.load("이미지/student.png")#김밥 먹지 않을 때
howtoplay = pygame.image.load("이미지/게임방법.png")
def mainmenu():
    
    howtobutton = False
    main = True
    
    while True:
        mouse = pygame.mouse.get_pos()
        
        screen.fill(WHITE)

        screen.blit(idle, (student_posX, student_posY))
        screen.blit(professor[0], (professor_posX, professor_posY))
        
        font = pygame.font.Font('글꼴/Jalnan.ttf', 90)
        gamestartText = font.render("몰래김밥먹기", True, BLACK)
        gamestartRect = gamestartText.get_rect()
        gamestartRect.centerx = round(screen_width/2)
        gamestartRect.centery = round(screen_height/5)
        screen.blit(gamestartText, gamestartRect)

        Buttonfont = pygame.font.Font('글꼴/Jalnan.ttf', 40)
        startButtonText = Buttonfont.render("게임시작", True, BLACK)
        startButtonRect = startButtonText.get_rect()
        startButtonRect.centerx = round(screen_width/2-200)
        startButtonRect.centery = round(screen_height/2+150)
        screen.blit(startButtonText, startButtonRect)

        Buttonfont = pygame.font.Font('글꼴/Jalnan.ttf', 40)
        startButtonText = Buttonfont.render("게임방법", True, BLACK)
        startButtonRect = startButtonText.get_rect()
        startButtonRect.centerx = round(screen_width/2+200)
        startButtonRect.centery = round(screen_height/2+150)
        screen.blit(startButtonText, startButtonRect)

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            break

        if main:
            if event.type == pygame.MOUSEBUTTONUP:
                if(120 < mouse[0] < 280 and 430 < mouse[1] < 470):
                    break
                if(520 < mouse[0] < 680 and 430 < mouse[1] < 470):
                    howtobutton = True
                    main = False
    
        if howtobutton:
            howtoplay_rect = howtoplay.get_rect()
            howtoplay_rect.centerx = round(screen_width/2)
            howtoplay_rect.centery = round(screen_height/2)
            screen.blit(howtoplay, howtoplay_rect)
            returnButtonText = Buttonfont.render("뒤로가기", True, BLACK)
            returnButtonRect = returnButtonText.get_rect()
            returnButtonRect.centerx = round(screen_width/2)
            returnButtonRect.centery = round(screen_height-40)
            screen.blit(returnButtonText, returnButtonRect)

            if event.type == pygame.MOUSEBUTTONUP:
                if(320 < mouse[0] < 480 and 520 < mouse[1] < 600):
                    howtobutton = False
                    main = True
        pygame.display.update()
    

def init():
    global clock, screen_width, screen_height, screen, score, start_time, hungryPoint, thirstPoint, comeAcross, eating, drinking, isNeedToRestart, studentCount, drinkingCount, remain_second

    clock = pygame.time.Clock()
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height)) #화면 크기

    #점수 관련 변수
    score = 0

    start_time = int(time.time())   #시작 시간

    hungryPoint = 50
    thirstPoint = 50
    comeAcross = False

    eating = False
    drinking = False

    isNeedToRestart = False

    professor_state = 1  #교수님의 상태
    student_state = 0  #학생의 상태

    studentCount = 0
    drinkingCount = 0

    remain_second = -2   #교수님 뒤 도는 타이머 변수

def studentEating():#김밥 먹는 함수
    global studentCount, student_posX, student_posY, hungryPoint, thirstPoint, student_state

    if studentCount > 2:#이미지 반복하도록 이미지 1,2,3 반복
        studentCount = 0

    if eating == True and hungryPoint < 100:
        screen.blit(student_eating[studentCount], (student_posX, student_posY))
        studentCount += 1

        #음식을 먹을 때 달거나 차는  양
        hungryPoint += 0.4
        thirstPoint -= 0.4

    else:
        screen.blit(idle, (student_posX, student_posY)) #식사중이 아닐때로
        
def studentDrinking():
    global drinkingCount, student_posX, student_posY, thirstPoint
    if drinkingCount > 2:
        drinkingCount = 0

    if drinking == True and thirstPoint < 100:
        screen.blit(student_drink[drinkingCount], (student_posX, student_posY))
        drinkingCount += 1
        #목마름 차는 양
        thirstPoint += 0.7

def professor_code():
    global professor_posX,professor_posY, remain_second, comeAcross, eating, drinking

    font = pygame.font.SysFont('impact', 120)

    if remain_second > 0 and remain_second <= 0.3:
        screen.blit(font.render("!", True, RED), [400, 300])
    if remain_second <= 0:
        screen.blit(professor[1], (professor_posX, professor_posY))
        if eating or drinking:   #학생들이 교수님에게 걸렸을때
            comeAcross = True
    else:
        screen.blit(professor[0], (professor_posX, professor_posY))
            
                
        
def scoreFunction():
    global score, dancing, excitingPoint, hungryPoint, thirstPoint
    
    if(eating):
        score += 2
        
def printFunction():
    global score, hungryPoint, thirstPoint
    screen.fill(WHITE)
    if hungryPoint>30:
        hungryPoint_Color = GREEN
    elif hungryPoint>10:
        hungryPoint_Color = YELLOW
    else:
        hungryPoint_Color = RED
    pygame.draw.rect(screen, hungryPoint_Color, [125, 15, hungryPoint*6.5, 20])
    if thirstPoint>30:
        thirstPoint_Color = BLUE
    elif thirstPoint>10:
        thirstPoint_Color = PUPPLE
    else:
        thirstPoint_Color = RED
    pygame.draw.rect(screen, thirstPoint_Color, [125, 40, thirstPoint*6.5, 20])
    font = pygame.font.Font('글꼴/Jalnan.ttf', 23)
    screen.blit(font.render("점수: " + str(int(score)), True, BLACK), [15, 70])
    screen.blit(font.render("배고픔", True, BLACK), [15, 15])
    screen.blit(font.render(str(int(hungryPoint)), True, BLACK), [90, 14])
    screen.blit(font.render("목마름", True, BLACK), [15, 40])
    screen.blit(font.render(str(int(thirstPoint)), True, BLACK), [90, 39])
    
    
def gameOver():
    global score, screen_width, screen_height, isNeedToRestart, high_Score, i
    screen.fill(WHITE)

    isNeedToRestart = True

    gameOverMark = professor[2].get_rect()
    gameOverMark.centerx = round(screen_width/2)
    gameOverMark.centery = round(screen_height/2)
    screen.blit(professor[2], gameOverMark)
    
    font = pygame.font.Font('글꼴/Jalnan.ttf', 60)
    scoreText = font.render("점수: " + str(int(score)), True, BLACK)
    score_Rect = scoreText.get_rect()
    score_Rect.centerx = round(screen_width/2)
    score_Rect.centery = round(screen_height*13/20)
    screen.blit(scoreText, score_Rect)

    if high_Score < score:
        high_Score = score
        new = True
    else:
        new = False

    highScoreFont = pygame.font.Font('글꼴/Jalnan.ttf', 35)
    newHighScoreFont = pygame.font.SysFont("impact", 70)
    screen.blit(highScoreFont.render("최고 점수: " + str(int(high_Score)), True, BLACK), [15, 15])

    if new:
        highScoreText = newHighScoreFont.render("NEW HIGH SCORE!", True, RED)
        highScoreText_Rect = highScoreText.get_rect()
        highScoreText_Rect.centerx = round(screen_width/2)
        highScoreText_Rect.centery = round(screen_height*12/40)
        screen.blit(highScoreText, highScoreText_Rect)
    
    pygame.display.update()
    
    sleep(0.5)

    restartFont = pygame.font.Font('글꼴/Jalnan.ttf', 30)
    restartText = restartFont.render("'R'키를 눌러 다시하기", True, BLACK)
    restartText_Rect = restartText.get_rect()
    restartText_Rect.centerx = round(screen_width/2)
    restartText_Rect.centery = round(screen_height*59/80)
    screen.blit(restartText, restartText_Rect)
    
    pygame.display.update()

def rungame():
    global eating, drinking, dancing, hungryPoint, thirstPoint, excitingPoint, start_time, remain_second, isNeedToRestart
    while True:
        clock.tick(30)
        current_time = float(time.time())
        if remain_second <= -2:
            random_second = random.randrange(1, 6)
            start_time = float(time.time())
        remain_second = random_second - (current_time - start_time)

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            break

        if event.type == pygame.KEYDOWN:#스페이스바 눌렸을때
            if event.key == pygame.K_SPACE:
                eating = True
                drinking = False

        elif event.type == pygame.KEYUP:#스페이스바 떼어졌을때
            if event.key == pygame.K_SPACE:
                eating = False
                drinking = False

        if event.type == pygame.KEYDOWN: #방향키 오른쪽
            if event.key == pygame.K_RIGHT:
                eating = False
                drinking = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                eating = False
                drinking = False
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            dancing = True
        
        elif event.type == pygame.MOUSEBUTTONUP:
            dancing = False

        current_time = int(time.time())
        
        #가만히 있을 때 소모되는 양
        hungryPoint -= 0.1
        thirstPoint -= 0.1
    
        printFunction()

        studentEating()

        studentDrinking()

        professor_code()

        pygame.display.flip()
        
        scoreFunction()

        if (hungryPoint <= 0 or thirstPoint <= 0 or comeAcross):
            time.sleep(1)
            gameOver()
            while isNeedToRestart == True:
                event = pygame.event.poll()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    isNeedToRestart = False
                    break
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    break
            if isNeedToRestart == False:
                init()
                continue

mainmenu()
rungame()
