# TIC-TAC-TOW GAME
import random
import time


def display_board():
    # ======================= GAME BOARD ===========================
    print("\n**************** NEW GAME ******************")
    print("===GAME BOARD===\n")
    board_index = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    print("", board_index[0], "  | ", board_index[1], " | ", board_index[2], "\n",
          " - ", "+", " - ", "+", " - ", "\n",
          board_index[3], "  | ", board_index[4], " | ", board_index[5], "\n",
          " - ", "+", " - ", "+", " - ", "\n",
          board_index[6], "  | ", board_index[7], " | ", board_index[8], "\n")

    # ====================== GETTING PLAYER NAME===================
    player_one = "YOU"
    player_two = "PYTHON"
    board_box_count = 0

    while True:
        print(board_box_count)
        if board_box_count == 0:
            print(f"===== {player_one} Mark is 'X' and {player_two} Mark is 'O' =====")

        # ****************** GAME CHECK ROW AND COLUMN WISE FOR PLAYER 2 ****************************
        if (board_index[0] == "O" and board_index[1] == "O" and board_index[2] == "O") or \
                (board_index[0] == "O" and board_index[3] == "O" and board_index[6] == "O"):
            print("\n\t\t\t*****", player_two, " is the Winner*****")
            option = input("\nWANT TO PLAY NEW GAME? Y/N: ")
            option = option.lower()
            if option == "y":
                print("\n\n\n")
                display_board()
            else:
                exit()

        if (board_index[1] == "O" and board_index[4] == "O" and board_index[7] == "O") or \
                (board_index[3] == "O" and board_index[4] == "O" and board_index[5] == "O"):
            print("\n\t\t\t*****", player_two, " is the Winner*****")
            option = input("\nWANT TO PLAY NEW GAME? Y/N: ")
            option = option.lower()
            if option == "y":
                print("\n\n\n")
                display_board()
            else:
                exit()

        if (board_index[2] == "O" and board_index[5] == "O" and board_index[8] == "") or \
                (board_index[6] == "O" and board_index[7] == "O" and board_index[8] == "O"):
            print("\n\t\t\t*****", player_two, " is the Winner*****")
            option = input("\nWANT TO PLAY NEW GAME? Y/N: ")
            option = option.lower()
            if option == "y":
                print("\n\n\n")
                display_board()
            else:
                exit()

        if (board_index[0] == "O" and board_index[4] == "O" and board_index[8] == "O") or \
                (board_index[6] == "O" and board_index[4] == "O" and board_index[2] == "O"):
            print("\n\t\t\t*****", player_two, " is the Winner*****")
            option = input("\nWANT TO PLAY NEW GAME? Y/N: ")
            option = option.lower()
            if option == "y":
                print("\n\n\n")
                display_board()
            else:
                exit()

        # ****************** END *********************

        # ****************** GAME CHECK ROW AND COLUMN WISE FOR PLAYER 1 ****************************
        if (board_index[0] == "X" and board_index[1] == "X" and board_index[2] == "X") or \
                (board_index[0] == "X" and board_index[3] == "X" and board_index[6] == "X"):
            print("\n\t\t\t*****", player_one, " is the Winner*****")
            option = input("\nWANT TO PLAY NEW GAME? Y/N: ")
            option = option.lower()
            if option == "y":
                print("\n\n\n")
                display_board()
            else:
                exit()

        if (board_index[1] == "X" and board_index[4] == "X" and board_index[7] == "X") or \
                (board_index[3] == "X" and board_index[4] == "X" and board_index[5] == "X"):
            print("\n\t\t\t*****", player_one, " is the Winner*****")
            option = input("\nWANT TO PLAY NEW GAME? Y/N: ")
            option = option.lower()
            if option == "y":
                print("\n\n\n")
                display_board()
            else:
                exit()

        if (board_index[2] == "X" and board_index[5] == "X" and board_index[8] == "X") or \
                (board_index[6] == "X" and board_index[7] == "X" and board_index[8] == "X"):
            print("\n\t\t\t*****", player_one, " is the Winner*****")
            option = input("\nWANT TO PLAY NEW GAME? Y/N: ")
            option = option.lower()
            if option == "y":
                print("\n\n\n")
                display_board()
            else:
                exit()

        if (board_index[0] == "X" and board_index[4] == "X" and board_index[8] == "X") or \
                (board_index[6] == "X" and board_index[4] == "X" and board_index[2] == "X"):
            print("\n\t\t\t*****", player_one, " is the Winner*****")
            option = input("\nWANT TO PLAY NEW GAME? Y/N: ")
            option = option.lower()
            if option == "y":
                print("\n\n\n")
                display_board()
            else:
                exit()
        # ****************** END *********************

        # ============ GETTING INPUT FROM PLAYER ==================
        while True:
            try:
                i = int(input("\nENTER PLACE YOU WANT TO MARK 'X': "))
                break
            except ValueError:
                print("invalid input!, Enter number from Game Board")
                continue

        while i >= 9:
            print("invalid input!, Enter box number")
            i = int(input("\nENTER PLACE YOU WANT TO MARK 'X': "))

        if board_index[i] == i:
            board_index[i] = "X"  # (ASSIGNING MARK TO GAME BOARD)
        else:
            while board_index[i] != i:
                print("box already marked")
                i = int(input("\nENTER PLACE YOU WANT TO MARK 'X': "))
            board_index[i] = "X"

        board_box_count += 1

        print("\n")
        print("", board_index[0], "  | ", board_index[1], " | ", board_index[2], "\n",
              " - ", "+", " - ", "+", " - ", "\n",
              board_index[3], "  | ", board_index[4], " | ", board_index[5], "\n",
              " - ", "+", " - ", "+", " - ", "\n",
              board_index[6], "  | ", board_index[7], " | ", board_index[8], "\n")

        # ****************** END *********************

        # ================ CHECKING IS GAME IS TIE OR NOT===========
        if board_box_count == 9:
            print("\n***** GAME OVER *****\n")
            option = input("\nWANT TO PLAY NEW GAME? Y/N: ")
            option = option.lower()
            if option == "y":
                print("\n\n\n")
                display_board()
            else:
                exit()
            exit()
        # ****************** END *********************

        # ============ GETTING INPUT FROM AI ==================

        # if board_box_count == 1:
        i = random.randint(0, 8)

        if board_index[i] == i:
            board_index[i] = "O"  # (ASSIGNING MARK TO GAME BOARD)
        else:
            while board_index[i] != i:
                i = random.randint(0, 8)
            board_index[i] = "O"
        board_box_count += 1
        time.sleep(1)
        print(f"{player_two} Marked 'O' at {i}")
        print("\n")
        print("", board_index[0], "  | ", board_index[1], " | ", board_index[2], "\n",
              " - ", "+", " - ", "+", " - ", "\n",
              board_index[3], "  | ", board_index[4], " | ", board_index[5], "\n",
              " - ", "+", " - ", "+", " - ", "\n",
              board_index[6], "  | ", board_index[7], " | ", board_index[8], "\n")

        # ****************** END *********************


if __name__ == "__main__":
    display_board()

