text = input("Введите текст: ")


punctuation = '''.,!?;:\()'-"[]{}<>'''
for sign in punctuation:
    text = text.replace(sign, '')


words = text.lower().split()
words_count = len(words)
longest_word = ''
for word in words:
    if len(word) > len(longest_word):
        longest_word = word


vowels = 'аеёиоуыэюя'
count_vowels = sum(1 for sign in text.lower() if sign in vowels)

word_frequency = {}
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1


print(f"Количество слов в тексте: {words_count}")
print(f"Самое длинное слово в тексте: {longest_word}")
print(f"Количество гласных букв в тексте: {count_vowels}")
print("Сколько раз слово встречается в тексте: {}".format(word_frequency))