
## Manage the Inventory  
Ash is tasked with maintaining an inventory list of all the items in a lab. The inventory list contains entries of all the items present in the lab along with its quantity. On daily basis items can be borrowed from the lab or new items can be added to the Lab. Hence Ash usually performs 2 operations on the inventory list:

- Adding items to the list
- Deleting items from the list
Ash usually does this manually and would prefer to use a program to maintain the inventory list. Your task is to write a program that will help Ash.

Consider there are N items in the lab initially. Therefore create a list L that will contain all the names of items (item_name) along with its quantity (item_quantity).

Also, make provision for adding/deleting items to/from the list. The item name and its quantity along with the operation (ADD / DELETE) will be specified. 

- Condition for Adding:
Format: ADD item_name quantity

If the item_name of the item to be added does not exist in the list, then add item_name and its quantity to the List L and print ADDED Item item_name
If the item_name of the item to be added exists in the list, then simply update the quantity of the item and print UPDATED Item item_name

- Condition for Deleting:
Format: DELETE item_name quantity

If the item_name of the item to be deleted does not exist in the list, then print Item item_name does not exist
If the item_name of the item to be deleted exists in the list, then check if its quantity in the list L is less than the quantity specified in the Delete operation.
If it is less then, print Item item_name could not be DELETED
Else update the quantity by subtracting the specified amount and print DELETED Item item_name
The code stub provided here is to be used. It calls the function manageInventory(). Your task is to complete the function.
## Input
- First line will contain T, number of testcases. Then the testcases follow.
- Each testcase contains the following:
    - N, the number of items in the lab initially.
    - Followed by list of items in the next N lines. Every line will specify the item_name and item_quantity separated by space.
    - M, the number of operations to be performed.
    - Followed by sequence of operations on every new line. The operation format is: operation_name item_name quantity separated by space.
## Output
For each testcase, output should be as follows:

- Sequence of the print statements for every operation performed on individual lines.
- Finally print the sum of quantities of all items in the list L
## Constraints
- 1≤T≤25
- 1≤N≤100
- 1≤M≤100
- Operations will be either ADD or DELETE in capitals
- 1≤ quantities of each item ≤100
## Subtasks
- **Subtask #1 (20 points):** T≤5 and M≤10
- **Subtask #2 (80 points):** original constraints
## Sample Input
    1
    3
    Servo 3
    Drone 6
    Board 7
    3
    ADD LEDs 4
    DELETE Board 4
    DELETE Servo 4
## Sample Output
    ADDED Item LEDs
    DELETED Item Board
    Item Servo could not be DELETED
    16
## Explanation
Initially the list contained 3 items i.e. {Servo:3,Drone:6,Board:7}
On ADD operation the list was updated to {Servo:3,Drone:6,Board:7,LEDs:4}
On DELETE operation of Board , the list was updated to {Servo:3,Drone:6,Board:3,LEDs:4}
However on DELETE operation of Servo, since the quantity of the Servo in the List was 3 (which is less than 4 as specified in the DELETE operation), hence the operation was not performed and the list remained the same as {Servo:3,Drone:6,Board:3,LEDs:4} and finally the sum 16 was printed.
