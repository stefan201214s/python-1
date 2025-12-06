board = [" ","1","2","3", "1","-","-","-","2","-","-","-","3","-","-","-"]
player_1_turn = True
have_winner = False


while not have_winner:
    for i in range(0,16,4):
        print(board[i]+"|"+board[i+1]+"|"+board[i+2]+"|"+board[i+3]+"|")
    if player_1_turn:
         print("player 1's turn")
    else:
        print("Player 2's turn")
    row=int(input("Which row you need? : "))
    column=int(input("Which column you need? : "))
    if player_1_turn:
        board[4 * row + column] = "o"
    else:
        board[4 * row + column] = "x"
    
    if board[5]==board[6] and board[6] == board[7] and board[7] != "-":
        if player_1_turn:
            print("player 1 win. ")
        else:
            print("Player 2 win")
    if board[9]==board[10] and board[10] == board[11] and board[11] != "-":
        if player_1_turn:
            print("player 1 win. ")
        else:
            print("Player 2 win")
    if board[13]==board[14] and board[14] == board[15] and board[15] != "-":
        if player_1_turn:
            print("player 1 win. ")
        else:
            print("Player 2 win")

    if board[5]==board[9] and board[9] == board[13] and board[13] != "-":
        if player_1_turn:
            print("player 1 win. ")
        else:
            print("Player 2 win")
    if board[6]==board[10] and board[10] == board[14] and board[14] != "-":
        if player_1_turn:
            print("player 1 win. ")
        else:
            print("Player 2 win")
    if board[7]==board[11] and board[11] == board[15] and board[15] != "-":
        if player_1_turn:
            print("player 1 win. ")
        else:
            print("Player 2 win")
    if board[5]==board[10] and board[10] == board[15] and board[15] != "-":
        if player_1_turn:
            print("player 1 win. ")
        else:
            print("Player 2 win")
    if board[7]==board[10] and board[10] == board[13] and board[13] != "-":
        if player_1_turn:
            print("player 1 win. ")
        else:
            print("Player 2 win")











    player_1_turn=not(player_1_turn)
    