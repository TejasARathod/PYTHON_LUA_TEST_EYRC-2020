
## Stars in our pattern
Given a number N, generate a star pattern such that on the first line there are N stars and on the subsequent lines the number of stars decreases by 1.

The pattern generated should have N rows. In every row, every fifth star (*) is replaced with a hash (#).

Every row should have the required number of stars (*) and hash (#) symbols.

The code stub provided here is to be used. It calls the function generatePattern(). Your task is to complete the function.



## Input
- First line will contain T, number of testcases. Then the testcases follow.
- Each testcase contains a single integer N
## Output
- For each testcase, print the star and hash pattern.
## Constraints
- 1≤T≤25
- 1≤N≤100
## Subtasks
- **Subtask #1 (40 points):** N≤15
- **Subtask #2 (60 points):** original constraints
## Sample Input
    2
    14
    5
## Sample Output
    ****#****#****
    ****#****#***
    ****#****#**
    ****#****#*
    ****#****#
    ****#****
    ****#***
    ****#**
    ****#*
    ****#
    ****
    ***
    **
    *
    ****#
    ****
    ***
    **
    *
## Explanation
The first 14 lines is the output of the first test case. The first line should have 14 stars with every 5th star replaced with a hash. Therefore we get pattern of 12 stars and 2 hashes placed at 5th and 10th position. In the subsequent lines the number of * or # keep on decreasing by one until we reach the line 14.

On the 15th line you have the output of the second test case. Hence you have 4 stars and 1 hash which makes 5 characters. The number of characters keep decreasing on the subsequent lines.
