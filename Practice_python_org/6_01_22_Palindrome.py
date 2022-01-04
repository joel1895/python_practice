# Ask the user for a string and print out whether this string is a palindrome or not.
#  (A palindrome is a string that reads the same forwards and backwards.)
s = input("Enter a string: ")
s = s.lower()



######1st approach#####
c = 1
flag = 0
for i in range(len(s)//2):
    if s[i]==s[len(s)-c]:
        c+=1
        flag=1
    else:
        print(s,' is not palindrome')
        flag=0
        break
if flag==1:
    print(s,' is palindrome')


######one line code approach####
if s==s[::-1]:
    print(s,'is a palindrome')
else:
    print(s,"is not a palindrome")


#####3rd approach#####
# s='mother'
s2 = ""
for i in range(len(s)-1,-1,-1):
    print(i)
    s2+= s[i]

print("s2: ",s2)
if s==s2:
    print(s," is a palindrome")
else:
    print(s," is not a palindrome")


####4th approach######
# s = 'dad'
s2 = ''
for i in range(len(s)):
    s2+= s[len(s)-1-i]

print(s2)
if s==s2:
    print(s," is a palindrome")
else:
    print(s," is not a palindrome")