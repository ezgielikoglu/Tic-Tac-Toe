from environment import TicTacToe
from agent import QLearningAgent

env = TicTacToe()
agent = QLearningAgent(alpha=0.1, gamma=0.9, epsilon=0.2)

# AI kendi kendine öğreniyor
episodes = 5000
for _ in range(episodes):
    state = env.reset()
    done = False
    while not done:
        # AI hamle seçiyor
        action = agent.choose_action(env)
        next_state, reward, done = env.step(action)
        # Öğrenme fonksiyonu
        agent.learn(state, action, reward, next_state, done)
        state = next_state

# AI test
state = env.reset()
env.render()
done = False
while not done:
    action = agent.choose_action(env)
    print(f"\nAI hamlesi: {action}")
    state, reward, done = env.step(action)
    env.render()

# Sonuç
if reward == 1:
    print("Kazanan: X")
elif reward == -1:
    print("Kazanan: O")
else:
    print("Berabere!")