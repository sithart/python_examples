#!/usr/bin/env python
# coding: utf-8

# In[6]:


# 1. Slice a Sequence
a = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(a[1:3])
print(a[1:9:2])
print(a[:5])
print(a[9:])
print(a[:])


# In[8]:


# 2. Reverse a Sequence
a = (1, 2, 3, 4, 5)
b = 'sitharthan'
print(a[::-1])
print(b[::-1])


# In[10]:


# 3. Access an Element in a Sequence Using the Reverse Index
a = 'Hello World!'
print(a[-1])
print(a[-5:-1])


# In[12]:


# 4. Multiple Assignments
a, b = 8, 5
print(f'a is {a}; b is {b}')
numbers = [1, 2, 3, 4, 5]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)


# In[13]:


# 5. Check if a Sequence Is Empty
empty_list = [(), '', [], {}, set()]
for item in empty_list:
    if not item:
        print(f'Do something with the {type(item)}')


# In[16]:


# 6. List Comprehensions
a = [1, 2, 3, 4, 5]
[x*2 for x in a]
[x*3 for x in a if x%2 == 1]
[x*3 for x in a if x%2 == 0]


# In[17]:


# 7. Set Comprehensions
a = [1, -2, 2, -3, 3, 4, 4, 5, 5, 5]
{x*x for x in a}


# In[18]:


# 8. Dict Comprehensions
a = [1, 2, 3, 4, 5]
{x: x*x for x in a}


# In[21]:


# 9. Generator Expression
sum(x**2 for x in range(100))
max(x**2 for x in range(100))


# In[25]:


# 10. Unpack a Tuple
items = (0, 'b', 'one', 10, 11, 'zero')
a, b, c, d, e, f = items
print(f)
a, *b, c = items
print(b)
*_, a, b = items
print(a)


# In[28]:


# 11. Use Enumerate() In for Loops
students = ('John', 'Mary', 'Mike')
for i, student in enumerate(students):
    print(f'Iteration: {i}, Student: {student}')
    
for i, student in enumerate(students, 35001):
    print(f'ID: {i}, Student: {student}')


# In[30]:


# 12. Use Reversed() In for Loops
tasks = ['laundry', 'picking up kids', 'gardening', 'cooking']
for task in reversed(tasks):
    print(task)


# In[32]:


# 13. The Zip() Function
students = ('John', 'Mary', 'Mike')
ages = (15, 17, 16)
scores = (90, 88, 82, 17, 14)
for student, age, score in zip(students, ages, scores):
    print(f'{student}, age: {age}, score: {score}')


# In[33]:


# 14. Lambdas for Sorting
students = [{'name': 'John', 'score': 98}, {'name': 'Mike', 'score': 94}, {'name': 'Jennifer', 'score': 99}]
sorted(students, key=lambda x: x['score'])


# In[35]:


# 15. Shorthand Conditional Assignment
some_condition = True
if some_condition:
    x = 5
else:
    x = 3
print(f'x is {x}')
x = 3 if some_condition else 5
print(f'x is {x}')


# In[37]:


# 16. Membership Testing in a Collection
a = ('one', 'two', 'three', 'four', 'five')
if 'one' in a :
    print('The tuple contains one')
b = {0: 'zero', 1: 'one', 2: 'two', 3: 'three'}
if 2 in b.keys():
    print('The dic has the key of 2')


# In[43]:


# 17. Use Get() to Retrieve a Value in a Dictionary
number_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three'}
# number_dict[5]
number_dict.get(5, 'Five')


# In[50]:


# 18. Get the Key Whose Value Is Maximal in a Dictionary
model_scores = {'model_a': 100, 'model_z': 198, 'model_t': 150}
keys, values = list(model_scores.keys()), list(model_scores.values())
keys[values.index(max(values))]
max(model_scores, key=model_scores.get)


# In[54]:


# 19. Debug With the Print() Function
for i in range(5):
    print(i, end=', ' if i < 4 else '\n')
for i in range(5):
    print(f'{i} & {i*i}', end=', ' if i < 4 else '\n')


# In[56]:


# 20. Walrus Operator
# a = ['j', 'a', 'k', 'd', 'c']
# if (n := len(a))%2 == 1:
#     print(f'The number of letters is {n}, which is odd.')


# In[68]:


# 21. Split a String
sentence = 'this is, a python, tutorial, about, idioms.'
sentence.split(', ')
sentence.split(', ', 2)
sentence.rsplit(', ')
sentence.rsplit(', ', 2)


# In[70]:


# 22. Join Strings in an Iterable
words = ('Hello', 'Python', 'Programmers')
'!'.join(words)
words_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three'}
'&'.join(words_dict.values())


# In[72]:


# 23. The Map() Function
numbers = (1, 2, 4, 6)
indices = (2, 1, 0.5, 2)
list(map(pow, numbers, indices))
[pow(x, y) for x, y in zip(numbers, indices)]


# In[77]:


# 24. The Filter() Function
def good_word(x: str):
    has_vowels = not set('aeiou').isdisjoint(x.lower())
    long_enough = len(x) > 7
    good_start = x.lower().startswith('pre')
    return has_vowels & long_enough & good_start
words = ['Good', 'Presentation', 'preschool', 'prefix']
list(filter(good_word, words))


# In[78]:


# 25. Find Out the Most Frequent Element in a List
winnings = ['John', 'Billy', 'Billy', 'Sam', 'Billy', 'John']
max(set(winnings), key = winnings.count)


# In[81]:


# 26. Track the Frequencies of the Elements in a List
winnings = ['John', 'Billy', 'Billy', 'Sam', 'Billy', 'John']
tracked = {item: winnings.count(item) for item in set(winnings)}
sorted(tracked.items(), key=lambda x: x[1], reverse=True)


# In[83]:


# 27. Check the Type of an Object
def check_type(number):
    if type(number) == int:
        print('do something with an int')
    if isinstance(number, (int, float)):
        print('do something with an int or float')
check_type(5)


# In[86]:


# 28. The Any() Function
arrival_hours = {'Mon': 8.5, 'Tue': 8.75, 'Wed': 9, 'Thu': 8.5, 'Fri': 8.5}
arrival_checks = [x>8.75 for x in arrival_hours.values()]
print(arrival_checks)
any(arrival_checks)


# In[89]:


# 29. The All() Function
arrival_hours = {'Mon': 8.5, 'Tue': 8.75, 'Wed': 9, 'Thu': 8.5, 'Fri': 8.5}
arrival_checks_all = [x<9.5 for x in arrival_hours.values()]
all(arrival_checks_all)


# In[91]:


# 30. Use the With Keyword on a File
# with open('a_file.txt') as file:
#     pass
# file.closed

