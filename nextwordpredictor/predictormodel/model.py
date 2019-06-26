from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences

class NextWordModel(object):
	"""docstring for NextWordModel"""
	def __init__(self):
		super(NextWordModel, self).__init__()
	
	def load_model_and_tokenizer(self, tokenizer, model_path):
		self.tokenizer = tokenizer
		print('Loading model...')
		self.model = load_model(model_path)
		self.model._make_predict_function()
		print('Model Loaded!')

	def generate_seq(self, seq_length, seed_text, n_words):
		result = list()
		in_text = seed_text
		# generate a fixed number of words
			# for _ in range(n_words):
		# encode the text as integer
		print(seed_text)
		encoded = self.tokenizer.texts_to_sequences([in_text])[0]
		# truncate sequences to a fixed length
		encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
		# predict probabilities for each word
		# yhat = self.model.predict_classes(encoded, verbose=0)
		predicted_l = list(tuple(enumerate(self.model.predict(encoded)[0])))
		top_3 = sorted(predicted_l, key=lambda x: x[1], reverse=True)[:3]
		print(top_3)
		# map predicted word index to word
		predicted_words = []
		for i, word in enumerate(top_3):
			for w in list(self.tokenizer.word_index.items()):
				if w[1] == word[0]:
					predicted_words.append({'word': w[0], 'probability': word[1]})
		return predicted_words