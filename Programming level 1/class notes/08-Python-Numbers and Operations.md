# Numbers and Operations
5,Nov, 2025
## Numbers, Variables, and Operations
|Name|  python Name | Example|
  |---|            ---                 | ---      |
  string, 'str'," mr.ubail "
  Boolean, bool,true  false
  integer, int,1 ,2,-100
 ```python
sum= 1+1
diff= 10-8
```
# Multipication and Division
```python
product = 8 * 8
divison = 10/2
```
## Order of operations
```python
#BEDMAS- Brackets.exponents, div/multi, Add/Sub
answer =(2+3)* 4+2/3
```
## Cool
```python
# exopnents
ans+ 3**2
# floor division
ans= 10//3                      #3
# Modulo
ans = 10%2                      #r0
ans = 11%2                      #r1
ans = 12%2                      #r0
ans = 13%2                      #r1
# Increment, decrement, multi-rement, divisi-rement
egg_count = 1
egg_count += 1			# raise the value of egg-count
egg_count -= 1			# decrease value of egg-count
egg-count *= 5			# multiplies value of egg-count
egg_count /= 2			# halves the value of egg-count
```


## Loops again
Recall:

```python
# Repeat something 10 times
for _ in range(10):
	print("This will be printed 10 times.")
```

Another way to loop, over a *sequence*.

```python
grocery_list = [
	"cucmber",
	"eggs",
	"hot wheels",
	"tea"
]

for item in grocery_list:
	# Create a bulleted list and print it out
	bulleted_item = "* " + item
	dashes = "- - -"
	print(bulleted_item)
	print(dashes)
```
Output:
```
* cucmbers
- - -
* eggs
- - -
* hot wheels
- - -
* tea
- - -
``