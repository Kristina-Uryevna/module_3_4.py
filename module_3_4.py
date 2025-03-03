def single_root_words(root_word, *other_words):
    root_word = root_word.lower()
    same_words = []

    for word in other_words:
        lower_word = word.lower()
        if root_word.count(lower_word) > 0 or lower_word.count(root_word) > 0:
            same_words.append(word)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)