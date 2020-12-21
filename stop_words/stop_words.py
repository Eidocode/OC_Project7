import glob


# Stop Words file used by the application
SW_FILE = "..\\grandpy\\bot\\final_stop_words.fic"

# Gets all .txt in .\stop_words directory
files = glob.glob(".\\stop_words\\*.txt")


def get_words(file):
    """Function used to get all words stored in a file"""

    with open(file, "r", encoding='utf-8') as tfile:
        file_content = tfile.read()
        lines_in_file = file_content.split("\n")

        word_in_file = []
        for word in lines_in_file:
            word_in_file.append(word)

    return word_in_file


def compare_files(file):
    """Function used to compare words stored in one file with the stop_words
    list"""

    sw_file_list = get_words(SW_FILE)  # Words from stop_words file
    this_file_list = get_words(file)  # Words from the specified file0

    diff_list = []  # List used to store all words not present in both lists

    for word in this_file_list:
        if word not in sw_file_list:
            diff_list.append(word)

    return diff_list


def search_word(word):
    """Function used to search a word in stop_words list"""

    sw_file_list = get_words(SW_FILE)

    if word in sw_file_list:
        print("Word *" + word + "* already exist in file")
        return True

    print("Word *" + word + "* not found in file")
    return False


def add_words(words):
    """Function used to add word(s) in stop_words list"""

    i = 0
    if len(words) > 0:
        with open(SW_FILE, "a", encoding='utf-8') as file:
            for word in words:
                i += 1
                print('Added word : ' + word)
                file.write('\n' + word)
            print('==========')
            print(str(i) + ' new word(s) added...')
            print('==========')
    else:
        print('No new word(s) added...')


def main_menu():
    """Main menu"""

    print('')
    print('')
    print('--')
    print('1 : Add new stop word')
    print('2 : Compare/Add stop words file(s) in ./stop_words')
    print('3 : Search a word')
    print('--')
    print('0 : EXIT')
    print('--')
    print('')


print('')
try:
    with open(SW_FILE, 'r'):
        print(SW_FILE + ' already exist')
except:
    with open(SW_FILE, 'w'):
        print('Create ' + SW_FILE)


main_menu_is_active = True
while main_menu_is_active:
    main_menu()
    user_input = input('Choice : ')

    if user_input == '0':
        print('')
        print('Exiting...')
        main_menu_is_active = False
    elif user_input == '1':
        print('')
        word_input = (input('New word : ')).lower()
        is_exist = search_word(word_input)
        if not is_exist:
            add_words(word_input.split(" "))
    elif user_input == '2':
        print('')
        for file in files:
            test = []
            print("***** FILE " + file + " *****")
            words_to_adds = compare_files(file)
            add_words(words_to_adds)
    elif user_input == '3':
        print('')
        word_input = (input('Search : ')).lower()
        search_word(word_input)
    else:
        print('')
        print('Please type a valid menu choice...')
