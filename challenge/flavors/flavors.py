#!/usr/bin/env python3
icecream =["flavors", "salty"]
icecream.append(99)
name = input("What is your name?\n") 
print(name)
print(icecream)

print(f"{icecream[-1]} flavors, and {name} chooses to be {icecream[-2]}")
