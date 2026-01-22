# Weekly Journal
5 December 2025
Mia Zhou

## Selection Sort

> Given the following list, using selection sort, sort the indicated element. Outline the steps you would follow in a way similar to the notes.

```
The List:

-- indicates that this part of the list is already sorted
** indicates the element that you should sort

  --  --  **   3    4   5
[-11,  1, 55, 43, 100, 34]
First Comparison:
--  --  **   3    4   5
[-11,  1, 55, 43, 100, 34]
lowest_number = 55
current_number = 55
lowest_index = 2
"current_number is equal to 55 move to next number"

Second Comparison:
--  --  2   **    4   5
[-11,  1, 55, 43, 100, 34]
lowest_number = 55
current_number = 43
lowest_index = 2
"current_number is lower than 55 set lowest_number to 43 set lowest_index to 3"

New values:
lowest_number = 43
lowest_index = 3

Third Comparison:  --  --  2   3   **   5
[-11,  1, 55, 43, 100, 34]
lowest_number = 43
current_number = 100
lowest_index = 3
"current_number is not lower than 43 move onto next number"

Forth Comparison:  --  --  2   3   4  **
[-11,  1, 55, 43, 100, 34]
lowest_number = 43
current_number = 34
lowest_index = 3
"current_number is lower than 43"

Swap:
--  --  *   L    4    5[-11,  1, 55, 43, 100, 34]
swap * and L

New values:--  --  2   3   4  5
[-11,  1, 43, 55, 100, 34]
```

## Sorting Algorithms

> Check out https://visualgo.net/en/sorting.

17

## Closing Questions

> How are you feeling?

Tired and sleepy

> Do you have any food sensitivities or food that you avoid?

avocados and olives

> What's a challenging concept, problem, or idea to understand you remember over the past week in programming?

I was very confused on the sort/sorting concept, but I kinda figured it out after a while. 


> Happy Friday