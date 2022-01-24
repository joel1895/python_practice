# consider an experiment, selecting an element from the list A randomly with probability proportional to its magnitude.
# assume we are doing the same experiment for 100 times with replacement, in each experiment you will print a number that is selected randomly from A.

# Ex 1: A = [0 5 27 6 13 28 100 45 10 79]
# let f(x) denote the number of times x getting selected in 100 experiments.
# f(100) > f(79) > f(45) > f(28) > f(27) > f(13) > f(10) > f(6) > f(5) > f(0)

from random import uniform

A = [0 ,5 ,27, 6, 13, 28, 100, 45, 10, 79]

def pick_a_number_from_list(A):
    # your code here for picking an element from with the probability propotional to its magnitude
    list_sum = sum(A)
    normalize_list = [i/list_sum for i in A]
    cum_sum = [sum(normalize_list[0:i]) for i in range(1,len(A)+1)]  
    random_uniform = uniform(0,1)
    for i in range(len(cum_sum)):
        if random_uniform<=cum_sum[i]:
            return A[i]    
        else:
            continue

def sampling_based_on_magnitued():
    max_list = []
    for i in range(1,100):
        number = pick_a_number_from_list(A)
        max_list.append(number)
        print(number)
        
    print("Maximum occurence of the number: ",max(max_list,key=max_list.count))



sampling_based_on_magnitued()