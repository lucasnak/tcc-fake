#from nltk.corpus import stopwords
import unicodedata
import spacy
import re
import string
nlp = spacy.load('pt_core_news_sm')

class preprocessor:

	def __init__(self):
		with open('var/stopwords.txt') as f:
			self.cachedStopWords = f.read()
		# self.cachedStopWords = stopwords.words('portuguese')
		# self.stemmer = nltk.stem.SnowballStemmer('portuguese')
		self.translator = str.maketrans({key:' ' for key in string.punctuation})

	def removePonctuation(self, string):
		return string.translate(self.translator)

	def removeNumbers(self, string):
		return re.sub('[0-9]', '' , string)

	def removeStopWords(self, string):
		doc = nlp(string)
		return ' '.join([token.text for token in doc if token.is_stop is False])

	def lemmatize(self, string):
		doc = nlp(string)
		return ' '.join([token.lemma_ for token in doc])

	def prep(self, string, useStopWords = True, lemma = True):
		#removing numbers and ponctuations
		result = self.removeNumbers(self.removePonctuation(string)).lower()

		if useStopWords and lemma:
			doc = nlp(result)
			result = ' '.join([token.lemma_ for token in doc if token.is_stop is False])
		elif useStopWords:
			doc = nlp(result)
			result = ' '.join([token.text for token in doc if token.is_stop is False])
		elif lemma:
			doc = nlp(result)
			result = ' '.join([token.lemma_ for token in doc])

		return result