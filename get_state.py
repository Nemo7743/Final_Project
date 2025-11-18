def get_state(self, game):
    head = game.snake[0]
    #先定義好蛇頭下一步可能的位置（4個方向）
    point_l = Point(head.x - 20, head.y)
    point_r = Point(head.x + 20, head.y)
    point_u = Point(head.x, head.y - 20)
    point_d = Point(head.x, head.y + 20)

    #判斷目前行進的方向，只會有一個變數的值會是1
    dir_l = game.direction == Direction.LEFT
    dir_r = game.direction == Direction.RIGHT
    dir_u = game.direction == Direction.UP
    dir_d = game.direction == Direction.DOWN

    #建立狀態向量
    state = [
        ## 直行會遇到的碰撞
        (dir_r and game.is_collision(point_r)) or  #蛇朝右方向前進，直走時蛇頭會和(畫布)右邊的相鄰位置碰撞
        (dir_l and game.is_collision(point_l)) or
        (dir_u and game.is_collision(point_u)) or
        (dir_d and game.is_collision(point_d)),

        ## 右轉（順時針）會遇到的碰撞
        (dir_u and game.is_collision(point_r)) or  #蛇朝上方前進，向右轉時蛇頭會和(畫布)右邊的相鄰位置碰撞
        (dir_d and game.is_collision(point_l)) or
        (dir_l and game.is_collision(point_u)) or
        (dir_r and game.is_collision(point_d)),

        ## 左轉（逆時針）會遇到的碰撞
        (dir_d and game.is_collision(point_r)) or  #蛇朝下方前進，向左轉時蛇頭會和(畫布)右邊的相鄰位置碰撞
        (dir_u and game.is_collision(point_l)) or
        (dir_r and game.is_collision(point_u)) or
        (dir_l and game.is_collision(point_d)),

        dir_l,
        dir_r,
        dir_u,
        dir_d,

        game.food.x < game.head.x, # 食物在左邊
        game.food.x > game.head.x,
        game.food.y < game.head.y, # 食物在上面
        game.food.y > game.head.y
        ]

    return np.array(state, dtype=int)
