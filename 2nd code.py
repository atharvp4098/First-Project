Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 2+3
5
>>> print(Hello World)
  File "<python-input-1>", line 1
    print(Hello World)
          ^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("Hello")
Hello
>>> a=2;
>>> b=2
>>> axb
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    axb
NameError: name 'axb' is not defined
>>> a*b
4
>>> marks==60
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    marks==60
    ^^^^^
NameError: name 'marks' is not defined. Did you mean: 'vars'?
>>>
>>> v
Traceback (most recent call last):
  File "<python-input-9>", line 1, in <module>
    v
NameError: name 'v' is not defined
>>> var marks==60
  File "<python-input-10>", line 1
    var marks==60
        ^^^^^
SyntaxError: invalid syntax
>>> a=60
>>> if(a>40):
...     print("The Student is Passed")
... else:
...     print("Fail")
...
The Student is Passed
>>> "5"+"3"
'53'
>>> "Pass"+"Fail"
'PassFail'
>>> a=5
>>> b="5"
>>> print(type(a))
<class 'int'>
>>> print(type(a))
<class 'int'>
>>> print(type(b))
<class 'str'>
>>> 5 + "5"
Traceback (most recent call last):
  File "<python-input-20>", line 1, in <module>
    5 + "5"
    ~~^~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> a="10"
>>> b=2
>>> a*b
'1010'
>>> a=73
>>> python
Traceback (most recent call last):
  File "<python-input-25>", line 1, in <module>
    python
NameError: name 'python' is not defined
>>> print("7"+"3"*2)
733
>>> print(2+3*4)
14
>>> print(5 == 5)
True
>>> print(5 == "5")
False
>>> print(True+True)
2
>>> print(true+false)
Traceback (most recent call last):
  File "<python-input-31>", line 1, in <module>
    print(true+false)
          ^^^^
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> print(True+False)
1
>>> print(type(True))
<class 'bool'>
>>> print(isinstance(True, int))
True
>>> print(isinstance(True, int))
True
>>> print(True * 5)
5
>>> print("True" * 5)
TrueTrueTrueTrueTrue
>>>