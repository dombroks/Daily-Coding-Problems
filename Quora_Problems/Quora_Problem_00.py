# -*- coding: utf-8 -*-
"""
This problem was asked by Quora.

Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
"""

def is_palindrome(word):
  return word == word[::-1]

def get_closest_palindrome(word):
  if is_palindrome(word):
    return word
  
  if word[0] == word[-1]:
    return word[0] + get_fewest_number_of_characters_palindrome(word[1:-1]) + word[-1]

  else:
    palindrome_one = word[0]  + get_closest_palindrome(word[1:]) + word[0]
    palindrome_two = word[-1] + get_closest_palindrome(word[:-1]) + word[-1]

    if len(palindrome_one) > len(palindrome_two):
      return palindrome_two
    elif len(palindrome_one) < len(palindrome_two):
      return palindrome_one
    
    return palindrome_one if palindrome_one < palindrome_two else palindrome_two
    
# Driver code
assert get_closest_palindrome("google") == "elgoogle"
assert get_closest_palindrome("race") == "ecarace"
