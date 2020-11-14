from stop_words import get_stop_words

class Parser:
	"""docstring for Parser"""
	
	def __init__(self):
		self.stop_words = get_stop_words('./stop_words_fr.txt')
		