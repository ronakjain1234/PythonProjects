#Created to determine the reprodruction and death of Rabbits
import CountFunction as CF
import random

def rabbit(x_pos, y_pos, list):
    empty, rabbit, alligator,python = CF.count(x_pos,y_pos,list)
    if list[x_pos][y_pos] == 1:#function will only proceed if the state being observed is a rabbit
        if list[x_pos - 1][y_pos] == 0:#evaluates state one to the left of the current rabbit
            Probability_of_Birth = 0.80 * (empty / (rabbit + alligator + empty + python))#rate set for probabilty of birth, if the state next to rabbit is empty
            if random.random() > Probability_of_Birth:
                list[x_pos - 1][y_pos] = 0#the state will remain empty if the random generator generates a number higher than the likelyhood of reproduction
            else:
                list[x_pos - 1][y_pos] = 1
        elif list[x_pos - 1][y_pos] == 1:#sets conditional statements if the neighboring state is another rabbit
            Probability_of_Death = 0.30 * (rabbit / (rabbit + alligator + empty + python))#determines whether the neighboring state will become empty or the rabbit will reproduce
            if random.random() > Probability_of_Death:#random generator determines whether rabbit will die or not
                list[x_pos][y_pos] = 1
            else:
                list[x_pos][y_pos] = 0
    if list[x_pos][y_pos] ==1:#function will only proceed if the state being observed is a rabbit
        if list[x_pos + 1][y_pos] == 0:# same as previous set of conditional statements, however, evaluating state one to the right of the current rabbit
            Probability_of_Birth = 0.80 * (empty / (rabbit + alligator + empty + python))
            if random.random() > Probability_of_Birth:
                list[x_pos + 1][y_pos] = 0
            else:
                list[x_pos + 1][y_pos] = 1
        elif list[x_pos + 1][y_pos] == 1:
            Probability_of_Death = 0.30 * (rabbit / (rabbit + alligator + empty + python))
            if random.random() > Probability_of_Death:
                list[x_pos][y_pos] = 1
            else:
                list[x_pos][y_pos] = 0
    if list[x_pos][y_pos] ==1:#function will only proceed if the state being observed is a rabbit
        if list[x_pos][y_pos - 1] == 0:#same as previous set of conditional statements, however, evaluating state one below the current rabbit
            Probability_of_Birth = 0.80 * (empty / (rabbit + alligator + empty + python))
            if random.random() > Probability_of_Birth:
                list[x_pos][y_pos - 1] = 0
            else:
                list[x_pos][y_pos - 1] = 1
        elif list[x_pos][y_pos - 1] == 1:
            Probability_of_Death = 0.30 * (rabbit / (rabbit + alligator + empty + python))
            if random.random() > Probability_of_Death:
                list[x_pos][y_pos] = 1
            else:
                list[x_pos][y_pos] = 0
    if list[x_pos][y_pos] ==1:#function will only proceed if the state being observed is a rabbit
        if list[x_pos][y_pos + 1] == 0:#same as previous set of conditional statements, however, evaluating state one above the current rabit
            Probability_of_Birth = 0.80 * (empty / (rabbit + alligator + empty + python))
            if random.random() > Probability_of_Birth:
                list[x_pos][y_pos + 1] = 0
            else:
                list[x_pos][y_pos + 1] = 1
        elif list[x_pos][y_pos + 1] == 1:
            Probability_of_Death = 0.30 * (rabbit / (rabbit + alligator + empty + python))
            if random.random() > Probability_of_Death:
                list[x_pos][y_pos] = 1
            else:
                list[x_pos][y_pos] = 0
