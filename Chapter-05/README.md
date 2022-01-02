## Solutions for practice questions in Chapter-5
### 1.  What does the code for an empty dictionary look like?
> - An empty dictionary is shown as {}.   
### 2. What does a dictionary value with a key 'foo' and a value 42 look like?
> - The dictionary value looks like
```python
{'foo':42}
```
### 3. What is the main difference between a dictionary and a list?
> - Dictionaries are unordered, whereas Lists are ordered. As dictionaries are not ordered as lists, they can't be sliced.
### 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
> - It shows an KeyError as the key 'foo' is not there in the dictionary.
### 5.  If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
> - Both the statements look for 'cat' key in the dictionary.
### 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
> - If a dictionary is sotred in spam, then 'cat' in spam looks whether there is a 'cat' key in the dictionary, whereas 'cat' is spam.values() looks whether there is a  with key with value 'cat' in the dictionary.
### 7. What is a shortcut for the following code?
```python
if 'color' not in spam:
    spam['color'] = 'black'
```
> - Answer
```python
spam.setdefault('color','black')
```
### 8. What module and function can be used to “pretty print” dictionary values?
> - For 'pretty print function pprint module is needed. pprint() function is needed.
- The commands required are
```python
import pprint #module required for pretty print
```
```python
pprint.pprint() #function required for pretty print
```