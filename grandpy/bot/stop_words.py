def get_stop_words(file):
	file_content = []
	with open(file, "r") as file:
		for word in file:
			file_content.append(word)

	return file_content

test = get_stop_words('./stop_words_fr.txt')

for t in test:
	print(t)
