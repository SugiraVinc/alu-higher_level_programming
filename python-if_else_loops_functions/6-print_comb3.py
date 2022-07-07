#!/usr/bin/python3
for i in range(1, 89):
    if i not in(10, 11):
        print("{:02d}".format(i), end=", ")
print("89")
