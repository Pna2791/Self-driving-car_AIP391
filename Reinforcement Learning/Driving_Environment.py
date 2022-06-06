import cv2
import numpy as np
from draw import draw_center, rotaion

sin = np.sin
cos = np.cos
tan = np.tan


class Driving:
    def __init__(self):
        self.map = cv2.imread('Map/Map_1.png')
        self.start_point = (200, 300)
        self.car = Car(self.start_point[0], self.start_point[1])

    def show(self):
        img, crash = draw_center(self.map, self.car.img, self.car.get_position())
        # img, _ = draw_center(self.map, self.car.img, self.car.get_position())
        cv2.imshow('Driving', img)

    def action(self, choice):
        self.car.action(choice)
        self.show()


class Car:
    max_speed = 20
    delta_angle = 15
    raw_img = cv2.imread('car.png')

    def __init__(self, x, y):
        self.img = self.raw_img
        self.pos_x = x
        self.pos_y = y
        self.direct = 0
        self.speed = 0

    def get_position(self):
        return self.pos_x, self.pos_y

    def turn(self, angle):
        self.direct += angle
        if self.direct > 180:
            self.direct = 360 - self.direct
        self.img = rotaion(self.raw_img, self.direct)

    def accelerate(self, acc):
        self.speed += acc
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def action(self, choice):
        if choice == 1:
            self.accelerate(1)
        elif choice == 3:
            self.accelerate(-1)
        elif choice == 2:
            self.turn(self.delta_angle)
        elif choice == 4:
            self.turn(-self.delta_angle)

        self.update()

    def update(self):
        alpha = self.direct * np.pi / 180
        dx = round(self.speed*cos(alpha))
        dy = round(self.speed*sin(alpha))

        self.pos_x += dx
        self.pos_y -= dy
