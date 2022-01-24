# Replace the digits in the string with 

# consider a string that will have digits in that, we need to remove all the not digits and replace the digits with #

# Ex 1: A = 234                Output: ###
# Ex 2: A = a2b3c4             Output: ###
# Ex 3: A = abc                Output:   (empty string)
# Ex 5: A = #2a$#b%c%561#      Output: ####

String = '#2a$#b%c%561#'
def replace_digits(String):
    # write your code
    NewString = ''
    for i in String:
        if i.isnumeric():
            NewString+="#"
    return(NewString) # modified string which is after replacing the # with digits

print(replace_digits(String))