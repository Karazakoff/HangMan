import pygame
import sys
import time
# Initialiasation of Game
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1000,680))
# Text on Bottom Template


class TextBox():
    def __init__(self, main = ""):
        self.win = False
        self.main = main
        self.temp = []
        for i in self.main:
            if i == " ":
                self.temp.append(" ")
            else:
                self.temp.append("_")

        self.font = pygame.font.SysFont('Gill Sans', 80)
        self.text = self.font.render(' '.join(self.temp), True, (0,0,0), (255,255,255))
        self.textRect = self.text.get_rect()
        self.textRect.center = (500, 600)
    def drawer(self):
        screen.blit(self.text, self.textRect)

class Front(TextBox):
    def __init__(self):
        super().__init__()
        self.textRect.center = (5, 260)
    def drawer(self, keyname):
        self.main = keyname
        self.text = self.font.render(self.main, True, (0,0,0), (255,255,255))
        screen.blit(self.text, self.textRect)

def submit(keyname, text):
    global attempt
    if keyname in text.main:
        for i in range(len(text.main)):
            if keyname == text.main[i]:
                text.temp[i] = keyname
        text.text = text.font.render(' '.join(text.temp), True, (0,0,0), (255,255,255))
    else:
        attempt -= 1
    if text.main == text.temp:
        return True



# Main
while True:
    main = list(input("Give me a text in range 1-15: ").upper())
    if len(main) > 15 or len(main) <= 0:
        print("Sorry, your text is not valid, try to give another one!")
    else:
        print("Successfully got the text!")
        break


attempt = 13
text = TextBox(main)
front = Front()
keyname = ""
bc = pygame.image.load('images/background.jpg')
white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)
x = False
win = pygame.image.load("images/win.jpg")
lose = pygame.image.load("images/over.jpg")

hangman = [pygame.image.load('images/0.jpg'),
    pygame.image.load('images/1.jpg'),
    pygame.image.load('images/2.jpg'),
    pygame.image.load('images/3.jpg'),
    pygame.image.load('images/4.jpg'),
    pygame.image.load('images/5.jpg'),
    pygame.image.load('images/6.jpg'),
    pygame.image.load('images/7.jpg'),
    pygame.image.load('images/8.jpg'),
    pygame.image.load('images/9.jpg'),
    pygame.image.load('images/10.jpg'),
    pygame.image.load('images/11.jpg'),
    pygame.image.load('images/12.jpg'),
    pygame.image.load('images/13.jpg'),
]

while True:
    # Text on Bottom
    screen.blit(bc, (0,0))

    # screen.blit(text.text, text.textRect)
    text.drawer()

    # pygame.draw.line(screen, pygame.Color(168,168,168), (0,520), (1000,520), 3)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and len(pygame.key.name(event.key)) == 1 and pygame.key.name(event.key).isalpha():
            keyname = pygame.key.name(event.key).upper()

        elif event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        x = submit(keyname, text)
        time.sleep(0.3)
        print(attempt)
        if x:
            text.drawer()
            pygame.display.update()
            time.sleep(2)
            screen.blit(pygame.image.load('images/win.jpg'), (75, -50))
            pygame.display.update()
            time.sleep(1)
            break
        if attempt <= 1:
            screen.blit(pygame.image.load('images/over.jpg'), (100, 100))
            pygame.display.update()
            time.sleep(2)
            break
    screen.blit(pygame.image.load('images/{}.jpg'.format(attempt)), (475, 20))



    screen.blit(front.font.render("     ", True, (255,255,255), (255,255,255)), front.textRect)
    front.drawer(keyname)

    pygame.display.update()
