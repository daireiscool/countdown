# Countdown  
   
Simple model to imitate the TV show, "Countdown"  
It uses nltk.corpus.words, as a dictionary of english words.  
Other lists of words can also be used.  


### Generate list of words  
Can Generate words in two methods:  

* generate_letters_automatic(i,j)  
Creates a list of letters, with i consonants and j vowels  
  
* generate_letters(max_length = None)  
Creates a list of letters, where the user chooses constance or vowel.  
If max_length is an int, will only get that many letters.  
Else it will ask the user to input the max_length.  
  
  
### Get words with best score
To get the words with the best score, from the generated letters, run:  
* get_longest_word(letters)  
This returns a list of the words which would generate the highest score, and the score.


### Check word
To check if a created word is correct, run:  
* check_word(word, letters)  
Returns a bool if the word contains the letters.