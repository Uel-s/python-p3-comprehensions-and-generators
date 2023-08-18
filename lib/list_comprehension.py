#!/usr/bin/env python3

def return_evens(num_list):

    return[digit for digit in num_list if digit % 2 == 0 ]

results=return_evens([0, 1, 3, 5, 7, 8, 9])

print(results)


pass

def make_exclamation(sentence_list):

    return [sentence + "!" for sentence in sentence_list]

out = make_exclamation(["Hello", "I'm doing great", "Python is fun"]) 

print(out)
pass