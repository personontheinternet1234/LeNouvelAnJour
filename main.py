import pygame,random
from pygame.locals import *

xmax = 1000
ymax = 600


class Particle:

    def __init__(self, startx, starty, col, firework):
        self.firework = firework

        self.x = startx
        self.y = starty
        self.col = col

        self.x_vel = random.uniform(-2,2)
        self.y_vel = random.uniform(-2,2)

        self.x_acl = random.uniform(-0.01, 0.01)
        self.y_acl = 0.1

    def tick(self):
        if self.y < 590:
            self.x = self.x + self.x_vel
            self.y = self.y + self.y_vel
            if self.x_vel > 0:
                if (self.x_vel - self.x_acl) > 0:
                    self.x_vel -= self.x_acl
                else:
                    self.x_vel = 0
                    self.suicide()
            if self.x_vel < 0:
                if (self.x_vel + self.x_acl) < 0:
                    self.x_vel += self.x_acl
                else:
                    self.x_vel = 0
                    self.suicide()
            self.y_vel += self.y_acl
        else:
            self.suicide()

    def suicide(self):
        self.firework.particles.remove(self)


class Firework:

    def __init__(self, start_x, start_y, color):
        self.start_x = start_x
        self.start_y = start_y

        self.particles = []

        self.color = color

        self.create()

    def create(self):
        for part in range(300):
            if self.color == "red":
                if part % 2 > 0:
                    col = red
                elif part % 3 > 0:
                    col = l_red
                else:
                    col = white
            if self.color == "white":
                if part % 2 > 0:
                    col = white
                else:
                    col = grey
            if self.color == "blue":
                if part % 2 > 0:
                    col = blue
                elif part % 3 > 0:
                    col = l_blue
                else:
                    col = white

            self.particles.append(Particle(mouse_x, mouse_y, col, self))

    def tick(self):
        for p in self.particles:
            p.tick()
            pygame.draw.circle(screen, p.col, (p.x, p.y), 2)


def display_text(text, x, y, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


pygame.init()
screen = pygame.display.set_mode((xmax,ymax))

black = (0,0,0)

white = (255, 255, 255)
grey = (100, 100, 100)

blue = (50,50,160)
l_blue = (100,100,255)

red = (160, 50, 50)
l_red = (255,100,100)

clock = pygame.time.Clock()

pygame.display.set_caption("Le Nouvel An")
font = pygame.font.Font(None, 50)
show_text = False
text_display_time = 0

fireworks = []
color_var = white
text_x = 0
text_y = 0
exit_flag = False
while not exit_flag:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            color = ["red", "white", "blue"][random.randint(0,2)]
            fireworks.append(Firework(mouse_x, mouse_y, color))

            text_x = mouse_x - 100 + random.randint(-50,50)
            text_y = mouse_y - 50 + random.randint(-50,50)
            show_text = True
            text_display_time = pygame.time.get_ticks()

        elif event.type == QUIT:
            exit_flag = True

    screen.fill(black)
    for f in fireworks:
        f.tick()

    if show_text:
        if color == "blue":
            color_var = blue
        if color == "red":
            color_var = red
        if color == "white":
            color_var = white

        display_text("Feu d'Artifice", text_x, text_y, color_var)
        if pygame.time.get_ticks() - text_display_time > 250:
            show_text = False

    pygame.display.flip()
    clock.tick(50)

pygame.quit()
