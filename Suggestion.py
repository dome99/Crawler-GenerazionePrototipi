import json
import os


def writeWordInf(file, word, value):
    spaces = 35 - len(word) + 1
    stri = word + ":"
    for idx in range(spaces):
        stri = stri + " "

    stri = stri + str(value)
    file.write(stri + "\n")


genres = {}
with open('data.txt') as json_file:
    data = json.load(json_file)

    for s in data['songs']:
        for i in range(len(s['attributes'])):
            attribute = s['attributes'][i].split(" (")[0]

            if attribute not in genres:
                genres[attribute] = 0
            genres[attribute] += 1


f = open("./attributes.txt", "w+")

for key in sorted(genres):
    if genres[key] > 60:
        writeWordInf(f, key, genres[key])

f.close()
