## Solutions for practice questions in Chapter-4
1. What is []?
   
   > - [] represents an empty list which doesn't contain anything.
   
2.  How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
  
  > - As the spam contains [2, 4, 6, 8, 10], and we need add 'hello' as the third value, as the 3rd place in the list has an index value 2. So it can be done by using spam[2]='hello' statement.

- For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].

3. What does spam[int(int('3' * 2) // 11)] evaluate to?
    
    > - as '3'*2 is 33 as '3' is a string and 33//11=3 and converting into integer it looks like, spam[3]. As spam =  ['a', 'b', 'c', 'd'], then spam[3] = 'd'.
    
4. What does spam[-1] evaluate to?
    
    > - Similarly as spam = ['a', 'b', 'c', 'd'], spam[-1] = 'd'
    
5. What does spam[:2] evaluate to?
    
    > - spam[:2] slices the first 2 characters in the list, therefore spam[:2]= ['a', 'b']
    
### For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

6. What does bacon.index('cat') evaluate to?
    
    > - As bacon = [3.14, 'cat', 11, 'cat', True]. And using the index() function we can find the index of a string or character in a list which we need. Such bacon.index('cat')=1
    
7. What does bacon.append(99) make the list value in bacon look like?
    
    > - bacon.append(99) adds 99 to the list, then the final output looks like, [3.14, 'cat', 11, 'cat', True, 99]
    
8. What does bacon.remove('cat') make the list value in bacon look like?
    
    > - bacon.remove('cat') removes the string 'cat' from the list, then the final output looks like [3.14, 11, 'cat', True]
    
9. What are the operators for list concatenation and list replication?
    
    > - Same as the strings, we use + for concatenation of list and * for replication of lists.
    
10. What is the difference between the append() and insert() list methods?
    
    > - Using append() function we can add an element only at the end of list, whereas using insert() function we can add an element at any position in the list.
    
11. What are two ways to remove values from a list?
    
    > - A list has two ways to remove values from a list, one is remove() function and another is delete statement.
    
12. Name a few ways that list values are similar to string values.
    
    > - The lists and strings both can be sliced and both have indexes, both of them can be concatenated and replicated, both can be passed through len() function for counting, both can be used in for loops and in and not in operators can also be used with them.
    
13. What is the difference between lists and tuples?
    
    > - Lists are mutable, whereas Tuples are immutable form of list data type.
    
14. How do you type the tuple value that has just the integer value 42 in it?
    
    > - If the tuple value that has just the integer value 42 in it then it is represented as (42,). That comma is referred as a trailing coma which indicates that it is a tuple data type.
    
15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
    
    > - Using tuple() we can get tuple form from list and using list() we can get list form from tuple.
    
16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
    
    > - Variables that contain list directly don't contain lists directly, they contain references to list values.
    
17. What is the difference between copy.copy() and copy.deepcopy()?
    
    > - copy.copy() is used for copying lists, whereas copy.deepcopy() will also copy the lists which are in the list.
    
