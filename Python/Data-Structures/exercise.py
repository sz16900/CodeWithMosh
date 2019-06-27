###############################
# His solution

from pprint import pprint
sentence = "This is a common interview question"

char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)

print(char_frequency[0])


################################
# My solution


sentence = "This is a common interview question"
sentence = sentence.replace(" ", "")

chars = [*sentence]

dicto = {}
for char in chars:
    if char in dicto:
        dicto[char] += 1
    else:
        dicto[char] = 1

x = 0
newKey = ""
for key, value in dicto.items():
    if value > x:
        newKey = key
        x = value
print(newKey, x)
