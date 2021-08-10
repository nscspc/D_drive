Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> eachers["karen"]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    eachers["karen"]
NameError: name 'eachers' is not defined


>>> teachers={"dimple":"cs",'karen':'sociology','harpreet':'mathematics','sabah':'legal studies'}
>>> teachers["karen"]
'sociology'


>>> print("karen teaches",teachers["karen"])
karen teaches sociology
>>> 


>>> teachers
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    teachers
NameError: name 'teachers' is not defined
>>> teachers={"dimple":"cs",'karen':'sociology','harpreet':'mathematics','sabah':'legal studies'}
>>> teachers
{'dimple': 'cs', 'karen': 'sociology', 'harpreet': 'mathematics', 'sabah': 'legal studies'}




>>> d={'vowel1':'a','vowel2':'e','vowel3':'i','vowel4':'o','vowel5':'u'}
>>> d
{'vowel1': 'a', 'vowel2': 'e', 'vowel3': 'i', 'vowel4': 'o', 'vowel5': 'u'}




>>> print(d)
{'vowel1': 'a', 'vowel2': 'e', 'vowel3': 'i', 'vowel4': 'o', 'vowel5': 'u'}




>>> d={"vowel1":"a","vowel2":"e","vowel3":"i","vowel4":"o","vowel5":"u"}
>>> d
{'vowel1': 'a', 'vowel2': 'e', 'vowel3': 'i', 'vowel4': 'o', 'vowel5': 'u'}
>>> print(d)
{'vowel1': 'a', 'vowel2': 'e', 'vowel3': 'i', 'vowel4': 'o', 'vowel5': 'u'}
>>> d[vowel4]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    d[vowel4]
NameError: name 'vowel4' is not defined
>>> d['vowel4']
'o'
