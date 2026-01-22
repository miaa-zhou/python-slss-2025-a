
# Functions

8 October 

## Function *friends* 

```python
print("Hello!")
print(2.1)
```

Print is a **function** that outputs values to the console. 

```python
user_information = input()
```

Waits until the user puts some information down, then returns their input. 

## What is a Function

> A function is a **block of reusable code** with a **name**

## `def`ining your own Function

```python
def <function_name>(<optional params>):
    <code block>
```

1. Use the `def` keyword
2. give the function a **name**
        1. convention - use lowercase and underscores
3. write your code in an **indented code block**

# Calling a Function 

```python
def say_hello_nicely(name:str):
    print("hello(name)!")


say_hello_nicely("Steve")
```

We use functions to help us save time/keystrokes. 

```python
def
normalize_input(user_input:str)
    """"Takes user input and cleans it up"""
	output = 
user_input.lower().strip(",.!?")
    return output
```


## Parameters

## `return` values

```python
def some_fun():
	print("hello!")

def some_fun_return() -> str:
	print("hello!")
	return "hello"

return_val = some_fun()

print(return_val) # what's the difference?

return_val = some_fun_return()

print(return_val) # what's the difference?
```

## Default Arguments

```python
# our example from notes-3-functions.py
def say_hello_personal(name: str):
	print(f"hello {name}")
say_hello_nicely("David")
say_hello_nicely()
```