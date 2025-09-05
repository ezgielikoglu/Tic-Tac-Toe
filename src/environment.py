import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)  # 0: empty, 1: player 1, -1: player 2
        self.current_player = 1  # Player 1 starts

    def reset(self):
        self.board.fill(0)
        self.current_player = 1
        return self.board.copy()

    def step(self, action):
        row, col = action
        if self.board[row, col] != 0:
            raise ValueError("Invalid action: Cell already occupied.")
        
        self.board[row, col] = self.current_player
        reward, done = self.check_winner()
        
        if not done:
            self.current_player *= -1  # Switch player
        
        return self.board.copy(), reward, done

    def check_winner(self):
        for player in [1, -1]:
            # Check rows and columns
            if any(np.all(self.board[i, :] == player) for i in range(3)) or \
               any(np.all(self.board[:, j] == player) for j in range(3)):
                return (1 if player == 1 else -1), True
            
            # Check diagonals
            if np.all(np.diag(self.board) == player) or \
               np.all(np.diag(np.fliplr(self.board)) == player):
                return (1 if player == 1 else -1), True
        
        if np.all(self.board != 0):
            return 0, True  # Draw
        
        return 0, False  # Game continues

    def render(self):
        symbols = {1: 'X', -1: 'O', 0: ' '}
        for row in self.board:
            print("|".join(symbols[cell] for cell in row))
            print("-" * 5)