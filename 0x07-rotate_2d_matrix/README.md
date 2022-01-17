# Rotate 2D Matrix

Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Requirements:

* Prototype: `def rotate_2d_matrix(matrix):`
* Do not return anything. The matrix must be edited **in-place**. 
* Assuming the matrix will have 2 dimensions and will not be empty.

Sample using main_0.py as sample script:

```bash
candiepih$ cat main_0.py
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

candiepih$
candiepih$
candiepih$
candiepih$ ./main_0.py
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]

candiepih$
```

File: [0-rotate_2d_matrix.py](./0-rotate_2d_matrix.py)