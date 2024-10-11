from PartA import *

import string

def compareList(tokens, curFile) -> int:
    output = 0
    seen = set()
    fullStr = ""
    alphanum = set(string.ascii_letters + string.digits)
    with open(curFile, "r") as file:
        while True:
            character = file.read(1) #Read character by character to reduce file overload
            if not character:
                
                if fullStr in tokens and fullStr not in seen:
                    output += 1
                    seen.add(fullStr)
                break

            if not character in alphanum:

                if fullStr in tokens and fullStr not in seen: #Checks if the string is empty. If it is continue, otherwise append the string to the tokens.
                    output += 1
                    seen.add(fullStr)

                fullStr = "" 
            else:
                fullStr += character.lower() #Set the character of the alphanum to lowercase in order to satisfy the requirement of tokenization
        return output


def main():
    try:
        if len(sys.argv) == 3:
            tokens = tokenize(sys.argv[1])
            print(compareList(set(tokens), sys.argv[2]))
        else:
            raise IndexError()
    except IndexError:
        print("Please have exactly 2 files.")
    except FileNotFoundError:
        print("FileNotFound: Check file path")

if __name__ == "__main__":
    main()