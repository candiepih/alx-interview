# Pascal's Triangle

Pascal's triangle is a triangular array of the binomial coefficients that arises in probability theory, combinatorics, and algebra.
All values outside the triangle are considered zero (0).

## Algorithm

This is how i implemented it:

START
  Step  1 - Take number of rows to be printed, n.
  Step  2 - Create a list to store the result.
  Step  3 - Make outer iteration I for n times to print rows
  Step  4 - Make inner iteration for J to (N - 1)
  Step  5 - Add the two numbers in the current row and store it in the next row (N - 1)
  Step  6 - Append the row to the initial list
  Step  7 - Close inner loop
  Step  8 - Close outer loop
STOP

## Files

[0-pascal_triangle.py](./0-pascal_triangle.py)

Creates a `function def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:
