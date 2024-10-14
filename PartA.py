import sys
import string

import string
import sys

def tokenize(TextFilePath): 
    '''
    Space Complexity: O(n) - In the worst case, if every character is alphanumeric, 
    the size of the tokens list will be the same as the number of characters (n).
    Time Complexity: O(n) - The function reads through each character in the file, 
    and the operations within each iteration (if statements, appending, and lowercase) 
    all take constant time (O(1)).
    '''
    
    tokens = []
    alphanum = set(string.ascii_letters + string.digits) # Set of all alphanumeric characters

    with open(TextFilePath, "r", encoding="utf-8", errors="replace") as file: 
        fullStr = ""
        while True:
            character = file.read(1) # Read character by character
            if not character:
                if fullStr != "": # If fullStr has a string, append it to tokens
                    tokens.append(fullStr)
                fullStr = ""
                break
            if not character in alphanum:
                if fullStr != "": # If fullStr is not empty, append it to tokens
                    tokens.append(fullStr)
                fullStr = "" 
            else:
                fullStr += character.lower() # Convert to lowercase for consistency
        
    return tokens

def computeWordFrequencies(tokens: list): 
    '''
    Time Complexity: O(n log n) - Iterates through the tokens list (O(n)) to populate 
    the dictionary, then sorts it using Python's sorted function, which has 
    an average time complexity of O(n log n) (Timsort algorithm).
    '''
    
    tokenMap = {}
    
    for values in tokens:
        if values not in tokenMap:
            tokenMap[values] = 0
        tokenMap[values] += 1
    
    tokenMap = dict(sorted(tokenMap.items(), key=lambda x: x[1], reverse=True)) 
    return tokenMap

def print_freq(freq): 
    '''
    Time Complexity: O(n) - Iterates through the dictionary's items, printing each one. 
    Since freq.items() returns an iterator over n items, and printing takes O(1) per item, 
    the overall time complexity is O(n).
    '''
    
    for values in freq.items(): 
        print(f"{values[0]} = {values[1]}")

def main():
    '''
    The time complexity of this function depends on the time complexities of 
    `tokenize`, `computeWordFrequencies`, and `print_freq`.
    Given that `tokenize` is O(n), `computeWordFrequencies` is O(n log n), and 
    `print_freq` is O(n), the overall complexity is dominated by the highest, 
    which is O(n log n).
    '''
    
    try:
        for fileName in sys.argv[1:]:
            if fileName[-4::] != ".txt":
                raise TypeError
            tokens = tokenize(fileName)   # O(n)
            freq = computeWordFrequencies(tokens)  # O(n log n)
            print_freq(freq)  # O(n)
    except IndexError:
        print("Please input a textFile")
    except FileNotFoundError:
        print("FileNotFound: Check file path")
    except TypeError:
        print("TypeError: File type not accepted")
    except Exception:
        print("Something unexpected happened")

if __name__ == "__main__":
    main()
