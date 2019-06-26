
# import string
# import os
# # load doc into memory
# def load_doc(filename):
# 	# open the file as read only
# 	file = open(filename, 'r')
# 	# read all text
# 	text = file.read()
# 	# close the file
# 	file.close()
# 	return text

# # turn a doc into clean tokens
# def clean_doc(doc):
# 	# replace '--' with a space ' '
# 	doc = doc.replace('--', ' ')
# 	# split into tokens by white space
# 	tokens = doc.split()
# 	# remove punctuation from each token
# 	table = str.maketrans('', '', string.punctuation)
# 	tokens = [w.translate(table) for w in tokens]
# 	# remove remaining tokens that are not alphabetic
# 	tokens = [word for word in tokens if word.isalpha()]
# 	# make lower case
# 	tokens = [word.lower() for word in tokens]
# 	return tokens

# # save tokens to file, one dialog per line
# def save_doc(lines, filename):
# 	data = '\n'.join(lines)
# 	file = open(filename, 'w')
# 	file.write(data)
# 	file.close()

# # load document
# in_filename = 'republic_cleaned.txt'
# doc = load_doc(in_filename)
# print(doc[:200])

# # clean document
# tokens = clean_doc(doc)
# print(tokens[:200])
# print('Total Tokens: %d' % len(tokens))
# print('Unique Tokens: %d' % len(set(tokens)))

# # organize into sequences of tokens
# length = 50 + 1
# sequences = list()
# for i in range(length, len(tokens)):
# 	# select sequence of tokens
# 	seq = tokens[i-length:i]
# 	# convert into a line
# 	line = ' '.join(seq)
# 	# store
# 	sequences.append(line)
# print('Total Sequences: %d' % len(sequences))

# # save sequences to file
# out_filename = 'republic_sequences.txt'
# save_doc(sequences, out_filename)
# import keras

# load doc into memory
def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text
from keras.preprocessing.text import Tokenizer

# load
in_filename = 'republic_sequences.txt'
doc = load_doc(in_filename)
lines = doc.split('\n')
# integer encode sequences of words
tokenizer = Tokenizer()
tokenizer.fit_on_texts(lines)
# sequences = tokenizer.texts_to_sequences(lines)

import pickle

# saving
with open('tokenizer0.pkl', 'wb') as handle:
    pickle.dump(tokenizer, handle)