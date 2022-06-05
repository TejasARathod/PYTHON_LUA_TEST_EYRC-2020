
## Arithmetic Progression with Lambda function
This task was to generate Arithmetic Progression (A.P.) and perform few operations on the series. The first term of sequence a1, the common difference between terms d and the number of terms n in series is given.

We had to generate the A.P. series in a given function. The code stub provided here is to be used. It calls the function generate_AP() to generate the A.P. series and return it.

Then with the use of lambda and map functions, find squares of the terms in series and print it. Finally with the use of reduce function, compute the sum of the squares of terms in series and print it.
## Input
- First line will contain T, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, three integers a1, d and n.
- Single input line contains a1, d and n, first term of series, common difference between terms and the length or number of terms in series, separated by space.
## Output
Output in three lines,

- First line will contain the A.P. series
- Second line will contain the squares of terms in series
- Third line will contain the sum of the squares of terms in series
## Constraints
- 1≤T≤25
- 1≤a1≤100
- 1≤d≤100
- 1≤n≤100
## Subtasks
- **Subtask #1 (30 points):** 1≤a1,d,n≤20
- **Subtask #2 (70 points):** original constraints
## Sample Input
    1
    2 5 7
## Sample Output
    2 7 12 17 22 27 32
    4 49 144 289 484 729 1024
    2723
## Explanation
The series with a1 as 2 and d as 5 will be [2,7,12,17,22,27,32] till the n as 7. The squares of terms in series is self-explanatory. The sum of squares of each term in series is 2723.
