def tic_tac_toe():
    gameboard = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

## draw gameboard

    def draw():
        print(gameboard[0], '|', gameboard[1], '|',  gameboard[2])
        print ("----------")
        print(gameboard[3], '|', gameboard[4], '|', gameboard[5])
        print ("----------")
        print(gameboard[6], '|',  gameboard[7], '|',  gameboard[8])
        print ("----------")
        print()

## throws an error if the cell is not free (for Player 1)
    def Player_1():
        n = choose_number()
        if gameboard[n] == "X" or gameboard[n] == "O":
            print("\nYou can't go there. The cell is not free. Please, try again")
            Player_1()
        else:
            gameboard[n] = "X"

## throws an error if the cell is not free (for Player 2)
    def Player_2():
        n = choose_number()
        if gameboard[n] == "X" or gameboard[n] == "O":
            print("\nYou can't go there. The cell is not free. Please, try again")
            Player_2()
        else:
            gameboard[n] = "O"

    def choose_number():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nThe number is outside the board. Please, try again")
                        continue
                except ValueError:
                   print("\nThat's not a number. Please, try again")
                   continue

    def check_board():
        count = 0
        for a in win_commbinations:
            if gameboard[a[0]] == gameboard[a[1]] == gameboard[a[2]] == "X":
                print("Player 1 is winner\n")
                print("Congratulations!\n")
                return True

            if gameboard[a[0]] == gameboard[a[1]] == gameboard[a[2]] == "O":
                print("Player 2 is winner\n")
                print("Congratulations!\n")
                return True
        for a in range(9):
            if gameboard[a] == "X" or gameboard[a] == "O":
                count += 1
            if count == 9:
                print("No sides!\n")
                return True

    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 1 choose where to place X ")
        Player_1()
        print()
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 2 choose where to place O ")
        Player_2()
        print()

    if input("Do you want play again (y/n)\n") == "y":
        print()
        tic_tac_toe()

tic_tac_toe()

