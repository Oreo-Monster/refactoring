'''
name: Naser Al Madi
file: .py
data: 9/22/2020
course: CS151 fall
description: 
'''

import turtle
from window import GameWindow




def check_win(grid, player):
    ''' checks the winner in the grid
    returns true if player won
    returns false if player lost
     '''

    count = 0

    # check rows
    for row in range(len(grid)):
        count = 0
        for col in range(len(grid[0])):
            if grid[row][col] == player:
                count += 1

                if count == 4:
                    return True
            else:
                count = 0
            

    # check columns
    for col in range(len(grid[0])):
        count = 0
        for row in range(len(grid)):
            if grid[row][col] == player:
                count += 1
                
                if count == 4:
                    return True
            else:
                count = 0

    # check diagonal
    for row in range(len(grid)):
        for col in range(len(grid[0])):

            if row + 3 < len(grid) and col + 3 < len(grid[row]):
                if grid[row][col] == 1\
                   and grid[row+1][col+1] == 1\
                   and grid[row+2][col+2] == 1\
                   and grid[row+3][col+3] == 1:
                   return True 



# setting up the window
window = make_window("Connect 4", "light sky blue", 800, 600) #No global code


# the grid
grid = []

for rows in range(5):
    grid.append([0]*7)

# drawing_turtle
my_turtle = make_turtle('classic', "white", 1, 1, 0, 0 )

x_offset = -150
y_offset = 200
tile_size = 50

turn = 1

def play(x_pos, y_pos):
    ''' '''
    global turn

    row = int(abs((y_pos - y_offset - 25) // (50) + 1))
    col = int(abs((x_pos - x_offset - 25) // (50) + 1))
    print(row, col)
    grid[row][col] = turn
    draw_grid(grid, my_turtle, x_offset, y_offset, tile_size)
    window.update()

    if check_win(grid, 1): #Only need to check 
        print("player 1 won")

    elif check_win(grid, 2):
        print("player 2 won")

    if turn == 1:
        turn = 2
    else:
        turn = 1




def main():
    ''' the main function where the game events take place '''

    global turn

    draw_grid(grid, my_turtle, x_offset, y_offset, tile_size)

    while True: #Make some exit condition

        # selected_row = int(input("enter row, player "+ str(turn) +": "))
        # selected_col = int(input("enter col, player "+ str(turn) +": "))

        # if grid[selected_row][selected_col] == 0:

        #     if turn == 1:
        #         grid[selected_row][selected_col] = 1
        #     else:
        #         grid[selected_row][selected_col] = 2

        draw_grid(grid, my_turtle, -150, 200, 50)
        window.update()

        # if check_win(grid, 1):
        #     print("player 1 won")

        # elif check_win(grid, 2):
        #     print("player 2 won")

        # if turn == 1:
        #     turn = 2
        # else:
        #     turn = 1

        window.onscreenclick(play)
        window.listen()

        # window.onclick(play())
        # play()


    # window.exitonclick()

if __name__ == "__main__":
	main()

