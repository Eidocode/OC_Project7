def get_stop_words(file):
	file_content = []
	with open(file, "r", encoding='utf-8') as file:
		for word in file:
			file_content.append(word)

	return file_content

test = get_stop_words('./stop_words_fr.txt')

i = 1
for t in test:
	print(str(i) + " - " + t)
	i += 1
