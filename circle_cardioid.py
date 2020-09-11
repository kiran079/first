import pygame
import math
from win32api import GetSystemMetrics

pygame.init()

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

x_length = GetSystemMetrics(0)
y_length = GetSystemMetrics(1)

wn= pygame.display.set_mode((x_length, y_length), pygame.FULLSCREEN)
wn.fill(WHITE)
clock = pygame.time.Clock()

run = True

centerx = int(x_length/2)
centery = int(y_length/2)
radius = min([centerx,centery])-40
width = 1

multiplied_num = 1


class Point:
    def __init__(self,num, x, y):
        self.num = num
        self.x = x
        self.y = y


def getPoints(total_nums):
    t = 0
    x = 0
    y = 0
    all_points = []

    for i in range(total_nums):
        x = -math.cos(t)
        y = math.sin(t)
        all_points.append(Point(i, int(centerx+x*radius), int(centery+y*radius)))
        t+= 2*math.pi/total_nums
    return all_points

def whoToConnect(points_list, total_nums, multiple):
    connections = []
    for point in points_list:
        #this line will be enough for integers only
        #connections.append([point, points_list[(point.num*multiple)%total_nums]])
        scale = 2*math.pi/total_nums
        after_multiplied = (point.num*multiple)%total_nums
        connections.append([point, Point(after_multiplied,
        -math.cos(after_multiplied*scale)*radius+centerx,
        math.sin(after_multiplied*scale)*radius+centery)])
    return connections

#Start Screen
temp = True
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render("Click to Start!", False, (0, 0, 0))
while temp:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            temp = False
        if event.type == pygame.QUIT:
            temp=False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        temp=False

    wn.blit(textsurface, (100,100))
    pygame.display.update()
    wn.fill(WHITE)

#Main animation
while run:

    clock.tick(50)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run=False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    pygame.draw.circle(wn, RED, (centerx, centery), radius, width)

    total_nums = 300
    all_points = getPoints(total_nums)
    for p in all_points:
        pygame.draw.circle(wn, BLACK, (p.x, p.y), 1)

    connection = whoToConnect(all_points, total_nums, multiplied_num)
    for pair in connection:
        x1 = int(pair[0].x)
        y1 = int(pair[0].y)
        x2 = int(pair[1].x)
        y2 = int(pair[1].y)
        pygame.draw.line(wn, BLUE, (x1, y1), (x2, y2))

    multiplied_num+=0.01
    pygame.display.update()
    wn.fill(WHITE)

pygame.quit()
