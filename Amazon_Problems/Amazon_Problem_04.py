# -*- coding: utf-8 -*-
"""
This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
"""



def is_palindrome(s):
    return s == s[::-1] 

def get_longest_palindromic_contiguous_substring(word):
  if is_palindrome(word):
    return word
  
  str1 = get_longest_palindromic_contiguous_substring(word[1:])
  str2 = get_longest_palindromic_contiguous_substring(word[:-1])

  return str1 if len(str1) >= len(str2) else str2

assert get_longest_palindromic_contiguous_substring("bananas") == "anana"
assert get_longest_palindromic_contiguous_substring("aabcdcb") == "bcdcb"
