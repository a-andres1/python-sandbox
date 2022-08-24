# CH 3 exercise 1 - need to add a conditional statement

print("What is your name?")
name = input()
print("How much do you make per hour?")
rate = float(input())
print("How many hours did you work?")
hours = float(input())

# conditional - works just fine!
if hours <= 40 :
    total_pay = round(hours * rate)
else :
    if hours > 40 :
        overtime = hours - 40
        base_pay = (40 * rate)
        overtime_pay = (overtime * (rate * 1.5))
        total_pay = (overtime_pay + base_pay)

print("Hey, " + name + "! You worked " + str(hours) +
      " hours and made $" + str(total_pay) + ".")