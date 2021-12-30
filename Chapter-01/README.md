## Solutions for practice questions in Chapter-1
### 1. Which of the following are operators, and which are values?
```python
*
'hello'
-88.8
-
/
+
5
```
> - The operators are: * , - , / , + ; The values are: 'hello' , -88.8 , 5 .
### 2. Which of the following is a variable, and which is a string?
```python
spam
'spam'
```
> - Among those, 'spam' is a string, whereas spam in variable.
### 3. Name three data types.
> - The three data types are string, floating-point numbers and integers.
### 4. What is an expression made up of? What do all expressions do?
> - The expressions are made up of numbers,variables and operators; and they do what they were told to do using operators, like adding,subtracting and multiplying etc.
### 5. This chapter introduced assignment statements, like spam = 10. What is the difference between an expression and a statement?
> - A statement is for assigning something to a variable or something, whereas expression is used to find result of something with the operators provided.
### 6. What does the variable bacon contain after the following code runs?
```python
bacon = 20
bacon + 1
```
> - After the following code runs the variable bacon contains 21, which is an integer data type.
### 7. What should the following two expressions evaluate to?
```python
'spam' + 'spamspam'
'spam' * 3
```
> - We can say that the first expression is concatenation of two strings and the second expression was multiplication of a string and the outcome of both expressions is same, i.e, 'spamspamspam'.
### 8. Why is eggs a valid variable name while 100 is invalid?
> - As a name of variables shouldn't start with integers, so 100 is invalid to keep as a variable name.
### 9. What three functions can be used to get the integer, floating-point number, or string version of a value?
> - Fuctions used on a value to get integer is- int() , string is- str() , floating-point number is- float().
### 10. Why does this expression cause an error? How can you fix it?
```python
'I have eaten ' + 99 + ' burritos.'
```
> - Here in the given expression 99 is and integer data type, hence it can't be concatinated (or added) to a string, We can solve this error by converitng 99 to string by using str(99), then the expression will be like: 'I have eaten ' + str(99) + ' burritos.'