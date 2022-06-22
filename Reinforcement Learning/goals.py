

class Goal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.checked = False

    def check(self, x, y, d):
        distance = (x - self.x)**2 + (y-self.y)**2
        d = d*d
        if distance < d:
            self.checked = True
            return True
        return False


def get_goals():
    goals = []
    lines = open('map/checkpoint.txt', 'r')
    for line in lines:
        try:
            words = line.split()
            goal = Goal(int(words[0]), int(words[1]))
            goals.append(goal)
        except:
            pass
    return goals
