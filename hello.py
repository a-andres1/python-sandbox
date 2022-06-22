import random
n = random.random()
print(n)

#a for loop that repeats until it has 5 integers
#created empty list
randomlist = [ ]
#for loop, declaring how many numbers you should go to
for i in range(0,5):
#pick a number between 1 and 40
    x = random.randint(1,40)
    #append the numbers to the list randomlist
    randomlist.append(x)
    #print the list
    print(randomlist)
