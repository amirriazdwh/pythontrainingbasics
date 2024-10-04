#Python OOPS


class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Bark"


class Cat(Animal):
    def speak(self):
        return "Meow"


def make_animal_speak(animal: Animal):
    print(animal.speak())


dog = Dog()
cat = Cat()

make_animal_speak(dog)  # Output: Bark
make_animal_speak(cat)  # Output: Meow
#
# Composition in Functional Programming In functional programming, instead of creating a class hierarchy, you create small,
# reusable functions and compose them to achieve the desired behavior.
#
#Let’s say we want to achieve similar functionality using composition in JavaScript:
#
# JavaScript

def speak(sound):
    return lambda: sound

dog_speak = speak("Bark")
cat_speak = speak("Meow")

def make_animal_speak(speak_function):
    print(speak_function())

make_animal_speak(dog_speak)  # Output: Bark
make_animal_speak(cat_speak)  # Output: Meow


#
# Higher - Order
# Functions in Functional
# Programming
# Higher - order
# functions
# are
# functions
# that
# take
# other
# functions as arguments or
# return them as results.This
# allows
# for flexible and reusable code.
#
# Here’s
# an
# example in Python:

def speak(sound):
    def inner():
        return sound

    return inner


dog_speak = speak("Bark")
cat_speak = speak("Meow")


def make_animal_speak(speak_function):
    print(speak_function())


make_animal_speak(dog_speak)  # Output: Bark
make_animal_speak(cat_speak)  # Output: Meow
#
# AI - generated
# code.Review and use
# carefully.More
# info
# on
# FAQ.
#
# Summary
# Inheritance in OOP: You
# define
# a
# base
#
#
# class and create subclasses that inherit from it.This allows you to reuse and extend the base class ’s functionality.
#
#
# Composition in Functional
# Programming: You
# create
# small, reusable
# functions and combine
# them
# to
# achieve
# the
# desired
# behavior.
# Higher - Order
# Functions: Functions
# that
# take
# other
# functions as arguments or
# return them as results, allowing
# for flexible and reusable code.