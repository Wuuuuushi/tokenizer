from PartA import tokenize

import unittest

class TokenizerTests(unittest.TestCase):

    def test_tokenize1(self):
        result = tokenize("/home/rudyx/INF141/Tokenizer/testFile1.txt")
        self.assertEqual(result, ["hi", "1234"])
    
    def test_tokenize2(self):
        result = tokenize("/home/rudyx/INF141/Tokenizer/testFile2.txt")
        self.assertEqual(1,1)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
