from PartA import *

import string

'''
O(n) running time. The program will already have the set of tokens from the function call. 
It only has to iterate through the comparison file, which in this case is the third command line argument 
or the second inputted file. This results in an O(n) running time where n is the size of the second file.

Time Complexity: O(n) - The function reads through the entire file character by character (O(n)), 
where n is the number of characters in the file. The operations within the loop (membership checks 
and string operations) all take constant time (O(1)), so the overall complexity remains O(n).
'''

def compareList(tokens, curFile) -> int: 

    
    output = 0
    seen = set()
    fullStr = ""
    alphanum = set(string.ascii_letters + string.digits)
    with open(curFile, "r") as file:
        while True:
            character = file.read(1) # Read character by character to reduce file overload
            if not character:
                if fullStr in tokens and fullStr not in seen:
                    output += 1
                    seen.add(fullStr)
                break

            if not character in alphanum:
                if fullStr in tokens and fullStr not in seen: # Check if the string is empty. If not, add it.
                    output += 1
                    seen.add(fullStr)
                fullStr = "" 
            else:
                fullStr += character.lower() # Convert character to lowercase for consistency
        return output

def main():
    '''
    Time Complexity: O(n) - The overall time complexity depends on the function calls. 
    tokenize(sys.argv[1]) is O(n) as it reads and processes the first file.
    compareList(set(tokens), sys.argv[2]) is also O(n) as it reads and processes the second file.
    Therefore, the overall time complexity is O(n), assuming n is the number of characters 
    in the larger of the two files.
    '''
    
    try:
        if len(sys.argv) == 3:
            tokens = tokenize(sys.argv[1]) # O(n)
            print(compareList(set(tokens), sys.argv[2])) # O(n)
        else:
            raise IndexError()
    except IndexError:
        print("Please have exactly 2 files.")
    except FileNotFoundError:
        print("FileNotFound: Check file path")

if __name__ == "__main__":
    main()
