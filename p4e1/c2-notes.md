# Chapter 2: Variables, Expressions, and Statements 

## The building blocks of Python: Constants, Reserved words, and Variables

- Constants: fixed values
    - numbers/letters/strings (" or ')
- Reserved words
    - very similar to JS words
- Variables: named place in the memore where we store data and retrieve it later
    - variable data is...variable! meaning you can change it later with additional statements

### Variable name rules in Python
- Must start w/letter or underscore_
- Must consist of letters, numbers, and underscores
- Case sensitive (spam, Spam, and SPAM are all different but why would you do that to yourself?)

### Variable "Best Practices" 
- use variable names to help you remember what you're referring to. 

## Assignment statement
- it's the (=) sign. (=) means "assign this to something. 
- "arrow nature"  x = do this first OR x -> things over here will be computed THEN (x) will be changed

```
{
    <!-- start here -->
    x = 0.6
    <!-- have python run this -->
    x = 3.9 * x * ( 1 - x)
    <!-- this should be the output -->
    x = 0.936
}
```

## Exercises

There are five exercises at the end of the chapter I'm going to give a try. 

### Exercise 1

Hmm. What was exercise 1? I'll have to go find it!

### Exercise 2

- Write a program that uses input to prompt a user for their name and then welcomes them.
Easy enough! A big thanks to W3 schools, as always. 

### Exercise 3

- Write a program to prompt the user for hours and rate per hour to compute gross pay.

Some math this time. Still think it will be mostly straight forward. (this is fun, like Node, but easier?)
That was a fun one! Python is nice because I can just wrap things in <int> or <str> and it will convert them. 
Learned that one because the inputs were originally <str> and I needed <int> to do the math. And also learned you can't concat <int>, you must convert to <str> to concat. Which python makes very easy! 

~just found out this won't work with decimals, will return. Or I guess I need to just use a float? I'll check that out~

<float> worked out just fine. Maybe I should just stick to python. Or maybe it's just the beginning so everything is easy! It's like 99.9% that one. But I'll enjoy it while it lasts. 

### Exercise 4

- Assume that we execute the following assignment statements:

    width = 17  
    height = 12.0  

    For each of the following expressions, write the value of the expression and the type (of the value of the expression).

Honestly, this one was pretty straightforward. Just wanted to do some math and look at types. 


### Exercise 5
 - Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

 This one will take a little bit longer, just because I need to google the conversion from Celcius to Fahrenheit. 
 Let's see how long it takes!
 

