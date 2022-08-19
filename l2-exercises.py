# exercise 2 - uses input to prompt a user for their name and welcome user

print("What is your name?")
inp = input()
print("Whaddup, " + inp)

# exercise 3 - small script that prompts user for rate & hours, then does the math for them. I think I will try the round function...
print("What is your name?")
name = input()
print("How much do you make per hour?")
rate = float(input())
print("How many hours did you work?")
hours = float(input())

total_pay = round(hours * rate)

print("Hey, " + name + "! You worked " + str(hours) +
      " hours and made $" + str(total_pay) + ".")

# exercise 4 - getting into expressions

width = 17
height = 12.0

half_w = width//2

half_w_dec = width/2.0

third_height = height/3

math = 1 + 2 * 5

print("Divided by 2 = ", half_w)
print("Divided by decimal = ", half_w_dec)
print("Height Divided by 3 = ", third_height)
print("Some operators and numbers = ", math)
print("Types: ", type(half_w), type(half_w_dec), type(third_height), type(math))
