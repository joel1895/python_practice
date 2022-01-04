# Ask the user for a string and print out whether this string is a palindrome or not.
#  (A palindrome is a string that reads the same forwards and backwards.)
input_string = input("Enter a string: ")
input_string = input_string.lower()



######1st approach#####
count = 1
flag = 0
for i in range(len(input_string)//2):
    if input_string[i]==input_string[len(input_string)-count]:
        count+=1
        flag=1
    else:
        print(input_string,' is not palindrome')
        flag=0
        break
if flag==1:
    print(input_string,' is palindrome')


######one line code approach####
if input_string==input_string[::-1]:
    print(input_string,'is a palindrome')
else:
    print(input_string,"is not a palindrome")


#####3rd approach#####
# s='mother'
s2 = ""
for i in range(len(input_string)-1,-1,-1):
    print(i)
    s2+= input_string[i]

print("s2: ",s2)
if input_string==s2:
    print(input_string," is a palindrome")
else:
    print(input_string," is not a palindrome")


####4th approach######
# s = 'dad'
s2 = ''
for i in range(len(input_string)):
    s2+= input_string[len(input_string)-1-i]

print(s2)
if input_string==s2:
    print(input_string," is a palindrome")
else:
    print(input_string," is not a palindrome")