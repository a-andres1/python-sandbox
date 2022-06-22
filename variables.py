# some bad variables. 
xlq3z9ocd = 35.0 
xlq3z9afd = 12.50
xlq3p9afd = xlq3z9ocd * xlq3z9afd
print(xlq3p9afd)

# some less confusing variables
a = 35
b = 12.50
c = a * b
print(c)

# some descriptive variables
hours = 35
rate = 12.50
pay = a * b
print("pay =", pay)
#meaningful variables doesn't mean that python understands payroll....lol. 
#looks like in order to concat strings and variables with python you have to use commas? 
#used [print("pay =", pay, c)]  as a test case for my comma experiment. Yes that works and Python automatically adds spaces which is nice

# import math - don't need math since I'm not going to .floor x {rounds to 0 anyway}
# some further experiements with variables
# declare x as 0.6, now 0.6 is stored
x = 0.6
# here x will be 0.6
# i didn't add a space this time, wonder if that changes the output in the terminal
print ("x is",x)
# because x has not been update yet since everthing on the RIGTH of the assignment statement aka (=), the "x" on the right will be 0.6 still
x = 3.9 * x * ( 1 - x )
# x should now be 0.936
print ("now x is", x)
# update after running code 1.) yes python automatically adds spaces, cool. 2.) python didn't round, but the answer is 0.9359(repeating) so, does python floor something? 
# i had to import math
# using [math.floor(x * 100)/100.0)] rounds it to two decimal places. So, not what we're looking for
# looks like you need to write a function to round down numbers. Will play around with that later. 