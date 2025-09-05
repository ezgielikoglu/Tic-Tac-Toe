from environment import TicTacToe
from agent import QLearningAgent

env = TicTacToe()
agent = QLearningAgent(alpha=0.1, gamma=0.9, epsilon=0.2)

# AI önce kendi kendine öğreniyor
episodes = 5000
for _ in range(episodes):
    state = env.reset()
    done = False
    while not done:
        action = agent.choose_action(env)
        next_state, reward, done = env.step(action)
        agent.learn(state, action, reward, next_state, done)
        state = next_state

# İnsan vs AI modu
state = env.reset()
env.render()
done = False
while not done:
    # İnsan hamlesi
    valid = False
    while not valid:
        try:
            move = input("Hamleni gir (satır,sütun): ")
            row, col = map(int, move.split(","))
            if env.board[row, col] == 0:
                valid = True
            else:
                print("Bu hücre dolu! Tekrar dene.")
        except:
            print("Geçersiz giriş! Format: satır,sütun (0-2 arası)")

    state, reward, done = env.step((row, col))
    env.render()
    if done:
        break

    # AI hamlesi
    ai_action = agent.choose_action(env)
    print(f"\nAI hamlesi: {ai_action}")
    state, reward, done = env.step(ai_action)
    env.render()

# Sonuç
if reward == 1:
    print("Kazanan: X")
elif reward == -1:
    print("Kazanan: O (AI)")
else:
    print("Berabere!")