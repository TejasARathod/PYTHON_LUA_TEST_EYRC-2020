
## Slice the List 

Given a list L of numbers and its length, our task was to read these numbers into an array or a list.

Assuming the index starts from 0, use the slice operations to do the following operations:

- print list in reverse order
- for every third number starting with index 0, add 3 to it and print them
- for every fifth number starting with index 0, subtract 7 from it and print
- add all the numbers whose index is in between 3 and 7 (inclusive) and print the result
- You can use the code stub provided here as start to write the solution.
## Input
- First line will contain T, number of testcases. Then the testcases follow.
- Each testcase contains a two line input.
- First line consists of the length of list L.
- Second line consists of the list L of numbers, each separated by space.
## Output
For each testcase, output the following

- list of numbers in the reverse order, each separated by space
- print every 3rd number with 3 added to it
- print every 5th number with 7 subtracted from it
- sum of all numbers with index between 3 and 7 (inclusive)
## Constraints
- 1≤T≤25
- 8≤Length(L)≤50
- every number n in L is an integer
- 100≤n≤100
## Subtasks
- **Subtask #1 (100 points):** original constraints
## Sample Input
    1
    8
    -2 3 -5 1 8 -4 2 7
## Sample Output
    7 2 -4 8 1 -5 3 -2 
    4 5
    -11
    14
## Explanation
The list contains [ -2, 3, -5, 1 , 8 , -4 , 2 , 7 ]. The output on the first line is the reverse of the list.

Every 3rd number in the list filters 1 and 2 therefore we get [ 1, 2 ]. Then 3 is added to each of the number and output is [ 4, 5 ].

Similarly every 5th number in the list filters out [ -4 ]. Subtract 7 from it and print the result that is -11.

Finally add the numbers from index 3 to 7 that is [1, 8, -4, 2, 7 ]. Sum of which is 14.
