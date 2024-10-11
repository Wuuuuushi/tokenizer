import sys
import string


def tokenize(TextFilePath): # Space = O(n) <- Worst Case if every letter is alphanum then the size of token will be of size N + O(62) <- Number of alphanum | Time Complexity = O(n) <- It will read through the number of characters in the file + 0(3) for the three if statements + 0(1) for appending +  0(1) for lowercase
    tokens = []
    alphanum = set(string.ascii_letters + string.digits)#This is a set of all alphanum characters. This set is used to find whether or not a character in the file is a alpha num

    with open(TextFilePath, "r", encoding = "utf-8", errors = "replace") as file: #Open the file to read and close the file when done
        fullStr = ""
        while True:
            character = file.read(1) #Read character by character to reduce file overload
            if not character:
                if fullStr != "": #This checks if fullStr still has a string that can be appended
                    tokens.append(fullStr)
                fullStr = ""
                break
            if not character in alphanum:
                if fullStr != "": #Checks if the string is empty. If it is continue, otherwise append the string to the tokens.
                    tokens.append(fullStr)
                fullStr = "" 
            else:
                fullStr += character.lower() #Set the character of the alphanum to lowercase in order to satisfy the requirement of tokenization
        
    #File closes here
    return tokens

def computeWordFrequencies(tokens: list): # O(nlogn) only iterates n times where n is equal to the len of the tokens and sorts the list using a quick sort algorithm.

    tokenMap = {}
    
    for values in tokens:
        if values not in tokenMap:
            tokenMap[values] = 0
        tokenMap[values] += 1
    
    tokenMap = dict(sorted(tokenMap.items(), key= lambda x:x[1], reverse = True)) #Sort the frequencies from highest to least here. Python Sorted uses Tim Sort(Much like quickSort). The Average time complexity is O(nlogn) 
    return tokenMap

def print_freq(freq): #O(2n) == O(n) first it sorts the freq and iterates through the sorted list and prints the values

    for values in freq.items(): #Print the values of the sorted array. Sort the array by the values of the dictionary. Dictionary items() returns a tuple of the object use lamba to make an inline function that takes the tuple from items and returns the key which is in index 1
        print(f"{values[0]} = {values[1]}")


def main():
    try:
        for fileName in sys.argv[1::]:
            tokens = tokenize(fileName)
            freq = computeWordFrequencies(tokens)
            print_freq(freq)
    except IndexError:
        print("Please input a textFile")
    except FileNotFoundError:
        print("FileNotFound: Check file path")


if __name__ == "__main__":
    main()