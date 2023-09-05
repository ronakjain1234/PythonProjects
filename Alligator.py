#Created to determine the reprodruction and death of Alligators
import CountFunction as CF
import random
def alligator (x_pos, y_pos, list):
    empty, rabbit, alligator,python = CF.count(x_pos, y_pos, list)
    if list[x_pos][y_pos] == 2:#Function will proceed only  if the observed state is an alligator
        if list[x_pos - 1][y_pos] == 2 :#proceeds if the state neighboring one left is also an alligator
            Probability_of_Death = 0.80 * ((alligator + 1) / (rabbit + alligator + empty + 1 + python))
            if random.random() > Probability_of_Death:
                list[x_pos][y_pos]#based on random generator, alligator does not die
            else:
                list[x_pos][y_pos] = 0#alligator will die if the previous conditional is not satisfied
        elif list[x_pos - 1][y_pos] == 1 or list[x_pos - 1][y_pos] == 0 :#conditional statement, function proceeds if the state to the left is empty or is a rabbit
            Probability_of_Birth =  0.10 * ((empty + rabbit) / (rabbit + alligator + empty + python))#determines likely hood of rabbit or empty state
            if random.random() > Probability_of_Birth:#the state will either remain unchange or
                list[x_pos - 1][y_pos]
            else:
                list[x_pos - 1][y_pos] = 2
    if list[x_pos][y_pos] == 2:#Function will proceed only  if the observed state is an alligator
        if list[x_pos + 1][y_pos] == 2:#evaluates state to the right of the alligator, set of conditional statements, same as previous
            Probability_of_Death =  0.80 * (( 1 + alligator) / (rabbit + alligator + empty + 1 + python))
            if random.random() > Probability_of_Death:
                list[x_pos][y_pos]
            else:
                list[x_pos][y_pos] = 0
        elif list[x_pos + 1][y_pos] == 1 or list[x_pos + 1][y_pos] == 0:
            Probability_of_Birth =  0.10 * ((rabbit + empty) / (rabbit + alligator + empty + python))
            if random.random() > Probability_of_Birth:
                list[x_pos + 1][y_pos]
            else:
                list[x_pos + 1][y_pos] = 2
    if list[x_pos][y_pos] == 2:#Function will proceed only  if the observed state is an alligator
        if list[x_pos][y_pos-1] == 2:#evaluates state directly below the alligator, set of conditionals, same as previous
            Probability_of_Death = 0.80 * (( 1 + alligator) / (rabbit + alligator + empty + 1 + python))
            if random.random() > Probability_of_Death:
                list[x_pos][y_pos]
            else:
                list[x_pos][y_pos] = 0
        elif list[x_pos][y_pos - 1] == 1 or list[x_pos][y_pos - 1] == 0:
            Probability_of_Birth = 0.10 * ((rabbit + empty) / (rabbit + alligator + empty + python))
            if random.random() > Probability_of_Birth:
                list[x_pos][y_pos - 1]
            else:
                list[x_pos][y_pos -1] = 2
    if list[x_pos][y_pos] == 2:#Function will proceed only  if the observed state is an alligator
        if list[x_pos][y_pos-1] == 2:#evaluates on above the alligator, set of conditionals same as previous
            Probability_of_Death =  0.80 * ((1 + alligator) / (rabbit + alligator + empty + 1 + python))
            if random.random() > Probability_of_Death:
                list[x_pos][y_pos]
            else:
                list[x_pos][y_pos] = 0
        elif list[x_pos][y_pos + 1] == 1 or list[x_pos][y_pos + 1] == 0:
            Probability_of_Birth = 0.10 * ((rabbit + empty) / (rabbit + alligator + empty + python))
            if random.random() > Probability_of_Birth:
                list[x_pos][y_pos + 1]
            else:
                list[x_pos][y_pos + 1] = 2
