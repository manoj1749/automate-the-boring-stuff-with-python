## Solutions for practice questions in Chapter-3
1. Why are functions advantageous to have in your programs?
    > - To reduce the duplicating the code, we use functions. Whenever we decide to change the code, then we need to change the each and every code, instead of it defining functions makes it easier.
2. When does the code in a function execute: when the function is defined or when the function is called?
    > - The code in a function runs when it is called.
3. What statement creates a function?
    > - The 'def' statement creates a function.
4. What is the difference between a function and a function call?
    > - A function is what we define using 'def' statement and contains the code which needs to be executed. And a function call is when a fucntion defined is called and it gets executed.
5. How many global scopes are there in a Python program? How many local scopes?
    > - There is only one global scope, whereas one local function will be assigned for a founction when it is called.
6. What happens to variables in a local scope when the function call returns?
    > - When a function returns, the all variables stored in it gets forgotten as the scope containing these varibales gets destroyed.
7. What is a return value? Can a return value be part of an expression?
    > - When a founction is called and it gets executed there will be result or evaluation of final value, which can be called as return value. And the return value can be part of a expression.
8. If a function does not have a return statement, what is the return value of a call to that function?
    > - When the function does not have a return statement, the return value will be None.
9. How can you force a variable in a function to refer to the global variable?
    > - We can a force a function in local scope to be a global variable by using global statement.
10. What is the data type of None?
    > - The data type of None can be said aas NoneType.
11. What does the import areallyourpetsnamederic statement do?
    > - The statement import areallyourpetsnamederic imports a python library or module called as areallyourpetsnamederic.
12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?
    > - After importing a module called spam, we call the function bacon() in spam using the statement spam.bacon().
13. How can you prevent a program from crashing when it gets an error?
    > - We can prevent a program from crashing when it's getting a error by keeping the line or block of code which causes the error in try clause.
14. What goes in the try clause? What goes in the except clause?
    > - The code-block or the line of code which causes an error goes into the try clause, And when the try clause causes an error the execution moves to the code in except clause.