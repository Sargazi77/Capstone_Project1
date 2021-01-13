Sentence = input('Write your sentece')
split_sentece = Sentence.split()
sentence_to_word_list = []
for i in split_sentece:
    sentence_to_word_list.append(i.title())

first_word = sentence_to_word_list[0]

print(str(first_word.lower())+ str(''.join(sentence_to_word_list[1:])))
