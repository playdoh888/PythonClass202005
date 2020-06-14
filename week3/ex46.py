banned = "hit"
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
wordlist = paragraph.split(' ')
cleaned_wordlist = []
for aword in wordlist:
    newword = aword.replace(',', '')
    newword = newword.replace('.', '')
    cleaned_wordlist.append(newword.lower())

print(f"Clean Word List: {cleaned_wordlist}")
occur = {}
for word in cleaned_wordlist:
    if word not in occur:
        occur[word] = 1
    else:
        occur[word] = occur[word] + 1
print(f"Occurance: {occur}")

most_occured_count = 0
most_occured_word = ''
for word, count in list(occur.items()):
    if word == banned:
        continue
    else:
        if count > most_occured_count:
            most_occured_count = count
            most_occured_word = word

print(most_occured_word)

print("Start another script that does the same thing!")


def most_common_word(paragraph, banned):
    from collections import Counter
    paragraph = paragraph.lower()
    for i in ['!', "'", '?', ',', ';', '.']:
        paragraph = paragraph.replace(i, '')

    cleaned_wordlist = paragraph.split(' ')
    cleaned_wordlist = [x for x, y in Counter(cleaned_wordlist).most_common() if x not in banned]
    print(cleaned_wordlist)


most_common_word(paragraph, banned)
