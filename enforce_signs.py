
class car_variables:
    actings  = [{'sign name': 'Bien giam toc--yeild-', 'type': 'warning'},
               {'sign name': 'Den do', 'type': 'speed stacking', 'speed': ['*', 0]},
               {'sign name': 'Den giao thong', 'type': 'warning'},
               {'sign name': 'Den vang', 'type': 'immediately', 'speed': ['*', 0.5]},
               {'sign name': 'Di Thang', 'type': 'do nothing'},
               {'sign name': 'Duong cam', 'type': 'warning'},
               {'sign name': 'Stop', 'type': 'immediately', 'speed': ['*', 0]},
               {'sign name': 'canh bao queo phai', 'type': 'warning'},
               {'sign name': 'canh bao queo trai', 'type': 'warning'},
               {'sign name': 'den xanh', 'type': 'green light'},
               {'sign name': 'duoc queo phai', 'type': 'warning'},
               {'sign name': 'duong uu tien', 'type': 'warning'},
               {'sign name': 'end limit 30km-h', 'type': 'end restriction', 'limit': 30},
               {'sign name': 'end limit 40km-h', 'type': 'end restriction', 'limit': 40},
               {'sign name': 'end limit 50km-h', 'type': 'end restriction', 'limit': 50},
               {'sign name': 'end limit 60km-h', 'type': 'end restriction', 'limit': 60},
               {'sign name': 'end limit 70km-h', 'type': 'end restriction', 'limit': 70},
               {'sign name': 'end limit 80km-h', 'type': 'end restriction', 'limit': 80},
               {'sign name': 'gioi han toc do 10km-h', 'type': 'do nothing'},
               {'sign name': 'gioi han toc do 120km-h', 'type': 'do nothing'},
               {'sign name': 'gioi han toc do 20km-h', 'type': 'do nothing'},
               {'sign name': 'gioi han toc do 30km-h', 'type': 'set restriction', 'limit': 30},
               {'sign name': 'gioi han toc do 40km-h', 'type': 'set restriction', 'limit': 40},
               {'sign name': 'gioi han toc do 50km-h', 'type': 'set restriction', 'limit': 50},
               {'sign name': 'gioi han toc do 60km-h', 'type': 'set restriction', 'limit': 60},
               {'sign name': 'gioi han toc do 70km-h', 'type': 'set restriction', 'limit': 70},
               {'sign name': 'gioi han toc do 80km-h', 'type': 'set restriction', 'limit': 80},
               {'sign name': 'gioi han toc do 90km-h', 'type': 'do nothing'},
               {'sign name': 'limit 5km-h', 'type': 'do nothing'},
               {'sign name': 'min limit 20km-h', 'type': 'do nothing'},
               {'sign name': 'min limit 40km-h', 'type': 'do nothing'},
               {'sign name': 'min limit 60km-h', 'type': 'do nothing'},
               {'sign name': 'queo trai', 'type': 'warning'},
               {'sign name': 'slow', 'type': 'warning'},
               ]

    def __init__(self, speed=[50], min_speed=[0], max_speed=[80], signs_ratio_min=0, padding_top=0):
        self.speed = speed
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.signs_ratio_min = signs_ratio_min
        self.padding_top = padding_top

    def enforce(self, signs):
        for sign in signs:
            pass
        return signs

if __name__ == '__main__':
    car_var = car_variables()
    # print(car_var.enforce((1, 3, 0, 12, 25)))