def count(row, column, list): # creates the grid for alligators, rabbits, pythons,and empty space
    empty, rabbit, alligator,python = 0, 0, 0,0
    if row == 0: # represents the first group of columns and rows
        if column == 0:
            for x in [list[row][column + 1], list[row + 1][column]]:
                if x == 0:# the value zero represents empty space
                    empty += 1 #adds to count of empty space
                elif x == 1: # the value one represents the rabbits
                    rabbit += 1 #adds to count of rabbit
                elif x == 2: # the value two represents the alligators
                    alligator += 1 #adds to count of the alligator
                elif x == 3: # the value three represents the python
                    python += 1 #adds to count of the pythons
    if column == 0:
        if row != 0 and row != 29:# gets count of the rows inbetween the first and last row at the first column
            for x in [list[row+1][column], list[row-1][column], list[row][column+1]]:
                if x == 0:
                    empty += 1
                elif x == 1:
                    rabbit += 1
                elif x == 2:
                    alligator += 1
                elif x == 3:
                    python += 1
    if row == 0:
        if column == 29: #counts the final column at the first row
            for x in [list[row][column - 1], list[row + 1][column]]:
                if x == 0:
                    empty += 1
                elif x == 1:
                    rabbit += 1
                elif x == 2:
                    alligator += 1
                elif x == 3:
                    python += 1
    if row == 0:
        if column != 0 and column != 29: # used to count for all the columns inbetween the first ad last column
            for x in [list[row][column-1], list[row][column + 1], list[row + 1][column]]:
                if x == 0:
                    empty += 1
                elif x == 1:
                    rabbit += 1
                elif x == 2:
                    alligator += 1
                elif x == 3:
                    python += 1
    if row == 29: #gets count of the last row at the first column
        if column == 0:
            for x in [list[row - 1][column], list[row][column + 1]]:
                if x == 0:
                    empty += 1
                elif x == 1:
                    rabbit += 1
                elif x == 2:
                    alligator += 1
                elif x == 3:
                    python += 1
    if row == 29: #gets count of the last row in between first and last column
        if column != 0 and column != 29:
            for x in [list[row - 1][column], list[row][column + 1], list[row][column - 1]]:
                if x == 0:
                    empty += 1
                elif x == 1:
                    rabbit += 1
                elif x == 2:
                    alligator += 1
                elif x == 3:
                    python += 1
    if row == 29:
        if column == 29:#gets count of the last row and the last column
            for x in [list[row - 1][column], list[row][column - 1]]:
                if x == 0:
                    empty += 1
                elif x == 1:
                    rabbit += 1
                elif x == 2:
                    alligator += 1
                elif x == 3:
                    python += 1
    if column == 29:
        if row != 0 and row != 29:#gets count for all the rowsin between the first and last row in the last column
            for x in [list[row + 1][column], list[row - 1][column], list[row][column - 1]]:
                if x == 0:
                    empty += 1
                elif x == 1:
                    rabbit += 1
                elif x == 2:
                    alligator += 1
                elif x == 3:
                    python += 1
    if row != 29 and row != 0:#gets count of all the rows in between the first and last rows
        if column != 0 and column != 29:#gets count of all columns in between firstand last column
            for x in [list[row][column + 1], list[row][column - 1], list[row + 1][column], list[row - 1][column]]:
                if x == 0:
                    empty += 1
                elif x == 1:
                    rabbit += 1
                elif x == 2:
                    alligator += 1
                elif x == 3:
                    python += 1
    return empty, rabbit, alligator,python #receives the count for the four variables




