# -*- coding: utf-8 -*-
"""
This problem was asked by Facebook.

Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""

from random import randint

NUM_CARDS = 52

def generate_random_number(k):
  return randint(0,k)

def shuffle_card_deck(cards,n):
  for i in deck:
    num = i + generate_random_number(NUM_CARDS - i - 1 )
    temp = cards[num]
    cards[num] = cards[i]
    cards[i] = temp
  return cards

# Driver code
cards=[x for x in range(NUM_CARDS)]
print(shuffle_card_deck(cards,NUM_CARDS))
