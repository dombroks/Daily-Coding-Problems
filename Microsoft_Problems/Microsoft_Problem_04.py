
"""
This problem was asked by Microsoft.

Implement a URL shortener with the following methods:

    shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
    restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?
"""

import hashlib

class UrlShortner():

    def __init__(self):
      self.hash_map = dict()
      self.m = hashlib.sha256
    
    def shorten(self,url):
      sha_signature = self.m(url.encode()).hexdigest()
      short_hash = sha_signature[:6]
      self.hash_map[short_hash] = url
      return short_hash
    
    def restore(self, short):
        return self.hash_map[short]

# Driver code
url = "https://www.facebook.com/"
url_shortner = UrlShortner()
short = url_shortner.shorten(url)
assert url_shortner.restore(short) == url
assert url_shortner.restore(url_shortner.shorten(url)) == url
