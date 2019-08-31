nums =[0,1,2,3,4,5,6,7]
squares =[]
triples=[]
for x in nums:
    squares.append(x**2)
    triples.append(x**3)
print("squares are",squares)
print("triples are",triples)

nums=[1,3,4,5,6]
squares = [x**2 for x in nums]
print(squares)

nums=[0,1,2,3,4,5,6,7,8,9,11,14,20]
evensq = [x**2 for x in nums if x%2==0]
print(evensq)