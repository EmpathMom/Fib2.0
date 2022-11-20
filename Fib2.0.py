
## list comprehentions part 2 nested lists

##look up nested lists
# Author :  Gaylene
# Created by : Gaylene
# Architect(s): Gaylene
# Developer(s): Gaylene
# Created Date: 11/18/22
# Description : 
# Version: 1.0
# Modified by:Gaylene
# Modified Date: 11/18/2022
# Description:
#
##
# assignment: use armstrong and another
#program to convert in to list comprehension

# Regarding fibonacci:
#    Mathematically, we should get the following
 #   fibonacci series: 0 1 1 2 3 5 8 13 21 34 55 89 ... etc

n = int(input())
myList = [0,1]

for i in range(2, n):
    myList.append(myList[i-1] + myList[i-2])

print(myList)
