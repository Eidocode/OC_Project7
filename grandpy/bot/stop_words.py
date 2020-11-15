def get_stop_words(file):
	stop_words = []
	with open(file, "r", encoding='utf-8') as this_file:
		file_content = this_file.read()
		lines = file_content.split("\n")
		for word in lines:
			if "##" not in word:
				stop_words.append(word)

	return stop_words
