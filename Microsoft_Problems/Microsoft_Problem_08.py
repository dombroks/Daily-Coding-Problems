"""
This problem was asked Microsoft.

Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.
"""


class MyFile:
    def __init__(self, contents):
        self.contents = contents
        self.offset = 0
        self.buffer = ""

    def read_7(self):
        start = self.offset
        end = min(self.offset + 7, len(self.contents))
        self.offset = end
        return self.contents[start:end].strip()

    def read_n(self, n):
        while len(self.buffer) < n:
            extra_chars = self.read_7()
            if not extra_chars:
                break
            self.buffer += extra_chars
        n_chars = self.buffer[:n]
        self.buffer = self.buffer[n:]
        return n_chars.strip()


f = MyFile('Hello world')
assert f.read_7() == "Hello w"
assert f.read_7() == "orld"
assert f.read_7() == ""

f = MyFile("Hello world")
assert f.read_n(8) == "Hello wo"
assert f.read_n(8) == "rld"
