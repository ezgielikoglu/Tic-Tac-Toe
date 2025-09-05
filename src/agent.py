import numpy as np
import random

class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.q_table = {}  # state-action değerleri
        self.alpha = alpha  # öğrenme hızı
        self.gamma = gamma  # indirim faktörü
        self.epsilon = epsilon  # keşfetme olasılığı

    def get_state_key(self, state):
        return tuple(state.flatten())

    def choose_action(self, env):
        state_key = self.get_state_key(env.board)
        available = [(i,j) for i in range(3) for j in range(3) if env.board[i,j]==0]

        # epsilon-greedy
        if random.random() < self.epsilon or state_key not in self.q_table:
            return random.choice(available)

        q_values = [self.q_table[state_key].get(a, 0) for a in available]
        max_q = max(q_values)
        best_actions = [a for a, q in zip(available, q_values) if q == max_q]
        return random.choice(best_actions)

    def learn(self, state, action, reward, next_state, done):
        state_key = self.get_state_key(state)
        next_key = self.get_state_key(next_state)

        if state_key not in self.q_table:
            self.q_table[state_key] = {}

        q_predict = self.q_table[state_key].get(action, 0)
        q_target = reward
        if not done:
            if next_key not in self.q_table:
                self.q_table[next_key] = {}
            next_max = max(self.q_table[next_key].values(), default=0)
            q_target += self.gamma * next_max

        self.q_table[state_key][action] = q_predict + self.alpha * (q_target - q_predict)