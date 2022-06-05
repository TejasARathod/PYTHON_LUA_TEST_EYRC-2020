
## Palindrome  
Given a string str, check if its a palindrome. Consider it to be case insensitive.
A palindrome string is a sequence of characters that reads the same forwards and backwards.

If str is found to be a palindrome, print

    It is a palindrome

else print

    It is not a palindrome


## Input
- First line will contain T, number of testcases. Then the testcases follow.
- Each testcase contains a single string str
## Output
- For each testcase, print the output on new line
## Constraints
- 1≤T≤25
- 2≤length(str)≤100
- str may contain alphanumeric characters
## Subtasks
- **Subtask #1 (30 points):** T≤5  and length(str)≤70
- **Subtask #2 (70 points):** original constraints
## Sample Input
    3
    AhheioIehHA
    OeaiensneIaIeO
    wieowppwoeiw
## Sample Output
    It is a palindrome
    It is not a palindrome
    It is a palindrome
## Explanation
The first test case is considered a palindrome since it reads the same forwards or backwards. The capital and lowercase version of the same is considered equivalent as it is mentioned to be case insensitive.
The second test case is not a palindrome since its third character does not match the third character from back.
The third test case is again a palindrome.
