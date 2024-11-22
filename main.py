# tic-tac-toe game requirements #

# 1. import logo for the game #
# 2. need 2 players - one user and another computer #
# 3. create the table #
# 4. figure out how to place the mark inside the table created #
# 5. once a square is occupied u cannot place the mark inside the same square #
# 6. check for horizontal 3, vertical 3 or diagonal 3 to check for the winner #
# 7. if the number of marks of each player is same and all squares are occupies, the game becomes a draw #
# 8. if the first 3 marks on the vertical/horizontal/diagonal is made by either the user/comp, then either of them
# wins #
# 9. finally ask whether to play again or quit #

import logo
import random


def grid(arr):

    for row in arr:
        temp = ""
        for i in range(len(row)):
            if i < 2:
                temp += str(row[i]) + " | "
            else:
                temp += str(row[i])
        print(temp)
        print("--------")


def opponents_turn(user_choice, possibilities):
    possibilities.remove(user_choice)
    print(possibilities)
    c = random.choice(possibilities)
    possibilities.remove(c)
    return c


def calculating_index_values(choice):
    abc = ["A", "B", "C"]
    y_value = abc.index(list(choice)[0])
    num = ["1", "2", "3"]
    x_value = num.index(list(choice)[1])
    return x_value, y_value


def analyse_sign(arr):
    for i in range(len(arr)):
        col = [row[i] for row in arr]
        diagonal1 = [arr[0][0], arr[1][1], arr[2][2]]
        diagonal2 = [arr[0][2], arr[1][1], arr[2][0]]
        if arr[i] == ["❌", "❌", "❌"]:
            return "❌"
        if col == ["❌", "❌", "❌"]:
            return "❌"
        if diagonal1 == ["❌", "❌", "❌"] or diagonal2 == ["❌", "❌", "❌"]:
            return "❌"
        if arr[i] == ["⭕", "⭕", "⭕"]:
            return "⭕"
        if col == ["⭕", "⭕", "⭕"]:
            return "⭕"
        if diagonal1 == ["⭕", "⭕", "⭕"] or diagonal2 == ["⭕", "⭕", "⭕"]:
            return "⭕"
    return "none"


def game():
    decision = input('Do you want to play the game of tic, toe? Type "Y" for yes and "N" for no: ').upper()

    if decision == "Y":
        arr = [[0 for i in range(3)] for j in range(3)]
        possibilities = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]

        sign_selection = input("Choose your symbol to start the game. Type '1' for '❌' or 'O' for '⭕' \n")
        if sign_selection == "1":
            user_sign = "❌"
            opponent_sign = "⭕"
        elif sign_selection == "0":
            opponent_sign = "❌"
            user_sign = "⭕"
        else:
            print("invalid number entered")
            game()
        grid(arr)

        my_dict = {
            user_sign: "you",
            opponent_sign: "other_person",
        }

        n = 5
        while n >= 0:
            user_position = input("Please enter a position like A1, A2, B1, C3...").upper()

            x, y = calculating_index_values(user_position)

            while arr[x][y] != 0:
                user_position = input("Please enter a valid position").upper()
                x, y = calculating_index_values(user_position)
                
            arr[x][y] = user_sign
            grid(arr)

            winner = analyse_sign(arr)
            if winner == "none":
                pass
            else:
                print(f"{my_dict[winner]} are/is the winner")
                game()
                break

            if n == 1:
                print("It's a Draw!")
                game()
                arr = [[0 for i in range(3)] for j in range(3)]
                break

            print("🤔 OPPONENTS TURN 🤔")
            opponent_choice = opponents_turn(user_position, possibilities)
            p, q = calculating_index_values(opponent_choice)
            arr[p][q] = opponent_sign
            grid(arr)

            winner = analyse_sign(arr)
            if winner == "none":
                pass
            else:
                print(f"{my_dict[winner]} are/is the winner")
                game()
                break

            n -= 1

game()