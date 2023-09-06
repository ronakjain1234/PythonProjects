#Created to determine the reprodruction and death of Pythons
import CountFunction as CF
import random
def python (x_pos, y_pos, list):
    empty, rabbit, alligator,python = CF.count(x_pos, y_pos, list)
    if list[x_pos][y_pos] == 3:#function will only proceed if the observed state is a python
        if list[x_pos - 1][y_pos] == 3 :#if the neighboring state is also a python:
            Probability_of_Death = 0.5 * ((python + 1) / (rabbit + alligator + empty + 1 + python))#probability of death is calculated
            if random.random() > Probability_of_Death:#based on this, the state will either remain the same or become empyty
                list[x_pos][y_pos]
            else:
                list[x_pos][y_pos] = 0
        elif list[x_pos - 1][y_pos] == 1 or list[x_pos - 1][y_pos] == 0 or list[x_pos - 1][y_pos] == 2:#if the neighboring state is anything other than a python
            Probability_of_Birth =  0.4 * ((empty + rabbit + alligator) / (rabbit + alligator + empty + python))#likelyhood of reproduction is calculated
            if random.random() > Probability_of_Birth:#the neighboring state will either remain the same or become a python
                list[x_pos - 1][y_pos]
            else:
                list[x_pos - 1][y_pos] = 3
    if list[x_pos][y_pos] == 3:#same as previous set of conditional statements however evaluating the state to the right of the observed python
        if list[x_pos + 1][y_pos] == 3:#evaluates the state to the right of the python
            Probability_of_Death =  0.5 * (( 1 + python) / (rabbit + alligator + empty + 1 + python))
            if random.random() > Probability_of_Death:
                list[x_pos][y_pos]
            else:
                list[x_pos][y_pos] = 0
        elif list[x_pos + 1][y_pos] == 1 or list[x_pos + 1][y_pos] == 0 or list[x_pos + 1][y_pos] == 2:
            Probability_of_Birth =  0.4 * ((rabbit + empty + alligator) / (rabbit + alligator + empty + python))
            if random.random() > Probability_of_Birth:
                list[x_pos + 1][y_pos]
            else:
                list[x_pos + 1][y_pos] = 3
    if list[x_pos][y_pos] == 3:#same as previous set of conditional statements however evaluating the state below the observed python
        if list[x_pos][y_pos-1] == 3:#evaluates the state below the python
            Probability_of_Death = 0.5 * (( 1 + python) / (rabbit + alligator + empty + 1 + python))
            if random.random() > Probability_of_Death:
                list[x_pos][y_pos]
            else:
                list[x_pos][y_pos] = 0
        elif list[x_pos][y_pos - 1] == 1 or list[x_pos][y_pos - 1] == 0 or list[x_pos][y_pos - 1] == 2:
            Probability_of_Birth = 0.4 * ((rabbit + empty + alligator) / (rabbit + alligator + empty + python))
            if random.random() > Probability_of_Birth:
                list[x_pos][y_pos - 1]
            else:
                list[x_pos][y_pos -1] = 3
    if list[x_pos][y_pos] == 3:#same as previous set of conditional statements however evaluating the state above the observed python
        if list[x_pos][y_pos-1] == 3:#evaluates state above the python
            Probability_of_Death =  0.5 * ((1 + python) / (rabbit + alligator + empty + 1 + python))
            if random.random() > Probability_of_Death:
                list[x_pos][y_pos]
            else:
                list[x_pos][y_pos] = 0
        elif list[x_pos][y_pos + 1] == 1 or list[x_pos][y_pos + 1] == 0 or list[x_pos][y_pos + 1] == 2:
            Probability_of_Birth = 0.4 * ((rabbit + empty + alligator) / (rabbit + alligator + empty + python))
            if random.random() > Probability_of_Birth:
                list[x_pos][y_pos + 1]
            else:
                list[x_pos][y_pos + 1] = 3
