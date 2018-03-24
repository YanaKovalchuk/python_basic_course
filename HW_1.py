Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> age=input("Сколько Вам лет")
Сколько Вам лет30
>>> year=input("Текущий год")
Текущий год2018
>>> type(year)
<class 'str'>
>>> age=int(age)
>>> type(age)
<class 'int'>
>>> year=int(year)
>>> type(year)
<class 'int'>
>>> s=year-age
>>> print(s)
1988
>>> result=(f"You were born in{s}")
>>> print (result)
You were born in1988
>>> 
