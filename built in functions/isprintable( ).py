print("saffs".isprintable())
print(" ".isprintable())
print("".isprintable())
print("\n".isprintable())
# esccape sequences are not printable

s=chr(97)+chr(27)
ss=chr(27)+chr(97)
print(chr(97)+chr(27),s.isprintable())
print(ss,ss.isprintable())


'''
The isprintable() methods returns True if all characters in the string are printable or the string is empty. If not, it returns False.

Characters that occupy printing space on the screen are known as printable characters. For example:

letters and symbols
digits
punctuation
whitespace
The syntax of isprintable() is:

string.isprintable()

'''
