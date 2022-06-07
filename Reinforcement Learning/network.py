import numpy as np
import tensorflow as tf
import numpy as np



class DDQN_Agent:
    def __init__(self):
        self.brain_eval = Brain()

    def get_action(self, observations):
        actions = self.brain_eval.predict(observations)

        return np.argmax(actions)


class Brain:
    def __init__(self, n_action):
        self.n_action = n_action
        self.model = self.createModel()

    def createModel(self):
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Dense(64, activation=tf.nn.relu))  # prev 256
        model.add(tf.keras.layers.Dense(32, activation=tf.nn.relu))  # prev 256
        model.add(tf.keras.layers.Dense(self.n_action, activation=tf.nn.softmax))
        model.compile(loss="mse", optimizer="adam")

        return model

    def predict(self, obs):
        return self.model.predict(obs)
