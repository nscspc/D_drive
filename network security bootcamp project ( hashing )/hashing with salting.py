import hashlib, binascii, os
 
def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),salt,100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt+pwdhash).decode('ascii')
 
def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

# How it works....
'''
There are two functions involved here:

hash_password : Encodes a provided password in a way that is safe to store on a database or file
verify_password : Given an encoded password and a plain text one is provided by the user,
it verifies whether the provided password matches the encoded (and thus saved) one
hash_password actually does multiple things; it doesn’t just hash the password.
The first thing it does is generate some random salt that should be added to the password.
That’s just the sha256 hash of some random bytes read from os.urandom .
It then extracts a string representation of the hashed salt as a set of
hexadecimal numbers ( hexdigest).

The salt is then provided to pbkdf2_hmac together with the password
itself to hash the password in a randomized way. As pbkdf2_hmac  requires
bytes as its input, the two strings (password and salt) are previously encoded
in pure bytes. The salt is encoded as plain ASCII, as the hexadecimal
representation of a hash will only contain the 0-9 and A-F characters.
While the password is encoded as utf-8 , it could contain any character.
(Is there anyone with emojis in their passwords?)

The resulting pbkdf2 is a bunch of bytes, as you want to store it into
a database; you use binascii.hexlify  to convert the bunch of bytes into
their hexadecimal representation in a string format.  Hexlify is a convenient
way to convert bytes to strings without losing data. It just prints all the
bytes as two hexadecimal digits, so the resulting data will be twice as big
as the original data, but apart from this, it’s exactly the same as the converted data.

In the end, the function joins together the hash with its salt. As you know
that the hexdigest of a sha256  hash (the salt) is always 64 characters
long, by joining them together, you can grab back the salt by reading the
first 64 characters of the resulting string. This will permit verify_password
to verify the password and verify whether the salt used to encode it is required.

Once you have your password, verify_password can then be used to verify
provided passwords against it. So it takes two arguments: the hashed password
and the new password that should be verified. The first thing verify_password
does is extract the salt from the hashed password (remember, you placed it as
the first 64 characters of the string resulting from hash_password).

The extracted salt and the password candidate are then provided to pbkdf2_hmac
to compute their hash and then convert it into a string with binascii.hexlify . If
the resulting hash matches with the hash part of the previously stored password
(the characters after the salt), it means that the two passwords match.

If the resulting hash doesn’t match, it means that the provided password is wrong.
As you can see, it’s very important that you make the salt and the password available
together, because you’ll need it to be able to verify the password and a different
salt would result in a different hash and thus you’d never be able to verify the password.

'''
