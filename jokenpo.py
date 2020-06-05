def play_poker(player1_select : int, player2_select : int) -> String:
    #0 = stone, 1 = scissor, 2 = paper
    if player1_select == 0:
        if player2_select == 0:
            return "draw"
        elif player2_select == 1:
            return "player1"
        else
            return "player2"
    elif player1_select = 1:
        if player2_select == 0:
            return "player2"
        elif player2_select == 1:
            return "draw"
        else
            return "player1"
    else:
        if player2_select == 0:
            return "player1"
        elif player2_select == 1:
            return "player2"
        else
            return "draw"
