# Chapter 3 Conditional Execution

## The 'if' statement: conditionals to skip some things and execute others

**Indentions are important for ```if``` statements**
### Indentation - This is Scope for Code Blocks in Python
- INCREASE INDENT after an ```if``` or ```for``` statement (after ```:```)
- MAINTAIN INDENT to indicate the scope of the block
- REDUCE INDENT to indicate the end of the block, should align with original ```if``` or ```for```
- Blanks and comments are ignored

Apparently you aren't supposed to use the TAB key, but I have been. Which of course is actually fine since good ol' VSCode automatically makes TAB = 4 spaces in .py files. I wonder how quickly someone came up with a way to switch that for .py files so they didn't have to hit space 4 times for a new line for all that code.  

### Conditionals

- The lines UNDER the ```if``` statements are the conditionals. 

```
    <!-- If statment -->
    if x > 20
        <!-- Conditional -->
        print('Bigger')
```

### Comparison Operators 
- Comparison Operators seem to be the same as JS (doesn't seem to have the ```===``` of JS)
- Comparison Operators look at variables but do not change the variables

### Booleans
- Booleans ask a question and produce a yes/no result which is used to control program flow
- Booleans using comparison operators evaluate to ```True, False``` or Yes/No. 

### Nested Decisions

```
x = 42
if x > 1 :
    print("More than 1")
    <!-- nested if statement, can only be reached through the first block, must be yes -->
    if x < 100 :
        print("Less than 100")
print('all done')


```

### If/Then/Else
Two-way decisions - only choose one path
```if/else``` statements have 1 scope - indentation is the same  

```
x = 4 
if x > 2 :
    print('Bigger')
else :
    print('smaller')

print('all done')

```




## More Complex Conditional Statements

### The "Multi-Way" Branch - if/elif/else

!! Order matters for ```if/elif``` statements because if the first one is true, the block will jump straight to the end. It will not check your ```elif``` statements. !!

```
x = 5
<!-- false -->
if x < 2 :
    print('small')
<!-- true -->
elif x < 10 :
    print('medium')
<!-- does not run -->
else :
    print('large')
<!-- will run because it's not conditional -->
print('All done')

```

Options for multi-way:
- No else 
    - Means somethings may not run (no catch all)
- Many elifs
    - Must be very careful with how you write them

Traceback: determine the origin of an exception/problem in your code. 

### Try/Except structure
- Surround a dangerous section of code with ```try``` / ```except ``` 
- If the code in the ```try``` works, skip the ```except```
- If the code in the ```try``` fails, run the ```except``` section

```try``` /```except``` are for anticipating user errors

- The ```except``` blocks only work in case of errors. Be careful not to overuse it. 
- Whatever line "blows up" is the last line that is printed. 
- Most of the time, wrap user inputs in ```try```'s 


## Exercises
### Exercise 1
 Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
 
### Exercise 2

### Exercise 3
