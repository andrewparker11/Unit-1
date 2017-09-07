#Andrew Parker
#9/7/17
#stringAnalysis.py - Gives word and character statistics of a given sentence

sentence = input('Enter A Sentence - ')
characters = len(sentence)
words = sentence.count(' ')
letters = characters-words

print('Your sentence has', characters, 'characters,', letters, 'letters, and', words+1, 'words' )