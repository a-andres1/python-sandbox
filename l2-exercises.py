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

# exercise 4 -
