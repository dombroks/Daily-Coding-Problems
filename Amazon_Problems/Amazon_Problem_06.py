# -*- coding: utf-8 -*-
"""
This problem was asked by Amazon.

Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.
"""

def break_test(sentence, k):
  words = sentence.split()

  broken_text = list()
  char_counter = -1
  current_words = list()
  index = 0 
  while index < len(words):
    word = words[index]

    if len(word) > k :
      return None
    
    if char_counter + len(word) + 1 <= k:
      char_counter += len(word) + 1
      current_words.append(word)
      index += 1
    else:
      broken_text.append(" ".join(current_words))
      char_counter = -1
      current_words = list()
  broken_text.extend(current_words)
  return broken_text

# Driver code
assert not break_test("wikipedia",8)
assert break_test("the quick brown fox jumps over the lazy dog", 10) == [
    "the quick", "brown fox", "jumps over", "the lazy", "dog"]
