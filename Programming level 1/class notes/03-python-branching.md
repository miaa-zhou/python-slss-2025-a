# Branching 
23 september

## `if`
Branching is a concept in computer science that allows us to write code that has *two or more different outcomes*.

This is the "grammar" of the `if` expression. 
```python
if <statement>:
    <code block - line 1>
	<...>
	<code block - line n> 
```

Example:
```python
user_naame = "Mr.Ubial"
if user_name == "Mr.Ubial":
    print ("Access granted.")
	print (" You can see all the secret information")
```

## `elif` and `else`

`elif` and `else` are keywrds we can use to extend our `if` expressions.

If we want to add *more* branches, we use these keyboards. 

`elif` is short for **else if**
`

## Booleans 
>Asking my Computer Science nerd friends.
>"Do you want pizza or burgers?"
>They replied
>"YES"

**Booleans** are a type of data in Python. Booleans are binary and are either `True` or `False`

```python
is_sunny = True
     print ("Bring your sunscreen.")
else:
     print ("Bring a sweater?")
```

### `or`
`or` can be used to join two or more statements together.
An `or` expression is `True` if and only if at least one statment is `True.`
```python
want_burgers = True 
want_pizza = True 

if want_burgers or want_pizza:
     print ("YES")
else:
     print("NO")
```

### `and`

An `and` expression is `True` if anf only if **both** statments are `True`.

```python
want-cookies = True 
want_chips = False

if want_cookies and want_chips:
     print("You get both!")
else:
     print("You get none.") # This will print 
``` 