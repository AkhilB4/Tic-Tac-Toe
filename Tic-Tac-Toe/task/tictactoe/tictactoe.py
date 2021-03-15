count_X = count_O = 0
flag1 = flag2 = flag3 = flag4 = False

# For printing the tic-tac-toe
print("---------")
rows = []
for i in range(3):
    col = []
    for j in range(5):
        if j in (0, 4):
            print("|", end=" ")
        else:
            col.append('_')
            print(' ', end=" ")
    rows.append(col)
    print()
print("---------")


count = count_empty = 0
while count < 9:
    count_empty = 0
    x_coordinate, y_coordinate = input("Enter the coordinates: ").split()

    if x_coordinate.isnumeric() is True and y_coordinate.isnumeric() is True:

        x_coordinate = int(x_coordinate)
        y_coordinate = int(y_coordinate)

        if 1 <= x_coordinate <= 3 and 1 <= y_coordinate <= 3:
            if rows[x_coordinate - 1][y_coordinate - 1] != '_':
                print("This cell is occupied! Choose another one!")
            else:
                if count % 2 == 0:
                    rows[x_coordinate - 1][y_coordinate - 1] = 'X'
                    count_X += 1
                else:
                    rows[x_coordinate - 1][y_coordinate - 1] = 'O'
                    count_O += 1

                count += 1
                count1 = 0
                print("---------")
                for i in range(3):
                    count2 = 0
                    for j in range(5):
                        if j in (0, 4):
                            print("|", end=" ")
                        else:
                            print(rows[count1][count2], end=" ")
                            count2 += 1
                    print()
                    count1 += 1
                print("---------")

                if (rows[0][0] == 'X' and rows[0][1] == 'X' and rows[0][2] == 'X') \
                   or (rows[1][0] == 'X' and rows[1][1] == 'X' and rows[1][2] == 'X') \
                   or (rows[2][0] == 'X' and rows[2][1] == 'X' and rows[2][2] == 'X') \
                   or (rows[0][0] == 'X' and rows[1][0] == 'X' and rows[2][0] == 'X') \
                   or (rows[0][1] == 'X' and rows[1][1] == 'X' and rows[2][1] == 'X') \
                   or (rows[0][2] == 'X' and rows[1][2] == 'X' and rows[2][2] == 'X') \
                   or (rows[0][0] == 'X' and rows[1][1] == 'X' and rows[2][2] == 'X') \
                   or (rows[0][2] == 'X' and rows[1][1] == 'X' and rows[2][0] == 'X'):
                    flag1 = True
                    break

                if (rows[0][0] == 'O' and rows[0][1] == 'O' and rows[0][2] == 'O') \
                   or (rows[1][0] == 'O' and rows[1][1] == 'O' and rows[1][2] == 'O') \
                   or (rows[2][0] == 'O' and rows[2][1] == 'O' and rows[2][2] == 'O') \
                   or (rows[0][0] == 'O' and rows[1][0] == 'O' and rows[2][0] == 'O') \
                   or (rows[0][1] == 'O' and rows[1][1] == 'O' and rows[2][1] == 'O') \
                   or (rows[0][2] == 'O' and rows[1][2] == 'O' and rows[2][2] == 'O') \
                   or (rows[0][0] == 'O' and rows[1][1] == 'O' and rows[2][2] == 'O') \
                   or (rows[0][2] == 'O' and rows[1][1] == 'O' and rows[2][0] == 'O'):
                    flag2 = True
                    break

                for row in rows:
                    if '_' in row:
                        count_empty += 1

                if (rows[0][0] == 'X' and rows[0][1] == 'X' and rows[0][2] == 'X') \
                   or (rows[1][0] == 'X' and rows[1][1] == 'X' and rows[1][2] == 'X') \
                   or (rows[2][0] == 'X' and rows[2][1] == 'X' and rows[2][2] == 'X') \
                   or (rows[0][0] == 'X' and rows[1][0] == 'X' and rows[2][0] == 'X') \
                   or (rows[0][1] == 'X' and rows[1][1] == 'X' and rows[2][1] == 'X') \
                   or (rows[0][2] == 'X' and rows[1][2] == 'X' and rows[2][2] == 'X'):
                    flag3 = True
                    break

                if (rows[0][0] == 'O' and rows[0][1] == 'O' and rows[0][2] == 'O') \
                   or (rows[1][0] == 'O' and rows[1][1] == 'O' and rows[1][2] == 'O') \
                   or (rows[2][0] == 'O' and rows[2][1] == 'O' and rows[2][2] == 'O') \
                   or (rows[0][0] == 'O' and rows[1][0] == 'O' and rows[2][0] == 'O') \
                   or (rows[0][1] == 'O' and rows[1][1] == 'O' and rows[2][1] == 'O') \
                   or (rows[0][2] == 'O' and rows[1][2] == 'O' and rows[2][2] == 'O'):
                    flag4 = True
                    break

        else:
            print("Coordinates should be from 1 to 3!")

    else:
        print("You should enter numbers!")

if (flag3 and flag4) or (abs(count_X - count_O) >= 2 and count_empty != 0):
    print("Impossible")
elif flag1:
    print("X wins")
elif flag2:
    print("O wins")
elif count_empty != 0 and (flag1 is False or flag2 is False):
    print("Game not finished")
else:
    print("Draw")
