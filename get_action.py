def get_action(self, state):
    # random moves: tradeoff exploration / exploitation
    self.epsilon = 80 - self.n_games # n_games 是遊戲的局數，所以玩越多遊戲，epsilon就會越小
    final_move = [0, 0, 0]
    if random.randint(0, 200) < self.epsilon: # 如果epsilon越小、範圍越小，move就會越不隨機、死板
        move = random.randint(0, 2)
        final_move[move] = 1
    else:
        # 所以當遊戲局數越多，就會減少隨機步驟而依賴我們之前model裡面的權重。
        state0 = torch.tensor(state, dtype = torch.float)
        prediction = self.model(state0)
        move = torch.argmax(prediction).item()
        final_move[move] = 1


    return final_move