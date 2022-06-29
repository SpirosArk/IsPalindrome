import string 
import random
import requests
from colorama import Fore   
from random import randint



def palindrome(input):

    
    LowercasedInput = input.lower()
    LowercasedInputWithoutWhitespaces = ''.join(LowercasedInput.split())

    if (LowercasedInputWithoutWhitespaces == LowercasedInputWithoutWhitespaces[::-1]):              #Takes the LowercasedInputWithoutWhitespaces, reverses it and checks if they are equal with LowercasedInputWithoutWhitespaces
        print(Fore.GREEN + input + " is a palindrome")                                              #Used green colour if palindrome, because it was difficult to separate on output
         
    else:
        print(Fore.RED + input + " is not a palindrome")                                            #Used red colour if not palindrome, because it was difficult to separate on output
        


word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
WORDS = response.content.splitlines()                                                               #WORDS taken as a list of bytes splitlined

RandomIndexInWordsList =  randint(1,9000)                                                           #Variable to select a random index from WORDS list, and decode the next 1000 words after the random index, range is until 9000 to avoid an out of range error if random chose a number > 9000(9001+1000 = 10001>10000 wordlist so out of range)
print(" {} {} {}".format("\n" "I will generate", 1000,"random words from MIT's online word list" "\n"))

for i in range(RandomIndexInWordsList , RandomIndexInWordsList + 1000):

    palindrome(WORDS[i].decode("utf-8"))                                                            #Decodes the splitlined list of bytes that got as a response from word_site request and checks if they are palindromes

