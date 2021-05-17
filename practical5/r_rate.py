print("the average number of individual infected by individual with the virus")
r=input()
r=float(r) 
n=84
x=0 
# generation

while x<5:
    n=n*r+n 
#each round n people inferct n*r people,and plus original n people
    x=x+1 
#round
print("r="+str(r)+" n="+str(n))
