# IsPalindrome
Method in Python in order to check whether an input is palindrome or not.


Steps of the method:

  a) Gets input
  
  b) Turns to lowercase all the letters of the input
  
  c) Eliminates all the spaces between the words
  
  d) Checks if the lowercased input without spaces is equal as the reversed lowercased input without spaces and prints is palindrome if they are equal and not palindrome if they are not
  
  In order for terminal outputs to be easier to read I used Fore from colorama. If the output is palindrome it gets colored Green while if it is not it is colored Red.
  
  *This may creates an output problem on some terminals. For example in my case:
  
        i) works perfect on online IDE and Microsoft Visual Studio Code 
                                           
        ii) Returns Ascii color characters before the input if I execute the script through windows cmd*/
                                                          

In order to check if the script runs correct I accessed MIT's free wordlist on URl: https://www.mit.edu/~ecprice/wordlist.10000 with 10000 free english words.
I made a request in order to retrieve the URl's content in bytes and after that I generate a random number in range of 1 to 9000 which is the index of the WORDS list that will be decoded from utf8 (remember we retrieved the list in bytes not as a string). 

After that it just checks if the next 1000 words from the random generated index are palindromes and prints the result.  



![A simple run of the programm](https://user-images.githubusercontent.com/25775301/176483418-f39653f8-6bf4-4080-8833-13e20449e624.png)

