def count_word_occurrences(fpath, word):
    count = 0
    with open(fpath, 'r') as file:
        for line in file:
            count += line.lower().count(word.lower())
    return count

fpath = 'words.txt'
search = 'future'

occurrences = count_word_occurrences(fpath, search)
print("The word '{}' appears {} times in the file.".format(search, occurrences))