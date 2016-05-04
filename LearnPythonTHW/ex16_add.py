# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN"

raw_input("?")

print "Opening the file..."
target = open(filename, "w")

print "Truncating the file..."
target.truncate()

print "What's your name?"
name = raw_input("name: ")
print "How old are you?"
age = raw_input("age: ")
print "How much is your weight?"
weight = raw_input("weight: ")
print "How much is your height?"
height = raw_input("height: ")

print "Now riting..."
target.write(name)
target.write("\n")
target.write(age)
target.write("\n")
target.write(weight)
target.write("\n")
target.write(height)
target.write("\n")

print "Now closing..."
target.close()
