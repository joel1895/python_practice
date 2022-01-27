# Find Which line separates oranges and apples

# consider you have given two set of data points in the form of list of tuples like
# Red =[(R11,R12),(R21,R22),(R31,R32),(R41,R42),(R51,R52),..,(Rn1,Rn2)]
# Blue=[(B11,B12),(B21,B22),(B31,B32),(B41,B42),(B51,B52),..,(Bm1,Bm2)]
# and set of line equations(in the string formate, i.e list of strings)
# Lines = [a1x+b1y+c1,a2x+b2y+c2,a3x+b3y+c3,a4x+b4y+c4,..,K lines]
# Note: you need to string parsing here and get the coefficients of x,y and intercept
# your task is to for each line that is given print "YES"/"NO", you will print yes, if all the red points are one side of the line and blue points are other side of the line, otherwise no
# Ex:
# Red= [(1,1),(2,1),(4,2),(2,4), (-1,4)]
# Blue= [(-2,-1),(-1,-2),(-3,-2),(-3,-1),(1,-3)]
# Lines=["1x+1y+0","1x-1y+0","1x+0y-3","0x+1y-0.5"]

import re
# write your python code here
# you can take the above example as sample input for your program to test
# it should work for any general input try not to hard code for only given input strings


# you can free to change all these codes/structure
def i_am_the_one(red,blue,line):
  
    param = re.findall("[0-9.-]+",line)
    for point in red:
        values = (float(param[0])*point[0])+(float(param[1])*point[1])+float(param[2])
        if values < 0:
            return 'NO'
    
    for point in blue:
        values = (float(param[0])*point[0])+(float(param[1])*point[1])+float(param[2])
        if values > 0:
            return 'NO'

    return 'YES'

Red= [(1,1),(2,1),(4,2),(2,4), (-1,4)]
Blue= [(-2,-1),(-1,-2),(-3,-2),(-3,-1),(1,-3)]
Lines=["1x+1y+0","1x-1y+0","1x+0y-3","0x+1y-0.5"]

for i in Lines:
    yes_or_no = i_am_the_one(Red, Blue, i)
    print(yes_or_no) # the returned value