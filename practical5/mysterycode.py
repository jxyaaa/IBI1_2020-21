# What does this piece of code do?
# Answer: judge the size between n and 50

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil


p=False
while p==False:
	p = True
	n = randint(1,100)
#select a number between 1 and 100
	if n > 50:
#compare the size between n and 50
		p = False
#until the number less than 50 is selected

print(n)


