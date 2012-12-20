# Cyrus Smith (https://github.com/smithcyr/project_euler)
# 
# http://projecteuler.net/problem=67
from re import findall
f = open("triangle67.txt","r")
# initialize the running total for row 0
array = findall("(\d{2})",f.readline())

# Given the x coordinate of a node in the row one level below the 
# running total, return its largest parent node
def next(k,i):
    a = 0
    b = 0
    # if the node is on the right edge of the triangle
    if i==len(k):
        return int(k[i-1])
    # if the node is on the left edge of the triangle
    if i==0:
        return int(k[0])
    # all other cases
    return max(int(k[i-1]),(k[i]))

for i in range(1,100):
    # read each line and store the newest level in a buffer variable
    n = findall("(\d{2})",f.readline())
    # calculate the new largest total for each node in the newest level
    for q in range(0,len(n)):
        n[q] = int(n[q])+next(array,q)
    # overwrite the running total with the buffer
    array = n

# when it's finished print the value of largest path sum
print max(array)
