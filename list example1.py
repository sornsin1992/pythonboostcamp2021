Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> garage = ['toyota','honda','isuzu']
>>> garage.append('suzuki')
>>> print(garage)
['toyota', 'honda', 'isuzu', 'suzuki']
>>> print(garage[2])
isuzu
>>> garage.remove('honda')
>>> print(garage)
['toyota', 'isuzu', 'suzuki']
>>> garage.insert(1,'benz')
>>> print(garage)
['toyota', 'benz', 'isuzu', 'suzuki']
>>> del garage[2]
>>> print(garage)
['toyota', 'benz', 'suzuki']
>>> print(garage[-1])
suzuki
>>> print(garage[-2])
benz
>>> print(garage)
['toyota', 'benz', 'suzuki']
>>> mycar = garage.pop(-1)
>>> print(mycar)
suzuki
>>> print(garage)
['toyota', 'benz']
>>> #.pop ดึงค่ามาเก็บ ถ้าไม่ใส่เลขคือดึงตัวสุดท้าย
>>> garage.appened('suzuki')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    garage.appened('suzuki')
AttributeError: 'list' object has no attribute 'appened'
>>> garage.append('suzuki')
>>> garage[1] = 'tesla'
>>> print(garage)
['toyota', 'tesla', 'suzuki']
>>> print(len(garage))
3
>>> users = ['z','r','t','b','n','p']
>>> user.sort()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    user.sort()
NameError: name 'user' is not defined
>>> users.sort()
>>> print(user)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(user)
NameError: name 'user' is not defined
>>> print(users)
['b', 'n', 'p', 'r', 't', 'z']
>>> users.sort(reverse=True)
>>> print(users)
['z', 't', 'r', 'p', 'n', 'b']
>>> print(sorted(uerse))
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(sorted(uerse))
NameError: name 'uerse' is not defined
>>> print(sorted(users))
['b', 'n', 'p', 'r', 't', 'z']
>>> print(users)
['z', 't', 'r', 'p', 'n', 'b']
>>> users = ['z','r','t','b','n','p']
>>> for u in user:
	print(u)

	
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    for u in user:
NameError: name 'user' is not defined
>>> for u in users:
	print(u)

	
z
r
t
b
n
p
>>> for in sorted(users):
	
SyntaxError: invalid syntax
>>> for u in sorted(users):
	print(u)

	
b
n
p
r
t
z
>>> users.reverse()
>>> for u in users:
	print(u)

	
p
n
b
t
r
z
>>> for u in users:
	print('สวัสดี',u)

	
สวัสดี p
สวัสดี n
สวัสดี b
สวัสดี t
สวัสดี r
สวัสดี z
>>> 