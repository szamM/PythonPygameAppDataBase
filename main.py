import pygame
pygame.init()
import db


class Titles:
    def __init__(self, x, y, title, colors):
        self.x = x
        self.y = y
        self.title = title
        self.color = colors
        self.ch = colors

    def drawing(self, f):
        text1 = f.render(str(self.title), True, self.ch)
        screen.blit(text1, (self.x, self.y))

    def checker(self):
        if pygame.mouse.get_pos()[0] in range(self.x, 24 * len(str(self.title)) + self.x) and pygame.mouse.get_pos()[1] in range(self.y, 24 + self.y):
            self.ch = (0, 180, 0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
        else:
            self.ch = self.color


class InpBlocks:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.entlogin = False
        self.puted = False
        self.login_recta = pygame.Rect((x, y, width, height))

    def drawing(self):
        pygame.draw.rect(screen, self.color, self.login_recta, 2)

    def checker(self):
        if (not self.puted) and pygame.mouse.get_pos()[0] in range(self.x, self.x + self.width) and pygame.mouse.get_pos()[1] in range(self.y, self.y + self.height) and event.type == pygame.MOUSEBUTTONDOWN:
            self.color = (0, 200, 0)
            self.entlogin = True

    def refresh(self):
        self.color = (0, 0, 0)

    def entered(self):
        self.color = (0, 0, 255)
        self.puted = True


login_list = []
f1 = pygame.font.SysFont('arial', 24)
f2 = pygame.font.SysFont('arial', 14)
f3 = pygame.font.SysFont('arial', 30)
end_game = False
clock = pygame.time.Clock()
FPS = 60
WIDTH = 500
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
registration = Titles(400, 30, 'Sign up', (0, 0, 180))
enter = Titles(10, 29, 'Sign in', (0, 0, 180))
screen.fill((255, 255, 255))
###

login_enter = Titles(20, 30, 'Login: ', (0, 0, 180))
password_enter = Titles(20, 105, 'Password: ', (0, 0, 180))
login_rect = InpBlocks(20, 60, 150, 25, (0, 0, 0))
password_rect = InpBlocks(20, 135, 150, 25, (0, 0, 0))
back_rect = pygame.Rect((350, 20, 150, 50))
go_back = Titles(370, 30, 'BACK', (180, 0, 0))
go_back_s = Titles(370, 60, 'BACK', (180, 0, 0))
helper_l = Titles(20, 90, 'click on the input box to enter the login, if color of frame changed you can put ur data', (200, 200, 200))
color_r = (0, 0, 0)
already_exist_title = Titles(5, 200, 'Your account already exist', (200, 0, 0))
new_ac = Titles(5, 200, 'Your account is registered', (0, 200, 0))
enter_data = []
go_l = True
go_p = True
registration_checker = False
exist = False
passw_list = []
###
cc = 0
registration_go = False
enter_go = False
choice = True
while not end_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game = True
        if choice:
            if cc < 1:
                screen.fill((255, 255, 255))
                cc += 1
            registration.drawing(f1)
            registration.checker()
            enter.drawing(f1)
            enter.checker()
            if registration.checker():
                registration_go = True
                cc = 0
            if enter.checker():
                enter_go = True
                cc = 0
        if registration_go:
            choice = False
            if cc < 1:
                screen.fill((255, 255, 255))
                cc += 1
            go_back_s.drawing(f1)
            go_back_s.checker()
            login_rect.drawing()
            login_rect.checker()
            login_enter.drawing(f1)
            helper_l.drawing(f2)
            password_rect.drawing()
            password_rect.checker()
            password_enter.drawing(f1)
            if event.type == pygame.KEYDOWN and password_rect.entlogin and event.key == 13 and go_p:
                go_p = False
                enter_data.append(str(''.join(passw_list)))
                password_rect.entered()
                registration_checker = True
            if event.type == pygame.KEYDOWN and password_rect.entlogin and go_p:
                passw_list.append(event.unicode)
            if event.type == pygame.KEYDOWN and login_rect.entlogin and event.key == 13 and go_l:
                go_l = False
                enter_data.append(str(''.join(login_list)))
                login_rect.entered()
            if event.type == pygame.KEYDOWN and login_rect.entlogin and go_l:
                login_list.append(event.unicode)
            if len(enter_data) == 2:
                if cc < 2:
                    print(enter_data)
                    cc += 1
            if registration_checker:
                if db.checker(enter_data):
                    exist = False
                else:
                    exist = True
                if exist:
                    already_exist_title.drawing(f3)
                else:
                    new_ac.drawing(f3)
                registration_checker = False
            if go_back_s.checker():
                login_rect.refresh()
                registration_checker = False
                password_rect.refresh()
                login_rect.entlogin = False
                password_rect.entlogin = False
                enter_data.clear()
                passw_list.clear()
                login_list.clear()
                go_l = True
                go_p = True
                login_rect.puted = False
                password_rect.puted = False
                registration_go = False
                cc = 0
                choice = True
        if enter_go:
            choice = False
            if cc < 1:
                screen.fill((255, 255, 255))
                cc += 1
            login_rect.drawing()
            login_rect.checker()
            login_enter.drawing(f1)
            go_back.drawing(f1)
            go_back.checker()
            helper_l.drawing(f2)
            if event.type == pygame.KEYDOWN and login_rect.entlogin:
                login_list.append(event.unicode)
            if event.type == pygame.KEYDOWN and login_rect.entlogin and event.key == 13:
                login_list.pop(-1)
                print(''.join(login_list))
                login_list.clear()
                login_rect.refresh()
                login_rect.entlogin = False
            if go_back.checker():
                registration_go = False
                enter_go = False
                choice = True
                login_rect.refresh()
                cc = 0

    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()