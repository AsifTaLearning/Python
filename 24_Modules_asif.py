# Modules
# Create a Module - step 1

# Use a Module

import my_module

my_module.greeting("tintu")

# Variables in Module

a = my_module.person1["age"]

print(a)

# Re-naming a Module

import my_module as mx

a = mx.person1["age"]

print(a)

# Built-in Modules

import platform

x = platform.system()

print(x)

# Using the dir() Function

import platform

x = dir(platform)

print(x)

# Import From Module

from my_module import person1

print(person1["age"])

