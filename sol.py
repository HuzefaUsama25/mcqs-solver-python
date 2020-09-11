from google import google
import re
import os

search_text = input("Question: ")
choices = input("Enter Choices Separated by (;): ").split(";")

print("\n\tGathering Results")
content = google.search(search_text, lang='en', pages=1)
print("\tPreprocessing Results...")

text= ''
for page in content:
        text+= page.description

text = text.lower()

var = ""
wordlist = []
word_re = re.compile(r"\w+")
words = [text[word.start():word.end()] for word in word_re.finditer(text)]
ngrams = ((words[k] for k in range(j, j + i + 1)) for i in range(len(words)) for j in range(len(words) - i))
for ngram in ngrams:
    for eword in ngram:
        var += eword+" "
    var = var.strip() +  "\n"


text = var.lower().split("\n")

print("\tProcessing Results..\n")

for each in text:
    if "." in each:
        text.remove(each)
    if ">" in each:
        text.remove(each)


nums = []
for this in choices:
    choicenum = 0
    for word in text:
        if this.lower() in word.lower():
            #print("found "+this)
            choicenum = choicenum + 1
    nums.append(choicenum)

whocorrect = nums.index(max(nums))

res = "\n".join("{} {}".format(x, y) for x, y in zip(choices, nums))
print(res)

print("\nThe correct Choice is: "+choices[whocorrect])

