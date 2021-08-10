fs="abc"
ss="ghi"
ts="ab"

mktrns="".maketrans(fs,ss,ts)
print("".translate(mktrns))

string="abcdef"
mktrns=string.maketrans(fs,ss,ts)
print(string.translate(mktrns))
