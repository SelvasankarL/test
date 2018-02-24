#!/usr/bin/python
import commands
test=raw_input("Enter the command to run: ")
x=commands.getoutput(test)
print(x)
