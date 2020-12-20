
"""

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

# node structure.
class TrieNode(): 
    def __init__(self): 
        self.children = {} 
        self.isWord = False
  
class Trie(): 
    def __init__(self):         
        self.root = TrieNode() 
        self.word_list = [] 
  
    def makeTrie(self, keys):        
        for key in keys: 
            self.insert(key) 
  
    def insert(self, key): 
        node = self.root 
  
        for a in list(key): 
            if not node.children.get(a): 
                node.children[a] = TrieNode() 
  
            node = node.children[a] 
  
        node.isWord = True
  
  
    def suggestionsRec(self, node, word): 
        if node.isWord: 
            self.word_list.append(word) 
  
        for a,n in node.children.items(): 
            self.suggestionsRec(n, word + a) 
  
    def printAutoSuggestions(self, key): 
        node = self.root 
        not_found = False
        temp_word = '' 
  
        for a in list(key): 
            if not node.children.get(a): 
                not_found = True
                break
  
            temp_word += a 
            node = node.children[a] 
  
        if not_found: 
            return 0
        elif node.isWord and not node.children: 
            return -1
  
        self.suggestionsRec(node, temp_word) 
  
        for s in self.word_list: 
            print(s) 
        return 1
  
if __name__ == "__main__" :
  keys = ["hello","hi", "dog", "holder", "superman", "x",  
        "hel","hundred", "helper", "help", "helping", "helpers"]  
  key = "he" 
  
  

  t = Trie() 
 
  t.makeTrie(keys) 
  

  msg = t.printAutoSuggestions(key) 
  
  if msg == -1: 
      print("No other strings found with this prefix\n") 
  elif msg == 0: 
      print("No string found with this prefix\n")
