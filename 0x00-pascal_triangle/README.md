# Pascal's Triangle

Pascal's triangle is a triangular array of the binomial coefficients that arises in probability theory, combinatorics, and algebra.
All values outside the triangle are considered zero (0).

![pascal](https://user-images.githubusercontent.com/44834632/143431774-a28ac101-d89a-4b79-83ae-749f4e0d57f9.gif)

(***Image courtesy of wikipedia***)

## Algorithm

This is how i implemented it:

START

  Step  1 - Create an empty list to store results
  
  Step  2 - Return same list if N is 0 or less than 0.
  
  Step  3 - Append a list with `1` to list created in step 1
  
  Step  4 - Take number of rows to be printed, n.
  
  Step  3 - Make outer iteration I for n times to print rows
  
  Step  4 - Make inner iteration for J to row I (N - 1)
  
  Step  5 - Add the two numbers in the current row and store it in the next row (N - 1)
  
  Step  6 - Append the row to the initial list
  
  Step  7 - Close inner loop
  
  Step  8 - Close outer loop
  
  Step  9 - Return list created in Step 1
  
STOP

## Files

[0-pascal_triangle.py](./0-pascal_triangle.py)

Creates a `function def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:
