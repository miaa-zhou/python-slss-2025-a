# Files and Data

18 November 2025

## Files
For this section, we'll learn how to open and read text files.
When we open up files, we need to consider the location or **path** to the file.
The path to the file is where the **text file** is with respect to the **python file**. This includes information about the file's **name** and the **folder** that the file lives in.

### Opening Files
To open a file, we use the `open()` function.
the `open()` function returns a **file stream**.
Once open, the **file stream** is like a pipe that we van get information from.

```python
# information.txt is a file we want 
# to connect to
file = open("infrmation.txt")
```

### Reading their contents 
When reading a file stream, you receive the first part of the file first. Then the second, ..., all the way to the end.
To read a part of the file stream, we use the `readline()`method. It gives one line of informatio. If you call it again, you'll get the next line.

```python
# omitte code above

# read a line of text from file 
line = file.readline()		# returns string
second_line = file.readline() # next line
```

If you want to read all lines, you can iterat over the file stream.
```python
# omitted code above
# read every line until the end
for line in file:
    # do something with that line's data
	print(line)
```

### Managing File Streams 
When we open a file stream, we should always close it when we finish. This helps to lower the risk of corrupting any data in the file. To close a file strea, use the `.close()` method.
```python
# omited code aobve
file.close()			# closes stream safely
```

Use with `with` expression to deal with closures 
```python
with open("information.txt") as file:
	line = file.readline()
	for line in file:
		print(line)

file.readline()			# this will break
```

## Lists