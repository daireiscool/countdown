from nltk.corpus import words
import random
from tqdm import tqdm

try:
    word_list = words.words()
except LookupError as e:
    print(e)
    print("Downloading words...")
    import nltk
    nltk.download('words')

    word_list = words.words()

consonants = "qwrtypsdfghjklzxcvbnm"
vowels = "aeoiu"

def generate_letters_automatic(
    consonant_count=0, 
    vowel_count=0
):
    """
    Randomely picks severals consonants and vowels.
    
    ::param consonant_count: (int) Number of consonants, defualt 0
    ::param vowel_count: (int) Number of vowels, defualt 0
    ::return: (list[string])
    """
    return random.choices(consonants, k = consonant_count) + \
           random.choices(vowels, k = vowel_count)


def generate_letters(max_length = None):
    """
    Function to pick random consonants and vowels,
        by user input.
    If max length is none, has to be manually inputted.
    
    ::param max_length: (int)
    ::returns: (list[string])
    """
    while type(max_length) != int:
        max_length = input("Amount of letters to pick: ")
        try:
            max_length = int(max_length)
        except:
            print("Please input a number, eg 10")

    letters = []
    for letter in range(int(max_length)):
        print("Consonant or Vowel?")
        response = None
        while response not in {"consonant", "vowel", "c", "v"}:
            response = input("Please enter consonant or vowel: ")\
                .lower().strip()
            if response == "consonant" or response == "c":
                letters += [random.choice(consonants)]
                print(f"Letters so far: {letters}")
            elif response == "vowel" or response == "v":
                letters += [random.choice(vowels)]
                print(f"Letters so far: {letters}")
            else:
                print("Please only input consonants or vowel.")
            
    return letters


def check_letters_in_words(word, letters):
    """
    Function to get the number of letters in a word.
    
    ::param word: (string)
    ::param letters: (list)
    """
    count =  0
    for i in letters:
        if i in word:
            ind = word.find(i)
            word = word[:ind] + word[ind+1:]
            count += 1
        else:
            pass

    if len(word) > 0:
        return 0
    else:
        return count


def get_longest_word(letters, word_list=word_list):
    """
    Return the word with the most countdown words.
    Creates  
    
    ::param letters: (list[strings]) List of letters
    ::param word_list: (list[string]) List of strings (english)
    ::return: (list)
    """
    max_words, max_count = [""], 0
    
    for word in tqdm(word_list):
        if all(item in letters for item in word):
            count = check_letters_in_words(word, letters)
            if count > max_count:
                max_words, max_count = [word], count
            elif count == max_count:
                max_words += [word]
            else:
                pass
            
    print(f"The words which contains {', '.join(letters)} are {', '.join(max_words)}, with {max_count} points.")
    return list(set(max_words)), max_count


def check_word(word, letters, word_list=word_list):
    """
    Function to check if a created word is correct.
    
    ::param word: (string)
    ::param letters: (list[string])
    ::param word_list: (list[string])
    ::returns: (boolean)
    """
    word_copy = word
    count = 0
    for i in letters:
        if i in word:
            ind = word.find(i)
            word = word[:ind] + word[ind+1:]
            count += 1
        else:
            pass
    if len(word) > 0:
        print(f"These letters in {word_copy} are extra, : {word}.")
        print(f"Therefore the word does not count.")
        return False
    else:
        print(f"All of {word_copy}'s letters are in the choosen letters.")
        print(f"{word_copy.capitalize()} has a score of {count}.")
        return True