#Andrew Parker
#9/7/17
#stringAnalysis.py - Gives word and character statistics of a given sentence

sentence = input('Enter A Sentence')
characters = len(sentence)
letters = characters-words
words = sentence.count(' ')



print('Your sentence has', characters, 'characters,',  words+1, 'words' )