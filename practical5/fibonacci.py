one=0
two=1
current=0
i=1
#set initial values
while i<=13:
     if i<3:
             current=1
     else:
             current=one+two
#get the third value
     print(current)
     one=two
     two=current
     i=i+1

1
1
2
3
5
8
13
21
34
55
89
144
233
