from random import choice

"""Word Finder: finds random words from a dictionary.

>>> wf = WordFinder("tester.txt")
    5 words read.

"""


class WordFinder:
    words_list = []
    def __init__(self, words_file):
        """Reads dictionary, reports number of words in dictionary."""
        self.words_file = open(words_file, "r")
        WordFinder.words_list = []
        self.printer()
        print (f"{len(self.words_list)} words read.")

    def printer(self):
        """Adds words from the dictionary to an array."""
        for line in self.words_file:
            WordFinder.words_list.append(line.strip())

    def random(self):
        """Returns random word in array of read dictoinary words."""
        print(choice(WordFinder.words_list))


class SpecialWordFinder(WordFinder):
    """Reads dictionary, reports number of words in dictionary excluding commentts or blank lines."""
    def __init__(self, words_file):
        super().__init__(words_file)
    
    """Adds words from the dictionary to an array excluding comments or blank lines"""
    def printer(self):
        WordFinder.words_list = [line.strip() for line in self.words_file if line.strip() and not line.startswith('#')]
        
        
