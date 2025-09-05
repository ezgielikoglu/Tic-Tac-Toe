from environment import TicTacToe  # Eğer src içindeyse: from src.environment import TicTacToe

game = TicTacToe()
print("Tic-Tac-Toe oyununa hoş geldiniz!")
game.render()

done = False
while not done:
    print(f"\nSıra oyuncu: {'X' if game.current_player == 1 else 'O'}")
    try:
        row = int(input("Satır (0-2): "))
        col = int(input("Sütun (0-2): "))
        state, reward, done = game.step((row, col))
    except ValueError as e:
        print(f"Hata: {e}")
        continue
    game.render()

if done:
    if reward == 1:
        print("Kazanan: X")
    elif reward == -1:
        print("Kazanan: O")
    else:
        print("Berabere!")