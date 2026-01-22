# Drawing and Loops
 14 October 2025

 ## Turtles!
Turtle is a library that helps us visually interact with Python code. 

To draw on the screen with the turtle library, we need to create turtles first. 

 ## Turtle Boilerplate
 
 **Boilerplate** is code that os frequently copied and pasted. It's geeral use is to set up an envrionment. 

 ```python
import turtle

wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")

# TMNT - turtles


wn.exitonclick()
```

## Creating Turtles

> The names of the Teenage Mutant Ninja Turtles
>  Blue bandana - Leonardo (leo)
>  Red bandana - Raphael (raph)
>  Purple bandana - Donatello (donnie)
>  Orange bandana - Michaelangelo (mikey)

To draw on the screen, we need to create **turtle objecs**.

to create a turtle, we can do the following. 

```python
# create a turtle called mikey
mikey = turtle.Turtle()
```


## Functions and Turtles
## Loops/Literation
- **literation** is a word that means repatition.
If we ever want to repat a code we can use a couple of methods.
- When we know **how many times we want repat something** we use for loops.
 ```python
## print "Hello" 10 times
for _ in range(10)
 print("Hello")
	
# example of a loop is a 'counter'
forcounter in range(100)
print(counter).    #0,1,2, ....,99