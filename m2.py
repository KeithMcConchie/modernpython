Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 10
>>> print('The answer is %d today' % 10)
The answer is 10 today
>>> print('The answer is %d today %d, %20 tomorrow' % 10)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print('The answer is %d today %d, %20 tomorrow' % 10)
TypeError: not enough arguments for format string
>>> print('The answer is %d today %d, %20 tomorrow' % 10, 20)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print('The answer is %d today %d, %20 tomorrow' % 10, 20)
TypeError: not enough arguments for format string
>>> print('The answer is %d today %d, %d tomorrow' % 10)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print('The answer is %d today %d, %d tomorrow' % 10)
TypeError: not enough arguments for format string
>>> print('The answer is %d today %d, %d tomorrow' % 10, 20)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print('The answer is %d today %d, %d tomorrow' % 10, 20)
TypeError: not enough arguments for format string
>>> print('The answer is %d today, %d tomorrow' % 10, 20)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print('The answer is %d today, %d tomorrow' % 10, 20)
TypeError: not enough arguments for format string
>>> print('The answer is %d today' % 10)
The answer is 10 today
>>> print('The answer is %d today, %d tomorrow' % 10 20)
SyntaxError: invalid syntax
>>> print('The answer is %d today, %d tomorrow' % 10, 20)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print('The answer is %d today, %d tomorrow' % 10, 20)
TypeError: not enough arguments for format string
>>> print('The answer is %d today, %d tomorrow' % (10, 20))
The answer is 10 today, 20 tomorrow
>>> print('The answer is %d today, %d %s' % (10, 20, 'tomorrow'))
The answer is 10 today, 20 tomorrow
>>> print('The answer is %d today, %d %s' % (10.3, 20, 'tomorrow'))
The answer is 10 today, 20 tomorrow
>>> print('The answer is {0} today'.format(x))
The answer is 10 today
>>> print('The answer is {0} today {1} tomorrow'.format(x, y))
