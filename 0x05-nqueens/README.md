# N Queens

Contains methods that find the possible solutions to the n-queens can
be placed without them attacking each other(The n-queens problem).

## Files

### [0-nqueens.py](./0-nqueens.py)

Usage: `./0-nqueens.py N`

`N` is the number of queens to place.

Sample Output:

```commandline
candiepih@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
candiepih@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
candiepih@ubuntu:~/0x08. N Queens$ 
```



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
