## Solutions for practice questions in Chapter-2
### 1. What are the two values of the Boolean data type? How do you write them?
> - The two values in Boolean data type are True and False, they were written with their first letter in uppercase and remaining letters in lowercases like - True, False.
### 2. What are the three Boolean operators?
> - The three Boolean operators are and, or & not.
### 3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).   
|**and-operator**|**value**|
|----|----|
|False and False|False|
|False and True|False|
|True and True|True|
|True and False|False|
       
|**or-operator**|**value**|
|----|----|
|False or False|False|
|False or True|True|
|True or True|True|
|True or False|True|
   
|**not-operator**|**value**|
|----|----|
|not True|False|
|not False|True|

### 4. What do the following expressions evaluate to?
    ```python
    (5 > 4) and (3 == 5)
    not (5 > 4)
    (5 > 4) or (3 == 5)
    not ((5 > 4) or (3 == 5))
    (True and True) and (True == False)
    (not False) or (not True)
    ```
- Answer
   ```python
   (5 > 4) and (3 == 5) evaluates to False.
   not (5 > 4) evaluates to False.
   (5 > 4) or (3 == 5) evaluates to True.
   not ((5 > 4) or (3 == 5)) evaluates to False.
   (True and True) and (True == False) evaluates to False.
   (not False) or (not True) evaluates to True.
   ```
### 5.  What are the six comparison operators?
> - The six comparison operators are == , != , > , >= , < , <= .
### 6. What is the difference between the equal to operator and the assignment operator?
> - The equal to (==) operator is used for comparision, whereas assignment operator (=) is used for assigning values to variables and all.
### 7. Explain what a condition is and where you would use one.
> - A Condition is used in a expression in flow control statements. These are evaluated to a boolean values(True, False).
### 8. Identify the three blocks in this code:
```python
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')
```
Answer
> - The 1st block of code starts at print('eggs') line and in this block the other 2 blocks are there, 2nd block of code is print('bacon') which is a single line and 3rd block od code is print('spam') which is also a single line.
### 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
- Answer
 ```python
   if spam == 1:
       print('Hello')
   elif spam == 2:
       print('Howdy')
   else:
       print('Greetings!')
   ```
### 10. What keys can you press if your program is stuck in an infinite loop?
> - We use ctrl+C for exiting a program struck in an infinite loop.
### 11. What is the difference between break and continue?
> - The continue statement probably moves the execution to start of the loop, whereas the break statement will make the execution jump out of the loop to next step of exectution after the loop.
### 12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
> - All these range functions do the same, the range(10) gives 10 integers starting from 0, which means 10 will not be included, where ranege(0,10) the functions tells to start calling from 0 to 10(not including 10), similarly range(0,10,1) does the same but it mentions that it should increase by 1 for every time the loop comes to the start.
### 13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
- Using for loop:
    ```python
    for i in range(1,11):
          print(i)
    ```
- Using while loop:
    ```python
    i = 0
    while i<10:
         i = i + 1
         print(i)
    ```
### 14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
> - After importing the spam module, we call the bacon() function using the command spam.bacon().
