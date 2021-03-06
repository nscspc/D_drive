x="asdf"
print(x.encode())
print(x.encode(encoding="UTF-8",errors='strict'))

'''
The string encode() method returns encoded version of the given string.

Since Python 3.0, strings are stored as Unicode, i.e. each character in the string is represented by a code point. So, each string is just a sequence of Unicode code points.

For efficient storage of these strings, the sequence of code points is converted into a set of bytes. The process is known as encoding.

There are various encodings present which treats a string differently. The popular encodings being utf-8, ascii, etc.

Using string's encode() method, you can convert unicoded strings into any encodings supported by Python. By default, Python uses utf-8 encoding.


String encode() Parameters
By default, encode() method doesn't require any parameters.

It returns utf-8 encoded version of the string. In case of failure, it raises a UnicodeDecodeError exception.

However, it takes two parameters:

encoding - the encoding type a string has to be encoded to
errors - response when encoding fails. There are six types of error response
strict - default response which raises a UnicodeDecodeError exception on failure
ignore - ignores the unencodable unicode from the result
replace - replaces the unencodable unicode to a question mark ?
xmlcharrefreplace - inserts XML character reference instead of unencodable unicode
backslashreplace - inserts a \uNNNN escape sequence instead of unencodable unicode
namereplace - inserts a \N{...} escape sequence instead of unencodable unicode

'''
