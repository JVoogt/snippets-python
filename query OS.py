'''
    Get Files from OS Dir
'''
import os
items = os.listdir(".")

newlist = []
for names in items:
    if names.endswith(".csv"):
        newlist.append(names)
print(newlist)