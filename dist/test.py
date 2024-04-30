s = "example is  good"

word_list = s.split(" ")

for word in word_list:
    if word.isspace():
        print(word)
    else:
        print("ff")