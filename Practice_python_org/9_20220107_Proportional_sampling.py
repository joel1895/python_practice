from random import uniform

A = [0 ,5 ,27, 6, 13, 28, 100, 45, 10, 79]
# write your python code here
# you can take the above example as sample input for your program to test
# it should work for any general input try not to hard code for only given input examples


# you can free to change all these codes/structure
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