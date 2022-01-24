# consider you have given n data points in the form of list of
# tuples like S=[(x1,y1),(x2,y2),(x3,y3),(x4,y4),(x5,y5),..,(xn,yn)] and 
# a point P=(p,q) <br> your task is to find 5 closest points(based on cosine distance) in S from P
import math

def closest_points_to_p(S, P):
    cos_dist = []
    for i in S:
        dnomintor = (i[0]*P[0]) + (i[1]*P[1])
        numerator = math.sqrt(i[0]**2 + i[1]**2) * math.sqrt(P[0]**2+P[1]**2)
        n = dnomintor/numerator
        cos_dist.append(math.acos(n))
    closest_points_to_p = [j for i,j in sorted(zip(cos_dist,S))][:5]

    return closest_points_to_p  # its list of tuples

S= [(1,2),(3,4),(-1,1),(6,-7),(0, 6),(-5,-8),(-1,-1),(6,0),(1,-1)]
P= (3,-4)
points = closest_points_to_p(S, P)
print(points) #print the returned values