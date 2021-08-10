# else in loops :-

for i in range(10):
    print(i)
else:
    print(10)

print("\n\n")
# the else block will not be executed if the loop is stopped by a break .

for j in range(10):
    print(j)
    if(j==7):
        break
else:
    print(10)

# same with while loop .
