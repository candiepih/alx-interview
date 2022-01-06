# N Queens

Contains methods that find the possible solutions to the n-queens can
be placed without them attacking each other(The n-queens problem).

## Files

### [0-nqueens.py](./0-nqueens.py)

The main file for the project.

**Algorithm**:

1. Start in the leftmost column
2. If all queens are placed
    `return true`
3. Try all rows in the current column.
    For every row:

   
    a) If the queen can be placed safely in this row 
       then mark this [row, column] as part of the 
       solution and recursively check if placing
       queen here leads to a solution.
    b) If placing the queen in [row, column] leads to
       a solution then return true.
    c) If placing queen doesn't lead to a solution then
       unmark this [row, column] (Backtrack) and go to 
       step (a) to try other rows.

4. If all rows have been tried and nothing worked,
   return false to trigger backtracking.
