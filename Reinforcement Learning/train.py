from Driving_Environment import Driving
from network import DDQN_Agent


driving = Driving()
show_flag = True

TOTAL_GAMETIME = 1000 # Max game time for one episode
N_EPISODES = 10000
REPLACE_TARGET = 50

ddqn_agent = DDQN_Agent()

ddqn_scores = []
eps_history = []

for e in range(N_EPISODES):
    driving.reset()
    done = False
    score = 0
    counter = 0

    observation, reward, done = driving.run(0)
    g_time = 0

    while not done:
        action = ddqn_agent.get_action(observation)


