import cv2
import numpy as np
from draw import draw_center, rotaion

sin = np.sin
cos = np.cos
tan = np.tan
pi = np.pi


class Driving:
    def __init__(self):
        self.map = cv2.imread('Map/Map_1.png', 0)
        self.start_point = (200, 300)
        self.car = Car(self.start_point[0], self.start_point[1])
        self.img_show = None

    def show(self):
        cv2.imshow('Driving', self.img_show)

    def run(self, choice):
        self.car.run(choice)
        observations = self.car.get_observation(self.map, 100)

        self.img_show, self.car.crash = draw_center(self.map, self.car.img, self.car.get_position())
        reward = 0
        if self.car.crash:
            reward = -1

        return observations, reward, self.car.crash

    def check_point(self):
        pos_X, pos_Y = self.car.get_position()
        start_X, start_Y = self.start_point
        return round((pos_X-start_X)/40)

    def reset(self):
        self.car = Car(self.start_point[0], self.start_point[1])
        # self.car.reset()


class Car:
    max_speed = 10
    delta_angle = 15
    raw_img = cv2.imread('car.png', 0)

    def __init__(self, x, y):
        self.img = self.raw_img
        self.pos_x = x
        self.pos_y = y
        self.direct = 0
        self.speed = 0
        self.crash = False

    def get_position(self):
        return self.pos_x, self.pos_y

    def turn(self, angle):
        self.direct += angle
        if self.direct > 180:
            self.direct = 360 - self.direct
        elif self.direct < -180:
            self.direct += 360

        self.img = rotaion(self.raw_img, self.direct)

    def accelerate(self, acc):
        self.speed += acc
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def run(self, choice):
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

    def get_observation(self, map, max):
        def get_distance(map, angle, max):
            angle += self.direct
            if angle > 180:
                angle = 360 - angle
            elif angle < -180:
                angle += 360

            sin_a = sin(angle*pi / 180)
            cos_a = cos(angle*pi / 180)
            for i in range(1, max, 2):
                dx = round(i * cos_a)
                dy = round(i * sin_a)
                if map[self.pos_y-dy, self.pos_x+dx] > 128:
                    return i
            return max

        observations = [self.speed]
        for angle in [-60, -30, 0, 30, 60]:
            distance = get_distance(map, angle, max)
            observations.append(distance)

        return np.array(observations)

    def reset(self):
        pass
