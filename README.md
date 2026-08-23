# Matrix Operations Toolkit in Python

A comprehensive Python project that demonstrates fundamental **2D Matrix operations** using nested lists, loops, and conditional statements. This project is ideal for beginners learning matrices without using external libraries like NumPy.

## Features

* Create a matrix of any size (`Rows × Columns`)
* Display the original matrix
* Generate the transpose of the matrix
* Calculate the main diagonal sum
* Check whether the matrix is symmetric
* Count even and odd elements
* Find the maximum element in each row
* Find the minimum element in each column
* Search for an element and display its position
* Perform scalar multiplication
* Check whether the matrix is an identity matrix

## Concepts Used

* Nested Lists (2D Lists)
* List Comprehension
* Nested `for` Loops
* Matrix Traversal
* Conditional Statements
* Searching Algorithms
* Matrix Properties

## Example Input

```text
Rows: 3
Columns: 3

1 2 3
2 5 6
3 6 9

Search Element: 6
Scalar Value: 2
```

## Example Output

```text
Original Matrix:
[1, 2, 3]
[2, 5, 6]
[3, 6, 9]

Transposed Matrix:
[1, 2, 3]
[2, 5, 6]
[3, 6, 9]

Main Diagonal Sum: 15
Matrix is Symmetric
Even Elements: 4
Odd Elements: 5

Maximum in Row 1: 3
Maximum in Row 2: 6
Maximum in Row 3: 9

Minimum in Column 1: 1
Minimum in Column 2: 2
Minimum in Column 3: 3

Element found at Row 2, Column 3

Matrix after Scalar Multiplication:
2 4 6
4 10 12
6 12 18

Not an Identity Matrix
```

## Time Complexity

| Operation             | Complexity |
| --------------------- | ---------: |
| Matrix Input          |   O(r × c) |
| Display Matrix        |   O(r × c) |
| Transpose             |   O(r × c) |
| Main Diagonal Sum     |       O(r) |
| Symmetric Check       |      O(r²) |
| Even & Odd Count      |   O(r × c) |
| Row Maximum           |   O(r × c) |
| Column Minimum        |   O(r × c) |
| Element Search        |   O(r × c) |
| Scalar Multiplication |   O(r × c) |
| Identity Matrix Check |      O(r²) |

> **Overall Time Complexity:** **O(r × c)**

## Learning Outcomes

Through this project, you will learn:

* How matrices are represented using Python lists
* Row-wise and column-wise traversal techniques
* Matrix transposition logic
* Diagonal and symmetry concepts
* Searching elements inside a matrix
* Scalar multiplication
* Identity matrix validation
* Writing modular and efficient nested-loop algorithms

---

## Author

**Krishna Sharma**

B.Tech Computer Science & Engineering (AI & ML)

Lovely Professional University
