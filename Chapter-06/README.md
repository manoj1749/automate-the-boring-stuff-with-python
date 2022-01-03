## Solutions for practice questions in Chapter-6
### 1. What are escape characters?
> - 
### 2. What do the \n and \t escape characters represent?
> - 
### 3. How can you put a \ backslash character in a string?
> - 
### 4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?
> - 
### 5. If you don’t want to put \n in your string, how can you write a string with newlines in it?
> - 
### 6. What do the following expressions evaluate to?
```python
'Hello, world!'[1]
'Hello, world!'[0:5]
'Hello, world!'[:5]
'Hello, world!'[3:]
```
> - 'Hello, world!'[1] acceses the character from index-1 which will be 'e'
> -'Hello, world!'[0:5] acceses the character from index-0 upto all the characters before index-5(character in index-5 is not included) which will be 'Hello'
> - 'Hello, world!'[:5] acceses the character before index-5 which will be 'Hello'
> - 'Hello, world!'[3:] acceses the character from index-3 which will be 'lo, world!'
### 7. What do the following expressions evaluate to?
```python
'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()
```
> - 'Hello'.upper() converts the complete string into uppercase letters, which returns with string 'HELLO'
> - 'Hello'.upper().isupper() coverts the complete string to uppercase letters and checks whether the all characters in the string are in uppercase are not, which returns with a boolean value 'True'
> - 'Hello'.upper().lower() coverts the complete string to uppercase letters and again coverts the complete string to lowercase letters, which returns with a string 'hello'
### 8. What do the following expressions evaluate to?
```python
'Remember, remember, the fifth of November.'.split()
```
```python
'-'.join('There can be only one.'.split())
```
> - 
### 9. What string methods can you use to right-justify, left-justify, and center a string?
> - 
### 10. How can you trim whitespace characters from the beginning or end of a string?
> - 