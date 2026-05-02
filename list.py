Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[4.6.7,"python",5+9j,True,False]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a=[4,6.7,"python",5+9j,True,False]
print(a)
[4, 6.7, 'python', (5+9j), True, False]
type(a)
<class 'list'>
b=8.9
type(b)
<class 'float'>
c=[7.8]
type(c)
<class 'list'>


#append
a=["python","java","html"]
a.append("java")
a
['python', 'java', 'html', 'java']
a.append("java","c")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.append("java","c")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["java","c"])
a
['python', 'java', 'html', 'java', ['java', 'c']]


#extend
a="python","java","html"
a.extend(["ai"])
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.extend(["ai"])
AttributeError: 'tuple' object has no attribute 'extend'
a.extend(["ai","mi","ds"])
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.extend(["ai","mi","ds"])
AttributeError: 'tuple' object has no attribute 'extend'
a=["python","java","html"]
a.extend(["ai","mi","ds"])
a
['python', 'java', 'html', 'ai', 'mi', 'ds']
a.extend(["ai"])
a
['python', 'java', 'html', 'ai', 'mi', 'ds', 'ai']
['python', 'java', 'html', 'ai', 'mi', 'ds', 'ai']
['python', 'java', 'html', 'ai', 'mi', 'ds', 'ai']

#insert
a=["apple","banana"]
a.insert(1,"mango")
a
['apple', 'mango', 'banana']


#copy
a=["c","c++","java","python"]
a.copy()
['c', 'c++', 'java', 'python']
a
['c', 'c++', 'java', 'python']

#index
a.index("java")
2

#clear
a.clear()
a
[]
a.append("data")
a
['data']
b=[]
a.append("data")
b.append("data")
b
['data']


#sort
a={"as","by","why","cry","fast","waste","dont"]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
a=["as","by","why","cry","fast","waste","dont"]
a.sort()
a
['as', 'by', 'cry', 'dont', 'fast', 'waste', 'why']
b=[6,7,4,2,9,6,4,3,7,]
b.sort()
b
[2, 3, 4, 4, 6, 6, 7, 7, 9]
a=["@","#","&","!","*"]
a.sort()
a
['!', '#', '&', '*', '@']


# reverse
a=["hi","why","how","hello"]
a.reverse()
a
['hello', 'how', 'why', 'hi']
b=[7,8,3,2,5,4,6]
b.reverse()
b
[6, 4, 5, 2, 3, 8, 7]

#to print decending order
a=[3,1,5,4,9,2,7,6]
a.sort()
a
[1, 2, 3, 4, 5, 6, 7, 9]
a.reverse()
a
[9, 7, 6, 5, 4, 3, 2, 1]
b=[5,1/2,4,6,8,2/4]
a.sort()
a
[1, 2, 3, 4, 5, 6, 7, 9]
b.sort()
b
[0.5, 0.5, 4, 5, 6, 8]
b.reverse()
b
[8, 6, 5, 4, 0.5, 0.5]
b.sort(reverse=True)
b
[8, 6, 5, 4, 0.5, 0.5]


#pop
a=[3,5,4,7,8,9]
a.pop()
9
a
[3, 5, 4, 7, 8]
>>> a.pop(1)
5
>>> a.pop(3)
8
>>> a.pop()
7
>>> a
[3, 4]
>>> 
>>> #remove
>>> a.remove(5)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    a.remove(5)
ValueError: list.remove(x): x not in list
>>> a=[2,4,5,3,6,7,1]
>>> a.remove(3)
>>> a
[2, 4, 5, 6, 7, 1]
>>> 
>>> 
>>> #length
>>> a=[3,5,6,7,8,9,2,]
>>> a.length()
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    a.length()
AttributeError: 'list' object has no attribute 'length'
>>> a.len()
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    a.len()
AttributeError: 'list' object has no attribute 'len'
>>> len(a)
7
>>> a="hello"
>>> len(a)
5
>>> b=["hello'}
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> b=["hello"]
...    
>>> len(b)
...    
1
